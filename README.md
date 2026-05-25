# Guardian Mosaic - Gemini XPRIZE Public Demo

Official public demonstration repository for the XPRIZE-facing, contest-safe subset of Guardian Mosaic.

## Product Wedge

`ATG Responder Coherence Operator`

This is the public-safety MVP: an AI-assisted resilience and coherence operating system for law enforcement, fire, EMS, dispatch, training academies, peer-support teams, chaplains, and municipal wellness staff.

The promise is narrow on purpose:
- daily resilience prompts
- sleep and recovery check-ins
- tactical decompression routines
- peer-support routing
- aggregate dashboarding for sponsors
- AI-generated coherence briefs with human review

What it does not do:
- diagnosis
- treatment
- medication advice
- PHI handling
- return-to-duty or fitness-for-duty decisions
- psychedelic guidance
- clinical claims

## Cost Model

The recommended launch path is low-out-of-pocket and local-first:
- build in Workspace and locally first
- sell one small paid public-safety pilot immediately
- use Google Cloud and Gemini only for the minimum deployed proof path required by the contest
- keep budgets, quotas, and feature scope hard-limited

See `docs/launch-plan.md` for the execution path.
See `docs/layered-evidence-model.md` for the timing and biomarker policy.
See `docs/compliance-boundary.md` for the minimum-disclosure and existing-subscriptions policy.
See `docs/goal-routing.md` for the bounded execution policy.
See `docs/regulatory-roadmap.md` for the public wellness track versus future regulated track split.

## What This Repo Contains

- `appsheet/`: no-code app configuration and anonymized data model
- `gemini/`: sanitized prompt templates and sample API payloads
- `logs-evidence/`: sample session logs, redacted revenue proof, metrics summary
- `architecture/`: public system overview
- `docs/`: launch, corpus-selection, and evidence-model notes for the public demo
- `docs/`: launch, corpus-selection, evidence-model, and goal-routing notes for the public demo
- `docs/`: launch, corpus-selection, evidence-model, goal-routing, and regulatory-roadmap notes for the public demo
- `src/`: minimal provenance logging example
- `demo-video/`: link and instructions for the public demo video

## What Is Intentionally Excluded

- Mosaic Organism internal logic
- 6D Tesseract / QNPA spines
- Proprietary edge sandbox components
- Private decision trees, parameters, and sovereign telemetry
- Any private customer data or proprietary deployment secrets

## Quick Start

1. Review `architecture/tech-stack.md`.
2. Review `docs/launch-plan.md`.
3. Load the AppSheet config from `appsheet/appsheet-config.json`.
4. Use the prompt templates in `gemini/system-prompts/`.
5. Replace placeholder sample files with redacted pilot artifacts.
6. Publish the demo video link in `demo-video/README.md`.

## Compliance Notes

- Public repo only.
- No proprietary internal Mosaic code.
- No PII.
- No secret keys.
- No private customer data.
- One Google Cloud product and one Gemini API call remain in the minimal deployed proof path if the app uses LLM functionality.

## Funding and Pilot Model

The clean operating model is:

`agency applicant -> public pilot -> contracted implementation -> evidence package`

Use the current funding map in `memory/2026-05-25_guardian_mosaic_funding_map.md` and keep the first paid pilot small, measurable, and agency-centered.
