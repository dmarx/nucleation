---
number: 594
status: Proposed
formerly:
- CLAIM-tmp7y162
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
- CASE-216
bears_on:
- QUESTION-374
summary: >-
  The assistant's, on the owner's request of 2026-11-05 to connect the
  record's inquiry to DNA origami. The record's budgeted reachability holds
  the costs fixed and lets a budget admit more moves, so more budget never
  loses a state ([CLAIM-581](CLAIM-581.md), [CLAIM-570](CLAIM-570.md)). Heat in DNA origami folding is not
  such a budget: it pays for crossing barriers and also sets the free
  energies, raising entropic barriers and melting the target. In a
  four-state annealing toy with free energies linear in temperature
  ([CASE-216](../cases.d/CASE-216.md)), at most 90.4 % is folded at one hour, at
  318.6 K, at least 90 % at sixteen hours from 313 to 323.5 K, and a
  schedule of five minutes at 327 K then 318 K leaves 98.5 % folded at the
  hour; the chance of having reached the folded state agrees to four
  places. The readings filed beside it report the same shape in DNA
  origami: a narrow folding window and folding–melting hysteresis
  (Sobczak's dissertation), stepped schedules matching long ramps
  (Wagenbauer, Wachauf and Dietz), designs that fold better after rapid
  cooling and not after slow, and a nucleating intermediate (Schneider, Möritz and Dietz).
  The wording is the assistant's (Claude, in this session); adopting it is
  the owner's call.
---
<!-- inactive-ok-file: CLAIM-581 CLAIM-570 CLAIM-569 CASE-216 — Proposed; the fixed-cost claims this one qualifies and its construction -->

# CLAIM-594: When the resource that pays for crossing barriers also sets the costs it pays, as heat does when DNA origami folds, reaching a target within a time budget is not monotone in the resource: the target is reached only in a window of levels that more time widens, and a schedule of levels can reach what no constant level reaches; budgeted reachability with fixed costs, where more budget never loses a reachable state, is the special case of a resource that leaves the costs unchanged

## The claim

Let a system's moves have costs c(m; θ) that depend on a level θ of some
resource, and let a time budget t be spent on top. For fixed costs,
[CLAIM-581](CLAIM-581.md)'s threshold structure holds: the states reached within a
budget form an up-set in the budget, and their classes nest into one
tree. Three things change when θ also sets the costs.

1. **Reachability is not monotone in θ.** A higher θ can raise some
   barriers and remove the target, so the levels at which the target is
   reached within t can form a window rather than everything above a
   threshold.
2. **The window depends on t.** For the chance of having reached the
   target by t, more time can only widen the window. For the fraction
   folded at t it need not, since a target can melt again; in the toy it
   widens because the folded state holds. More time widens it, because barriers that
   cannot be crossed in an hour can be crossed in sixteen. So θ and t do
   not combine into one scalar budget.
3. **A schedule can beat every level.** A path through levels θ₁ then θ₂
   can reach, within t, a target no constant θ reaches within t: a level
   that makes a precursor without a trap, then a level that completes the
   target from the precursor.

All three are shown by [CASE-216](../cases.d/CASE-216.md), computed with python3 -I.

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

- **That temperature is consumed.** The claim's "resource" is a level θ of
  a controlled condition, not a consumable budget. Heat sets rates and
  equilibria together; time is what is spent.

- **That the record's fixed-cost claims are wrong.** [CLAIM-581](CLAIM-581.md) and
  [CLAIM-570](CLAIM-570.md) hold when the costs do not depend on the budget. This claim
  marks their scope.
- **That DNA origami folds by the toy's mechanism or at its numbers.** The
  toy is chosen to show the effect. The readings show the shape, not the
  mechanism.
- **Anything new to annealing practice.** Folding windows and stepped
  protocols are the origami literature's own results. What is new here is
  only what they mean for the record's resource-bounded reachability.
- **That every resource is like heat, or that only heat is.** Other
  resources in DNA origami also set the costs they pay, but not all the same
  way. Staple excess has a window of its own: for a single fold, yield falls
  as excess rises, because two staple molecules can each take one end and
  block the fold (Majikes et al. 2021). That window is an equilibrium share,
  which a slower anneal did not change, so more time does not widen it, as it
  does for heat. Magnesium speeds proper folding and aggregation together
  (Douglas et al. 2009).
  Which organizational resources reshape the landscape they pay for, the
  way funding can change the incentives it is spent against, is open
  ([QUESTION-374](../questions.d/QUESTION-374.md)).

## Note of 2026-11-05: the further DNA origami readings

The works cited in A's two syntheses on DNA origami, pasted by the owner on 2026-11-05, read in this pull request.

**Douglas et al., "Self-assembly of DNA into nanoscale three-dimensional shapes".** Douglas et al. (2009), [LIT-2130](../literature.d/LIT-2130.md), roughly support the time-widens part
(longer ramps raise yield at fixed Mg2+) and add a second, non-thermal
non-monotone resource: Mg2+ at 4 mM gives gross defects, and more Mg2+
raises proper folding and aggregation together, implying a usable Mg2+
window (the reader's inference; the text names no upper failure point
within 0–30 mM). Whether more time widens the Mg2+ window is not shown. No
status changes.

**Majikes et al., "Failure Mechanisms in DNA Self-Assembly".** Majikes et al. (2021), [LIT-2133](../literature.d/LIT-2133.md), are a parallel case on another
resource: staple excess has a window (peak near 1–5×, falling below 50% at
high excess), but at the single fold this is an equilibrium effect, not a
time-budget one (a twofold slower anneal gives the same trend), so the
claim's heat-and-barrier mechanism is not what drives it. No status
changes.

No status changes.

## Note of 2026-11-05: the readings on correction, repair, replication and nucleation barriers

Read at the owner's invitation to add readings to the DNA origami filing; the works were chosen by the assistant.

**Cumberworth, Frenkel and Reinhardt, "Design-dependent nucleation barriers".** Supports from simulation. Temperature sets whether a nucleation barrier exists at all: the three-row barrier is present at Tm and "disappears after a few degrees" below it. A barrier-keeping isothermal protocol must sit in that window, as the authors propose. Left open: no kinetics or yields are simulated.

No status changes.
