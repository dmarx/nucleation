---
number: 1369
status: Proposed
formerly:
- THEORY-tmp2e4h8
promote_when: >-
  An independent experiment or computation reproduces edge-localized
  folding in a quasi-1D origami strip at the edge, and with the decay rate
  ln κ, that the paper's formula gives; and an independent computation or
  experiment finds a localized zero mode at a domain wall between kirigami
  of different topological polarizations, and none between equal ones; and
  a proof, or a computation over periodic triangulated origami beyond the
  paper's, finds no triangulation with nonzero polarization.
title: 'Chen and colleagues show that marginally rigid origami and kirigami carry a topological polarization, so that a quasi-1D origami strip folds at the edge its pattern angles select and a domain wall between kirigami of different polarizations is flexible though constraints locally match the degrees of freedom, while periodic triangulated origami appears always to have zero polarization'
version: 2
history:
- version: 2
  date: '2026-11-11'
  note: >-
    Bears on QUESTION-383, at the reading review of 2026-11-11 (by
    question, ADR-091). The question names Chen et al. (NOTE-1624), read
    here, as a place the first-order picture breaks: extra zero modes "at
    linear order which do not extend to higher order". No other change.
tags:
- natural-sciences
- mathematics
date: '2026-11-05'
source:
- LIT-2049
summary: >-
  Chen, Liu, Evans, Paulose, Cohen, Vitelli and Santangelo (2016; arXiv
  2015), [LIT-2049](../literature.d/LIT-2049.md), read in full in [NOTE-1624](../notes.d/NOTE-1624.md). Proposed: the strip
  result has the authors' own experiment, but the domain-wall result is
  numerical and the 2D origami claim is a conjecture on numerics. It does
  not say that joining rigid parts creates freedom in general: equal
  polarizations give no wall mode, and walls of the other orientation are
  stressed lines that carry load.
bears_on:
- QUESTION-383
---

# THEORY-1369: Chen and colleagues show that marginally rigid origami and kirigami carry a topological polarization, so that a quasi-1D origami strip folds at the edge its pattern angles select and a domain wall between kirigami of different polarizations is flexible though constraints locally match the degrees of freedom, while periodic triangulated origami appears always to have zero polarization

## Source

Chen, Liu, Evans, Paulose, Cohen, Vitelli and Santangelo (2016; arXiv v1 2015-08-04), [LIT-2049](../literature.d/LIT-2049.md); read in [NOTE-1624](../notes.d/NOTE-1624.md).

## What was actually shown

- **The strip**: "As each vertex contributes a DOF and a constraint, this
  origami structure has marginal rigidity"; u(j+1) = κu(j) localizes the
  folding mode at the edge set by the sign of ln κ, and in Mylar–PLA
  strips "the decay lengths extracted from the fit are in good agreement
  with 1/l = ln κ". The fit could have failed.
- **The flat state**: "Coplanar hinges in the flat state are redundant
  constraints, and this results in extra zero modes at linear order which
  do not extend to higher order", so a second-order rigidity matrix is
  used.
- **Kirigami walls**: numerically, a wall between polarizations (1, 0) and
  (0, 0) is flexible "while keeping it rigid further away"; "a domain wall
  between distinct patterns with equal polarization has no such localized
  modes".
- **2D origami**: det R(q) real for every periodic triangulation tested,
  forcing zero polarization; "a proof of this statement for all
  triangulated origami eludes us".

## What this does not say

- That 2D triangulated origami is proved unpolarized.
- That any interface between rigid structures is flexible: it takes
  different polarizations, and the opposite orientation gives a stressed
  line.
- That the modes survive along finite folding paths.
