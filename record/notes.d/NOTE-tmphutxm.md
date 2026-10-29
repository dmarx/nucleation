---
status: Read
paper: 'LIT-1411'
title: 'Li, Lin, Duan, Liang and Shroff — Theory on mixture-of-experts in continual learning'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Read on 2026-10-29 from arXiv (https://arxiv.org/pdf/2406.16437, v3
    of 19 February 2025, the ICLR 2025 version, 38 pages), text extracted
    with pdftotext. Read in full: the main paper, §§1–7 (ten pages), with
    Algorithm 1, Lemma 1, Propositions 1–4 and Theorems 1–2 as stated;
    Appendix A (experimental details, the MNIST, CIFAR-100 and Tiny
    ImageNet runs and the termination-threshold experiment). Not read:
    the proofs in Appendices B–J, beyond the statement of Proposition 2's
    full version and the opening lemmas of its proof (F), which were read
    to see what drives the gate outputs together. So the theorems are
    recorded as stated, not as checked. Several displayed equations
    (17)–(22) were garbled in extraction and are summarized, not quoted.
    No number was taken from a chart.
date: '2026-10-29'
summary: >-
  In a stylized continual-learning model, overparameterized linear
  regression tasks drawn from N ground truths, each carrying a feature
  signal a linear gate can read, a top-1 MoE whose gate is trained on a
  "locality" loss plus a Switch-style balancing loss sorts its experts
  into one set per task (or task cluster) within about M/η rounds. If
  gate training continues, the balancing loss eventually erases the gaps
  between experts' gate outputs and routing goes wrong; stopping it once
  the gaps settle keeps specialization, and noise then spreads load
  within each set. Forgetting then decays as 1/t, and more experts only
  lengthen exploration.
---

# NOTE-tmphutxm: Li, Lin, Duan, Liang and Shroff — Theory on mixture-of-experts in continual learning

## Contribution

A first analysis of a mixture-of-experts model learning a sequence of
tasks. In a linear model designed to be analysable, it proves that
experts specialize and the router learns to send each task to its
specialists, gives expressions for forgetting and generalization error
that beat a single model when tasks differ, and finds that the gating
network must stop training at some point or its balancing term undoes
the specialization.

## Key insight

Two pressures act on the gate: a locality loss that rewards sending a
task where the expert's weights need not move, which drives
specialization, and a load-balancing loss that rewards equal use, which
drives all gate outputs together. Early on the first wins and experts
separate into task sets; run long enough, the second wins and the gaps
that encode the separation shrink below the routing noise. Stopping the
gate at the right time keeps the gaps between sets while the routing
noise, larger than the remaining gaps within a set, shares load among
that set's experts.

## Assumptions

- **Tasks (Definition 1).** Each round one of N ground truths w_n is drawn
  uniformly; data X_t ∈ ℝ^{d×s} has one column β_t v_n carrying the
  task's feature signal (‖v_n‖_∞ = O(1)) and s − 1 Gaussian noise columns;
  y_t = X_tᵀ w_n; overparameterized, s < d. Ground truths are close:
  ‖w_n − w_n′‖_∞ = O(σ₀), σ₀ ∈ (0, 1).
- **Experts.** Each updated by the minimum-norm interpolating step from
  its previous weights (eq. 5), the limit of GD in this regime.
- **Gate.** Linear, h_m = Σ_i θ_mᵀ X_{t,i}; top-1 routing on h plus
  Uniform[0, λ] noise; softmax probabilities for the loss. Locality loss
  Σ_m π_m ‖w_t^(m) − w_{t−1}^(m)‖² (eq. 6) plus auxiliary loss
  α·M·Σ f^(m) P^(m) with cumulative fractions since t = 1 (eq. 7).
- **Scalings (Algorithm 1).** Γ = O(σ₀^1.25), λ = Θ(σ₀^1.25),
  α = O(σ₀^0.5), η = O(σ₀^0.5), T₁ = ⌈M/η⌉; Theorem 1 needs
  M = Ω(N ln N), Theorem 2 M = Ω(K ln K) with K clusters,
  intra-cluster gaps O(σ₀^1.5).
- The gate's routing problem is separable by construction: the feature
  signal identifies the task. The paper calls it a "binary
  classification sub-problem"; it is N-way.

## Key results

- **Lemma 1.** Gate outputs for two inputs with the same feature signal
  differ by O(σ₀^1.5), so routing depends on the signal.
- **Proposition 1.** After T₁ = ⌈M/η⌉ rounds each expert sits in one
  task set M_n and its weights stop changing (M > N).
- **Proposition 2.** If the gate keeps training, at t₁ = ⌈M/(ησ₀^0.25)⌉
  gaps are O(σ₀^1.75) within a set and Θ(σ₀^0.75) between sets; by
  t₂ = ⌈M/(ησ₀^0.75)⌉ all gaps are O(σ₀^1.75), and routing errs.
- **Proposition 3.** With termination (all gaps to the chosen expert
  below Γ after T₁), updates stop by T₂ = O(M/(ησ₀^0.25)) and each expert
  in the right set is chosen with probability 1/|M_n|.
- **Proposition 4 (M = 1).** Expected forgetting and generalization
  error grow with Σ_{n≠n′} ‖w_n − w_n′‖² and oscillate; generalization
  error tends to the full model-gap term as T grows.
- **Theorem 1 (M > N).** For t > T₁, E[F_t] = (T₁ − 1)/(t − 1)·E[F_{T₁}],
  which goes to zero; E[G_T]'s model-gap coefficient is fixed at T₁, so
  it is smaller than the single expert's. Larger M lengthens T₁ and
  raises both.
- **Theorem 2 (M < N, clusters).** Adds terms in the intra-cluster gap
  Ψ₁ and a cross term Ψ₂ that more experts cannot remove.
- **Experiments.** Synthetic (d = 10, s = 6, N = 6, K = 3, M ∈ {1, 5, 10,
  20}): with termination forgetting and error rise then fall to near
  zero; without it they oscillate. CIFAR-10 with ResNet-18 and four
  "task types" (airplane, deer, dog, truck), and MNIST, CIFAR-100, Tiny
  ImageNet in Appendix A, show the same pattern. A threshold Γ above the
  noise level λ leaves load unbalanced within sets and raises
  generalization error (App. A, Fig. 9, 100 runs).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | In this model, experts specialize into task sets and routing becomes correct after O(M/η) rounds | moderate | Propositions 1 and 3; proofs not checked here |
| C2 | Continued gate training under the balancing loss destroys the specialization | moderate | Proposition 2; synthetic and DNN runs without termination |
| C3 | Terminating gate updates yields correct routing with balanced load within each set | moderate | Proposition 3; App. A threshold experiment |
| C4 | MoE lowers forgetting and generalization error relative to one expert when tasks differ | moderate | Theorem 1 vs Proposition 4 |
| C5 | Adding experts beyond what the tasks need does not help and delays convergence | moderate | T₁ = ⌈M/η⌉ in Theorem 1; M = 10 vs 20 runs |
| C6 | The insights carry to deep networks | weak | small image-classification runs with an adapted algorithm |

## Method

Algorithm 1: each round, draw routing noise, pick the expert, update it
by (5); after T₁, mark as converged any expert whose gate output is
within Γ of the chosen expert's; while any expert is unmarked, update
all gate parameters by GD on the training, locality and auxiliary
losses (9). Once all are marked the gate is frozen for good.

## Concepts

- **Locality loss**: the softmax-weighted change in expert weights a task
  would cause; small when tasks go to experts already fitted to them.
- **Expert set M_n**: experts whose gate parameter aligns best with v_n.
- **Forgetting F_t**: the average increase in old tasks' model error
  since they were learned; **generalization error G_T**: the final
  model's average error over the rounds' tasks.

## Connections

The balancing loss is Switch Transformers' (LIT-1412), changed to
cumulative counts, and top-1 routing is cited to that paper. The
single-expert baseline follows Lin, Ju, Liang and Shroff's earlier
theory of forgetting in overparameterized linear models, and the MoE
analysis builds on Chen et al.'s (2022) analysis of MoE for single-task
classification; neither is registered here. Wang et al. (LIT-1414) solve
the same tension between balance and learning differently, by taking
balancing out of the gradient instead of stopping it.

## Bearing on the record

- **CASE-117.** The LIT says "its result that the gate must stop updating
  for convergence is a condition CASE-117 should test". The reading
  qualifies this. Termination is necessary here because of the paper's
  own gate objective: the cumulative load-balancing term keeps pulling
  every gate output together, and Proposition 2 shows that pull
  eventually wins. It is not shown to be necessary for MoE in continual
  learning in general, nor for a router without a balancing term in its
  gradient. The condition CASE-117 can test is the narrower one: when
  balance is imposed through the routing gradient, does specialization
  survive continued routing updates? The paper's answer in its model is
  no, unless updating stops.
- **CASE-117, specialization.** The paper does prove specialization among
  identically initialized experts (all w₀ = 0, all θ₀ = 0), with
  symmetry broken by routing noise and the order of task arrivals. That
  matches the case's "operators differ only by initialization and
  experience", with the strong caveat that the tasks carry a signal that
  makes routing separable.
- **QUESTION-083.** "Rare contexts" are not modelled: tasks arrive
  uniformly. Whether a specialist for a rare task survives termination
  is not addressed.

The paper offers design guidance for MoE training and so is
anthology-relevant; it carries the anthology-candidate flag.

## Limitations

- A model built to be analysable: linear tasks, an explicit feature
  signal per task, uniform task arrival, small task differences (σ₀),
  and top-1 routing; the authors say top-k is outside scope.
- Proofs not checked in this reading.
- The DNN experiments adapt Algorithm 1 and use few classes; they show
  the termination effect qualitatively.
- **Slips.** (i) σ₀ is called "the variance" while it bounds ‖w_n − w_n′‖_∞
  and is used as a standard deviation in the synthetic data (N(0, σ₀)).
  (ii) The routing sub-problem is called binary. (iii) The synthetic
  runs use M = 5 and 10 with N = 6, below Theorem 1's M = Ω(N ln N)
  (N ln N ≈ 10.8), and the CIFAR-10 run calls 300 rounds "N = 300 tasks"
  drawn from K = 4 types.

## Open questions

- Is termination needed with a balancing rule outside the gradient, such
  as LIT-1414's bias, or with no balancing at all?
- What happens with non-uniform, drifting task frequencies, or new tasks
  arriving after termination? A frozen gate cannot route an unseen task
  to a fresh expert.
