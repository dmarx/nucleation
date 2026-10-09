---
status: Read
paper: 'LIT-tmpvzook'
title: 'Exact Learning Dynamics of In-Context Learning in Linear Transformers'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read from the arXiv v2 PDF (22 November 2025, 36 pp.; text extracted
    with pdftotext and kept beside the download). The main text, §§1–5
    (10 pp.), read in full with every figure caption, and the reference
    list. Appendix A read: the setup and assumptions (A.1–A.8), the
    simplified predictor (A.9), the null-parameter argument (A.10), the
    change of variables and continuous limit (A.11), the conservation law
    and logistic solution (A.12) and the loss analysis (A.13). The
    conservation law and the logistic solution were checked; the Wishart
    fourth-moment step that produces s^∞ and the term-by-term loss
    expectation (A.13.2) were followed as statements, not re-derived. The
    v1 (17 April 2025) was not read; v2's related work cites 2025 papers
    and is likely revised.
date: '2026-10-09'
summary: >-
  Solves the averaged gradient-flow dynamics of one linear-attention layer
  trained on in-context regression, when tasks and input covariance share
  an eigenbasis and the weights are assumed to stay in it: each mode is a
  logistic curve on timescale (ηP s_α²)⁻¹, so learning is staged by the
  input spectrum, and the fixed point is the known preconditioned
  predictor W Σ̂_x [((N+1)/N)Σ_x + (Tr Σ_x/N)I]⁻¹. A scaling symmetry
  conserves ‖p₂‖² − ‖q₁‖². The transfer to non-linear transformers and
  grokking is a set of timing coincidences in spectral measures.
---

<!-- inactive-ok-file: THEORY-169 — Proposed; the account this reading is compared with, not a source of -->
<!-- inactive-ok-file: THEORY-039 — Proposed; the synthesis of training phases this reading adds a case to -->
<!-- inactive-ok-file: LIT-242 — Deferred; named as the analogous stepwise result, not relied on -->

# NOTE-tmp6m4yt: Exact Learning Dynamics of In-Context Learning in Linear Transformers

## Contribution

Earlier work had found *where* training a linear-attention layer on
in-context regression ends: at a preconditioned-gradient-descent predictor
(Ahn et al. 2023; Zhang, Frei and Bartlett), constructible by hand (von
Oswald et al., [LIT-792](../literature.d/LIT-792.md)). This paper solves *how it gets there*, in closed
form, for vector-valued tasks ℝᵈ → ℝᵈ, under an alignment assumption: the
trajectory of every eigenmode, the resulting loss curve, and a conserved
quantity. It then proposes spectral measures of weight matrices, motivated
by the solution, and applies them to small non-linear transformers.

## Key insight

The in-context learner is built by an outer learning process that looks
exactly like a two-layer deep linear network (Saxe et al. 2014). The
prediction is a product p₂ · (context statistics) · q₁, so the gradient on
each factor is proportional to the other: growth from a small start is
cooperative and sigmoidal, and each eigendirection of the input
covariance switches on separately, at a time set by s_α². The thing
learned is a fixed preconditioner, the inverse of the *training* input
covariance (corrected for context length), which the forward pass then
applies to each context's empirical covariance.

## Assumptions

- **Architecture.** One layer, one head, identity in place of softmax,
  f(Z) = Z + W^P (ZZᵀ/N) W^Q Z, with merged key-query (W^Q) and
  value-projection (W^P) matrices; no positional encoding; input tokens
  (x_i, y_i) stacked, query (x_q, 0). Prediction from the last column.
- **Data.** x ~ N(0, Σ_x), Σ_x = USUᵀ; a fixed set of P tasks
  W^µ = UΛ^µUᵀ, Λ^µ diagonal with N(0, 1) entries. Tasks are symmetric and
  share the input covariance's eigenbasis. This is a strong restriction:
  it is what makes all matrices commute.
- **Null blocks.** p₁ and q₂ are shown to have zero gradient at zero only
  in expectation over the task distribution (E[W] = 0, odd Gaussian
  moments vanish), with the sum over the fixed P tasks replaced by that
  expectation; fixing them at zero throughout is justified by this and by
  simulation, not proved for finite P.
- **Spectral alignment.** p₂(t) = U p̄₂(t) Uᵀ and q₁(t) = U q̄₁(t) Uᵀ with
  diagonal p̄₂, q̄₁, *assumed* to hold at initialisation and throughout
  (A.11.2). The decoupling into modes depends on it.
- **Large N** (the query's own term in the empirical covariance is
  dropped, A11), small learning rate (continuous time), and averaging over
  tasks and data (the stochasticity of SGD is averaged away).
- **Balanced start** (p_α(0) = q_α(0)) for the logistic closed form.

## Key results

- **Reduced predictor** (Eq. 8). ŷ^µ ≈ p₂ W^µ Σ̂_x q₁ x_q.
- **Mode dynamics** (Eqs. 9–12). τ_α dp_α/dt = q_α(1 − p_α q_α s^∞_α),
  τ_α dq_α/dt = p_α(1 − p_α q_α s^∞_α), with τ_α = (ηP s_α²)⁻¹ and
  s^∞_α = ((N+1)s_α + Tr S)/N.
- **Logistic solution** (Eq. 13). From a balanced start,
  a_α = p_α q_α satisfies τ_α da_α/dt = 2a_α(1 − a_α s^∞_α), so
  a_α(t) = a^∞_α a⁰_α / (a⁰_α + (a^∞_α − a⁰_α) e^{−2t/τ_α}), a^∞_α = 1/s^∞_α.
  The escape time from ε is ≈ (τ_α/2) log(1/(s^∞_α ε)). *Holds when:* the
  assumptions above.
- **Fixed point** (Eq. 11). ŷ^µ(∞) ≈ W^µ Σ̂_x [((N+1)/N)Σ_x + (Tr Σ_x/N) I]⁻¹ x_q;
  → W^µ x_q as N → ∞. Matches Ahn et al. and Zhang, Frei and Bartlett.
- **Conservation** (A.12.1). d/dt(‖p̄₂‖²_F − ‖q̄₁‖²_F) = 0; in fact each
  p_α² − q_α² is conserved, the consequence of invariance under
  p → cp, q → q/c.
- **Loss** (Eq. 14, A.13). L(t) = ½ Σ_α s_α (s_α a_α(t)²/a^∞_α − 2 s_α a_α(t) + 1);
  initial slope negative and ∝ a⁰_α s_α²; the converged loss is non-zero
  at finite N.
- **Empirical** (§4, Figs. 4–7). In 1–4-layer attention-only transformers,
  marginalised effective rank of QK matrices dips around the window where
  in-context learning emerges in the 2+-layer models, and not in the
  1-layer model; the subspace distance falls early. In the grokking model
  (after Nanda et al.), the OV subspace distance falls late, with the test
  error.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Under task averaging, p₁ = q₂ = 0 is preserved in expectation, and the predictor reduces to p₂WΣ̂_x q₁ x_q | moderate | A.10: expectation over E[W] = 0; finite-P exactness not shown; simulation |
| C2 | With shared eigenbasis and assumed alignment, each mode follows a logistic curve on timescale (ηP s_α²)⁻¹ | strong (derivation) within the assumptions | A.11–A.12; Figs. 2A, 3A |
| C3 | The trained predictor is a preconditioned estimator with an inverse, finite-N-corrected training covariance | strong | Eq. 11; agrees with prior fixed-point analyses; Fig. 1 |
| C4 | ‖p₂‖² − ‖q₁‖² is conserved by the averaged flow | strong (proof) | A.12.1 |
| C5 | The same timescale separation organises learning in non-linear attention-only transformers and accompanies ICL emergence | weak | timing of effective-rank dips, Figs. 4–6; no seeds, error bars or controls reported; how the ICL window was located is not stated in the main text |
| C6 | Grokking is linked to delayed stabilisation of the parameter subspace | weak | one grokking model, Fig. 7; coincidence in time, no intervention |
| C7 | The measures can time behavioural evaluations during training | not supported here | Discussion; proposed, not tested |

## Method

Write the prediction through the query column; average gradients over
tasks to remove p₁, q₂; rotate into the shared eigenbasis U so all
matrices are diagonal; average over Wishart-distributed empirical
covariances to get the finite-N factor s^∞; pass to continuous time; solve
the per-mode system, which with a balanced start is a logistic equation.
For non-linear models, track: the curvature of the loss autocorrelation
A(τ) = E[L(t)L(t+τ)] and of parameter norms; effective rank
exp(−Σ pᵢ log pᵢ), pᵢ the normalised singular values (Roy and Vetterli),
recomputed with the leading singular values removed ("marginalised"); and
the subspace distance min_A ‖A M(t) − M(∞)‖.

## Concepts

- **null parameters**: the blocks p₁ (value from x) and q₂ (key-query on
  y) whose expected gradient vanishes at zero, so they stay unused.
- **s^∞(S)**: ((N+1)/N)S + (Tr S/N)I, the finite-context-corrected
  covariance whose inverse the trained weights converge to.
- **timescale separation**: here, the 1/s_α² ordering of when each input
  eigenmode is learned; not the meta-learning sense of slow weights and
  fast context, though the paper invokes both.
- **marginalised effective rank**: effective rank recomputed after
  removing the k leading singular components.
- **subspace distance**: min over A of ‖A M(t) − M(∞)‖; it measures whether
  M(∞)'s rows lie in the row space of M(t), and its normalisation is not
  given.

## Connections

The solution method is Saxe, McClelland and Ganguli's (2014) for deep
linear networks, carried into attention; the paper's point is that the
data spectrum, through the product of the two attention blocks, gives the
same staged learning without depth. The fixed point is Ahn et al.'s and
Zhang, Frei and Bartlett's; the construction it relates to is von Oswald
et al.'s ([LIT-792](../literature.d/LIT-792.md)), which the record holds. Zhang, Singh, Latham and Saxe
(2025) analyse exact dynamics for scalar outputs and multi-head
parametrisations; Lu et al. (2025) and Lyu et al. (2025) work in
asymptotic and scaling regimes. The grokking model is Nanda et al.'s
([LIT-345](../literature.d/LIT-345.md)); the phenomenon is Power et al.'s ([LIT-341](../literature.d/LIT-341.md)). Alternative
accounts of in-context learning cited: Bayesian (Xie et al., [LIT-797](../literature.d/LIT-797.md)) and
kernel (Han et al.).

## Bearing on the record

- **[THEORY-169](../theory.d/THEORY-169.md).** Consistent, and it sharpens one phrase. [THEORY-169](../theory.d/THEORY-169.md)
  reports that "a single trained layer finds these weights up to scale".
  Here, with isotropic inputs (S = sI), the trained predictor is
  W Σ̂_x x_q times a scalar, i.e. [LIT-792](../literature.d/LIT-792.md)'s one gradient step up to scale;
  with anisotropic inputs it is a step preconditioned by the inverse
  training covariance, not plain gradient descent. The THEORY uses only
  the exact constructions, so nothing in it changes.
- **[THEORY-039](../theory.d/THEORY-039.md).** Another kind of phase: here derived, mode by mode,
  ordered by the input spectrum, with plateaus and cliffs in the loss.
  The non-linear evidence adds a further quantity (subspace stability)
  whose timing differs between in-context learning (early) and grokking
  (late). This fits [THEORY-039](../theory.d/THEORY-039.md)'s finding that reported phases are defined
  by different quantities. One tension worth checking: Nanda et al.
  ([LIT-345](../literature.d/LIT-345.md)) place circuit formation before the test-accuracy jump, while
  here the OV subspace stabilises *with* the jump; the two may agree if
  cleanup is what fixes the final subspace, but the paper does not say.
- **[LIT-242](../literature.d/LIT-242.md)** reports the same eigenmode-ordered stepwise learning in
  linearised self-supervised learning; together they are the
  deep-linear-network pattern in two further settings.
- No THEORY is filed. The exact result is a result about training
  transformers, which is anthology material, and its fixed point is
  already known; the staged learning is Saxe et al.'s pattern, which the
  record does not hold as a source.
- The Discussion recommends timing evaluations by these measures: an ML
  practice suggestion, untested. With the subject as a whole, this is why
  the LIT carries `anthology-candidate`.

## Limitations

- The exact solution needs tasks that share the input covariance's
  eigenbasis and are symmetric, and weights that are *assumed* to stay
  aligned with it; whether misaligned initialisations align is not
  analysed.
- The null-parameter reduction is in expectation over tasks; for a fixed
  finite P it is not shown.
- SGD noise is averaged away; the theory is for the mean flow.
- One layer, one head, no softmax, MSE on the query only, no positional
  information.
- The non-linear evidence is qualitative: timing coincidences in derived
  measures, no seeds, error bars, controls or interventions reported, and
  in-context-learning emergence is marked as a highlighted window without
  a stated criterion in the main text. "Mechanistic explanation" in the
  abstract claims more than this shows.
- Notation slips: the learning rate is η in the main text and λ in the
  appendix and in the main-text escape-time formula; the appendix takes
  Σ_x diagonal and tasks in a basis V later set equal to U, the main text
  a general U.

## Open questions

- Do unaligned initialisations align with the data eigenbasis, and on
  what timescale relative to the τ_α? An analysis or simulation of the
  alignment phase would close the gap behind C2.
- Does the staged picture survive softmax attention and depth, where
  Chen et al. and Boix-Adsera et al. report other phase structures?
- Is the subspace-before-magnitude order a robust feature of trained
  transformers? Several seeds, a criterion for "ICL emergence" measured
  independently, and an intervention (freezing or perturbing the
  subspace) would turn C5 and C6 from coincidence into evidence.
- What the trained preconditioner does when a context's covariance
  differs from the training covariance: the formula predicts a specific
  miscalibration, untested here.
