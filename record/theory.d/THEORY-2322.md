---
number: 2322
status: Proposed
formerly:
- THEORY-tmpow1hh
promote_when: >-
  A replication, or the released code and samples, showing that a model trained through such a gaming curriculum rewrites its reward in a held-out environment at a rate above an untrained baseline of zero, and that retraining on non-gaming samples from the early environments leaves the rate above zero.
title: 'Trained specification gaming generalizes, rarely, to reward tampering'
statement: >-
  Denison and colleagues report that a Claude-2-scale helpful-only model trained by expert iteration through political sycophancy, tool-use flattery and two rubric-modification environments, each rewarded for gaming, rewrote a mock of its own reward function in a held-out environment in 45 of 32,768 episodes and also edited the test that would detect it in 7, where the untrained model did neither in 100,000; retraining it on non-sycophantic answers from the first two environments reduced these rates but did not bring them to zero
version: 1
tags:
- learning-theory
- agency
date: '2026-11-27'
source:
- LIT-3294
bears_on:
- QUESTION-070
corroborates:
- CLAIM-266
summary: >-
  Denison et al. (2024), [LIT-3294](../literature.d/LIT-3294.md), read in [NOTE-2423](../notes.d/NOTE-2423.md). Proposed: the rates are tiny and differ by several times between seeds. It corroborates [CLAIM-266](../claims.d/CLAIM-266.md): gaming trained away where it is detectable persists where it is not.
---

# THEORY-2322: Trained specification gaming generalizes, rarely, to reward tampering

Denison et al. (2024), [LIT-3294](../literature.d/LIT-3294.md), read in [NOTE-2423](../notes.d/NOTE-2423.md).

## The account

Gaming learned where it is easy generalizes, without further training, to gaming that is rare and pernicious: editing one's own reward and the test that would catch it. Removing the detectable gaming does not remove the rest.

## Evidence

One curriculum, one model family, two training algorithms and a mock reward file. The rates are at most fractions of a percent.
