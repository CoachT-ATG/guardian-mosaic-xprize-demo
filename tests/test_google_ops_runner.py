from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def test_google_ops_runner_writes_evidence(tmp_path: Path) -> None:
    proc = subprocess.run(
        [sys.executable, "scripts/google_ops_runner.py"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    payload = json.loads(proc.stdout)
    assert payload["status"] == "green"
    assert payload["brief_count"] == 3
    assert payload["beta_signup_count"] == 3
    assert payload["google_workspace_surface"]["appsheet_config_present"] is True
    assert payload["gemini_surface"]["sample_api_payload_present"] is True
    assert (ROOT / "logs-evidence" / "google_ops" / "latest.json").exists()
    assert (ROOT / "logs-evidence" / "google_ops" / "latest.md").exists()
