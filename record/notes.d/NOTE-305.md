---
number: 305
status: Read
formerly:
- NOTE-tmpv9x5v
paper: LIT-329
title: 'Die Vollständigkeit der primitiven Darstellungen einer geschlossenen kontinuierlichen Gruppe'
version: 1
history:
- version: 1
  date: '2026-09-29'
  note: >-
    Read in full (The full paper, *Mathematische Annalen* 97, pp. 737–755,
    from the Göttingen Digitisation Centre (GDZ) scan, image-only. I read
    all 19 pages in the German original from page images: §1 (foundations,
    orthogonality relations), §2 (Bessel's inequality, setting up the
    problem), §3 (construction of the representation belonging to the
    highest eigenvalue of a group function), §4 (splitting the
    representation obtained), §5 (iteration, proof of the completeness
    relation), §6 (expansion theorem, approximation theorem, applications),
    and footnotes 1–6. Nothing was skipped. The summary below is in English
    and the quotations are my translations unless given in German.). The
    first NOTE on this paper, which was seeded from its abstract alone.
date: '2026-09-29'
summary: >-
  For a "closed continuous group", a compact Lie group with invariant
  volume, the Fundamentalsatz (p. 752) proves the Parseval equality over
  all inequivalent irreducible representations E = (e_ik) of order n. It
  is n Σ_{i,k} |α_ik|² + … = V ∫ |x(s)|² ds for every *continuous* x, with
  α_ik = ∫ x ē_ik ds. For continuous class functions it reads |α|² + … = V
  ∫ |x|² ds with α = ∫ x χ̄ ds. The proof applies Hilbert–Schmidt theory
  to the convolution kernel z(st⁻¹), z = x x̃. The consequences are that
  finite combinations of matrix coefficients uniformly approximate every
  continuous function (Approximationssatz), that representations separate
  points (Satz I), and that characters separate conjugacy classes (Satz
  II).
---

# NOTE-305: Die Vollständigkeit der primitiven Darstellungen einer geschlossenen kontinuierlichen Gruppe

## Contribution

Schur's orthogonality relations (extended to continuous groups by integration) show that the matrix coefficients of inequivalent irreducible representations form an orthogonal system on the group manifold, with ∫ e_ik ē_ικ ds = V/n δ_iι δ_kκ (eq. 7). The paper proves that this system is *complete*. The method is constructive: the irreducible representations occurring in an arbitrary continuous function are *produced* as eigenspaces of the Hermitian convolution kernel z(st⁻¹), z = x x̃, using E. Schmidt's 1905 iteration method. The completeness relation then becomes the integral-equation fact that a kernel's trace equals the sum of its eigenvalues (p. 743). The paper derives from it:

- the expansion theorem (convolutions have uniformly convergent Fourier series in matrix coefficients);
- the approximation theorem (matrix coefficients uniformly dense in the continuous functions);
- the class-function versions (characters);
- two separation theorems (I, II).

## Key insight

Functions on a compact group form an algebra under convolution. A continuous function x gives a compact self-adjoint (Hermitian) operator z = x x̃. Its eigenspaces are invariant under right translation, because the kernel depends only on st⁻¹, so each eigenspace *is* a finite-dimensional representation. Spectral theory for integral operators thus both manufactures the irreducible representations and proves that nothing is left over. Finite groups do not need this, because they have a unit "1" in the group algebra. Continuous groups lack one, and the fix is an approximate identity 1_ν (p. 752).

## Assumptions

- **The group.** 𝔊 is a closed continuous group whose infinitesimal elements form an r-parameter linear family (Lie). It carries a volume measure ds invariant under left and right translation and inversion, which is proved for compact groups via |det Ad| = 1 (§1.1). The total volume is V = ∫ ds.
- **Representation of order n.** It is a continuous assignment s ↦ E(s), n×n, with E(st) = E(s)E(t) (eq. 2). One may restrict to E(o) = 1.
- **Functions.** Continuous functions on 𝔊 ("Gruppenzahlen"). The approximation argument uses uniform continuity, via the compactness of 𝔊.

## Key results

- **§1.4, unitarity.** Every representation with E(o) = 1 is equivalent to a unitary one, by averaging the Hermitian unit form over the group (eqs. 3–5).
- **Orthogonality relations.** For inequivalent irreducibles, ∫ e_ik(s) e′_κι(s⁻¹) ds = 0 (eq. 6). Within one irreducible, eq. 7 holds (Schur's lemma). "The components of the various inequivalent irreducible representations E(s) thus form a unitary-orthogonal function system on the manifold 𝔊" (p. 740, italic). For characters, eq. 8: ∫ χ χ̄′ = 0 and ∫ χ χ̄ = V.
- **Bessel's inequalities (§2).** With A(x) = ∫ x(s) Ē(s) ds and α(x) = Sp A(x) = ∫ x χ̄ ds: n Σ|α_ik(x)|² + … ≤ V ∫|x|² ds, and |α(x)|² + … ≤ V ∫|x|² ds. "Completeness" means equality in the first always, and in the second for class functions.
- **Group algebra.** Multiplication is xy(s) = ∫ x(sr⁻¹) y(r) dr, the adjoint is x̃(s) = x̄(s⁻¹), and the trace is S(x) = V·x(o). The Fourier map is multiplicative: A(xy) = A(x)A(y). For a class function x, A(x) = (α(x)/n)·1.
- **§3, construction.** Iterating z = x x̃, the ratios of traces σ_ν/σ_{ν−1} increase to the largest eigenvalue γ. z^ν/γ^ν converges uniformly to an idempotent e (ze = ez = γe, ee = e), with e(st⁻¹) = Σ_{i=1}^n φ_i(s) φ̄_i(t) (eq. 13). The φ_i transform among themselves under s ↦ st⁻¹ by a unitary representation Ē(t) of order n (eq. 14), and A(z) ≠ 0 for it.
- **§4, reduction.** Via "characteristic units" f(st⁻¹) = Σ λ_ik φ_i(s) φ̄_k(t) (eq. 16), E splits into irreducible blocks. The orthogonality relations (18) are re-derived for the blocks, and e_ip e_qk = δ_pq (V/n) e_ik (eq. 19). The bilinear form Σ λ_ik φ_i(s) φ̄_k(t) depends only on st⁻¹ iff Λ commutes with all E(s) (eq. 20).
- **§5, completeness.** Subtracting the constructed components and iterating gives z^(p) with ∫|z^(p)|² ≤ γ^(p−1) ≤ V/p (eq. 23). Equicontinuity then gives uniform convergence of z^(p) → 0, with the explicit remainder estimate |z^(p)(s)| ≤ 2ε once p > V/(ε² V_ε). At s = o this gives n Sp(A(x)A(x̃)) + … = S(x x̃) (eq. 24).
- **Fundamentalsatz (p. 752, italic, translated).** "If for every irreducible representation E(s) = ‖e_ik(s)‖ (i, k = 1, …, n) and its character χ(s) one forms the Fourier coefficients α_ik = ∫ x(s) ē_ik(s) ds, α = ∫ x(s) χ̄(s) ds, then n Σ_{i,k} |α_ik|² + … = V·∫|x(s)|² ds for every continuous function, and |α|² + … = V·∫|x(s)|² ds for every continuous class function x(s). The sums on the left extend over all inequivalent irreducible representations."
- **Approximate identity (p. 752).** 1_ν ≥ 0, supported in shrinking neighbourhoods of o, with integral 1. A(1_ν) → 1, so every irreducible representation occurs in some 1_ν.
- **§6, Entwicklungssatz.** For u(s) = ∫ x(st⁻¹) y(t) dt, V·u(s) = n Σ α_ik(u) e_ik(s) + …, converging uniformly. It contains S(xy) = n Sp(A(x)A(y)) + ….
- **§6, Approximationssatz (italic, translated).** "Every continuous function x(s) on 𝔊 can be uniformly approximated by a finite sum Σ β_ik e_ik(s) + … in which only components of irreducible representations occur for which the Fourier coefficient A(x) of x does not vanish." For class functions: "every continuous class function can be approximated to any degree by a finite linear combination of those primitive characters χ for which ∫ x χ̄ ds ≠ 0" (p. 754). This uses 1*_ν, class-averaged.
- **Satz I (p. 754).** If E(s₀) = E(t₀) for all irreducible representations, then s₀ = t₀.
- **Satz II (p. 754).** If χ(s₀) = χ(t₀) for all primitive characters, then s₀ and t₀ are conjugate. The proof uses the approximation theorem and closedness.
- **Closing remarks (p. 755).** The results matter for semisimple groups via the "unitary restriction" to a compact simply connected 𝔊_u (footnote 6). Bohr's almost-periodic functions are "the first example of the character theory of a truly open group", and the authors hope to return to them.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Every representation of a compact Lie group is equivalent to a unitary one | proof | §1.4 (averaging) |
| C2 | Matrix coefficients of inequivalent irreducibles are orthogonal with norms V/n | proof (Schur's method, integrated) | §1, eqs. 6–7; re-derived constructively in §4, eq. 18 |
| C3 | Parseval equality over all irreducibles for every continuous function, and via characters for continuous class functions | proof | Fundamentalsatz, §§3–5 (Schmidt iteration, eq. 23 remainder estimate) |
| C4 | Matrix coefficients are uniformly dense in continuous functions; characters in continuous class functions | proof | §6, Approximationssatz |
| C5 | Irreducible representations separate points; characters separate conjugacy classes | proof | §6, Sätze I and II |
| C6 | The method extends to open groups (almost-periodic functions) | informal (cites Weyl, Math. Ann. 97 p. 338ff.) | §2 end, §6 end |

## Method

Integral-equation (Hilbert–Schmidt/Schmidt) spectral theory applied to convolution kernels on the group; an approximate identity; averaging over the invariant measure.

## Concepts

- **Primitive (irreducible) representation; Charakteristik (character).**
- **Gruppenzahl.** A function on 𝔊 in the convolution algebra.
- **Kerne von der Form k(s, t) = x(st⁻¹).** Right-invariant kernels.
- **Charakteristische Einheit.** A kernel f(st⁻¹) that is a bilinear form in the eigenfunctions.
- **Klassenfunktion.** A function constant on conjugacy classes.

## Connections

- **[LIT-333](../literature.d/LIT-333.md) (Pontryagin).** For compact *abelian* groups every irreducible is one-dimensional, so Peter–Weyl's completeness says the characters are complete. Pontryagin's 1934 paper uses this, citing Peter–Weyl and von Neumann, as the input for duality.
- **[LIT-305](../literature.d/LIT-305.md) (Kondor & Trivedi) and [LIT-314](../literature.d/LIT-314.md), [LIT-319](../literature.d/LIT-319.md) (equivariance / geometric DL).** Generalised convolution on compact groups is diagonalised by the Peter–Weyl Fourier transform A(x). The paper's multiplicativity A(xy) = A(x)A(y) is exactly the convolution theorem those works use.
- **[LIT-300](../literature.d/LIT-300.md) (Walsh).** Walsh's closure theorem is, in hindsight, completeness of characters for the compact abelian group (ℤ/2)^ℕ. That group is not a Lie group, so it lies *outside* this paper's hypotheses.
- **[LIT-309](../literature.d/LIT-309.md), [LIT-331](../literature.d/LIT-331.md) (Wedderburn/Artin).** The eigenspace/idempotent construction (e, e_ik with e_ip e_qk = δ_pq (V/n) e_ik) is the matrix-unit structure of a simple algebra. It is the continuous analogue of the group algebra being a direct sum of full matrix algebras. The paper does not draw this connection.

## Bearing on the record

- **Map row 7, "predicate harmonics = characters; irrep multiplets = spectral degeneracies".** Peter–Weyl supplies two things.
  - *Harmonic analysis.* Completeness of matrix coefficients (and of characters for class functions) on a compact Lie group. That is what licenses expanding any continuous "predicate" x on a symmetry group into harmonics.
  - *Multiplets.* §3 shows that the eigenspaces of any invariant kernel z(st⁻¹) carry representations. That is the precise sense in which "irrep multiplets = spectral degeneracies": an eigenvalue γ of a group-invariant Hermitian operator has an eigenspace that is a representation, with multiplicity at least the irreducible's dimension n. The multiplicity can exceed n, since several copies occur and are split by §4's reduction.
  - *The paper's own phrasing.* It states that the degenerate eigenspace of the kernel carries the representation (§§3–4). It does not state the converse diagnostic, "degeneracy implies symmetry". That inference, needed for "detect symmetry via spectral degeneracy", is the owner's, and it is not valid in general, since accidental degeneracies exist.
- **Scope caveat for the owner.** The theorem needs a compact group with invariant measure acting. A trained embedding space has no given group. The detection proposal requires first positing or estimating one.
- **ML practice.** Nothing directly. It is the mathematical basis of group-equivariant networks, which the Anthology would cite through [LIT-314](../literature.d/LIT-314.md), [LIT-305](../literature.d/LIT-305.md) or [LIT-319](../literature.d/LIT-319.md), not this paper.

## Limitations

- **Compact Lie groups only**, as hypothesised. Arbitrary compact groups are not treated (they came later, via Haar measure, 1933).
- **Continuous functions, with no L² statement.** The L² completeness follows by density of the continuous functions, but it is not stated.
- **Irreducibility of the split blocks.** It is proved via the orthogonality relations (18). The argument is compressed in places, e.g. "by linear combination of f and its iterates one can crystallise out" the unit e′.

## Open questions

- The paper's own: extension to open groups (almost-periodic functions, Bohr). For the record: whether the owner's "symmetry detection" has a group to apply this to.

## Corrections to the seeded skim

- Seeded from metadata; the text shows the summary is right in substance but its framing is modern. (1) The group is assumed to be a closed (compact) continuous group to which "Lie's infinitesimal concepts" apply, i.e. a compact Lie group (§1.1), not an arbitrary compact group. (2) Completeness is proved as a Parseval equality for *continuous* functions, plus uniform approximation of continuous functions by matrix coefficients. The paper does not use "L²(G)", does not state a decomposition into isotypic components, and does not speak of "unitary" representations as an assumption (every representation is shown to be equivalent to a unitary one, §1.4).
- Terminology: "primitive Darstellung" = irreducible representation (§1.2). "Charakteristik" = character. "Gruppenzahl" = a function on the group, with convolution as multiplication (§2).
- The paper was received 24 July 1926 and published in volume 97 (1927). The authors are F. Peter (Karlsruhe) and H. Weyl (Zürich). Footnote 3 says the programme and result were already announced in Weyl's "Darstellung kontinuierlicher halbeinfacher Gruppen" III (Math. Z. 24, p. 390).
