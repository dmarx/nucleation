---
status: Active
title: "For a log-integrable linear cocycle over an ergodic probability-preserving system, vectors grow at finitely many exponential rates along an invariant flag, and for isometries of a proper metric space with integrable displacement the linear drift is detected by a horofunction, with no curvature assumed"
version: 1
tags:
- mathematics
date: '2026-10-16'
source:
- LIT-093
summary: >-
  Filip (2017), [LIT-093](../literature.d/LIT-093.md), expository notes read in full in [NOTE-078](../notes.d/NOTE-078.md). Thm
  2.2.6 is the Oseledets theorem, proved without Kingman; Thm 4.3.1 is the
  Karlsson–Ledrappier theorem, proved completely apart from cited
  measurable-selection results. Both are classical and not in doubt. The
  notes' own renditions of two other steps are flawed: Prop. 3.4.8(iii)
  is mis-stated, and the §5.3 tracking proof misapplies its lemma, so the
  Karlsson–Margulis and Kaimanovich forms should be cited to their
  originals. The hypotheses are ergodic stationary sampling and N → ∞.
---

<!-- inactive-ok-file: THEORY-325 — Proposed; named in Connections for contrast, not leaned on -->

# THEORY-tmp13a2u: For a log-integrable linear cocycle over an ergodic probability-preserving system, vectors grow at finitely many exponential rates along an invariant flag, and for isometries of a proper metric space with integrable displacement the linear drift is detected by a horofunction, with no curvature assumed

## Source

Filip (2017), "Notes on the Multiplicative Ergodic Theorem", *Ergodic
Theory and Dynamical Systems* 39(5), [LIT-093](../literature.d/LIT-093.md), read in full in [NOTE-078](../notes.d/NOTE-078.md) from
arXiv v1, every proof followed at the level of its argument.

## What was actually shown

**Oseledets (Thm 2.2.6).** Let (Ω, µ, T) be ergodic and probability
preserving, and T_ω : V_ω → V_{Tω} a measurable cocycle of invertible linear
maps with ∫ log⁺‖T_ω‖ dµ < ∞. Then there are exponents λ₁ > ⋯ > λ_k and an
invariant filtration V^{≤λ_k} ⊊ ⋯ ⊊ V^{≤λ₁} = V such that
(1/N) log‖T^N v‖ → λ_i for v in V^{≤λ_i} but not in V^{≤λ_{i+1}}. The proof
avoids Kingman. It rests on a growth dichotomy (Lemma 2.3.1) and an explicit
invariant splitting when one subbundle grows faster than its quotient
(Lemma 2.3.3), which a reader with ergodic-theory basics can check (C2).

**Karlsson–Ledrappier (Thm 4.3.1).** Let X be a proper metric space and
ω ↦ g_ω a measurable map into its isometries with ∫ d(g_ω x₀, x₀) dµ < ∞.
The drift l = lim (1/N) d(g_ω⋯g_{T^{N−1}ω} x₀, x₀) exists almost everywhere,
and there is a measurable family of horofunctions h_ω with
−(1/N) h_ω(g_ω⋯g_{T^{N−1}ω} x₀) → l, lying on the boundary when l > 0. No
curvature is assumed. [NOTE-078](../notes.d/NOTE-078.md) checked the step from the integral bound to
the almost-everywhere limit (C5).

**The geometric reading (§3).** The metrics ‖v‖_N = ‖T^N v‖ form a sequence
in the symmetric space GLₙ/Oₙ that tracks a geodesic: the rate vector is the
Lyapunov spectrum and the endpoint is the Oseledets flag (Thm 3.5.1, under
two-sided log-integrability).

**A by-product (Cor. 4.5.1).** Applied to ℝ with a concave metric, the
horofunction theorem gives a Marcinkiewicz–Zygmund-type law S_N/N^{1/p} → 0
for f ∈ Lᵖ, 0 < p < 1.

**What could have come out otherwise.** Growth rates could have varied
continuously across directions, or drift could have needed curvature to be
seen at the boundary. Neither is the case.

## What this does not say

- **That the geometric form is proved here in general.** Kaimanovich's
  regularity criterion (Thm 3.3.9) is proved for the hyperbolic plane only,
  and Prop. 3.4.8(iii) is mis-stated: it needs a logarithm, and a
  one-dimensional cocycle with CLT-size fluctuations is a counterexample as
  printed ([NOTE-078](../notes.d/NOTE-078.md), corrections).
- **That the notes' tracking proof is sound.** The §5.3 rendition of
  Karlsson–Margulis misapplies Lemma 5.1.5. The theorem is not in doubt;
  cite Karlsson and Margulis (1999) for it.
- **That "without Kingman" covers every proof here.** Only §2 avoids it;
  §§3.5 and 4 invoke it.
- **That it applies to trained deep networks.** The hypotheses are ergodic,
  stationary sampling of the matrices and N → ∞. They fit i.i.d. random
  products at initialisation, where Furstenberg–Kesten already suffices,
  not the layer-dependent finite-depth Jacobian products of trained
  networks. The notes make no ML claim.

## Connections

- [THEORY-325](THEORY-325.md) is about growth of non-normal products under time dependence
  at finite times. The exponents here are asymptotic rates and say nothing
  about transient growth.
