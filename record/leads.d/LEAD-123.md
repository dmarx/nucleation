---
number: 123
status: Open
formerly:
- LEAD-tmplcp4l
title: 'Build the three-perspective agenda model with a latent Condorcet cycle, in which a chair or a legibility regime controls which pairwise contests enter the record'
version: 1
stage: idea
priority: medium
method:
- formal
tags:
- emotion-and-affect
- motivation
- self-governance
date: '2026-11-19'
line:
- organizational-affect
- distributed-agency
advances:
- CLAIM-448
- CLAIM-451
- CLAIM-440
summary: >-
  Named in [CLAIM-448](../claims.d/CLAIM-448.md). Filed by the backlog audit of 2026-11-19.
---

<!-- inactive-ok-file: CASE-tmpn19tk — new on 2026-11-22; the executed study this lead produced, cited in the note of 2026-11-22 -->

# LEAD-123: Build the three-perspective agenda model with a latent Condorcet cycle, in which a chair or a legibility regime controls which pairwise contests enter the record

## What it would do

Write the model and compute, for each admission rule, which outcome the
record shows.

Where the record names it:

- [CLAIM-448](../claims.d/CLAIM-448.md): "A three-perspective agenda model with a latent Condorcet
  cycle, where a chair or legibility regime controls which pairwise contests
  enter the record."

## What would count

Outcomes set by admission rather than preference support [CLAIM-448](../claims.d/CLAIM-448.md) and
give it a demonstrated warrant.

## Note of 2026-11-22: carried out

Built as [CASE-tmpn19tk](../cases.d/CASE-tmpn19tk.md), an executed study in numpy
(`scratch/studies/lead-123/`, 9 pytest tests passing). The model takes the
latent Condorcet cycle of [CLAIM-451](../claims.d/CLAIM-451.md)'s example and shows the recorded
outcome under four admission rules: chair exclusion (installs any of the three),
successive agenda (elects the last-introduced option), legibility filter, and a
protected challenge channel (raising the suppressed contest's admission
probability from 0 to 1 drops coherent records 1.0 -> 0.0 and raises recorded
conflict 0 -> 1/3), plus a persistence variant across windows. It illustrates
[CLAIM-448](../claims.d/CLAIM-448.md) and generalizes [CASE-221](../cases.d/CASE-221.md); dated notes on
[CLAIM-448](../claims.d/CLAIM-448.md), [CLAIM-451](../claims.d/CLAIM-451.md) and [CLAIM-440](../claims.d/CLAIM-440.md) record the bearing.
What remains for the owner: whether the demonstrated instance moves
[CLAIM-448](../claims.d/CLAIM-448.md)'s warrant from interpretive to demonstrated, and whether to adopt
[CASE-tmpn19tk](../cases.d/CASE-tmpn19tk.md). The stage and status are left unchanged.
