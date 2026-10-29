---
status: Active
title: 'A proposed study: direct and relay translations of one set of source utterances through three languages, to find whether agreement between the routes, the task-relative loss on each route, and the preservation of response to later framing come apart, and whether correspondences fitted between the communities'' response structures on some items predict receivers'' judgements on held-out items, translators and situations'
version: 1
standing: stipulated
kind: proposed-study
tags:
- translation
- pragmatics
- psychometrics
date: '2026-10-29'
illustrates:
- CLAIM-tmpgwud2
- CLAIM-202
- CLAIM-257
variant_of:
- CASE-055
line: pragmatic-transport
summary: >-
  Put together from A4 §6, A5 §5 and A6's synthesis of the exchange
  "Paper assessment" (2026-10-28 to 29), which proposed carrying
  [LIT-tmpr8qf7](../literature.d/LIT-tmpr8qf7.md)'s comparison of alternative paths into [CASE-055](CASE-055.md) as
  independent translation routes. It adds to [CASE-055](CASE-055.md) a relay arm, a
  path-discrepancy readout set beside the task loss, two negative
  controls, and an arm that fits correspondences between the
  communities' response matrices and scores them on held-out data. Not
  run; every margin is left to a preregistration.
---
<!-- inactive-ok-file: CLAIM-202 CLAIM-257 CLAIM-259 CLAIM-135 — Proposed; the record's theses and measures this design would test, cited as open -->

# CASE-tmph0fxi: A proposed study: direct and relay translations of one set of source utterances through three languages, to find whether agreement between the routes, the task-relative loss on each route, and the preservation of response to later framing come apart, and whether correspondences fitted between the communities' response structures on some items predict receivers' judgements on held-out items, translators and situations

## The design

[CASE-055](CASE-055.md) with a third language and a second route. Its Stage 0
(measurement), its named receiver populations, its criterion (choice of
act and of continuation under stated tasks) and its rule that predictors
are rated by other raters than those supplying the criterion all carry
over unchanged.

**Items.** Utterances whose pragmatic effect can be separated from their
content: requests, promises against predictions, honorific and T/V
choices, implicatures, and pragmatic explicitations of the kind PETra
annotates ([LIT-tmp1n8bp](../literature.d/LIT-tmp1n8bp.md)). VakyArth's items ([LIT-tmpog7aw](../literature.d/LIT-tmpog7aw.md)) pair translation
with pragmatic inference on the same material, for its four Indic
languages.

**Routes.** For each source item in language A, a direct translation into
C and a relay through B, by translators assigned independently and
working to stated briefs.

**Readouts, on the same items.**

| readout | what it measures |
|---|---|
| static preservation | proposition, act, stance, politeness, as [CASE-055](CASE-055.md) rates them |
| dynamic preservation | response to a later framing or continuation ([CLAIM-202](../claims.d/CLAIM-202.md)) |
| path discrepancy | distance between the direct and relay routes' target response distributions |
| task loss | [CLAIM-259](../claims.d/CLAIM-259.md)'s directed decision term on declared tasks, per route |
| change of cover | target questions the source leaves open, asked of source readers too ([CLAIM-257](../claims.d/CLAIM-257.md)) |

**Correspondence arm.** Build each community's response matrix R(u, q):
utterances by pragmatic probes, from its own readers. Fit
correspondences on training items by: orthogonal Procrustes on embedded
responses; unrestricted linear maps; stochastic kernels; Gromov–Wasserstein
([LIT-tmpprsxm](../literature.d/LIT-tmpprsxm.md)); fused GW with independently validated anchor items, varying
the weight on structure ([LIT-tmpjs7kp](../literature.d/LIT-tmpjs7kp.md)); and co-optimal transport, which
matches utterances and probes jointly ([LIT-tmpbnbe3](../literature.d/LIT-tmpbnbe3.md)). Score each on held-out
items, translators and, where possible, situations. Fit each edge
independently, so that the composed A→B→C map can disagree with the A→C
map.

**Controls.**

- **A degenerate translator** that renders every item as one generic
  expression. It should reach low path discrepancy and fail the task
  readouts ([CLAIM-tmpgwud2](../claims.d/CLAIM-tmpgwud2.md)).
- **A shared-provenance pair**: two routes through the same intermediate
  translation or translator, to estimate how much agreement between routes
  shared provenance alone explains.
- **A flipped distinction**: formal and informal address exchanged with
  proposition kept, to test that the readouts see a change of effect and
  not only of wording.
- **Baselines** a transport account must beat: static pragmatic
  similarity, xCOMET ([LIT-tmplu4ga](../literature.d/LIT-tmplu4ga.md)), and a supervised predictor of act
  labels. [CASE-071](CASE-071.md) shows why the metric is a baseline, not a criterion.

## What would be measured, and the main threat

The main test is incremental prediction of held-out receiver choices from
path discrepancy, dynamic preservation and the fitted correspondences,
over the static profile and the baselines. The main threat is
measurement. PragSim's judges agreed at a mean correlation of 0.45
([LIT-tmphdoda](../literature.d/LIT-tmphdoda.md)), so Stage 0's reliability targets must be met before any
transport readout is interpreted. A second threat is identification. GW
and co-optimal transport can swap symmetric categories, or swap utterances
and probes together, at equal cost, so the anchors must be validated
independently of the fit.

## What each outcome would show

- **Path discrepancy and task loss uncorrelated across routes**: the
  independence [CLAIM-tmpgwud2](../claims.d/CLAIM-tmpgwud2.md) constructs also holds of real translations.
- **Dynamic preservation predicting choices the static profile does not**:
  support for [CLAIM-202](../claims.d/CLAIM-202.md)'s measured structure beyond the static profile.
- **Anchored fused GW or co-optimal transport beating orthogonal maps on
  held-out items**: evidence that the right transports are lossy and not
  invertible, as [CLAIM-098](../claims.d/CLAIM-098.md) holds, and against carrying [LIT-tmpr8qf7](../literature.d/LIT-tmpr8qf7.md)'s O(d)
  machinery over to translation.
- **No transport readout beating the baselines**: the pragmatic point may
  stand without the transport mathematics.

Stipulated, it shows nothing yet. Run, it could not show that a fitted
correspondence constitutes a communicative kind ([CLAIM-135](../claims.d/CLAIM-135.md)), only that it
predicts.
