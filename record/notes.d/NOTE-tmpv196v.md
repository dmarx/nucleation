---
status: Skimmed
paper: LIT-tmpyklac
title: 'Sevi, Rilling and Borgnat — Harmonic analysis on directed graphs and applications'
version: 1
history:
- version: 1
  date: '2026-11-23'
  note: >-
    Read by the lead run of 2026-11-23 from arXiv 1811.11636 v3 (51
    pages, stamped 1 Nov 2021), text extracted with pdftotext. Read
    closely: §1.2 (contributions), §4.4 (the operator T and the
    isometry with ℓ²(V, π)), the opening of §5, the opening of §8, §8.2
    in full and §8.3.1. Read by headings only: §§2–3, 4.1–4.3, 6, 7, 8.1,
    8.3.2–8.3.3; figures not seen. Skimmed, because the paper is read
    here for its restatement of the biorthogonal diffusion-wavelet
    construction, which it stands in for, and not as a whole.
date: '2026-11-23'
summary: >-
  §8.2 extends diffusion wavelets to strongly connected directed graphs.
  T = Π^{1/2}PΠ^{−1/2} (lazy if needed) is represented on the Kronecker
  basis; at each level a subset of the columns of the restricted operator
  is selected and kept as a non-orthogonal basis of scaling functions;
  the operator is compressed by the pseudo-inverse and squared for the
  next level, and wavelets with dual bases come from the projector onto
  the complement. The authors say the scaling functions are those of
  the 2005 biorthogonal report. The biorthogonal transform is localized
  better and conditioned far worse (κ ≈ 2 × 10⁴ against 33). No error
  bound is given.
---
<!-- inactive-ok-file: LIT-tmpzikaq CLAIM-tmpdsu37 — Unfetched, and new; the report this reading stands in for and the bound filed from it, by the lead run of 2026-11-23 -->

# NOTE-tmpv196v: Sevi, Rilling and Borgnat — Harmonic analysis on directed graphs and applications

## Contribution

A harmonic analysis on strongly connected directed graphs whose
cornerstone is the random walk operator P. Its eigenvectors serve as a
non-orthogonal Fourier basis, with frequency read from their Dirichlet
energy. From it the paper builds a redundant spectral wavelet frame
(§8.1) and a critically sampled transform that "generaliz[es] the
framework of diffusion wavelets [22, 27] to the directed case" (§1.2).
For this record the second is the point: it is the one accessible
statement of the biorthogonal diffusion-wavelet construction, LIT-tmpzikaq.

## Key results

- **The operator (§4.4, eq. 11).** T = Π^{1/2}PΠ^{−1/2}, with Π the
  diagonal of the stationary measure. The map ϕ: f ↦ Π^{−1/2}f is an
  isometry from ℓ²(V) to ℓ²(V, π) (Proposition 4.4) and "intertwines the
  operator T on ℓ²(V) to the operator P on ℓ²(V, π)" (Proposition 4.5).
- **Which T (§8.2.3).** "In the original diffusion wavelets framework by
  Coifman and Maggioni [22], the graph is assumed undirected and they
  suggest using the reversible random walk operator P. More generally,
  any operator T can be used as long as it acts like a low-pass filter."
  Since "the highest frequency eigenvectors may have eigenvalues with
  modulus arbitrarily close to one (as e.g. for the cycle graph)", a lazy
  walk T = Π^{1/2}(γI + (1 − γ)P)Π^{−1/2} is used instead.
- **Selection, not orthonormalization (§8.2.3).** The columns of
  [T]^{Φ₀}_{Φ₀} are taken as candidate scaling functions. "The aim is to
  find a small number of columns of Φ̃₁, forming a set C such that the
  residual ‖[Φ̃₁]_{Φ₀} − Π_C[Φ̃₁]_{Φ₀}‖_β is as minimal as possible", in the
  spectral or Frobenius norm. The selected columns are kept as they are:
  "Φ₁ is by definition a basis of V₁ that is generally not orthogonal."
- **Compression and squaring (§8.2.3).** [T]^{Φ₁}_{Φ₁} =
  [I]^{Φ₁}_{Φ₀}[T]^{Φ₀}_{Φ₀}[I]^{Φ₀}_{Φ₁}, where the restriction
  [I]^{Φ₁}_{Φ₀} is the Moore–Penrose pseudo-inverse of [Φ₁]_{Φ₀} (§8.2.1).
  The next level uses T² restricted to V₁, with
  [T²]^{Φ₁}_{Φ₁} ≈ ([T]^{Φ₁}_{Φ₁})², and selects Φ₂ from its columns, and so
  on, giving V_j ⊂ V_{j−1} ⊂ ⋯ ⊂ V₁. The "≈" is not quantified.
- **Wavelets (§8.2.3).** Wavelet bases Ψ_j are columns selected from
  [I_{V_j} − Φ_{j+1}Φ_{j+1}^†]^{Φ_j}_{Φ_j}, "the orthogonal projector on the
  complement of V_{j+1} into V_j", with duals Ψ̂_j such that Ψ̂_j^†Ψ_j = I. The
  attribution: "in [36], biorthogonal wavelet transform is proposed but
  only the scaling functions are actually defined. Our construction is
  identical but we also propose a definition for wavelets."
- **Generalization (§8.2.4).** The dyadic powers T^{2^j} may be replaced by
  "more arbitrary low-pass filters" H_j.
- **The directed cycle C₂₅₆ (§8.3.1).** Six scales. Biorthogonal scaling
  functions have smaller supports than orthogonal ones, and "orthogonal
  scaling functions as well orthogonal wavelet functions have more
  oscillations than their biorthogonal counterparts". But "the
  orthogonal wavelet transform is more robust with respect to
  perturbations": the condition numbers of the inverse transforms are
  κ(W_ortho) ≈ 33 and κ(W_biortho) ≈ 2 × 10⁴.

## Assumptions

- The graph is strongly connected, so the walk is ergodic and π > 0.
- P is assumed diagonalizable for the Fourier basis (§5); the wavelet
  construction does not use this.
- T acts "like a low-pass filter". Nothing quantifies this, and nothing
  about the spectrum of T (decay, gaps) is assumed for §8.2.

## Concepts

- **Non-orthogonal scaling basis.** A basis of V_j made of selected
  columns of the restricted power, kept unorthogonalized, with a dual
  basis from the pseudo-inverse. The space V_j and the orthogonal
  projector onto it are the same whichever basis of it is used; what
  biorthogonality changes is the basis and its conditioning.
- **Column subset selection.** Choosing columns so that the residual of
  projecting all columns onto their span is small.

## Connections

It cites the 2005 biorthogonal report as [36], Coifman and Maggioni as
[22] (LIT-1256, NOTE-984) and diffusion wavelet packets as [27]. It
restates, for LIT-tmpzikaq, the scaling-function construction, by the
authors' own account of identity. It does not restate any theorem or
error statement of that report, and the record cannot tell whether the
report has one.

## Bearing on the record

- **CLAIM-164, and the bound filed by the lead run of 2026-11-23
  (CLAIM-tmpdsu37).** Background and a test case. The construction's
  subspace chain has the form the bound covers: each level is the
  orthogonal compression of a power of the previous level's operator onto
  the span of selected columns, so the projector perturbation argument
  applies whatever basis is kept. The paper gives no bound itself. Its
  unquantified [T²]_{Φ₁} ≈ ([T]_{Φ₁})² is where, for a non-symmetric T, the
  bound needs a row residual as well as the column residual that column
  selection controls.
- **NOTE-984's open question on non-reversible operators.** In part.
  The ranges of compressed dyadic powers still give a nested chain for a
  directed walk, and the paper builds one. Whether the levels can be read
  as bands is not addressed: the paper's frequency reading is through the
  eigenvectors of P (§6), and §8.2 does not connect the levels to it.
- **THEORY-758.** A contrast on one point. That account's induction
  (each level is a spectral space) uses T = Tᵀ. The directed construction
  keeps the nesting, which needs no symmetry, and gives up the spectral
  identification.

## Limitations

- **No error analysis.** The approximation [T²]_{Φ₁} ≈ ([T]_{Φ₁})² is stated
  without a bound. Written out, the difference on V₁ is
  P₁T(I − P₁)TP₁ with P₁ the orthogonal projector onto V₁, whose norm is
  at most ‖(I − P₁)TP₁‖·‖P₁T(I − P₁)‖. For symmetric T both factors are the
  selection residual; for a directed T the second is a row residual that
  selecting columns does not control. (The record's, not the paper's.)
- **‖T‖₂ ≤ 1 is not stated.** It follows from Proposition 4.5 and the
  contraction of P on ℓ²(V, π), and the record's check confirms it on a
  directed small-world walk. The paper does not use it.
- **One conditioning example.** κ ≈ 2 × 10⁴ is reported for C₂₅₆ only.
- **Attribution to [36] rests on the authors' word.** The record has not
  read [36].
