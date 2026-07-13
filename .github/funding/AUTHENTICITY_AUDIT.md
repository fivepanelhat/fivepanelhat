# Authenticity audit — org READMEs

**Date:** 2026-07-13
**Company stage:** Coastal Alpine Tech Limited = **pre-seed startup**

## Scope

All public `README.md` files in core fivepanelhat org repositories.

## Checks performed

1. Company stage language (pre-seed)
2. Removal/softening of role-play capital narratives (fake ACTIVE $ budgets)
3. Softening of enterprise / production-grade / partnership overclaims without evidence
4. Architecture image + Mermaid labelled as **target architecture**
5. Asset presence (`assets/social_preview.png`, `assets/architecture_overview.png` where referenced)
6. No fictional SOC 2 certification claims

## Repo results

| Repo | Notes |
| :--- | :--- |
| fivepanelhat | org profile: pre-seed + claim hygiene; WRITTEN |
| Aether | pre-seed line + overclaim soften + diagram note; WRITTEN |
| coastal-alpine-stack | pre-seed line + overclaim soften + diagram note; WRITTEN |
| Coastal-Alpine-Core | pre-seed line + overclaim soften + diagram note; WRITTEN |
| Weaver | pre-seed line + overclaim soften + diagram note; WRITTEN |
| Front_Line_Whanau | pre-seed line + overclaim soften + diagram note; WRITTEN |
| Sovereign-Edge-Firmware | pre-seed line + overclaim soften + diagram note; WRITTEN |
| Blue-Moon-Portal | pre-seed line + overclaim soften + diagram note; WRITTEN |
| Sting-Operation-AI | pre-seed line + overclaim soften + diagram note; WRITTEN |
| SoilGuard-Portal | pre-seed line + overclaim soften + diagram note; WRITTEN |
| AquaGuard-Portal | pre-seed line + overclaim soften + diagram note; WRITTEN |

## Mermaid ↔ image alignment

Org and product READMEs use a consistent pattern:

1. Hero / social banner image
2. Architecture overview image (liquid glass)
3. Mermaid system map for the **same conceptual layers**
4. Optional layer summary table

Layer naming may differ slightly by product (e.g. field sensors vs grow-room inputs) but maps to the same stack story: inputs → edge runtime (RPi 5 16GB + Hailo-10H) → actions/compliance → optional Aether companion → dual-platform hosts.

## Residual risks / follow-ups

- Re-verify any real pilot partner names before stating “partnership with …”
- Demo sites (e.g. Vercel) should be labelled demos, not mature production products
- Funding roadmap todos remain aspirational until owners fill real dates/evidence
- Deep skill docs under `.github/compliance` still use normative compliance language — treat as **framework design**, not completed audits

## Policy going forward

- Prefer *designed to*, *target*, *pre-seed*, *early-stage*, *roadmap*
- Avoid *enterprise-grade*, *certified*, *ACTIVE $1.2M*, *guarantee*, *in partnership with* without a signed relationship
- HITL before public claims about iwi, health, or capital

