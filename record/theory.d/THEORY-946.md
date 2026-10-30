---
number: 946
status: Active
formerly:
- THEORY-tmpzogk3
title: "In the zero-sum meta-game on an antisymmetric evaluation matrix the maximum-entropy Nash equilibrium is unique; when the meta-game has only one Nash equilibrium, adding exact copies of an agent splits that agent's mass evenly and leaves every Nash average unchanged; the equilibrium is uniform exactly when every agent's mean log-odds is zero, and uniform on the top-rated agents when the matrix is a pure gradient"
version: 2
history:
- version: 2
  date: '2026-10-30'
  note: >-
    Promoted to Active at the status review's ruling (the owner delegated
    these rulings), under ADR-065 §5. A second checker followed
    Proposition 4, the lemma, the reader's step from the lemma to
    invariance under a unique equilibrium, Theorem 1's P3 and the
    counterexample, and re-ran them by script with controls (status review
    22). The old promote_when: A checked re-derivation recorded in this
    file, which the reading made (NOTE-1155) and which ADR-047 counts
    toward promotion. It is refuted by an antisymmetric matrix whose
    meta-game has a single Nash equilibrium and in which adding an exact
    copy of an agent, distinct from every other, changes some original
    agent's Nash average. The title is limited to that case. The reading's
    counterexample with a segment of equilibria is outside it, and so are
    results about near-copies or about non-redundant additions. Those
    neither promote nor refute it.
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

## Note of 2026-10-30: the second check

The second check at the status review (ADR-065 §5) followed each step.

Uniqueness. The value is 0, so p is an equilibrium strategy of either
player exactly when Ap ≤ 0. The equilibrium set {p in the simplex : Ap ≤
0} is a convex polytope, the same for both players, and entropy, being
strictly concave, has one maximiser on it.

The lemma. Copy agent c as c′. In the padded matrix A′, A′p′ is A m(p′) on
the original agents and (A m(p′))_c on c′, where m(p′) merges the masses
of c and c′. So p′ is an equilibrium of the padded game exactly when m(p′)
is one of the original.

Invariance. If the original equilibrium p is unique, every padded
equilibrium is a split of it, with αp_c on c and (1 − α)p_c on c′. Its
entropy is H(p) + p_c h(α), h being the binary entropy, which is largest
at α = ½. The Nash averages A′p′ on the original agents are Ap, and the
copy gets (Ap)_c.

P3. If div A = 0, the uniform u has Au = 0, so it is an equilibrium, and
it has the most entropy on the whole simplex. Conversely Σ_i (Au)_i = 0
for antisymmetric A, so Au ≤ 0 forces Au = 0, which is div A = 0. If A_ij
= r_i − r_j, then (Ap)_i = r_i − r·p ≤ 0 for every i forces r·p = max r,
so p lies on argmax r, and the maximum-entropy one is uniform there.

The counterexample. E's mass in an equilibrium would raise the sum of the
rock, paper and scissors rows by 3p_E > 0, so E has none, and Ap ≤ 0 then
makes the three equal. With mass λ on them and 1 − λ on D, E's row needs λ
≥ ½. Maximising −λ ln(λ/3) − (1 − λ) ln(1 − λ) gives ln(3(1 − λ)/λ) = 0,
so λ = ¾, and E's Nash average is −¾ + ¼ = −½. With D copied the second
term becomes −(1 − λ) ln((1 − λ)/2), which gives λ = 3/5, p* = (⅕, ⅕, ⅕,
⅕, 0, ⅕), and E's average −3/5 + 2/5 = −⅕.

A script (numpy, with an exact linear-programming solver, in the session's
scratchpad) checked these. In 400 random antisymmetric matrices of 3 to 7
agents with a unique equilibrium, one agent copied, every split tried was
an equilibrium of the padded game, the solver's padded equilibrium merged
back to the original, and the even split left every original Nash average
unchanged. P3 held on 100 matrices each way. The counterexample is the
control: there a grid search over λ agreed with the closed forms above,
and the "invariant" split (¼, ¼, ¼, ⅛, 0, ⅛) is an equilibrium of lower
entropy than the selection.
