---
number: 842
status: Proposed
formerly:
- CLAIM-tmpu6t8z
title: 'Spectral dimension, not width, sets order'
statement: >-
  If a representation's collective deformations have a local Gaussian
  elastic energy on an interaction graph of spectral dimension d_s, their
  long-wavelength fluctuations diverge for d_s at or below 2, so whether
  conventional order survives is set by the spectral dimension of the
  interaction geometry, not by layer width
version: 2
history:
- version: 2
  date: '2026-11-22'
  note: >-
    Edited in place on 2026-11-22 after Mermin and Wagner (LIT-2985) was
    found Unavailable and read through three neighbours, Kosterlitz and
    Thouless (LIT-2969) through two, and Toner and Tu (LIT-2970) read: the
    graph version is held in the literature as Cassi's theorem (1992),
    after Hattori, Hattori and Watanabe (1987), both registered; a section
    states the conditions the theorem needs and its exceptions, and the
    worked case where non-equilibrium terms remove the 2D logarithm
    (ARG-200). The claim stays supposed; its status is unchanged.
role: supposed
warrant: demonstrated
tags:
- representation-learning
- complex-systems
- mathematics
date: '2026-11-21'
line:
- learned-structure
bears_on:
- QUESTION-515
uses:
- TERM-136
grounds:
- THEORY-2047
- THEORY-2051
- LIT-2985
- THEORY-2194
- THEORY-2195
- LIT-3061
- LIT-3051
summary: >-
  A29 §6 of the exchange "Rich Get Richer Power Laws" (2026-11-21):
  equipartition over the Laplace modes of an interaction graph whose
  eigenvalue density goes as λ^(d_s/2 − 1) makes the mean-square
  deformation diverge at small λ for d_s ≤ 2, the lower critical dimension
  of the Mermin–Wagner theorem read on a learned manifold. Supposed: every
  premise (a local elastic energy, equilibrium fluctuations, a chosen
  graph) is assumed, not derived from training. Read through neighbours
  on 2026-11-22, the graph version is a theorem for spin models in
  equilibrium (Cassi 1992, after Hattori, Hattori and Watanabe 1987),
  with conditions and exceptions this claim's premises do not meet. The
  wording is A's (the
  other assistant in the exchange "Rich Get Richer Power Laws", A29);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: LIT-2969 — Unfetched; Kosterlitz and Thouless, read through neighbours -->
<!-- inactive-ok-file: THEORY-2194 THEORY-2195 THEORY-2203 THEORY-2199 NOTE-2295 ARG-200 LIT-3061 LIT-3051 — Proposed, Skimmed, Deferred or new; the readings of 2026-11-22, the works registered from them and the argument on this claim -->
<!-- inactive-ok-file: TERM-136 CLAIM-798 THEORY-2047 THEORY-2051 THEORY-1272 — new and Proposed, filed from the exchange "Rich Get Richer Power Laws" on 2026-11-21; Deferred works registered from that exchange and not read; Proposed entries the record already held, cited for context -->
<!-- inactive-ok-file: LIT-2985 until 2027-05-22 — Unavailable; Mermin and Wagner, read through Halperin, Gelfert and Nolting, and Nachtergaele -->

# CLAIM-842: Spectral dimension, not width, sets order

## The claim

A29 §6 supposes a collective deformation field u on the learned manifold M
with energy F[u] = (κ/2)∫_M ‖∇_M u‖² dV. Expanding u in the eigenfunctions
of the Laplace–Beltrami operator, −Δ_M φ_n = λ_n φ_n, gives
F = (κ/2)Σ λ_n |a_n|², and for "equilibrium-like Gaussian fluctuations"
⟨|a_n|²⟩ ∝ T_eff/(κ λ_n), the spin-wave spectrum. If the small-eigenvalue
density goes as ρ(λ) ∝ λ^(d_s/2 − 1), which defines the spectral dimension
d_s of the interaction geometry ([TERM-136](../terms.d/TERM-136.md)), then

⟨u²⟩ ∼ ∫_0^Λ ρ(λ)/λ dλ ∼ ∫_0^Λ λ^(d_s/2 − 2) dλ,

which diverges at the lower limit for d_s ≤ 2, logarithmically at d_s = 2.
"That's the same lower-critical-dimensional phenomenon we encountered in the
XY model": the Mermin–Wagner theorem ([LIT-2985](../literature.d/LIT-2985.md), Unavailable, read
through neighbours), read on the learned interaction graph. The reading
on a graph is not Mermin and Wagner's own result but Cassi's (below).

The conclusion A29 draws: "A high ambient dimension does not tell us whether
the representation has these fluctuation properties." A 4,096-wide layer
whose interactions live on a graph of low spectral dimension can still have
strong long-wavelength fluctuations; "the governing collective dimension may
be neither the neural layer width nor even the manifold's ordinary intrinsic
dimension, but the effective spectral dimension of the network-mediated
interactions" (A29 §12).

The integral is checked: for ρ(λ) = λ^(d_s/2 − 1) on (0, 1] the integral of
ρ/λ is finite, 1/(d_s/2 − 1), exactly when d_s > 2.

## Why it is only supposed

The filing found these premises assumed, not derived (they are A29's own
caveats, made sharper):

- **The elastic energy.** No continuous symmetry that a trained
  representation breaks is identified, and the field u is never defined, so
  there is no Goldstone mode for the spectrum to describe. A29 itself: "the
  existence of such an elastic description must be derived or justified
  from the training dynamics".
- **Equilibrium.** T_eff presumes a fluctuation–dissipation relation, which
  A29 §4 doubts for training.
- **Which graph.** d_s is a property of a graph's Laplacian, and A29 does
  not say which: a k-nearest-neighbour graph of the embeddings, the kernel
  K_ij of [CLAIM-798](CLAIM-798.md), or the data's adjacency. The criterion d_s ≤ 2 depends on
  the choice. The record's held spectral dimension of SGD's drift
  ([THEORY-1272](../theory.d/THEORY-1272.md)) is a fourth, different object.
- **Zero modes.** A29: "not every near-zero eigenmode represents a physical
  Goldstone mode. Some can be artifacts of parameter redundancy, arbitrary
  rotations of embedding coordinates, or weakly constrained features."

## What the record holds

[THEORY-2047](../theory.d/THEORY-2047.md) (Laplacian eigenmaps) holds the graph Laplacian's low modes as an
embedding; [THEORY-2051](../theory.d/THEORY-2051.md) holds a symmetry-broken phase with Goldstone-type
behaviour in equivariant deep networks at initialisation. Neither holds the
fluctuation criterion.

## Where the theorem is held, and its limits

*Added 2026-11-22, after the neighbours of Mermin and Wagner were read
([ARG-200](../arguments.d/ARG-200.md)).*

**The graph version exists.** As Gelfert and Nolting report it
([LIT-3057](../literature.d/LIT-3057.md), [THEORY-2194](../theory.d/THEORY-2194.md), §3.4), Cassi (1992, [LIT-3061](../literature.d/LIT-3061.md)) applied
Hattori, Hattori and Watanabe's Gaussian field theory on general
networks (1987, [LIT-3051](../literature.d/LIT-3051.md)) to show that on fractal and disordered
lattices "whose spectral dimension is less or equal to 2", "at finite
temperature no spontaneous magnetization can exist for the classical
O(n) and the ferromagnetic (quantum) Heisenberg model", from "the
infrared divergencies displayed by the corresponding Gaussian models".
Hattori et al.'s premise, that "the only geometrical structure that spins
can feel is the one given by the Hamiltonian", is A29's point that the
governing dimension is the interaction graph's. Nachtergaele's proof
([LIT-3050](../literature.d/LIT-3050.md), [THEORY-2195](../theory.d/THEORY-2195.md)) needs no translation invariance. Both
originals are registered and unread; the record holds them at second
hand.

**What the theorem needs** (Halperin, [LIT-3054](../literature.d/LIT-3054.md), [THEORY-2203](../theory.d/THEORY-2203.md),
which `bounds` this claim):

- a continuous symmetry of the Hamiltonian whose generator is a sum of
  local generators: orientational order in a 2D crystal escapes, since
  "the generator of these rotations cannot be written as an unweighted
  sum of local operators" (§II). The first caveat above, no identified
  symmetry, is this condition unmet;
- equilibrium: the inequality "follows directly from the quantum version
  of the fluctuation dissipation theorem" (§III). The second caveat is
  this condition unmet;
- finite second moments of the couplings: ferromagnetic couplings falling
  "slower than 1/r⁴" can restore order (§II). On an interaction graph,
  long edges are the analogue.

**Where the Gaussian divergence is not the answer.**

- In tethered membranes the Gaussian fluctuations of the normal diverge,
  but nonlinear coupling renormalizes the bending constant, "which
  removes the divergence" (Halperin §II): order survives where the
  Gaussian criterion predicts its loss.
- In Toner and Tu's flock ([LIT-2970](../literature.d/LIT-2970.md), [THEORY-2199](../theory.d/THEORY-2199.md), which `bounds` this
  claim) the linear theory has this claim's divergence, logarithmic in
  d = 2, and the non-equilibrium convective terms remove it, giving true
  long-range order. Relaxing the equilibrium premise can reverse the
  conclusion.
- At d_s = 2 exactly, the XY case shows that what survives can be
  algebraic order, decided by defects that no Gaussian elastic energy
  contains: the spin-wave energy alone "is perfectly analytic" and has no
  transition (Drouin-Touchette, [NOTE-2295](../notes.d/NOTE-2295.md)). A learned-manifold
  analogue would need its defects identified.

So the criterion's mathematics is a held theorem for spin models with a
continuous symmetry in equilibrium; its application to a trained
representation remains supposed, for the reasons in "Why it is only
supposed".

