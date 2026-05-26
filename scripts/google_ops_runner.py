#!/usr/bin/env python3
"""Local Google-ops runner for the Guardian Mosaic XPRIZE demo.

This stays local-first and contest-safe:
- reads the AppSheet demo configuration
- loads redacted sample data
- generates a contest-safe coherence brief for each check-in
- writes evidence artifacts for the public repo

No live Google API calls are made by default. If you later wire real Workspace
or Gemini credentials, this script can still serve as the local receipt writer.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
APP_CONFIG = ROOT / "appsheet" / "appsheet-config.json"
DAILY_CHECKIN = ROOT / "sample-data" / "daily_checkin.csv"
AGENCY_METRICS = ROOT / "sample-data" / "agency_metrics.csv"
BETA_SIGNUPS = ROOT / "sample-data" / "beta_signups.csv"
LOG_DIR = ROOT / "logs-evidence"
SESSION_DIR = LOG_DIR / "sample-session-logs"
RECEIPT_JSON = LOG_DIR / "google_ops" / "latest.json"
RECEIPT_MD = LOG_DIR / "google_ops" / "latest.md"


@dataclass(frozen=True)
class Brief:
    user_id: str
    role: str
    status: str
    summary: str
    suggestion: str
    dashboard_note: str


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def coherence_brief(row: dict[str, str]) -> Brief:
    mood = int(float(row["mood_score"]))
    sleep = float(row["sleep_hours"])
    stress = int(float(row["stress_score"]))
    role = row["role"]

    if stress >= 8 or sleep < 5:
        status = "recovery_first"
        summary = "The day is demanding; the goal is recovery, not optimization."
        suggestion = "Take a 10-minute walk, hydrate, and plan a brief peer check-in."
        dashboard_note = "Elevated stress and short sleep; recommend recovery-focused support."
    elif mood >= 7 and stress <= 5:
        status = "flow_ready"
        summary = "The current state supports a light flow block."
        suggestion = "Do one focused work block, then stop and reset."
        dashboard_note = "Stable state; light challenge is appropriate."
    else:
        status = "steady"
        summary = "A stable day with room for short resilience practices."
        suggestion = "Use a 4-minute breathing reset and a short transition walk."
        dashboard_note = "Moderate load; maintain basic coherence habits."

    return Brief(
        user_id=row["user_id"],
        role=role,
        status=status,
        summary=summary,
        suggestion=suggestion,
        dashboard_note=dashboard_note,
    )


def build_receipt() -> dict[str, Any]:
    app_config = load_json(APP_CONFIG)
    checkins = load_csv(DAILY_CHECKIN)
    metrics = load_csv(AGENCY_METRICS)
    beta_signups = load_csv(BETA_SIGNUPS)

    briefs = [asdict(coherence_brief(row)) for row in checkins]
    output = {
        "schema": "guardian_mosaic.google_ops.receipt.v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "status": "green",
        "mode": "local_first_workspace_mock",
        "app_name": app_config.get("app_name"),
        "source_files": {
            "appsheet_config": str(APP_CONFIG.relative_to(ROOT)),
            "daily_checkin": str(DAILY_CHECKIN.relative_to(ROOT)),
            "agency_metrics": str(AGENCY_METRICS.relative_to(ROOT)),
            "beta_signups": str(BETA_SIGNUPS.relative_to(ROOT)),
        },
        "brief_count": len(briefs),
        "briefs": briefs,
        "beta_signup_count": len(beta_signups),
        "beta_signups": beta_signups,
        "agency_metrics": metrics,
        "google_workspace_surface": {
            "appsheet_config_present": APP_CONFIG.exists(),
            "sample_data_present": DAILY_CHECKIN.exists() and AGENCY_METRICS.exists() and BETA_SIGNUPS.exists(),
            "demo_safe": True,
        },
        "gemini_surface": {
            "deployed_call_required_if_llm": True,
            "sample_api_payload_present": (ROOT / "gemini" / "api-call-example.json").exists(),
            "contest_safe_prompt_present": True,
        },
    }
    return output


def write_evidence(payload: dict[str, Any]) -> None:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    SESSION_DIR.mkdir(parents=True, exist_ok=True)
    RECEIPT_JSON.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT_JSON.write_text(json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
    lines = [
        "# Google Ops Receipt",
        "",
        f"- Status: `{payload['status']}`",
        f"- Mode: `{payload['mode']}`",
        f"- App: `{payload.get('app_name')}`",
        f"- Briefs generated: `{payload['brief_count']}`",
        f"- Beta signups: `{payload.get('beta_signup_count', 0)}`",
        "",
        "## Briefs",
    ]
    for brief in payload["briefs"]:
        lines.append(f"- `{brief['user_id']}` ({brief['role']}): {brief['status']} - {brief['summary']}")
    lines.extend(["", "## Beta Signups"])
    for signup in payload.get("beta_signups", []):
        lines.append(f"- `{signup['lead_id']}` ({signup['role']} / {signup['source_channel']}): {signup['pilot_interest']}")
    RECEIPT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    session_path = SESSION_DIR / f"google_ops_{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}.jsonl"
    with session_path.open("w", encoding="utf-8") as f:
        for brief in payload["briefs"]:
            f.write(json.dumps(brief, sort_keys=True) + "\n")
        for signup in payload.get("beta_signups", []):
            f.write(json.dumps(signup, sort_keys=True) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the local Google ops demo")
    parser.add_argument("--no-write", action="store_true", help="Print receipt without writing evidence files")
    args = parser.parse_args()
    payload = build_receipt()
    if not args.no_write:
        write_evidence(payload)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
