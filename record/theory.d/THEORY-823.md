---
number: 823
# Don't copy this file by hand — run `luria new theory`, which assigns the
# code and fills in what a machine can compute.
#
# A theory is a claim about WHY something happens, or about what is true of
# these systems. State it as a finding, not as an instruction: "Batch
# normalization helps by smoothing the optimization landscape" rather than
# "Use batch normalization". If what you are about to write tells the reader
# what to do in machine learning, it is a practice, and it belongs in the
# Anthology of the SOTA (ANTH-ADR-031).

# Active | Proposed | Deferred | Superseded | Rejected, optionally " — note".
# What each one means here is in luria.yaml, and it is NOT what the same word
# means on a practice: this status says whether the record believes the
# ACCOUNT, and an explanation can be `Rejected` while the thing it explained
# goes on working exactly as well as it ever did.
status: Proposed
formerly:
- THEORY-tmpkxsq7

# REQUIRED while the status is Proposed or Deferred; delete it when the
# explanation goes Active. What would settle it — a KIND of result, not a
# quantity of them (ANTH-ADR-014). An explanation that cannot say what would show
# it wrong is a story, and this field is where that shows up.
promote_when: >-
  An experiment in Tetris or a task like it in which the cost or availability of
  the physical action is varied (a delay on the rotate key, or rotation disabled
  until a piece is fully in view) and the internal computation it is said to
  replace is measured directly, as decision time, placement errors or a
  working-memory probe. It promotes the account if extra and early rotations fall
  as the action gets dearer and placement time or error rises where they are
  blocked; it refutes the epistemic reading if blocking them costs nothing. More
  keystroke counts, or another comparison of physical with mental rotation time,
  cannot settle it: those re-establish that the moves happen and are fast, which
  is already held.

# The claim. Repeat it as the body's `# THEORY-823:` heading; the lint checks
# that the two agree.
title: 'Tetris players rotate pieces more often than planning a placement and then executing it would require, rotate them early and check the column more the higher the drop, because these moves are epistemic actions: physical action that stands in for mental computation at the moment of use'

version: 1

# One or more topics from luria.yaml, primary first — the same table the
# reading list uses. Take the topic of what the account is about.
tags:
- cognition
- embodied-cognition

date: '2026-10-20'

# There is deliberately no `published:` line. It is DERIVED from the first
# entry in `source:` below, and writing it down is a lint violation, because
# the value has one home and this is not it.

# REQUIRED, and a LIST. The papers this account rests on, primary first. An
# explanation with no paper behind it is a hunch, and the lint will say so.
source:
- LIT-1054
- LIT-1076

# What the index table shows.
summary: >-
  Kirsh and Maglio (1994), [LIT-1054](../literature.d/LIT-1054.md), read in full in [NOTE-878](../notes.d/NOTE-878.md), with Kirsh
  (1995), [LIT-1076](../literature.d/LIT-1076.md), read in [NOTE-871](../notes.d/NOTE-871.md), argue that the extra, early and
  checking moves of Tetris players are epistemic actions: physical moves
  whose primary function is to cut the space, time or unreliability of the
  player's own computation. The record holds as shown, in [THEORY-360](THEORY-360.md), only
  the early-rotation timing and the drop-length difference after the wall
  check. Over-rotation and the rise of the check with drop height rest on
  figures without printed numbers, and the saving is argued from a
  three-player pilot, not measured. Filed under [ADR-047](../decisions.d/ADR-047.md) v4 when the
  narrowing dropped it.
extends:
- THEORY-360
answers:
- QUESTION-095
---

# THEORY-823: Tetris players rotate pieces more often than planning a placement and then executing it would require, rotate them early and check the column more the higher the drop, because these moves are epistemic actions: physical action that stands in for mental computation at the moment of use

## Source

Kirsh and Maglio (1994), "On distinguishing epistemic from pragmatic
action", [LIT-1054](../literature.d/LIT-1054.md), read in full in [NOTE-878](../notes.d/NOTE-878.md) from the scan of the version of
record, with Kirsh (1995), [LIT-1076](../literature.d/LIT-1076.md), read in [NOTE-871](../notes.d/NOTE-871.md), which restates the
Tetris case (§5.1).

## What this asserts

Two things, as the authors do. First, that players rotate each piece more
often than plan-then-act would need (Figure 6: about 1.7 to 1.75 rotations
against an expected 1.5 for four-orientation pieces, read off the figure),
start rotating within a few hundred milliseconds, and use the
translate-to-wall check more the higher the drop (Figure 15). Second, that
these are epistemic actions in the authors' sense, "a physical action whose
primary function is to improve cognition" by reducing the memory, the
number of steps or the probability of error of mental computation, taken
because a physical rotation (as little as 100 ms) is faster than a mental
one, at the moment of use and with nothing stored.

## What the record holds toward it

[THEORY-360](THEORY-360.md) (Active) holds the timing ("rotation begins in earnest by 400 to
600 ms") and Table 1's longer drops after the wall check at every skill
level. The physical-versus-mental comparison comes from a pilot with three
players, and on its figure 800 to 1200 ms is total reaction time, not the
increment for a 90° rotation (about 300 ms). No score or placement was
compared with and without the moves.

## What would confirm or reject it

The promote_when, carried over unchanged from [THEORY-360](THEORY-360.md): an experiment
that varies what the physical action costs and measures the computation it
is said to replace directly.

## What this does not say

- That a result is stored for later; the paper sets itself against caching.
- That offloading pays wherever action is possible; the paper names speed
  and a determinate local effect as the conditions.
