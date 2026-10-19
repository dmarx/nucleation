---
number: 763
status: Read
formerly:
- NOTE-tmp6orlr
paper: LIT-948
title: 'Calo et al. — Distances for Markov chains from sample streams'
version: 2
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv PDF (v1 of 23 May 2025, 29 pages),
    fetched from arxiv.org/pdf/2505.18005 and extracted with
    pdftotext -layout: the main text (§§1–6), Appendix A (proof of
    Proposition 1), Appendix B (derivation of the updates and B.4 on
    sampling), Appendix C (the proof of Theorem 1, followed through
    Lemma 1, the rounding bound of Lemma 2, the regret lemmas 4–8 and the
    final assembly in C.4), Appendices D–E (online-learning and technical
    lemmas, statements checked) and Appendix F (experiments,
    implementation and environments). The NeurIPS 2025 camera-ready was
    not compared with this preprint. Figures were read from their
    captions only. Expressions were restored by eye where extraction
    split them.
- version: 2
  date: '2026-10-19'
  note: >-
    The dual radii corrected from (1−γ)/6 and (1−γ)/2 to 6/(1−γ) and
    2/(1−γ), as found when the promotion audit (batch 042) re-checked
    Theorem 1 against the arXiv text; dated note at the end.
date: '2026-10-14'
summary: >-
  The bicausal transport distance between two finite Markov chains, which
  the authors' earlier paper identified with the bisimulation metric, has
  a second linear program whose constraints use only the chains'
  discounted state-transition occupancy measures, not their kernels. A
  stochastic primal-dual method on it gets an ε-accurate estimate with
  probability 1−δ from
  O((|X||Y|(|X|+|Y|) + (|X|+|Y|) log(1/δ)) / ((1−γ)²ε²)) independent
  transition samples per chain. The guarantee assumes independent draws
  from the occupancy measures, which needs restarts; samples from one
  running trajectory are outside it.
---
<!-- inactive-ok-file: QUESTION-008 CLAIM-034 — Deferred or Proposed; the set-aside question this work was filed for and its surviving one-way claim, cited as open -->

# NOTE-763: Calo et al. — Distances for Markov chains from sample streams

## Contribution

All earlier methods for computing bisimulation metrics with guarantees
need the transition kernels. Here the bisimulation metric between two
finite Markov chains is estimated from sampled transitions, with a
high-probability error bound and no problem-dependent constants. The
enabling step is a new LP whose constraints mention the kernels only
through each chain's discounted occupancy measure over (state, next state)
pairs, which can be sampled. The authors call it "the first result of its
kind".

## Key insight

In the earlier LP ([LIT-962](../literature.d/LIT-962.md)), the kernels enter as P_X(x'|x) multiplying
the coupling. But "the coupling's next X-state follows P_X given the
current X-state" can be rewritten as "the coupling's (x, x') marginal,
split by y, is the chain's own occupancy ν_X(x, x') times a conditional
λ_X(y|x)". ν_X can be sampled. So the constraint becomes an expectation
under the chain's own behaviour, and a stochastic saddle-point method can
handle it with one sample per chain per step.

## Assumptions

- **Finite chains with fixed starts.** As in [LIT-962](../literature.d/LIT-962.md): finite X and Y,
  stationary kernels, Dirac initial states x0 and y0, and γ ∈ (0, 1).
- **A known, bounded ground cost.** c : X × Y → R+ with ‖c‖∞ ≤ 1, which
  the algorithm evaluates on every state pair. In the experiments
  c(x, y) = |r(x) − r(y)|.
- **States are observed and enumerated.** The primal variable µ is a full
  table over (X × Y)², so both state spaces must be known in advance and
  each sample must reveal the state.
- **Sampling model.** Each iteration receives (X_k, X'_k) ~ ν_X and
  (Y_k, Y'_k) ~ ν_Y, independently of the past. Here
  ν_X(x, x') = (1−γ) Σ_t γ^t P[X_t = x, X_{t+1} = x'].
  - B.4 shows how to draw one exactly: draw a geometric time G with mean
    1/(1−γ), run the chain from x0 to time G+1, and keep the last pair.
    Exact sampling therefore needs the ability to restart the chain at
    x0.
  - Using pairs from a single long trajectory, undiscounted, is "abuse"
    that the authors "expect" the method to survive, untested (B.4,
    F.2). "All our experiments have made use of i.i.d. transitions
    sampled from the occupancy measures of the two chains."
- **Normalisation.** d_γ(M_X, M_Y) = inf over Π_bc of ∫ c_γ dπ (Eq. 1),
  rewritten as inf ⟨µ^π, c⟩ (Eq. 2). The factor 1/(1−γ) that [LIT-962](../literature.d/LIT-962.md)'s
  Theorem 1 carries is dropped here.

## Key results

- **Proposition 1 (the kernel-free LP).** µ is the occupancy coupling of a
  bicausal coupling if and only if there exist λ_X ∈ R_+^{Y×X} and
  λ_Y ∈ R_+^{X×Y} with:
  - (6) the flow constraint,
    Σ_{x'y'} µ(x,y,x',y') = γ Σ µ(x̂,ŷ,x,y) + (1−γ)ν0(x,y);
  - (7) Σ_{y'} µ(x,y,x',y') = ν_X(x,x') λ_X(y|x);
  - (8) Σ_{x'} µ(x,y,x',y') = ν_Y(y,y') λ_Y(x|y).

  Any solution has Σ_y λ_X(y|x) = 1 and Σ_x λ_Y(x|y) = 1. *Proof
  (App. A):* (7) is shown equivalent to [LIT-962](../literature.d/LIT-962.md)'s (24), using
  P_X(x'|x) = ν_X(x,x')/ν_X(x). Normalisation follows from Lemma 12, which
  says ν_X is the unique solution of its own flow and coherence equations.
- **The Lagrangian (Eq. 9).** d_γ = min over (µ, λ) of max over (α, V) of
  L. The gradients in α_X and α_Y are expectations under ν_X and ν_Y, so
  they have unbiased one-sample estimators (Eqs. 11–14).
- **SOMCOT (Algorithm 1, Eqs. 16–21).** Entropic stochastic mirror
  descent on µ, λ_X and λ_Y, and projected stochastic gradient ascent on
  α_X, α_Y and V within sup-norm balls of radius 6/(1−γ) and 2/(1−γ) (corrected 2026-10-19; see the dated note). The
  output is the averaged µ̄_K, and the estimate is
  d̂_γ = ⟨µ̄_K, c⟩.
- **Theorem 1.** Suppose ‖c‖∞ ≤ 1 and the stated learning rates are used
  (each ∝ 1/√K). Then with probability at least 1 − δ,
  |⟨µ̄_K − µ*, c⟩| = O( (1/(√K (1−γ))) · ( √(|X||Y|(|X|+|Y|)) + √((|X|+|Y|) log(1/δ)) ) ).
  Equivalently, ε accuracy needs
  K ≥ O( (|X||Y|(|X|+|Y|) + (|X|+|Y|) log(1/δ)) / ((1−γ)²ε²) ) iterations,
  each using one sampled transition from each chain and Θ(|X|²|Y|²)
  computation. *Holds when:* samples are independent draws from ν_X and
  ν_Y, the cost is known and bounded by 1, and the state spaces are finite
  and enumerated.
  - **Proof route.** The error is bounded by the duality gap (Lemma 1)
    through a rounding device used only in the analysis (Lemma 2:
    ‖µ − r(µ)‖₁ ≤ (3C_X + 3C_Y + ∂F)/(1−γ)). The gap is the sum of the
    players' regrets (Lemmas 5–8, two of them holding with high
    probability via Hoeffding–Azuma).
  - **Optimality.** The authors say the ε⁻² scaling is optimal up to logs,
    "as can be deduced from" lower bounds for static OT. They argue this
    and do not prove it. The big-O "only hides numerical constants".
- **Experiments (§5, App. F).**
  - **Block chains.** A uniform random walk on {1..n} against a copy with
    an irrelevant noise variable taking B values, with a cost that
    distinguishes only the end states. The averaged λ_X and λ_Y, read as
    encoder and decoder, recover the block structure at 10⁵ samples
    (n = 10, B = 5).
  - **Model selection.** In a family of biased random walks, the
    estimated distance is smallest at the true bias θ = 0.5. In a
    pendulum discretised to 49 bins under a fixed DDPG policy, it is
    smallest at the true gravity g = 9.8. The authors note that the
    discretised pendulum process is not Markov.
  - **Pairwise distances.** For 72 random-walk instances, the
    distance matrices from 10³ and 10⁴ steps reproduce the ground truth
    "qualitatively" but not "very accurately" in value (F.1).
  - **Tuning.** It is "a grueling task": too small a dual step drives the
    estimate towards zero, and too large a one overestimates (F.2).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Bicausal occupancy couplings are exactly the solutions of (6)–(8), which use the chains' occupancy measures and not their kernels | strong | Proposition 1, App. A |
| C2 | SOMCOT estimates the bisimulation metric to ε with probability 1−δ from O((\|X\|\|Y\|(\|X\|+\|Y\|) + (\|X\|+\|Y\|)log(1/δ))/((1−γ)²ε²)) independent occupancy samples per chain | strong, within its sampling model | Theorem 1, App. C |
| C3 | The ε⁻² dependence is optimal up to logarithmic factors | weak | appeal to lower bounds for static OT, §4 |
| C4 | Correlated samples from one long trajectory would also work | weak | the authors' expectation, B.4 and F.2; no experiment |
| C5 | The estimated distances and the averaged conditionals recover latent block structure and the true model in a parametric family | moderate | random-walk and pendulum experiments, §5 |

## Method

SOMCOT. Each round draws one transition from each chain's occupancy
measure. It updates µ by a multiplicative-weights step on the exact
gradient c − α_X − α_Y + γV(x', y') − V(x, y), and updates λ_X(·|X_k) and
λ_Y(·|Y_k) by multiplicative steps on one-sample gradient estimates, only
at the sampled states. It moves the dual variables α_X, α_Y and V by
projected stochastic gradient steps on the constraint residuals, and
outputs the running average of µ.

## Concepts

- **Marginal occupancy measure ν_X(x, x').** The discounted distribution
  of consecutive state pairs of one chain. It is the only form in which
  the kernel enters the new LP.
- **λ_X(y|x), λ_Y(x|y).** Conditional laws of one chain's state given
  the other's under the coupling. In the experiments they are read as an
  encoder–decoder pair between the two state spaces.
- **Bisimulation metric.** Used here as a name for the bicausal OT
  distance (Eq. 1), "following the observation made by" [LIT-962](../literature.d/LIT-962.md). The
  paper does not re-derive the identification.

## Connections

The paper extends [LIT-962](../literature.d/LIT-962.md), whose occupancy-coupling LP it reformulates
and whose rounding procedure it adapts. Its stochastic primal-dual
approach comes from static OT solvers (Genevay et al.; Ballu et al.) and
from the LP view of MDPs (Puterman). It sets its result against deep-RL
"approximate bisimulation" methods (Castro; Zhang et al.; Chen and Pan;
Kemertas and Jepson), which it says "are not well-founded in theory".

## Bearing on the record

- **[QUESTION-008](../questions.d/QUESTION-008.md).** [LIT-948](../literature.d/LIT-948.md) was filed for this question as "a way to
  estimate bisimulation distances between Markov chains from sample
  streams alone", which "would make approximate bisimulation measurable
  for systems whose update structure is not known". The paper supports
  less than that:
  - **Transitions, not observations.** The samples are state transitions,
    with the states observed and drawn from a known, enumerated, finite
    space. The kernel can be unknown. The states cannot be latent. The
    record's fidelity notion ([TERM-033](../terms.d/TERM-033.md)) is defined over observed
    responses "with no shared latent state required". An audience's
    state after an utterance is just what is not observed. So the
    estimator does not apply to communicative systems as [QUESTION-008](../questions.d/QUESTION-008.md)
    frames them, unless their states are made observable.
  - **Restarts, not a stream.** The guarantee is for independent draws
    from the discounted occupancy measure, which needs restarts from the
    initial state. A single running stream is outside it. The title's
    "sample streams" is broader than the theorem.
  - **No actions.** As in [LIT-962](../literature.d/LIT-962.md), the chains have no actions, so this is
    not bisimulation of systems driven by utterances.
  - **The ground cost is supplied.** The cost on state pairs is given in
    advance. Choosing it is the normative choice of observables that
    [CLAIM-034](../claims.d/CLAIM-034.md) and the A40 discussion treat as interpretive, and the
    paper offers nothing on it.
  - **What it does show.** Where states are observed, approximate
    bisimulation is a statistically estimable quantity at a polynomial
    sample cost. That answers one practical doubt about using it as a
    criterion, and does not touch the question's demand for a judgement
    that observational equivalence gets wrong.
- **The anthology.** The applications in §5–6 (state abstraction,
  model selection, a differentiable loss for representation learning) are
  machine-learning practice and belong in the anthology if anywhere. The
  estimation theorem is not practice. The LIT keeps its
  `anthology-candidate` flag.

## Limitations

- Exact guarantees need independent occupancy samples, so restarts are
  needed. Single-trajectory data are untested.
- The primal variable is a full |X|²|Y|² table, so the method does not
  scale past small finite spaces. The authors call scaling to large or
  infinite spaces the main open problem.
- The cost must be known on every pair of states.
- Hyperparameters are hard to tune in practice. The theory's step sizes
  are "too conservative", and the reported runs use a decaying schedule
  and minibatches that the theorem does not cover.
- The pendulum experiment uses a non-Markov process. It illustrates the
  method's use and does not test the theorem.
- The optimality of the rate is argued by analogy to static OT, not
  proved.

## Open questions

- Does the guarantee survive dependent samples from a single trajectory
  without restarts? A mixing-time version of Theorem 1 would settle it.
- Can the primal variables be parametrised, to reach large or continuous
  state spaces, while keeping a guarantee? The authors leave this open.
- What about partially observed states, where only labels or responses
  are sampled? That is the case [QUESTION-008](../questions.d/QUESTION-008.md) needs, and the paper does not
  raise it.

## Note of 2026-10-19: the dual radii

The first reading transcribed the projection domains of SOMCOT as sup-norm
balls of radius (1−γ)/6 for α and (1−γ)/2 for V. The radii are 6/(1−γ) and
2/(1−γ). Lemma 1 needs them: the dual maximum must reach
(6∂C_X + 6∂C_Y + 2∂F)/(1−γ) to dominate twice the rounding error of Lemma 2,
and the step sizes, which scale as 1/(1−γ), and the gradient bound
|g_µ| ≤ 1 + 12/(1−γ) + 4/(1−γ) in Lemma 7 agree. pdftotext -layout had set
the fractions' numerators on a separate line. Nothing else in this note
depends on the radii.
