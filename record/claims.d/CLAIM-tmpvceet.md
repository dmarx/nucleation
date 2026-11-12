---
status: Proposed
title: 'An organization scored against the demands it recognizes can only score the same or worse when its inquiry comes to recognize more of them, since a larger set of demands is met by fewer arrangements; so where its governance rewards the absence of recognized failures, getting better at discovering its own obligations is penalized, and identification and satisfaction can move in opposite directions'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation below. As a contribution, defeated if the
  record already holds that recognizing further demands can only lower a
  score taken against the recognized set, and the incentive this gives
  under a reward for few recognized failures; CLAIM-347's downward closure
  is the premise, and CLAIM-619's counter-corrective disposition and
  CLAIM-475's resource-bounded specification are the nearest, and state
  neither.
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
- QUESTION-tmpuftum
summary: >-
  A's (ChatGPT's), A44 §3 of the exchange "Medical Ethics and Media
  Enshitification" (2026-11-11), on the owner's U21. A's example: a game
  developer scored only on commercial viability passes; an audit that
  adds a justified obligation to honour players' spending limits makes it
  fail, "despite its audit becoming more capable". A: "An organization
  can acquire a practical incentive not to become better at discovering
  its own obligations." The first half follows from CLAIM-347's downward
  closure; the second is conditional on the reward stated. Rechecked by
  the filer. The wording is A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-tmpz1l6r — Proposed; filed from the same exchange -->
<!-- inactive-ok-file: CLAIM-619 — Proposed; the counter-corrective disposition this complements -->

# CLAIM-tmpvceet: An organization scored against the demands it recognizes can only score the same or worse when its inquiry comes to recognize more of them, since a larger set of demands is met by fewer arrangements; so where its governance rewards the absence of recognized failures, getting better at discovering its own obligations is penalized, and identification and satisfaction can move in opposite directions

## The claim

A44 §3 separates two kinds of progress:

- satisfaction progress: "The organization becomes better at meeting a
  fixed collection of demands."
- identification progress: "The organization becomes better at
  recognizing requirements that its previous evaluation omitted."

and observes that "A better identification procedure can reveal worse
substantive performance without causing a deterioration in performance."

## The derivation

Let D_0 ⊆ D_1 be the demands recognized before and after an improved audit,
each demand i with acceptance set A_i, and let x be the organization's
current arrangement.

1. x meets every demand in D_1 only if it meets every demand in D_0, since
   ⋂_{i∈D_1} A_i ⊆ ⋂_{i∈D_0} A_i. So the pass indicator against the
   recognized set cannot rise when the set grows, for any x.
2. The same holds of any score monotone in the set of met recognized
   demands, and of the compatibility complex itself: if D_0 is not a face,
   no superset is (CLAIM-347's downward closure), and if D_1 is a face, so
   is D_0.
3. Suppose the organization's governance rewards a low count of recognized
   failures, and an audit improvement adds a demand that x fails. By 1,
   the improvement lowers the measured score while x is unchanged. So the
   reward penalizes the improvement, and an organization that acts on its
   rewards has a reason not to make it.

Steps 1 and 2 are monotonicity and hold for any demands. Step 3 is
conditional on the stated reward. Checked by the filer on 2026-11-12.

## Where it sits

- CLAIM-475 holds that specifying is a resource-bounded realization, so
  some questions an agent cannot yet ask. This claim adds that asking them
  can be penalized.
- CLAIM-619 (a disposition to answer challenge by reducing the capacity
  for challenge) is the active form; this is the passive one, which
  needs no response to any challenge, only a reward for quiet.
- CLAIM-549 (the quiescent complex is not the compatibility complex): A44
  §2 notes the twin route to a better score, relaxing tolerances ("it could
  relax the criteria used to decide whether a requirement has been
  satisfied"), which raises the pass rate without any accommodation.

## What it does not say

That any organization behaves this way, or which demands are justified:
A44 §7, the experiment "would not derive the legitimacy of the underlying
requirements". CASE-tmpz1l6r gives a design that would test whether the
incentive produces avoidance of inquiry.
