# stateaxis-chunked-prefill

Extension ID: `org.vllm-hust.stateaxis-chunked-prefill`

Decode-fair token-budgeted chunked prefill.

This repository is the independent MOD boundary for StateAxis issues [#8](https://github.com/Qixin-Gaoke/stateaxis/issues/8).
Version `0.2.0.dev0` is an active, default-off experimental policy. Extension Manager
binds the immutable `RESEARCH_MANIFEST.json` digest into the launch and StateAxis owns
the scheduler hook and effect counters. The split does not inherit correctness,
device, performance, or publication qualification from the aggregate StateAxis
repository.

## Evidence boundary

Status: **negative**.

The 36-cell exact matrix reduced blocking but repeatedly regressed throughput and cold TTFT.

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
1,024 tokens only while decode requests are active and reports applied chunks,
deferred tokens, and no-contention bypasses. It remains unqualified until it passes
exactness, lifecycle, release, failure-recovery, and matched real-online gates.

## Validate

```bash
python -m pip install -e '.[test]'
pytest -q
```

Maintainer: Shuhao Zhang (Tony), directly responsible; no advisor is declared.
