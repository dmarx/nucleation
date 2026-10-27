---
number: 1069
status: Active
formerly:
- THEORY-tmper2kf
title: 'In a von Neumann measurement the measuring variable''s information about the measured variable grows continuously under the unitary coupling, in Di Biagio and Rovelli''s model as I_{A:B}(t) = sin²(ωt)H_A, so the discontinuity of a quantum measurement lies only in a threshold on when information counts as a fact; with an idealized pure ready state a fact conditional on a pointer value appears at once, which they attribute to the idealization'
version: 1
tags:
- quantum-foundations
- information-theory
date: '2026-10-27'
source:
- LIT-1676
summary: >-
  Di Biagio and Rovelli (2025), [LIT-1676](../literature.d/LIT-1676.md), read from arXiv v2 in
  [NOTE-1214](../notes.d/NOTE-1214.md), §VII and App. B. Active as mathematics: (B7) follows
  from (B6), which I rederived; (B8) as printed has a sign error, and the
  correct form is I_A^max − cos²(ωt)H_A. The continuity is of the expected
  quantities. A conditional relative fact appears at once in the ideal
  model, and the full-rank case that would remove that is described, not
  computed. The authors say the point is not specifically quantum.
---

# THEORY-1069: In a von Neumann measurement the measuring variable's information about the measured variable grows continuously under the unitary coupling, in Di Biagio and Rovelli's model as I_{A:B}(t) = sin²(ωt)H_A, so the discontinuity of a quantum measurement lies only in a threshold on when information counts as a fact; with an idealized pure ready state a fact conditional on a pointer value appears at once, which they attribute to the idealization

## Source

Di Biagio and Rovelli (2025), [LIT-1676](../literature.d/LIT-1676.md), arXiv 2510.11349v2, §VII
(pp. 5–6), Fig. 1 and App. B (pp. 8–9); read in [NOTE-1214](../notes.d/NOTE-1214.md).

## What was actually shown

**The general claim.** In von Neumann's scheme the coupled system goes from
Σ αₙ|aₙ⟩|b_r⟩ to Σ αₙ|aₙ⟩|bₙ⟩ (eqs. 17–18) under the Schrödinger equation.
I_{A:B} goes from 0 to H_A, and the relative information I_{A|B} reaches
I_A^max. "There is no special moment in which the information that the
apparatus has about the system jumps from zero to a finite value" (p. 6). "A
discontinuity only comes from the definition of 'fact' as something whose
probability reaches a sufficiently high threshold" (p. 5).

**The model.** With Ĥ = iω Σₙ |aₙ⟩⟨aₙ| ⊗ (|bₙ⟩⟨b_r| − |b_r⟩⟨bₙ|) on
t ∈ [0, π/2ω] (B3), |ψ(t)⟩ = cos ωt|ψ_i⟩ + sin ωt|ψ_f⟩ (B5), and
p_t(aₙ, b_k) = |αₙ|²(cos²ωt δ_kr + sin²ωt δ_nk) (B6). The marginal p_t(aₙ)
= |αₙ|² does not change, so the outside system's information about A is
constant, while I_{A:B}(t) = sin²(ωt) H_A (B7). The reading checked (B7) from
(B6): H_B and H_AB each carry the binary entropy of cos²ωt, which cancels.
By eq. (7), I_{A|B}(t) = I_A^max − cos²(ωt)H_A. The paper prints "+"
(B8, p. 8), which would exceed the maximum for t < T. That is a sign error.

**What could have come out otherwise, and did, in the ideal case.** The
conditional quantity behaves differently. "according to the state |ψ(t)⟩, A
is a fact relative to B = bₙ for all values of t > 0, because
p_{t>0}(a|bₙ) = δ_{a,aₙ}" (p. 9). As soon as the pointer reads bₙ with any
probability, that reading fixes A. The authors call this "an artefact of
studying a too idealised system, where p_0(bₙ) is exactly vanishing". In a
realistic, full-rank state I_{A|bₙ} starts at I_A^max − H_A "and smoothly
increases to close to maximal over a short time" (p. 9). That case is
described, not computed.

**Not specifically quantum.** "All the above has actually little to do with
quantum theory": a classical register shows "the same apparent tension
between discrete outcomes and continuous information acquisition" (p. 6).

## What this does not say

- **That every relative fact is reached continuously.** The expected
  relative information is continuous. A fact conditional on a pointer value
  is reached at once in the ideal model, and the paper's remedy, full rank,
  is asserted with citations [56, 57] and not worked out.
- **When a measurement ends.** That is set by a threshold on information, "an
  'acceptable' level" (p. 6), and the paper does not fix it.
- **That continuity solves the measurement problem.** Which outcome occurs is
  outside the account. The paper's position is that asking what "really"
  happened has no empirical content (§IX).
- **That a measurement differs from any correlating interaction.** Nothing in
  the definitions separates the two. A measurement is a coupling that takes
  I_{A|B} to its maximum.
- **That this is new as mathematics.** It is Shannon quantities evaluated on
  the standard von Neumann model, and the authors say as much for the
  classical case.
