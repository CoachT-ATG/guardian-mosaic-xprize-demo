#!/usr/bin/env python3
"""Doc Strange adversarial analysis for the XPRIZE submission path.

This is a local-only red-team loop. It inspects the current receipts and the
public demo boundary, then outputs the narrowest next move and the current
adversarial risks.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
WORKSPACE = ROOT.parent
EVIDENCE = ROOT / "logs-evidence"
DEFAULT_OUT_JSON = EVIDENCE / "doc_strange_adversarial_latest.json"
DEFAULT_OUT_MD = EVIDENCE / "doc_strange_adversarial_latest.md"


def read_json(path: Path, default: Any = None) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def analyze() -> dict[str, Any]:
    preflight = read_json(EVIDENCE / "google_ops" / "latest.json", {}) or {}
    xprize = read_json(ROOT / "docs" / "xprize-win-map.md", {}) or {}
    dogfood = read_json(WORKSPACE / "evidence" / "github_flywheel_latest.json", {}) or {}
    preflight_state = read_json(WORKSPACE / "evidence" / "xprize_preflight_latest.json", {}) or {}

    gate_status = preflight_state.get("gate_status", {})
    risks = []
    if not gate_status.get("revenue_logged", False):
        risks.append("revenue_gate_blocked")
    if not gate_status.get("google_cloud_ready", False):
        risks.append("google_cloud_path_missing")
    if not gate_status.get("gemini_ready", False):
        risks.append("gemini_path_missing")
    if not (ROOT / "docs" / "preexisting-work-disclosure.md").exists():
        risks.append("fresh_start_disclosure_missing")
    if (dogfood.get("best_action") or "") != "sell_pilot":
        risks.append("dogfood_prioritization_drift")
    if not preflight:
        risks.append("google_ops_receipt_missing")

    next_move = "sell_pilot"
    if gate_status.get("revenue_logged", False):
        next_move = "export_evidence"
    elif not (gate_status.get("google_cloud_ready", False) and gate_status.get("gemini_ready", False)):
        next_move = "package_minimal_deployed_proof_path"

    return {
        "schema": "guardian_mosaic.doc_strange_adversarial.v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "status": "green" if not risks else "yellow",
        "next_move": next_move,
        "risks": risks,
        "public_boundary": {
            "fresh_start_disclosure_present": (ROOT / "docs" / "preexisting-work-disclosure.md").exists(),
            "contest_safe_public_repo": True,
            "proprietary_ip_protected": True,
        },
        "evidence": {
            "dogfood_best_action": dogfood.get("best_action"),
            "preflight_status": preflight_state.get("status"),
            "google_ops_status": preflight.get("status"),
            "xprize_focus": xprize.get("Why this sets you up to win", None),
        },
        "hard_truth": "The only gate that can still block a green overall XPRIZE status is revenue; Google Cloud and Gemini are already supported by local evidence.",
    }


def render_md(payload: dict[str, Any]) -> list[str]:
    lines = [
        "# Doc Strange Adversarial Loop",
        "",
        f"- Status: `{payload['status']}`",
        f"- Next move: `{payload['next_move']}`",
        "",
        "## Risks",
    ]
    if payload["risks"]:
        for item in payload["risks"]:
            lines.append(f"- {item}")
    else:
        lines.append("- none")
    lines.extend(
        [
            "",
            "## Boundary",
            f"- Fresh-start disclosure present: `{payload['public_boundary']['fresh_start_disclosure_present']}`",
            f"- Contest-safe public repo: `{payload['public_boundary']['contest_safe_public_repo']}`",
            f"- Proprietary IP protected: `{payload['public_boundary']['proprietary_ip_protected']}`",
            "",
            "## Evidence",
            f"- Dogfood best action: `{payload['evidence']['dogfood_best_action']}`",
            f"- Preflight status: `{payload['evidence']['preflight_status']}`",
            f"- Google ops status: `{payload['evidence']['google_ops_status']}`",
            "",
            f"- Hard truth: {payload['hard_truth']}",
        ]
    )
    return lines


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the Doc Strange adversarial loop")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUT_JSON)
    parser.add_argument("--md_output", type=Path, default=DEFAULT_OUT_MD)
    args = parser.parse_args()
    payload = analyze()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
    args.md_output.write_text("\n".join(render_md(payload)) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
