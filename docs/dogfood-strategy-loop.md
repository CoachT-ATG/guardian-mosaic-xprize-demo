# Dogfood Strategy Loop

This document defines the public-safe control loop used to improve the XPRIZE submission without disclosing proprietary internals.

## Operating principle

Run the product the same way a judge or pilot customer would experience it, then use the resulting receipts to choose the next move.

The loop has four parts:

1. **Ideation Monte Carlo** - generate a small set of candidate next actions.
2. **RO Learning** - score each action against real evidence, revenue, user activity, safety, and cost.
3. **QNPA Hybrid Rounds** - explore multiple bounded variants, then exploit the best one.
4. **Doc Strange Adversarial Analysis** - red-team every candidate for privacy leakage, clinical overreach, missing evidence, and unnecessary spend.
5. **Doc Strange Evidence Sweep** - compare candidate actions against the current preflight, disclosure, and repo guardrails before promotion.

## What it optimizes

- real pilot revenue
- user evidence
- contest compliance
- safety boundaries
- freshness of receipts
- demo readiness
- cost discipline

## What it will not do

- reveal proprietary Mosaic internals
- include PHI
- claim diagnosis or treatment
- inflate telemetry
- let stale accountability or integrity receipts drive evidence packaging

## Forcing action

Before the submission packet or evidence export is promoted, refresh accountability and integrity receipts first.

If the freshness guard reports stale receipts, the loop must repair them before advancing.

## Why this matters

The judges will not reward poetry. They will reward:

- a real business
- a working product
- safe scope
- current evidence
- clear logs
- a minimal and defensible Google Cloud/Gemini path

This loop is how the project keeps moving without drifting into stale proof, hidden cost, or scope creep.
