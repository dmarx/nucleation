---
number: 1357
status: Active
formerly:
- THEORY-tmp4s0in
title: 'Lake, Salakhutdinov and Tenenbaum report that a model representing handwritten characters as probabilistic programs, composing strokes from primitives fit to 30 background alphabets into types whose executions give tokens, erred 3.3% against people''s 4.5% on 20-way one-shot classification within 10 held-out Omniglot alphabets, and that judges identified its exemplars and new characters at 49–59%, near chance; removing compositionality raised its error to 14.0% and made its productions easier to detect, inflating its learned token-level variability raised error to 11.0% and made exemplars easier to detect, and replacing its learned type-level priors with uniform ones left classification unchanged (3.5%) and exemplars not reliably easier to detect, but made its new characters easier to detect (64–69%)'
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Narrowed and promoted by the thirtieth status review, at the status
    review's ruling (the owner delegated these rulings; ADR-065; ADR-047's
    evidence ruling): one study's measurements, read in full in the main text
    and in the Supplementary Materials' lesions, methods and results
    (NOTE-1542, now Read). The lesion clause was mis-stated (ADR-047, kind 3):
    the learning-to-learn lesion that raised classification error is
    token-level, and removing the learned type-level priors left
    classification unchanged (3.5%, SM §6.1) and exemplar generation not
    reliably worse, degrading only the generation of new characters. The
    independent replication the promote_when asked for moves to
    QUESTION-tmpn1jcn. The old title: Lake, Salakhutdinov and Tenenbaum show
    that a model representing handwritten characters as probabilistic
    programs, composing strokes from primitives learned on other alphabets
    into types whose executions produce tokens, classifies new characters from
    one example as accurately as people and generates exemplars and new
    characters that judges mostly cannot tell from people's, and that removing
    either compositionality or the learned priors degrades both. The
    promote_when deleted here read: An independent replication on the Omniglot
    one-shot task, or a comparable held-out set of characters, confirms that
    the program-induction model reaches human one-shot classification
    accuracy, that its generated exemplars and characters are near chance in
    human-against-machine identification, and that the lesions without
    compositionality or without learned priors do worse on both.
tags:
- cognition
- compositionality
- probabilistic-modeling
date: '2026-11-04'
source:
- LIT-2009
summary: >-
  Lake, Salakhutdinov & Tenenbaum (2015), [LIT-2009](../literature.d/LIT-2009.md), main text and
  Supplementary Materials read in [NOTE-1542](../notes.d/NOTE-1542.md). BPL erred 3.3% against people's 4.5% on 20-way one-shot
  classification within 10 held-out Omniglot alphabets; judges identified
  its productions at 49–59% in four visual Turing tests; lesions without
  token-level learning to learn or without compositionality erred 11.0%
  and 14.0% and were easier to detect, while removing the type-level priors
  left classification at 3.5%. Active as the reported measurements, read
  with the Supplementary Materials' lesions and controls. Independent
  replication is QUESTION-tmpn1jcn's. The wording is the reader's; adopting it is the
  owner's call.
---

# THEORY-1357: Lake, Salakhutdinov and Tenenbaum report that a model representing handwritten characters as probabilistic programs, composing strokes from primitives fit to 30 background alphabets into types whose executions give tokens, erred 3.3% against people's 4.5% on 20-way one-shot classification within 10 held-out Omniglot alphabets, and that judges identified its exemplars and new characters at 49–59%, near chance; removing compositionality raised its error to 14.0% and made its productions easier to detect, inflating its learned token-level variability raised error to 11.0% and made exemplars easier to detect, and replacing its learned type-level priors with uniform ones left classification unchanged (3.5%) and exemplars not reliably easier to detect, but made its new characters easier to detect (64–69%)

## Source

Lake, Salakhutdinov & Tenenbaum (2015), [LIT-2009](../literature.d/LIT-2009.md); main text and Supplementary Materials read in [NOTE-1542](../notes.d/NOTE-1542.md).

## What was actually shown

- **The model** (pp. 1333–1334): types of parts, sub-parts from a library
  learned on 30 background alphabets, and relations; tokens with motor
  noise and affine warps; images rendered stochastically. Inference by
  bottom-up proposals, continuous optimisation and local search.
- **Classification** (p. 1335): 20-way, within-alphabet, 10 held-out
  alphabets. "People were skilled one-shot learners, achieving an average
  error rate of 4.5% (N = 40). BPL showed a similar error rate of 3.3%".
  Deep baselines erred 8.0% (Siamese) to 34.8%.
- **Lesions** (p. 1335; SM §§4, 6): "without learning to learn
  (token-level only) or compositionality (11.0% errors and 14.0%,
  respectively)". The token-level lesion sets variability to "three times
  their normal value" (SM §4.3). The type-level lesion "did not change the
  final level of classification performance, achieving a 3.5% error rate"
  (SM §6.1) and was "not reliably easier to detect than BPL" for exemplars
  (54%, SM §6.2), but was detected at 69% for new characters in an
  alphabet and 64% unconstrained (p. 1336). Compositionality was detected
  at 65% for exemplars and 68% unconstrained; the token-level lesion at 80%
  for exemplars.
- **Controls** (SM §6.4): a novelty control (new tokens of the shown
  characters) was detected at 68%, a style control (wrong alphabet) at
  49%.
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
