---
status: Active
title: 'In sparse autoencoders of about 1M, 4M and 34M features on Claude 3 Sonnet''s middle-layer residual stream, whether a concept among chemical elements, cities, animals and foods had a dedicated feature depended on how often it occurs in the training data: the frequency at which a concept became more than 50% likely to have one was slightly below one over the number of live features, and the three dictionaries'' curves roughly coincided when frequency was rescaled by that number'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Active from NOTE-tmpfpjyr, the reading of Templeton et al. (2024)
    in full. One study; the title claims what its completeness analysis
    measured on four categories and three dictionaries, and nothing in the
    record contradicts it (ADR-047 v3). The extrapolation to "a billion
    alive features" for a once-in-a-billion concept, and the Zipf
    speculation, are the authors' and are not claimed.
tags:
- representation-learning
date: '2026-10-26'
source:
- LIT-tmp8w8uj
extended_by:
- THEORY-tmp14ee2
summary: >-
  Templeton et al. (2024), [LIT-tmp8w8uj](../literature.d/LIT-tmp8w8uj.md), read in [NOTE-tmpfpjyr](../notes.d/NOTE-tmpfpjyr.md): Feature
  Completeness. 100–200 single-word concepts per category, presence of a
  feature judged from Sonnet's explanations of the top five features on a
  prompt naming the concept, by a human rater. The 34M dictionary (about 12
  million live features) had features for about 60% of London boroughs,
  although the model names them all. It does not separate frequency in the
  model's training data from frequency in the autoencoder's, which the
  authors say are similar mixtures.
---
<!-- inactive-ok-file: THEORY-tmpz7jrx THEORY-017 CLAIM-tmpwr001 THEORY-tmp14ee2 — Proposed; the accounts and claim this one bears on, cited as open -->
# THEORY-tmplbzq5: In sparse autoencoders of about 1M, 4M and 34M features on Claude 3 Sonnet's middle-layer residual stream, whether a concept among chemical elements, cities, animals and foods had a dedicated feature depended on how often it occurs in the training data: the frequency at which a concept became more than 50% likely to have one was slightly below one over the number of live features, and the three dictionaries' curves roughly coincided when frequency was rescaled by that number

## Source

Templeton, Conerly, Marcus, Lindsey et al. (2024), *Scaling
monosemanticity*, [LIT-tmp8w8uj](../literature.d/LIT-tmp8w8uj.md), read in full in [NOTE-tmpfpjyr](../notes.d/NOTE-tmpfpjyr.md): Our SAE
experiments (dead-feature fractions) and Feature Completeness.

## What was actually shown

**The procedure.** For each concept, a prompt naming it is run and the
five features most active on its last token are explained by Sonnet; a
human judges whether an explanation specifically names the concept. The
concept's frequency is counted in a proxy of the training data by
searching for the name between spaces, with false positives the authors
note (the element "lead").

**The dictionaries.** About 1M, 4M and 34M features, with about 2%, 35%
and 65% dead, so roughly 1.0M, 2.7M and 11.7M live (computed here from the
stated fractions; the paper says "about 12M" for the largest).

**The result.** For each dictionary and category, the share of concepts
with a feature rises with frequency, and the point where it passes one
half is "consistently slightly lower than the inverse of the number of
alive features". Rescaling frequency by the live-feature count makes the
curves roughly coincide, a sigmoid in log frequency, with a similar
threshold across categories. Separately, the 34M dictionary had features
for about 60% of London boroughs.

**What could have come out otherwise.** Coverage could have depended on
the category (places before foods), or on salience rather than frequency,
or grown with size along curves that do not coincide.

## What this does not say

- **Not that a concept without a feature is absent from the model.** The
  authors say the model "can use multiple related features
  compositionally to reference a specific concept", and the model names
  every London borough.
- **Not which frequency matters.** The autoencoder's training data
  resembles the model's pre-training data, so the two frequencies are not
  separated.
- **Not the extrapolation.** That a once-in-a-billion concept needs about
  a billion live features is the authors' projection.
- **Not a measured detection error.** Presence is judged from Sonnet's
  explanations of the top five features by one human rule; a feature
  outside the top five, or mislabelled, would be missed.

## Connections

- **[THEORY-tmpz7jrx](THEORY-tmpz7jrx.md).** Which concepts are units depends on dictionary
  size: the measured part of the claim that the feature set is a
  resolution.
- **[THEORY-017](THEORY-017.md).** A decomposition whose parts appear as the dictionary
  grows is one fixed by the analyst's budget, not by the model alone.
- **[CLAIM-tmpwr001](../claims.d/CLAIM-tmpwr001.md).** A concept the model uses with no feature of its own
  is held by a combination of features, the claim's case of something
  carried by an arrangement and not by a single recovered unit.
