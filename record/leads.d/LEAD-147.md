---
number: 147
status: Open
formerly:
- LEAD-tmpqgjya
title: 'Derive the PMI spectrum of a co-occurrence model with implication among binary attributes, and measure PMI additivity across a known hierarchy and across analogy families'
version: 1
stage: idea
priority: high
method:
- formal
- empirical
tags:
- representation-learning
- mathematics
date: '2026-11-19'
line:
- pragmatic-transport
advances:
- QUESTION-025
- QUESTION-178
summary: >-
  [QUESTION-025](../questions.d/QUESTION-025.md) is among the most-cited questions in the record and names
  both halves. Named in [QUESTION-025](../questions.d/QUESTION-025.md) and [QUESTION-178](../questions.d/QUESTION-178.md). Filed by the
  backlog audit of 2026-11-19.
---
<!-- inactive-ok-file: CASE-344 — new, filed today by this lead's run -->

# LEAD-147: Derive the PMI spectrum of a co-occurrence model with implication among binary attributes, and measure PMI additivity across a known hierarchy and across analogy families

## What it would do

Work out the PMI spectrum for a generative model with implication among
attributes; then measure additivity in real co-occurrence counts along
WordNet hypernymy and across analogy families.

Where the record names it:

- [QUESTION-025](../questions.d/QUESTION-025.md): "A derivation. A generative model of co-occurrence with a
  stated implication structure among binary attributes"
- [QUESTION-025](../questions.d/QUESTION-025.md): "In real co-occurrence data, a test of whether the PMI is
  additive across the attributes of a known hierarchy (WordNet hypernymy,
  say)"
- [QUESTION-178](../questions.d/QUESTION-178.md): "a measurement of how far the PMI departs from additivity
  in the attributes across all context words"

## What would count

A spectrum that shows the hierarchy, and measured additivity along it,
answers [QUESTION-025](../questions.d/QUESTION-025.md); a measured departure from additivity sizes
[QUESTION-178](../questions.d/QUESTION-178.md).

## Note of 2026-11-22: carried out by a delegated worker

Both halves were done on the branch claude/lead-147-pmi-spectrum. The
scripts, tests and per-item results are in scratch/studies/lead-147/.

- **Derivation.** [CLAIM-902](../claims.d/CLAIM-902.md) (demonstrated). Under multiplicative
  co-occurrence with any implication order and positive strengths, every
  attribute is an exact readout of the full-rank PMI embedding. On a
  balanced tree, the spectrum is branch contrasts with eigenvalues
  ordered by depth, so truncation keeps exactly the shallow attributes.
  Along a tree, additivity reduces to group constancy.
- **Measurement.** [CASE-344](../cases.d/CASE-344.md), on text8 with WordNet 3.0 and the
  word2vec analogy set. In every analogy family the PMI is far from
  additive (interaction share 0.21–0.30 against 0.33 for random
  quadruples). The families and quadruples nearer additivity complete
  more often (Spearman −0.83 across families). WordNet attributes carry a
  small, real additive part of the PMI. Probe errors fall inside the
  parent attribute about twice as often as chance, with no fall in probe
  accuracy by WordNet depth.

What remains:

- the intervention arm of [QUESTION-178](../questions.d/QUESTION-178.md);
- a control for word frequency;
- a test of the truncation clause on a hierarchy with even levels, since
  WordNet depth is uneven;
- a larger corpus.

The status and stage are left to the owner.

