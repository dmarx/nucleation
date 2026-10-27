---
status: Proposed
promote_when: >-
  A quantitative test of the description against the units it describes:
  the hand-written curve units, or any network written from the
  description alone, predicting the natural mixed3b curve units'
  activations on dataset positions drawn across the whole activation
  distribution, not only strongly activating curves, with most of the
  variance accounted for; the named families carrying most of the curve
  units' input attribution, given the long tail of small weights the
  authors report; and the substitution repeated on the full validation
  set. Refuted if the hand-written units account for little of the
  natural units' variance away from strong curve stimuli, or if most of
  the input attribution lies outside the named families. More figures of
  synthetic-curve responses or weight patterns cannot settle it: they are
  the evidence it already rests on.
title: 'The curve units of InceptionV1''s mixed3b implement a simple algorithm that can be read off their weights and written down in a few sentences: families of Gabors, lines and early curves, each a set of rotated copies of one unit, tiled along the curve''s tangent, with negative weights against similar shapes of opposing orientation, rotational and scale equivariance reducing the circuit''s more than 50,000 parameters about fifty-fold, so that a network written from this description reimplements them and the description accurately reflects the circuit, as Cammarata, Goh, Carter, Voss, Schubert and Olah claim'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed Proposed from NOTE-tmphb6el, as the claim the measured
    THEORY-tmp90225 leaves out (ADR-047 v4). The authors call their five
    comparisons "strong evidence these patterns accurately reflect the
    underlying circuits"; four are figures and the fifth is preliminary.
tags:
- representation-learning
date: '2026-10-27'
source:
- LIT-tmpl1s2e
extends:
- THEORY-tmp90225
summary: >-
  Cammarata et al. (2021), [LIT-tmpl1s2e](../literature.d/LIT-tmpl1s2e.md), read in [NOTE-tmphb6el](../notes.d/NOTE-tmphb6el.md). The
  article's account of how curve detectors are built, and its claim that
  the account is the circuit. The family structure and the echo edit are
  measured ([THEORY-tmp90225](THEORY-tmp90225.md)); that the description is complete, and that
  the reimplementation matches the natural units beyond strong cases, is
  shown by figures only.
---
<!-- inactive-ok-file: THEORY-1022 — Proposed; the curve account this would serve, cited as open -->
# THEORY-tmpxjvwo: The curve units of InceptionV1's mixed3b implement a simple algorithm that can be read off their weights and written down in a few sentences: families of Gabors, lines and early curves, each a set of rotated copies of one unit, tiled along the curve's tangent, with negative weights against similar shapes of opposing orientation, rotational and scale equivariance reducing the circuit's more than 50,000 parameters about fifty-fold, so that a network written from this description reimplements them and the description accurately reflects the circuit, as Cammarata, Goh, Carter, Voss, Schubert and Olah claim

## Source

Cammarata et al. (2021), *Curve Circuits*, [LIT-tmpl1s2e](../literature.d/LIT-tmpl1s2e.md), read in full in
[NOTE-tmphb6el](../notes.d/NOTE-tmphb6el.md): the introduction, The Curve Detector Algorithm, The
Components of Curve Detectors and An Artificial Artificial Neural
Network.

## What is asserted

"Although curve detection involves more than 50,000 parameters, those
parameters actually implement a simple algorithm that can be read off the
weights and described in just a few English sentences." The sentences:
"Gabor filters turn into proto-lines which build lines and early curves.
Finally, lines and early curves are composed into curves. In each case,
each shape family ... has positive weight across the tangent of the shape
family it builds", and each "implements the rotational equivariance
motif". After the reimplementation: "we think this is strong evidence
these patterns accurately reflect the underlying circuits that construct
curve detectors."

## What the record holds toward it

- **The echo edit, the reimplementation and the substitution**
  ([THEORY-tmp90225](THEORY-tmp90225.md)): one tested weight-level prediction, a qualitative
  match on synthetic curves and strong dataset examples, and 26 of 46
  lost classifications recovered on 2,000 images.
- **The structure,** read from the strongest weights and the
  highest-magnitude position per layer, by decomposed feature
  visualization and weight matrices.
- **Against it, the authors' own caveats**: a "long tail of neurons with
  low magnitude that collectively make up a large fraction of the total
  weight"; mixed3a's line-to-curve matrix is "indecipherable" until one
  goes back a layer; the hand-written units lack colour and texture, and
  the authors expect "many false-negatives".

## Why it stays Proposed

"Simple" and "accurately reflect" are claims about the whole circuit,
and the evidence is about its strongest parts, compared by figure. The
weak firings that [THEORY-1022](THEORY-1022.md) finds unexplained are not compared.

## What would confirm or reject it

The promote_when above.
