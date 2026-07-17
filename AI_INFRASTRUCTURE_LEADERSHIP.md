# AI Infrastructure Leadership — Coastal Alpine Tech & Kiwi Edge AI Stack

**Coastal Alpine Tech is pioneering and leading New Zealand's sovereign AI Infrastructure for production edge systems and primary industries.**

We ship the foundational layers — not point solutions — so Aotearoa can run trustworthy, offline-first, culturally aligned AI without foreign cloud dependency or cultural risk.

## Leadership Positioning

The **Kiwi Edge AI Stack** (Coastal-Alpine-Core + Weaver + Aether + Sovereign-Edge-Firmware + domain portals) is New Zealand's reference implementation for sovereign edge AI Infrastructure:

- **Core Infrastructure Primitives**: SecurityGuard (input/output screening, injection defence), DataFlywheel (local trajectories + human feedback + golden sets), TelemetryTracker (energy/joules/tokens), SovereignOllamaClient, portal_core — reusable across any edge deployment.
- **Orchestration Infrastructure**: Weaver multi-tenant LangGraph mesh with strict isolation, local RAG, and HITL routing.
- **Agentic & Companion Layer**: Aether for ReAct orchestration, skills, computer-use (HITL-gated), and threat modeling — the "control plane" for agent fleets.
- **Hardware & Runtime Infrastructure**: Canonical RPi 5 16GB + Hailo-10H NPU target, dual-platform (Win/Linux dev → edge prod), K3s/compose orchestration, mTLS MQTT field layer.
- **Sovereignty & Safety Infrastructure**: aether-nz-ai-safety hardened guidelines, Te Mana Raraunga operational controls, full threat modeling, SOC2-mapped compliance as code, fail-closed defaults.
- **Continuous Improvement Flywheel**: Local data loops that improve models and decisions over time without exfiltration — turning every farm/node into infrastructure value.

**Platform + Beachhead Narrative**: We built **one core platform** (Core + Weaver + Aether + stack) that powers sovereign edge AI. **Byte-Size-Kai** is the first validated beachhead application (microgreens / Mana Kai agritech). Sting-Operation-AI is the first ML pipeline. Everything else is scaffolding or future modules on the same foundation. This is the winning 2026 structure: platform engine + focused wedge that proves the engine works.

This is infrastructure because it is:
- **Reusable & Composable**: Same Core/Weaver/Aether powers agritech (Byte Size Kai), biosecurity (Sting), water/soil (AquaGuard/SoilGuard), founder tools (NZ-Start-Up), and future verticals.
- **Production-Grade Hardened**: Not prototypes — Security & Compliance Roadmap, Threat Models, Governance, Diamond-level CAT Architectural Standards.
- **NZ-Native & Culturally Safe**: Privacy Act 2020, Algorithm Charter, Public Service AI Framework, Te Tiriti partnership, OCAP-aligned data control.
- **Rural & Offline Resilient**: Designed for blackouts, low-power, no cloud required for core operation.

**We are the sovereign AI Infrastructure layer for Aotearoa's primary industries and edge future.**

## Hardening & Safety (aether-nz-ai-safety Applied)

All work follows hardened NZ AI safety (see full skill for details):

**Core Principles Enforced**:
1. **Human Authority Non-Negotiable** — Agents inform/draft/prepare/monitor/remind only. Humans advise/decide/sign/file/send/pay/actuate. No agent output treated as final authority (hard HITL gates L0–L4 per aether-hitl-protocol).
2. **Sovereignty First** — Local/on-device/NZ-resident by default. Owner-controlled keys. Explicit consent graphs. No silent exfiltration. Māori data/knowledge as taonga (aether-data-sovereignty).
3. **Fail-Closed & Least Privilege** — Default deny. SecurityGuard on every model path and action. Degrade to safe deterministic behaviour on failure.
4. **Transparency with Purpose** — Structured audit trails for prompts, tool calls, decisions, human overrides. Meaningful explanations aligned with Algorithm Charter.
5. **Cultural Safety & Te Tiriti** — Active bias mitigation, Te Ao Māori perspectives in design/eval, operational partnership.
6. **Risk-Proportionate Oversight** — Tiered gates: Low (L0/L1 logging), Medium (L2 approval), High (L2/L3 + cultural), Critical/Novel (L3/L4 + impact assessment + founder gate).
7. **Continuous Assurance** — Grounding checks, red-teaming (prompt injection, cultural bias, escalation), outcome recording before promotion.
8. **Accountability** — Clear ownership, versioned policies, records for regulatory/cultural/legal scrutiny.

**Mandatory Technical Controls in Stack**:
- SecurityGuard (or equiv) before every model invocation and high-impact action.
- Hard HITL stops for actuation, data export, model updates, computer-use, regulatory outputs.
- Local-first preference (Ollama + Hailo); cloud only with justification + minimisation + documented flow.
- Strict tenant isolation + data classification.
- Adversarial testing + cultural safety review for High/Critical paths.
- Full structured logging with human-readable views.

**Risk Tiering in Practice** (examples from stack):
- Low: Internal research, non-personal drafting → L0/L1 + basic guards.
- Medium: Tenant recommendations, operational insights → L2 explicit approval.
- High: Actuation (fertigation, biosecurity alerts), personal/Māori data, compliance outputs → L2/L3 + multi-review + cultural check.
- Critical: New model classes, cross-border, high-stakes autonomous loops → L3/L4 + formal assessment + external advisory.

**Anti-Patterns We Explicitly Avoid**:
- Treating voluntary NZ guidance as sufficient without enforcement.
- Claiming alignment (Te Mana Raraunga, Algorithm Charter) without concrete, auditable controls.
- Allowing agents to present as authoritative without human gate.
- Defaulting to cloud for convenience on sensitive or cultural workloads.
- Skipping impact assessment or cultural review for high-stakes features.
- Logging full personal/cultural prompts without minimisation.

See implementation in:
- `.github/compliance/SECURITY_ROADMAP.md` & `THREAT_MODEL.md`
- `aether-nz-ai-safety` skill (full guidelines + checklist)
- `aether-hitl-protocol`, `aether-data-sovereignty`, `cat-architectural-standards` (Diamond target)
- SecurityGuard patterns across Core/Weaver/Aether
- `.github/compliance/NZ_AI_FRAMEWORKS_ALIGNMENT.md` (detailed mapping including global regulatory moat)

## Skills Architecture & Extensibility

The infrastructure is skills-native (powered by aether-core + aether-agent-fleet + aether-skill-authoring).

Current hardened skills include: agent-hardening, compliance-registrar, data-sovereignty, hitl-protocol, nz-ai-safety, cat-architectural-standards, and domain-specific (grants, market, finance, etc.).

We are actively expanding the fleet with AI Infrastructure-specific skills for:
- Orchestration & routing governance
- Flywheel curation & golden-set management
- Hardware posture & energy optimisation
- Cross-portal infrastructure monitoring
- Sovereign deployment automation

New skills follow production authoring standards (frontmatter, progressive disclosure, HITL integration, cultural safety, tests).

**GitHub Topics for Discoverability**: edge-ai, sovereign-ai, ai-infrastructure, raspberry-pi, hailo, langgraph, hitl, te-mana-raraunga, data-sovereignty, new-zealand-agritech, biosecurity, compliance

## Why This Matters for NZ

Primary industries, iwi, EDAs, and founders need AI they can trust on whenua — not extractive cloud platforms. We are shipping the hardened, local infrastructure to make that possible at scale.

Pre-seed, focused on pilots, grants (MBIE, MPI, TPK, RDTI), and strategic partners who value sovereignty, safety, and real rural impact over hype.

**Contact & Collaborate**: fivepanelhat@gmail.com | Taranaki, Aotearoa New Zealand | github.com/fivepanelhat

*This document is part of our commitment to transparent, hardened, leadership-grade AI Infrastructure.*
