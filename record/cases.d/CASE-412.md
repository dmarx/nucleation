---
number: 412
status: Active
formerly:
- CASE-tmpo8bsc
title: 'A matched-performance model of regulation run under six budget regimes: every regime produces the same output until a contingency arrives, while readiness at a deadline of six periods ranges from 0.147 to 0.894; a redesigned route is lost under the peak rule unless a reserve is also held, a drill each period holds the budget as a reserve does, readiness is a step function of the reserve, the reserve is most ready at every deadline but cheapest only at some, and it pays above a break-even that moves with the deadline and with how often the capability is used'
version: 3
history:
- version: 1
  date: '2026-11-23'
  note: >-
    Filed 2026-11-23 by the assistant, for the manuscript
    governance-of-possibility (its gap GC1 and join JC1). The model,
    sweep, tests and outputs are under
    scratch/manuscripts/governance-of-possibility/analysis/, the single
    copy, run at commit 28a3708c1 and reproduced.
- version: 2
  date: '2026-11-24'
  note: >-
    Promoted to Active at the owner's word of 2026-11-24 ("promote the
    ten", under the dialectic regime; ADR-057, status-review README
    section 2): a CASE goes Active when it is demonstrated, and its run
    has been checked by a session other than its filer's. The study was
    run and reproduced at filing; the fact-check of the manuscript
    governance-of-possibility, by a reader who did not write it
    (2026-11-23), reran study.py in a copy (results.json reproduced in
    every field but runtime_s, results.md identical) and its 24 tests
    (all pass); this pass reran it again on 2026-11-24 from a copy, with
    the same result. The wording is unchanged but for the summary's
    sentence on its standing, which said it "stays Proposed until a
    status review rules that it is demonstrated".
- version: 3
  date: '2026-11-25'
  note: >-
    Gains the line governing-possibility (atlas scope 14) under ADR-
    tmpd3ckn: the entry is in that scope's core fiber in the hyperarticle
    atlas v0.3 (scratch/atlas/atlas-v0.3.md), and each atlas scope is
    documented as a line. No other change.
standing: documented
kind: executed-study
tags:
- operations-research
- society-and-governance
- probabilistic-modeling
date: '2026-11-23'
illustrates:
- CLAIM-577
- CLAIM-1099
- CLAIM-878
- CLAIM-1180
bears_on:
- QUESTION-395
variant_of:
- CASE-315
line:
- readiness
- formal-apparatus
- realizability
- governing-possibility
summary: >-
  The executed study behind §9 of the manuscript governance-of-possibility,
  carrying out the design of [LEAD-226](../leads.d/LEAD-226.md) on [CASE-315](CASE-315.md)'s simulator idea.
  Two configurations held at 1 are joined by an original path of peak 3 and
  a redesigned, slower path of peak θ′ = 2. Six regimes (peak rule; a floor
  at 3; redesign under the peak rule; redesign with a floor at θ′; redesign
  with a drill each period; capped carry-over) and three controls are run
  over 8 seeds of 4,000 periods and 2,000 imposed contingencies each. Output
  is matched by construction, [CLAIM-577](../claims.d/CLAIM-577.md)'s and [CLAIM-1099](../claims.d/CLAIM-1099.md)'s conditions
  hold exactly, and readiness, cost ranking, the reserve's break-even and
  the step function come out as stated here, on choices the body names.
  It was run and reproduced; a status review ruled it demonstrated on 2026-11-24. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---

<!-- inactive-ok-file: CLAIM-922 CLAIM-584 CLAIM-654 CLAIM-646 CLAIM-1137 CASE-200 CASE-345 — Proposed or new; the claims this study illustrates or bears on, the simulator it extends, its novel-demand variant and the account that maps it -->

# CASE-412: A matched-performance model of regulation run under six budget regimes: every regime produces the same output until a contingency arrives, while readiness at a deadline of six periods ranges from 0.147 to 0.894; a redesigned route is lost under the peak rule unless a reserve is also held, a drill each period holds the budget as a reserve does, readiness is a step function of the reserve, the reserve is most ready at every deadline but cheapest only at some, and it pays above a break-even that moves with the deadline and with how often the capability is used

## The study

**Where it comes from.** The motivating draft of the manuscript
governance-of-possibility set three regimes side by side and stated their
outcomes as "analytical outcomes under stipulated assumptions". [LEAD-226](../leads.d/LEAD-226.md)
gives the design for running them: "Extend the readiness simulator with a
redesign arm, a sweep of reserve sizes between holding cost and threshold,
and a harm absent from the demand specification introduced mid-run". It
builds on [LEAD-080](../leads.d/LEAD-080.md)'s simulator, run as [CASE-315](CASE-315.md). This case is that study,
less its novel-demand arm, which is [CASE-397](CASE-397.md).

It varies [CASE-315](CASE-315.md) in a stated respect. It keeps that study's peak
accounting of the budget, its drill, its partial-rollover and [CASE-200](CASE-200.md)
rules, and its seeding, and does not modify its code. It drops the rescue
squad, its skill and its arrivals. In their place it puts a graph of
configurations with two paths between them, so that a redesign and a
reserve sweep can be run. The model has no competence that decays, so it
isolates [CLAIM-577](../claims.d/CLAIM-577.md)'s mechanism from [CASE-343](CASE-343.md)'s.

**The model.**
- **Configurations and paths.** A and B are each held at r = 1. The
  original path runs A → M → B with r(M) = 3, over two edges. The redesigned
  architecture adds a staged path A → S1 → S2 → B with r(S) = θ′, over three
  edges. Each edge completes with chance 0.5 a period and occupies the
  larger r of its two ends while it is crossed. A path's threshold is its
  peak, and an architecture's is the least over its paths ([CLAIM-571](../claims.d/CLAIM-571.md)).
- **Budget rules.** Peak: B′ = s ([CLAIM-577](../claims.d/CLAIM-577.md)). Floor: B′ = max(s, F), a
  reserve of F − 1, which can lapse to the peak rule with a per-period
  hazard. Carry: B′ = min(3, 1.5 + (B − s)), [CASE-200](CASE-200.md)'s rule with a cap.
- **Regimes.**

  | Regime | Path | Budget rule |
  |---|---|---|
  | I | original | peak |
  | II | original | floor 3 |
  | III-a | redesigned | peak |
  | III-b | redesigned | floor θ′ |
  | IV | redesigned | peak, with a drill each period at θ′ |
  | V | original | carry |

  Controls: II and III-b with a reserve that lapses (0.005 a period), and
  IV drilling every second period (the negative control).
- **Contingency.** Each period, with chance p, demand switches to the other
  configuration. The organization takes the fastest affordable path. If
  none is affordable, outside money arrives with chance 0.1 a period and
  raises the budget to the least threshold, [CLAIM-577](../claims.d/CLAIM-577.md)'s minimum outside
  money. A response later than the deadline τ costs L; a reserve costs c
  per unit above holding per period. Output is 1 in a period with no
  contingency pending and 0 otherwise.
- **Readiness** R(t) is measured under an imposed contingency after 50
  quiet periods ([TERM-115](../terms.d/TERM-115.md)'s do(c)), 2,000 per regime, and pairs of curves
  are classed by first-order dominance for t from 0 to 40, tolerance 0.02.
- **Reference values.** p = 0.02, θ′ = 2, L = 50, c = 0.1. Long runs: 8
  seeds of 4,000 periods, with common random numbers across regimes.

**The run.** Made on 2026-11-23 by `python3 -I study.py` with the code as
committed in 28a3708c1, and re-run by the coordinator before committing;
the outputs reproduced exactly except the runtime, and a second
reproduction matched again. The 21 tests in `test_model.py` pass, among
them [CLAIM-577](../claims.d/CLAIM-577.md)'s and [CLAIM-1099](../claims.d/CLAIM-1099.md)'s exact conditions and the negative
control. The same directory holds `test_speed_noise.py`, whose three tests
are for [CLAIM-1137](../claims.d/CLAIM-1137.md) and are not part of this study.

**One copy.** The data and scripts are in
scratch/manuscripts/governance-of-possibility/analysis/ (`model.py`,
`study.py`, `test_model.py`, `results.json`, `results.md` and a README
that says how to rerun them). That directory is the only copy. This case
cites it and copies nothing from it but the figures quoted below, all
from `results.md` or `results.json`.

## Results

**Present output is matched, by construction.** Every regime and control
produces 1.0000 a period before the first contingency, and 1 in every
period when there is none (tested). Output does not depend on the budget
except through how fast a contingency is met, so the match is built in and
is no evidence. Once contingencies arrive the regimes come apart:

| Regime | output overall | capacity above holding | mean response |
|---|---|---|---|
| I | 0.7868 | 0.171 | 12.76 |
| II | 0.9183 | 2.000 | 4.13 |
| III-a | 0.7578 | 0.117 | 14.83 |
| III-b | 0.8820 | 1.000 | 6.11 |
| IV | 0.8820 | 1.000 | 6.11 |
| V | 0.9158 | 1.941 | 4.25 |
| II, reserve lapsing | 0.7924 | 0.241 | 12.47 |
| III-b, reserve lapsing | 0.7668 | 0.149 | 14.53 |
| IV, drill every second period | 0.7623 | 0.124 | 14.72 |

**[CLAIM-577](../claims.d/CLAIM-577.md) and [CLAIM-1099](../claims.d/CLAIM-1099.md) hold exactly.** The tests check that under
the peak rule the budget never rises; that one holding period forecloses
every route whose threshold exceeds 1; that a redesigned route is kept
under the peak rule exactly when θ′ ≤ 1 (θ′ in {1, 1.25, 1.5, 2, 2.5, 3});
and that a floor F keeps a route exactly when F is at least its threshold
(F from 1 to 3 in steps of 0.25). The draft's redesigned regime, with an
"accessible transition capacity" of 2, is III-b, a reserve of 1. Without
that reserve it is III-a, and its route is lost like I's. These checks are
of the model; they add no warrant to claims already demonstrated.

**Readiness under an imposed contingency** (θ′ = 2):

| Regime | t = 2 | t = 3 | t = 4 | t = 6 | t = 8 | t = 12 | t = 20 |
|---|---|---|---|---|---|---|---|
| I | 0.025 | 0.081 | 0.146 | 0.267 | 0.395 | 0.607 | 0.845 |
| II | 0.237 | 0.492 | 0.673 | 0.894 | 0.961 | 0.997 | 1.000 |
| III-a | 0.000 | 0.011 | 0.044 | 0.147 | 0.269 | 0.508 | 0.792 |
| III-b | 0.000 | 0.118 | 0.304 | 0.647 | 0.855 | 0.974 | 1.000 |
| IV | 0.000 | 0.118 | 0.304 | 0.647 | 0.855 | 0.974 | 1.000 |
| V | 0.237 | 0.492 | 0.673 | 0.894 | 0.961 | 0.997 | 1.000 |

- **II is the most ready at every deadline.** II and V are equal and
  dominate every other regime; II dominates III-b and IV, which are equal.
- **III-a is dominated by every other regime, I included.** The minimum
  outside money buys the cheapest route, which after redesign is the slower
  staged one, so redesign without a reserve does worse than none.
- **I and III-b cross** (sign change at t = 3). At t = 2, I with outside
  money (0.025) is ahead of III-b (0), because the staged route cannot
  finish in fewer than three periods; from t = 3 on III-b is ahead. This is
  [CLAIM-922](../claims.d/CLAIM-922.md)'s deadline effect, the budget saved paid for in time, as in
  [CASE-345](CASE-345.md).

**The drill is a reserve under peak accounting.** IV's budget sits at θ′
because each period's drill sets that period's peak. Its capacity cost
equals III-b's (1.000 against 1.000), and its readiness curve is identical
at every deadline. What differs is what breaks each:
- a lapsing reserve does not touch the drill, while under lapse II's R(6)
  falls from 0.894 to 0.752 and III-b's from 0.647 to 0.535;
- skipping a drill loses the route: drilling every second period gives
  R(6) = 0.147, the same as III-a (the negative control, which fails as
  predicted).

**The cost ranking moves with the deadline.** Long-run cost is c × reserve
+ L × late rate, at the reference values:

| τ | by readiness | by long-run cost |
|---|---|---|
| 2 | II > V > I > III-a > III-b > IV | I < III-a < II < V < III-b < IV |
| 3 | II > V > III-b > IV > I > III-a | II < V < I < III-a < III-b < IV |
| 4 | II > V > III-b > IV > I > III-a | II < V < I < III-b < IV < III-a |
| 6 | II > V > III-b > IV > I > III-a | II < V < III-b < IV < I < III-a |
| 8 | II > V > III-b > IV > I > III-a | II < V < III-b < IV < I < III-a |
| 12 | II > V > III-b > IV > I > III-a | III-b < IV < V < II < I < III-a |
| 20 | II > III-b > IV > V > I > III-a | III-b < IV < I < V < III-a < II |

At τ = 2 I is cheapest (0.8203 a period against II's 0.975): the reserve
costs more than the lateness it saves, though II is far readier there. II
is cheapest from τ = 3 to 8. At τ = 12 and 20, III-b and IV cost 0.0812
and 0.100 a period less than II before any redesign cost, which bounds the
amortized redesign cost that would pay.

**The reserve's break-even.** A reserve (II against I) pays when p·L
exceeds pL*, the value at which c times the extra capacity held equals L
times the fall in late contingencies a period. From the long runs, at
c = 0.1:

| p | τ = 3 | τ = 6 | τ = 12 |
|---|---|---|---|
| 0.005 | 0.579 | 0.363 | 0.625 |
| 0.01 | 0.63 | 0.394 | 0.571 |
| 0.02 | 0.701 | 0.401 | 0.565 |
| 0.05 | 1.15 | 0.502 | 0.689 |

- It is linear in c: at τ = 6 and p = 0.02, 0.2 at c = 0.05 and 0.802 at
  c = 0.2. The set of p·L at which the reserve is preferred is closed
  upward (tested).
- It is not a function of p·L and c alone. It is U-shaped in τ, lowest
  where the deadline lies between the reserve's transit time and the wait
  for outside money.
- It rises with p at τ = 3 and τ = 6, because under the peak rule a
  transition just made leaves the budget at its peak for a period, which
  is [CLAIM-878](../claims.d/CLAIM-878.md)'s mechanism (a use is a mobilization). At τ = 12 it does not
  move monotonically.
- The approximation c·Δcap/ΔR(τ) with readiness under do(c) is loose: at
  τ = 6 it gives 0.268 to 0.311 where the long runs give 0.363 to 0.502,
  and 0.409 at τ = 3, p = 0.05, where they give 1.15. Readiness observed
  in operation is not readiness under an imposed contingency.

**Readiness is a step function of the reserve.** Swept from 0 to 2 in
steps of 0.25, every reserve strictly between two path thresholds gives
exactly the readiness of the threshold below it, identical under common
random numbers. In the original architecture R(6) is 0.269 for every
reserve from 0 to 1.75 and 0.907 at 2; in the redesigned one, 0.151 from 0
to 0.75, 0.664 from 1 to 1.75 and 0.907 at 2. The only reserves worth
holding are the thresholds less holding: 0, θ′ − 1 and 2. This is the
converse of [CLAIM-679](../claims.d/CLAIM-679.md), as its note of 2026-11-23 states.

**A reserve is general within its budget, a redesign specific to its
path.** II's budget of 3 serves any transition with threshold at most 3;
III-b's and IV's budget of 2 serves only those at most 2. The novel-demand
variant, [CASE-397](CASE-397.md), shows the difference on a route the specification
did not name, and [CLAIM-1180](../claims.d/CLAIM-1180.md) states it for one capacity usable
anywhere.

## What depends on the modeller's choices

- **The staged route is slower**, three edges to two. If it were as fast,
  III-b would match II at every deadline with half the reserve, and the
  crossing of I and III-b would go.
- **Outside money buys the cheapest route**, not the fastest. If it bought
  the fastest, III-a would match I, and redesign without a reserve would
  stop being worse than none ([CLAIM-1099](../claims.d/CLAIM-1099.md)'s note of 2026-11-23).
- **The carry rule is capped at 3.** Without the cap V's budget would grow
  without bound in quiet periods.
- **The policy reads the budget.** The organization takes the fastest
  affordable path, so here more budget is never slower. [CLAIM-654](../claims.d/CLAIM-654.md) shows
  that need not hold, and the step function assumes it.
- **Every rate and cost is invented.**

What does not depend on them: [CLAIM-577](../claims.d/CLAIM-577.md)'s and [CLAIM-1099](../claims.d/CLAIM-1099.md)'s conditions,
the step function within its scope, the equality of drill and reserve
under peak accounting, and the matched output. Each follows from the
budget rule and the thresholds. What is the study's own is the rest: III-a
below I, the cost ranking, pL* and how it moves, and the size of the
divergence.

## What it can show

- That [CLAIM-577](../claims.d/CLAIM-577.md)'s mechanism, [CLAIM-1099](../claims.d/CLAIM-1099.md)'s objection and [CLAIM-878](../claims.d/CLAIM-878.md)'s
  drill run together in one model of a regulated organization, the join
  the manuscript calls JC1, and that their exact conditions hold there.
- That ordinary output cannot tell the regimes apart while readiness at a
  deadline differs several-fold, which [CLAIM-577](../claims.d/CLAIM-577.md)'s "The loss leaves no
  trace in output" predicts.
- That, against [CLAIM-1093](../claims.d/CLAIM-1093.md) as worded, reserve and redesign are not
  alternative routes under the peak rule: redesign lowers the reserve a
  route needs and does not replace it. [CLAIM-1093](../claims.d/CLAIM-1093.md)'s own concession,
  that the two change different things, is untouched.
- For [QUESTION-395](../questions.d/QUESTION-395.md), a decision rule if readiness is known: what it needs
  (p, L, c, the deadline, the paths' thresholds and times), and when
  [CLAIM-584](../claims.d/CLAIM-584.md)'s proposition holds of the reserve (p·L below pL*) and when it
  fails.

## What it cannot show

- **Anything about real industries or budget rules.** The numbers are
  invented and the model is the assistant's. [CLAIM-577](../claims.d/CLAIM-577.md) says real rules are
  "rarely pure spend-matching".
- **[QUESTION-395](../questions.d/QUESTION-395.md)'s identification half**, which observations tell a
  warranted reserve from waste. It sharpens it instead: under the peak rule
  readiness observed in operation and readiness under do(c) differ, by how
  often the capability is used.
- **Several resources, cumulative costs or several deadlines.** It has one
  capacity resource, one contingency type and one novel demand. [CLAIM-585](../claims.d/CLAIM-585.md),
  [CLAIM-646](../claims.d/CLAIM-646.md) and [CLAIM-878](../claims.d/CLAIM-878.md)'s limit for budgets in money or hours are not
  run; [LEAD-230](../leads.d/LEAD-230.md) would run them.
- **Whether a redesign creates a capability or only cheapens one**
  ([QUESTION-392](../questions.d/QUESTION-392.md)). The space here is connected, so it only cheapens.
- **That the claims it illustrates are true.** It illustrates them; the
  checks are on the model.

## The lead it answers

A CASE cannot point at a LEAD: its `operationalizes` is derived from the
lead's `operationalized_in`. [LEAD-226](../leads.d/LEAD-226.md) names this case there, with
[CASE-397](CASE-397.md), and carries a note of 2026-11-23. This case answers the
lead's design in part. It runs the redesign arm and the reserve sweep and
reports what the lead asked for, "readiness curves over the deadline
([TERM-115](../terms.d/TERM-115.md)), reserve cost, and which regime ranks first at which
deadlines". Its third arm, the harm absent from the specification, is
[CASE-397](CASE-397.md). The redesign is run with its cost reported as a
break-even, not charged up front as the lead's design has it.

## Note of 2026-11-23: restated as equivalence under routine queries, from "Explain First Contact RL"

<!-- inactive-ok-block: CLAIM-1054 — Proposed, filed from A50 of the exchange "Explain First Contact RL" on 2026-11-23 -->
A50 §7 of the exchange "Explain First Contact RL" (ChatGPT, 2026-11-23) restates this study's matched performance as equivalence under a routine query family Q₀ ([TERM-069](../terms.d/TERM-069.md)), broken by a new query q⋆, reorganization after a supplier failure within a deadline. It adds a query side: a regulator that samples only Q₀ rewards the system that optimized away the capacities q⋆ needs, and its success confirms the regulator's tests, a "query-induced capability trap" ([CLAIM-1054](../claims.d/CLAIM-1054.md)). This study holds the query family fixed, so it shows the divergence and not the trap; [LEAD-218](../leads.d/LEAD-218.md) would add the questioner. The case is unchanged.

## Note of 2026-11-25: half of CLAIM-700's study, run, from the review of the manuscript governance-of-becoming, Part III
<!-- inactive-ok-file: CLAIM-700 — Proposed; the hidden-subsidy claim whose study this case runs in part, cited with its standing -->

The review of Part III (2026-11-25, Part A, §1.2) found that this study
runs, in part, the study CLAIM-700 proposes, and that neither entry cites
the other. CLAIM-700 (Proposed) holds the hidden-subsidy loop: members'
conscientious compensation covers a shortfall, the organization "budgets
to what it observes", resources are cut toward what the present
configuration needs, and the reconfigurations that would remove the
shortfall "pass out of reach while the present arrangement stays
feasible". Its study, from A33 §10A: "Construct two institutions with
identical obligations and equivalent present performance", one with
reconfiguration slack and one with exactly enough for the present
configuration, and introduce a failure that needs a transition.

This case is that design without the compensator: output matched by
construction under six budget regimes until a contingency arrives,
readiness at a deadline of six periods from 0.147 to 0.894, and a
redesigned route lost under the peak rule unless a reserve is held. With
CASE-343 and CLAIM-921 (a budget that follows observed use loses a
rarely used capability), CLAIM-1099 and CLAIM-1180 (the peak rule and the
reserve), and CLAIM-679, which is in CLAIM-700's own `rests_on`, it runs
the budget-to-observed-use half of the loop and the matched-performance
contrast. What it does not run is the coupling: compensation masking the
shortfall, so that the budget rule reads it as adequacy. So CLAIM-700's
study is done in part. LEAD-022 (Open) also advances CLAIM-700, by the
study of a fall in complaints with working conditions fixed. The
case is unchanged; no change of status. The wording is the assistant's
(Claude, in this session); adopting it is the owner's call.
