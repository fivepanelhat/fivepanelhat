# Model Benchmarks on Target Hardware — RPi 5 16GB + Hailo-10H

**Status (July 2026)**: Initial validated models and methodology. Expanding with real agritech corpus results.

## Canonical Hardware
- Raspberry Pi 5 (16GB RAM)
- Hailo-10H AI Accelerator (40 TOPS) via official AI HAT+
- OS: Raspberry Pi OS 64-bit (or Ubuntu 24.04 for dev)
- Local LLM runtime: Ollama (with Hailo acceleration where supported)

## Validated / Priority Models (2026 Enterprise Defaults)

| Model | Size | Quantisation | Tokens/sec (est. on target) | Power Draw (est.) | Accuracy Notes (agritech tasks) | Status |
|-------|------|--------------|-----------------------------|-------------------|----------------------------------|--------|
| **Qwen2.5-7B** | 7B | Q4_K_M / Q5 | ~25-40 t/s (text) | ~10-14 W sustained | Strong reasoning; good for planning & compliance text | Validated baseline |
| **Llama-3.2-3B** | 3B | Q4_K_M | ~50-70 t/s | ~8-11 W | Lightweight; fast for simple monitoring & alerts | Validated |
| **Mistral-Small-24B** | 24B | Q4 | ~12-20 t/s | ~12-16 W | High quality for complex agritech reasoning | In testing |
| **Gemma 2 / Gemma 4 class** | 2-9B | Q4/Q5 | ~30-55 t/s | ~9-13 W | Current default; solid but being compared | Baseline |
| **Domain-specific distilled (planned)** | 3B | Q4 | TBD | Lower | Fine-tuned on Byte-Size-Kai / agritech corpus | Experiment stage |

**Notes**:
- All numbers are preliminary / literature + early internal tests. Real measured values will replace estimates as hardware validation completes.
- Hailo-10H primarily accelerates vision (YOLO, etc.). LLM acceleration depends on Ollama/Hailo integration maturity.
- Power numbers include system overhead on RPi 5.

## Benchmark Methodology
- Workload: Representative agritech prompts (crop status summary, irrigation recommendation, compliance check, anomaly explanation).
- Metrics: Tokens/sec (output), time-to-first-token, power draw (joules per token via TelemetryTracker), accuracy vs. human agronomist baseline (planned pilot).
- Hardware conditions: Lab (25°C) + simulated greenhouse thermal chamber.
- Reproducibility: Scripts + exact model tags + quantisation files committed in repo.

## Next Steps
- Publish full measured results for top 3 models on real Hailo-10H hardware.
- Run domain-specific distillation from Qwen2.5-7B using Byte-Size-Kai corpus (IP asset potential).
- Add vision + multimodal benchmarks (YOLO variants compiled for Hailo).

**Open-weight, hardware-optimised models are a core part of our sovereign edge moat.** We own the weights and the optimisation, not rent API calls.
