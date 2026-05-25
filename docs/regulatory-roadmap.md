# Regulatory Roadmap

## Public XPRIZE Track

The current submission is a wellness-safe, contest-facing product:
- daily resilience and coherence support
- self-report and biometrics-driven routing
- no diagnosis
- no treatment claims
- no PHI in the public repo
- no return-to-duty or fitness-for-duty outputs

This is the only path that belongs in the public GitHub submission.

## Future Private Track

Any later regulated product version should be treated as a separate private effort:
- separate repository or private branch
- separate validation artifacts
- separate regulatory review
- separate change-control process

That future track may eventually support SaMD and PCCP-style versioning, but those details should remain outside the contest-facing repo until the regulated path is actually pursued.

## Control Principles

- keep the public contest demo minimal
- keep regulated features private
- separate wellness support from clinical claims
- use human review and change logs for any future regulated evolution

## Boundary Rule

If a feature would change the product from wellness support into regulated clinical software, it does not belong in the public XPRIZE submission.
