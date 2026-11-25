---
number: 138
status: Proposed
formerly:
- TERM-tmpol232
title: 'separation'
statement: >-
  separation, in three senses that come apart: of scales or levels, when a
  gap in rates, sizes or coupling lets a coarser description close over a
  window; of classes, when an observer or readout under its budget can tell
  two states or populations apart; and spectral, when an outlier eigenvalue
  detaches from a noise bulk
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
  [CLAIM-829](../claims.d/CLAIM-829.md)). (2) Separation of classes: an observer or readout under
  its budget tells two states or populations apart ([SYNTHESIS-109](../syntheses.d/SYNTHESIS-109.md),
  [SYNTHESIS-083](../syntheses.d/SYNTHESIS-083.md), [TERM-069](TERM-069.md)). (3) Spectral separation: an outlier eigenvalue
  detaches from a noise bulk, so a direction becomes detectable without
  labels ([CLAIM-799](../claims.d/CLAIM-799.md), [CLAIM-827](../claims.d/CLAIM-827.md)). They come apart in both
  directions, as the body shows. Its job is to let an entry say which it
  means. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-819 CLAIM-478 CLAIM-829 CLAIM-845 CLAIM-840 CLAIM-826 ARG-125 CLAIM-157 SYNTHESIS-054 SYNTHESIS-048 SYNTHESIS-109 SYNTHESIS-083 CLAIM-799 CLAIM-827 CLAIM-837 CASE-301 CASE-305 SYNTHESIS-119 SYNTHESIS-120 — Proposed or new; the entries each sense points to -->
<!-- inactive-ok-file: CLAIM-1196 CLAIM-1174 — new; filed from the owner's U6 of 2026-11-22, cited in the note of that date -->

# TERM-138: separation

## Definition

- **Separation of scales or levels (sense 1).** A gap between characteristic rates, sizes or lengths, or weak coupling between blocks against strong coupling within them, such that a coarser description closes to a good approximation over the window the gap opens.
  - **In time:** [CLAIM-478](../claims.d/CLAIM-478.md), where a rate gap makes a constraint over the window between two rates, and [SYNTHESIS-048](../syntheses.d/SYNTHESIS-048.md), where coupling separates time scales only where it dissipates differences.
  - **In interaction strength:** [THEORY-661](../theory.d/THEORY-661.md), Simon's near-decomposability, and [SYNTHESIS-054](../syntheses.d/SYNTHESIS-054.md), where a combined form is a unit while it is a block isolated by a gap ([CLAIM-157](../claims.d/CLAIM-157.md)).
  - **In size:** [CLAIM-829](../claims.d/CLAIM-829.md), where a bulk with a fixed small scale is separated from a tail whose cutoff runs away as a continuous transition nears. This is reading (b) of the owner's U5 ([CLAIM-840](../claims.d/CLAIM-840.md)).
- **Separation of classes (sense 2).** Two states, populations or hypotheses can be told apart by an observer, a probe family or a readout, under a stated budget.
  - [SYNTHESIS-109](../syntheses.d/SYNTHESIS-109.md): what can be told apart grows with the observing budget.
  - [SYNTHESIS-083](../syntheses.d/SYNTHESIS-083.md): a regularized linear readout separates exactly what its kernel separates.
  - [TERM-069](TERM-069.md): observational equivalence under a probe family is the failure of this sense.

  "Linearly separable" is this sense with a linear readout.
- **Spectral separation (sense 3).** An eigenvalue of a sample covariance, or of another random-matrix ensemble, detaches from the bulk's edge, so the direction carrying it can be found without labels. In the spiked model it happens above β = √γ, with γ = D/N.
  - [CLAIM-799](../claims.d/CLAIM-799.md): geometric separation, decodability and spectral detectability come apart.
  - [CLAIM-827](../claims.d/CLAIM-827.md): the spectral threshold placed on one scale with the others.
  - [CLAIM-837](../claims.d/CLAIM-837.md): the lag before sample PCA sees a feature.

## How they come apart

- **Sense 2 without sense 3.** In [CASE-301](../cases.d/CASE-301.md), below the spectral threshold (β = 0.4 against 0.5), PCA finds nothing while a trained readout is 74% accurate. A class distinction can be drawn before any direction is spectrally visible ([CLAIM-799](../claims.d/CLAIM-799.md)).
- **Sense 2 without sense 1.** Near a critical point a system is "harder to separate but easier to classify" ([CLAIM-826](../claims.d/CLAIM-826.md), A17 §5): fluctuations stay consequential across scales, so no level separates, while universality makes the class easy to tell. A finite correlation length does not give sense 1 in Simon's form: Simon's condition is weak interaction, not decay of correlation, and holds for large blocks even at criticality ([CLAIM-819](../claims.d/CLAIM-819.md); the route it corrects is [ARG-125](../arguments.d/ARG-125.md)). What criticality removes is the separation of time scales Simon's consequence needs.
- **Sense 1 and sense 3 share a shape, not a mechanism.** Both have a bulk and something set apart from it. The spectral case realizes the other reading of U5, a gap in support ([CLAIM-845](../claims.d/CLAIM-845.md)), and only above its threshold. Below β = √γ the top eigenvalue sits at the bulk's edge (1 + √γ)². Above it, the outlier sits at (1 + β)(1 + γ/β), a gap of (β − √γ)²/β from the edge; the algebra is checked by expanding both. That is the pattern percolation and the epidemic show above their thresholds, where one giant cluster stands apart ([CASE-305](../cases.d/CASE-305.md)). Below a continuous transition, sense 1 in size holds without any gap. A32's tie of the owner's bulk-and-tail intuition to the spectral outlier is sound for this supercritical gap, not for the subcritical separation of scales.

## What it is not

- **Separability of a joint law**, independence or a product form: a sense of its own, not covered here.
- **Separation of variables:** a method, not a property.
- **A claim that any sense implies another.** Where an entry says "separated", this term asks which sense, and the record's entries above hold what is known of how they relate.

## Sources

The three senses are the assistant's sorting of the exchange's uses (A7, A13 §9, A17 §5, A21, A31, A32, A42) against the record's held entries. They are integrated in two accounts: [SYNTHESIS-119](../syntheses.d/SYNTHESIS-119.md) for sense 1 in this exchange, and [SYNTHESIS-120](../syntheses.d/SYNTHESIS-120.md) for senses 2 and 3.

## Note of 2026-11-21: Acharya, Rimal & Dhakal, read

A sense the term does not list ([NOTE-2251](../notes.d/NOTE-2251.md)). The paper uses Park, Choe
and Veitch's "causally separable" concepts (p. 1; [LIT-304](../literature.d/LIT-304.md)): concepts that
"can be varied freely and in isolation", the joint counterfactual
Y(W = w, Z = z) being well-defined for every pair of values; Park et al.'s
Assumption 3.3 ties it to independence of λ̄_Wᵀγ and λ̄_Zᵀγ for an
unembedding vector γ drawn uniformly from the vocabulary. That is closest
to the separability of a joint law, which "What it is not" sets aside as a sense
of its own. The paper's probes (accuracy above 0.99, §6) are sense 2 with
a linear readout; its head-against-tail POS probes are sense 2 restricted
to a subspace. Nothing in it is sense 3. Its "anti-concentration" is not a
separation in any sense: it places a direction relative to a spectrum. No
relation written.

## Note of 2026-11-22: the owner's "separating", for perspectives

In the exchange "Explain First Contact RL" (ChatGPT, shared 2026-11-22), the owner asked at U6 whether "separating" is the record's sense for telling perspectives apart, after A11's "The address of a perspective is thus relative to the tests we can afford to perform". It is this term's separation of classes, applied to perspectives as the classes: what an observer under its budget can tell apart. A13 §1 used all three senses for a self ("Class separation", "Scale separation", "Spectral separation") and said "none entails the others", as this term does. The entries filed from that turn are [CLAIM-1196](../claims.d/CLAIM-1196.md) and [CLAIM-1174](../claims.d/CLAIM-1174.md) (the owner's proposal, in two readings) and the term [TERM-165](TERM-165.md). A use of the term, not evidence about it. No change.
