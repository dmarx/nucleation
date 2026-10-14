---
status: Read
paper: LIT-975
title: 'Zhai — Contextures: The Mechanism of Representation Learning'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read from the arXiv PDF of 2504.19792v1 (CMU-CS-25-104, April 2025),
    text extracted with pdftotext. Read in full: Chapters 1–7, Appendix A
    (proofs for Chapter 2) and Appendix B (proofs for Chapter 3), on which
    the central claims rest. Chapter 6 (distribution shift) was read in
    its main text; Appendices C, D and E (proofs of the Chapter 4, 5 and 6
    results) were not read line by line, and nothing below leans on them.
date: '2026-10-14'
summary: >-
  For any joint law of an input X and a context A, symmetric or not, the
  conditional-expectation operator from L²(P_A) to L²(P_X) has a singular
  value decomposition (assuming Hilbert–Schmidt), and its top-d left
  singular functions are the unique d-dimensional encoder, up to
  invertible linear maps, that minimizes worst-case linear-probe
  approximation error over tasks of compatibility at least 1−ε. Several
  squared-error objectives reach that span at their optimum. The claims
  about scaling and about moderate association are argued and measured,
  not proved.
---
<!-- inactive-ok-file: THEORY-001 THEORY-005 THEORY-009 THEORY-tmp1iy33 — Proposed; the accounts this reading bears on, and the one filed from it, open -->

# NOTE-tmp7o2ar: Zhai — Contextures: The Mechanism of Representation Learning

## Contribution

A PhD dissertation that recasts many pretraining set-ups as one object:
a joint distribution P⁺ of an input X and a "context variable" A
(a label, an augmented view, a graph neighbour, a caption, a masked
text). It shows that the encoder which recovers the top singular
functions of the induced conditional-expectation operator is optimal, in
a stated worst-case sense, for every task compatible with that context,
and that several squared-error objectives are optimized exactly by that
span. X and A may live in different spaces, so the result is a
singular-function result for a pair operator that is not self-adjoint.

## Key insight

The thing a pretrained encoder should learn is not an eigenspace of a
symmetric pair operator but the left singular space of the map
g ↦ E[g(A) | X = x]. Symmetry is never assumed; a self-adjoint operator
appears only by composing that map with its adjoint (X → A → X′), whose
kernel is the "dual kernel" k_X⁺. The adjoint is written down directly by
Bayes' rule.

## Assumptions

- P_X and P_A live on compact Hausdorff spaces; P_X is fixed until
  Chapter 6.
- Both T_P⁺T_P⁺* and T_P⁺*T_P⁺ are Hilbert–Schmidt (stated once in §1.3
  and assumed "throughout").
- Downstream use is a linear probe W Φ(x) + b only.
- The optimality results are at the population optimum. Optimization,
  architecture and finite width are explicitly set aside ("independent of
  the optimizer", §2.1; Chapter 7 lists their effect as open).
- All objectives are squared-error ("spectral (that is L²)"); the theory
  does not cover cross-entropy or NT-Xent, and says so (§2 intro).
- Example 1.13 (graphs) assumes an undirected graph, w(u,v) = w(v,u), and
  the proof of Theorem 2.8 uses that symmetry.

## Key results

- **Definition 1.1 and Lemma 1.4 (duality).** T_P⁺ : L²(P_A) → L²(P_X),
  (T_P⁺g)(x) = E[g(A)|x]; its adjoint is (T_P⁺*f)(a) = E[f(X)|a]. T_P⁺T_P⁺*
  and T_P⁺*T_P⁺ share eigenvalues λ_i = κ_i ∈ [0,1]; μ_i = λ_i^(−1/2) T_P⁺ν_i
  and ν_i = λ_i^(−1/2) T_P⁺*μ_i. s_i = λ_i^(1/2) are the singular values,
  with μ₀ = ν₀ ≡ 1. *Holds when:* both compositions are Hilbert–Schmidt.
- **Lemma 1.5 (spectral decomposition).**
  P⁺(x,a) = Σ_i s_i μ_i(x) ν_i(a) P_X(x) P_A(a). So the density ratio is the
  kernel of T_P⁺, and its singular expansion is the signature.
- **Definition 1.7.** Φ "learns the contexture" if span{φ₁..φ_d} equals
  the span of some top-d left singular functions μ₁..μ_d, excluding μ₀.
  Only the span is fixed; the contexture depends on P_X even though T_P⁺
  does not (Remark 1.9).
- **Theorems 2.2–2.11 (objectives).** At the optimum: one-hot MSE
  extracts the top-d eigenspace of T_P⁺ΛT_P⁺* with Λ set by class sizes
  (2.2), and the √P_A-balanced loss learns the contexture exactly (2.4);
  the spectral contrastive loss and the covariance-constrained
  non-contrastive loss give Ψ̃ spanning top right singular functions, and
  Φ = T_P⁺Ψ learns the contexture (2.9; proof by Eckart–Young–Mirsky in
  App. A.5); SVME, min E‖Φ(X) − Ψ(A)‖² s.t. Cov[Φ] = I, with the
  constraint on Φ only, reduces to KISE and learns the contexture (2.11;
  the optimal Ψ for fixed Φ is T_P⁺*Φ, App. A.6). An encoder composed with
  a fixed feature map learns the contexture of the convolution of the two
  contexts (2.12).
- **Theorem 3.2 (compatible tasks are nearly invariant).** If
  ρ(f*, P⁺) ≥ 1 − ε then f* = E[g*(A)|x] with
  E_X E_{A,A′|X}[(g*(A) − g*(A′))²] ≤ 4ε‖g*‖². Compatibility is
  ρ(f,P⁺) = max_g ⟨f̃, T_P⁺g⟩ / (‖f̃‖‖g‖), equal to
  (Σ s_i²u_i² / Σ u_i²)^(1/2) for f = Σ u_iμ_i.
- **Theorem 3.4 (optimality).** If 1 − ε ≤ s₁, then among all d-dimensional
  Φ with φ_i ∈ L²(P_X), Φ minimizes the worst-case approximation error on
  F_ε(P⁺) = {f : ρ(f,P⁺) ≥ 1 − ε} if and only if it learns the contexture,
  and the minimum is (s₁² − (1−ε)²)/(s₁² − s²_{d+1}). Conversely every
  d-dimensional Φ has a task at compatibility exactly 1 − ε with at least
  that error. Proof in App. B.2.
- **Theorem 3.10.** For an arbitrary encoder, the worst-case error on
  F_ε is at most (s₁² − (1−ε)² + s₁·TG)/(s₁² − TG²), with TG the trace gap
  built from the ratio trace Tr(C_Φ⁻¹B_Φ), B_Φ = Cov[T_P⁺*Φ].
- **§3.3 (context usefulness).** A heuristic metric τ_d =
  1/(1 − s²_{d+1}) + β Σ_{i≤d}s_i² / Σ_{i≤d₀}s_i². Across 28 OpenML datasets
  and 140 contexts its Pearson correlation with the best downstream error
  has median 0.587 and mean 0.431, negative on four datasets (Table 3.1).
- **Chapter 4.** Convolution, convex combination and concatenation of
  contexts; Proposition 4.1 gives the dual kernel of a convolution as
  T_k1…T_kr…T_k1, self-adjoint, and Remark 4.2 notes that T_kr…T_k1 alone
  is not. A minimax over convex weights picks the weakest association
  (Theorem 4.8). Tabular results beat XGBoost on average (Tables 4.3–4.4).
- **Chapter 5.** Context complexity κ² bounds
  k_X⁺(x,x) = D_χ²(P⁺(·|x) ‖ P_A) + 1; generalization bounds polynomial in
  κ (Theorems 5.11, 5.12), which the author notes is exponential in input
  dimension for masking (Examples 5.2–5.4). Power kernels k^p give the
  diffusion distance of Coifman and Lafon (§5.3, citing [29]).
- **Chapter 6.** Under over-parameterization and small-step gradient
  descent, reweighting and DRO converge to the ERM solution unless
  regularization is strong enough to raise training loss
  (Theorems 6.4–6.11); DORO trims the worst losses to resist outliers.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | For any joint law of X and A, the top-d left singular functions of E[·(A)|X] minimize worst-case linear-probe approximation error over tasks of compatibility ≥ 1−ε, uniquely up to span | strong | Theorem 3.4, App. B.2 |
| C2 | Tasks compatible with a context are nearly invariant across two context draws for the same input | strong | Theorem 3.2, App. B.1 |
| C3 | Spectral contrastive, covariance-constrained non-contrastive, balanced MSE and SVME objectives reach the contexture at their optimum | strong | Theorems 2.4, 2.9, 2.11, App. A |
| C4 | Larger networks align more closely with the top-d singular functions, up to a point | weak | one tabular dataset (abalone), KNN context, CCA ≈ 0.9 (§2.6, Fig. 2.4) |
| C5 | Scaling model size alone gives diminishing returns, so better contexts are needed | weak | inference from C4; not tested on any foundation model |
| C6 | A useful context has moderate association | moderate | qualitative argument plus τ's median 0.587 correlation, with stated failures (§3.3) |
| C7 | Reweighting and DRO cannot beat ERM without large regularization in over-parameterized models | moderate | Theorems 6.4–6.11 (proofs in App. E, not read here) |

## Method

Two encoders, Φ on inputs and Ψ on contexts, trained by SVME with an
orthonormality constraint on Φ alone (implemented with VICReg, which the
author reports does not enforce it exactly, §2.2); or one encoder by
KISE when the dual kernel can be evaluated. Exact eigenfunctions are
recovered post hoc from a generalized eigenproblem B_Φ v = λ C_Φ v (§2.5).

## Concepts

- **Context.** A variable A with a joint law P⁺(x,a); access is by pairs,
  by a kernel, or by repeated transformation.
- **Expectation operator T_P⁺.** g ↦ E[g(A)|X=x], from L²(P_A) to L²(P_X).
- **Dual kernel k_X⁺ and positive-pair kernel k_A⁺.** The kernels of
  T_P⁺T_P⁺* and T_P⁺*T_P⁺; both p.s.d. by construction.
- **Contexture.** The span of the top-d left singular functions, μ₀
  excluded.
- **Compatibility ρ(f,P⁺).** How far f lies in the range of T_P⁺ with a
  low-variance preimage; mean and scale of f do not enter.
- **Association.** The decay rate of s_i²: independence gives only s₀,
  A = X gives no decay.

## Connections

It generalizes the augmentation-graph line (HaoChen et al., Johnson et
al., the positive-pair kernel of the latter) from a single space to an
input–context pair, and absorbs supervised learning, multi-view SSL,
CLIP-style pairs, multi-step generation and RLHF as instances. The
compatibility class is the RKHS-isometry condition of the author's
earlier STKR work. Neural eigenfunctions (Deng et al.) give the exact
eigenfunctions (Theorem 2.14). The power kernels connect to diffusion
maps. Also held in the Anthology of the SOTA as [ANTH-LIT-459](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-459.md).

## Bearing on the record

- **[QUESTION-052](../questions.d/QUESTION-052.md) (answered in part; filed as [THEORY-tmp1iy33](../theory.d/THEORY-tmp1iy33.md)).** The
  question asks for "a singular-function result for a non-symmetric pair
  operator, with its own sufficiency guarantee". Theorem 3.4 is that
  result for linear decisions: the operator runs between two different
  spaces and is never assumed symmetric, and the guarantee is exact and
  "if and only if". It is not a directed-transport result in the
  question's other sense: when A = X with a non-reversible kernel, the
  thesis has no worked case, and its only graph example is undirected.
- **[THEORY-009](../theory.d/THEORY-009.md).** Partly corrected, partly confirmed.
  - The thesis obtains every self-adjoint operator by composing T_P⁺ with
    its adjoint, not from the symmetry of (X,A). In the multi-view case the
    positive pair (A,A⁺) is exchangeable because both are drawn from
    P⁺(·|x), which is the same mechanism [THEORY-009](../theory.d/THEORY-009.md) names, seen from the
    construction side.
  - No Riesz: the adjoint is given in closed form by Bayes' rule
    (Definition 1.1).
  - Its promote_when asks for an analysis of an asymmetric objective in
    which eigenfunctions are replaced by singular functions of a
    non-self-adjoint operator. SVME is asymmetric only in where the
    constraint sits; the thesis does not analyse BYOL or SimSiam, naming
    them only as "asymmetry-based" (§2.1). So this is a nearer miss than
    [LIT-228](../literature.d/LIT-228.md) (the identification is derived, Theorem 2.11, and holds for
    X ≠ A), but it does not meet the clause as written. [THEORY-009](../theory.d/THEORY-009.md) should
    record it among the near misses.
- **[THEORY-005](../theory.d/THEORY-005.md).** The thesis assumes Hilbert–Schmidt rather than deriving
  it, but its context complexity is the same χ² quantity pointwise:
  k_X⁺(x,x) = D_χ²(P⁺(·|x)‖P_A) + 1 (Definition 5.1), and A = X "is not
  Hilbert-Schmidt if X and A are infinite sets" (§1.3).
- **[THEORY-007](../theory.d/THEORY-007.md).** Theorem 3.4 is a sibling of Johnson et al.'s minimax
  result: same object in the symmetric case, but the target class here is
  defined by compatibility, not by bounded view-discrepancy, and the
  answer is an exact worst-case value.
- **[THEORY-001](../theory.d/THEORY-001.md).** Supported in a broader form: Theorems 2.4, 2.9 and 2.11
  give one optimum for several objectives. Only up to span; only the
  spectral contrastive loss preserves eigenvalue order (§2.3).
- **[QUESTION-060](../questions.d/QUESTION-060.md).** At the population level, the learned variables are
  fixed by the context alone, independent of architecture, and the thesis
  says the inductive bias of an architecture "should be considered as a
  part of the context" (Chapter 7), left open. Theorem 2.12 is the one
  proved case: a fixed feature map enters as a convolved context. The
  scaling experiment shows learned eigenvalues decaying faster than the
  true ones, which the author puts down to architecture and optimization.
- The LIT's seeded body says "representations learn the top singular
  functions"; the thesis proves that certain objectives are optimized by
  that span, and shows alignment of trained networks on one tabular
  dataset only.
- Its practice content (SVME and KISE as training recipes, context mixing
  for tabular data, DORO) belongs to the Anthology, which already holds
  it as [ANTH-LIT-459](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-459.md).

## Limitations

- Population optimum only; training dynamics, edge-of-stability
  oscillation and architecture are named as open (§2 intro, Chapter 7).
- Squared-error objectives only; cross-entropy and InfoNCE are not
  covered.
- Linear probes only; the optimality is for approximation error, not
  estimation.
- The context-usefulness metric is heuristic, fails on some datasets,
  and cannot compare contexts of different types (§3.3).
- Generalization bounds scale with κ, exponential in dimension for
  masking contexts; the author calls this an open discrepancy (§5.1).
- The pair-access generalization bound is posed as open (§5.2).

## Open questions

- Does the optimality transfer to non-reversible kernels on one space,
  A = X with P⁺(a|x)P_X(x) ≠ P⁺(x|a)P_A(a), where left and right singular
  functions differ on the same space? A worked case would show whether the
  left or the right space is the signature.
- Do BYOL- or SimSiam-type objectives reach the contexture?
- How does an architecture's inductive bias enter as a context?
