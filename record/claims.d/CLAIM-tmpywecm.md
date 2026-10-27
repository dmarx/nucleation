---
status: Active
title: 'Coupling does not by itself separate time scales: two identical undamped oscillators coupled with stiffness k have normal modes at ω₀ and √(ω₀² + 2k), nearly equal when k ≪ ω₀², and neither decays; separation comes where the coupling dissipates relative differences faster than collective ones, as in ẋ = −ax − k(x − y), ẏ = −ay − k(y − x), whose collective and relative modes relax at rates a and a + 2k, and in a Laplacian flow ẋ = −κLx, where the spectrum of L sets the rates'
version: 1
role: counter
warrant: demonstrated
tags:
- complex-systems
- mathematics
date: '2026-10-27'
line:
- distributed-agency
- formal-apparatus
objects_to:
- CLAIM-tmpfw510
complements:
- CLAIM-tmpmx2ql
grounds:
- LIT-tmpnpxhs
- LIT-tmpfywhk
summary: >-
  The answer A20, A21 and A23 gave to the owner's conjecture at U20 that
  coupling necessarily induces scale separation ([CLAIM-tmpfw510](CLAIM-tmpfw510.md)). Two
  small computations: conservative coupling splits modes without
  separating or damping them, and dissipative coupling damps the relative
  mode at a rate that grows with the coupling. For a Laplacian flow the
  kernel is exact compatibility and the nonzero spectrum is the hierarchy
  of relaxation rates, so a spectral gap is where the separation comes
  from. Conceded, so Active. It gives a mechanism for [CLAIM-tmpmx2ql](CLAIM-tmpmx2ql.md)'s
  second half and is not a test of individuality.
---
<!-- inactive-ok-file: CLAIM-tmpfw510 CLAIM-tmpmx2ql CLAIM-157 CLAIM-tmpdjt64 — Rejected or Proposed; the conjecture this answers and the claims it serves -->
<!-- inactive-ok-file: LIT-tmpnpxhs LIT-tmpfywhk LIT-tmp6zanw — Deferred; registered from the exchange, unread, cited for what they are standardly cited for -->

# CLAIM-tmpywecm: Coupling does not by itself separate time scales: two identical undamped oscillators coupled with stiffness k have normal modes at ω₀ and √(ω₀² + 2k), nearly equal when k ≪ ω₀², and neither decays; separation comes where the coupling dissipates relative differences faster than collective ones, as in ẋ = −ax − k(x − y), ẏ = −ay − k(y − x), whose collective and relative modes relax at rates a and a + 2k, and in a Laplacian flow ẋ = −κLx, where the spectrum of L sets the rates

## The counterexample

Take two identical oscillators of unit mass, coupled by a spring of stiffness k
(A21 §3):

ẍ₁ + ω₀²x₁ + k(x₁ − x₂) = 0,  ẍ₂ + ω₀²x₂ + k(x₂ − x₁) = 0.

With s = x₁ + x₂ and d = x₁ − x₂ the equations separate:

s̈ + ω₀²s = 0,  d̈ + (ω₀² + 2k)d = 0.

The collective mode oscillates at ω₀ and the relative mode at √(ω₀² + 2k). For
k ≪ ω₀² the two frequencies are nearly equal. Nothing is dissipated, so the
relative mode never dies away. The coupling splits the motion into normal modes
but makes no hierarchy, and the relative degree of freedom is not suppressed.
This holds for every k > 0. So coupling does not necessarily induce scale
separation, and [CLAIM-tmpfw510](CLAIM-tmpfw510.md) is false as stated.

A22 §6 made the same point in port-Hamiltonian form. An ideal power-conserving
interconnection ([LIT-tmp6zanw](../literature.d/LIT-tmp6zanw.md)) "can sustain oscillations indefinitely". And it
cited Spivak ([LIT-tmpfywhk](../literature.d/LIT-tmpfywhk.md), unread) for one networked potential that admits a
heat-like or a wave-like dynamics: "**The same relational organization need not
imply the same temporal hierarchy.**"

## When coupling does separate time scales

Make the coupling dissipative (A20 §3):

ẋ = −ax − k(x − y),  ẏ = −ay − k(y − x),  a > 0, k ≥ 0.

With u = (x + y)/2 and v = (x − y)/2:

u̇ = −au,  v̇ = −(a + 2k)v.

The collective mode relaxes on τ = 1/a, the relative one on 1/(a + 2k). For
k ≫ a the difference dies long before the collective state moves, and the
system settles onto x ≈ y. A20: "**In this precise sense, interaction has
generated an effective gluing condition and a separation of timescales
together.**"

In general, for ẋ = −κLx with L positive semidefinite (a graph Laplacian, or
the sheaf Laplacian δ*δ of [CLAIM-tmpdjt64](CLAIM-tmpdjt64.md)), each eigenmode decays as
e^{−κλ_j t}. The kernel of L is the exactly compatible configurations, and the
nonzero eigenvalues are the rates at which incompatible variations are
suppressed (A21 §3; Hansen and Ghrist, [LIT-tmpnpxhs](../literature.d/LIT-tmpnpxhs.md)). A spectral gap is a
separation of time scales. Two cases A21 and A22 worked out:

- **Two clusters.** Units 1–2 and 3–4 are coupled internally with strength K
  and joined by a bridge of strength ε ≪ K. The Laplacian has a zero mode,
  one eigenvalue of order ε and the rest of order K. Over 1/(κK) ≪ t ≪
  1/(κε) the four units are described by two cluster averages, and at
  longer times by one. A21: "the **effective decomposition of a coupled system
  changes with observation timescale**." That window is [CLAIM-tmpmx2ql](CLAIM-tmpmx2ql.md)'s and
  [CLAIM-157](CLAIM-157.md)'s.
- **A chain.** For n units coupled to their nearest neighbours, the slowest
  nonzero eigenvalue is 2(1 − cos(π/n)) ≈ π²/n², so the slowest relaxation
  time grows as n²/(κπ²). Size alone makes a slow collective mode. That is the
  diffusive scaling of hydrodynamic modes (A22 §2).

## What it does not show

- **That a gap makes an individual.** Synchrony can come from a common drive
  ([QUESTION-063](../questions.d/QUESTION-063.md)). A gap can support prediction without any organization that
  maintains itself (A23 §XIII).
- **That coupling is the only source of separation.** Conservation laws,
  metastability, critical slowing near an instability and imposed time scales
  give it too (A23 §XII).
- **Anything about nonlinear coupling.** Strong coupling can destabilize
  rather than synchronize, and a synchrony subspace can be invariant without
  being attracting (A22 §7).

## Checked

The four reductions above were rederived for this entry: the normal modes of
the conservative pair, the two rates of the dissipative pair, the modal decay
of a Laplacian flow, and the path-graph eigenvalues 2 − 2cos(πk/n),
k = 0, …, n − 1. The two-cluster spectrum was computed numerically for K = 100,
ε = 1: eigenvalues 0, 0.995, 200 and 201.0, so one of order ε and two of
order K, as A21 said; the path graph for n = 10 gave λ₂ = 0.0979 against
2(1 − cos(π/10)) = 0.0979.

## Note of 2026-10-27 (evening): the readings of the U15–U23 works

- **Hansen and Ghrist** (NOTE-tmpzqos6, Prop. 8.1, p. 34) prove that
  ẋ = −Δx converges exponentially to the orthogonal projection onto the
  kernel, each eigencomponent decaying at its own eigenvalue. The words
  "relaxation rate" and "separation of time scales" are this claim's, not
  theirs. The projection depends on the stalk weights. The two-cluster and
  chain computations are not in the paper; they are A21's and A22's,
  rechecked here.
- **Spivak** (NOTE-tmplvblh; THEORY-tmp09707) is cited in the body for "the
  same relational organization need not imply the same temporal hierarchy".
  That phrase is A22's gloss. What the paper shows is that one harmonic
  arrangement gives the discrete wave equation when the integrator stores
  momentum, and the heat equation when it does not, with the same wiring,
  potential and response (Prop. 7.4.1, Remark 7.4.2). So the coupling data
  underdetermine whether relative modes decay. The difference lies in a
  modeller's choice of semantics, which is this claim's condition seen from
  the other side.
- **Torres-Hugas et al.** (NOTE-tmpb8jge): under nonzero holonomy the twisted
  Laplacian has no kernel, and its least eigenvalue is a floor of
  incompatibility, not the first rate above a collective mode. For the
  nonlinear Sakaguchi–Kuramoto dynamics, stability is set by the Jacobian,
  not by that spectrum. This is a worked case of the claim's exclusion of
  nonlinear coupling.
- **Stewart, Golubitsky and Pivato** (NOTE-tmp4riih) support only "invariant
  without being attracting" (p. 626), and as a scope statement rather than
  a result.
