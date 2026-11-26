---
status: Proposed
title: 'Accessible corpus growth can raise realization cost'
statement: >-
  Beyond some workload-dependent point, increasing the readily accessible
  corpus increases the cost of realizing inquiries that the corpus already
  contains sufficient information to support: what is held but not needed
  for a task still has to be searched past, recognized as not covering it
  and kept apart from what does, so that holding more can make a held
  answer dearer to reach
version: 1
history:
- version: 1
  date: '2026-11-26'
  note: >-
    Filed from A34 (H2, "Memory interference") of the exchange "Alignment
    consequences brainstorm" (ChatGPT, 2026-11-26). The second clause of
    the statement glosses A's sentence with the mechanism A31 §14 and
    A33 §13 point to. The defeater is the assistant's (step 9a): A's
    "some workload-dependent point" is a free parameter, and a defeater
    that leaves it free could not be met.
role: thesis
warrant: empirical
defeated_if: >-
  For a declared workload of tasks whose answers the record already holds,
  run under a fixed token budget with the information available held
  constant and only its accessibility varied: the cost of reaching the held
  answer (tokens spent, steps taken, or the rate at which the answer is
  re-derived rather than found) does not rise at any accessible-corpus size
  within the record's range, from one line's working view to the whole
  record and its generated views, as entries the tasks do not need are added;
  that holding for each workload tried defeats the claim for this record.
tags:
- information-retrieval
- design-rationale
- cognition
date: '2026-11-26'
line:
- record-as-apparatus
- nucleating-argument
bears_on:
- QUESTION-095
- QUESTION-109
summary: >-
  A's second hypothesis for its pilots, the claim the owner's U15 makes
  about this record ("retired and superseded content still impacts
  retrieval cost and discoverability"; CLAIM-tmpu1fef) stated generally and with a threshold. CLAIM-314 holds one
  mechanism, a recognition cost that grows with the number and size of the
  stored definitions; this claim adds the net effect, that past a point the
  added cost outweighs what holding the answer saved, which is the limit
  QUESTION-095 asks about for leaving results where they can be retrieved.
  The wording is A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-314 CLAIM-1068 CLAIM-180 CLAIM-182 CLAIM-tmp6toz6 CLAIM-tmpu1fef TERM-tmp96b3g — Proposed; the mechanisms and the leads this hypothesis is filed among on 2026-11-26 -->

# CLAIM-tmpdid0k: Accessible corpus growth can raise realization cost

## The claim

A34 states it as H2, "Memory interference": "Beyond some
workload-dependent point, increasing the readily accessible corpus
increases the cost of realizing inquiries that the corpus already contains
sufficient information to support."

The distinction it turns on is between what the record holds and what an
inquiry can reach at its budget. The record draws it as storage against
addressability (CLAIM-182) and, for leaving results to be retrieved, as a
trade whose limits are open (QUESTION-095). The claim says the trade
reverses past a point: accessible but unneeded entries cost more to pass
over than the needed ones save.

## What the record holds near it

- **The mechanism.** CLAIM-314: certifying that stored answers cover a new
  question "grows with the number and size of the stored definitions rather
  than being a constant per item". That is a cost per use that rises with
  the corpus; this claim adds that it can overtake the saving.
- **The symptom.** CLAIM-1068: content the record held under codes was
  re-derived without them in 20 of 48 reconstructed exchanges, "because the
  collaborator had to find the code by what the content said". That is
  held information failing to be realized, measured once and not against
  corpus size, so it neither supports nor tests the threshold.
- **Drift.** CLAIM-180 reads drift as retrieval failure beyond a critical
  distance. More accessible near-duplicates would shrink the distance at
  which a restatement retrieves the wrong one.
- **What adds to accessibility without adding information.** CLAIM-tmp6toz6
  (A31 §14): generated projections repeat an entry's title and summary, so
  a search meets one entry many times.
- **The conditional in CLAIM-761.** Stored work expands capability only net
  of "the costs of constructing, keeping, retrieving, verifying and
  revising" it. This claim says the retrieving term grows with what else is
  kept.

## What it does not say

- It does not say the corpus is too large now; the point is
  workload-dependent and unmeasured.
- It does not say the answer is to delete. Accessibility is what varies;
  the information can stay recoverable (TERM-tmp96b3g).

## How it would be tested

LEAD-tmpolbqp compares ordinary inquiry on one line's working view with
the full retrieval surface; LEAD-tmpe579v replays cooling policies over the
record's history; LEAD-tmp79qro finds the candidates. CASE-091's design,
persistent memory varied with information and token budget controlled
separately, is the controlled form the defeater asks for.
