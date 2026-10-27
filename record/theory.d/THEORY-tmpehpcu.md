---
status: Proposed
promote_when: >-
  Membership fixed by a procedure stated in advance and applied without a
  labeller's judgement (a clustering of weights or activations, or the
  equivariance of weights within a candidate family), which recovers most
  of the article's named, unflagged families in InceptionV1 at well above
  the agreement expected by chance; and the same procedure, run on at
  least one independently trained network of another architecture or
  training set, finding corresponding families. Refuted if such a
  procedure recovers the named families no better than chance, or if
  families found in one model have no counterpart in the other. More
  hand-sorting of units, in this model or another, cannot settle it: that
  is the evidence it already rests on.
title: 'The units of the early layers of trained vision networks fall largely into neuron families, sets of variants of one feature across orientation, colour or scale, which reflect structure in the network rather than a convenience of the person sorting them, and the same families form across models, as Olah, Cammarata, Schubert, Goh, Petrov and Carter propose'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed Proposed from NOTE-tmpdmtd9, as the claim the measured
    THEORY-tmpjdph0 leaves out (ADR-047 v4). The authors grade it
    themselves: the families are "ad-hoc, human defined", some are
    suspected "real", and "many others are categories of convenience".
tags:
- representation-learning
date: '2026-10-27'
source:
- LIT-tmp6ii6u
extends:
- THEORY-tmpjdph0
summary: >-
  Olah et al. (2020), LIT-tmp6ii6u, read in NOTE-tmpdmtd9. The article's
  organizing hypothesis: early vision's units come in families, some of
  them real structure (said to be recoverable by factorizing weight
  matrices), and the families recur across models. The census
  (THEORY-tmpjdph0) is by eye in one model; neither the factorization nor
  a second model's sorting is shown.
---
# THEORY-tmpehpcu: The units of the early layers of trained vision networks fall largely into neuron families, sets of variants of one feature across orientation, colour or scale, which reflect structure in the network rather than a convenience of the person sorting them, and the same families form across models, as Olah, Cammarata, Schubert, Goh, Petrov and Carter propose

## Source

Olah et al. (2020), *An Overview of Early Vision in InceptionV1*,
LIT-tmp6ii6u, read in full in NOTE-tmpdmtd9: Playing Cards with Neurons,
Caveats and the Conclusion.

## What is asserted

"Our experience is that many neurons in vision models seem to fall into
families of similar features", "it's not unusual to see a dozen neurons
detecting the same feature in different orientations or colors", and
"the same 'neuron families' seem to recur across models!" Some families
are suspected "real": "some can be recovered from factorizing the layer's
weight matrices". Early vision "seems most likely to be universal".

## What the record holds toward it

- **One model, sorted by eye** (THEORY-tmpjdph0): 77 groups over 1,056
  units, 37% flagged by the authors as uncertain or catch-all.
- **Equivariant families in depth** for the curve circuit: Curve Circuits
  (LIT-tmpl1s2e) finds rotated copies of one unit across Gabor, line and
  early-curve families, which is the kind of structure a family would
  have if it were real.
- **Another model's first layer** only: the TF-Slim InceptionV1, whose
  conv2d0 is crisper, shown in a footnote.

## Why it stays Proposed

The factorization that would make a family more than a label is
mentioned, not shown, and no second model is sorted. The authors list
the question as open: "To what extent do these feature families reflect
fundamental clusters in features, versus a taxonomy that might be helpful
to humans but is ultimately somewhat arbitrary?"

## What would confirm or reject it

The promote_when above.
