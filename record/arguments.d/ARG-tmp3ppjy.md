---
status: Proposed
title: "Newman's review, as a source, carries items 2, 3, 6 and 7 of the catalogue of feedback-free power-law mechanisms, by its percolation, random-walk return, growth-at-random-age and inverse-quantity derivations, and not items 1, 4 and 5"
version: 1
form: source
grounds:
- THEORY-tmp6jdas
concludes:
- CLAIM-795
tags:
- probabilistic-modeling
- complex-systems
date: '2026-11-22'
line:
- formal-apparatus
summary: >-
  Whether Newman's review ([LIT-2976](../literature.d/LIT-2976.md)), read in [NOTE-tmpa7yd2](../notes.d/NOTE-tmpa7yd2.md), carries
  [CLAIM-795](../claims.d/CLAIM-795.md), which cited it unread as A's general reference. It carries
  four of the seven items: tuned criticality (percolation), the walk's 3/2
  (as first return), growth with a spread of ages (Reed and Hughes, as a
  combination of exponentials) and the inverse of a uniform variable. It
  has nothing on critical branching, mixtures of rates or sample-space
  reduction. It grounds the claim for items 2, 3, 6 and 7 only, and adds
  four feedback-free mechanisms the catalogue lacks. The wording is the assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-795 THEORY-tmp6jdas — Proposed; the claim and the reading this argument joins -->
<!-- inactive-ok-file: LIT-2997 LIT-2962 — Deferred; the works items 5 and 4 rest on, registered and unread -->

# ARG-tmp3ppjy: Newman's review, as a source, carries items 2, 3, 6 and 7 of the catalogue of feedback-free power-law mechanisms, by its percolation, random-walk return, growth-at-random-age and inverse-quantity derivations, and not items 1, 4 and 5

## The inference

[CLAIM-795](../claims.d/CLAIM-795.md): power laws arise from many mechanisms with no positive feedback,
in seven constructions. [THEORY-tmp6jdas](../theory.d/THEORY-tmp6jdas.md): Newman's catalogue, with its
exponents.

## Critical questions (source)

**Does the work say this, read in context?** For four items. Item 2:
percolation at p_c = 0.5927462 and a scale-free cluster distribution
(§IV.E). Item 3: "So the distribution of return times follows a power law
with exponent α = 3/2" (§IV.C, p. 16), for the first return of a
symmetric walk, not first passage to a boundary; the exponent is the same.
Item 6: Reed and Hughes, exponential growth observed at an exponentially
distributed time (§IV.A, p. 14); with a = −λ and b = g, Newman's
α = 1 − a/b is 1 + λ/g, the density form of the item's survival exponent
λ/g (checked, python3 -I). Item 7: x = 1/y gives p(x) ∝ x^(−2) (§IV.B),
without the d-ball geometry. And none needs a rich-get-richer feedback.

**Is it said within the scope the claim needs?** Not for items 1, 4 and 5.
The review has no branching process, no mixture of exponential rates (its
"combinations of exponentials" is an exponential of an exponentially
distributed variable, item 6's mechanism) and no sample-space reduction.
Those rest on [CASE-303](../cases.d/CASE-303.md), [THEORY-2131](../theory.d/THEORY-2131.md) and [LIT-2962](../literature.d/LIT-2962.md), and [LIT-2997](../literature.d/LIT-2997.md).

**Does the claim lean on the reading for more than it holds?** It did, in
calling the review the general reference for all seven. Corrected in the
claim's body.

## Verdict

Support for items 2, 3, 6 and 7. [THEORY-tmp6jdas](../theory.d/THEORY-tmp6jdas.md) replaces [LIT-2976](../literature.d/LIT-2976.md) in
the claim's grounds. Random typing, highly optimized tolerance, coherent
noise and record dynamics are additions, recorded in the claim.
