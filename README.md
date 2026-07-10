# Coastal Alpine Tech Limited: Kiwi Edge AI Stack

![Coastal Alpine Tech Banner](assets/social_preview.png)


Welcome to the official repository landing page for **Coastal Alpine Tech Limited**, headquartered in New Plymouth, Taranaki, New Zealand. We design and deploy offline-native, data-sovereign edge intelligence systems for remote, high-stakes industrial, agricultural, and biosecurity settings across New Zealand.

Our stack operates entirely on-premise on the **canonical edge node** — **Raspberry Pi 5 (16GB)** with **Hailo-10H NPU** (40 TOPS AI Accelerator / AI HAT+ 2) — to maintain customary data rights (Te Mana Raraunga / Maori Data Sovereignty) and guarantee 100% operational uptime in rural catchments facing cloud blackouts.

---

## Canonical hardware target

| Component | Specification |
| :--- | :--- |
| Compute | **Raspberry Pi 5 — 16GB RAM** |
| NPU | **Hailo-10H** (40 TOPS) via Raspberry Pi **AI Accelerator / AI HAT+ 2** |
| OS | Raspberry Pi OS (64-bit) |
| Local LLM | Ollama + Gemma 4 (`gemma4:e4b`) on-device |

All Coastal Alpine edge repositories document this same target. Do not mix Hailo-8 / Hailo-10L / 8GB SKUs in product docs.

---

## The Kiwi Edge AI Stack Portfolio

| Repository | Role | Core NZ Regulations | Primary Hardware Target |
| :--- | :--- | :--- | :--- |
| [Weaver](https://github.com/fivepanelhat/Weaver) | Multi-tenant helpdesk & local RAG mesh | Privacy Act 2020, Public Records Act 2005 | RPi 5 16GB + Hailo-10H |
| [Blue-Moon-Portal](https://github.com/fivepanelhat/Blue-Moon-Portal) | Multi-modal edge AI for microgreen cultivation (Byte Size Kai) | Biosecurity Act 1993, HSNO Act 1996, Food Act 2014 | RPi 5 16GB + Hailo-10H |
| [Sting-Operation-AI](https://github.com/fivepanelhat/Sting-Operation-AI) | YOLO wasp & bee classifier beehive sentinel | Biosecurity Act 1993, Animal Welfare Act 1999 | RPi 5 16GB + Hailo-10H |
| [AquaGuard-Portal](https://github.com/fivepanelhat/AquaGuard-Portal) | Water runoff, sediment, & turbidity telemetry | RMA 1991, Horizons One Plan, regional consents | RPi 5 16GB + Hailo-10H |
| [SoilGuard-Portal](https://github.com/fivepanelhat/SoilGuard-Portal) | Soil N-P-K, pH, & moisture crop control | NES-F 2020 (Synthetic N cap), FWFPs | RPi 5 16GB + Hailo-10H |
| [Coastal-Alpine-Core](https://github.com/fivepanelhat/Coastal-Alpine-Core) | Shared SDK (offline LLM wrapper, safety, telemetry) | — | RPi 5 16GB + Hailo-10H |
| [coastal-alpine-stack](https://github.com/fivepanelhat/coastal-alpine-stack) | Full stack compose / K3s edge runtime | — | RPi 5 16GB + Hailo-10H |
| [Sovereign-Edge-Firmware](https://github.com/fivepanelhat/Sovereign-Edge-Firmware) | ESP32 sensor firmware + edge hub | — | RPi 5 16GB hub + ESP32 nodes |
| [Aether](https://github.com/fivepanelhat/Aether) | Sovereign agentic development orchestrator | — | Dev workstation / edge companion |

---

## Stack Architecture Overview

End-to-end data path on a **single sovereign edge node** (Raspberry Pi 5 16GB + Hailo-10H). Sensors and actuators stay on-farm; inference and orchestration never leave the property.

![Kiwi Edge AI Stack — liquid glass architecture](assets/architecture_overview.png)

### System layers (readable map)

```mermaid
%%{init: {
  "theme": "dark",
  "themeVariables": {
    "fontSize": "18px",
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
    "nodeSpacing": 48,
    "rankSpacing": 56,
    "padding": 24,
    "htmlLabels": true,
    "curve": "basis"
  }
}}%%
flowchart TB
    classDef hw fill:#0c4a6e,stroke:#38bdf8,stroke-width:2px,color:#f0f9ff
    classDef core fill:#134e4a,stroke:#2dd4bf,stroke-width:2px,color:#f0fdfa
    classDef app fill:#1e1b4b,stroke:#a5b4fc,stroke-width:2px,color:#eef2ff
    classDef ai fill:#3b0764,stroke:#e879f9,stroke-width:2px,color:#fdf4ff
    classDef fw fill:#422006,stroke:#fbbf24,stroke-width:2px,color:#fffbeb
    classDef sense fill:#052e16,stroke:#4ade80,stroke-width:2px,color:#f0fdf4

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

    subgraph RUNTIME["③ Edge runtime — RPi 5 16GB + Hailo-10H · coastal-alpine-stack"]
        direction TB
        K3s["K3s / compose<br/>on-device services"]
        Ollama["Ollama<br/>Gemma 4 e4b local LLM"]
        Hailo["Hailo-10H NPU<br/>40 TOPS vision accel"]
    end

    subgraph SDK["④ Shared SDK — Coastal-Alpine-Core"]
        direction LR
        Guard["Input / security guards"]
        Tele["Telemetry · energy"]
        Client["SovereignOllamaClient"]
    end

    subgraph PORTALS["⑤ Domain portals — offline agents"]
        direction LR
        Weaver["Weaver<br/>multi-tenant RAG mesh"]
        Blue["Blue-Moon<br/>microgreens AI"]
        Sting["Sting-Operation<br/>bee / wasp sentinel"]
        Aqua["AquaGuard<br/>water quality"]
        Soil["SoilGuard<br/>soil & fertigation"]
    end

    subgraph ORCH["⑥ Development companion"]
        Aether["Aether<br/>agentic ReAct orchestrator"]
    end

    S1 & S2 & S3 & S4 --> ESP
    ESP --> HUB
    HUB --> K3s
    K3s --> Guard & Tele & Client
    Client --> Ollama
    S3 & S4 --> Hailo
    Guard & Tele & Client --> Weaver & Blue & Sting & Aqua & Soil
    Aether -.->|skills · CI · HITL| Weaver & Blue & Sting & Aqua & Soil

    class S1,S2,S3,S4 sense
    class ESP,HUB fw
    class K3s,Ollama,Hailo hw
    class Guard,Tele,Client core
    class Weaver,Blue,Sting,Aqua,Soil app
    class Aether ai
```

| Layer | What runs | Why it matters |
| :--- | :--- | :--- |
| **① Sensors** | Probes, cameras, audio | Capture stays local to whenua / farm |
| **② Firmware** | ESP32 + mTLS MQTT | Hardened field devices, no cloud telemetry bus |
| **③ Runtime** | Pi 5 16GB, Hailo-10H, Ollama, K3s | Full offline inference + orchestration |
| **④ Core SDK** | Guards, telemetry, LLM client | Shared safety and observability for every portal |
| **⑤ Portals** | Domain agents | Agritech, biosecurity, water, soil, helpdesk |
| **⑥ Aether** | Dev-time agentic tooling | HITL planning, skills, remediation for the stack |

---

## Core Operating Philosophies

1. **Sovereign by Design**: Data generated on NZ *whenua* is processed and stored locally, fully conforming to Te Mana Raraunga principles. We avoid commercial third-party cloud data leakage.
2. **Rural Resilience**: Our systems are engineered to withstand rural connectivity blackouts, executing local multi-modal vision and audio inference without any internet connection.
3. **Regulatory Safety**: Systems actively control actuators (like locking out fertigation lines or disabling class 3B lasers) to automatically prevent regulatory breaches of Regional Council rules.

Developed with pride in **Taranaki, New Zealand**.

---

## Project badges

Status badges for this repository (CI, security, license, and stack metadata):

[![License](https://img.shields.io/badge/License-Proprietary--Commercial-blue?style=flat-square)](LICENSE)  
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square)](https://www.python.org/)  
[![Hardware Target](https://img.shields.io/badge/Hardware-Raspberry%20Pi%205%2016GB-C11A5B?style=flat-square&logo=raspberry-pi&logoColor=white)]()  
[![NPU Acceleration](https://img.shields.io/badge/NPU-Hailo--10H%20Accelerated-005A9C?style=flat-square)]()  
[![Sovereignty](https://img.shields.io/badge/Sovereignty-NZ%20Data%20Bound-00247D?style=flat-square)]()  
[![CI](https://github.com/fivepanelhat/fivepanelhat/actions/workflows/ci-scan.yml/badge.svg?branch=main)](https://github.com/fivepanelhat/fivepanelhat/actions/workflows/ci-scan.yml)  
[![SecOps](https://img.shields.io/github/actions/workflow/status/fivepanelhat/fivepanelhat/secops.yml?branch=main&label=SecOps&style=flat-square&color=success)](https://github.com/fivepanelhat/fivepanelhat/actions/workflows/secops.yml)  
[![RedTeam](https://img.shields.io/github/actions/workflow/status/fivepanelhat/fivepanelhat/redteam.yml?branch=main&label=RedTeam&style=flat-square&color=critical)](https://github.com/fivepanelhat/fivepanelhat/actions/workflows/redteam.yml)  
[![Dependabot](https://img.shields.io/badge/Dependencies-Monitored-brightgreen?style=flat-square&logo=dependabot)]()  
[![Sustainability](https://img.shields.io/badge/EECA%20NZ-Carbon%20Tracked-green?style=flat-square)]()
