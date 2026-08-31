#!/usr/bin/env python3
"""Create non-canonical proposal envelopes linked to immutable raw captures.

No AI provider is invoked here. This module persists a proposal produced by an
external actor (human or AI) without mutating the raw capture receipt. Proposal
creation is not canonical promotion and grants no publication authority.
"""

from __future__ import annotations

import argparse
import json
import os
import tempfile
import uuid
from datetime import datetime, timezone
from pathlib import Path

SCHEMA_ID = "cognos-eisman/capture-proposal/v1"
NORMATIVE_SCOPE = "VERTICAL_EISMAN_PROVISIONAL"
PUBLICATION_CLASS = "DENY"
ALLOWED_MODES = {"HUMAN_ASSERTED", "AI_PROPOSED", "AI_EXTRACTED"}
ALLOWED_TYPES = {"OBSERVATION", "CLAIM", "RELATION", "ENTITY_CANDIDATE"}


def load_receipt(path: Path) -> dict:
    receipt = json.loads(path.expanduser().resolve(strict=True).read_text(encoding="utf-8"))
    required = ["capture_id", "capture_state", "publication_class", "content"]
    missing = [key for key in required if key not in receipt]
    if missing:
        raise ValueError(f"capture receipt missing required fields: {missing}")
    if receipt["capture_state"] != "INBOX":
        raise ValueError("proposal source capture must remain INBOX")
    if receipt["publication_class"] != "DENY":
        raise ValueError("proposal source capture must be DENY")
    content = receipt.get("content", {})
    if content.get("digest_algorithm") != "sha256":
        raise ValueError("capture receipt digest algorithm must be sha256")
    sha256 = content.get("sha256")
    if not isinstance(sha256, str) or len(sha256) != 64:
        raise ValueError("capture receipt has invalid sha256")
    if not isinstance(content.get("object_ref"), str) or not content["object_ref"]:
        raise ValueError("capture receipt has invalid object_ref")
    return receipt


def write_proposal(
    receipt_path: Path,
    root: Path,
    proposal_type: str,
    text: str,
    assertion_mode: str,
    confidence: float,
) -> dict:
    if proposal_type not in ALLOWED_TYPES:
        raise ValueError(f"unsupported proposal_type: {proposal_type}")
    if assertion_mode not in ALLOWED_MODES:
        raise ValueError(f"unsupported assertion_mode: {assertion_mode}")
    if not 0.0 <= confidence <= 1.0:
        raise ValueError("confidence must be between 0 and 1")
    if not text.strip():
        raise ValueError("text must not be empty")

    root = root.expanduser().resolve()
    receipt_path = receipt_path.expanduser().resolve(strict=True)
    try:
        receipt_ref = receipt_path.relative_to(root).as_posix()
    except ValueError as exc:
        raise ValueError("capture receipt must be inside the configured capture root") from exc

    receipt = load_receipt(receipt_path)
    proposal_id = f"prop_{uuid.uuid4().hex}"
    created_at = datetime.now(timezone.utc).isoformat()

    proposal = {
        "schema_id": SCHEMA_ID,
        "schema_version": 1,
        "normative_scope": NORMATIVE_SCOPE,
        "proposal_id": proposal_id,
        "proposal_state": "PROPOSED",
        "review_state": "PENDING",
        "publication_class": PUBLICATION_CLASS,
        "created_at_utc": created_at,
        "assertion_mode": assertion_mode,
        "proposal_type": proposal_type,
        "confidence": confidence,
        "text": text,
        "source_capture": {
            "capture_id": receipt["capture_id"],
            "sha256": receipt["content"]["sha256"],
            "receipt_ref": receipt_ref,
        },
        "canonical_entity_ref": None,
    }

    out_dir = root / "proposals"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{proposal_id}.json"
    payload = json.dumps(proposal, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=out_dir, delete=False) as tmp:
        tmp.write(payload)
        tmp_path = Path(tmp.name)
    os.replace(tmp_path, out_path)
    return {"proposal": proposal, "proposal_path": str(out_path)}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Persist a non-canonical proposal for one raw capture")
    parser.add_argument("receipt", type=Path)
    parser.add_argument("--root", type=Path, default=Path.home() / ".cognos-eisman" / "capture")
    parser.add_argument("--type", dest="proposal_type", choices=sorted(ALLOWED_TYPES), required=True)
    parser.add_argument("--mode", dest="assertion_mode", choices=sorted(ALLOWED_MODES), required=True)
    parser.add_argument("--confidence", type=float, required=True)
    parser.add_argument("--text", required=True)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    result = write_proposal(
        args.receipt,
        args.root,
        args.proposal_type,
        args.text,
        args.assertion_mode,
        args.confidence,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
