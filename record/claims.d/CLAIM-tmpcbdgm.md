---
status: Proposed
title: 'Computational mechanics gives effortless action a cost reading: for a system
  driven without feedback, the average work it dissipates at each switch of its
  drive is the memory it keeps of the current input that fails to predict the next,
  so a memory that keeps only what carries over wastes nothing and effortlessness
  is predictive economy; but wu-wei is action, and with feedback prediction is not
  enough, since in the record''s one worked channel no predictive agent is efficient
  and the efficient agent forgets its actions'
version: 2
history:
- version: 2
  date: '2026-11-23'
  note: >-
    At the status review of 2026-11-23 (ADR-057). The title's clause "the
    work it dissipates is the memory it keeps that fails to predict its
    next input, so a memory that holds only the causal states of its drive
    wastes nothing" is corrected: a drive's causal states can keep what
    the next input does not carry, and then pay for it (a two-state Markov
    drive gives H(X_t|X_{t+1}) > 0), and THEORY-026's identity is an
    average per switch. The claim is kept Proposed; see the note of this
    date.
role: supposed
warrant: interpretive
defeated_if: A model of acting with feedback in which the efficient agents
  are exactly the maximally predictive ones, so that the feedback caveat does
  not hold beyond the one binary channel; or a case of effortless action whose
  cost is not governed by the memory it keeps about its inputs and actions,
  so that the cost reading does not apply to it.
tags:
- information-theory
- thermodynamics
- self-governance
date: '2026-11-23'
line:
- will-organization
- formal-apparatus
grounds:
- THEORY-026
complements:
- CLAIM-541
- CLAIM-tmp0doyo
bears_on:
- QUESTION-494
summary: 'The assistant''s, after the owner''s ruling ([CLAIM-tmpwjpc8](CLAIM-tmpwjpc8.md)) that
  computational mechanics and nonlinear dynamics take precedence in the record''s
  account of wu-wei. It reads effortless action through [THEORY-026](../theory.d/THEORY-026.md), using
  [TERM-062](../terms.d/TERM-062.md)''s causal states, and carries that theory''s own feedback limit.
  Supposed: it is a reading of an Active account ([THEORY-026](../theory.d/THEORY-026.md)) beyond the scope that account states. The wording is the
  assistant''s (Claude, in this session); adopting it is the owner''s call.'
---

<!-- inactive-ok-file: CLAIM-541 CLAIM-tmp0doyo — Proposed; the account read and the claims beside it -->

# CLAIM-tmpcbdgm: Computational mechanics gives effortless action a cost reading: for a system driven without feedback, the average work it dissipates at each switch of its drive is the memory it keeps of the current input that fails to predict the next, so a memory that keeps only what carries over wastes nothing and effortlessness is predictive economy; but wu-wei is action, and with feedback prediction is not enough, since in the record's one worked channel no predictive agent is efficient and the efficient agent forgets its actions

## The reading

[THEORY-026](../theory.d/THEORY-026.md), for a system driven without feedback through fixed kernels,
says the average work dissipated at each switch of the drive equals
I[s_t; x_t] − I[s_t; x_{t+1}]. That is the memory the system keeps of the
current input that does not carry over to the next. Summed over a
protocol it bounds dissipation below. "Predictive memory costs nothing
in it." A memory that keeps of the current input only what carries over to the
next has no nostalgia, so it wastes nothing at the switch (the nostalgia is
nonnegative under a Markov drive, and summed it bounds dissipation from
below when each kernel keeps its equilibrium stationary). That is not the
same as holding the drive's causal states ([TERM-062](../terms.d/TERM-062.md)): they are prescient
for the whole future, yet where the next input does not fix the current
causal state they keep what it does not carry, and pay for it. For a
two-state Markov drive with transition rows (0.9, 0.1) and (0.2, 0.8) the
causal state is the current input, and the nostalgia is H(X_t|X_{t+1}) ≈
0.38 nats.

Read as an account of effortlessness, this adds a third axis to
[CLAIM-541](CLAIM-541.md)'s timing and [CLAIM-tmp0doyo](CLAIM-tmp0doyo.md)'s direction: economy of memory. An
actor whose state is shaped to what its situation will do next pays
nothing for being moved by it. Strain is keeping what does not predict:
nostalgia, in the source's own term.

## The limit, which is the point for action

Wu-wei is action, and action feeds back on its situation. [THEORY-026](../theory.d/THEORY-026.md)
carries the feedback case from Fiderer et al. Without feedback the
efficient agents are exactly those that are maximally predictive and
"randomise-and-forget their actions", which is Boyd, Mandal and
Crutchfield's tape-setting principle: "randomize-and-forget your
actions, predict your percepts". With feedback, in one binary memoryless
channel, the predictive, maximum-entropy-action and efficient agents are
three disjoint sets, "Every predictive agent there extracts at most
zero", and the efficient agent is memoryless.

So under feedback the reading must not equate effortlessness with
prediction. What is economical in the one worked case is an agent that
does not keep its own actions. [QUESTION-494](../questions.d/QUESTION-494.md) asks which partition a
dissipation-minimizing memory keeps in such a loop. This supposition
bears on it: it would make that question the record's formal question
about effortless action.

## Why supposed

[THEORY-026](../theory.d/THEORY-026.md) is Active, but its feedback result is one channel. The step
from dissipated work to felt or organizational effort is a reading, not
a derivation.

## Note of 2026-11-23: what holds it back

The causal-state clause was shown false at this review and corrected the
same day (version 2): a two-state Markov drive with rows (0.9, 0.1) and
(0.2, 0.8) keeps about 0.38 nats it does not carry to the next input. The
corrected reading, and the bound it states from [THEORY-026](../theory.d/THEORY-026.md) for kernels that
keep their equilibrium stationary, want a checked re-derivation in scratch/
before the ruling is made; nothing else holds it back.
