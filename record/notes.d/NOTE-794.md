---
number: 794
status: Read
formerly:
- NOTE-tmpknpce
paper: LIT-951
title: 'Liu et al. — Physics of Skill Learning'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv PDF (2501.12391v1, 21 January 2025,
    29 pages, "Preprint. Under review."), text extracted with pdftotext:
    §§1–8, every model definition and derivation (Eqs. 1–13), Appendix A,
    and every figure caption. Plotted values were read from captions and
    text, not off the images; several figure panels extract as unordered
    numbers. The references were consulted only for the works named below.
date: '2026-10-14'
summary: >-
  Three toy models of skill learning. In the Geometry model, independent
  skills are orthogonal directions in parameter space weighted by
  frequency. Under SGD each is learned at its own rate, the second taking
  about 1/p₂ as long. Under sign descent they compete for coordinate
  signs, and each starts as the one before finishes (the Domino effect),
  so the n-th skill takes time ∝ n. A one-parameter Resource ODE fits
  these curves and has exact conserved quantities u_i^(1/p_i). A small MLP
  also shows the effect when one parity is the XOR of two others.
---
<!-- inactive-ok-file: THEORY-186 THEORY-212 THEORY-039 — Proposed; the account filed from this reading and the accounts of acquisition order it is set beside -->

# NOTE-794: Liu et al. — Physics of Skill Learning

## Contribution

The paper names the Domino effect: skills learned in sequence, some
starting just as others finish. It builds three toy models of decreasing
detail to explain it. It shows that, in the most detailed model, the
effect depends on the optimizer. Gradient descent on orthogonal skills
gives no Domino. Sign descent does, and Adam lies between. It also gives
an ODE with one fitted parameter that reproduces those curves and admits
exact conserved quantities.

## Key insight

When skills share parameters, a coordinate-wise nonlinear optimizer makes
them compete for a fixed budget of update directions. The dominant skill
takes almost all the signs until its gradient vanishes, and only then
does the next one move. Under plain gradient descent, orthogonal skills
do not interact, and each simply proceeds at a rate proportional to its
frequency.

## Assumptions

- **Geometry model (§2.2).** The loss is ℓ = Σ_i p_i L(s_i), with skill
  level s_i = (θ − θ₀)·t_i for a fixed task vector t_i, and
  L(s) = (1 − s)² or −log σ(s). Its assumptions are:
  - Skills are independent: the loss is a weighted sum.
  - Skills are linearly represented: the paper appeals to task
    arithmetic.
  - Frequencies are Zipfian, p_i ∝ i^(−α).
  - Task vectors are random Gaussian. They are orthogonalised when
    n_task ≤ n_dim ("overparametrized") and correlated otherwise.
- **Resource model (§2.4).** Skills draw on a shared pool in proportion
  to their gradient magnitudes N_i = p_i u_i, with u_i = 1 − s_i. One
  phenomenological constant N₀ stands for the resources not allocated to
  any task. The ODE is matched to the Geometry model under SignGD.
- **Domino model (§2.6).** The Resource model with N₀ = 0 and a strong
  hierarchy p₁ ≫ p₂ ≫ ….
- **What the models leave out (§8).** They describe training loss only,
  with no generalisation gap. Each per-skill loss is convex. Each data
  point belongs to exactly one skill. No map from real data to skills is
  given.

## Key results

- **Domino effect, observed (§1, Fig. 2).** Two sparse-parity tasks with
  p₁ = 1 and p₂ = 0.1, a two-layer MLP, Adam: task 2 progresses rapidly
  only after task 1 finishes. It takes about two times as long, not
  p₁/p₂ = 10 times.
- **Optimizer dependence (§2.3, Fig. 4).** Geometry model, two orthogonal
  tasks, n_dim = 1000, batch 128.
  - SGD: the convergence time of task 2 grows "roughly ∼ 1/p₂".
  - SignGD: the delay is constant, and the ratio t₂/t₁ saturates at 2
    as p₁/p₂ grows.
  - Adam: in between, sub-linear in p₁/p₂.
  - The explanation: sign(g₁ + g₂) ≈ sign(g₁) when ‖g₁‖ ≫ ‖g₂‖. The
    count of sign-aligned coordinates n_i,align falls for task 1 as it
    rises for task 2 (Fig. 5). *Holds:* in simulation.
- **Many tasks (Fig. 5).** With p_i ∝ i^(−α), α ∈ {1, 2, 4} and n_task
  up to 10, under SignGD, skills are learned in order of frequency. The
  Domino form "seems to be valid only for large α and the first few
  skills".
- **Resource model, Eq. (1).** du_i/dt = −η_eff p_i u_i /
  (Σ_j p_j u_j + N₀), with η_eff = 2√n_dim η_geo, matched for one task.
  - **Exact conserved quantities:** u_i^(1/p_i) = C for all i, the same C.
  - **Time to reach C:** t = (n_task − Σ_j C^(p_j))/η_eff + (−N₀ ln C)/η_eff
    (Eq. 3). The first term grows in proportion to n_task, the second
    to N₀.
  - **Fit:** N₀ ≈ 0.003 matches the Geometry model in the default case
    (Fig. 7). It rises with learning rate, gradient noise and smaller
    batches, and does not change with α or n_task.
- **Domino model, Eq. (6).** With N₀ = 0 and strong hierarchy, the Resource
  model reduces to strict sequence: skill n rises linearly between n·t₀
  and (n + 1)·t₀, with t₀ = 1/η_eff. So t_n ∝ n. The Quanta model's SGD
  assumption gives t_n ∝ 1/p_n ∝ n^α instead.
- **Scaling exponents (§3).**
  - Quanta model: α_N = α − 1, α_S = (α − 1)/α.
  - Domino model: α_N = α_S = α − 1.
  - Geometry model at α = 1 (simulated, n_task = 1000): α_N ≈ 0.34,
    which "happens to be" the Chinchilla value. Under SignGD its α_S
    follows the Domino line at large α.
  - Multitask sparse parity MLPs (n_tasks = 500, n = 100, k = 3)
    land between the two lines, depending on Adam's betas (Fig. 11).
- **Quadratic loss (§4.1, Fig. 12).** ℓ = x₁² + 0.1x₂² + 0.01x₃² +
  0.001x₄², with x = Rθ.
  - SGD gives the same dynamics for R = I and for a Hadamard R.
  - SignGD synchronises the four losses when R = I and gives a Domino
    sequence when R = H₄.
  - So the Domino effect needs the loss's eigendirections to be
    misaligned with the coordinates the optimizer acts on.
- **Dependence (§5.1, Fig. 16).** A two-layer MLP, Adam, 10,000 samples,
  learns y₁ = x₁⊕x₂, y₂ = x₃⊕x₄ and y₃ = x₁⊕x₂⊕x₃⊕x₄. Task 3 starts
  only after tasks 1 and 2 reach perfect accuracy. Replacing y₃ with an
  independent 4-parity, x₅⊕x₆⊕x₇⊕x₈, delays it "much" more. So the
  network uses y₁ and y₂. A soft-AND factor B(u₁, u₂) in the Resource
  model reproduces the curve, but it is chosen by hand, with γ = 0.01
  (Eqs. 10–12).
- **Modularity (§6).** With dedicated parameters per skill, the Domino
  model gives total time ∝ √n_task instead of ∝ n_task. One MLP
  experiment, (x, y) → (x², y²) with y sparse, shows t₂ ≳ 2t₁ without
  modularity and t₂ ≈ t₁ with it (100 seeds, Fig. 19).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | In the Geometry model, the Domino effect appears under sign descent and not under gradient descent | moderate | simulations, Figs. 4–5, and the quadratic example, Fig. 12 |
| C2 | Under gradient descent on orthogonal skills, the time to learn a skill scales as 1/p | moderate | Fig. 4b; follows from the decoupled linear dynamics |
| C3 | The Resource ODE has n_task − 1 conserved quantities u_i^(1/p_i) | strong | derivation from Eq. (1) |
| C4 | A single N₀ fits Geometry-model dynamics across data distributions | moderate | Fig. 7 fits |
| C5 | Dependent skills start after their prerequisites, beyond what frequency predicts | moderate | one MLP experiment with an ablation, Fig. 16 |
| C6 | The Geometry model reproduces Chinchilla's α_N ≈ 0.34 at Zipf α = 1 | weak | one simulation family; the authors' "happens to be" |
| C7 | Modular networks learn imbalanced skills in parallel | weak | one two-variable MLP task, Fig. 19 |

## Method

The paper's method is to simulate toy models and fit their curves. The
Geometry model is trained with SGD, SignGD, Adam, AdEMAMix or Lion. The
Resource ODE is solved numerically with N₀ fitted by eye. The Domino model
is derived from the Resource model in a limit.

## Concepts

- **Skill / task.** A unit of loss with frequency p_i, linearly
  represented by a direction t_i in parameter space. The terms are used
  interchangeably.
- **Domino effect.** Sequential learning of skills in which "some skills
  kick off learning right after others complete learning".
- **Resource.** The number of coordinates whose update sign agrees with a
  skill's gradient, n_i,align. In the Resource model it becomes an
  abstract share Ñ_i of the gradient magnitude.
- **N₀.** Wasted resources, a phenomenological constant set by optimizer
  details.

## Connections

It extends the Quanta model of Michaud et al. (2023): skills as discrete
units with Zipfian frequencies. That model assumed learning time ∝ 1/p,
which this paper says holds only for SGD. It draws on Song et al. (2024)
for a resource interpretation of scaling, on task arithmetic (Ilharco et
al.; Ortiz-Jiménez et al.) for linear representation, and on
Shalev-Shwartz et al. (2017) for the hardness of k-parities.

## Bearing on the record

- **[QUESTION-039](../questions.d/QUESTION-039.md).** The paper adds a factor that the question does not
  list: the optimizer. In its toy model, the order of acquisition is set
  by frequency whatever the optimizer. Whether acquisitions are
  sequential or simultaneous, and how the n-th one's time scales (∝ n or
  ∝ n^α), is set by the optimizer. It also shows a second, different
  cause of sequential onset, dependency between skills. This bears on
  whether acquisition is one kind of event: on its evidence there are at
  least two. Held as [THEORY-253](../theory.d/THEORY-253.md).
- **[THEORY-229](../theory.d/THEORY-229.md), filed today from [LIT-242](../literature.d/LIT-242.md), and [THEORY-186](../theory.d/THEORY-186.md)/[THEORY-187](../theory.d/THEORY-187.md).** These
  get stepwise acquisition under gradient flow from *small
  initialization*: each mode waits near an unstable equilibrium for a
  time ∝ log(1/scale)/eigenvalue. The Geometry model has no such
  equilibrium. Its loss is convex in θ − θ₀, quadratic for squared error, and from θ₀ gradient
  descent moves every skill at once. The stepwise behaviour here comes
  instead from the optimizer's coordinate-wise sign. So [THEORY-229](../theory.d/THEORY-229.md) and
  this paper describe two different mechanisms for one-at-a-time
  acquisition, and they predict differently under a change of optimizer:
  [THEORY-229](../theory.d/THEORY-229.md)'s steps are a property of gradient flow, while these vanish
  under it. Under SGD the Geometry model behaves like the kernel picture
  of [THEORY-086](../theory.d/THEORY-086.md): every direction is fitted at once, at a rate set by its
  weight.
- **[THEORY-212](../theory.d/THEORY-212.md).** There, a conserved quantity of the initialization
  decides between staged and simultaneous learning. Here the optimizer
  does. Both say "staged or not" is not fixed by the data alone.
- **[LIT-951](../literature.d/LIT-951.md)'s seeded claim.** It says the three models "explain the
  order". The reading corrects this. The order is frequency order in
  every case. What the models explain is the *timing* and the
  sequential onset, and only under sign-based optimizers. The status_note
  and summary are corrected.
- **Machine-learning practice.** The paper's proposals belong in the
  anthology if anywhere and are not filed here: loss reweighting on GPT-2
  (§4.3), SignGD against grokking (§4.2), and optimizer comparisons
  (§4.4).

## Limitations

- The Domino effect in the Geometry model is shown in simulation only. No
  analysis of SignGD dynamics is given. The Resource model is fitted to
  it, not derived.
- The Domino model is a limit of the Resource model, and a fitted ODE
  stands in for the optimizer, so the claims about scaling exponents
  rest on the fit.
- The real-network evidence is small. It is a few MLP experiments on
  sparse parities and one two-variable regression, with Adam.
- The paper says its models do not describe overfitting, are convex
  per skill, and give no map from data to skills (§8).

## Open questions

- Does the Domino effect appear under Adam in a solvable model, and does
  its strength track β₂? An analysis of SignGD on the quadratic of
  Eq. (9) with a rotation R would settle the mechanism.
- In a real network, can the frequency ordering be separated from the
  dependency ordering? Fig. 17's Resource-model cases predict that
  dependency overrides frequency, and that prediction is untested.
