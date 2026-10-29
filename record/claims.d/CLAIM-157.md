---
number: 157
status: Proposed
formerly:
- CLAIM-tmp8tsw5
title: 'Relative to a stated target, a combined form is one system while its joint dynamics are nearly decomposable with the form as a block whose gap beats the Occam factor, and it lasts as long as that block persists; the unit is the gap-isolated block, not any member'
version: 8
history:
- version: 2
  date: '2026-10-11'
  note: >-
    The objection CLAIM-173 was rejected the same day
    (CLAIM-167), so the passages that called it open are revised.
    One-way drive passes rightly, and direction is read as the system's
    architecture. The criterion is unchanged.
- version: 3
  date: '2026-10-14'
  note: >-
    Four readings of the day, set beside the criterion without changing
    it. NOTE-791 (LIT-979): dynamical independence allows outgoing
    coupling but not incoming, which differs from a near-decomposable
    block. NOTE-773 (LIT-989): a case where the block verdict stays
    the same while the module's ability to act as a unit changes.
    NOTE-756 (LIT-953): the duration clause needs a window and a
    tolerance, since averaged and local verdicts can disagree.
    NOTE-814 (LIT-955): one global threshold fits some regions and
    not others.
- version: 4
  date: '2026-10-16'
  note: >-
    grounds gains THEORY-661, which states Simon's
    near-decomposability result that the criterion relies on. The claim
    is unchanged.
- version: 5
  date: '2026-10-19'
  note: >-
    Note of 2026-10-19 added, from the exchange on coarse-to-fine
    processes: closure without a block (CLAIM-388), and the two
    questions it opens (QUESTION-218, QUESTION-219). The
    criterion is unchanged.
- version: 6
  date: '2026-10-20'
  note: >-
    Note of 2026-10-20 added, from the readings of that day: bounds on how block tests and closure relate (CLAIM-390, CLAIM-386), equitable partitions (THEORY-755), the spectral reading of near-decomposability (NOTE-977), and scale locality (THEORY-754). The criterion is unchanged.
- version: 7
  date: '2026-10-20'
  note: >-
    The note of 2026-10-20 gains a fifth point, from the reading of Nadler et al. (NOTE-986): a data-driven gap finds the block well and its duration poorly. The criterion is unchanged.
- version: 8
  date: '2026-10-29'
  note: >-
    Note of 2026-10-29 added by the eleventh status review (ADR-057):
    CLAIM-154, on which this claim rests, is narrowed to candidates whose
    model stays regular at the switch-off, conceding CLAIM-188. The
    claim is unchanged.
role: thesis
warrant: interpretive
defeated_if: >-
  Measured cases in which the block criterion and independent marks of
  unity come apart systematically, for the same target: blocks that clear
  the threshold whose members do not compensate for each other under
  perturbation, or forms that do compensate and entrain but never clear
  it. A block that passes because the coupling is strong one way does not
  count: one-way drive passes rightly (CLAIM-167).
tags:
- individuation
- complex-systems
- embodied-cognition
date: '2026-10-11'
line: distributed-agency
answers:
- QUESTION-035
rests_on:
- CLAIM-154
- CLAIM-164
- CLAIM-152
grounds:
- LIT-905
- THEORY-661
complements:
- CLAIM-172
- CLAIM-167
uses:
- TERM-049
- TERM-046
- TERM-044
- TERM-045
summary: >-
  The record's proposed answer to [QUESTION-035](../questions.d/QUESTION-035.md), joining the
  dual-filed MOM results. Simon's near-decomposability says what to
  compare: interaction inside a candidate block against interaction
  across its edge. The gap theorem says the unit is the block, and the
  Occam factor says when the gap is big enough to name it. Persistence is
  how long the block keeps clearing the threshold. It answers the owner's
  "privileged nomenclature" for the dancing couple with a test. Proposed:
  nothing has been measured. One-way drive passes, rightly
  (CLAIM-167), and the direction of coupling gives the system's
  architecture.
illustrated_by:
- CASE-045
objected_by:
- CLAIM-173
- CLAIM-194
supports:
- CLAIM-174
---
<!-- inactive-ok-file: QUESTION-281 LIT-1654 LIT-1642 — the question the pressures are filed in (Open) and its sources, registered unread (Deferred) -->
<!-- inactive-ok-file: QUESTION-009 — Deferred; the broader agent question this claim sets apart from its own -->
<!-- inactive-ok-file: CLAIM-172 CLAIM-175 CLAIM-161 CLAIM-167 — Proposed; the neighbouring tests, the owner's claims and the reply that defends this criterion, open -->
<!-- inactive-ok-file: THEORY-257 THEORY-265 THEORY-268 THEORY-254 — Proposed; readings of 2026-10-14 set beside the criterion, open -->
<!-- inactive-ok-file: CLAIM-173 — Rejected; cited as the answered objection, not as standing -->
<!-- inactive-ok-file: LIT-902 — cited for the compensation test (unread) and the extended-mind case; not leaned on beyond what is said -->

# CLAIM-157: Relative to a stated target, a combined form is one system while its joint dynamics are nearly decomposable with the form as a block whose gap beats the Occam factor, and it lasts as long as that block persists; the unit is the gap-isolated block, not any member

## The claim

Fix a target, meaning what the description must predict ([CLAIM-152](CLAIM-152.md)).
For the dancing couple it might be the next beat's positions. Model the
joint dynamics of the candidate's members and their surroundings, for
example as a linear model of their state variables. Then:

1. **Block.** The candidate is one system ([TERM-049](../terms.d/TERM-049.md)<!-- ref::uses: TERM-049 -->) when, with its members grouped,
   the interaction matrix is nearly decomposable ([LIT-905](../literature.d/LIT-905.md)). The
   couplings inside the group are strong and those across its edge are
   weak.
2. **Threshold.** The gap that sets the block off clears the Occam factor ([TERM-046](../terms.d/TERM-046.md)<!-- ref::uses: TERM-046 -->)
   for that block: δ/ε > τ, with τ² the log prior-to-posterior variance
   ratio ([CLAIM-154](CLAIM-154.md)). Below it, the block is not worth naming.
3. **Unit.** What is named is the gap-isolated block, the projector onto
   the pair's joint mode, not either member or any coordinate
   ([CLAIM-164](CLAIM-164.md)).
4. **Duration.** The form lasts while the block keeps clearing the
   threshold. The couple is one system for the song and two after it.
   Simon's short-run independence and long-run aggregate dependence say
   what the boundary licenses while it holds.

This answers the owner's "privileged nomenclature" ([CLAIM-175](CLAIM-175.md)) with a
test. The name is earned when the gap beats the cost of keeping it.

## How it sits with the other tests

- **Mutual entrainment ([CLAIM-172](CLAIM-172.md))** is a sufficient mark, and it says
  the members are peers. This claim measures strength and passes one-way
  drive as well. The direction of the coupling then gives the system's
  architecture, peers or hierarchy ([CLAIM-167](CLAIM-167.md)). The objection that
  one-way drive should not pass ([CLAIM-173](CLAIM-173.md)) is rejected.
- **Reciprocal compensation** ([LIT-902](../literature.d/LIT-902.md), unread) is a perturbation test.
  A block that clears the threshold should also compensate. If it does not,
  that is evidence against this claim (`defeated_if`).
- **Persistence and unity** are further tests. [CLAIM-161](CLAIM-161.md) asks whether a
  coherence measure is conserved within the block. [CLAIM-153](CLAIM-153.md) asks
  whether the block's contexts glue. A form can clear the threshold and
  still fail either.
- **Otto's notebook** is not a dynamical partner. Its coupling is a write
  and a later read, and a block test on synchronous dynamics will not see
  it. The storage route ([CASE-043](../cases.d/CASE-043.md)) needs a time-lagged version of
  the criterion, which is not built.
- **Dynamical independence** ([THEORY-257](../theory.d/THEORY-257.md), [LIT-979](../literature.d/LIT-979.md), [NOTE-791](../notes.d/NOTE-791.md))
  asks only that no information flow into the coarse variable from the
  rest. It allows outgoing coupling and forbids incoming. Near-decomposability
  asks for weak coupling across the edge in both directions. A module that
  drives the rest and receives nothing is dynamically independent; one that
  is driven never is. The two pick different blocks whenever coupling is
  one-way.
- **Acting as a unit** ([THEORY-265](../theory.d/THEORY-265.md), [LIT-989](../literature.d/LIT-989.md), [NOTE-773](../notes.d/NOTE-773.md)). In a
  modular coordination game the interaction matrix is nearly decomposable
  throughout, so the block verdict is the same before and after
  entrainment. What changes is timing, and with it whether the module
  responds to the others as one. So a block that clears the threshold need
  not behave as a unit. That is consistent with this claim, which
  disclaims agency, but it shows the two come apart in a concrete case.

## What it does not say

- **That the verdict is target-free.** A different target can group the
  members differently.
- **That a form clearing the threshold is an agent ([TERM-044](../terms.d/TERM-044.md)<!-- ref::uses: TERM-044 -->) or a self ([TERM-045](../terms.d/TERM-045.md)<!-- ref::uses: TERM-045 -->).** Those are
  [QUESTION-009](../questions.d/QUESTION-009.md) and the subject sense of [ADR-024](../decisions.d/ADR-024.md).
- **That anything has been measured.** [CASE-045](../cases.d/CASE-045.md) is the study it would
  need.
- **When the block stops persisting.** The duration clause is stated over
  joint dynamics, which are estimated over an interval. For information
  measures the averaged verdict and the verdict at a moment can disagree
  in sign ([THEORY-268](../theory.d/THEORY-268.md), [LIT-953](../literature.d/LIT-953.md), [NOTE-756](../notes.d/NOTE-756.md)), so the clause needs a
  window and a tolerance for how many failing moments end the form. Neither
  is set.
- **That one threshold serves the whole system.** On tangles, each region
  of a network has its own best order, and one global threshold splits
  some forms and misses others ([THEORY-254](../theory.d/THEORY-254.md), [LIT-955](../literature.d/LIT-955.md), [NOTE-814](../notes.d/NOTE-814.md)).
  The Occam factor here is set per block, which is the kind of per-region
  setting a global threshold lacks.

## Note of 2026-10-19: closure without a block, and flux

A5 of the exchange of 2026-10-19 on coarse-to-fine processes asked whether
"organizational unity require[s] a subsystem boundary, or can it arise from
a dynamically closed collective mode distributed across multiple otherwise
entangled subsystems?" Two things came of it.

- **The two tests come apart under symmetric coupling too.** This claim
  already records that dynamical independence and the block pick different
  units when coupling is one-way. [CLAIM-388](CLAIM-388.md) shows they also differ
  when it is symmetric. Under uniform coupling the sum of all units is
  exactly closed, and no grouping of the units is a block ([CASE-120](../cases.d/CASE-120.md)).
  The unit named here is already a mode (point 3, after [CLAIM-164](CLAIM-164.md)), but it
  is found by grouping members. Whether a mode found without a grouping can
  be one system is [QUESTION-218](../questions.d/QUESTION-218.md). A case of it that compensated and
  entrained would meet this claim's `defeated_if`.
- **A third kind of organization.** A5 set containment (this claim's
  block) and mode (closure) beside flux: a pattern of transfer that
  persists while constituents are replaced. In turbulence, transfer across
  scales is local without the scales being weakly coupled blocks (Eyink and
  Aluie, [LIT-1239](../literature.d/LIT-1239.md), unread). Whether flux picks out units this test
  misses is [QUESTION-219](../questions.d/QUESTION-219.md). A5's guard is this claim's: a newly found
  mode or flux "should not automatically be treated as an individual, much
  less an agent."

## Note of 2026-10-20: what the readings did to the block test

The first readings of the coarse-to-fine program bear on this claim in four
ways. None changes the criterion.

- **Weak coupling in, little dependence.** For a block's full state in a
  linear Gaussian VAR(1), dynamical dependence is of second order in the
  coupling into the block, whatever the coupling out of it
  ([CLAIM-390](CLAIM-390.md)). So a block that clears this claim's test because its
  incoming coupling is weak is also nearly closed in Barnett and Seth's
  sense. A block that clears it with strong outgoing coupling and weak
  incoming coupling is too. That is the one-way case this claim already
  passes ([CLAIM-167](CLAIM-167.md)).
- **The aggregate is another matter.** The sum over a block closes only if
  the block's own dynamics close on it. In one step that needs equal
  column sums within the block ([CLAIM-386](CLAIM-386.md)). Simon's argument relies on
  the fast transient to make the rest small. The unit this claim names, the
  projector onto the block's joint mode (point 3), is the right object for
  that reason: it is the slow part of the block, not its sum.
- **Read the gap spectrally.** Shpak, Stadler, Wagner and Altenberg's flat
  landscape ([NOTE-977](../notes.d/NOTE-977.md)) has entrywise weak coupling between blocks and
  no separation of time scales at any rate. This claim's test compares a
  gap against coupling, so it is already the spectral reading, which is
  the one that works.
- **Groupings that close without being blocks.** Column-equitable
  partitions ([THEORY-755](../theory.d/THEORY-755.md)) and turbulent scale bands ([THEORY-754](../theory.d/THEORY-754.md),
  conditional) organize a system without a gap. Whether either is "one
  system" is [QUESTION-218](../questions.d/QUESTION-218.md) and [QUESTION-219](../questions.d/QUESTION-219.md).
- **A data-driven gap gives the block, not its duration.** Nadler et al.
  ([NOTE-986](../notes.d/NOTE-986.md)) recover the wells of a double-well diffusion from
  equilibrium samples almost perfectly (99.6–99.8% of points). But they
  underestimate the slow eigenvalue that sets the wells' lifetime by
  30–80%, because few samples cross the barrier. This claim's duration
  clause needs a lifetime, and equilibrium data are the weak place to get
  one.

## Note of 2026-10-27: pressures from the dynamics of transitions

A14 of the exchange of 2026-10-27 raised three pressures on criteria that read
an individual off a gap. They are filed as [QUESTION-281](../questions.d/QUESTION-281.md), not as
objections, since none is shown to defeat this claim's coupling-gap criterion.
(i) Non-normal transient growth can carry a system out of a regime whose
linearization is stable at every instant ([THEORY-724](../theory.d/THEORY-724.md); [LIT-932](../literature.d/LIT-932.md)). (ii)
Rate-induced tipping can end a form whose frozen-parameter attractor still
exists ([LIT-1654](../literature.d/LIT-1654.md), unread), which bears on "it lasts as long as that block
persists". (iii) Localized structures persist as dynamical individuals while
their material turns over ([LIT-1642](../literature.d/LIT-1642.md), unread), a case for testing whether
the criterion follows a form through turnover.

## Note of 2026-10-27 (later): the pressures read

Two of the pressures noted above are now read. In Ashwin et al.'s model the
matrix M is the same at every instant (their eq. 4), so a gap or spectral
verdict computed from frozen dynamics stays constant through the tip
([NOTE-1215](../notes.d/NOTE-1215.md)). Read on frozen dynamics, "it lasts as long as that block
persists" would say the form lasts after the system has left it; the clause
survives if "persists" is read on the trajectory. In Toner and Tu's theory
([NOTE-1228](../notes.d/NOTE-1228.md)) the order is a gapless mode of a field, stabilized by
neighbourhoods that keep changing, so no fixed grouping of members persists
while the order does. It is a case for [QUESTION-218](../questions.d/QUESTION-218.md), a mode found without a
grouping.

## Note of 2026-10-29: the narrowed rule

CLAIM-154 now holds only where the candidate's model stays regular at its
switch-off. Where it is singular the rule overcharges (CLAIM-188), so a
candidate it rejects may still earn a name.
