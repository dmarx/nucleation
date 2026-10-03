---
status: Proposed
promote_when: >-
  A second group's measurement of the case that carries the claim: two
  sets of trained networks with the same endpoint Hessian (top eigenvalue
  and trace) and different test accuracy, where the less accurate set is
  the one whose independently trained solutions are poorly connected or
  compute less similar functions. It has to be on an architecture or task
  outside Yang et al.'s ResNet18 on CIFAR-10, and with connectivity
  measured both by a fitted curve and after permutation alignment, so
  that a barrier one curve family failed to remove is not read as a
  separation between basins. The account is refuted if, at matched
  curvature, connectivity and output similarity stop ordering accuracy,
  or if the poorly connected, flat runs turn out to be connected once
  aligned while their accuracy deficit stays, which would make the
  measured barrier an artefact of the probe and not the predictor. More
  runs of the same ResNet18 grid cannot settle it, and neither can a
  local measure other than the Hessian (such as a learning-coefficient
  estimate) that separates the cases, since that would bear on why
  curvature fails, not on whether global structure predicts.
title: 'Across load and temperature, the connectivity and output similarity of independently trained solutions predict test accuracy where endpoint curvature does not: a flat but poorly connected landscape generalizes worse than a connected one of the same curvature'
version: 1
tags:
- loss-landscapes
- learning-theory
- anthology-candidate
date: '2026-10-03'
source:
- LIT-tmpf3sak
summary: >-
  Yang, Hodgkinson, Theisen, Zou, Gonzalez, Ramchandran & Mahoney (2021),
  [LIT-tmpf3sak](../literature.d/LIT-tmpf3sak.md): thousands of trained networks on a load by temperature
  grid, measured by the endpoint Hessian, by mode connectivity on a
  trained Bezier curve between two independent runs, and by CKA of their
  outputs. Phases III (flat, poorly connected) and IV-A (flat, connected)
  have almost the same Hessian and different accuracy; with 10% noisy
  labels the sharp, unconverged phases beat phase III; label noise barely
  moves the Hessian while connectivity and CKA fall. The best accuracy is
  in the flat, connected, high-similarity phase IV-B. The counterexamples
  are to the anthology's [ANTH-SOTA-012](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/practices.d/SOTA-012.md). One architecture family carries
  most of it, phases are read by eye, and connectivity alone also fails
  when the load is data amount.
---
<!-- inactive-ok-file: THEORY-087 THEORY-078 — Proposed; named in Connections for what endpoint curvature measures, nothing here rests on them -->

# THEORY-tmp7wk2u: Across load and temperature, the connectivity and output similarity of independently trained solutions predict test accuracy where endpoint curvature does not: a flat but poorly connected landscape generalizes worse than a connected one of the same curvature

## Source

- Yang, Hodgkinson, Theisen, Zou, Gonzalez, Ramchandran & Mahoney (2021),
  [LIT-tmpf3sak](../literature.d/LIT-tmpf3sak.md), read in [NOTE-tmp3zzdt](../notes.d/NOTE-tmp3zzdt.md): Sections 2–3 (Figures 2–8),
  Appendices A–D.

## The claim

A trained network's landscape has a local character, the curvature where
training stopped, and a global one: whether two independently trained
solutions can be joined at low loss, and whether they compute the same
function. Yang et al. ([LIT-tmpf3sak](../literature.d/LIT-tmpf3sak.md)) vary a load-like control parameter
(width, amount of data, fraction of noisy labels) against a
temperature-like one (batch size, learning rate, weight decay), and at
every grid point measure three things. The local probe is the top Hessian
eigenvalue and trace at the endpoint. Connectivity is
mc = ½(L(θ) + L(θ′)) − L(γ(t*)) at the worst point of a trained quadratic
Bezier curve between two runs, in 0-1 training error (Eq. 4). Similarity
is linear CKA of the two runs' softmax outputs on mixup points (Eq. 3).
The grid falls into four phases: I sharp and poorly connected, II sharp
and well connected, III flat and poorly connected, IV flat and well
connected, with IV split by CKA into IV-A and IV-B.

What carries the claim is the set of cases in which curvature and
accuracy part company, and the global measures do not:

- **Same curvature, different accuracy.** In the standard grid (ResNet18,
  CIFAR-10, width against batch size), "the test accuracy in Phase III is
  lower than Phase IV-A but the Hessian eigenvalues are almost the same"
  (Figure 2). What separates them is connectivity.
- **Sharper and better.** With 10% of labels randomized, on a width
  column cutting through phase III, the best test accuracy is in phases
  I/II, which are sharp and not trained to zero loss. The authors write
  that "one will wrongly predict that Phase III outperforms Phase I/II if
  one only looks at local sharpness", since both Hessian measures are
  smaller in phase III (Figure 4). Phase III has poor connectivity and low
  CKA.
- **Curvature blind to data quality.** As the fraction of noisy labels
  rises from 2.5% to 60%, the Hessian trace below a training loss of 5e-3
  changes little, while connectivity and CKA degrade with the noise
  (Figure 8).
- **Curvature moving the wrong way.** Lower weight decay makes the Hessian
  trace very small in wide models, though weight decay is known to help
  (Figure 5). More training data raises the Hessian while accuracy rises
  (Figures 6–7).

The best accuracy sits in phase IV-B, flat, connected and similar, in
every image-classification grid shown: with learning-rate decay, with
weight decay or learning rate as the temperature, and on CIFAR-100, SVHN
and VGG11 in the appendix (Sections 3.2–3.3, Appendix D). The one
language task does not reach that phase. A six-layer Transformer on 4K
pairs of IWSLT'16 De-En stays poorly connected up to embedding dimension
512, so the whole grid is phase I by the authors' reading, and there
early stopping beats training to zero loss (Appendix D.4, Figures
18–19). That is consistent with the claim, not a test of its IV-B half.
The authors' own reading of the earlier correlation between sharpness
and generalization is that it "may be correlative and not causative",
confounded by studying "reasonably-good models trained to
reasonably-good data".

The global half has to be read as connectivity and similarity together.
When the load is the amount of data, connectivity alone also mispredicts:
the well-connected region shrinks as data grow while accuracy rises, and
only CKA tracks the trend (Figures 6–7). The paper says as much: "both
similarity and connectivity metrics are required."

## Against the anthology

The anthology's practice that sharpness in the loss landscape correlates
with test error ([ANTH-SOTA-012](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/practices.d/SOTA-012.md), from Li et al.'s filter-normalised
landscape plots, [ANTH-LIT-014](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-014.md)) is the claim these cases are
counterexamples to. Phase III against IV-A, the noisy-label column and the
weight-decay grid are each a pair of training configurations whose
sharpness ordering and accuracy ordering disagree. The anthology already
qualifies that practice by the argument that networks are singular, so
that effective complexity is the scaling of near-optimal volume and not
curvature ([ANTH-THEORY-075](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-075.md)), and it holds a proposed alternative
measurement, degeneracy rather than curvature once the loss has saturated
([ANTH-SOTA-325](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/practices.d/SOTA-325.md)). Yang et al. answer the same insufficiency from the other
side: not a better local measure, but a global one.

## What this does not say

- **It does not say curvature is uninformative.** The Hessian transition
  is real and coincides with a more than tenfold fall in training loss
  (Figure 2). Curvature separates converged from unconverged training. The
  claim is that it does not rank converged solutions by test accuracy
  across the grid.
- **It does not say the phases are phases in the statistical-mechanics
  sense.** No limit is taken, the boundaries are read from colour maps,
  and the IV-A/IV-B split is admitted to be "a smooth crossover".
- **It does not establish that the barriers are real separations between
  basins.** Connectivity is measured on one curve family, a quadratic
  Bezier trained for 50 epochs, without permutation alignment. A negative
  mc says this family found no low path, not that none exists.
- **It does not reach networks trained as in practice.** There is no data
  augmentation, by design, and ResNet18 on CIFAR-10 makes up most figures.
  Outside image classification there is one small translation task, which
  never leaves the poorly connected phase.
- **It does not explain phase III.** The authors attribute its deficit to
  "insufficient exploration" at constant low temperature, and the
  noisy-label result is shown only without learning-rate decay.
- **It is not cheap.** Each grid point needs several trainings plus a
  curve fit, and the global measures need no test data but do need two
  independent runs.

## Connections

- **The phase framing** is Martin and Mahoney's ([LIT-tmpms4ta](../literature.d/LIT-tmpms4ta.md)), who
  proposed the load and temperature parameters and a phase diagram for
  generalization as a cartoon; Yang et al. measure it. The curve-fitting
  instrument is Garipov et al.'s ([LIT-tmpotq71](../literature.d/LIT-tmpotq71.md)).
- **What the endpoint Hessian measures.** In Papyan's class/cross-class
  picture ([LIT-613](../literature.d/LIT-613.md)), stated in the record as [THEORY-078](THEORY-078.md), the top
  eigenvalues are class-driven outliers, so the "top eigenvalue" probe
  here partly measures between-class structure at the endpoint. In
  Watanabe's singular learning theory ([LIT-616](../literature.d/LIT-616.md), [THEORY-087](THEORY-087.md)) the local
  quantity that sets the complexity penalty is degeneracy, which neither a
  trace nor a top eigenvalue measures. Either may be why curvature fails
  here. Neither is tested by this paper, and nothing in the claim rests on
  them.
- **MacKay's Occam factor** ([LIT-623](../literature.d/LIT-623.md)) prices a basin by the determinant of
  its Hessian. Phase III, flat yet poorly generalizing, is a case where a
  large Occam factor at the endpoint does not by itself mean
  generalization when the basins are disconnected. That is the reading in
  [NOTE-tmp3zzdt](../notes.d/NOTE-tmp3zzdt.md), not the paper's.
- **Double descent.** With noisy labels a dark band of low accuracy runs
  along the Hessian transition, read as double descent at a phase
  boundary. The exact accounts the paper says it corroborates are the
  random-feature and linear ones ([LIT-tmpufwlh](../literature.d/LIT-tmpufwlh.md), [LIT-tmpzk7ci](../literature.d/LIT-tmpzk7ci.md)).
