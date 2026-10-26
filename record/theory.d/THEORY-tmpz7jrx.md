---
status: Proposed
promote_when: >-
  A measurement of what dictionaries of increasing width share: in a model
  with known features (a toy model with planted sparse features, or a
  network trained to implement a known computation), or across many
  widths, seeds and penalties in a real model, with a stated matching
  criterion. It is borne out if features at one width are, by that
  criterion, sums or refinements of features at another, with no width at
  which the set stops changing, or if planted features are recovered only
  at a width-dependent granularity. It is refuted if the dictionaries
  converge on one set as width grows, the same across seeds and penalties.
  More examples of features that look split, read from browsers, cannot
  settle it: that is the evidence it rests on now.
title: 'The features a sparse autoencoder recovers from a language model are a resolution set by the dictionary''s width and sparsity penalty, not a unique set of the model''s units: as the dictionary widens, features split into families of finer features, and splits also merge, so that the number of features is not well-posed'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Proposed from NOTE-tmpz50gz, as the reading of feature splitting
    that THEORY-tmpkq43g leaves out (ADR-047 v4). The splitting is
    observed; that it shows no unique feature set is the authors' own
    conclusion ("finding the 'correct number of features' may not be
    well-posed"), reached from examples, and their alternative picture of
    an idealized feature set is a conjecture.
tags:
- representation-learning
date: '2026-10-26'
source:
- LIT-tmpn9ui7
- LIT-tmp8w8uj
extends:
- THEORY-tmpkq43g
summary: >-
  Bricken et al. (2023), LIT-tmpn9ui7, read in NOTE-tmpz50gz, Feature
  Splitting and Discussion; and Templeton et al. (2024), LIT-tmp8w8uj, read
  in NOTE-tmpfpjyr, for the same splitting at 1M, 4M and 34M features in a
  large model. In a one-layer model one base64 feature becomes three, then
  more; in Claude 3 Sonnet a San Francisco feature becomes two, then
  eleven. The authors offer two pictures, an idealized set seen at varying
  resolution and feature manifolds with no finite description; both deny
  that one width is the right one.
---
<!-- inactive-ok-file: THEORY-017 CLAIM-tmpwr001 — Proposed; the neighbouring account and claim, cited as open -->
# THEORY-tmpz7jrx: The features a sparse autoencoder recovers from a language model are a resolution set by the dictionary's width and sparsity penalty, not a unique set of the model's units: as the dictionary widens, features split into families of finer features, and splits also merge, so that the number of features is not well-posed

## Source

- Bricken et al. (2023), LIT-tmpn9ui7, read in full in NOTE-tmpz50gz:
  Feature Splitting (the mathematics and physics example, the two "bugs"),
  Universality, and the Discussion's "Theories of Superposition".
- Templeton et al. (2024), LIT-tmp8w8uj, read in full in NOTE-tmpfpjyr:
  Exploring Feature Neighborhoods and Feature Completeness.

## What is asserted

That a sparse autoencoder's features are not the model's units read off
once, but a decomposition at a granularity the analyst sets by width and
penalty. In Bricken et al.'s words: "the features we find at one level may
both split and merge to form refined features at the next", "determining
the 'correct number of features' for dictionary learning is less important
than it might initially seem", and in some theories "finding the 'correct
number of features' may not be well-posed".

## What the record holds toward it

- **Observed splitting.** In the one-layer model, base64 is one feature at
  512, three at 4,096 (letters, digits, base64 encoding ASCII) and more at
  16,384; the three cover the one. In Claude 3 Sonnet a San Francisco
  feature at 1M is two at 4M and eleven at 34M, and some 4M and 34M
  features (earthquakes) have no 1M analogue.
- **Splits that merge.** The mathematics and physics example is "more
  complex than a tree".
- **Coverage tracks width.** In Claude 3 Sonnet a concept gets its own
  feature when its frequency passes about one over the number of live
  features (THEORY-tmplbzq5), so which concepts are units depends on
  dictionary size.

## What it would take

See promote_when. The record holds examples read from feature browsers and
neighbourhood plots, with a cosine or activation-similarity threshold
chosen to make a graph legible. No measurement says what fraction of
features split, merge or persist across widths.

## Connections

- **THEORY-017.** Its thesis, that parts and features are fixed by an
  extrinsic choice, here in a measured case of a learned network: the
  dictionary's width and penalty are the choice.
- **THEORY-018.** The softmax leaves the final layer free up to an
  invertible map; this account adds that even with the basis fixed by
  sparsity, the number of units is not.
- **CLAIM-tmpwr001.** If the features are a resolution, then whether a
  perspective or regime "coincides with one feature" depends on width as
  well as on the model.
- **QUESTION-tmpivbso.** A feature model fitted across checkpoints
  inherits this: a feature that appears to split during training may be
  the dictionary's resolution moving, not the network's.
