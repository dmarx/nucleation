---
status: Active
title: "Every finite stochastic transition matrix on a configuration space equals the entrywise squared modulus of a complex matrix, unitary after dilation, so the Hilbert-space formalism can be written over any indivisible stochastic process as a non-unique representation; within that representation interference is the term by which the process fails to divide at an intermediate time, relative to the chosen configurations, and an ideal correlating environment restores divisibility"
version: 1
tags:
- quantum-foundations
- probabilistic-modeling
date: '2026-10-16'
source:
- LIT-086
summary: >-
  Barandes (2023), [LIT-086](../literature.d/LIT-086.md), read in full in [NOTE-080](../notes.d/NOTE-080.md). Γ_ij = |Θ_ij|² =
  tr(Θ†P_iΘP_j) is an identity (Θ_ij = √Γ_ij works), and a unitary Θ on
  the original space exists only for doubly stochastic Γ. Interference is
  the cross-term of Eq. 43 against a would-be Markov factorization, and a
  perfectly correlating environment that then evolves separately makes the
  process divisible (Eqs. 45–56). The "emergent" Schrödinger equation is
  the definition of H, unitarity is a choice the claimed gauge freedom
  does not preserve, and the decomposition is relative to a configuration
  basis the paper never fixes.
---

<!-- inactive-ok-file: LIT-001 — Rejected; named as the contrasting stochastic-mechanics derivation its reading compares -->
<!-- inactive-ok-file: THEORY-010 — Proposed; named in Connections, not leaned on -->

# THEORY-tmp6wtwf: Every finite stochastic transition matrix on a configuration space equals the entrywise squared modulus of a complex matrix, unitary after dilation, so the Hilbert-space formalism can be written over any indivisible stochastic process as a non-unique representation; within that representation interference is the term by which the process fails to divide at an intermediate time, relative to the chosen configurations, and an ideal correlating environment restores divisibility

## Source

Barandes (2023; v3 2025), [LIT-086](../literature.d/LIT-086.md), read in full in [NOTE-080](../notes.d/NOTE-080.md), which checked
the algebra.

## What was actually shown

**Indivisible stochastic process (§2).** A configuration space
C = {1,…,N} and transition matrices Γ(t←t0), stochastic and with
Γ(t0←t0) = 1, specified only from conditioning times. Divisibility,
Γ(t←0) = Γ̃(t←t′)Γ(t′←0) with Γ̃ stochastic, is not assumed, and
higher-order conditionals are left unspecified.

**Dictionary (Eqs. 12–15).** Γ_ij(t←0) = |Θ_ij(t←0)|² =
tr(Θ†P_iΘP_j), with Σ_i |Θ_ij|² = 1. This is an identity: the entrywise
square root always works ([NOTE-080](../notes.d/NOTE-080.md), C1). Then ρ(t) = Θ diag(p(0)) Θ† gives
p_i(t) = tr(P_iρ(t)) (Eqs. 16–17), Kraus operators K_β = ΘP_β (Eqs. 25–27),
and, after a cited Stinespring dilation, a unitary U with Γ_ij = |U_ij|²
(Eqs. 30–32).

**Interference (Eq. 43).** Γ_ij(t←0) − [|U(t←t′)|²|U(t′←0)|²]_ij =
Σ_{k≠l} U_ik(t←t′)Ψ_k(t′) conj(U_il(t←t′)Ψ_l(t′)). The cross-term is the
gap between the actual transition probabilities and a pretend Markov
factorization at t′. [NOTE-080](../notes.d/NOTE-080.md) confirms the algebra (C5).

**Division events (Eqs. 45–58).** If at t′ the system is perfectly
correlated with an environment, p^{SE}_{i′e′}(t′) = p^S_{i′}(t′)δ_{e′e(i′)}
with the e(i) distinct, and afterwards U^{SE} = U^S ⊗ U^E, the cross-terms
vanish and Γ^S(t←0) = Γ^S(t←t′)Γ^S(t′←0). Regular division events with a
time-homogeneous U^S give a Markov chain, Γ^S(nδt←0) = (Γ^S)ⁿ. The density
matrix after a division event is diagonal (Eqs. 59–62).

**Measurement (§4).** Given a unistochastic evolution that correlates a
device with the eigenbasis of a non-diagonal Ã^S (Eq. 73), the device
configurations follow the Born rule for Ã^S (Eq. 78), and conditioning on
the device reproduces collapse (Eqs. 89–94).

**What could have come out otherwise.** A stochastic matrix with no complex
"square root" would have blocked the representation; there is none. The
cross-terms could have survived a perfectly correlating environment; under
Eqs. 45–46 they cannot.

## What this does not say

- **That quantum dynamics are derived from stochastic processes.** The
  Schrödinger, von Neumann and Ehrenfest equations follow from the
  definition H ≡ iħ(∂U/∂t)U† (Eq. 33), and carry no content beyond the
  choice of U ([NOTE-080](../notes.d/NOTE-080.md), C4). The paper's "new result" labels mark
  identities and definitions.
- **That unitarity is inevitable.** A unitary Θ on the original N
  configurations exists only for doubly stochastic Γ (Eq. 32); general Γ
  needs the dilated space, which is cited, not constructed. The claimed
  gauge freedom Θ_ij ↦ e^{iθ_ij}Θ_ij does not preserve unitarity ([NOTE-080](../notes.d/NOTE-080.md)'s
  check on the Hadamard), so the choice of unitary representative is not
  gauge-invariant (C3, C13).
- **That interference needs indivisible dynamics on any ontology.** The
  decomposition is relative to the chosen configuration space. [NOTE-080](../notes.d/NOTE-080.md)
  notes that an odd-d stabilizer circuit shows Eq. 43's interference on the
  computational configurations yet has a divisible deterministic model on
  [LIT-007](../literature.d/LIT-007.md)'s larger ontic space.
- **That every quantum system is such a process in a physical sense.** The
  quantum-to-stochastic direction, Γ = |U|², needs a chosen configuration
  basis, which the paper does not fix (C12). Multi-time statistics beyond
  the measurement model, locality and Bell-type questions are deferred.
- **That Markovianity is explained in practice.** Only the ideal division
  event is shown; the approximate case is asserted (fn. 18).

## Connections

- Auffèves & Grangier ([LIT-077](../literature.d/LIT-077.md)) reach the same unistochastic matrices as a
  claimed consequence of postulates about contexts, where here they are a
  chosen representation between times ([NOTE-080](../notes.d/NOTE-080.md)). Their contextual
  objectivity is [THEORY-010](THEORY-010.md).
- The paper places itself outside the ontological-models framework, and so
  outside PBR ([THEORY-tmppgcbt](THEORY-tmppgcbt.md)), with a nomic wave function (§5.3).
- [LIT-001](../literature.d/LIT-001.md) (Rejected) reaches a Schrödinger equation from stochastic
  mechanics but leaves no real stochastic process; this paper keeps the
  process and gives the equation no dynamical content ([NOTE-080](../notes.d/NOTE-080.md)).
