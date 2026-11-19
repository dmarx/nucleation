---
status: Proposed
title: 'Akter and colleagues find that replacing a fifth of an 8B language model''s general pretraining data with reasoning-style data raises its accuracy after the same supervised fine-tuning and after reinforcement learning, and that doubling a baseline''s fine-tuning data does not close the gap'
version: 1
source:
- LIT-tmpofzg6
tags:
- learning-theory
- representation-learning
date: '2026-11-19'
promote_when: >-
  An independent study, or a rerun with several seeds at a second model
  size, finds that models pretrained with a share of reasoning data at
  matched total pretraining tokens end above a no-reasoning baseline after
  an identical SFT recipe, and above that baseline given twice the SFT
  data.
summary: >-
  From the reading of [LIT-tmpofzg6](../literature.d/LIT-tmpofzg6.md) in [NOTE-tmpw5r9u](../notes.d/NOTE-tmpw5r9u.md). An earlier phase that
  raises what later fine-tuning reaches, measured as final scores.
  Proposed until its promote_when is met.
---

# THEORY-tmpgk8nb: Akter and colleagues find that replacing a fifth of an 8B language model's general pretraining data with reasoning-style data raises its accuracy after the same supervised fine-tuning and after reinforcement learning, and that doubling a baseline's fine-tuning data does not close the gap

## The account

Four 8B arms pretrained on 1T tokens, three with 20 per cent reasoning data; after the same SFT the reasoning arms average 35.92 against 26.62, and the baseline with doubled SFT reaches 34.01 against 37.33 for the weakest reasoning arm. Diverse data helps most in pretraining, high-quality data most in SFT.

## Evidence

One run per arm; total reasoning data not held fixed; no cost measured.
