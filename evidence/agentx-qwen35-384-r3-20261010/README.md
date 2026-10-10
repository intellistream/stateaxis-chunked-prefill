# AgentX Qwen3.5-35B-A3B repeated ON/OFF — 384-token candidate

Evidence label: `real-online-repeated-workload-scoped-positive-experimental`;
performance qualification: `false`.

Three matched pairs used six fresh vLLM services on two Ascend 910B2 devices. The
frozen 32-request agent-research dataset ran at 1 RPS with 256 forced output tokens,
temperature 0, seed 0, BF16, TP2, eager mode, and identical server limits. The only
arm difference was activation of
`org.vllm-hust.stateaxis-chunked-prefill` through Extension Manager/ECPA.

| Pair | ON output tok/s | OFF output tok/s | Throughput change | ON mean TPOT | OFF mean TPOT | TPOT change |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 72.662 | 70.352 | +3.28% | 335.26 ms | 352.76 ms | -4.96% |
| 2 | 83.713 | 77.304 | +8.29% | 272.72 ms | 307.86 ms | -11.42% |
| 3 | 86.740 | 76.894 | +12.80% | 249.25 ms | 294.94 ms | -15.49% |
| Primary-metric median run | 83.713 | 76.894 | +8.87% | 272.72 ms | 294.94 ms | -7.54% |

Every run completed 32/32 requests with identical input/output length vectors (6,374
input and 8,192 output tokens). Each ON run emitted `chunks_applied=6` and
`tokens_deferred=822`. The selected median-throughput runs reduce P99 TTFT by 4.33%
and P99 TPOT by 5.75%, but regress mean TTFT by 24.41% and median TTFT by 2.20%.
All metrics in this comparison come from the selected actual run; metrics were not
independently cherry-picked across repeats.

This is a workload-scoped positive result, not broad performance qualification.
Service startup and latency varied materially across repeats. Peak HBM and end-to-end
latency percentiles were not sampled, the campaign order did not implement the
predeclared alternating arm order, and generated text was not byte-identical across
independent services. The source of that variation was not isolated, and no strict
numerical or semantic equivalence gate was run. Those omissions keep the
MOD default-off and `performance_qualified=false`.

Raw evidence is retained outside Git under
`/root/stateaxis-benchmark-evidence/chunked-prefill-agentx-384-20261010/`; the first
OFF arm is retained under
`/root/stateaxis-benchmark-evidence/chunked-prefill-agentx-256-20261010/off-r1/`.
`RESULT.json` binds every raw file, dataset, config, source identity, metric, and
known limitation.
