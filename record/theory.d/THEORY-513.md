---
number: 513
status: Active
formerly:
- THEORY-tmpeh08y
title: "Observational entropy taken relative to a maximum-entropy prior τ, S(τ) − D_M(ρ‖τ), lies between S(ρ) and S(τ) for states meeting the prior's constraint, is finite and continuous whenever S(τ) is, and reduces to about two dozen textbook entropies by choice of measurement and prior; its second laws are bounds on the time-averaged state's divergence from the prior, proved small only under sufficient conditions (nondegenerate energy gaps for equilibration, the eigenstate thermalization hypothesis for fit to the prior)"
version: 1
tags:
- information-theory
- thermodynamics
- quantum-foundations
date: '2026-10-16'
source:
- LIT-082
summary: >-
  Schindler, Strasberg, Galke, Winter & Jabbour (2025), [LIT-082](../literature.d/LIT-082.md), read in full in [NOTE-043](../notes.d/NOTE-043.md),
  with Proofs 1, 2, 7, 10 and 11 checked line by line. The bounds, the
  special cases and the decomposition are proved. The central target, a
  small divergence of the time-averaged state from the prior, is proved
  for no concrete system; in the paper's own examples "in none of those
  cases was the smallness proved here analytically" (p. 12). Unpublished
  as of the reading.
---

# THEORY-513: Observational entropy taken relative to a maximum-entropy prior τ, S(τ) − D_M(ρ‖τ), lies between S(ρ) and S(τ) for states meeting the prior's constraint, is finite and continuous whenever S(τ) is, and reduces to about two dozen textbook entropies by choice of measurement and prior; its second laws are bounds on the time-averaged state's divergence from the prior, proved small only under sufficient conditions (nondegenerate energy gaps for equilibration, the eigenstate thermalization hypothesis for fit to the prior)

## Source

Schindler, Strasberg, Galke, Winter & Jabbour (2025), "Unification of observational entropy with
maximum entropy principles", arXiv 2503.15612v1, [LIT-082](../literature.d/LIT-082.md), read in full
in [NOTE-043](../notes.d/NOTE-043.md). The simulation code was not run.

## What was actually shown

**The definition (Eqs. 10–13).** Any state τ defines a linear constraint
in informational form, S(ρ;τ) ≤ S(τ), on which τ is the MaxEnt state.
Then S^τ_M(ρ) = S(τ) − D_M(ρ‖τ) = −Σ p_x log(p_x/V_x), with prior-weighted
volumes V_x = Tr(τM_x)e^{S(τ)}.

**Bounds (Eqs. 17–18, Proof 2).** S(τ) ≥ S^τ_M(ρ) ≥ S(ρ) for ρ in the
constraint set; the upper bound is tight iff M cannot tell ρ from τ. S(τ)
is the most information any measurement can extract from a constrained
state (Proof 1, with a saturating state).

**Special cases (§V, Table II).** Twenty-four numbered items: Jaynes, von
Neumann, traditional observational entropy (τ ∝ 1), Boltzmann, Gibbs,
canonical, microcanonical, Wehrl, free energy, the H-theorem entropies
and others. Item 21 recasts von Neumann's 1929 H-theorem entropy
difference as D_M(ψ‖Uψ).

**Infinite dimensions.** Traditional observational entropy is infinite
for almost all states there; the prior makes it finite whenever S(τ) < ∞
(§VIII.7). The continuity bound (Eq. 39) needs finitely many non-zero
volumes.

**Second laws (Eq. 27, Proof 7).** The time-averaged D_M(ρ(t)‖τ) splits
into an equilibration term, D_M(ρ(t)‖ρ̄) averaged, and a prior-fit term,
D_M(ρ̄‖τ). The first is small when the number of outcomes m ≪ √d₂(ρ̄),
under nondegenerate energies and gaps (Eq. 28). The second is small under
the ETH (Eq. 31). Under local detailed balance the entropy is
non-decreasing (Eq. 35, Proof 11).

What could have come out otherwise: the lower bound could have failed for
some measurement, and the prior could have left the infinite-dimensional
pathology in place. Neither happens, under the stated constraint.

## What this does not say

- **That entropy increase is proved.** Only sufficient conditions are.
  The mesoscopic regime of the paper's own Fig. 4 falls between them, and
  the equilibration time is shown to exist but is not estimated.
- **That fluctuation probability decays as Δ/δ.** Proof 5 gives only the
  Markov upper bound Pr ≤ 2Δ/δ; the main text's "∝" overstates it.
- **That the prior-weighted volumes are necessary for generic increase.**
  Argued from §VI and Figs. 4–5, with no theorem (C11).
- **That integrable systems differ in kind.** Four hand-chosen initial
  conditions in one 2-D gas (C12).
- **Which measurement and prior are right.** The entropy is objective once
  (M, τ) are fixed; choosing them is a modelling decision (§X).

## Connections

- [THEORY-463](THEORY-463.md) holds that a strictly irreversible approach to
  equilibrium cannot come from isolated Hamiltonian dynamics alone, and
  names this paper as the constructive side of the coarse-graining and
  maximum-entropy threads. The two agree: here the increase comes from
  the choice of M and τ, and is proved only under extra conditions.
- The algebra "prior entropy minus measured divergence from the prior"
  restates cross-entropy and KL identities; the paper draws no
  connection to learning.
