---
number: 332
status: Active
formerly:
- THEORY-tmp326zp
title: "For one index with no space limit, Bruno and Chaudhuri's online tuner, which builds the index once the savings it would have given have risen by its build cost above their last low and drops it once they have fallen by the build cost below their last high, is not three-competitive: when every statement's saving or loss is at most a fraction f of the build cost, a repeated workload makes it cost nearly 3 + 2f times the offline optimum, and one statement whose saving exceeds the build cost makes the ratio unbounded; no upper bound is shown"
version: 2
history:
- version: 2
  date: '2026-10-20'
  note: >-
    Promoted with a corrected title, carrying out the promotion audit's
    decision for THEORY-332 (batch 053, ADR-047 v2). The old title left
    open whether the rule stays within three when every saving is small
    next to the build cost. A construction shows it does not, for any
    positive bound on step size: the ratio approaches 3 + 2f. The title
    now states that lower bound. The promote_when asked for an upper
    bound, which moves to QUESTION-tmp7o5ig.
tags:
- databases
- operations-research
date: '2026-10-15'
source:
- LIT-1095
answers:
- QUESTION-114
summary: >-
  Bruno and Chaudhuri (2007), [LIT-1095](../literature.d/LIT-1095.md), read in [NOTE-896](../notes.d/NOTE-896.md). An always-on
  index tuner keeps, per index, the running sum of what each statement would
  have saved (updates counting as losses) and creates or drops the index when
  that sum moves by the build cost from its last extreme. The paper calls the
  single-index rule three-competitive, but its proof is one workload on which the
  ratio approaches 3, a lower bound. The reading's own check found ratios up to
  4.7 when one statement's saving is near the build cost, and an unbounded ratio
  when it exceeds it; with every saving at most a tenth of the build cost no
  random workload passed 2.4, but a constructed one with steps at most fB approaches 3 + 2f (note of 2026-10-20). The multi-index tuner with a space limit is
  heuristic, and all costs are optimizer estimates.
---

# THEORY-332: For one index with no space limit, Bruno and Chaudhuri's online tuner, which builds the index once the savings it would have given have risen by its build cost above their last low and drops it once they have fallen by the build cost below their last high, is not three-competitive: when every statement's saving or loss is at most a fraction f of the build cost, a repeated workload makes it cost nearly 3 + 2f times the offline optimum, and one statement whose saving exceeds the build cost makes the ratio unbounded; no upper bound is shown

## Source

Bruno and Chaudhuri (2007), [LIT-1095](../literature.d/LIT-1095.md), ICDE, read in full in [NOTE-896](../notes.d/NOTE-896.md)
from the accepted version: Definition 1, Figure 4 (Online-SI), Theorems 1 and 2,
Section 3 (OnlinePT) and the experiments. The simulation reported below is the
reading's own ([NOTE-896](../notes.d/NOTE-896.md), "My check, not the paper's"), not the paper's.

## What was actually shown

**The model.** A workload is a sequence of queries and updates known only up to
now. A schedule of configurations is priced by each statement's cost under the
configuration in force plus a build cost B_I for each index created; dropping is
free. Upkeep enters as the extra cost of update statements.

**The rule.** For one index, Δ is the running sum of cost without the index
minus cost with it. Online-SI creates the index once Δ − Δmin ≥ B_I and drops it
once Δmax − Δ ≥ B_I. The paper's rationale: "we transition configurations after
gathering the information that proves that the optimal strategy would have done
so at a past point in time." In structure this is Karlin et al.'s switching rule
([LIT-1096](../literature.d/LIT-1096.md)) applied in both directions, though the paper cites no work on
competitive analysis.

**The ratio.** Theorem 2: "Algorithm Online-SI is three-competitive (i.e., it is
no worse than 3 times the optimal algorithm Opt-SI)." The proof gives one
alternating workload, with each statement's saving equal to B_I, on which Opt
pays B_I + 2ε per pair and Online-SI 3B_I + 2ε. That shows the ratio can come
arbitrarily close to 3; no upper-bound argument is given.

**What the reading's check found.** With an exact dynamic program for the
optimum and random workloads, the ratio reached 4.7 with every |δ| ≤ B_I. One
query that costs K without the index and nothing with it makes the optimum pay
B_I and Online-SI pay K, so the ratio is unbounded once one saving exceeds B_I.
With every |δ| at most B_I/10, the worst ratio found was 2.4.

## What this does not say

- **That the tuner is three-competitive.** As stated, without a bound on
  per-statement savings, it is not. With such a bound it is unproved: a
  simulation that finds no counterexample is not a proof, and the right bound may
  be a ratio that grows with step size.
- **That the deployed tuner has any guarantee.** The multi-index case, with
  interacting indexes, a space limit, merging and an anti-oscillation rule, is
  heuristic; the paper says so ("but cannot guarantee three-competitiveness
  anymore").
- **That the measured costs are real.** All costs in the experiments are
  optimizer estimates, and index builds are synchronous and instantaneous in the
  analysis. On TPC-H the paper shows bars without numbers.
- **That dropping, staleness or build time are priced.** Dropping is free, upkeep
  is paid per statement and never deferred, and builds take no time.
- **That it covers precomputed answers.** It selects indexes, not views.

## Connections

- For [QUESTION-114](../questions.d/QUESTION-114.md) this is the nearest the record holds to a joint model:
  one-time build cost, per-statement savings, upkeep, space and an unknown
  workload on one schedule. Its only guarantee covers the narrowest case.
- Karlin et al. ([LIT-1096](../literature.d/LIT-1096.md), [THEORY-348](THEORY-348.md)) prove the one-directional
  rent-or-buy rule within 2 under unit steps; this rule is two-sided, and its step condition is unstated.
- [THEORY-333](THEORY-333.md) builds structure on every query with no such rule; [THEORY-350](THEORY-350.md)
  budgets upkeep for views but has no build cost and no time.
- [CASE-094](../cases.d/CASE-094.md) and [CLAIM-307](../claims.d/CLAIM-307.md): a near-free bin makes the create rule fire at
  the first retrieval that would have gone faster, but one search through a large
  pile can cost more than the bin, which is outside the small-step regime.

## Note of 2026-10-20: the lower bound, derived

Derived for the promotion audit (batch 053, [ADR-047](../decisions.d/ADR-047.md) v2), in the paper's
single-index model. A statement is (c0, c1), its cost without and with the
index. Its saving is c0 − c1, and D is the running sum of savings.

1. **The cycle.** Fix f in (0, 1] and a small η > 0. In the query phase,
   statements (s, 0) with every s ≤ fB come until their savings sum to
   B − η, and then one (fB, 0) follows. In the update phase, statements
   (0, s) with s ≤ fB come until their losses sum to B − η, and then one
   (0, fB) follows.
2. **What Online-SI pays.** D − Dmin first reaches B on the last query of
   the phase. So the rule pays every query of the phase without the index,
   B − η + fB, and then builds for B. Dmax − D first reaches B on the last
   update, so it pays every update with the index, B − η + fB, and then
   drops. Dmin and Dmax reset at the drop and at the build, so each cycle
   costs 3B + 2fB − 2η.
3. **What the optimum pays.** Build at the start of each query phase and
   drop before its update phase: B per cycle.
4. **The ratio.** Over m cycles it is 3 + 2f − 2η/B. No additive constant
   saves a factor of 3, for any bound f. The paper's own example is the
   case with no overshoot, which gives 3.
5. **One large saving.** A single (K, 0) with K > B costs the rule K + B,
   since it builds only after the statement, while the optimum builds
   first for B. The ratio grows without bound in K.

A check, with the recipe in the decision file: hill-climbing over workloads
with steps at most fB found 3.998, 3.400, 3.199 and 3.093 at f = 0.5, 0.2,
0.1 and 0.05. That is 3 + 2f, approached from below. The note's earlier 2.4
at f = 0.1 came from random workloads, which do not find this pattern.
Whether some constant bounds the rule from above on such workloads is
[QUESTION-tmp7o5ig](../questions.d/QUESTION-tmp7o5ig.md).
