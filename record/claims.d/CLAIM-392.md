---
number: 392
status: Active
formerly:
- CLAIM-tmpfqsca
title: 'Stochastic information-bottleneck optima at two budgets need not be nested: for X uniform on four states and binary Y with P(Y=1|x) = (0, 0, 1/8, 3/8), the unique optima at β = 8 and β = 12 admit no Markov chain X → T₂ → T₁, so raising the budget reorganizes the optimum even with noisy encoders'
version: 2
history:
- version: 2
  date: '2026-10-21'
  note: >-
    Note of 2026-10-21 added, from the exchange of 2026-10-20 on effective
    description, agency and legibility: A2 and A5 proposed a paper on this
    result and CLAIM-387, keeping the numerical certificate and dropping
    three of its limits. The claim is unchanged.
role: thesis
warrant: demonstrated
defeated_if: >-
  A better or a second optimum at β = 8 or β = 12 for this source, against
  the numerical certificate below; or a channel from the β = 12 optimum's
  decoder points onto every β = 8 decoder point, that is, the β = 8 point
  (0.376, 0.376, 0.244, 0.004) lying in the β = 12 decoder hull after all.
tags:
- information-theory
- learning-theory
date: '2026-10-20'
line:
- learned-structure
- formal-apparatus
answers:
- QUESTION-220
rests_on:
- CLAIM-387
grounds:
- THEORY-753
- LIT-1258
summary: >-
  Computed in the reading of Charvin, Catenacci Volpi and Polani (2023),
  [NOTE-981](../notes.d/NOTE-981.md), on the source of [CLAIM-387](CLAIM-387.md), and re-run here. With
  [THEORY-753](../theory.d/THEORY-753.md)'s criterion (refinable iff some pair of optima forms the
  chain, iff the coarse decoder points lie in the fine decoder hull when
  that hull is non-degenerate), and optima certified unique, the hull test
  fails. It answers the stochastic half of [QUESTION-220](../questions.d/QUESTION-220.md) in the
  negative for this source. The certificate is numerical, not interval
  arithmetic, and the loss is small: 0.49% of the larger budget, in unique
  information.
---

# CLAIM-392: Stochastic information-bottleneck optima at two budgets need not be nested: for X uniform on four states and binary Y with P(Y=1|x) = (0, 0, 1/8, 3/8), the unique optima at β = 8 and β = 12 admit no Markov chain X → T₂ → T₁, so raising the budget reorganizes the optimum even with noisy encoders

## The claim

[CLAIM-387](CLAIM-387.md) showed that the optimal *partitions* of this source at two
budgets are incomparable. This claim is the same for the unrestricted
information bottleneck, whose optima are stochastic encoders.

- **Criterion** ([THEORY-753](../theory.d/THEORY-753.md), after Charvin et al., Propositions 1, 4
  and 8). The bottleneck is refinable from λ₁ to λ₂ iff some pair of
  optimal encoders forms X → T₂ → T₁, equivalently iff the coarse encoder
  is a garbling of the fine one. When the fine decoder points q(X|t) are
  affinely independent, this holds iff every coarse decoder point lies in
  their convex hull. If the optima are unique, up to relabelling and
  merging duplicate points, a failed hull test proves non-refinability.
- **The optima.** States 0 and 1 share P(Y|x), so the problem reduces to
  three states. The optima were found from 400 Blahut–Arimoto restarts.
  - At β = 8: I(X;T) = 0.546 bits and I(T;Y) = 0.097 bits, with two
    decoder points.
  - At β = 12: I(X;T) = 0.952 bits and I(T;Y) = 0.139 bits, with three
    decoder points, one of them pure on {0, 1}.
- **The certificate.** Each was certified globally optimal and unique by
  checking that F_β minus the tangent plane through its decoder points is
  non-negative over the simplex. The check used a grid of spacing 1/1200
  (minimum away from the decoder points 1.9 × 10⁻⁵ at β = 12), 300 local
  minimizations, all ending at the decoder points, and a bound near the
  vertices.
- **The test.** The β = 8 decoder point (0.376, 0.376, 0.244, 0.004) lies
  outside the hull of the β = 12 points. The LP phase-one minimum is 0.26,
  and the distance to the hull is 5.6 × 10⁻³, against solver error near
  10⁻⁷. The same failure holds for β = 8 against 10, and 10 against 12.
  Re-run here from the reader's script, with the same figures.

So no optimal encoder at β = 12 can be refined down to the optimum at β = 8
by adding noise. Moving from the smaller to the larger budget changes
which distinctions the representation draws, not only how many.

## What it does not say

- **Not a proof in exact arithmetic.** The certificate is a fine grid plus
  local search, not interval arithmetic. A sharper certificate would make
  it a theorem.
- **Not that the loss is large.** In unique information, the price of
  forcing nesting is 4.7 × 10⁻³ bits for β = 8 against 12: 0.49% of the
  larger budget.
- **Not that bottlenecks generally fail to nest.** Charvin et al. prove
  nesting at every pair of budgets when Y = f(X), and when X and Y are both
  binary ([THEORY-757](../theory.d/THEORY-757.md)). With this source, the smallest case where
  failure is possible is three effective states with binary Y. The
  reader's uncertified scan over β from 5 to 60 found failures mostly at
  nearby budgets, and nesting for far-apart pairs.

## Note of 2026-10-21: proposed as a paper with three of its limits dropped

A2 and A5 of the exchange of 2026-10-20 proposed a paper on this result
and CLAIM-387 ("More Information, Different Categories") as "perhaps the
cleanest paper-sized result in the current record". They kept its
numerical certificate and dropped three of its limits: the cost of forcing
nesting is 0.49% of the budget, the reader's scan found nesting for
far-apart budgets, and nesting is proved when Y = f(X) or X and Y are both
binary (THEORY-757).
