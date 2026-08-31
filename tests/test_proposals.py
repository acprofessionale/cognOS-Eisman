import json
import tempfile
import unittest
from pathlib import Path

from capture.capture import ingest
from capture.proposals import write_proposal
from capture.real_photo_gate import GateError, run_gate


class ProposalTests(unittest.TestCase):
    def _capture(self, base: Path, payload: bytes = b"fake-jpeg-bytes") -> tuple[Path, Path, dict]:
        source = base / "photo.jpg"
        source.write_bytes(payload)
        root = base / "store"
        result = ingest(source, root, "raw note")
        return root, Path(result["receipt_path"]), result["receipt"]

    def test_proposal_does_not_mutate_raw_receipt(self):
        with tempfile.TemporaryDirectory() as td:
            base = Path(td)
            root, receipt_path, receipt = self._capture(base)
            before = receipt_path.read_bytes()

            result = write_proposal(
                receipt_path,
                root,
                "OBSERVATION",
                "Possible wine bottle visible in the image",
                "AI_PROPOSED",
                0.73,
            )

            self.assertEqual(receipt_path.read_bytes(), before)
            proposal = result["proposal"]
            self.assertEqual(proposal["proposal_state"], "PROPOSED")
            self.assertEqual(proposal["review_state"], "PENDING")
            self.assertEqual(proposal["publication_class"], "DENY")
            self.assertIsNone(proposal["canonical_entity_ref"])
            self.assertEqual(proposal["source_capture"]["capture_id"], receipt["capture_id"])
            self.assertEqual(proposal["source_capture"]["sha256"], receipt["content"]["sha256"])
            self.assertEqual(
                proposal["source_capture"]["receipt_ref"],
                f"inbox/{receipt['capture_id']}.json",
            )
            self.assertFalse(Path(proposal["source_capture"]["receipt_ref"]).is_absolute())

    def test_rejects_non_deny_source(self):
        with tempfile.TemporaryDirectory() as td:
            base = Path(td)
            root, receipt_path, _ = self._capture(base)
            receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
            receipt["publication_class"] = "PUBLIC"
            receipt_path.write_text(json.dumps(receipt), encoding="utf-8")

            with self.assertRaisesRegex(ValueError, "must be DENY"):
                write_proposal(receipt_path, root, "CLAIM", "x", "HUMAN_ASSERTED", 0.5)

    def test_rejects_non_raw_capture_schema(self):
        with tempfile.TemporaryDirectory() as td:
            base = Path(td)
            root, receipt_path, _ = self._capture(base)
            receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
            receipt["schema_id"] = "example/not-a-raw-capture"
            receipt_path.write_text(json.dumps(receipt), encoding="utf-8")

            with self.assertRaisesRegex(ValueError, "raw-capture v1"):
                write_proposal(receipt_path, root, "CLAIM", "x", "HUMAN_ASSERTED", 0.5)

    def test_rejects_raw_capture_with_derived_assertions(self):
        with tempfile.TemporaryDirectory() as td:
            base = Path(td)
            root, receipt_path, _ = self._capture(base)
            receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
            receipt["derived_assertions"] = ["not raw anymore"]
            receipt_path.write_text(json.dumps(receipt), encoding="utf-8")

            with self.assertRaisesRegex(ValueError, "inference-free"):
                write_proposal(receipt_path, root, "CLAIM", "x", "HUMAN_ASSERTED", 0.5)

    def test_rejects_object_ref_inconsistent_with_digest(self):
        with tempfile.TemporaryDirectory() as td:
            base = Path(td)
            root, receipt_path, _ = self._capture(base)
            receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
            receipt["content"]["object_ref"] = "objects/sha256/00/not-the-object"
            receipt_path.write_text(json.dumps(receipt), encoding="utf-8")

            with self.assertRaisesRegex(ValueError, "object_ref"):
                write_proposal(receipt_path, root, "CLAIM", "x", "HUMAN_ASSERTED", 0.5)

    def test_rejects_invalid_confidence(self):
        with tempfile.TemporaryDirectory() as td:
            base = Path(td)
            root, receipt_path, _ = self._capture(base)
            with self.assertRaisesRegex(ValueError, "confidence"):
                write_proposal(receipt_path, root, "CLAIM", "x", "AI_PROPOSED", 1.1)

    def test_rejects_receipt_outside_capture_root(self):
        with tempfile.TemporaryDirectory() as td:
            base = Path(td)
            root, receipt_path, _ = self._capture(base)
            other_root = base / "other"
            with self.assertRaisesRegex(ValueError, "inside the configured capture root"):
                write_proposal(receipt_path, other_root, "CLAIM", "x", "AI_PROPOSED", 0.5)

    def test_real_photo_gate_mechanics_pass_and_cleanup_ephemeral_proposal(self):
        with tempfile.TemporaryDirectory() as td:
            base = Path(td)
            root, receipt_path, receipt = self._capture(base, b"real-device-equivalent-test-bytes")
            before = receipt_path.read_bytes()

            evidence = run_gate(root, receipt["content"]["sha256"])

            self.assertEqual(evidence["verdict"], "REAL_PHOTO_PROPOSAL_GATE_PASS")
            self.assertTrue(evidence["raw_receipt_unchanged"])
            self.assertFalse(evidence["canonical_promotion"])
            self.assertFalse(evidence["semantic_image_assertion"])
            self.assertTrue(evidence["proposal_ephemeral"])
            self.assertTrue(evidence["proposal_cleanup"])
            self.assertEqual(len(evidence["proposal_sha256"]), 64)
            self.assertEqual(receipt_path.read_bytes(), before)
            self.assertFalse((root / evidence["ephemeral_proposal_ref"]).exists())

    def test_real_photo_gate_blocks_tampered_object(self):
        with tempfile.TemporaryDirectory() as td:
            base = Path(td)
            root, _, receipt = self._capture(base)
            object_path = root / receipt["content"]["object_ref"]
            object_path.write_bytes(b"tampered")

            with self.assertRaisesRegex(GateError, "digest"):
                run_gate(root, receipt["content"]["sha256"])

    def test_real_photo_gate_requires_capture_id_when_digest_is_ambiguous(self):
        with tempfile.TemporaryDirectory() as td:
            base = Path(td)
            source = base / "photo.jpg"
            source.write_bytes(b"same-bytes")
            root = base / "store"
            first = ingest(source, root, None)["receipt"]
            second = ingest(source, root, None)["receipt"]
            digest = first["content"]["sha256"]

            with self.assertRaisesRegex(GateError, "multiple receipts"):
                run_gate(root, digest)

            evidence = run_gate(root, digest, second["capture_id"])
            self.assertEqual(evidence["capture_id"], second["capture_id"])
            self.assertTrue(evidence["proposal_cleanup"])


if __name__ == "__main__":
    unittest.main()
