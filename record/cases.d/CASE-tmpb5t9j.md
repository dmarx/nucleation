---
status: Proposed
title: 'A positively curved origami vertex: its popped-up and popped-down states lie in components that no rigid, non-self-intersecting motion joins, so no budget reaches one from the other, and only widening the admissible moves reconnects them'
version: 1
standing: documented
kind: specimen
tags:
- mathematics
- natural-sciences
date: '2026-11-05'
line:
- distributed-agency
- formal-apparatus
illustrates:
- CLAIM-tmpbi4ca
- CLAIM-tmp9jvpb
variant_of:
- CASE-tmpe48yq
reported_in:
- LIT-tmp24k66
- NOTE-tmpt066u
summary: >-
  Filed at the owner's request on 2026-11-05, to file "one or more CASEs
  for origami as a toy model of a resource bounded constraint
  configuration space". Berry, Lee-Trimble and Santangelo (NOTE-tmpt066u)
  show that near the flat state a rigid vertex with small positive
  Gaussian curvature, faces forbidden to pass through each other, has its
  popped-up and popped-down nappes in disconnected components; Foschi,
  Hull and Ku (NOTE-tmpt4jsa) find degree-4 modes disconnected whenever
  the sector angles do not sum to 2π. With no admissible path, the
  bottleneck budget is infinite for every resource and every budget. The
  authors report, anecdotally, that letting faces pass through each other
  reconnects the nappes; Jules et al. (NOTE-tmpwz8jy) give a second
  instance, states reached only by a move outside the loading protocol.
  The case where no budget helps and only the admissible-move set does. A
  mechanical specimen; its organizational reading is an analogy.
  Adopting it is the owner's call.
---
<!-- inactive-ok-file: NOTE-tmpt4jsa — Skimmed; Foschi, Hull and Ku, read in part -->
<!-- inactive-ok-file: CLAIM-tmpbi4ca CLAIM-tmp9jvpb TERM-tmp2ysyt CASE-tmpe48yq CASE-tmpez9ok — Proposed; the entries filed beside it on 2026-11-05, cited as filed, nothing here rests on their being settled -->

# CASE-tmpb5t9j: A positively curved origami vertex: its popped-up and popped-down states lie in components that no rigid, non-self-intersecting motion joins, so no budget reaches one from the other, and only widening the admissible moves reconnects them

## The case

**The specimen.** A single rigid origami vertex whose sector angles sum to
a little less than 2π, so that it carries a small positive Gaussian
curvature K = 2π − Σα_i (Berry, Lee-Trimble and Santangelo,
NOTE-tmpt066u). Faces are flat and rigid and may not pass through each
other, which the authors implement as fold angles strictly inside
(−π, π). Unlike CASE-tmpe48yq's vertex, it has no flat state: a vertex
whose sector angles do not sum to 2π cannot have every fold angle zero at
once (Foschi, Hull and Ku, NOTE-tmpt4jsa).

**What is reported.** Near the flat state the vertex's second-order
isometry condition is hᵀQh = K, with one negative eigenvalue in Q. At
K = 0 this is a double cone whose two nappes, popped up and popped down,
touch at the flat state. For K > 0 it is a two-sheeted hyperboloid, and
the nappes "have split into two disconnected components". For K < 0 they
stay joined by a neck, except at degree 4, where they are split for both
signs. Tracing a symmetric 5-fold vertex numerically, the authors find
the nappes touching, disconnected or joined by a narrow neck as K is
zero, positive or negative. Foschi, Hull and Ku reach the degree-4
disconnection from exact equations, in a worked example.

**The resource reading (the filer's).** Take any resource r on
configurations and any budget b. The bottleneck budget of CLAIM-tmpbi4ca
is the least, over admissible paths from a popped-up state to a
popped-down one, of the largest r on the path, and +∞ when there is no
such path. Here there is none. So B* = +∞ whatever r is declared, every
budget leaves the two nappes in different components, and the
reconfiguration slack (TERM-tmp2ysyt) is infinite. Raising the budget
changes nothing; no resource is being rationed.

**Widening the moves.** The separation rests on the move set. The
authors contrast Streinu and Whiteley, who find the configuration space
connected, and note that "in their analysis, faces can pass through each
other". They add: "Anecdotally, it does appear that when faces are
allowed to pass through each other, isometric trajectories can pass from
one nappe to the other for any K." The paper's abstract, as the reading
quotes it, puts the alternative as tearing: there is "no pathway between
them without tearing the origami". Both widenings are unavailable to a
sheet of paper. Within the declared moves the separation is absolute;
across a wider class it may vanish.

**A second instance.** Jules et al.'s stack of Kresling barrels
(NOTE-tmpwz8jy) is a memory whose 16 states are all reachable under
uniaxial loading with the ends clamped against rotation. Twisting parts
of the stack by hand reaches defect states that no loading protocol
reaches, and the load, once applied, leaves them only by erasing or
shifting the defect. There the wider move is available, to a hand; here
it is not available at all.

## What it can show

- **CLAIM-tmpbi4ca's infinite case**, in a real mechanism: each nappe's
  states are feasible, and no budget of any resource joins them.
- **That reachability is relative to the declared moves**, as
  CLAIM-tmp9jvpb says it is: the same states are disconnected under rigid,
  non-self-intersecting motion and, reportedly, connected once faces may
  pass through each other.
- **A separation that is not frustration.** Every configuration on each
  nappe meets every constraint, so no demand set is jointly
  unsatisfiable, and TERM-060's structural frustration does not apply.
  CLAIM-347's compatibility complex does not see the separation; the
  reading of the paper says as much.
- **A kinematic, not an energetic, separation**, for QUESTION-281: no
  energy suffices to cross it without tearing. Contrast CASE-tmpe48yq,
  where a finite budget crosses, and CASE-tmpez9ok, where widening the
  moves is itself priced.
- **An analogy, the filer's.** An organization may face a transition that
  no amount of money, staff or time buys under its present rules, only a
  change in what counts as an admissible move. The specimen shows the
  logical shape; it says nothing about which organizations face one.

## What it cannot show

- **Anything about organizations.** It is a mechanical specimen, and the
  organizational reading is an analogy.
- **Global facts.** The results are local to the flat state, for small
  |K|; the several-vertex statement is conditional, and which
  combinations of nappes can be realized is open.
- **That passing faces through each other reconnects the nappes.** That
  is the authors' anecdote, not a result.
- **What a widening of the moves would cost.** Tearing or
  self-intersection is not priced; the case only shows that the budget
  is the wrong lever.
