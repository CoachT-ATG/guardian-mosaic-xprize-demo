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
See `docs/sensorium-interfaces.md` for the supported biometric device families, signal classes, and the trend-only rule.
See `docs/grant-requirements-matrix.md` for the grant requirement ladder and the MVP feature set that exceeds it.
See `docs/freemium-linkedin-gtm.md` for the iOS freemium and LinkedIn conversion strategy.
See `docs/linkedin-launch-copy.md` for draft outbound posts only.
See `docs/beta-to-pilot-pipeline.md` for the measurable signup-to-pilot funnel.
See `docs/ios-beta-launch-checklist.md` for the required Apple / Google setup steps.
See `docs/apple-launch-kit.md` for the official Apple pages and setup requirements.
See `docs/apple-release-assets.md` for the App Store Connect and TestFlight metadata drafts.
See `docs/xcode-project-setup.md` for the exact Xcode build and signing steps.
See `ios/README.md` for the native SwiftUI scaffold.
See `docs/compliance-boundary.md` for the minimum-disclosure and existing-subscriptions policy.
See `docs/goal-routing.md` for the bounded execution policy.
See `docs/regulatory-roadmap.md` for the public wellness track versus future regulated track split.
See `docs/xprize-win-map.md` for the requirement-to-win mapping and freshness guard.
See `docs/dogfood-strategy-loop.md` for the ideation / RO learning / QNPA / adversarial iteration loop.

## What This Repo Contains

- `appsheet/`: no-code app configuration and anonymized data model
- `gemini/`: sanitized prompt templates and sample API payloads
- `logs-evidence/`: sample session logs, redacted revenue proof, metrics summary
- `architecture/`: public system overview
- `docs/`: launch, corpus-selection, evidence-model, sensorium, goal-routing, regulatory-roadmap, and win-map notes for the public demo
- `scripts/`: local receipt writers, adversarial analysis, and guardrails for the contest-safe proof path
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
3. Open `index.html` or `app/index.html` to launch the local demo.
4. Load the AppSheet config from `appsheet/appsheet-config.json`.
5. Use the prompt templates in `gemini/system-prompts/`.
6. Run `python3 scripts/google_ops_runner.py` to generate a local Google-ops receipt and demo-safe coherence briefs.
7. Replace placeholder sample files with redacted pilot artifacts.
8. Publish the demo video link in `demo-video/README.md`.

## Compliance Notes

- Public repo only.
- No proprietary internal Mosaic code.
- No PII.
- No secret keys.
- No private customer data.
- One Google Cloud product and one Gemini API call remain in the minimal deployed proof path if the app uses LLM functionality.
- The public demo is ready to generate local Google-ops receipts with `scripts/google_ops_runner.py` so the repo stays judge-reproducible even before live credentials are wired.
- The Doc Strange adversarial loop is available in `scripts/doc_strange_adversarial_loop.py` and must stay green before any promotion decision.
- The public demo also exposes the five-pillar progression and the grant-fit ladder so the user-facing product story stays aligned with law-enforcement wellness funding requirements.

## Fresh Start And Provenance

This is a fresh contest submission, not a dump of the full private Mosaic archive.

- Any pre-existing work is referenced explicitly in `docs/preexisting-work-disclosure.md`.
- Only the contest-safe subset is included here.
- Proprietary methods, trade secrets, patent-sensitive details, and private internal artifacts remain outside the public repo.
- Any strategic decisions in this repo should be red-teamed through the dogfood / Doc Strange adversarial loop before promotion.

## Funding and Pilot Model

The clean operating model is:

`agency applicant -> public pilot -> contracted implementation -> evidence package`

Use the current funding map in `memory/2026-05-25_guardian_mosaic_funding_map.md` and keep the first paid pilot small, measurable, and agency-centered.
