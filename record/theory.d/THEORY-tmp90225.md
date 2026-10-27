---
status: Active
title: 'In InceptionV1, the ten curve units of mixed3b, which respond to curves of one orientation and not to the opposite one, regain the 180° echo of earlier curve units when their input is restricted to mixed3a early curves with the negative weights removed, and not when the negative weights are kept; a network one author wrote by hand from the described circuit, without looking at the original weights and tuned afterwards, has grayscale curve units that the authors show, by figures only, approximating the natural ones on synthetic curves across radii and orientations; and substituting them for the ten units recovered 26 of the 46 top-5 classifications lost by deleting the units, on 2,000 validation images, a result the authors call preliminary'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed Active from NOTE-tmphb6el, the reading of Cammarata et al.
    (2021) in full. One study, read in full; the title claims no more
    than the article measured and shows, with its own hedges (by
    figures, tuned afterwards, preliminary), and nothing in the record
    contradicts it (ADR-047 v3). The accuracy footnote's arithmetic was
    checked (2.3% and 1.0% of 2,000 are 46 and 20). The authors' fuller
    claim, that curve detection is a simple algorithm read off the
    weights, is THEORY-tmpxjvwo, Proposed.
tags:
- representation-learning
date: '2026-10-27'
source:
- LIT-tmpl1s2e
summary: >-
  Cammarata et al. (2021), LIT-tmpl1s2e, read in NOTE-tmphb6el: the three
  results of Curve Circuits that test its account of the mixed3b curve
  units, the echo edit, the hand-written reimplementation and the
  substitution. Only the last is a number, and a small one. It holds for
  one model's neuron basis and says nothing about weak firings or other
  families.
---
<!-- inactive-ok-file: THEORY-tmpxjvwo THEORY-1013 THEORY-1022 — Proposed; the authors' full claim, the Zoom In account and the curve account it bears on, cited as open -->
# THEORY-tmp90225: In InceptionV1, the ten curve units of mixed3b, which respond to curves of one orientation and not to the opposite one, regain the 180° echo of earlier curve units when their input is restricted to mixed3a early curves with the negative weights removed, and not when the negative weights are kept; a network one author wrote by hand from the described circuit, without looking at the original weights and tuned afterwards, has grayscale curve units that the authors show, by figures only, approximating the natural ones on synthetic curves across radii and orientations; and substituting them for the ten units recovered 26 of the 46 top-5 classifications lost by deleting the units, on 2,000 validation images, a result the authors call preliminary

## Source

Cammarata, Goh, Carter, Voss, Schubert and Olah (2021), *Curve Circuits*,
Distill, LIT-tmpl1s2e, read in full in NOTE-tmphb6el: 3a Early Curve
Family, An Artificial Artificial Neural Network and its footnotes. The
figures were not rendered; their content is from captions and text.

## What was actually shown

**The echo edit.** mixed3a early curve units respond slightly to curves
rotated 180° from their preferred orientation; the mixed3b curve units do
not. The weights from early curves to curves are positive where
orientations match and negative where they oppose. Radial tuning curves
are shown for three versions of the curve units: unedited ("does not have
echoes"), early-curve input only ("lower resolution ... but do not have
echoes") and early-curve input with positive weights only ("low
resolution and have echoes").

**The reimplementation.** Chris Olah set the weights of a blank network
by hand to implement the families and motifs the article describes, "a
few hour process", without looking at the original weights; before
publication the weights were "tweaked" and negative weights added to
remove echoes. It has no colour or texture units. Compared by feature
visualization, synthetic curves, saliency on dataset examples, circuit
structure and raw weights, it is shown to approximate the natural units,
with a slight echo left.

**The substitution.** On 2,000 ImageNet validation images, top-5
accuracy is 88.6% for the model, 86.3% with the ten curve units removed
(46 fewer correct) and 87.6% with the hand-written units in their place
(20 fewer). The authors give operational reasons for the subset and call
the experiment preliminary.

**What could have come out otherwise.** Removing the negative weights
could have left the curve units without echoes, which would have put
their suppression elsewhere. The hand-written units could have responded
to other radii or orientations than the natural ones. Substituting them
could have recovered nothing, or made accuracy worse than deleting the
units.

## What this does not say

- **Not a quantitative match.** No measure of agreement between the
  hand-written and natural units is given, and nothing on positions drawn
  across the activation distribution.
- **Not a blind test of the echo.** The negative weights that remove the
  echo were added to the hand-written network after it was compared.
- **Not that the deleted accuracy is curve-specific.** The substitution
  measures accuracy, not whether downstream units use the substitutes as
  curve evidence.
- **Not about other models, layers or families.**

## Connections

- **THEORY-1013.** With THEORY-1028, all seven of Zoom In's arguments
  are now held for one family, and the echo edit is one tested
  weight-level prediction. Its promote_when asks for such predictions
  over whole layers.
- **THEORY-1022.** Its promote_when asks for a reimplementation that
  predicts the units' activations across the whole distribution,
  weak firings included, and a downstream intervention. This is a
  reimplementation compared on strong cases, and an intervention on
  accuracy; neither condition is met.
- **THEORY-1028.** The behaviour this circuit is said to produce.
