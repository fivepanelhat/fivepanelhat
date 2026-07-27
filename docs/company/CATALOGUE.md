# Product & Stack Catalogue — Coastal Alpine Tech

**Purpose:** Single catalogue of what exists in the Kiwi Edge portfolio, by role and maturity.  
**Updated:** 2026-07-27 · **Version:** 0.1.0

Maturity labels are **internal design targets**, not third-party certifications.

---

## How to read this catalogue

| Tag | Meaning |
|-----|---------|
| **P0 beachhead** | Active GTM / pilot narrative |
| **Platform** | Shared foundation other products sit on |
| **Supporting** | Available when a beachhead needs it |
| **Parked** | Maintained lightly; not the sales story |
| **Archived** | Do not contribute; redirected |

---

## Platform layer

| Product | Repo | Role | Surfaces |
|---------|------|------|----------|
| **Coastal-Alpine-Core** | [Coastal-Alpine-Core](https://github.com/fivepanelhat/Coastal-Alpine-Core) | Shared edge SDK — SecurityGuard, telemetry, Ollama client, portal_core, flywheel patterns | Win / Linux / RPi |
| **Weaver** | [Weaver](https://github.com/fivepanelhat/Weaver) | Multi-tenant orchestration + local RAG mesh | Win / Linux / RPi |
| **Aether** | [Aether](https://github.com/fivepanelhat/Aether) | Sovereign agentic companion, skills, HITL, computer-use (gated) | Win / Linux / macOS |
| **coastal-alpine-stack** | [coastal-alpine-stack](https://github.com/fivepanelhat/coastal-alpine-stack) | Compose / K3s monorepo deploy fabric | Win / Linux / RPi |
| **Sovereign-Edge-Firmware** | [Sovereign-Edge-Firmware](https://github.com/fivepanelhat/Sovereign-Edge-Firmware) | ESP32 + edge hub field layer (mTLS MQTT intent) | Field + Pi hub |

**Canonical node:** Raspberry Pi 5 **16GB** + **Hailo-10H** (do not mix 8GB / Hailo-8 narratives in product docs).

---

## Beachheads (P0)

### Byte Size Kai — agritech

| | |
|--|--|
| **Brand** | Byte Size Kai |
| **Repo** | [Byte-Size-Kai](https://github.com/fivepanelhat/Byte-Size-Kai) |
| **Role** | Lead commercial edge product — multi-modal crop / microgreens / Mana Kai–class intelligence |
| **Why it exists** | Rural latency, cloud blackouts, fragmented sensors, sovereignty on whenua |
| **Stack** | Core + Hailo vision + local Ollama paths |
| **GTM note** | Primary industries narrative; separate from social care pitch |

### Front Line Whanau — social / care

| | |
|--|--|
| **Brand** | Front Line Whanau |
| **Repo** | [Front_Line_Whanau](https://github.com/fivepanelhat/Front_Line_Whanau) |
| **Live** | https://front-line-whanau.vercel.app |
| **Role** | National platform for whānau and practitioners on preterm / frontline pathways |
| **Capabilities** | Dual portals, directory, Taonga Vault patterns, AI draft/prepare only, moderation HITL |
| **Narrative** | Holds both hard days and celebration (milestones, first holds, discharge) |
| **Scorecard** | L0–L1 — strong external Te Mana Raraunga claims blocked until MVS evidence |
| **GTM note** | Own cultural HITL and care narrative — **not** mixed into agritech cold pitch |

---

## Domain portals (supporting)

| Product | Repo | Domain |
|---------|------|--------|
| SoilGuard | [SoilGuard-Portal](https://github.com/fivepanelhat/SoilGuard-Portal) | Soil / nutrient context |
| AquaGuard | [AquaGuard-Portal](https://github.com/fivepanelhat/AquaGuard-Portal) | Water / runoff / turbidity |
| Sting-Operation-AI | [Sting-Operation-AI](https://github.com/fivepanelhat/Sting-Operation-AI) | Hive / biosecurity vision |

Background until a beachhead or pilot explicitly needs them.

---

## Founder & utility

| Product | Repo | Role |
|---------|------|------|
| **NZ-Start-Up** | [NZ-Start-Up](https://github.com/fivepanelhat/NZ-Start-Up) | Founder OS + EDA-oriented tools, skills pack |
| **CAT-mail** | CAT-mail | Privacy-first email assist — **parked** vs beachheads |
| **fivepanelhat** | [fivepanelhat](https://github.com/fivepanelhat/fivepanelhat) | Portfolio landing, architecture map, company pack |

---

## Archived

| Former | Status |
|--------|--------|
| whanau-preterm-support-hub | Merged into Front_Line_Whanau (2026-07-16) — do not contribute |

---

## Skills & intelligence (Aether)

Aether hosts production and experimental skills. **System of record for alignment evidence:** [Aether `docs/alignments/`](https://github.com/fivepanelhat/Aether/tree/main/docs/alignments).

---

## Packaging intent (no public $)

Commercial packaging is documented for segments and GTM sequence without public dollar prices. Agents **do not** invent ARR, pilot counts, or signed LOIs.

---

## Licence posture

Portfolio standardised on **Coastal Alpine Tech proprietary** terms unless a specific repo declares otherwise. See each repo `LICENSE`.
