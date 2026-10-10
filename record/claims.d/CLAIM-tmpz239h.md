---
status: Proposed
title: 'The decision term should be the positive part of the risk increase on the same decision problem, with losses in [0, 1] and a stated prior; so restated it is directed, counts no improvement as loss, and vanishes for every problem and prior exactly when the rendering is at least as informative as the source in Blackwell''s order'
version: 1
role: thesis
defeated_if: >-
  Receivers' task-indexed fidelity verdicts, on renderings that improve
  some tasks and worsen others, track the symmetric distance D_Q better
  than its positive part, so that judged fidelity counts improvement as
  loss; or the designs supply no distribution of situations from which to
  state the prior.
tags:
- mathematical-statistics
- information-theory
date: '2026-10-10'
line: pragmatic-transport
grounds:
- THEORY-156
complements:
- CLAIM-050
- CLAIM-106
uses:
- TERM-028
- TERM-043
summary: >-
  The record's repair, on 2026-10-10, of A86's D_Q after [CLAIM-tmpbi9eb](CLAIM-tmpbi9eb.md).
  Define D⁺_Q(U → V; π) = sup over q in Q of [r_q,π(V) − r_q,π(U)]⁺, with
  r the Bayes risk under the prior π. It is directed and blind to
  improvement. With Q all finite problems and π all priors, it is zero
  exactly when V is at least as informative as U in Blackwell's order, by
  the Bayes form of Blackwell's theorem for finitely many states. A86's
  D_Q, with the identity on tasks, is its symmetrization. Under report
  fidelity ([CLAIM-tmp95pjv](CLAIM-tmp95pjv.md)) the paired task is the same task, so no scale
  between tasks is needed. The mathematics is checkable; the claim that
  this is the right decision term is a proposal. It does not say Q is
  fixed.
---
<!-- inactive-ok-file: CLAIM-050 CLAIM-106 — Proposed; the Blackwell thesis and the directed-fidelity thesis this measure serves, cited as open -->
<!-- inactive-ok-file: THEORY-156 — Proposed; cited as the reading of Blackwell's theorem the derivation uses, not as settled -->
<!-- inactive-ok-file: CLAIM-tmp95pjv — Proposed; the report/re-performance distinction, cited as open -->
<!-- inactive-ok-file: CLAIM-tmpyeik3 — Proposed; open, cited for its worked case -->
<!-- inactive-ok-file: LIT-778 — Deferred; Torgersen, unread here, named for the constants and not leaned on -->

# CLAIM-tmpz239h: The decision term should be the positive part of the risk increase on the same decision problem, with losses in [0, 1] and a stated prior; so restated it is directed, counts no improvement as loss, and vanishes for every problem and prior exactly when the rendering is at least as informative as the source in Blackwell's order

## What it answers

This is the record's reply of 2026-10-10 to [CLAIM-tmpbi9eb](CLAIM-tmpbi9eb.md) (granted, and
right), which showed that A86's D_Q(U, V) = sup_q |R_q(U) − R_τ(q)(V)| is not
Blackwell's order: one number per task needs a prior or a minimax summary;
subtracting the risks of two tasks needs their losses on one scale; the
absolute value counts improvement as loss and makes D_Q symmetric; and τ on
tasks is unanchored. The reply restates the term so that the first three
points are met. The fourth is met for report fidelity, where τ is the
identity ([CLAIM-tmp95pjv](CLAIM-tmp95pjv.md)), and stays open for re-performance
([QUESTION-005](../questions.d/QUESTION-005.md)). Steps (a) to (d) below are elementary and checkable. That
receivers' judged fidelity behaves like this term is a proposal, and the
defeat condition tests it.

## The claim

**Definition.** Let U be the source and V the rendering, both experiments
about one situation Z, which is finite in any design. A decision problem q
has a finite set of actions and a loss L_q(z, a) in [0, 1]. Let π be a
stated prior on Z, taken from the design's distribution of situations. The
Bayes risk r_q,π(U) is the least expected loss, under π, over decision
rules that read U. Then

D⁺_Q(U → V; π) = sup over q ∈ Q of [r_q,π(V) − r_q,π(U)]⁺,

where [x]⁺ = max(x, 0). It is the largest increase in risk, over the
problems in Q, from using the rendering in place of the source. The same
problem is used on both sides, so no scale between tasks is needed.

**(a) A garbling never gains.** Suppose V is a garbling of U: there is a
Markov kernel G with P(V | Z) = G P(U | Z). Any rule δ that reads V gives a
rule on U, namely apply G to U and then δ, and under each z it has the same
distribution of actions, so the same risk. So the best rule on U does at
least as well as the best rule on V, and r_q,π(U) ≤ r_q,π(V) for every q
and π. Hence D⁺_Q(V → U; π) = sup_q [r_q,π(U) − r_q,π(V)]⁺ = 0 always. This
is the easy direction, the one the manuscript uses.

**(b) The converse.** Suppose D⁺(U → V; π) = 0 for every finite problem
with losses in [0, 1] and every prior π. Then r_q,π(V) ≤ r_q,π(U) for all of
them. Rescaling a bounded loss to [0, 1], by L ↦ (L − m)/(M − m) with m and
M its least and greatest values, rescales every Bayes risk by the same
increasing affine map, so the inequality holds for every bounded loss. By
the Bayes form of Blackwell's theorem for finitely many states ([THEORY-156](../theory.d/THEORY-156.md)),
V is then at least as informative as U. So D⁺(U → V; ·) vanishes for every
problem and prior exactly when the rendering loses nothing the source
offered. A rendering that is a strict garbling has D⁺(U → V) > 0 for some
problem and prior, and D⁺(V → U) = 0 for all.

**(c) It is directed.** Let Z be uniform on {0, 1}, U = Z, and V a constant.
Take q = "guess Z" with 0–1 loss. From U the guess is always right:
r(U) = 0. From V nothing is learnt, and any guess is wrong with probability
1/2: r(V) = 1/2. So D⁺(U → V) = [1/2 − 0]⁺ = 1/2, and
D⁺(V → U) = [0 − 1/2]⁺ = 0. The term charges the rendering for its loss and
does not charge the source for being better.

**(d) A86's D_Q is its symmetrization.** With τ the identity on tasks and the
same prior, D_Q(U, V) = sup_q |r_q(U) − r_q(V)|. For any real x,
|x| = max([x]⁺, [−x]⁺), and a supremum of a maximum is the maximum of the
suprema. So

D_Q(U, V) = max(sup_q [r_q(V) − r_q(U)]⁺, sup_q [r_q(U) − r_q(V)]⁺)
= max(D⁺(U → V), D⁺(V → U)).

This is [CLAIM-tmpbi9eb](CLAIM-tmpbi9eb.md)'s third point, that D_Q counts improvement as
distortion, stated exactly. In [CLAIM-tmpyeik3](CLAIM-tmpyeik3.md)'s worked case, the rendering
that answers "Is Z = 3?" loses 1/3 on "Is Z = 1?" and gains 1/3 on "Is Z =
3?". So D⁺(U → V) = 1/3 and D⁺(V → U) = 1/3, and D_Q = 1/3. A rendering that
told its reader nothing at all would also have D_Q = 1/3 on these two
problems (it loses 1/3 on "Is Z = 1?", since the risk with no information
is 1/3, and gains nothing), but its directed pair is (1/3, 0). The directed
pair tells the two renderings apart, and D_Q does not.

**(e) A prior-free form.** Taking the supremum over priors, or using
minimax risks, gives a task-restricted analogue of Le Cam's deficiency. The
exact relation, with its constants, depends on how losses and deficiency
are normalised and is in Torgersen ([LIT-778](../literature.d/LIT-778.md)), which the record has not
read, so it is not stated here.

## What it does not say

- It does not say Q is fixed. Which tasks are named is a choice
  ([CLAIM-tmpvh0gc](CLAIM-tmpvh0gc.md), [QUESTION-tmppstva](../questions.d/QUESTION-tmppstva.md)), and D⁺ is relative to it.
- It does not say improvements do not matter. They are reported in the
  other direction, D⁺(V → U), as [CLAIM-106](CLAIM-106.md)'s asymmetry asks.
- It does not supply a correspondence of tasks for re-performance
  fidelity. That stays [QUESTION-005](../questions.d/QUESTION-005.md).
