---
status: Proposed
promote_when: >-
  A reading of the full construction in Sevi, Rilling and Borgnat §8.2
  that confirms the three steps as stated here (column selection without
  orthonormalization, pseudo-inverse compression, squaring of the
  compressed operator), together with a run on a strongly connected
  directed graph that reproduces a nested chain of selected-column
  spaces and a biorthogonal transform conditioned markedly worse than
  the orthogonal one. Not satisfied by a check that the 2005 report says
  the same, which bears on the attribution, not on this account.
title: 'On a strongly connected directed graph, diffusion wavelets extend to T = Π^{1/2}PΠ^{−1/2} by selecting columns of each restricted dyadic power as a non-orthogonal basis, compressing by the pseudo-inverse and squaring, which keeps the nested chain of spaces and trades orthogonality for localization at a large cost in conditioning'
version: 1
tags:
- mathematics
- network-science
- complex-systems
date: '2026-11-23'
source:
- LIT-tmpyklac
summary: >-
  Sevi, Rilling and Borgnat (2023), [LIT-tmpyklac](../literature.d/LIT-tmpyklac.md), skimmed in [NOTE-tmpv196v](../notes.d/NOTE-tmpv196v.md),
  §8.2–8.3.1. Their critically sampled transform on directed graphs,
  which they say has the scaling functions of the 2005 biorthogonal
  report ([LIT-tmpzikaq](../literature.d/LIT-tmpzikaq.md)). The chain of spaces is nested by construction
  and the projector onto each is orthogonal; only the basis is
  non-orthogonal. It gives no error bound, does not read the levels as
  spectral bands, and reports conditioning on one example.
---
<!-- inactive-ok-file: NOTE-tmpv196v LIT-tmpzikaq — new, Unfetched and new; the reading, the report it stands in for, and the bound filed by the lead run of 2026-11-23 -->

# THEORY-tmpyi9zg: On a strongly connected directed graph, diffusion wavelets extend to T = Π^{1/2}PΠ^{−1/2} by selecting columns of each restricted dyadic power as a non-orthogonal basis, compressing by the pseudo-inverse and squaring, which keeps the nested chain of spaces and trades orthogonality for localization at a large cost in conditioning

## Source

Sevi, Rilling and Borgnat (2023), *Applied and Computational Harmonic
Analysis* 62: 390–440, [LIT-tmpyklac](../literature.d/LIT-tmpyklac.md), §8.2 (construction) and §8.3.1
(the directed cycle C₂₅₆), skimmed in [NOTE-tmpv196v](../notes.d/NOTE-tmpv196v.md). They attribute the
scaling functions to Maggioni, Bremer, Coifman and Szlam (2005),
[LIT-tmpzikaq](../literature.d/LIT-tmpzikaq.md), which the record has not read: "Our construction is
identical but we also propose a definition for wavelets."

## What was actually shown

- **The operator.** T = Π^{1/2}PΠ^{−1/2}, lazy if P has eigenvalues of
  modulus near one away from 1. It is similar to P on ℓ²(V, π) through an
  isometry (Propositions 4.4–4.5).
- **The chain.** Level 1 selects columns of T so that every column is
  well approximated in their span; they are kept as a basis Φ₁ that "is
  generally not orthogonal". T is compressed to V₁ by the pseudo-inverse,
  [T]_{Φ₁} = Φ₁^†TΦ₁; level 2 selects columns of ([T]_{Φ₁})², taken as T²
  on V₁; and so on. Since each Φ_j is written on Φ_{j−1}, the spaces are
  nested, V_j ⊂ V_{j−1}, with no use of symmetry.
- **The cost.** On C₂₅₆, biorthogonal scaling functions and wavelets are
  better localized and oscillate less than the orthogonal ones, but the
  inverse transforms have κ ≈ 2 × 10⁴ against 33.

What could have come out otherwise: the selected-column basis could have
been as well conditioned as the orthonormal one, and was not.

## What this does not say

- **Not an error bound.** "[T²]_{Φ₁} ≈ ([T]_{Φ₁})²" is unquantified. The
  bound the record files from this lead ([CLAIM-tmpdsu37](../claims.d/CLAIM-tmpdsu37.md)) supplies one, and
  shows that a directed T needs a row residual the column selection does
  not control.
- **Not that the levels are spectral bands.** For symmetric T the levels
  are spectral spaces ([THEORY-758](THEORY-758.md)). Nothing here says what a level of a
  directed walk is in the spectrum of P.
- **Not that biorthogonality changes the spaces.** The projector onto
  V_j is orthogonal however V_j's basis is chosen. Biorthogonality is a
  choice of basis inside a level, and its cost is in coordinates, not in
  which subspace is kept.
- **Not a general conditioning law.** One example.
