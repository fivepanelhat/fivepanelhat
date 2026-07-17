# Power Budget & Thermal Characterisation — RPi 5 16GB + Hailo-10H (Kiwi Edge AI Stack)

**Canonical Target**: Raspberry Pi 5 (16GB) + Hailo-10H AI Accelerator / AI HAT+ 2
**Status (July 2026)**: Initial measurements and design targets. Real-world greenhouse testing in progress.

## Why This Matters
Edge AI in NZ primary industries must survive rural power constraints, summer heat in greenhouses/poly-tunnels, and long-term reliability without active cooling. Power and thermal behaviour is a core part of the hardware moat.

## Current Measured / Target Budget (RPi 5 16GB + Hailo-10H)

| Component / Workload | Idle | Typical Inference (Vision + LLM) | Peak / Stress | Notes |
|----------------------|------|----------------------------------|---------------|-------|
| **RPi 5 SoC + RAM** | ~3-4 W | 6-8 W | 10-12 W | With active cooling or good airflow |
| **Hailo-10H NPU** | ~1-2 W | 4-7 W (40 TOPS vision) | 8-10 W | Quantised models; depends on model size and batch |
| **Total System (est.)** | ~5-7 W | 10-15 W | 18-22 W | Includes peripherals, storage, networking |
| **Target (Summer Greenhouse)** | <8 W average | <12 W sustained | <18 W peak | With passive or low-power active cooling; avoid thermal throttling |

**Design Goal**: Sub-15 W sustained inference load for typical agritech workloads (multi-modal crop monitoring) under NZ summer conditions (30-40°C ambient in enclosure).

## Thermal Throttling Tests (Planned / In Progress)
- Enclosure: Standard IP-rated field box with passive heatsink + optional low-power fan.
- Ambient: 25°C lab baseline + 35-40°C simulated greenhouse.
- Workload: Continuous YOLO + LLM inference loop (Byte-Size-Kai style).
- Metrics: CPU/GPU/NPU temp, frequency throttling events, inference latency degradation, power draw over 2-4 hours.

**Current Observations (preliminary)**:
- With good passive heatsinking, sustained loads stay under throttling threshold for typical agritech models.
- Hailo-10H runs significantly cooler and more efficient than equivalent GPU inference on the same board.
- Need real greenhouse data for dust, humidity, and solar loading effects.

## Power Optimisation Levers (in Stack)
- Model quantisation + Hailo compilation (.hef where applicable)
- Selective inference (only run heavy models when triggered by lightweight detector)
- Dynamic voltage/frequency scaling awareness in TelemetryTracker
- Deep sleep / duty-cycling in Sovereign-Edge-Firmware for field nodes
- DataFlywheel prioritisation: prefer cheap local improvement over constant high-load inference

## Related Artefacts
- `MODEL_BENCHMARKS.md` (in progress) — tokens/sec, accuracy, and power per model on target hardware
- `Sovereign-Edge-Firmware` — power-aware sensor node design
- `TelemetryTracker` (Core) — joules, tokens/sec, energy-per-inference metrics
- `cat-architectural-standards` (Diamond target includes energy/resilience)

**Power and thermal behaviour is now a first-class design constraint, not an afterthought.** Real measurements will be published as they become available from field deployments.
