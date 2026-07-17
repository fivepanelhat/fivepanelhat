# Red Team Report — Initial Adversarial Testing (Kiwi Edge AI Stack)

**Status (July 2026)**: Initial internal red teaming completed. This is a living document. Full public version will be published after first pilot with sensitive data redacted.

## Scope of Initial Testing
- Prompt injection attempts on Aether and Weaver agents
- Attempts to bypass HITL gates (social engineering, malformed tool calls, context poisoning)
- Cultural bias / Māori data handling tests (prompts designed to elicit biased or inappropriate outputs)
- Model output grounding failures (hallucination on agritech facts)
- Multi-tenant isolation bypass attempts in Weaver

## Key Findings (Summary — Non-Sensitive)
- **SecurityGuard + input screening** caught the majority of direct prompt injection attempts. Success rate of bypass < 5% in controlled tests.
- **Hard HITL gates** (especially L2+) prevented all tested attempts to trigger high-impact actions without human approval.
- **Cultural safety prompts** surfaced some bias risks in base models; mitigated by explicit Te Tiriti-aligned instructions in system prompts and cultural review gates.
- **Multi-tenant isolation** in Weaver held under simulated cross-tenant attack scenarios (vector store separation + tenant ID enforcement).
- **Grounding / anti-hallucination** measures (DataFlywheel feedback + retrieval) reduced ungrounded agritech claims significantly vs. base model.

## Residual Risks & Mitigations (Current)
- Sophisticated multi-turn jailbreaks still possible on less-guarded paths → Mitigated by stronger Constitution + ongoing red teaming.
- Vision model adversarial examples (e.g., crafted images for YOLO) → In progress; Hailo compilation + input sanitisation planned.
- Social engineering of human approvers → Addressed via training + dual-approval for highest tiers + clear escalation.

## Ongoing Red Teaming Plan
- Quarterly internal red team exercises
- External red team engagement before first paid pilot (budgeted)
- Continuous adversarial testing integrated into CI where feasible
- Publish updated reports (redacted) after significant changes or pilots

**Red teaming is not a one-time checkbox — it is continuous assurance.** Findings directly feed model improvement, Constitution updates, and SecurityGuard rule tuning.
