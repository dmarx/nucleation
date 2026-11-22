---
number: 211
status: Open
formerly:
- LEAD-tmpp8z85
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
- CLAIM-829
- CLAIM-840
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
<!-- inactive-ok-file: THEORY-tmpehudh CLAIM-tmpfwwrf — Proposed or new; the reading of Bak, Tang and Wiesenfeld and the record's sandpile reproduction, cited in the note of 2026-11-22 -->
<!-- inactive-ok-file: THEORY-tmp6jdas THEORY-tmpw4qgu — Proposed; the readings of 2026-11-22 cited in the notes -->
<!-- inactive-ok-file: CLAIM-803 CLAIM-845 CASE-303 — Proposed or new; the claims and case filed with this lead from the same exchange -->

# LEAD-211: Track the cutoff of an event-size distribution, and how it scales with system size, rather than its exponent, as a sign that a system is approaching a continuous transition, and compare it with the variance and autocorrelation warnings of critical slowing down

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
§5's test for self-organized criticality ([CLAIM-803](../claims.d/CLAIM-803.md)).

## What a test must face (the assistant's)

This lead is the cutoff row of [LEAD-209](LEAD-209.md)'s protocol, which reads the
mechanism behind a power law from its cutoff, collapse, dynamics and
response together and subsumes the cutoff test. What this lead adds is
the comparison with the variance and autocorrelation warnings below.

- **Data cost.** In the Poisson cascade ([CASE-303](../cases.d/CASE-303.md)), the share of
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
  ([CLAIM-845](../claims.d/CLAIM-845.md)). An organization's cascades ([QUESTION-091](../questions.d/QUESTION-091.md)) would be a
  place to try it.

## What would count

Formal: for the cascade and for one spatial model, compare the error in
estimating distance to the transition from s_c and from the sample
variance, at equal numbers of events. Empirical: a system with a known
control parameter and size, cascades or avalanches, in which s_c tracks
the parameter before the variance does. The lead fails if the cutoff
estimate is never better than the variance at equal data.

## Note of 2026-11-22: Newman; Clauset, Shalizi and Newman, read

**Background and method.** Newman ([LIT-2976](../literature.d/LIT-2976.md), [NOTE-tmpa7yd2](../notes.d/NOTE-tmpa7yd2.md),
[THEORY-tmp6jdas](../theory.d/THEORY-tmp6jdas.md)) notes finite-size cutoffs at criticality and the forest
fire's cutoff at the lattice size (§IV.F, p. 22), without using a cutoff
as a test. Clauset, Shalizi and Newman ([LIT-2987](../literature.d/LIT-2987.md), [NOTE-tmphbwdu](../notes.d/NOTE-tmphbwdu.md),
[THEORY-tmpw4qgu](../theory.d/THEORY-tmpw4qgu.md)) give a ready test for a cutoff in one sample (§5.2), and
nothing on its scaling with system size. The lead's step is still open.

## Note of 2026-11-22: Bak, Tang and Wiesenfeld, read; the sandpile run

**A precedent, and a first worked case.** Bak, Tang and Wiesenfeld
(LIT-2992, read in NOTE-tmpnl00y; the reading is THEORY-tmpehudh)
already use this lead's size test, in words only: "The falloff at the
largest cluster sizes is due to finite-size effects, as we checked by
comparing simulations for different array sizes" (p. 383), with no data
shown. The record's reproduction, CLAIM-tmpfwwrf, supplies the data for
the 2-D sandpile: ⟨s²⟩/⟨s⟩ = 92, 467, 2,607 and 15,822 at L = 16, 32, 64
and 128, a cutoff growing roughly as L^2.5, with local exponents still
rising (2.34, 2.48, 2.60). Two lessons for the lead: the cutoff exponent
drifts at these sizes, so a size test needs a factor of eight or more in
L to separate growth from an intrinsic cutoff; and the moment ratio
⟨s²⟩/⟨s⟩ uses every event, while the CCDF's 10⁻⁴ point rests on about
ten of 10⁵, the data cost noted above. The lead's comparison with the variance
warning is not touched: the sandpile has no control parameter to move.

