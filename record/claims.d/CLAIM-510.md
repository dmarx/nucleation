---
number: 510
status: Proposed
formerly:
- CLAIM-tmp665pn
title: 'Measurement can establish, and not only estimate, a correspondence among local descriptions: some correspondences that measurement estimates can be checked against evidence the measurement did not itself produce'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  That the correspondences measurement estimates cannot be checked
  against anything but their own consistency, so that "establish" is too
  strong: an argument that every check on a measured correspondence is a
  consistency check (around cycles, of a residual, under a noise model) or
  presupposes the correspondence it checks. The cases the record holds do
  not meet this. Singer's are validated only by cycle consistency under a
  noise model (NOTE-1224), and Robinson's are trusted (NOTE-1221). They
  show that no case is held, not that none can be.
tags:
- philosophy-of-science
- contextuality
- complex-systems
date: '2026-10-30'
line:
- distributed-agency
complements:
- CLAIM-471
- CLAIM-143
summary: >-
  The clause [CLAIM-471](CLAIM-471.md) dropped when the twenty-fourth status review
  narrowed "establish" to "estimate" ([ADR-047](../decisions.d/ADR-047.md), kind 2). It is the record's
  own wording, and no source asserts it. [CLAIM-143](CLAIM-143.md)'s order of tests needs
  it to be possible, since the order asks for correspondences that are
  independently validated. No held case meets it yet.
---
<!-- inactive-ok-file: CASE-tmp33vf4 CLAIM-tmpvqmwc — new, on pull request #740 (LEAD-177), not yet on staging; cited as a candidate for this claim's condition, and the citation depends on #740 merging -->
<!-- inactive-ok-file: CASE-333 — Proposed; filed from LEAD-098's run of 2026-11-22, cited as a partial case -->
<!-- inactive-ok-file: CASE-tmp17zl1 NOTE-tmp2d035 THEORY-tmp5gcq1 — new; the case LEAD-164 filed and its reading -->

# CLAIM-510: Measurement can establish, and not only estimate, a correspondence among local descriptions: some correspondences that measurement estimates can be checked against evidence the measurement did not itself produce

## The claim

[CLAIM-471](CLAIM-471.md) version 4 said measurement "can establish correspondences among
local descriptions". The twenty-fourth status review narrowed that to
"estimate", because nothing the record holds goes further. This entry keeps
the stronger form as a thesis: for some measured correspondences there is
evidence, not produced by the measurement, against which the estimate can
be checked. That is what [CLAIM-143](CLAIM-143.md)'s proviso asks for ("independently
validated and not admitted because they remove the disagreement"). It is
also what [CLAIM-342](CLAIM-342.md) asks of any loop: evidence whose arrival or scoring
does not pass through the interpretation it tests.

## Where it stands

- Singer ([NOTE-1224](../notes.d/NOTE-1224.md)) estimates relative angles and validates them jointly,
  by consistency around cycles, under a noise model.
- Hansen and Ghrist ([NOTE-1233](../notes.d/NOTE-1233.md), §8.7) adjust measured relationships until
  a section exists.
- Robinson ([NOTE-1221](../notes.d/NOTE-1221.md)) trusts his maps, and in his Case 2 a sensor bias
  cannot be told apart from an error in the maps.

None of them checks a correspondence against independent evidence. A held
case would promote this claim. An example is clock offsets estimated by
signal exchange and then checked against a co-located reference that took
no part in the exchange. An argument that every check reduces to
consistency would defeat it. The pragmatic-transport form of the question
is [QUESTION-005](../questions.d/QUESTION-005.md).

## Note of 2026-10-30: what holds it back

No held case checks a measured correspondence against evidence the
measurement did not produce: Singer's are validated only by cycle
consistency under a noise model ([NOTE-1224](../notes.d/NOTE-1224.md)), Robinson's are trusted
([NOTE-1221](../notes.d/NOTE-1221.md)), and Hansen and Ghrist adjust relationships until a section
exists ([NOTE-1233](../notes.d/NOTE-1233.md)). One such case would promote it.

## Note of 2026-11-22: three candidate cases, under three readings of the condition, from [LEAD-164](../leads.d/LEAD-164.md)

[LEAD-164](../leads.d/LEAD-164.md) searched the record and the literature for a case that
checks a measured correspondence against evidence the measurement did not
itself produce. Three candidates, and three readings of "evidence the
measurement did not itself produce" that sort them differently. The
readings are alternatives; which one the condition means is the owner's
call, and so is any change of status. No status changes here.

**The candidates.**

- [CASE-tmp33vf4](../cases.d/CASE-tmp33vf4.md) ([LEAD-177](../leads.d/LEAD-177.md), [CLAIM-tmpvqmwc](CLAIM-tmpvqmwc.md); on pull request [#740](https://github.com/dmarx/nucleation/issues/740), not
  yet on staging). A simulated sensor network estimates its sensors' maps
  and revises them. Revised against beacons the world places, through a
  channel the revision can neither rewrite nor refuse, its error on the
  target's true positions returns to its level before the drift (0.044, 40
  of 40 seeds); revised by the sensors' disagreement alone it becomes
  consistent and no more accurate (0.40). The beacons are evidence the
  sensors' reports did not produce, and the estimate is scored on
  positions no arm sees.
- [CASE-333](../cases.d/CASE-333.md) ([LEAD-098](../leads.d/LEAD-098.md), on staging). An apparatus revising its
  maps of an oscillator network keeps a revision only if it predicts
  held-out kicks the apparatus did not choose. That checks its model of
  the phase responses (gains, pinning) against interventions the fitting
  did not use; the offsets revised by consistency are shown to change no
  prediction, not checked themselves. It meets the condition for the
  response model and not for the offsets, so it is a partial case.
- [CASE-tmp17zl1](../cases.d/CASE-tmp17zl1.md), filed by this lead from Riedel et al.
  ([LIT-tmp37bkp](../literature.d/LIT-tmp37bkp.md), [NOTE-tmp2d035](../notes.d/NOTE-tmp2d035.md), [THEORY-tmp5gcq1](../theory.d/THEORY-tmp5gcq1.md)). Frequency differences
  between remote clocks in four European laboratories, estimated over a
  satellite link by signal exchange, agree with a second satellite
  technique the authors call "completely independent" and, for LNE-SYRTE
  and PTB, with an optical-fibre comparison of the same clocks, one run
  simultaneously. This is the claim's own example (clock offsets by signal
  exchange, checked against a reference that took no part) in a working
  practice, with the reference a second channel to the same remote clock
  rather than a co-located one.

**Reading A: evidence whose production and scoring do not pass through
the estimate, as [CLAIM-342](CLAIM-342.md) states it; a construction suffices, since the
claim says "can".** The condition looks met by [CASE-tmp33vf4](../cases.d/CASE-tmp33vf4.md), once [#740](https://github.com/dmarx/nucleation/issues/740)
merges. Its beacons come from the world through a protected channel, and
the network's estimate is scored against true positions no arm sees.
Against it: the beacons feed the revision rather than being held out, so
the check proper is the simulator's ground truth, which no real apparatus
has; and the independence is stipulated by construction. [CASE-333](../cases.d/CASE-333.md)
meets it in part, as above.

**Reading B: a measurement practice in which the independence of the
checking evidence is the practitioners' and not a modeller's
stipulation.** No held case met it before this lead; the simulations do
not. [CASE-tmp17zl1](../cases.d/CASE-tmp17zl1.md) does, the condition looks met by it, and it is the
nearer fit to the claim's own example. Against it: the agreement is
judged within uncertainty budgets the reading did not check, only one
clock pair has a fibre check, and the case is Proposed with its reading
Skimmed.

**Reading C: the checking evidence presupposes no correspondence at
all.** No candidate meets it. The beacons' own channel map is trusted in
[CASE-tmp33vf4](../cases.d/CASE-tmp33vf4.md), and in [CASE-tmp17zl1](../cases.d/CASE-tmp17zl1.md) each channel has calibrated delays,
and all three share the clocks and one geodetic redshift correction. This
reading asks more than the claim's defeater does: the defeater is met by a
check that "presupposes the correspondence it checks", and none of these
does; each presupposes a different one. If the owner takes reading C, the
claim's thesis is in doubt for every case, and the regress (every check
rests on another trusted correspondence) would be an argument towards the
defeater, not a missing case.

**The assistant's lean**: reading B, met by [CASE-tmp17zl1](../cases.d/CASE-tmp17zl1.md), with
[CASE-tmp33vf4](../cases.d/CASE-tmp33vf4.md) as the construction that shows what the independence
consists in (a channel the estimate can neither rewrite nor refuse). On
that lean the condition the 2026-10-30 note set, "One such case would
promote it", looks met. Promotion is the owner's call. The wording is the
assistant's (Claude, in this session); adopting it is the owner's call.
