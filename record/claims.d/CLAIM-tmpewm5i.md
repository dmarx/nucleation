---
status: Proposed
title: "Decay of correlation between blocks is not weak interaction between them, so a finite correlation length does not make a system nearly decomposable in Simon's sense; near-decomposability is a condition on coupling strengths, which large blocks of a short-range system meet at a critical point too"
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A short-range system in which large blocks fail Simon's condition, the
  interactions between blocks not becoming weak against those within them
  as the blocks grow, because of how correlated the system is; or a
  showing that THEORY-661's near-decomposability is a condition on
  correlation rather than on interaction strengths. Not defeated by the
  failure of THEORY-661's consequence, fast dynamics inside parts against
  slow dynamics between them, at a critical point: that failure goes
  through time scales, as the body says.
tags:
- complex-systems
- natural-sciences
date: '2026-11-21'
line:
- formal-apparatus
grounds:
- THEORY-661
complements:
- CLAIM-478
- CLAIM-626
summary: >-
  The finding that ARG-tmp09yqc records as a failed route, stated as a
  claim of its own so that entries can build on it, as TERM-tmpol232 and
  the note of 2026-11-21 on SYNTHESIS-054 do (ADR-tmp44npm; the owner's
  "go with your lean", 2026-11-21). Simon's near-decomposability
  (THEORY-661) is about interaction strengths: interactions within
  subsystems much stronger than between them. A correlation length
  measures statistical dependence. In a system with short-range
  interactions, a block of side L in d dimensions has interactions across
  its boundary in number of order L^(d−1) against L^d inside, so large
  blocks meet Simon's condition whatever the correlation length, at a
  critical point as elsewhere. So a finite correlation length is not what
  gives near-decomposability, and an unbounded one does not take it away.
  What does fail at a critical point is THEORY-661's consequence, the
  separation of fast dynamics inside parts from slow dynamics between
  them, because relaxation inside a block slows with its size (CLAIM-626);
  the loss of separable levels at criticality goes through time scales,
  not coupling. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: ARG-tmp09yqc TERM-tmpol232 ADR-tmp44npm CLAIM-478 CLAIM-626 CLAIM-tmpjbee7 — Proposed, Rejected or new; the route this states the finding of, and its users -->

# CLAIM-tmpewm5i: Decay of correlation between blocks is not weak interaction between them, so a finite correlation length does not make a system nearly decomposable in Simon's sense; near-decomposability is a condition on coupling strengths, which large blocks of a short-range system meet at a critical point too

**The claim.** Two properties that are easily run together come apart:

- **Weak interaction between blocks** (THEORY-661): the couplings that act across a block's boundary are weak against those inside it.
- **Decay of correlation between blocks**: what happens in one block says little about another, which a finite correlation length ξ gives for blocks much larger than ξ.

Near-decomposability, in Simon's sense, is the first. A finite correlation length is the second.

**The step, checked.** Take short-range interactions on a d-dimensional lattice, and a cubic block of side L. The bonds inside number of order L^d, and those across the boundary of order L^(d−1). Their ratio is of order 1/L, whatever the temperature or the correlation length. So for large blocks the interaction across the boundary is weak against that inside, which is Simon's condition, at a critical point (ξ unbounded) as elsewhere. (The counting is exact for nearest-neighbour bonds: 2·d·L^(d−1) of them cross the boundary, against d·L^(d−1)(L−1) inside.)

**What does fail at criticality.** THEORY-661 draws a consequence from the condition: each subsystem's short-run behaviour is approximately independent, and fast dynamics inside parts separate from slow dynamics between them. That consequence needs a block to relax internally faster than the influence from outside arrives. Near a critical point, relaxation inside a block slows with its size, τ ∝ L^z for L < ξ (dynamic scaling, cited in CLAIM-626's note). Large blocks then no longer relax quickly. So the separation of levels that criticality removes (CLAIM-tmpjbee7) is lost through time scales, not through coupling. That is the same window in time as CLAIM-478's.

**Why it is held as a claim.** It was first recorded as the reason a route failed: A13 §9's bridge from a finite correlation length to Simon's condition (ARG-tmp09yqc, Rejected). Two entries already build on it as a positive finding: TERM-tmpol232, the senses of separation, and the note of 2026-11-21 on SYNTHESIS-054. Under ADR-tmp44npm a finding entries build on is held as a claim, not only inside a Rejected argument.

The wording is the assistant's (Claude, in this session); adopting it is the owner's call.
