import json
import tempfile
import unittest
from pathlib import Path

from capture.capture import ingest
from capture.proposals import write_proposal


class ProposalTests(unittest.TestCase):
    def test_proposal_does_not_mutate_raw_receipt(self):
        with tempfile.TemporaryDirectory() as td:
            base = Path(td)
            source = base / "photo.jpg"
            source.write_bytes(b"fake-jpeg-bytes")
            root = base / "store"

            capture_result = ingest(source, root, "raw note")
            receipt_path = Path(capture_result["receipt_path"])
            before = receipt_path.read_bytes()

            result = write_proposal(
                receipt_path,
                root,
                "OBSERVATION",
                "Possible wine bottle visible in the image",
                "AI_PROPOSED",
                0.73,
            )

            after = receipt_path.read_bytes()
            self.assertEqual(before, after)

            proposal = result["proposal"]
            self.assertEqual(proposal["proposal_state"], "PROPOSED")
            self.assertEqual(proposal["review_state"], "PENDING")
            self.assertEqual(proposal["publication_class"], "DENY")
            self.assertEqual(proposal["canonical_entity_ref"], None)
            self.assertEqual(proposal["source_capture"]["capture_id"], capture_result["receipt"]["capture_id"])
            self.assertEqual(proposal["source_capture"]["sha256"], capture_result["receipt"]["content"]["sha256"])

    def test_rejects_invalid_confidence(self):
        with tempfile.TemporaryDirectory() as td:
            base = Path(td)
            source = base / "x.txt"
            source.write_text("x")
            root = base / "store"
            receipt_path = Path(ingest(source, root)["receipt_path"])

            with self.assertRaises(ValueError):
                write_proposal(receipt_path, root, "CLAIM", "x", "AI_PROPOSED", 1.1)

    def test_rejects_non_deny_source_capture(self):
        with tempfile.TemporaryDirectory() as td:
            base = Path(td)
            source = base / "x.txt"
            source.write_text("x")
            root = base / "store"
            result = ingest(source, root)
            receipt_path = Path(result["receipt_path"])
            receipt = json.loads(receipt_path.read_text())
            receipt["publication_class"] = "ALLOW"
            receipt_path.write_text(json.dumps(receipt))

            with self.assertRaises(ValueError):
                write_proposal(receipt_path, root, "CLAIM", "x", "AI_PROPOSED", 0.5)


if __name__ == "__main__":
    unittest.main()
