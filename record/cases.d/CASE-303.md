---
number: 303
status: Proposed
formerly:
- CASE-tmpi5vfh
title: 'Cascade sizes of a Poisson branching process below and at criticality'
version: 1
standing: stipulated
kind: construction
tags:
- probabilistic-modeling
- complex-systems
date: '2026-11-21'
line:
- formal-apparatus
illustrates:
- CLAIM-829
- CLAIM-832
summary: >-
  A's worked example at A5 §1, A7 §2 to §3 and A8 §2 to §4 of the exchange
  "Rich Get Richer Power Laws" (2026-11-20): each event triggers a
  Poisson(R) number of further events, and the total size S of a cascade
  follows the Borel law. Every figure A gives was rechecked with python3 -I
  from the closed form. A's cutoff table holds to within 16% at R = 0.8 and
  0.7% at R = 0.99, as A says ("increasingly accurate as R approaches 1").
  Stipulated: a model, not a measured system. The checks and the added
  rows are the assistant's (Claude, in this session). The example's
  wording is A's (the other assistant in the exchange "Rich Get Richer
  Power Laws", A5, A7 and A8); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-829 CLAIM-832 CLAIM-845 CLAIM-815 — Proposed or new; the claims filed with this case from the same exchange -->
<!-- inactive-ok-file: THEORY-2177 — Proposed; the reading of Reed and Hughes, 2026-11-22 -->

<!-- inactive-ok-file: THEORY-2168 — Proposed or new; the reading of Azizpour and colleagues, 2026-11-22 -->

# CASE-303: Cascade sizes of a Poisson branching process below and at criticality

## The model

Each event triggers a Poisson-distributed number of further events with
mean R. The total size S of the cascade started by one event has the Borel
law

    P(S = s) = e^(−Rs) (Rs)^(s−1) / s!,

which for large s is (2π)^(−1/2) R^(−1) s^(−3/2) e^(−s/s_c) with
s_c = 1/(R − 1 − ln R) ≈ 2/(1 − R)^2 near R = 1. The law is the
hitting-time identity of [CLAIM-815](../claims.d/CLAIM-815.md) applied to Poisson offspring. Its
mean is 1/(1 − R) and its variance R/(1 − R)^3 for R < 1. At R = 1 the
cascade still ends with probability one, but its mean is infinite.

## What A said, rechecked

- **The cutoff (A7 §2).** A's table: R = 0.8, 0.9, 0.95, 0.99, 0.999
  give s_c ≈ 50, 200, 800, 20,000, 2,000,000. The exact 1/(R − 1 − ln R)
  gives 43, 187, 773, 19,867 and 1,998,667. A's are the near-critical
  approximation 2/(1 − R)^2, which A labels as such. The overstatement
  is 16% at 0.8 and 7% at 0.9. A's "from 0.99 to 0.999 … the cutoff
  grows a hundredfold" holds for both forms (100.6× exact).
- **The asymptotic form.** log P + 1.5 log s + s/s_c is constant to six
  digits between s = 10 s_c and 30 s_c at R = 0.9 and 0.99.
- **The single-event share and the mean (A8 §3).** P(S = 1) = e^(−R):
  60.7%, 40.7%, 37.2%, 36.8% and 36.8% at R = 0.5, 0.9, 0.99, 0.999 and 1;
  means 2, 10, 100, 1,000 and infinite. All as A gives them.
- **Conditional exceedance (A8 §4).** At R = 1, P(S > 10s | S > s) is
  0.316 from any s ≥ 1,000, A's 10^(−1/2) "≈ 0.316".

## Added rows (the assistant's)

- No gap: the law is strictly decreasing in s at every R checked
  ([CLAIM-845](../claims.d/CLAIM-845.md)).
- The bulk holds while the cutoff runs: the median is 2 at R = 0.9, 0.99
  and 0.999, and the share beyond s_c is about 0.05·(1 − R)
  ([CLAIM-829](../claims.d/CLAIM-829.md)).
- Count against total: at R = 0.99 the cascades larger than 1,000 are
  1.66% of cascades and 75.6% of all events; those above 100 are 7.1% and
  92.6% ([CLAIM-832](../claims.d/CLAIM-832.md)).

## The check

```python
import numpy as np
from scipy.special import gammaln
s = np.arange(1, 5_000_001, dtype=float)
def borel(R): return np.exp(-R*s + (s-1)*np.log(R*s) - gammaln(s+1))
for R in [0.8, 0.9, 0.95, 0.99, 0.999]:
    print(R, 1/(R-1-np.log(R)), 2/(1-R)**2)          # cutoff, exact vs A's
p = borel(0.99); m = p*s
print(p[1000:].sum(), m[1000:].sum()/m.sum())      # 1.66% of cascades, 75.6% of events
p = borel(1.0); tail = p[::-1].cumsum()[::-1] + np.sqrt(2/(np.pi*5e6))
print([tail[10*k]/tail[k] for k in (10, 100, 1000, 10000)])  # -> 0.316
```

## What it cannot show

It is the mean-field cascade. Spatial avalanches in low dimensions have
other exponents (A's s^(−3/2) is the Galton–Watson value, which A states
"for a standard branching process with finite, nonzero offspring
variance"), so the 37% and the 3/2 are Poisson- and mean-field-specific.

## Note of 2026-11-22: Azizpour, Priesemann, Zierenberg and Levina, read

Background ([NOTE-2259](../notes.d/NOTE-2259.md), [THEORY-2168](../theory.d/THEORY-2168.md)). The paper's network is a
branching process of this case's kind driven by Poisson input, with the
absorbing-to-active transition at λ = 1; it uses the subcritical regime
for computation, finding the best discrimination of inputs there for
every finite readout window. Nothing in it bears on the cascade-size
distributions this case computes.

## Note of 2026-11-22: Reed and Hughes, read

A **contrast**, with no edge. Reed and Hughes ([LIT-3007](../literature.d/LIT-3007.md), read in
[NOTE-2264](../notes.d/NOTE-2264.md); [THEORY-2177](../theory.d/THEORY-2177.md)) get a power law from a *supercritical*
branching process killed at a geometric generation, exponent 1 + κ with
κ = ln[1/(1 − p)]/ln μ, where this case's s^(−3/2) needs the process
exactly critical. The case is unchanged.
