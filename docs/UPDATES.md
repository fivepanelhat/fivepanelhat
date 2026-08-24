# Company Updates — Coastal Alpine Tech

**Purpose:** Single place for clients, partners, and the founder to see major company and product updates across the Kiwi Edge AI Stack, with direct links to the relevant repositories and artefacts.

**Last updated:** 24 August 2026

---

## 24 August 2026 — Sprintit AI

### Don't audit. Sprintit.

**Sprintit AI** is Coastal Alpine Tech’s client-facing readiness product.

> **Tagline:** Don't audit. Sprintit.  
> **Product:** Sprintit AI

We deliberately avoid the word *audit*. For many founders, farms, and regional operators, “audit” signals inspection, pass/fail, regulatory exposure, and cost. **Sprintit** keeps the work rigorous and time-boxed, but frames it as a collaborative improvement sprint — partnership and momentum, not inspection.

### What Sprintit AI is

A time-boxed, collaborative readiness sprint for New Zealand founders, farms, EDAs, and operators who are adopting or assessing AI, edge systems, or data-sovereign practices.

It uses Coastal Alpine Tech’s skills fleet, governance patterns, and Kiwi Edge architecture knowledge to produce a clear picture of current state and a prioritised action list — without the language or baggage of a formal audit.

Typical Sprintit AI work can cover:

| Focus | What the sprint examines |
|-------|--------------------------|
| **Founder / company readiness** | Formation hygiene, compliance calendar, grant/RDTI evidence posture, legal draft readiness |
| **AI & agent posture** | HITL ceilings, claim discipline, where agents draft vs where humans must act |
| **Data & sovereignty** | Local-first defaults, consent, residency, Te Mana Raraunga alignment where relevant |
| **Edge / agritech path** | Node readiness, pilot partnership clarity, farm/community consent gates (Byte Size Kai context) |
| **Go-to-market & narrative** | One-pagers, investor/EDA packs, stage-honest positioning |

Outputs are practical: findings, gaps, and a short ranked plan the client can act on with their own advisors. Sprintit AI does **not** issue formal audit opinions, certifications, or legal conclusions.

### Why the tagline

| | |
|--|--|
| **Don't audit** | Removes the reputation problem: inspection, blame, and disengagement |
| **Sprintit** | Time-boxed, collaborative, improvement-focused — work the client owns |
| **Sprintit AI** | The product name for the readiness sprint, powered by CAT’s skills and stack |

### Why we developed it

1. **Client language** — Regional founders, farms, and EDAs need diagnostic help; “audit” closes doors.
2. **Reuse of the fleet** — NZ Start-Up skills, Byte Size Kai operational skills, Aether governance, and stack architecture already encode the questions a readiness review must ask.
3. **Stage-honest commercial path** — Short engagement, clear deliverable, path into deeper pilot or white-label work.
4. **Trust** — Same HITL rules: we prepare findings and recommendations; the client decides and acts with their own professional advisors where required.

**Status:** Concept, tagline, and client framing formalised 24 August 2026. Delivery uses existing skills and architecture; packaging and offer materials will continue to evolve.

**Related:** [NZ-Start-Up](https://github.com/fivepanelhat/NZ-Start-Up) · [Byte-Size-Kai](https://github.com/fivepanelhat/Byte-Size-Kai) · [Aether](https://github.com/fivepanelhat/Aether) · [Kiwi Edge landing](https://github.com/fivepanelhat/fivepanelhat)

---

## 24 August 2026 (pm) — Continuous iteration: skills, harness, Aether, Weaver

Ongoing hardening and refinement across the operating system and foundation layers. Stage-honest design/iteration work — not production claims.

### Skills fleet improvements

| Area | What improved |
|------|----------------|
| **HITL consistency** | All new NZ Startup + Byte Size Kai skills enforce L2 minimum on legal, finance, data, and cultural paths; Human Action Checklist pattern standardised |
| **Cultural sensitivity flags** | Byte Size Kai skills and mana-kai-consent-and-sovereignty elevate Te Mana Raraunga gates; explicit “escalate rather than assume” language |
| **Evidence-only synthesis** | customer-discovery-synthesis and community-insight-synthesis refuse invented quotes/outcomes |
| **Progressive disclosure** | Skill frontmatter + short SKILL.md bodies; detailed artefacts kept in references/ where needed |
| **Manifest as source of truth** | NZ Startup in a Box and Byte Size Kai manifests kept in sync with live skill set |

**Repos:** [NZ-Start-Up](https://github.com/fivepanelhat/NZ-Start-Up) · [Byte-Size-Kai](https://github.com/fivepanelhat/Byte-Size-Kai)

### cat-agent-harness improvements

| Area | What improved |
|------|----------------|
| **Plugin-first runtime posture** | Local-first, hard HITL, Te Mana Raraunga-aligned framing reinforced |
| **Sovereignty boundary** | Explicit “no silent exfil” and owner-controlled key posture in harness description |
| **Fleet coherence** | Harness positioned as the runtime under the Kiwi Edge stack (alongside Aether skills and Core primitives) |

**Repo:** [cat-agent-harness](https://github.com/fivepanelhat/cat-agent-harness) *(private)*

### Aether improvements

| Area | What improved |
|------|----------------|
| **Computer-use HITL** | Default per-step approval for click/type/shell; dry-run and auto-approve switches documented |
| **Skills catalogue** | Kiwi Edge architecture, Te Mana Raraunga sovereignty, error-remediation, git-workflow, CI failure parser skills surface clearly |
| **Webhook remediation** | Propose-only default; optional auto-remediate behind explicit env flag; retry/backoff documented |
| **Dual-platform install** | install.sh / install.ps1 + doctor path kept current |
| **Claim discipline** | Architecture diagrams labelled as target design; stage honesty in economic benefits section |

**Repo:** [Aether](https://github.com/fivepanelhat/Aether) · Skills guide: [docs/SKILLS.md](https://github.com/fivepanelhat/Aether/blob/main/docs/SKILLS.md)

### Weaver improvements

| Area | What improved |
|------|----------------|
| **Tenant isolation posture** | Intake / Fulfilment / Resolution agents + partitioned vector/SQL stores reiterated as design baseline |
| **Core pin hygiene** | Documented pin to Coastal-Alpine-Core (v0.5.x line) in install paths |
| **Hybrid stack links** | Clear pairing with Aether (companion/HITL) and Core (guards, telemetry, flywheel) |
| **Offline edge framing** | Local Ollama + RPi 5 16GB + Hailo-10H target kept consistent with portfolio |
| **Stage honesty** | Performance numbers and deployment scenarios labelled as targets / illustrative, not production SLAs |

**Repo:** [Weaver](https://github.com/fivepanelhat/Weaver) · [ARCHITECTURE.md](https://github.com/fivepanelhat/Weaver/blob/main/ARCHITECTURE.md)

---

## 24 August 2026 (am) — NZ Startup in a Box + Byte Size Kai skill fleets completed

Major expansion of the digital-employee / skills operating system.

### NZ Startup in a Box (Founder OS)

The full early-stage founder skill fleet is now complete and documented.

**Core skills now live (Priority 1–4):**

| Skill | Role |
|-------|------|
| legal-document-assistant | Draft-only NDAs, pilot LOIs, MSAs, Privacy Policy, ToS, contractor & employment skeletons |
| finance-clerk | Runway, GST/IRD calendar, Xero guidance, simple cash & unit-economics views |
| compliance-registrar | Annual returns, director duties, Privacy Act 2020, H&S, employment status support |
| content-comms-officer | Brand voice, website/LinkedIn copy, one-pagers, press, founder narrative |
| nz-angel-networks | Icehouse / Ice Angels pathway + Enterprise Angels, Angel HQ, Flying Kiwi Angels, K1W1 |
| people-ops-officer | Contractor vs employee, role scorecards, onboarding checklists |
| ip-protection-officer | IPONZ trademarks, patent pathway notes, trade secrets, open-source vs proprietary |
| customer-discovery-synthesis | Interview notes → insight reports, personas, JTBD maps |
| risk-insurance-advisor | Stage-appropriate insurance checklist and broker conversation prep |

**Primary repo:** [NZ-Start-Up](https://github.com/fivepanelhat/NZ-Start-Up) — Founder OS + EDA white-label kit  
**Landing / portfolio:** [fivepanelhat](https://github.com/fivepanelhat/fivepanelhat)

### Byte Size Kai (live farm / community kai operational layer)

A dedicated, tight skill fleet for live farm node deployment, pilot partnerships, and Te Mana Raraunga-aligned data practice.

| Skill | Role |
|-------|------|
| byte-size-kai-orchestrator | Routes work, weekly status, enforces cultural + HITL gates |
| kai-pilot-partnership | Pilot LOIs with farms / whānau / iwi / councils — success criteria, data ownership, reciprocal value |
| farm-node-commissioning | Five-gate path from site agreement → hardware live → first validated data under local control |
| community-insight-synthesis | Farm & community conversation notes → themes and action implications |
| mana-kai-consent-and-sovereignty | Consent artefacts, data residency checks, Te Mana Raraunga gates |

**Primary product repo:** [Byte-Size-Kai](https://github.com/fivepanelhat/Byte-Size-Kai)  
**Framing rule:** Public and external language uses **Byte Size Kai**. Horowhenua Mana Kai is referenced only as pilot context when accurate.

---

## 27 July 2026 — Company knowledge pack

- Added `docs/company/` (COMPANY_PROFILE, CATALOGUE, BRAIN)
- Alignment evidence and congruence hygiene updates

**Links:**
- [docs/company/](https://github.com/fivepanelhat/fivepanelhat/tree/main/docs/company)
- [docs/CHANGELOG.md](https://github.com/fivepanelhat/fivepanelhat/blob/main/docs/CHANGELOG.md)

---

## 17 July 2026 — AI Infrastructure Leadership + Hardening

- New [AI_INFRASTRUCTURE_LEADERSHIP.md](https://github.com/fivepanelhat/fivepanelhat/blob/main/AI_INFRASTRUCTURE_LEADERSHIP.md)
- Positioning as NZ sovereign edge AI infrastructure leader
- Hardening and claim-discipline updates

---

## 16 July 2026 — Commercial Positioning + Enterprise Readiness

- [Commercial Positioning](https://github.com/fivepanelhat/fivepanelhat/blob/main/.github/funding/COMMERCIAL_POSITIONING.md)
- [GOVERNANCE.md](https://github.com/fivepanelhat/fivepanelhat/blob/main/GOVERNANCE.md)
- [Security & Compliance Roadmap](https://github.com/fivepanelhat/fivepanelhat/blob/main/.github/compliance/SECURITY_ROADMAP.md)
- [Threat Model](https://github.com/fivepanelhat/fivepanelhat/blob/main/.github/compliance/THREAT_MODEL.md)

---

## 13 July 2026 — Funding system scaffold + authenticity hygiene

- Funding guide, tracker, grants agent skill, knowledge base, fit scorer
- Pre-seed stage honesty and claims hygiene across the portfolio

**Links:**
- [Funding index](https://github.com/fivepanelhat/fivepanelhat/tree/main/.github/funding)
- [FUNDING_GUIDE.md](https://github.com/fivepanelhat/fivepanelhat/blob/main/.github/funding/FUNDING_GUIDE.md)
- [INVESTOR_MATRIX.md](https://github.com/fivepanelhat/fivepanelhat/blob/main/.github/funding/INVESTOR_MATRIX.md)

---

## 12 July 2026 — Hybrid foundation + dual-platform installers

- Core | Weaver | Aether | coastal-alpine-stack aligned
- `install.sh` + `install.ps1` on foundation repos
- Landing page restored with full portfolio and architecture

**Key repos:**
- [Coastal-Alpine-Core](https://github.com/fivepanelhat/Coastal-Alpine-Core)
- [Weaver](https://github.com/fivepanelhat/Weaver)
- [Aether](https://github.com/fivepanelhat/Aether)
- [coastal-alpine-stack](https://github.com/fivepanelhat/coastal-alpine-stack)

---

## How to use this page

- **Clients / partners:** Use the dated entries and hyperlinks to jump straight to the relevant product or documentation.
- **Founder:** This is the canonical chronological view of major company updates for board packs, investor updates, and grant narratives.
- **Agents:** Prefer this page + the individual repo READMEs over inventing status.

For the full technical changelog of the landing repo itself, see [docs/CHANGELOG.md](./CHANGELOG.md).

---

*Coastal Alpine Tech Limited — Pre-seed | Taranaki, Aotearoa New Zealand*
