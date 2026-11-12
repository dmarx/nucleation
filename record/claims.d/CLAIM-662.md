---
number: 662
status: Proposed
formerly:
- CLAIM-tmpvceet
title: 'For a fixed arrangement, expanding the recognized demand set cannot improve conjunctive compliance and cannot decrease the count of recognized violations; where governance penalizes newly recognized violations without rewarding their discovery, an organization may acquire an incentive not to improve its identification of its obligations'
version: 2
history:
- version: 2
  date: '2026-11-12'
  note: >-
    Narrowed after the owner's review of #485 on 2026-11-12. Version 1
    extended step 1 to "any score monotone in the set of met recognized
    demands" and said the organization "can only score the same or worse";
    that does not follow, since a count of satisfied demands rises when a
    met demand is newly recognized. The claim now states the two
    monotonicity facts that hold, conjunctive compliance and the count of
    recognized violations, in the owner's wording, with the owner's table
    of four scores checked by exhaustive enumeration, and makes the
    incentive conditional on governance that penalizes newly recognized
    violations without rewarding their discovery. Warrant unchanged:
    demonstrated for the two facts.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation or the enumeration below. As a contribution,
  defeated if the record already holds that, for a fixed arrangement,
  recognizing further demands cannot improve conjunctive compliance or
  lower the count of recognized violations, and the incentive this gives
  where newly recognized violations are penalized and their discovery is
  not rewarded; CLAIM-347's downward closure is the premise, and
  CLAIM-619's counter-corrective disposition and CLAIM-475's
  resource-bounded specification are the nearest, and state neither.
tags:
- epistemology
- society-and-governance
- mathematics
date: '2026-11-12'
line:
- organizational-normativity
- distributed-agency
rests_on:
- CLAIM-347
complements:
- CLAIM-619
- CLAIM-475
bears_on:
- QUESTION-441
- QUESTION-456
summary: >-
  A's (ChatGPT's), A44 §3 of the exchange "Medical Ethics and Media
  Enshitification" (2026-11-11), on the owner's U21, narrowed by the
  owner's review of [#485](https://github.com/dmarx/nucleation/issues/485) on 2026-11-12. A's example: a game developer
  scored only on commercial viability passes; an audit that adds a
  justified obligation to honour players' spending limits makes it fail,
  "despite its audit becoming more capable". The owner's statement: "For
  a fixed arrangement, expanding the recognized demand set cannot improve
  conjunctive compliance and cannot decrease the count of recognized
  violations. Where governance penalizes newly recognized violations
  without rewarding their discovery, the organization may acquire an
  incentive to avoid improving its normative identification." The two
  monotonicity facts are demonstrated and checked by enumeration; the
  incentive is conditional on the governance assumption. The wording is
  the owner's and A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-652 CLAIM-657 — Proposed; filed from the same exchange -->
<!-- inactive-ok-file: CASE-249 — Proposed; filed from the same exchange -->
<!-- inactive-ok-file: CLAIM-619 — Proposed; the counter-corrective disposition this complements -->

# CLAIM-662: For a fixed arrangement, expanding the recognized demand set cannot improve conjunctive compliance and cannot decrease the count of recognized violations; where governance penalizes newly recognized violations without rewarding their discovery, an organization may acquire an incentive not to improve its identification of its obligations

## The claim

A44 §3 separates two kinds of progress:

- satisfaction progress: "The organization becomes better at meeting a
  fixed collection of demands."
- identification progress: "The organization becomes better at
  recognizing requirements that its previous evaluation omitted."

and observes that "A better identification procedure can reveal worse
substantive performance without causing a deterioration in performance."

The owner's review of [#485](https://github.com/dmarx/nucleation/issues/485) narrowed what follows from this: "For a fixed
arrangement, expanding the recognized demand set cannot improve
conjunctive compliance and cannot decrease the count of recognized
violations. Where governance penalizes newly recognized violations without
rewarding their discovery, the organization may acquire an incentive to
avoid improving its normative identification."

## The derivation

Let D_0 ⊆ D_1 be the demands recognized before and after an improved audit,
each demand i with acceptance set A_i, and let x be the organization's
current arrangement, held fixed.

1. **Conjunctive compliance cannot improve (demonstrated).** x meets every
   demand in D_1 only if it meets every demand in D_0, since
   ⋂_{i∈D_1} A_i ⊆ ⋂_{i∈D_0} A_i. So the indicator "x passes every
   recognized demand" cannot rise when the set grows. The same holds of
   the compatibility complex itself: if D_0 is not a face, no superset is
   ([CLAIM-347](CLAIM-347.md)'s downward closure), and if D_1 is a face, so is D_0.
2. **Recognized violations cannot decrease (demonstrated).** The demands in
   D_0 that x fails are among those in D_1 that it fails, so their count
   cannot fall as the set grows.
3. **Not every score behaves so.** The count of recognized demands that x
   satisfies cannot fall and may rise: if x meets A and B and only A was
   recognized, recognizing B raises it from 1 to 2. The fraction satisfied
   may rise or fall. So "any score monotone in the set of met recognized
   demands", as version 1 had it, does not follow.
4. **The incentive (conditional).** Suppose the organization's governance
   penalizes newly recognized violations and does not reward their
   discovery, and an audit improvement adds a demand that x fails. By 2,
   the improvement raises the recognized violations while x is unchanged.
   So the penalty falls on the improvement, and an organization that acts
   on its rewards has a reason not to make it. Under governance that
   scores the count of demands met, or rewards discovery, step 4 does not
   follow.

Steps 1 and 2 hold for any demands and any arrangement. Step 4 holds only
under its stated governance assumption.

## The owner's table, checked

Holding x fixed and adding recognized demands:

| Score | Effect |
|---|---|
| Passes every recognized demand | cannot improve |
| Number of recognized violations | cannot decrease |
| Number of recognized demands satisfied | cannot decrease, may increase |
| Fraction satisfied | may increase or decrease |

Checked by the filer with python3 -I by exhaustive enumeration: every
satisfaction pattern of x over n demands and every pair D_0 ⊊ D_1, the
empty D_0 included (the fraction only for D_0 non-empty).

- **n = 2 (20 cases).** Pass: 0 up, 9 down, 11 same. Violations: 11 up,
  0 down. Satisfied: 11 up, 0 down. Fraction: 2 up, 2 down, 4 same.
- **n = 3 (152 cases).** Pass: 0 up, 61 down, 91 same. Violations: 91 up,
  0 down. Satisfied: 91 up, 0 down. Fraction: 30 up, 30 down, 36 same.

Each row of the table holds, and each "may" is realized.

## Where it sits

- [CLAIM-475](CLAIM-475.md) holds that specifying is a resource-bounded realization, so
  some questions an agent cannot yet ask. This claim adds that asking them
  can be penalized, under the governance stated.
- [CLAIM-619](CLAIM-619.md) (a disposition to answer challenge by reducing the capacity
  for challenge) is the active form. This is a passive one: it needs no
  response to any challenge, only a penalty on newly recognized violations.
  The owner's review distinguishes it, as selection of the questions
  investigated, from selection of the observed population ([CLAIM-652](CLAIM-652.md))
  and from the counter-corrective model; see [CLAIM-657](CLAIM-657.md).
- [CLAIM-549](CLAIM-549.md) (the quiescent complex is not the compatibility complex): A44
  §2 notes the twin route to a better score, relaxing tolerances ("it could
  relax the criteria used to decide whether a requirement has been
  satisfied"), which raises the pass rate without any accommodation.

## What it does not say

That any organization behaves this way, or which demands are justified:
A44 §7, the experiment "would not derive the legitimacy of the underlying
requirements". [CASE-249](../cases.d/CASE-249.md) gives a design that would test whether the
incentive produces avoidance of inquiry.
