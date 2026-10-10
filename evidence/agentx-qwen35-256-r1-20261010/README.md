# AgentX Qwen3.5-35B-A3B matched ON/OFF — 256-token candidate

Evidence label: `real-online-single-pair-negative`; performance qualification: `false`.

This run used the frozen 32-request agent-research custom dataset at 1 RPS with 256 forced output
tokens per request, temperature 0, seed 0, BF16, TP2, eager mode, and two Ascend 910B2 devices.
Each arm used a fresh vLLM service. The only arm difference was activation of
`org.vllm-hust.stateaxis-chunked-prefill` v0.2.1 through Extension Manager/ECPA.

| Metric | ON | OFF | ON relative to OFF |
| --- | ---: | ---: | ---: |
| Successful requests | 32 | 32 | equal |
| Output throughput | 70.469 tok/s | 70.352 tok/s | +0.17% |
| Mean TTFT | 11472.58 ms | 7462.07 ms | +53.75% (worse) |
| P99 TTFT | 23308.20 ms | 14731.83 ms | +58.22% (worse) |
| Mean TPOT | 340.54 ms | 352.76 ms | -3.46% (better) |
| P99 TPOT | 418.43 ms | 422.49 ms | -0.96% (better) |

ON emitted `chunks_applied=11` and `tokens_deferred=1704`; OFF exposed no MOD-effect series. Input
and output token-length vectors are identical across arms (6374 total input and 8192 total output
tokens). The mechanism therefore activated, but the small decode-latency gain does not offset the
large prefill/TTFT regression. This candidate is a negative result and must not be represented as a
general or repeated performance gain.

Raw evidence is retained outside Git at
`/root/stateaxis-benchmark-evidence/chunked-prefill-agentx-256-20261010/`:

- ON `raw.json`: `bd0a8233154de08e8e02b970d4b89aec9316b2cf22f384dca1d6ec94584480cf`
- OFF `raw.json`: `4131641fa9732cf671588d9f9073e1d54ca13b6b5f79388d717ea1407d48b1c1`
- Dataset: `13347797c3660c5b3efbf8912bbcb76d8bba50ffee5f77944b95b9cde1b6ca3c`
- ON config: `bc291a3496a2085e948f5585277e0f7b8f7c693ff40c6d0f7850ed68860522f2`
- OFF config: `9cc72b65f5ec15056b1a0b2d7d89210a85f7b35cb1de948e9b1ce85540032455`

Frozen source identities: MOD merge `959b14f47ab248560a77b91222ff21766f80f407`, StateAxis
mechanism merge `729e4b9a311c595869fa70b464ba2c41a9775e21`, Ascend integration
`913841ce6cbeed2e23a29ea40a8d91b158a9ebe0`, and Extension Manager merge
`7d98891a2e7546f46de9b84d7549e831a85e3c20`.
