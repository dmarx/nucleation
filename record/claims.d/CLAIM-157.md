---
number: 157
status: Proposed
formerly:
- CLAIM-tmp8tsw5
title: 'Relative to a stated target, a combined form is one system while its joint dynamics are nearly decomposable with the form as a block whose gap beats the Occam factor, and it lasts as long as that block persists; the unit is the gap-isolated block, not any member'
version: 3
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
    it. NOTE-tmpjuj7z (LIT-979): dynamical independence allows outgoing
    coupling but not incoming, which differs from a near-decomposable
    block. NOTE-tmp9ypte (LIT-989): a case where the block verdict stays
    the same while the module's ability to act as a unit changes.
    NOTE-tmp0o608 (LIT-953): the duration clause needs a window and a
    tolerance, since averaged and local verdicts can disagree.
    NOTE-tmpv7vus (LIT-955): one global threshold fits some regions and
    not others.
role: thesis
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
<!-- inactive-ok-file: QUESTION-009 — Deferred; the broader agent question this claim sets apart from its own -->
<!-- inactive-ok-file: CLAIM-172 CLAIM-175 CLAIM-161 CLAIM-153 CLAIM-167 — Proposed; the neighbouring tests, the owner's claims and the reply that defends this criterion, open -->
<!-- inactive-ok-file: THEORY-tmpc7h4d THEORY-tmph3haa THEORY-tmpjvv0j THEORY-tmpaf2sz — Proposed; readings of 2026-10-14 set beside the criterion, open -->
<!-- inactive-ok-file: CLAIM-173 — Rejected; cited as the answered objection, not as standing -->
<!-- inactive-ok-file: LIT-902 LIT-097 — cited for the compensation test (unread) and the extended-mind case; not leaned on beyond what is said -->

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
- **Dynamical independence** ([THEORY-tmpc7h4d](../theory.d/THEORY-tmpc7h4d.md), [LIT-979](../literature.d/LIT-979.md), [NOTE-tmpjuj7z](../notes.d/NOTE-tmpjuj7z.md))
  asks only that no information flow into the coarse variable from the
  rest. It allows outgoing coupling and forbids incoming. Near-decomposability
  asks for weak coupling across the edge in both directions. A module that
  drives the rest and receives nothing is dynamically independent; one that
  is driven never is. The two pick different blocks whenever coupling is
  one-way.
- **Acting as a unit** ([THEORY-tmph3haa](../theory.d/THEORY-tmph3haa.md), [LIT-989](../literature.d/LIT-989.md), [NOTE-tmp9ypte](../notes.d/NOTE-tmp9ypte.md)). In a
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
  in sign ([THEORY-tmpjvv0j](../theory.d/THEORY-tmpjvv0j.md), [LIT-953](../literature.d/LIT-953.md), [NOTE-tmp0o608](../notes.d/NOTE-tmp0o608.md)), so the clause needs a
  window and a tolerance for how many failing moments end the form. Neither
  is set.
- **That one threshold serves the whole system.** On tangles, each region
  of a network has its own best order, and one global threshold splits
  some forms and misses others ([THEORY-tmpaf2sz](../theory.d/THEORY-tmpaf2sz.md), [LIT-955](../literature.d/LIT-955.md), [NOTE-tmpv7vus](../notes.d/NOTE-tmpv7vus.md)).
  The Occam factor here is set per block, which is the kind of per-region
  setting a global threshold lacks.
