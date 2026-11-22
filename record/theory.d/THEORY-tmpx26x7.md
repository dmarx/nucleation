---
status: Proposed
title: 'Quinn, Abbott, Transtrum, Machta and Sethna call a model sloppy, and its model manifold a hyperribbon, when its Fisher eigenvalues and geodesic widths are both hierarchical, roughly evenly spaced in log over several decades; they present the ubiquity of this shape as empirical, bound it rigorously only for least-squares models smooth in their control variables, hold that it gives a low-dimensional description only where many widths fall below the precision demanded, and say that its explanations in renormalizable physics and in least-squares fitting seem completely different'
promote_when: >-
  Quinn, Wilber, Townsend and Sethna 2019 (LIT-tmpmksrk) is read and
  confirms that the model manifold of a least-squares model meeting the
  review's smoothness condition lies within a hyperellipsoid whose j-th
  axis is bounded by ρ^(−j).
version: 1
tags:
- information-geometry
- model-comparison
- complex-systems
date: '2026-11-22'
source:
- LIT-2958
corroborates:
- CLAIM-813
bears_on:
- QUESTION-517
summary: >-
  The 2023 review of the sloppy-model programme, [LIT-2958](../literature.d/LIT-2958.md), read in
  [NOTE-tmp3keyy](../notes.d/NOTE-tmp3keyy.md). Its sharp edges: "sloppy" needs widths as well as
  eigenvalues to be hierarchical; ΛCDM is sloppy and yet fully determined,
  because sloppiness is low-dimensional only against a demanded precision;
  the rigorous bound is for smooth least-squares models, restated from the
  2019 paper ([LIT-tmpmksrk](../literature.d/LIT-tmpmksrk.md), Deferred); and the review offers no single
  account of why simple effective theories exist. It grounds [CLAIM-820](../claims.d/CLAIM-820.md)
  ([ARG-tmp6xwk9](../arguments.d/ARG-tmp6xwk9.md)) and is drawn on by [TERM-135](../terms.d/TERM-135.md) and [TERM-140](../terms.d/TERM-140.md).
---
<!-- inactive-ok-file: LIT-tmpmksrk ARG-tmp6xwk9 CLAIM-820 CLAIM-813 TERM-135 TERM-140 THEORY-777 — Proposed, Deferred or new; the reading, the work it restates and the entries it bears on -->

# THEORY-tmpx26x7: Quinn, Abbott, Transtrum, Machta and Sethna call a model sloppy, and its model manifold a hyperribbon, when its Fisher eigenvalues and geodesic widths are both hierarchical, roughly evenly spaced in log over several decades; they present the ubiquity of this shape as empirical, bound it rigorously only for least-squares models smooth in their control variables, hold that it gives a low-dimensional description only where many widths fall below the precision demanded, and say that its explanations in renormalizable physics and in least-squares fitting seem completely different

## Source

Quinn, Abbott, Transtrum, Machta and Sethna, "Information geometry for
multiparameter models: New perspectives on the origin of simplicity",
Rep. Prog. Phys. (2023), [LIT-2958](../literature.d/LIT-2958.md), read from the arXiv e-print 2111.07176
in [NOTE-tmp3keyy](../notes.d/NOTE-tmp3keyy.md).

## What was actually shown

- The definition (§2): "We call a model sloppy, and the model manifold a
  hyperribbon, if the parameter-space eigenvalues and prediction-space
  widths are hierarchical: roughly equally spaced in log, spanning several
  decades."
- Empirical ubiquity (§1, "an empirical fact"), from spectra and widths of
  earlier papers.
- A rigorous bound restated, not proved (§3), "for the special case of a
  multiparameter nonlinear least-squares model", resting on "the
  smoothness of the predictions as the experimental controls ... are
  varied": within ε_N of a Vandermonde-skewed parallelepiped, or inside a
  hyperellipsoid with j-th axis bounded by ρ^(−j) (geometric decay, though
  the text calls it "a power law").
- Sloppy is not low-dimensional (§2): only "if many of its widths are
  small compared to the precision of the predictions demanded"; the ΛCDM
  model is sloppy and "all parameters are well determined from the data".
- Two explanations (§8.2): coarse-graining in physics and smoothness in
  least squares; "our explanations for the two seem completely different".

What could have failed: the rates-set-to-one test (§3) could have removed
the spread, making it an artefact of separated scales; it did not ("The
cost Hessian remains sloppy").

## What this does not say

- Not that simple effective theories have one explanation: the review
  says the opposite.
- Not that a sloppy model is low-dimensional, nor that large neural
  networks are sloppy ("We have speculated", §8).
- Not a bound for general probabilistic models: "we do not yet have an
  explanation for this in general, except for ... exponential families"
  (§8.2).

## Connections

Grounds [CLAIM-820](../claims.d/CLAIM-820.md), with the precision qualification ([ARG-tmp6xwk9](../arguments.d/ARG-tmp6xwk9.md)).
Corroborates [CLAIM-813](../claims.d/CLAIM-813.md) (practical vs structural identifiability). Bears on
[QUESTION-517](../questions.d/QUESTION-517.md). Drawn on by [TERM-135](../terms.d/TERM-135.md) and [TERM-140](../terms.d/TERM-140.md). Restates [LIT-1299](../literature.d/LIT-1299.md),
[THEORY-742](THEORY-742.md), [THEORY-774](THEORY-774.md) and [THEORY-777](THEORY-777.md) in §6.
