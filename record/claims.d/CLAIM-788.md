---
number: 788
status: Proposed
formerly:
- CLAIM-tmpydua7
title: 'First Contact''s interface learning is learning occasioned by an obstruction whose product is a new channel: the interface cannot know the user''s task, a failure of information, and it repairs that not by acquiring the information but by forming a channel through which the party who has it, the user, can steer; command-to-outcome mutual information measures that channel without passing through the task, and maximizing it pursues the record''s new channel, a maintained capacity, directly'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  Either of two results. (a) Interfaces learned by maximizing
  command-to-outcome information turn out to encode the particular task
  they were trained on, so that the interface acquired the missing
  information rather than formed a channel; shown by a learned interface
  that helps on its training targets and not on new targets in the same
  domain, the transfer test of CLAIM-532. (b) A case of a failure of
  information that a channel to an informed party cannot repair even in
  principle, because the informed party cannot act through any channel the
  system could form, stated so that it bears on this claim's repair and not
  only on its measure.
tags:
- learning-theory
- agency
- information-theory
date: '2026-11-21'
line:
- will-organization
- distributed-agency
grounds:
- THEORY-2147
rests_on:
- CLAIM-532
- CLAIM-361
bears_on:
- QUESTION-404
complements:
- CLAIM-787
summary: >-
  The owner, 2026-11-21, under the dialectic regime: "relate our theory of
  obstruction-motivated learning to the 'first contact' RL paper". The
  paper is Reddy, Levine and Dragan (2022), held and read by the anthology
  as [ANTH-LIT-503](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-503.md), [ANTH-NOTE-250](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/notes.d/NOTE-250.md) and [ANTH-THEORY-091](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-091.md), not registered here.
  The relation is the assistant's (Claude, in this session); adopting it is
  the owner's call.
---
<!-- inactive-ok-file: CLAIM-787 — Proposed or Open; filed with this on 2026-11-21 -->

# CLAIM-788: First Contact's interface learning is learning occasioned by an obstruction whose product is a new channel: the interface cannot know the user's task, a failure of information, and it repairs that not by acquiring the information but by forming a channel through which the party who has it, the user, can steer; command-to-outcome mutual information measures that channel without passing through the task, and maximizing it pursues the record's new channel, a maintained capacity, directly

## The paper

First Contact (Reddy, Levine and Dragan, 2022; arXiv 2205.12381; read by the
anthology as [ANTH-NOTE-250](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/notes.d/NOTE-250.md)) fits a control interface with no labels, no
reward and no knowledge of the user's task. It scores an interface by the
mutual information I(x_t; (s_t, s_{t+Δ})) between the user's command and
the state transition it induces, and maximizes that by human-in-the-loop
RL while the user adapts too. Offline the score predicted task success in 4
of 5 domains (Spearman ρ = 0.43); online, over 12 users, it tracked task
reward at ρ = 0.87, and the learned cursor interfaces converged on two
mappings, no perturbation and exact inversion. The anthology's reading
([ANTH-THEORY-091](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-091.md)) is that the score rewards a learnable channel, how
reliably input determines outcome, not an intuitive one.

## The relation

The record's theory of learning occasioned by obstruction is [CLAIM-532](CLAIM-532.md): an
unresolved discrepancy is a sufficient occasion, not a guarantee, for a
maintained capacity to form, either a new distinction (the policy comes to
depend on a feature it did not) or a new channel (the outcomes reachable
under one's own policy grow), which outlasts the discrepancy and serves a
class of later ones. The manuscript of pull request 555 states it as P5.

First Contact is a case of it, with three features worth keeping.

- **The obstruction is a failure of information, split between parties.**
  The interface could move the cursor anywhere; what it lacks is which
  target the user wants. That is the obstruction [QUESTION-404](../questions.d/QUESTION-404.md) asks about:
  a path exists and the inputs could execute it, but the system cannot tell
  which response its context calls for. The user has the information and
  lacks the actuation; the interface has the actuation and lacks the
  information.
- **The repair is a channel, not the information.** The interface never
  learns the task. It forms a channel through which the party with the
  information can steer, so that what the pair can reach grows. That is
  [CLAIM-532](CLAIM-532.md)'s new channel, and it suggests an answer to [QUESTION-404](../questions.d/QUESTION-404.md)'s
  last part: one repair for a failure of information is a channel to a
  party that has it.
- **The measure does not pass through the task.** Command-to-outcome
  information is evidence about the channel that does not use the
  categories the task would supply, which is what P3 of the manuscript asks
  of evidence that is to certify a capacity. That is why it can score an
  interface the task is unknown to.

**Who formed what.** In co-adaptation the channel is formed jointly, and
the two converged mappings divide the work differently. At no perturbation
the interface carries the user's existing habit; at exact inversion the user
has formed a new distinction, steering against their habit, and the
interface has installed a mapping. [CLAIM-532](CLAIM-532.md) holds that whether a capacity
was formed or installed cannot be read from it afterwards; the bimodal
result is a case where the same score covers both.

**The test it suggests.** [CLAIM-532](CLAIM-532.md)'s transfer test applies directly: a
channel serves a class, so an interface learned on some targets should help
on new targets in the same domain. The local reading ([NOTE-2236](../notes.d/NOTE-2236.md)) finds
no such test: targets are "randomly-sampled" each episode and the interface
is a single rotation, or a linear map that ignores state, so it cannot
encode a particular target. The channel reading holds by construction, and
defeater (a) is excluded by design, not tested. User adaptation is assumed
(Fig. 1), shown within episodes, and not measured across them.

## What it does not say

- Not that First Contact was framed this way. Its own reason is that an
  intuitive interface makes commands less noisy.
- Not that mutual information measures every channel the record means.
  It measures the channel at a horizon Δ; which horizon is the subject of
  [CLAIM-787](CLAIM-787.md).
- Not the paper's own framing of the score's other half: it also rewards
  information flowing from the state to the user (the perception term),
  which ties the channel to the user's adaptation as well as the
  interface's.
