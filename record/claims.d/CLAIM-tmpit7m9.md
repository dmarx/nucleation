---
status: Proposed
title: "A savings buffer is a stock of time: where shocks must be absorbed or a household is ruined, an investment that pays only after a delay is worth taking only above a buffer that rises with the delay, so households with the same preferences decline profitable delayed investments below it, a choice that reads as impatience and is the right policy for survival by a deadline; covering needs through the delay buys the time"
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the model: a household whose savings take steps of +1 or
  −1 with equal chance, ruined below zero, for which paying k now for
  G > k after L periods beats not paying at a buffer that does not rise
  with L, or for which covering shocks through the L periods does not
  lower that buffer. Not defeated by evidence that some poor households
  do discount the future more steeply, which the claim leaves open: it
  shows that a short horizon need not be read as a preference, not that
  it never is one.
tags:
- social-science
- mathematics
- society-and-governance
date: '2026-11-05'
line:
- readiness
- realizability
rests_on:
- CLAIM-595
uses:
- TERM-105
grounds:
- THEORY-tmp19alc
- THEORY-tmp5v6r5
- THEORY-tmpmcnzn
complements:
- CLAIM-tmpc3x0c
- CLAIM-tmpw4ai2
summary: >-
  The assistant's, after the owner read Haushofer and Fehr's finding,
  that deprivation produces short-sighted choices, as decision-making
  under a resource constraint: "deprivation induces added time pressure
  to the decision making process." In [TERM-105](../terms.d/TERM-105.md)'s terms a savings buffer
  is a replenishable reserve, and its depth sets a deadline: how many bad
  seasons the household can absorb before ruin. A toy shows the
  consequence. Savings move +1 or −1 each period, and the household can
  pay 3 now for 6 later. Investing raises survival over 40 periods only
  above a buffer of 4 when the payoff comes after 1 period, rising to 5,
  6, 9 and 14 at delays of 4, 9, 16 and 25. Below it, declining is right.
  Survival, the objective deprivation makes binding, needs a deeper
  buffer than expected wealth. At delay 16 and buffer 8, investing raises
  expected wealth from 8.15 to 10.30 and lowers survival from 0.846 to
  0.835. Covering shocks through the delay lowers the threshold to the
  outlay alone, which is what graduation programmes' consumption support
  does. The time pressure here is the planning horizon. Deliberation time
  and attention are a second sense, left to the scarcity readings. The
  wording is the assistant's (Claude, in this session); adopting it is
  the owner's call.
---
<!-- inactive-ok-file: CLAIM-595 CLAIM-tmpc3x0c CLAIM-tmpw4ai2 TERM-105 — Proposed or new; claims and a term this one rests on or extends, cited as open -->

# CLAIM-tmpit7m9: A savings buffer is a stock of time: where shocks must be absorbed or a household is ruined, an investment that pays only after a delay is worth taking only above a buffer that rises with the delay, so households with the same preferences decline profitable delayed investments below it, a choice that reads as impatience and is the right policy for survival by a deadline; covering needs through the delay buys the time

## The model

A household's savings w take a step of +1 (a good season) or −1 (a
shock) each period with equal chance. If w falls below 0 the household is
ruined, and ruin is absorbing. At the start it may pay k = 3 for a return
G = 6 that arrives L periods later. Over a horizon of T = 40 periods two
objectives are compared:
- **survival**, the chance of not being ruined by T;
- **expected wealth** at T, with ruined paths counted as 0.

scratch/formal/deprivation_horizon_toy.py reproduces and asserts every
number.

## The claim

1. **The buffer needed rises with the delay.** Investing raises survival
   only from a buffer of 4 when L = 1, rising to 5, 6, 9 and 14 at
   L = 4, 9, 16 and 25. For expected wealth the thresholds are 3, 4, 4,
   5 and 6. The investment is profitable throughout. What it costs is
   time spent exposed with a thinner buffer.
2. **Below the threshold, declining is right.** At w = 3 and L = 16,
   investing cuts survival from 0.467 to 0.188. A household that declines
   is not discounting the future. It is meeting the deadline its buffer
   sets.
3. **Deprivation changes which objective binds.** Survival needs a deeper
   buffer than expected wealth. At L = 16 and w = 8, investing raises
   expected wealth from 8.15 to 10.30 and lowers survival from 0.846 to
   0.835. This is [CLAIM-595](CLAIM-595.md)'s distinction between eventual success and
   success by a deadline, in a household. Near ruin, success by the
   deadline is what counts, and the policy that maximizes it is
   short-horizon.
4. **Covering needs through the delay buys the time.** If shocks are
   covered for the L periods before the payoff, as a consumption stipend
   would, the survival threshold at L = 16 falls from 9 to 3, which is the
   outlay alone. In the script the stipend comes with the investment, as
   in a graduation package.

## What it adds

- **To the owner's reading.** Deprivation adds time pressure in a
  precise sense: a shallow buffer is a short deadline, in [TERM-105](../terms.d/TERM-105.md)'s
  terms a replenishable reserve whose depth bounds how long any path may
  run at a loss. Behaviour that looks like impatience is what the deadline
  calls for.
- **To Haushofer and Fehr** ([NOTE-tmpv5r2w](../notes.d/NOTE-tmpv5r2w.md)). Their causal chain runs from
  poverty, through stress and negative affect, to short-sighted choices.
  This gives a second route to the same choices that needs no change in
  psychology, only a short horizon. The two are not exclusive, and the
  model does not say which dominates.
- **To Balboni et al.** ([NOTE-tmp6tzyt](../notes.d/NOTE-tmp6tzyt.md)). A buffer threshold that rises
  with an investment's delay is one way an asset threshold can arise
  without differences in ability or preference. Their finding that
  households above the threshold cut consumption at year 2, in order to
  invest, fits a household that can afford the exposure.
- **To graduation programmes** ([NOTE-tmpl3nvb](../notes.d/NOTE-tmpl3nvb.md)). Their months of
  consumption support cover needs while the transferred asset starts
  paying. On this model that is the component that buys the time.
- **To [CLAIM-tmpc3x0c](CLAIM-tmpc3x0c.md).** Support can be large enough in total and still
  fail if it leaves the household exposed through the delay. The
  condition on size is also a condition on timing.

## What it does not say

- **That the poor never discount steeply.** It shows that a short
  horizon need not be read as a preference, not that it never is one.
- **That deliberation time is the mechanism.** The time pressure modelled
  here is the planning horizon. Pressure on the time and attention
  available for a decision, the scarcity literature's sense, is a
  different resource, a capacity rather than a reserve. It is not
  modelled.
- **That the numbers fit any population.** The walk is symmetric and the
  returns are invented. A household with positive expected savings would
  have lower thresholds, and one with negative expected savings would have
  higher ones.
