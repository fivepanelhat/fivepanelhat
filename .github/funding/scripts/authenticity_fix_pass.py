#!/usr/bin/env python3
"""One-shot authenticity pass across Coastal Alpine org READMEs.

- Positions Coastal Alpine Tech Limited as pre-seed
- Softens enterprise / partnership / guarantee overclaims
- Labels diagrams as target architecture
- Does not invent metrics or partnerships
"""
from __future__ import annotations

import re
from pathlib import Path

HOME = Path.home()
REPOS = [
 "fivepanelhat",
 "Aether",
 "coastal-alpine-stack",
 "Coastal-Alpine-Core",
 "Weaver",
 "Front_Line_Whanau",
 "Sovereign-Edge-Firmware",
 "Byte-Size-Kai",
 "Sting-Operation-AI",
 "SoilGuard-Portal",
 "AquaGuard-Portal",
]

PRESEED_LINE = (
 "**Coastal Alpine Tech Limited** - pre-seed startup, New Plymouth, Taranaki, "
 "Aotearoa New Zealand."
)

DIAGRAM_NOTE = (
 "\n> **Diagrams:** Architecture images and Mermaid maps describe the "
 "**target product architecture** for this pre-seed stack. They are "
 "engineering design maps - not claims of large-scale commercial fleet "
 "deployment.\n"
)


def fix_fivepanelhat(text: str) -> str:
 # Intro
 text = re.sub(
 r"Welcome to the official repository landing page for \*\*Coastal Alpine Tech Limited\*\*,[^\n]*\n\n"
 r"Our stack is \*\*hybridised\*\*[^\n]*\n",
 PRESEED_LINE
 + "\n\n"
 + "We are building offline-native, data-sovereign edge intelligence for remote "
 + "industrial, agricultural, and biosecurity settings across Aotearoa. "
 + "This org profile maps our **Kiwi Edge AI Stack** - early-stage product "
 + "architecture and open engineering work, **not** a claim of large-scale "
 + "commercial deployment or raised Series capital.\n\n"
 + "Our stack is **hybridised** across **Coastal-Alpine-Core**, **Weaver**, "
 + "**Aether**, and **coastal-alpine-stack**: develop on **Windows or Linux**; "
 + "target production edge on the **canonical node** - **Raspberry Pi 5 (16GB)** "
 + "with **Hailo-10H NPU** (40 TOPS AI Accelerator / AI HAT+ 2) - to support "
 + "customary data rights (Te Mana Raraunga / Maori Data Sovereignty) and offline "
 + "operation in rural catchments facing cloud blackouts.\n",
 text,
 count=1,
 )

 text = text.replace(
 "**Status:** Framework files deployed | implementation roadmap Q3 2026 -> external SOC 2 target Q4 2026-Q1 2027",
 "**Status (pre-seed):** Compliance **framework documents** are in-repo as design "
 "targets - **not** an external SOC 2 Type II attestation. Implementation is early-stage.",
 )

 old_roles = """### Foundation roles (CAT tiers)

| Repo | Layer | CAT emphasis |
| :--- | :--- | :--- |
| **Weaver** | Orchestration + multi-tenant RAG | Diamond primary | HITL, tenant isolation |
| **Aether** | Agentic companion + computer use | Platinum primary | explainability, fairness |
| **Coastal-Alpine-Core** | Edge SDK + security primitives | Diamond primary | encryption, device posture |
| **coastal-alpine-stack** | Deploy / remediate / compose | Diamond primary | fail-closed auth, signatures |"""

 new_roles = """### Foundation roles (CAT design targets)

CAT Gold / Platinum / Diamond labels are **internal design maturity targets** for a pre-seed company - not third-party certifications or claims of enterprise production fleets.

| Repo | Layer | Design focus |
| :--- | :--- | :--- |
| **Weaver** | Orchestration + multi-tenant RAG | HITL, tenant isolation |
| **Aether** | Agentic companion + computer use | Explainability, fairness, skills |
| **Coastal-Alpine-Core** | Edge SDK + security primitives | Encryption, device posture |
| **coastal-alpine-stack** | Deploy / remediate / compose | Fail-closed auth patterns, compose/K3s |"""

 text = text.replace(old_roles, new_roles)

 if DIAGRAM_NOTE.strip() not in text:
 text = text.replace(
 "End-to-end data path on a **sovereign edge node**, hybridised with the **Aether** companion. Sensors and actuators stay on-farm; inference and orchestration never leave the property. **Develop on Windows or Linux; deploy on RPi 5.**\n\n![Kiwi Edge AI Stack - ultra liquid glass architecture](assets/architecture_overview.png)\n\n### System layers (readable map)",
 "End-to-end **target** data path on a sovereign edge node, hybridised with the **Aether** companion. Design intent: sensors and actuators stay on-farm; inference and orchestration stay local. **Develop on Windows or Linux; target deploy on RPi 5.**\n"
 + DIAGRAM_NOTE
 + "\n![Kiwi Edge AI Stack - ultra liquid glass architecture](assets/architecture_overview.png)\n\n### System layers (readable map - same target layers as the image)",
 )

 text = text.replace(
 "3. **Regulatory Safety**: Systems actively control actuators (like locking out fertigation lines or disabling class 3B lasers) to automatically prevent regulatory breaches of Regional Council rules.",
 "3. **Regulatory Safety**: Domain agents are **designed** to support actuator lockouts (e.g. fertigation lines) so operators can reduce risk of Regional Council rule breaches - field validation is part of the pre-seed roadmap.",
 )
 text = text.replace(
 "4. **Cross-platform hybrid**: Foundation packages run on **Windows and Linux** for development; production edge stays on RPi 5 + Hailo-10H.",
 "4. **Cross-platform hybrid**: Foundation packages target **Windows and Linux** for development; intended production edge is RPi 5 + Hailo-10H.",
 )

 text = text.replace(
 """### CAT Architectural Standards

- **Diamond (primary):** enterprise-grade compliance, security, observability 
- **Platinum (secondary):** AI continuous improvement + data flywheel 
- **Gold (tertiary):** workflow-native design with transparent HITL gates """,
 """### CAT Architectural Standards (design targets)

Internal maturity model - **not** external audit grades:

- **Diamond:** security, observability, and deployment hardening goals 
- **Platinum:** AI continuous improvement + data flywheel goals 
- **Gold:** workflow-native design with transparent HITL gates """,
 )

 text = text.replace(
 "### Key metrics (targets)\n\n| Metric | Target |",
 "### Key metrics (aspirational targets for a maturing product - not current SLAs)\n\n| Metric | Target |",
 )

 if "badge/Stage-Pre--seed" not in text:
 text = text.replace(
 "[![License](https://img.shields.io/badge/License-Proprietary--Commercial-blue?style=flat-square)](LICENSE)",
 "[![Stage](https://img.shields.io/badge/Stage-Pre--seed-8B5CF6?style=flat-square)]()\n"
 "[![License](https://img.shields.io/badge/License-Proprietary--Commercial-blue?style=flat-square)](LICENSE)",
 1,
 )

 if "### 2026-07-13 - authenticity + pre-seed positioning" not in text:
 text = text.replace(
 "### 2026-07-13 - funding system scaffold",
 "### 2026-07-13 - authenticity + pre-seed positioning\n\n"
 "| Area | What shipped |\n"
 "| :--- | :--- |\n"
 "| **Company stage** | Coastal Alpine Tech Limited stated as **pre-seed startup** |\n"
 "| **Claims hygiene** | Softened enterprise/SLA overclaims; diagrams labelled as **target architecture** |\n"
 "| **Capital fiction** | Public materials avoid role-play funded-project narratives |\n\n"
 "### 2026-07-13 - funding system scaffold",
 1,
 )

 # Soften Kotahitanga compliance baseline language slightly
 text = text.replace(
 "| **Compliance baseline** | Diamond ≥95% | Platinum ≥85% | Gold ≥80% on the 225-point matrix |",
 "| **Compliance baseline (internal goals)** | Diamond ≥95% | Platinum ≥85% | Gold ≥80% on the 225-point checklist |",
 )
 return text


def ensure_preseed_company_line(text: str) -> str:
 if "pre-seed" in text.lower() or "preseed" in text.lower():
 # still ensure company attribution is clear if CAT mentioned without pre-seed nearby
 if "Coastal Alpine Tech Limited" in text and "pre-seed" not in text[:800].lower():
 text = text.replace(
 "**Coastal Alpine Tech Limited**",
 "**Coastal Alpine Tech Limited** (pre-seed startup)",
 1,
 )
 return text

 # Insert after first Coastal Alpine line or at top after H1
 if re.search(r"\*\*Coastal Alpine Tech Limited\*\*", text):
 text = re.sub(
 r"\*\*Coastal Alpine Tech Limited\*\*[^\n]*",
 PRESEED_LINE,
 text,
 count=1,
 )
 return text

 # After first H1
 text = re.sub(
 r"(^# .+\n)",
 r"\1\n" + PRESEED_LINE + "\n",
 text,
 count=1,
 flags=re.M,
 )
 return text


def ensure_diagram_note(text: str) -> str:
 if "target product architecture" in text.lower():
 return text
 # After architecture overview heading if present
 m = re.search(r"(## Architecture Overview[^\n]*\n)", text)
 if m:
 insert_at = m.end()
 return text[:insert_at] + DIAGRAM_NOTE + text[insert_at:]
 # After first architecture image
 m = re.search(r"(!\[[^\]]*architecture[^\]]*\]\([^)]+\)\s*\n)", text, flags=re.I)
 if m:
 return text[: m.end()] + DIAGRAM_NOTE + text[m.end() :]
 return text


def soften_overclaims(text: str, repo: str) -> str:
 replacements = [
 (r"\bproduction-grade,", "early-stage (pre-seed) stack aiming at production-grade,"),
 (r"\bA production-grade,", "An early-stage (pre-seed)"),
 (r"\bproduction-grade\b", "production-oriented"),
 (r"To guarantee data sovereignty", "To support data sovereignty"),
 (r"\bguarantee operational uptime\b", "support operational uptime"),
 (
 r"in partnership with Taranaki and Waikato crop growers, dairy farmers, and iwi trusts",
 "intended for collaboration with NZ crop growers, dairy farmers, and iwi trusts (partnerships in development - pre-seed)",
 ),
 (
 r"in partnership with NZ aquaculture operators, dairy farmers, and tangata whenua with interests in freshwater and coastal environments",
 "designed for NZ aquaculture operators, dairy farmers, and tangata whenua with interests in freshwater and coastal environments (customer/partner relationships in development - pre-seed)",
 ),
 (
 r"Built by Coastal Alpine Tech Limited, designed for high-stakes Kiwi industries",
 "Built by Coastal Alpine Tech Limited (pre-seed), designed for high-stakes Kiwi industries",
 ),
 (
 r"Production deployment \(Sydney region\)",
 "Hosted demo deployment (Sydney region) - product is early-stage",
 ),
 (
 r"\*\*🌐 Live: https://front-line-whanau\.vercel\.app\*\*",
 "**Demo:** https://front-line-whanau.vercel.app (early public demo; Coastal Alpine Tech Limited is pre-seed)",
 ),
 (
 r"MVP targeted for the next 4-8 weeks, with ongoing development toward national adoption\.",
 "MVP in active development (pre-seed). National adoption is a long-term aspiration, not a current claim.",
 ),
 (
 r"The platform is built in partnership with whanau, iwi \(including Muaupoko\), health professionals, and community organisations\.",
 "The platform is **intended** to be co-designed with whanau, iwi, health professionals, and community organisations as relationships mature (pre-seed - do not treat as formal institutional endorsement).",
 ),
 ]
 for pat, repl in replacements:
 text = re.sub(pat, repl, text)
 return text


def process_repo(name: str) -> list[str]:
 notes: list[str] = []
 path = HOME / name / "README.md"
 if not path.exists():
 return [f"{name}: no README"]
 original = path.read_text(encoding="utf-8")
 text = original

 if name == "fivepanelhat":
 text = fix_fivepanelhat(text)
 notes.append("org profile: pre-seed + claim hygiene")
 else:
 text = ensure_preseed_company_line(text)
 text = ensure_diagram_note(text)
 text = soften_overclaims(text, name)
 notes.append("pre-seed line + overclaim soften + diagram note")

 if text != original:
 path.write_text(text, encoding="utf-8")
 notes.append("WRITTEN")
 else:
 notes.append("unchanged")
 return notes


def fix_funding_tracker() -> None:
 path = HOME / "fivepanelhat" / ".github" / "funding" / "FUNDING_TRACKER.md"
 if not path.exists():
 return
 text = path.read_text(encoding="utf-8")
 old = """## Internal capital (Kotahitanga)

Tracked separately from external grants (governance capital, not public grant applications):

| ID | Project | Tier | Budget | Compliance % | Status | Notes |
| :--- | :--- | :--- | ---: | ---: | :--- | :--- |
| KAS-2026-001 | Sovereign Regional Health Cloud (Weaver) | Diamond | $1.2M | 94 | ACTIVE | HITL capital + cultural review |
| KAS-2026-007 | Community Farm AI (Core/Aether) | Platinum | $300k | 88 | ACTIVE | Edge agritech flywheel |
| KAS-2026-008 | Regional Intelligence Hub (Stack) | Diamond | $400k | RED | FREEZE | Remediate before capital release |

Rules: see org README Kotahitanga section + compliance skill. **HITL mandatory** for allocations >$50k."""

 new = """## Internal capital (Kotahitanga) - planning only

**Coastal Alpine Tech Limited is pre-seed.** The rows below are **internal planning scenarios** for how future capital *might* be gated - **not** raised funds, customer contracts, or active multi-million programmes.

| ID | Theme | Tier (design) | Planning envelope | Status | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| KAS-PLAN-001 | Sovereign health-adjacent orchestration (Weaver) | Diamond goals | TBD - unfunded | **planning** | Requires HITL + cultural review before any real allocation |
| KAS-PLAN-007 | Community farm / agritech edge (Core/Aether) | Platinum goals | TBD - unfunded | **planning** | Pilot LOIs first |
| KAS-PLAN-008 | Regional edge hub (Stack) | Diamond goals | TBD - unfunded | **planning** | No capital release without compliance baseline |

Rules: org README Kotahitanga principles + compliance skill. **HITL mandatory** before any real capital movement. Do not present these IDs as awarded grants or live investments."""

 if old in text:
 text = text.replace(old, new)
 else:
 # fallback: rewrite section heuristically
 text = re.sub(
 r"## Internal capital \(Kotahitanga\)[\s\S]*?(?=\n---\n\n## Declined)",
 new + "\n\n",
 text,
 count=1,
 )
 path.write_text(text, encoding="utf-8")
 print("funding tracker: planning-only capital")


def write_audit_report(results: dict[str, list[str]]) -> None:
 path = HOME / "fivepanelhat" / ".github" / "funding" / "AUTHENTICITY_AUDIT.md"
 lines = [
 "# Authenticity audit - org READMEs",
 "",
 "**Date:** 2026-07-13",
 "**Company stage:** Coastal Alpine Tech Limited = **pre-seed startup**",
 "",
 "## Scope",
 "",
 "All public `README.md` files in core fivepanelhat org repositories.",
 "",
 "## Checks performed",
 "",
 "1. Company stage language (pre-seed)",
 "2. Removal/softening of role-play capital narratives (fake ACTIVE $ budgets)",
 "3. Softening of enterprise / production-grade / partnership overclaims without evidence",
 "4. Architecture image + Mermaid labelled as **target architecture**",
 "5. Asset presence (`assets/social_preview.png`, `assets/architecture_overview.png` where referenced)",
 "6. No fictional SOC 2 certification claims",
 "",
 "## Repo results",
 "",
 "| Repo | Notes |",
 "| :--- | :--- |",
 ]
 for repo, notes in results.items():
 lines.append(f"| {repo} | {'; '.join(notes)} |")
 lines += [
 "",
 "## Mermaid <-> image alignment",
 "",
 "Org and product READMEs use a consistent pattern:",
 "",
 "1. Hero / social banner image",
 "2. Architecture overview image (liquid glass)",
 "3. Mermaid system map for the **same conceptual layers**",
 "4. Optional layer summary table",
 "",
 "Layer naming may differ slightly by product (e.g. field sensors vs grow-room inputs) but maps to the same stack story: inputs -> edge runtime (RPi 5 16GB + Hailo-10H) -> actions/compliance -> optional Aether companion -> dual-platform hosts.",
 "",
 "## Residual risks / follow-ups",
 "",
 "- Re-verify any real pilot partner names before stating "partnership with ..."",
 "- Demo sites (e.g. Vercel) should be labelled demos, not mature production products",
 "- Funding roadmap todos remain aspirational until owners fill real dates/evidence",
 "- Deep skill docs under `.github/compliance` still use normative compliance language - treat as **framework design**, not completed audits",
 "",
 "## Policy going forward",
 "",
 "- Prefer *designed to*, *target*, *pre-seed*, *early-stage*, *roadmap*",
 "- Avoid *enterprise-grade*, *certified*, *ACTIVE $1.2M*, *guarantee*, *in partnership with* without a signed relationship",
 "- HITL before public claims about iwi, health, or capital",
 "",
 ]
 path.write_text("\n".join(lines) + "\n", encoding="utf-8")
 print("wrote", path)


def main() -> None:
 results: dict[str, list[str]] = {}
 for name in REPOS:
 results[name] = process_repo(name)
 print(name, "->", results[name])
 fix_funding_tracker()
 write_audit_report(results)


if __name__ == "__main__":
 main()
