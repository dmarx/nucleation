---
# Don't copy this file by hand — run `luria new theory`, which assigns the
# code and fills in what a machine can compute.
#
# A theory is a claim about WHY something happens, or about what is true of
# these systems. State it as a finding, not as an instruction: "Batch
# normalization helps by smoothing the optimization landscape" rather than
# "Use batch normalization". If what you are about to write tells the reader
# what to do in machine learning, it is a practice, and it belongs in the
# Anthology of the SOTA (ANTH-ADR-031).

# Active | Proposed | Deferred | Superseded | Rejected, optionally " — note".
# What each one means here is in luria.yaml, and it is NOT what the same word
# means on a practice: this status says whether the record believes the
# ACCOUNT, and an explanation can be `Rejected` while the thing it explained
# goes on working exactly as well as it ever did.
status: Proposed

# REQUIRED while the status is Proposed or Deferred; delete it when the
# explanation goes Active. What would settle it — a KIND of result, not a
# quantity of them (ANTH-ADR-014). An explanation that cannot say what would show
# it wrong is a story, and this field is where that shows up.
promote_when: >-
  An audit of the extracted edges themselves against human labels, by
  experts or by the papers' authors, on a sample drawn by decade, field
  and method, at the baseline EO ≥ 4. Promoted if edge-level precision and
  recall for the causal label are high and roughly stable across decades,
  so that the rise cannot be laid to modern papers naming their designs
  more explicitly. Refuted if the causal label's precision on 1980s and
  1990s papers is low or its recall rises sharply with time. More runs of
  the same pipeline, agreement between its passes, or agreement with a
  trend measured by a similar design-keyword method cannot settle it.

# The claim. Repeat it as the body's `# THEORY-tmpx9ksh:` heading; the lint checks
# that the two agree.
title: 'Economics working papers increasingly back their claims with design-based identification: in NBER and CEPR working papers the share of claims supported by difference-in-differences, instrumental variables, an RCT, regression discontinuity or synthetic control rose about fourfold from 1990 to 2020'

version: 1

# One or more topics from luria.yaml, primary first — the same table the
# reading list uses. Take the topic of what the account is about.
tags:
- social-science
- causality
- philosophy-of-science

date: '2026-10-20'

# There is deliberately no `published:` line. It is DERIVED from the first
# entry in `source:` below, and writing it down is a lint violation, because
# the value has one home and this is not it.

# REQUIRED, and a LIST. The papers this account rests on, primary first. An
# explanation with no paper behind it is a hunch, and the lint will say so.
source:
- LIT-079

# What the index table shows.
summary: >-
  Garg and Fetzer (2024; arXiv v2 2026), [LIT-079](../literature.d/LIT-079.md), read in full in [NOTE-083](../notes.d/NOTE-083.md),
  read the rise in their extraction's design-backed share as a change in
  economics: "economic papers have increasingly incorporated causal
  inference methods to substantiate their claims over the past three
  decades". The record holds as shown, in [THEORY-674](THEORY-674.md), only the extraction's
  series, whose edges were never checked against human labels and whose
  per-decade slope nearly vanishes with method-mix and graph-volume
  controls. This is the paper's reading, filed under [ADR-047](../decisions.d/ADR-047.md) v4 when the
  narrowing dropped it.
extends:
- THEORY-674
---

<!-- inactive-ok-file: LIT-079 — Proposed by its close reading for edges never validated against human labels; the only source, and that limit is why this account is Proposed -->
# THEORY-tmpx9ksh: Economics working papers increasingly back their claims with design-based identification: in NBER and CEPR working papers the share of claims supported by difference-in-differences, instrumental variables, an RCT, regression discontinuity or synthetic control rose about fourfold from 1990 to 2020

## Source

Prashant Garg and Thiemo Fetzer, "Causal Claims in Economics" (OSF 2024;
arXiv v2, February 2026), [LIT-079](../literature.d/LIT-079.md), read in full in [NOTE-083](../notes.d/NOTE-083.md). The claim is
the paper's §3 reading of its own series: "This upward trend indicates that
economic papers have increasingly incorporated causal inference methods to
substantiate their claims over the past three decades."

## What this asserts

That the rise from 7.7% (1990) to 31.7% (2020) in the share of extracted
edges labelled design-backed is a rise in what economics papers actually
claim on design-based evidence, by field roughly as the paper reports
(Health, Urban and Development highest after 2000, Macro lowest), and not an
artefact of how a language model reads older and newer papers.

## What the record holds toward it

[THEORY-674](THEORY-674.md) (Active) holds the series as the extraction's output. Its
direction is robust to the edge-overlap threshold; its level is not; and the
per-decade slope falls from +0.0187 to +0.0011 once method mix and graph
volume are controlled. Paper-level method labels agree with Goldsmith-Pinkham
(2024) on the field ordering. No edge was checked against a human label, and
the paper-level RCT label reaches F1 about 0.03.

## What would confirm or reject it

The promote_when, carried over unchanged from [THEORY-674](THEORY-674.md): an edge-level
audit against human labels on a sample drawn by decade, field and method.
High and stable precision and recall for the causal label would confirm it;
low precision on 1980s and 1990s papers, or recall rising sharply with time,
would show the rise is in the extractor.

## What this does not say

- That design-based claims are correct, or better identified than the
  claims they replaced; the pipeline records what papers claim.
- That causal claims are rewarded with top-five publication; that is a
  conditional association in the paper and is not part of this claim.
