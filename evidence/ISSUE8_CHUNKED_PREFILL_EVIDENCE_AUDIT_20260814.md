# Issue #8 chunked-prefill evidence audit — 2026-08-14

> **Point-in-time report — not current repository status.** Current
> classification lives in [`NATIVE_ENGINE_STATUS.md`](../../NATIVE_ENGINE_STATUS.md).

## Decision

Two tested production-shaped mechanisms are negative and remain default-off:

- V181's resumable fixed-K cursor/requeue path was exact online but its K768 and
  K1089 variants lost roughly 35% throughput and made cold TTFT materially worse.
- V203--V208 tested a distinct layer-16 prefill/decode safe point. V204 proved
  the component mechanism; V205--V207 did not actually interleave decode. V208
  activated all five observed safe points, but throughput fell 4.4104%, cold
  TTFT rose 27.04%, hot TPOT rose 1.30%, and HBM rose 48 MiB.

This rejects those implementations, not the entire design space. Issue #8 stays
open because its pre-registered multi-length/concurrency and fault matrix has
not been completed.

## Capacity-17 R8 audit

The later R8 evidence was never an additional formal campaign. Its own metadata
calls the cold runs `native-mixed-hot-cold-correctness-smoke` and expressly
forbids throughput/formal-latency claims. Re-aggregation found:

| Median of three cold runs | Atomic control | K1089 candidate | Candidate change |
|---|---:|---:|---:|
| request/s | 7.011813 | 6.908211 | -1.4775% |
| hot wall P50 (ms) | 1104.371 | 1248.821 | +13.0798% |
| hot wall P95 (ms) | 1107.828 | 1254.525 | +13.2418% |
| hot TPOT P95 (ms) | 35.479 | 40.250 | +13.4469% |
| cold TTFT P50 (ms) | 1357.383 | 1390.265 | +2.4224% |
| cold TTFT P95 (ms) | 1358.040 | 1391.433 | +2.4589% |
| cold wall P95 (ms) | 2260.360 | 2297.068 | +1.6240% |
| peak HBM (MiB) | 43,922 | 43,940 | +18 MiB |

Each cold run contains 60 exact-hot and four exact forced-cold P2177/O32
requests. Candidate execution doubles prefill batches from four to eight, so
the treatment did activate. All six runs bind one official local `.23` image,
physical NPU0, prompt, oracle, model artifact, server and worker identity within
the intended arm/config distinction.

The files named warm1--warm3 are only four-token retained-decision lifecycle
replays: 64 exact hits, zero executor batches and one stale-generation rejection
per run. They do not exercise chunking and are excluded from performance
interpretation.

## Identity correction and claim boundary

R8 metadata incorrectly labels the frozen model as Qwen2.5-7B. Its authoritative
manifest records hidden size 5120, 48 layers and 29,540,067,328 tensor bytes,
which identifies the frozen 14B geometry. The stale label is preserved in raw
evidence and explicitly rejected; it was not silently rewritten.

The cold result files also carry a stale `claim_scope` naming “V183 capacity34”.
Every audited run instead binds `state_capacity=17`, execution-plan revision 10
and the R8 artifact identity. The normalized record preserves and rejects that
string rather than using it as provenance.

The normalized record and source-file SHA-256 values are under
[`results/issue8-chunked-prefill-evidence-audit-20260814/`](../../../results/issue8-chunked-prefill-evidence-audit-20260814).
No new timing sample was collected. The result supports “tested variants
negative”; it does not support “Issue #8 acceptance exhausted” or a general
claim that chunked prefill cannot work.

## 2026-08-15 R13c closure update

The repository subsequently completed the previously missing frozen matrix.
R13c covers 2,177/8,192/16,384 prompt tokens, concurrency 1/8/16/32 and three
matched fresh-process repeats per control/candidate arm: 36 cells and 72 arms.
All accepted arms are exact and recycle temporary state. Candidate authority
activates in every contention run with zero bypass; c1 correctly fail-closes.

The mechanism materially bounds long prefill execution, but every contention
cell fails the preregistered joint guardrail. For 8K/16K, maximum continuous
prefill falls roughly 82--92% and hot TPOT P99 improves in several cells, while
request throughput regresses 12--24% and cold TTFT P95 regresses 39--117%.
The 2,177-token contention cells regress throughput 21--26% and cold TTFT about
116--118%. No matrix point qualifies as positive. Issue #8's current frozen
candidate is therefore rejected and remains default-off; this is not a claim
that every possible chunking design has been exhausted.

The aggregate and all accepted/rejected run references are frozen under
[`results/issue8-long-matrix-20260815-r13c-aggregate/`](../../../results/issue8-long-matrix-20260815-r13c-aggregate).
