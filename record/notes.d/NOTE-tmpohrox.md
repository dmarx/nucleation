---
status: Read
paper: 'LIT-tmpdrddx'
title: 'Felekis et al. — Causal optimal transport of abstractions'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Read in full from the arXiv preprint 2312.08107v1 (13 December 2023),
    the only arXiv version, 31 pp., which precedes the CLeaR 2024
    proceedings version (PMLR 236:462–498); the proceedings PDF was not
    read, so differences are unknown. Extracted with `pdftotext -layout`,
    which garbled several displayed equations (eqs. 7–12, 17); I read
    them against the surrounding text. I read the abstract, §§1–7, the
    acknowledgements and references, and Appendices A–H (the normalising
    vectors, the proof of Theorem 1, the costs, the battery task, all
    result tables 6–19, Approximate COTA, the DAGs and posets, and the
    optimal-transport background), with all captions. Pages are the
    preprint's. Check: I derived from eqs. (6), (9), (10), (12) and (17)
    that the do-calculus term is constant on the feasible set (Key
    results), and read, without running, the authors' released code
    (github.com/yfelekis/COTA, optimization_functions.py and runs.py) to
    see how it builds the problem.
date: '2026-10-29'
summary: >-
  COTA learns a stochastic map from a low-level to a high-level causal
  model's state space from samples of paired interventional
  distributions, given both DAGs and the map between interventions, by
  solving one entropic optimal-transport problem per intervention with a
  cost that rewards compatibility with the paired interventions and a
  term meant to impose do-calculus relations between plans. As written,
  that term depends only on the plans' marginals, which the transport
  constraints fix, so it is constant on the feasible set and its weight
  acts only by rescaling the other terms. The reported gains come from
  the compatibility cost when interventions are many; with few, a
  Hamming cost does better.
---
<!-- inactive-ok-file: QUESTION-282 — Open; the question this reading bears on, cited as open -->

# NOTE-tmpohrox: Felekis et al. — Causal optimal transport of abstractions

## Contribution

The paper poses the learning of a causal abstraction τ between a base
model M and an abstracted model M′ in Rubenstein et al.'s τ-ω framework
when the structural functions are unknown but the DAGs, a finite poset of
interventions I, the order-preserving surjection ω: I → I′ and samples
from every paired interventional distribution are available (§3, p. 4).
It casts the problem as multi-marginal entropic optimal transport, one
plan per intervention pair, with an "ω-cost" and a term meant to enforce
do-calculus relations among the plans of comparable interventions (§4,
pp. 5–7), proves the objective convex (Theorem 1, p. 8), and reports lower
leave-one-intervention-out abstraction error than non-causal OT baselines
on two synthetic models and lower downstream regression error than
Zennaro et al. (2023) on a battery-manufacturing dataset (§6, pp. 8–10).

## Key insight

The intended insight is that an abstraction map has to make the paired
interventional distributions correspond, all of them at once, so the
transport problems for different interventions should not be solved
separately. "Our aim is to learn a single τ-ω transformation from data
sampled from the pairs in Πω(I)" (p. 4). The insight the reading adds is
that as the problem is written, the coupling between interventions does
not reach the plans: what joins them is a shared cost matrix and the
final averaging, not the do-calculus term.

## Assumptions

- **Acyclic, faithful, causally sufficient SCMs** (p. 2). Semi-Markovian
  models are named as an open challenge (p. 11).
- **Given inputs** (p. 4): "(a) access to the causal DAGs of the base M and
  the abstracted M′ models; (b) a finite set of interventions I; (c) an
  intervention mapping ω : I → I′; (d) samples from the observational and
  interventional distributions." So ω, the correspondence between
  interventions, is not learned; and both models must be sampled under
  every intervention in I.
- **Discrete domains** in all experiments; the stochastic map
  f_s: dom[X] → Δ^{|dom[X′]|} needs a finite target (p. 4).
- **Exact τ-ω transformation** (Definition 4, p. 3, after Rubenstein et
  al.): τ#(P_{M_ι}) = P_{M′_{ω(ι)}} for every ι ∈ I, with a single
  exogenous distribution on each side. Approximation is measured by the
  average abstraction error e(τ) = E_{ι∼q} D(τ#(P_{M_ι}), P_{M′_{ω(ι)}})
  with q uniform (Definition 5, p. 3).

## Key results

### The objective (§4, pp. 5–7)

- **Per-pair transport.** For each pair π_ι a plan P^ι in the transport
  polytope U(π_ι), whose column sums are the base empirical distribution
  under ι and whose row sums are the abstracted one under ω(ι) (eq. 6,
  p. 6).
- **The ω-cost** (eq. 11, p. 6): c_ω(x, x′) = |I| − Σ_ι 1[Cmp(x, ι) ∧
  Cmp(x′, ω(ι))], lower for pairs of states compatible with more paired
  interventions. With few interventions it is "almost-uniform and
  uninformative" (p. 9).
- **The do-calculus term** (eqs. 7–10, p. 6). For comparable ι ⪯ η the
  truncated factorisation relates P_{M_do(b)} to P_M divided by the
  intervened variables' conditionals. The paper writes this as a
  divergence δ_{ι,η}(P^ι, P^η) = d(Σ_i P^η_{ij}, (1/Z^η_j) Σ_i P^ι_{ij})
  on compatible columns, and its analogue δ′ on rows, with the
  normalisers Z expressed through P^ι (Appendix A, eq. 17, p. 14).
- **COTA** (eq. 12, p. 7): over the plans of a maximal chain,
  minimise Σ κ⟨C_ω, P^ι⟩ + λᵀD(P^ι, P^{ι+1}) − μH(P^ι), with
  κ + λ + λ′ + μ = 1, subject to P^ι ∈ U(π_ι). The final τ is the
  stochastic map of the average plan, or the average of the plans'
  stochastic maps (Algorithm 1, p. 7).
- **Theorem 1** (p. 8): jointly convex, strictly so for μ > 0.

### The do-calculus term is constant on the feasible set

Both arguments of δ_{ι,η} are column sums of a plan: Σ_i P^η_{ij} and
Σ_i P^ι_{ij}. The normaliser Z^η of eq. (17) is a ratio of sums of
entries of P^ι over index sets defined by conditions on the base state
x_j alone, so it too is a function of the column sums. The constraint
P ∈ U(π) fixes every column sum to the corresponding empirical
distribution (eq. 6). So δ, and by the same argument on rows δ′, takes one
value on the whole feasible set, determined by the data. Eq. (12)'s
minimiser therefore depends on λ only through the normalisation κ + λ +
λ′ + μ = 1, that is, through the ratio μ/κ. The proof of Theorem 1 states
the term in the same form, δ(P_n, P_{n+1}) = d(P_n 1, P_{n+1} 1), "where 1
is a vector of ones" and "P_n 1 and P_nᵀ 1 are the marginals of P_n"
(p. 15). Two consequences:

- **Fig. 2's evidence does not test the constraint.** "Values of λ close to
  zero present high abstraction error, demonstrating the benefit of the
  do-calculus constraints in the OT problem" (p. 10). On a ternary grid
  over (κ, λ, μ), moving λ changes the entropy weight relative to the
  cost weight, which does change the plan; the figure cannot separate
  that from any effect of the constraint.
- **Table 1's margins are consistent with it.** In STC_np the best COTA
  setting has e_WASS 0.011 ± 0.003, the same as Pwise OT, independent
  plans with no causal term (0.011 ± 0.002), and e_JSD 0.010 against
  0.013 (p. 10). The large gains in that table are of the ω-cost over the
  Hamming cost, in every method.

The released code (read, not run) builds all chains into one problem. A
plan is given its marginal constraints the first time its intervention
appears; when a later chain reaches an intervention already handled, it
gets a fresh variable with no marginal constraints, coupled to its
neighbour by the δ term, and plans not summing to 1 are dropped at the
end (optimization_functions.py, lines 63–74; runs.py, lines 69–108). In
multi-chain posets the term can therefore act, on unconstrained copies.
That is a different problem from eq. (12), and the paper does not
describe it.

**Approximate COTA** (Appendix F, pp. 19–20) replaces δ by an element-wise
divergence between P^ι/φ(Z) and P^η, which does depend on the plans'
entries; its results (Tables 15–19) are close to COTA's.

### Theorem 1's proof (Appendix B, pp. 15–16)

The conclusion holds, but two steps are misstated. "d is a Bregman
divergence between probability vectors, which is jointly convex in both
its inputs" (p. 15) is false in general; Bregman divergences are convex
in the first argument, and jointly convex only in cases such as squared
Euclidean distance and KL. Neither divergence the experiments use is a
Bregman divergence: JSD is an f-divergence (jointly convex), and the
Frobenius term in the code is the norm, not its square (convex). And the
proof combines "+ μ·H(P_n)" with "the (strict) convexity of H" (p. 16),
while H is the Shannon entropy, which the paper elsewhere calls strongly
concave (p. 31), entering eq. (12) as −μH. Read with −μH and with the
two divergences actually used, the objective is convex; and since δ is
constant on the feasible set, its convexity is not needed there.

### Experiments (§6, pp. 8–10; Appendix E, pp. 19–23)

- **STC** (smoking → tar → cancer, abstracted to smoking → cancer): with
  parent-free interventions COTA with the ω-cost has the lowest error
  (Table 1); with interventions on tar only (two interventions), the
  Hamming cost does better (Table 2, p. 10).
- **LUCAS** (a 9-variable synthetic lung-cancer model to 3 variables):
  COTA lowest, by small margins (Table 4, p. 11: e_JSD 0.263 against 0.294
  for the best baseline).
- **EBM** (battery coating data from two labs): abstraction error favours
  the Hamming cost (Table 3, p. 10). The text says the opposite: "the
  limited size of the interventional data prevents cH to lead to better
  abstractions compared to cω" (p. 10), while Table 3 and its caption
  show cH at 0.220 and cω at 0.379. In the downstream regression, COTA's
  MSE is lower than Zennaro et al.'s in all three tasks (Table 5, p. 11),
  but the first task's spreads overlap (1.40 ± 1.39 against 1.86 ± 1.75).
- **Figure and text disagree** on the grid: "1000 convex combinations"
  (Fig. 2 caption, p. 10) against "100" (p. 9).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Learning a τ-ω abstraction from paired interventional samples can be posed as multi-marginal entropic OT with an ω-cost | strong | construction, §§3–4 |
| C2 | COTA's objective is jointly convex, strictly for μ > 0 | moderate | Theorem 1; the proof misstates Bregman joint convexity and the entropy's sign, but the conclusion holds for the divergences used |
| C3 | The do-calculus constraints make COTA learn better abstractions | weak | Fig. 2 varies λ inside a normalised simplex; as written the term is constant on the feasible set (derived above) |
| C4 | The ω-cost beats a Hamming cost when the intervention set is rich, and not when it is small | moderate | Tables 1, 2, 3, 4 and 6–13; two synthetic models and one dataset |
| C5 | COTA gives lower abstraction error than non-causal OT baselines | moderate | Tables 1, 4; margins small on LUCAS and nil on STC_np's WASS |
| C6 | Data augmented through COTA's map improves downstream regression over the prior method | weak | Table 5; one dataset, overlapping spreads in one of three tasks |

## Method

Algorithm 1 (p. 7): sample each paired distribution, build the ω-cost
matrix, enumerate the maximal chains of I, solve eq. (12) per chain, and
return the stochastic map of the averaged plan (COTA(P̂)) or the average
of per-plan maps (COTA(τ̂)). Hyperparameters (κ, λ, μ) are chosen by grid
search over convex combinations, with evaluation by leaving one
intervention pair out (p. 9).

## Concepts

- **τ-ω transformation** — a map τ on states with an order-preserving
  surjection ω on interventions; exact when τ pushes each base
  interventional law to the paired abstracted one (Definition 4, p. 3).
- **Abstraction error** — the average divergence between τ#(P_{M_ι}) and
  P_{M′_{ω(ι)}} over a distribution on I (Definition 5, p. 3).
- **Compatibility** Cmp(b, ι) — a setting b agrees with intervention ι
  (Definition 3, p. 3).
- **Comparable plans** — plans of interventions on a common chain
  (Definition 7, p. 5).
- **ω-cost** — |I| minus the number of paired interventions with which a
  base state and an abstracted state are both compatible (eq. 11).

## Connections

- **Rubenstein et al. 2017** (exact transformations; the record's [LIT-1334](../literature.d/LIT-1334.md))
  supplies the definition; **Beckers and Halpern 2019** ([LIT-1316](../literature.d/LIT-1316.md), read in
  [NOTE-1032](NOTE-1032.md)) and **Beckers, Eberhardt and Halpern 2020** are cited for the
  general theory and for approximation (pp. 1–3).
- **Zennaro et al. 2023** learns α-abstractions in Rischel's framework but
  needs fully specified SCMs; COTA is compared with it (Appendix D,
  pp. 17–19).
- **[LIT-tmpagj3g](../literature.d/LIT-tmpagj3g.md)** (Simoes, Dastani and van Ommen) cites COTA among
  efforts to learn high-level models, as distinct from its own abstraction
  of a variable for a target.

## Bearing on the record

- **[THEORY-849](../theory.d/THEORY-849.md): COTA's notion is the weakest of those the theory ranks.**
  [THEORY-849](../theory.d/THEORY-849.md) holds that, for deterministic models with countable
  interventions, matching coarse-grained interventional laws for every
  distribution on contexts is a context-by-context commuting condition,
  that "exactness for one distribution is strictly weaker, since a
  well-chosen distribution lets unrelated models match", and that τ- and
  strong abstraction are stronger still. COTA adopts the one-distribution
  notion (Definition 4), relaxes it to an average divergence over a finite
  I (Definition 5), and makes τ stochastic (a Markov kernel, p. 4). It
  does not match [THEORY-849](../theory.d/THEORY-849.md)'s reading of causal abstraction; it is below
  its lowest rung. Whatever an exact transformation can be fooled by, a
  learned stochastic approximation of one can be fooled by too.
- **[CLAIM-399](../claims.d/CLAIM-399.md): applies with more force.** The claim is that exact
  transformation, τ-abstraction and zero approximate distance all accept a
  coarse-graining whose coarse state drops a governing bit, "because each
  lets high-level noise carry what the coarse state drops". A stochastic τ
  is exactly a licence for that: the kernel's randomness can supply what
  the base state does not determine.
- **[CLAIM-414](../claims.d/CLAIM-414.md) and [CASE-179](../cases.d/CASE-179.md): partly supports A7's description, with the
  limit stated.** COTA does fit every paired interventional distribution,
  not only the observational one, so two systems that agree observationally
  and differ under an intervention in I give different fits; the
  leave-one-pair-out error is the right shape of test for [CLAIM-414](../claims.d/CLAIM-414.md)'s
  point that a specified intervention exposes what observation conceals.
  But COTA does not tell systems apart, it assumes the abstraction relation
  and learns a map; it needs both models sampled under every intervention
  and the intervention correspondence ω given; and the part meant to carry
  causal structure between interventions, the do-calculus term, is inert
  as written. For [CASE-179](../cases.d/CASE-179.md) it is a method that takes the correspondence
  between interventions as input, which is the structure that study wants
  to manipulate and recover.
- **[CLAIM-150](../claims.d/CLAIM-150.md): consistent.** A good abstraction here is a distributional
  match, and not even a unique one: the authors call for "guarantees of
  existence and uniqueness of the estimated maps" (p. 11). It says nothing
  about constitution.
- **The exchange's description in the LIT ("a correspondence that respects
  interventions, not only observations") is right about the data and the
  cost and wrong about the do-calculus constraints doing that work.** The
  LIT's summary is corrected.
- **Two THEORYs**: [THEORY-tmp1lvzk](../theory.d/THEORY-tmp1lvzk.md) (the do-calculus term is constant on the
  feasible set; Active, derived) and [THEORY-tmpd2jd5](../theory.d/THEORY-tmpd2jd5.md) (the ω-cost's
  dependence on the intervention set; Proposed).
- **No instruction for ML practice** beyond a method; not an anthology
  candidate on that ground.

## Limitations

- **The do-calculus term, as above.** The paper's headline mechanism is
  untested by its own experiments.
- **Small, discrete problems.** Domains of a few binary or few-valued
  variables; complexity cubic in the domain size (p. 7).
- **Strong inputs.** DAGs, ω and interventional samples from both models
  for every intervention are required.
- **Errors in the text**: Theorem 1's proof steps; the EBM sentence that
  contradicts Table 3; 1000 against 100 grid points.
- **Preprint only.** The CLeaR version may differ.

## Open questions

- Does a version in which the do-calculus relation couples the plans'
  entries (as Approximate COTA's element-wise term does, or a joint plan
  over interventions) beat independent plans with the same cost and
  entropy weight? That ablation, with μ/κ held fixed, is the test the
  paper needs.
- Can ω be learned as well as τ, and with what data? That would make the
  correspondence between interventions an output, which is what the
  record's [QUESTION-282](../questions.d/QUESTION-282.md) asks about.
- How does a stochastic τ learned this way fare against [CLAIM-399](../claims.d/CLAIM-399.md)'s
  hidden-bit construction? A worked case would show whether the learned
  kernel uses its randomness to carry the dropped bit.
