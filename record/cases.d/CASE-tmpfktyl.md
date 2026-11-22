---
status: Proposed
title: 'The record''s individuation criteria applied to the Game of Life block and eater, by computation: the block repairs any one lost cell and nothing else, the eater only the glider strike it is shaped for, single-flip coupling inside the block is zero while a birth on its border kills it, and the two blocks of the earlier two-glider collision share two cells throughout'
version: 1
standing: documented
kind: executed-study
tags:
- individuation
- complex-systems
- mathematics
date: '2026-11-22'
line:
- distributed-agency
bears_on:
- QUESTION-281
- QUESTION-035
summary: >-
  LEAD-069's study. The block and eater 1 of CASE-260 and CASE-259 are run
  in Conway's Game of Life against each individuation criterion the record
  holds. Both are fixed points. The block returns from each of its four
  single deletions and from no birth on its border or pair of deletions.
  The eater returns from none of its single deletions but from the glider
  strike in its lane, in all four phases. Coupling read as sensitivity to
  one flipped cell is zero inside the block at every horizon and large
  from its border, in the gun too. The eater's inside coupling beats its
  border's at one generation and not at five. In CASE-260's collision, the
  block that is destroyed and the block that lasts occupy the same four
  cells, two of them live throughout. Random soups give the cleaner
  transient: an isolated block with all four cells dead two generations
  later. The idea of the Life cases is the owner's. The study and its
  wording are the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CASE-259 CASE-260 CLAIM-157 CLAIM-615 CLAIM-672 CLAIM-694 ARG-101 — Proposed; the constructions studied and the claims whose criteria are applied -->

# CASE-tmpfktyl: The record's individuation criteria applied to the Game of Life block and eater, by computation: the block repairs any one lost cell and nothing else, the eater only the glider strike it is shaped for, single-flip coupling inside the block is zero while a birth on its border kills it, and the two blocks of the earlier two-glider collision share two cells throughout

## The case

**What was asked.** LEAD-069: does the record individuate the block of
CASE-260 and the eater of CASE-259? QUESTION-281's answer asks for "a form
the record individuates", and its note of 2026-11-14 says the record "has
not said whether a block is one".

**The criteria the record holds.** CLAIM-405 (Active): an individuation is
well defined only once its criterion is fixed, "the target it serves, the
transformations its unity must survive, the scale". TERM-088 (Active)
separates four senses: descriptive, dynamical, constitutive and
organizational autonomy. CLAIM-157 (Proposed) is the record's answer to
QUESTION-035, when a combined form is one system: a nearly decomposable
block whose gap beats the Occam factor. Bearing on token identity are
CLAIM-615 (Proposed; identity over time by causal transmission) and
CLAIM-694 (Proposed; a conserved type does not fix tokens). CLAIM-194
(Active) says a coupling test cannot tell a boundary a form makes from one
imposed on it.

**The criterion fixed here.** Scale: the cell lattice. Transformations:
every single-cell flip of the form and of every cell within Chebyshev
distance 3 of it; every pair of deletions; the glider strike of CASE-259;
the gun's own cycle. Target: the form's own cells over the next 200
generations. A form "returns" if the lattice is exactly the form again.

**Method.** B3/S23 on a torus large enough that nothing wraps, in NumPy,
run on 2026-11-22. Code, tests and outputs are in
`scratch/studies/lead-069/` (`study.py`, `transient.py`, `test_study.py`;
nine tests pass). Coupling is read as sensitivity: the fraction of ordered
pairs of cells (j, i), i ≠ j, for which flipping j changes i k generations
later. That is the nearest a Boolean rule has to the interaction matrix
CLAIM-157 compares, inside the candidate block against across its edge.

## Results

**1. Persistence alone, and under flips.**

| | block | eater |
|---|---|---|
| fixed point over 1,000 generations | yes | yes |
| one of its own cells deleted: returns | 4 of 4, in one generation | 0 of 7 |
| one birth on the border (distance 1): returns | 0 of 12 | 0 of 21 |
| one birth at distance 2: returns | 4 of 20 | 11 of 28 |
| one birth at distance 3: returns | 28 of 28 | 36 of 36 |
| two of its own cells deleted: returns | 0 of 6 | 0 of 21 |
| CASE-259's glider strike: returns | no, annihilated (CASE-259) | yes, in all 4 phases |

A distance-3 birth is a lone cell that dies at once, so it tests nothing.
The block's one repair is the rule's: any three of its cells give the
fourth exactly three live neighbours, and each of the three keeps two. The
eater regrows a cell only in the strike its shape is suited to. Shifted one
to three cells across the glider's path, it is destroyed four times out of
six, and the glider misses it once.

**2. Coupling inside and across the edge.**

| k-step sensitivity | inside | border to form | form to border |
|---|---|---|---|
| lone block, k = 1 | 0 | 0.42 | 0 |
| lone block, k = 2 | 0 | 0.58 | 0 |
| lone block, k = 5 and 10 | 0 | 0.75 | 0 |
| block in Gosper's gun, k = 1, mean over one period | 0.06 | 0.38 | 0.02 |
| lone eater, k = 1 | 0.24 | 0.07 | 0.05 |
| lone eater, k = 2 | 0.36 | 0.32 | 0.10 |
| lone eater, k = 5 | 0.52 | 0.55 | 0.18 |
| lone eater, k = 10 | 0.71 | 0.75 | 0.20 |

Inside the lone block nothing a single flip does reaches another of its
cells, at any horizon. Deleting one cell leaves each neighbour two live
neighbours and regrows the lost cell, so the lattice is the same a
generation later. A birth on the edge-adjacent border gives the two block
cells beside it four neighbours, and they die. The block's members tolerate
each other's loss and do not tolerate an incursion.

**3. Roles.** In 300 generations of Gosper's gun each block keeps at least
two of its four cells live, and at most three of its border cells are live
at once. The eater across the gun's stream keeps at least six of its seven
cells live from t = 300 to 600. Gliders away from the gun: 2, 6, 9 and 12
at t = 100 to 400 (CASE-260 has 5 at t = 200; the difference is one glider
at the edge of the box counted).

**4. Which block is which, in CASE-260's collision.** Followed cell by cell
(the cells of CASE-260's frame; the block at (6,1), (6,2), (7,1), (7,2)):

| t | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26–29 |
|---|---|---|---|---|---|---|---|---|
| block cells live | 3 | 4 | 4 | 2 | 2 | 3 | 3 | 4 |
| border cells live | 0 | 0 | 2 | 4 | 3 | 1 | 0 | 0 |

The block of t = 20, "destroyed at t = 22", and the block that lasts from
t = 26 are on the same four cells, and (6,1) and (6,2) are live at every
generation from t = 19 to 29. Counted as exact blocks with dead borders,
there are two instances, as CASE-260 says. Counted by continuity of the
cells that carry it, in CLAIM-615's sense of transmission, there is one
block, damaged at t = 22 and restored by t = 26, the gun's mechanism in
little.

**5. A transient with no continuity.** Of 300 random 6 × 6 soups (density
½, seeds 0–299, 150 generations), 149 contain a block that appears exactly,
with an all-dead border, and then loses all four cells and never has them
all live again. Of 1,263 such appearances, counted once per position, 540
end that way. The quickest is in seed 1. The block is isolated at t = 28,
all four cells are live at t = 29, as the rule guarantees, and none at
t = 30. The soup, rows top to bottom, set at the centre of a 64 × 64 torus:

```
oo..oo
.o.o.o
oo.oo.
o.ooo.
o.oooo
ooo.o.
```

## The criteria, one by one

- **Fixing the criterion (CLAIM-405).** Done above. Every verdict below is
  relative to that scale, those transformations and that target.
- **Descriptive (TERM-088).** Met by both. Each is an exact pattern that
  any inquiry can find and follow from generation to generation.
- **Dynamical (TERM-088), "persists under specified dynamics and
  perturbations, with robust identity and boundaries".** Met by both for
  stated families and failed for others. The block persists alone and
  under single deletions, and in the gun under the shuttle's strike. The
  eater persists alone, under its glider strike, and across the gun's
  stream. Neither persists through one birth on its border. Whether that
  is "robust" depends on which family the criterion names. TERM-088 asks
  only that it be specified.
- **Constitutive (TERM-088), "its relational organization helps fix its
  identity and boundary".** Met by the block in a strict form. A block
  cell's live neighbours are the other three, any two of them keep it
  alive, and any three make the fourth. So the 2 × 2 extent is fixed by
  the cells' relations to each other under the rule. For the eater, partly: its cells fix its shape as a still life, but
  no six of them regrow the seventh, and its regrowth after the strike
  needs the glider's cells. In Life the rule is given exactly, so the
  relations can be read off it, and CLAIM-528's limit, that interventions
  alone cannot show a constitutive dependence, does not apply.
- **Boundary (CLAIM-194).** Nothing in Life imposes a boundary. The block
  does not make its dead border either. Its cells give each border cell
  one or two live neighbours, never three, so the border stays dead only
  while nothing outside adds the missing count.
- **Organizational autonomy (TERM-088, TERM-070).** Not met by either alone.
  Neither maintains a constraint distinct from the states it acts on. In
  the gun, whether the block-and-shuttle loop is closure of constraints is
  left open, as CASE-260 leaves it.
- **One system by the gap-isolated block (CLAIM-157).** With coupling read
  as above, the lone block fails at every horizon and for every threshold.
  Its inside coupling is zero and its border's is not. The gun's block
  fails too. The eater's inside coupling is about 3.5 times its border's
  at one generation and no larger at five. It clears the test at one
  generation if the Occam threshold τ is below about 3.5, and not at
  longer horizons. τ is not set for Life. Read instead on realized
  interaction in an empty surround, nothing interacts at all. Every region
  then passes, so the test does not discriminate.
- **Token identity (CLAIM-615, CLAIM-694).** The block is a type and its
  instances are tokens. The token count depends on the criterion. Shape
  instances count CASE-260's run 1 as two blocks. Cell continuity counts
  it as one. The soup transient of result 5 is one created, unstabilized
  token on either count.

## What it can show

Within Life, every number here is a fact anyone can recompute. They fix
which criteria the block and eater meet once a criterion is fixed. They
also show that two of the record's criteria come apart on the block. The
property that keeps it in being under deletion, its cells' tolerance of one
another's loss, is the property that makes CLAIM-157's test read zero
coupling inside it.

## What it cannot show

- **Which criterion QUESTION-281 means.** That is a reading of the
  question, which the claims filed with this case give as alternatives.
- **That sensitivity is the right reading of CLAIM-157's interaction
  matrix for a Boolean rule.** It is the nearest analogue, not the only
  one. A coarse variable such as "block present" would need its own
  model.
- **Anything outside Life.**
- **Why "documented".** Every fact is a computation any reader can
  repeat, as in CASE-260 and CASE-259.
