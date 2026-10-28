---
number: 386
status: Active
formerly:
- THEORY-tmpsvwtz
title: "When a cached interval of width W is kept valid by its source, which pushes a refresh at cost C_vr whenever the value leaves it, and queries fetch the exact value at cost C_qr whenever it is too wide, and the chances of the two per step go as 1/W² and as W, the expected refresh cost is least at W* = (ρK₁/K₂)^(1/3) with ρ = 2C_vr/C_qr, where ρ times the chance of a pushed refresh equals the chance of a fetch"
version: 1
tags:
- databases
- operations-research
date: '2026-10-15'
source:
- LIT-1109
summary: >-
  Olston, Loo and Widom (2001), [LIT-1109](../literature.d/LIT-1109.md), read in [NOTE-912](../notes.d/NOTE-912.md). The cost rate
  Ω(W) = C_vr·K₁/W² + C_qr·K₂·W is least where ρ·P_vr = P_qr. The minimum is
  calculus on assumed forms. P_qr ∝ W follows exactly from uniform precision
  demands; P_vr ∝ 1/W² comes from a Chebyshev bound on a random walk used as an
  estimate, and the paper's simulation of a random walk measured both
  proportionalities. Staleness here is priced as refresh traffic: the source
  guarantees validity, so a stale read is imprecise but never wrong, and there
  is no build cost and no cost of a wrong or imprecise answer.
extended_by:
- THEORY-377
supports:
- CLAIM-303
bears_on:
- QUESTION-114
---

# THEORY-386: When a cached interval of width W is kept valid by its source, which pushes a refresh at cost C_vr whenever the value leaves it, and queries fetch the exact value at cost C_qr whenever it is too wide, and the chances of the two per step go as 1/W² and as W, the expected refresh cost is least at W* = (ρK₁/K₂)^(1/3) with ρ = 2C_vr/C_qr, where ρ times the chance of a pushed refresh equals the chance of a fetch

## Source

Olston, Loo and Widom (2001), [LIT-1109](../literature.d/LIT-1109.md), SIGMOD 2001, pp. 355–366, read in
full in [NOTE-912](../notes.d/NOTE-912.md) from the camera-ready copy in the University of
Pennsylvania's repository: Section 3, Appendix A, Section 4.2.

## What was actually shown

**The model.** A source validates every cached interval whenever its value
changes and pushes a new one if the value has left it (a value-initiated
refresh, cost C_vr). A query that finds the interval too wide fetches the exact
value (a query-initiated refresh, cost C_qr). Intervals are centred and
constant until refreshed, so width W describes one. The objective is network
traffic, the expected cost rate per step Ω = C_vr·P_vr + C_qr·P_qr.

**The forms.** Appendix A takes a random walk of step s, one value per query, a
query every T_q steps and precision demands uniform on [0, δ_max]. Then
P_qr = W/(T_q·δ_max) for W ≤ δ_max, exactly. For P_vr, Chebyshev gives
P ≤ t·(s/k)², and with k = W/2 the paper treats "the upper bound as a rough
approximation", so P_vr ∝ 1/W². In general P_vr = K₁/W² and P_qr = K₂·W.

**The optimum.** Ω(W) = C_vr·K₁/W² + C_qr·K₂·W has its minimum at
W* = (ρ·K₁/K₂)^(1/3), ρ = 2·C_vr/C_qr, where ρ·P_vr = P_qr. With ρ = 1 the best
width is where the two refreshes are equally likely.

**The check.** With one value on a random walk (steps uniform on [0.5, 1.5],
T_q = 2, δ_avg = 20, ρ = 1) and W fixed per run, the measured P_vr and P_qr were
proportional to 1/W² and W, and the measured cost was least where they crossed
(Figure 3). That check could have failed: other drift processes, or
precision demands not spread evenly, would change the exponents and move the
optimum off the crossing.

## What this does not say

- **That the balance holds for other drift.** The 1/W² form is a Chebyshev
  bound used as an estimate, for an unbiased random walk. For trending data the
  paper found other interval shapes better (Section 4.5), and with other
  exponents the factor 2 in ρ changes; under Divergence Caching's update-count
  staleness the paper's own analysis gives ρ′ = C_vr/C_qr.
- **That staleness costs anything but messages.** Validity is guaranteed, so
  there is no cost of reusing a wrong value and no cost of an imprecise answer;
  queries that need more precision simply pay C_qr.
- **That build cost, space or stored answers are priced.** Nothing is paid
  once, the cache limit is a heuristic eviction of the widest intervals, and
  the cached items are base values.
- **Anything in the worst case.** The optimum is of an expected rate under a
  stationary stochastic model; no competitive bound is given.
- **That the record's argument has a monitoring source.** The model needs one
  that sees every change and tests every copy.

## Connections

- [QUESTION-114](../questions.d/QUESTION-114.md): the first model the record holds in which upkeep and
  tolerated staleness are traded in one objective, with an interior optimum.
  [THEORY-348](THEORY-348.md) forbids stale reads; [THEORY-350](THEORY-350.md) budgets upkeep with no staleness;
  [THEORY-332](THEORY-332.md) has upkeep and build cost without staleness.
- [THEORY-364](THEORY-364.md): the query side this model's P_qr summarizes.
- [THEORY-377](THEORY-377.md): the adaptive rule that seeks this balance without knowing
  K₁ and K₂.
- [CLAIM-303](../claims.d/CLAIM-303.md): its upkeep u and per-use verification c_a become functions of one
  dial, the tolerance a filed item claims, with a best level between them;
  usable only where something watches the premises and triggers upkeep.
- [CLAIM-308](../claims.d/CLAIM-308.md): once staleness is admitted, the two-state choice of [THEORY-348](THEORY-348.md)
  becomes a continuum of widths, and the best choice is an interior balance;
  the cache-or-not choice is the endpoint case.
- [THEORY-348](THEORY-348.md): the rent-or-buy rule is the endpoint of this model, with
  intervals of zero width; the adaptive rule here has no competitive
  guarantee.
