---
number: 501
status: Active
formerly:
- THEORY-tmpdgxy5
title: "In weekly waste collection where each point's visit days are free and its bin capacity must cover the longest gap between visits, a genetic algorithm that searches visit schedules and derives bins from them builds routes about 6% cheaper than eight-hour Gurobi incumbents but buys about 20% more bin capacity, ending level on overall cost at its best of 30 runs and 4–6% worse on a typical run, on five 12-point instances where the incumbents' own optimality gaps are 26–32%"
version: 1
tags:
- operations-research
date: '2026-10-16'
source:
- LIT-008
summary: >-
  González et al. (2025), [LIT-008](../literature.d/LIT-008.md), read in [NOTE-015](../notes.d/NOTE-015.md). The comparison is
  against incumbents whose distance from optimum is unknown, on five
  12-point random subsets of one real instance, one of which was also used
  to tune the GA. Best of 30 against the MILP: −0.08% overall; against the
  MIQP: +1.70%; the GA's mean or median is +3.75% and +5.61%. The
  abstract's "able to match the results of exact solvers" says less than it
  appears to. On 40–163 points there is no bound or baseline.
---

# THEORY-501: In weekly waste collection where each point's visit days are free and its bin capacity must cover the longest gap between visits, a genetic algorithm that searches visit schedules and derives bins from them builds routes about 6% cheaper than eight-hour Gurobi incumbents but buys about 20% more bin capacity, ending level on overall cost at its best of 30 runs and 4–6% worse on a typical run, on five 12-point instances where the incumbents' own optimality gaps are 26–32%

## Source

González et al. (2025), [LIT-008](../literature.d/LIT-008.md), arXiv 2504.10648v1 (*Annals of Operations
Research* 350: 979–1015), read in full in [NOTE-015](../notes.d/NOTE-015.md). The journal version and
the GitHub instances were not compared.

## What was actually shown

**The problem (§3, §4.1).** Collection points have fixed sites; each gets
one of eight bin combinations (capacity 1.1–5.6 m³). Waste accumulates
deterministically each day, with no collection on Sunday, cyclic over the
week. Visit days are a free decision, not chosen from patterns, and service
time depends on the bins. The cost is weekly bin cost plus routing time.
The MIQP is linearised exactly as a MILP.

**Why bins follow visits.** The bin needed at a point is the smallest
combination at least as large as its maximum accumulation, which the
longest gap between visits sets (Eqs. 2c, 2k–2m). The GA evolves only a
visit mask and daily orders and derives the bins in the decoder (App. A).

**The comparison (Tables 5–6).** On five 12-point instances, Gurobi 10 ran
8 h on each formulation and stopped with gaps of 29.06–32.15% (MILP) and
26.15–32.34% (MIQP). The GA ran 30 times per instance (about 7.5–7.7 h in
total). Mean over instances of (C_GA − C_exact)/C_exact:

| | bin cost | routing cost | overall cost |
|---|---|---|---|
| GA best vs MILP | +19.88% | −5.75% | −0.08% |
| GA mean/median vs MILP | +18.65% | −0.36% | +3.75% |
| GA best vs MIQP | +22.59% | −5.74% | +1.70% |
| GA mean/median vs MIQP | +21.24% | +1.37% | +5.61% |

**Larger instances (Table 7).** On 40–163 points, all 30 runs were feasible,
at 0.72–5.58 h mean per run, with no bound, alternative method or
current-practice baseline.

**What could have come out otherwise.** The GA could have matched the exact
incumbents on both cost components. It systematically trades bin cost for
routing cost: it finds shorter routes by visiting less often, which forces
larger bins.

## What this does not say

- **That either method is near optimal.** Both are compared with incumbents
  roughly 30% from Gurobi's bound.
- **That the GA "consistently" routes better than the MILP.** On i.12.2 its
  best routing cost is 0.76% worse ([NOTE-015](../notes.d/NOTE-015.md), C5).
- **That the exact bins are 26–29% cheaper.** The GA's bin excess is up to
  +25.62% and +28.78%, so the exact bins are up to about 20% and 22%
  cheaper. The paper makes the same slip (§6).
- **That the tuned GA generalises.** Operators were tuned on i.12.1, which is
  also a test instance, and the 12-point instances are subsets of the one
  real instance.
- **That runtime grows linearly.** Four points with different generation
  budgets and penalty weights do not establish it.
- **That the bin deficit is inherent.** The repair only adds visits, which
  may cause it; the paper does not analyse this.

## Connections

The record holds no other account of vehicle routing or metaheuristic
evaluation. The paper builds on Mahéo, Rossit and Kilby (2020, 2023) and is
positioned against Hemmelmayr et al. (2014, 2017) and Gläser and Stücken
(2021), none of which is held.
