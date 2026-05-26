# XPRIZE Win Map

This repository is scoped to the contest in the smallest honest way that still satisfies the rules.

Canonical rules governance file: `docs/xprize-rules-governance.md`

## What the rules require

- A real business.
- A public or judge-accessible code repository.
- A working demo the judges can run.
- A sub-3-minute demo video.
- Revenue evidence and user evidence.
- Logs, screenshots, and API usage records.
- At least one Google Cloud product.
- At least one Gemini API call in the deployed app if LLM functionality is part of the product.
- English submission materials.

## How ATG Responder Coherence Operator maps to those rules

- Real business: `ATG Responder Coherence Operator` is the customer-facing pilot offer.
- Devpost project: `https://devpost.com/software/guardian-mosaic`.
- Repository: this repo holds the contest-safe code, docs, demo assets, and evidence templates.
- Working demo: the local-first wellness app and dashboard are the judge-facing proof path.
- Demo video: the product flow can be shown in under three minutes without revealing proprietary internals.
- Revenue evidence: the first paid pilot is the business proof, not a theory deck.
- User evidence: daily check-ins, participation counts, testimonials, and aggregate sponsor reporting.
- Google requirement: the deployment path uses Google Workspace and a minimal Google Cloud/Gemini proof surface.
- Safety boundary: general wellness only, no diagnosis, no treatment, no PHI, no fitness-for-duty.
- Grant alignment: phase one should map cleanly to LEMHWA, VALOR, JMHCP-adjacent collaboration, NIJ safety/health/wellness research priorities, and state/local wellness funding norms.

## The forcing action

Do not let accountability or integrity telemetry drift stale before evidence export or submission packaging.

- If a core receipt is stale or yellow, refresh it locally before using it as evidence.
- Keep the refresh path deterministic and cheap.
- Prefer local receipt repair and integrity replay over new model calls.
- Do not promote a submission packet from stale telemetry.
- Red-team every promotion decision with the Dogfood / Doc Strange adversarial loop before it reaches GitHub or a judge-facing artifact.

## Why this sets you up to win

- It keeps the product inside the safest contest lane.
- It proves real users and real revenue instead of only capability.
- It minimizes spend by using existing subscriptions and a minimal deployed proof path.
- It keeps the judges focused on business viability, working product, and evidence quality.
- It avoids leaking proprietary IP while still showing a credible, differentiated system.
