# Coastal Alpine Tech Limited: Kiwi Edge AI Stack

![Coastal Alpine Tech Banner](assets/social_preview.png)

Welcome to the official repository landing page for **Coastal Alpine Tech Limited**, headquartered in New Plymouth, Taranaki, New Zealand. We design and deploy offline-native, data-sovereign edge intelligence systems for remote, high-stakes industrial, agricultural, and biosecurity settings across Aotearoa.

Our stack is **hybridised** across **Coastal-Alpine-Core**, **Weaver**, **Aether**, and **coastal-alpine-stack**: develop on **Windows or Linux**, deploy production on the **canonical edge node** — **Raspberry Pi 5 (16GB)** with **Hailo-10H NPU** (40 TOPS AI Accelerator / AI HAT+ 2) — to maintain customary data rights (Te Mana Raraunga / Māori Data Sovereignty) and guarantee operational uptime in rural catchments facing cloud blackouts.

---

## Compliance at a glance

A compact view of the governance work now living in this org profile (full framework under [`.github/compliance/`](.github/compliance/nz-ai-compliance-soc2/)):

| Pillar | Focus |
| :--- | :--- |
| **Privacy Act 2020** | IPP 1–11 mapping, DSAR pathways, retention |
| **Te Mana Raraunga** | Māori data sovereignty + OCAP®-aligned control |
| **SOC 2 Type II** | CC / A / S / P controls, 225-item matrix |
| **MBIE Responsible AI** | Safety-by-design, explainability, HITL gates |
| **NZ Algorithm Charter** | Transparent decisions, human appeal |

**Status:** Framework files deployed · implementation roadmap Q3 2026 → external SOC 2 target Q4 2026–Q1 2027  
**Local docs:** [SKILL.md](.github/compliance/nz-ai-compliance-soc2/SKILL.md) · [Implementation guide](.github/compliance/nz-ai-compliance-soc2/README.md) · [Audit checklist](.github/compliance/nz-ai-compliance-soc2/references/COMPLIANCE_AUDIT_CHECKLIST.md)

---

## Canonical hardware target

| Component | Specification |
| :--- | :--- |
| Compute | **Raspberry Pi 5 — 16GB RAM** |
| NPU | **Hailo-10H** (40 TOPS) via Raspberry Pi **AI Accelerator / AI HAT+ 2** |
| OS (edge) | Raspberry Pi OS (64-bit) |
| Dev hosts | **Windows 10/11** · **Linux** (Ubuntu/Debian/RPi OS) · macOS optional |
| Local LLM | Ollama + Gemma 4 (`gemma4:e4b`) on-device |

All Coastal Alpine edge repositories document this same target. Do not mix Hailo-8 / Hailo-10L / 8GB SKUs in product docs.

---

## The Kiwi Edge AI Stack Portfolio

| Repository | Role | Platforms | Core NZ Regulations | Primary hardware |
| :--- | :--- | :--- | :--- | :--- |
| [Coastal-Alpine-Core](https://github.com/fivepanelhat/Coastal-Alpine-Core) | Shared SDK (guards, telemetry, Ollama, portal_core, flywheel) | **Windows · Linux · RPi** | Te Mana Raraunga 2018 | RPi 5 16GB + Hailo-10H |
| [Weaver](https://github.com/fivepanelhat/Weaver) | Multi-tenant helpdesk & local RAG mesh | **Windows · Linux · RPi** | Privacy Act 2020, Public Records Act 2005 | RPi 5 16GB + Hailo-10H |
| [Aether](https://github.com/fivepanelhat/Aether) | Sovereign agentic companion + computer use | **Windows · Linux · macOS** | Te Mana Raraunga 2018 | Dev workstation / edge companion |
| [coastal-alpine-stack](https://github.com/fivepanelhat/coastal-alpine-stack) | Full stack compose / K3s monorepo | **Windows · Linux · RPi** | Te Mana Raraunga 2018 | RPi 5 16GB + Hailo-10H |
| [Blue-Moon-Portal](https://github.com/fivepanelhat/Blue-Moon-Portal) | Multi-modal edge AI for microgreen cultivation | Edge Linux | Biosecurity Act 1993, HSNO Act 1996, Food Act 2014 | RPi 5 16GB + Hailo-10H |
| [Sting-Operation-AI](https://github.com/fivepanelhat/Sting-Operation-AI) | YOLO wasp & bee classifier beehive sentinel | Edge Linux + Hailo | Biosecurity Act 1993, Animal Welfare Act 1999 | RPi 5 16GB + Hailo-10H |
| [AquaGuard-Portal](https://github.com/fivepanelhat/AquaGuard-Portal) | Water runoff, sediment, & turbidity telemetry | Edge Linux | RMA 1991, Horizons One Plan, regional consents | RPi 5 16GB + Hailo-10H |
| [SoilGuard-Portal](https://github.com/fivepanelhat/SoilGuard-Portal) | Soil N-P-K, pH, & moisture crop control | Edge Linux | NES-F 2020 (Synthetic N cap), FWFPs | RPi 5 16GB + Hailo-10H |
| [Sovereign-Edge-Firmware](https://github.com/fivepanelhat/Sovereign-Edge-Firmware) | ESP32 sensor firmware + edge hub | Field + Pi hub | Te Mana Raraunga 2018 | RPi 5 16GB hub + ESP32 nodes |

### Foundation roles (CAT tiers)

| Repo | Layer | CAT emphasis |
| :--- | :--- | :--- |
| **Weaver** | Orchestration + multi-tenant RAG | Diamond primary · HITL, tenant isolation |
| **Aether** | Agentic companion + computer use | Platinum primary · explainability, fairness |
| **Coastal-Alpine-Core** | Edge SDK + security primitives | Diamond primary · encryption, device posture |
| **coastal-alpine-stack** | Deploy / remediate / compose | Diamond primary · fail-closed auth, signatures |

---

## Stack Architecture Overview

End-to-end data path on a **sovereign edge node**, hybridised with the **Aether** companion. Sensors and actuators stay on-farm; inference and orchestration never leave the property. **Develop on Windows or Linux; deploy on RPi 5.**

![Kiwi Edge AI Stack — ultra liquid glass architecture](assets/architecture_overview.png)

### System layers (readable map)

```mermaid
%%{init: {
  "theme": "dark",
  "themeVariables": {
    "fontSize": "15px",
    "fontFamily": "Inter, ui-sans-serif, system-ui, sans-serif",
    "primaryColor": "#0ea5e9",
    "primaryTextColor": "#f8fafc",
    "primaryBorderColor": "#38bdf8",
    "lineColor": "#67e8f9",
    "secondaryColor": "#1e293b",
    "tertiaryColor": "#0f172a",
    "clusterBkg": "#0b1220cc",
    "clusterBorder": "#38bdf880",
    "titleColor": "#e2e8f0"
  },
  "flowchart": {
    "nodeSpacing": 36,
    "rankSpacing": 44,
    "padding": 18,
    "htmlLabels": true,
    "curve": "basis",
    "useMaxWidth": true
  }
}}%%
flowchart TB
    classDef hw fill:#0c4a6e,stroke:#38bdf8,stroke-width:2px,color:#f0f9ff
    classDef core fill:#134e4a,stroke:#2dd4bf,stroke-width:2px,color:#f0fdfa
    classDef app fill:#1e1b4b,stroke:#a5b4fc,stroke-width:2px,color:#eef2ff
    classDef ai fill:#3b0764,stroke:#e879f9,stroke-width:2px,color:#fdf4ff
    classDef fw fill:#422006,stroke:#fbbf24,stroke-width:2px,color:#fffbeb
    classDef sense fill:#052e16,stroke:#4ade80,stroke-width:2px,color:#f0fdf4
    classDef companion fill:#4c1d95,stroke:#c4b5fd,stroke-width:2px,color:#f5f3ff
    classDef host fill:#052e16,stroke:#86efac,stroke-width:2px,color:#f0fdf4

    subgraph FIELD["① Field & marine sensors"]
        direction LR
        S1["Water probes<br/>pH · DO · turbidity"]
        S2["Soil probes<br/>N-P-K · moisture"]
        S3["Vision / audio<br/>CSI · mics"]
        S4["Hive cameras<br/>YOLO streams"]
    end

    subgraph FIRMWARE["② Edge nodes — Sovereign-Edge-Firmware"]
        direction LR
        ESP["ESP32 nodes<br/>mTLS MQTT"]
        HUB["Pi hub services<br/>Mosquitto · Node-RED"]
    end

    subgraph RUNTIME["③ Hybrid runtime — Core · Weaver · stack · RPi 5 16GB + Hailo-10H"]
        direction TB
        K3s["K3s / compose<br/>coastal-alpine-stack"]
        Core["Coastal-Alpine-Core<br/>SecurityGuard · Telemetry · Flywheel · portal_core"]
        Weaver["Weaver<br/>LangGraph multi-tenant RAG"]
        Ollama["Ollama<br/>Gemma 4 e4b local LLM"]
        Hailo["Hailo-10H NPU<br/>40 TOPS vision accel"]
    end

    subgraph PORTALS["④ Domain portals — offline agents"]
        direction LR
        Blue["Blue-Moon"]
        Sting["Sting-Operation"]
        Aqua["AquaGuard"]
        Soil["SoilGuard"]
    end

    subgraph ORCH["⑤ Aether companion — hybrid edge AI + computer use"]
        Aether["Aether<br/>ReAct · skills · HITL · desktop control"]
    end

    subgraph HOSTS["⑥ Hosts — dual platform"]
        direction LR
        Win["Windows 10/11<br/>install.ps1"]
        Lin["Linux workstation<br/>install.sh"]
        RPi["RPi 5 16GB + Hailo-10H<br/>production edge"]
    end

    S1 & S2 & S3 & S4 --> ESP
    ESP --> HUB
    HUB --> K3s
    K3s --> Core
    Core --> Weaver
    Weaver --> Blue & Sting & Aqua & Soil
    Core --> Ollama
    S3 & S4 --> Hailo
    Aether -.->|skills · CI · HITL · computer use| Core & Weaver
    RUNTIME -.-> HOSTS
    ORCH -.-> Win & Lin

    class S1,S2,S3,S4 sense
    class ESP,HUB fw
    class K3s,Ollama,Hailo hw
    class Core core
    class Weaver,Blue,Sting,Aqua,Soil app
    class Aether companion
    class Win,Lin,RPi host
```

| Layer | What runs | Why it matters |
| :--- | :--- | :--- |
| **① Sensors** | Probes, cameras, audio | Capture stays local to whenua / farm |
| **② Firmware** | ESP32 + mTLS MQTT | Hardened field devices, no cloud telemetry bus |
| **③ Hybrid runtime** | Core + Weaver + stack + Ollama + Hailo | Shared SDK, multi-tenant routing, offline inference |
| **④ Portals** | Domain agents | Agritech, biosecurity, water, soil |
| **⑤ Aether** | Companion + computer use | HITL, skills, remediation, desktop control (Win/Linux) |
| **⑥ Hosts** | Windows · Linux · RPi 5 | Same hybrid packages; dual-platform installers |

---

## Install — Windows + Linux

The hybrid foundation repos ship **one-line installers** for both platforms. Production edge remains **RPi 5 (Linux)**; Windows and Linux workstations are first-class for development.

### Prerequisites

| | 🐧 Linux (Ubuntu / Debian / RPi OS) | 🪟 Windows 10/11 |
| :--- | :--- | :--- |
| **Python** | 3.10+ (`python3`, `python3-venv`, `python3-pip`) | 3.10+ from [python.org](https://www.python.org/downloads/) — **Add to PATH** |
| **Git** | `sudo apt-get install -y git` | [Git for Windows](https://git-scm.com/) |
| **Build tools** | `sudo apt-get install -y build-essential python3-dev` | Usually not required for pure Python |
| **Ollama** | [ollama.com](https://ollama.com) install script | [Windows installer](https://ollama.com/download/windows) |
| **PowerShell** | — | 5.1+ or 7+; if scripts blocked: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` |
| **Docker** (optional) | `docker.io` / compose for stack services | [Docker Desktop](https://www.docker.com/products/docker-desktop/) |

```bash
# Linux system packages (Debian/Ubuntu/RPi OS)
sudo apt-get update
sudo apt-get install -y python3 python3-dev python3-venv python3-pip git build-essential
```

### One-line installers

#### Coastal-Alpine-Core (shared SDK)

<details open>
<summary><strong>🐧 Linux / macOS</strong></summary>

```bash
curl -fsSL https://raw.githubusercontent.com/fivepanelhat/Coastal-Alpine-Core/main/install.sh | bash
```

</details>

<details>
<summary><strong>🪟 Windows (PowerShell)</strong></summary>

```powershell
irm https://raw.githubusercontent.com/fivepanelhat/Coastal-Alpine-Core/main/install.ps1 | iex
```

</details>

#### Weaver (multi-tenant orchestration)

<details open>
<summary><strong>🐧 Linux / macOS</strong></summary>

```bash
curl -fsSL https://raw.githubusercontent.com/fivepanelhat/Weaver/main/install.sh | bash
# or from a clone: python3 bootstrap.py
```

</details>

<details>
<summary><strong>🪟 Windows (PowerShell)</strong></summary>

```powershell
irm https://raw.githubusercontent.com/fivepanelhat/Weaver/main/install.ps1 | iex
# or from a clone: python bootstrap.py
```

</details>

#### Aether (agentic companion + computer use)

<details open>
<summary><strong>🐧 Linux / macOS</strong></summary>

```bash
curl -fsSL https://raw.githubusercontent.com/fivepanelhat/Aether/main/install.sh | bash
aether doctor
```

</details>

<details>
<summary><strong>🪟 Windows (PowerShell)</strong></summary>

```powershell
irm https://raw.githubusercontent.com/fivepanelhat/Aether/main/install.ps1 | iex
aether doctor
```

</details>

#### coastal-alpine-stack (full monorepo)

<details open>
<summary><strong>🐧 Linux / macOS</strong></summary>

```bash
curl -fsSL https://raw.githubusercontent.com/fivepanelhat/coastal-alpine-stack/main/install.sh | bash
```

</details>

<details>
<summary><strong>🪟 Windows (PowerShell)</strong></summary>

```powershell
irm https://raw.githubusercontent.com/fivepanelhat/coastal-alpine-stack/main/install.ps1 | iex
```

</details>

### Local models

```bash
ollama pull gemma4:e4b          # Weaver / portals / edge
ollama pull qwen2.5-coder:7b    # Aether text
ollama pull qwen2.5-vl:7b       # Aether computer-use vision
```

### Quick reference

| Repo | Linux | Windows | Docs |
| :--- | :--- | :--- | :--- |
| **Core** | `install.sh` | `install.ps1` | [README](https://github.com/fivepanelhat/Coastal-Alpine-Core#installation) · [DEVELOPER_SETUP](https://github.com/fivepanelhat/Coastal-Alpine-Core/blob/main/DEVELOPER_SETUP.md) |
| **Weaver** | `install.sh` · `bootstrap.py` | `install.ps1` · `bootstrap.py` | [setup.md](https://github.com/fivepanelhat/Weaver/blob/main/setup.md) · [installation.md](https://github.com/fivepanelhat/Weaver/blob/main/installation.md) |
| **Aether** | `install.sh` | `install.ps1` | [README](https://github.com/fivepanelhat/Aether#download--install-terminal-cross-platform) · [GETTING_STARTED](https://github.com/fivepanelhat/Aether/blob/main/docs/GETTING_STARTED.md) |
| **Stack** | `install.sh` | `install.ps1` | [README](https://github.com/fivepanelhat/coastal-alpine-stack#getting-started-windows--linux) · [ARCHITECTURE](https://github.com/fivepanelhat/coastal-alpine-stack/blob/main/ARCHITECTURE.md) |

---

## Core Operating Philosophies

1. **Sovereign by Design**: Data generated on NZ *whenua* is processed and stored locally, fully conforming to Te Mana Raraunga principles. We avoid commercial third-party cloud data leakage.
2. **Rural Resilience**: Our systems are engineered to withstand rural connectivity blackouts, executing local multi-modal vision and audio inference without any internet connection.
3. **Regulatory Safety**: Systems actively control actuators (like locking out fertigation lines or disabling class 3B lasers) to automatically prevent regulatory breaches of Regional Council rules.
4. **Cross-platform hybrid**: Foundation packages run on **Windows and Linux** for development; production edge stays on RPi 5 + Hailo-10H.
5. **HITL by default**: High-risk agent actions and capital/compliance decisions require human approval — no silent autonomous implementation of governance changes.

Developed with pride in **Taranaki, New Zealand**.

---

## Governance & capital (summary)

Condensed from the compliance and Kotahitanga work added to this profile — product landing above remains primary.

### CAT Architectural Standards

- **Diamond (primary):** enterprise-grade compliance, security, observability  
- **Platinum (secondary):** AI continuous improvement + data flywheel  
- **Gold (tertiary):** workflow-native design with transparent HITL gates  

### Kotahitanga investment principles

**Kotahitanga** (collective unity) guides capital allocation for sovereign AI and indigenous data infrastructure:

| Guardrail | Rule of thumb |
| :--- | :--- |
| **OCAP® alignment** | Ownership, Control, Access, Possession — data stays in Aotearoa |
| **Compliance baseline** | Diamond ≥95% · Platinum ≥85% · Gold ≥80% on the 225-point matrix |
| **Remediation** | 🟢 ≥90% full release · 🟡 70–89% escrow · 🔴 &lt;70% freeze |
| **HITL capital gates** | Large allocations and Māori-data decisions need human / Cultural Advisory Board sign-off |

Full reference set on this repo:

| Doc | Path |
| :--- | :--- |
| Master skill | [`.github/compliance/nz-ai-compliance-soc2/SKILL.md`](.github/compliance/nz-ai-compliance-soc2/SKILL.md) |
| Privacy Act mapping | [references/NZ_PRIVACY_ACT_2020_MAPPING.md](.github/compliance/nz-ai-compliance-soc2/references/NZ_PRIVACY_ACT_2020_MAPPING.md) |
| SOC 2 matrix | [references/SOC2_CONTROL_MATRIX.md](.github/compliance/nz-ai-compliance-soc2/references/SOC2_CONTROL_MATRIX.md) |
| Te Mana Raraunga | [references/TE_MANA_RARAUNGA_PRINCIPLES.md](.github/compliance/nz-ai-compliance-soc2/references/TE_MANA_RARAUNGA_PRINCIPLES.md) |
| Incident playbook | [references/INCIDENT_RESPONSE_PLAYBOOK.md](.github/compliance/nz-ai-compliance-soc2/references/INCIDENT_RESPONSE_PLAYBOOK.md) |
| Audit checklist | [references/COMPLIANCE_AUDIT_CHECKLIST.md](.github/compliance/nz-ai-compliance-soc2/references/COMPLIANCE_AUDIT_CHECKLIST.md) |

### Key metrics (targets)

| Metric | Target |
| :--- | :--- |
| Availability SLO | 99.5% monthly |
| Audit log retention | 18 months (immutable) |
| DSAR response | 20 working days |
| Breach notification | 72 hours (Privacy Commissioner) |
| Backup RTO / RPO | ≤4 h / ≤1 h |
| Incident P0 response | 15 minutes |

---

## Recent stack updates

### 2026-07-12 — front page hybrid + compliance blend

| Area | What shipped |
| :--- | :--- |
| **Landing page** | Restored product portfolio, architecture, dual-platform install from pre-rewrite front page |
| **Compliance mix** | Kept NZ AI / SOC 2 / Kotahitanga highlights with **local** doc links (no broken branch paths) |
| **Visuals** | Ultra liquid glass morphism hero + architecture overview refresh |

### 2026-07-12 — hybridise + dual-platform install

| Area | What shipped |
| :--- | :--- |
| **Hybrid foundation** | Core · Weaver · Aether · stack diagrams and docs aligned |
| **Installers** | `install.sh` + `install.ps1` on Core, Weaver, Aether, coastal-alpine-stack |
| **Core pin** | Consumers document **@v0.5.4** tagged releases |

### 2026-07-11 — harden, document, productise

| Area | What shipped |
| :--- | :--- |
| **Coastal-Alpine-Core** | **v0.5.3** edge SDK optimisations; **v0.5.4** expanded SecurityGuard patterns |
| **Security (org-wide)** | Least-privilege Actions, Dependabot, SECURITY sections |
| **Aether** | Kiwi Edge skills, computer-use hybrid, dual installers |

**Next focus (suggested):** keep submodules on Core ≥0.5.4; smoke-test installers on clean Windows and Linux hosts; advance Week 1–12 compliance implementation against the local checklist.

---

## Project badges

Status badges for this repository (CI, security, license, and stack metadata):

[![License](https://img.shields.io/badge/License-Proprietary--Commercial-blue?style=flat-square)](LICENSE)  
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square)](https://www.python.org/)  
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20RPi-0078D6?style=flat-square)]()  
[![Hybrid](https://img.shields.io/badge/Hybrid-Core%20%7C%20Weaver%20%7C%20Aether%20%7C%20Stack-8B5CF6?style=flat-square)]()  
[![Install](https://img.shields.io/badge/Install-install.sh%20%7C%20install.ps1-0ea5e9?style=flat-square)]()  
[![Hardware Target](https://img.shields.io/badge/Hardware-Raspberry%20Pi%205%2016GB-C11A5B?style=flat-square&logo=raspberry-pi&logoColor=white)]()  
[![NPU Acceleration](https://img.shields.io/badge/NPU-Hailo--10H%20Accelerated-005A9C?style=flat-square)]()  
[![Sovereignty](https://img.shields.io/badge/Sovereignty-NZ%20Data%20Bound-00247D?style=flat-square)]()  
[![Compliance](https://img.shields.io/badge/Compliance-Privacy%20Act%20%7C%20SOC%202%20%7C%20TMR-0f766e?style=flat-square)](.github/compliance/nz-ai-compliance-soc2/)  
[![CI](https://github.com/fivepanelhat/fivepanelhat/actions/workflows/ci-scan.yml/badge.svg?branch=main)](https://github.com/fivepanelhat/fivepanelhat/actions/workflows/ci-scan.yml)  
[![SecOps](https://img.shields.io/github/actions/workflow/status/fivepanelhat/fivepanelhat/secops.yml?branch=main&label=SecOps&style=flat-square&color=success)](https://github.com/fivepanelhat/fivepanelhat/actions/workflows/secops.yml)  
[![RedTeam](https://img.shields.io/github/actions/workflow/status/fivepanelhat/fivepanelhat/redteam.yml?branch=main&label=RedTeam&style=flat-square&color=critical)](https://github.com/fivepanelhat/fivepanelhat/actions/workflows/redteam.yml)  
[![Dependabot](https://img.shields.io/badge/Dependencies-Monitored-brightgreen?style=flat-square&logo=dependabot)]()  
[![Sustainability](https://img.shields.io/badge/EECA%20NZ-Carbon%20Tracked-green?style=flat-square)]()

---

*Coastal Alpine Tech — Sovereign Edge AI for Aotearoa New Zealand 🇳🇿*
