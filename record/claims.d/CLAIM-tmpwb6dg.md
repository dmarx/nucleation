---
status: Proposed
title: 'A response profile that is positive, linear and normalized in the continuous test is a probability measure, and a declared family of tests turns the largest disagreement between two such measures into a pseudometric, which is a metric exactly when the family separates measures, so that observational equivalence under the family is distance zero'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant from A26 of the exchange "Explain
    First Contact RL" (ChatGPT, shared 2026-11-22), with the assistant's
    fills on the premise that does the work, the bounds the metrics need,
    and the measure–metric distinction.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the cited theorems as applied: a compact Hausdorff space and
  a positive, normalized linear functional on its continuous functions
  with no regular Borel probability measure representing it, or two
  distinct measures at distance zero under a family that separates
  measures. That a real response profile is not linear in the test does
  not defeat the claim; it means the claim's premise fails for that
  profile, which the claim says is the premise to check.
tags:
- mathematics
- probabilistic-modeling
- individuation
date: '2026-11-22'
line:
- formal-apparatus
- distributed-agency
uses:
- TERM-069
- TERM-134
complements:
- CLAIM-574
summary: >-
  A26 of the exchange "Explain First Contact RL" (2026-11-22), answering
  the owner's U13 and U14 ([CLAIM-tmphxbli](CLAIM-tmphxbli.md)). On a compact Hausdorff space
  X, the Riesz–Markov theorem represents each positive, normalized linear
  functional on C(X) by a unique regular Borel probability measure. For a
  declared family F of tests, d_F(μ, ν) = sup over F of |∫f dμ − ∫f dν|
  is a pseudometric, a metric when F separates measures (1-Lipschitz
  tests give Wasserstein-1; the unit ball of a characteristic kernel's
  space gives MMD). Distance zero is [TERM-069](../terms.d/TERM-069.md)'s observational equivalence,
  graded. Fills by the assistant: linearity in the test is the premise
  that does the work, F must be uniformly bounded (or the measures share
  moments) for d_F to be finite, and a measure is not a metric. The
  construction's wording is A's (ChatGPT, in the exchange of 2026-11-22);
  the fills' wording is the assistant's (Claude, in this session); adopting
  either is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmphxbli — Proposed; the owner's thesis this works out and the term it extends -->

# CLAIM-tmpwb6dg: A response profile that is positive, linear and normalized in the continuous test is a probability measure, and a declared family of tests turns the largest disagreement between two such measures into a pseudometric, which is a metric exactly when the family separates measures, so that observational equivalence under the family is distance zero

## The claim

A26's construction, in four steps.

1. **Profiles as functionals.** Let X be a space of dispositional
   configurations or histories, and let an organization S assign to each
   continuous test f: X → ℝ a value L_S(f), such as its expected response.
2. **Riesz–Markov.** If X is compact Hausdorff and L_S is positive
   (f ≥ 0 gives L_S(f) ≥ 0), linear and normalized (L_S(1) = 1), there is
   a unique regular Borel probability measure μ_S with
   L_S(f) = ∫ f dμ_S. A26: "the positivity, linearity, and normalization
   conditions matter: arbitrary graded predicates do not automatically
   define a measure."
3. **The test family's pseudometric.** For a declared family F,
   d_F(μ, ν) = sup_{f∈F} |∫ f dμ − ∫ f dν|. It is symmetric, satisfies
   the triangle inequality and vanishes on the diagonal, so it is a
   pseudometric. It is a metric exactly when F separates the measures
   considered (distinct measures disagree on some f ∈ F). Examples, as A26
   gave them: the 1-Lipschitz functions on a metric space give
   Wasserstein-1 (Kantorovich–Rubinstein duality); the unit ball of a
   reproducing-kernel Hilbert space with a characteristic kernel gives the
   maximum mean discrepancy.
4. **Observational equivalence, graded.** d_F(μ, ν) = 0 is [TERM-069](../terms.d/TERM-069.md)'s
   equivalence under the probe family F. A positive distance says how far
   the most discriminating affordable test tells them apart. A26: "Two
   organizational distributions are close when no affordable test can
   strongly distinguish them." Enlarging F can only raise d_F, the graded
   form of [CLAIM-574](CLAIM-574.md)'s monotone refinement.

A26 also let the tests be functions of whole histories, f: Γ_H → ℝ, so
that the measure is over trajectories (a perspective regaining influence
after contrary evidence, recovery after a member leaves). A29 §8 added
interventions: d_{Q,F}(S, T) = sup over q ∈ Q and f ∈ F of
|∫ f dμ_S^(q) − ∫ f dμ_T^(q)|, with μ_S^(q) the law of histories under
intervention q. That is the distance-valued form of comparing two states'
governance-response profiles ([TERM-067](../terms.d/TERM-067.md)) under a declared intervention
family.

## Fills (the assistant's)

- **Which premise does the work.** Step 2 is a theorem; what must be
  checked in an application is that the profile is linear in the test.
  An expected response is linear by construction. A profile of
  thresholded or saturating responses (does the organization pass f?) is
  not, and then no measure represents it. So the chain from predicates to
  measures goes through expectation, not through predicates alone.
- **Finiteness.** d_F is finite when F is uniformly bounded, as A26
  required, or when every measure considered integrates every test (for
  Wasserstein-1, a finite first moment).
- **A measure is not a metric** (U14: "measure theoretic sense. a
  metric"). The tests give a measure for each organization and a
  pseudometric between measures; the owner's chain needs both, in that
  order.

## What it does not say

That a measure over observed histories fixes an organization: two
organizations with one observational law under Q are at distance zero
and may still differ under an intervention outside Q ([TERM-069](../terms.d/TERM-069.md), "Not
interventional equivalence").

## Check

Standard results: Riesz–Markov–Kakutani for compact Hausdorff spaces;
integral probability metrics (Müller 1997), of which Wasserstein-1 and
MMD are cases. None is a work held here; [LIT-230](../literature.d/LIT-230.md) is the Hilbert-space
Riesz theorem, a different result. The pseudometric axioms were checked
by hand.
