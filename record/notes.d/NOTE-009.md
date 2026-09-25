---
number: 9
status: Read
formerly:
- NOTE-tmpb47ly
paper: LIT-011
title: 'Spectral Sets'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (full text of arXiv:1302.0546v1 (3 Feb 2013), 26 PDF pp.,
    extracted with PyMuPDF into raw4/1302.0546.txt (no pdftotext on this
    host). Read line by line: the preamble; §107.1–107.8 in full, every
    Definition, Fact, Example and Open Problem; and the reference list (pp.
    22–26). Figure 107.1, the six two-disk configurations, came through only
    as its labels. Crossref confirms the published chapter: "Spectral Sets",
    Badea & Beckermann, Handbook of Linear Algebra, 2nd ed., pp. 613–638,
    DOI 10.1201/b16113-41, print date 2013-12-05.). Upgraded from `Skimmed`
    to `Read`: the claims table, assumptions and results are new, and the
    skim is corrected where the full text disagreed.
date: '2026-09-25'
summary: >-
  A survey of when a set X ⊃ σ(A) satisfies ‖f(A)‖ ≤ K sup_X|f| for all
  rational f. Its headline entries are that the closure of the numerical
  range is completely K-spectral with a universal K_Crouzeix ∈ [2, 11.08]
  (Fact 107.7.2a; completely 2-spectral for 2×2, Fact 107.7.2b) and that
  σ(A) is K-spectral iff A is diagonalisable, with K the eigenvector
  condition number (Example 107.2.5). §107.8 turns these into Krylov error
  bounds such as Arnoldi ε_m ≤ 2K_Crouzeix ρ_{m−1}(f,E) for convex E ⊃
  W(A).
---

# NOTE-009: Spectral Sets

## Contribution

The chapter is a structured survey, not a research paper. It collects in handbook format (Definitions / Facts / Examples / Open Problems) the modern theory of spectral and K-spectral sets for Hilbert-space operators and matrices:
- basic properties and characterisations (§107.2);
- variations of von Neumann's inequality, including Banach-space and constrained versions (§107.3);
- multivariable von Neumann inequalities and their failure for n ≥ 3 (§107.4);
- dilations, complete bounds and similarity to contractions (§107.5);
- intersections of (K-)spectral sets and the annulus problem (§107.6);
- the numerical range as a K-spectral set (§107.7);
- applications to computing and bounding matrix functions and Krylov methods (§107.8).

The only result it presents as new is the improved annulus lower bound in Example 107.6.2.

## Key insight

For a normal matrix, ‖f(A)‖ = max over the spectrum of |f|. For a non-normal matrix the spectrum is the wrong set: it is not even K-spectral unless A is diagonalisable, and then K is the eigenvector condition number. The right move is to enlarge the set until the constant is controlled. The numerical range W(A) is the canonical choice. It is always K-spectral with a universal K ≤ 11.08 (conjecturally 2), so any polynomial or rational approximation error of f on a convex set E ⊃ W(A) transfers to the matrix at the cost of at most that constant (§107.8).

## Assumptions

- **Setting:**
  - A is a bounded operator on a complex Hilbert space H, or a matrix on ℂⁿ with the Euclidean norm, unless a Fact says otherwise;
  - X is closed with σ(A) ⊂ X;
  - f ranges over rational functions with poles off X (R(X)), and f(A) is defined by the Riesz functional calculus (§107.2).
- **Hilbert-space dependence:** von Neumann's inequality characterises Hilbert spaces (Fact 107.3.1). Banach-space versions carry worse constants: 3 for Banach contractions (Fact 107.2.12), and (πn+1) for subordinate matrix norms (Fact 107.3.3).
- **§107.8:**
  - E is compact and convex, K(E)-spectral for A, and f is analytic on E;
  - the Faber-based bounds need the conformal map φ of the exterior of E;
  - the Padé bounds are for Markov functions f(z) = c + ∫ dμ(x)/(z−x) with β < −w(A), and some also need E symmetric about ℝ.

## Key results

Theorem-level entries as the chapter states them, all attributed to the literature.

- **Disk and half-plane von Neumann inequalities** (Fact 107.2.1):
  - {|z−α| ≤ r} is spectral iff ‖A−αI‖ ≤ r;
  - a closed half-plane is spectral iff it contains W(A).
- **Spectrum** (Example 107.2.5): σ(A) is K-spectral iff A is diagonalisable, with K ≤ cond(V) for V the eigenvector matrix. No finite set is K-spectral for a non-diagonalisable matrix.
- **Pseudospectrum** (Example 107.2.7): the closure of the ε-pseudospectrum is K-spectral with K = length(∂X)/(2πε).
- **Numerical-radius disk** (Example 107.2.8): {|z| ≤ w(A)} is 2-spectral, and 2 is best possible.
- **Class C_s** (Fact 107.2.10): the unit disk is K-spectral for A ∈ C_s, with best constant K = max(1, s) ([OA75]).
- **Banach contractions** (Fact 107.2.12): ‖p(A)‖ ≤ sup_{|z|≤3}|p(z)|, and 3 is sharp.
- **Bohr** (Fact 107.3.4a): ‖p(rS)‖_{L(ℓ¹)} ≤ ‖p‖_D iff r ≤ 1/3.
- **Multivariable** (§107.4):
  - holds for commuting pairs (Andô) and for Σ‖A_j‖² ≤ 1 (Brehmer);
  - fails for n = 3 with 5×5 matrices (Varopoulos, Example 107.4.2);
  - explicit 8×8 counterexample with ‖p(A)‖ ≥ 4 > ‖p‖_{𝕋³} (Crabb–Davie, Example 107.4.3);
  - whether a finite C_n exists is open (Dixon), with C_n growing faster than any power of n if it does.
- **Dilation and similarity** (§107.5):
  - Arveson: a normal ∂X-dilation exists iff X is completely spectral;
  - Paulsen: A is similar to a contraction iff D is completely K-spectral;
  - Pisier: a polynomially bounded operator not similar to a contraction;
  - Peller/Bourgain: for M = sup‖Aⁿ‖, ‖p(A)‖ ≤ M²(log d)‖p‖_D;
  - Bourgain: a matrix with ‖f(A)‖ ≤ C‖f‖_D is similar to a contraction with ‖L⁻¹‖‖L‖ ≤ K C⁴ log(n+1).
- **Intersections of spectral disks** (Fact 107.6.4, [BBC09]):
  - n spectral disks intersect in a complete K-spectral set with K ≤ n + n(n−1)/√3;
  - the convex case gives 11.08;
  - for n = 2, K = 2 + 2/√3.
- **Annulus X(R) = {R⁻¹ ≤ |z| ≤ R}, for ‖A‖, ‖A⁻¹‖ ≤ R** (Fact 107.6.5):
  - Shields: K(R) ≤ 2 + √((R²+1)/(R²−1));
  - [BBC09]: K_cb(R) ≤ 2 + (R+1)/√(R²+R+1) ≤ 2 + 2/√3;
  - K(R) ≤ 3 for R ≥ 2.0953;
  - Crouzeix 2012 gives an integral bound;
  - lower bound: K(R) ≥ 4/3 ([BBC09]), improved in Example 107.6.2 to > 3/2.
- **Numerical range, shape-dependent constants** (Fact 107.7.1): every compact convex X ⊃ W(A) is completely K-spectral with
  - K = 3 + (2π diam(X)²/area(X))³ (Delyon–Delyon 1999);
  - K = 1 + 2/(1−q(X)) (Putinar–Sandberg), where q(X) is Neumann's configuration constant;
  - K = 2 + π + TV(log r) (Badea–Crouzeix–Delyon).
- **Numerical range, universal constant** (Fact 107.7.2a, [Cro07, Theorem 1]): K_Crouzeix ∈ [2, 11.08] such that the closure of W(A) is complete K-spectral for every bounded A. For 2×2 matrices, W(A) is completely 2-spectral (Fact 107.7.2b).
- **Numerical range, special shapes** (Example 107.7.3):
  - sector, strip, parabola and hyperbola: 2 + 2/√3;
  - ellipse with eccentricity e: 2 + 2/√(4−e²);
  - equilateral triangle: 2 + π + 6 log 2;
  - square: 2 + π + 4 log 2.
- **Drury** (Fact 107.7.3d): w(A) ≤ 1 implies w(f(A)) ≤ (5/4)‖f‖_D, and 5/4 is best.
- **Crouzeix's conjecture:** known to hold for generalised Jordan blocks with a scalar in the lower-left entry (Example 107.7.5, [GC12]).
- **Applications** (§107.8):
  - Faber-sum error: ‖(f − p_m)(A)‖ ≤ 2 Σ_{j>m} |f_j| ([BR09]), since the Faber operator satisfies ‖F(F)(A)‖ ≤ 2 max_D|F| ([Bec05]);
  - Arnoldi f(A)b error: ε_m ≤ 2K_Crouzeix ρ_{m−1}(f,E) or ε_m ≤ 4 Σ_{j≥m}|f_j|;
  - GMRES residual: ‖r_m‖/‖r_0‖ ≤ min{1, 2/|F_m(0)|} ≤ (2 + 1/|φ(0)|)/|φ(0)|^m;
  - for positive-definite A + A* (lens E), the convergence factor is 1/|φ(0)| = 2 sin(β/(4−2β/π)) < sin β, with cos β = dist(0, W(A))/w(A);
  - FOM error: ≤ 4|φ(0)|^{−m}/dist(0, E).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | σ(A) is K-spectral iff A is diagonalisable (K = eigenvector condition number) | strong | proof sketched in Examples 107.2.3–107.2.5 |
| C2 | A is normal / Hermitian / unitary iff σ(A) / ℝ / 𝕋 is spectral | strong | converse proved in Example 107.2.6 via Möbius maps and Lagrange interpolation |
| C3 | The closure of W(A) is a complete K-spectral set with a universal K ∈ [2, 11.08] | strong (as report) | cites [Cro07, Thm 1]; no proof in the chapter |
| C4 | For 2×2 matrices, K = 2 is attained and suffices (completely) | strong (as report) | cites [Cro04a, Thm 1.1]; Example 107.7.7 shows 2 is attained |
| C5 | Spectral and completely spectral constants for W(A) can differ (3×3 example) | weak–moderate | Example 107.7.4, sourced to "personal communication" [Cro12b]; no proof given |
| C6 | The annulus X(R) is not 3/2-spectral for the explicit 2×2 A, for any R > 1 | strong | explicit computation in Example 107.6.2; checkable by hand |
| C7 | The multivariable von Neumann inequality fails for n = 3 | strong | explicit counterexamples (Examples 107.4.2–107.4.3), from [Var74, CD75] |
| C8 | Arnoldi and GMRES errors are bounded by polynomial/Faber approximation errors on E ⊃ W(A), times at most 2K_Crouzeix or 4 | strong (as report) | [Bec05, BR09] |
| C9 | Is K_Crouzeix = 2 (even for 3×3)? | open problem | Open Problem 107.7.1 |

## Concepts

- **(K-)spectral set** — a closed X ⊃ σ(A) with ‖f(A)‖ ≤ K‖f‖_X for all f ∈ R(X). "Spectral" means K = 1.
- **Complete K-spectral set** — the same inequality for all matrices (f_ij) of rational functions, in the operator norm on ⊕ⁿH. It is equivalent to X being completely spectral for some B similar to A with ‖L⁻¹‖‖L‖ ≤ K (Fact 107.5.2).
- **Numerical range / numerical radius** — W(A) = {⟨Ax,x⟩ : ‖x‖ = 1} and w(A) = sup|W(A)|, with ‖A‖/2 ≤ w(A) ≤ ‖A‖.
- **Class C_s (Sz.-Nagy–Foias)** — operators with a unitary s-dilation. C₁ is the contractions; C₂ is the numerical-radius contractions.
- **Normal ∂X-dilation** — A = P_H f(N)|_H with N normal and σ(N) ⊂ ∂X.
- **Faber polynomials / Faber operator** — the polynomial parts of φᵐ at ∞, for φ the exterior conformal map of E. The operator carries F on D to Σ f_j F_j.

## Connections

The chapter:
- builds on von Neumann's 1951 paper;
- organises the Sz.-Nagy–Foias dilation theory, the Arveson/Paulsen complete-boundedness framework and the Pisier counterexample around the single notion of a K-spectral set;
- ties the numerical-range line (Delyon–Delyon 1999 → Crouzeix 2004/2007 → the Badea–Beckermann–Crouzeix lens/sector/annulus work) to Krylov-method error analysis (Beckermann 2005; Beckermann–Reichel 2009).

Both authors are among the contributors to the results it reports (BBC09, BC02, BC06, BC07, Bec05, BR09).

## Bearing on the record

No THEORY document in this record rests on it, and it contradicts none. It is a reference for any future note that needs a norm bound on a function of a non-normal matrix.

For ML practice it carries no instruction, and the chapter mentions no ML. The anthology practice closest in subject is [ANTH-SOTA-011](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/practices.d/SOTA-011.md): extreme Hessian eigenvalues by Lanczos on Hessian-vector products. It works with a symmetric Hessian, which is normal, so σ(A) is already a spectral set (Fact 107.2.6) and the chapter's non-normal machinery adds nothing there. Where the chapter would matter is analysing non-normal linear recurrences or Krylov approximations of f(A)b for non-symmetric A. Those settings would call for its §107.7–107.8 bounds; no anthology document currently makes such a claim.

## Limitations

- **A survey with almost no proofs.** Apart from the short arguments in §107.2's Examples and the Example 107.6.2 computation, every Fact is cited, and its support is the cited paper.
- **One entry rests on unpublished support.** Example 107.7.4 is sourced to a personal communication.
- **Frozen at early 2013.** In particular, the upper bound 11.08 in Fact 107.7.2a is no longer the best known. I recall Crouzeix–Palencia (2017) proving 1 + √2, but did not verify it in this session. Whether Crouzeix's conjecture K = 2 has since been settled was not checked.
- **Uneven scope of the application bounds.** The §107.8 bounds need E convex and containing W(A). When W(A) contains or nearly contains 0, which can happen for indefinite or highly non-normal A, the GMRES and FOM bounds become vacuous: 1/|φ(0)| → 1.

## Open questions

As listed in the chapter, with what would close each.

- **Is K_Crouzeix = 2, even for 3×3 matrices?** (Open Problem 107.7.1.) Closed by a proof of the 2 bound, or a matrix exceeding it.
- **Does a finite C_n exist with ‖f(A₁,…,A_n)‖ ≤ C_n‖f‖_{D^n} for all commuting contractions?** (Open Problem 107.4.1, Dixon.) It is believed not.
- **What obstructs commuting unitary dilations of commuting contraction n-tuples?** (Open Problem 107.5.1.)
- **Is the intersection of two K-spectral sets K′-spectral in general?** (§107.6 preamble.) It is known when the boundaries are disjoint (Fact 107.6.1).
- **What is the optimal annulus constant K(R)?** Currently between > 3/2 (Example 107.6.2) and the upper bounds of Fact 107.6.5.

## Corrections to the seeded skim

- **Several dossier locators are wrong: most of the §107.2 items it cites are Examples, not Facts.**
  - "σ(A) is K-spectral iff A is diagonalisable" is Example 107.2.5, with the proof sketched there. It is not "Facts 5". Fact 107.2.5 is Williams' existence of minimal spectral sets.
  - The characterisations of normal, Hermitian and unitary A by σ(A), ℝ and 𝕋 being spectral are Fact 107.2.9(a)–(c), with the converse proved in Example 107.2.6. Fact 107.2.6 is only von Neumann's "A normal ⇒ σ(A) is a (minimal) spectral set".
  - The pseudospectrum result is Example 107.2.7, K = length(∂X)/(2πε), cross-referred to Fact 16.3.5 of the Handbook. It is not Fact 7. Fact 107.2.7 is Williams' criterion using functions vanishing at an interior point.
- **The dossier's definition drops a condition.** K-spectrality also requires σ(A) ⊂ X (§107.2, Definitions), not just the norm inequality.
- **The chapter contains one result it presents as new, which the dossier misses.** Example 107.6.2 gives the lower bound K(R) ≥ 2(1+R²+R)/(1+R²+2R) > 3/2 for the annulus X(R) = {R⁻¹ ≤ |z| ≤ R}. It uses f(z) = g(z) − g(1/z), g(z) = R(z−1)/(R²−z), on A = [[1, R−1/R],[0,1]]. The chapter notes that this improves the lower bound K(R) ≥ 4/3 of Fact 107.6.5c ([BBC09]). The computation is explicit and checkable.
- **The constant 11.08 appears twice, for two different results.** Fact 107.7.2a (Crouzeix 2007) gives it for the numerical range. Fact 107.6.4a gives it for convex intersections of spectral disks. The dossier cites only the first.
- **Spectral and completely spectral constants can differ.** Example 107.7.4 (Crouzeix, personal communication) gives a 3×3 matrix whose W(A) is 2-spectral but *not completely* 2-spectral. This limits how far the 2×2 result (Fact 107.7.2b) can be read as evidence for K = 2 in the complete sense. The dossier's "2×2 matrices are completely 2-spectral" is correct but omits this example.
- The dossier's section list, Delyon–Delyon, the Crouzeix interval [2, 11.08] and the §107.8 applications check out. The dossier's "ML link (SSM/RNN transition matrices, Krylov)" is its own inference; the chapter makes no such connection.
