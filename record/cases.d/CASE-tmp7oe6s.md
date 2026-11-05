---
status: Proposed
title: 'In A''s branching assembly model, one unit of supply placed on the nucleating step or on the completing step gives yields 71.1 and 62.7 %, and the same total supply delivered early, evenly or late gives 70.6, 58.8 and 24.8 % when nucleation uses it, but 45.4, 58.8 and 65.3 % when it traps the unnucleated scaffold and completes the nucleated one'
version: 1
standing: fictional
kind: construction
tags:
- complex-systems
- mathematics
- natural-sciences
date: '2026-11-05'
line:
- realizability
- readiness
illustrates:
- CLAIM-562
- CLAIM-tmpt0fnx
summary: >-
  The assistant's construction of the case A proposes in its fourth
  synthesis on DNA origami, pasted by the owner on 2026-11-05: "Two
  equal-cost nucleating interventions with identical target compatibility
  but different assembly yields", together with A's Prediction 5, on the
  order of allocation at equal total expenditure. A's model is used (U →
  N at α, U → K at β, N → F at γ, N → K at δ; baseline 1, 0.5, 2, 0.25),
  with F and K absorbing. A unit of a component's supply doubles the rate
  of the step that component takes part in. The target and its
  compatibility are the same in every arm. Computed with python3 -I by
  matrix exponentials over a horizon of 4. Whether early or late supply
  is better turns on which steps the supplied component enters, which is
  CLAIM-tmpt0fnx's point in time instead of amount. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-tmpj3cmd CLAIM-562 CLAIM-tmpt0fnx — Proposed, Skimmed or new; entries cited as open -->

# CASE-tmp7oe6s: In A's branching assembly model, one unit of supply placed on the nucleating step or on the completing step gives yields 71.1 and 62.7 %, and the same total supply delivered early, evenly or late gives 70.6, 58.8 and 24.8 % when nucleation uses it, but 45.4, 58.8 and 65.3 % when it traps the unnucleated scaffold and completes the nucleated one

## The case

A's branching model (CASE-tmpj3cmd) at its baseline, eventual yield
59.3 %.

**Placement at equal cost.** One extra unit of supply doubles the rate of
the step its component takes part in:

| Placed on | Eventual yield |
|---|---|
| nucleation, α × 2 | 71.1 % |
| completion, γ × 2 | 62.7 % |

**Timing at equal total supply.** A supply profile c(t) on [0, 4] with
∫c dt = 4: front-loaded (2 then 0), even (1 throughout) or delayed (0 then
2). Yield at the horizon:

| The supplied component enters | front-loaded | even | delayed |
|---|---|---|---|
| nucleation (α ∝ c) | 70.6 % | 58.8 % | 24.8 % |
| nucleation and trapping from N (α, δ ∝ c) | 64.1 % | 58.8 % | 22.6 % |
| trapping from U and completion (β, γ ∝ c) | 45.4 % | 58.8 % | 65.3 % |

## What it can show

- **A's proposed case.** Two interventions of equal cost, the same target,
  different yields. Placement matters at equal quantity, as CLAIM-562
  holds for actuators.
- **Order matters at equal expenditure.** This is A's Prediction 5:
  "Two policies can have identical cumulative expenditure ... while
  inducing different formation probabilities".
- **The sign of the order effect is not general.** A warns that "It would
  be incorrect to conclude generally that early expenditure is better.
  Early support could stabilize a trap." The third row is that case.
  Supply that binds an unnucleated scaffold into a trap is best withheld
  until the nucleus has formed. Which order helps depends on which steps
  the supply enters in the state the system is in when it arrives. That
  extends CLAIM-tmpt0fnx from how much supply to when.

Being fictional, with A's invented rates, it shows the logic, not its size
in DNA origami. Wah et al. 2016 changed staple concentrations and so the
folding path, but they did not test equal-total timing.
