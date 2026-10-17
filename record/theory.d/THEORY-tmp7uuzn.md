---
status: Active
title: "The information about a target carried by the Gács–Körner common random variable of the sources is a redundancy defined for any number of sources that is nonnegative, target-monotone and no larger than I_min, and is a lower bound on any reasonable redundancy; but it counts only deterministic shared structure, so it is zero whenever the sources' joint distribution has full support, fails the identity property and continuity, and gives negative synergy already for two sources"
version: 1
tags:
- information-theory
- complex-systems
date: '2026-10-17'
source:
- LIT-tmpk8n6l
summary: >-
  Griffith, Chong, James, Ellison & Crutchfield (2014), [LIT-tmpk8n6l](../literature.d/LIT-tmpk8n6l.md), read
  in full in [NOTE-tmpm0azr](../notes.d/NOTE-tmpm0azr.md). The lemmas are short and exact, and every
  example was recomputed, with Harder, Salge and Polani's copy family and
  a three-source copy added. It is the record's one redundancy defined for
  n > 2, and it does not have the identity property there or for n = 2.
---

# THEORY-tmp7uuzn: The information about a target carried by the Gács–Körner common random variable of the sources is a redundancy defined for any number of sources that is nonnegative, target-monotone and no larger than I_min, and is a lower bound on any reasonable redundancy; but it counts only deterministic shared structure, so it is zero whenever the sources' joint distribution has full support, fails the identity property and continuity, and gives negative synergy already for two sources

## Source

Griffith, Chong, James, Ellison & Crutchfield (2014), "Intersection
Information Based on Common Randomness", arXiv 1310.1538v3 (Entropy 16,
1985–2000), [LIT-tmpk8n6l](../literature.d/LIT-tmpk8n6l.md), read in full in [NOTE-tmpm0azr](../notes.d/NOTE-tmpm0azr.md).

## What was actually shown

**The measure (Lemma 8).** I_∧(X_1, …, X_n : Y) = I(X_1 ∧ … ∧ X_n : Y),
the most information about Y in any variable that is a function of every
source.

**Properties (Lemmas 4–6, 9).** Global positivity, equivalence-class
invariance, target monotonicity, weak monotonicity, weak symmetry, lower
bound, self-redundancy; I_∧ ≤ I_min. Not identity, local positivity,
strong monotonicity or strong symmetry.

**The failure.** Any noise between the sources makes their common random
variable trivial. ImperfectRdn: I_∧ = 0 and synergy −0.99 bit
(recomputed −0.9896). On Harder, Salge and Polani's copy family I_∧ is 0
for every correlation short of perfect, against I(X : Y) up to 0.24 bit,
so synergy is −I(X : Y).

**The zero-error variant.** H(∧X_i ∧ Y) satisfies nine of eleven
properties, identity for zero-error information among them, and still
gives Subtle −0.252 bit (recomputed −0.2516).

**More than two sources (recomputed).** For a target copying three
equally correlated bits, I_∧ is 1 at full correlation and 0 at λ = 0.5,
where each pairwise mutual information is 0.046.

What could have come out otherwise: the common random variable could
have captured ImperfectRdn's 0.99 bit of near-copy. It captures none.

## What this does not say

- **That redundancy is only shared structure.** That is the measure's
  premise, the source-redundancy pole of the dispute [THEORY-708](THEORY-708.md) takes
  the other side of.
- **That a multivariate identity-property redundancy exists or does not.**
  This measure is multivariate and lacks identity. Whether any measure
  can have both with local positivity is a separate question
  (Rauh et al., [LIT-tmpeurmb](../literature.d/LIT-tmpeurmb.md)).
- **Anything for noisy data.** It is zero there.

## Connections

- It is the "only correlation makes redundancy" view of Griffith and
  Koch's first version ([THEORY-tmpims74](THEORY-tmpims74.md)), made exact: in AND it gives
  their v1 answer, 0 redundant and 0.189 synergistic.
- It lies below [THEORY-706](THEORY-706.md)'s I_min, and disagrees with [THEORY-708](THEORY-708.md) and
  [THEORY-705](THEORY-705.md) wherever the sources are noisily correlated.
- [THEORY-568](THEORY-568.md)'s Shannon invariants do not depend on it, since its atoms
  satisfy the consistency equations.
