---
status: Proposed
promote_when: >-
  An independent kTAM simulation or analysis, or an experiment with DNA
  tiles, reproduces all three of the following: the change in the
  speed/error scaling from ε² to ε¹ for 2×2 proofreading near the melting
  transition; the shortfall from ε^(2/K) at K = 3; and the attribution of
  that shortfall to growth on facets.
title: 'Winfree and Bekbolatov show, in kinetic Tile Assembly Model simulation and kinetic-trap theory, that replacing each tile of a tile set with a K×K block whose internal bonds are unique keeps the logical assembly unchanged but forces any mismatch to stall until it dissociates, raising the optimal speed for a target error ε from r ≈ βε² to r ≈ βε at K = 2; their thermodynamic argument predicts an error rate exponential in K, and the simulated gain beyond K = 2 falls short of it, which they attribute to facet-roughening errors that proofreading does not correct'
version: 1
tags:
- natural-sciences
- complex-systems
date: '2026-11-05'
source:
- LIT-tmp1pdwj
summary: >-
  Winfree and Bekbolatov (2004), [LIT-tmp1pdwj](../literature.d/LIT-tmp1pdwj.md), read in [NOTE-tmppy063](../notes.d/NOTE-tmppy063.md) from
  the authors' submitted preprint. Simulation and kinetic-trap theory,
  with trap rates fitted and no rigorous proof. It does not say that
  proofreading has been shown in DNA, that its gain is exponential in
  practice, or that it corrects every error: growth on facets, nucleation
  of boundaries and implementation errors are outside it.
---
# THEORY-tmpxgxmn: Winfree and Bekbolatov show, in kinetic Tile Assembly Model simulation and kinetic-trap theory, that replacing each tile of a tile set with a K×K block whose internal bonds are unique keeps the logical assembly unchanged but forces any mismatch to stall until it dissociates, raising the optimal speed for a target error ε from r ≈ βε² to r ≈ βε at K = 2; their thermodynamic argument predicts an error rate exponential in K, and the simulated gain beyond K = 2 falls short of it, which they attribute to facet-roughening errors that proofreading does not correct

## Source

Winfree and Bekbolatov (2004), [LIT-tmp1pdwj](../literature.d/LIT-tmp1pdwj.md); read in [NOTE-tmppy063](../notes.d/NOTE-tmppy063.md).

## What was actually shown

- **The baseline** (§2, Fig. 5): direct tile sets lie above r ≈ βε², because
  a mismatch is "frozen in place by further growth" before it leaves.
- **The mechanism** (§3, Figs. 6d, 7): in a K×K block there is no compatible
  continuation of a single mismatch, so "The assembly process stalls, giving
  time for the initial mismatched tile to fall off and be replaced by a
  correct tile"; every path to a mismatch has at least two unfavourable
  steps.
- **The gain** (§§2–3, Fig. 5): fitted exponents of ε about 1.0 for 2×2 and
  0.89 for 3×3; at fixed conditions errors of 1%, 0.01% and 0.001% for 1×1,
  2×2 and 3×3.
- **The prediction and its shortfall** (§3): ε ≈ e^{-KGse} gives
  r ≈ βε^{2/K}, but "the simulation results for K = 3 (figure 5) and K = 4
  (data not shown) fall short of the prediction", which the authors put
  down to "spontaneous growth on a facet".
- **Could have come out otherwise**: blocks could have changed nothing, as a
  pre-assembled block would not (footnote 11); the simulated kTAM showed the
  stall at work.

## What this does not say

- That proofreading works in DNA: no experiment is reported.
- That the gain is exponential in K in practice.
- That it corrects facet errors, nucleation of boundaries, or errors of
  implementation such as unequal bond strengths, none of which it treats.
- That the trap models are derived: their freezing rates are fitted, with
  "no strong justification" (footnote 9).
