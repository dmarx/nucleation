---
status: Active
title: 'Granger causality: the past of one series improving the prediction of another''s next value beyond the past of everything else in a stated information set, a predictive relation relative to that set and its lags, and not by itself the effect of an intervention'
version: 1
tags:
- causality
- mathematical-statistics
date: '2026-10-16'
line: formal-apparatus
summary: >-
  The record names Granger causality in its readings of transfer entropy
  ([NOTE-053](../notes.d/NOTE-053.md)), causal emergence ([NOTE-010](../notes.d/NOTE-010.md), [NOTE-726](../notes.d/NOTE-726.md), [NOTE-791](../notes.d/NOTE-791.md)) and IIT
  ([NOTE-122](../notes.d/NOTE-122.md)), always through other authors. This fixes the word: relative
  to an information set, predictive, and interventional only under the
  conditions of [THEORY-tmp4g68i](../theory.d/THEORY-tmp4g68i.md). Defined from Barnett, Barrett and Seth,
  Seth, and Eichler and Didelez; Granger (1969) itself is Unavailable.
used_by:
- CLAIM-tmp6nu4a
- CLAIM-tmpa4kr6
- CLAIM-tmpu9ivq
---

# TERM-tmpq0ms2: Granger causality: the past of one series improving the prediction of another's next value beyond the past of everything else in a stated information set, a predictive relation relative to that set and its lags, and not by itself the effect of an intervention

## Definition

Let X_V be a stationary multivariate time series and A, B disjoint sets
of its components. **X_A Granger-causes X_B relative to X_V** if the past
of X_A improves the prediction of X_B(t + 1) beyond the past of the
other components of V. **Strong** Granger noncausality is the
distributional form: X_B(t + 1) ⊥⊥ X_A's past | X_{V∖A}'s past
(Eichler and Didelez, Def. 4.1, [NOTE-tmpm48uq](../notes.d/NOTE-tmpm48uq.md)). The usual measure is
linear. For a univariate predictee it is the log ratio of residual
variances of the restricted and full regressions. For a multivariate
predictee it is Geweke's log ratio of their determinants
([NOTE-tmp2veo7](../notes.d/NOTE-tmp2veo7.md), Eqs. 8–9).

Three things are always relative and should be stated with it:

1. **The information set V.** Adding or removing a series can create or
   remove a Granger-causal relation ([NOTE-tmpm48uq](../notes.d/NOTE-tmpm48uq.md), Example 4.7).
2. **The lags and the sampling interval.** An influence faster than one
   sampling step shows as contemporaneous dependence, not as Granger
   causation ([CLAIM-tmp6nu4a](../claims.d/CLAIM-tmp6nu4a.md)).
3. **The model class**, for the measured quantity. A linear Granger
   statistic is blind to dependence a linear predictor cannot use (Seth,
   §2.3, [NOTE-tmp5fslk](../notes.d/NOTE-tmp5fslk.md)).

## What it must not be confused with

- **Intervention (Pearl-type) causation.** The effect on X_B of setting
  X_A. Granger noncausality implies its absence only under Eichler and
  Didelez's conditions ([THEORY-tmp4g68i](../theory.d/THEORY-tmp4g68i.md)). A Granger-causal relation is
  at most "potentially causal".
- **Transfer entropy.** H(X_B(t + 1) | rest's past) − H(X_B(t + 1) | all
  past). It is the same quantity, halved, for jointly Gaussian processes
  ([THEORY-tmp0xaeq](../theory.d/THEORY-tmp0xaeq.md)). In general it is the likelihood-ratio limit of a
  well-specified model ([THEORY-641](../theory.d/THEORY-641.md)). Granger causality is the linear
  case, not an approximation to it, when the data are Gaussian.
- **Directed information** (Massey). For Gaussian data Granger causality
  corresponds to its lagged part, full-history transfer entropy; the
  instantaneous part, which Geweke's measure of instantaneous feedback
  tracks, is outside it ([THEORY-tmppkvwa](../theory.d/THEORY-tmppkvwa.md), [TERM-tmpj9z04](TERM-tmpj9z04.md)).
- **Interventional information flow** (Ay and Polani), the
  information-theoretic counterpart of an intervention effect
  ([THEORY-tmpkovi2](../theory.d/THEORY-tmpkovi2.md)).
- **Downward (Granger) causation** in Seth's sense: Granger causation from
  a macro variable to its micro variables. A use of the term, not a kind
  of causation ([CLAIM-tmpa4kr6](../claims.d/CLAIM-tmpa4kr6.md)).
- **Granger's own definition** (1969, [LIT-tmppqyor](../literature.d/LIT-tmppqyor.md)), which the record has
  not read. The citing works agree that it is predictive and relative to
  the relevant information. The record's definition is theirs.
