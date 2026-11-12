---
status: Proposed
title: 'Sikder (2026) argues that a point estimate of an error-rate gap does not certify a classifier as fair, and offers FairCert, which certifies that every pairwise FPR (or TPR) gap across protected and intersectional groups is within a tolerance at a stated confidence using Clopper-Pearson intervals with a Bonferroni correction; on benchmark data the certificate passes for single sensitive attributes but fails for their intersections on Credit Default, and large-language-model classifiers'' gaps vary sharply by domain and prompt.'
version: 1
source:
- LIT-tmppyl6o
bears_on:
- QUESTION-tmpuftum
tags:
- mathematical-statistics
- society-and-governance
date: '2026-11-12'
promote_when: >-
  an independent application of finite-sample error-rate certificates finds
  a classifier certified on single attributes but not on intersectional
  groups, or an LLM classifier's certified gap differing materially across
  domains.
summary: >-
  Md Fahim Sikder, read in NOTE-tmppe0ip (Read). FairCert is a black-box
  audit pipeline that turns per-group false-positive-rate (FPR) and
  true-positive-rate (TPR) gaps into finite-sample certificates. Five
  stages: a stratified split with a walled-off 15% audit set; LLM-guided
  discovery of candidate intersectional subgroups from aggregate training
  statistics (hypotheses), confirmed on the disjoint audit set; per-group
  error rates of the classifier's predictions; a certificate built from
  Clopper-Pearson exact intervals per group with a Bonferroni correction
  over K groups, which bounds the worst pairwise gap with probability at
  least 1−δ and passes if the bound is within tolerance ε; and, for
  failures, per-group threshold calibration with the TPR cost reported, plus
  a structured EU AI Act-oriented report.
---

# THEORY-tmp76i78: Sikder (2026) argues that a point estimate of an error-rate gap does not certify a classifier as fair, and offers FairCert, which certifies that every pairwise FPR (or TPR) gap across protected and intersectional groups is within a tolerance at a stated confidence using Clopper-Pearson intervals with a Bonferroni correction; on benchmark data the certificate passes for single sensitive attributes but fails for their intersections on Credit Default, and large-language-model classifiers' gaps vary sharply by domain and prompt.

## The account

Sikder (2026) argues that a point estimate of an error-rate gap does not certify a classifier as fair, and offers FairCert, which certifies that every pairwise FPR (or TPR) gap across protected and intersectional groups is within a tolerance at a stated confidence using Clopper-Pearson intervals with a Bonferroni correction; on benchmark data the certificate passes for single sensitive attributes but fails for their intersections on Credit Default, and large-language-model classifiers' gaps vary sharply by domain and prompt.

## Evidence

The reading in NOTE-tmppe0ip; its key results are quoted there with locations.
