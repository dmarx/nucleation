---
number: 9
status: Skimmed
formerly:
- NOTE-tmpb47ly
paper: LIT-011
title: 'Spectral Sets'
version: 1
date: '2026-09-25'
summary: >-
  A set X is (K-)spectral for a matrix A when ‖f(A)‖ ≤ K·sup_X|f| for all rational f bounded on X; the survey collects when common sets qualify, e.g. the numerical range is always a complete K-spectral set with a universal K (Crouzeix: K ∈ [2, 11.08]), and gives the consequences for bounding matrix functions.
---

<!-- inactive-ok-file: LIT-011 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-25 -->

# NOTE-009: Spectral Sets

## Contribution

This is a survey chapter on von Neumann's spectral and K-spectral sets, a tool for bounding the norm of a function of a matrix by the sup-norm of the function on a set. Examples include the numerical range and pseudospectra. Such bounds matter across numerical linear algebra, functional analysis and numerical analysis, including semigroups, time discretization of evolution equations and GMRES convergence. The topic ties together linear algebra, operator theory, approximation theory and complex analysis.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- Sections: matrices and operators; basic properties; around the von Neumann inequality; multidimensional von Neumann inequality; dilations, complete bounds and similarity problems; intersections of (K-)spectral sets; numerical range as a K-spectral set; applications to approximate computation of matrix functions (§107.1-107.8).
- The spectrum σ(A) is K-spectral iff A is diagonalisable, with K the eigenvector condition number; no finite set is K-spectral for a non-diagonalisable matrix (§107.2, Facts 5).
- Normal/Hermitian/unitary A are characterised by σ(A), R or T being spectral (§107.2, Fact 6).
- The closure of the ε-pseudospectrum is K-spectral with K depending on its boundary length (§107.2, Fact 7).
- Numerical range: Delyon-Delyon 1999 gave a shape-dependent K; Crouzeix 2007 gave a universal K ∈ [2, 11.08]; 2×2 matrices are completely 2-spectral (§107.7).

## Open questions

- As a handbook chapter it is a reference, not an argument. Check whether the constants have improved since 2013 (Crouzeix's conjecture that K = 2; Crouzeix-Palencia 2017 gave 1+√2, per general knowledge that was not verified in this session).
- ML link (modest, real): bounds on ‖f(A)‖ for non-normal A matter for analysing matrix-function approximations (Krylov, polynomial preconditioning) and for stability of linear recurrences such as state-space model or RNN transition matrices. The chapter makes none of these connections itself.
- It sits oddly in a "quantum" cluster; the owner's interest may be in operator theory or the von Neumann inequality.
