---
number: 786
status: Read
formerly:
- NOTE-tmpiolrn
paper: LIT-972
title: 'Merullo et al. — Linear Representations and Pretraining Data Frequency'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv PDF, v1 of 16 April 2025 (25 pages, the
    ICLR 2025 camera-ready), fetched from arxiv.org/pdf/2504.12459 and
    extracted with pdftotext: §§1–7 and Appendices A–G, with the figure
    captions and Tables 1–2. The per-relation plots of Appendices C, F
    and G were read only through their captions. The arXiv PDF's Figure
    2 has draft text from an earlier layout embedded in it ("TODO: What
    to do about awkward spacing", "TODO: make more concise"); the
    numbers below are from the body text and the table in that figure.
date: '2026-10-14'
summary: >-
  For 24 factual relations in OLMo-1B, OLMo-7B and GPT-J, how well an
  affine map from subject to object representation reproduces the model
  (LRE causality) correlates with the mean subject–object co-occurrence
  count in pretraining (r = 0.82). It correlates less with subject or
  object counts alone. Mean causality passes 0.9 beyond about 4.4k, 2.0k
  and 1.1k co-occurrences respectively, at any training step.
  Correlational; LREs are relation maps, not attribute directions.
---
<!-- inactive-ok-file: THEORY-185 THEORY-234 THEORY-269 — Proposed; the accounts this reading bears on, and the one filed from it -->

# NOTE-786: Merullo et al. — Linear Representations and Pretraining Data Frequency

## Contribution

The paper ties a measure of linear structure in language models to
counts in their actual training batches. For subject–relation–object
facts, the quality of a linear relational embedding (LRE) tracks how
often subjects and objects co-occur in pretraining. Above a
model-dependent mean count, the relation is almost always linear, at
whatever training step the count is reached. Then the direction is
reversed: LRE quality, used as a feature, predicts a term's training
frequency to within an order of magnitude more often than log
probabilities do, including for a second model.

## Key insight

Whether a relation is computed in a way an affine map approximates
looks, in these models, like a matter of exposure. Enough co-occurrences
of a relation's subjects and objects, and the LRE works. This holds
regardless of the model's overall stage of training. Few-shot accuracy
can run ahead of linearity for rare relations.

## Assumptions

- **LREs (§2.1, Eq. 1), after Hernandez et al. (2024).**
  - F(s, c) ≈ W s + b, where s is the subject's hidden state at a middle
    layer and F(s, c) the last-layer, last-token state.
  - W = E[∂F/∂s] and b = E[F(s, c) − (∂F/∂s) s], averaged over n = 8
    examples, each with a 5-shot prompt.
  - W is scaled by a β per relation. The layer is chosen by causality.
  - Examples the model gets wrong are allowed in the fit. Appendix B
    reports this makes no considerable difference.
- **Metrics.**
  - Faithfulness: the LRE's top prediction matches the model's.
  - Causality: editing the subject representation through the LRE's
    inverse, of a chosen rank, makes the model output another subject's
    object.
  - Causality above 0.9 is taken as "nearly perfectly linear".
- **Counting.**
  - A co-occurrence is the subject and object in one training sequence.
    It is counted exactly in OLMo's reconstructed batches of Dolma (~2T
    tokens) with the Batch Search tool.
  - For GPT-J it is counted per document in the Pile with WIMBD, which
    overcounts. The fitted slope of batch counts on WIMBD counts is 0.94
    (Appendix D).
  - Co-occurrence is a proxy for mentions of the fact (Elsahar et al.).
- **Data.**
  - The 25 factual relations of the RELATIONS dataset, less
    "landmark-on-continent" (74% Antarctica). That leaves 24 relations
    over 10,488 unique subjects and objects.
  - OLMo-7B is read at checkpoints of 41B, 104B, 209B, 419B, 628B, 838B,
    1T and 2T tokens.

## Key results

- **Frequency and linearity (§4.2, Fig. 2).**
  - Pearson r = 0.82 between causality and (log) mean subject–object
    co-occurrence.
  - Against subject frequency alone, r = 0.66. Against object frequency
    alone, r = 0.59. The text says "for both OLMo-7B and OLMo-1B,
    respectively", which leaves unclear which model gives which value.
- **Thresholds (table in Fig. 2).** The mean co-occurrence count above
  which mean causality exceeds 0.9:

  | model | count |
  |---|---|
  | GPT-J (6B) | 1,097 |
  | OLMo-7B | 1,998 |
  | OLMo-1B | 4,447 |

  - "Regardless of pretraining step, models that surpass this threshold
    have very high causality scores."
  - The abstract's "consistently (but not exclusively)" means some
    relations below the threshold are linear too.
  - The abstract reads "In OLMo-7B and GPT-J (6B) … at least 1k and 2k
    times, respectively". The table gives the reverse: about 2k for
    OLMo-7B and 1k for GPT-J. The table is followed here.
  - Scale may matter: "we cannot draw conclusions from only three
    models."
- **Accuracy (§4.3, Appendix F).**
  - In OLMo-7B, causality correlates with co-occurrence at 0.82 and with
    5-shot accuracy at 0.74.
  - Star–constellation: 84% 5-shot accuracy, 44% causality, about 21
    co-occurrences on average.
  - Food–from–country early in training: causality 65%, accuracy 42%.
  - In the final model, causality and 5-shot accuracy differ by 11% on
    average.
  - Only star–constellation and product–by–company have few-shot
    accuracy far above causality, and both are rare (§6).
- **Predicting frequency (§5).**
  - A random forest (100 trees) was trained on held-out relations over 4
    seeds. Scores are the share of predictions within 10× of the truth.
  - Object frequency: LRE features succeed about 70% of the time, and
    log-probability features barely beat baseline.
  - Mean absolute error in natural-log space, LRE features against
    LM-only features: 2.1 against 4.2 for objects, 1.9 against 2.3 for
    subject–object counts.
  - Subject–object predictions are "within one standard deviation of the
    mean baseline".
  - Hard causality is the most important feature (about 15% accuracy).
- **Across models (Table 1).**

  | target | LRE features | log-prob features | mean baseline |
  |---|---|---|---|
  | object, evaluated on GPT-J | 0.65 ± 0.12 | 0.42 ± 0.10 | 0.31 ± 0.15 |
  | object, evaluated on OLMo | 0.49 ± 0.12 | 0.41 ± 0.09 | 0.41 ± 0.17 |
  | subject–object, evaluated on GPT-J | 0.76 ± 0.12 | 0.66 ± 0.09 | 0.57 ± 0.15 |
  | subject–object, evaluated on OLMo | 0.68 ± 0.08 | 0.60 ± 0.07 | 0.67 ± 0.16 |

  Errors range from 1× (Brazil to Portuguese) to 346× (Arcturus to
  Boötes) (Table 2).
- **Commonsense relations (Appendix G).** Eight such relations in
  OLMo-7B give r = 0.42. The authors caution that co-occurrence may not
  track mentions of such relations.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | LRE causality correlates strongly with mean subject–object co-occurrence in pretraining, more than with either term's frequency | strong (as a correlation) | Fig. 2; 24 relations, three models, eight checkpoints |
| C2 | Above a model-dependent mean count, relations are almost always linear, regardless of training step | moderate | Fig. 2 table; one threshold per model, three models |
| C3 | Few-shot accuracy can exceed linearity for rare relations | moderate | star–constellation, product–by–company |
| C4 | LRE features carry frequency information that log probabilities lack, and it transfers across models for object counts | moderate | Table 1, Fig. 3; within-10× accuracy, wide error bars |
| C5 | Frequency causes linear representations to form | not claimed | Appendix A: "we can not draw causal claims" |

## Method

1. Fit an LRE per relation and model by Eq. (1), with a sweep of layer,
   β and rank (Appendix C).
2. Count subject–object co-occurrences per training sequence up to each
   checkpoint.
3. Correlate causality with the relation's mean count.
4. Fit a regression from LRE metrics to term counts.

## Concepts

- **Linear representation.** As used here: an affine map from subject
  state to object state that reproduces the model's prediction, one per
  relation. It is not a direction for an attribute.
- **Causality.** The share of edits through the LRE that change the
  model's answer to the intended object.
- **Co-occurrence.** Subject and object within one training sequence (or
  document, for GPT-J).

## Connections

The work builds on Hernandez et al.'s LREs and Chanin et al.'s linear
relational concepts. For static embeddings it cites Ethayarajh et al.
(2019), who found that analogies form under frequency conditions. It sets
itself beside Jiang et al. (2024), who derive linearity from the
training objective under a matched log-odds frequency condition. Counts
use Elazar et al.'s WIMBD and a new batch search.

## Bearing on the record

- **[QUESTION-025](../questions.d/QUESTION-025.md).**
  - [LIT-972](../literature.d/LIT-972.md) is registered there as "an empirical test of the question's
    premise that co-occurrence statistics give linear attribute
    directions". That overstates what the paper shows, in three ways.
  - First, LREs are affine maps between two hidden states in a
    transformer, one per relation. They are not directions for binary
    attributes in an embedding.
  - Second, the variable is how often a subject and object co-occur. The
    structure of co-occurrence across attributes, which is what the
    premise is about, is not measured.
  - Third, the result is a correlation, as the authors stress.
  - Its bearing on the question is narrower: in trained language models,
    linearity is graded and depends on exposure. A probe that finds no
    direction for a rare attribute may be finding low counts, not
    structure.
  - It says nothing on correlated, hierarchical or implicational
    attributes, or on lattices.
- **[THEORY-185](../theory.d/THEORY-185.md).** Its promote_when asks for a measurement of how far
  the PMI departs from additivity, family by family. This paper does not
  measure that. The thresholds fit loosely with [THEORY-185](../theory.d/THEORY-185.md)'s account of
  noise: low counts mean a noisy PMI and lost directions. That is the
  reader's remark, and not tested here.
- **[THEORY-234](../theory.d/THEORY-234.md).** The regression transfers between OLMo and GPT-J for
  object counts. That suggests LRE quality is comparable across models
  trained on different corpora. This is weak, and is not evidence about
  identifiability.
- **Filed from this reading:** [THEORY-269](../theory.d/THEORY-269.md).
- **The anthology.** The authors' closing suggestion, to manipulate
  training data to meet frequency thresholds, and the data-inference
  tool are ML practice. They belong in the Anthology of the SOTA, and the
  LIT keeps its `anthology-candidate` flag.

## Limitations

- **Correlational.** "We can not draw causal claims about how exposure
  affects individual representations, due to the cost of counterfactual
  pretraining" (Appendix A).
- **Few data points.** 24 relations, three models, one threshold
  definition (mean causality > 0.9). The per-relation scatter is in
  figures only.
- **The threshold is a property of a relation's mean.** It is not a
  per-fact threshold.
- **Proxies.** Co-occurrence stands in for mentions of the fact.
  Presentation of facts in text is not studied.
- **Fitting choices.** The layer, β and rank are tuned per relation, so
  causality partly measures how well a sweep can fit.
- **Frequency prediction is coarse.** It is within 10× about 50–76% of
  the time, and barely above baseline for subject–object counts.

## Open questions

- A counterfactual pretraining run, raising or lowering one relation's
  co-occurrence count, would settle whether frequency causes the
  linearity.
- Does the threshold scale with model size? Three models cannot say.
- For attributes rather than relations: does a linear probe's quality
  track the attribute's co-occurrence count in the same way? And does
  correlation among attributes change the count needed?
