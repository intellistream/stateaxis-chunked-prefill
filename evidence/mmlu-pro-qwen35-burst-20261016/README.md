# Qwen3.5 MMLU-Pro burst boundary

This evidence records the vLLM 0.25.1 host port and matched real-online
screening of 1,024- and 1,280-token contention-aware prefill chunks. The
official client submits at infinite request rate.

The 8-request smoke was useful for confirming activation and exposing the
TTFT/TPOT tradeoff, but did not predict the 40-request result. The 1,280-token
candidate is therefore rejected for this burst workload. This does not erase
the earlier 1-RPS AgentX result; it narrows where that result applies.

Raw logs and all failed/negative cells remain in the external roots listed in
`RESULT.json`.
