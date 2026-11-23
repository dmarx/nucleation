---
number: 191
status: Open
formerly:
- LEAD-tmpycitu
title: 'Compare a sheaf route that allows signalling with Contextuality-by-Default 2.0 on one signalling data set, where their verdicts diverge'
version: 1
stage: idea
priority: medium
method:
- formal
- empirical
tags:
- contextuality
- philosophy-of-language
date: '2026-11-19'
line:
- pragmatic-transport
- formal-apparatus
advances:
- CLAIM-037
summary: >-
  Named in [CLAIM-037](../claims.d/CLAIM-037.md). Filed by the backlog audit of 2026-11-19.
---
<!-- inactive-ok-file: CLAIM-037 — Proposed; cited in the backlog audit of 2026-11-19 -->
<!-- inactive-ok-file: CASE-tmpskejj CLAIM-tmptzmky CLAIM-tmprfjkk CLAIM-tmprq0nb CLAIM-tmpzvz98 — new; filed by the lead run of 2026-11-23 -->

# LEAD-191: Compare a sheaf route that allows signalling with Contextuality-by-Default 2.0 on one signalling data set, where their verdicts diverge

## What it would do

Reanalyse [LIT-844](../literature.d/LIT-844.md)'s data by both routes and say which verdict is right and
why.

Where the record names it:

- [CLAIM-037](../claims.d/CLAIM-037.md): "It goes Active on a comparison of a sheaf route with CbD 2.0
  on one signalling data set."

## What would count

The comparison is what [CLAIM-037](../claims.d/CLAIM-037.md) names as promoting it.

## Note of 2026-11-23: run, and what remains

**The full reanalysis was not possible.** [LIT-844](../literature.d/LIT-844.md) publishes aggregate
counts and the (SF, Δ) of 25 printed instances. It does not publish the
per-instance BERT probabilities.

- **The repository.** The one its §9 names held only a README on
  2026-11-23.
- **The release page** returned 403 and was not retried.
- **Zenodo** has no deposit.

**What was done instead.** On this support both verdicts are functions of
(SF, Δ), so the published figures were reanalysed by both routes, the
sheaf test [LIT-844](../literature.d/LIT-844.md) applies and CbD 2.0. Linear programs and 249 tests are
in scratch/studies/lead-191/, and [CASE-tmpskejj](../cases.d/CASE-tmpskejj.md) reports the run.

**Results.** The sheaf test is the signalling threshold SF < 1/6, since
CF is 1 on every model with this support. CbD 2.0 is Δ < 2, and the first
set lies inside the second. The published counts then fix the divergence:
36,861,830 instances (70.9%) are CbD-contextual and not sheaf-contextual,
and none diverge the other way. Read as "the no-signalling part is
contextual", the sheaf route is SF < 1, which calls at least 71.1%
contextual. [CLAIM-tmptzmky](../claims.d/CLAIM-tmptzmky.md) (demonstrated) states this.

**Which verdict is right.** Three alternative readings are filed. The
lead worker leans to the first:

- [CLAIM-tmprfjkk](../claims.d/CLAIM-tmprfjkk.md): the data cannot discriminate, because the support is
  fixed and every verdict is a signalling threshold;
- [CLAIM-tmprq0nb](../claims.d/CLAIM-tmprq0nb.md): only CbD gives a single verdict, which corroborates
  [CLAIM-037](../claims.d/CLAIM-037.md);
- [CLAIM-tmpzvz98](../claims.d/CLAIM-tmpzvz98.md), a counter: on the reading of signalling as error, the
  sheaf figure is the defensible one, which objects to [CLAIM-037](../claims.d/CLAIM-037.md).

**What remains.**

- The per-instance data, if the authors release them. That would allow
  the distance readings to be counted on the real instances.
- A reading of Vallée et al., the source of the corrected criterion.
- A comparison on a data set whose support is measured rather than
  stipulated, which the first alternative says is the one that could
  discriminate.

No status or stage was changed.
