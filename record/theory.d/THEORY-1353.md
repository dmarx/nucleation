---
number: 1353
status: Proposed
formerly:
- THEORY-tmpbwwow
promote_when: >-
  An independent group, on models and code not the author's, replicates
  the three fingerprints the title names: formation time flat across total
  circuit size at a fixed number of missing parts in a task with no subset
  signal; single-part ablation of identified circuits leaving well below
  the 1 − 1/K partial-credit level with non-part controls near intact; and,
  on an aged substrate, a query–key-only re-initialization restoring
  learnability of a withheld capability where doubling its data
  concentration and a value-only re-initialization do not. Failure of any
  one refutes that clause.
title: 'Circuits form when last parts align at once'
statement: >-
  In transformer language models to about 1B parameters, a conjunction
  circuit forms when its last missing parts align together in one stochastic
  attempt, with no credit for partial alignment, so its formation time
  depends on how many parts are missing and not on its size, and ablating
  one part collapses the capability; plasticity loss is the same law read
  backward, a depletion of uncommitted attention heads that more data cannot
  undo and re-initializing query–key weights can
version: 1
tags:
- learning-theory
- representation-learning
- complex-systems
- anthology-candidate
date: '2026-11-04'
source:
- LIT-2006
rivals:
- THEORY-213
- THEORY-293
summary: >-
  Dong (2026), read in [NOTE-1540](../notes.d/NOTE-1540.md). One rate equation, sites × attempts
  × drive × e^(−βK) minus destruction, with K the missing parts. Forward,
  a capability ignites above a data-concentration floor that is a
  saddle–node; backward, plasticity loss is site depletion, silent in the
  loss and repaired by a query–key reset; and no native SGD knob is a
  temperature. Evidence: a toy grid, ablation on Pythia (32 of 32 cells
  below partial credit, 22 of 32 on the preregistered criterion) and six
  seeds for the reset. Proposed: single-author, unreplicated, mixing
  unproved.
---
<!-- inactive-ok-file: THEORY-2015 THEORY-2027 — Proposed; cited in this filing of 2026-11-19 -->

# THEORY-1353: Circuits form when last parts align at once

## Source

Dong (2026), [LIT-2006](../literature.d/LIT-2006.md), read in [NOTE-1540](../notes.d/NOTE-1540.md).

## What was actually shown

- **Missing parts, not size**, in a controlled toy grid of 46 cells: "a
  five-part circuit missing three waits as long as a three-part circuit
  missing three" (§4.4, p. 10). This could have come out the other way:
  under accumulating partial credit the larger circuit waits longer.
- **Ablation collapse** on Pythia across seven capabilities and three
  scales: "32 of 32 cells fall below" each cell's partial-credit
  prediction; the stricter preregistered criterion "passes 22 of 32"
  (§9, p. 27).
- **Plasticity loss is site-limited**: doubling the drive fails, and
  "re-initializing only the query–key slices 6/6" against value and
  output 0/6, on aged Pythia-70M (§7, p. 21). Theorem 1 proves, in a gated
  model with oracle gating, that the deadline is invisible in the loss.

## What this does not say

- **Not that training is thermal nucleation.** No native knob passes the
  paper's temperature test; formation is "athermal, driven nucleation"
  (§5, p. 12).
- **Not that the exponential in K is measured on real models.** Directly
  measured K spans 2–4, over which exponential, power and linear fits are
  indistinguishable (Remark 5), and β ≈ 0.23 on real models.
- **Not beyond about 1B parameters,** whatever the abstract's "1.4B", nor
  beyond conjunction circuits of attention heads.
- **Not that a query–key reset is free.** Whether background skills
  survive it is not reported.

## Note of 2026-11-19: readings for the exchange "Topological protection explained"

Dohare and colleagues ([THEORY-2027](THEORY-2027.md)), read: supports the depletion reading of plasticity loss, independently of Dong's attention-head account. They find loss of plasticity with dead units, growing weights and falling effective rank, name its root cause as the benefits of random initialization "lost over time", and repair it by reinitializing low-utility units, the same kind of act as Dong's query–key reset. Their networks are small and their setting continual learning, so the title's clauses on conjunction circuits and attention heads are not tested.

Han and colleagues ([THEORY-2015](THEORY-2015.md)), read: related, not the same construct. Higher pretraining weight decay lowers the rank of query–key products more than value–projection ones, and improves fine-tuning. That puts plasticity-relevant structure in the query–key product, as Dong's query–key reset does. Neither paper tests the other's intervention, and the authors call their rank mechanism correlational, so the entry's plasticity clause is left open.

No status change.

## Note of 2026-11-19: Liu, Neubig and Xiong, read
A parallel ([NOTE-2154](../notes.d/NOTE-2154.md)): both locate a loss of malleability late in Pythia-family training; Liu and colleagues' is behavioural, inferred from when specialized data is introduced, and confounded with the learning-rate schedule.
