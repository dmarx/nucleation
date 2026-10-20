---
status: Active
title: 'Over a fixed finite set of basis functions, slow feature analysis is a generalized eigenproblem: the outputs that minimize ⟨ẏ²⟩ under zero mean, unit variance and decorrelation are the bottom generalized eigenvectors of the derivative covariance against the covariance, in order of slowness, and a stack of such stages, each of whose function spaces contains its inputs, can only keep or lower each of its first m slowness values on the training signal, and may keep them'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Filed Active from NOTE-tmp6kiiy. The closed form is the paper's §3,
    argued there in one paragraph with a citation to Mitchison (1991).
    The treatment of a singular covariance, the generalized eigenproblem,
    the uniqueness up to rotation in degenerate eigenspaces, the joint
    (trace) form, the invariance to the choice of basis, the lag-one
    identity and the monotonicity across stages are the record's. Every
    step is re-derived below, which meets the condition for Active under
    ADR-047 v2. Numerical checks are reported with it.
tags:
- mathematics
- representation-learning
date: '2026-10-20'
source:
- LIT-tmpf5lvd
answers:
- QUESTION-tmp8qovh
summary: >-
  Wiskott and Sejnowski (2002), [LIT-tmpf5lvd](../literature.d/LIT-tmpf5lvd.md), read in full in
  [NOTE-tmp6kiiy](../notes.d/NOTE-tmp6kiiy.md). Within the span of a fixed basis, the slowest
  decorrelated unit-variance outputs are the bottom generalized
  eigenvectors of the pencil (⟨ż̃ż̃ᵀ⟩, cov z̃), and each output's slowness is
  its eigenvalue. A consequence the paper does not draw: a stack of such
  stages whose function spaces contain their inputs is never faster at a
  higher stage, componentwise, on the training signal, so in this model
  "higher is slower" is imposed by the objective, weakly, and can stall.
  It is about the training signal and a fixed function space. It says
  nothing about test data, about a generative model, about invariance as
  opposed to slowness, or about learning dynamics.
---
<!-- inactive-ok-file: CLAIM-331 THEORY-186 — Proposed; claims and accounts this bears on, nothing here rests on their being settled -->

# THEORY-tmp45pcv: Over a fixed finite set of basis functions, slow feature analysis is a generalized eigenproblem: the outputs that minimize ⟨ẏ²⟩ under zero mean, unit variance and decorrelation are the bottom generalized eigenvectors of the derivative covariance against the covariance, in order of slowness, and a stack of such stages, each of whose function spaces contains its inputs, can only keep or lower each of its first m slowness values on the training signal, and may keep them

## Source

Wiskott and Sejnowski (2002), "Slow Feature Analysis: Unsupervised
Learning of Invariances", *Neural Computation* 14(4): 715–770,
[LIT-tmpf5lvd](../literature.d/LIT-tmpf5lvd.md), read in full in [NOTE-tmp6kiiy](../notes.d/NOTE-tmp6kiiy.md) from the authors' PostScript
preprint. The learning problem is §2, Eqs. 1–4. The closed form is §3,
Eqs. 5–8 and steps 1–7 (Eqs. 9–33). The repeated application is step 6
and Example 3 (§4.2). The derivations below are the record's.

## What was actually shown

**Setting.** A training signal x(t), t ∈ [t₀, t₁], and averages
⟨f⟩ = (t₁ − t₀)⁻¹ ∫ f dt over that interval (for sampled data, means over
samples, with ż a difference quotient; the paper does not say which it
used). A fixed basis h̃ = (h̃₁, …, h̃_K), the expanded signal
z̃(t) = h̃(x(t)), C = ⟨(z̃ − ⟨z̃⟩)(z̃ − ⟨z̃⟩)ᵀ⟩ and Ḋ = ⟨ż̃ż̃ᵀ⟩. The candidate
outputs are y = w₀ + wᵀz̃. The problem (§2): for j = 1, …, J, minimize
Δ(y_j) = ⟨ẏ_j²⟩ subject to ⟨y_j⟩ = 0, ⟨y_j²⟩ = 1 and ⟨y_j′y_j⟩ = 0 for
j′ < j.

**Step 1, the offset.** ẏ = wᵀż̃ does not involve w₀, nor does the
variance. ⟨y⟩ = 0 fixes w₀ = −wᵀ⟨z̃⟩. So y = wᵀ(z̃ − ⟨z̃⟩), with
⟨y²⟩ = wᵀCw, ⟨y_j′y_j⟩ = w_j′ᵀCw_j and Δ(y) = wᵀḊw.

**Step 2, a singular covariance.** If Cv = 0, then
⟨(vᵀ(z̃ − ⟨z̃⟩))²⟩ = 0, so vᵀ(z̃(t) − ⟨z̃⟩) = 0 for almost every t, and for
every t if z̃ is continuous. Its derivative vᵀż̃ is then 0 too, so Ḋv = 0.
Adding v to w changes neither y nor Δ. Nothing is lost by working on the
range of C, of rank r. This is what the paper's discarding of near-zero
singular values does (§3, after step 7), and why it calls that choice
"not critical".

**Step 3, sphering.** Write C = UΛUᵀ on its range, with Λ the r positive
eigenvalues, and S = Λ^{−1/2}Uᵀ. Set z = S(z̃ − ⟨z̃⟩), so ⟨z⟩ = 0 and
⟨zzᵀ⟩ = I_r (Eqs. 15–17). Every admissible y is vᵀz for exactly one
v ∈ ℝ^r (take v = Λ^{1/2}Uᵀw). The constraints become vᵀv = 1 and
v_j′ᵀv_j = 0 (Eqs. 6–8), and Δ(y) = vᵀMv with M = ⟨żżᵀ⟩ = SḊSᵀ, symmetric
and positive semi-definite.

**Step 4, the order.** Let M = Σ_i μ_i u_i u_iᵀ with μ₁ ≤ … ≤ μ_r and the u_i
orthonormal. For a unit v, vᵀMv = Σ μ_i c_i² ≥ μ₁ with c_i = u_iᵀv, and
equality holds exactly when v lies in the μ₁-eigenspace. Suppose
v₁, …, v_{j−1} are orthonormal eigenvectors for μ₁, …, μ_{j−1}. Their span
V is M-invariant, so M maps V^⊥ into itself, and the eigenvalues of M on
V^⊥ are μ_j ≤ … ≤ μ_r. The same argument on V^⊥ gives min Δ(y_j) = μ_j,
attained exactly on the μ_j-eigenspace within V^⊥. By induction, the
sequential solution is v_j = u_j and Δ(y_j) = μ_j (Eqs. 19–26). It is
unique up to sign, and up to rotation inside a degenerate eigenspace. So
Δ(y_j′) ≤ Δ(y_j) for j′ < j, as §2 says.

**Step 5, the generalized eigenproblem.** With w = Sᵀv,
Mv = μv ⇔ SḊSᵀv = μv ⇔ Ḋw = μCw restricted to the range of C (multiply by
UΛ^{1/2} and use Sᵀ = UΛ^{−1/2}). The slow features are the bottom
generalized eigenvectors of the pencil (Ḋ, C), and the slowness values
are the generalized eigenvalues. The paper does not use this phrase. It
spheres and then runs PCA on ⟨żżᵀ⟩, which is the same computation.

**Step 6, the joint form.** By Ky Fan's theorem, min Σ_{j≤k} Δ(y_j) over
all k outputs with ⟨yyᵀ⟩ = I is μ₁ + … + μ_k, attained by any orthonormal
basis of span{u₁, …, u_k} when μ_k < μ_{k+1}. So the sequential and the
joint problems agree on the span. Decorrelation is what picks a basis
inside it.

**Step 7, the basis does not matter.** If h̃ is replaced by A h̃ + b with A
invertible, then C → ACAᵀ and Ḋ → AḊAᵀ, and the same functions solve the
problem. The solution depends on the function space span{1, h̃₁, …, h̃_K},
not on the basis. That is the precise content of the abstract's "the
optimal solution within a family of functions".

**Step 8, the lag-one form.** For sampled data with a unit step,
Δ₁(y) = ⟨(y(t+1) − y(t))²⟩ = ⟨y(t+1)²⟩ + ⟨y(t)²⟩ − 2⟨y(t)y(t+1)⟩, which is
2(1 − ρ₁) when the two windows have unit variance, ρ₁ being the lag-one
autocorrelation. So SFA maximizes each output's lag-one autocorrelation.
With a = y(t), b = y(t − 1), the same assumptions give
V(a + b) = 4 − Δ₁ and V(a − b) = Δ₁, so Becker and Hinton's
I = ½ log(V(a + b)/V(a − b)) (Eq. 42) is ½ log((4 − Δ₁)/Δ₁), strictly
decreasing in Δ₁. This makes exact the paper's "almost identical"
optimization problem for a single output.

**Step 9, stacking.** Let stage k + 1 take the first m outputs
y^(k)_1, …, y^(k)_m of stage k as input (or several stages' outputs, as in
the convergent a-layers of Example 4), and let its function space contain
the linear functions of its inputs, as both linear and quadratic SFA do.
By Courant–Fischer, μ^(k+1)_j is the minimum, over j-dimensional subspaces
of that space, of the largest Δ of a unit-variance output in the subspace.
span{y^(k)_1, …, y^(k)_j} is such a subspace, and its outputs are already
orthonormal, with largest Δ equal to μ^(k)_j. So μ^(k+1)_j ≤ μ^(k)_j for
every j ≤ m. On the training signal, each stage is componentwise at least
as slow as the stage it reads. The inequality need not be strict. The
paper's Example 3 has two quadratic stages that "did not yield an η-value
lower than that of the input signal" before a third extracts the hidden
slow signal (correlations 0.59, 0.61, 0.97; Fig. 7, Table 2).

**Checks.** On the paper's Fig. 2 example (x̃₁ = sin t + cos²(11t),
x̃₂ = cos(11t), 4096 samples), quadratic SFA by sphering and PCA and by
the generalized eigenproblem gave the same eigenvalues (1.00, 121.0,
229.5, 357.6, 484.1). The first output correlated with sin t to within
10⁻¹¹, and its η-index (Eq. 34) was 1.000, as the footnote's computation
for a sine of one cycle predicts. On a reconstruction of Example 3 (one
seed, its own filters), the first three slowness values over four stacked
quadratic stages were (0.0491, 0.0995, 0.1304), (0.0491, 0.0981, 0.1067),
(0.0490, 0.0660, 0.0992) and (0.0413, 0.0491, 0.0985). They never rose,
stalled for three stages in the first component, and the hidden slow
signal moved to the first output only at the fourth stage (|r| = 0.93).
The lag-one identity held to 5 × 10⁻⁴, the edge terms.

What could have failed. The sequential definition, with each output
constrained only against the earlier ones, could have given something
other than the eigenvectors; it does not. A singular covariance could
have let a degenerate direction look infinitely slow; Step 2 rules it
out. And the stack could have got faster at a higher stage, which would
have made "higher is slower" a finding of the model rather than a
property of its objective. Step 9 rules that out on the training signal.

## What this does not say

- **Not that the slowest features are invariances.** The objective
  selects slow functions. In the paper's own Example 4, the slowest output
  is a "where" component that tracks pattern location, and the authors
  say location and identity "may vary on similar time scales" (§1). Slow
  and invariant come apart in both directions: a cyclic variable such as
  phase is slow and cannot be extracted (Example 1).
- **Not about test data.** Every statement holds for the averages over
  the training signal. Test outputs are "only approximately normalized"
  (Eqs. 31–33), and Fig. 19's test curves across layers "are not monotonic
  and cross each other".
- **Not that a stack of stages is optimal.** Each stage is optimal for
  its own input. The stack is greedy, trained without backpropagation,
  and is not the optimum over the composite function class. Step 9 gives
  monotonicity, not optimality.
- **Not with clipping.** Example 4 clips each transferred signal at ±3.7.
  The clipped signal is not in the next stage's span, so Step 9 does not
  cover that network exactly.
- **Not a generative account.** No model of how x(t) is produced enters.
  When the slowest features recover the latent causes, and when they are
  coarse or predictively sufficient, is not addressed. Step 8 shows that
  each feature is maximally self-predictable at lag one from its own past
  value, not that the features are sufficient for predicting the input.
- **Not an order of acquisition.** The solution is computed in one shot.
  Nothing here says in what order an online learner would find the
  features.
- **Not isolation of features.** Decorrelation separates outputs, not
  sources. Example 2 spreads velocity over three outputs (correlations
  0.66, 0.34, 0.33), and the authors call the constraint "not sufficient".

## Connections

- **[QUESTION-tmp8qovh](../questions.d/QUESTION-tmp8qovh.md): answers in part.** Within one stage the slowness
  order is the eigenvalue order of one fixed symmetric pencil, so the
  spans of the first k outputs nest, as [THEORY-tmp3xg7a](THEORY-tmp3xg7a.md)'s truncated
  diffusion maps do. Across stages, Step 9 gives each level a function of
  the level below, a refinement chain by construction, with slowness
  non-increasing up the chain. The two orders agree because the hierarchy
  is built from the objective. That is the exactly commuting case again.
  The question's third order, acquisition, is not touched.
- **[LIT-252](../literature.d/LIT-252.md), [NOTE-824](../notes.d/NOTE-824.md).** Pfau et al. treat SFA as the graph-Laplacian case
  of a spectral inference network. With a unit step, Σ_t (y(t+1) − y(t))²
  is the quadratic form of the Laplacian of the path graph on consecutive
  samples, so Step 5's bottom eigenvectors are that Laplacian's bottom
  eigenfunctions within the function space. The identity is Sprekeler's
  (2011), as cited there, not this paper's.
- **[CLAIM-331](../claims.d/CLAIM-331.md).** In a stack built to minimize Δ, a higher stage is never
  faster than the one below it, on the training signal. The temporal
  facet of level holds here because the objective imposes it, so this
  model cannot count as independent evidence that higher levels are
  slower. The stalls in Example 3 show that it holds only weakly.
- **[THEORY-186](THEORY-186.md).** That entry orders acquisition by singular value. This
  one orders converged features by slowness. The two are different
  spectra, of different operators.
