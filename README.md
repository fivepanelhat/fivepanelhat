# Coastal Alpine Tech Limited: Kiwi Edge AI Stack

![CI](https://github.com/fivepanelhat/fivepanelhat/actions/workflows/ci-scan.yml/badge.svg?branch=main)

![Coastal Alpine Tech Banner](assets/social_preview.png)

[![License](https://img.shields.io/badge/License-Proprietary--Commercial-blue?style=flat-square)](LICENSE)  
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)  
[![Hardware Target](https://img.shields.io/badge/Hardware-Raspberry%20Pi%205%2016GB-C11A5B?style=flat-square&logo=raspberry-pi&logoColor=white)]()  
[![NPU Acceleration](https://img.shields.io/badge/NPU-Hailo--10H%20Accelerated-005A9C?style=flat-square)]()  
[![Sovereignty](https://img.shields.io/badge/Sovereignty-NZ%20Data%20Bound-00247D?style=flat-square)]()  
[![SecOps Scan](https://img.shields.io/github/actions/workflow/status/fivepanelhat/fivepanelhat/secops.yml?branch=main&label=SecOps%20Scan&style=flat-square&color=success)](https://github.com/fivepanelhat/fivepanelhat/actions/workflows/secops.yml)  
[![Sustainability](https://img.shields.io/badge/EECA%20NZ-Carbon%20Tracked-green?style=flat-square)]()

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

The following diagram illustrates how the shared core SDK powers data-sovereign telemetry parsing, security screening, and offline reasoning across the different application portals:

```mermaid
flowchart TD
    subgraph "Sovereign Local Hardware — RPi 5 16GB + Hailo-10H"
        Core["Coastal-Alpine-Core SDK<br/>(Safety Guards / Telemetry)"]
        
        subgraph "Application Layer"
            Weaver["Weaver<br/>(LangGraph AI Helpdesk)"]
            BlueMoon["Blue-Moon-Portal<br/>(Microgreen Crop AI)"]
            Sting["Sting-Operation-AI<br/>(Bee Sentinel Box)"]
            Aqua["AquaGuard-Portal<br/>(Runoff Telemetry)"]
            Soil["SoilGuard-Portal<br/>(NPK Soil Monitor)"]
        end
    end
    
    Weaver & BlueMoon & Sting & Aqua & Soil -->|Imports & Telemetry| Core
    Core -->|Local Port Inference| Ollama["Local Ollama<br/>(Gemma 4 Instruct)"]
    Core -->|NPU| Hailo["Hailo-10H NPU<br/>40 TOPS"]
```

---

## Core Operating Philosophies

1. **Sovereign by Design**: Data generated on NZ *whenua* is processed and stored locally, fully conforming to Te Mana Raraunga principles. We avoid commercial third-party cloud data leakage.
2. **Rural Resilience**: Our systems are engineered to withstand rural connectivity blackouts, executing local multi-modal vision and audio inference without any internet connection.
3. **Regulatory Safety**: Systems actively control actuators (like locking out fertigation lines or disabling class 3B lasers) to automatically prevent regulatory breaches of Regional Council rules.

Developed with pride in **Taranaki, New Zealand**.
