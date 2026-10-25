---
status: Active
title: 'In a finite partial-monitoring game, an action optimal wherever two neighbouring actions tie has a loss vector on the segment between theirs, so a degenerate or duplicate action never creates a neighbouring pair or decides the trivial class, yet its signals count toward the pair''s local observability; and the T^2/3 lower bound for a pair that is not locally observable needs the separating direction in the kernel of the signal matrices of all such actions, not only of the two neighbours'
version: 1
history:
- version: 1
  date: '2026-10-25'
  note: >-
    Filed Active from NOTE-tmpkgxba. The convex-combination fact is
    Lattimore and Szepesvári's Lemma 1, cited from Bartók et al.'s
    Lemma 11. The kernel correction is their footnote to the proof of
    Theorem 4. Both are re-derived below step by step, under ADR-047 v2,
    and the correction is checked on a three-outcome game where it
    matters. The spam-game boundary case is computed. That forced
    exploration alone fails for degenerate actions is the paper's
    remark; the record checked it by simulation, not proof, and holds it
    in the body, not the title.
tags:
- learning-theory
- game-theory
date: '2026-10-25'
source:
- LIT-tmpfjv79
- LIT-tmpwpq36
extends:
- THEORY-tmpwtj3m
summary: >-
  Lattimore and Szepesvári (2019), [LIT-tmpfjv79](../literature.d/LIT-tmpfjv79.md), read in [NOTE-tmpkgxba](../notes.d/NOTE-tmpkgxba.md), on
  Bartók et al. (2014), [LIT-tmpwpq36](../literature.d/LIT-tmpwpq36.md). Of actions optimal only on a boundary:
  "Although these actions are never uniquely optimal, they can be
  informative". They enter the
  classification only through the neighbourhood set N_ab. Bartók et al.'s
  lower-bound proof chose the separating direction in the kernel of the
  two neighbours' signals alone. With such an action informative, that
  direction can be told apart cheaply. The fix is to take it in the kernel
  of every action in N_ab, which the definition of local observability
  already provides. It says what such actions contribute, not how often an
  algorithm must play them.
---
<!-- inactive-ok-file: CLAIM-446 — Proposed; the claim whose check variant is the boundary case here, nothing here rests on it -->
<!-- inactive-ok-file: THEORY-tmpz3a05 — Proposed; its summary of the lower bound repeats the slip corrected here, nothing here rests on it -->
# THEORY-tmpwqg2f: In a finite partial-monitoring game, an action optimal wherever two neighbouring actions tie has a loss vector on the segment between theirs, so a degenerate or duplicate action never creates a neighbouring pair or decides the trivial class, yet its signals count toward the pair's local observability; and the T^2/3 lower bound for a pair that is not locally observable needs the separating direction in the kernel of the signal matrices of all such actions, not only of the two neighbours

## Source

Lattimore and Szepesvári (2019), [LIT-tmpfjv79](../literature.d/LIT-tmpfjv79.md), read in [NOTE-tmpkgxba](../notes.d/NOTE-tmpkgxba.md): their
Lemma 1 (from Bartók et al.'s Lemma 11), §1's definitions, Remark 1, and
footnote 2 to the proof of their Theorem 4. The proof corrected is Bartók
et al.'s Theorem 4 ([LIT-tmpwpq36](../literature.d/LIT-tmpwpq36.md), [NOTE-tmpupizd](../notes.d/NOTE-tmpupizd.md)). The derivations below
are the record's.

## What was actually shown

**Lemma 1, re-derived.** Let a and b be neighbours, F = C_a ∩ C_b, and
d ∈ N_ab, so d is optimal on all of F. On F, ⟨ℓ_a, u⟩ = ⟨ℓ_b, u⟩ =
⟨ℓ_d, u⟩. F has affine dimension E − 2 inside the hyperplane Σu_i = 1,
which misses the origin, so its linear span has dimension E − 1. The
vectors orthogonal to that span form a line, and ℓ_b − ℓ_a ≠ 0 spans it.
Hence ℓ_d = ℓ_a + β(ℓ_b − ℓ_a) for one β. If β < 0, then near F inside C_a,
where ⟨ℓ_b − ℓ_a, u⟩ > 0, d is strictly better than a, which contradicts
a's optimality there. If β > 1, then ℓ_d − ℓ_b = (1 − β)(ℓ_a − ℓ_b), and d
beats b inside C_b. So ℓ_d = αℓ_a + (1 − α)ℓ_b with α = 1 − β ∈ [0, 1]. When
α ∈ (0, 1), ⟨ℓ_d, u⟩ ≥ min(⟨ℓ_a, u⟩, ⟨ℓ_b, u⟩), with equality only where
the two tie, so C_d = F: d is degenerate. When α ∈ {0, 1}, d duplicates a or
b.

**What follows for the classification.**

- Such an action never makes a pair of neighbours, since neighbours are
  non-degenerate and duplicates share a cell. So it never moves a game out
  of the trivial class ([THEORY-tmpyulw1](THEORY-tmpyulw1.md)).
- Its signal matrix enters Σ_{c∈N_ab} Im S_cᵀ, so it can make the pair
  locally observable. The paper's spam game, L = ((0, 1), (1, 0), (c, c))
  with only the third action revealing, has that action degenerate at
  c = ½, with cell {(½, ½)} = C_1 ∩ C_2. It lies in N_12 and the game is
  locally observable (easy). At c > ½ the action is dominated and the game
  is hard. Computed, with the same result for [CLAIM-446](../claims.d/CLAIM-446.md)'s check variant at
  k = Hc/(H + c).
- Its cost near the boundary is small. Under u_a = u − Δv, ℓ_d costs
  ⟨ℓ_d − ℓ_a, u_a⟩ = (1 − α)Δ, so it is an inexpensive source of
  information exactly where information matters.

**The kernel step, corrected.** Bartók et al.'s proof of their Theorem 4
reads: "ℓ₂ − ℓ₁ ∉ Im S₁ᵀ ⊕ Im S₂ᵀ … Thus, there exists a vector v such that
v ∈ Ker S₁ ∩ Ker S₂ and (ℓ₂ − ℓ₁)ᵀv ≠ 0". Later steps use the claim that no
action in N₁ ∪ N₂ ∪ N₃, the latter the actions between the two, separates
p₀ ± εv. That needs S_c v = 0 for those actions as well. The paper's
footnote: "The minor error in Bartók et al. [2014] appears in their
definition of v, which is in the kernel of a different S constructed by
stacking just S_a and S_b and not the degenerate/duplicate actions in
between." The repair: the pair is not locally observable, so ℓ_a − ℓ_b
has a component w ≠ 0 in Ker S, S the stack over N_ab, and v =
w/⟨w, ℓ_a − ℓ_b⟩ serves ([THEORY-tmpwtj3m](THEORY-tmpwtj3m.md)'s construction with D = N_ab).

**A game where it matters** (three outcomes, computed). Take
ℓ_a = (0, 1, ½), ℓ_b = (1, 0, ½), ℓ_d = (½, ½, ½) and ℓ_c = (1, 1, 1). Actions a
and b show one symbol, d shows whether the outcome is 3, and c reveals it.
Then d is degenerate with C_d = C_a ∩ C_b = {u₁ = u₂}, N_ab = {a, b, d}, and c
is dominated. The pair is not locally observable but is globally
observable, so the game is hard. The vector v = (−¼, ¾, −½) is in
Ker S_a ∩ Ker S_b with ⟨v, ℓ_a − ℓ_b⟩ = 1, but S_d v = (½, −½) ≠ 0. Under
u ± Δv, d's symbol laws differ while d costs only Δ/2 per play, so the
proof's step fails for this choice. The kernel of the full stack gives
v = (−½, ½, 0), with S_d v = 0, and the argument goes through. So the
theorem stands and only the proof needed the change. In non-degenerate
games N_ab = {a, b}, and the two choices coincide.

**Forced exploration, as the paper says it.** NeighborhoodWatch's local
games put no weight on a degenerate action, so it is played only through
the γ/K exploration, "and non-adaptive forced exploration is not
sufficient for O(√n) regret in partial monitoring" (§3). Their redistribution moves mass onto d
from a and b. It gives d at least min(P̃_a, P̃_b)/(2K) and leaves the
expected loss unchanged, because ℓ_d is the matching mixture of ℓ_a and ℓ_b
(their Lemma 4). Remark 1 says why d should not get much more: its
estimator's variance is about max(1/P_a, 1/P_b). The loss-preserving
property and Lemma 4 (a), (b), (d), and (c) for d, were checked on 200,000
random instances. A simulation on the degenerate spam game gave regret/√n
flat with redistribution and growing without it ([THEORY-tmpyulw1](THEORY-tmpyulw1.md)). That
is evidence for the remark on one game, not a proof of it.

## What this does not say

- **Not a rate for a degenerate game by itself.** Which class a game is
  in is [THEORY-tmpyulw1](THEORY-tmpyulw1.md)'s. This entry says how degenerate and duplicate
  actions enter that decision.
- **Not that forced exploration provably fails.** That is the paper's
  statement and the record's simulation. No lower bound for γ/K
  exploration is proved.
- **Not that Bartók et al.'s Theorem 4 is false.** The statement holds,
  and the proof needed the right kernel.
- **Not about dominated actions.** A dominated action is outside every
  N_ab and contributes only to global observability, as the check does
  above its threshold.

## Connections

- **[THEORY-tmpwtj3m](THEORY-tmpwtj3m.md).** This is its span lemma applied with D = N_ab. The
  choice of D is the whole correction.
- **[THEORY-tmpz3a05](THEORY-tmpz3a05.md)**'s summary of the lower bound, "with v in the kernel
  of both signal matrices", repeats the slip, and so does
  [NOTE-tmpupizd](../notes.d/NOTE-tmpupizd.md)'s Key results ("v in Ker S_1 ∩ Ker S_2"). Both are correct
  for non-degenerate games only.
- **[CLAIM-446](../claims.d/CLAIM-446.md).** Its check, at exactly k = Hc/(H + c), is a degenerate
  revealing action. Checking that costs exactly the value of not having to
  guess is cheap to learn from, and costing more is the hard case.
