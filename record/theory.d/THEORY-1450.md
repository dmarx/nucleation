---
number: 1450
status: Active
formerly:
- THEORY-tmptmlc7
title: 'Douglas, Bachelet and Church built a DNA-origami barrel whose opening is governed by two aptamer locks forming a logical AND gate over cell-surface antigen inputs, so that the device stays closed and reconfigures to expose its payload only when both designated keys are present, shorter locks also opening spontaneously more often, with the key concentration needed to open set by the lock-duplex length, activation at about 10 pM for 16 to 23 bp against about 1 nM for 30 to 44 bp'
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Narrowed and promoted at the status review's ruling (the owner
    delegated these rulings), under ADR-065: the title reports what
    Douglas, Bachelet and Church built and measured, and NOTE-1634 reads
    the report and captions in full. The authors' hedge on spontaneous
    activation is restored (ADR-047 kind 3). The old title was 'Douglas,
    Bachelet and Church built a DNA-origami barrel whose opening is
    governed by two aptamer locks forming a logical AND gate over
    cell-surface antigen inputs, so that the device stays closed and
    reconfigures to expose its payload only when both designated keys
    are present, with the key concentration needed to open set by the
    lock-duplex length, activation at about 10 pM for 16 to 23 bp
    against about 1 nM for 30 to 44 bp'. The condition asked for the
    unread Supporting Online Material or an independent replication, and
    it moves unchanged to QUESTION-tmpdtizm, which lists it under this
    entry's code; this entry bears_on it: 'A reading of the Supporting
    Online Material, or an independent replication, confirms in
    quantitative form the AND truth table across the lock-pair versions
    (closed with neither or one key, open with both) and the dependence
    of the key concentration needed to open on lock length.'
tags:
- natural-sciences
- complex-systems
date: '2026-11-05'
source:
- LIT-2136
bears_on:
- QUESTION-tmpdtizm
summary: >-
  Douglas, Bachelet and Church (2012), [LIT-2136](../literature.d/LIT-2136.md), read in [NOTE-1634](../notes.d/NOTE-1634.md)
  (main text and captions; the Supporting Online Material, with the
  lock-length data, unread). Active as a report; its limits: one lab, a proof of principle,
  conformations read by TEM counts and flow cytometry. The title asserts
  the gate and the lock-length dependence; it does not assert that the
  device can revise its rule, which it cannot, nor anything about
  cycling, holding costs or clinical use.
---

# THEORY-1450: Douglas, Bachelet and Church built a DNA-origami barrel whose opening is governed by two aptamer locks forming a logical AND gate over cell-surface antigen inputs, so that the device stays closed and reconfigures to expose its payload only when both designated keys are present, shorter locks also opening spontaneously more often, with the key concentration needed to open set by the lock-duplex length, activation at about 10 pM for 16 to 23 bp against about 1 nM for 30 to 44 bp

## Source

Douglas, Bachelet and Church (2012), [LIT-2136](../literature.d/LIT-2136.md); read in [NOTE-1634](../notes.d/NOTE-1634.md).

## What was actually shown

- **The gate** (Fig. 2B): "Both locks needed to be opened simultaneously to
  activate the robot. The robot remained inactive when only one of the two
  locks was opened." It could have opened on one key; it did not.
- **The rule in sequence** (Fig. 2C): six versions from "pairwise
  combinations of aptamer locks drawn from a set of three" aptamers, the
  inputs chosen by which aptamers were installed.
- **Lock length against key concentration** (p. 831): 16–23 bp locks
  activate at 10 pM, while "30, 37, and 44 bp required 1 nM", with shorter
  locks opening spontaneously more often.
- **The construction aid** (pp. 831–832): guide staples "increased the
  yield of closed robots from 48% to 97.5%".

## What this does not say

- That the device can revise its own rule: the aptamer pair is fixed at
  fold time, and opening is a one-shot conformational change.
- That opening is reversible or the barrel cycles: re-closing and the
  energy of the entropic spring are not characterized in the text read.
- Quantitative thermodynamics or kinetics of the locks: these are in the
  unread Supporting Online Material.
- Anything about the barrel's own folding pathway or traps, the subject of
  [THEORY-1398](THEORY-1398.md).