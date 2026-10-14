---
status: Read
paper: LIT-260
title: 'Muandet et al. — Kernel Mean Embedding of Distributions'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read from the arXiv v4 PDF (arxiv.org/pdf/1605.09522, "the final
    version", 147 pp.), text extracted with pdftotext: every section,
    §§1–7, and every numbered statement, but not the 26-page reference
    list. Chapters 2 and 3 (pp. 13–80) were read closely, with each
    statement THEORY-003 and THEORY-009 cite checked against the text.
    Chapters 4–7 were read through at survey depth. The review gives
    proof sketches and defers full proofs to the cited papers; where it
    proves something, that is said below.
date: '2026-10-14'
summary: >-
  A survey whose load-bearing chain is short and explicit. An RKHS is a
  Hilbert space with bounded evaluation, so Riesz gives k_x (Thm 2.4, Prop.
  2.1). If E_P√k(X,X) < ∞, the expectation functional is bounded and Riesz
  gives μ_P with E_P f = ⟨f, μ_P⟩ (Lemma 3.1, proved). MMD is ‖μ_P − μ_Q‖
  (eq. 3.29), a metric on distributions exactly when k is characteristic.
  HSIC is the squared Hilbert–Schmidt norm of the centred cross-covariance.
  Every result is for a fixed kernel.
---
<!-- inactive-ok-file: THEORY-003 THEORY-009 THEORY-005 — Proposed; the accounts that cite this review, and the operator account its §3.2 and §4 bear on -->

# NOTE-tmpgvy79: Muandet et al. — Kernel Mean Embedding of Distributions

## Contribution

The review collects the theory and applications of embedding probability
distributions in an RKHS, P ↦ μ_P = ∫k(x,·)dP(x). It covers marginal
embeddings, MMD and HSIC; conditional embeddings as operators, and the sum,
product and Bayes rules built from them; and the relations to density
estimation, characteristic functions and energy distance. Its theoretical
content is a numbered chain of standard results with sketched proofs and
pointers. It adds no new theorem of its own. What it adds is the chain in
one place.

## Key insight

An expectation is a bounded linear functional on the RKHS whenever
E√k(X,X) is finite, so it has a representer, μ_P. Everything else (MMD,
HSIC, the conditional operators) is geometry of these representers. How
much of P they keep is a property of the kernel.

## Assumptions

- **A fixed, symmetric, positive-definite kernel** k on a nonempty set X
  (Def. 2.1), real-valued.
- **Measurability, and integrability for existence.** Lemma 3.1 needs
  E_(X∼P)√k(X,X) < ∞. §3.2's covariance operators assume
  E_X k(X,X) < ∞ and E_Y l(Y,Y) < ∞ (eq. 3.13, printed "≤ ∞"), which is
  stronger and puts H inside L²(P_X).
- **Separability** of H and G where Hilbert–Schmidt operators are used
  (§2.3, §3.6).
- **Mercer (Thm 2.1)** needs X compact Hausdorff, μ a finite Borel measure
  with support X, and k continuous. **Theorem 3.4** needs k continuous and
  bounded on a separable topological space.
- **Conditional embeddings (§4.1)** need E[g(Y)|X = ·] ∈ H for all g ∈ G,
  and Theorem 4.1 also needs C_XX injective and μ_Π ∈ R(C_XX). The review
  warns that this "may not hold in general": for Gaussian kernels and
  independent X, Y it fails. It then switches to the regularized form
  C_YX(C_XX + λI)⁻¹.

## Key results

- **Def. 2.4 (p. 22).** H is an RKHS if every evaluation functional
  F_x[f] = f(x) is bounded: |f(x)| ≤ C‖f‖_H.
- **Thm 2.4, Riesz (p. 23, eq. 2.15).** A bounded linear A: H → R has a
  g_A ∈ H with A[f] = ⟨f, g_A⟩. Stated, proof cited. "The Riesz
  representation theorem will be used to prove a sufficient condition for
  the existence of the kernel mean embedding in an RKHS (see Lemma 3.1)."
- **Prop. 2.1 (p. 23, eq. 2.16).** For each x there is k_x ∈ H with
  f(x) = ⟨k_x, f⟩. This follows from Def. 2.4 and Thm 2.4, and
  k(x,y) := k_y(x) = ⟨k_x, k_y⟩ (eq. 2.17).
- **Thm 2.5, Aronszajn (p. 24).** Every positive-definite k has an RKHS,
  unique up to isometric isomorphism, and conversely. Stated, cited. H is
  the closed span of {k(x,·)}.
- **Thm 2.1, Mercer (p. 17).** Under its compactness conditions,
  k(u,v) = Σλ_iψ_i(u)ψ_i(v), converging absolutely and uniformly, with
  ψ_i eigenfunctions of T_k on L²(X,μ).
- **Bochner and eq. 2.11.** For translation-invariant k,
  ⟨μ_P, μ_Q⟩_H = ⟨φ_P, φ_Q⟩_(L²(R^d,Λ)), where φ_P is P's characteristic
  function and Λ the spectral measure.
- **Def. 3.1 and Lemma 3.1 (pp. 30–31; Smola et al. 2007).** μ_P :=
  ∫k(x,·)dP(x), "a Bochner integral" (eq. 3.11). If E_(X∼P)√k(X,X) < ∞,
  then μ_P ∈ H and E_P f(X) = ⟨f, μ_P⟩.
  - Proved. |L_P f| ≤ E|f(X)| = E|⟨f, k(X,·)⟩| ≤ E√k(X,X)·‖f‖, using
    Jensen and Cauchy–Schwarz. So L_P is bounded, Riesz gives h, and
    h(x) = L_P k(x,·) = ∫k(x,x′)dP(x′), so h = μ_P.
  - The proof opens "We assume L_P is bounded" and then shows it.
  - The review calls E_P f = ⟨f, μ_P⟩ "a reproducing property of the
    expectation operation".
- **§3.2, eqs. 3.14–3.16.** C_YX := E[φ(Y) ⊗ φ(X)] = μ_(P_YX), Hilbert–
  Schmidt under eq. 3.13. Equivalently it is "a unique bounded operator"
  with ⟨g, C_YX f⟩ = E[g(Y)f(X)] (uncentred; the centred version subtracts
  μ_(P_Y) ⊗ μ_(P_X)). C_XX is "positive and self-adjoint", and
  C_XY = C_YX*.
- **Theorem 3.2 (Fukumizu et al.).** If E[g(Y)|X = ·] ∈ H, then
  C_XX E[g(Y)|X = ·] = C_XY g.
- **§3.2, closing.** C_XX, transported to L²(X, P_X), "happens to
  coincide with" the Mercer operator T_k, "hence they have the same
  eigenvalues". Cited, not proved.
- **Thm 3.4 (Tolstikhin et al.).** If sup k(x,x) ≤ C_k, then with
  probability ≥ 1 − δ, ‖μ̂_P − μ_P‖ ≤ √(C_k/n) + √(2C_k log(1/δ)/n).
  The rate is minimax.
- **Def. 3.2 (p. 38).** k is characteristic if P ↦ μ_P is injective.
  Sufficient conditions (§3.3.1): H + R dense in L^q(P) for all P;
  universal kernels on compact domains; translation-invariant kernels
  whose spectral measure has full support; integrally strictly
  positive-definite kernels. Table 3.1: Gaussian, Laplacian and Matérn
  are characteristic on R^d; linear and polynomial are not; the Dirac
  kernel 1[x = y] is characteristic on a finite set.
- **§3.5, eq. 3.29.** MMD[H,P,Q] := sup_(‖f‖≤1)(E_P f − E_Q f) =
  ‖μ_P − μ_Q‖_H, citing Borgwardt et al. and Gretton et al. (2012a,
  Lemma 4). Eq. 3.30 gives MMD² = E k(X,X̃) − 2E k(X,Y) + E k(Y,Ỹ). It
  is a metric on distributions iff k is characteristic. Otherwise it is a
  pseudometric whose zero set is "an equivalence class of distributions".
- **§3.6, eq. 3.37.** HSIC = ‖C_XY‖²_HS for the centred cross-covariance,
  in kernel form. If the product kernel k ⊗ l is characteristic, HSIC = 0
  iff X ⊥ Y, because C_XY = μ_(P_YX) − μ_(P_Y ⊗ P_X). The review also
  notes that "the MaxMMD of Jegelka et al. (2009) is in fact equivalent to
  the dependence maximization framework", and that HSIC-based clustering
  with a suitable output kernel recovers k-means.
- **§3.7.** κ(P,Q) = ⟨μ_P, μ_Q⟩ is a kernel on distributions. It is linear
  in P, so it is not universal on distributions. The Gaussian of
  ‖μ_P − μ_Q‖ is universal when the embedding is injective on a compact X
  (Thm 3.8).
- **§4.1, Def. 4.1.** U_(Y|X) := C_YX C_XX⁻¹, U_(Y|x) := C_YX C_XX⁻¹k(x,·),
  with E[g(Y)|X = x] = ⟨g, U_(Y|x)⟩ under the conditions above. The
  empirical form is μ̂_(Y|x) = Σβ_i l(y_i,·), β = (K + nλI)⁻¹k_x
  (Thm 4.2). It is also the solution of a vector-valued ridge regression
  (§4.2). Remark 4.1 records that the unregularized operator needs
  conditions that are "often impractically strong".
- **§5.** Relations: the L² distance between kernel density estimates is
  a biased MMD under a convolved kernel; energy distance and distance
  covariance are MMD and HSIC with distance-induced kernels (Sejdinovic et
  al.); a Gaussian-process reading gives μ_P = E[f(x)f(·)] for f ∼ GP(0,k).
- **§6.1.** "How to choose the 'right' kernel function remains an
  ultimate problem." The review has no result for kernels or feature maps
  learned from data. Its kernel choice is selection, such as test-power
  maximization (Gretton et al. 2012b).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Bounded evaluation plus Riesz gives the reproducing kernel | strong | Def. 2.4, Thm 2.4, Prop. 2.1 |
| C2 | If E√k(X,X) < ∞, μ_P exists in H and represents expectation | strong | Lemma 3.1, proved in the text |
| C3 | MMD over the RKHS unit ball equals ‖μ_P − μ_Q‖, and separates distributions iff k is characteristic | strong | eq. 3.29 with Def. 3.2; standard, cited |
| C4 | HSIC is ‖C_XY‖²_HS and vanishes iff independence when the product kernel is characteristic | strong | §3.6, argued from §3.2 |
| C5 | The conditional mean embedding C_YX C_XX⁻¹ need not exist without strong conditions, so a regularized form is used | strong | Remark 4.1, with the Gaussian-kernel counterexample |
| C6 | The empirical embedding converges at n^(−1/2) for bounded kernels, minimax | strong | Thm 3.4, cited from Tolstikhin et al. |

## Concepts

- **Kernel mean embedding.** μ_P = ∫k(x,·)dP(x) ∈ H, a Bochner integral.
- **Characteristic kernel.** One for which P ↦ μ_P is injective. A
  property of the kernel and the class of distributions.
- **Universal kernel.** H dense in C_b(X) on compact X. Universal implies
  characteristic, but not the converse.
- **Cross-covariance operator.** C_YX: H → G with ⟨g, C_YX f⟩ = E[g(Y)f(X)]
  (uncentred) or Cov[g(Y), f(X)] (centred).
- **Conditional mean embedding.** An operator H → G, not an element: for
  each x it returns U_(Y|x), the embedding of P(Y|X = x).

## Connections

The review follows Berlinet & Thomas-Agnan (2004, ch. 4) for the
measure-theoretic presentation and Smola et al. (2007) for the embedding.
It credits characteristic kernels to Fukumizu et al. (2004) and
Sriperumbudur et al. (2008–2011), MMD to Borgwardt et al. and Gretton et
al., HSIC to Gretton et al. (2005), and conditional embeddings to Song et
al. (2009) and Fukumizu et al. (2013). Li et al.'s SSL-HSIC ([LIT-248](../literature.d/LIT-248.md))
applies §3.5–3.6 with image identities as labels. The review's remark on
Jegelka et al. already has MMD maximization as dependence maximization.
The RKHS chain it states (Def. 2.4 → Riesz → k_x) is the same one Jorgensen
& Tian state as Def. 11.1 and Claim 11.2 ([LIT-259](../literature.d/LIT-259.md)).

## Bearing on the record

- **[THEORY-003](../theory.d/THEORY-003.md): the Muandet half is confirmed.**
  - Def. 2.4, Thm 2.4, Prop. 2.1, Lemma 3.1 with its condition
    E_P√k(X,X) < ∞, Def. 3.2 and §3.5 say what [THEORY-003](../theory.d/THEORY-003.md) says they say.
  - Lemma 3.1 is proved in the review, not only cited, and credited to
    Smola et al. (2007).
  - So this half of [THEORY-003](../theory.d/THEORY-003.md)'s promote_when ("confirming ... the lemma
    with [its] integrability conditions") is met.
  - One wording point. [THEORY-003](../theory.d/THEORY-003.md) says "MMD is then a norm". Eq. 3.29 says
    MMD equals the RKHS norm of μ_P − μ_Q. As a distance on distributions
    it is a metric only for a characteristic kernel.
- **[THEORY-009](../theory.d/THEORY-009.md) overstates what the review says about Riesz.**
  - [THEORY-009](../theory.d/THEORY-009.md) says Riesz "is what makes a kernel mean embedding exist",
    citing Lemma 3.1. The review does prove existence by Riesz.
  - But it also defines μ_P as a Bochner integral (eq. 1.1 and eq. 3.11).
    The same condition, E‖k(X,·)‖ = E√k(X,X) < ∞, is the standard
    criterion for Bochner integrability, and a Bochner integral commutes
    with bounded linear functionals, which gives E_P f = ⟨f, μ_P⟩ directly.
    That second route is the record's inference; the review does not
    write it out.
  - So the review shows that Riesz suffices, not that it is needed.
    [THEORY-009](../theory.d/THEORY-009.md) should say "the review obtains it by Riesz".
- **[THEORY-005](../theory.d/THEORY-005.md): two pointers.**
  - The review's §3.2 closing remark (C_XX on L²(P_X) coincides with T_k)
    and Theorem 3.2 are the RKHS-side versions of [THEORY-005](../theory.d/THEORY-005.md)'s operator on
    L²(p). The conditional mean embedding of §4 is the
    conditional-expectation operator restricted to an RKHS.
  - Remark 4.1 records that this restriction "may not exist in the
    continuous domain" without strong conditions. That is a reason
    [THEORY-005](../theory.d/THEORY-005.md) works on L²(p) and not on an RKHS. Nothing in the review
    states [THEORY-005](../theory.d/THEORY-005.md)'s χ² condition.
- **[QUESTION-052](../questions.d/QUESTION-052.md).** The review offers the signature's discrimination
  criterion: a characteristic kernel makes μ_P a complete description of
  a kind's distribution. Its §4 conditional operator is defined for any
  joint law, symmetric or not. It does not discuss singular functions.
- **For the anthology.** The applications in §§3.4–4.8 (testing,
  distribution regression, kernel Bayes, MDPs) carry ML practice, which is
  why [LIT-260](../literature.d/LIT-260.md) carries `anthology-candidate`. The theory used here does not.

## Limitations

- A survey: proofs are sketched or cited. Of the statements used here,
  only Lemma 3.1 and Prop. 2.1's derivation are argued in full in the text.
- Every result assumes a fixed kernel. Nothing covers kernels induced by
  learned features. §6.1 names kernel choice as open.
- The review's Theorem 3.3 says V_YX maps "H → F" where G is meant. The
  review itself records that Kanagawa & Fukumizu (2014), Theorem 1, which
  it summarizes in §3.8.1, is wrong.

## Open questions

- Under what conditions on a learned feature map does injectivity of
  P ↦ μ_P survive, and does it matter for the per-image distributions of
  [LIT-248](../literature.d/LIT-248.md)?
- Is there a statement of the conditional mean embedding's spectrum, its
  singular values as an operator H → G, that would connect §4 to the
  singular-function results the record holds for directed pairs
  ([QUESTION-052](../questions.d/QUESTION-052.md))?
