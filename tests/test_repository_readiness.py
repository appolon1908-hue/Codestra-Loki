from __future__ import annotations

import hashlib
import json
import subprocess
import tarfile
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadinessTests(unittest.TestCase):
    def test_validator(self) -> None:
        subprocess.run(["python3", "scripts/validate_repository_readiness.py"], cwd=ROOT, check=True)

    def test_bundle_is_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            first = Path(directory) / "first.tar.gz"
            second = Path(directory) / "second.tar.gz"
            for output in (first, second):
                subprocess.run(["python3", "scripts/build_config_bundle.py", "--output", str(output)], cwd=ROOT, check=True)
            self.assertEqual(hashlib.sha256(first.read_bytes()).digest(), hashlib.sha256(second.read_bytes()).digest())
            manifest = json.loads((ROOT / "codestra/release/config-bundle.manifest.json").read_text())
            with tarfile.open(first) as archive:
                self.assertEqual(set(archive.getnames()), set(manifest["files"]) | {"codestra/release/config-bundle.manifest.json"})

    def test_secret_file_boundary(self) -> None:
        compose = (ROOT / "codestra/deploy/compose.candidate.yaml").read_text()
        config = (ROOT / "codestra/config/loki.yaml").read_text()
        self.assertIn("AWS_SHARED_CREDENTIALS_FILE: /run/secrets/loki_s3_credentials", compose)
        self.assertNotIn("LOKI_S3_SECRET_ACCESS_KEY", compose + config)
        self.assertNotIn("access_key_id:", config)


if __name__ == "__main__":
    unittest.main()
