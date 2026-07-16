# Funding Guide - Coastal Alpine Tech

**Audience:** Founders, grant leads, Aether/Weaver agents (HITL) 
**Last updated:** 2026-07-13 
**Classification:** Diamond (governance) + Gold (workflow)

---

## 1. Purpose

Win **non-dilutive** (and selectively dilutive) capital that advances:

1. **Sovereign edge AI** - offline-first, NZ data residency, RPi 5 + Hailo-10H 
2. **Agritech / primary industries** - water, soil, biosecurity, cultivation portals 
3. **Maori data & economic outcomes** - Te Mana Raraunga, whenua productivity, export readiness 
4. **Deeptech R&D** - multi-modal edge inference, local RAG, agentic computer use 

This guide is the human playbook. The machine playbook is [grants-agent/SKILL.md](grants-agent/SKILL.md).

---

## 2. Operating principles (non-negotiable)

| Principle | Practice |
| :--- | :--- |
| **Sovereignty first** | No proposal that requires silent offshore export of Maori / farm / health data |
| **Truth in claims** | Only claim capabilities shipped or roadmap-dated in public repos |
| **HITL** | Every submit / signature / budget figure needs a human owner |
| **Cultural review** | Iwi/hapu/whanau framing, Te Mana Raraunga claims -> Cultural Advisor path |
| **No double-dip** | Track co-funding sources; New to R&D forbids other NZ public co-fund for the 60% |
| **CAT tiers** | Map each project to Diamond / Platinum / Gold before writing narrative |
| **Kotahitanga** | Capital allocation follows OCAP + compliance baselines when internal funds involved |

---

## 3. Portfolio -> funding themes

| Product / layer | Strongest funding themes | Example funds |
| :--- | :--- | :--- |
| **Coastal-Alpine-Core** | Edge SDK, security, offline inference | New to R&D, RDTI, NZIAT partner |
| **Weaver** | Multi-tenant RAG, orchestration, public-sector readiness | New to R&D, NZIAT, SOC 2 narrative |
| **Aether** | Agentic AI, computer use, skills | New to R&D, R&D Career, NZIAT |
| **coastal-alpine-stack** | Deploy, remediate, K3s | Diamond infra + PSGF systems projects |
| **Blue-Moon / SoilGuard / AquaGuard** | Agritech, water, soil, kai | PSGF, MABx, MDF (with Maori partners) |
| **Sting-Operation-AI** | Biosecurity vision | PSGF, biosecurity / MPI pathways |
| **Sovereign-Edge-Firmware** | Field IoT, mTLS MQTT | PSGF hardware + New to R&D |
| **Whanau hubs** | Community / health-adjacent digital | Careful: privacy + cultural review first |

---

## 4. Standard funding workflow (Gold)

```text
1. Discover -> grants-agent scan + tracker update
2. Fit-score -> score_fit.py + human review (70 to pursue)
3. Partner -> iwi / farm / uni / CRIs if required by fund
4. Narrative -> agent draft from knowledge-base + product facts
5. Budget -> human finance lead; co-fund source locked
6. HITL gate -> Compliance + Cultural + CFO as applicable
7. Submit -> portal / regional office
8. Track -> FUNDING_TRACKER status machine
9. Deliver -> reports, evidence, compliance artefacts
10. Learn -> update knowledge-base + agent references
```

### Status machine (tracker)

`watch -> researching -> fit_scored -> partnering -> drafting -> hitl_review -> submitted -> clarification -> awarded | declined | withdrawn -> reporting -> closed`

---

## 5. Eligibility readiness checklist (org)

Before first application:

- [ ] NZ legal entity confirmed (company / Maori incorporation / eligible trust as required)
- [ ] NZBN, bank account, 3-year financials available
- [ ] R&D spend history documented (New to R&D: <$150k R&D and <$5k gov R&D funding last 3 years)
- [ ] Co-funding capacity for 60% (cashflow + bank evidence) **or** 6-month raise plan
- [ ] Compliance posture narrative (Privacy Act, Te Mana Raraunga, SOC 2 roadmap)
- [ ] Named Compliance Officer / Privacy Officer / Cultural Advisor contacts
- [ ] Hardware BOM and demo path (RPi 5 16GB + Hailo-10H) documented
- [ ] No over-claims vs public README / releases

---

## 6. Narrative building blocks

Reuse these blocks; customise per fund:

### 6.1 Problem (NZ primary / rural)

Rural connectivity blackouts, biosecurity pressure, nutrient / water regulation, labour shortages, and cloud-dependent AI that exports data offshore.

### 6.2 Solution (sovereign edge)

Offline-native multi-modal agents on **RPi 5 16GB + Hailo-10H**, local Ollama LLMs, mTLS MQTT field mesh, Te Mana Raraunga-aligned residency.

### 6.3 Differentiation

Hybrid **Windows + Linux** develop -> **RPi production**; open architecture map; compliance skill pack; domain portals (water, soil, hive, microgreens).

### 6.4 Impact metrics (examples - replace with evidence)

- Inference latency / offline uptime SLO 
- On-farm decisions without cloud 
- Regulatory lockout events prevented (actuators) 
- Local FTEs / rangatahi training hours 
- Maori partner benefit-sharing (if applicable)

### 6.5 Risk & HITL

High-risk agent actions gated; capital and cultural decisions human-approved; dual-key models for sensitive Maori data where required.

---

## 7. Co-funding & stacking rules

| Fund | Typical co-fund | Stack notes |
| :--- | :--- | :--- |
| New to R&D | Applicant 60% cash (not NZ public) | Can later use RDTI on ongoing R&D |
| PSGF | Co-investment (ratios by project type) | Distinct activities if also seeking TPK |
| MDF | Case-by-case; ROI + sustainability plan | Contact TPK regional office first |
| RDTI | Tax credit, not a cash grant | Compatible after capability built |
| R&D Experience / Career | Wage subsidy style | Builds capability for larger R&D |

**Rule:** One workstream, multiple funders only if activities are **distinct and attributable**.

---

## 8. Partner strategy

| Partner type | When needed | CAT use |
| :--- | :--- | :--- |
| Iwi / hapu / Maori agribusiness | MDF, whenua, cultural data | Benefit-sharing + OCAP |
| Farm / orchard / hive operators | PSGF pilots | Field validation data (local) |
| University / CRI | NZIAT, research platforms | Joint IP + student grants |
| Regional incubators / chambers | Navigation | Innovation Services intros |

---

## 9. Proposal quality bar (Diamond)

1. **Uncertainty stated** - scientific/technical uncertainty a competent professional cannot already resolve from public knowledge 
2. **Systematic method** - plan, milestones, evaluation 
3. **Sovereignty** - data flow diagram (edge stay local) 
4. **Compliance mapping** - IPP / TMR / SOC 2 control IDs where relevant 
5. **Budget realism** - labour, hardware, capability development 5% for New to R&D 
6. **Outcomes & evidence** - measurable KPIs + reporting cadence 
7. **Exit / sustainability** - what happens when grant ends 

---

## 10. Cadence

| Cadence | Action |
| :--- | :--- |
| **Weekly** | Agent scan open calls; update tracker CSV |
| **Fortnightly** | Human review of P0/P1 pipeline |
| **Monthly** | Knowledge-base refresh from skill / product changes |
| **Per submission** | Post-mortem -> agent reference updates |

---

## 11. Contacts (fill-in)

| Role | Name | Email |
| :--- | :--- | :--- |
| Grant lead | _TBD_ | _TBD_ |
| Finance / CFO | _TBD_ | _TBD_ |
| Compliance Officer | _TBD_ | _TBD_ |
| Cultural Advisor | _TBD_ | _TBD_ |
| Innovation Services (MBIE) | - | [funds.business.govt.nz/customer-support](https://funds.business.govt.nz/customer-support/) |
| TPK regional (Taranaki) | - | [tpk.govt.nz/whakapa-mai](https://www.tpk.govt.nz/whakapa-mai) |
| MPI PSGF | - | psgfund@mpi.govt.nz (confirm on MPI site) |

---

## 12. Disclaimer

This guide is operational research, **not legal or financial advice**. Always verify eligibility, open/closed status, and terms on the funder's official pages before applying.
