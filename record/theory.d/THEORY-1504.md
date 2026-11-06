---
number: 1504
status: Active
formerly:
- THEORY-tmphrwgv
title: 'Grelu and Akhmediev hold that a dissipative soliton differs from a conservative one in being a single attractor rather than a member of a continuous family: a conservative soliton balances nonlinearity against dispersion alone, with its parameters selected by the initial data, whereas a dissipative soliton also needs an exact balance of gain and loss, kept by a continuous energy exchange with the environment and an internal flow from regions that gain energy to regions that lose it, so that its energy, profile and chirp are fixed by the system''s parameters, not by its initial conditions; such solitons can bind into robust molecules whose energy scales with the number of constituents'
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Promoted at the status review's ruling (the owner delegated these
    rulings), under ADR-065: the title reports what the source holds,
    read in full in NOTE-1688, and nothing in the record contradicts the
    report. Each clause of the title is the review's, at the pages
    NOTE-1688 cites. Its promote_when asked that the authors be right,
    which is more than the title asserts; it moves word for word to
    THEORY-1548, Proposed, which extends this entry (ADR-047 kind
    1). The old condition: A reading or computation showing, for the
    cubic–quintic complex Ginzburg–Landau equation at fixed parameters:
    (i) that localized initial conditions of differing energy converge
    to one profile whose energy, shape and chirp do not depend on the
    initial data; (ii) that the same solution decays when the gain terms
    are set to zero; (iii) that its phase is non-uniform, with the
    energy flow running from the regions where gain exceeds loss to
    those where loss exceeds gain; and (iv) a bound pair whose energy is
    close to twice the single soliton's. Set against it, the NLSE with
    the same conservative coefficients should give a family whose
    amplitude follows the initial data. The evidence should come from
    the numerical work the review cites (Soto-Crespo, Akhmediev and
    co-workers) or from a direct simulation, not from the review's own
    statements.
tags:
- natural-sciences
- complex-systems
date: '2026-11-06'
source:
- LIT-2196
bears_on:
- QUESTION-398
summary: >-
  Grelu and Akhmediev (2012), [LIT-2196](../literature.d/LIT-2196.md), read in full in [NOTE-1688](../notes.d/NOTE-1688.md)
  from the authors' manuscript on HAL. Held as a report of what the source holds, its truth left to THEORY-1548; the caveats: the review states the
  account and cites the simulations and experiments behind it without
  reproducing them. Its contrast with conservative solitons is with the
  integrable case; it does not say that a dissipative soliton exists only
  above a pump threshold, or that it is bistable or hysteretic.
---
<!-- inactive-ok-file: THEORY-1548 — Proposed; the wide form of this reading, split off by the status review of 2026-11-06 -->

# THEORY-1504: Grelu and Akhmediev hold that a dissipative soliton differs from a conservative one in being a single attractor rather than a member of a continuous family: a conservative soliton balances nonlinearity against dispersion alone, with its parameters selected by the initial data, whereas a dissipative soliton also needs an exact balance of gain and loss, kept by a continuous energy exchange with the environment and an internal flow from regions that gain energy to regions that lose it, so that its energy, profile and chirp are fixed by the system's parameters, not by its initial conditions; such solitons can bind into robust molecules whose energy scales with the number of constituents

## Source

Grelu & Akhmediev (2012), [LIT-2196](../literature.d/LIT-2196.md); read in [NOTE-1688](../notes.d/NOTE-1688.md). Manuscript
page numbers.

## What was actually shown

A review; it surveys, it does not demonstrate.

- **Family against attractor** (p. 4): in the conservative case a set of
  parameters "generally leads to a family comprising an infinity of soliton
  solutions", whereas "the attractor in a dissipative system is a fixed
  localised solution", its "energy, profile and chirp are predetermined by
  the equation parameters, rather than by the initial conditions". Fig. 1a
  draws the family as a curve and the dissipative solution as a point.
- **Exact gain–loss balance** (p. 3): it "should be exact in order to produce
  stationary localised solutions".
- **Exchange and internal flow** (p. 5): the soliton needs "distinct internal
  regions which extract energy from an external source" and others "where
  energy is lost into the environment"; the flow is proportional to the
  first temporal derivative of the phase.
- **Molecules** (p. 12): "dissipative soliton molecules are robust
  multi-soliton structures", their energy "proportional to the number of
  single-soliton constituents", against higher-order NLSE solitons whose
  energy goes as N² and which are easily destroyed.
- The model is the cubic–quintic CGLE (p. 6), non-integrable; the evidence
  behind each point is the cited simulations and experiments on lasers.

## What this does not say

- That every conservative soliton keeps its identity through collisions:
  the review says that of integrable solitons; conservative structures
  outside integrability are fragile in its account.
- That a dissipative soliton exists only above a pump threshold, or that it
  is bistable or hysteretic: none of these is discussed. The one threshold
  is on background fluctuations in soliton rain.
- That the soliton needs a finite seed to form; that is an inference from the
  model's linear loss, not the review's.
- Anything about merger or annihilation, slow decay, or topological
  protection.
- That the structure produces any of the conditions (cavity, absorber, gain
  medium) it depends on.
