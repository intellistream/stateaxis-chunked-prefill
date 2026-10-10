# ECPA activation-contract evidence

Evidence label: `manager_contract_non_performance`.

The vLLM-HUST Extension Manager 0.3 check, plan, dry-run launch, and real
managed `native_state_engine --assembly-check-only` process all passed
for version 0.2.3. The manager verified the exact `RESEARCH_MANIFEST.json`
SHA-256, host/API/protocol ranges, and rendered the sole activation argument as
`--additional-config` with `experiment_mode=true`, the pinned MOD identity, and
the reviewed 384-token contention-only in-place paged-append contract.

StateAxis tests separately cover strict parsing, stale-digest and unsafe-policy
rejection, matched ON/OFF identity, exact outputs, effect counters, lifecycle
shutdown, and the pre-existing chunk continuation/failure paths. This record is
not accelerator execution and makes no latency, throughput, memory, capacity,
or production-performance claim. The managed process exited normally without
escalation. Historical Qwen3.5-35B-A3B real-online
results remain scoped to `evidence/agentx-qwen35-384-r3-20261010/`.

Reproduce from the repository root:

```bash
VLLM_HUST_EXT_CONFIG=evidence/ecpa-contract-20261010/manager-config.json \
  vllm-hust-ext extension check org.vllm-hust.stateaxis-chunked-prefill
VLLM_HUST_EXT_CONFIG=evidence/ecpa-contract-20261010/manager-config.json \
  vllm-hust-ext extension plan org.vllm-hust.stateaxis-chunked-prefill
VLLM_HUST_EXT_CONFIG=evidence/ecpa-contract-20261010/manager-config.json \
  vllm-hust-ext run --dry-run -- /bin/true
```
