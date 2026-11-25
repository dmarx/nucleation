---
number: 402
status: Active
formerly:
- CASE-tmpgqbyq
title: 'SGD vs the 6-gon in the toy superposition model'
statement: >-
  In the toy model of superposition with six features in two dimensions,
  1,008 SGD runs not started at the 6-gon, across n from 300 to 2,000, batch
  sizes 1 to 100, rates 0.001 to 0.2, four initialisations and up to 45,000
  epochs, never reach it, while the sampled posterior passes from the 5-gon
  to the 6-gon at n ≈ 270 in the free-energy formula's units, not 601
version: 2
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-175 for
    QUESTION-363. Scripts, tests and results are committed under
    scratch/studies/lead-175/, with a README saying how to rerun.
- version: 2
  date: '2026-11-23'
  note: >-
    Proposed to Active at the status review's ruling (the owner delegated
    these rulings): the run reproduces; the 28 tests pass, every summary
    regenerates identically from the committed runs, and reruns of one SGD
    job (96 runs) and of the first two confined-HMC blocks of region 6
    match the committed output bit for bit. The full sweep and the rest of
    the posterior were not rerun.
standing: documented
kind: executed-study
tags:
- learning-theory
- loss-landscapes
- mathematical-statistics
date: '2026-11-22'
line:
- learned-structure
bears_on:
- QUESTION-363
reported_in:
- THEORY-1275
draws_on:
- THEORY-1353
summary: >-
  [LEAD-175](../leads.d/LEAD-175.md) asked for the two tests [QUESTION-363](../questions.d/QUESTION-363.md)'s note of 2026-11-06 moved
  there from [THEORY-1275](../theory.d/THEORY-1275.md): SGD at n = 1,000 and on both sides of n ≈ 600
  across rates, batch sizes and initialisations, to see whether the 6-gon
  is reached; and posterior sampling across n to check the critical sample
  sizes the free-energy formula gives for the chain 4⁺⁺⁻ → 4⁺ → 5 → 5⁺.
  In the model of Chen et al. ([LIT-1894](../literature.d/LIT-1894.md)), in numpy: no SGD run reached the
  6-gon. The 5-gon's dropped feature gets an exactly zero gradient from
  every sample, so SGD cannot move it at any setting. The 5⁺-gon is a
  live local minimum that SGD does not leave in 45,000 epochs. Sampling
  exp(−nL) under the N(0, 1) prior puts 5 → 6 at n ≈ 265–279 and
  5 → 5⁺ at n ≈ 780. The first two steps of the chain have no crossing
  above n ≈ 1. Chen et al.'s NUTS likelihood carries a factor ½ that their
  formula's nL does not, so their sample size is twice these n; on that
  scale the sampled 5 → 6 is at about 530–560, consistent with their Fig.
  2. The wording is the assistant's (Claude, in this session); adopting it
  is the owner's call.
---
<!-- inactive-ok-file: THEORY-1353 — Proposed; Dong's test of a temperature, cited as a check -->

# CASE-402: SGD vs the 6-gon in the toy superposition model

## What was done

The model is Chen et al.'s ([LIT-1894](../literature.d/LIT-1894.md), as read in [THEORY-1275](../theory.d/THEORY-1275.md)). It has
c = 6 features and r = 2 hidden dimensions, in the high-sparsity limit:
x = μe_i, with i uniform and μ ~ U[0, 1]. The network is
f(x) = ReLU(WᵀWx + b), with loss ‖x − f(x)‖². Table 1's L carries no
factor ½. The population loss and its gradient are computed in closed
form, checked against quadrature, Table 1 and finite differences. Regions
are classified as Chen et al. classify them: k, the convex-hull vertices
among the six columns, and σ, the positive biases among non-vertex columns.
A finer count adds the switched-off vertices, written '−'. Code, 20 pytest
tests and all results are in scratch/studies/lead-175/.

**SGD.** Plain minibatch SGD on a fixed training set, for 4,500 epochs as
in the paper:

- n = 300, 500, 700, 1,000 and 2,000;
- batch 100 and 20 at every n, and batch 5 at n = 500 and 1,000;
- rates 0.001, 0.005, 0.02 and 0.05;
- initialisations: the paper's 4-gon plus noise of s.d. 0.01, the 5-gon
  plus the same noise, the 6-gon plus noise (a control), and a draw from
  the N(0, 1) prior;
- six seeds.

That is 1,152 runs. Three extensions followed:

- batch 1 at rates 0.05, 0.1 and 0.2, for 1,000 epochs at n = 500 and
  1,000 (72 runs);
- the 5⁺-gon plus noise at n = 1,000, batch 100 and 20, all four rates (48
  runs);
- 45,000 epochs, ten times the paper's budget, at n = 1,000, batch 20,
  rates 0.02 and 0.05 (24 runs).

The rates cover both readings of the paper's 0.005. With the loss summed
over outputs, as here, it is 0.005. Under a loss averaged over outputs it
would be about 0.0008 here.

**Posterior.** The target is p_n(w) ∝ exp(−nL(w))N(w; 0, I₁₈), with L the
population loss: the posterior whose free energy is the formula
f_α(n) = nL_α + λ_α log n + c_α (their App. F.1). It was sampled two ways:

- **Parallel tempering.** HMC over 44 values of n from 20 to 10,000, with
  16 chains, counting each region's occupancy.
- **Confined runs.** HMC confined to each of the regions 6, 5, 5⁺, 4, 4⁺,
  4⁺⁺ and 4⁺⁺⁻, over 64 values of n from 0.5 to 10,000. Since
  d log Z_α/dn = −E_{α,n}[L], integrating from the prior mass of each
  region (2,000,000 prior draws) gives each region's free energy down to
  probabilities the tempering run cannot see.

## Results

**SGD never reaches the 6-gon.** None of the 1,008 runs not started there
ended at the 6-gon, and none was at it at any checkpoint. All 288 controls
started there stayed. Every 5-gon start ended at the 5-gon (288 of 288).
Every 5⁺-gon start stayed at the 5⁺-gon: 48 of 48 at 4,500 epochs and 8
of 8 at 45,000. The paper's 4-gon start ended at 4, 4⁺ or 4⁺⁺ in 265 of
288 runs, at 5 in 18 and at 5⁺ in 5. Higher noise ended with fewer
features, not more. At batch 1 the 5⁺-gon starts lost their positive-bias
column: they ended at the 5-gon at rates 0.05 and 0.1, and at a 4-gon at
0.2. No value of n, batch, rate or initialisation reached the 6-gon,
on either side of n ≈ 600.

**Why the 5-gon cannot go on.** At the 5-gon the dropped feature's column
is zero and its bias negative. Its output is silenced for every input, and
its input excites no output while the other biases are non-positive. Every
per-sample gradient in that column and bias is then exactly zero, so
SGD's noise is zero in those coordinates. A test runs 3,000 steps at
three settings, up to rate 0.1 at batch 1, and the column does not move by
one bit. In the sweep, 460 of the 476 runs that ended at the 5-gon have
the dropped feature's output silenced, and in 386 its column gets no
gradient at all.

**The posterior's transitions.** The sampler was checked three ways:

- n(E[L] − L_crit) at n = 10,000 is 7.2 for the 5-gon, 8.5 for the
  5⁺-gon and 8.6 for the 6-gon, against Table 1's 7, 8.5 and 8.5;
- the confined runs' log-odds agree with the tempering occupancy at 114
  (pair, n) points, rms 0.13 nats;
- the 6-gon carries all the mass from n ≈ 850 up.

In the formula's units:

| transition | formula, Table K.1 λ̂ | formula, theory λ | tempering | integration |
|---|---|---|---|---|
| 4⁺⁺⁻ → 4⁺ | 190 | 190 | — | none: 4⁺ is ahead at every n from 0.5 |
| 4⁺ → 5 | 370 | 237 | — | ≈ 1: 5 is ahead from the prior on |
| 5 → 5⁺ | 2,477 | 1,593 | — | 781 |
| 5 → 6 | 538 | 601 | 265 | 279 |

The dominant region, among the seven integrated, is 4⁺ at the prior, then
4 from n ≈ 1, 5 from n ≈ 77 and 6 from n ≈ 315.

**The units.** Chen et al.'s likelihood (Eq. 3) is exp(−½‖x − f‖²), and
their NUTS runs (App. F) sample its posterior, exp(−(n/2)L_n)φ. Their
formula (App. F.1) uses nL with Table 1's L, which has no ½. Their sample
size is therefore twice the n above. On their scale:

- the sampled 5 → 6 falls at about 530–560, consistent with the 600–700
  of their Fig. 2, which used ten finite datasets per n;
- 5 → 5⁺ falls at about 1,560.

The formula with Table C.2's prior-only constants gives 601 on the
formula's own scale. That number agrees with Fig. 2 only across the
change of scale.

## What it can show

**That "inaccessible" holds for the 5-gon.** For plain SGD in this model,
"not reached in 4,500 epochs at one setting" is the wrong description of
the missing 5 → 6. From the 5-gon the move is closed at every rate, batch
size and time, by construction and not by a barrier.

**Not for every route.** The live route, through a positive-bias column
(5⁺), is a local minimum that SGD did not leave at these settings. That
is "not reached", not shown closed.

**The noise.** SGD's noise is zero exactly where the posterior's prior
acts. This bears on [QUESTION-363](../questions.d/QUESTION-363.md)'s "effective temperature": the
stationary accounts' temperature does not reach directions in which
every sample's gradient vanishes, as Dong's test of isotropy ([THEORY-1353](../theory.d/THEORY-1353.md))
would lead one to expect.

**The posterior side.** The critical sizes [THEORY-1275](../theory.d/THEORY-1275.md) computed from the
formula are not what sampling finds, apart from 5 → 6 on Chen et al.'s
own scale. The chain's first two steps have no crossing in the range
where SGD trains. The regions are ordered 4⁺⁺⁻ < 4⁺ < 5 in the posterior
from n ≈ 1, and 5⁺ overtakes 5 at n ≈ 780 in the formula's units.

## What it cannot show

- **Other trainers.** One model, plain SGD only: no momentum, no weight
  decay, no injected noise. A Langevin term or weight decay acts on the
  frozen coordinates and could change the SGD result.
- **The finite-dataset posterior.** The posterior uses the population
  loss, not a finite dataset's. The fluctuation term Chen et al.'s NUTS
  runs include is absent.
- **The 4-gon family's critical points.** At large n, the 4-gon family's
  regions are not dominated by their critical points:
  n(E[L] − L_crit) goes negative. The region free energies are those of
  Chen et al.'s regions W_{k,σ}, as counted in their Fig. 2, not of the
  critical points the formula's L_α describe.
- **Error bars.** The confined runs have six to nine post-burn blocks,
  and the integration's error is the order of the 0.13-nat disagreement.
  The crossings 265 and 279 bracket the 5 → 6 estimate.

## Filed from it

- [CLAIM-1098](../claims.d/CLAIM-1098.md): the dropped feature's frozen gradient.
- [CLAIM-1057](../claims.d/CLAIM-1057.md): the sweep's result for [QUESTION-363](../questions.d/QUESTION-363.md).
- [CLAIM-1162](../claims.d/CLAIM-1162.md): the posterior's critical sizes.
