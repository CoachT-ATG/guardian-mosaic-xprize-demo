# Layered Evidence Model

## Purpose

This document translates the broader ATG timing model into the safest and most useful operating policy for the `ATG Responder Coherence Operator`.

The core rule is simple:
- use the slowest, richest evidence only as a slow calibration layer
- use the fastest signals for daily routing
- keep the public XPRIZE demo wellness-safe and non-clinical

## Layer 1: Structural Prior

Primary role:
- long-horizon baseline
- eligibility and contraindication context
- coarse stratification

Candidate signals:
- WGS
- family history
- durable trait information

Policy:
- off by default in the public demo
- only appropriate for a separate privacy-gated research cohort
- never used for day-to-day timing in the public pilot

## Layer 2: Physiologic Calibration

Primary role:
- update the model over weeks to months
- define the current state of the person
- refine which intervention families are appropriate

Candidate signals:
- routine labs
- richer blood panels
- optional biomarker trends
- metabolic and recovery markers

Policy:
- useful for sponsor-side reporting and long-horizon coaching
- not required for the public pilot
- never exposed as diagnosis or treatment output

## Layer 3: Real-Time Routing

Primary role:
- decide what to recommend today
- decide when to recommend it
- decide whether to defer or simplify the prompt

Candidate signals:
- HRV
- sleep duration and sleep quality
- resting heart rate
- activity and load
- schedule
- mood
- self-reported readiness
- optional wearable or CGM trends

Policy:
- this is the core layer for the public demo
- this is where daily coaching and coherence briefs should run
- this layer should drive the default human review queue

## Layer 4: Slow Recalibration

Primary role:
- long-horizon drift detection
- quarterly or slower review
- trend-based course correction

Candidate signals:
- methylation outputs
- biological-age composites
- pace-of-aging measures

Policy:
- never a same-day control signal
- useful only as a slow recalibration input
- must not be presented as proof of reversal, cure, or diagnosis

## ATG Responder Coherence Operator Default Policy

For the public-safety MVP:
- route daily recommendations from Layer 3
- use Layer 2 only if a sponsor or pilot cohort has provided the data
- keep Layer 1 out of the default demo
- use Layer 4 only for optional quarterly review

Recommended daily decision order:
1. check safety and wellness boundaries
1. read schedule and sleep/recovery state
1. read HRV or equivalent readiness trend
1. generate a low-risk coherence brief
1. escalate to human review if distress or instability is detected

## Why This Is Optimal

This structure matches the evidence hierarchy:
- fast state signals drive timing
- slower biological signals inform calibration
- genomic data informs priors, not daily routing
- methylation informs drift, not minute-by-minute prompts

It is also the safest way to ship:
- no diagnostic claims
- no PHI default
- no clinical treatment logic
- no overfitting to a single biomarker

## Product Conclusion

The best implementation of ATG for the public XPRIZE path is not a blended score.
It is a layered control system with explicit timing roles, hard safety boundaries, and human oversight.
