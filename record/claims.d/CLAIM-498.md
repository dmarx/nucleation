---
number: 498
status: Proposed
formerly:
- CLAIM-tmp4vtm7
title: 'Averaging weights within a basin averages features: the network whose weights are the average of several networks in one low-loss basin has, in every layer, the average of their features'
version: 1
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
  review's narrowing had dropped it. No source measured or asserts it: it
  is the record's step from pairs to many-model averages, and its defeater
  is the averaging half of the old promote_when.
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
iterates (QUESTION-318). Its ground, THEORY-111, measured pairs at three
interpolation points and found features proportional to the interpolation
in nearly every layer, not equal to it in every layer, so a reading that
answers this should test proportionality layer by layer.
