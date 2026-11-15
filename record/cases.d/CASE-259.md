---
number: 259
status: Proposed
formerly:
- CASE-tmpjucsj
title: 'The eater in Conway''s Game of Life: alone it is a fixed point; struck by a glider in one lane it loses a cell and regrows it by its own neighbour counts, where a block in its place is annihilated; set across a glider gun''s stream it repairs itself every 30 generations and makes gun and eater one bounded period-30 whole'
version: 1
standing: documented
kind: construction
tags:
- complex-systems
- individuation
- mathematics
date: '2026-11-15'
line:
- distributed-agency
variant_of:
- CASE-260
bears_on:
- QUESTION-281
summary: >-
  A second construction in Conway's Game of Life, computed and checkable,
  varying [CASE-260](CASE-260.md)'s block. Eater 1, a seven-cell still life, is
  unchanged for 1,000 generations alone. Struck by a glider in one lane,
  its corner cell dies and is reborn the next generation from its own
  cells, and the glider is gone. A block in the same place is annihilated
  by the same strike, and the eater struck in any other lane tried is
  destroyed. Placed across the output lane of Gosper's glider gun, it
  loses and regrows a cell every 30 generations, nothing passes it, and
  the whole is periodic. It adds a third mechanism of stabilization,
  self-repair, beside the block's fixed point and the gun block's repair
  by the gun. Built at the owner's request; the construction and wording
  are the assistant's (Claude, in this session); adopting it is the
  owner's call.
---

<!-- inactive-ok-file: CASE-260 — Proposed; the block construction this case varies, filed with it -->

# CASE-259: The eater in Conway's Game of Life: alone it is a fixed point; struck by a glider in one lane it loses a cell and regrows it by its own neighbour counts, where a block in its place is annihilated; set across a glider gun's stream it repairs itself every 30 generations and makes gun and eater one bounded period-30 whole

## The case

**The form.** Eater 1, in cells (row, column) (0,0), (0,1), (1,0), (1,2),
(2,2), (3,2), (3,3):

```
oo..
o.o.
..o.
..oo
```

Under B3/S23 it is a still life. Alone on an empty lattice it is
unchanged after 1,000 generations, a fixed point like the block of
[CASE-260](CASE-260.md). It was computed on 2026-11-15 with the same simulator as
that case.

**1. Self-repair after a strike.** A glider in cells (0,1), (1,2), (2,0),
(2,1), (2,2) moves down-right toward the eater in cells (12,12), (12,13),
(13,12), (13,14), (14,14), (15,14), (15,15):

- **t = 35.** The glider first interacts with the eater.
- **t = 36.** The eater's corner cell (0,0) is dead.
- **t = 37.** The corner cell is reborn: it has exactly three live
  neighbours, from the eater's own cells.
- **t = 38.** Only the exact eater remains. The glider is gone, and
  nothing changes after this generation.

All four phases of the glider in this lane give the same result. Nothing
outside the eater takes part in the repair.

**2. What the same strike does to other forms and lanes.**

- **A block in the eater's place** (cells (12,12) to (13,13)), struck in
  this lane and in every lane from −2 to +3, leaves an empty lattice.
- **The eater struck one to three cells to either side** (lanes −3 to
  −1 and +1 to +3) is destroyed. Three lanes leave nothing; three leave
  debris (20, 30 and 53 cells) without the eater.

Its robustness covers the one strike its shape is suited to.

**3. Self-repair in a role.** In the frame where Gosper's gun cell (x, y)
is at row y, column x ([CASE-260](CASE-260.md)'s gun), the eater is placed with its
cell (0,0) at row 30, column 44, across the gun's output lane. Then:

- From t = 103, one eater cell is dead at t = 103, 133, 163, 193, 223, 253
  and 283, and every 30 generations after. Each time it is reborn the
  next generation.
- No live cell lies beyond the eater at t = 200, 400 or 600.
- The whole lattice, gun and eater, is periodic with period 30 from
  t = 300 to t = 600, with 58 to 83 live cells.

Without the eater the gun's gliders leave for ever ([CASE-260](CASE-260.md): 12 by
t = 400).

## What it shows

- **A third mechanism of stabilization.** The lone block and the lone
  eater are fixed points. The struck eater persists by self-repair: a
  lost cell is rebuilt from the form's own cells, with no help from
  outside. The gun's blocks in [CASE-260](CASE-260.md) persist by repair from the
  pattern they serve. Three mechanisms keep the same kind of form, a
  still life, in being.
- **The role again changes the mechanism.** The eater's role, absorbing
  the gun's stream so that gun and eater form one bounded whole, moves it
  from fixed point to repeated self-repair. As with the block, the role
  consists in taking strikes, so the change of mechanism comes with the
  role.
- **Self-repair is narrow.** It holds for one lane. Struck otherwise, the
  eater fares no better than the block.

## What it cannot show

- **Anything outside Life.** It is the same as [CASE-260](CASE-260.md) here.
- **That self-repair is more robust than repair by a larger pattern.**
  Only one strike lane each was tried in a role. [CLAIM-456](../claims.d/CLAIM-456.md) finds, in
  another system, that self-production can be the more fragile
  arrangement.
- **Why "documented".** As in [CASE-260](CASE-260.md), every fact is a
  computation any reader can repeat.
