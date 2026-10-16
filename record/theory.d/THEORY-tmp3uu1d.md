---
status: Active
title: "For classical systems with Markovian, microscopically reversible dynamics, the entropy production of a trajectory obeys an exact finite-time symmetry against the time-reversed process, P_F(+ω)/P_R(−ω) = e^ω, wherever ω is odd under reversal; Jarzynski's work equality and the mean second law follow as corollaries, and the symmetry constrains fluctuations, not which steady state a system selects"
version: 1
tags:
- thermodynamics
- natural-sciences
date: '2026-10-16'
source:
- LIT-522
- LIT-517
- LIT-523
summary: >-
  Crooks (1999), [LIT-522](../literature.d/LIT-522.md), read in [NOTE-413](../notes.d/NOTE-413.md), with Jarzynski (1997), [LIT-517](../literature.d/LIT-517.md)
  ([NOTE-417](../notes.d/NOTE-417.md)), and Seifert's review (2012), [LIT-523](../literature.d/LIT-523.md) ([NOTE-420](../notes.d/NOTE-420.md)). The work
  equality ⟨e^{−βW}⟩ = e^{−βΔF} holds at any switching rate, and Crooks
  derives it from a trajectory-level entropy-production theorem; Seifert
  derives every known theorem of the kind from one master theorem. These
  are exact given their premises. They are not proofs of the second law,
  since the dynamics build irreversibility in, and they say nothing about
  extremum principles for steady states. Their practical reach is work
  fluctuations of order k_BT.
presupposed_by:
- THEORY-tmp1lcfx
---

<!-- inactive-ok-file: THEORY-026 THEORY-030 THEORY-tmp1lcfx THEORY-tmpxjvy1 — Proposed; named as accounts these theorems are background to or contrasted with, not leaned on -->

# THEORY-tmp3uu1d: For classical systems with Markovian, microscopically reversible dynamics, the entropy production of a trajectory obeys an exact finite-time symmetry against the time-reversed process, P_F(+ω)/P_R(−ω) = e^ω, wherever ω is odd under reversal; Jarzynski's work equality and the mean second law follow as corollaries, and the symmetry constrains fluctuations, not which steady state a system selects

## Source

Crooks (1999), [LIT-522](../literature.d/LIT-522.md) (*Phys. Rev. E* 60, 2721), read in full in [NOTE-413](../notes.d/NOTE-413.md)
from arXiv v4. Jarzynski (1997), [LIT-517](../literature.d/LIT-517.md) (*Phys. Rev. Lett.* 78, 2690),
read in full in [NOTE-417](../notes.d/NOTE-417.md) from the arXiv preprint. Seifert (2012), [LIT-523](../literature.d/LIT-523.md)
(*Rep. Prog. Phys.* 75, 126001), read in [NOTE-420](../notes.d/NOTE-420.md): §§1–4, 6, 7, 8.1–8.2,
9.1, 9.3–9.4, 10 and 12 closely, the case studies and heat engines
skimmed. No version of record was seen for any of the three.

## What was actually shown

**The work equality ([LIT-517](../literature.d/LIT-517.md)).** Switch a classical system that starts in
canonical equilibrium from H_0 to H_1 along a fixed path in a fixed time.
Then ⟨e^{−βW}⟩ = e^{−βΔF} (Eq. 2), whatever the path and the switching
time. The proof is exact for an isolated Hamiltonian system, by Liouville's
theorem (Eqs. 6–8, checked in [NOTE-417](../notes.d/NOTE-417.md)), and for a Nosé–Hoover thermostat
with no further assumption (p. 9). For a physical reservoir it needs weak
coupling (Eqs. 9–10), which the author states. Thermodynamic integration
and the Zwanzig formula are its slow and fast limits. ⟨W⟩ ≥ ΔF follows by
Jensen's inequality, "rather than by invoking the increase of entropy"
(p. 6). If W is Gaussian, W_diss = βσ²/2 (Eq. 12).

**The fluctuation theorem ([LIT-522](../literature.d/LIT-522.md)).** Assume Markovian dynamics that are
microscopically reversible: a path's probability over its reverse's is
e^{−βQ} (Eq. 5). Define the entropy production of a path as ω = ln
ρ(x_{−τ}) − ln ρ(x_{+τ}) − βQ (Eq. 6). If ω is odd under time reversal,
then P_F(+ω)/P_R(−ω) = e^{ω} exactly, at any finite time (Eq. 2), and
⟨e^{−ω}⟩ = 1 (Eq. 4), so ⟨ω⟩ ≥ 0. ω is odd in two classes (§III):

- processes that start in equilibrium and relax to equilibrium again,
  where ω = β(W − ΔF) and the work equality is one line (Eqs. 9–10);
- time-symmetric driving into a reversal-invariant steady state, where
  P(+ω)/P(−ω) = e^{ω} for whole cycles (Eq. 12).

If ω is Gaussian, its variance is twice its mean, which gives the
Green–Kubo relations "without the standard assumption that the system is
close to equilibrium" (§IV). [NOTE-413](../notes.d/NOTE-413.md) checked the derivations.

**The unification ([LIT-523](../literature.d/LIT-523.md)).** Choosing a conjugate dynamics (reversed,
dual or dual-reversed) gives a master theorem (§4, Eqs. 78–79) from which
the integral, detailed and Crooks-type theorems all follow. The integral
theorem for total entropy production, ⟨e^{−Δs_tot}⟩ = 1, holds for any
initial state, driving and duration (Eq. 64). Apparent violations of the
second law are of order 1 in the entropy produced, so exponentially rare
in system size (pp. 19–20). Dissipated work bounds the distinguishability
of forward and reverse processes, ⟨w⟩ − ΔF ≥ T·D[p(x(t))‖p_eq(x(t))]
(Eq. 150, read with T as [NOTE-420](../notes.d/NOTE-420.md) corrects it).

**What could have come out otherwise.** These are theorems, so what can
fail is the premises. The Crooks paper shows one way: its long-time heat
theorem is "wholly inaccurate" for Δt ≤ 256 steps in its own model
(Fig. 4). The review rests the thermodynamic reading of every theorem on
noise that is "not affected by the presence of a time-dependent force"
(p. 11), and says this "could be violated in experiments" (§5.1).

## What this does not say

- **That the second law has been derived.** The integral theorems are not
  a proof of it, because a Langevin or master-equation dynamics builds
  irreversibility in ([LIT-523](../literature.d/LIT-523.md), §3.3.1, §12).
- **Which steady state a system adopts.** The results are exact symmetries
  of fluctuations, not extremum principles for the mean. They neither
  support nor refute minimum or maximum entropy production ([NOTE-413](../notes.d/NOTE-413.md),
  [NOTE-420](../notes.d/NOTE-420.md)). The framework that succeeded the Brussels school for small
  systems uses no variational selection principle for steady states.
- **That the work equality is a practical method for large systems.** The
  average is dominated by rare runs with W far below ⟨W⟩, which "pretty
  much rules out macroscopic systems" ([LIT-517](../literature.d/LIT-517.md), p. 7). The steady-state
  theorem is formally exact but cannot be measured directly, since "we have
  no independent method for calculating the probability of a state in a
  nonequilibrium ensemble" ([LIT-522](../literature.d/LIT-522.md), p. 5).
- **That the theorem holds for any endpoint.** It needs ω odd under
  reversal. A run that ends in a nonequilibrium distribution that is not
  reversal-invariant is outside it, so it does not carry over to the
  setting of [LIT-327](../literature.d/LIT-327.md) as it stands ([NOTE-413](../notes.d/NOTE-413.md)).
- **That "dissipated work" has one meaning.** Here W_diss = W − ΔF, with ΔF
  between equilibrium states. [LIT-327](../literature.d/LIT-327.md)'s dissipation subtracts the
  nonequilibrium free energy instead. The two agree only when the system
  ends in equilibrium ([NOTE-417](../notes.d/NOTE-417.md)).
- **Anything quantum, non-Markovian or strongly coupled.** All three works
  are classical. The physical-reservoir case of the work equality needs weak
  coupling, and what it becomes under strong coupling is left open.
- **The distribution of work.** The equality fixes one exponential moment
  of p(W). The relation between forward and reverse distributions is
  Crooks's result.

## Connections

- **The record's thermodynamics of computation.** [THEORY-026](THEORY-026.md) rests on an
  average-level identity for a discrete Markov chain and uses no
  fluctuation theorem; these works are its background, not its source.
  [THEORY-030](THEORY-030.md)'s subject is framed by [LIT-523](../literature.d/LIT-523.md) §7.3, which restores the second
  law under feedback through Landauer's erasure cost and reports an erasure
  experiment approaching the Landauer bound for slow cycles. The quantum
  review [LIT-010](../literature.d/LIT-010.md) re-derives both classical relations.
- **England's macrostate bound ([THEORY-tmpy68ek](THEORY-tmpy68ek.md)).** A coarse-grained second
  law of the same family, derived under detailed balance and extended to
  time-symmetric driving by citing Crooks.
- **Dissipative adaptation ([THEORY-tmp1lcfx](THEORY-tmp1lcfx.md))** takes the Crooks relation
  and its macrostate form as premises.
- **Maximum entropy production ([THEORY-tmpxjvy1](THEORY-tmpxjvy1.md)).** Dewar's path-entropy
  argument ([LIT-521](../literature.d/LIT-521.md)) produces a fluctuation theorem of the same form,
  p(σ) = e^{τσ/k_B} p(−σ), from an inferred path measure, not from a
  dynamics. It explains the theorem if real path statistics are
  maximum-entropy, and does not show that they are ([NOTE-426](../notes.d/NOTE-426.md)).
