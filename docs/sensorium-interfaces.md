# Sensorium Interfaces

This document defines the public, contest-safe biometric interface layer for `ATG Responder Coherence Operator`.

## Purpose

The sensorium layer is a trend-only input surface. It helps the wellness app route daily prompts and aggregate sponsor reporting. It does **not** diagnose, treat, or infer a medical condition.

## Primary-Safe Evidence Basis

The strongest public evidence base supports **state estimation from wearable signals**, not diagnosis.

- Wearable and smartphone streams can support personalized mood or depressed-state modeling.
- Sleep, activity, heart rate, HRV, skin temperature, EDA, and contextual usage can all contribute to state estimation.
- These signals remain probabilistic and noisy, so they should be used for wellness routing and human review, not clinical conclusions.

The closest primary-source match I found to the study you referenced is *Personalized machine learning of depressed mood using wearables* in *Translational Psychiatry*. I am treating that line of evidence as support for passive sensing of mood-state trends, not for diagnosis.

## Supported Device Families

The public demo may accept normalized inputs from:

- Apple Watch
- Fitbit
- Oura Ring
- Garmin watches
- WHOOP bands
- HeartMath sensors
- Muse headbands
- generic BLE / CSV / JSON wearable exports

## Supported Signal Classes

The public demo may ingest:

- heart rate
- HRV
- sleep duration and timing
- activity and movement
- respiration rate
- skin temperature
- electrodermal activity
- subjective check-ins
- session adherence
- recovery trend scores

## Allowed Uses

- daily wellness routing
- enhanced Flow support
- foundational purpose / transcendence support
- sleep and recovery prompts
- aggregate sponsor dashboards
- human review queue triggers
- pilot evidence export

## Disallowed Uses

- diagnosis
- treatment claims
- medication advice
- fitness-for-duty decisions
- return-to-duty decisions
- clinical triage by AI
- crisis-response automation
- PHI exposure in the public repo

## Interface Rule

Every sensor stream must be treated as a **low-confidence trend input**. The routing output should remain conservative and fail closed when the signal is missing, noisy, or outside the public wellness lane.
