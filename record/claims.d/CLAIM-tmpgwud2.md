---
status: Active
title: 'Agreement between routes of translation is a measure of coherence, not of fidelity, and the two are independent: a rendering that sends every source utterance to one output makes direct and relay transport agree exactly while a receiver who could tell a promise from a prediction with no error is left at chance, and two routes that keep the act and differ in register disagree completely while losing nothing the act-identification task needs'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in either construction. The reading, that path discrepancy
  and task-relative loss must both be measured, is defeated by a bound of
  one by the other over a class of transports a study would actually
  use, for instance one showing that for transports which preserve a
  declared family of tasks, path discrepancy restricted to those tasks'
  observables is zero.
tags:
- translation
- pragmatics
- mathematics
date: '2026-10-29'
line:
- pragmatic-transport
- formal-apparatus
works:
- what-survives-translation
bears_on:
- QUESTION-130
uses:
- TERM-tmpfomje
- TERM-034
complements:
- CLAIM-259
- CLAIM-050
summary: >-
  From A4 and A5 of the exchange "Paper assessment" (2026-10-29), where
  the assistant carried [LIT-tmpr8qf7](../literature.d/LIT-tmpr8qf7.md)'s comparison of alternative paths
  over to translation and then warned that "path agreement is a
  coherence criterion, not a fidelity criterion". The constructions are
  the record's. It does not say path discrepancy is uninformative: it
  says it measures something [CLAIM-259](CLAIM-259.md)'s directed loss does not, and
  conversely.
---
<!-- inactive-ok-file: QUESTION-130 CLAIM-259 — Open or Proposed; the question this bears on and the loss it is set beside, cited as open -->

# CLAIM-tmpgwud2: Agreement between routes of translation is a measure of coherence, not of fidelity, and the two are independent: a rendering that sends every source utterance to one output makes direct and relay transport agree exactly while a receiver who could tell a promise from a prediction with no error is left at chance, and two routes that keep the act and differ in register disagree completely while losing nothing the act-identification task needs

## The claim

Take three communities A, B, C and transports between their response
spaces, given as stochastic kernels. Compare the direct route K_{C←A} with
the relay K_{C←B}K_{B←A} by their path discrepancy, the expected distance
between the two routes' outputs on the source's response distributions
(A4's Δ_{A,B,C}, with d total variation). Set beside it the directed
task loss of [CLAIM-259](CLAIM-259.md): the positive part of the rise in a receiver's
optimal risk on a declared decision problem.

**Agreement with total loss.** Let the source utter a promise or a
prediction with probability ½ each, rendered so that a source reader
names the act with zero error. Let every kernel on both routes send every
input to one fixed output, the same ambiguous expression. The two routes
then give the same output for every input, so Δ = 0. A target reader
sees one expression whatever was said, so the best guess has risk ½ on
the act-identification task with 0–1 loss, and the directed loss is ½,
its maximum for two equiprobable acts.

**Disagreement with no loss.** Let the target's outputs be pairs (act,
register), with register formal or informal. Let the direct route keep the
act and render it formal, and the relay keep the act and render it
informal. For every input the two routes' outputs have disjoint supports,
so Δ = 1, its maximum. A target reader on either route names the act with
zero error, so the directed loss on act identification is 0.

So neither measure bounds the other. A low path discrepancy is evidence
that the routes are coherent with each other, and says nothing about
whether either keeps what a receiver needs. A high one can mean that the
routes keep different things a task does not need. A study of
translation paths needs both measures, and needs the task declared before
the loss is read ([CASE-tmph0fxi](../cases.d/CASE-tmph0fxi.md)).

## What it does not say

- **That consistency is worthless.** In settings where the truth is known
  to be consistent, as in [LIT-tmpr8qf7](../literature.d/LIT-tmpr8qf7.md)'s synchronization benchmark,
  disagreement between routes does locate error ([THEORY-tmpy1s8c](../theory.d/THEORY-tmpy1s8c.md)).
- **That the collapse is only a toy.** It is the extreme of a real
  pressure. A model trained on consistency between routes alone is
  rewarded by moving toward it, as [THEORY-1088](../theory.d/THEORY-1088.md)'s discourse sheaves reach
  consensus by changing their expression maps.
- **That a disagreement which loses nothing on one task is harmless.**
  Register may be what a different task needs. The loss is relative to the
  declared family of tasks, as [CLAIM-348](CLAIM-348.md) warns of coarse-grainings
  generally.
- **Anything about holonomy in the gauge sense.** Stochastic kernels are
  generally not invertible, so path discrepancy is not a Wilson loop and
  carries none of [THEORY-tmpf3jtf](../theory.d/THEORY-tmpf3jtf.md)'s invariance.
