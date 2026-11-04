---
status: Proposed
promote_when: >-
  An independent replication on the Omniglot one-shot task, or a comparable
  held-out set of characters, confirms that the program-induction model
  reaches human one-shot classification accuracy, that its generated
  exemplars and characters are near chance in human-against-machine
  identification, and that the lesions without compositionality or without
  learned priors do worse on both.
title: 'Lake, Salakhutdinov and Tenenbaum show that a model representing handwritten characters as probabilistic programs, composing strokes from primitives learned on other alphabets into types whose executions produce tokens, classifies new characters from one example as accurately as people and generates exemplars and new characters that judges mostly cannot tell from people''s, and that removing either compositionality or the learned priors degrades both'
version: 1
tags:
- cognition
- compositionality
- probabilistic-modeling
date: '2026-11-04'
source:
- LIT-tmp8aj28
summary: >-
  Lake, Salakhutdinov & Tenenbaum (2015), LIT-tmp8aj28, main text read in
  NOTE-tmp6p61k. BPL erred 3.3% against people's 4.5% on 20-way one-shot
  classification within 10 held-out Omniglot alphabets; judges identified
  its productions at 49–59% in four visual Turing tests; lesions without
  learning to learn or without compositionality erred 11.0% and 14.0% and
  were easier to detect. Proposed: one study by the model's authors, with
  the model's specification and controls in Supplementary Materials this
  reading did not cover. The wording is the reader's; adopting it is the
  owner's call.
---
<!-- inactive-ok-file: LIT-tmp8aj28 NOTE-tmp6p61k — new; the reading of Lake, Salakhutdinov & Tenenbaum (2015) this account is filed from -->

# THEORY-tmp4s0in: Lake, Salakhutdinov and Tenenbaum show that a model representing handwritten characters as probabilistic programs, composing strokes from primitives learned on other alphabets into types whose executions produce tokens, classifies new characters from one example as accurately as people and generates exemplars and new characters that judges mostly cannot tell from people's, and that removing either compositionality or the learned priors degrades both

## Source

Lake, Salakhutdinov & Tenenbaum (2015), LIT-tmp8aj28; main text read in NOTE-tmp6p61k.

## What was actually shown

- **The model** (pp. 1333–1334): types of parts, sub-parts from a library
  learned on 30 background alphabets, and relations; tokens with motor
  noise and affine warps; images rendered stochastically. Inference by
  bottom-up proposals, continuous optimisation and local search.
- **Classification** (p. 1335): 20-way, within-alphabet, 10 held-out
  alphabets. "People were skilled one-shot learners, achieving an average
  error rate of 4.5% (N = 40). BPL showed a similar error rate of 3.3%".
  Deep baselines erred 8.0% (Siamese) to 34.8%.
- **Lesions** (p. 1335): "without learning to learn (token-level only) or
  compositionality (11.0% errors and 14.0%, respectively)"; the lesioned
  models were also easier for judges to detect in generation.
- **Generation** (pp. 1335–1336): judges' identification of BPL against
  people was 52% for exemplars, 59% for drawing movies, 49% for new
  characters in an alphabet and 51% for unconstrained new characters.
- What could have come out otherwise: BPL could have fallen short of
  people, the lesions could have done as well, and judges could have told
  the productions apart.

## What this does not say

- That people represent characters as these programs. The evidence is
  behavioural; the authors suggest it and propose a neural test.
- That the structure was learned: the drawing process is prewired, and
  BPL learns from stroke data the deep baselines did not see.
- That it extends beyond handwritten characters.
- That generation is human-like to every judge: some judges did better
  than chance, and in one test 10 of 35 were significantly below it.
