import hashlib
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "capture" / "capture.py"
spec = importlib.util.spec_from_file_location("cognos_capture", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


class CaptureTests(unittest.TestCase):
    def test_ingest_is_content_addressed_and_inference_free(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "store"
            source = Path(tmp) / "sample.txt"
            source.write_text("evidence\n", encoding="utf-8")

            result = module.ingest(source, root, "verbatim note")
            receipt = result["receipt"]
            digest = hashlib.sha256(b"evidence\n").hexdigest()

            self.assertEqual(receipt["content"]["sha256"], digest)
            self.assertEqual(receipt["publication_class"], "DENY")
            self.assertEqual(receipt["capture_state"], "INBOX")
            self.assertEqual(receipt["raw_note"], "verbatim note")
            self.assertEqual(receipt["derived_assertions"], [])

            object_path = root / receipt["content"]["object_ref"]
            self.assertTrue(object_path.exists())
            self.assertEqual(object_path.read_bytes(), b"evidence\n")

            receipt_path = Path(result["receipt_path"])
            persisted = json.loads(receipt_path.read_text(encoding="utf-8"))
            self.assertEqual(persisted, receipt)

    def test_same_bytes_reuse_object_but_create_distinct_receipts(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "store"
            a = Path(tmp) / "a.txt"
            b = Path(tmp) / "b.txt"
            a.write_bytes(b"same")
            b.write_bytes(b"same")

            first = module.ingest(a, root)
            second = module.ingest(b, root)

            self.assertEqual(first["receipt"]["content"]["sha256"], second["receipt"]["content"]["sha256"])
            self.assertEqual(first["receipt"]["content"]["object_ref"], second["receipt"]["content"]["object_ref"])
            self.assertNotEqual(first["receipt"]["capture_id"], second["receipt"]["capture_id"])


if __name__ == "__main__":
    unittest.main()
