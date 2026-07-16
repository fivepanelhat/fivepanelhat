# Threat Model – Kiwi Edge AI Stack

**Coastal Alpine Tech Limited**  
**Version:** 0.1 (July 2026)  
**Scope:** Pre-seed target architecture (RPi 5 16GB + Hailo-10H, Coastal-Alpine-Core, Weaver, Aether, domain portals, Sovereign-Edge-Firmware)

This is a living document. It describes the primary assets, trust boundaries, and realistic threats for the current design. It is **not** a claim of completed penetration testing or formal certification.

---

## 1. Assets Worth Protecting

| Asset | Why it matters | Sensitivity |
|-------|----------------|-------------|
| Local model weights & prompts | Core inference capability | Medium–High |
| DataFlywheel trajectories & golden sets | Proprietary learning loop; may contain operational context | High |
| Tenant knowledge bases (Weaver) | Customer / farm / operational documents | High |
| Sensor telemetry & actuator commands | Physical world impact (irrigation, alerts, biosecurity) | High |
| Device identity & firmware baselines | Prevents rogue nodes | High |
| Human feedback & quality scores | Improves future decisions | Medium |
| Cultural / Māori data (if present) | Te Mana Raraunga obligations | Highest |

---

## 2. Trust Boundaries

```
[Field sensors / ESP32]  --mTLS MQTT-->  [RPi 5 Hub]
                                              |
                                              v
                                    [Coastal-Alpine-Core]
                                    SecurityGuard | Telemetry | Flywheel
                                              |
                                              v
                                    [Weaver / Portals / Ollama]
                                              |
                                    (optional human terminal)
                                              |
                                    [Aether companion – HITL gated]
```

Key boundaries:
- Field devices ↔ Pi hub (mTLS expected)
- Local process boundary (Python services)
- Tenant isolation boundary inside Weaver
- Human approval boundary for high-impact actions
- No default trust of external cloud services

---

## 3. STRIDE Summary (Primary Threats)

### Spoofing
- **Threat:** Rogue ESP32 or compromised node impersonates a legitimate field device.
- **Mitigation (current):** Firmware baseline registration + device posture checks in Core. mTLS design target for MQTT.
- **Gap:** Full certificate lifecycle and revocation still early.

### Tampering
- **Threat:** Modification of trajectories, golden sets, or local model behaviour.
- **Mitigation:** Local-only storage by default; DataFlywheel rotation and integrity-conscious design; HITL for high-impact changes.
- **Gap:** Cryptographic signing of trajectories not yet implemented.

### Repudiation
- **Threat:** Inability to prove who approved an actuator action or data export.
- **Mitigation:** Explicit HITL policy (“humans sign / send / pay”); audit-oriented trajectory recording.
- **Gap:** Immutable, long-retention audit log still design target.

### Information Disclosure
- **Threat:** Tenant data leakage across Weaver tenants or accidental cloud exfiltration.
- **Mitigation:** Tenant-partitioned stores, SecurityGuard scoping, default-offline architecture, Te Mana Raraunga constraints.
- **Gap:** Formal cross-tenant isolation tests and DSAR tooling still early.

### Denial of Service
- **Threat:** Resource exhaustion on constrained RPi 5 (CPU, memory, SD card, power).
- **Mitigation:** Energy-aware telemetry, SD-card safe flywheel rotation, fail-closed defaults, lightweight local models.
- **Gap:** Formal load and soak testing under realistic multi-tenant load.

### Elevation of Privilege
- **Threat:** Local process or agent gains ability to bypass HITL or actuate hardware without approval.
- **Mitigation:** Hard HITL ceilings in Aether and agent policy; SecurityGuard on inputs; actuators designed for lockout patterns.
- **Gap:** Runtime enforcement of privilege boundaries still maturing.

---

## 4. Edge-Specific Considerations

- **Physical access:** RPi nodes may be in rural or semi-public locations. Physical security is an operational responsibility of the deployer.
- **Offline operation:** Many classic cloud-centric controls (central SIEM, remote wipe) are intentionally limited. Local fail-closed behaviour is preferred.
- **Power & thermal:** Denial-of-service via resource exhaustion is more relevant than in cloud environments. Telemetry already tracks estimated joules.
- **Model supply chain:** Local Ollama models are a trust boundary. Prefer known good models; future work includes model attestation.

---

## 5. Priority Mitigations (Next 90 Days)

1. Strengthen SecurityGuard coverage for the most common injection and scoping attacks.
2. Document and test DataFlywheel backup / restore.
3. Formalise tenant isolation test cases in Weaver.
4. Complete first internal Compliance Audit Checklist pass.
5. Define clear Cultural Advisory escalation path for any Māori data.

---

## 6. Out of Scope (for this version)

- Full formal STRIDE workshops with external parties
- Detailed attack trees for every portal
- Cloud control plane threats (the architecture intentionally minimises them)
- Supply-chain attacks on upstream Python packages beyond Dependabot monitoring

---

## Related Documents

- [Security & Compliance Roadmap](./SECURITY_ROADMAP.md)
- [NZ AI Compliance + SOC 2 Skill](./nz-ai-compliance-soc2/SKILL.md)
- [Incident Response Playbook](./nz-ai-compliance-soc2/references/INCIDENT_RESPONSE_PLAYBOOK.md)
- [Portfolio Architecture](https://github.com/fivepanelhat/fivepanelhat#stack-architecture-overview)
- [GOVERNANCE.md](../../GOVERNANCE.md)

---

*This threat model will be revised after the first paid pilot and after any material architecture change.*
