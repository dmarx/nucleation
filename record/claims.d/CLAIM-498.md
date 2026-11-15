---
number: 498
status: Proposed
formerly:
- CLAIM-tmp4vtm7
title: 'Averaging weights within a basin averages features: the network whose weights are the average of several networks in one low-loss basin has, in every layer, the average of their features'
version: 2
history:
- version: 2
  date: '2026-11-15'
  note: >-
    Note of 2026-11-15 added: Zhou et al. (2024), LIT-tmptiitv, read in
    NOTE-tmpjupyx, assert the step from weight averaging to feature
    averaging and measure it for soups of 5 CIFAR-10 and 10 ImageNet
    ViT-B/32 fine-tunes, finding approximate equality; THEORY-tmpjlixb
    corroborates the claim. SWA iterates and decoder-only language models
    are not measured. In the summary, the sentence "No source measured or
    asserts it: it is the record's step from pairs to many-model averages,
    and its defeater is the averaging half of the old promote_when.", now
    false, is replaced by one naming the reading and what it leaves. No
    status change.
role: thesis
warrant: interpretive
defeated_if: >-
  Measured on the averages practice actually uses, soups of many
  fine-tuned models and SWA iterates, the features of the averaged network
  differ from the average of the members' features, though the claim holds
  for pairs.
tags:
- loss-landscapes
- representation-learning
- anthology-candidate
date: '2026-10-30'
line:
- learned-structure
grounds:
- THEORY-111
bears_on:
- QUESTION-318
summary: >-
  The averaging clause of [THEORY-111](../theory.d/THEORY-111.md)'s old title, kept as a Proposed claim
  by the [ADR-047](../decisions.d/ADR-047.md) sweep of 2026-10-30 (kind 2) when the eleventh status
  review's narrowing had dropped it. Zhou et al. (2024), LIT-tmptiitv,
  assert it and measure it for soups of 5 and 10 ViT-B/32 fine-tunes
  (THEORY-tmpjlixb); SWA iterates, the other half of its defeater, are not
  measured.
---
<!-- inactive-ok-file: ADR-047 — Superseded by ADR-057, which keeps its evidence rulings; cited for the kind-2 rule this entry is filed under -->

# CLAIM-498: Averaging weights within a basin averages features: the network whose weights are the average of several networks in one low-loss basin has, in every layer, the average of their features

## The claim

[THEORY-111](../theory.d/THEORY-111.md) holds that between two linearly connected image classifiers
nearly every layer's features at points on the line are proportional to
the interpolation of the endpoints' features. The record's step is to read
that as a statement about weight averaging in general: if the interior of
a basin is linear in features as well as in loss, then the network whose
weights are an average of several members of the basin computes, layer by
layer, the average of their features. Weight averaging would then be
feature averaging, which is what model soups and stochastic weight
averaging do in practice. [NOTE-512](../notes.d/NOTE-512.md) proposed it in this form; Zhou et al.
do not state it.

## What it does not say

It is not measured. Every measurement behind [THEORY-111](../theory.d/THEORY-111.md) is an
interpolation between two endpoints. A many-model average needs the
conditions of Zhou et al.'s Theorem 1 to hold jointly for every member,
and nothing in the record tests that. Nor does it say why averaging
improves accuracy where it does.

## Note of 2026-10-30: what holds it back

The measurement its defeated_if names has not been made: no reading in the
record compares an averaged network's layer features with the average of
its members' features, for soups of many fine-tuned models or for SWA
iterates ([QUESTION-318](../questions.d/QUESTION-318.md)). Its ground, [THEORY-111](../theory.d/THEORY-111.md), measured pairs at three
interpolation points and found features proportional to the interpolation
in nearly every layer, not equal to it in every layer, so a reading that
answers this should test proportionality layer by layer.

## Note of 2026-11-15: Zhou, Chen, Chen, Zhang & Yan (2024), read

<!-- inactive-ok-file: THEORY-tmpjlixb — Proposed; the reading of 2026-11-15 that measures this claim for soups, cited as corroboration, the claim does not rest on it -->

The 2026-10-30 note said no reading in the record compares an averaged network's layer features with the average of its members' features. That is no longer so. Zhou et al. (2024), [LIT-tmptiitv](../literature.d/LIT-tmptiitv.md), read in [NOTE-tmpjupyx](../notes.d/NOTE-tmpjupyx.md), assert the step ("We explain the averaging of weights as the averaging of features at each layer", §1) and measure it. For soups of 5 CIFAR-10 and 10 ImageNet ViT-B/32 fine-tunes from CLIP, the averaged network's features approximate the average of the members' features, with cosine near 1 and projection-length ratio near 1 (§4.2), in all blocks for the ImageNet soup (App. C.4) and the last 7 blocks for the other. That is approximate equality, the stronger form this note asked a reading to test. [THEORY-tmpjlixb](../theory.d/THEORY-tmpjlixb.md), filed from it, corroborates the claim; the claim does not rest on it. The defeater is not tripped: the soups measured agree with the pairs.

What stays open: SWA iterates, the other half of the defeater, are not measured; nor are decoder-only language models. The soups are same-task fine-tunes from one pretrained start, which fits "within a basin". The paper's multi-model theorem (Theorem 4.2) rests on an unproved transitivity conjecture, so the step from pairs to many models is measured, not derived. Whether soups alone are enough to move the status is the owner's call. No status change.
