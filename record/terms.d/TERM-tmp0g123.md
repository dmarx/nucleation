---
status: Proposed
title: 'stabilization, in the control-theoretic sense: the damping of perturbations and convergence to what is expected, an equilibrium, a set or a stationary law; contraction is a sufficient condition for it, and attraction toward a convention is one case of it'
version: 1
tags:
- complex-systems
- design-rationale
- mathematics
date: '2026-11-21'
line:
- nucleating-argument
- record-as-apparatus
- formal-apparatus
draws_on:
- THEORY-2043
complements:
- TERM-tmp7m4at
- TERM-132
summary: >-
  The owner's sense, 2026-11-21: "I'm using 'stabilization' in the control
  theoretic sense, it isn't a narrow term of art describing attraction
  specifically towards conventions, the attraction toward a convention is
  a manifestation of a more general 'stabilization' process. I'm using
  stability to mean the damping of perturbations and convergence to
  expectation." The definition's wording, and its relation to contraction,
  are the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: THEORY-2043 TERM-132 CLAIM-068 CLAIM-772 CLAIM-tmp8v75o TERM-tmp7m4at — Proposed; the contraction reading, the terms and claims this is stated against, and those filed with it on 2026-11-21 -->

# TERM-tmp0g123: stabilization, in the control-theoretic sense: the damping of perturbations and convergence to what is expected, an equilibrium, a set or a stationary law; contraction is a sufficient condition for it, and attraction toward a convention is one case of it

## Definition

A process **stabilizes** a state, a set of states or a law when perturbations
away from it are damped and the process converges to it: it is what the
process is expected to be in after a perturbation. Stabilization is
**asymptotic** when every perturbation in a region decays and **exponential**
when it decays by at least a fixed factor per step or unit of time. It can be
partial: a process can damp perturbations in some directions and leave others
**neutral**, neither damped nor magnified, so that it converges to a set and
moves freely inside it.

Two relations fix the term against the record's others:

- **Contraction is a sufficient condition.** A step that contracts in some
  metric damps the difference between any two trajectories, so all of them
  converge together ([THEORY-2043](../theory.d/THEORY-2043.md), Lohmiller and Slotine): incremental
  stabilization. [CLAIM-772](../claims.d/CLAIM-772.md)'s one contraction is a mechanism of
  stabilization, not another name for it.
- **Attraction toward a convention is one case.** Repeated reconstruction
  pulled toward conventional regions ([CLAIM-068](../claims.d/CLAIM-068.md)) stabilizes the convention.
  The same process stabilizes whatever the step's fixed points are: a
  convention, a source's value, or the set of versions an entry's
  predicates allow ([CLAIM-tmp8v75o](../claims.d/CLAIM-tmp8v75o.md)).

For an entry of the record, its predicates ([TERM-tmp7m4at](TERM-tmp7m4at.md)) stabilize the
dimensions they constrain: a perturbation off the allowed set is damped,
wholly by a hard predicate and by a factor 1/(1 + λ) per step by a soft one
of strength λ ([CLAIM-tmp8v75o](../claims.d/CLAIM-tmp8v75o.md), part 4). The dimensions no predicate
constrains are neutral; they are [TERM-132](TERM-132.md)'s local degrees of freedom.

## Not to be confused with

- **Attraction toward a convention** in particular. The record has used
  "stabilized" for that ([CLAIM-068](../claims.d/CLAIM-068.md)); in this term it is one case.
- **Stopping changing.** A process that has stopped can be unstable, with
  the next perturbation growing; and a stable process can keep moving in its
  neutral directions. That an entry has stopped changing does not show what
  stopped it ([CLAIM-768](../claims.d/CLAIM-768.md)).
- **Viability.** A stable regime can lose access to trajectories that keep
  satisfying its constraints ([CLAIM-079](../claims.d/CLAIM-079.md)). Stabilization says perturbations
  decay, not that what they decay to is good.
