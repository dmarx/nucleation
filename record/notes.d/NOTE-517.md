---
number: 517
status: Read
formerly:
- NOTE-tmp54otp
paper: 'LIT-666'
title: 'Mode Connectivity and Data Heterogeneity of Federated Learning'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full from the arXiv HTML of v1, main text, Appendix A, and
    Appendix B through Proposition 1, Lemma 2 and the proof of Theorem 1;
    the Theorem 2 proof was followed for its structure (it applies
    Kuditipudi et al.'s construction). Figures were read from captions and
    text; numbers below are those the text states.
date: '2026-10-03'
summary: >-
  FedAvg, 10 clients, 200 rounds, Dirichlet label skew α ∈ {0.1, 0.2, 0.5}
  and PACS. Client/global low-loss overlap shrinks with heterogeneity;
  global models from one start under different α disagree on > 20% of
  inputs, are separated on the line (about 10% accuracy drop) and joined by a
  one-bend chain. Theory: ε_C = C e^{C T_max} max(√h(α), √h(α′))((√log N +
  z)/√N + √ε(√(D + log N) + z)), via mean-field dropout stability. MNIST
  two-layer net: dropout error < 0.01 at N = 6400, up to 0.06 at N = 200.
---

# NOTE-517: Mode Connectivity and Data Heterogeneity of Federated Learning

## Contribution

It is a first look at mode connectivity in federated learning. It compares
client models with the global model, and global models trained under
different heterogeneity with each other, and gives a bound that ties
connectivity error to a heterogeneity factor and to width.

## Key insight

Heterogeneous clients pull the global model's update in different
directions, and that disagreement behaves like extra noise in SGD. Extra
noise worsens dropout stability, and dropout stability is what guarantees a
short low-loss path between solutions, so heterogeneity loosens
connectivity, and width tightens it.

## Assumptions

- **FedAvg** with K = 10 clients, global model θ = Σ_k (n_k/n) θ_k. Section
  III: 200 rounds, SGD lr 0.01, momentum 0.9, batch 50, 1 local epoch,
  dropout 0.5 for VGG. Section VII: 50 / 200 rounds for MNIST / CIFAR-10,
  lr 0.02 / 0.01, 10 local iterations, 20 trials.
- **Heterogeneity**: Dirichlet label skew Dir(α); PACS domain shift for
  feature skew.
- **Modes**: permutations of the same neurons count as the same mode
  (§III).
- **ε_C-connectivity** (Def. 1): a path with L ≤ max(L(θ₁), L(θ₂)) + ε_C
  throughout.
- **Theory** (§VI): a two-layer network f_θ(x) = (1/N) Σ σ(⟨x, θ_i⟩), ReLU,
  squared loss, one-pass i.i.d. sampling from the global distribution.
  Assumptions 1–4 are Mei et al.'s mean-field conditions on step size, data,
  activation and initialisation. Assumption 5 models the heterogeneity
  term n_i (gradient drift plus output bias, Eq. 7) as √(βh(α)) times a
  standard Gaussian, with h(α) larger for smaller α.
- **Barrier metric** (Eq. 4): B = max_a |L(π(a)) − min(L(θ), L(θ′))| / |L(θ) −
  L(θ′)| − 1, normalised by the endpoints' loss difference.

## Key results

- **Client modes** (Figs. 2–4): lower test loss than the global model on
  their own data but outside its low-loss region; linear paths from clients
  to the global model can reach the global low-loss region. On the
  client-to-client path through the global model, the point that serves
  both clients drifts away from the global model under α = 0.1.
  Pre-training narrows the gap between linear and chain paths (App. A-A,
  Fig. 11).
- **Global modes** (Figs. 5–7, 13): line barrier higher for (0.1, 0.2) than
  (0.1, 0.5), growing with rounds after an initial oscillation; no barrier
  on the polygonal chain; more samples needed to find the chain under more
  heterogeneity (Fig. 6, right); function dissimilarity > 0.2; pairwise
  distance smaller than distance to initialisation.
- **Lemma 1** (mean-field approximation): sup_τ |L_N(θ^τ) − L(ρ_{τε})| ≤
  C e^{CT} √h(α)((√log N + z)/√N + √ε(√(D + log N) + z)) with probability
  ≥ 1 − e^{−z²}, stated for h(α) ≤ C₅.
- **Theorem 1**: the global model is ε_D-dropout stable for a subset A,
  with ε_D = C e^{CT} √h(α)((√log|A| + z)/√|A| + √ε(√(D + log N) + z)),
  stated for h(α) ≥ C₅.
- **Theorem 2**: two global models under h(α), h(α′) are ε_C-connected with
  ε_C as in the summary, by a path of 7 line segments.
- **Numerics** (§VII): dropout error falls as α rises, ε_D < 0.04 on MNIST
  and < 0.15 on CIFAR-10 (Fig. 8); at α = 0.1, dropout error < 0.01 at N =
  6400 and up to 0.06 at N = 200; the line barrier between global models
  falls with width and is higher for (0.1, 0.2) than (0.1, 0.5) at N = 200
  (Fig. 9). Update-noise norms fall with α and with N, stay below 0.012,
  and are weakly correlated with iteration for α ≥ 0.4 (Figs. 10, 14).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Heterogeneity reduces the overlap of client and global low-loss regions | moderate: landscape slices on VGG11, two α values and PACS | Figs. 2–3, 11 |
| C2 | FedAvg global models from one start under different heterogeneity are distinct modes, barrier-separated on the line and chain-connected | moderate: one start, CIFAR-10, three α | Figs. 5–7, 13 |
| C3 | Connectivity error grows with √h(α) and shrinks with width | moderate as a bound under Assumption 5 for two-layer networks; trends matched on MNIST | Thms. 1–2, Fig. 9 |
| C4 | Heterogeneity acts on FedAvg as iteration-independent Gaussian noise | weak: noise-norm plots only | Assumption 5, Fig. 10 |

## Concepts

- **client mode / global mode**: solutions of a client's objective and of
  the federated objective (Eq. 3).
- **h(α)**: a generalised function of the Dirichlet parameter measuring the
  effect of heterogeneity on update noise.
- **ε_D-dropout stability** (Def. 3): |L_N(θ) − L_{|A|}(θ_S)| ≤ ε_D for the
  subnetwork on neurons A.
- **PolyChain**: Garipov et al.'s one-bend polygonal chain (Eq. 2).

## Connections

- **Kuditipudi et al. ([LIT-671](../literature.d/LIT-671.md))**: dropout stability implies a
  piecewise-linear low-loss path; Theorem 2 applies it.
- **Shevchenko & Mondelli (2020); Mei, Montanari & Nguyen (2018); Mei,
  Misiakiewicz & Montanari (2019)**, not in the record: the mean-field
  approximation and dropout-stability results the proofs adapt, adding
  √h(α) outside the constant.
- **Garipov et al. ([LIT-673](../literature.d/LIT-673.md))**: the curve-finding objective (Eq. 1) and
  the polygonal chain.
- **Draxler et al. ([LIT-653](../literature.d/LIT-653.md))**: cited with Garipov et al. for
  connectivity in centralised training.
- **Entezari et al. ([LIT-652](../literature.d/LIT-652.md))**: permutation as a cause of line
  barriers; the paper's function-dissimilarity test is offered as evidence
  that these global models are genuinely different modes.
- **FedAvg ([ANTH-LIT-307](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-307.md))**: the algorithm studied.

## Bearing on the record

- Evidence for the THEORY candidate on data structure setting the barrier
  (with the GNN reading), and a counter-case to Mirzadeh et al.'s
  shared-start linear connectivity. Not filed.
- Any instruction is implicit (prefer wider models, pre-trained starts);
  the flag follows [ADR-027](../decisions.d/ADR-027.md)'s batch rule.

## Limitations

- **The two theorems' conditions conflict as written**: Lemma 1 requires
  h(α) ≤ C₅ and Theorem 1, which uses it, states h(α) ≥ C₅.
- **The theory is for two-layer networks, squared loss and one-pass data**;
  the experiments use VGG11, CNNs and cross-entropy.
- **Assumption 5** replaces the structured drift of Eq. 7 with isotropic
  Gaussian noise.
- **The barrier metric (Eq. 4)** divides by |L(θ) − L(θ′)|, which is
  undefined when the endpoints' losses are equal and large when they are
  close.
- Landscape findings rest on two-dimensional slices and t-SNE projections.

## Open questions

- Is there an explicit form for h(α)?
- Can FedAvg be steered towards the solutions that serve both client and
  global objectives, which §IV says it overlooks?
