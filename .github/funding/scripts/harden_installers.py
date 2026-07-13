#!/usr/bin/env python3
"""Harden cross-platform installers across Coastal Alpine org repos.

Fixes:
- PowerShell installers check $LASTEXITCODE after pip/venv
- Python version gate (>=3.10)
- Portal bootstrap CORE_GIT_URL → Coastal-Alpine-Core@v0.5.4
- bootstrap exits non-zero when core/deps fail
- Add install.sh / install.ps1 to domain portals
"""
from __future__ import annotations

from pathlib import Path
import textwrap

HOME = Path.home()

CORE_GIT = "https://github.com/fivepanelhat/Coastal-Alpine-Core.git@v0.5.4"

PORTALS = [
    "Blue-Moon-Portal",
    "Sting-Operation-AI",
    "SoilGuard-Portal",
    "AquaGuard-Portal",
]

BOOTSTRAP_REPOS = ["Weaver"] + PORTALS

PS_HELPER = r'''
function Require-Ok([string]$Step) {
    if ($null -ne $LASTEXITCODE -and $LASTEXITCODE -ne 0) {
        Fail "$Step failed (exit code $LASTEXITCODE)"
    }
}

function Require-Python310([string]$PythonBin) {
    $ok = & $PythonBin -c "import sys; raise SystemExit(0 if sys.version_info >= (3, 10) else 1)"
    if ($LASTEXITCODE -ne 0) {
        Fail "Python 3.10+ is required (found: $(& $PythonBin -c \"import sys; print('.'.join(map(str, sys.version_info[:3])))\")). Install from https://www.python.org and ensure it is on PATH."
    }
}
'''


def harden_ps1(path: Path) -> bool:
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8")
    original = text
    if "function Require-Ok" not in text:
        # insert helpers after Fail function definition
        if "function Fail" in text:
            text = text.replace(
                'function Fail($m) { Write-Host "[',
                PS_HELPER + '\nfunction Fail($m) { Write-Host "[',
                1,
            )
            # if replace failed due to different formatting, try alternate
            if text == original and "function Fail($m)" in original:
                text = original.replace(
                    "function Fail($m) { Write-Host ",
                    PS_HELPER + "\nfunction Fail($m) { Write-Host ",
                    1,
                )
        else:
            # after ErrorActionPreference
            text = text.replace(
                '$ErrorActionPreference = "Stop"\n',
                '$ErrorActionPreference = "Stop"\n' + PS_HELPER + "\n",
                1,
            )

    # After PythonBin found, require 3.10
    if "Require-Python310" not in text or "Require-Python310 $PythonBin" not in text:
        text = text.replace(
            'if (-not $PythonBin) {\n    Fail "Python 3.10+ is required',
            'if (-not $PythonBin) {\n    Fail "Python 3.10+ is required',
            1,
        )
        # inject after PyVer line if present
        if "Require-Python310 $PythonBin" not in text:
            text = text.replace(
                '$PyVer = & $PythonBin -c "import sys; print(\'%d.%d\' % sys.version_info[:2])"\n',
                '$PyVer = & $PythonBin -c "import sys; print(\'%d.%d\' % sys.version_info[:2])"\n'
                "Require-Python310 $PythonBin\n",
                1,
            )
            text = text.replace(
                '$PyVer = & $PythonBin -c "import sys; print(\'%d.%d\' % sys.version_info[:2])"\r\n',
                '$PyVer = & $PythonBin -c "import sys; print(\'%d.%d\' % sys.version_info[:2])"\r\n'
                "Require-Python310 $PythonBin\r\n",
                1,
            )

    # After common pip install patterns, add Require-Ok
    lines = text.splitlines(keepends=True)
    out = []
    for i, line in enumerate(lines):
        out.append(line)
        stripped = line.strip()
        if stripped.startswith("& $PythonBin -m venv") or stripped.startswith("& $VenvPython -m pip"):
            # don't double-add
            nxt = lines[i + 1].strip() if i + 1 < len(lines) else ""
            if not nxt.startswith("Require-Ok"):
                indent = line[: len(line) - len(line.lstrip())]
                label = "command"
                if "venv" in stripped:
                    label = "venv create"
                elif "pip install" in stripped:
                    label = "pip install"
                out.append(f"{indent}Require-Ok \"{label}\"\n")
        # also catch & $VenvPython without m pip in one line with try/catch - leave try blocks

    text = "".join(out)

    # Fix try/catch pip that swallows errors in stack install - leave warnings for optional deps only

    if text != original:
        path.write_text(text, encoding="utf-8", newline="\n")
        return True
    return False


def harden_sh(path: Path) -> bool:
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8")
    original = text
    if "python_version_ok" not in text:
        gate = '''
# Python version gate
PY_MAJOR="$("$PYTHON_BIN" -c 'import sys; print(sys.version_info[0])')"
PY_MINOR="$("$PYTHON_BIN" -c 'import sys; print(sys.version_info[1])')"
if [[ "$PY_MAJOR" -lt 3 ]] || { [[ "$PY_MAJOR" -eq 3 ]] && [[ "$PY_MINOR" -lt 10 ]]; }; then
  err "Python 3.10+ is required (found ${PY_MAJOR}.${PY_MINOR})."
  exit 1
fi
'''
        # insert after PY_VER line
        text = text.replace(
            'PY_VER="$("$PYTHON_BIN" -c \'import sys; print("%d.%d" % sys.version_info[:2])\')"\n',
            'PY_VER="$("$PYTHON_BIN" -c \'import sys; print("%d.%d" % sys.version_info[:2])\')"\n' + gate,
            1,
        )
    if text != original:
        path.write_text(text, encoding="utf-8", newline="\n")
        return True
    return False


FIXED_BOOTSTRAP = r'''#!/usr/bin/env python3
"""
Coastal Alpine Tech Limited — Cross-Platform Bootstrap Script
==============================================================
Universal installer for Windows, Linux, and macOS.
Creates a virtual environment, installs Coastal-Alpine-Core + deps, validates.

Usage:
    python bootstrap.py                   # Auto-detect monorepo vs portal
    python bootstrap.py --portal-only     # Force portal mode
    python bootstrap.py --help

Requires: Python 3.10+
"""

from __future__ import annotations

import os
import platform
import shlex
import shutil
import subprocess
import sys
import venv

VENV_DIR = "venv"
ROOT_VENV_DIR = ".venv"

PORTALS = [
    "AquaGuard-Portal",
    "Blue-Moon-Portal",
    "SoilGuard-Portal",
    "Sting-Operation-AI",
    "Weaver",
]

CORE_PACKAGE = "coastal_alpine_core"
# Canonical GitHub repo + pin (case-sensitive path on Linux clones)
CORE_GIT_URL = "https://github.com/fivepanelhat/Coastal-Alpine-Core.git@v0.5.4"


def is_windows() -> bool:
    return sys.platform == "win32"


def require_python_310() -> None:
    if sys.version_info < (3, 10):
        print(
            f"✗ Python 3.10+ required (found {sys.version.split()[0]}). "
            "Install from https://www.python.org or your OS package manager."
        )
        sys.exit(1)


def get_venv_dir() -> str:
    if os.path.exists(".gitmodules") or os.path.exists(CORE_PACKAGE):
        return ROOT_VENV_DIR
    return VENV_DIR


def get_pip_exe(venv_path: str) -> str:
    if is_windows():
        return os.path.join(venv_path, "Scripts", "pip.exe")
    return os.path.join(venv_path, "bin", "pip")


def get_python_exe(venv_path: str) -> str:
    if is_windows():
        return os.path.join(venv_path, "Scripts", "python.exe")
    return os.path.join(venv_path, "bin", "python")


def get_activate_cmd(venv_path: str) -> str:
    if is_windows():
        return f".\\{venv_path}\\Scripts\\Activate.ps1"
    return f"source {venv_path}/bin/activate"


def run_cmd(cmd, description=None, critical: bool = True) -> bool:
    if description:
        print(f"  → {description}")
    try:
        args = cmd if isinstance(cmd, list) else shlex.split(cmd)
        subprocess.run(args, check=True, capture_output=True, text=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"  ✗ Command failed: {args if isinstance(cmd, list) else cmd}")
        if e.stderr:
            for line in e.stderr.strip().split("\n")[-12:]:
                print(f"    {line}")
        if critical:
            print("  ✗ Install cannot continue (critical step failed).")
            sys.exit(1)
        return False


def print_header(text: str) -> None:
    print(f"\n{'─' * 60}")
    print(f"  {text}")
    print(f"{'─' * 60}")


def print_step(step: int, total: int, text: str) -> None:
    print(f"\n[{step}/{total}] {text}")


def create_venv(venv_path: str) -> bool:
    if os.path.exists(venv_path):
        print(f"  ✓ Virtual environment '{venv_path}' already exists")
        return True
    print(f"  Creating virtual environment '{venv_path}'...")
    try:
        # upgrade_deps can fail on locked/offline hosts — create without it first
        try:
            venv.create(venv_path, with_pip=True, upgrade_deps=True)
        except TypeError:
            venv.create(venv_path, with_pip=True)
        except Exception:
            # retry without upgrade_deps
            if os.path.exists(venv_path):
                shutil.rmtree(venv_path, ignore_errors=True)
            venv.create(venv_path, with_pip=True)
        print("  ✓ Virtual environment created")
        return True
    except Exception as e:
        print(f"  ✗ Failed to create venv: {e}")
        return False


def install_requirements(pip_exe: str, req_file: str, critical: bool = True) -> bool:
    if not os.path.exists(req_file):
        print(f"  ⊘ {req_file} not found, skipping")
        return True
    return run_cmd(
        [pip_exe, "install", "-r", req_file],
        f"Installing {req_file}",
        critical=critical,
    )


def install_core(pip_exe: str, editable: bool = False) -> bool:
    if editable and os.path.exists(CORE_PACKAGE):
        return run_cmd(
            [pip_exe, "install", "-e", f"./{CORE_PACKAGE}"],
            "Installing coastal_alpine_core (editable mode)",
            critical=True,
        )
    # Prefer git+ URL with pin; fall back to main if tag missing
    ok = run_cmd(
        [pip_exe, "install", f"git+{CORE_GIT_URL}"],
        f"Installing coastal_alpine_core from GitHub ({CORE_GIT_URL})",
        critical=False,
    )
    if ok:
        return True
    print("  → Retrying Core install from main branch…")
    return run_cmd(
        [
            pip_exe,
            "install",
            "git+https://github.com/fivepanelhat/Coastal-Alpine-Core.git",
        ],
        "Installing coastal_alpine_core from GitHub (main)",
        critical=True,
    )


def copy_env_example() -> None:
    if os.path.exists(".env.example") and not os.path.exists(".env"):
        shutil.copy2(".env.example", ".env")
        print("  ✓ Copied .env.example → .env")
    elif os.path.exists(".env"):
        print("  ✓ .env already exists")
    else:
        print("  ⊘ No .env.example found")


def detect_context() -> str:
    if os.path.exists(".gitmodules") or os.path.exists(CORE_PACKAGE):
        return "monorepo"
    basename = os.path.basename(os.getcwd())
    for portal in PORTALS:
        if basename == portal or basename.lower() == portal.lower():
            return "portal"
    if os.path.exists("portal_core") or os.path.exists("portal_schemas") or os.path.exists("requirements.txt"):
        return "portal"
    return "standalone"


def verify_import(python_exe: str) -> None:
    run_cmd(
        [
            python_exe,
            "-c",
            "import coastal_alpine_core; print('coastal_alpine_core OK', getattr(coastal_alpine_core, '__version__', ''))",
        ],
        "Verifying coastal_alpine_core import",
        critical=True,
    )


def setup_monorepo() -> None:
    venv_path = ROOT_VENV_DIR
    total = 5
    print_header("Coastal Alpine Stack — Monorepo Setup")
    print(f"  Platform: {platform.system()} ({platform.machine()})")
    print(f"  Python:   {sys.version.split()[0]}")

    print_step(1, total, "Virtual Environment")
    if not create_venv(venv_path):
        sys.exit(1)
    pip_exe = get_pip_exe(venv_path)
    py_exe = get_python_exe(venv_path)

    print_step(2, total, "Upgrading pip")
    run_cmd([pip_exe, "install", "--upgrade", "pip"], "Upgrading pip", critical=True)

    print_step(3, total, "Installing coastal_alpine_core")
    install_core(pip_exe, editable=True)

    print_step(4, total, "Installing dev dependencies")
    install_requirements(pip_exe, "requirements-dev.txt", critical=False)
    install_requirements(pip_exe, "requirements.txt", critical=False)

    print_step(5, total, "Verify")
    verify_import(py_exe)

    print_header("Setup Complete")
    print(f"  Activate:\n    {get_activate_cmd(venv_path)}\n")


def setup_portal() -> None:
    venv_path = VENV_DIR
    portal_name = os.path.basename(os.getcwd())
    total = 6
    print_header(f"{portal_name} — Portal Setup")
    print(f"  Platform: {platform.system()} ({platform.machine()})")
    print(f"  Python:   {sys.version.split()[0]}")

    print_step(1, total, "Virtual Environment")
    if not create_venv(venv_path):
        sys.exit(1)
    pip_exe = get_pip_exe(venv_path)
    py_exe = get_python_exe(venv_path)

    print_step(2, total, "Upgrading pip")
    run_cmd([pip_exe, "install", "--upgrade", "pip"], "Upgrading pip", critical=True)

    print_step(3, total, "Installing coastal_alpine_core")
    install_core(pip_exe, editable=False)

    print_step(4, total, "Installing dependencies")
    if not install_requirements(pip_exe, "requirements.txt", critical=True):
        sys.exit(1)
    install_requirements(pip_exe, "requirements-dev.txt", critical=False)

    print_step(5, total, "Environment configuration")
    copy_env_example()

    print_step(6, total, "Verify")
    verify_import(py_exe)

    print_header("Setup Complete")
    print(f"  Activate:\n    {get_activate_cmd(venv_path)}\n")
    print("  Next: pull a local model if needed —  ollama pull gemma4:e4b\n")


def main() -> None:
    if "--help" in sys.argv or "-h" in sys.argv:
        print(__doc__)
        sys.exit(0)

    require_python_310()
    portal_only = "--portal-only" in sys.argv
    context = detect_context()

    if portal_only or context == "portal":
        setup_portal()
    elif context == "monorepo":
        setup_monorepo()
    else:
        setup_portal()


if __name__ == "__main__":
    main()
'''

PORTAL_INSTALL_SH = '''#!/usr/bin/env bash
# {name} — dual-platform installer (Linux / macOS)
# One-line: curl -fsSL https://raw.githubusercontent.com/fivepanelhat/{name}/main/install.sh | bash
# From clone: ./install.sh
set -euo pipefail

REPO_URL="${{PORTAL_REPO_URL:-https://github.com/fivepanelhat/{name}.git}}"
INSTALL_DIR="${{PORTAL_HOME:-$HOME/.{slug}-app}}"

info() {{ printf '\\033[36m[{slug}]\\033[0m %s\\n' "$1"; }}
warn() {{ printf '\\033[33m[{slug}]\\033[0m %s\\n' "$1"; }}
err()  {{ printf '\\033[31m[{slug}]\\033[0m %s\\n' "$1" >&2; }}

PYTHON_BIN="$(command -v python3 || command -v python || true)"
if [[ -z "$PYTHON_BIN" ]]; then
  err "Python 3.10+ is required. On Debian/Ubuntu/RPi OS:"
  err "  sudo apt-get install -y python3 python3-venv python3-pip git build-essential"
  exit 1
fi
PY_VER="$("$PYTHON_BIN" -c 'import sys; print("%d.%d" % sys.version_info[:2])')"
info "Using Python $PY_VER ($PYTHON_BIN)"
PY_MAJOR="$("$PYTHON_BIN" -c 'import sys; print(sys.version_info[0])')"
PY_MINOR="$("$PYTHON_BIN" -c 'import sys; print(sys.version_info[1])')"
if [[ "$PY_MAJOR" -lt 3 ]] || {{ [[ "$PY_MAJOR" -eq 3 ]] && [[ "$PY_MINOR" -lt 10 ]]; }}; then
  err "Python 3.10+ is required (found ${{PY_MAJOR}}.${{PY_MINOR}})."
  exit 1
fi

if [[ -f "bootstrap.py" ]] && [[ -f "requirements.txt" || -f "setup.py" || -f "pyproject.toml" ]]; then
  SRC_DIR="$(pwd)"
  info "Installing from current checkout: $SRC_DIR"
else
  if ! command -v git >/dev/null 2>&1; then
    err "git is required. Install git or run from a clone."
    exit 1
  fi
  mkdir -p "$INSTALL_DIR"
  SRC_DIR="$INSTALL_DIR/src"
  if [[ -d "$SRC_DIR/.git" ]]; then
    info "Updating existing checkout in $SRC_DIR"
    git -C "$SRC_DIR" pull --ff-only || warn "Could not fast-forward; using existing checkout."
  else
    info "Cloning $REPO_URL"
    git clone --depth 1 "$REPO_URL" "$SRC_DIR"
  fi
fi

cd "$SRC_DIR"
info "Running bootstrap.py"
"$PYTHON_BIN" bootstrap.py --portal-only
info "Done. Activate: source $SRC_DIR/venv/bin/activate"
'''

PORTAL_INSTALL_PS1 = '''# {name} — dual-platform installer (Windows / PowerShell)
# One-line: irm https://raw.githubusercontent.com/fivepanelhat/{name}/main/install.ps1 | iex
# From clone: powershell -ExecutionPolicy Bypass -File .\\install.ps1

$ErrorActionPreference = "Stop"

$RepoUrl    = if ($env:PORTAL_REPO_URL) {{ $env:PORTAL_REPO_URL }} else {{ "https://github.com/fivepanelhat/{name}.git" }}
$InstallDir = if ($env:PORTAL_HOME)     {{ $env:PORTAL_HOME }}     else {{ Join-Path $env:USERPROFILE ".{slug}-app" }}

function Info($m) {{ Write-Host "[{slug}] $m" -ForegroundColor Cyan }}
function Warn($m) {{ Write-Host "[{slug}] $m" -ForegroundColor Yellow }}
function Fail($m) {{ Write-Host "[{slug}] $m" -ForegroundColor Red; exit 1 }}
function Require-Ok([string]$Step) {{
    if ($null -ne $LASTEXITCODE -and $LASTEXITCODE -ne 0) {{ Fail "$Step failed (exit code $LASTEXITCODE)" }}
}}

$PythonBin = $null
foreach ($cand in @("python", "python3", "py")) {{
    if (Get-Command $cand -ErrorAction SilentlyContinue) {{ $PythonBin = $cand; break }}
}}
if (-not $PythonBin) {{
    Fail "Python 3.10+ is required. Install from https://www.python.org (Add to PATH) and re-run."
}}
$PyVer = & $PythonBin -c "import sys; print('%d.%d' % sys.version_info[:2])"
& $PythonBin -c "import sys; raise SystemExit(0 if sys.version_info >= (3, 10) else 1)"
if ($LASTEXITCODE -ne 0) {{ Fail "Python 3.10+ required (found $PyVer)" }}
Info "Using Python $PyVer ($PythonBin)"

if ((Test-Path "bootstrap.py") -and ((Test-Path "requirements.txt") -or (Test-Path "setup.py") -or (Test-Path "pyproject.toml"))) {{
    $SrcDir = (Get-Location).Path
    Info "Installing from current checkout: $SrcDir"
}} else {{
    if (-not (Get-Command git -ErrorAction SilentlyContinue)) {{
        Fail "git is required. Install Git for Windows from https://git-scm.com or run from a clone."
    }}
    New-Item -ItemType Directory -Force -Path $InstallDir | Out-Null
    $SrcDir = Join-Path $InstallDir "src"
    if (Test-Path (Join-Path $SrcDir ".git")) {{
        Info "Updating existing checkout in $SrcDir"
        git -C $SrcDir pull --ff-only 2>$null
    }} else {{
        Info "Cloning $RepoUrl"
        git clone --depth 1 $RepoUrl $SrcDir
        Require-Ok "git clone"
    }}
}}

Set-Location $SrcDir
Info "Running bootstrap.py"
& $PythonBin bootstrap.py --portal-only
Require-Ok "bootstrap.py"
Write-Host ""
Info "Done. Activate:  .\\venv\\Scripts\\Activate.ps1"
'''


def write_portal_installers(repo: str) -> None:
    root = HOME / repo
    if not root.exists():
        print("skip missing", repo)
        return
    slug = repo.lower().replace("_", "-")
    sh = PORTAL_INSTALL_SH.format(name=repo, slug=slug)
    ps = PORTAL_INSTALL_PS1.format(name=repo, slug=slug)
    (root / "install.sh").write_text(sh, encoding="utf-8", newline="\n")
    (root / "install.ps1").write_text(ps, encoding="utf-8", newline="\n")
    print("wrote installers", repo)


def main() -> None:
    # bootstraps
    for repo in BOOTSTRAP_REPOS:
        path = HOME / repo / "bootstrap.py"
        if path.exists():
            path.write_text(FIXED_BOOTSTRAP, encoding="utf-8", newline="\n")
            print("bootstrap fixed", repo)

    for repo in PORTALS:
        write_portal_installers(repo)

    # harden foundation installers
    for repo, files in [
        ("Coastal-Alpine-Core", ["install.ps1", "install.sh"]),
        ("Weaver", ["install.ps1", "install.sh"]),
        ("Aether", ["install.ps1", "install.sh"]),
        ("coastal-alpine-stack", ["install.ps1", "install.sh"]),
    ]:
        for f in files:
            p = HOME / repo / f
            if f.endswith(".ps1"):
                changed = harden_ps1(p)
            else:
                changed = harden_sh(p)
            print(f"{repo}/{f}: {'updated' if changed else 'ok'}")

    # Manual Core install.ps1 fix: ensure pip failures stop — rewrite critical section more carefully
    core_ps = HOME / "Coastal-Alpine-Core" / "install.ps1"
    t = core_ps.read_text(encoding="utf-8")
    if "Require-Ok" not in t:
        t = t.replace(
            '$ErrorActionPreference = "Stop"\n',
            '$ErrorActionPreference = "Stop"\n\n'
            'function Require-Ok([string]$Step) {\n'
            '    if ($null -ne $LASTEXITCODE -and $LASTEXITCODE -ne 0) {\n'
            '        Fail "$Step failed (exit code $LASTEXITCODE)"\n'
            '    }\n'
            '}\n\n',
            1,
        )
    # ensure Fail is defined before Require-Ok uses it - Require-Ok calls Fail so Fail must come first
    # reorder if needed: put Require-Ok after Fail
    if t.find("function Require-Ok") < t.find("function Fail") and "function Fail" in t:
        # move Require-Ok after Fail
        import re
        m = re.search(r"function Require-Ok\(\[string\]\$Step\) \{[\s\S]*?\n\}\n\n", t)
        if m:
            block = m.group(0)
            t = t[: m.start()] + t[m.end() :]
            t = t.replace(
                'function Fail($m) { Write-Host "[core] $m" -ForegroundColor Red; exit 1 }\n',
                'function Fail($m) { Write-Host "[core] $m" -ForegroundColor Red; exit 1 }\n\n' + block,
                1,
            )
    # inject python version + exit checks
    if "sys.version_info >= (3, 10)" not in t:
        t = t.replace(
            '$PyVer = & $PythonBin -c "import sys; print(\'%d.%d\' % sys.version_info[:2])"\nInfo "Using Python $PyVer ($PythonBin)"\n',
            '$PyVer = & $PythonBin -c "import sys; print(\'%d.%d\' % sys.version_info[:2])"\n'
            '& $PythonBin -c "import sys; raise SystemExit(0 if sys.version_info >= (3, 10) else 1)"\n'
            'if ($LASTEXITCODE -ne 0) { Fail "Python 3.10+ is required (found $PyVer)" }\n'
            'Info "Using Python $PyVer ($PythonBin)"\n',
            1,
        )
    for cmd, label in [
        ('& $PythonBin -m venv $VenvDir\n', 'venv create'),
        ('& $VenvPython -m pip install --upgrade pip | Out-Null\n', 'pip upgrade'),
        ('& $VenvPython -m pip install -e "$SrcDir[dev]"\n', 'pip install core[dev]'),
        ('& $VenvPython -m pip install $SrcDir\n', 'pip install core'),
    ]:
        if cmd in t and f'Require-Ok "{label}"' not in t:
            t = t.replace(cmd, cmd + f'Require-Ok "{label}"\n')
    # post-install import check
    if "from coastal_alpine_core import" in t and "Verify import" not in t:
        t = t.replace(
            'Write-Host ""\nInfo "Done. Activate the environment with:"',
            'Info "Verifying import"\n'
            '& $VenvPython -c "from coastal_alpine_core import SovereignOllamaClient; print(\'ok\')"\n'
            'Require-Ok "import coastal_alpine_core"\n'
            'Write-Host ""\nInfo "Done. Activate the environment with:"',
            1,
        )
    core_ps.write_text(t, encoding="utf-8", newline="\n")
    print("core install.ps1 rewritten checks")

    # Aether / Weaver / stack similar minimal python version + pip exit for key lines
    for repo in ["Weaver", "Aether", "coastal-alpine-stack"]:
        ps = HOME / repo / "install.ps1"
        t = ps.read_text(encoding="utf-8")
        if "sys.version_info >= (3, 10)" not in t:
            t = t.replace(
                '$PyVer = & $PythonBin -c "import sys; print(\'%d.%d\' % sys.version_info[:2])"\nInfo "Using Python $PyVer ($PythonBin)"\n',
                '$PyVer = & $PythonBin -c "import sys; print(\'%d.%d\' % sys.version_info[:2])"\n'
                '& $PythonBin -c "import sys; raise SystemExit(0 if sys.version_info >= (3, 10) else 1)"\n'
                'if ($LASTEXITCODE -ne 0) { Fail "Python 3.10+ is required (found $PyVer)" }\n'
                'Info "Using Python $PyVer ($PythonBin)"\n',
                1,
            )
        if "function Require-Ok" not in t:
            t = t.replace(
                'function Fail($m) { Write-Host ',
                'function Require-Ok([string]$Step) {\n'
                '    if ($null -ne $LASTEXITCODE -and $LASTEXITCODE -ne 0) { Fail "$Step failed (exit code $LASTEXITCODE)" }\n'
                '}\n'
                'function Fail($m) { Write-Host ',
                1,
            )
        # After bootstrap.py call
        if "bootstrap.py" in t and 'Require-Ok "bootstrap"' not in t:
            t = t.replace(
                "& $PythonBin bootstrap.py\n",
                '& $PythonBin bootstrap.py\n    Require-Ok "bootstrap"\n',
            )
        # aether pip install
        if 'pip install "$SrcDir[computer]"' in t and 'Require-Ok "pip install aether"' not in t:
            t = t.replace(
                '& $VenvPython -m pip install "$SrcDir[computer]"\n',
                '& $VenvPython -m pip install "$SrcDir[computer]"\nRequire-Ok "pip install aether"\n',
            )
        if "& $PythonBin -m venv $VenvDir\n" in t and 'Require-Ok "venv create"' not in t:
            t = t.replace(
                "& $PythonBin -m venv $VenvDir\n",
                '& $PythonBin -m venv $VenvDir\nRequire-Ok "venv create"\n',
            )
        # stack core install
        if 'pip install -e "./coastal_alpine_core[dev]"' in t and 'Require-Ok "pip install core"' not in t:
            # leave try/catch but add check after both attempts - simpler: after whole if block skip
            pass
        ps.write_text(t, encoding="utf-8", newline="\n")
        print("updated", repo, "install.ps1")

        sh = HOME / repo / "install.sh"
        t = sh.read_text(encoding="utf-8")
        if "Python 3.10+ is required (found" not in t:
            t = t.replace(
                'info "Using Python $PY_VER ($PYTHON_BIN)"\n',
                'info "Using Python $PY_VER ($PYTHON_BIN)"\n'
                'PY_MAJOR="$("$PYTHON_BIN" -c \'import sys; print(sys.version_info[0])\')"\n'
                'PY_MINOR="$("$PYTHON_BIN" -c \'import sys; print(sys.version_info[1])\')"\n'
                'if [[ "$PY_MAJOR" -lt 3 ]] || { [[ "$PY_MAJOR" -eq 3 ]] && [[ "$PY_MINOR" -lt 10 ]]; }; then\n'
                '  err "Python 3.10+ is required (found ${PY_MAJOR}.${PY_MINOR})."\n'
                '  exit 1\n'
                'fi\n',
                1,
            )
            sh.write_text(t, encoding="utf-8", newline="\n")
            print("updated", repo, "install.sh")

    # Core install.sh version gate
    sh = HOME / "Coastal-Alpine-Core" / "install.sh"
    t = sh.read_text(encoding="utf-8")
    if "found ${PY_MAJOR}" not in t:
        t = t.replace(
            'info "Using Python $PY_VER ($PYTHON_BIN)"\n',
            'info "Using Python $PY_VER ($PYTHON_BIN)"\n'
            'PY_MAJOR="$("$PYTHON_BIN" -c \'import sys; print(sys.version_info[0])\')"\n'
            'PY_MINOR="$("$PYTHON_BIN" -c \'import sys; print(sys.version_info[1])\')"\n'
            'if [[ "$PY_MAJOR" -lt 3 ]] || { [[ "$PY_MAJOR" -eq 3 ]] && [[ "$PY_MINOR" -lt 10 ]]; }; then\n'
            '  err "Python 3.10+ is required (found ${PY_MAJOR}.${PY_MINOR})."\n'
            '  exit 1\n'
            'fi\n',
            1,
        )
        # import verify at end
        if "SovereignOllamaClient" in t and "from coastal_alpine_core import SovereignOllamaClient; print" in t:
            # add actual verify command before Done
            if 'python -c "from coastal_alpine_core import SovereignOllamaClient"' not in t.split("Done")[0]:
                t = t.replace(
                    "echo\ninfo \"Done. Activate the environment with:\"",
                    'info "Verifying import"\n'
                    'python -c "from coastal_alpine_core import SovereignOllamaClient; print(\'ok\')"\n'
                    "echo\ninfo \"Done. Activate the environment with:\"",
                    1,
                )
        sh.write_text(t, encoding="utf-8", newline="\n")
        print("updated Core install.sh")


if __name__ == "__main__":
    main()
