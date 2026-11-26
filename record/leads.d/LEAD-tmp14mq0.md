---
status: Open
title: "Map the record's claims in a stability-generativity phase space, prose stability against new structure formed around each claim, at matched age, and test whether the regimes the map shows are distinguishable and stable under reasonable choices of measure"
version: 1
history:
- version: 1
  date: '2026-11-26'
  note: >-
    Filed from A34's second pilot in the exchange "Alignment consequences
    brainstorm" (ChatGPT, 2026-11-26), which A pairs with the first as its
    recommended first experiment and the owner has asked to start. The
    measures, controls and criteria are the assistant's (Claude, in this
    session).
stage: costed
method:
- empirical
tags:
- individuation
- design-rationale
- epistemology
date: '2026-11-26'
line:
- record-as-apparatus
- nucleating-argument
advances:
- CLAIM-tmpk015q
- CLAIM-tmp4fc0k
- QUESTION-038
presupposes:
- LEAD-tmpn6mi2
summary: >-
  A34: "Use the temporal data to classify entries according to how much
  they change and how much development occurs around them", with "a
  scatter plot of the claim corpus, with drill-down into representative
  entries and their histories" as the deliverable. Its research payoff is
  a test of [CLAIM-tmpk015q](../claims.d/CLAIM-tmpk015q.md) (H1); its practical payoff is to tell "mature
  knowledge worth condensing from neglected knowledge worth reviewing".
  A33 §5 gives the four quadrants and §14 the idea of finding regimes
  rather than drawing them. The design must control for the coupling
  [CLAIM-tmp4fc0k](../claims.d/CLAIM-tmp4fc0k.md) describes, since on this record reliance draws revision.
  The pilot is A's; the measures, controls and criteria are the
  assistant's (Claude, in this session), and adopting them is the owner's
  call.
---
<!-- inactive-ok-file: CLAIM-tmpk015q CLAIM-tmp4fc0k CLAIM-768 CASE-307 — Proposed; the hypothesis tested, the caution it must control for and the entries it is read against, cited on 2026-11-26 -->

# LEAD-tmp14mq0: Map the record's claims in a stability-generativity phase space, prose stability against new structure formed around each claim, at matched age, and test whether the regimes the map shows are distinguishable and stable under reasonable choices of measure

## The measures

From [LEAD-tmpn6mi2](LEAD-tmpn6mi2.md)'s profiles, for every claim alive at each weekly
snapshot date `t`:

- **Prose stability** (x): the claim's substantive-revision intensity at
  τ = 30 days, negated, so that higher is more stable. A second form, days
  since the last substantive revision, is reported beside it.
- **Generativity** (y), A33 §7's flow, not its stock: the new structure
  formed around the claim in the 30 days before `t`. Primary: new incoming
  `rests_on` and `grounds`. Secondary, reported separately by kind (A33's
  conceptual, epistemic, investigative and integrative generativity): new
  TERMs it uses or that cite it, new ARGs concluding it and new objections,
  new LEADs and QUESTIONs on it, new SYNTHESIS integrations.
- **Centrality**, the stock: total incoming reliance at `t`. A covariate,
  not an axis.

## The controls

- **Age.** Every comparison within age bins ([CASE-307](../cases.d/CASE-307.md)'s: 0–1, 1–3, 3–7,
  7–14, 14–28 and 28 or more days), and the plot drawn both raw and with
  each axis as a residual on age bin.
- **Recheck revisions** ([CLAIM-tmp4fc0k](../claims.d/CLAIM-tmp4fc0k.md)). Revisions within 24 hours of a new
  incoming edge are counted apart, and the map is drawn with and without
  them.
- **Filing-day burst and bulk commits.** The first day of each claim
  dropped, and commits touching more than 20 claims dropped, as [CASE-307](../cases.d/CASE-307.md)'s
  sensitivities did.

## The deliverables

1. The scatter at the latest snapshot and at three earlier ones, with A33's
   quadrants split at the medians and labelled as A33 labels them.
2. For each quadrant, the three claims nearest its centre with their event
   histories, for drill-down.
3. The regimes found without the quadrants: Gaussian mixtures on the two
   standardized axes, and on A33 §14's vector (revision intensity, incoming
   reliance rate, outgoing exploration rate, neighbourhood activity,
   synthesis mediation, standing volatility), for k = 1 to 6, chosen by BIC.

## What would count for and against [CLAIM-tmpk015q](../claims.d/CLAIM-tmpk015q.md)

For, both of:

- **Distinguishable.** A model with k ≥ 2 beats k = 1 by more than 10 in
  BIC, and the assignment is stable: adjusted Rand index of at least 0.6
  between the main run and each variant (lenient or strict classifier, τ of
  7, 14 or 30, recheck revisions in or out, bulk commits in or out).
- **Predictive.** A claim's regime at `t` improves the prediction of its
  next 30 days (any new incoming reliance; any substantive revision;
  supersession or rejection) over a model with age bin and incoming count
  alone, fitted on snapshots before a cut date and scored after it, by at
  least 0.05 in AUC on one outcome or more.

Against: k = 1 preferred; an adjusted Rand index below 0.3 for any one
variant; or no predictive gain on any outcome. Any of these meets
[CLAIM-tmpk015q](../claims.d/CLAIM-tmpk015q.md)'s defeater for this record at its present age. Between the
two (regimes stable but not predictive, or the reverse) the result is
reported as it falls and the claim is not moved.

For the practical payoff: ten claims from the established-anchor quadrant
and ten from the dormant one, shuffled, are read by the owner or a worker
blind to the quadrant and marked "mature" or "neglected". The quadrants
discriminate if at least 14 of 20 marks agree with them.

## What it cannot show

Why a claim settled ([CLAIM-768](../claims.d/CLAIM-768.md): settling does not show what stopped an
entry; note of 2026-11-26 there). Whether a regime is good (A33: the
locations "are descriptive, not judgments of epistemic worth"). And
whether a thin anchor quadrant says anything about individuation, since
on this record reliance draws revision ([CLAIM-tmp4fc0k](../claims.d/CLAIM-tmp4fc0k.md)): the quadrant can
only be read after the controls.

## Cost

Low once [LEAD-tmpn6mi2](LEAD-tmpn6mi2.md)'s profiles exist: a script and a plot, half a day,
plus the blind reading of twenty claims.
