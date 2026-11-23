---
number: 481
status: Active
formerly:
- CLAIM-tmpywecm
title: 'Coupling does not by itself separate time scales: two identical undamped oscillators coupled with stiffness k have normal modes at ω₀ and √(ω₀² + 2k), nearly equal when k ≪ ω₀², and neither decays; separation comes where the coupling dissipates relative differences faster than collective ones, as in ẋ = −ax − k(x − y), ẏ = −ay − k(y − x), whose collective and relative modes relax at rates a and a + 2k, and in a Laplacian flow ẋ = −κLx, where the spectrum of L sets the rates'
version: 4
history:
- version: 2
  date: '2026-11-11'
  note: >-
    Stale text corrected, from the ninth synthesis review of
    2026-11-11: the body called Spivak (LIT-1649) unread, though
    it is read in NOTE-1225 and cited so further down, and the
    inactive-ok comment called LIT-1639 Deferred where it is
    Unfetched (a lawful full text found on 2026-10-27, not
    fetched). Both now say what the record holds. No other change.
- version: 3
  date: '2026-11-11'
  note: >-
    From the by-topic reading review of 2026-11-11, at the status
    review's ruling (the owner delegated these rulings; ADR-058).
    LIT-1659 and LIT-1649 leave grounds. The claim proves its own
    case: its section "Checked" rederives the modal decay of a
    Laplacian flow and the other reductions. Hansen and Ghrist
    (LIT-1659) are cited for the Laplacian flow's convergence, and
    Spivak (LIT-1649) for A22's gloss "the same relational
    organization need not imply the same temporal hierarchy"; both
    are parallels, and their readings THEORY-1070 and THEORY-1054
    already corroborate this claim. The body keeps both citations.
    The text is unchanged.
- version: 4
  date: '2026-11-23'
  note: >-
    Joins the work governance-of-possibility (ADR-144) at its
    membership pass of 2026-11-23, under ADR-104's rule: the revised
    manuscript in scratch/manuscripts/governance-of-possibility/ states
    its proposition or uses it as a step, in §3.1. No other change.
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
- CLAIM-473
complements:
- CLAIM-478
- CLAIM-521
- CLAIM-626
summary: >-
  The answer A20, A21 and A23 gave to the owner's conjecture at U20 that
  coupling necessarily induces scale separation ([CLAIM-473](CLAIM-473.md)). Two
  small computations: conservative coupling splits modes without
  separating or damping them, and dissipative coupling damps the relative
  mode at a rate that grows with the coupling. For a Laplacian flow the
  kernel is exact compatibility and the nonzero spectrum is the hierarchy
  of relaxation rates, so a spectral gap is where the separation comes
  from. Conceded, so Active. It gives a mechanism for [CLAIM-478](CLAIM-478.md)'s
  second half and is not a test of individuality.
works:
- governance-of-possibility
---
<!-- inactive-ok-file: THEORY-2291 — Proposed; readings of LEAD-094's batch, 2026-11-22 -->
<!-- inactive-ok-file: THEORY-2012 THEORY-2018 THEORY-2033 THEORY-2043 THEORY-2047 — Proposed; cited in this filing of 2026-11-19 -->
<!-- inactive-ok-file: CLAIM-762 — Proposed; cited in this filing of 2026-11-19 -->
<!-- inactive-ok-file: CLAIM-473 CLAIM-478 CLAIM-157 — Rejected or Proposed; the conjecture this answers and the claims it serves -->
<!-- inactive-ok-file: LIT-1639 — Unfetched; registered from the exchange, a lawful full text found on 2026-10-27 but not fetched, unread, cited for what it is standardly cited for -->

# CLAIM-481: Coupling does not by itself separate time scales: two identical undamped oscillators coupled with stiffness k have normal modes at ω₀ and √(ω₀² + 2k), nearly equal when k ≪ ω₀², and neither decays; separation comes where the coupling dissipates relative differences faster than collective ones, as in ẋ = −ax − k(x − y), ẏ = −ay − k(y − x), whose collective and relative modes relax at rates a and a + 2k, and in a Laplacian flow ẋ = −κLx, where the spectrum of L sets the rates

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
separation, and [CLAIM-473](CLAIM-473.md) is false as stated.

A22 §6 made the same point in port-Hamiltonian form. An ideal power-conserving
interconnection ([LIT-1639](../literature.d/LIT-1639.md)) "can sustain oscillations indefinitely". And it
cited Spivak ([LIT-1649](../literature.d/LIT-1649.md), since read in [NOTE-1225](../notes.d/NOTE-1225.md)) for one networked potential that admits a
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
the sheaf Laplacian δ*δ of [CLAIM-471](CLAIM-471.md)), each eigenmode decays as
e^{−κλ_j t}. The kernel of L is the exactly compatible configurations, and the
nonzero eigenvalues are the rates at which incompatible variations are
suppressed (A21 §3; Hansen and Ghrist, [LIT-1659](../literature.d/LIT-1659.md)). A spectral gap is a
separation of time scales. Two cases A21 and A22 worked out:

- **Two clusters.** Units 1–2 and 3–4 are coupled internally with strength K
  and joined by a bridge of strength ε ≪ K. The Laplacian has a zero mode,
  one eigenvalue of order ε and the rest of order K. Over 1/(κK) ≪ t ≪
  1/(κε) the four units are described by two cluster averages, and at
  longer times by one. A21: "the **effective decomposition of a coupled system
  changes with observation timescale**." That window is [CLAIM-478](CLAIM-478.md)'s and
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

- **Hansen and Ghrist** ([NOTE-1233](../notes.d/NOTE-1233.md), Prop. 8.1, p. 34) prove that
  ẋ = −Δx converges exponentially to the orthogonal projection onto the
  kernel, each eigencomponent decaying at its own eigenvalue. The words
  "relaxation rate" and "separation of time scales" are this claim's, not
  theirs. The projection depends on the stalk weights. The two-cluster and
  chain computations are not in the paper; they are A21's and A22's,
  rechecked here.
- **Spivak** ([NOTE-1225](../notes.d/NOTE-1225.md); [THEORY-1054](../theory.d/THEORY-1054.md)) is cited in the body for "the
  same relational organization need not imply the same temporal hierarchy".
  That phrase is A22's gloss. What the paper shows is that one harmonic
  arrangement gives the discrete wave equation when the integrator stores
  momentum, and the heat equation when it does not, with the same wiring,
  potential and response (Prop. 7.4.1, Remark 7.4.2). So the coupling data
  underdetermine whether relative modes decay. The difference lies in a
  modeller's choice of semantics, which is this claim's condition seen from
  the other side.
- **Torres-Hugas et al.** ([NOTE-1218](../notes.d/NOTE-1218.md)): under nonzero holonomy the twisted
  Laplacian has no kernel, and its least eigenvalue is a floor of
  incompatibility, not the first rate above a collective mode. For the
  nonlinear Sakaguchi–Kuramoto dynamics, stability is set by the Jacobian,
  not by that spectrum. This is a worked case of the claim's exclusion of
  nonlinear coupling.
- **Stewart, Golubitsky and Pivato** ([NOTE-1217](../notes.d/NOTE-1217.md)) support only "invariant
  without being attracting" (p. 626), and as a scope statement rather than
  a result.

## Note of 2026-11-19: the exchange "Topological protection explained"

A26 §6 put a general form of this claim's dissipative case: "A dynamical process can make an equivalence relation approximately true by dissipating the differences that violate it." The owner, at U12, on that sentence: "reminds me of self supervised learning". The connection is recorded as the owner's.

A27 §2 made it concrete. The alignment energy tr(ZᵀLZ), minimized by gradient flow, gives Laplacian diffusion of the representations along the edges that assert equivalence. That is consensus dynamics of this claim's kind: relative differences across an edge decay and the components of the graph survive. The SSL equivalence is held as [LIT-228](../literature.d/LIT-228.md) (contrastive and non-contrastive methods as spectral embeddings) and [LIT-249](../literature.d/LIT-249.md) (spectral contrastive loss). A27 §2 kept a limit: augmentation graphs may at first connect only views of the same instance, so classes across instances need further assumptions. A27 §2 also noted that pure diffusion collapses each component, so non-collapse terms are needed for an informative representation.

Whether such collapse is how the classes become reified distinctions is the owner's U10 thesis, [CLAIM-762](CLAIM-762.md). No status change.

## Note of 2026-11-19: readings for the exchange "Topological protection explained"

These readings bear on the note of 2026-11-19 above, the reading of self-supervised alignment as Laplacian diffusion, not on the claim's computations, which stand demonstrated.

Bardes, Ponce and LeCun's VICReg ([THEORY-2012](../theory.d/THEORY-2012.md)), read: in the ablation (Appendix D.4, Table 7) the invariance term alone, the alignment energy the note reads as diffusion, sends every input to one vector, and the covariance term "has no repulsive effect preventing collapse". Only the variance hinge holds the spread. That bears out A27's remark that pure diffusion collapses, and leaves the claim as it is.

Belkin and Niyogi ([THEORY-2047](../theory.d/THEORY-2047.md)), read, have the energy and the collapse the note needs: minimizing Σ(y_i − y_j)²W_ij alone gives the constant vector, "which collapses all vertices of G onto the real number 1", and their constraints exist to stop it; a disconnected graph is embedded component by component. They study no flow, so reading the minimization as dissipation is the record's step. It qualifies the note.

Zbontar and colleagues' Barlow Twins ([THEORY-2018](../theory.d/THEORY-2018.md)), read, prevent collapse by decorrelating units standardized over the batch, not by a spectral constraint. Their ablation (Table 5) gives the decorrelation term alone 0.1% linear accuracy, and invariance with batch standardization alone 57.3%, so part of the anti-collapse work is done by the standardization. That qualifies the note: non-collapse terms differ in kind.

Wang and Isola ([THEORY-2033](../theory.d/THEORY-2033.md)), read, prove the split for the contrastive case: with many negatives InfoNCE is an alignment term plus a uniformity term, and with alignment weighted far above uniformity every input goes to one vector (§5). The anti-collapse term is a repulsion toward the uniform measure, and nothing is said of diffusion along a graph. It qualifies the note.

Lohmiller and Slotine ([THEORY-2043](../theory.d/THEORY-2043.md)), read: full contraction sends all trajectories to one, and "A convex contraction region contains at most one equilibrium point". Contraction that keeps distinctions appears only in two remarks of §3.9. The selective contraction A29 invoked is Wang and Slotine's later partial contraction, which the record does not hold. It leaves the claim open on that point.

No status change.

## Note of 2026-11-19: Wang and Slotine, read
<!-- inactive-ok-file: THEORY-2044 — Proposed; cited from the readings of 2026-11-19 -->

Wang and Slotine ([THEORY-2044](../theory.d/THEORY-2044.md), corroborates; [NOTE-2096](../notes.d/NOTE-2096.md)), read: the partial contraction the note of 2026-11-19 said the record did not hold. Three bearings.

- **The dissipative-coupling case, generalized.** For identical nonlinear units with symmetric positive-definite diffusive coupling on a connected graph, the relative modes contract once the coupling, through λm+1 of the weighted Laplacian, beats the units' own expansion rate (Theorem 6). The chain's eigenvalue 2(1 − cos(π/n)) appears as a synchronization threshold, and "the effort to synchronize an open chain network is four times of that to a closed one" (Ex. 4.5): the claim's chain computation, read as a threshold.
- **The bullet on nonlinear coupling.** For positive-definite diffusive coupling, strong enough coupling always gives global synchrony; destabilization by strong coupling belongs to semi-definite coupling without contraction of the coupled block (§4.4.3, after Pecora). Ex. 4.2 shows a synchronous set that is "both an invariant set and a linear constraint" and attracts.
- **Selective contraction.** Partial contraction erases differences transverse to a manifold and keeps what lies along it: "the common phase of the steady states is determined by the initial conditions" (p. 7). It needs no rate comparison between within-class and between-class variation. The point the earlier note left open now has its source.

No status change.

## Note of 2026-11-22: Ott and Antonsen, read

A parallel, no edge. In the Kuramoto model with Lorentzian frequencies of
width Δ ([NOTE-2385](../notes.d/NOTE-2385.md), eq. 10) coupling slows the collective mode: its
damping rate is Δ − K/2 below locking and goes to zero at Kc = 2Δ, while
the approach to the reduced law is bounded below by Δ ([NOTE-2378](../notes.d/NOTE-2378.md)). So
there coupling makes a separation only near threshold, by bringing a mode
to an instability, which is [CLAIM-478](CLAIM-478.md)'s second half rather than this
claim's dissipative splitting of collective and relative modes; far from
threshold it makes none. Consistent with this claim: coupling does not by
itself separate time scales.

## Note of 2026-11-22 (later): Caprioglio and Berthouze, read

A parallel, no edge. In their hierarchically modular networks
([THEORY-2291](../theory.d/THEORY-2291.md)) the gaps between time scales come from the Laplacian
spectrum of the network's modular structure, the mechanism this claim gives
for a Laplacian flow, and the authors use the gaps to explain which states
appear in which layer.
