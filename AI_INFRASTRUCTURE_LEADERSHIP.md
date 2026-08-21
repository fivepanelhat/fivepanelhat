# AI Infrastructure — Coastal Alpine Tech & Kiwi Edge AI Stack

**Claim tier: L1 Designed.** Preferred external frame: **[Safe NZ AI Stack Partner](./docs/SAFE_NZ_AI_STACK_PARTNER.md)**.

Coastal Alpine Tech is building a **sovereign, local-first AI stack for Aotearoa** — edge runtime, agent governance, and primary-sector portals designed so partners keep data, control, and accountability onshore.

We ship foundational layers — not only point solutions — so NZ organisations can run trustworthy, offline-capable, culturally aware AI without defaulting to always-on foreign cloud dependency.

## Stack partner positioning

The **Kiwi Edge AI Stack** (Coastal-Alpine-Core + Weaver + Aether + cat-agent-harness + Sovereign-Edge-Firmware + domain portals) is CAT’s **reference architecture** for sovereign edge AI infrastructure in primary industries and founder tooling:

- **Core infrastructure primitives**: SecurityGuard, DataFlywheel, TelemetryTracker, SovereignOllamaClient, portal_core — reusable across edge deployments.
- **Orchestration**: Weaver multi-tenant LangGraph mesh with isolation, local RAG, and HITL routing.
- **Agentic & companion layer**: Aether for ReAct orchestration, skills, computer-use (HITL-gated), and threat modeling.
- **Agent runtime**: cat-agent-harness — plugin-first composition under hard governance.
- **Hardware & runtime**: Canonical RPi 5 16GB + Hailo-10H, dual-platform (Win/Linux dev → edge prod), K3s/compose, mTLS MQTT field layer.
- **Sovereignty & safety posture**: aether-nz-ai-safety guidelines, Te Mana Raraunga operational controls, threat modeling, SOC 2–mapped *design* controls, fail-closed defaults.
- **Continuous improvement flywheel**: Local trajectories and human feedback without default exfiltration.

**Platform + beachhead**: One core platform (Core + Weaver + Aether + harness + stack) with **Byte-Size-Kai** as the agritech beachhead and Sting-Operation-AI as an ML pipeline on the same foundation.

This is infrastructure because it is:
- **Reusable & composable** across agritech, biosecurity, water/soil, founder tools, and future verticals
- **Hardened by design** — security roadmap, threat models, governance, CAT Architectural Standards (internal maturity targets, not external grades)
- **NZ-native posture** — Privacy Act 2020, Algorithm Charter spirit, Te Tiriti–aware design, OCAP-aligned intent
- **Rural & offline capable** — blackouts, low power, no cloud required for core operation
- **Hardware-aware** — performance-per-joule and edge constraints as first-class goals

## Hardening & safety (aether-nz-ai-safety applied)

**Core principles enforced**:
1. **Human authority** — Agents inform/draft/prepare/monitor/remind only. Humans advise/decide/sign/file/send/pay/actuate.
2. **Sovereignty first** — Local/on-device/NZ-resident by default. Owner-controlled keys. No silent exfiltration.
3. **Fail-closed & least privilege** — Default deny; SecurityGuard on model paths and high-impact actions.
4. **Transparency with purpose** — Structured audit trails; Algorithm Charter–aligned explanations where relevant.
5. **Cultural safety & Te Tiriti** — Bias mitigation and cultural review readiness for high-stakes paths.
6. **Risk-proportionate oversight** — L0–L4 gates per aether-hitl-protocol.
7. **Continuous assurance** — Grounding, red-team, outcome recording before promotion.
8. **Accountability** — Versioned policies and records for scrutiny.

**Anti-patterns we avoid**:
- Claiming certification or full Te Mana Raraunga compliance without evidence and agreements
- Agents as final authority without human gate
- Default cloud on sensitive or cultural workloads
- Skipping cultural review on high-stakes features

See: `.github/compliance/`, Aether `aether-nz-ai-safety`, `aether-hitl-protocol`, `te-mana-raraunga-controls`, `docs/SAFE_NZ_AI_STACK_PARTNER.md`.

## Why this matters for NZ

Primary industries, iwi, EDAs, and founders need AI they can trust on whenua — not only extractive cloud platforms. CAT ships stack layers designed for that context.

Pre-seed, focused on pilots, grants (MBIE, MPI, TPK, RDTI), and partners who value sovereignty, safety, and rural reality over hype.

**Contact**: fivepanelhat@gmail.com | Taranaki, Aotearoa New Zealand | github.com/fivepanelhat

*External claims remain L1 Designed unless a higher scorecard tier is founder-approved.*
