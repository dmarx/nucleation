---
number: 178
status: Open
formerly:
- QUESTION-tmpwzwpl
title: 'Is word co-occurrence close to independent, multiplicative binary attributes in the analogy families where spectral embeddings complete parallelograms, and does adding an interaction between two attributes break their parallelogram?'
version: 1
tags:
- representation-learning
- compositionality
date: '2026-10-19'
line: 'pragmatic-transport'
refines:
- QUESTION-025
summary: >-
  Filed when the promotion audit (batch 037, [ADR-047](../decisions.d/ADR-047.md) v2) narrowed and
  promoted [THEORY-185](../theory.d/THEORY-185.md), Korchinski et al.'s conditional theorem: under
  independent, multiplicative binary attributes the PMI is affine in the
  attributes and its spectral embedding gives exact parallelograms. The
  theorem is conditional on that premise. Its former promote_when asked
  for the premise to be measured on real text, and this question holds
  that request.
---
<!-- inactive-ok-file: CASE-tmpby7xp — new, filed today by LEAD-147 -->

# QUESTION-178: Is word co-occurrence close to independent, multiplicative binary attributes in the analogy families where spectral embeddings complete parallelograms, and does adding an interaction between two attributes break their parallelogram?

## Why it is a question

[THEORY-185](../theory.d/THEORY-185.md) now states, as a theorem, what follows when each binary
attribute of a word affects its co-occurrence independently and
multiplicatively. The PMI then has rank at most d + 1 with eigenvectors
affine in the attributes, so its spectral embedding gives parallelograms
exactly. The source infers that real co-occurrence is close to this form
from the shape of the PMI spectrum and of analogy accuracy against
dimension, and those are shapes the model was built to match. No
attribute, strength or dimension is recovered from data.

## What would answer it

For the word quadruples of analogy families, a measurement of how far the
PMI departs from additivity in the attributes across all context words,
finding that families close to additive are the ones a spectral embedding
completes and those far from it are not, would answer it yes. So would an
intervention on a corpus that adds an interaction between two attributes
(contexts that favour one combination beyond the sum of the two effects),
with that pair's parallelogram breaking in the PMI embedding while the
others stay. Families that the embedding completes although their PMI is
far from additive would answer it no. What cannot settle it: more
agreement in the shape of analogy accuracy against dimension, or of the
PMI spectrum.

## Note of 2026-11-22: a first measurement of the departure from additivity

LEAD-147 measured it on text8, about 17M tokens of English Wikipedia. The
case is CASE-tmpby7xp. The PMI was taken over the 5 000 most frequent
context words, in a window of ±5. For each quadruple a:b :: c:d of the
word2vec analogy set, the PMI rows were split into a relation effect, a
pair effect and an interaction, P_a − P_b − P_c + P_d. The interaction's
noise was removed using the two half-corpora. Additivity predicts an
interaction share of 0; quadruples drawn at random from a family's words
give about 0.33.

The measured median share, noise-corrected, runs from 0.21 to 0.30 by
family. No family is close to additive. On this measure the departure is
most of what an unstructured quadruple shows. The departure still tracks
completion. Across the 14 families, 3CosAdd accuracy in a rank-300 PMI
embedding falls with the interaction share (Spearman −0.83). Within 13 of
the 14 families, the third of quadruples with the least interaction
completes more often than the third with the most (mean 0.59 against
0.31). That is the pattern this question names as a yes, in graded form:
families nearer additivity are the ones completed. Two things temper it.
No family is near the additive end, and word frequency, which affects
both measures, was not controlled. The intervention limb is not attempted.
