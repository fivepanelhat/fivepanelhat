# Governance – Coastal Alpine Tech

**Company:** Coastal Alpine Tech Limited  
**Stage:** Pre-seed (New Plymouth, Taranaki, Aotearoa New Zealand)  
**Last updated:** July 2026

This document is the single top-level reference for how decisions are made, who holds authority, and how human oversight is enforced across the Kiwi Edge AI Stack.

---

## 1. Core Autonomy Ceiling (Non-negotiable)

**Agents inform, draft, prepare, monitor, and remind.**  
**Humans advise, sign, file, send, and pay.**

No agent may autonomously:
- Commit capital or move money
- File government forms or make regulatory submissions
- Send external communications that bind the company
- Approve cultural data uses involving Māori data
- Bypass SecurityGuard or HITL gates on high-impact actions

This ceiling is enforced in Aether, agent-fleet policies, and the Technical Moat description.

---

## 2. Decision Rights

| Decision Type | Authority | Notes |
|---------------|-----------|-------|
| Product & architecture direction | Founder / CEO | Day-to-day |
| Security control changes | Founder (Security Lead) | Must not weaken fail-closed defaults |
| High-impact agent actions | Human approver (HITL) | Required by policy |
| Capital allocation / fundraising | Founder / future Board | Kotahitanga principles apply |
| Māori / cultural data use | Founder + Cultural Advisory (when formed) | Te Mana Raraunga / OCAP |
| Compliance policy changes | Founder + Compliance Officer (designate) | |
| Public claims about readiness | Founder | Must remain stage-honest |

---

## 3. Roles (Current Pre-seed Reality)

| Role | Current Holder | Responsibility |
|------|----------------|----------------|
| Founder / CEO | Wayne Roberts | Overall accountability, product, capital, cultural interface |
| Security Lead | Founder | Threat model, SecurityGuard, SecOps, device posture |
| Compliance Officer | Designate (Founder until appointed) | Checklist ownership, Privacy Act, incident coordination |
| Cultural Advisor / Board | To be formed | Te Mana Raraunga decisions, data use agreements |
| Technical contributors | Open (public repos) | Code under review; no automatic write access to production paths |

As the company grows, these roles will be separated. Until then, the Founder holds multiple hats and is explicitly accountable for the resulting concentration of risk.

---

## 4. Human-in-the-Loop (HITL) Gates

High-risk actions require explicit human approval. Examples:
- Actuator commands that affect physical systems
- Export or movement of trajectory / golden-set data off-node
- Changes to tenant isolation or security policy
- Any use of data classified under Te Mana Raraunga Level 2 or 3
- External communications that could create legal or cultural obligations

Aether and the agent-fleet skills implement these gates. Circumvention is a policy violation.

---

## 5. Cultural & Data Sovereignty Governance

- All work involving Māori data or whenua-derived operational data is subject to Te Mana Raraunga principles (Ownership, Control, Access, Possession).
- No automatic cloud exfiltration of such data.
- Formal Cultural Advisory Board will be established before any scaled use of Level 2/3 cultural data.
- Until the Board exists, the Founder is personally accountable for any such decisions and must document them.

See: [Te Mana Raraunga Principles](.github/compliance/nz-ai-compliance-soc2/references/TE_MANA_RARAUNGA_PRINCIPLES.md)

---

## 6. CAT Architectural Standards (Internal Maturity Model)

These are **design targets**, not external certifications:

- **Diamond** — Security, observability, deployment hardening
- **Platinum** — Continuous improvement + data flywheel
- **Gold** — Workflow-native design with transparent HITL gates

Progress against these targets is tracked in the compliance skill and Security Roadmap.

---

## 7. Escalation & Incident Paths

| Situation | Primary Contact | Escalation |
|-----------|-----------------|------------|
| Suspected security incident | Security Lead (Founder) | Immediate |
| Privacy / data subject request | Compliance Officer | Within SLA |
| Cultural / Māori data concern | Founder → Cultural Advisory (when formed) | Before any action |
| Agent policy violation | Founder | Immediate review |
| Public claim that overstates readiness | Founder | Correct within 24 h |

Detailed playbooks live under `.github/compliance/nz-ai-compliance-soc2/references/`.

---

## 8. Related Documents

- [Security & Compliance Roadmap](.github/compliance/SECURITY_ROADMAP.md)
- [Threat Model](.github/compliance/THREAT_MODEL.md)
- [NZ AI Compliance + SOC 2 Skill](.github/compliance/nz-ai-compliance-soc2/SKILL.md)
- [Agent Fleet / HITL Policy](.github/agent-fleet/AGENTS.md)
- [Anti-hallucination Policy](.github/agent-fleet/anti-hallucination.md)
- [Technical Moat](https://github.com/fivepanelhat/fivepanelhat#technical-moat)
- [CAT Congruence](CAT_CONGRUENCE.md)

---

*This governance document is reviewed at least quarterly or after any material change in team, architecture, or regulatory exposure.*
