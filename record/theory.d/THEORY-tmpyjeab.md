---
status: Active
title: 'For a deterministic supervenient feature V of a Markov system, Rosas et al.''s practical emergence criterion Ψ equals the parts'' whole-minus-sum information about V''s next value minus V''s one-step dynamical dependence I(V_t′; X_t | V_t), so dynamical independence raises Ψ but neither implies emergence nor is implied by it, and the paper''s sufficient test for causal decoupling can pass a feature that is not dynamically independent'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Filed from the reading of Rosas et al. (2020) in NOTE-tmpvy64o. The
    identity is the record's, derived from the paper's Eq. (10a) and
    Definition 1. The link to dynamical independence uses Barnett and
    Seth's definition as THEORY-257 states it. Every step is re-derived
    below. The identity was checked numerically on random three-bit Markov
    chains with random features (agreement to 10⁻¹⁰). The four examples
    were computed exactly, and the AR(1) case was also simulated. Filed
    Active under ADR-047 v2.
tags:
- complex-systems
- information-theory
- causality
date: '2026-10-20'
source:
- LIT-tmp8mwu9
- LIT-979
answers:
- QUESTION-115
summary: >-
  Rosas et al. (2020), [LIT-tmp8mwu9](../literature.d/LIT-tmp8mwu9.md), read in [NOTE-tmpvy64o](../notes.d/NOTE-tmpvy64o.md), with Barnett and
  Seth's dynamical independence ([LIT-979](../literature.d/LIT-979.md), [THEORY-257](THEORY-257.md)). By the chain rule,
  Ψ(V) = [I(X_t;V_t′) − Σ_j I(Xʲ_t;V_t′)] − I(V_t′;X_t|V_t). The subtracted
  term vanishing implies Barnett–Seth independence for Markov X. Examples
  show each condition without the other. The independent sum of AR(1)
  channels has both, with no interaction. The identity concerns Ψ, the
  paper's practical criterion; it says nothing about the PID quantities
  themselves.
---
<!-- inactive-ok-file: THEORY-257 THEORY-497 THEORY-222 — Proposed; the accounts this one relates, nothing here rests on their being settled -->

# THEORY-tmpyjeab: For a deterministic supervenient feature V of a Markov system, Rosas et al.'s practical emergence criterion Ψ equals the parts' whole-minus-sum information about V's next value minus V's one-step dynamical dependence I(V_t′; X_t | V_t), so dynamical independence raises Ψ but neither implies emergence nor is implied by it, and the paper's sufficient test for causal decoupling can pass a feature that is not dynamically independent

## Source

Rosas, Mediano, Jensen, Seth, Barrett, Carhart-Harris and Bor (2020),
[LIT-tmp8mwu9](../literature.d/LIT-tmp8mwu9.md), read in full in [NOTE-tmpvy64o](../notes.d/NOTE-tmpvy64o.md): the definitions of
supervenience (Definition 1) and of the criteria Ψ, Δ, Γ (Eq. 10), and
Proposition 1. Barnett and Seth (2023), [LIT-979](../literature.d/LIT-979.md), read in [NOTE-791](../notes.d/NOTE-791.md), for
dynamical independence. Neither paper states the identity below. It is the
record's derivation.

## What was actually shown

**Setting.** X_t = (X¹_t, …, Xⁿ_t) is a Markov process, and V_t = F(X_t) is
a deterministic feature, as in all three of the paper's case studies. With
t′ the next time point, the paper's criterion at order 1 is
Ψ(V) = I(V_t; V_t′) − Σ_j I(Xʲ_t; V_t′). Write

- W(V) := I(X_t; V_t′) − Σ_j I(Xʲ_t; V_t′), the whole-minus-sum
  information of the parts about V's next value;
- T₁(V) := I(V_t′; X_t | V_t), the one-step dynamical dependence.

**The identity, Ψ(V) = W(V) − T₁(V).**

1. Since V_t = F(X_t), H(V_t | X_t) = 0, so I(V_t; V_t′ | X_t) = 0.
2. By the chain rule, I((X_t, V_t); V_t′) = I(X_t; V_t′) + I(V_t; V_t′ |
   X_t) = I(X_t; V_t′).
3. By the chain rule the other way, I((X_t, V_t); V_t′) = I(V_t; V_t′) +
   I(X_t; V_t′ | V_t).
4. So I(V_t; V_t′) = I(X_t; V_t′) − T₁(V). Subtracting Σ_j I(Xʲ_t; V_t′)
   from both sides gives the identity. For order k, the sum runs over the
   groups of k parts and the argument is unchanged.

Checked on five random three-bit Markov chains with random three-valued
features: both sides agree to 10⁻¹⁰.

**T₁ = 0 implies Barnett–Seth dynamical independence.** Their condition is
I(V_t′; X⁻_t | V⁻_t) = 0, with histories up to t ([THEORY-257](THEORY-257.md), Eq. 2.6,
no environment).

1. X is Markov, so p(V_t′ | X⁻_t) = p(V_t′ | X_t).
2. T₁ = 0 means p(V_t′ | X_t) = p(V_t′ | V_t).
3. So p(V_t′ | X⁻_t) depends on X⁻_t only through V_t, which is a function
   of V⁻_t. Hence V_t′ ⫫ X⁻_t | V⁻_t.

More precisely, for Markov X the multi-lag dependence never exceeds T₁.
Write V⁻_t = (V_t, V_past). Then I(V_t′; X_t | V⁻_t) = T₁ + I(V_t′; V_past |
X_t, V_t) − I(V_t′; V_past | V_t). The middle term is 0 by the Markov
property, so Barnett and Seth's dependence equals T₁ − I(V_t′; V_past | V_t)
≤ T₁. The converse implication is not claimed: V's longer history can
remove dependence that V_t alone leaves.

**Consequences.**

- *For a dynamically independent feature* (T₁ = 0), Ψ = W. Among features
  with the same W, Ψ is largest for the independent ones.
- *Ψ > 0 does not need independence.* Take three bits whose parity is kept
  with probability γ(x¹), with γ(0) = 0.95 and γ(1) = 0.6, the next state
  otherwise uniform within the parity class. Example 1 of the paper is the
  case of constant γ.
  - Exactly: Ψ = 1 − H(0.775) = 0.231 bits, Γ = max_j I(V_t; Xʲ_t′) = 0 and
    T₁ = H(0.775) − ½[H(0.95) + H(0.6)] = 0.141 bits.
  - So the parity meets Proposition 1's stated sufficient condition for
    causal decoupling (Ψ > 0, Γ = 0), and it is not dynamically
    independent.
  - With constant γ (Example 1), T₁ = 0: the paper's own "statistical ghost"
    is exactly dynamically independent.
- *Independence does not give emergence.* Take two independent bits, each
  copying itself, with V = X¹. Then T₁ = 0 and Ψ = 0. By the paper's Lemma
  1, a function of a single part is never causally emergent.
- *Both can hold with no interaction.* Take n ≥ 2 independent stationary
  Gaussian AR(1) channels with a common coefficient a, 0 < |a| < 1, and V
  their sum.
  - V_t′ = aV_t + noise, so T₁ = 0.
  - Ψ = −½ log(1 − a²) + (n/2) log(1 − a²/n). That is positive because
    log(1 − x) is strictly concave and vanishes at 0, so
    n log(1 − a²/n) > log(1 − a²).
  - For a = 0.9 and n = 2, Ψ = 0.449 bits; a simulation of 2 × 10⁵ steps
    gives 0.454.
  - The discrete analogue: two self-copying bits with V = X¹ ⊕ X² give
    Ψ = 1 bit and T₁ = 0.

**What could have come out otherwise.** Ψ could have been unrelated to
closure, with an independent feature penalized or a dependent one
rewarded. The identity shows the dependence term enters with a fixed
negative sign and unit weight.

## What this does not say

- **Nothing about the PID quantities.** The identity concerns Ψ, a
  redundancy-free bound. Whether a feature is causally emergent or
  decoupled in the paper's formal sense (Un⁽ᵏ⁾ > 0) depends on the
  decomposition chosen. [NOTE-tmpvy64o](../notes.d/NOTE-tmpvy64o.md) shows that Ψ > 0 does not
  establish it for the candidate feature under the minimum-MI
  decomposition. So the parity example shows that Ψ's *test* for
  decoupling passes a dependent feature, not that formal decoupling and
  independence come apart in every decomposition.
- **Not for noisy features as written.** For V_t = F(X_t) + ν_t, step 1
  needs I(V_t; V_t′ | X_t) = 0. That holds when the noise at t is
  independent of everything at t′. The paper's Definition 1 does not state
  it in that form.
- **Not the multi-lag dependence.** T₁ conditions on V_t alone. Barnett
  and Seth's dependence conditions on V's history and is smaller by
  I(V_t′; V_past | V_t), the memory of the reduced process. Ψ penalizes the
  larger, one-step quantity, so a feature that is independent only given
  its history is still penalized.
- **Not that Ψ > 0 marks interaction or integration.** The AR(1) and
  copying examples pass with independent parts. Ψ > 0 marks a feature
  whose own persistence beats the sum of what each part says about its
  future.
- **Not a ranking of levels.** Neither Ψ nor T₁ prices the size of the
  feature. W can grow with the number of parts summed, as in the AR(1)
  case.

## Connections

- **[THEORY-257](THEORY-257.md), [THEORY-733](THEORY-733.md).** This places the ΦID practical criterion
  relative to dynamical independence. On closure the two agree in sign: Ψ
  rewards it. They differ on what else counts. Ψ adds the parts'
  whole-minus-sum and penalizes redundancy among them. Independence asks
  for nothing beyond closure, so a lone self-copying part qualifies. In a
  linear Gaussian VAR(1), [THEORY-733](THEORY-733.md)'s invariant subspaces have T₁ = 0,
  so for them Ψ reduces to W.
- **[THEORY-497](THEORY-497.md)** holds the ΦID account this criterion serves. The examples
  here show its practical test detects persistence of aggregates of
  independent parts.
- **[QUESTION-115](../questions.d/QUESTION-115.md): answers in part.**
  - Where dynamical independence and the ΦID criterion part: a single
    persistent part is independent and not emergent, and a parity whose
    persistence depends on one part passes Ψ's decoupling test and is not
    independent.
  - What each tracks: independence tracks closure. Ψ tracks closure plus
    collective, non-redundant predictability.
  - Neither tracks interaction, and neither prices size.
- **[THEORY-222](THEORY-222.md).** Effective information ranks levels by how much they say
  under interventions. Ψ cannot, since I(V_t; V_t′) ≤ I(X_t; X_t′). The two
  are not rivals on one scale.
- **[CLAIM-tmpkoi6k](../claims.d/CLAIM-tmpkoi6k.md).** The AR(1) sum is the uncoupled case (coupling 0) of
  its uniformly coupled VAR(1), where the sum of all units is exactly
  independent. Here it also passes Ψ.
