---
status: Proposed
title: "separation, in three senses that come apart: of scales or levels, when a gap in rates, sizes or coupling lets a coarser description close over a window; of classes, when an observer or readout under its budget can tell two states or populations apart; and spectral, when an outlier eigenvalue detaches from a noise bulk"
version: 1
tags:
- complex-systems
- information-geometry
- representation-learning
date: '2026-11-21'
line:
- formal-apparatus
- learned-structure
draws_on:
- THEORY-661
summary: >-
  At the owner's question of 2026-11-21, whether the record had an account
  of "the notion of separability raised in the conversation" ("Rich Get
  Richer Power Laws"), and the owner's go-ahead ("dialectic on") for the
  term the answer proposed. The exchange uses "separation" in three senses
  and moves between them: A32 ties the owner's bulk-and-tail intuition (U5)
  to a spectral outlier. The record held each sense under another name and
  had no word that kept them apart. (1) Separation of scales or levels: a
  gap in rates, sizes or coupling lets a coarser description close over a
  window ([THEORY-661](../theory.d/THEORY-661.md), [CLAIM-478](../claims.d/CLAIM-478.md), [SYNTHESIS-054](../syntheses.d/SYNTHESIS-054.md), [SYNTHESIS-048](../syntheses.d/SYNTHESIS-048.md),
  [CLAIM-tmplb1ow](../claims.d/CLAIM-tmplb1ow.md)). (2) Separation of classes: an observer or readout under
  its budget tells two states or populations apart ([SYNTHESIS-109](../syntheses.d/SYNTHESIS-109.md),
  [SYNTHESIS-083](../syntheses.d/SYNTHESIS-083.md), [TERM-069](TERM-069.md)). (3) Spectral separation: an outlier eigenvalue
  detaches from a noise bulk, so a direction becomes detectable without
  labels ([CLAIM-tmp5y856](../claims.d/CLAIM-tmp5y856.md), [CLAIM-tmpk33au](../claims.d/CLAIM-tmpk33au.md)). They come apart in both
  directions, as the body shows. Its job is to let an entry say which it
  means. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpewm5i CLAIM-478 CLAIM-tmplb1ow CLAIM-tmpvrbdt CLAIM-tmpr9au6 CLAIM-tmpjbee7 ARG-tmp09yqc CLAIM-157 SYNTHESIS-054 SYNTHESIS-048 SYNTHESIS-109 SYNTHESIS-083 CLAIM-tmp5y856 CLAIM-tmpk33au CLAIM-tmpqbo50 CASE-tmp59xy5 CASE-tmpykltu SYNTHESIS-tmp69tyj SYNTHESIS-tmpsejrp — Proposed or new; the entries each sense points to -->

# TERM-tmpol232: separation, in three senses that come apart: of scales or levels, when a gap in rates, sizes or coupling lets a coarser description close over a window; of classes, when an observer or readout under its budget can tell two states or populations apart; and spectral, when an outlier eigenvalue detaches from a noise bulk

## Definition

- **Separation of scales or levels (sense 1).** A gap between characteristic rates, sizes or lengths, or weak coupling between blocks against strong coupling within them, such that a coarser description closes to a good approximation over the window the gap opens.
  - **In time:** [CLAIM-478](../claims.d/CLAIM-478.md), where a rate gap makes a constraint over the window between two rates, and [SYNTHESIS-048](../syntheses.d/SYNTHESIS-048.md), where coupling separates time scales only where it dissipates differences.
  - **In interaction strength:** [THEORY-661](../theory.d/THEORY-661.md), Simon's near-decomposability, and [SYNTHESIS-054](../syntheses.d/SYNTHESIS-054.md), where a combined form is a unit while it is a block isolated by a gap ([CLAIM-157](../claims.d/CLAIM-157.md)).
  - **In size:** [CLAIM-tmplb1ow](../claims.d/CLAIM-tmplb1ow.md), where a bulk with a fixed small scale is separated from a tail whose cutoff runs away as a continuous transition nears. This is reading (b) of the owner's U5 ([CLAIM-tmpr9au6](../claims.d/CLAIM-tmpr9au6.md)).
- **Separation of classes (sense 2).** Two states, populations or hypotheses can be told apart by an observer, a probe family or a readout, under a stated budget.
  - [SYNTHESIS-109](../syntheses.d/SYNTHESIS-109.md): what can be told apart grows with the observing budget.
  - [SYNTHESIS-083](../syntheses.d/SYNTHESIS-083.md): a regularized linear readout separates exactly what its kernel separates.
  - [TERM-069](TERM-069.md): observational equivalence under a probe family is the failure of this sense.

  "Linearly separable" is this sense with a linear readout.
- **Spectral separation (sense 3).** An eigenvalue of a sample covariance, or of another random-matrix ensemble, detaches from the bulk's edge, so the direction carrying it can be found without labels. In the spiked model it happens above β = √γ, with γ = D/N.
  - [CLAIM-tmp5y856](../claims.d/CLAIM-tmp5y856.md): geometric separation, decodability and spectral detectability come apart.
  - [CLAIM-tmpk33au](../claims.d/CLAIM-tmpk33au.md): the spectral threshold placed on one scale with the others.
  - [CLAIM-tmpqbo50](../claims.d/CLAIM-tmpqbo50.md): the lag before sample PCA sees a feature.

## How they come apart

- **Sense 2 without sense 3.** In [CASE-tmp59xy5](../cases.d/CASE-tmp59xy5.md), below the spectral threshold (β = 0.4 against 0.5), PCA finds nothing while a trained readout is 74% accurate. A class distinction can be drawn before any direction is spectrally visible ([CLAIM-tmp5y856](../claims.d/CLAIM-tmp5y856.md)).
- **Sense 2 without sense 1.** Near a critical point a system is "harder to separate but easier to classify" ([CLAIM-tmpjbee7](../claims.d/CLAIM-tmpjbee7.md), A17 §5): fluctuations stay consequential across scales, so no level separates, while universality makes the class easy to tell. A finite correlation length does not give sense 1 in Simon's form: Simon's condition is weak interaction, not decay of correlation, and holds for large blocks even at criticality ([CLAIM-tmpewm5i](../claims.d/CLAIM-tmpewm5i.md); the route it corrects is [ARG-tmp09yqc](../arguments.d/ARG-tmp09yqc.md)). What criticality removes is the separation of time scales Simon's consequence needs.
- **Sense 1 and sense 3 share a shape, not a mechanism.** Both have a bulk and something set apart from it. The spectral case realizes the other reading of U5, a gap in support ([CLAIM-tmpvrbdt](../claims.d/CLAIM-tmpvrbdt.md)), and only above its threshold. Below β = √γ the top eigenvalue sits at the bulk's edge (1 + √γ)². Above it, the outlier sits at (1 + β)(1 + γ/β), a gap of (β − √γ)²/β from the edge; the algebra is checked by expanding both. That is the pattern percolation and the epidemic show above their thresholds, where one giant cluster stands apart ([CASE-tmpykltu](../cases.d/CASE-tmpykltu.md)). Below a continuous transition, sense 1 in size holds without any gap. A32's tie of the owner's bulk-and-tail intuition to the spectral outlier is sound for this supercritical gap, not for the subcritical separation of scales.

## What it is not

- **Separability of a joint law**, independence or a product form: a sense of its own, not covered here.
- **Separation of variables:** a method, not a property.
- **A claim that any sense implies another.** Where an entry says "separated", this term asks which sense, and the record's entries above hold what is known of how they relate.

## Sources

The three senses are the assistant's sorting of the exchange's uses (A7, A13 §9, A17 §5, A21, A31, A32, A42) against the record's held entries. They are integrated in two accounts: [SYNTHESIS-tmp69tyj](../syntheses.d/SYNTHESIS-tmp69tyj.md) for sense 1 in this exchange, and [SYNTHESIS-tmpsejrp](../syntheses.d/SYNTHESIS-tmpsejrp.md) for senses 2 and 3.
