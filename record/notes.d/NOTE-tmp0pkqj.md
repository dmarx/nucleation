---
status: Read
paper: LIT-962
title: 'Calo et al. — Bisimulation metrics are optimal transport distances'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv PDF (v2 of 11 June 2024, 36 pages),
    fetched from arxiv.org/pdf/2406.04056 and extracted with
    pdftotext -layout: the main text (§§1–6), Appendix A (related work on
    bisimulation and optimal transport), Appendix B (the MDP formulation,
    Theorem 3, and the proof of Lemma 1), Appendix C (the proof of
    Theorem 2, followed at the level of its lemmas and theorems 4 and 5),
    Appendix D (Sinkhorn Policy Iteration and Theorem 6), Appendix E
    (Proposition 1, the rounding procedure, Lemma 8) and Appendix F (the
    experiments). The NeurIPS 2024 camera-ready was not compared with
    this version. Figures were read from their captions only.
    Expressions were restored by eye where extraction split them.
date: '2026-10-14'
summary: >-
  For two finite Markov chains with real-valued state labels, the
  discounted bisimulation metric of Ferns et al. and van Breugel and
  Worrell solves the same fixed-point equation as the optimal-transport
  distance over bicausal couplings with ground cost (1−γ)|r(x)−r(y)|, so
  the two are one object. That distance equals the value of a finite
  linear program over discounted occupancy couplings, and an
  entropy-regularised alternating-projection method (Sinkhorn Value
  Iteration) reaches ε accuracy in O(‖c‖²∞ log(|X||Y|)/((1−γ)⁵ε²))
  iterations under exact inner projections.
---
<!-- inactive-ok-file: QUESTION-008 CLAIM-034 — Deferred or Proposed; the set-aside question this work was filed for and its surviving one-way claim, cited as open -->

# NOTE-tmp0pkqj: Calo et al. — Bisimulation metrics are optimal transport distances

## Contribution

The paper makes two contributions. The first is an identification: the
standard bisimulation metric between Markov chains is an optimal-transport
distance between their path laws, restricted to couplings that respect
time (bicausal couplings). The authors say no one had stated this before.
The second is a reformulation: that infinite-dimensional transport problem
equals a finite linear program over "occupancy couplings", whose size is
fixed by the two state spaces. On that program an entropy-regularised,
Sinkhorn-style method gets a convergence guarantee and runs faster than
earlier methods.

## Key insight

A bisimulation metric asks how cheaply the two processes can be run side by
side, step by step, when each one's next state may depend only on the joint
past. Each step pays the label difference. Such a coupling may not look at
the other chain's future. That restriction is what separates it from an
ordinary transport distance between path laws. Because the coupling is a
policy in an MDP over state pairs, the problem has a Bellman equation and a
dual linear program, as optimal control does.

## Assumptions

- **Finite chains, no actions.** M_X = (X, P_X, ν0,X) and
  M_Y = (Y, P_Y, ν0,Y), with |X| = m and |Y| = n finite and stationary
  kernels. The initial states are fixed, X0 = x0 and Y0 = y0, "without
  significant loss of generality".
- **A ground cost on state pairs.** c : X × Y → R+ is given. For the
  bisimulation identity it is c(xy) = (1−γ)|r(x) − r(y)| for a real-valued
  labelling r : X ∪ Y → R.
- **Discounting.** γ ∈ (0, 1). The cost of a pair of sequences is
  c_γ(x, y) = Σ_t γ^t c(x_t, y_t).
- **Bicausal couplings.** A coupling M_XY of the two path laws is bicausal
  if Σ_{y_n} M_XY(x_n y_n | x^{n−1} y^{n−1}) = M_X(x_n | x^{n−1}), and
  symmetrically for Y. That is, given the joint past, each chain's next
  state has its own law and does not depend on the other chain's next
  state.
- **Exact inner projections** (m = ∞) for the convergence theorems. The
  practical algorithm uses small m, and its guarantees do not cover that
  case (§6).

## Key results

- **Definition (Eq. 2).** W_γ(M_X, M_Y; c, x0, y0) = inf over
  M_XY ∈ Π_bc of ∫ c_γ(X, Y) dM_XY.
- **Bellman form (Eq. 3; Theorem 3 in App. B, after Moulos 2021).** The
  infimum is attained by a Markovian transition coupling π*. Its value
  V*(xy) = W_γ(M_X, M_Y; c, x, y) is the unique solution of
  V*(xy) = c(xy) + γ inf_{p ∈ Π_xy} Σ_{x'y'} p(x'y') V*(x'y'), where Π_xy is
  the set of couplings of P_X(·|x) and P_Y(·|y). *Holds when:* the chains
  are finite and γ < 1. The proof applies Bertsekas (1977) under its
  contraction assumption.
- **The identification (§2.2, Eqs. 4–5).** For a chain with no actions,
  the bisimulation metric of Ferns et al. (2004) is the unique solution of
  U*(xy) = (1−γ)|r(x) − r(y)| + γ inf_{p ∈ Π_xy} Σ p(x'y') U*(x'y'), and
  U*(xy) = d_γ(M_X, M_Y; r, x, y), the logical (Desharnais et al.)
  bisimulation metric. Comparing this with Eq. 3, "bisimulation metrics
  and our notion of optimal transport distances coincide when picking the
  ground cost function c(xy) = (1 − γ)|r(x) − r(y)|". *Holds when:* the
  chains have no actions and the labels are real-valued. The step is a
  side-by-side comparison of two fixed-point equations with unique
  solutions. The equality of the fixed point with the logical definition
  is cited to van Breugel and Worrell (2001), not reproved.
- **Occupancy couplings (Lemma 1).** For a transition coupling π, let
  µ^π(xy, x'y') = (1−γ) E_π[Σ_t γ^t 1{(X_t,Y_t) = xy, (X_{t+1},Y_{t+1}) = x'y'}].
  A distribution µ over (X×Y)² is the occupancy coupling of some valid
  transition coupling if and only if it satisfies three linear systems:
  - the flow constraint (6):
    Σ_{x'y'} µ(xy, x'y') = γ Σ_{x'y'} µ(x'y', xy) + (1−γ)ν0(xy);
  - transition coherence for X (7):
    Σ_{y'} µ(xy, x'y') = P_X(x'|x) Σ_{x''y''} µ(xy, x''y'');
  - transition coherence for Y (8), the same with the roles swapped.
- **Theorem 1 (the LP).** W_γ(M_X, M_Y; c, x0, y0) =
  (1/(1−γ)) · inf over µ ∈ B ∩ S_X ∩ S_Y of ⟨µ, c⟩. The program has
  |X|²|Y|² variables. The authors state that, by Ye (2011), it is solvable
  in strongly polynomial time by simplex or policy iteration. They assert
  this ("one can show") and do not prove it.
- **Sinkhorn Value Iteration (§4, Eqs. 9–10).** The method runs mirror
  descent on ⟨µ, c⟩ with the conditional relative entropy
  H(µ‖µ') = Σ µ(xy, x'y') log(π_µ(x'y'|xy)/π_µ'(x'y'|xy)), projecting
  alternately onto B_X (constraints 6 and 7) and B_Y (constraints 6 and 8).
  Each projection solves a soft Bellman fixed point, V_k = T_X^{π_k} V_k,
  and then updates π_{k+1}(x'y'|xy) ∝ π_k(x'y'|xy) exp(−η Q_k(xy, x'y')) on
  each P_X(x'|x) slice. Proposition 1: these closed-form updates are the
  mirror-descent steps.
- **Theorem 2.** Take η = (1/(4‖c‖∞)) √((1−γ)³ log(|X||Y|)/K) and a uniform
  initial coupling. Then the rounded output satisfies
  V^{π_out}(x0y0) ≤ W_γ(M_X, M_Y; c, x0, y0) + ε once
  K ≥ 324 ‖c‖²∞ log(|X||Y|) / ((1−γ)⁵ ε²). *Holds when:* the inner fixed
  points are solved exactly (m = ∞). The proof splits the error into
  mirror-descent regret (Theorem 5: Σ_k ⟨µ_k − µ*, c⟩ ≤ H(µ*‖µ1)/η + 2‖c‖∞)
  and rounding error from constraint violations (Theorem 4).
- **Theorem 6 (Sinkhorn Policy Iteration, App. D).** With
  η = ((1−γ)/(3‖c‖∞)) √(8 log(|X||Y|)/K), the same guarantee holds for
  K ≥ 5 ‖c‖²∞ log(|X||Y|) / ((1−γ)⁴ ε²). The policy evaluation is exact
  and the iterate is rounded at every step.
- **Cost per iteration (App. F.2).** |X|²|Y|² operations, or |X||Y|S² if at
  most S states are reachable in one step.
- **Experiments (§5, App. F).**
  - On the 4-rooms environment, convergence is "basically unaffected by
    m", and m = 1 remains competitive.
  - On randomly generated chains, SVI and SPI reach a near-optimal coupling
    up to ten times faster than EntropicOTC (O'Connor et al.) and dWL
    (Brugère et al.). The authors trace the speed-up to warm-starting the
    couplings, and say the other methods become competitive when given the
    same warm start.
  - The distances between a 9-state grid and a 4-rooms chain reflect the
    rooms' rotational symmetry. An MDS embedding of 35 4-rooms instances
    clusters them by how many doors stand between the start and the
    nearest reward.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The discounted bisimulation metric between finite labelled Markov chains equals the bicausal OT distance with ground cost (1−γ)\|r(x)−r(y)\| | strong | uniqueness of the two fixed points, Eqs. 3 and 5; the logical form is cited, §2.2 |
| C2 | The bicausal OT distance equals the value of a finite LP over occupancy couplings | strong | Lemma 1 and Theorem 1, proved in App. B |
| C3 | Sinkhorn Value Iteration reaches ε accuracy in O(‖c‖²∞ log(\|X\|\|Y\|)/((1−γ)⁵ε²)) iterations | strong, under exact inner projections only | Theorem 2, App. C |
| C4 | In practice SVI and SPI are faster than earlier dynamic-programming methods | moderate | timing on random chains, App. F.2; hyperparameters tuned per method against a ground truth |
| C5 | The approximate inner steps (small m) do not degrade convergence | weak | 4-rooms experiments only; the authors leave it as a conjecture, §6 |
| C6 | The bisimulation metric is a pseudometric that is zero exactly on bisimilar states | strong, but second-hand | cited to van Breugel and Worrell (2001) and Desharnais et al. (2002), App. A.1 |

## Method

The method is Sinkhorn Value Iteration. It starts from the independent
coupling P_X ⊗ P_Y. In odd rounds it iterates the Bellman–Sinkhorn operator
T_X^{π_k} m times to obtain V_X, forms
Q_k(xy, x'y') = c(xy) + γ Σ_{x''} P_X(x''|x') V_k(x'y', x''), and reweights
π_k multiplicatively within each X-marginal slice. Even rounds do the same
with the roles of X and Y swapped. It averages the occupancy couplings,
rounds the average to a valid transition coupling (Altschuler et al.), and
evaluates that coupling exactly by solving the linear Bellman system.

## Concepts

- **Bicausal coupling.** A joint process of the two chains in which, given
  the joint past, each chain's next state keeps its own conditional law.
  Neither chain may "see" the other's future.
- **Transition coupling.** A map π : X×Y → Δ(X×Y) with π(·|xy) ∈ Π_xy,
  that is, a coupling of P_X(·|x) and P_Y(·|y) in each state pair. These
  are the stationary deterministic policies of the MDP in App. B.
- **Occupancy coupling.** The discounted distribution of
  consecutive state-pair transitions under a transition coupling, a finite
  object (a distribution on (X×Y)²) that stands in for the
  infinite-dimensional joint law.
- **Bisimulation metric.** As used here, the metric of Desharnais et al.
  and van Breugel and Worrell for labelled Markov chains, in the
  fixed-point form of Ferns et al. with no actions. It is not the metric
  for labelled transition systems with actions, nor the weak-bisimulation
  metric.

## Connections

The paper puts together two literatures that it says had not met. One is
probabilistic bisimulation (Larsen and Skou; Desharnais et al.; van
Breugel and Worrell; Ferns et al. for MDPs). The other is adapted, or
bicausal, optimal transport (Backhoff-Veraguas et al.; Moulos; O'Connor et
al.; Brugère et al.). Chen, van Breugel and Worrell (2012) had an LP for
bisimulation metrics with one constraint per next-state coupling, which is
intractable as stated. Eckstein and Pammer's Sinkhorn method for adapted
transport is close for finite horizons. Appendix A.1 records that Bian and
Abate (2017) show ε-bisimilar processes give close distributions over
finite-length label sequences in total variation, "but the reverse
implication is not shown to hold". The sequel, [LIT-948](../literature.d/LIT-948.md), starts from this
paper's LP and removes the need to know the kernels.

## Bearing on the record

- **[QUESTION-008](../questions.d/QUESTION-008.md).** This is the first reading in the record of what
  approximate bisimulation is, formally, and it bears on the question at
  the level of definitions only.
  - **What it supplies.** Approximate bisimulation between action-free
    chains has an exact quantitative form. It is a bicausal transport cost,
    with distance zero on bisimilar states (C6, second-hand). The
    approximate counterpart of the bisimulation relation is therefore a
    number, not a relation with a tolerance.
  - **What it does not supply.** [QUESTION-008](../questions.d/QUESTION-008.md) is about communicative
    systems updated by utterances, that is, about labelled transition
    systems with actions, or about intervention sequences a_1:k as in
    [TERM-033](../terms.d/TERM-033.md). This paper's chains have no actions. The extension to
    MDPs is Ferns et al.'s, mentioned and not developed. Nor does it state
    a judgement that trace or observational equivalence gets wrong and
    bisimulation gets right, which is what the question says an answer
    must name.
  - **The ordering [QUESTION-008](../questions.d/QUESTION-008.md) needs.** Through Bian and Abate, the paper
    reports one direction of the ordering the question relies on:
    near-bisimilar implies near trace-equivalent, but not conversely. That
    is the right direction for A40's ordering of the candidates. It is
    cited, not proved, here.
  - **The record's reading, not the paper's.** In this formulation,
    dropping the bicausality constraint leaves an ordinary transport
    distance between the path laws. When the cost depends only on labels,
    that distance depends only on the label-sequence laws, so it is of the
    trace kind. If so, the gap between trace distance and bisimulation
    distance is exactly the constraint that a coupling may not anticipate.
    The paper says the general coupling "does not respect the temporal
    structure" (§2.1), and does not state this consequence.
- **[LIT-962](../literature.d/LIT-962.md)'s own entry** cites the paper as showing that "bisimulation
  metrics are optimal-transport distances between Markov chains". That is
  right, with two qualifications. The chains carry real-valued labels and
  no actions, and the identification is an observation about two
  fixed-point equations, not a long proof. Its summary omits the
  identification, which is the title result.
- **[CLAIM-034](../claims.d/CLAIM-034.md)** wants one-way simulation, not equivalence. The paper
  treats only the symmetric metric, so it does not bear on that claim.
- **The anthology.** The paper has a machine-learning motivation:
  representation learning in reinforcement learning (§6). It gives no
  instruction for practice beyond saying that its metrics could serve.
  Nothing goes to the anthology from this reading. The LIT already
  carries `anthology-candidate`.

## Limitations

- The convergence theorems need exact inner fixed points (m = ∞). The
  practical small-m algorithm is supported only by experiment (§6).
- The dependence on the effective horizon is heavy: (1−γ)⁻⁵ for SVI. The
  authors expect a worse dependence once inexact steps are analysed.
- Finite state spaces and known kernels are assumed throughout. The
  authors name learning from data as the main open direction (§6), and
  [LIT-948](../literature.d/LIT-948.md) takes it up.
- The identification covers only the discounted, action-free,
  real-labelled case. Undiscounted and weak-bisimulation metrics are not
  treated.
- The runtime comparison depends on tuning each method's hyperparameters
  against a ground truth. The authors concede that warm-starting closes
  most of the gap.

## Open questions

- Does the small-m practical algorithm keep the guarantee of Theorem 2?
  An analysis of inexact projections would settle it.
- Does the identification extend to chains with actions or inputs, with a
  coupling that must also match actions? That is the case [QUESTION-008](../questions.d/QUESTION-008.md)
  needs. A transport form of the Ferns et al. MDP metric, with its LP,
  would answer it.
- Is there a pair of processes whose label-sequence laws are close in
  every finite window while their bicausal distance stays large? An
  explicit example would give [QUESTION-008](../questions.d/QUESTION-008.md) the judgement it asks for, at
  least for action-free chains.
