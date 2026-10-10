import hashlib
import json
from pathlib import Path

from vllm_hust_ext.manifest import activation_blocker, load_manifest

import stateaxis_chunked_prefill


def test_policy_is_discoverable_and_experimentally_activatable() -> None:
    manifest = load_manifest(
        Path(stateaxis_chunked_prefill.__file__).with_name(
            "vllm-hust-extension-v0.3.json"
        )
    )
    assert manifest.bundle_id == "org.vllm-hust.stateaxis-chunked-prefill"
    assert manifest.bundle_version == "0.2.2"
    assert manifest.schema_version == "0.3-experimental"
    assert activation_blocker(manifest) is None
    additional = dict(manifest.activation.additional_config)
    research_manifest = Path(stateaxis_chunked_prefill.__file__).parents[2] / (
        "RESEARCH_MANIFEST.json"
    )
    assert (
        additional["stateaxis_mod"]["manifest_sha256"]
        == hashlib.sha256(research_manifest.read_bytes()).hexdigest()
    )
    assert additional["stateaxis_mod"]["performance_qualified"] is False
    assert additional["stateaxis_chunked_prefill"] == {
        "chunk_tokens": 384,
        "contention_only": True,
        "inplace_continuation": True,
    }


def test_research_manifest_matches_package_contract() -> None:
    research_manifest = Path(stateaxis_chunked_prefill.__file__).parents[2] / (
        "RESEARCH_MANIFEST.json"
    )
    payload = json.loads(research_manifest.read_text())
    assert payload["mod_id"] == stateaxis_chunked_prefill.MOD_ID
    assert payload["version"] == "0.2.2"
    assert payload["mechanism"] == {
        "name": "contention-aware-prefill-chunk",
        "chunk_tokens": 384,
        "contention_only": True,
        "inplace_continuation": True,
    }
    assert payload["qualification"]["performance_qualified"] is False
    assert (
        payload["qualification"]["evidence_label"]
        == "real-online-repeated-workload-scoped-positive-experimental"
    )

    provenance = json.loads((research_manifest.parent / "PROVENANCE.json").read_text())
    assert (
        provenance["implementation_boundary"]["research_manifest_sha256"]
        == hashlib.sha256(research_manifest.read_bytes()).hexdigest()
    )
