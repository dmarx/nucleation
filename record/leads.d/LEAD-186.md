---
number: 186
status: Open
formerly:
- LEAD-tmpxhqs2
title: 'Read the owed IP-Adapter work and test whether a LoRA learned on one base model is reusable on its successor'
version: 1
stage: idea
priority: medium
method:
- reading
- empirical
tags:
- learning-theory
- cognition
- embodied-cognition
date: '2026-11-19'
line:
- distributed-agency
- nucleating-argument
advances:
- CLAIM-647
- QUESTION-095
summary: >-
  Named in [ARG-079](../arguments.d/ARG-079.md) and the curation entry of 2026-11-12 (015626). Filed by
  the backlog audit of 2026-11-19.
---
<!-- inactive-ok-file: ARG-079 CLAIM-647 — Proposed; cited in the backlog audit of 2026-11-19 -->

# LEAD-186: Read the owed IP-Adapter work and test whether a LoRA learned on one base model is reusable on its successor

## What it would do

Read the IP-Adapter paper in full, then train a LoRA on one base model and
measure what of it survives on the successor model.

Where the record names it:

- [ARG-079](../arguments.d/ARG-079.md): "The ARG stays Proposed until a transfer test."
- The curation entry of 2026-11-12 (015626): "the IP-Adapter abstract
  quote was checked against arXiv, and the reading is still owed"

## What would count

A LoRA that transfers weakens [CLAIM-647](../claims.d/CLAIM-647.md)'s premise that stored adaptations
erode with the base; one that does not supports it and lets [ARG-079](../arguments.d/ARG-079.md) move.

## Note of 2026-11-22: the reading already held, as [NOTE-1722](../notes.d/NOTE-1722.md)

The lead audit of this date found the reading half already done.
[NOTE-1722](../notes.d/NOTE-1722.md) (Read, dated 2026-11-12) reads the IP-Adapter paper
(arXiv 2308.06721) in full, abstract, §§1–5 and Table 1, and finds that
the abstract's "not compatible with other base models" concerns transfer
between fine-tunes of one base, not to a successor base, so [CLAIM-647](../claims.d/CLAIM-647.md)
carries less than it cited the paper for. The curation entry of
2026-11-12 (015626) that called the reading owed was overtaken the same
day. The LoRA transfer test is not held. No status or stage is changed
here.
