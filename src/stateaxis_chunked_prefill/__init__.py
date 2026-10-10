"""Contract constants for the StateAxis contention-aware prefill policy."""

from dataclasses import dataclass

MOD_ID = "org.vllm-hust.stateaxis-chunked-prefill"


@dataclass(frozen=True, slots=True)
class ChunkedPrefillConfig:
    """Manifest-owned configuration consumed by the StateAxis host."""

    enabled: bool = True
    chunk_tokens: int = 384
    contention_only: bool = True
    inplace_continuation: bool = True
    paged_append_required: bool = True
    fail_closed: bool = True

    def __post_init__(self) -> None:
        if (
            not self.enabled
            or self.chunk_tokens != 384
            or not self.contention_only
            or not self.inplace_continuation
            or not self.paged_append_required
            or not self.fail_closed
        ):
            raise ValueError(
                "chunked-prefill 0.2.3 admits only the pinned 384-token, "
                "contention-only, in-place paged-append, fail-closed contract"
            )


def chunked_prefill() -> ChunkedPrefillConfig:
    """Return the default-off candidate's admitted ON configuration."""

    return ChunkedPrefillConfig()


__all__ = ["MOD_ID", "ChunkedPrefillConfig", "chunked_prefill"]
