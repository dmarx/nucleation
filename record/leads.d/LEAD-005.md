---
number: 5
status: Open
formerly:
- LEAD-tmpe9tzc
title: 'Reproduce a known result on the thermodynamics of prediction without feedback, as the first milestone toward asking which memory a costed agent with feedback keeps'
version: 1
stage: idea
method:
- formal
tags:
- thermodynamics
- information-theory
date: '2026-11-19'
line:
- learned-structure
advances:
- QUESTION-494
summary: >-
  ChatGPT's first milestone for [QUESTION-494](../questions.d/QUESTION-494.md) (A80, A84): reproduce a known
  no-feedback result before adding feedback, so that the question's model
  is checked against what is known.
---
<!-- inactive-ok-file: CASE-tmp3axlj CLAIM-tmpk8x2j CLAIM-tmpx0pvr CLAIM-tmpk8zw2 CLAIM-tmpj5z7a — filed by the lead run of 2026-11-23 -->

# LEAD-005: Reproduce a known result on the thermodynamics of prediction without feedback, as the first milestone toward asking which memory a costed agent with feedback keeps

## What it would do

Choose a published result on the cost of predictive memory without
feedback, reproduce it in a small finite-state model, then add feedback
and compare memories that keep the predictive partition, the
interventional partition, or neither.

## What is not yet settled

Which result to reproduce; that needs a reading lead first, and the
record has not yet named one.

## Note of 2026-11-23: reproduced, then run with feedback

Carried out by a delegated lead worker; code, 15 tests and results under
scratch/studies/lead-005/. The result chosen is Still, Sivak, Bell and
Crooks (2012), the one QUESTION-494 names. It was already registered and
read (LIT-327, NOTE-295) and held as THEORY-026, so no second reading was
filed. Its text was re-checked from arXiv v3. THEORY-026's note of
2026-10-19 had a one-off numerical check without code; nothing held a
reproduction with code, or the feedback half.

One executed study, CASE-tmp3axlj, in three parts:

- **Without feedback**, in 300 random driven systems, every identity and
  bound of the paper holds and no step's nostalgia is negative.
- **With feedback** from state to drive, the identities and the summed
  bound still hold, but the nostalgia, and in a few systems the
  dissipation itself, go negative: CLAIM-tmpk8x2j.
- **A percept–action loop** in which the predictive partition is a sticky
  nuisance and the interventional partition is the context the action
  must match. The memory keeping only the context is the cheapest that
  does the task, by every cost measured. The policy that uses a memory
  changes its nostalgia and not its heat: CLAIM-tmpx0pvr. Which partition
  that memory keeps depends on what the interventional partition is taken
  relative to, so two alternative claims are filed: CLAIM-tmpk8zw2 (the
  outcome: the interventional partition; the assistant leans here) and
  CLAIM-tmpj5z7a (the whole percept: neither).

What remains: a memory that revises (every kernel and policy here is
fixed); pricing the controller that reads the memory; a loop with a hidden
common cause, where the partitions differ as THEORY-1146 describes. The
choice between the two alternative claims is the owner's.
