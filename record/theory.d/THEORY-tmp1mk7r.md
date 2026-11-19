---
status: Proposed
title: 'Hernandez and colleagues find that, in the low-data regime, pretraining a transformer on text is worth an amount of from-scratch Python data that grows as a power law in the fine-tuning data and in model size, so that it multiplies the fine-tuning data by a factor that falls as that data grows, and that outside this regime pretraining can leave small models worse than training from scratch'
version: 1
source:
- LIT-tmpcdjoe
tags:
- learning-theory
- representation-learning
- anthology-candidate
date: '2026-11-19'
promote_when: >-
  An independent study with several seeds fits effective data transferred,
  measured against same-size from-scratch models at equal loss, as a power
  law in fine-tuning data and parameter count in the low-data regime for
  at least one source–target pair, with exponents and their uncertainty
  stated, and shows pretrained small models falling short of from-scratch
  performance once fine-tuning data approaches the amount that saturates
  them.
corroborates:
- CLAIM-756
- CLAIM-758
summary: >-
  From the reading of LIT-tmpcdjoe in NOTE-tmpmxg4d. The cleanest measure
  on record of an earlier acquisition lowering a later one's sample cost;
  pretraining's own cost excluded. Proposed until its promote_when is met.
---

# THEORY-tmp1mk7r: Hernandez and colleagues find that, in the low-data regime, pretraining a transformer on text is worth an amount of from-scratch Python data that grows as a power law in the fine-tuning data and in model size, so that it multiplies the fine-tuning data by a factor that falls as that data grows, and that outside this regime pretraining can leave small models worse than training from scratch

## The account

D_T = k·D_F^α·N^β, with α≈0.18 and β≈0.38 for text→Python and α≈0.096 for text and code→Python, fitted over four orders of magnitude in size and three in fine-tuning data. The multiplier (D_F+D_T)/D_F falls with D_F and rises with N. Beyond a tenth of saturating data the fit fails, and small pretrained models do not reach from-scratch performance.

## Evidence

No seeds or confidence intervals; one target; pretraining cost never counted.
