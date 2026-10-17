---
number: 705
status: Active
formerly:
- THEORY-tmp8ox3d
title: "For a target and two sources with finite alphabets, if unique information is to depend only on the two source–target pair marginals, then the minimum of the conditional mutual information over all joints with those marginals is an upper bound on every non-negative decomposition's unique information, and the shared and synergistic information it implies are lower bounds; this unique information vanishes exactly when the other source is Blackwell-sufficient, and the measures are non-negative, satisfy the bivariate partial-information axioms and the identity property, and do not extend to three sources on the partial-information lattice"
version: 2
history:
- version: 2
  date: '2026-10-17'
  note: >-
    Connections: equivalence with Griffith and Koch's S_VK for two sources, and Rauh et al.'s monotonicity results and impossibility.
tags:
- information-theory
- mathematical-statistics
date: '2026-10-17'
source:
- LIT-1162
summary: >-
  Bertschinger et al. (2014), [LIT-1162](../literature.d/LIT-1162.md), read in full in [NOTE-937](../notes.d/NOTE-937.md). The
  bounds, the Blackwell characterisation and the properties are proved.
  The motivating property is argued, not derived. Example 30 and the Table
  1 rows reproduce, except two entries that conflict with the paper's own
  Proposition 18. Under this measure, the record's transfer-entropy
  examples split exactly as under I_min.
supports:
- CLAIM-335
---

<!-- inactive-ok-file: THEORY-156 — Proposed; cited for Blackwell's theorem as it states it, which Lemma 6 matches; nothing here rests on its being settled -->

# THEORY-705: For a target and two sources with finite alphabets, if unique information is to depend only on the two source–target pair marginals, then the minimum of the conditional mutual information over all joints with those marginals is an upper bound on every non-negative decomposition's unique information, and the shared and synergistic information it implies are lower bounds; this unique information vanishes exactly when the other source is Blackwell-sufficient, and the measures are non-negative, satisfy the bivariate partial-information axioms and the identity property, and do not extend to three sources on the partial-information lattice

## Source

Bertschinger, Rauh, Olbrich, Jost & Ay (2014), "Quantifying unique
information", arXiv 1311.2852v2 (Entropy 16(4): 2161–2183),
[LIT-1162](../literature.d/LIT-1162.md), read in full in [NOTE-937](../notes.d/NOTE-937.md). The Entropy version was not
compared.

## What was actually shown

**The definitions.** For target X and sources Y, Z, Δ_P is the set of joints
with P's (X,Y) and (X,Z) marginals. UĨ(X : Y \ Z) = min_{Q∈Δ_P} MI_Q(X : Y | Z),
SĨ = max CoI_Q, CĨ = MI(X : (Y,Z)) − min MI_Q(X : (Y,Z)). One convex programme
gives all three (Lemma 4).

**The bounds (Lemma 3).** If a non-negative, continuous decomposition has
unique information depending only on p(x), p(y|x), p(z|x), then its unique
information is at most UĨ, and its shared and synergistic information at
least SĨ and CĨ. Equality holds exactly when some joint in Δ_P has no synergy.

**Operational meaning (Lemma 6, Corollary 7).** UĨ(X : Y \ Z) = 0 if and only
if Y is a garbling of Z with respect to X, that is, Z dominates Y in
Blackwell's order.

**Properties.** Non-negativity (Lemma 5); symmetry, consistency and the
bivariate PI axioms (Lemmas 11–13); the identity property, SĨ((Y,Z) : Y; Z)
= MI(Y : Z) (Proposition 18); additivity (Lemma 19); unique information that
cannot grow as sources are added (Lemma 25).

**The two-term split (Remark 14).** For any binary decomposition,
MI(X : Z | Y) = UI(X : Z \ Y) + CI(X : Y; Z).

**Checked** ([NOTE-937](../notes.d/NOTE-937.md)): AND gives SĨ = 0.311 and CĨ = 0.5, as in Example
30. XOR, RDN and Copy reproduce Table 1, except its Unq row (CĨ printed as
1; Proposition 18 and the computation give 0) and its Copy entry (printed as
MI(X : Y); Proposition 18 and the computation give MI(Y : Z)).

What could have come out otherwise: the bound need not have been attained
by any decomposition. Lemma 3 shows it is attained exactly when Δ_P holds a
synergy-free joint, and Lemma 5's construction shows the shared part is
non-negative.

## What this does not say

- **That property (∗) is required of unique information.** It is argued
  from decision problems. A measure without it is not shown wrong.
- **Anything for three or more sources.** By §6, citing earlier work, the
  identity property is incompatible with a non-negative decomposition on
  the PI lattice for three sources.
- **That the optimum is easy to find.** Convex, but ill-conditioned
  (Example 31). An unparametrised solver run got AND wrong in this reading.
- **That transfer entropy's split depends on I_min in the record's
  examples.** It does not ([NOTE-937](../notes.d/NOTE-937.md)): where the target's past carries no
  information about its next value, any such decomposition gives the same
  split.

## Connections

- For two sources its synergy is Griffith and Koch's S_VK: the constraint
  set is the same, and H(Y) is fixed on it ([THEORY-716](THEORY-716.md); the record's
  derivation). Rauh et al. show its unique information is monotone and its
  shared and synergistic parts are not, and that no identity-respecting
  extension to three sources keeps atoms nonnegative ([THEORY-713](THEORY-713.md)).

- It answers the flaw in Williams and Beer's I_min ([LIT-1172](../literature.d/LIT-1172.md)) that
  Harder, Salge and Polani identified ([LIT-1168](../literature.d/LIT-1168.md)), and is compared with
  their I_red.
- Remark 14 is the two-term split behind [THEORY-712](THEORY-712.md), [THEORY-707](THEORY-707.md) and
  [CLAIM-335](../claims.d/CLAIM-335.md).
- [THEORY-568](THEORY-568.md)'s Shannon invariants hold for this decomposition, as for any
  that satisfies the consistency equation.
- Lemma 6 is Blackwell's theorem as [THEORY-156](THEORY-156.md) states it (Proposed): being
  at least as informative for every decision problem is being able to
  simulate the other by a garbling. Here it is relative to the target X.
- [THEORY-497](THEORY-497.md) (ΦID) needs a redundancy function for more than two
  variables. This one, as it stands, is not one.
