---
number: 381
status: Active
formerly:
- THEORY-tmpnbhb3
title: "In the cell-probe model, a near-neighbour structure on n random points that answers in t probes with m cells of w bits must satisfy m^t·w/n ≥ the robust expansion of the metric's neighbourhood graph at measure 1/m^t (and (mwt/n)^t ≥ its vertex expansion if deterministic), so in expanding spaces such as the hypercube fast queries need space polynomially larger than the data; the bounds are average case, approximate, and fall off exponentially in t"
version: 1
tags:
- databases
- mathematics
date: '2026-10-15'
source:
- LIT-1102
answers:
- QUESTION-114
summary: >-
  Panigrahy, Talwar and Wieder (2010), [LIT-1102](../literature.d/LIT-1102.md), read in [NOTE-914](../notes.d/NOTE-914.md) from
  the arXiv preprint. For graphical neighbour search, to which decision
  approximate near neighbour reduces, on data drawn so that neighbourhoods
  rarely overlap: deterministic t-probe structures satisfy (mwt/n)^t ≥ Φv and
  m^t·t·w/n ≥ Φv(1/m^t); randomized ones satisfy m^t·w/n ≥ Φr(1/m^t, γ/t) and
  (mwt⁴/n)^{2t} ≥ Φr(1/m, γ/t). On the hypercube this gives space
  n^{1+Ω(1/(ct))} at approximation c and n^{Ω(1/(tε²))} at 1 + ε; a one-probe
  structure matches on Cayley graphs; low-contention dynamic structures need
  update time at least Φr(τ, 1/(4t²)) over poly(t). Tight only for constant t;
  nothing about worst-case or structured data, workloads or build time.
presupposed_by:
- THEORY-372
---

# THEORY-381: In the cell-probe model, a near-neighbour structure on n random points that answers in t probes with m cells of w bits must satisfy m^t·w/n ≥ the robust expansion of the metric's neighbourhood graph at measure 1/m^t (and (mwt/n)^t ≥ its vertex expansion if deterministic), so in expanding spaces such as the hypercube fast queries need space polynomially larger than the data; the bounds are average case, approximate, and fall off exponentially in t

## Source

Panigrahy, Talwar and Wieder (2010), [LIT-1102](../literature.d/LIT-1102.md), FOCS 2010, read in
[NOTE-914](../notes.d/NOTE-914.md) from arXiv:1005.0418v1; the FOCS text was not seen.

## What was actually shown

**The setting.** Join two points of a metric space when they are within r.
In graphical neighbour search each data point carries a hidden bit, and a
query with a unique neighbour among the data must return that bit; the
decision version of (c, r)-approximate near neighbour reduces to it when
data points are far apart (Theorems 4.1, 4.2). Data points are random, drawn
so that neighbourhoods rarely meet. Structures are cell-probe: t adaptive
probes into m cells of w bits, arbitrary encoding, free computation.

**Expansion bounds space (Theorems 1.4, 1.5).** Deterministic:
(mwt/n)^t ≥ Φv and m^t·t·w/n ≥ Φv(1/m^t), Φv the vertex expansion.
Randomized, success at least 1/2, t ≤ n^{1/4}: (mwt⁴/n)^{2t} ≥ Φr(1/m, γ/t)
and m^t·w/n ≥ Φr(1/m^t, γ/t), Φr the robust expansion (the least relative
measure of a set capturing a γ fraction of the edges from a small set). The
proof: if neighbourhoods expand, each data point's neighbours are spread
over many cells, so a small sample of cells decodes many hidden bits, and a
small structure would compress n random bits.

**Consequences on the hypercube (Section 4).** Approximation about c:
space n^{1+Ω(1/(ct))}; approximation 1 + ε: space n^{Ω(1/(tε²))};
deterministic, approximation 1/ε: t ≥ dε²·log a/log(mwd/n). The same recipe
recovers the ℓ∞ bound of earlier work.

**Matching and dynamic results.** On Cayley graphs a one-probe structure
with m = nΦr(1/m, γ) cells succeeds with constant probability (Theorem 5.1),
so (4) is tight at t = 1. A dynamic t-probe structure in which no cell is
read by more than a τ measure of queries has update time
Ω(Φr(τ, 1/(4t²))/32t⁴) (Theorem 1.8).

**What could have come out otherwise.** A structure on random hypercube data
with constant probes and space below these bounds would refute the
theorems.

## What this does not say

- **Anything tight beyond a constant number of probes.** "In our results, as
  in all previous results, the dependence on t is weak; that is, the bound
  drops exponentially in t." Structures probing n^ρ cells, such as LSH, are
  not addressed; [THEORY-372](THEORY-372.md) handles that regime only for hashing-based
  structures. Conjecture 1.6, which would make t enter polynomially, is open.
- **Anything about worst-case or structured data.** The bounds hold for
  random data, which is enough for a lower bound but says nothing about how
  much cheaper search is on a given collection.
- **That updates in general cost this much.** Theorem 1.8 covers
  low-contention structures only; Conjecture 1.7 is open.
- **Anything about exact search, workloads, amortization or build time.**

## Connections

- [THEORY-340](THEORY-340.md): the similarity analogue of Yao's lookup floor in the same
  model. It survives arbitrary cell encoding, which Yao's sorted-order
  optimality did not, but it is average case and approximate where Yao's is
  worst case and exact.
- [QUESTION-114](../questions.d/QUESTION-114.md): a floor under the per-query side of the trade, priced in
  space, and a lower bound on upkeep in a restricted class; part-answer
  only, with no workload and no amortization.
- [CLAIM-310](../claims.d/CLAIM-310.md): the cost comes from expansion of neighbourhoods; for exact
  lookup on a discrete attribute there is none and the bound is empty, which
  is consistent with attribute bins working (the record's reading).
- [THEORY-372](THEORY-372.md) uses Theorem 1.5 with a tight expansion estimate for its
  one-probe bound.
