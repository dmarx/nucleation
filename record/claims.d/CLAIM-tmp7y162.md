---
status: Proposed
title: 'When the resource that pays for crossing barriers also sets the costs it pays, as heat does when DNA origami folds, reaching a target within a time budget is not monotone in the resource: the target is reached only in a window of levels that more time widens, and a schedule of levels can reach what no constant level reaches; budgeted reachability with fixed costs, where more budget never loses a reachable state, is the special case of a resource that leaves the costs unchanged'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the construction: a recomputation of the four-state toy with
  its stated parameters that finds the target reached within the hour above
  some threshold temperature and at every temperature above it, or a
  constant temperature that reaches 95 % within the hour; or a proof that,
  for Arrhenius kinetics whose free energies and barriers depend on
  temperature, the set of states reached within a time budget is monotone
  in temperature. Not defeated by evidence that real DNA origami folds
  differently from the toy, which bears on the empirical reading below,
  not on the claim.
tags:
- natural-sciences
- mathematics
- complex-systems
date: '2026-11-05'
line:
- realizability
- formal-apparatus
complements:
- CLAIM-581
- CLAIM-570
- CLAIM-569
grounds:
- CASE-tmpa6s9d
bears_on:
- QUESTION-374
summary: >-
  The assistant's, on the owner's request of 2026-11-05 to connect the
  record's inquiry to DNA origami. The record's budgeted reachability holds
  the costs fixed and lets a budget admit more moves, so more budget never
  loses a state (CLAIM-581, CLAIM-570). Heat in DNA origami folding is not
  such a budget: it pays for crossing barriers and also sets the free
  energies, raising entropic barriers and melting the target. In a
  four-state annealing toy with free energies linear in temperature
  (CASE-tmpa6s9d), the target is reached within an hour only near
  318.6 K, best 90.3 %, within sixteen hours from 313 to 323.5 K, and a
  schedule of five minutes at 327 K then 318 K reaches 98.5 % within the
  hour. The readings filed beside it report the same shape in DNA
  origami: a narrow folding window and folding–melting hysteresis
  (Sobczak's dissertation), stepped schedules matching long ramps
  (Wagenbauer, Wachauf and Dietz), designs that fold better after rapid
  cooling and not after slow, and a nucleating intermediate (Schneider, Möritz and Dietz).
  The wording is the assistant's (Claude, in this session); adopting it is
  the owner's call.
---
<!-- inactive-ok-file: CLAIM-581 CLAIM-570 CLAIM-569 CASE-tmpa6s9d — Proposed; the fixed-cost claims this one qualifies and its construction -->

# CLAIM-tmp7y162: When the resource that pays for crossing barriers also sets the costs it pays, as heat does when DNA origami folds, reaching a target within a time budget is not monotone in the resource: the target is reached only in a window of levels that more time widens, and a schedule of levels can reach what no constant level reaches; budgeted reachability with fixed costs, where more budget never loses a reachable state, is the special case of a resource that leaves the costs unchanged

## The claim

Let a system's moves have costs c(m; θ) that depend on a level θ of some
resource, and let a time budget t be spent on top. For fixed costs,
CLAIM-581's threshold structure holds: the states reached within a
budget form an up-set in the budget, and their classes nest into one
tree. Three things change when θ also sets the costs.

1. **Reachability is not monotone in θ.** A higher θ can raise some
   barriers and remove the target, so the levels at which the target is
   reached within t can form a window rather than everything above a
   threshold.
2. **The window depends on t.** More time widens it, because barriers that
   cannot be crossed in an hour can be crossed in sixteen. So θ and t do
   not combine into one scalar budget.
3. **A schedule can beat every level.** A path through levels θ₁ then θ₂
   can reach, within t, a target no constant θ reaches within t: a level
   that makes a precursor without a trap, then a level that completes the
   target from the precursor.

All three are shown by CASE-tmpa6s9d, computed with python3 -I.

## Why DNA origami

In thermal annealing, temperature is the textbook budget for crossing
barriers, kT ln(νt) of barrier per unit of time, and it is also the
parameter of every free energy, G = H − TS. The readings filed beside this
claim report each of the three points in origami:

- **A window.** Sobczak's dissertation: folding "can only occur in a
  narrow temperature window"; a brick object is mostly folded after 2 h at
  50 °C, while at 6 °C higher there are "absolutely no folded origamis
  even after 48 hours"; and "a significant hysteresis of 5 C to 10 C
  between folding and unfolding".
- **Time and level interact.** Dannenberg et al.'s domain-level model:
  faster cooling lowers the assembly temperature by 5.3 °C and raises the
  melting temperature by 1.3 °C.
- **A schedule.** Wagenbauer, Wachauf and Dietz: a 1.5 h schedule of three
  temperature steps matched a 16 h ramp, while hours at one temperature
  never did. Sobczak's dissertation: a short-domain design folded at 40 °C
  with "significantly higher" yield and rate when cooled from 65 °C by
  shock-freezing, and not at all when the cooling step was slowed.
- **A precursor.** Schneider, Möritz and Dietz: early nucleating domains
  form a compacted intermediate before the folded state.

## What it does not say

- **That the record's fixed-cost claims are wrong.** CLAIM-581 and
  CLAIM-570 hold when the costs do not depend on the budget. This claim
  marks their scope.
- **That DNA origami folds by the toy's mechanism or at its numbers.** The
  toy is chosen to show the effect. The readings show the shape, not the
  mechanism.
- **Anything new to annealing practice.** Folding windows and stepped
  protocols are the origami literature's own results. What is new here is
  only what they mean for the record's resource-bounded reachability.
- **That every resource is like heat.** Staple excess, for instance, mostly
  admits more without reshaping much (Rothemund), though not entirely.
  Which organizational resources reshape the landscape they pay for, the
  way funding can change the incentives it is spent against, is open
  (QUESTION-374).
