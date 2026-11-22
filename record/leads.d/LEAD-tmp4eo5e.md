---
status: Open
title: 'Separate interface improvement from user accommodation in an adaptive scroll interface: cross user experience with a fixed or updated mapping, freeze the mapping at intervals, test transfer to unfamiliar documents, and restore standard scrolling for a while to see what the user can do unassisted'
version: 1
stage: idea
priority: medium
method:
- empirical
tags:
- learning-theory
- control-theory
- agency
date: '2026-11-22'
line:
- will-organization
- distributed-agency
advances:
- CLAIM-788
- CLAIM-532
- QUESTION-504
operationalized_in:
- CASE-tmptzhse
summary: >-
  From A8 §2C and §3B of the exchange "Explain First Contact RL" (ChatGPT,
  2026-11-22). First Contact assumes the user adapts and does not measure
  it, and runs no transfer test (NOTE-2236); A proposes a design that does
  both in the smart-scroll setting, with an arm that removes the
  adaptation. The wording is A's (ChatGPT, in the exchange of 2026-11-22);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-788 QUESTION-504 CASE-tmptzhse — Proposed or Open; the entries this would test and the case holding its design -->

# LEAD-tmp4eo5e: Separate interface improvement from user accommodation in an adaptive scroll interface

## What to do

The design is part 4 of CASE-tmptzhse. A's conditions:

| Condition | User experience | Scroll mapping |
|---|---|---|
| Baseline | Untrained | Standard |
| Learning only | Increasing | Fixed |
| Adaptation only | Measured | Updated |
| Co-adaptation | Increasing | Updated |

The adaptation-only arm cannot remove human learning, so exposure is
randomized and counterbalanced, and the learned mapping is frozen at
intervals. Then two tests: transfer, the mapping learned on one document
used on unfamiliar ones; and removal, standard scrolling restored for a
block, with performance compared against the learning-only group.

## What it would move

- **CLAIM-788** defeater (a): a mapping that helps on its training
  documents and not on new ones would have learned the content, not formed
  a channel.
- **CLAIM-532**: the transfer test is its test of a maintained capacity.
- **QUESTION-504**: lower unassisted performance after co-adaptation, at
  equal assisted performance, would be erosion the score cannot see.
