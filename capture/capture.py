#!/usr/bin/env python3
"""CognOS-Eisman mobile capture MVP.

Ingests a local file into an immutable, content-addressed object store and writes
an inference-free JSON receipt into an inbox. Standard library only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import mimetypes
import os
import shutil
import tempfile
import uuid
from datetime import datetime, timezone
from pathlib import Path

SCHEMA_ID = "cognos-eisman/raw-capture/v1"
NORMATIVE_SCOPE = "VERTICAL_EISMAN_PROVISIONAL"
PUBLICATION_CLASS = "DENY"


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        while chunk := fh.read(chunk_size):
            digest.update(chunk)
    return digest.hexdigest()


def atomic_copy_verified(source: Path, destination: Path, expected_sha256: str) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists():
        actual = sha256_file(destination)
        if actual != expected_sha256:
            raise RuntimeError(f"existing object digest mismatch: {destination}")
        return

    with tempfile.NamedTemporaryFile(dir=destination.parent, delete=False) as tmp:
        tmp_path = Path(tmp.name)
        with source.open("rb") as src:
            shutil.copyfileobj(src, tmp)

    try:
        actual = sha256_file(tmp_path)
        if actual != expected_sha256:
            raise RuntimeError("copied object digest mismatch")
        os.replace(tmp_path, destination)
    finally:
        if tmp_path.exists():
            tmp_path.unlink()


def ingest(source: Path, root: Path, note: str | None = None) -> dict:
    source = source.expanduser().resolve(strict=True)
    if not source.is_file():
        raise ValueError(f"not a regular file: {source}")

    digest = sha256_file(source)
    object_path = root / "objects" / "sha256" / digest[:2] / digest
    atomic_copy_verified(source, object_path, digest)

    stat = source.stat()
    captured_at = datetime.now(timezone.utc).isoformat()
    source_modified_at = datetime.fromtimestamp(stat.st_mtime, timezone.utc).isoformat()
    capture_id = f"cap_{uuid.uuid4().hex}"
    media_type, _ = mimetypes.guess_type(source.name)

    receipt = {
        "schema_id": SCHEMA_ID,
        "schema_version": 1,
        "normative_scope": NORMATIVE_SCOPE,
        "capture_id": capture_id,
        "capture_state": "INBOX",
        "publication_class": PUBLICATION_CLASS,
        "captured_at_utc": captured_at,
        "source": {
            "kind": "LOCAL_FILE",
            "original_filename": source.name,
            "source_modified_at_utc": source_modified_at,
            "size_bytes": stat.st_size,
            "media_type": media_type or "application/octet-stream",
        },
        "content": {
            "digest_algorithm": "sha256",
            "sha256": digest,
            "object_ref": str(object_path.relative_to(root)),
        },
        "raw_note": note,
        "derived_assertions": [],
    }

    inbox = root / "inbox"
    inbox.mkdir(parents=True, exist_ok=True)
    receipt_path = inbox / f"{capture_id}.json"

    payload = json.dumps(receipt, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=inbox, delete=False) as tmp:
        tmp.write(payload)
        tmp_path = Path(tmp.name)
    os.replace(tmp_path, receipt_path)

    return {"receipt": receipt, "receipt_path": str(receipt_path)}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Capture evidence into the CognOS-Eisman inbox")
    sub = parser.add_subparsers(dest="command", required=True)

    ingest_parser = sub.add_parser("ingest", help="ingest one file without inference")
    ingest_parser.add_argument("file", type=Path)
    ingest_parser.add_argument(
        "--root",
        type=Path,
        default=Path.home() / ".cognos-eisman" / "capture",
        help="local capture root (default: ~/.cognos-eisman/capture)",
    )
    ingest_parser.add_argument(
        "--note",
        default=None,
        help="optional verbatim human note; stored as raw input, never promoted automatically",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.command == "ingest":
        result = ingest(args.file, args.root.expanduser(), args.note)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
