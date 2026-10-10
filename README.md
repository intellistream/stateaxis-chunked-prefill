# stateaxis-chunked-prefill

Extension ID: `org.vllm-hust.stateaxis-chunked-prefill`

Decode-fair token-budgeted chunked prefill.

This repository is the independent MOD boundary for StateAxis issue #8.
Version `0.2.2` is an active, default-off experimental policy. Extension Manager
binds the immutable `RESEARCH_MANIFEST.json` digest into the launch and StateAxis owns
the scheduler hook and effect counters. The split does not inherit correctness,
device, performance, or publication qualification from the aggregate StateAxis
repository.

## Evidence boundary

Status: **workload-scoped positive, experimental and not performance-qualified**.

Earlier 256-token and long-prefill variants were negative. The 384-token policy has
three independent-service matched ON/OFF pairs on the frozen AgentX/agent-research
workload. All three pairs improved output throughput (+3.28%, +8.29%, and +12.80%)
and mean TPOT (4.96%, 11.42%, and 15.49% lower). The primary-metric median-run
comparison is +8.87% output throughput and 7.54% lower mean TPOT, with a 24.41%
mean-TTFT regression. This is evidence
only for Qwen3.5-35B-A3B, BF16 TP2 eager, 1 RPS, 32 requests, and 256 forced output
tokens; it is not a general chunked-prefill claim.

The copied evidence and its SHA-256 are recorded in `PROVENANCE.json`. Negative,
failed, and inconclusive results are retained. Microbenchmarks and component results
must not be restated as online end-to-end gains.

## Install and inspect

```bash
python -m pip install .
vllm-hust-ext extension inspect org.vllm-hust.stateaxis-chunked-prefill
vllm-hust-ext extension check org.vllm-hust.stateaxis-chunked-prefill
```

Activation requires `experiment_mode`, the exact research-manifest SHA-256, and a
StateAxis host containing the declared policy contract. It caps long prefill work at
384 tokens only while decode requests are active and reports applied chunks,
deferred tokens, and no-contention bypasses. It remains unqualified until it passes
exactness, lifecycle, release, failure-recovery, and matched real-online gates.

The 384-token budget is an explicit AgentX/agent-research candidate, not a general
default recommendation. With Qwen3.5-35B-A3B, the frozen 32-request benchmark corpus
contains 73–555-token prompts; the earlier 1,024-token candidate could not activate on
that corpus, and the 256-token candidate regressed mean TTFT by 53.75%. The repeated
384-token evidence is in `evidence/agentx-qwen35-384-r3-20261010/`. It remains
unqualified because peak HBM and end-to-end latency percentiles were not collected,
and strict output equivalence was not established.

## Validate

```bash
python -m pip install -e '.[test]'
pytest -q
```

Maintainer: Shuhao Zhang (Tony), directly responsible; no advisor is declared.
