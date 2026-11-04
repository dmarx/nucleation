---
status: Proposed
title: 'The quiescent complex, the sets of perspectives that some attainable arrangement keeps below their activation thresholds, is not the compatibility complex of their requirements: either can hold a face the other lacks, since a perspective can be quiet while its requirement is unmet and active while it is met; raising thresholds can only enlarge the quiescent complex and leaves the requirement complex as it was, so it is not relief of frustration'
version: 2
history:
- version: 2
  date: '2026-11-04'
  note: >-
    Vocabulary only, under ADR-070: "endorse" in TERM-053's sense now
    reads conferral (TERM-tmplu4ih) or grant (TERM-tmp08c21). The
    content is unchanged.
role: thesis
warrant: demonstrated
defeated_if: >-
  A threshold model in which the quiescent complex is fixed by the
  requirement complex, which needs every perspective's below-threshold
  region to be exactly its acceptance set in every context; or a showing
  that raising a threshold can enlarge the jointly realizable set of the
  original requirements. Not defeated by an organization in which the two
  complexes happen to coincide, which the claim allows.
tags:
- mathematics
- motivation
- self-governance
date: '2026-11-04'
line:
- will-organization
- formal-apparatus
rests_on:
- CLAIM-347
- CLAIM-361
uses:
- TERM-060
- TERM-094
complements:
- CLAIM-534
- CLAIM-459
grounds:
- CASE-129
- CASE-109
bears_on:
- QUESTION-131
summary: >-
  From the exchange "Organizational Nucleation and SLT" (2026-11-04). After
  the owner's U17 ("reframe "complaint" as something closer to
  "intervention threshold" or "activation threshold""), A17 built a
  complex from activation thresholds and called it "a quiescent
  compatibility complex". A19, A20 and A26 kept it apart from the
  requirement complex, and A28 restated the split for motivating
  perspectives ([TERM-tmpszrpp](../terms.d/TERM-tmpszrpp.md)). The requirement complex is the one the
  record already holds: [CLAIM-347](CLAIM-347.md)'s, over [TERM-060](../terms.d/TERM-060.md)'s acceptance sets. A
  wrote at A28 as if it were new. The two-perspective example is the
  reader's. The wording is A's, sharpened by the reader; adopting it is
  the owner's call.
---
<!-- inactive-ok-file: CLAIM-361 CLAIM-534 TERM-tmpszrpp — Proposed, Deferred, Unavailable or new; cited from the exchange "Organizational Nucleation and SLT" of 2026-11-04 as open -->

# CLAIM-tmp7oo4d: The quiescent complex, the sets of perspectives that some attainable arrangement keeps below their activation thresholds, is not the compatibility complex of their requirements: either can hold a face the other lacks, since a perspective can be quiet while its requirement is unmet and active while it is met; raising thresholds can only enlarge the quiescent complex and leaves the requirement complex as it was, so it is not relief of frustration

## The claim

Fix an organization, its attainable arrangements ℛ(c) in context c, and a
set P of perspectives. There are two complexes over P.

- **The requirement complex.** Each perspective i has an acceptance set
  Aᵢ(c), as in [TERM-060](../terms.d/TERM-060.md). A set S is a face when ℛ(c) ∩ ⋂_{i∈S} Aᵢ(c) ≠ ∅.
  This is [CLAIM-347](CLAIM-347.md)'s complex. A26 wrote it as 𝒦_𝒪(c) and said it
  "records which subsets of motivational requirements can be realized
  together."
- **The quiescent complex.** Each perspective has a region Tᵢ(c) of
  arrangements that leave it below its activation threshold. In A20 the
  region is Tᵢ^ε(c) = {w : Pr(aᵢ = 1 | w, c) ≤ ε}. A set S is a face when
  ℛ(c) ∩ ⋂_{i∈S} Tᵢ(c) ≠ ∅. A17: "it records which collections of
  perspectives can simultaneously remain below their reactive activation
  thresholds."

Both are downward-closed. The claim has three parts.

1. **Neither fixes the other.** A28: "A motivating perspective may remain
   inactive while its requirements are being violated. Alternatively, two
   perspectives may become highly active while their requirements are
   jointly satisfiable, perhaps because they're collaborating to secure a
   shared outcome. Therefore the low-activation compatibility complex and
   the substantive-requirement compatibility complex need not coincide."
2. **Raising thresholds is monotone.** A20: "if θᵢ′ ≥ θᵢ, then the
   corresponding quiescent tolerance set cannot shrink, and the quiescent
   compatibility complex cannot shrink either." The requirement complex
   does not depend on thresholds, so it does not move.
3. **So it is not relief.** [CLAIM-361](CLAIM-361.md) judges relief against a fixed set of
   the original demands. A larger quiescent complex with the same
   requirement complex is a quieter organization, not a less frustrated
   one. A26: "Increasing activation thresholds can enlarge the quiescent
   compatibility complex without making any original requirement more
   attainable. Genuine relief, relative to fixed requirements, requires
   expanding what can be jointly realized."

## The example

The reader's. Two perspectives, two attainable arrangements x and y.

- **A quiet face with no requirement face.** Let A₁ = {x} and A₂ = {y}.
  {1, 2} is not a face of the requirement complex. With thresholds high
  enough that neither activates at either arrangement, T₁ = T₂ = {x, y},
  and {1, 2} is a face of the quiescent complex.
- **A requirement face with no quiet face.** Let ℛ = {x} and
  A₁ = A₂ = {x}. {1, 2} is a requirement face. If both perspectives are
  highly active at x, securing it together, then T₁ = T₂ = ∅, and even the
  singletons are not quiescent faces.

## Why it matters

A19 said why: "simply raising the activation thresholds until none of the
processes reacts would also expand the quiet compatibility complex, but it
would not necessarily improve the agent's capacities." A20 put it as
"quiescence is not the right ultimate goal". [CASE-129](../cases.d/CASE-129.md) is the record's case
of this: two alarms are both quiet, and only one responds to a new hazard.
[CASE-109](../cases.d/CASE-109.md) is a case where two people show the same calm with their conflict
settled in different ways.

A28 asked the question that follows: "could an organization learn to
expand the latter without reducing the sensitivity of its motivating
perspectives?" That is relief in [CLAIM-361](CLAIM-361.md)'s sense, with thresholds held
fixed.

## A term A read past

**Compatibility complex ([CLAIM-347](CLAIM-347.md), [TERM-060](../terms.d/TERM-060.md)).**

- (a) A28 presents the requirement complex as a new move, "rather than
  merely the compatibility of current activation levels". The contrast
  between the two complexes is worth keeping, and this claim keeps it.
- (b) Read as intended, A would have said: keep [TERM-060](../terms.d/TERM-060.md)'s complex as the
  requirement complex the record already has, and add the quiescent
  complex as a second object relative to activation, whose relation to the
  first is the open question.
- (c) The owner made no correction.

**Endorsement ([TERM-053](../terms.d/TERM-053.md)), now conferral (TERM-tmplu4ih).** A28 §5: "Previously, we treated tolerance as
the amount of discrepancy from an endorsed will".

- (a) This is Frankfurt's sense, the will a perspective would approve. The
  idea is worth keeping under another word, "the will i would accept".
- (b) In [TERM-053](../terms.d/TERM-053.md)'s sense, a perspective's region of tolerance would be the
  set of effective wills on which its activity leaves other processes'
  future shares of influence unchanged. Where it intervenes, its
  conferral on the governing processes turns negative. Tolerance is then
  the zero set of i's row of E_ij, which can be measured.
- (c) The owner made no correction at A28.

## What it does not say

- **That quiescence is bad.** Hysteresis and high thresholds can be
  useful. A20: "It prevents rapid switching in response to noisy input."
- **That thresholds are irrelevant to integration.** [CLAIM-534](CLAIM-534.md)'s tolerance
  is recognized tolerance. This claim says only that moving a threshold
  does not move the requirement complex.
- **That Tᵢ^ε is well defined as A wrote it.** zᵢ carries memory, so
  Pr(aᵢ = 1 | w, c) depends on history. The region needs a stationary
  zᵢ*(w, c) or an index by history.
- **Anything about which complex an organization tracks.** That is
  empirical.
