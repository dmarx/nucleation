---
status: Read
paper: 'LIT-tmpzdaep'
title: 'Kumar, Tan and Sharma — Probing classifiers are unreliable for concept removal'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Read on 2026-11-15 by a delegated reader from arXiv:2207.04153v3,
    https://arxiv.org/pdf/2207.04153v3 (47 pp.), text by pdftotext: the
    abstract, §1, §2, §§3.1–3.4 (the statements of Lemma 3.1 and Theorems
    3.2 and 3.3), §4.2 (null-space results) and the Limitations paragraph.
    Skimmed: §4.3 (adversarial removal) and §§5–6. Not read: the appendix
    proofs (§§B–D) and the extra experiments. Read for the main text, so
    Read with the proofs unchecked. The filer rechecked every quotation
    below against a fresh text extraction of the same PDF; all were found.
date: '2026-11-15'
summary: >-
  For frozen, disentangled representations under max-margin training, a
  concept probe uses correlated main-task features, so probe-guided
  removal (INLP, adversarial) can leave concept features while corrupting
  task features; on a classifier that never used the concept, INLP drives
  main-task accuracy to chance.
---
<!-- inactive-ok-file: THEORY-292 — Proposed; a held reading cited as a neighbour, nothing rests on it -->

# NOTE-tmpqbu99: Kumar, Tan and Sharma — Probing classifiers are unreliable for concept removal

## Contribution

Theory and experiments showing that the proxy, the probing classifier
that stands in for "the concept's features", is where concept removal
fails, and a spuriousness score for auditing the result.

## Key insight

A probe is trained to separate the concept, not to find the concept's
causal features. Where task and concept labels are correlated, the
max-margin probe spreads its weight onto task features, and every method
that removes what the probe uses removes those task features too.

## Assumptions

- A frozen, disentangled representation z = [zm, zp], with zp the
  concept-causal features and zp fully predictive of the concept.
- Binary labels and a max-margin loss, for the theory (§3, Limitations).
- Main-task and concept labels correlated on the margin points
  (Assumption 3.4).

## Key results

- **Abstract**: such methods "are unable to remove the concepts entirely,
  and in some cases may fail severely by destroying all task-relevant
  features."
- **Lemma 3.1**: under the assumptions the max-margin concept probe "will
  use spurious features", cp(z) = wp·zp + wm·zm with wm ≠ 0.
- **Theorem 3.2(1)**: "The first step of linear-INLP will corrupt the
  main-task features and this corruption is non-invertible with subsequent
  projection steps of INLP."
- **Theorem 3.3**: an adversarially trained encoder that still depends on
  zp can be "indistinguishable from desired encoder" in adversarial-task
  accuracy while "better for main-task", so adversarial removal cannot
  tell it from a clean one.
- **§4.2**: applied to a classifier that does not use the concept, INLP
  still collapses it: "for all values of κ, the main-task classifier's
  accuracy eventually goes to 50% random guess accuracy".
- **§1**: amnesic probing is "also flawed because they depend on access to
  a good quality concept classifier."

## Concepts

- **Concept-causal feature** (Def. 2.1): a feature the concept label
  depends on causally.
- **Probing proxy**: the classifier used in place of the concept's
  features.
- **Spuriousness score (ΔProb)**: the paper's audit of how far a
  removal's output depends on the spurious concept.

## Bearing on the record

- **[THEORY-281](../theory.d/THEORY-281.md)** (the perfect-erasure cap): complementary. The cap says
  what perfect erasure must cost at least; this shows probe-guided methods
  losing far more than that, all task information on a clean classifier,
  while not reaching independence.
- **[TERM-064](../terms.d/TERM-064.md)**: the probe is an observer of a restricted class, and its
  errors, weight on correlates, shape what gets erased, not only which
  distinctions it can see.
- **[THEORY-292](../theory.d/THEORY-292.md)** (co-occurring attributes give aligned concept
  directions): the entanglement this paper's mechanism needs.
- **[QUESTION-010](../questions.d/QUESTION-010.md)**: a one-step case of the trade-off, removal aimed at one
  task (the concept) destroying another (the main task) because they
  share directions; not a chain.

## Connections

Directly criticizes INLP (Ravfogel et al. 2020, [LIT-tmp3i6ea](../literature.d/LIT-tmp3i6ea.md)) and amnesic
probing (Elazar et al. 2021, [LIT-tmp52idf](../literature.d/LIT-tmp52idf.md)). Elazar et al.'s §9 concedes a
milder form of the same point.

## Limitations

The theory assumes frozen, disentangled representations and max-margin
training; the experiments are text classification. The proofs were not
checked.
