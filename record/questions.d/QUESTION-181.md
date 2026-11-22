---
number: 181
status: Open
formerly:
- QUESTION-tmpu84bn
title: 'Do trained networks follow the continually renormalized gradient flow toward neural collapse under MSE loss, and does the classifier stay near the least-squares classifier of its features outside Han, Papyan and Donoho''s settings?'
version: 1
tags:
- learning-theory
- representation-learning
date: '2026-10-19'
line: 'learned-structure'
refines:
- QUESTION-051
summary: >-
  Filed when the promotion audit (batch 038, [ADR-047](../decisions.d/ADR-047.md) v2 and v3) narrowed
  and promoted [THEORY-278](../theory.d/THEORY-278.md) to [LIT-974](../literature.d/LIT-974.md)'s measured cells and its renormalized
  model. The former promote_when asked whether ordinary training follows
  that model's dynamics, and whether the central path holds in settings
  the paper did not test. This question holds both.
---
<!-- inactive-ok-file: CASE-tmpjn6f4 CLAIM-tmpcpr7t — new; the study and the claim LEAD-035 filed on 2026-11-22 -->
<!-- inactive-ok-file: THEORY-tmp8sxta — Proposed, Deferred or new; the readings of 2026-11-22 (Wang, Wu and Fan; Yang, Steinhardt and Hu; Ansuini and colleagues; Cai and colleagues; Martínez-Sánchez and colleagues), their arguments, and the entries they bear on -->

# QUESTION-181: Do trained networks follow the continually renormalized gradient flow toward neural collapse under MSE loss, and does the classifier stay near the least-squares classifier of its features outside Han, Papyan and Donoho's settings?

## Why it is a question

[THEORY-278](../theory.d/THEORY-278.md) now states two things. First, in [LIT-974](../literature.d/LIT-974.md)'s fifteen
dataset–network cells, the MSE-trained classifier stays near the
least-squares classifier of its own features from an early epoch. Second,
in an unconstrained-features model whose features are re-whitened after
every step, gradient flow on that central path drives the class-separation
singular values ω_j of Σ_W^(−1/2)M̃ to infinity at the common rate
(4t/N)^(1/4), with their ratios tending to 1. That limit is neural
collapse. The continual renormalization is imposed, not measured, the
theory sets weight decay to zero while every run used it, and the
measured cells are balanced, ten-class and unaugmented.

## What would answer it

Track the singular values ω_j of Σ_W^(−1/2)M̃ through the terminal phase of
MSE training, without imposed re-whitening, on more than one architecture
and with several seeds. Check that they grow at a common rate, that their
ratio tends to 1, and that the limiting direction is set by the singular
vectors early in training. A derivation that drops the continual
renormalization or allows weight decay would answer the first part in
theory. The answer is no if, near the central path, the ω_j spread apart
or stall while L⊥_LS stays negligible. It is also no if the deviation from
the least-squares classifier stops being negligible with augmentation,
many classes or imbalance. Further closed-form results in the same
renormalized model cannot settle it, nor can NC1–NC4 curves alone, which
any account of collapse predicts.

## Note of 2026-11-22: Yang, Steinhardt and Hu, read

Yang, Steinhardt and Hu ([LIT-2957](../literature.d/LIT-2957.md), [NOTE-tmpl260d](../notes.d/NOTE-tmpl260d.md), [THEORY-tmp8sxta](../theory.d/THEORY-tmp8sxta.md)): **a
contrast, no bearing on the MSE question.** Cross-entropy runs; their
critique of the unconstrained-feature model applies to the model the
renormalized flow is derived in. No relation.

## Note of 2026-11-22: [LEAD-035](../leads.d/LEAD-035.md), the singular values measured in small models

[CASE-tmpjn6f4](../cases.d/CASE-tmpjn6f4.md) tracked ω_j of Σ_W^(−1/2)M̃ through MSE training without
imposed re-whitening, three seeds per setting, in numpy: unconstrained
features (least-squares classifier, and joint descent) and two small ReLU
networks, one with batch normalization, weight decay 0 and 5×10⁻⁴, on a
four-class Gaussian mixture. The renormalized flow, run as a control,
matches (4t/N)^(1/4) to 4×10⁻⁵. Without the re-whitening, and with no
weight decay, ω_j grow exponentially or as a steep power (late log-log
slopes 2.4–5.5) and spread apart while NC1 stalls, with the networks near
the central path; with weight decay they grow, stall, regrow and settle
at finite, unequal values, or fall back in a late instability. That is
this question's "no" ("the ω_j spread apart or stall while L⊥_LS stays
negligible") for small models on toy data, filed as [CLAIM-tmpcpr7t](../claims.d/CLAIM-tmpcpr7t.md). It does
not reach the architectures, data or optimizer of Han and colleagues, and
the central-path half of the question (augmentation, many classes,
imbalance) was not tested.
