---
number: 374
status: Proposed
formerly:
- CASE-tmpndpz3
title: 'A stochastic assembly Markov chain with two alternative seams, a shared body and two kinetic traps, run and scored by committor: each seam alone raises the chance of completing from 0.19 to 0.81 while both seams together lower it to 0.04, the committor ranks a one-bond nucleus above the four-bond misfolded state, targeted stabilisation of one seam is productive and of both a trap, and reallocating a fixed component stock between the seams slides the realised form from one fold to the other with the attainable set unchanged'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-116. The code,
    tests and outputs are under scratch/studies/lead-116/.
standing: documented
kind: executed-study
tags:
- complex-systems
- probabilistic-modeling
- mathematics
- natural-sciences
date: '2026-11-22'
line:
- realizability
- formal-apparatus
variant_of:
- CASE-219
- CASE-220
- CASE-216
illustrates:
- CLAIM-567
- CLAIM-566
- CLAIM-599
bears_on:
- QUESTION-400
draws_on:
- THEORY-1398
summary: >-
  [LEAD-116](../leads.d/LEAD-116.md) asked that [CASE-219](../cases.d/CASE-219.md)'s stochastic assembly study and its
  factorial variant [CASE-220](../cases.d/CASE-220.md) be run, extending [CASE-216](../cases.d/CASE-216.md)'s annealing toy, and
  the intermediates scored by the committor q(s) = Pr_s(tau_F < tau_K). The
  model is a continuous-time Markov chain whose state is the set of bonds
  formed (a subset of four), with two alternative seams a and b each
  nucleating a shared body c, d into two valid folds F_A and F_B, an
  incompatible-seam trap (both seams) and an unnucleated collapse (a seamless
  assembly), the two traps taken from Dunn et al. and from DeLuca et al. /
  Sobczak. Committors are exact linear solves. Each seam alone is a productive
  nucleus (q from 0.19 to 0.81) but both together are a trap (0.04): an
  assembly-dynamics instance of [CLAIM-599](../claims.d/CLAIM-599.md)'s non-monotone V, which had only a
  stipulated example. The committor ranks a one-bond nucleus (0.81) above the
  four-bond misfolded state (0.05), so it orders intermediates by their future
  not their extent, as [CLAIM-567](../claims.d/CLAIM-567.md) separates reachable from reliably reached.
  Targeted early stabilisation of one designed seam is productive (Delta_q_N
  about +0.6) and of both a trap (-0.18), [CASE-220](../cases.d/CASE-220.md)'s factorial 2x2. At fixed
  total stock, moving the seam budget from a to b slides the realised share of
  F_A from 1.00 to 0.00 with the attainable set unchanged ([QUESTION-400](../questions.d/QUESTION-400.md)). A
  fold is reached far more often than it persists ([CLAIM-566](../claims.d/CLAIM-566.md)). The model and
  its rates are the assistant's and invented. The wording is the assistant's
  (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-219 CASE-220 — Proposed; the proposed studies this executed study realises and extends -->
<!-- inactive-ok-file: CLAIM-969 — new; the claim grounded in this study, filed with it -->

# CASE-374: A stochastic assembly Markov chain with two alternative seams, a shared body and two kinetic traps, run and scored by committor: each seam alone raises the chance of completing from 0.19 to 0.81 while both seams together lower it to 0.04, the committor ranks a one-bond nucleus above the four-bond misfolded state, targeted stabilisation of one seam is productive and of both a trap, and reallocating a fixed component stock between the seams slides the realised form from one fold to the other with the attainable set unchanged

## The model

A continuous-time Markov chain whose microstate is the set of bonds currently
formed, a subset of {a, b, c, d}, together with one absorbing misfold sink K
(16 subset states and K, 17 in all). Two alternative seams a and b are the
two routings of [CASE-220](../cases.d/CASE-220.md); c and d are a shared body. A seam present
nucleates the body (a body bond forms only while at least one seam is
present). Seam a completes to the valid fold F_A = {a, c, d}, seam b to
F_B = {b, c, d}; both are feasible by construction.

| Transition | Rate |
|---|---|
| seam i forms, i in {a,b} | 0.3 c_i (x the routing's designed-seam factor) |
| seam i breaks | 0.2 (x temperature factor, / stabilisation) |
| body bond forms, a seam present | 3.0 c_i |
| body bond breaks | 0.3 (x temperature factor, / stabilisation) |
| unnucleated collapse to K, no seam present | 2.0 |
| incompatible-seam misfold to K, both seams present | 8.0 |

Two kinetic traps, both from the DNA origami readings: the incompatible-seam
trap is Dunn et al.'s early long-range seams forcing a wrong fold
([CLAIM-599](../claims.d/CLAIM-599.md)'s note); the unnucleated collapse is DeLuca et al.'s accessible
structures collapsing into a disordered precursor and Sobczak's "sea of
easily accessible incorrect states" ([THEORY-1398](../theory.d/THEORY-1398.md), which the model draws on
as [CASE-220](../cases.d/CASE-220.md) does). The committor q(s) = Pr_s(tau_F < tau_K), with F the
valid folds and K the sink, is the exact solution of Q_TT q_T + Q_TF 1 = 0 off
F and K. The rates are invented to show mechanisms, as [CASE-215](../cases.d/CASE-215.md)'s are; a
temperature knob scales the off-rates, echoing [CASE-216](../cases.d/CASE-216.md). None is a DNA
origami measurement.

**Checks.** The solver reproduces the gambler's-ruin committor
(1 - r^i)/(1 - r^M) to 1e-12, matches a Gillespie estimate of q from the empty
state (0.187 exact against 0.189 in 40,000 runs), conserves the generator rows,
and satisfies Qq = 0 on the transient states to 1e-10. Thirteen tests pass
(`test_assembly_committor.py`).

## Results

**Two productive nuclei combine into a trap** ([CLAIM-599](../claims.d/CLAIM-599.md), from dynamics). With
F = either valid fold:

| do(S) | q(S) | Delta against empty |
|---|---|---|
| empty | 0.187 | — |
| {a} | 0.808 | +0.621 (productive) |
| {b} | 0.808 | +0.621 (productive) |
| {a, b} | 0.040 | -0.146 (a trap) |

V is non-monotone: a and b are each a minimal productive nucleus, and the pair
they form is a trap. [CLAIM-599](../claims.d/CLAIM-599.md) proved upward non-closure from a stipulated
table (V(a) = V(b) = 0.6, V(a,b) = 0.1); this is the same shape arising from an
assembly model, which that claim's readings had not supplied.

**The committor ranks intermediates by their future, not their extent**
([CLAIM-567](../claims.d/CLAIM-567.md)). Every transient subset state, by committor:

| state | bonds | q |
|---|---|---|
| {a,c}, {a,d}, {b,c}, {b,d} | 2 | 0.867 |
| {a}, {b} | 1 | 0.808 |
| {c,d} | 2 | 0.225 |
| {c}, {d} | 1 | 0.199 |
| empty | 0 | 0.187 |
| {a,b,c,d} | 4 | 0.047 |
| {a,b,c}, {a,b,d} | 3 | 0.043 |
| {a,b} | 2 | 0.040 |

The one-bond nucleus {a} (q = 0.81) outranks the fully assembled {a,b,c,d}
(q = 0.05) and every state holding both seams. Reachable is not reliably
reached: an intermediate's committor is its future, not how much of the target
it already shows. This is [CASE-220](../cases.d/CASE-220.md)'s "progress is not completion" and
DeLuca et al.'s run best folded at 1 s and second worst at 3.6 s, computed as a
committor.

**The factorial 2x2** ([CASE-220](../cases.d/CASE-220.md)). Routing A designs seam a (it nucleates
twice as fast), routing B seam b; targeted early stabilisation divides the
designed seam's off-rate. Delta_q_N scores forming the designed nucleus:

| cell | q(empty) | Delta_q_N | yield (t large) |
|---|---|---|---|
| Routing A, uniform | 0.243 | +0.570 | 0.243 |
| Routing A, targeted | 0.250 | +0.601 | 0.250 |
| Routing B, uniform | 0.243 | +0.570 | 0.243 |
| Routing B, targeted | 0.250 | +0.601 | 0.250 |
| stabilise both seams | 0.196 | -0.185 | 0.196 |

Targeted stabilisation of the one designed seam is a productive nucleus;
stabilising both seams locks in the incompatible pair and is a trap. The two
routings are symmetric here, since the seams are interchangeable by
construction.

**Allocation selects the form at fixed total** ([QUESTION-400](../questions.d/QUESTION-400.md)). Total stock
C = 4 held fixed; both folds F_A and F_B stay reachable throughout, so the
attainable set is unchanged. Splitting a fixed seam budget between the two
seams:

| fraction on b | q(succeed) | realised share of F_A |
|---|---|---|
| 0.0 | 0.214 | 1.00 |
| 0.2 | 0.196 | 0.82 |
| 0.4 | 0.188 | 0.61 |
| 0.6 | 0.188 | 0.39 |
| 0.8 | 0.196 | 0.18 |
| 1.0 | 0.214 | 0.00 |

Reallocating the fixed stock slides the realised form continuously from F_A to
F_B without changing which forms are attainable: [QUESTION-400](../questions.d/QUESTION-400.md) answered yes for
this model. An even split minimises the chance of completing at all, because it
maximises the chance of forming both seams and misfolding. Moving the budget
between the seams and the body has an interior optimum (q from 0.05 with too
little seam, through 0.20, to 0.10 with too little body), [CASE-219](../cases.d/CASE-219.md)'s two
outcomes in one sweep: a small early allocation to a seam raises the chance of
global organization, and over-allocation to the seams traps.

**Assembly is not persistence** ([CLAIM-566](../claims.d/CLAIM-566.md)). With the folds made reversible
and their off-rates lowered so they are metastable, a fold is reached from
empty with probability about 0.20 but survives as a fold with a smaller,
decaying probability (0.73 at t = 1, 0.046 at t = 10), falling faster as the
temperature rises. Reaching a fold and keeping it are separate probabilities
that move differently.

## What it can show

- **That [CASE-219](../cases.d/CASE-219.md) and [CASE-220](../cases.d/CASE-220.md) are runnable and that the committor does what
  their design asks**: it scores intermediates by their futures, separates a
  productive nucleus from an advanced trap, and gives Delta_q_N a sign.
- **An assembly-dynamics instance of [CLAIM-599](../claims.d/CLAIM-599.md)'s non-monotonicity**, which the
  claim's readings had not supplied, and of [CLAIM-567](../claims.d/CLAIM-567.md)'s separation and
  [CLAIM-566](../claims.d/CLAIM-566.md)'s. The finding stated as a claim is [CLAIM-969](../claims.d/CLAIM-969.md).
- **An answer to [QUESTION-400](../questions.d/QUESTION-400.md) for the model**: allocation of a fixed stock
  selects the realised form with the attainable set fixed.

Being a stipulated model with invented rates, it shows nothing about any real
DNA origami, nor that organizations behave so. The committor orders
intermediates but does not by itself establish causal productivity, as
[TERM-117](../terms.d/TERM-117.md) warns; the factorial Delta_q_N is the interventional measure the
term asks for, read here as a committor difference under do(S). The two traps,
the two forms and the nucleation rule are design choices, not findings.

Code: `scratch/studies/lead-116/` (`assembly_committor.py`,
`test_assembly_committor.py`, outputs in `results.txt`, `results.json`).
