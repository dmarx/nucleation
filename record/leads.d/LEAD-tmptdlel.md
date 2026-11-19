---
status: Open
title: 'Run the identity-acquisition study: when does a capability reachable by sampling become reliable in training, and does reliability coincide with the learned identity becoming localized'
version: 1
stage: idea
method:
- empirical
tags:
- representation-learning
- learning-theory
- individuation
date: '2026-11-19'
line:
- learned-structure
advances:
- CLAIM-697
- CLAIM-695
- CLAIM-tmpvnjh2
- QUESTION-039
- QUESTION-tmpihjeu
operationalized_in:
- CASE-tmpoqr8p
summary: >-
  The owner's suggestion of 2026-11-19 that the unfinished identity
  projects (LIT-tmpevryj, LIT-tmp64sbf) offer a directional experiment for
  accidental against reliable capability. Complements the backlog audit's
  lead for CLAIM-699 (pull request 542), which compares RL with best-of-N
  at matched compute.
---
<!-- inactive-ok-file: CASE-tmpoqr8p CLAIM-697 CLAIM-695 CLAIM-tmpvnjh2 — Proposed or newly filed; cited in this filing -->

# LEAD-tmptdlel: Run the identity-acquisition study: when does a capability reachable by sampling become reliable in training, and does reliability coincide with the learned identity becoming localized

## What it would do

Run CASE-tmpoqr8p: fine-tune a text-to-image model on new identities, and
across checkpoints set best-of-N verifier success (reachable by sampling)
against the owner's identity strength and single-sample success
(reliable), then probe and intervene on an identity-specific direction at
the transition.

## What would count

A measured gap between the checkpoints at which identities become
reachable by sampling and those at which they become reliable would bear
on CLAIM-695's account of amortized search and on QUESTION-039. A
direction whose removal takes away reliability but not sampling
reachability would support CLAIM-tmpvnjh2's independence of
identifiability and localization in this domain; no such direction at any
stage would bear on the owner's alternative that identities stay
compositional.

## Cost

Not estimated; small fine-tunes of an open text-to-image model, a
face-match model and repeated sampling at each checkpoint.
