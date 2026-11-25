---
number: 859
status: Proposed
formerly:
- CLAIM-tmpywy3c
title: 'Survival exponent is one over the structured share'
statement: >-
  In two distinct mechanisms that mix a structured step with a uniform one,
  preferential attachment or copying with a uniform share and noisy
  sample-space reduction, the tail's survival exponent is one over the
  structured share
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant when closing the first round of the
    remaining readings, from a pattern the filer of Corominas-Murtra et al.
    and Reed and Hughes noted on QUESTION-505. The three exponent formulas
    were checked against the filed NOTEs, and the attachment case by
    simulation (python3 -I; the script is described in the body).
role: supposed
warrant: interpretive
defeated_if: >-
  A third mechanism of the same shape, a structured step taken with
  probability s and a uniform step otherwise, whose stationary tail has a
  survival exponent other than 1/s; or a correct derivation showing that
  noisy sample-space reduction's frequency exponent is not 1 + 1/λ in the
  share λ of nested steps, or that mixed attachment's degree exponent is
  not 1 + 1/(1 − α) in the uniform share α.
tags:
- probabilistic-modeling
- mathematics
date: '2026-11-22'
line:
- formal-apparatus
grounds:
- THEORY-2150
- THEORY-2175
bears_on:
- QUESTION-505
summary: >-
  Two mechanisms the record now holds readings for mix a structured step
  with a uniform one. In attachment with a uniform share (Mitzenmacher,
  [THEORY-2150](../theory.d/THEORY-2150.md); Barabási's directed copying is the same formula, [NOTE-2270](../notes.d/NOTE-2270.md)),
  a new link goes to a uniformly chosen node with probability α and by
  degree otherwise, and the degree density falls as k^−(2−α)/(1−α), so the
  survival exponent is 1/(1 − α). In noisy sample-space reduction
  (Corominas-Murtra et al., [THEORY-2175](../theory.d/THEORY-2175.md)), a step is nested with
  probability λ and uniform otherwise, occupation falls as i^−λ in rank,
  and the frequency exponent is 1 + 1/λ, so the survival exponent is 1/λ.
  In both the survival exponent is one over the share of structured steps:
  structure alone gives the marginal exponent 1, and the uniform share sets
  how far the tail is diluted from it. This is a pattern across two
  mechanisms, offered as a candidate row for [QUESTION-505](../questions.d/QUESTION-505.md), not a theorem;
  whether it reaches past processes of this mixed form is not shown. The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CLAIM-795 CLAIM-803 — Proposed, Rejected, Deferred or new; the entries this filing made or touched -->

# CLAIM-859: Survival exponent is one over the structured share

## The two cases

- **Attachment with a uniform share.** Each new link goes to a uniformly chosen earlier node with probability α, and otherwise to a node chosen in proportion to its degree. [NOTE-2237](../notes.d/NOTE-2237.md) (Mitzenmacher) gives the degree exponent as (2 − α)/(1 − α), that is 1 + 1/(1 − α), so the survival exponent is 1/(1 − α), where 1 − α is the structured (preferential) share. Barabási's directed copying, γ = (2 − p)/(1 − p), is the same formula, as the chapter's NOTE ([NOTE-2270](../notes.d/NOTE-2270.md)) records; it is not a third mechanism.
- **Noisy sample-space reduction.** Each step jumps to a uniformly chosen lower state with probability λ, and uniformly over all states otherwise. Corominas-Murtra, Hanel and Thurner give occupation ∝ i^−λ in rank and the frequency exponent α = (1 + λ)/λ ([NOTE-2266](../notes.d/NOTE-2266.md)), that is 1 + 1/λ, so the survival exponent is 1/λ, where λ is the structured (nested) share.

In both, with the structured step alone (share 1) the survival exponent is 1, the marginal Zipf case; the uniform share dilutes the tail and steepens it in proportion 1/share.

## Check

The attachment case was simulated with python3 -I (script kept in the session scratchpad, `checks/share_tail.py`, not in the repository): 400,000 items, each linking to a uniformly chosen earlier item with probability a and otherwise to the target of a uniformly chosen earlier link (which is choosing by in-degree), with the survival exponent estimated by the Hill estimator on the top 2,000 degrees.

| uniform share a | predicted 1/(1 − a) | Hill estimate |
|---|---|---|
| 0.2 | 1.250 | 1.182 |
| 0.4 | 1.667 | 1.613 |
| 0.6 | 2.500 | 2.154 |

The estimates fall below the prediction, more at the steeper tail, as the Hill estimator does at finite size. The sample-space-reduction case was checked by the reader of Corominas-Murtra et al. (stationary-vector slopes −1.0000, −0.7022 and −0.5027 for λ = 1, 0.7, 0.5; [NOTE-2266](../notes.d/NOTE-2266.md)), which gives the rank exponent λ and so the survival exponent 1/λ.

## What it does not say

- It does not say the two mechanisms are one. Attachment reinforces; sample-space reduction is a Markov chain with no reinforcement ([CLAIM-795](CLAIM-795.md), item 5). The shared form is in how a uniform share dilutes a marginal tail, not in the mechanism.
- It does not cover mechanisms of other shapes. Kesten's κ (fixed by E[A^κ] = 1) and Reed and Hughes's exponent (a root of a quadratic with noise) are balances of a moment against a loss rate, recorded on [QUESTION-505](../questions.d/QUESTION-505.md); they are not of this form.
- It does not make the exponent evidence of a mechanism ([CLAIM-803](CLAIM-803.md)): the same exponent arises from both cases at matched shares.

## Bearing

A candidate row for [QUESTION-505](../questions.d/QUESTION-505.md) (what fixes an exponent): in mixtures of a structured and a uniform step, the exponent counts the uniform dilution.
