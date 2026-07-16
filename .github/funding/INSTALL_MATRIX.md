# Cross-platform install matrix

**Coastal Alpine Tech Limited** (pre-seed)  
**Last verified (Windows smoke):** 2026-07-13  

## Prerequisites

| Tool | Windows | Linux (Debian/Ubuntu/RPi OS) |
| :--- | :--- | :--- |
| Python | 3.10+ (3.11–3.12 recommended) from [python.org](https://www.python.org) **Add to PATH** | `sudo apt-get install -y python3 python3-venv python3-pip python3-dev build-essential` |
| Git | [Git for Windows](https://git-scm.com) | `sudo apt-get install -y git` |
| Ollama (optional) | [Windows installer](https://ollama.com/download/windows) | [install script](https://ollama.com) |
| Node 22+ (Front_Line_Whanau only) | [nodejs.org](https://nodejs.org) | nvm / nodesource / distro packages |

## Install commands

### Foundation (Python)

| Repo | Linux / macOS | Windows (PowerShell) | Status |
| :--- | :--- | :--- | :--- |
| **Coastal-Alpine-Core** | `curl -fsSL https://raw.githubusercontent.com/fivepanelhat/Coastal-Alpine-Core/main/install.sh \| bash` | `irm https://raw.githubusercontent.com/fivepanelhat/Coastal-Alpine-Core/main/install.ps1 \| iex` | ✅ Win smoke 2026-07-13 |
| **Weaver** | `curl -fsSL …/Weaver/main/install.sh \| bash` | `irm …/Weaver/main/install.ps1 \| iex` | ✅ Win bootstrap |
| **Aether** | `curl -fsSL …/Aether/main/install.sh \| bash` | `irm …/Aether/main/install.ps1 \| iex` | ✅ Win smoke |
| **coastal-alpine-stack** | `curl -fsSL …/coastal-alpine-stack/main/install.sh \| bash` | `irm …/install.ps1 \| iex` | Scripts hardened |

From a clone: run `./install.sh` or `.\install.ps1` in the repo root (uses checkout, not re-clone).

### Domain portals

| Repo | Linux | Windows | Notes |
| :--- | :--- | :--- | :--- |
| Byte-Size-Kai | `./install.sh` or `python bootstrap.py` | `.\install.ps1` | Core pin `@v0.5.4` |
| SoilGuard-Portal | same | same | `pyaudio` optional only |
| AquaGuard-Portal | same | same | `pyaudio` optional only |
| Sting-Operation-AI | same | same | Needs torch wheels; prefer Python **3.11–3.12** |

### Other

| Repo | Install |
| :--- | :--- |
| **Front_Line_Whanau** | `./install.sh` / `.\install.ps1` → `npm install` (Node 22+) |
| **Sovereign-Edge-Firmware** | Arduino / `arduino-cli` — see [install.md](https://github.com/fivepanelhat/Sovereign-Edge-Firmware/blob/master/install.md) |
| **fivepanelhat** (org profile) | Docs only — no runtime install |

## Hardening applied (2026-07-13)

1. PowerShell installers **fail on non-zero** `$LASTEXITCODE` (no silent pip failures).
2. Python **≥3.10** gate on all scripts.
3. Portal `bootstrap.py` uses **Coastal-Alpine-Core@v0.5.4** (correct casing + pin).
4. Critical steps exit non-zero; optional deps (`requirements-optional.txt`) may fail without aborting.
5. `pyaudio` moved off the default portal path (needs PortAudio system packages).
6. Post-install **import verify** for `coastal_alpine_core` where applicable.

## Optional audio (SoilGuard / AquaGuard)

```bash
# Debian/Ubuntu/RPi
sudo apt-get install -y portaudio19-dev python3-dev
source venv/bin/activate
pip install -r requirements-optional.txt
```

```powershell
# Windows: install PortAudio + VS Build Tools, then:
.\venv\Scripts\Activate.ps1
pip install -r requirements-optional.txt
```

## Known platform caveats

| Issue | Mitigation |
| :--- | :--- |
| Python 3.14 + some torch/opencv builds | Prefer 3.11 or 3.12 for Sting / heavy CV |
| Disk full mid-pip | Free space; installers now exit non-zero on failure |
| Ollama models not pulled | Installers warn only — pull models separately |
| Firmware | Not a Python install |

## Smoke checklist (maintainers)

```powershell
# Windows
cd Coastal-Alpine-Core; .\install.ps1
cd ..\Aether; .\install.ps1
cd ..\Weaver; python bootstrap.py
cd ..\SoilGuard-Portal; python bootstrap.py --portal-only
```

```bash
# Linux
cd Coastal-Alpine-Core && ./install.sh
cd ../Aether && ./install.sh
cd ../Weaver && python3 bootstrap.py
cd ../SoilGuard-Portal && python3 bootstrap.py --portal-only
```
