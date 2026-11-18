---
status: Proposed
title: 'Same claim, two procedural paths: a claimant certain to win 100 at judgment, with 50 to spend at 10 a month, nets 60 if judgment takes four months and nothing if the defendant can stretch it to seven, so an offer it would refuse becomes one it accepts with its preferences and the merits unchanged; with relief arriving at a constant hazard, halving the claimant''s runway from eight months to four cuts its chance of relief from 86 to 63 per cent, and a cost that moves the cheapest route to relief past the claimant''s budget removes the whole remedy'
version: 1
standing: fictional
kind: construction
tags:
- game-theory
- mathematics
- society-and-governance
date: '2026-11-17'
line:
- dependence-and-domination
- distributed-agency
bears_on:
- QUESTION-tmpcz1ui
summary: >-
  A's constructions, A61 §2 to §3 and A64 §2 to §10 of the exchange
  "Assess Depp Heard Abuse" (2026-11-16), at the owner's U28 (litigation
  dragged out "in an effort to bankrupt their opposition") and U29
  ("flesh this out further leveraging formal constructions as much as
  possible"). Every number was rechecked with python3 -I in the session's
  scratchpad. Three of A's statements are corrected below: the coupled
  depletion model does not create "a reinforcing process"; the
  descriptive condition A calls "one sufficient condition" is written as a
  biconditional; and the vulnerability gap is not nonnegative as defined.
  Fictional, with illustrative parameters. Proposed because the
  constructions are A's; adopting them is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpyo35b CLAIM-tmpbqunx — filed from the same exchange, Proposed or new -->
<!-- inactive-ok-file: CLAIM-679 — Proposed; the record's nearest construction, cited with its standing -->

# CASE-tmphljcr: Same claim, two procedural paths: a claimant certain to win 100 at judgment, with 50 to spend at 10 a month, nets 60 if judgment takes four months and nothing if the defendant can stretch it to seven, so an offer it would refuse becomes one it accepts with its preferences and the merits unchanged; with relief arriving at a constant hazard, halving the claimant's runway from eight months to four cuts its chance of relief from 86 to 63 per cent, and a cost that moves the cheapest route to relief past the claimant's budget removes the whole remedy

## The model

A64 of the exchange (https://chatgpt.com/share/6afcb46d-83a8-83e9-9c85-4a0c3604405b).
B asserts a claim against A, seeking a corrective objective J through an
adjudicative arrangement G. Each party i holds accessible resources K_i,
replenished at f_i and spent at c_i:

    K̇_i = f_i − c_i,     τ_i = inf{t : K_i(t) < m_i(t)},

where m_i is the reserve needed for the next required step. τ_i is "a
*litigation-exhaustion time*, not necessarily bankruptcy." With constant
net depletion and m = 0, τ_i = K_i(0)/(c_i − f_i). A's strategy u_A
enters B's spending, c_B(t, u_A, π_B), and the time to relief, T_J(u_A,
π_B, G); B fails to reach relief by that route when τ_B(u_A) < T_J(u_A).

## The constructions, rechecked

- **Runway** (A61 §2). A claimant with $60,000 spending $10,000 a month
  lasts 6 months; a defendant with $4,000,000 at $20,000 lasts 200; the
  case is expected to take 24.
- **Liquidity** (A61 §3). B has an 80 per cent chance at $1,000,000 and
  $250,000 of costs to go: 0.8 × 1,000,000 − 250,000 = $550,000 expected.
  A offers $150,000. B can raise only $60,000, so it cannot pursue the
  better route and accepts. "**the stronger party may obtain concessions
  not by changing what the weaker party believes is just, but by changing
  what the weaker party can afford to pursue**".
- **Two procedural paths** (A64 §4). B is certain to win 100 at judgment,
  has 50 of funding and spends 10 a month, so lasts 5 months. On the
  ordinary path judgment takes 4 months and B nets 100 − 40 = 60. On the
  extended path it takes 7, which B cannot finance; abandoning yields 0.
  A's cost is 8 + 100 = 108 on the ordinary path and 15 on the extended
  one, so the threat to extend is credible. "Yet the claimant's effective
  reservation value has fallen from 60 to zero." **A's Proposition 2**,
  with V_B^cont(u) = max{0, sup over feasible π_B of E[W_J − C_B]}: if
  V_B^cont(u_1) < V_B^cont(u_0), an offer B would refuse under u_0 can be
  one it accepts under u_1, with no change in B's preferences. That
  follows from the acceptance rule alone: "It requires only a change in
  the claimant's feasible alternatives."
- **The race between relief and exhaustion** (A64 §5). If relief arrives
  at a constant hazard λ, T_J ~ Exponential(λ), then Pr(T_J ≤ τ_B) = 1 −
  exp(−λK_B(0)/(c_B − f_B)). At λ = 0.25 a month, the chance of relief is
  39.3, 63.2, 77.7, 86.5, 91.8 and 95.0 per cent at runways of 2, 4, 6, 8,
  10 and 12 months, all as A gives them; cutting the runway from 8 months
  to 4 costs 23.3 points. The derivative in net spending c,
  −(λK_B(0)/c²) exp(−λK_B(0)/c), is negative, and agrees with a numerical
  difference.
- **The threshold** (A64 §6). With C_B^J(u) the least B must spend to
  reach J under A's conduct u, C_B^J(u_0) ≤ K_B < C_B^J(u_1) makes J
  reachable under u_0 and not under u_1. A's proof, from the definition of
  the minimum, is correct. Its instance: enforcement needs $98,000, B has
  $100,000, A adds $5,000 of unnecessary expense, and $103,000 exceeds the
  budget, so a 5 per cent burden removes the whole remedy. A calls this
  "**threshold-mediated amplification**".

## Corrections

- **No reinforcing process.** A64 §7 couples depletion to operational
  disruption D_B:

      K̇_B = f_B^0 − γD_B − c_B(u_A),     Ḋ_B = ηu_A − ρD_B,

  and says "That creates a reinforcing process." It does not. D_B depends
  on A's strategy and not on B's reserves, so for a constant u_A it
  settles at ηu_A/ρ and B's replenishment falls to f_B^0 − γηu_A/ρ and
  stays there. Depletion speeds up and then levels off: a bounded drag.
  (With η = 1, ρ = 0.5, γ = 0.4, f_B^0 = 2 and c_B = 1 + u_A at u_A = 1,
  dK_B/dt goes from −0.31 at one month to −0.80 for good.) A reinforcing
  loop needs falling reserves to raise disruption or spending, for
  instance Ḋ_B growing as K_B falls; the model has no such term.
- **Sufficient, not equivalent.** A64 §10 introduces attritional
  foreclosure with "Formally, one sufficient condition is:" and writes
  AF(B, J) ⟺ τ_B < T_J. A sufficient condition is τ_B < T_J ⟹ AF(B, J).
  The biconditional would make exhaustion the only route to foreclosure,
  which A's own text (no affordable alternative route, other bottlenecks)
  denies.
- **The vulnerability gap can be negative.** A64 §9 defines worst-case
  adversarial correctability, α̲_J = inf over u_A in 𝒰_A^adm of sup over
  π_B of Pr(T_J ≤ H, T_J < τ_B(u_A)), and the gap 𝒱_J = α_J^baseline −
  α̲_J, read as "A large positive gap". The gap is nonnegative only when
  the baseline course is one of A's admissible strategies (or is matched
  by one), for then the infimum is at most the baseline value. As defined,
  the baseline is a procedure, not one of A's strategies, so a baseline
  less favourable to B than every admissible strategy gives a negative
  gap. The fix is to require u_0 ∈ 𝒰_A^adm. [CLAIM-tmpbqunx](../claims.d/CLAIM-tmpbqunx.md) (F4, from A76 and
  A81) files the adversarial quantity itself.
- **The offer is arbitrary.** On A64 §4's extended path B's alternative is
  0, so any positive offer is accepted; on the ordinary path any offer of
  60 or more. A's offer of 10 illustrates; nothing in the model picks it.
- **No materiality threshold.** A64 §10's Siege_N has the disjunct
  ΔV_B < 0, which any loss satisfies, where the prose says "materially
  impair".

## What it shows

- **For [CLAIM-tmpyo35b](../claims.d/CLAIM-tmpyo35b.md).** A party's conduct can move a corrective objective
  out of an opponent's reach with the merits, the law and the opponent's
  preferences fixed: by raising its spending, by delaying relief, or by a
  small cost at a threshold. [CLAIM-tmpyo35b](../claims.d/CLAIM-tmpyo35b.md) grounds on this.
- **Beside [CLAIM-679](../claims.d/CLAIM-679.md).** The threshold is [CLAIM-679](../claims.d/CLAIM-679.md)'s structure with an
  adversary: a cut in the resource held removes exactly the transitions
  whose requirement lies between the old holding and the new. A64 §6
  points at "Nucleation's work on slack and reconfiguration capacity"
  without the code.

## What it does not show

- That courts work this way. A: "This is a constructed result under
  restrictive assumptions, not an empirical estimate"; the hazard model "is
  not a model fitted to actual court durations."
- That the burden was unjustified. A valid discovery demand can cross the
  same threshold (A64 §6), and τ_B is treated as known while T_J is random.
- That the stronger party is the defendant. A64 §14: "Our model must be
  role-symmetric."
