---
status: Active
title: "With finitely many states and finitely many outcomes, the positive part of the Bayes-risk increase on the same decision problem is directed, is zero from a garbling back to its source, vanishes for every finite problem and prior exactly when the rendering is at least as informative as the source, and has A86's D_Q as its symmetrization"
version: 1
history:
- version: 1
  date: '2026-10-19'
  note: >-
    Split from CLAIM-326 and filed Active at the owner's direction, carrying
    out the promotion audit's decision (record/promotion-audit/decisions/CLAIM-326.yaml,
    batch 014, ADR-047). CLAIM-326's step (b) uses the converse of
    Blackwell's theorem. With finitely many outcomes that converse is
    THEORY-717, which is Active. For unrestricted outcome spaces it is
    THEORY-156, which is Proposed. This claim is steps (a) to (d) on the
    finite case, which is the case coded renderings fall in. CLAIM-326
    keeps the general statement and rests on it.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in steps (a) to (d) for experiments with finitely many states and
  finitely many outcomes: a finite problem with losses in [0, 1] and a prior
  under which a garbling has lower Bayes risk than its source; two such
  experiments with D⁺(U → V; π) = 0 for every finite problem and prior where
  U is not reproducible from V by a Markov matrix; or a pair for which D_Q,
  with the identity on tasks and the same prior, differs from
  max(D⁺(U → V), D⁺(V → U)).
tags:
- mathematical-statistics
- information-theory
date: '2026-10-19'
line:
- pragmatic-transport
- formal-apparatus
grounds:
- THEORY-717
supports:
- CLAIM-259
- CLAIM-326
summary: >-
  The finite-outcome part of [CLAIM-326](CLAIM-326.md). Define
  D⁺_Q(U → V; π) = sup over q in Q of [r_q,π(V) − r_q,π(U)]⁺, with losses in
  [0, 1] and a stated prior. A garbling never gains. The term is directed.
  A86's D_Q is its symmetrization. And with every finite problem and prior,
  it vanishes exactly when V is at least as informative as U, by Blackwell's
  Theorem 6 ([THEORY-717](../theory.d/THEORY-717.md)). It does not cover outcome spaces that are not
  finite, or say this is the right decision term.
---
<!-- inactive-ok-file: CLAIM-326 CLAIM-259 THEORY-156 — Proposed; the general statement this was split from, the proposal it supports, and the general converse this does not use, cited as open -->

# CLAIM-tmpew698: With finitely many states and finitely many outcomes, the positive part of the Bayes-risk increase on the same decision problem is directed, is zero from a garbling back to its source, vanishes for every finite problem and prior exactly when the rendering is at least as informative as the source, and has A86's D_Q as its symmetrization

## The claim

**Setting.** U is the source and V the rendering, both experiments about
one situation Z with finitely many values. U and V each take finitely many
values. That is the case once renderings are coded into finitely many
categories. A decision problem q has a finite set of actions and a loss
L_q(z, a) in [0, 1], and π is a stated prior on Z. r_q,π(U) is the least
expected loss under π over rules that read U, and

D⁺_Q(U → V; π) = sup over q ∈ Q of [r_q,π(V) − r_q,π(U)]⁺.

**(a) A garbling never gains.** Suppose P(V | Z) = G P(U | Z) for a Markov
matrix G. A rule δ that reads V gives the rule "apply G to U, then δ", with
the same distribution of actions under each z. So r_q,π(U) ≤ r_q,π(V), and
D⁺(V → U; π) = 0.

**(b) The converse.** Suppose D⁺(U → V; π) = 0 for every finite problem
with losses in [0, 1] and every prior. Then r_q,π(V) ≤ r_q,π(U) for all of
them. Rescaling a bounded loss by L ↦ (L − m)/(M − m) maps every Bayes risk
by the same increasing affine map, so the inequality holds for every
bounded loss. By Blackwell's Theorem 6 ([THEORY-717](../theory.d/THEORY-717.md)), U is then
reproducible from V by a Markov matrix.

**(c) It is directed.** With Z uniform on {0, 1}, U = Z, V constant and
q = "guess Z" under 0–1 loss, r(U) = 0 and r(V) = 1/2. So D⁺(U → V) = 1/2
and D⁺(V → U) = 0.

**(d) A86's D_Q is its symmetrization.** With the identity on tasks and the
same prior, D_Q(U, V) = sup_q |r_q(U) − r_q(V)|. Since
|x| = max([x]⁺, [−x]⁺), and a supremum of maxima is the maximum of the
suprema, D_Q(U, V) = max(D⁺(U → V), D⁺(V → U)).

For example, take [CLAIM-323](CLAIM-323.md)'s experiments: Z is uniform on
{1, 2, 3}, U says whether Z = 1, and V says whether Z = 3.
- On "is Z = 3?" the risks are 1/3 from U and 0 from V. On "is Z = 1?"
  they are 0 and 1/3.
- So the directed pair is (1/3, 1/3).
- A constant rendering has risk 1/3 on both problems, which gives the pair
  (1/3, 0).
- D_Q is 1/3 in both cases.

## What it does not say

- It says nothing about outcome spaces that are not finite, such as raw
  texts. There step (b) needs the general converse, which [CLAIM-326](CLAIM-326.md)
  keeps on [THEORY-156](../theory.d/THEORY-156.md).
- It does not say this is the decision term fidelity should use. That is
  [CLAIM-259](CLAIM-259.md)'s proposal.
- It does not state the prior-free form or the relation to Le Cam's
  deficiency.
