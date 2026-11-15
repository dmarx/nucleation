---
status: Proposed
promote_when: >-
  A replication on BERT-base, or on another masked language model, with
  the same six properties shows no significant rank correlation between
  probe accuracy and the amnesic drop in word-prediction accuracy, and
  above-chance probe accuracy for the property at layers after the one
  where INLP was applied.
title: 'On Elazar and colleagues, in BERT-base how accurately a linear probe decodes a linguistic property does not predict how much masked-word prediction suffers when the property is removed by iterative nullspace projection, and property information removed at one layer is partly re-decodable at later layers'
version: 1
tags:
- representation-learning
- causality
date: '2026-11-15'
source:
- LIT-tmp52idf
bears_on:
- QUESTION-010
summary: >-
  Elazar, Ravfogel, Jacovi & Goldberg (2021), [LIT-tmp52idf](../literature.d/LIT-tmp52idf.md), read in
  [NOTE-tmpab3ti](../notes.d/NOTE-tmpab3ti.md). The non-correlation rests on six properties (Spearman
  8.5, p = 0.871); the re-decodability is reported for coarse POS in the
  unmasked setting, with the masked setting reversing the layer trend. The
  wording is the reader's; adopting it is the owner's call.
---

# THEORY-tmpi5d5l: On Elazar and colleagues, in BERT-base how accurately a linear probe decodes a linguistic property does not predict how much masked-word prediction suffers when the property is removed by iterative nullspace projection, and property information removed at one layer is partly re-decodable at later layers

## Source

Elazar et al. (2021), [LIT-tmp52idf](../literature.d/LIT-tmp52idf.md); read in [NOTE-tmpab3ti](../notes.d/NOTE-tmpab3ti.md).

## The result

- Across six properties, probe accuracy and the amnesic drop in LM
  accuracy are uncorrelated: "Spearman correlation of 8.5, with a p-value
  of 0.871" (§4).
- Removing coarse POS at one of the first seven layers costs 5.72–12.69
  points of word-prediction accuracy, against 16.57–46.39 in the second
  half of the network, because the information "is highly recoverable in
  subsequent layers" (§7.1, unmasked).
- §9: "we neutralize the information from certain layers, but
  occasionally observe higher probing accuracy in following layers."

## What it does not show

- That probe accuracy never predicts use: six properties is a small
  sample for a rank correlation.
- That the property, rather than its linear correlates, is what INLP
  removed (§9 says this may not hold).
- Anything about nonlinear erasure, other architectures, or the masked
  setting, where the layer trend is reversed.
