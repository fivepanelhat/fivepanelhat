# Funding Tracker

**Snapshot date:** 2026-07-13  
**Machine file:** [tracker.csv](tracker.csv)  
**Status legend:** `watch` · `researching` · `fit_scored` · `partnering` · `drafting` · `hitl_review` · `submitted` · `clarification` · `awarded` · `declined` · `withdrawn` · `reporting` · `closed` · `opens_soon` · `open` · `paused`

> Verify every row against the funder site before acting. NZ science system reforms (Callaghan → MBIE / NZIAT) are in flight.

---

## Active pipeline

| ID | Opportunity | Funder | Status | Window | Amount (indicative) | Fit (0–100) | Theme tags | Next action | Owner | Brief |
| :--- | :--- | :--- | :--- | :--- | ---: | ---: | :--- | :--- | :--- | :--- |
| CAT-G-001 | New to R&D Grant | MBIE Innovation Services | **open** | Rolling (applications open) | 40% of eligible R&D up to **$400k** | 92 | deeptech,sovereign-ai,edge | Contact Innovation Services navigator; confirm R&D spend history | Grant lead | [link](opportunities/new-to-rd-grant.md) |
| CAT-G-002 | Māori Development Fund | Te Puni Kōkiri | **open** | Rolling (contact regional office first) | Proposal-based; Fund **$40.21m p.a.** | 78 | maori,whenua,exports,resilience | Book Taranaki TPK regional discussion; define kaitono entity | Grant lead + Cultural Advisor | [link](opportunities/maori-development-fund.md) |
| CAT-G-003 | Primary Sector Growth Fund (PSGF) | MPI | **open** | Open for proposals (to 2029 programme window) | Co-investment; multi-scale | 88 | agritech,biosecurity,water,soil | Draft EOI for SoilGuard + AquaGuard offline stack pilot | Grant lead | [link](opportunities/primary-sector-growth-fund.md) |
| CAT-G-004 | R&D Tax Incentive (RDTI) | IR / MBIE | **open** | Ongoing tax year | **15%** tax credit on eligible R&D | 85 | deeptech,r&d | Map eligible costs after New to R&D; book RDTI intro session | Finance | [link](opportunities/rdti.md) |
| CAT-G-005 | R&D Experience Grant | MBIE Innovation Services | **opens_soon** | Opens **2026-07-13 09:00 NZST** | Student intern ~10 weeks support | 80 | capacity,deeptech | Prep project brief + supervisor plan before open | Grant lead | [link](opportunities/rd-experience-grant.md) |
| CAT-G-006 | R&D Career Grant | MBIE Innovation Services | **opens_soon** | Opens **2026-08-31 09:00 NZST** | Up to **$30k** masters / **$35k** PhD (6 months) | 82 | capacity,ai,research | Define Aether / vision grad role | Grant lead | [link](opportunities/rd-career-grant.md) |
| CAT-G-007 | NZIAT AI Research Platform | MBIE / NZIAT | **watch** | Full funding from **Jul 2026**; final selection H1 2026 | Up to **$70m** over 7 years (platform) | 70 | ai,maori-data,research | Identify shortlisted OutdoorAI/BioAI partners; propose edge pilots | Grant lead | [link](opportunities/nziat-ai-platform.md) |
| CAT-G-008 | Māori Agribusiness / whenua funds | MPI MABx + Tupu.nz multi-fund | **researching** | Programme-dependent | Cluster / whenua dependent | 75 | maori,agritech,whenua | Search tupu.nz for Taranaki; engage MABx if cluster fits | Cultural Advisor | [link](opportunities/maori-agribusiness.md) |
| CAT-G-009 | Māori Climate Platform | MfE | **watch** | Stage 2 underway; watch Stage 3 | Stage 2 ~$7.25m across projects | 55 | maori,climate,marae | Only if marae resilience + edge energy/water stack | Cultural Advisor | [link](opportunities/maori-climate-platform.md) |
| CAT-G-010 | Callaghan wind-down services | Callaghan / MBIE transfer | **watch** | Org winds down through 2026 | N/A | 40 | transition | Prefer MBIE portals; do not build new Callaghan-only paths | Grant lead | [link](opportunities/callaghan-transition.md) |

---

## Internal capital (Kotahitanga)

Tracked separately from external grants (governance capital, not public grant applications):

| ID | Project | Tier | Budget | Compliance % | Status | Notes |
| :--- | :--- | :--- | ---: | ---: | :--- | :--- |
| KAS-2026-001 | Sovereign Regional Health Cloud (Weaver) | Diamond | $1.2M | 94 | ACTIVE | HITL capital + cultural review |
| KAS-2026-007 | Community Farm AI (Core/Aether) | Platinum | $300k | 88 | ACTIVE | Edge agritech flywheel |
| KAS-2026-008 | Regional Intelligence Hub (Stack) | Diamond | $400k | RED | FREEZE | Remediate before capital release |

Rules: see org README Kotahitanga section + compliance skill. **HITL mandatory** for allocations &gt;$50k.

---

## Declined / closed watchlist

| ID | Opportunity | Note |
| :--- | :--- | :--- |
| CAT-G-X01 | SFF Futures | **Closed** — replaced by PSGF (May 2025) |
| CAT-G-X02 | Endeavour Fund 2026 contestable | **Paused** during science system reforms; extensions only |

---

## Weekly update log

| Date | Change |
| :--- | :--- |
| 2026-07-13 | Initial tracker scaffold + research sweep (open NZ funds for Māori AI / deeptech / agritech / sovereign edge) |
| 2026-07-13 | Added [ROADMAP_TIMELINE.md](ROADMAP_TIMELINE.md) — phased todos + due dates for every capital path |

---

## How to update

1. Edit this table **and** `tracker.csv` (same IDs).  
2. Bump `last_verified` in the opportunity brief.  
3. If status → `submitted` / `awarded`, attach evidence path under `opportunities/evidence/` (private; do not commit secrets).  
4. Run `python scripts/score_fit.py` after product roadmap changes.
