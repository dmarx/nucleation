---
status: Read
paper: LIT-330
title: 'The approximation of one matrix by another of lower rank'
version: 1
history:
- version: 1
  date: '2026-09-29'
  note: >-
    Read in full (The full paper, *Psychometrika* 1(3), September 1936, pp.
    211–218, from the Internet Archive's scan of the issue. *Psychometrika*
    has no copyright renewals on record, so the scan is in the US public
    domain. I read all eight pages from the page images, including the
    abstract, the introduction, "Some preliminary theorems and remarks",
    "Solution of the problem", "Concerning a hypothetical interpretation of
    the canonic components of β", and all footnotes. Nothing was skipped. I
    checked the bound l(1−r/R)^{1/2} and the error formula myself.). The
    first NOTE on this paper, which was seeded from its abstract alone.
date: '2026-09-29'
summary: >-
  For a real n×N matrix a, the rank-r matrix β nearest in the
  least-squares (Frobenius) distance is obtained by writing a = u′λU (u, U
  orthogonal, λ diagonal ≥ 0, "Theorem I") and zeroing all but the r
  largest diagonal elements. The solution is unique unless λ_r = λ_{r+1}.
  The squared error is Σ_{i>r} λ_i², so the error is at most
  l(1−r/R)^{1/2}, with l the length of a and R its rank. The paper also
  argues that the resulting canonic components cannot straightforwardly be
  read as psychological factors.
---

# NOTE-tmpqnm9t: The approximation of one matrix by another of lower rank

## Contribution

Factor theory postulates that an n×N score matrix (n tests, N individuals) is well approximated by a matrix of lower rank r. The paper turns this into a least-squares problem: find the rank-r β minimising the distance from a. It solves the problem in closed form via the canonic (singular-value) resolution. The result is to keep the r largest canonical multipliers and zero the rest. The paper derives the minimal error and an a-priori bound on it, and shows that the best approximation of the score matrix gives the best approximations of both correlation matrices, aa′ and a′a. The last section examines whether canonic components can be read as factors, and concludes that the straightforward reading is "not a tenable interpretation" (pp. 217–218).

## Key insight

The distance is invariant under orthogonal transformations on either side, (uaU′, uβU′) = (a, β) (eq. 9). Once β is written in canonic form, the only free coordinates that matter are its multipliers. A stationarity argument then forces the optimal β to share a's singular vectors. The problem collapses to choosing r of the diagonal entries: minimise Σ(λ_i − μ_i)² with only r of the μ_i non-zero, whose answer is obvious.

## Assumptions

- **Real matrices.** a is n×N with real entries; n = N is allowed.
- **The criterion.** The criterion is the least-squares one: every element has equal weight. The scalar product is (a, β) = Σ_ij a_ij β_ij (eq. 1), the "length" is l² = (a, a), and the distance is the length of a − β.
- **The rank constraint.** β is required to have rank r, with r < min(n, N). a has rank R > r.
- **Theorems I and II.** Both are assumed from the literature (Courant–Hilbert 1924; MacDuffee 1933), not proved.
- **Existence of the minimiser.** The derivation assumes a minimiser exists, and that at it the first variation along orthogonal increments δu = us, with s skew-symmetric (eq. 13), vanishes.

## Key results

- **Theorem I (p. 213, verbatim).** "For any real matrix a, two orthogonal matrices u and U can be found so that λ = uaU′ is a real diagonal matrix with no negative elements." Equivalently a = u′λU (eq. 10), or a = u′vω with ωω′ = 1_n (eq. 10.1).
- **How to compute it.** u and v² come from diagonalising aa′, and ω = v⁻¹ua when v is invertible (pp. 213–214). "The multipliers and characteristic values of a correlational matrix are identical" (p. 214).
- **Theorem II (p. 214, verbatim).** "If aβ′ and β′a are both symmetric matrices, then and only then can two orthogonal matrices u and U be found such that λ = uaU′ and μ = uβU′ are both real diagonal matrices." It is presented as generalising "the principal axes of two symmetric matrices coincide if and only if ab = ba".
- **The stationarity step (p. 215).** Write β = u′μU. Varying u gives 0 = −(aβ′, s) for every skew s (eq. 15), so aβ′ is symmetric. Varying U likewise makes β′a symmetric. By Theorem II, a and β are simultaneously diagonal, and x² = Σ_i (λ_i − μ_i)² (eq. 11.1).
- **The solution (p. 216, eq. 17).** With λ₁ ≥ λ₂ ≥ …, take μ_i = λ_i for i ≤ r and μ_i = 0 for i > r. "This is also the only solution unless λ_r = λ_{r+1}."
- **The error (p. 216).** The minimum of x² is Σ_{i=r+1}^R λ_i². Hence, "if l is the length of a, the smallest upper bound for x is l(1−r/R)^{1/2}". I checked this: the R−r smallest of R squares sum to at most (R−r)/R of their total, with equality when all multipliers are equal.
- **The correlation-matrix corollary (p. 216).** If β is the best rank-r approximation to a, then ββ′ is the best rank-r approximation to aa′, and β′β to a′a. The proof is "readily supplied from the foregoing results" and is not written out.
- **The interpretation section (pp. 216–218).** Canonic component ρ is the n+N+1 numbers (u_ρp, λ_ρ, U_ρi), with β_pi = Σ_ρ u_ρp λ_ρ U_ρi (eq. 19). Reading N^{1/2}U_ρi as individual i's ability and n^{1/2}u_ρp as test p's demand for factor ρ is tested against two populations sharing the same u-matrix. There, λ_ρ² = λ_ρ,I² + λ_ρ,II² (eq. 20). This would fit λ² as variances, but that is "not a tenable interpretation … because of the symmetric manner in which the individuals and the tests enter". The authors suggest instead that λ_ρ,I²/nN_I is the product of the variance of individuals and the variance of tests. They note that scores are measured from a common fiducial zero, not centred.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Every real matrix has a canonic resolution a = u′λU, with u, U orthogonal and λ diagonal ≥ 0 | cited, not proved | Theorem I, p. 213; Courant–Hilbert |
| C2 | Two matrices are simultaneously diagonalisable by one orthogonal pair iff aβ′ and β′a are symmetric | cited, not proved | Theorem II, p. 214 |
| C3 | The best rank-r least-squares approximation keeps the r largest multipliers | proof (first-order, assuming a minimiser exists) | eqs. 11–17; stationarity along skew increments, then Theorem II |
| C4 | The solution is unique unless λ_r = λ_{r+1} | proof sketch | p. 216, from eq. 11.1 |
| C5 | The minimal squared error is Σ_{i>r} λ_i², and x ≤ l(1−r/R)^{1/2} | proof | p. 216; checked |
| C6 | The best approximation of the score matrix gives the best approximations of both correlation matrices | asserted ("proof readily supplied") | p. 216 |
| C7 | Canonic components cannot directly be read as factors with λ² as variances | informal argument | pp. 217–218, the two-population thought experiment |

## Method

Orthogonal invariance of the Frobenius inner product; first-order conditions on the orthogonal group via skew-symmetric increments; a cited simultaneous-SVD theorem; reduction to a separable problem on diagonal entries.

## Concepts

- **Canonic resolution.** The SVD, a = u′λU.
- **Canonical multipliers.** Singular values (Sylvester's term).
- **Canonic component.** A triple (row of u, multiplier, row of U).
- **Length, span.** The Frobenius norm and its square.

## Connections

- **[THEORY-004](../theory.d/THEORY-004.md).** A representation is fixed by its kernel only up to an orthogonal transformation. The paper's ββ′ corollary (C6) is the matrix form of that: the best approximation of the Gram/correlation matrix aa′ is ββ′, and ββ′ determines β only up to right multiplication by an orthogonal matrix. The paper's own remark that u and U are not independent parameters (p. 215) is the same freedom.
- **[THEORY-002](../theory.d/THEORY-002.md) and [LIT-302](../literature.d/LIT-302.md) (Platonic Representation Hypothesis).** Convergence of kernels fixes representations only up to symmetry. Eckart–Young gives the low-rank truncation of the kernel, not a unique factor.
- **[LIT-250](../literature.d/LIT-250.md), [LIT-254](../literature.d/LIT-254.md).** Representation-comparison works. Truncated SVD underlies CCA/CKA-style comparisons, but this paper makes no such use.

## Bearing on the record

- **Map row 10, "owner of the unique-factorization/low-rank machinery".** Half right.
  - *What it owns.* The paper does own the low-rank machinery: best rank-r Frobenius approximation = truncation of the canonic resolution.
  - *What it does not own.* It does not own a "unique factorization". Uniqueness is proved only for the approximating *matrix* β, and only when λ_r > λ_{r+1}. The factors u, U are explicitly not unique. The paper's last section argues against reading the canonic factors as the "real" underlying factors, because tests and individuals enter symmetrically.
  - *Consequence for the map.* A Universal Convergence argument that leans on Eckart–Young for uniqueness of the *factors* (and so of representations) goes beyond what the paper proves. It supplies uniqueness of the rank-r truncation of a fixed matrix under a spectral gap, and nothing about models trained separately. This supports the map's own verdict (`AT-RISK`, "do not state it as proved").
- **ML practice.** It is foundational for PCA/low-rank methods, but the Anthology's practices would cite modern treatments. It carries nothing new for the Anthology.

## Limitations

- **Only the Frobenius/least-squares norm, and only real matrices.** The spectral-norm and general unitarily-invariant-norm versions (Mirsky 1960) are not here.
- **The optimality argument is first-order.** It assumes a minimiser exists. Existence follows from compactness of the rank ≤ r set intersected with a ball, but the paper does not say so. It treats "rank r" rather than "rank ≤ r".
- **Theorems I and II are imported without proof.**
- **Priority.** The low-rank approximation theorem was, by standard historical accounts (e.g. Stewart, "On the early history of the singular value decomposition", SIAM Review 1993), already given by E. Schmidt (1907) for integral operators. I did not check that here, and the paper does not mention it.

## Open questions

- None the paper raises. For the record, the question is only whether the owner's Universal Convergence text states a uniqueness of factors that no version of this theorem gives.

## Corrections to the seeded skim

- Seeded from metadata; the text confirms the summary. The paper does not use the words "singular value decomposition". It calls a = u′λU the "canonic resolution" and the diagonal elements of λ Sylvester's "canonical multipliers". The norm is called "length", and its square the Frobenius "span".
- The uniqueness condition belongs in the summary. The paper states the solution is "unique unless λ_r = λ_{r+1}" (p. 216). The factorisation itself (u, λ, U) is not claimed unique, and in general it is not: the remaining rows of U are arbitrary, and equal multipliers allow rotations.
- The two structure theorems it relies on (Theorem I, existence of the canonic resolution; Theorem II, simultaneous diagonalisation of a and β by one pair u, U iff aβ′ and β′a are symmetric) are stated "will not be proven here". They are cited as generalisations of Courant–Hilbert results.
- Identification: authors Carl Eckart and Gale Young, University of Chicago. The pages, volume and issue in the seed are correct.
