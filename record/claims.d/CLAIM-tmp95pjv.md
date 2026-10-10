---
status: Proposed
title: 'Fidelity as a report and fidelity as a re-performance are different decision targets: Blackwell''s order compares a rendering with its source as evidence about the source''s situation, which both readers decide about, while a rendering that re-performs the act in the target''s situation is compared only through a correspondence of situations'
version: 1
role: thesis
defeated_if: >-
  Receivers' fidelity verdicts on the same renderings do not differ
  between a report task (what was the source's speaker doing?) and a
  re-performance task (does this do, here, what the source did there?),
  so that the distinction does no work; or the line's central cases are
  shown to be re-performances, so that Blackwell's order reaches none of
  them.
tags:
- information-theory
- translation
- philosophy-of-language
date: '2026-10-10'
line: pragmatic-transport
grounds:
- THEORY-156
objects_to:
- CLAIM-tmpyeik3
complements:
- CLAIM-050
summary: >-
  The record's reply, on 2026-10-10, to [CLAIM-tmpyeik3](CLAIM-tmpyeik3.md), which it
  reconciles rather than refutes. In report fidelity the parameter is the
  source's situation, common to both readers, so Blackwell's order is
  defined; the objection's worked case then gets a precise verdict,
  incomparability, as [CLAIM-128](CLAIM-128.md) expects, and a context-aware translator's
  non-garbling is compared by the order and quantified by
  [CLAIM-tmpz239h](CLAIM-tmpz239h.md). The objection is right about re-performance, where
  [CLAIM-091](CLAIM-091.md)'s compensation lives: there a correspondence of situations is
  needed ([QUESTION-005](../questions.d/QUESTION-005.md)). For report tasks the task correspondence is the
  identity, which removes two of [CLAIM-tmpbi9eb](CLAIM-tmpbi9eb.md)'s points there. A
  proposal; it does not say which kind of fidelity literary translation
  aims at.
---
<!-- inactive-ok-file: CLAIM-tmpyeik3 — Proposed; open, and cited as the objection this replies to, which stands for re-performance -->
<!-- inactive-ok-file: CLAIM-050 CLAIM-091 CLAIM-128 — Proposed; the Blackwell thesis, the compensation claim and the profile claim, cited as open -->
<!-- inactive-ok-file: THEORY-156 — Proposed; cited as the reading of Blackwell's order, not as settled -->
<!-- inactive-ok-file: CLAIM-tmpz239h — Proposed; the restated decision term, cited as the measure this uses -->
<!-- inactive-ok-file: LIT-778 — Deferred; Torgersen, unread here, named and not leaned on -->

# CLAIM-tmp95pjv: Fidelity as a report and fidelity as a re-performance are different decision targets: Blackwell's order compares a rendering with its source as evidence about the source's situation, which both readers decide about, while a rendering that re-performs the act in the target's situation is compared only through a correspondence of situations

## What it answers

This is the record's reply of 2026-10-10 to [CLAIM-tmpyeik3](CLAIM-tmpyeik3.md), which says that
Blackwell's order needs one parameter and that the line's central cases
lack one: the situation changes under compensation ([CLAIM-091](CLAIM-091.md)), and where
it is common, a translator with context knowledge makes a rendering that is
not a garbling. The reply is a reconciliation. The objection runs together
two decision targets. For one of them its premise fails and the order
applies; for the other it is right. The distinction is a proposal: whether
receivers' verdicts track it, and which target the line's central cases
have, are open, and the defeat condition says so.

## The claim

**Two targets.** A reader of a rendering can be asked two kinds of
question.

- **Report.** What was the source's speaker doing, in the source's
  situation? The target reader, like the source reader, decides about the
  source's situation z. The rendering is evidence about z.
- **Re-performance.** Does this rendering do, here, in the target's
  situation z′, what the source did there? The target reader decides about
  z′, and the comparison needs to know which z′ corresponds to which z.

**In report fidelity the order is defined.** Both experiments, P(U | Z) for
the source and P(V | Z) for the rendering, are indexed by the source's
situation, so they share the parameter [THEORY-156](../theory.d/THEORY-156.md) requires ("an n-tuple of
probability measures on a common space, one per state"). A translator who
knows the context makes a rendering that depends on Z other than through
U, so V is not a garbling of U. The order still compares the two. The
direction the manuscript uses (garbling implies no worse) is silent, and
the order's verdict is often incomparability.

[CLAIM-tmpyeik3](CLAIM-tmpyeik3.md)'s worked case, read as a report case. Let Z be uniform on
{1, 2, 3}. The source tells its reader whether Z = 1 (U = 1 if Z = 1, else
U = 0). The rendering tells its reader whether Z = 3 (V = 1 if Z = 3, else
V = 0). Take 0–1 loss.

- "Is Z = 3?" From V the risk is 0, since V answers it. From U: when U = 1
  (probability 1/3), Z = 1 and the answer is certainly no, with no error;
  when U = 0 (probability 2/3), Z is 2 or 3 with probability 1/2 each, so
  any answer is wrong with probability 1/2. The risk is
  (1/3)(0) + (2/3)(1/2) = 1/3.
- "Is Z = 1?" By the same steps with the roles exchanged, the risk is 0
  from U and 1/3 from V.

So each does better on one problem, neither dominates, and they are
incomparable in Blackwell's order. That is a precise verdict, and it is
the verdict [CLAIM-128](CLAIM-128.md) expects: profiles that trade off are incomparable
until a task fixes weights. The size of each direction's loss is what
[CLAIM-tmpz239h](CLAIM-tmpz239h.md)'s directed decision term measures: the rendering loses 1/3
on "Is Z = 1?" and gains 1/3 on "Is Z = 3?".

**In re-performance fidelity the objection holds.** [CLAIM-091](CLAIM-091.md)'s translation
(u, s, a, k, g) → (u′, s, a, k′, g′) compensates for changed social
coordinates, so the target reader decides about a situation with
coordinates (k′, g′). Comparing the experiments needs a correspondence
z ↦ z′ and both indexed by one parameter through it. That correspondence is
[QUESTION-005](../questions.d/QUESTION-005.md)'s, and the record has no anchor for it. Until it does,
Blackwell's order does not reach re-performance.

**What this does to the decision term.** In a report task the paired task
is the same task asked of both readers, so the task correspondence is the
identity. Then [CLAIM-tmpbi9eb](CLAIM-tmpbi9eb.md)'s second point (losses of two different tasks
on one scale) and its fourth (an unanchored correspondence of tasks) do not
arise. They arise for re-performance.

## What it does not say

- It does not say which kind of fidelity literary translation aims at.
  Compensation ([CLAIM-091](CLAIM-091.md)) is a re-performance notion, and much translation
  practice may aim at it.
- It does not say the order reaches the line's central cases. If they are
  re-performances, it does not, and the defeat condition's second clause
  says so.
- It does not supply the correspondence of situations. That is
  [QUESTION-005](../questions.d/QUESTION-005.md).
- It does not say how far apart incomparable experiments are in Le Cam's
  sense; that rests on Torgersen ([LIT-778](../literature.d/LIT-778.md)), unread here.
