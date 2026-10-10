"""Contract constants for the StateAxis contention-aware prefill policy."""

from dataclasses import dataclass

MOD_ID = "org.vllm-hust.stateaxis-chunked-prefill"


@dataclass(frozen=True, slots=True)
class ChunkedPrefillConfig:
    """Manifest-owned configuration consumed by the StateAxis host."""

    chunk_tokens: int = 384
    contention_only: bool = True
    inplace_continuation: bool = True
