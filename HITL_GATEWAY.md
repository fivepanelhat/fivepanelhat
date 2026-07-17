# HITL Gateway — Explicit Human Approval Layer (Kiwi Edge AI Stack)

**Purpose**: This document defines exactly which actions in the Kiwi Edge AI Stack require human approval, how approval is requested and logged, and the integration points (webhook, Slack, email, TTY). It makes the HITL policy from `aether-hitl-protocol` and `GOVERNANCE.md` operational and auditable.

**Status (July 2026)**: Design target + initial implementation in Aether. Full webhook/Slack/email integration is in active development.

## Core Principle (Non-Negotiable)
Agents inform, draft, prepare, monitor, and remind. **Humans alone advise, decide, sign, file, send, pay, or actuate high-impact controls.** No system may present agent output as final authority.

## Risk-Tiered HITL Matrix

| Risk Tier | Examples in Stack | Minimum Gate | Approval Mechanism | Logging | Escalation |
|-----------|-------------------|--------------|--------------------|---------|------------|
| **Low (L0/L1)** | Internal drafting, non-personal research, low-impact recommendations | Logging only | Auto-approved with audit trail | Structured JSONL in DataFlywheel / Aether memory | None |
| **Medium (L2)** | Tenant-facing advice, operational recommendations (e.g., irrigation plan suggestion), model output used in reports | Explicit approval before action | TTY prompt (Aether), webhook to Slack/Email, or UI checkbox | Full prompt + decision + approver + timestamp | To Cultural Advisory if Māori data involved |
| **High (L2/L3)** | Actuation (valve control, fertigation, biosecurity alerts), personal/Māori data processing, compliance outputs, computer-use on production systems | Multi-person or elevated review + cultural check where relevant | Webhook + Slack/Email + TTY fallback; requires at least one human sign-off | Full chain: prompt → tool calls → proposed action → human decision + reason | Founder + Cultural Advisory for Māori data or high-stakes |
| **Critical / Novel (L3/L4)** | New model classes, cross-border data flows, high-stakes autonomous loops, public high-impact systems, changes to governance or Constitution | Formal impact assessment + external/cultural advisory input + founder-level gate | Formal approval workflow (documented ticket + multiple sign-offs) | Immutable audit (Walrus or equivalent) + full impact assessment attached | Founder + external advisor + iwi representative where relevant |

## Concrete Actions That Pause for Human Approval

**In Aether (agentic companion)**:
- Any `computer use` actuation (click, type, shell on production or sensitive hosts)
- File writes outside sandbox or to production configs
- Git operations (commit, push, PR creation) on main branches
- Model updates or fine-tuning triggers
- Sending external communications (email, Slack, reports)

**In Weaver (multi-tenant orchestration)**:
- Tenant-specific RAG updates or knowledge base changes that affect other tenants
- Actuation commands routed to field devices (via Core/MQTT)
- Changes to tenant isolation policies

**In Core / Portals (Byte-Size-Kai, SoilGuard, AquaGuard, Sting)**:
- Any actuator commands (valves, pumps, alerts that trigger physical action)
- Updates to compliance or regulatory reports
- Data export or sharing outside the node
- Changes to DataFlywheel golden sets that affect production models

**In Sovereign-Edge-Firmware**:
- OTA firmware updates
- Changes to sensor calibration or deep-sleep schedules that affect data quality

## Integration Points (Current & Planned)
- **TTY / Terminal** (Aether default): Immediate interactive prompt with context and proposed action.
- **Webhook** (planned): POST to configurable endpoint with JSON payload (action, risk tier, context summary, proposed output). Returns approval/reject + optional reason.
- **Slack / Email** (planned): Formatted message with approve/reject buttons or reply commands. Fallback to TTY if no response in timeout.
- **Audit Trail**: Every gated action logged with full prompt, tool calls, proposed action, human decision, approver identity, timestamp, and reason. Stored locally in DataFlywheel / Aether memory (immutable where possible).

## Example Flow (High-Risk Actuation)
1. Agent proposes: "Soil moisture low — recommend opening irrigation valve for 12 minutes."
2. Risk tier detected as High → pause.
3. HITL Gateway sends webhook + Slack message with context, expected outcome, and confidence.
4. Human reviews (optionally with Cultural Advisory if relevant) → approves or rejects with reason.
5. If approved: Action executed + logged. If rejected: Agent notified with reason for learning.
6. Full record stored for audit, red-teaming, and model improvement.

## Non-Gated Actions (by design)
- Read-only queries and recommendations that stay within the node
- Internal research and drafting
- Low-risk monitoring and alerting (human still sees the alert)
- Self-remediation within safe bounds defined in Constitution

## Related Documents
- `GOVERNANCE.md` — Decision rights and escalation
- `aether-hitl-protocol` — Gate levels and approval artefacts
- `aether-nz-ai-safety` — Risk tiering and cultural safety requirements
- `CONSTITUTION.md` (planned) — What the agent will and will not do
- `REDTEAM_REPORT.md` — Adversarial testing of HITL bypass attempts

**This gateway makes our HITL policy enforceable, auditable, and ready for enterprise due diligence.**
