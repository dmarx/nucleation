---
number: 672
status: Proposed
formerly:
- CLAIM-tmp9os8f
title: 'How a form is kept in being is not fixed by the form: the same still form can persist as a fixed point, by repairing itself after a strike, or by being rebuilt by a larger pattern it serves, and taking on a constitutive role can change which of these holds, so a form''s stabilization and its role, though they can come apart, are not independent'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  Any one of three results. (1) A correct run of the constructions in
  CASE-260 and CASE-259 shows the forms in their roles
  untouched: no cell of a gun block, or of the eater across the gun's
  stream, ever dies. Persistence in the role would then be the same fixed
  point as alone. (2) An argument that the mechanisms named are one
  mechanism under every reasonable choice of what the form is, so that
  the "change" is only a change in what is counted as the form. It is not
  enough to note that the whole gun is a periodic orbit, since the claim
  concerns the block's persistence, not the gun's. (3) A held claim
  already states that one form's mechanism of persistence varies with its
  role; CLAIM-280 (persistence by damage and repair) and CLAIM-456
  (internal against external maintenance) were checked and do not.
tags:
- complex-systems
- individuation
date: '2026-11-15'
line:
- distributed-agency
grounds:
- CASE-260
- CASE-259
bears_on:
- QUESTION-281
summary: >-
  An existence claim, shown in Conway's Game of Life. A block and an eater
  are each fixed points alone. In roles, the gun's blocks are partly
  destroyed and rebuilt by the gun every 30 generations, and the eater
  across the gun's stream loses and regrows a cell from its own cells
  every 30 generations. Same form, three mechanisms of persistence, and
  the role sets which. Filed at the owner's request, who proposed the Life
  case and asked for the general claim. The wording is the assistant's
  (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-2008 THEORY-2024 — Proposed; cited in this filing of 2026-11-19 -->

<!-- inactive-ok-file: CASE-260 CASE-259 ARG-101 — Proposed; the constructions and the argument filed with this claim -->

# CLAIM-672: How a form is kept in being is not fixed by the form: the same still form can persist as a fixed point, by repairing itself after a strike, or by being rebuilt by a larger pattern it serves, and taking on a constitutive role can change which of these holds, so a form's stabilization and its role, though they can come apart, are not independent

## The claim

[QUESTION-281](../questions.d/QUESTION-281.md) separates a form's creation, its stabilization and its
coming to have a constitutive role, and asks whether they are three
achievements. This claim concerns the second and third.

- **They can come apart.** A lone block in Life is stable and has no
  role ([CASE-260](../cases.d/CASE-260.md)).
- **They are not independent.** The mechanism that stabilizes the form
  is not a property of the form. In Life, the same still life persists by
  one of three mechanisms:
  - as a fixed point, alone;
  - by its own repair, the eater across a glider stream ([CASE-259](../cases.d/CASE-259.md));
  - by repair from the pattern it serves, the blocks of Gosper's gun
    ([CASE-260](../cases.d/CASE-260.md)).

  In both constructions, taking the role is what moved the form from the
  first mechanism to one of the others.

The argument is [ARG-101](../arguments.d/ARG-101.md), an existence proof.

## What it does not say

- **That a role always changes the mechanism.** In both constructions
  the role consists in absorbing strikes, so the role and the
  perturbation are one fact. A role that involved no perturbation would
  leave a fixed point a fixed point. The claim is that a role *can* change
  the mechanism.
- **That any system outside Life behaves so.** The claim is shown in one
  formal system; its interest for other systems is as a possibility,
  shown to be coherent.
- **That the block or the eater is an individual**, or that the gun's
  block-and-shuttle loop is closure in [TERM-070](../terms.d/TERM-070.md)'s sense.
- **Which mechanism is more robust.** The eater's self-repair covers one
  strike lane. On fragility, [CLAIM-456](CLAIM-456.md) is the record's held result.

## Neighbours

- **[CLAIM-280](CLAIM-280.md).** A pattern can persist through damage and repair, and the
  persistence of a product and of the organization producing it are
  separate facts. This claim adds that one form can switch between
  persisting without repair and persisting by repair, and that the switch
  comes with a role.
- **[CLAIM-456](CLAIM-456.md).** Internal maintenance can be more fragile than reset from
  outside. This claim's eater and gun blocks are the two kinds, for one
  form, but nothing is said here about which is more fragile.

## Note of 2026-11-19: readings for the exchange "Topological protection explained"

Mordvintsev and colleagues ([THEORY-2024](../theory.d/THEORY-2024.md)), read, show one form, a grown lizard, kept either as an almost stable pattern that does not repair or as an attractor that repairs itself after a strike, depending only on how the shared rule was trained. That supports the claim's thesis that the mode of persistence is not fixed by the form, in a trained system rather than Life. What changes the mode there is training, not a role, so it does not bear on the claim's second clause.

Masumori and colleagues ([THEORY-2008](../theory.d/THEORY-2008.md)), read, show the trained lizard is not a fixed point: the system "continuously traverses a structured region of state space" and returns to it after damage. That is a mode between the claim's fixed point and repair after a strike, an attracting recurrent state that is repairing all the time. The claim's list is given as what can hold, not as exhaustive, so this extends it and leaves the claim standing.

No status change.

## Note of 2026-11-25: rerun of the Life computations, and what holds it back

Rerun on 2026-11-25 by the assistant, a session other than the filer's, in the recomputation pass of [LEAD-tmpc0rqa](../leads.d/LEAD-tmpc0rqa.md), at the owner's go-ahead of 2026-11-25 ("go ahead with the reruns"). The filer's 40-line simulator was not kept, so the computations this claim uses were rebuilt from [CASE-260](../cases.d/CASE-260.md) and [CASE-259](../cases.d/CASE-259.md) as `scratch/formal/life_form_mechanisms_check.py`, a set-based B3/S23 on the unbounded plane written for this check, run with python3 -I. Reproduced: the lone block and the lone eater unchanged after 1,000 generations; the struck eater's corner alive at t = 35, dead at 36, reborn at 37, the exact eater alone at 38 and after; a block in its place annihilated; the gun's left block incomplete at t = 19 to 21 and 49 to 51 and whole at 22; the intact gun's 2, 5, 9 and 12 gliders away by t = 100, 200, 300 and 400, and populations 113, 185 and 23 at t = 400 for the intact gun and with the left or the right block removed; the eater across the stream incomplete at 103, 133, 163, 193, 223, 253 and 283, nothing beyond it at 200, 400 and 600, and gun and eater periodic with period 30 from t = 300 with 58 to 83 live cells. One set of figures depends on a criterion the case does not state: counting five-cell components at least 15 rows below the gun as gliders away (the reading under which the intact gun's counts match), the gun without its left block gives 2, 2, 2, 2 and without its right 1, 1, 1, 1, against the case's 2, 2, 3, 3 and 1, 2, 2, 2. That the gun fails without either block holds under either count. What holds it back: [ADR-057](../decisions.d/ADR-057.md)'s first criterion, its grounds [CASE-260](../cases.d/CASE-260.md) and [CASE-259](../cases.d/CASE-259.md) being Proposed constructions. The note is the assistant's (Claude, in this session). No status change.
