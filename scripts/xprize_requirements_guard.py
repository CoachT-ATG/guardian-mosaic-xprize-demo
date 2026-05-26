#!/usr/bin/env python3
"""Lightweight guard for the contest-facing repo requirements.

This enforces:
- fresh-start disclosure exists
- prior work is referenced explicitly
- public repo remains contest-safe
- the Google ops runner is present
"""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    required_files = [
        ROOT / "README.md",
        ROOT / "docs" / "preexisting-work-disclosure.md",
        ROOT / "docs" / "xprize-rules-governance.md",
        ROOT / "docs" / "agency-pilot-offer.md",
        ROOT / "docs" / "xprize-submission-command-center.md",
        ROOT / "scripts" / "google_ops_runner.py",
        ROOT / "logs-evidence" / "google_ops" / "latest.md",
        ROOT / "logs-evidence" / "financial-statement.md",
    ]
    missing = [str(path.relative_to(ROOT)) for path in required_files if not path.exists()]
    if missing:
        print(f"missing_required_files: {missing}")
        return 1

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    disclosure = (ROOT / "docs" / "preexisting-work-disclosure.md").read_text(encoding="utf-8")
    rules = (ROOT / "docs" / "xprize-rules-governance.md").read_text(encoding="utf-8")
    command_center = (ROOT / "docs" / "xprize-submission-command-center.md").read_text(encoding="utf-8")
    checks = [
        ("fresh contest submission", readme),
        ("pre-existing work", readme),
        ("Dogfood / Doc Strange adversarial loop", readme),
        ("pre-existing work", disclosure),
        ("proprietary methods", disclosure),
        ("https://xprize.devpost.com/rules", rules),
        ("Gemini API", rules),
        ("testing@devpost.com", rules),
        ("https://devpost.com/software/guardian-mosaic", command_center),
        ("yellow reason: revenue evidence", command_center),
    ]
    failures = [needle for needle, text in checks if needle.lower() not in text.lower()]
    if failures:
        print(f"missing_required_phrases: {failures}")
        return 2

    print("xprize_requirements_guard:ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
