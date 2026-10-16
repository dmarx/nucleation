---
number: 307
status: Active
formerly:
- CLAIM-tmp6u639
title: 'Retrieval pressure and evidence are different criteria for carving a category,
  and they move in opposite directions with copy count: evidence that a distinction
  exists grows with its copies, the search a bin saves shrinks with them, so the
  bins a deadline forces are often the ones the data least supports'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A search model in which the expected cost of finding one of c copies among m similar
  items does not fall as c grows, or an evidence model in which a distinction's
  d'² does not grow with its copies. Either removes the opposition. Or a case in
  which a system with a deadline leaves a rare, often-wanted item that is similar
  to its binmates unsorted, at no cost in time.
tags:
- model-comparison
- information-retrieval
- cognition
date: '2026-10-15'
line:
- formal-apparatus
- distributed-agency
grounds:
- CASE-094
complements:
- CLAIM-154
- CLAIM-309
illustrated_by:
- CASE-094
summary: >-
  From [MOM-CLM-166](https://github.com/dmarx/mathematics-of-meaning/blob/main/record/claims.d/CLM-166.md), which reads the owner's LEGO parable ([CASE-094](../cases.d/CASE-094.md)) against
  a formalism that cited it with the sign reversed. [CLAIM-154](CLAIM-154.md) says when a distinction
  is real enough to name. Its evidence grows with the number of copies. The parable
  says when a distinction must be built to act in time: a single brick among similar
  ones. Expected search falls as copies grow. The two answer different questions,
  "is it there?" and "can it be reached in time?", and come apart in both directions.
  MOM's table was re-run here and reproduced, and a simulation of the search agrees.
---
<!-- inactive-ok-file: THEORY-385 — Proposed; one set of the authors' own tests, cited as a related case -->

# CLAIM-307: Retrieval pressure and evidence are different criteria for carving a category, and they move in opposite directions with copy count: evidence that a distinction exists grows with its copies, the search a bin saves shrinks with them, so the bins a deadline forces are often the ones the data least supports

## The claim

[MOM-CLM-166](https://github.com/dmarx/mathematics-of-meaning/blob/main/record/claims.d/CLM-166.md): "Keep both criteria and stop calling them one." Detection
asks whether a distinction is in the data, and a large margin is evidence
that it is ([CLAIM-154](CLAIM-154.md): keep it when d'² exceeds the Occam cost).
Retrieval asks whether the distinction must be built to act in time, and
a large margin means it need not, because the item already stands out:
"if it's a single black brick in a box of white bricks: ok, it's buried
but its' still detectable" ([CASE-094](../cases.d/CASE-094.md)).

**Copy count separates them.** Take a kind with c copies among m similar
items, effect μ, noise σ and prior scale s.

- **Evidence.** d'² = cμ²/σ², against an Occam cost of ln(1 + cs²/σ²).
  Evidence grows linearly in c, the cost only logarithmically.
- **Search.** With the bin in random order, the expected number of other
  items examined before the first copy is m/(c+1). It falls as 1/c.

[MOM-CLM-166](https://github.com/dmarx/mathematics-of-meaning/blob/main/record/claims.d/CLM-166.md)'s table, with m = 200, μ = 0.8, σ = 1, s = 3 and a deadline of
D = 12 items, re-run here:

| c | d'² | Occam | detection | m/(c+1) | simulated | retrieval |
|---:|---:|---:|---|---:|---:|---|
| 1 | 0.64 | 2.30 | prune | 100.00 | 100.53 | carve |
| 2 | 1.28 | 2.94 | prune | 66.67 | 67.05 | carve |
| 5 | 3.20 | 3.83 | prune | 33.33 | 33.74 | carve |
| 20 | 12.80 | 5.20 | keep | 9.52 | 9.48 | leave |
| 100 | 64.00 | 6.80 | keep | 1.98 | 2.02 | leave |
| 400 | 256.00 | 8.19 | keep | 0.50 | 0.51 | leave |

The simulation shuffles the bin and counts the items examined before the
first copy, with 20,000 draws per row (4,000 for the last two). The
closed form is exact.

**That the criteria disagree on every row is a fact of these parameters,
not a theorem.** With a deadline of 5, the row c = 20 both keeps and
carves. What is general is the direction: one criterion rises with c and
the other falls, so the copy counts where each says "make a bin" lie at
opposite ends. "Very few of but use often" ([CASE-094](../cases.d/CASE-094.md)) is the cell where
retrieval demands a bin and the evidence is weakest.

**Use frequency enters retrieval and not detection.** A bin pays when
the search it saves, summed over the retrievals expected, exceeds its
cost. If the bin is made when the item is found, as in [CASE-094](../cases.d/CASE-094.md), that cost
is little more than the bin. Detection does not depend on how often the
item is wanted. So the categories retrieval forces depend on the
system's tasks and deadlines as well as its data, which is [MOM-CLM-166](https://github.com/dmarx/mathematics-of-meaning/blob/main/record/claims.d/CLM-166.md)'s
reading of the parable: "the concepts are the ones the system's
deadlines forced it to build, and those are not derivable from the data
alone."

## Why it is Active

The two monotonicities are elementary, and both were checked: d'² and the
Occam term from [CLAIM-154](CLAIM-154.md)'s own statement, the search cost against a
simulation. The reading of them as two criteria, *entitled* to carve
against *must* carve, is [MOM-CLM-166](https://github.com/dmarx/mathematics-of-meaning/blob/main/record/claims.d/CLM-166.md)'s. Nothing here depends on how any
real person searches.

## What it does not say

- **Not that evidence does not matter.** A system carving by retrieval
  alone would make bins for distinctions that are not there. [MOM-CLM-166](https://github.com/dmarx/mathematics-of-meaning/blob/main/record/claims.d/CLM-166.md):
  a system "carves a category when the second fails, and it is
  *entitled* to carve one when the first succeeds."
- **Not that search is always serial.** m/(c+1) is a scan through items
  that must each be checked. Treisman and Gelade ([LIT-1082](../literature.d/LIT-1082.md)) found such
  scans where the wanted item differs from the others only in a
  combination of features. An item with a feature none of the others has
  ([CASE-094](../cases.d/CASE-094.md)'s black brick) was found almost regardless of their
  number. That is the case in which retrieval says no bin is needed. Their
  absent-target scans, about twice the per-item time of present-target
  ones, also make a failed search expensive to complete.
- **Not a psychological claim.** The parameters are MOM's, chosen to
  show the opposition, and nothing was measured.

## Note of 2026-10-15: a related case in graph indexes

In a proximity-graph index over clustered data, items in small isolated
clusters became unfindable when each new item was linked only to its
nearest neighbours, and findable when the linking rule kept links between
clusters ([THEORY-385](../theory.d/THEORY-385.md), Proposed: one set of the authors' own tests).
An arrangement fitted to the common case loses rare items that resemble
their neighbours, which is this claim's opposition in another medium. It
concerns links, not copy counts, and it was not built as a test of the
claim.
