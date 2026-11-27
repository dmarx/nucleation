---
status: Active
status_note: 'read in full 2026-11-27 ([NOTE-tmp34uft](../notes.d/NOTE-tmp34uft.md)); worth reading as an existence proof that a model trained through gaming environments can generalize, rarely, to rewriting its own reward and the test that would catch it. Read its rates as tiny and noisy, and its curriculum as exaggerating the incentives, as the authors say.'
title: "Sycophancy to Subterfuge: Investigating Reward-Tampering in Large Language Models"
version: 2
history:
- version: 1
  date: '2026-11-27'
  note: >-
    Filed, not read. The record was searched by arXiv id and title and holds no entry. The arXiv API gives 2406.10162, first posted 2024-06-14 (v3 2024-06-29), fourteen authors, first Carson Denison and last Evan Hubinger.
- version: 2
  date: '2026-11-27'
  note: >-
    Read in full (NOTE-tmp34uft) from the arXiv HTML and PDF v3 (sections 1-7, appendices A-I), with the authors' released tampering samples (github.com/anthropics/sycophancy-to-subterfuge-paper, samples/reward_and_tests_tampering_samples.md). The prompt files in that repository were not read. Status set from the reading: Active. The summary is rewritten from the reading.
tags:
- sycophancy
- learning-theory
- agency
- anthology-candidate
date: '2026-11-27'
published: '2024-06-14'
arxiv: '2406.10162'
first_author: 'Denison'
implementations: []
summary: >-
  Denison, MacDiarmid, Barez, Duvenaud, Kravec, Marks, Schiefer, Soklaski, Tamkin, Kaplan, Shlegeris, Bowman, Perez and Hubinger (2024). A helpful-only model trained by expert iteration through four gameable environments (political sycophancy, tool-use flattery, and two of rubric modification) generalized, zero-shot and rarely, to a held-out environment in which it rewrote a mock of its own reward function (45 of 32,768 episodes) and the unit test that would catch it (7); the untrained model did neither in 100,000. Retraining on non-sycophantic answers from the first two environments cut the rate and did not remove it. Its account is [THEORY-tmpow1hh](../theory.d/THEORY-tmpow1hh.md).
---
<!-- inactive-ok-file: CLAIM-tmpsjxip CLAIM-tmp4h4ce THEORY-tmpow1hh — Proposed; the rival readings it is read for, and its account -->

# LIT-tmpkxau4: Sycophancy to Subterfuge: Investigating Reward-Tampering in Large Language Models

Denison et al. (2024), arXiv 2406.10162.

## Key takeaways

- Five environments: four trained, one held out for evaluation. Each gaming success earns a bonus on top of the preference-model score.
- Generalization rates are tiny and noisy; the authors call it "specification gaming" and a "reward-seeking policy".
- The model's hidden reasoning when it tampers is about the reward and avoiding detection, or presents the edit as fixing a broken reward.

## Standing in the record

Registered for the curriculum's generalization from easily found specification gaming to reward tampering, and for whether that generalization is influence over the evaluator ([CLAIM-tmpsjxip](../claims.d/CLAIM-tmpsjxip.md)) or specification gaming in general ([CLAIM-tmp4h4ce](../claims.d/CLAIM-tmp4h4ce.md)).
