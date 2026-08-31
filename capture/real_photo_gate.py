#!/usr/bin/env python3
"""Exercise proposal creation against an existing real-photo capture receipt.

This gate is intentionally host-local. It locates a previously ingested capture
by SHA-256, verifies the content-addressed object, creates one non-canonical
proposal, and proves that the raw receipt bytes were not mutated.

It does not inspect image semantics, promote knowledge, publish content, or call
an AI provider.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from capture.capture import sha256_file
from capture.proposals import load_receipt, write_proposal

GATE_TEXT = (
    "Host validation exercise: proposal envelope created from a previously "
    "validated raw capture; no semantic image assertion is made."
)


class GateError(RuntimeError):
    pass


def _inside(root: Path, candidate: Path) -> Path:
    root = root.expanduser().resolve(strict=True)
    candidate = candidate.expanduser().resolve(strict=True)
    try:
        candidate.relative_to(root)
    except ValueError as exc:
        raise GateError(f"path escapes capture root: {candidate}") from exc
    return candidate


def find_receipt(root: Path, digest: str, capture_id: str | None = None) -> Path:
    if len(digest) != 64 or any(ch not in "0123456789abcdef" for ch in digest.lower()):
        raise GateError("sha256 must be 64 hexadecimal characters")
    root = root.expanduser().resolve(strict=True)
    inbox = root / "inbox"
    if not inbox.is_dir():
        raise GateError(f"capture inbox not found under {root}")

    matches: list[tuple[str, Path]] = []
    for path in sorted(inbox.glob("cap_*.json")):
        try:
            receipt = load_receipt(path)
        except (OSError, json.JSONDecodeError, ValueError):
            continue
        if receipt["content"]["sha256"].lower() == digest.lower():
            matches.append((receipt["capture_id"], path))

    if capture_id:
        matches = [item for item in matches if item[0] == capture_id]
    if not matches:
        raise GateError("no matching capture receipt found")
    if len(matches) > 1:
        ids = ", ".join(item[0] for item in matches)
        raise GateError(f"multiple receipts match this digest; rerun with --capture-id: {ids}")
    return matches[0][1]


def run_gate(root: Path, digest: str, capture_id: str | None = None) -> dict:
    root = root.expanduser().resolve(strict=True)
    receipt_path = find_receipt(root, digest, capture_id)
    receipt_before = receipt_path.read_bytes()
    receipt = load_receipt(receipt_path)

    object_path = _inside(root, root / receipt["content"]["object_ref"])
    object_digest = sha256_file(object_path)
    if object_digest != receipt["content"]["sha256"]:
        raise GateError("content-addressed object digest does not match receipt")
    if object_digest.lower() != digest.lower():
        raise GateError("requested digest does not match stored object")

    result = write_proposal(
        receipt_path,
        root,
        "OBSERVATION",
        GATE_TEXT,
        "AI_PROPOSED",
        1.0,
    )

    receipt_after = receipt_path.read_bytes()
    if receipt_after != receipt_before:
        raise GateError("raw capture receipt mutated during proposal creation")

    proposal_path = _inside(root, Path(result["proposal_path"]))
    proposal = json.loads(proposal_path.read_text(encoding="utf-8"))
    expected_source = {
        "capture_id": receipt["capture_id"],
        "sha256": receipt["content"]["sha256"],
        "receipt_ref": receipt_path.relative_to(root).as_posix(),
    }
    if proposal.get("source_capture") != expected_source:
        raise GateError("proposal source linkage does not match raw capture")
    if proposal.get("proposal_state") != "PROPOSED":
        raise GateError("proposal_state is not PROPOSED")
    if proposal.get("review_state") != "PENDING":
        raise GateError("review_state is not PENDING")
    if proposal.get("publication_class") != "DENY":
        raise GateError("publication_class is not DENY")
    if proposal.get("canonical_entity_ref") is not None:
        raise GateError("proposal unexpectedly contains a canonical entity reference")

    return {
        "verdict": "REAL_PHOTO_PROPOSAL_GATE_PASS",
        "capture_id": receipt["capture_id"],
        "source_sha256": digest.lower(),
        "receipt_ref": receipt_path.relative_to(root).as_posix(),
        "object_ref": object_path.relative_to(root).as_posix(),
        "proposal_id": proposal["proposal_id"],
        "proposal_ref": proposal_path.relative_to(root).as_posix(),
        "raw_receipt_unchanged": True,
        "proposal_state": proposal["proposal_state"],
        "review_state": proposal["review_state"],
        "publication_class": proposal["publication_class"],
        "canonical_promotion": False,
        "semantic_image_assertion": False,
    }


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run the PR #8 real-photo proposal evidence gate")
    parser.add_argument("--root", type=Path, default=Path.home() / ".cognos-eisman" / "capture")
    parser.add_argument("--sha256", required=True)
    parser.add_argument("--capture-id", default=None)
    return parser


def main() -> int:
    args = _parser().parse_args()
    try:
        result = run_gate(args.root, args.sha256, args.capture_id)
    except (OSError, json.JSONDecodeError, ValueError, GateError) as exc:
        print(json.dumps({"verdict": "REAL_PHOTO_PROPOSAL_GATE_BLOCKED", "error": str(exc)}))
        return 2
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
