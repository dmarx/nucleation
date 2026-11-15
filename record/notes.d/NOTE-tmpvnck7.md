---
status: Read
paper: 'LIT-tmp3i6ea'
title: 'Ravfogel et al. — Null It Out (INLP)'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Read on 2026-11-15 by a delegated reader from arXiv:2004.07667v2,
    https://arxiv.org/pdf/2004.07667v2 (20 pp.), text by pdftotext: the
    abstract, §1, §§3–4 (objective and method), §6.1 (gender in GloVe),
    §6.3 results, §7 Limitations and §8 Conclusion. Skimmed: §5, §6.2 and
    the appendices; the Appendix A guarantees were seen, not checked. The
    filer rechecked every quotation below against a fresh text extraction
    of the same PDF; all were found (line-break hyphenation aside).
date: '2026-11-15'
summary: >-
  INLP makes a protected attribute linearly undecodable by iterated
  nullspace projection (gender SVM accuracy 100% → 49.3% on GloVe), while
  a one-hidden-layer MLP still recovers it at 85.0%; the paper says itself
  that the guarantee covers linear classifiers only.
---

# NOTE-tmpvnck7: Ravfogel et al. — Null It Out (INLP)

## Contribution

A data-driven, iterative, multi-direction alternative to hand-chosen bias
directions for removing a protected attribute from representations, with
a stated and narrow guarantee: the result is "linearly guarding" for the
attribute, in that no linear classifier predicts it above chance.

## Key insight

Erasure is defined against a class of readers. INLP removes every
direction a linear classifier can use, one classifier at a time, and so
makes the attribute illegible to linear readers only; what a nonlinear
reader can still recover is left as it is.

## Assumptions

- Training data for (X, Z) large and i.i.d. with the test data (§7).
- The downstream consumer is a linear decoder.
- Z is a labelled categorical attribute.

## Key results

- **Method** (abstract): "repeated training of linear classifiers that
  predict a certain property we aim to remove, followed by projection of
  the representations on their null-space."
- **Gender in GloVe** (§6.1.1): a linear SVM separates gender at 100%
  accuracy before INLP; after 35 iterations "The accuracy drops to 49.3%".
  Then: "To measure to what extent gender is still encoded in a nonlinear
  way, we train a 1-layer ReLU-activation MLP. The MLP recovers gender
  with accuracy of 85.0%. This is expected, as the INLP method is only
  meant to achieve linear guarding."
- **Fair classification** (§6.3.1): the correlation between a profession's
  TPR gender gap and women's share of it falls, for BERT "from 0.883 prior
  to INLP to 0.470".
- **Limitation, stated** (§7): "the method is designed to achieve a very
  specific sense of protection: removal of linear information regarding a
  protected attribute", and "the attributes are not protected under
  non-linear classifiers."

## Concepts

- **Linear guardedness**: no linear classifier predicts Z from the
  projected X above chance.
- **Nullspace projection**: projecting X onto the nullspace of a linear
  classifier's weights, iterated and composed.

## Bearing on the record

- **TERM-064** (legibility relative to an observer's rule class): INLP is
  erasure indexed to one rule class, the linear one. Gender becomes
  illegible to linear observers and stays legible to a one-hidden-layer
  MLP. This is the term's observer-relativity in an engineering setting,
  measured by the authors themselves.
- **THEORY-281** (the perfect-erasure cap): INLP aims at a weaker target
  than independence of the representation and the concept, so the cap
  does not apply to it; the 85.0% MLP result is a measured case of linear
  erasure far from perfect erasure.
- **THEORY-1827** (LEACE): the closed-form, least-edit version of the same
  linear target. INLP reaches linear guardedness by iteration; LEACE
  characterizes it exactly.
- **THEORY-846** (V-information can be created by computation): explains
  why a nonlinear family can extract what the linear family cannot.
- **QUESTION-010**: no direct bearing. INLP is one step, not a chain.

## Connections

Kumar, Tan & Sharma (2022), LIT-tmpzdaep, NOTE-tmpqbu99, prove that the
first step of INLP can corrupt main-task features irreversibly when the
probe leans on correlated task features.

## Limitations

The guarantee is linear only, by the authors' statement. The fairness
experiments are limited (§7). The Appendix A proofs were not checked.
