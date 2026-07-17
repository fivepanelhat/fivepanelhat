# NZ AI Frameworks Alignment — Kiwi Edge AI Stack (Coastal Alpine Tech)

**Status (July 2026)**: This document maps the Kiwi Edge AI Stack (Coastal-Alpine-Core, Weaver, Aether, Sovereign-Edge-Firmware, domain portals, DataFlywheel, SecurityGuard, HITL protocols) to current New Zealand AI frameworks and guidance. It demonstrates proactive alignment, hardening beyond minimums, and leadership in sovereign edge AI Infrastructure for primary industries and Aotearoa.

It builds on `aether-nz-ai-safety` (hardened operational guidelines) and complements existing artefacts: `THREAT_MODEL.md`, `SECURITY_ROADMAP.md`, `GOVERNANCE.md`, `AI_INFRASTRUCTURE_LEADERSHIP.md`, and `.github/compliance/nz-ai-compliance-soc2/`.

**Pre-seed honesty**: This is design-target alignment and internal hardening. No external certification or large-scale deployment is claimed.

## Key NZ AI Frameworks & Guidance (as of July 2026)

### 1. Public Service AI Framework (GCDO / digital.govt.nz)
- **Vision**: Adopt AI responsibly to modernise public services and deliver better outcomes for all New Zealanders.
- **5 Principles** (OECD-aligned): Inclusive & sustainable development; Human-centred values (privacy, human oversight, rights); Transparency & explainability; etc.
- **Policy Context**: Existing laws (Privacy Act 2020, Bill of Rights, Human Rights Act, Public Records Act, Public Service Act) + Te Tiriti o Waitangi / Māori views on AI ethics, bias, data.
- **6 Pillars of GCDO AI Work Programme**: Governance (human accountability, transparency); Guardrails (safe & trustworthy use); Innovation (safe pathways); Social Licence (public trust, worker engagement); Capability (internal/external, safety-by-design); Global Voice.
- **Related**: Public Service AI Toolkit (policy templates, records management for AI); Responsible AI Guidance for the Public Service: GenAI (safe, transparent GenAI use).

### 2. Algorithm Charter for Aotearoa New Zealand (data.govt.nz / evolving since 2020)
- Commitment to transparency, accountability, and human oversight for algorithms (especially high-risk/ high-impact ones).
- Focus on minimising unintended consequences, particularly for vulnerable communities; human review of significant decisions; stakeholder views; bias mitigation.
- Ongoing evolution for AI/LLM era; independent reviews and calls for stronger integration with Māori data safeguards, algorithm registers, and whole-of-government policy.
- Many agencies signed (e.g., IRD, Justice, Police).

### 3. National AI Strategy & MBIE Business Guidance (launched ~July 2025)
- **"Investing with Confidence"** strategy for businesses: agile, light-touch, principles-based (OECD AI Principles), technology-neutral regulation where possible. Existing laws (Privacy Act etc.) remain primary.
- **Responsible AI Guidance for Businesses**: Voluntary practical good practices for safe adoption, innovation, and risk management.

### 4. Māori Data Sovereignty & Te Tiriti Alignment
- **Te Mana Raraunga principles** (Rangatiratanga, Kaitiakitanga, Whakapapa, Manaakitanga, Kotahitanga): Data as taonga; Māori authority/control; collective benefit.
- **Te Kāhui Raraunga Māori AI Governance framework** (unveiled Oct 2025): Stronger safeguards for Māori data in AI — Māori involvement in decisions about collection/use/sharing of Māori data; bias monitoring; accountability; transparent algorithms; ability to exit/change systems; calls to strengthen Algorithm Charter and create independent monitoring + public algorithm register.
- Public Service Framework explicitly references Treaty of Waitangi and Māori views on AI ethics/bias/data.

### 5. Other Relevant
- OECD AI Principles (NZ Cabinet alignment since 2024).
- Privacy Act 2020 (primary data/AI law; IPPs, DSARs, retention, consent).
- Emerging: Ministry for Regulation "Responsible AI in Action" guidance (2026) for regulators; sector-specific rules (e.g., biosecurity, food, environment, health).

## Kiwi Edge AI Stack Alignment & Hardening

Our stack is designed as **sovereign edge AI Infrastructure** that exceeds baseline expectations by being offline-first, fail-closed, hardware-optimised for rural NZ, and deeply integrated with Te Mana Raraunga operational controls.

### Mapping Table (High-Level)

| Framework / Principle / Pillar | Kiwi Edge AI Stack Alignment & Hardening (Core | Weaver | Aether | Flywheel | SecurityGuard | HITL) |
|--------------------------------|-----------------------------------------------------------------------|
| **Public Service AI Framework Vision & Principles** | Full alignment via offline/local-first design (no default cloud exfil); human oversight non-negotiable (hard HITL L0–L4 gates); transparency via structured audit trails (prompts, decisions, overrides, trajectories); inclusive/sustainable (rural resilience, primary industry productivity, local jobs pathways); human-centred (privacy ethics, cultural safety, no silent automation of high-impact decisions). Exceeds via edge sovereignty + energy-aware telemetry. |
| **Governance Pillar** | `GOVERNANCE.md` + aether-hitl-protocol: Clear decision rights, HITL ceiling, Cultural Advisory interface, escalation. Human accountability enforced. No agent output treated as final authority. |
| **Guardrails Pillar** | `SECURITY_ROADMAP.md` + `THREAT_MODEL.md` (STRIDE for edge + multi-tenant + local-LLM); SecurityGuard on every model path & high-impact action (injection defence, screening); fail-closed defaults; least privilege; degrade safely on failure. Exceeds voluntary guidance with mandatory enforcement. |
| **Innovation & Capability Pillars** | Reusable primitives (Core SDK, DataFlywheel for continuous local improvement, SovereignOllamaClient); dual-platform (Win/Linux dev → RPi 5 + Hailo edge); skills architecture (`aether-core`, `aether-agent-fleet`, `aether-skill-authoring` + `aether-skills-ci`); safety-by-design baked in. Supports safe innovation for agencies/founders/primary sector. |
| **Social Licence & Transparency** | Algorithm Charter-aligned: High-risk paths (actuation, personal/Māori data, regulatory outputs) require elevated HITL + cultural review; explainable via audit views; stakeholder (iwi, whenua, community) considerations in design. Public algorithm-like transparency via open docs + proposed future register contribution. |
| **Algorithm Charter Commitments** | Human oversight for significant/high-impact decisions; bias mitigation via cultural safety reviews + red-teaming (prompt injection, cultural bias); transparency of high-risk uses; focus on vulnerable/rural communities (primary industries, whānau support). Evolving with Te Kāhui Raraunga calls (Māori involvement, exit rights, monitoring). |
| **Privacy Act 2020 & Data Ethics** | Local processing/storage by default; owner-controlled keys; explicit consent graphs; purpose limitation; DSAR-ready design; retention controls. No silent exfiltration. Exceeds via edge residency + Te Mana Raraunga operationalisation. |
| **Te Mana Raraunga / Māori AI Governance (Te Kāhui Raraunga)** | `aether-data-sovereignty` skill + operational controls: Rangatiratanga (Māori authority), Kaitiakitanga (guardianship), Whakapapa (provenance), Manaakitanga (care), Kotahitanga (collective benefit). Māori data treated as taonga; local custody; explicit involvement pathways in design/governance; bias safeguards; cultural advisory gates. Directly supports Te Kāhui Raraunga 2025 framework expectations. |
| **Responsible AI Guidance (GenAI / Business)** | Local-first preference (Ollama + Hailo); cloud only with justification + minimisation + documented flow; grounding/verification/red-teaming before promotion; human oversight for GenAI outputs used in decisions/actuation. Practical, production-ready implementation. |
| **National AI Strategy (Investing with Confidence)** | Supports safe, responsible innovation in primary industries & edge contexts; principles-based, technology-neutral where possible; builds confidence for NZ businesses/founders via hardened, sovereign infrastructure. |

### Global Regulatory Moat Extension (EU AI Act, ISO 42001, Sovereignty Quantification)

**Why this matters (July 2026 context):** Sovereign AI is shifting from cultural niche to global compliance requirement (EU AI Act full enforcement, US federal data-localisation hardening, Australia/Canada following). Enterprise buyers (hospitals, government contractors, agribusiness exporters) buy "procurement-passable" systems, not just "local on Pi".

**Our Position:** The Kiwi Edge Stack already exceeds NZ baselines. We extend it to global standards as a **sellable compliance primitive**.

- **EU AI Act Annex III (High-Risk Systems) Mapping**: SecurityGuard + hard HITL gates + audit trails + risk-tiered oversight directly support high-risk requirements (human oversight, transparency, accuracy, robustness, cybersecurity). Local processing reduces data transfer risks under Chapter V (international transfers).
- **ISO 42001 (AI Management Systems) Self-Assessment**: Our `GOVERNANCE.md`, `aether-nz-ai-safety`, Security Roadmap, Threat Model, and skills CI provide strong coverage of leadership, risk management, continual improvement, and internal audit. Gap analysis shows readiness for formal certification post-pilot.
- **Sovereignty Scorecard (Core primitive)**: 
  - **Latency**: Sub-100ms local inference vs. 200-800ms+ round-trip to nearest AWS/GCP region for typical agritech queries.
  - **Egress Cost Avoidance**: 100% local data flywheel = $0 cloud egress for continuous improvement loops (vs. significant per-GB costs at scale for vision + telemetry).
  - **Jurisdiction Risk**: NZ-resident processing + owner-controlled keys + explicit consent = materially lower GDPR Article 44 / Schrems-style transfer risk and EU AI Act third-country concerns.
  - **Quantified Moat**: For identical workloads, edge-local stack eliminates ongoing API inference bills and data-residency compliance overhead that kill unit economics in agriculture/logistics at scale.

SecurityGuard is positioned as the **enforceable compliance layer** — not just engineering guardrails. This turns sovereign edge into a procurement advantage for regulated buyers.

### Open-Weight Models & Hardware Co-Design (2026 Enterprise Defaults)

Enterprise buyers increasingly prefer **ownable weights** (Llama 3.2, Qwen 2.5, Mistral Small, DeepSeek) over rented APIs for data residency, cost predictability, and customisation.

**Our Approach:**
- Validated model cards + benchmarks (tokens/sec, power draw, accuracy) on canonical RPi 5 16GB + Hailo-10H target for Qwen2.5-7B, Llama-3.2-3B, Mistral-Small, plus domain-specific distillation experiments from agritech corpus.
- Hardware co-design: Hailo-10H compiled artefacts (.hef where applicable), POWER_BUDGET.md (system draw under load), thermal throttling characterisation for NZ summer greenhouse conditions. Generic PyTorch = commodity; NPU-optimised + quantised = moat.

These directly support the Public Service Framework "Guardrails" and "Capability" pillars and ISO 42001 continual improvement.

### How We Go Beyond Baseline (Leadership Differentiators)
- **Fail-Closed & Least Privilege by Default**: Not just recommended — enforced via SecurityGuard + HITL gates across all paths.
- **Edge Sovereignty & Offline Resilience**: Designed for rural blackouts and Te Mana Raraunga data residency — stronger than typical cloud-centric public service guidance.
- **Continuous Local Improvement (DataFlywheel)**: Trajectories + human feedback + golden sets stay local; turns every deployment into safer, better infrastructure without central data lakes.
- **Cultural Partnership Operationalised**: Not aspirational — `aether-data-sovereignty` + Cultural Advisory in Governance + risk-tiered cultural reviews for High/Critical items.
- **Skills-Native Extensibility**: Production authoring standards (`aether-skill-authoring`) ensure new capabilities inherit hardening, HITL, and NZ framework alignment.
- **Hardware-Aware & Energy Optimised**: Sub-10W rural nodes; joules/tokens telemetry — supports sustainable/resilient development principle.

### Anti-Patterns We Explicitly Avoid (per aether-nz-ai-safety)
- Treating voluntary guidance as sufficient without mandatory controls.
- Claiming alignment (Algorithm Charter, Te Mana Raraunga, Framework) without auditable, enforced mechanisms.
- Defaulting to cloud for sensitive/cultural workloads.
- Allowing agents to present outputs as authoritative without human gate.
- Skipping cultural review or impact assessment for high-stakes or novel uses.

## Recommendations & Next Steps (Internal Roadmap)
1. **Deepen Mapping**: Expand this doc with detailed control-level mapping to the 225-item SOC2 matrix and specific Framework pillars (ongoing in `.github/compliance/nz-ai-compliance-soc2/`).
2. **Algorithm Register Contribution**: Design future open contribution path for high-risk algorithms/paths (supports Charter evolution + Te Kāhui Raraunga calls).
3. **Pilot Alignment Evidence**: For first paid pilots, produce evidence pack mapping stack controls to Framework/Charter/Privacy Act + emerging global (EU AI Act / ISO 42001) requirements (HITL logs, audit trails, cultural review records).
4. **Skills Expansion**: Author new infra skills (orchestration governance, flywheel curation, hardware posture) using `aether-skill-authoring` + full nz-ai-safety checklist.
5. **External Engagement**: Share hardened approach with Venture Taranaki, iwi partners (e.g., Muaūpoko), EDAs, and GCDO/MBIE as relevant for sovereign edge use cases in primary industries.
6. **Continuous Review**: Revisit this alignment quarterly or on major Framework/Charter updates; gate via HITL (founder + Cultural Advisory for material claims).

## References & Sources
- Public Service AI Framework & Toolkit: digital.govt.nz (July 2026)
- Responsible AI Guidance for the Public Service: GenAI: digital.govt.nz
- Algorithm Charter for Aotearoa New Zealand: data.govt.nz (evolving)
- National AI Strategy "Investing with Confidence" & Business Guidance: MBIE (2025)
- Te Kāhui Raraunga Māori AI Governance framework (2025)
- Te Mana Raraunga principles & aether-data-sovereignty
- aether-nz-ai-safety, aether-hitl-protocol, cat-architectural-standards (Diamond target)
- Existing CAT compliance artefacts (Threat Model, Security Roadmap, Governance)
- EU AI Act, ISO 42001, and global sovereign AI trends (2026 context)

**This alignment positions Coastal Alpine Tech as a trusted sovereign AI Infrastructure partner for Aotearoa — ready for responsible pilots, grants, and collaboration that respects people, whenua, and the frameworks that protect them (NZ and emerging global).**

*Document owned by Coastal Alpine Tech Limited. Updates require founder + appropriate cultural/HITL approval.*
