# Digest: NZ AI Compliance + SOC 2 Type II

**Source:** `.github/compliance/nz-ai-compliance-soc2/SKILL.md` v1.0.0 (2026-07-12)  
**Extracted:** 2026-07-13  

## Five pillars (proposal annex)

1. Privacy Act 2020 (IPP 1–11)  
2. Te Mana Raraunga  
3. MBIE Responsible AI  
4. NZ Algorithm Charter  
5. Consumer/competition guardrails (Fair Trading, Commerce Act)

## SOC 2 families to mention as **roadmap**

- CC6/CC7 access control  
- Encryption & secrets  
- Availability (99.5% SLO target, RTO≤4h, RPO≤1h)  
- Privacy + TMR dual-key patterns  

## Audit protocol phases

Discovery → Risk → Gap → Remediation (HITL) → Verification → Sign-off  

## Decision tree (compressed)

PHI? → Health code + encryption + local  
Māori data? → TMR + consent + local  
Automated user decisions? → HITL + explainability  
Public sector? → Algorithm Charter + AIA  

## Funding usage

- Attach as **compliance methodology** not as completed external audit  
- Use metrics table from org README for targets  
- Point to full references under compliance pack for assessors  
