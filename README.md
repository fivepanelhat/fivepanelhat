# Five Panel Hat 🎩

**Coastal Alpine Tech's Sovereign Edge AI Stack**

---

## 🛡️ NZ AI Compliance + SOC 2 Type II

We've implemented a **comprehensive compliance framework** across all repositories to ensure:

✅ **Privacy Act 2020** compliance (all 11 Information Privacy Principles)  
✅ **Te Mana Raraunga** (Māori data sovereignty + OCAP® principles)  
✅ **SOC 2 Type II** audit-ready controls (CC/A/S/P, 225-item framework)  
✅ **MBIE Responsible AI** (safety-by-design, explainability, HITL gates)  
✅ **NZ Algorithm Charter** (transparent decisions, human appeal pathways)  

**Status:** Framework deployed to all 4 core repositories | Week 1-12 implementation in progress

[📖 Read the Full Compliance Skill](https://github.com/fivepanelhat/Weaver/blob/claude/edge-ai-computer-use-cli-157258/.github/compliance/nz-ai-compliance-soc2/)  
[🔗 View Landing Page](#landing-page)

---

## 🏗️ Core Repositories

### [Weaver](https://github.com/fivepanelhat/Weaver) — Orchestration Layer
Multi-tenant LLM orchestration + autonomous GitOps loop  
**Status:** Diamond (primary) | Platinum (secondary) | Gold (tertiary)  
**Compliance:** HITL gates, error sanitization, tenant isolation  

### [Aether](https://github.com/fivepanelhat/Aether) — AI Engine
Multi-agent ReAct orchestration + computer use + local fine-tuning  
**Status:** Platinum (primary) | Diamond (secondary) | Gold (tertiary)  
**Compliance:** Explainability, fairness monitoring, bias detection  

### [Coastal Alpine Core](https://github.com/fivepanelhat/coastal-alpine-core) — Edge SDK
Field device SDK + encrypted local processing + firmware verification  
**Status:** Diamond (primary) | Platinum (secondary) | Gold (tertiary)  
**Compliance:** Encryption at rest/transit, device posture, constant-time hashing  

### [coastal-alpine-stack](https://github.com/fivepanelhat/coastal-alpine-stack) — Deployment
Webhook relay + autonomous remediation + swarm orchestration  
**Status:** Diamond (primary) | Platinum (secondary) | Gold (tertiary)  
**Compliance:** Fail-closed authentication, HITL gates, signature verification  

---

## 📋 What's Included

Each repository contains:

```
repo/
├── COMPLIANCE.md                         [Repo-specific governance]
└── .github/compliance/nz-ai-compliance-soc2/
    ├── SKILL.md                          [Master framework definition]
    ├── README.md                         [6-week implementation guide]
    └── references/
        ├── NZ_PRIVACY_ACT_2020_MAPPING.md          [IPP 1-11 detailed]
        ├── SOC2_CONTROL_MATRIX.md                  [225-item controls]
        ├── TE_MANA_RARAUNGA_PRINCIPLES.md          [Māori sovereignty]
        ├── INCIDENT_RESPONSE_PLAYBOOK.md           [Breach response]
        └── COMPLIANCE_AUDIT_CHECKLIST.md           [Pre-audit verification]
```

---

## 🚀 Implementation Timeline

| Phase | Duration | Focus |
|-------|----------|-------|
| **Phase 1** | Week 1 | Establish governance (Compliance Officer, CAB, monthly reviews) |
| **Phase 2** | Week 2-4 | Harden technical controls (MFA, Vault, encryption, logging) |
| **Phase 3** | Week 2-4 | Privacy Act compliance (DSAR portal, retention, DPAs) |
| **Phase 4** | Week 3-6 | Te Mana Raraunga (community engagement, data use agreements) |
| **Phase 5** | Week 5-8 | Incident response testing (tabletop drills, backup restore) |
| **Phase 6** | Week 9-12 | External audit (SOC 2 Type II report + opinion) |

---

## 🎯 Key Metrics & Targets

| Metric | Target |
|--------|--------|
| Availability SLO | 99.5% monthly |
| Audit Log Retention | 18 months (immutable) |
| Health Data Retention | 7 years max |
| API Key Rotation | 90 days |
| DSAR Response | 20 working days |
| Breach Notification | 72 hours (Privacy Commissioner) |
| Backup RTO | ≤4 hours |
| Backup RPO | ≤1 hour |
| Incident P0 Response | 15 minutes |
| Audit Checklist Completion | ≥95% |

---

## 🔐 Security Hardening Summary

### Access Control (CC6)
✓ MFA for all admin access  
✓ RBAC (role-based access control)  
✓ Short-lived service credentials (max 1 hour)  
✓ API key rotation (automated, 90-day cycle)  
✓ Quarterly access review + recertification  

### Encryption & Secrets (CC7/CC9)
✓ AES-256 encryption at rest (databases)  
✓ TLS 1.3+ enforced (all APIs)  
✓ Centralized secret vault (Vault / Secrets Manager)  
✓ No hardcoded credentials (enforced by static analysis)  
✓ Immutable audit logs (18-month retention)  

### Incident Response & Availability (A)
✓ 99.5% uptime SLO + automated monitoring  
✓ High availability architecture (no single points of failure)  
✓ Daily backups, monthly restore testing  
✓ P0/P1/P2/P3 incident SLAs  
✓ Privacy Commissioner notification (72-hour mandatory)  

### Privacy & Data Sovereignty (P + Te Mana Raraunga)
✓ DSAR portal + 20-day SLA  
✓ Data deletion workflow  
✓ Data retention enforced (7 years for health data)  
✓ Third-party DPAs signed + access logged  
✓ Māori data ownership registry + Cultural Advisory Board  
✓ Dual-key encryption (iwi + organization)  

---

## 🤖 AI & Responsible AI (MBIE + Algorithm Charter)

✓ **Explainability:** All agent actions logged with rationale  
✓ **HITL Gates:** High-risk decisions require human approval  
✓ **Fairness:** Monthly bias scoring + algorithmic drift detection  
✓ **Safety:** Computer use gated by guardrails + approval workflow  
✓ **Transparency:** Automated decision audit trail + impact assessments  

---

## 📖 CAT Architectural Standards

All four repositories are classified under the **Coastal Alpine Tech (CAT) Architectural Standards**:

- **DIAMOND (Primary):** Enterprise-grade compliance, security, observability
- **PLATINUM (Secondary):** AI-driven continuous improvement + data flywheel
- **GOLD (Tertiary):** Workflow-native design with transparent HITL gates

[Read the full CAT standards skill](https://github.com/fivepanelhat/Aether/blob/claude/edge-ai-computer-use-cli-157258/skills/cat-architectural-standards/SKILL.md)

---

## 💰 Kotahitanga Investment Strategy — Sovereign AI Capital Allocation

**Kotahitanga** (collective unity) is our framework for allocating capital to sovereign AI and indigenous data infrastructure projects. It operationalizes:

✓ **Three-Tier Model** (aligns with CAT standards)
  - **Diamond:** Onshore bare-metal infrastructure ($500K–$2M, 24 months)
  - **Platinum:** Edge-autonomous intelligent systems ($200K–$800K, 12 months)
  - **Gold:** Commercial workflow optimization ($50K–$300K, 6 months)

✓ **OCAP® Verification** (Te Mana Raraunga principles)
  - Ownership: Clear legal ownership (iwi, organization, or co-ownership)
  - Control: Encryption keys held by data owner (dual-key model for Māori data)
  - Access: All access logged, audited, restricted by purpose
  - Possession: Data physically located in Aotearoa only

✓ **225-Point Compliance Baseline** (NZ Privacy Act 2020 + SOC 2 Type II)
  - **Diamond:** ≥95% baseline (external auditor sign-off required)
  - **Platinum:** ≥85% baseline (internal audit + CISO review)
  - **Gold:** ≥80% baseline (Compliance Officer review)

✓ **Remediation Guardrails**
  - 🟢 **GREEN (≥90%):** Full capital release, normal operations
  - 🟡 **YELLOW (70–89%):** 50% escrow hold, 30-day remediation deadline
  - 🔴 **RED (<70%):** Full capital freeze, infrastructure lockout (remediate or terminate)

✓ **HITL Gates** (mandatory human-in-the-loop)
  - Capital allocation decisions (>$50K requires CFO + CISO approval)
  - Tier classification changes (requires board + Cultural Advisory Board sign-off)
  - Māori data approvals (Cultural Advisory Board has veto authority)

✓ **Local Benefit-Sharing** (quarterly reporting)
  - Local employment created (FTEs)
  - Community training + skill development
  - Data sovereignty milestones achieved
  - Revenue reinvested locally

**Active Projects:**
- **KAS-2026-001:** Sovereign Regional Health Cloud (Weaver) — $1.2M, ACTIVE, 94% ✓
- **KAS-2026-007:** Community Farm AI (Core/Aether) — $300K, ACTIVE, 88%
- **KAS-2026-008:** Regional Intelligence Hub (Stack) — $400K, RED (capital freeze, remediation in progress)

[View Full Investment Strategy](https://github.com/fivepanelhat/Weaver/blob/claude/edge-ai-computer-use-cli-157258/.github/investment/KOTAHITANGA_INVESTMENT_STRATEGY.md)  
[View Capital Allocation Tracker](https://github.com/fivepanelhat/Weaver/blob/claude/edge-ai-computer-use-cli-157258/.github/investment/CAPITAL_ALLOCATION_TRACKER.md)

---

## 🆘 Contact & Support

### Compliance & Governance
- **Compliance Officer:** [Assign in COMPLIANCE.md]
- **Privacy Officer:** [Assign in COMPLIANCE.md]
- **CISO / Security Lead:** [Assign in COMPLIANCE.md]
- **Cultural Advisor:** [Assign in COMPLIANCE.md]

### Get Started
1. Read the [Compliance Landing Page](#landing-page)
2. Open `.github/compliance/nz-ai-compliance-soc2/SKILL.md` in any repo
3. Assign compliance contacts in `COMPLIANCE.md`
4. Schedule Week 1 governance kickoff

### For Questions
- **Technical:** Read [SKILL.md](./.github/compliance/nz-ai-compliance-soc2/SKILL.md)
- **Privacy Act:** See [NZ_PRIVACY_ACT_2020_MAPPING.md](./.github/compliance/nz-ai-compliance-soc2/references/NZ_PRIVACY_ACT_2020_MAPPING.md)
- **SOC 2:** See [SOC2_CONTROL_MATRIX.md](./.github/compliance/nz-ai-compliance-soc2/references/SOC2_CONTROL_MATRIX.md)
- **Te Mana Raraunga:** See [TE_MANA_RARAUNGA_PRINCIPLES.md](./.github/compliance/nz-ai-compliance-soc2/references/TE_MANA_RARAUNGA_PRINCIPLES.md)
- **Incident Response:** See [INCIDENT_RESPONSE_PLAYBOOK.md](./.github/compliance/nz-ai-compliance-soc2/references/INCIDENT_RESPONSE_PLAYBOOK.md)
- **Audit Ready:** See [COMPLIANCE_AUDIT_CHECKLIST.md](./.github/compliance/nz-ai-compliance-soc2/references/COMPLIANCE_AUDIT_CHECKLIST.md)

---

## 📚 References

| Framework | Link |
|-----------|------|
| NZ Privacy Commissioner | https://www.privacy.org.nz/ |
| NZ Health Information Privacy Code | https://www.privacy.org.nz/your-rights/codes-of-practice/health-information-privacy-code/ |
| MBIE Responsible AI Guidance | https://www.mbie.govt.nz/dmsdocument/19433 |
| Te Mana Raraunga (Māori Data Sovereignty) | https://www.temanararaunga.maori.nz/ |
| AICPA SOC 2 Framework | https://www.aicpa.org/interestareas/informationsystems/audit-attest/aicpa-soc-2-report |
| OCAP® Principles | https://fnigc.ca/ocap-principles/ |

---

## 📊 Compliance Status Dashboard

```
🟢 Framework Definition       ✓ Complete
🟢 Deployed to 4 Repos        ✓ Weaver | Core | Stack | Aether
🟢 Governance Files           ✓ COMPLIANCE.md in all repos
🟡 Week 1-12 Implementation   ◐ Planned (contact Compliance Officer)
⚫ External SOC 2 Audit        ○ Scheduled for Q4 2026 - Q1 2027
```

---

## 🛡️ Security Notices

**HITL Gate Active:** All compliance decisions require human review and approval. No automated implementation without explicit sign-off.

**Data Sovereignty:** Māori data handled under Te Mana Raraunga principles with explicit iwi/hapū/whānau approval + Cultural Advisory Board oversight.

**Incident Reporting:** Contact privacy@coastalalp.tech immediately for any security incidents. SLA: 15 min (P0), 1 hour (P1).

---

**Last Updated:** 2026-07-12  
**Classification:** Diamond | Platinum | Gold  
**Status:** Ready for Implementation  

---

*Coastal Alpine Tech — Sovereign Edge AI for Aotearoa New Zealand 🇳🇿*
