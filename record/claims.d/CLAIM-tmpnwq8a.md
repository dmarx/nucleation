---
status: Proposed
title: 'A specialization learned into a model''s weights goes stale when the base model it was trained against is replaced, though nothing it encodes has become false: its reuse ends at the next base-model change, so in the trade between learning once and computing on demand the reader''s turnover is a staleness term of its own, beside the world''s changing, and faster turnover of base models favours computing on demand'
version: 1
role: thesis
warrant: empirical
defeated_if: >-
  Character LoRAs, or other fine-tuned specializations, shown to carry over
  to a replacement base model at fidelity and cost near retraining's, so
  that a base-model change does not end their reuse; or practitioners'
  choices shown not to respond to the pace of base-model releases once
  per-use costs are held fixed. Also defeated as a claim of its own if it
  only restates a held entry: CLAIM-303's upkeep term (checking a filing
  is still current) and Dasgupta and Gershman's staleness, a store "not yet
  updated" after the world changes (QUESTION-095's note of 2026-10-15),
  are about the stored content going out of date; this is about the reader
  of the store being replaced while the content stays right, which neither
  states.
tags:
- learning-theory
date: '2026-11-12'
line:
- distributed-agency
bears_on:
- QUESTION-095
grounds:
- LIT-tmptzx4q
summary: >-
  The assistant's idea, offered at the filing of "Identify Synthesis
  Opportunities" and accepted by the owner. QUESTION-095's notes found that
  the readings price expected reuse and per-use cost but not staleness or
  the erosion of the alternative. In the owner's case CASE-tmp40vka, a
  trained character LoRA is tied to the base model it was trained on. When
  the base model is replaced, the LoRA's content is still right about the
  character, but nothing reads it. So the expected reuse that must repay
  the training is cut off at the next replacement. The evidence so far is
  one sentence of the IP-Adapter abstract, about a neighbouring kind of
  fine-tuning; the reading of IP-Adapter (LIT-tmptzx4q) is still owed, and
  the claim is a hypothesis until it and a transfer test are in. The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CASE-tmp40vka CASE-tmp3isyl — Proposed; filed from the same exchange -->
<!-- inactive-ok-file: LIT-tmptzx4q — Deferred; registered from the same exchange, not read -->
<!-- inactive-ok-file: CLAIM-303 — Proposed; the break-even this adds a term to -->

# CLAIM-tmpnwq8a: A specialization learned into a model's weights goes stale when the base model it was trained against is replaced, though nothing it encodes has become false: its reuse ends at the next base-model change, so in the trade between learning once and computing on demand the reader's turnover is a staleness term of its own, beside the world's changing, and faster turnover of base models favours computing on demand

## The claim

In CLAIM-303's arithmetic, learning pays when the uses n exceed the
up-front cost over the per-use saving, n > F/(c_r − c_a − u). For a
specialization learned into weights, n is bounded by the uses that fall
before its base model is replaced, since a replacement ends its reuse and
F must be paid again. If replacements come every T and uses at rate λ,
learning pays only when λT exceeds the break-even. Shorter T raises the
bar for learning and favours conditioning on references at each use.
The references themselves carry over to the new base model; a reference
adapter may need retraining too, but by its maker, once for every user,
not by each user for each character.

This staleness differs from the two the record holds. Dasgupta and
Gershman's is the world moving away from a stored answer. CLAIM-303's
upkeep is checking that a filed argument is still current. Here the
stored thing stays correct, and the system that reads it is what
changes. The speed bugs of QUESTION-095's cockpit case would go stale
this way if the airspeed indicator were replaced by one with no bugs.

## Evidence, and what is owed

- **The IP-Adapter abstract** (arXiv 2308.06721, checked on 2026-11-12):
  "Although existing methods of direct fine-tuning from pretrained models
  are effective, they require large computing resources and are not
  compatible with other base models, text prompt, and structural
  controls." That sentence is about fine-tuning a model for image prompts,
  not about character LoRAs. It is a neighbouring instance, not a test.
  The paper is registered and not read (LIT-tmptzx4q).
- **The test.** CASE-tmp3isyl's design can take one more arm: a LoRA
  trained on one base model, applied to its successor, scored at the same
  fidelity target. A transfer near retraining's fidelity defeats the
  claim for that pair.
- **What would support it**: practitioner records of LoRAs retrained
  across base-model releases, or of reference workflows adopted at a
  release.

## What it does not say

- That reference conditioning is cheaper per use. That is the case's open
  question, and this claim holds per-use costs fixed.
- That every learned specialization is tied to its reader. Some adapters
  are designed to transfer within a model family; how far that holds is
  the empirical part.
