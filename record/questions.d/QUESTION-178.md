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
