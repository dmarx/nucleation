---
status: Proposed
promote_when: >-
  A comparison on large-corpus co-occurrence data that fits Euclidean,
  hyperbolic and other candidate geometries to the same normalized log
  co-occurrences, at the windows used in practice, and finds Euclidean
  fit best by a criterion that could have preferred another, with
  hierarchical and function-word vocabularies included rather than
  excluded. Nearest-neighbour statistics within a tolerance, or a
  correlation with similarity ratings, do not settle it: they are
  necessary conditions that many non-Euclidean structures also meet.
title: 'Normalized log co-occurrences of words in large corpora behave as distances in a Euclidean semantic space: they correlate with human similarity ratings (r = 0.75 against MEN) and their nearest-neighbour centrality and reciprocity fall in the range expected of points sampled in a Euclidean space, apart from superordinate and function words'
version: 1
tags:
- representation-learning
- cognition
date: '2026-10-29'
source:
- LIT-tmp6ic5n
summary: >-
  Hashimoto, Alvarez-Melis and Jaakkola (2016), [LIT-tmp6ic5n](../literature.d/LIT-tmp6ic5n.md), §3, read
  in [NOTE-tmp6nipz](../notes.d/NOTE-tmp6nipz.md). The correlation follows a normalization chosen to
  maximize it; the two nearest-neighbour statistics are necessary
  conditions, the corpora exceed the asymptotic centrality bound and pass
  only a non-asymptotic range, and the free-association data fail the
  reciprocity criterion the paper states. Proposed.
---
<!-- inactive-ok-file: CLAIM-135 — Proposed; the distinction between identification and constitution this bears on, cited as open -->

# THEORY-tmp259r0: Normalized log co-occurrences of words in large corpora behave as distances in a Euclidean semantic space: they correlate with human similarity ratings (r = 0.75 against MEN) and their nearest-neighbour centrality and reciprocity fall in the range expected of points sampled in a Euclidean space, apart from superordinate and function words

## Source

Hashimoto, Alvarez-Melis and Jaakkola (2016), [LIT-tmp6ic5n](../literature.d/LIT-tmp6ic5n.md), §§2–3,
pp. 274–276 (Fig. 2, Table 2); read in [NOTE-tmp6nipz](../notes.d/NOTE-tmp6nipz.md).

## What was actually shown

**Correlation with judgments.** Normalized PMI against the MEN similarity
survey: "a strong linear relationship with semantic similarity judgments
from survey data (Pearson's r=0.75)" (p. 275). The normalization, unigram
frequency to the 3/4 power, "maximizes the linear correlation in Figure 2"
(n. 2). The authors add that this "does not by itself demonstrate that log
co-occurrences (with normalization) can be used to define an Euclidean
metric space" (p. 275).

**Embeddability.** Tversky and Hutchinson's statistics, on PMI nearest
neighbours (Table 2): centrality C = 2.21, 2.24, 2.66 and reciprocity
Rf = 0.63, 0.73, 0.62 for the Wikipedia, word2vec and GloVe corpora;
C = 1.51, Rf = 0.48 for free association. Under the geometric sampling
model C ≤ 2 asymptotically, "typical non-asymptotic values of C range
between 1 and 3, while non-embeddable hierarchical structures have C > 10",
and Rf "should be greater than 0.5" (pp. 275–276). The word "the" alone
raises Wikipedia's C from 2.21 to 3.46; superordinate and function words
"could not be embedded", per Tversky (p. 276).

**What could have failed.** The corpora could have shown C near 10, as
hierarchical vocabularies do, or Rf well below 0.5. They did not. The
free-association data did fall below the stated Rf criterion (0.48), which
the text does not mention.

## What this does not say

- **That the space is Euclidean rather than some other geometry.** Both
  statistics depend only on the single nearest neighbour and are
  "asymptotically dimension independent" (n. 3); they detect strongly
  hub-like or tree-like structure and are silent about curvature or
  dimension.
- **That co-occurrence distance is semantic similarity.** r = 0.75 after a
  tuned normalization leaves much of the variance unexplained, and the
  free-association metric of Table 4 behaves differently from the corpus
  metric (better on semantic analogies, near zero on syntactic ones;
  [NOTE-tmp6nipz](../notes.d/NOTE-tmp6nipz.md)).
- **That the space is the meaning of the words.** A metric that fits
  similarity ratings identifies a structure under that probe; whether it
  is the right kind of structure is a further question ([CLAIM-135](../claims.d/CLAIM-135.md)).
- **That the random-walk model of §4 is confirmed.** These statistics are
  about the data; the model is a separate tool the authors do not offer
  as a model of language (p. 277).
