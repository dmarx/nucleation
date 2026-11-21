---
status: Open
title: 'Track the cutoff of an event-size distribution, and how it scales with system size, rather than its exponent, as a sign that a system is approaching a continuous transition, and compare it with the variance and autocorrelation warnings of critical slowing down'
version: 1
stage: idea
method:
- formal
- empirical
tags:
- complex-systems
- probabilistic-modeling
date: '2026-11-21'
line:
- formal-apparatus
advances:
- CLAIM-tmplb1ow
- CLAIM-tmpr9au6
- QUESTION-091
- THEORY-1315
summary: >-
  A's proposal, from A7 §5 and A8 §6 of the exchange "Rich Get Richer
  Power Laws" (2026-11-20), answering the owner's U5: "Is the heavy tail
  an enduring property of the system, or is it expanding as the system
  approaches a critical threshold? If the latter, tracking the tail's
  cutoff, rather than merely fitting its power-law exponent, could provide
  information about proximity to the transition". With finite-size
  scaling, s_max ~ L^D, as the test that a power law is critical. The
  assistant adds what a test must face, which A leaves out: the data
  cost, the finite-size confound, and the overlap with the variance
  warning the record holds ([THEORY-1315](../theory.d/THEORY-1315.md)). The wording is A's (the other
  assistant in the exchange "Rich Get Richer Power Laws", A7 and A8);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmp8h6nt CLAIM-tmpvrbdt CASE-tmpi5vfh — Proposed or new; the claims and case filed with this lead from the same exchange -->

# LEAD-tmpp8z85: Track the cutoff of an event-size distribution, and how it scales with system size, rather than its exponent, as a sign that a system is approaching a continuous transition, and compare it with the variance and autocorrelation warnings of critical slowing down

## Sketch (A's)

A7 §5: "the most consequential early signal of criticality might not be a
visibly changing bulk of the distribution. It might be the expanding range
of possible extreme outcomes." The test is to fit s^(−τ)·f(s/s_c) at
several times or several values of a control parameter and to watch s_c,
not τ. A8 §6 adds the system-size version: at criticality the cutoff
grows as s_max ~ L^D, "In contrast, sufficiently far below criticality,
the intrinsic cutoff remains small compared with the system size", so
"finite-size scaling" is "one of the strongest ways to investigate whether
observed power laws reflect genuine critical phenomena". It is also A3
§5's test for self-organized criticality ([CLAIM-tmp8h6nt](../claims.d/CLAIM-tmp8h6nt.md)).

## What a test must face (the assistant's)

This lead is the cutoff row of [LEAD-tmpng7or](LEAD-tmpng7or.md)'s protocol, which reads the
mechanism behind a power law from its cutoff, collapse, dynamics and
response together and subsumes the cutoff test. What this lead adds is
the comparison with the variance and autocorrelation warnings below.

- **Data cost.** In the Poisson cascade ([CASE-tmpi5vfh](../cases.d/CASE-tmpi5vfh.md)), the share of
  cascades beyond s_c is about 0.05·(1 − R): 5.8 × 10⁻³ at R = 0.9 and
  5.0 × 10⁻⁵ at 0.999. So the events that locate the cutoff become rarer
  in proportion to the distance from the transition, while the cutoff
  itself grows as (1 − R)^(−2). To see the cutoff at R = 0.999 one needs
  of order 10⁵ cascades for a handful beyond it. The signal grows as the
  sample needed to see it grows faster.
- **The finite-size confound.** Near the transition, the intrinsic cutoff
  passes the system's own limit L^D, and from then on the observed cutoff
  stops moving whatever R does. A rising cutoff that then stalls may be
  approach followed by saturation, not retreat. A8 §6's size scaling
  separates the two only if L can be varied.
- **Overlap with the record's warnings.** [THEORY-1315](../theory.d/THEORY-1315.md) holds rising
  variance and lag-1 autocorrelation near a fold. In the cascade the
  variance R/(1 − R)^3 is carried by the tail, so it rises because the
  cutoff does. The two are not independent evidence. What the cutoff
  might add is robustness to the bulk: it ignores the many small events
  that dominate a variance estimate's noise. Whether that is a gain is the
  formal part of this lead.
- **Not every transition.** [THEORY-1315](../theory.d/THEORY-1315.md)'s scope caveat applies: such
  signals mark nearness to "a broad class of thresholds", not which kind.
  A first-order transition shows a gap, not a runaway cutoff
  ([CLAIM-tmpvrbdt](../claims.d/CLAIM-tmpvrbdt.md)). An organization's cascades ([QUESTION-091](../questions.d/QUESTION-091.md)) would be a
  place to try it.

## What would count

Formal: for the cascade and for one spatial model, compare the error in
estimating distance to the transition from s_c and from the sample
variance, at equal numbers of events. Empirical: a system with a known
control parameter and size, cascades or avalanches, in which s_c tracks
the parameter before the variance does. The lead fails if the cutoff
estimate is never better than the variance at equal data.
