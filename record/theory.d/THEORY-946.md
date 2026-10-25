---
number: 946
status: Proposed
formerly:
- THEORY-tmpzogk3
promote_when: >-
  A checked re-derivation recorded in this file, which the reading made
  (NOTE-1155) and which ADR-047 counts toward promotion. It is refuted
  by an antisymmetric matrix whose meta-game has a single Nash equilibrium
  and in which adding an exact copy of an agent, distinct from every
  other, changes some original agent's Nash average. The title is limited
  to that case. The reading's counterexample with a segment of equilibria
  is outside it, and so are results about near-copies or about
  non-redundant additions. Those neither promote nor refute it.
title: "In the zero-sum meta-game on an antisymmetric evaluation matrix the maximum-entropy Nash equilibrium is unique; when the meta-game has only one Nash equilibrium, adding exact copies of an agent splits that agent's mass evenly and leaves every Nash average unchanged; the equilibrium is uniform exactly when every agent's mean log-odds is zero, and uniform on the top-rated agents when the matrix is a pure gradient"
version: 1
tags:
- game-theory
- mathematics
date: '2026-10-24'
source:
- LIT-1508
summary: >-
  Balduzzi et al. (2018), [LIT-1508](../literature.d/LIT-1508.md), Proposition 4, Lemma 1 and Theorem
  1, read from arXiv v2 in [NOTE-1155](../notes.d/NOTE-1155.md), proofs followed. The paper claims
  invariance to redundant copies without the uniqueness condition. Its
  proof covers the Nash set, not the maximum-entropy selection. A
  counterexample checked by script (one copy of a null agent moves an
  outside agent's Nash average from −0.5 to −0.2) shows the condition is
  needed. Cardinal: payoffs are log-odds.
---
<!-- inactive-ok-file: NOTE-1155 — the reading this is filed from -->

# THEORY-946: In the zero-sum meta-game on an antisymmetric evaluation matrix the maximum-entropy Nash equilibrium is unique; when the meta-game has only one Nash equilibrium, adding exact copies of an agent splits that agent's mass evenly and leaves every Nash average unchanged; the equilibrium is uniform exactly when every agent's mean log-odds is zero, and uniform on the top-rated agents when the matrix is a pure gradient

## Source

Balduzzi, Tuyls, Pérolat & Graepel, [LIT-1508](../literature.d/LIT-1508.md), read in [NOTE-1155](../notes.d/NOTE-1155.md)
from arXiv:1806.02643v2: Proposition 4 (p. 6, proof p. 13), Theorem 1
(pp. 6–7, proofs pp. 14–15), Lemma 1 (p. 14), Example 1 (p. 6).

## What was actually shown

- **Uniqueness (Proposition 4).** The Nash equilibria of a two-player
  zero-sum game form a convex polytope. For an antisymmetric matrix the
  set is symmetric, and entropy is strictly concave, so one symmetric
  equilibrium has maximum entropy.
- **The key lemma.** The game's value is zero, so p is a Nash equilibrium
  exactly when Ap ≤ 0. Every agent then scores at most zero against p.
  Copy agent c. Each split (…, αp_c, (1 − α)p_c) of a Nash equilibrium is
  one of the padded game, and merging the copies of a padded equilibrium
  gives one of the original.
- **From the lemma to invariance.** This step is the reader's. If the
  original equilibrium is unique, every padded equilibrium has total mass
  p_c on the copies. Entropy is then maximized by the even split. The Nash
  average A′p′ equals the original on every original agent, and the
  copies get the copied agent's value. The paper's Example 1 (rock,
  paper, scissors with C doubled: (⅓, ⅓, ⅓) becomes (⅓, ⅓, ⅙, ⅙), and
  every Nash average stays 0, while uniform averaging gives B the edge) is
  this case.
- **Interpretability (Theorem 1, P3).** p* is uniform exactly when
  div A = 0, and when A = grad(r) the game decouples, so p* is uniform on
  argmax r.

What could have come out otherwise: in the paper's Example 1, uniform
averaging moves (div A′ = (−1.15, 1.15, 0, 0)) and Nash averaging does
not.

## What this does not say

- **That Nash averaging is invariant to copies in general.** The paper
  says so (Theorem 1, P1) and does not prove it. With a segment of
  equilibria, the maximum-entropy selection on the padded game weighs the
  copied agent's mass by the extra log 2 of its split and moves. Take
  rock-paper-scissors, a null agent D tying all three, and E, which loses
  to all three and beats D. Copying D moves the selection from
  (¼, ¼, ¼, ¼, 0) to (⅕, ⅕, ⅕, ⅕, 0, ⅕) and E's Nash average from −0.5 to
  −0.2 ([NOTE-1155](../notes.d/NOTE-1155.md), checked by script).
- **That it resists near-copies.** Continuity (P2) is of the payoff. The
  equilibrium itself can jump (the paper's Example 2).
- **That it resists a non-redundant addition.** A new agent beating the
  leader changes the equilibrium completely. That is the method working.
- **That the equilibrium measures skill.** It is the unexploitable team
  for this data set; the authors call it adversarial and "a harsh
  master".
- **Anything ordinal.** Payoffs are log-odds and the results use their
  magnitudes.

## Connections

The cleanest formal answer the record holds to one capture route: a
scoring layer that can be moved by padding the evaluated population. It
narrows [CASE-124](../cases.d/CASE-124.md)'s μ route and is distinct from [CASE-155](../cases.d/CASE-155.md)'s
share-dependent c ([NOTE-1155](../notes.d/NOTE-1155.md)). The value-based invariant of
Balduzzi et al. (2019), [THEORY-944](THEORY-944.md), needs no uniqueness and holds for
behavioural mixtures as well as copies.
