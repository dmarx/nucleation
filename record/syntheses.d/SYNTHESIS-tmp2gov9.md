---
status: Proposed
title: 'Granger causality and transfer entropy are predictive quantities relative to a stated information set: complete measurement is not enough for an interventional reading, Granger causation from a macro variable to its micro base has no intervention to stand for, transfer entropy adds synergy to unique information and so is not flow from the source alone, and a ΦID verdict on three or more parts rests on which axiom of redundancy is dropped'
version: 1
defeated_if: >-
  A component misstated or misattributed here; an in-force component of
  the directed-information part of the formal-apparatus line left out
  without a reason given; or a link this account states that no
  component states. Its standing is its components': a component retired
  or demoted takes its clause with it, and nothing here holds the clause
  up.
tags:
- causality
- information-theory
- mathematical-statistics
date: '2026-11-11'
line:
- formal-apparatus
integrates:
- TERM-058
- TERM-057
- CLAIM-333
- CLAIM-334
- CLAIM-335
- CLAIM-343
---
<!-- inactive-ok-file: ADR-075 THEORY-497 — Proposed; components, decisions and accounts cited with their standing -->
<!-- inactive-ok-file: SYNTHESIS-tmpa7ef9 SYNTHESIS-tmpe15k3 — Proposed; cited with its standing -->

# SYNTHESIS-tmp2gov9: Granger causality and transfer entropy are predictive quantities relative to a stated information set: complete measurement is not enough for an interventional reading, Granger causation from a macro variable to its micro base has no intervention to stand for, transfer entropy adds synergy to unique information and so is not flow from the source alone, and a ΦID verdict on three or more parts rests on which axiom of redundancy is dropped

*A part account of the formal-apparatus line: one of the line's eleven
small clusters, six entries, all first in formal-apparatus, filed from
the readings of Granger causality, transfer entropy and partial
information decomposition in October 2026. The line's account is built
over it and its sibling parts. No other account integrates any of them.*

## The account

- **The words.** TERM-058 (the record's, defined from Barnett, Barrett
  and Seth, Seth, and Eichler and Didelez; Active): Granger causality is
  predictive and relative to an information set, its lags and its model
  class, and "not by itself the effect of an intervention". TERM-057 (the
  record's, from Schreiber; Active): transfer entropy is
  I(X_{t+1}; Y_t^{(l)} | X_t^{(k)}), stated with k, l, the conditioning
  set and the estimator, "not a measure of information flow and not an
  intervention effect". For jointly Gaussian processes Geweke's Granger
  causality is twice the transfer entropy (TERM-057, TERM-058).
- **Measurement is not enough.** CLAIM-333 (the record's answer to the
  ΦID review's C5 as NOTE-010 records it; thesis, demonstrated, Active):
  measuring every relevant variable is necessary but not sufficient for
  an interventional reading. A two-series process with nothing hidden is
  Granger-noncausal from a to b, yet setting a(t) changes the mean of
  b(t + 1) by ργ. Under Eichler and Didelez's conditions "the two
  analyses agree on zero effects and share an estimand. They are still not
  one analysis."
- **Downward Granger causation.** CLAIM-334 (the record's; disclaimed,
  demonstrated, Active): Seth's Granger causation from a macro variable
  to the micro variables it supervenes on is not evidence of an
  intervention effect, because supervenience leaves no intervention on
  the macro variable that holds its base fixed. "Here it fails for a
  different reason than the sampling step: the intervention is ruled out
  by the definition of M, not by the data."
- **Transfer entropy is not flow.** CLAIM-335 (the record's position;
  thesis, demonstrated, Active, version 3): as a conditional mutual
  information, transfer entropy is unique plus synergistic information
  under any decomposition meeting the consistency equations, so it can
  credit a source with a bit carried only jointly and read zero from
  sources that jointly fix the target. Its summary: "This is a different
  failure from CLAIM-333's, prediction against intervention."
- **Three or more parts.** CLAIM-343 (the record's answer to the gap left
  by the PID filing; thesis, demonstrated, Active): on the Williams–Beer
  lattice from three sources up, no redundancy function satisfies both
  the identity axiom and nonnegative atoms, so "A ΦID verdict on three or
  more parts therefore rests on which axiom the analyst gave up." It
  leaves two-part ΦID untouched.

## The components

- TERM-058, the record's, Active; formal-apparatus only.
- TERM-057, the record's, Active; formal-apparatus only.
- CLAIM-333, the record's, thesis, demonstrated, Active; formal-apparatus
  only; uses TERM-058; grounds on THEORY-704; complements CLAIM-335.
- CLAIM-334, the record's, disclaimed, demonstrated, Active;
  formal-apparatus only; rests on CLAIM-333; uses TERM-058; grounds on
  LIT-1170 and THEORY-704.
- CLAIM-335, the record's, thesis, demonstrated, Active; formal-apparatus
  only; uses TERM-057 and TERM-058; complements CLAIM-333 and CLAIM-343.
- CLAIM-343, the record's, thesis, demonstrated, Active; formal-apparatus
  only; complements CLAIM-335; grounds on THEORY-713 and THEORY-714.

## Links the components state, and where

Nine pairs are linked, all inside the cluster:

- **The terms and the claims.** CLAIM-333 and CLAIM-334 use TERM-058;
  CLAIM-335 uses both terms. TERM-058's "What it must not be confused
  with" names CLAIM-333 for the sampling interval and CLAIM-334 for
  downward Granger causation, "A use of the term, not a kind of
  causation". TERM-057 names CLAIM-335 for flow, and "What CLAIM-333 says
  of Granger causality and interventions holds for transfer entropy too."
  TERM-057 and TERM-058 name each other.
- **Two failures, kept apart.** CLAIM-333 and CLAIM-335 complement each
  other. CLAIM-335's "What it does not say": "Prediction against
  intervention is CLAIM-333's separate question." CLAIM-333's
  counterexample has zero full-history transfer entropy and positive
  directed information, all in the instantaneous term, "That term is what
  Granger causality and transfer entropy leave out."
- **Supervenience as a second route.** CLAIM-334 rests on CLAIM-333: the
  step from complete measurement to an interventional reading "is exactly
  what CLAIM-333 denies in general".
- **Two parts and more.** CLAIM-343 and CLAIM-335 complement each other.
  CLAIM-343's "What it does not say": two-part ΦID is untouched, and "the
  record's transfer-entropy examples give the same values under all four
  two-source measures" (CLAIM-335).

## Links to other parts, stated

The community map found none; two mentions reach the cluster from other
parts:

- **To the effective-description account (SYNTHESIS-tmpa7ef9).** QUESTION-252 lists CLAIM-343 as a
  precedent: "Axiom-independence precedents: CLAIM-343 and CLAIM-353."
- **To the intervention account (SYNTHESIS-tmpe15k3).** TERM-068 defines informational
  closure as "transfer entropy from the micro past with Z's whole history
  and no environment (TERM-057 with k and l unbounded)".

CLAIM-335's note of 2026-10-21 and TERM-068 both cite THEORY-820, the
three-bit chain, outside the line. CLAIM-333, CLAIM-334 and CLAIM-343
leave NOTE-010's C4 and THEORY-497's interventional reading of ΦID's
atoms open.

## Where else these entries are integrated

Nowhere. All six are in formal-apparatus only.

## Not stated on the record

Tested by ADR-075's step 5 at this review and not filed:

- **Transfer entropy is neither necessary nor sufficient for influence
  from one source.** CLAIM-333's process has zero transfer entropy and an
  intervention effect; CLAIM-335's first example has a full bit of
  transfer entropy and no unique information. Already stated: TERM-057
  carries CLAIM-333's point over to transfer entropy, and CLAIM-335 states
  its own half. Nothing new.
- **A ΦID downward-causation verdict on three or more parts inherits the
  axiom choice.** CLAIM-334 sets ΦID's downward atom aside; CLAIM-343
  says any ΦID verdict on three or more parts rests on the axiom dropped,
  which covers the downward atom. Held by CLAIM-343. Nothing new.

## What it does not say

- That Granger analysis or transfer entropy is useless; CLAIM-333 and
  CLAIM-335 both disclaim it.
- Whether ΦID's quantities are interventional (NOTE-010's C4, THEORY-497).
