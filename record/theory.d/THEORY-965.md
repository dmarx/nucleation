---
number: 965
status: Proposed
formerly:
- THEORY-tmp14ee2
promote_when: >-
  A comparison fixed before the results are seen, on features not selected
  for success: sparse-autoencoder features of a large model, sampled at
  random or chosen by a stated rule, steer or localize the concepts they
  are labelled with at least as well as supervised baselines (difference
  of means, probes, distributed alignment search) given the same data, and
  their interventions predict held-out behaviour, with the reconstruction
  error kept out of the intervention or its share measured. It is refuted
  if, under such a comparison, they do worse than the model's own
  dimensions or than supervised directions, as MIB found for known causal
  variables (THEORY-968), and as MIB reports AxBench found for
  steering.
  Further steering transcripts of selected features cannot settle it: that
  is the evidence it rests on.
title: 'Sparse-autoencoder features of a large language model''s residual stream are units the model computes with: they track abstract concepts across languages, modalities and concrete or abstract instances, and intervening on one changes the model''s behaviour in the way its label predicts, better than directions found from a few labelled examples'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Proposed from NOTE-1178, as the paper's wider thesis, which
    THEORY-987 and THEORY-992 leave out (ADR-047 v4). The
    evidence for it is examples and steering of features the authors
    selected, and a comparison with few-shot probes on seven cases chosen
    where feature steering worked.
tags:
- representation-learning
- causality
date: '2026-10-26'
source:
- LIT-1533
- LIT-1545
extends:
- THEORY-987
- THEORY-992
summary: >-
  Templeton et al. (2024), [LIT-1533](../literature.d/LIT-1533.md), read in [NOTE-1178](../notes.d/NOTE-1178.md), with
  Bricken et al. (2023), [LIT-1545](../literature.d/LIT-1545.md), for the one-layer case. The thesis
  of both papers: features are the model's own units, shown by steering.
  The authors' own hedges: steering needs features clamped beyond their
  observed range; the reconstruction error rides along; "we haven't
  rigorously evaluated our features against other steering methods". The
  record holds a result against it for known causal variables
  ([THEORY-968](THEORY-968.md)).
---
<!-- inactive-ok-file: CLAIM-454 THEORY-1016 — Proposed; the claim and the account this bears on, cited as open -->
# THEORY-965: Sparse-autoencoder features of a large language model's residual stream are units the model computes with: they track abstract concepts across languages, modalities and concrete or abstract instances, and intervening on one changes the model's behaviour in the way its label predicts, better than directions found from a few labelled examples

## Source

- Templeton et al. (2024), [LIT-1533](../literature.d/LIT-1533.md), read in full in [NOTE-1178](../notes.d/NOTE-1178.md):
  Assessing Feature Interpretability, Safety-Relevant Features, Comparison
  to Other Approaches, and the steering appendices.
- Bricken et al. (2023), [LIT-1545](../literature.d/LIT-1545.md), read in full in [NOTE-1191](../notes.d/NOTE-1191.md), for
  the one-layer version of the thesis ([THEORY-991](THEORY-991.md)).

## What is asserted

That the features are not only a description of the activations but the
model's working concepts. "We find this compelling evidence that our
interpretations of features line up with how they are used by the model."
And that, in the few-shot regime, they are better handles than probe
directions.

## What the record holds toward it

- **For.** Examples of abstract features (the Golden Gate Bridge feature
  across languages and in images; a code-error feature across
  programming languages; an addition feature that follows function
  composition) and steering in the labelled direction, for features the
  authors chose. 82% of a random sample match no neuron. In the one-layer
  model, effects on the output agree with activations ([THEORY-991](THEORY-991.md)).
  Few-shot difference-of-means vectors steered as well in two of seven
  hand-picked cases and failed in five.
- **Against or qualifying.** Steering typically needs a clamp beyond the
  feature's observed range, which the authors attribute to correlated
  features acting together. The most active features are mostly not those
  that carry the answer ([THEORY-987](THEORY-987.md)). In MIB, features of public
  autoencoders on Gemma-2 and Llama-3.1 residual streams localized known
  causal variables worse than the model's own dimensions in all sixteen
  cells ([THEORY-968](THEORY-968.md)). Residual-stream autoencoders are the site where
  Gemma Scope's cost the most loss ([THEORY-504](THEORY-504.md)).

## What it would take

See promote_when.

## Connections

- **[CLAIM-454](../claims.d/CLAIM-454.md).** The thesis is the strong reading the claim denies
  for organizations: that a recovered feature is the variable that does
  the work. Its evidence is examples of a feature moving behaviour when
  pushed hard, which the claim allows of a constituent.
- **[THEORY-968](THEORY-968.md).** The present test against it.
- **[THEORY-1016](THEORY-1016.md).** If the features are a resolution, the thesis
  needs a statement of which resolution's features are the units.
