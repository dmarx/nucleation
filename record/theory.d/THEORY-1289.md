---
number: 1289
status: Active
formerly:
- THEORY-tmp7jall
title: 'In a dynamical model anchored to an identified mechanism, holding one part''s variable fixed and finding that the phenomenon persists indicates that the part is not a component of the mechanism responsible for that phenomenon, as when Smolen et al. fixed CLOCK and circadian oscillation continued; the verdict is relative to the phenomenon and only as good as the model, and it decides which pathways the phenomenon needs, not which lie inside the system'
version: 1
history:
- version: 1
  date: '2026-11-01'
  note: >-
    Filed Active from NOTE-1492, the reading of Bechtel and
    Abrahamsen in full. The inference is elementary for a model, and the
    caveats are the paper's own (pp. 325–326). One exemplar; the paper
    does not report whether the clamp's verdict was confirmed in vivo.
tags:
- philosophy-of-science
- philosophy-of-biology
date: '2026-11-01'
source:
- LIT-1936
summary: >-
  Bechtel and Abrahamsen (2010), [LIT-1936](../literature.d/LIT-1936.md), contribution C3 (p. 326),
  read in [NOTE-1492](../notes.d/NOTE-1492.md). Smolen et al. (2001) fixed the concentration of
  CLOCK in a reduced model of the Drosophila clock, and oscillation
  continued. They concluded that the positive CLOCK loop "was not
  critical". That is a part that belongs to the system and not to "the
  responsible mechanism for that particular phenomenon". The clamp is an
  ideal intervention, cheap in a model and hard in vivo. It is not a test
  of where the system's boundary lies.
---
<!-- inactive-ok-file: CLAIM-530 — Proposed; the claim that a boundary is presupposed, cited as open -->

# THEORY-1289: In a dynamical model anchored to an identified mechanism, holding one part's variable fixed and finding that the phenomenon persists indicates that the part is not a component of the mechanism responsible for that phenomenon, as when Smolen et al. fixed CLOCK and circadian oscillation continued; the verdict is relative to the phenomenon and only as good as the model, and it decides which pathways the phenomenon needs, not which lie inside the system

## Source

Bechtel and Abrahamsen (2010), [LIT-1936](../literature.d/LIT-1936.md), §3.3, p. 326, reporting
Smolen, Baxter and Byrne (2001); read in [NOTE-1492](../notes.d/NOTE-1492.md).

## What was actually shown

- **The question.** The Drosophila clock has a negative loop, PER:TIM
  inhibiting CLOCK:CYCLE's activation of per and tim, and a positive loop,
  CLOCK promoting its own transcription. Does the positive loop "cancel
  out" the negative, or is it needed for oscillation (p. 326)?
- **The test.** Smolen et al. built a reduced model. PER and TIM were
  merged into one variable, and transport was replaced by a delay. It
  oscillated with a period of 23.6 h, robust to parameter changes. They
  then "fixed the value for CLOCK concentrations in the model. The model
  continued to generate oscillations", still robustly.
- **The reading (C3).** "A model can indicate which parts and operations of
  a system that have been identified empirically are essential for
  producing the phenomenon of interest, and therefore should count as
  components of the responsible mechanism." A reduced model makes it
  easier to see "which are components of the system but not of the
  responsible mechanism for that particular phenomenon".
- **Why in a model.** The same manipulation in vivo would need "a buffer,
  or otherwise stabilizing the concentration of CLOCK"; "such exploration
  is much easier to accomplish in a model".
- **What could have failed.** Oscillation could have stopped when CLOCK
  was clamped, as it would if the positive loop were needed.

## What this does not say

- **That CLOCK plays no role in the clock.** It is the transcriptional
  activator. What the clamp removes is the oscillation of CLOCK, the
  positive loop's contribution, not CLOCK itself.
- **That the verdict holds in the fly.** The model omits and merges parts.
  The paper's general caution applies: model experiments "do not show that
  the mechanism in fact could produce these effects" (p. 325).
- **That a part found necessary is inside the system.** The clamp tests
  whether the phenomenon needs a pathway. A pathway can be needed and
  located outside the boundary of the system said to have the phenomenon,
  as McClelland et al.'s externally supplied hippocampal training is
  needed for their model's consolidation (p. 331). Where the boundary
  runs is a separate input ([THEORY-1287](THEORY-1287.md), [CLAIM-530](../claims.d/CLAIM-530.md)).

## Connections

- **The record's knockouts.** "Removing the c₂ → c₁ production collapses
  both capacities" ([CASE-189](../cases.d/CASE-189.md)). "Removing any single production pathway
  sends all three to zero" ([CASE-189](../cases.d/CASE-189.md), Construction 2). The knockout in
  [CASE-190](../cases.d/CASE-190.md) is the same. Each is a C3 test in a model. Each shows that the
  maintenance phenomenon needs that pathway. Since the models stipulate
  which terms are internal, each shows nothing about whether the pathway
  is the organization's own.
- **[CLAIM-516](../claims.d/CLAIM-516.md).** Removing a feedback edge set extinguishes every capacity.
  That is C3 applied to every cycle at once, and proved rather than
  simulated.
- **[CLAIM-414](../claims.d/CLAIM-414.md) and [CLAIM-522](../claims.d/CLAIM-522.md).** The separating intervention in each is a
  clamp or knockout of a production pathway. This paper's C3 is the same
  move in a model of real biology.
