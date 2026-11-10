---
number: 552
status: Active
formerly:
- CLAIM-tmpgjdby
title: 'A perspective''s tolerance for another process''s contribution is its criterion for conferring influence on that contribution, set by its own priorities: tolerances are directed, and the discrepancy each measures is the perspective''s own, so inside its tolerance the perspective''s interventions raise the other''s share of future influence and outside it they lower it; meeting the tolerance is necessary for that conferral where the criterion binds, and sufficient only for a grant, under a rule that grants influence on it'
version: 3
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Status Proposed → Active at the status review's ruling (the owner
    delegated these rulings), under ADR-057, in the same change that
    promotes CLAIM-534, the premise that alone held it back. CLAIM-347 and
    its terms TERM-103, TERM-101, TERM-060 and TERM-064 are Active, and
    nothing objects to it. Its tolerance is the acceptance sense, which
    CLAIM-553 keeps apart from CLAIM-550's activation sense; CLAIM-550's
    non-activation region is "not automatically an endorsement region",
    which this claim does not contradict.
- version: 3
  date: '2026-11-10'
  note: >-
    Drops `uses: TERM-064` at the lint sweep of 2026-11-10: the entry
    never speaks of legibility. What it says of a perspective, that it
    measures discrepancy by its own priorities, is about which
    discrepancies count as significant, not whether a distinction can be
    recovered. No other change.
role: thesis
warrant: interpretive
defeated_if: >-
  An organization in which one process's conferrals on another
  (TERM-103) are positive and negative on the same contributions in
  the same context with nothing in the conferring process to tell them
  apart, so that no acceptance region of its own predicts their sign; or a
  case the record accepts in which the tolerances between two processes
  must be the same in both directions and measured on one common scale for
  the frustration account to apply. Not defeated by a grant that
  fails to raise influence because the channel or the rule does not carry
  it, which the claim keeps apart.
tags:
- self-governance
- agency
date: '2026-11-04'
line:
- will-organization
- distributed-agency
rests_on:
- CLAIM-534
- CLAIM-347
complements:
- CLAIM-283
- CLAIM-285
- CLAIM-553
uses:
- TERM-103
- TERM-101
- TERM-060
bears_on:
- QUESTION-270
summary: >-
  The owner's U12 of the exchange "Organizational Nucleation and SLT"
  (2026-11-04), which continues "Assess SDT Coverage": "i was thinking
  more along the linesof tolerances expressing endorsement criteria
  relative to some given perspective's priorities. maybe I'm confusing
  necessary vs sufficient conditions." It turns [CLAIM-534](CLAIM-534.md)'s and
  [CLAIM-538](CLAIM-538.md)'s tolerances, symmetric bounds on an edge, into each
  perspective's criterion for conferring influence on another. A12 separated
  permission, grant and causal effect. The reading of the criterion as
  the boundary where the sign of conferral (TERM-103, formerly
  TERM-053's endorsement) changes is the reader's. Restated in ADR-070's
  words at the owner's review. The wording is A's, sharpened by the reader; adopting it is
  the owner's call.
---
<!-- inactive-ok-file: TERM-053 — Superseded by ADR-070 (conferral, TERM-103; grant, TERM-101); cited as the term of its time -->
<!-- ref::uses-file: TERM-060 — "grants can be jointly frustrated" when no attainable arrangement meets every ordered pair's acceptance relation is TERM-060's frustration -->

# CLAIM-552: A perspective's tolerance for another process's contribution is its criterion for conferring influence on that contribution, set by its own priorities: tolerances are directed, and the discrepancy each measures is the perspective's own, so inside its tolerance the perspective's interventions raise the other's share of future influence and outside it they lower it; meeting the tolerance is necessary for that conferral where the criterion binds, and sufficient only for a grant, under a rule that grants influence on it

## The claim

[CLAIM-534](CLAIM-534.md) and [CLAIM-538](CLAIM-538.md) give each overlap one tolerance, the same for both
sides. The owner's U12 makes a tolerance belong to a perspective.
Perspective i holds a criterion for j's contribution y:

  Q_{i→j}(y, c) = 1[d_i(y, c) ≤ τ_{i→j}(c)].

Three things follow.

- **Directed.** A12 §1: τ_{i→j} ≠ τ_{j→i} in general. "Two perspectives
  can hold different standards for one another, without either standard
  being reducible to a universal measure of agreement."
- **The measure is the perspective's, not only the threshold.** A12 §3:
  "two perspectives can disagree about *which discrepancies are
  significant*, even before disagreeing about how much discrepancy to
  permit."
- **Not a ball around i's own output.** A12 §4: i "might endorse a critic
  precisely because that critic reaches conclusions different from its
  own." The criterion is an acceptance set, and may hold several
  conditions.

**The criterion sets the sign of conferral.** i confers influence on j
([TERM-103](../terms.d/TERM-103.md)) to the extent that an intervention of i raises j's chance
of influence, and opposition is negative conferral. The claim is that
Q_{i→j} is the switching surface of that effect: inside A_{i→j}, i's
interventions raise j's share; outside, they lower it. This is the
reader's reading of the owner's "endorsement criteria".

**Necessary and sufficient.** A12 §2 separates three roles:

| role | what holds |
|---|---|
| permissibility | i does not object within the tolerance |
| grant (A12: "conditional endorsement") | i grants j support when the conditions are met ([TERM-101](../terms.d/TERM-101.md)) |
| conferral (A12: "effective endorsement") | i's activity raises j's future influence ([TERM-103](../terms.d/TERM-103.md)) |

Where the criterion is mandatory, a grant by i implies Q_{i→j} = 1,
"but the converse need not hold" (A12 §2). Under a rule G_{i→j} = Q_{i→j},
meeting it is "sufficient for the grant, by construction", and "Whether that grant
actually increases j's future influence remains a causal question." So
the owner's worry is not a confusion. It separates the criterion, the
grant and the effect.

**Joint realizability.** Collect the acceptance relations of every
required ordered pair. Whether some attainable arrangement meets them all
is [CLAIM-347](CLAIM-347.md)'s question with acceptance sets indexed by ordered pairs.
A12 §3: "every pair of perspectives might admit a mutually acceptable
relationship, while the complete collection does not." So grants can be jointly frustrated "even without any constituent
being intrinsically opposed to another."

**Width is not generosity.** A12 §6: "A broad tolerance could indicate
genuine respect for another's autonomy. It could equally indicate
indifference". A narrow one can be domination or a justified boundary.
What matters is how a tolerance is formed and whether the affected
perspective can contest it.

## What it does not say

- **That meeting a criterion is conferring.** A criterion met with no
  channel or rule to carry it raises nobody's influence. That gap is
  [QUESTION-270](../questions.d/QUESTION-270.md)'s denied uptake and [CLAIM-283](CLAIM-283.md)'s split between precedence
  claimed and authority granted.
- **That the criterion is an attitude.** It may be subpersonal and not
  represented, as conferral allows ([TERM-103](../terms.d/TERM-103.md)). The reflective sense is
  [TERM-102](../terms.d/TERM-102.md).
- **That widening a tolerance relieves frustration.** By [CLAIM-347](CLAIM-347.md) it
  changes the demand. Relief needs a new arrangement that meets the old
  criteria. A13 §6: "A widened tolerance is not automatically relief of
  frustration under the original demands."
- **That a perspective's priorities are warranted.** The claim is about
  structure, not about which criteria are good.
