---
number: 260
status: Proposed
formerly:
- CASE-tmpnqx8e
title: 'The block in Conway''s Game of Life: one two-glider collision makes a block that is destroyed the next generation and later a block that lasts, the difference set by a cell outside the form; a lone block is a fixed point that nothing depends on, while each block of Gosper''s glider gun is broken and rebuilt by the gun every 30 generations and the gun stops emitting without it'
version: 1
standing: documented
kind: construction
tags:
- complex-systems
- individuation
- mathematics
date: '2026-11-14'
line:
- distributed-agency
bears_on:
- QUESTION-281
summary: >-
  A construction in Conway's Game of Life (B3/S23), every step computed
  and checkable. The same form, the 2 × 2 block, is followed through the
  three achievements [QUESTION-281](../questions.d/QUESTION-281.md) separates. Creation: a collision of two
  gliders. Stabilization: a lone block is a fixed point, but whether it
  persists is decided by cells two away from it; in one collision an
  exact block with an empty border appears and is destroyed, and a later
  one lasts. Constitutive role: a lone block has none, while each block of
  Gosper's glider gun is needed for the gun to keep emitting, and is
  itself partly destroyed and rebuilt by the gun every 30 generations.
  Ending: a glider strike removes a block entirely. The idea of a case in
  Life is the owner's; the construction and its wording are the
  assistant's (Claude, in this session); adopting it is the owner's call.
---

<!-- inactive-ok-file: CLAIM-157 — Proposed; named as the record's individuation claim the case does not apply -->

# CASE-260: The block in Conway's Game of Life: one two-glider collision makes a block that is destroyed the next generation and later a block that lasts, the difference set by a cell outside the form; a lone block is a fixed point that nothing depends on, while each block of Gosper's glider gun is broken and rebuilt by the gun every 30 generations and the gun stops emitting without it

## The case

**The system.** Conway's Game of Life, rule B3/S23. A dead cell with
exactly three live neighbours is born, and a live cell with two or three
survives. The form followed is the **block**, four live cells in a
2 × 2 square. Each block cell has exactly three live neighbours, so a
block whose eight-cell border stays dead is unchanged for ever.

[QUESTION-281](../questions.d/QUESTION-281.md) asks for a form whose creation, stabilization and
constitutive role are each shown separately, and for a case in which two
of them come apart. Life lets each be shown exactly. Every claim below was
computed on 2026-11-14 with a 40-line NumPy implementation on a torus
large enough that nothing wraps during the runs used. The configurations
are given so that any Life program can check them.

**1. Creation, and creation without stabilization.** Two gliders, one
moving down-right and one down-left, start at t = 0 in these cells
(row, column): (0,5), (1,3), (1,4), (2,4), (2,5), and (4,1), (5,2), (6,0),
(6,1), (6,2).

```
......o.
....oo..
.....oo.
........
..o.....
...o....
.ooo....
```

Each moves on its own until t = 5, when they begin to interact. Then:

- **t = 20.** An exact block with an entirely dead border appears in the
  debris. A single live cell lies two rows below it. Two cells of the
  block's border each have exactly three live neighbours: two from the
  block and that one cell. Both are born at t = 21, while all four block
  cells survive, as the rule guarantees. At t = 22 two of the block's
  cells die of overcrowding, and the block is gone.
- **t = 26–27.** A second block forms from the remaining debris. By t = 27
  it is the only thing on the lattice, and it is unchanged at t = 300.

The same collision makes the same form twice. The first instance is
created and not stabilized; the second is created and stabilized. The
difference is not in the form: both are exact blocks with dead borders.
It is in one cell two away, outside the form. A block's own neighbour
counts keep its cells alive for one generation; whether it persists
depends on cells it does not contain.

**2. Stabilization without a constitutive role, and with one.** A lone
block on an empty lattice is unchanged after 1,000 generations: a fixed
point. Nothing depends on it. Removing it changes nothing but its own
cells.

Gosper's glider gun (36 cells; the standard pattern) has a block at each
end. The gun is periodic with period 30, and 2, 5, 9 and 12 gliders have
left it by t = 100, 200, 300 and 400. Its blocks are not left alone.
Every 30 generations the shuttle at each end strikes its block: the left
block at t = 18–21 and 48–51, the right at t = 23–26 and 53–56. At t = 19,
two of the left block's four cells are dead. By t = 22 all four are alive
again and the border is clear. In the gun, the block persists because the
gun rebuilds it, not because it is a fixed point.

Remove either block at t = 0 and the gun fails:

| | Gliders away at t = 100 / 200 / 300 / 400 | Population at t = 400 |
|---|---|---|
| Intact gun | 2 / 5 / 9 / 12 | 113 |
| Left block removed | 2 / 2 / 3 / 3 | 185; not periodic by t = 240 |
| Right block removed | 1 / 2 / 2 / 2 | 23; a period-30 remnant |

**3. The change that ends it.** A glider aimed at a lone block, with the
glider's cells at (0,1), (1,2), (2,0), (2,1), (2,2) and the block's at
(15,17), (15,18), (16,17), (16,18), leaves an empty lattice: population 0
at t = 300.

## What it shows

- **Creation and stabilization come apart, exactly.** In run 1 the same
  event makes the same form twice, and only one instance is stabilized.
  What stabilizes a block is not in the block. Its cells survive by the
  rule, but its persistence needs a border that no outside cell will
  populate, and that is fixed by the configuration two cells out.
- **Stabilization and constitutive role come apart.** The lone block is
  stable and constitutes nothing. The gun's blocks are constitutive: the
  gun's period-30 emission depends on each. That gives the "stabilized
  without any constitutive role" half of the question's request, shown,
  not argued.
- **The mechanism of stabilization changes with the role.** The lone
  block is stabilized as a fixed point. Each gun block is stabilized by
  repair: the gun breaks it and rebuilds it every cycle. The shuttle that
  needs the block is also what restores it, so in the gun the block's
  persistence and its role are one loop, not two separate achievements. A
  form's taking a constitutive role can change how it is stabilized.

## What it cannot show

- **Anything about physical or living systems.** Life is a stipulated
  rule. The case shows that the three achievements are logically
  separable and how they come apart in one exact system, not that they
  come apart in any other.
- **That the block is an individual.** The record has not said whether a
  block is a form it individuates ([QUESTION-035](../questions.d/QUESTION-035.md), [CLAIM-157](../claims.d/CLAIM-157.md)). The case
  takes the block as a form by its recurring shape, the sense of "real
  pattern" in Dennett ([LIT-220](../literature.d/LIT-220.md)).
- **Whether the gun's block-and-shuttle loop is organizational closure in
  [TERM-070](../terms.d/TERM-070.md)'s sense.** It resembles it: the block depends on the shuttle
  that depends on it. But the block is partly destroyed each cycle, and
  whether a constraint may be so is not settled here.
- **Why "documented".** This standing is used because every fact here is
  a computation any reader can repeat. The system is a formal rule, not
  an event in the world.
