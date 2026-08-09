# Data Sovereignty & Acquisition Protection — Coastal Alpine Tech

**Status:** Design target / pre-seed governance (Aug 2026)  
**Applies to:** All Māori data, whenua-derived operational data, customer data, and golden-set trajectories in the Kiwi Edge AI Stack.

## 1. Market context we are tracking (Enterprise DNA, Jul 2026)

Three things worth tracking in the NZ AI ecosystem:

1. **NZ AI regulatory framework** (MBIE) — may add obligations beyond Privacy Act 2020. Watch briefings.
2. **Consolidation** — a handful of NZ AI startups will be acquired or shut down in the next 12–18 months. Prefer counterparties with ≥12 months runway and a clear plan if acquired.
3. **Rise of agents** — AI that takes actions (not just answers). Real productivity upside; privacy and security questions get harder.

**CAT stance:** All three reinforce the same requirement — keep data and agency onshore under owner-controlled keys. Our edge + Te Mana Raraunga architecture is deliberately harder to hollow out than pure SaaS wrappers.

## 2. How we protect NZ / Māori data if CAT is acquired

Acquisition does not automatically transfer the right to move or re-purpose data. We design so that control survives change of ownership.

### Technical controls (already in architecture)
- **Local-first / edge default.** Sensitive and Māori data stays on-node or in NZ-resident storage under owner-controlled keys. No silent cloud path.
- **Data classification + gates.** Level 2/3 (Te Mana Raraunga / cultural) data cannot leave the node or tenant boundary without explicit HITL + Cultural Advisory approval.
- **Owner-controlled keys & encryption.** Encryption keys are not held solely by the company in a way that a new owner can unilaterally unlock and exfiltrate.
- **No automatic model training on customer / Māori data** without separate, revocable consent and audit trail.
- **Auditability.** Every export, model update, or high-impact action is logged and attributable.

### Contractual & legal controls (to be formalised at incorporation / first pilots)
- **Data Processing / Data Sovereignty Addendum** in every customer and pilot agreement: data remains subject to NZ law + Te Mana Raraunga principles; acquirer must honour existing consent and location restrictions or return/delete the data.
- **Change-of-control clause:** any sale or change of control triggers customer right to terminate, require data return/destruction, or re-consent under the original terms.
- **IP & licence structure:** core sovereignty controls and edge runtime remain licensed in a way that prevents stripping the local-first requirement post-acquisition (exact mechanism to be lawyered at seed).
- **Cultural Advisory veto / consultation right** on any material change to Māori data handling (to be written into governance once the Advisory exists).

### Governance controls
- GOVERNANCE.md and CONSTITUTION.md already treat Māori data as taonga and require Cultural Advisory involvement for Level 2/3 uses.
- Acquisition does not automatically lift HITL or Cultural Advisory gates; those are encoded in code and policy, not just goodwill.
- Founder / Board must document any proposed change to data residency or key control as a material governance event.

### Practical outcome we aim for
An acquirer can buy the company and the technology, but cannot simply ship NZ / Māori data overseas or retrain on it without:
1. Breaking existing customer contracts, and/or
2. Triggering customer termination + data return rights, and/or
3. Violating the technical and policy controls that are already part of the product.

This is the defensive moat against consolidation risk.

## 3. Open items (HITL required)
- Exact wording of change-of-control and data-return clauses (lawyer).
- Key-management design that survives acquisition without creating a single point of failure for customers.
- Formal Cultural Advisory charter before scaled Māori data use.
- Whether any “sovereignty escrow” or independent key trustee is required for larger deals.

---

*Related: [GOVERNANCE.md](../GOVERNANCE.md), [CONSTITUTION.md](../CONSTITUTION.md), [TE_MANA_RARAUNGA_PRINCIPLES.md](../.github/compliance/nz-ai-compliance-soc2/references/TE_MANA_RARAUNGA_PRINCIPLES.md), [COMMERCIAL_POSITIONING.md](../.github/funding/COMMERCIAL_POSITIONING.md), [AI_INFRASTRUCTURE_LEADERSHIP.md](../AI_INFRASTRUCTURE_LEADERSHIP.md)*
