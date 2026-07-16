# Security & Compliance Roadmap

**Coastal Alpine Tech Limited**  
**Stage:** Pre-seed (as of July 2026)  
**Status:** Design targets + working controls. Not yet externally audited.

This roadmap is deliberately stage-honest. It shows what exists today, what will be completed before first paid pilots, and what is required for seed / early enterprise conversations. It does **not** claim SOC 2 Type II certification or full enterprise readiness.

---

## Guiding Principles

1. **Fail-closed by default** — Security and sovereignty controls prefer denial over silent failure.
2. **Local-first** — Data and inference stay on the node unless the owner explicitly moves them.
3. **HITL for high-impact actions** — Agents inform, draft, prepare, monitor, and remind. Humans advise, sign, file, send, and pay.
4. **Te Mana Raraunga alignment** — Māori data sovereignty (OCAP) is a first-class design constraint, not an afterthought.
5. **Evidence over aspiration** — Every claim in this document maps to existing code, workflows, or documents in the repositories.

---

## Current State (Pre-seed – July 2026)

| Control Area | Status | Evidence |
|--------------|--------|----------|
| Input / prompt security | Working | `SecurityGuard` + `input_guard_check` in Coastal-Alpine-Core |
| Device posture | Working | Firmware baseline registration + checks |
| Telemetry & energy awareness | Working | `TelemetryTracker` (joules, latency, tokens/s on RPi 5 + Hailo) |
| Local data flywheel | Working | `DataFlywheel` (trajectories, human feedback, golden sets, SD-card safe rotation) |
| Multi-tenant isolation | Working design | Weaver tenant-partitioned stores + guards |
| CI / SecOps | Working | `secops.yml`, `redteam.yml`, Dependabot, least-privilege Actions |
| Compliance framework | Documented | Full NZ Privacy Act + SOC 2 + Te Mana Raraunga skill under `.github/compliance/nz-ai-compliance-soc2/` |
| Architecture diagrams | Present | Mermaid + images in portfolio, Core, Weaver, Aether, stack |
| Threat model | This document | First formal version |
| External audit | Not started | Planned post first paid pilot |

---

## Phase 1 – Harden for First Paid Pilot (Target: Q3–Q4 2026)

**Goal:** Safe enough for controlled, small-scale on-farm or EDA pilots with real data under owner control.

- [ ] Formalise `COMPLIANCE.md` in Core, Weaver, coastal-alpine-stack, and Aether (using existing template).
- [ ] Complete first internal pass of the Compliance Audit Checklist against live code paths.
- [ ] Document and test backup / restore for DataFlywheel trajectories and local vector stores (RTO/RPO targets as design goals).
- [ ] Expand SecurityGuard coverage for common edge attack patterns (prompt injection, path traversal, tenant cross-talk).
- [ ] Add basic runtime attestation / device posture reporting for RPi 5 nodes.
- [ ] Publish this Security Roadmap + Threat Model as public artefacts.
- [ ] Define Cultural Advisory interface for any Māori data use cases (HITL gate).

**Exit criteria:** Internal checklist >70% green on Diamond-relevant controls; first pilot data stays fully local; no critical open findings.

---

## Phase 2 – Seed / Early Enterprise Readiness (Target: post first revenue or major grant)

**Goal:** Credible for seed investors and first enterprise / regional council conversations.

- [ ] Implement structured audit logging with 18-month retention design (immutable where feasible on edge).
- [ ] Formal incident response playbook exercised (tabletop).
- [ ] Secrets management hygiene (no hardcoded credentials; rotation policy).
- [ ] DSAR / data subject request pathway documented and testable for any personal data held.
- [ ] External penetration test or red-team review of the edge node + Weaver surface.
- [ ] First external compliance gap assessment (Privacy Act + selected SOC 2 controls).
- [ ] Governance.md roles and escalation paths staffed or clearly designated.

**Exit criteria:** Can demonstrate end-to-end local-only operation under realistic load; incident response tested; clear ownership of security and privacy decisions.

---

## Phase 3 – Formal Attestation Path (Future)

Only after sustained pilots and revenue:

- Engage external SOC 2 Type II auditor if commercially justified.
- Complete full control matrix evidence collection.
- Cultural Advisory Board formalised for any ongoing Māori data stewardship.
- Continuous monitoring and monthly compliance cadence operational.

This phase is **not** committed on a fixed date. It is gated on commercial traction and risk profile of actual deployments.

---

## Ownership & Review

| Role | Responsibility |
|------|----------------|
| Founder / CEO | Overall accountability, capital and cultural decisions |
| Security Lead (currently Founder) | Technical controls, threat model ownership |
| Compliance Officer (designate) | Checklist, Privacy Act, incident coordination |
| Cultural Advisor / Board (when formed) | Te Mana Raraunga decisions, data use agreements |

**Review cadence:** This roadmap is reviewed at least quarterly or after any material security incident or architecture change.

---

## Related Documents

- [Threat Model](./THREAT_MODEL.md)
- [NZ AI Compliance + SOC 2 Skill](./nz-ai-compliance-soc2/SKILL.md)
- [Compliance Audit Checklist](./nz-ai-compliance-soc2/references/COMPLIANCE_AUDIT_CHECKLIST.md)
- [Incident Response Playbook](./nz-ai-compliance-soc2/references/INCIDENT_RESPONSE_PLAYBOOK.md)
- [Te Mana Raraunga Principles](./nz-ai-compliance-soc2/references/TE_MANA_RARAUNGA_PRINCIPLES.md)
- [Portfolio Technical Moat](https://github.com/fivepanelhat/fivepanelhat#technical-moat)
- [GOVERNANCE.md](../../GOVERNANCE.md)

---

*Last updated: July 2026 | Pre-seed design target*
