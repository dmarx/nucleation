---
# Don't copy this file by hand — run `luria new theory`, which assigns the
# code and fills in what a machine can compute.
#
# A theory is a claim about WHY something happens, or about what is true of
# these systems. State it as a finding, not as an instruction: "Batch
# normalization helps by smoothing the optimization landscape" rather than
# "Use batch normalization". If what you are about to write tells the reader
# what to do in machine learning, it is a practice, and it belongs in the
# Anthology of the SOTA (ANTH-ADR-031).

# Active | Proposed | Deferred | Superseded | Rejected, optionally " — note".
# What each one means here is in luria.yaml, and it is NOT what the same word
# means on a practice: this status says whether the record believes the
# ACCOUNT, and an explanation can be `Rejected` while the thing it explained
# goes on working exactly as well as it ever did.
status: 'Proposed'

# REQUIRED while the status is Proposed or Deferred; delete it when the
# explanation goes Active. What would settle it — a KIND of result, not a
# quantity of them (ANTH-ADR-014). An explanation that cannot say what would show
# it wrong is a story, and this field is where that shows up.
promote_when: "A proof, for a stated class of percept-action channels with feedback wider than Fiderer et al.'s one binary memoryless channel, that no maximally predictive agent attains the channel's work capacity. It is refuted for a class by a feedback channel in it whose work-efficient agents include a maximally predictive one. Further single-channel examples cannot settle it."

# The claim. Repeat it as the body's `# THEORY-tmprjbsb:` heading; the lint checks
# that the two agree.
title: "Once an agent's actions affect the percepts it receives, maximal prediction of those percepts is generally not what thermodynamic efficiency requires: in percept-action loops with feedback, maximally predictive agents generally extract less work than the most efficient agent"

version: 1

# One or more topics from luria.yaml, primary first — the same table the
# reading list uses. Take the topic of what the account is about.
tags:
- information-theory
- thermodynamics
- agency
- natural-sciences

date: '2026-10-20'

# There is deliberately no `published:` line. It is DERIVED from the first
# entry in `source:` below, and writing it down is a lint violation, because
# the value has one home and this is not it.

# REQUIRED, and a LIST. The papers this account rests on, primary first. An
# explanation with no paper behind it is a hunch, and the lint will say so.
source:
- LIT-041

# What the index table shows. The title already carries the claim, so spend
# this on provenance and on the sharp edge: who said it, and what it does not
# say. Prose, so bare codes in it get linked by `luria link --fix`.
summary: >-
  Fiderer et al. (2025), [LIT-041](../literature.d/LIT-041.md), read in [NOTE-032](../notes.d/NOTE-032.md), prove that without feedback the work-efficient agents are exactly the maximally predictive ones that randomise and forget their actions, and that with feedback one binary memoryless channel separates predictive, max-entropy-action and efficient agents; from that they assert that with feedback maximally predictive agents are generally inefficient. The record holds as proved, in [THEORY-026](THEORY-026.md), only the one channel. It does not say that efficiency under feedback is a trade-off between prediction and forgetting: in the proved example the efficient agent is memoryless.
extends:
- THEORY-026
---


# THEORY-tmprjbsb: Once an agent's actions affect the percepts it receives, maximal prediction of those percepts is generally not what thermodynamic efficiency requires: in percept-action loops with feedback, maximally predictive agents generally extract less work than the most efficient agent

## Source

Fiderer et al. (2025), [LIT-041](../literature.d/LIT-041.md), read in full in [NOTE-032](../notes.d/NOTE-032.md). They model
agent and environment as coupled hidden-Markov channels and bound the
work extracted per round. Without feedback the efficient agents are
exactly the maximally predictive ones that randomise and forget their
actions (Thm 4). With feedback, one binary memoryless channel makes the
predictive, max-entropy-action and efficient agents three nonempty,
pairwise-disjoint sets (Thm 5). From that they state, in their
introduction, that "in the presence of feedback, maximally predictive
agents are generally inefficient" ([NOTE-032](../notes.d/NOTE-032.md), claim C12).

## What is asserted, and by whom

The thesis is the general form: once an agent's actions affect the
percepts it receives, maximal prediction of those percepts is not what
thermodynamic efficiency requires, and maximally predictive agents
generally extract less work than the most efficient agent. Fiderer et
al. assert it.

## What the record holds toward it

- [THEORY-026](THEORY-026.md) (Active): without feedback, through fixed kernels, the
  dissipation at each switch of the drive equals the memory that fails to
  predict the next input (Still, Sivak, Bell and Crooks), so there only
  nonpredictive memory is wasteful; with feedback, in Fiderer et al.'s one
  binary channel, no predictive agent is efficient. That channel was
  recomputed: the optimum is about 0.272 bits per round, and every
  predictive agent extracts at most zero.
- One existence example is all that is proved. [NOTE-032](../notes.d/NOTE-032.md) notes that the
  Lemma 10 argument extends to any memoryless channel whose action rows
  are pairwise distinct and whose work capacity is positive. That
  extension is the record's reading and has not been checked as a proof.

## What this does not say

- Not that efficiency under feedback is a trade-off between prediction
  and forgetting. The paper's abstract says so, but in the only proved
  example the efficient agent is memoryless ([NOTE-032](../notes.d/NOTE-032.md), C13).
- Nothing about learning systems: the agent knows the full loop and
  nothing is learned.
- Nothing per operation: the quantities are averages.

## What would confirm or reject it

Confirmed by the promote_when: a proof for a stated class of feedback
channels wider than the one binary channel. Rejected for a class by a
feedback channel in it whose work-efficient agents include a maximally
predictive one.
