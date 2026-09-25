---
number: 15
status: Skimmed
formerly:
- NOTE-tmpgpyfe
paper: LIT-008
title: 'Periodic vehicle routing and facility location for waste collection'
version: 1
date: '2026-09-25'
summary: >-
  A mixed binary/integer-encoded genetic algorithm solves the joint bin-sizing and weekly-routing problem for municipal waste collection. On small instances it comes close to Gurobi's MILP/MIQP solutions within a similar time budget, and it stays feasible on a real 163-point instance from Bahía Blanca, where the exact models are intractable.
---

<!-- inactive-ok-file: LIT-008 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-25 -->

# NOTE-015: Periodic vehicle routing and facility location for waste collection

## Contribution

Two waste-collection decisions are usually optimized separately, because each is already hard: how much bin capacity to place at each collection point, and how to design and schedule the collection routes. This paper couples them in one model. It gives two exact formulations for this model and a genetic algorithm whose chromosome mixes binary and integer genes. The authors test several crossover and mutation operators to find a good configuration. The GA matches the exact solvers on small instances and still finds feasible solutions on large, realistic instances in reasonable time.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- Contributions (§2.1): collection frequency becomes a decision instead of a fixed set of predefined options, the model is written as both MIQP and a linearized MILP, a mixed binary-permutation GA is proposed, and it is tested on real instances.
- GA tuning (§5) uses a design-of-experiments analysis of operators. The chosen setting is cycle crossover with probability 0.8 plus a mutation operator ("EM") at 0.05 (§6).
- Cost breakdown against the exact solvers on the 12-point instances (§6, Table 6): the best GA solution routes better, about 5.7% lower routing cost than both MILP and MIQP, but places bins much worse, with the exact models up to about 26–29% cheaper on bin cost. Overall, MIQP averages about 1.7% cheaper than the GA.
- In scaling (§6–7), average GA runtime grows roughly linearly with the number of collection points (slope ≈ 0.035). Planned future work covers valid cuts, simulated annealing, a bi-objective formulation and parallelization (§7).
- Instances are public at github.com/diegorossit/ANOR-S-24-01950 (Declarations).

## Open questions

- The claim that the GA is "competitive" rests on five 12-point instances with an 8-hour budget for the exact solvers. Check whether the exact solvers' optimality gaps were closed and whether 30 GA runs × evaluations make a fair comparison.
- The link to ML is thin: an evolutionary metaheuristic for combinatorial optimization, with no learning component.
