---
number: 197
status: Active
formerly:
- CASE-tmps4kry
title: 'The toy model of superposition with six features in two dimensions, with each feature''s reconstruction loss taken as a demand: at the 5-gon critical point five features are met at 0.0158 and the dropped one only at 1/3, at the 6-gon every feature is met at 0.0482, so the posterior''s 5 → 6 transition strictly enlarges the compatibility complex for common tolerances from 0.0482 to 1/3, loses its five-feature face below 0.0482, and at the critical points changes no Betti number, only which features can be met at all'
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Promoted by the thirtieth status review, under the owner's delegation
    of 2026-10-29. It had been kept Proposed "because the neighbourhood
    results are sampled, not exhaustive", but its title claims only the
    critical-point results, which are computed, not sampled. The
    coordinator re-ran scratch/formal/tms_compatibility.py, which gave the
    figures in the tables above, and checked the 5-gon's per-feature loss
    by hand from Table 1's mean: (6 × 0.06874 − 1/3)/5 = 0.0158. Its
    source reading, NOTE-1462, went to Read in the twenty-ninth pass. The
    neighbourhood results stay what the body calls them, sample minima.
    The demands and the common tolerance remain stipulated, and adoption
    of the construction is listed for the owner's assent.
standing: stipulated
kind: construction
tags:
- learning-theory
- loss-landscapes
- representation-learning
date: '2026-11-04'
line:
- learned-structure
variant_of:
- CASE-119
- CASE-115
illustrates:
- CLAIM-555
- CLAIM-347
summary: >-
  A5 of the exchange "Organizational Nucleation and SLT" (2026-11-04)
  proposed this experiment: "decompose the toy model's population loss
  into feature-specific losses, define meaningful satisfaction thresholds,
  and construct the compatibility complexes associated with neighborhoods
  of the different polygonal phases". The reader ran it at the 5-gon and
  6-gon critical points and in sampled neighbourhoods of them. Whether the
  Bayesian transition counts as relief depends on the tolerance. Where it
  does, the change adds a vertex rather than filling a hole. The
  stipulated part is the choice of demands and of one common tolerance.
  The title's results are the critical points'; the neighbourhood ones are sampled.
  The construction is A's, run and sharpened by the reader; adopting it is
  the owner's call.
---
<!-- inactive-ok-file: CLAIM-555 — Proposed, Deferred, Unavailable or new; cited from the exchange "Organizational Nucleation and SLT" of 2026-11-04 as open -->

# CASE-197: The toy model of superposition with six features in two dimensions, with each feature's reconstruction loss taken as a demand: at the 5-gon critical point five features are met at 0.0158 and the dropped one only at 1/3, at the 6-gon every feature is met at 0.0482, so the posterior's 5 → 6 transition strictly enlarges the compatibility complex for common tolerances from 0.0482 to 1/3, loses its five-feature face below 0.0482, and at the critical points changes no Betti number, only which features can be met at all

## The construction

**The model.** This is the toy model of superposition ([LIT-323](../literature.d/LIT-323.md)) in Chen et
al.'s setting ([LIT-1894](../literature.d/LIT-1894.md), read in [NOTE-1462](../notes.d/NOTE-1462.md)):

- c = 6 input features and r = 2 hidden dimensions;
- output f(x) = ReLU(WᵀWx + b);
- high-sparsity inputs: one feature is active at a time, x = μe_i with
  μ ~ U[0, 1].

**The phases.** A k-gon puts k columns of W at the vertices of a regular
k-gon, with a common norm a and a common bias b. The other 6 − k columns are
zero, with bias −1. Any bias ≤ 0 does the same: the output for an
unrepresented feature is then 0.

**The demands.** Demand i is feature i's reconstruction loss,

  L_i(W, b) = E_μ ‖f(μe_i) − μe_i‖².

Its acceptance set at tolerance ε is A_i(ε) = {(W, b) : L_i ≤ ε}. The mean of
the six L_i is the population loss in this limit. So the decomposition splits
the model's own loss by which feature is active. It is not imposed from
outside the model.

**The complex.** [CLAIM-347](../claims.d/CLAIM-347.md)'s complex, with the attainable set taken as a
critical point, or as a neighbourhood of one:

  𝒦(U; ε) = {S : U ∩ ⋂_{i∈S} A_i(ε) ≠ ∅}.

The script is scratch/formal/tms_compatibility.py. It uses numpy, scipy and trapezoid
quadrature on 4001 points.

## Results

**The critical points reproduce the recorded losses.** Each phase's a and b
are optimized numerically.

| phase | a | b | mean loss | Table 1 ([NOTE-1462](../notes.d/NOTE-1462.md)) |
|---|---|---|---|---|
| 5-gon | 1.1705 | −0.2823 | 0.06874 | 0.06874 |
| 6-gon | 1.3205 | −0.6180 | 0.04819 | 0.04819 |

Re-minimizing all 18 parameters, from a perturbation of 10⁻³, returns the
same loss for both.

**Per-feature losses at the critical points.**

- 5-gon: 0.0158 for each represented feature, and 1/3 for the dropped one,
  which is ∫₀¹ μ² dμ.
- 6-gon: 0.0482 for each of the six.

**The complex at the critical points, for a common tolerance ε.**

| ε | 5-gon | 6-gon | 5 → 6 |
|---|---|---|---|
| below 0.0158 | empty | empty | no change |
| 0.0158 to 0.0482 | a 4-simplex on the five represented features | empty | loses faces: not relief |
| 0.0482 to 1/3 | a 4-simplex | the full 5-simplex | strict enlargement: relief |
| 1/3 and above | the full 5-simplex | the full 5-simplex | no change |

Every complex in the table is empty or a single simplex. So at the critical
points no reduced Betti number is ever nonzero, and none changes. What changes
is the vertex set: which demands can be met at all.

**Neighbourhoods.** 3000 points were sampled within radius about 0.05 of each
critical point. For each j, the run records the least tolerance at which some
j features are jointly met. These are sample minima, so they are upper bounds
on the true least tolerances.

| j features | 5-gon neighbourhood | 6-gon neighbourhood |
|---|---|---|
| 1 | about 0.004 | about 0.029 |
| 5 | about 0.0155 | about 0.048 |
| 6 | 1/3 | 0.0482 |

The critical-point verdicts survive:

- From 0.0158 to about 0.029, the 6-gon neighbourhood meets no feature while
  the 5-gon's meets five.
- Up to 0.0482, the 6-gon neighbourhood does not contain the 5-gon's
  five-feature face.
- From 0.0482 up to 1/3, the 6-gon neighbourhood meets all six, and the
  5-gon's never does.

The neighbourhood complexes need not be simplices, so the Betti-number remark
is made only for the critical points.

## What it shows and does not

**It shows one SLT transition read in [CLAIM-347](../claims.d/CLAIM-347.md)'s terms.** [NOTE-1462](../notes.d/NOTE-1462.md) and
[THEORY-1275](../theory.d/THEORY-1275.md) hold that the posterior moves from the 5-gon to the 6-gon at
n_cr ≈ 601. Read as a change of attainable set, that move is relief at
moderate tolerance: a dropped demand becomes satisfiable, and no face is lost.
At tight tolerance it is a trade: five demands met well give way to six met
less well. This fits [CLAIM-555](../claims.d/CLAIM-555.md). The same parameter space carries both the
singular geometry (λ = 7 against 8.5) and the complex, and the complex alone
says whether the transition is relief.

**It is not [CASE-119](CASE-119.md)'s kind of change.** [CASE-119](CASE-119.md) fills a missing triangle,
so β₁ goes from 1 to 0. Here no hole is filled: a vertex is added. A3's
conjecture, that "some developmental transitions are changes in the topology
of the system's effective organizational possibilities", is met here only in
the weak sense of a new vertex.
This bears on [QUESTION-275](../questions.d/QUESTION-275.md) and on A4's narrow hypothesis.

**It does not show:**

- That SGD makes the transition. [THEORY-1275](../theory.d/THEORY-1275.md) records that the 5 → 6
  transition "has not been observed as a dynamical transition", and
  [QUESTION-363](../questions.d/QUESTION-363.md) asks when the two orders agree.
- That a common tolerance is the right choice. With per-demand tolerances,
  other bands appear.
- Anything about neighbourhoods beyond the sampled radius, or about the
  posterior-weighted complex.
- That these demands are the network's own. They are the trainer's
  ([TERM-060](../terms.d/TERM-060.md), [CLAIM-288](../claims.d/CLAIM-288.md)).
