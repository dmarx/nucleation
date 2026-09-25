---
status: Deferred
status_note: seeded from the abstract and a skim on 2026-09-25; not read in full
title: 'Spectral Sets'
version: 1
tags:
- mathematics
date: '2026-09-25'
published: '2013-02-01'
arxiv: '1302.0546'
doi: '10.1201/b16113-41'
first_author: 'Badea'
keywords:
- 'spectral sets'
- 'K-spectral sets'
- 'von Neumann inequality'
- 'numerical range'
- 'matrix functions'
implementations: []
summary: >-
  Badea et al. (2013), [ARXIV-1302.0546](https://arxiv.org/abs/1302.0546). A set X is (K-)spectral for a matrix A when ‖f(A)‖ ≤ K·sup_X|f| for all rational f bounded on X; the survey collects when common sets qualify, e.g. the numerical range is always a complete K-spectral set with a universal K (Crouzeix: K ∈ [2, 11.08]), and gives the consequences for bounding matrix functions.
---

# LIT-tmpbnroa: Spectral Sets

Catalin Badea, Bernhard Beckermann (2013), *Chapter 107 in Handbook of Linear Algebra, Second Edition (L. Hogben, ed.), CRC Press, Discrete Mathematics and Its Applications (2013); also arXiv preprint* — [ARXIV-1302.0546](https://arxiv.org/abs/1302.0546)

## Key takeaways

- A set X is (K-)spectral for a matrix A when ‖f(A)‖ ≤ K·sup_X|f| for all rational f bounded on X; the survey collects when common sets qualify, e.g. the numerical range is always a complete K-spectral set with a universal K (Crouzeix: K ∈ [2, 11.08]), and gives the consequences for bounding matrix functions.

*Seeded from the abstract and a skim, not a reading. What follows is what the work says about itself.*

This is a survey chapter on von Neumann's spectral and K-spectral sets, a tool for bounding the norm of a function of a matrix by the sup-norm of the function on a set. Examples include the numerical range and pseudospectra. Such bounds matter across numerical linear algebra, functional analysis and numerical analysis, including semigroups, time discretization of evolution equations and GMRES convergence. The topic ties together linear algebra, operator theory, approximation theory and complex analysis.

## Standing in the record

Filed by the reading-time triage of 2026-09-25: 665 seconds of active reading over 4 sessions in the papers-feed tracker. `Deferred` because nobody has read it closely here yet, not on merit.

**Priority for a deeper reading: low — a reference survey that the skim indexes adequately; open the relevant fact when needed rather than read through (t=665 s).**

What a deeper reading should check:

- As a handbook chapter it is a reference, not an argument. Check whether the constants have improved since 2013 (Crouzeix's conjecture that K = 2; Crouzeix-Palencia 2017 gave 1+√2, per general knowledge that was not verified in this session).
- ML link (modest, real): bounds on ‖f(A)‖ for non-normal A matter for analysing matrix-function approximations (Krylov, polynomial preconditioning) and for stability of linear recurrences such as state-space model or RNN transition matrices. The chapter makes none of these connections itself.
- It sits oddly in a "quantum" cluster; the owner's interest may be in operator theory or the von Neumann inequality.

Access when seeded: arXiv abs page and full PDF (26 pp.) retrieved; read section list, §107.1 definitions, §107.2 facts (p. 5) and §107.7 (numerical range). The chapter DOI was found by a Crossref bibliographic search that returned title "Spectral Sets" in "Handbook of Linear Algebra, Second Edition" with authors Badea and Beckermann (online 2013-11-26); the chapter page was not opened.
