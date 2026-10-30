---
number: 269
status: Active
formerly:
- THEORY-tmpk5car
title: 'In OLMo-1B, OLMo-7B and GPT-J, how well an affine map from subject to object representation reproduces a factual relation (its LRE causality) tracks how often the relation''s subjects and objects co-occur in pretraining, with mean causality above 0.9 beyond about 4.4k, 2.0k and 1.1k co-occurrences respectively, and, across OLMo-7B''s eight checkpoints, at whatever step that count is reached'
version: 2
history:
- version: 2
  date: '2026-10-30'
  note: >-
    Narrowed first: the finding at any training step rests on OLMo-7B's
    eight checkpoints only (GPT-J has none), and LRE causality is a graded
    measure, not a yes or no. Old title: "In OLMo-1B, OLMo-7B and GPT-J,
    whether a factual relation is computed by an affine map from subject
    to object representation tracks how often its subjects and objects
    co-occur in pretraining, with mean causality above 0.9 beyond about
    4.4k, 2.0k and 1.1k co-occurrences respectively, whenever in training
    that count is reached". Promoted to Active under ADR-065, at the
    status review's ruling (the owner delegated these rulings). The title
    reports what one study, read in full in NOTE-786, measured, with the
    study's hedges kept, and nothing in the record contradicts it. The old
    promote_when read: "An intervention, not a further correlation. Two
    kinds would do. One is a pretraining run in which one relation's
    subject–object co-occurrences are raised above, or held below, the
    threshold while the rest of the corpus is unchanged, with that
    relation's LRE causality crossing 0.9 or failing to, as the account
    predicts. The other is the threshold recovered, with its spread,
    across more model sizes and families. The account is refuted if
    relations held below the threshold become linear as reliably as those
    above it, or if co-occurrence stops predicting causality once few-shot
    accuracy and subject and object frequency are controlled for. More
    correlations on the same relations cannot settle it, since they cannot
    separate exposure from whatever makes facts both frequent and easy."
    Its demand for an intervention on co-occurrence counts, or for the
    threshold across more model sizes and families, asks for a causal and
    general claim the title does not make; the authors disclaim causal
    claims (Appendix A), so it moves to QUESTION-344.
tags:
- representation-learning
date: '2026-10-14'
source:
- LIT-972
summary: >-
  Merullo, Smith, Wiegreffe and Elazar (2025), [LIT-972](../literature.d/LIT-972.md), read in full in
  [NOTE-786](../notes.d/NOTE-786.md). 24 factual relations, three models, eight OLMo-7B
  checkpoints; r = 0.82 between LRE causality and mean subject–object
  co-occurrence, above either term's frequency alone. Correlational by
  the authors' own statement. The linear objects are per-relation
  affine maps between hidden states, not attribute directions.
---

# THEORY-269: In OLMo-1B, OLMo-7B and GPT-J, how well an affine map from subject to object representation reproduces a factual relation (its LRE causality) tracks how often the relation's subjects and objects co-occur in pretraining, with mean causality above 0.9 beyond about 4.4k, 2.0k and 1.1k co-occurrences respectively, and, across OLMo-7B's eight checkpoints, at whatever step that count is reached

## Source

Merullo, Smith, Wiegreffe and Elazar (2025), "On Linear Representations
and Pretraining Data Frequency in Language Models", ICLR 2025, [LIT-972](../literature.d/LIT-972.md).
Read in full in [NOTE-786](../notes.d/NOTE-786.md): §3 (Eq. 1, counting), §4.2–4.3 (Fig. 2
and its table), §6, Appendices A, D and G.

## What was actually shown

- **The measure.**
  - Following Hernandez et al., each relation's computation from the
    subject's middle-layer state s to the final state is approximated by
    F(s, c) ≈ W s + b, with W the mean Jacobian over 8 examples.
  - Its quality is *causality*: the share of edits through the map that
    make the model output a chosen other object.
  - Subject–object co-occurrences within training sequences were counted
    exactly in OLMo's reconstructed Dolma batches, up to each of eight
    checkpoints from 41B to 2T tokens. For GPT-J they were counted per
    document in the Pile.
- **The correlation.**
  - Across 24 relations, causality correlates with the log of mean
    subject–object co-occurrence at r = 0.82.
  - Against subject frequency alone r = 0.66, and against object
    frequency alone r = 0.59.
  - It is also higher than causality's correlation with 5-shot accuracy
    (0.74, OLMo-7B).
- **The thresholds.**
  - Mean causality exceeds 0.9 above a mean count of 1,097 (GPT-J), 1,998
    (OLMo-7B) and 4,447 (OLMo-1B).
  - Relations past the threshold are linear at early checkpoints as well
    as late ones: "regardless of pretraining step".
- **Rare relations.** A rare relation can be recalled without a single
  consistent map. Star–constellation has 84% 5-shot accuracy but 44%
  causality, at about 21 co-occurrences.
- **What could have come out otherwise.** Linearity could have tracked
  training stage, or accuracy, rather than exposure. The checkpoint
  design separates exposure from stage, and the accuracy comparison
  separates it from recall.

## What this does not say

- **Not that frequency causes linearity.** "We can not draw causal
  claims about how exposure affects individual representations"
  (Appendix A). Frequent facts may differ in other ways.
- **Not about attribute directions.** An LRE is one affine map per
  relation between two hidden states. It is not a direction for a binary
  attribute in an embedding. The result does not transfer to probes for
  attributes without a further test.
- **Not a per-fact threshold.** The counts are means over a relation's
  pairs, and "consistently (but not exclusively)": some relations below
  them are linear.
- **Not a scaling law.** Three models give three thresholds. The
  authors say they "cannot draw conclusions from only three models".
- **Not about the structure of co-occurrence.** Only how often subjects
  and objects co-occur is measured. Whether the statistics are additive
  across attributes, correlated or hierarchical is not.
- **Not an instruction.** The authors' suggestion to shape training data
  to meet frequency thresholds, and their tool for inferring training
  data, are ML practice. They are left to the Anthology of the SOTA.

## Connections

- **[QUESTION-025](../questions.d/QUESTION-025.md).** No `answers` link. The question's premise is
  that co-occurrence structure gives linear attribute directions. This
  result is about relation maps and raw exposure. It bears on the
  question only by showing that linearity in trained models is graded
  and depends on counts. A measurement of the kind the question asks for
  would need to control for frequency, or a missing direction could
  just mean a rare attribute.
- **[THEORY-185](THEORY-185.md).** That account explains linear directions by additive
  PMI and treats departures as noise that buries the attribute modes. A
  count threshold fits that picture loosely, since low counts mean noisy
  PMI. This paper does not test it.
