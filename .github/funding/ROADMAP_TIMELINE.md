# Funding Roadmap & Timeline — Coastal Alpine Tech

**Version:** 1.0.0 · **Date:** 2026-07-13 (anchor)  
**Horizon:** ~24 months (2026-07 → 2028-06)  
**Companions:** [FUNDING_ELIGIBILITY_MATRIX.md](FUNDING_ELIGIBILITY_MATRIX.md) · [INVESTOR_MATRIX.md](INVESTOR_MATRIX.md) · [FUNDING_TRACKER.md](FUNDING_TRACKER.md)  
**Machine todos:** [matrices/roadmap_todos.csv](matrices/roadmap_todos.csv)

> **How to use:** Treat every `- [ ]` as a real todo. Check off in git as you complete, or copy into Linear/GitHub Issues with the same IDs (`RD-###`, `PS-###`, etc.). Dates are **targets**, not guarantees. HITL before any submit.

**Owners (fill names):**

| Role | Name | Owns |
| :--- | :--- | :--- |
| Grant lead | _TBD_ | Applications, navigator contact |
| Finance | _TBD_ | Co-fund, cashflow, RDTI, budgets |
| Cultural Advisor | _TBD_ | MDF, MABx, Māori-outcome claims |
| Tech lead | _TBD_ | R&D plan, pilots, demos |
| GTM / pilots | _TBD_ | Farm partners, LOIs, pricing |

---

## 0. Master timeline (one view)

```text
2026
Jul ████ FOUNDATION + New to R&D start + R&D Experience open
Aug ████ New to R&D submit path + R&D Career prep + RDTI setup
Sep ████ PSGF EOI draft + pilot LOIs + SOM pack v1
Oct ████ Pilot #1 live + MDF regional chat (if partnership ready)
Nov ████ PSGF full proposal path + angel soft circle
Dec ████ Year review · Experience grant wrap if used

2027
Q1  ████ Paid pilots ×2–3 · NZ seed materials · NZIAT partner push
Q2  ████ Angel / pre-seed close target · Career/grad outcomes
Q3  ████ ARR discipline · AU beachhead memo · agritech VC watch
Q4  ████ Seed or bridge · multi-farm metrics

2028
H1  ████ Series A prep only if ARR/pilot bar met · global agritech later
```

### Phase legend

| Phase | Window | Theme | Primary capital |
| :--- | :--- | :--- | :--- |
| **P0 Foundation** | Jul–Aug 2026 | Entity, books, narrative, roles | Enables all |
| **P1 Non-dilutive** | Jul–Dec 2026 | Grants that don’t sell equity | New to R&D, Experience, Career, RDTI |
| **P2 Field proof** | Sep 2026–Jun 2027 | Pilots + PSGF | PSGF, LOIs, paid PoCs |
| **P3 Partnership capital** | Oct 2026–ongoing | Māori / whenua (only if real) | MDF, MABx |
| **P4 Early equity** | Nov 2026–Q2 2027 | Angels / NZ seed | SAFE / seed |
| **P5 Scale equity** | 2027 H2–2028 | Only with metrics | Seed+ / agritech A |

---

## 1. Shared foundation (do first — unblocks everything)

**Goal:** Be application-ready for any P0 fund within 4–6 weeks.  
**Target complete:** **2026-08-31**

### Todos — Foundation `FD`

- [ ] **FD-001** · Assign named owners (Grant lead, Finance, Cultural, Tech, GTM) · _Due: 2026-07-18_ · Owner: Founder
- [ ] **FD-002** · Confirm legal entity type + NZBN + bank account for grants · _Due: 2026-07-25_ · Owner: Finance
- [ ] **FD-003** · Compile last 3 years financials (or available) + 12-month cashflow template · _Due: 2026-08-01_ · Owner: Finance
- [ ] **FD-004** · Document R&D spend last 3 years (total) + any gov R&D funding received · _Due: 2026-07-25_ · Owner: Finance
- [ ] **FD-005** · Cap table + IP assignment check (code/IP in company) · _Due: 2026-08-08_ · Owner: Founder + counsel
- [ ] **FD-006** · One-page **CAT narrative spine** (problem / solution / why now / moat / honesty) · _Due: 2026-07-20_ · Owner: Grant lead
- [ ] **FD-007** · Bottom-up **SOM v0** spreadsheet (price × farms × seats) · _Due: 2026-08-15_ · Owner: Finance + GTM
- [ ] **FD-008** · Demo kit BOM list (RPi 5 16GB + Hailo-10H + sensors) + cost card · _Due: 2026-07-25_ · Owner: Tech lead
- [ ] **FD-009** · Field demo script (10 min) + screen recording of offline inference · _Due: 2026-08-08_ · Owner: Tech lead
- [ ] **FD-010** · Compliance one-pager (Privacy Act / TMR / HITL / “framework not certified”) · _Due: 2026-07-25_ · Owner: Grant lead
- [ ] **FD-011** · Create private `opportunities/evidence/` folder policy (no secrets in git) · _Due: 2026-07-18_ · Owner: Grant lead
- [ ] **FD-012** · Weekly funding standup (15 min): tracker + this roadmap · _Due: start 2026-07-21_ · Owner: Grant lead

**Exit criteria:** FD-001–010 done → start New to R&D portal work without scrambling.

---

## 2. Per-opportunity roadmaps (todo lists)

### 2.1 CAT-G-001 — New to R&D Grant (P0 · likelihood 82)

| | |
| :--- | :--- |
| **Target submit** | **2026-08-29** (or earlier once co-fund locked) |
| **Target decision** | ~6–12 weeks post-submit (confirm with Innovation Services) |
| **Target start spend** | **2026-Q4** |
| **Depends on** | FD-002–004, FD-006, FD-008 |

#### Timeline

```text
W1–2  Contact navigator + eligibility verbal
W2–4  Project plan + capability skills + budget
W4–6  Cashflow + co-fund evidence
W6–8  Portal draft → HITL → submit
Q4+   Claims quarterly + RDTI intro
```

#### Todos — `RD`

- [ ] **RD-001** · Book Innovation Services navigator / FES call · _Due: 2026-07-18_ · [portal support](https://funds.business.govt.nz/customer-support/)
- [ ] **RD-002** · Confirm entity eligible (company / Māori incorporation path) · _Due: 2026-07-25_
- [ ] **RD-003** · Confirm &lt;$150k R&D spend + &lt;$5k gov R&D funding last 3 yrs · _Due: 2026-07-25_
- [ ] **RD-004** · Write R&D uncertainty statement (offline multi-modal + tenant isolation + TMR residency) · _Due: 2026-07-28_
- [ ] **RD-005** · Select ≥2 capability skills (recommend: Regulatory/compliance + Information management) · _Due: 2026-07-28_
- [ ] **RD-006** · Draft work packages (Core optimisations · Weaver offline RAG eval · portal pilot · capability) · _Due: 2026-08-08_
- [ ] **RD-007** · Full eligible cost budget ≤$1m total · 40% ask ≤$400k · ≥5% capability · _Due: 2026-08-15_
- [ ] **RD-008** · 12-month cashflow + bank evidence for 60% co-fund · _Due: 2026-08-20_
- [ ] **RD-009** · If raising co-fund: term sheet / shareholder declaration path (6-month window rule) · _Due: 2026-08-20_
- [ ] **RD-010** · Download application template + funding agreement; read obligations · _Due: 2026-07-25_
- [ ] **RD-011** · Complete portal draft offline → copy in · _Due: 2026-08-22_
- [ ] **RD-012** · HITL checklist (grant lead + finance) · _Due: 2026-08-27_ · see [application-checklist](grants-agent/references/application-checklist.md)
- [ ] **RD-013** · **SUBMIT** · update tracker → `submitted` · _Due: 2026-08-29_
- [ ] **RD-014** · Respond to clarification requests within 5 business days · _Ongoing_
- [ ] **RD-015** · On award: kickoff claim calendar + RDTI intro session · _Due: +2 weeks of award_

---

### 2.2 CAT-G-005 — R&D Experience Grant (P1 · opens 2026-07-13)

| | |
| :--- | :--- |
| **Target apply** | **2026-07-20 → 2026-08-15** (confirm close date on open) |
| **Project window** | Often summer / ~10 weeks — plan **2026-11–2027-02** or next cycle |
| **Depends on** | FD-001, RD-004 style project brief |

#### Todos — `EX`

- [ ] **EX-001** · Day-of-open: confirm official rules/dates on business.govt.nz · _Due: 2026-07-13_
- [ ] **EX-002** · Write 1-page intern project (Hailo benchmarks **or** Weaver eval harness **or** firmware fixtures) · _Due: 2026-07-18_
- [ ] **EX-003** · Name supervisor + H&S + IP ownership note · _Due: 2026-07-20_
- [ ] **EX-004** · University / polytech candidate pipeline list · _Due: 2026-07-25_
- [ ] **EX-005** · Apply when eligible · HITL · _Due: 2026-08-15_
- [ ] **EX-006** · On award: onboard intern checklist + weekly demo day · _Due: start week_

---

### 2.3 CAT-G-006 — R&D Career Grant (P1 · opens 2026-08-31)

| | |
| :--- | :--- |
| **Target apply** | **2026-09-01 → 2026-09-30** (confirm close) |
| **Placement** | 6 months · **2026-Q4–2027-Q2** |
| **Depends on** | Role def, supervision capacity |

#### Todos — `CR`

- [ ] **CR-001** · Define role: Aether reliability **or** Hailo vision science **or** sovereignty/eval · _Due: 2026-08-15_
- [ ] **CR-002** · Masters vs PhD track + budget (up to $30k / $35k) · _Due: 2026-08-20_
- [ ] **CR-003** · University relationship / candidate shortlist · _Due: 2026-08-28_
- [ ] **CR-004** · Apply at open · HITL · _Due: 2026-09-15_
- [ ] **CR-005** · On award: 6-month milestone plan aligned to Platinum flywheel · _Due: +1 week_

---

### 2.4 CAT-G-004 — RDTI (P1 · ongoing)

| | |
| :--- | :--- |
| **Target systems live** | **2026-09-30** |
| **First claim-ready year** | Tax year aligned after systems + New to R&D intro |

#### Todos — `RT`

- [ ] **RT-001** · Book RDTI intro (bundled with New to R&D path) · _Due: 2026-08-30_
- [ ] **RT-002** · Chart of accounts tags: R&D labour / materials / contractors · _Due: 2026-09-15_
- [ ] **RT-003** · Timesheet / project code policy for Core, Weaver, Aether, portals · _Due: 2026-09-15_
- [ ] **RT-004** · Eligible vs ineligible activity cheatsheet for eng · _Due: 2026-09-30_
- [ ] **RT-005** · Quarterly internal RDTI review · _Start: 2026-Q4_

---

### 2.5 CAT-G-003 — Primary Sector Growth Fund (P0 · likelihood 75)

| | |
| :--- | :--- |
| **Target EOI** | **2026-10-31** |
| **Target full proposal** | **2027-Q1–Q2** (expect long cycle) |
| **Depends on** | FD-007, pilot partners, co-invest plan |

#### Timeline

```text
Aug–Sep   Partner farm shortlist + LOI templates
Sep–Oct   EOI draft (problem, solution, economic benefit)
Oct       EOI HITL → submit / lodge per MPI process
Nov–Mar   Full proposal + co-invest packaging
2027      Contracting → delivery years
```

#### Todos — `PS`

- [ ] **PS-001** · Choose pilot wedge: SoilGuard **or** AquaGuard **or** Sting (pick one primary) · _Due: 2026-08-08_
- [ ] **PS-002** · List 10 target farms/orchards/hives (Taranaki + 1 other region) · _Due: 2026-08-22_
- [ ] **PS-003** · LOI / MoU template (data stays on-farm; pilot scope; no over-claim) · _Due: 2026-08-29_
- [ ] **PS-004** · Secure ≥2 signed pilot intent LOIs · _Due: 2026-09-30_
- [ ] **PS-005** · Economic benefit model (compliance cost avoided, labour, yield proxy) · _Due: 2026-10-10_
- [ ] **PS-006** · Co-investment plan (cash + in-kind hours + hardware) · _Due: 2026-10-15_
- [ ] **PS-007** · EOI draft via grants-agent → human rewrite · _Due: 2026-10-20_
- [ ] **PS-008** · HITL (grant + finance + tech) · **lodge EOI** · _Due: 2026-10-31_
- [ ] **PS-009** · Deploy pilot #1 hardware on-farm · _Due: 2026-11-30_
- [ ] **PS-010** · 30-day pilot evidence pack (uptime, offline rate, farmer feedback) · _Due: 2026-12-31_
- [ ] **PS-011** · Full proposal if invited / next stage · _Due: 2027-Q1_
- [ ] **PS-012** · Monthly MPI process check (guidelines, contacts) · _Ongoing_

---

### 2.6 CAT-G-002 — Māori Development Fund (P0* · likelihood 48 → 72 with partnership)

| | |
| :--- | :--- |
| **Target first regional meeting** | **2026-10-15** (only if pathway real) |
| **Target proposal** | **2027-Q1** earliest |
| **Hard gate** | Authentic kaitono / partnership — **no cold solo apply** |

#### Todos — `MD` (Cultural Advisor owns gate)

- [ ] **MD-001** · Cultural Advisor confirms go/no-go for MDF this year · _Due: 2026-08-31_
- [ ] **MD-002** · If go: identify kaitono legal entity or umbrella · _Due: 2026-09-30_
- [ ] **MD-003** · Map proposal to Priority 1 (assets/productivity) or 2 (exports) or resilience · _Due: 2026-10-05_
- [ ] **MD-004** · Contact **Taranaki / nearest TPK regional office** before writing template · _Due: 2026-10-15_
- [ ] **MD-005** · Co-design outcomes + benefit-sharing note (OCAP®) · _Due: 2026-11-15_
- [ ] **MD-006** · ROI evidence + post-grant sustainability plan · _Due: 2026-12-15_
- [ ] **MD-007** · Complete TPK template only after regional guidance · _Due: 2027-01-31_
- [ ] **MD-008** · HITL cultural + finance + grant · submit · _Due: 2027-Q1_
- [ ] **MD-009** · If no-go 2026: reassess Q2 2027 · park without tokenism · _Due: 2026-08-31_

---

### 2.7 CAT-G-008 — MABx / whenua multi-fund (P2)

| | |
| :--- | :--- |
| **Target research complete** | **2026-09-30** |
| **Target first cluster intro** | **2026-11-30** |

#### Todos — `MX`

- [ ] **MX-001** · Search [tupu.nz](https://www.tupu.nz/en/kokiri/search-for-funding-opportunities/) for Taranaki + nationwide digital/productivity · _Due: 2026-08-31_
- [ ] **MX-002** · Read MABx programme page; note eligibility · _Due: 2026-08-31_
- [ ] **MX-003** · One-pager “CAT as tech partner to whenua cluster” (not extractive vendor) · _Due: 2026-09-15_
- [ ] **MX-004** · Warm intro path via existing networks (no spam) · _Due: 2026-10-31_
- [ ] **MX-005** · If cluster forms: pilot kit offer + data residency MoU · _Due: 2026-Q4_

---

### 2.8 CAT-G-007 — NZIAT AI Platform partner (P2)

| | |
| :--- | :--- |
| **Target one-pager** | **2026-08-31** |
| **Target partner outreach** | **2026-09–2026-11** |

#### Todos — `NZ`

- [ ] **NZ-001** · Map shortlisted concepts (Outdoor AI / BioAI etc.) to CAT portals · _Due: 2026-08-15_
- [ ] **NZ-002** · One-pager: sovereign edge contribution (RPi fleets, offline pilots) · _Due: 2026-08-31_
- [ ] **NZ-003** · Identify 3 university/CRI contacts from public shortlist coverage · _Due: 2026-09-15_
- [ ] **NZ-004** · Outreach for edge pilot partnership (not “make us host”) · _Due: 2026-10-31_
- [ ] **NZ-005** · Revisit when platform host announced / funding flowing · _Due: 2026-Q4–2027-Q1_

---

### 2.9 CAT-G-009 — Māori Climate Platform (watch only)

#### Todos — `CL`

- [ ] **CL-001** · Quarterly check MfE / Beehive for Stage 3 · _Due: each quarter_
- [ ] **CL-002** · Engage only if marae-led kaitono + edge energy/water fit · _Gate_

---

### 2.10 Equity path A — Angels / pre-seed (likelihood 55 → 75)

| | |
| :--- | :--- |
| **Target materials ready** | **2026-11-30** |
| **Target first closes** | **2027-Q1–Q2** |
| **Depends on** | ≥1 pilot evidence + SOM v1 + FD complete |

#### Todos — `AN`

- [ ] **AN-001** · 10-slide deck (problem, product, market bottom-up, traction, team, ask) · _Due: 2026-11-15_
- [ ] **AN-002** · Data room v0 (demo, LOIs, financials, cap table, compliance one-pager) · _Due: 2026-11-30_
- [ ] **AN-003** · Target list 20 angels / small funds (agri, deeptech, NZ) · _Due: 2026-11-15_
- [ ] **AN-004** · Soft circle (coffee, no formal raise) · _Due: 2026-12-15_
- [ ] **AN-005** · Decide instrument (SAFE terms with counsel) · _Due: 2027-01-15_
- [ ] **AN-006** · Formal raise window (budget 3–4 months) · _Due: 2027-Q1 start_
- [ ] **AN-007** · HITL on any term sheet · close · _Due: 2027-Q2_

**Do not start AN-006 until PS-009 or equivalent field proof exists.**

---

### 2.11 Equity path B — NZ seed VC (likelihood 50 → 78)

| | |
| :--- | :--- |
| **Target intro readiness** | **2027-Q2** |
| **Target raise window** | **2027-Q3–Q4** if metrics hold |

#### Todos — `SV`

- [ ] **SV-001** · Research NZGCP Aspire / Icehouse / deeptech-relevant funds thesis fit · _Due: 2026-12-15_
- [ ] **SV-002** · Metrics pack: nodes, offline %, pilots, pipeline ARR · _Due: 2027-03-31_
- [ ] **SV-003** · AU beachhead memo (which state, channel, regulation) · _Due: 2027-04-30_
- [ ] **SV-004** · Warm intros only (portfolio founders, grants network) · _Due: 2027-Q2_
- [ ] **SV-005** · Full seed process if ≥2–3 paid pilots or clear ARR path · _Due: 2027-H2_
- [ ] **SV-006** · Skip global agritech / AI growth until SV metrics cleared · _Policy_

---

### 2.12 Equity path C — Global agritech / AI growth (low now)

#### Todos — `GL`

- [ ] **GL-001** · Annual re-score vs eligibility matrix (need multi-geo + scale metrics) · _Due: each Jul_
- [ ] **GL-002** · No cold outreach to Founders Fund / a16z-class until Series A proof bar · _Policy_
- [ ] **GL-003** · Track Halter-class field metrics definitions for long-term north star · _Ongoing_

---

### 2.13 Internal Kotahitanga capital

#### Todos — `KA`

- [ ] **KA-001** · Review internal planning scenario KAS-PLAN-008 (unfunded) before any capital narrative · _Due: 2026-08-15_
- [ ] **KA-002** · Monthly review of internal planning scenarios only (no fake ACTIVE budgets) · _Ongoing_
- [ ] **KA-003** · HITL for any internal allocation &gt;$50k · _Per event_
- [ ] **KA-004** · Ensure external grant co-fund never double-counts frozen/internal pots incorrectly · _Per application_

---

## 3. Cross-cutting quarterly OKRs

### Q3 2026 (Jul–Sep) — “Eligible & known”

| Objective | Key results |
| :--- | :--- |
| Foundation complete | FD-001–012 done |
| Non-dilutive in motion | New to R&D submitted **or** in portal final; Experience applied if fit |
| Market math | SOM v0 published internally |
| Field start | ≥2 pilot LOIs |

### Q4 2026 (Oct–Dec) — “Proof on whenua”

| Objective | Key results |
| :--- | :--- |
| PSGF | EOI lodged |
| Pilot | ≥1 live edge node on real site |
| Partnership | MDF go/no-go decided; if go, TPK meeting held |
| RDTI | Cost codes live |

### Q1–Q2 2027 — “Capital options”

| Objective | Key results |
| :--- | :--- |
| Evidence | 30–90 day pilot pack |
| Equity optional | Angel materials live; soft circle done |
| Grants | New to R&D claims running if awarded; PSGF full proposal path |

### Q3–Q4 2027 — “Seed or discipline”

| Objective | Key results |
| :--- | :--- |
| Metrics | Multi-pilot; pipeline ARR defined |
| Seed | Raise **or** deliberate bootstrap with grants+revenue |
| Export | AU memo + first AU conversation |

---

## 4. Critical path (dependencies)

```text
FD-002/003/004 ──► RD-003/008 ──► RD-013 submit ──► RT-001 RDTI
       │
FD-006/007 ──► PS-005/007 ──► PS-008 EOI ──► PS-009 pilot ──► AN-001 deck
       │                              │
       └──────── MX/MD cultural ──────┴── only if MD-001 go
       
PS-009 field proof ──► AN-006 raise ──► SV-005 seed
```

**Longest poles:** (1) co-fund cash for New to R&D, (2) real farm LOIs for PSGF, (3) authentic partnership for MDF.

---

## 5. Weekly operating rhythm

| Day | Action |
| :--- | :--- |
| **Mon** | 15-min standup: blockers on open todos |
| **Wed** | Optional grants-agent discovery scan (tracker refresh) |
| **Fri** | Check off completed `- [ ]` in this file or CSV; update [FUNDING_TRACKER.md](FUNDING_TRACKER.md) |

### Status tags for each todo

`todo` · `doing` · `blocked` · `hitl` · `done` · `wontfix`

---

## 6. Milestone scoreboard

| Milestone | Target date | Status | Evidence link |
| :--- | :--- | :--- | :--- |
| Foundation exit (FD complete) | 2026-08-31 | ☐ | |
| New to R&D submitted | 2026-08-29 | ☐ | |
| R&D Experience applied | 2026-08-15 | ☐ | |
| R&D Career applied | 2026-09-15 | ☐ | |
| RDTI systems live | 2026-09-30 | ☐ | |
| ≥2 pilot LOIs | 2026-09-30 | ☐ | |
| PSGF EOI lodged | 2026-10-31 | ☐ | |
| Pilot #1 live | 2026-11-30 | ☐ | |
| MDF go/no-go | 2026-08-31 | ☐ | |
| Angel deck + data room | 2026-11-30 | ☐ | |
| First paid pilot / PoC | 2027-01-31 | ☐ | |
| Angel round closed (optional) | 2027-Q2 | ☐ | |
| NZ seed materials ready | 2027-Q2 | ☐ | |

---

## 7. Risk register (timeline)

| Risk | Impact | Mitigation todo |
| :--- | :--- | :--- |
| Co-fund shortfall for New to R&D | Delays RD-013 | RD-009 parallel raise; reduce project scope |
| No farm LOIs | PSGF slips | Expand region list; paid PoC offer |
| Cultural pathway not ready | MDF false start | MD-001 no-go without shame |
| Grant award slow | Cash gap | Bootstrap pilot on smaller hardware count |
| Equity raise too early | Bad terms / distraction | Enforce PS-009 gate before AN-006 |
| Double-counting funds | Compliance failure | KA-004 + finance matrix per application |

---

## 8. Definition of done (per capital type)

| Capital | Done means |
| :--- | :--- |
| New to R&D | Agreement signed + first claim paid |
| Experience / Career | Student/grad started + mid-point demo |
| RDTI | First eligible period filed with clean codes |
| PSGF | Contract executed **or** formal decline + learnings |
| MDF | Investment agreement **or** documented no-go |
| Angel | Funds in bank + SAFE/equity docs executed |
| Seed | Round closed + board/reporting cadence live |

---

*Update this file when dates slip. Prefer moving dates over silent rotting checkboxes.*
