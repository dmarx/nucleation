---
status: Proposed
title: 'Twenty folding cells and three actuators: with each actuator driving a fixed group of cells, the configurations the actuators can command form a three-dimensional slice of the twenty-dimensional set the mechanism admits, and which profiles lie in it is fixed by the grouping, not the count'
version: 1
standing: fictional
kind: construction
tags:
- control-theory
- mathematics
- operations-research
date: '2026-11-05'
line:
- distributed-agency
illustrates:
- CLAIM-tmp675a9
summary: >-
  A's proposal, from the pasted synthesis on constraint architectures
  (pasted by the owner on 2026-11-04, continuing the exchange on emergency
  readiness whose share link could not be fetched), Part 4: "Suppose a
  structure contains twenty foldable cells, but only three independently
  driven actuators." A's model is q̇ = G(q)u, F(q)=0, ‖u‖ ≤ U_max, with
  m < n inputs. The grouping (cells 1–7, 8–14 and 15–20, one actuator
  each) and the profiles are the filer's. The commanded configurations
  are a three-dimensional slice of the twenty-dimensional set; a uniform
  profile lies in it, a step at cell 10 does not, and a regrouping of the
  same three actuators puts the step in and other profiles out. "A
  capability can exist kinematically without being practically
  controllable." The construction is the filer's, from A's limited budget
  of control authority; adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmp675a9 CASE-194 — Proposed; the record's claim that placement predicts better than count, and its case of one shared actuator setting, cited as filed -->

# CASE-tmpe3itu: Twenty folding cells and three actuators: with each actuator driving a fixed group of cells, the configurations the actuators can command form a three-dimensional slice of the twenty-dimensional set the mechanism admits, and which profiles lie in it is fixed by the grouping, not the count

## The case

**A's model.** A: "Suppose a structure contains twenty foldable cells,
but only three independently driven actuators. It may be mechanically
possible for the structure to assume many shapes, yet impossible to
control every folding angle independently." With q ∈ ℝ^n the folding
angles and u ∈ ℝ^m the inputs, m < n:

  q̇ = G(q)u,  F(q) = 0,  ‖u‖ ≤ U_max.

A's design problem: choose G and a policy π to minimize
C_actuators(G) + C_control(π) subject to every required configuration
being realizable.

**The filer's instance.** n = 20, m = 3. Each cell is a
one-degree-of-freedom unit whose angle may lie anywhere in [0, θ_max], so
the mechanism admits a twenty-dimensional box of configurations. Actuator
1 drives cells 1–7, actuator 2 cells 8–14, actuator 3 cells 15–20, each
cell in a group taking its actuator's angle. G is constant, a 20 × 3
matrix of zeros and ones with one 1 per row, and from the flat state the
commanded configurations are

  q = G u,  u ∈ [0, θ_max]^3, ‖u‖ ≤ U_max:

a three-dimensional slice of the box, since G has rank 3.

- **The uniform profile**, every cell at θ, is u = (θ, θ, θ): commanded.
- **A step at cell 10**, cells 1–10 at θ and 11–20 at 0, needs cells 8–10
  and 11–14 at different angles under one actuator: not commanded, for
  any U_max. It is admissible, so kinematically possible, and not
  controllable.
- **Regrouped**, the same three actuators on cells 1–10, 11–15 and 16–20
  command the step and lose profiles the first grouping had, such as
  cells 1–7 at θ and 8–20 at 0.
- **Commanding every profile** needs rank 20: twenty actuators.

Checked by the filer.

## What it can show

- **That the binding resource is control channels, not material.** A:
  "The resource limitation here is not the amount of material. It's the
  number, strength, and placement of independent control channels."
  Number sets the slice's dimension, strength (U_max) its extent, and
  placement (G) which profiles it holds. The last is the point of
  [CLAIM-tmp675a9](../claims.d/CLAIM-tmp675a9.md), here with no folding branches at all: at a fixed count
  the grouping decides what is reachable. Stern, Pinson and Murugan find
  the same in self-folding sheets ([NOTE-tmp9dvve](../notes.d/NOTE-tmp9dvve.md)), "spatial placement of
  actuators is a much better predictor of folding success than just the
  number of actuators".
- **That coupling economizes on actuators when the targets fit it.** A:
  "coupling several folds can let one actuator coordinate many movements.
  Constraint architecture can therefore economize on scarce control
  resources." If every required profile is constant on the three groups,
  three actuators do the work of twenty. Liu, Zhang and Fang
  ([NOTE-tmp2mkll](../notes.d/NOTE-tmp2mkll.md)) group the cells of an origami spring to share
  actuators: "the same arrangement of drivers can realize multiple
  distinct spatial configurations", and for a sinusoid a "structure with
  only 2 actuators is insufficient for accurate approximation". Dollar
  and Howe's hand ([NOTE-tmpb0ok0](../notes.d/NOTE-tmpb0ok0.md)) spends the gap differently, leaving
  joints unactuated and compliant so that contact chooses the shape: "An
  adaptive, underactuated hand has fewer actuators than degrees of
  freedom."
- **A's organizational reading.** "An organization can possess many
  possible configurations while having only limited authority to select
  among them." The cells are the configurations the organization admits;
  the actuators are the channels by which it can choose among them.

## What it cannot show

- **That m < n always confines the reachable set.** It does here because
  G is constant: the inputs integrate to Gu, a fixed subspace. When the
  input fields vary with q, motion around loops of inputs can reach
  directions no single input provides. Murray and Sastry ([NOTE-tmpygch2](../notes.d/NOTE-tmpygch2.md)):
  "Roughly speaking, Chow's theorem states that if we can move in every
  direction using Lie bracket motions (possibly of higher order than
  one), then the system is controllable." The count bounds the slice only
  for coupling like this case's, where each group is held to one angle.
- **Anything about cost** within the slice. Equal rank does not fix
  effort ([CLAIM-345](../claims.d/CLAIM-345.md)).
- **That organizations have such a G.** The mapping from authority to
  input channels is A's analogy; [CASE-194](CASE-194.md) gives one organizational
  failure of a shared actuator setting, as a construction.
