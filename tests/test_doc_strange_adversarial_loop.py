from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def test_doc_strange_adversarial_loop_reports_revenue_as_blocker() -> None:
    proc = subprocess.run(
        [sys.executable, "scripts/doc_strange_adversarial_loop.py"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    payload = json.loads(proc.stdout)
    assert payload["status"] == "yellow"
    assert payload["next_move"] == "sell_pilot"
    assert "revenue_gate_blocked" in payload["risks"]
    assert payload["public_boundary"]["fresh_start_disclosure_present"] is True
    assert (ROOT / "logs-evidence" / "doc_strange_adversarial_latest.json").exists()
    assert (ROOT / "logs-evidence" / "doc_strange_adversarial_latest.md").exists()
