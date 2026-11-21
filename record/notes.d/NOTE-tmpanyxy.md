---
status: Skimmed
paper: LIT-tmpa91zo
title: 'Fedus and colleagues — Hyperbolic discounting and learning over multiple horizons'
version: 1
history:
- version: 1
  date: '2026-11-21'
  note: >-
    Read on 2026-11-21 by a delegated reader from arXiv 1902.06865v3, as
    the main stand-in for Sozou (LIT-tmpk0e2v): the abstract, §§1–3 and
    Appendix B.2–B.3; §§4–9 (the method and Atari experiments) and the
    other appendices skipped. Status Skimmed because the paper's own
    method was not read. Running notes on the branch
    claude/readers/discounting-sozou. Quotations rechecked by the filer by
    script.
date: '2026-11-21'
summary: >-
  Restates Sozou: discounting as survival with an uncertain hazard is the
  Laplace transform of the prior over the hazard; an exponential prior
  gives 1/(1 + kt), uniform and gamma priors other forms. Its own method,
  learning over many exponential horizons to approximate hyperbolic
  discounting, was not read beyond the abstract.
---
<!-- inactive-ok-file: LIT-tmpk0e2v CLAIM-tmpve51e CLAIM-tmp6q7ma — Proposed, Deferred, Unfetched or new; filed in this contribution of 2026-11-21 or the ones it builds on -->

# NOTE-tmpanyxy: Fedus and colleagues — Hyperbolic discounting and learning over multiple horizons

## Key results

1. **Exponential prior** (§3.2): "Sozou (1998) shows that under an exponential prior of hazard p(λ) = 1/k exp(−λ/k) the expected survival rate for the agent is hyperbolic s(t) = 1/(1 + kt)"; derivation in Appendix B.2.
2. **Other priors** (Fig. 2, "We reproduce two figures from Sozou (1998)"): uniform → (1 − e^(−kt))/(kt); gamma → 1/(1 + bt)^c; delta → e^(−λt); all with the same mean hazard.
3. **Known hazard** (§1): exponential discounting is consistent with "a known constant risk to the agent in the environment".
4. **Interpretation** (§1): "Sozou (1998) demonstrates that this behavior is mathematically consistent with the agent maintaining some uncertainty over the hazard rate in the environment".
5. **Its own aim** (abstract): approximating hyperbolic discount functions by learning over multiple horizons, many exponential discount factors.

## Bearing on the record

- **[LEAD-tmp7rohc](../leads.d/LEAD-tmp7rohc.md)** (step 2): confirms the discounting half through Sozou: hyperbolic discounting is exponential discounting averaged over a spread of hazard rates, exactly so for an exponential spread; a gamma spread gives a power-law tail.
- **[THEORY-1117](../theory.d/THEORY-1117.md)** (Ainslie; qualifies): a rational, survival-based origin for the curve Ainslie takes as given; Ainslie's account of interests is untouched.
- **[CLAIM-tmpve51e](../claims.d/CLAIM-tmpve51e.md)** (qualifies): its E[a^W] = r/(r + ln(1/a)) is the same Laplace-transform integral with the roles of rate and time swapped: the wait is random there, the rate here.
- **[CLAIM-tmp6q7ma](../claims.d/CLAIM-tmp6q7ma.md)** (grounds).

## Limitations

Sozou's own text not read; the gamma result rests on a reproduced figure; the paper's reinforcement-learning method not read.
