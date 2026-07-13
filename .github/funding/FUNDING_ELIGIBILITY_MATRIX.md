# Funding Eligibility Matrix — Coastal Alpine Tech (CAT)

**Version:** 1.0.0 · **Date:** 2026-07-13  
**Purpose:** Score the **likelihood / possibility** of securing grants, non-dilutive co-funding, and early **seed** capital based on narrative strength, market size (TAM/SAM/SOM), traction, and funder prerequisites.  
**Companion:** [INVESTOR_MATRIX.md](INVESTOR_MATRIX.md) (equity VC / angels / founders)  
**Machine table:** [matrices/eligibility_matrix.csv](matrices/eligibility_matrix.csv)

> **Disclaimer:** Analytical planning tool only — not financial, legal, or investment advice. Likelihood bands are **judgment scores** (0–100) under stated assumptions, not predictions. Re-verify every funder rule before applying. Public comps (Halter, Sharesies, Cursor/Anysphere) are **illustrative patterns**, not valuation claims for CAT.

---

## 1. How to read this matrix

| Band | Likelihood | Meaning |
| ---: | :--- | :--- |
| **80–100** | **High** | Prerequisites largely met or cheap to meet; strong narrative fit |
| **60–79** | **Medium–High** | Pursue with clear gap-closure plan (3–9 months) |
| **40–59** | **Medium** | Possible with partners, pilots, or entity/structure work |
| **20–39** | **Low** | Structural blockers (eligibility, traction, or thesis mismatch) |
| **0–19** | **Unlikely now** | Wrong stage / wrong capital type |

**CAT stage assumption (2026-07):** **Pre-seed startup.** Product architecture + multi-repo stack public; compliance skill pack as design targets; limited/no disclosed commercial ARR; hardware target clear (RPi 5 16GB + Hailo-10H); Taranaki HQ. Adjust scores when ARR, pilots, or entity facts change.

---

## 2. CAT narrative spine (what funders must hear)

| Narrative pillar | CAT claim (truth-constrained) | Proof artefacts |
| :--- | :--- | :--- |
| **Problem** | Rural NZ primary industries face connectivity blackouts, biosecurity pressure, nutrient/water regulation, and cloud AI that exports data offshore | Domain portal READMEs; MPI/reg context |
| **Solution** | Offline-native multi-modal edge agents on sovereign hardware; local LLM + vision NPU | Architecture map; Core/Weaver/Aether/stack |
| **Why now** | NZ AI platform investment; Privacy Act + Te Mana Raraunga scrutiny; agritech global leaders (e.g. Halter) prove NZ can scale field systems | NZIAT AI platform; compliance pack |
| **Moat path** | Hybrid edge stack + domain portals + compliance-as-code + data flywheel (Platinum) | CAT standards; skills registry |
| **Not claimed** | SOC 2 Type II certified; unicorn ARR; iwi partnership without named kaitono | Explicit honesty in proposals |

---

## 3. Market sizing frame (TAM / SAM / SOM) for CAT

Investors and many grant assessors expect **bottom-up** market thinking (customer counts × willingness to pay), not only top-down Gartner slides. Seed-scale VC typically wants a credible path toward large markets (often **$1B+ TAM** framing for venture-scale theses).

### 3.1 Illustrative CAT market stack (directionally; refine with finance)

| Layer | Definition | Illustrative CAT framing | Notes |
| :--- | :--- | :--- | :--- |
| **TAM** | Global precision ag + edge AI for primary industries + offline enterprise AI agents | Multi-tens-of-billions USD long-term (precision ag + industrial edge AI combined) | Must not overstate “own the whole market” |
| **SAM** | English-speaking / Commonwealth farms + NZ/AU/Pacific agribusiness + sovereign gov/enterprise edge | NZ+AU primary digital spend + select export markets | Halter-scale comps show NZ field systems can go global |
| **SOM (3–5 yr)** | Paying edge nodes + portal subscriptions for water/soil/biosecurity/cultivation + SDK licenses | Bottom-up: *N* farms × $X/node/year + *M* enterprise seats | **Required for seed narrative** |

### 3.2 Bottom-up SOM sketch (fill numbers before pitch)

```text
SOM = (pilot farms × ARR/farm) + (enterprise seats × ARR/seat) + (SDK OEM deals)
     + hardware margin (optional) + services (setup, compliance packs)
```

| Driver | Example inputs to validate | Risk if missing |
| :--- | :--- | :--- |
| Price / edge node | $Y/year SaaS + hardware attach | Grant-only product perception |
| Farms addressable | Regional council catchments, dairy/beef/hort clusters | Abstract “all NZ farms” |
| Expansion | AU then US/Pacific (Halter path pattern) | NZ-only ceiling for VC |
| Expansion (software) | Developer / agent seats (Cursor path pattern) | Hardware-only low multiples |

### 3.3 Comps: how markets were *sold* (public patterns)

| Company | Market story pattern | Relevance to CAT |
| :--- | :--- | :--- |
| **Halter** (NZ) | Field hardware + software network effects on livestock ops; global ranch expansion; not “small NZ niche” | Agritech edge + NZ origin → global VC (Founders Fund, BOND, Bessemer, Icehouse, Blackbird) |
| **Sharesies** (NZ) | Democratise investing; massive local penetration → AU expansion; consumer + wealth platform | NZ product-market density + trust; less analogous to CAT B2B edge |
| **Cursor / Anysphere** (US) | AI-native developer tool; extreme revenue velocity / category defining | Software agent + AI narrative; CAT’s **Aether** is related *category*, not same GTM |

Sources (public reporting): Halter Series D/E coverage (e.g. company announcements, AgFunder News, Generate/Icehouse commentary); Sharesies raise history (company blog / NZ press); Cursor/Anysphere round reporting (CNBC, Crunchbase News, company blog). See [INVESTOR_MATRIX.md § comps](INVESTOR_MATRIX.md#5-public-comps-relevant-to-cat).

---

## 4. Universal prerequisite checklist (all capital types)

Score each **0–2** (0 = missing, 1 = partial, 2 = solid). Max **24**.

| # | Prerequisite | Investors care | Grant funders care | CAT default (Jul 2026) | Score |
| ---: | :--- | :---: | :---: | :--- | ---: |
| 1 | **Legal entity** fit for instrument | ✓ | ✓ | Confirm NZ company / eligible structure | 1 |
| 2 | **Clear problem + technical uncertainty** | ✓ | ✓ (R&D) | Strong offline/sovereign edge thesis | 2 |
| 3 | **Team / domain credibility** | ✓ | ✓ | Fill named leads + advisors | 1 |
| 4 | **Product / prototype evidence** | ✓ | ✓ | Public multi-repo stack | 2 |
| 5 | **Traction** (pilots, LOIs, revenue) | ✓✓ | medium | Likely weak unless pilots disclosed | 0–1 |
| 6 | **TAM/SAM/SOM + unit economics sketch** | ✓✓ | medium | Needs bottom-up pack | 1 |
| 7 | **Go-to-market** (who buys, sales motion) | ✓✓ | low–med | Domain portals defined; sales motion TBD | 1 |
| 8 | **Data / IP / moat story** | ✓ | medium | Architecture + compliance as moat path | 2 |
| 9 | **Regulatory / sovereignty narrative** | niche VC | **high** (NZ public) | Strong CAT differentiator | 2 |
| 10 | **Financial readiness** (books, co-fund, runway) | ✓ | ✓ (co-fund) | Must prepare cashflow packs | 1 |
| 11 | **HITL / governance** for high-risk claims | impact / ESG | **high** | Skills + compliance pack | 2 |
| 12 | **Honest stage labeling** | ✓ | ✓ | No false SOC 2 cert claims | 2 |

**Interpretation:** Grants can fund **capability** before full traction; equity seed still discounts heavily without pilots/revenue path.

---

## 5. Capital-type eligibility matrix (CAT)

Likelihood = composite of **fit** (narrative/market) × **readiness** (prerequisites) × **process openness**.

| Capital type | Instrument | Best CAT use-case | Key prerequisites | Likelihood (now) | 6–12 mo upside if gaps closed | Blockers |
| :--- | :--- | :--- | :--- | ---: | ---: | :--- |
| **MBIE New to R&D** | Grant co-fund 40% ≤$400k | Core/Weaver/Aether R&D uncertainty | New-to-R&D eligibility; 60% private co-fund; capability skills | **82** | **90** | R&D spend history; cash co-fund |
| **MPI PSGF** | Co-invest primary sector | SoilGuard / AquaGuard / Sting pilots | EOI; co-invest; economic benefit; farm partners | **75** | **88** | Pilot farms; multi-month process |
| **TPK Māori Development Fund** | Grant / investment | Whenua productivity + Māori outcomes | Regional office first; kaitono entity; ROI evidence | **48** | **72** | Without real Māori-led partnership → low |
| **RDTI** | 15% tax credit | Ongoing eligible R&D | Eligible expenditure systems | **70** | **85** | Not cash; needs cost capture |
| **R&D Experience / Career** | Wage-style grant | Capacity for vision/agent eval | Opens Jul/Aug 2026; student/grad plan | **72** | **80** | Timing windows |
| **NZIAT AI platform** | Partner / subcontract | Edge deployment partner to platform | Host selection; relationship | **45** | **70** | Not CAT as host; partner motion |
| **MABx / whenua multi-fund** | Programme / multi-grant | Cluster tech partner | Relationships; region filters | **50** | **75** | Cultural pathway required |
| **Angel / pre-seed equity** | SAFE / equity | GTM + pilots + team | Story + team + early proof | **55** | **75** | Traction thin for pure software VC |
| **NZ seed VC** (Icehouse, Blackbird-adjacent, Outset/deeptech, NZGCP Aspire-type) | Equity | Scale agritech+AI wedge | Venture-scale path; NZ deeptech fit | **50** | **78** | ARR / pilot density |
| **Global agritech VC** | Equity | Halter-class field scale | Multi-country field proof | **25** | **55** | Too early; need scale metrics |
| **Global AI pure-play VC** | Equity | Cursor-class agent velocity | Explosive product usage metrics | **20** | **45** | Wrong metric profile today |
| **Strategic corporate** (ag/telco/cloud NZ) | Equity / pilot $ | Distribution | Procurement path | **40** | **65** | Long sales cycles |
| **Internal Kotahitanga** | Planning only (pre-seed) | Stack completion goals | No real multi-M budgets; HITL before any real capital | **planning** | — | Do not invent ACTIVE funded rows |
| **Crowdfunding / retail** | Equity crowdfund | Brand | Not primary CAT path | **15** | **25** | Dilution / focus risk |

### 5.1 Likelihood heatmap (quick view)

```text
                Narrative fit   Market story   Traction   Process open   Likelihood
New to R&D           ███            ██           ░░           ███           High
PSGF                 ███            ███          ░░           ██            Med-High
MDF                  ██*            ██           ░            ██            Med*
RDTI                 ███            █            █            ███           Med-High
Angel pre-seed       ███            ██           ░            ██            Medium
NZ seed VC           ███            ██           ░            ██            Medium
Global agritech VC   ███            ███          ░            █             Low now
Global AI VC         ██             ███          ░            █             Low now
* only with authentic Māori partnership pathway
```

---

## 6. Dimension deep-dive: what moves likelihood

### 6.1 Narrative quality (weight high for grants + angels)

| Element | Weak | Strong (CAT target) |
| :--- | :--- | :--- |
| Problem specificity | “AI for farms” | Offline decisions under blackout + regulation lockouts |
| Technical uncertainty | Feature list | “Competent professional cannot ship multi-modal offline + tenant isolation + TMR residency yet” |
| Differentiation | Another RAG wrapper | Edge hardware + domain portals + compliance skills + hybrid Win/Linux→RPi |
| Trust | Buzzwords | Te Mana Raraunga, HITL, honest compliance roadmap |
| Founder story | Generic | Taranaki / whenua / primary industries presence |

### 6.2 TAM / market (weight high for equity)

| Signal | Funder reaction |
| :--- | :--- |
| Top-down only “$50B agtech market” | Discounted — shows slide literacy not customer math |
| Bottom-up SOM with named segments | Credible seed conversation |
| NZ-only ceiling with no export path | Caps valuation thesis (contrast Halter multi-country collars) |
| Pure grant-funded forever | Equity investors walk |

### 6.3 Traction ladder (weight high for seed+)

| Level | Evidence | Effect on equity likelihood |
| :--- | :--- | :--- |
| L0 | Public repos only | Grants OK; equity hard |
| L1 | Design partners LOIs | Angels possible |
| L2 | Paid pilot / paid PoC | Seed conversations open |
| L3 | Repeatable ARR / multi-farm | Series A prep (agritech often looks for ~$1M ARR or strong repeat sales at A) |
| L4 | Multi-geo scale | Global agritech / growth VC |

### 6.4 Team & co-founder signals (weight high early)

| Signal | Why |
| :--- | :--- |
| Complementary skills (edge/ML, GTM, domain farming/reg) | Reduces execution risk |
| Full-time commitment clarity | Angels/VCs underwrite people |
| Advisory (iwi, farm, CISO) | CAT sovereignty thesis credibility |
| Clean equity / IP ownership | Dilution and assignment hygiene |

See founder/investor expectations in [INVESTOR_MATRIX.md](INVESTOR_MATRIX.md).

### 6.5 Regulatory / ESG / sovereignty (CAT’s asymmetric advantage)

Public NZ funds and impact-oriented capital **pay for** Privacy Act, Te Mana Raraunga, Algorithm Charter, and rural resilience narratives. Pure growth equity may treat this as “nice” unless it **blocks competitors** (data cannot leave farm → switching costs / trust moat).

---

## 7. Path-dependent strategies (recommended sequence)

```text
Phase 0 (0–3 mo)   Non-dilutive: New to R&D + RDTI setup + Experience grant prep
                   → Buy R&D capacity without selling equity
Phase 1 (3–9 mo)   PSGF EOI + 2–3 paid/structured pilots + bottom-up SOM pack
                   → Convert architecture into field proof
Phase 2 (6–12 mo)  Angel / NZ seed with pilot metrics + export narrative
                   → Only after L1–L2 traction
Phase 3 (12–24 mo) Larger equity if multi-farm ARR + AU beachhead
                   → Halter-pattern field scale (different product, same NZ→global logic)
Parallel           MDF/MABx only via authentic partnership; NZIAT as edge partner
```

**Do not** reverse: seeking global AI VC (Cursor comps) before product usage metrics will destroy narrative credibility.

---

## 8. Scoring worksheet (per opportunity)

Copy for each fund/investor:

| Factor (0–10) | Weight | Score | Weighted |
| :--- | ---: | ---: | ---: |
| Eligibility match | 15% | | |
| Narrative / problem fit | 15% | | |
| Market / TAM credibility | 15% | | |
| Traction / proof | 20% | | |
| Team readiness | 10% | | |
| Co-fund / dilution terms acceptable | 10% | | |
| Process timing / openness | 10% | | |
| Sovereignty / compliance alignment | 5% | | |
| **Total** | 100% | | **/100** |

Band using §1. Update [FUNDING_TRACKER.md](FUNDING_TRACKER.md) `fit_score` when this moves ≥10 points.

---

## 9. Red flags that kill eligibility (any capital)

- Claiming **SOC 2 Type II certified** without audit  
- Token Māori branding without kaitono consent  
- Cloud-only architecture contradicting “sovereign offline” pitch  
- Co-funding New to R&D 60% with other NZ public money  
- No owner for sales/pilots (pure eng hobby)  
- Cap table / IP not assignable to the raising entity  

---

## 10. Maintenance

| Cadence | Action |
| :--- | :--- |
| Monthly | Re-score likelihood column with latest pilots/ARR |
| Per grant open | Run §8 worksheet → tracker |
| After major product ship | Refresh narrative spine + SOM |

**Owner:** Grant lead + Finance · **HITL:** Cultural Advisor for any Māori-outcome claims  

**Related:** [FUNDING_GUIDE.md](FUNDING_GUIDE.md) · [ROADMAP_TIMELINE.md](ROADMAP_TIMELINE.md) · [grants-agent/SKILL.md](grants-agent/SKILL.md) · [knowledge-base/portfolio-fit.md](knowledge-base/portfolio-fit.md)
