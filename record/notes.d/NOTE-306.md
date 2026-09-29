---
number: 306
status: Read
formerly:
- NOTE-tmpwmbz4
paper: LIT-347
title: 'Information-theoretic analysis of generalization capability of learning algorithms'
version: 2
history:
- version: 1
  date: '2026-09-29'
  note: >-
    Read in full (Full text of arXiv 1705.07809 v2 (6 Nov 2017; the NIPS
    2017 camera-ready, per its footer), 15 pp., from the arXiv PDF:
    abstract, §§1–4, Appendices A–F and all 23 references. Text was
    extracted with PyMuPDF, and p. 8 was rendered to check eq. (34). I
    checked the proof of Lemma 1 (Donsker–Varadhan plus the subgaussian
    quadratic-discriminant step), the Gibbs variational solution, and the
    arithmetic of Corollary 2's instantiation. I did not read v1, which the
    acknowledgement says contained errors.). The first NOTE on this paper,
    which was seeded from its abstract alone.
- version: 2
  date: '2026-09-29'
  note: >-
    Correction added: the Russo–Zou quantity is stated in this paper's
    notation, not theirs, per the reading of Russo & Zou.
date: '2026-09-29'
summary: >-
  If the loss ℓ(w,Z) is σ-subgaussian for every w, then the expected
  generalisation error of any learning algorithm P_{W|S} obeys |E[L_μ(W) −
  L_S(W)]| ≤ √(2σ²·I(S;W)/n) (Theorem 1). This extends Russo–Zou to
  uncountable hypothesis spaces, and the paper adds a high-probability
  version, n = (8σ²/α²)(ε/β + log(2/β)) (Theorem 3). Minimising empirical
  risk plus I(S;W), relaxed to a KL term against a prior Q, yields exactly
  the Gibbs algorithm (Theorem 5). Noisy ERM and adaptive composition are
  analysed through the same mutual-information quantity.
---

# NOTE-306: Information-theoretic analysis of generalization capability of learning algorithms

## Contribution

Russo & Zou had bounded the bias of adaptive data analysis by I(Λ_W(S);W), the information the output carries about the vector of empirical risks, for finite hypothesis classes. This paper:

*Correction (2026-09-29, from [NOTE-308](NOTE-308.md), the reading of Russo & Zou, [LIT-356](../literature.d/LIT-356.md)):* I(Λ_W(S);W) is this paper's notation for Russo & Zou's quantity. Their own is I(T;φ): the information the selection φ carries about the vector T of m candidate statistics. Russo & Zou's Lemma 1 (chaining over adaptive steps) is the origin of eq. (36) here.


- **Extends that to arbitrary, including uncountable, hypothesis spaces.**
- **Moves to the simpler quantity I(S;W).** This is the information the output carries about the training set.
- **Adds high-probability and absolute-error bounds.**
- **Turns the bound into algorithm design.** The Gibbs algorithm is the optimal information-regularised ERM, noisy ERM controls I(S;W), and adaptive composition is handled by the chain rule.

## Key insight

View the learner as a channel from datasets to hypotheses. Overfitting is then bounded by how much that channel transmits about its input: the less W can tell you about S, the less the empirical risk can differ from the population risk.

The mechanism is one decoupling inequality. Compare E f(X,Y) under the joint distribution with E f under the product of the marginals: by Donsker–Varadhan they differ by at most √(2σ²·I(X;Y)) when f is σ-subgaussian under the product.

## Assumptions

- **The setting.** An instance space Z, a hypothesis space W and a loss ℓ: W × Z → ℝ₊. The dataset S = (Z₁,…,Z_n) is i.i.d. from μ, and the algorithm is a Markov kernel P_{W|S} (§1).
- **Subgaussian loss.** ℓ(w,Z) is σ-subgaussian under μ for every w (Theorems 1–4). A bounded loss in [a,b] qualifies with σ = (b − a)/2.
- **Stability notions (§2).** (ε,μ)-stability means I(S;W) ≤ ε under the data distribution. ε-stability means sup_μ I(S;W) ≤ ε, which the paper reads as the channel's capacity under product-form inputs. The paper mainly uses the μ-dependent version.
- **Bounded loss where needed.** The Gibbs and noisy-ERM corollaries assume ℓ ∈ [0,1].
- **Lipschitz loss (Corollary 3).** ℓ(·,z) is ρ-Lipschitz on W = ℝ^d.

## Key results

- **Lemma 1.** If f(X̄,Ȳ) is σ-subgaussian under P_X ⊗ P_Y, then |E f(X,Y) − E f(X̄,Ȳ)| ≤ √(2σ²·I(X;Y)). The proof (App. A) is Donsker–Varadhan plus a nonnegative-parabola discriminant.
- **Theorem 1.** |gen(μ, P_{W|S})| ≤ √((2σ²/n)·I(S;W)).
- **Theorem 2 (Russo–Zou, extended to uncountable W).** The same bound with I(Λ_W(S);W). Since I(Λ_W(S);W) ≤ I(S;W) by data processing (eq. 13), Theorem 1 follows. The two are equal when W depends on S only through its empirical risks.
- **Theorem 3.** If I(Λ_W(S);W) ≤ ε, then P[|L_μ(W) − L_S(W)| > α] ≤ β once n = (8σ²/α²)(ε/β + log(2/β)).
  - The proof (App. B) adapts the Bassily et al. "monitor" technique over m = ⌊1/β⌋ parallel copies.
  - *Corollary 1:* with ε ≤ β·log(2/β), n = (16σ²/α²)·log(2/β) suffices, the same order as when S and W are independent.
- **Theorem 4.** E|L_μ(W) − L_S(W)| ≤ √((2σ²/n)(ε + log 2)). This improves Russo–Zou's σ/√n + 36√(2σ²ε/n).
- **Countable and quantised hypothesis spaces (§4.1).**
  - |gen| ≤ √(2σ²·H(W)/n).
  - Quantising W ⊂ a d-dimensional subspace of radius B at r = 1/√n gives |gen| ≤ √((2σ²d/n)·log(2B√(dn))) (eq. 20).
- **Binary classification (§4.2).** A two-stage algorithm (an empirical cover on S₁, then ERM on S₂) achieves E L_μ(W) ≤ inf L_μ + c·√(V·log n / n) via Sauer's lemma.
- **Theorem 5, Gibbs.**
  - argmin over P_{W|S} of E L_S(W) + (1/β)·D(P_{W|S}‖Q|P_S) is P*(dw|s) ∝ e^{−β·L_s(w)}·Q(dw).
  - Its information is I(S;W) ≤ 2β for ℓ ∈ [0,1], via differential privacy, and its gen ≤ β/(2n), citing Raginsky et al. 2016.
  - *Corollary 2:* E L_μ(W) ≤ inf L_μ + (1/β)·log(1/Q(w_o)) + β/(2n).
    - With Q(wᵢ) = 6/(π²i²) and β = √n, it becomes (2·log i_o + 1)/√n (eq. 30). I checked this: log(π²/6) + ½ ≈ 0.998 ≤ 1.
    - With a uniform Q over k hypotheses, the paper sets β = 2√(n·log k) and states the result as inf L_μ + √((1/n)·log k). The arithmetic with that β gives (3/2)·√((1/n)·log k). Even the optimal β = √(2n·log k) gives √2·√((1/n)·log k). The printed constant is understated, a small slip that does not affect the rate.
  - *Corollary 3:* for W = ℝ^d and Gaussian Q it gives an excess risk of order d^{1/4}ρ^{1/2}n^{−1/4}(‖w_Q − w_o‖² + 3) (eq. 32).
- **Corollary 4, noisy ERM.** Exponential noise with mean b_i = i^{1.1}/n^{1/3} gives E L_μ(W) ≤ min L_μ + (i_o^{1.1} + 3)/n^{1/3} (eq. 35). The proof bounds I(S;W) through the capacity of additive exponential-noise channels (F.23–F.26).
- **Pre- and post-processing (§4.5).** Noising or erasing data, or quantising or perturbing weights, gives I(S;W) ≤ min(I(S;S̃), I(S̃;W)) and the like. Strong data-processing inequalities could sharpen these.
- **Adaptive composition (§4.6).** I(S;W_k) ≤ Σ_j I(S;W_j | W^{j−1}) (eq. 36), which lets per-stage information add up.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Expected generalisation error ≤ √(2σ²·I(S;W)/n) for σ-subgaussian losses | strong (proof) | Lemma 1 + Theorem 1 |
| C2 | High-probability generalisation with sample complexity polynomial in 1/α, logarithmic in 1/β, when I(Λ_W(S);W) ≤ ε | strong (proof) | Theorem 3, App. B |
| C3 | The Gibbs algorithm is the optimal KL-relaxed information-regularised ERM | strong (proof) | Theorem 5, App. C (the convex per-sample problem, citing T. Zhang 2006) |
| C4 | Noisy ERM and Gibbs trade fit against generalisation with prior-dependent rates | strong (proof) | Corollaries 2–4 |
| C5 | Input–output MI can be "more tightly coupled" to generalisation than VC dimension or uniform stability | assertion (motivation) | §1; argued from I(S;W) depending on μ, the algorithm and the loss; no comparison shown |
| C6 | Many deep-learning regularisers may be read as inducing I(S;W)-stability | assertion (direction for future work) | §4.5 |

## Method

The paper uses information-theoretic decoupling: Donsker–Varadhan's variational formula, subgaussian concentration, the data-processing inequality and the chain rule. It adds a differential-privacy-style monitor argument for the tail bound, and convex duality for Gibbs. It has no experiments.

## Concepts

- **(ε,μ)-stability in input–output mutual information.** I(S;W) ≤ ε.
- **The learning algorithm as a channel.** P_{W|S}, with capacity sup_μ I(S;W).
- **Gibbs algorithm.** e^{−βL_S}·Q, with β an inverse temperature.
- **Noisy ERM.**
- **Adaptive composition.** Chain rule over stages.

## Connections

- **Earlier work.** Russo & Zou 2016 (extended here), Bassily et al. 2016 (the monitor technique), Raginsky et al. 2016 (the Gibbs gen ≤ β/(2n) bound), and differential privacy (Dwork et al.).
- **[LIT-236](../literature.d/LIT-236.md) (Sefidgaran et al. 2022).** It reinterprets the bound as a lossless compression rate and replaces it with lossy, rate–distortion bounds that stay finite where I(S;W) is infinite. §4.1 of this paper already has that move in embryo: I(S;W) ≤ H(W), and quantising W to a covering (eq. 20).
- **[LIT-233](../literature.d/LIT-233.md) (Sefidgaran & Zaidi 2023).** It makes such bounds data-dependent (empirical measure) rather than μ-dependent. This paper's (ε,μ)-stability is distribution-dependent but not computable from the sample.
- **[LIT-240](../literature.d/LIT-240.md) (Vera et al.).** It is the representation-level analogue: I(X;U) in place of I(S;W). [LIT-245](../literature.d/LIT-245.md) criticises that step, and its |U|-dependent vacuity parallels the vacuity of I(S;W) for deterministic W.

## Bearing on the record

**Row 12 ("information-theoretic generalization").** The role holds, and the paper owns more of §5 than the map says.

- **The founding move.** The owner's §5 opens with "Learning is a channel … the gradient literally as a finite binary message from the data to the parameters". This paper already models the learner as a channel P_{W|S} and names the channel capacity sup_μ I(S;W) as its stability notion (§2).
- **Per-step accounting.** The owner's bound I(θ_T;D) ≤ Σ_t S_grad,t (bits per gradient step, summed) is the same kind of accounting as eq. (36): I(S;W_k) ≤ Σ_j I(S;W_j | W^{j−1}), with each gradient step a stage of an adaptive composition.
  - The owner's per-step bound is a coarser, counting version: I(S;W_j | W^{j−1}) ≤ H(W_j | W^{j−1}) ≤ bits written.
  - So the novelty map should list this paper as owning the "learning-as-channel" frame, not only as a generalisation citation.

**What it adds to §5.** It makes §5 say something about generalisation. Composing the owner's bit-count with Theorem 1 gives:

    |gen| ≤ √((2σ²/n)·Σ_t S_grad,t)

This follows from Theorem 1 plus eq. (36) plus H ≤ bits, and is my composition, not in the paper. With S_grad,t = m·b bits per step (m parameters, b bits each) it is vacuous for any real network, since m·b·T ≫ n. That is the honest version of the "floors, not predictions" caveat already in the owner's document. The informative per-step quantity would be the conditional information actually transmitted, which is what [LIT-236](../literature.d/LIT-236.md)'s lossy rates try to estimate.

**Temperature and free energy.** The Gibbs algorithm minimises E L_S + (1/β)·KL, a free energy with β an inverse temperature (Theorem 5). This is the third distinct "temperature" in this batch.
- Here, β is the inverse temperature of the Gibbs posterior.
- In McCandlish ([LIT-348](../literature.d/LIT-348.md)), it is the SGD ratio ε/B.
- In Tishby ([LIT-338](../literature.d/LIT-338.md)), it is the IB trade-off parameter.

None is k_B·T. If row 13's thermodynamic bridge is to connect to learning theory, this is the cleanest formal point of contact, with [LIT-308](../literature.d/LIT-308.md) (Goldt & Seifert) as the physical one. Keep the analogy explicit.

**ML practice.** Mostly theory. Noisy or Gibbs training as a generalisation lever is the only practice-shaped content, and it is asserted rather than tested. `anthology-candidate` is fair. The anthology does not hold this paper (the seed's check of [ANTH-LIT-726](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-726.md) found a different Raginsky paper).

## Limitations

- **Expected error only.** Theorem 1 bounds the *expected* generalisation error. For deterministic algorithms with continuous W, I(S;W) is typically infinite, and the paper's remedy is quantisation (§4.1) or added noise (§§4.3–4.5).
- **Subgaussianity.** Assumed uniformly over w. Heavy-tailed losses are outside the scope.
- **The practical deep-learning reading is left as future work** (§4.5). There are no experiments.
- **Minor slips.** The main-text eq. (34) misplaces a term relative to its proof. Corollary 2's uniform-prior instantiation understates the constant: with the stated β it is 3/2, and at best √2, not 1.

## Open questions

- Is there a per-step quantity, the information transmitted by one minibatch gradient, that is both finite and small enough to make √(2σ²·Σ_t I_t/n) non-vacuous for SGD? If so, it would be where McCandlish's batch SNR ([LIT-348](../literature.d/LIT-348.md)) and this bound meet: I_t should rise with B/B_simple.
- Does the capacity reading of ε-stability, sup_μ I(S;W), have a useful computation for SGD with Gaussian gradient noise? A Shannon–Hartley-type answer there would ground the owner's C_step = d·log₂(1 + SNR) in a generalisation theorem rather than a counting bound.

## Corrections to the seeded skim

- Seeded from metadata. The text confirms the title, authors (Aolin Xu, Maxim Raginsky; University of Illinois at Urbana-Champaign), the arXiv id and the NIPS 2017 venue (the v2 footer reads "31st Conference on Neural Information Processing Systems (NIPS 2017), Long Beach"). The seed's "NeurIPS 2017" is the conference's later name.
- The seed summary is accurate, with three refinements.
  - *In expectation.* The headline bound is on the expected generalisation error, not the error itself. The absolute error gets separate bounds (Theorems 3–4) stated in terms of I(Λ_W(S);W) ≤ I(S;W).
  - *Gibbs (Theorem 5).* The algorithm solves the relaxed problem, with I(S;W) replaced by the upper bound D(P_{W|S}‖Q|P_S) = I(S;W) + D(P_W‖Q). It does not solve the I(S;W)-regularised problem itself.
  - *Noisy ERM* adds noise to each hypothesis's empirical risk (eq. 33), not to the weights.
- An arithmetic slip, found on the rendered p. 7. In the uniform-prior example after Corollary 2, β = 2√(n·log k) gives an excess of (3/2)·√((1/n)·log k), not the printed √((1/n)·log k).
- A typesetting inconsistency. The main-text eq. (34) puts −(Σ1/bᵢ)⁻¹ *inside* the square root (checked on the rendered page). The proof's (F.32) has it outside, followed by log(1+x) ≤ x. The appendix form is the proved one.
- Map role (row 12, "information-theoretic generalization") holds. The paper also owns more of row 12's "channel" language than the map credits; see Bearing on the record.
