---
number: 81
status: Read
formerly:
- NOTE-tmpxhy9p
paper: LIT-085
title: 'The No-U-Turn Sampler (NUTS)'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (Full text of arXiv 1111.4246v1 (18 Nov 2011, 30 pp.),
    downloaded to raw4/1111.4246.pdf and extracted with PyMuPDF to
    raw4/1111.4246.full.txt. I read everything: §1–5, Algorithms 1–6,
    Appendix A (ESS estimator) and the references. Figures 3–7 came through
    as axis ticks only, so I read them from their captions and from the §4
    prose, not from the plotted points. I did not read the JMLR 2014 version
    (vol. 15, pp. 1593–1623), and I have not checked how it differs from v1.
    Where the two might disagree (for example the recommended δ, or the
    "soon-to-be-released" Stan wording), this note describes v1.). Upgraded
    from `Skimmed` to `Read`: the claims table, assumptions and results are
    new, and the skim is corrected where the full text disagreed.
date: '2026-09-25'
summary: >-
  NUTS removes HMC's step-count L. It doubles a leapfrog trajectory
  forwards and backwards in random directions until some balanced subtree
  satisfies (θ⁺−θ⁻)·r⁻ < 0 or (θ⁺−θ⁻)·r⁺ < 0. It keeps detailed balance by
  slice sampling and by excluding states that could not have regenerated
  the tree. With ε set by a dual-averaging scheme (γ = 0.05, t₀ = 10, κ =
  0.75, target δ ≈ 0.6), it matched the best hand-tuned HMC in ESS per
  gradient on two logistic-regression posteriors. It beat that HMC by
  about 3× on a 250-D Gaussian and on a 3001-D stochastic-volatility model
  (§4.4).
---

# NOTE-081: The No-U-Turn Sampler (NUTS)

## Contribution

Before this paper, HMC needed two user-set parameters, ε and L. L in particular had no simple diagnostic, and it was usually tuned from autocorrelations in preliminary runs (§3). NUTS makes L unnecessary with a stopping rule that is reversible. It is built by recursive trajectory doubling, borrowed from Neal's (2003) slice-sampling doubling procedure. The paper also adapts Nesterov's (2009) primal-dual averaging to tune ε during warm-up, for both HMC and NUTS. Together these give an HMC-class sampler with no user-facing tuning parameters except a target acceptance statistic δ and a warm-up length M_adapt. That is what made HMC usable inside "turnkey" engines. The paper announces Stan as the first such engine (§5, p. 28).

## Key insight

The naive rule, "stop when (θ̃ − θ)·r̃ < 0", breaks time-reversibility, so it does not leave the target invariant. The fix is to make the trajectory a random balanced binary tree whose construction is equally probable, at 2⁻ʲ, from every leaf that could have generated it. The next state is then chosen only among leaves that (a) lie in the slice and (b) would not have triggered a stop before the full tree was built. Under those rules the kernel is uniform on the candidate set C, so the stopping rule costs no correctness. Trajectory length becomes a by-product of the geometry: it is long where the posterior is wide relative to ε and short where it is narrow.

## Assumptions

- The target is continuous, unconstrained and differentiable almost everywhere in θ. Discrete variables must be summed out or handled by other moves such as Gibbs. Simple constraints, such as positivity or the simplex, need a change of variables (§5, p. 27).
- The gradient ∇θL is available, for example by automatic differentiation (§1).
- The kinetic energy is ½r·r with r ~ N(0, I). There is no mass matrix (eq. 1, §5).
- Gradient evaluations dominate cost. The 2^{j+1} − 2 inner products for the U-turn check and the O(2ʲ) extra random numbers are treated as negligible "except for very simple models with very little data" (p. 9, p. 13). The efficiency metric, ESS per gradient evaluation, depends on this.
- **Validity conditions on the (B, C) construction, C.1–C.4 (p. 7):**
  - (C.1) states are added volume-preservingly;
  - (C.2) the current state is in C;
  - (C.3) every state in C lies in the slice u ≤ exp{L(θ′) − ½r′·r′};
  - (C.4) p(B, C | θ, r, u, ε) is the same for every (θ, r) ∈ C.
- Adapting ε invalidates the Markov property. The paper follows common practice: adapt during burn-in, then freeze ε = ε̄_{M_adapt} (p. 15, Algorithms 5–6). Vanishing adaptation (η_t = t^−κ, κ ∈ (0.5, 1]) is cited as preserving asymptotics, via Andrieu & Thoms 2008. It is not proved here.
- The dual-averaging argument assumes h(ε) = E[H_t | ε] is monotone (nonincreasing) in ε, for both H^HMC and H^NUTS. This is stated as an assumption (p. 16–17) and not verified.

## Key results

- **Invariance (§3.1.1, eqs. 6–7).** Suppose (B, C) satisfies C.1–C.4 and T leaves the uniform distribution on C invariant. Then the procedure (resample r ~ N(0, I); u ~ U[0, exp{L(θ) − ½r·r}]; (B, C) ~ p(B, C | θ, r, u, ε); (θ', r') ~ T) leaves p(θ, r, u, B, C | ε) invariant, and hence leaves p(θ) ∝ exp L(θ) invariant. The argument is a Gibbs step plus eq. 7, p(θ, r | u, B, C, ε) ∝ I[(θ, r) ∈ C].
- **The doubling construction satisfies C.4.** There are 2ʲ equally likely trees of height j from a given start, and any leaf reproduces a given tree with probability 2⁻ʲ. C.4 therefore holds if C excludes (i) every state added in the final doubling when that doubling triggered eq. 8 or 9 internally, and (ii) nothing else when the stop came from the full tree's endpoints (p. 10).
- **Stopping rules.**
  - U-turn (eq. 9): (θ⁺ − θ⁻)·r⁻ < 0 or (θ⁺ − θ⁻)·r⁺ < 0, checked on every balanced subtree.
  - Divergence (eq. 8): L(θ) − ½r·r − log u < −Δ_max, with Δ_max = 1000 recommended.
- **Efficient kernel (eq. 10).** Propose a uniform state from C_new and accept with probability min{1, |C_new|/|C_old|}. This is a Metropolis–Hastings kernel satisfying detailed balance w.r.t. uniform on C (eq. 11). Applied after every doubling, it biases moves toward far states, "akin to delayed-rejection" (p. 13). Memory falls from O(2ʲ) to O(j) vectors (Algorithm 3).
- **Dual averaging (eq. 16).** x_{t+1} ← μ − (√t/γ)·(1/(t + t₀))·Σᵢ Hᵢ; x̄_{t+1} ← η_t x_{t+1} + (1 − η_t)x̄_t, with x = log ε, η_t = t^−κ, and μ = log(10ε₁). For large t, x_{t+1} − x_t = O(−H_t t^−0.5) (eq. 17). The NUTS statistic is H^NUTS = mean over the final doubling's states of min{1, p(θ, r)/p(θ₀, r₀)} (eq. 19).
- **Initial ε heuristic (Algorithm 4).** Double or halve ε until the one-step Langevin acceptance ratio crosses 0.5.
- **Empirical results (§4).**
  - Design: 2000 iterations with 1000 of adaptation, on four targets:
    - MVN: 250-D, precision matrix drawn from Wishart(I, 250);
    - LR: German credit, 25 parameters, σ² = 100;
    - HLR: 302-D, exponential prior on σ² with λ = 0.01;
    - SV: S&P 500, 3000 days, 3001-D.
  - Grid: HMC used 10 log-spaced λ = εL values spanning 40× × 8 values of δ ∈ [0.25, 0.95]. NUTS used 15 values of δ ∈ [0.25, 0.95]. Each cell had 10 seeds, giving 3,200 HMC and 600 NUTS runs.
  - Metric: minimum over dimensions of the ESS of the mean or the second central moment, whichever is lower, per gradient evaluation.
  - Findings:
    - (a) dual averaging hits δ well except on SV, where burn-in is longer, and ε̄ converges within a few hundred iterations (Figs. 3–4);
    - (b) most NUTS trajectories have length 2ʲ, so whole half-trees are rarely discarded (Fig. 5, §4.3);
    - (c) HMC's best λ varied about 100× across targets, from 0.17 (LR) to 17.62 (MVN);
    - (d) NUTS at δ = 0.6 roughly equals HMC's best on LR and HLR and beats it by about 3× on MVN and SV (§4.4, Fig. 6).
- **Qualitative comparison (§4.5, Fig. 7).** On the 250-D MVN, at matched cost (about 10⁶ gradient/likelihood evaluations or iterations), RWM "has barely begun to explore", Gibbs leaves regions unexplored, and NUTS yields many effectively independent samples. This is a visual demonstration only. The paper also asserts that RWM and Gibbs need O(D²) per independent sample even after an ideal whitening.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Algorithm 2 (naive NUTS) leaves the target p(θ) invariant | strong | derivation §3.1.1: conditions C.1–C.4, eqs. 6–7 and the 2⁻ʲ tree-probability argument (pp. 7–10); a complete argument, not stated as a numbered theorem |
| C2 | The efficient kernel (eq. 10) and the incremental subtree sampling (eq. 12) preserve invariance while needing only O(j) memory | strong | detailed-balance check eq. 11 and the factorization eq. 12 (pp. 12–13) |
| C3 | Ergodicity / convergence of NUTS | not addressed | only invariance is shown; there is no irreducibility or aperiodicity argument (the paper notes that a badly chosen L can break HMC ergodicity, p. 4) |
| C4 | Dual averaging drives h(ε̄) → δ while the per-iteration change vanishes | moderate | an adaptation of Nesterov 2009 with t₀ and κ added; the convergence claim is asserted by reference and rests on the unverified monotonicity of h(ε) (pp. 15–17) |
| C5 | NUTS is at least as efficient as the best-tuned HMC, even before counting HMC's tuning cost | moderate | experiment §4.4: 4 targets, 10 seeds per cell; ≈ on LR and HLR, ≈3× on MVN and SV. Only basic identity-mass HMC is compared, and only four targets |
| C6 | δ ≈ 0.6 is a good NUTS default and δ ≈ 0.65 a good HMC default | moderate | experiment §4.4, Fig. 6; the HMC value also agrees with Beskos et al. 2010 |
| C7 | The default dual-averaging constants (γ = 0.05, t₀ = 10, κ = 0.75) "work consistently well" | weak | hand-tuned on SV, one of the four test targets; the authors disclaim generality (p. 16) |
| C8 | NUTS makes HMC usable with "no hand-tuning at all" (abstract) | moderate | follows from C4–C7 for ε and L; the constants were hand-set once, and mass-matrix tuning is left out entirely (§5) |
| C9 | HMC costs roughly O(D^{5/4}) per independent sample against O(D²) for RWM | assertion | cited to Creutz 1988, not shown (§1) |
| C10 | Part of NUTS's gain may come from having no single accept/reject step | weak | speculation from the success of windowed HMC (Neal 1994) (§5) |
| C11 | NUTS makes more progress than HMC when it hits zero-density regions under hard constraints | informal argument | §5, p. 27: it samples from the states visited so far instead of discarding the trajectory |

## Method

- **Per iteration:**
  1. Draw r₀ ~ N(0, I) and u ~ U[0, exp{L(θ) − ½r₀·r₀}].
  2. Set j = 0 and initialise the tree at (θ, r₀).
  3. Repeat until stopped:
     - pick v ~ U{−1, +1};
     - call BuildTree from the current leftmost or rightmost leaf for 2ʲ leapfrog steps of size vε;
     - if the new subtree is valid (s′ = 1), move to its representative sample with probability min{1, n′/n};
     - update n;
     - stop if s′ = 0 or the full-tree U-turn condition holds;
     - increment j.
- **BuildTree** is a recursive depth-first construction. Each leaf contributes:
  - n′ = I[u ≤ exp{L − ½r·r}];
  - s′ = I[u < exp{Δ_max + L − ½r·r}].

  Each internal node combines its two children's representative samples with probability n″/(n′ + n″), and ANDs their U-turn checks. With adaptation (Algorithm 6), it also accumulates Σ min{1, p/p₀} and a count n_α.
- **Adaptation:** for m ≤ M_adapt, update H̄_m, log ε_m and log ε̄_m by eq. 16 with t₀ = 10, γ = 0.05 and κ = 0.75, then freeze ε = ε̄_{M_adapt}.

## Concepts

- **Leapfrog integrator:** the volume-preserving, time-reversible half-step/full-step/half-step update (eq. 2). Its energy error scales as ε² for large L and ε³ for L = 1.
- **Slice variable u:** an auxiliary uniform on [0, p(θ, r)]. Given u, the target is uniform on the slice, which lets candidate states be treated as equally weighted (§3.1).
- **B, C:** B is every state visited in the iteration; C ⊆ B is the set of states that can be transitioned to without violating detailed balance.
- **U-turn:** (θ⁺ − θ⁻)·r < 0 at either end of a balanced subtree. It means an infinitesimal extension would shrink the endpoint distance (eq. 9).
- **Δ_max:** the divergence threshold on the energy error. It is set large (1000), so that it fires only on "astronomically" poor states.
- **Dual averaging:** Nesterov's primal-dual method, repurposed to find the zero of h(x) = E[H_t | x]. Here t₀ damps early iterates and κ < 1 forgets burn-in (pp. 15–16).
- **ESS (Appendix A):** M / (1 + 2Σ_{s ≤ M_cutoff}(1 − s/M)ρ̂_s). Autocorrelations are truncated at the first lag where ρ̂ < 0.05. The mean and variance come from a separate 50,000-sample NUTS run (δ = 0.5), not from the chain being evaluated. The paper computes ESS for both the mean and the second central moment, because resonant HMC produces anti-correlated draws that flatter mean-ESS (p. 20).

## Connections

- **Builds on:**
  - Neal's HMC review (2011) and the HMC originators Duane et al. (1987);
  - slice-sampling doubling (Neal 2003) for the tree construction;
  - Nesterov (2009) for dual averaging, as an alternative to Robbins–Monro (1951), which gives too much weight to early iterates;
  - adaptive MCMC (Andrieu & Thoms 2008);
  - optimal HMC acceptance ≈ 0.65 (Beskos et al. 2010).
- **Kernel analogy:** delayed-rejection MCMC (Tierney & Mira 1999), for the eq. 10 kernel.
- **Complementary, not compared:**
  - windowed HMC (Neal 1994);
  - Riemannian-manifold HMC (Girolami & Calderhead 2011). The paper proposes combining NUTS with RMHMC and says there are "no technical obstacles".
- **Downstream (not read here):** later accounts replace slice sampling with multinomial sampling from the trajectory, add a generalized U-turn criterion, and adapt diagonal or dense mass matrices in windows. The usual citation is Betancourt 2017, "A Conceptual Introduction to Hamiltonian Monte Carlo", arXiv 1701.02434. I have not verified the details against that text. The ESS estimator here was superseded in Stan by rank-normalized split-R̂/ESS (Vehtari et al.). I have not read that either.
- **Within nucleation:** this is [LIT-085](../literature.d/LIT-085.md). I found no other nucleation document that cites it. Its NOTE-081 is the seeded skim.

## Bearing on the record

- **In nucleation:** the paper is correctly filed under probabilistic-modeling. It supports no existing THEORY document. If a THEORY were ever written about why NUTS works, this paper supplies the invariance argument (C1–C2). It does not supply a convergence-rate or ergodicity argument (C3).
- **Anthology fit (asked explicitly).** NUTS is a probabilistic-programming workhorse: the default gradient-based sampler for continuous parameters in Stan, PyMC and NumPyro. It is Bayesian computation, not model training. Taken as a statistics method, the anthology would ordinarily not hold it. But the paper does carry an instruction for practice: "for a continuous, differentiable posterior, use NUTS with dual-averaged ε (target δ ≈ 0.6–0.65) instead of hand-tuned HMC, random-walk Metropolis or Gibbs; tune on warm-up, then freeze". Probabilistic-modeling practitioners in ML follow exactly this, whether they fit hierarchical models or Bayesian neural nets at small scale.
- **Finding: plausibly anthology material, and it would need a topic.** The anthology already holds a posterior sampler: [ANTH-LIT-245](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-245.md) (Welling & Teh, SGLD) is filed there, tagged `training-optimization`, and [ANTH-LIT-366](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-366.md) (asynchronous distributed Bayesian learning) is tagged `distributed-optimization`. So Bayesian sampling is not foreign to the anthology. Under [ANTH-ADR-059](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/decisions.d/ADR-059.md) ("the topics are an axis, not a scope") the question is only where it goes, and none of the anthology's 22 topics fits honestly:
  - `inference-optimization` lists "sampling algorithms", but in the serving-time sense (decoding), which is a different thing;
  - `training-optimization` is not what an MCMC sampler is.

  If it were moved, the honest step would be a new topic, something like probabilistic inference / Bayesian computation, with a decision. That would also be the right home for SGLD, whose current `training-optimization` tag is a stretch. I record this as a finding and have not moved anything.
- **What would carry over if it were moved.** The practice would need sourcing for the current algorithm (multinomial NUTS with adapted metric) from later work, not from this paper. The paper supports the shape of the practice, meaning no hand-set L and dual-averaged ε. It does not support the current defaults. For example, Stan's default δ is 0.8 per its documentation; that is unverified here and differs from this paper's 0.6.

## Limitations

- Only basic HMC with an identity mass matrix is compared. There is no comparison with RMHMC, windowed HMC, or HMC with a mass matrix (§5).
- There are four targets, all smooth and unimodal or close to it. There are no multimodal, funnel-shaped or heavy-tailed hierarchical targets, even though those are where HMC-family samplers are known to struggle. There is also no assessment of divergences as a diagnostic.
- The dual-averaging defaults were tuned on one of the evaluation targets (C7).
- The cost model counts gradient evaluations only. For cheap models the O(2ʲ) inner products and random numbers are not negligible, as the paper concedes.
- Only invariance is proved. Ergodicity and the effect of adapting ε are handled by the freeze-after-warm-up convention and by citation.
- The ESS reference moments come from a long run of NUTS itself. That is sensible, but the estimate of the target's variance used to judge both samplers therefore comes from one of the samplers being judged. With 50,000 draws this is probably harmless (unverified).
- The paper describes the 2011 algorithm. Production implementations have since changed the selection rule, the U-turn criterion and the adaptation (see Connections). "Use NUTS" today means a descendant of what is here.

## Open questions

- **Ergodicity.** Under what conditions on L is NUTS geometrically ergodic? Nothing here settles it. A convergence analysis of the doubling kernel would.
- **Mass matrices.** Do the paper's efficiency gains survive once HMC is given a mass matrix? §5 predicts both samplers benefit. A comparison of NUTS and HMC with matched metric adaptation would close this.
- **The windowed-HMC hypothesis.** How much of NUTS's gain comes from the adaptive length, and how much from having no single accept/reject step? This could be tested by comparing against windowed HMC at the best fixed λ.
- **Discrete variables.** Does NUTS's adaptive trajectory length help in models with discrete variables, as §5 conjectures? The paper does not test this.

## Corrections to the seeded skim

- **The recommended δ for NUTS is 0.6, not 0.65.** The seed says "δ = 0.65 is used in illustrations". That is true only of Figure 4. §4.4 concludes that "δ = 0.6 therefore seems like a reasonable default value for NUTS", and that NUTS's efficiency is flat over δ ∈ [0.45, 0.65]. The value 0.65 is the default the paper supports for HMC (Beskos et al. 2010, and HMC's best δ in Figure 6). Figure 7 and the ESS reference runs use δ = 0.5.
- **"Matches or beats" should be split.** It is about equal on LR and HLR, and about 3× better than HMC's best ESS on MVN and SV (§4.4, p. 25). The comparison ignores the cost of HMC's tuning runs, which favours HMC.
- **"No hand tuning" has a qualification the seed omits.** The dual-averaging constants γ, t₀ and κ were set "by trying a few settings for each parameter by hand" on the stochastic-volatility model, which is one of the four evaluation targets. The authors add that they "may not work as well for other sampling algorithms or for H statistics other than the ones described" (p. 16). The user tunes nothing, but the defaults were tuned on the test bed.
- **The stochastic-volatility target is 3001-dimensional.** τ is integrated out (eq. 24), leaving 3000 scales plus ν. The hierarchical logistic regression is 302-dimensional: α, 300 coefficients (24 main effects plus 276 two-way interactions) and σ². The seed gave no dimensions.
- **Mass matrices are not used anywhere in the paper.** The seed's "A mass matrix approximating the posterior covariance would help both samplers" is correctly attributed to §5, but it is future work. Every experiment uses the identity kinetic energy ½r·r.
- **The paper already notes, and chooses, the slice-variable form.** It says the variant without the slice variable "seems empirically to be slightly less efficient" (p. 6). The later switch to multinomial sampling therefore reverses an empirical judgement stated here. I did not read the source of that switch (see Connections).
