---
number: 67
status: Active
formerly:
- TERM-tmpf5k7x
title: 'governance-response profile, of a state for a declared family of interventions on the mechanisms that govern efficacy: the tuple of its response kernels, J_I(s) = (K_i(· | s))_{i∈I} with K_i(y | s) = P(Y^(i) = y | S = s); a description is governance-response sufficient for (I, Y) when the profile factors through it'
version: 4
history:
- version: 2
  date: '2026-10-21'
  note: >-
    Corrected from the readings of 2026-10-21 (NOTE-1037,
    NOTE-1032, NOTE-1045). Version 1 said the profile narrows
    TERM-043's causal component, as that component with the identity
    correspondence. It does not: that component compares push-forward
    laws and is zero for the hidden governance bit, where sufficiency
    fails. The `refines: TERM-043` link is removed, the section is
    rewritten, and the relation to causal abstraction is CLAIM-399.
    The definition is unchanged.
- version: 3
  date: '2026-10-21'
  note: >-
    Adopted by the owner at the second review of nucleation#305, 2026-10-21:
    status Proposed → Active. The definition is unchanged.
- version: 4
  date: '2026-10-25'
  note: >-
    A dated note added: the matched-populations test proposed three times,
    and not run. The term is unchanged.
tags:
- causality
- self-governance
date: '2026-10-21'
line: will-organization
summary: >-
  Defined at A15 §2, A16 §4 and A17 §4.1 of the exchange of 2026-10-20,
  and reused at A18 and A23. A15 called sufficiency for it "a direct
  application of the factorization criterion [CLAIM-350], not an
  independently established new theorem"; A16 §14 "a governance-specific
  causal preservation test, not necessarily a wholly independent kind of
  fidelity". It is not TERM-043's causal component with the identity
  correspondence, as this entry first said: that component compares
  interventional laws, and is zero for a coarse-graining that loses the
  response of every state (CLAIM-399). It is a fixed-target,
  state-conditional sufficiency. Adopted by the owner on 2026-10-21. It
  names what CLAIM-407 is stated in; it replaces nothing.
used_by:
- CLAIM-407
- CLAIM-399
---
<!-- inactive-ok-file: CLAIM-122 — Proposed; the supervisory test this profile parameterizes, open -->

# TERM-067: governance-response profile, of a state for a declared family of interventions on the mechanisms that govern efficacy: the tuple of its response kernels, J_I(s) = (K_i(· | s))_{i∈I} with K_i(y | s) = P(Y^(i) = y | S = s); a description is governance-response sufficient for (I, Y) when the profile factors through it

## Definition

Fix a state S with a law, a family I of interventions on what governs
which of a system's capacities become effective (authority, access,
precedence: [TERM-023](TERM-023.md)'s relations), and an outcome Y. The **governance-response
profile** of a state s is the tuple of its response kernels,

J_I(s) = (K_i(· | s))_{i∈I}, K_i(y | s) = P(Y^(i) = y | S = s).

A15 §2 wrote it as J_I(s) = (P(Y_{t+1} | s, do(i)))_{i∈I}, "where
\(\mathcal I\) is a specified family of interventions on authority, access,
or efficacy-governing relations". A coarse description T = f(S) is
**governance-response sufficient** for (I, Y) when J_I factors through T,
that is, when T(s) = T(s′) implies J_I(s) = J_I(s′). A17 §4.1: "A coarse
representation \(T=f(S)\) is governance-response sufficient for
\((\mathcal I,Y)\) when \(J_{\mathcal I}\) factors through \(T\)."

For a declared intervention distribution ρ, the deficiency
Γ_ρ(T) = I(S; Y^(I) | T(S), I) measures the failure, and is zero exactly
when the profile factors through T on the interventions ρ charges and the
states of positive probability ([CLAIM-407](../claims.d/CLAIM-407.md)). For one ρ and one
outcome it cannot rise under refinement ([CLAIM-409](../claims.d/CLAIM-409.md)).

**Beside [TERM-043](TERM-043.md), not under it.** [TERM-043](TERM-043.md)'s causal component is "Differences in
responses to corresponding interventions", Σ_a π(a) d(T_# P_o(Y | do(a)),
P_t(Y′ | do(τ(a)))). Version 1 of this entry read the profile as that
component with τ the identity, π the declared ρ and the interventions
restricted to the mechanisms of governance, and filed it as refining
[TERM-043](TERM-043.md). That was wrong. The component compares the push-forward of a
population's interventional law with a target's law, a graded form of
Rubenstein et al.'s exact transformation ([NOTE-1037](../notes.d/NOTE-1037.md)). For the hidden
governance bit it is zero: marginalising K is exact, and even a
τ-abstraction, because the coarse model's noise can carry K
([THEORY-848](../theory.d/THEORY-848.md), [THEORY-849](../theory.d/THEORY-849.md)), while the profile does not factor
through the coarse state and Γ = ρ(h = 1) bits. Sufficiency is the
state-conditional version: Beckers and Halpern's compatibility condition
with the high-level context required to be the coarse state itself,
compared on one outcome ([CLAIM-399](../claims.d/CLAIM-399.md)). So the `refines` link was
removed on 2026-10-21. A16 §14 declined a new dimension: "I would be
reluctant to add a new term such as governance fidelity as an entirely
separate dimension without checking whether it is already a specific
instance of causal fidelity". Checked, it is not an instance of that
component; whether the profile should become a further component of
[TERM-043](TERM-043.md), or stay a criterion beside it, is not settled here.
[CLAIM-122](../claims.d/CLAIM-122.md)'s supervisory test, "intervene on the governance relations", is
what the profile records.

**What would settle it.** Whether claims about will-organization that now
say "behaviourally equivalent but differently governed" ([CLAIM-122](../claims.d/CLAIM-122.md),
[QUESTION-086](../questions.d/QUESTION-086.md), [QUESTION-092](../questions.d/QUESTION-092.md)) are clearer stated in it, and whether the
owner wants the will line to carry a formal term.

## What it is not

- **Not a measure of will, or of self-governance.** A16: "It would not
  automatically be a judgment about self-governance." It records the
  response to governance set from outside, P(Y | do(i)), not whether the
  system changes its governance itself ([CLAIM-407](../claims.d/CLAIM-407.md)'s "What it does not
  say", and A27 §3: "An ordinary machine can respond dramatically to a
  technician rewiring it").
- **Not a new kind of fidelity.** A16 and A17 both declined that.
- **Not causal abstraction.** Exact transformation, τ-abstraction and
  zero approximate-abstraction distance all accept the hidden-bit
  coarse-graining that sufficiency rejects ([THEORY-848](../theory.d/THEORY-848.md),
  [THEORY-849](../theory.d/THEORY-849.md), [THEORY-843](../theory.d/THEORY-843.md); [CLAIM-399](../claims.d/CLAIM-399.md)).
- **Not identifiable from passive data.** A16: "Ordinary passive data may
  not identify \(\Gamma\)."
- **Not the behavioural profile.** A description can be exactly closed for
  the ordinary dynamics and keep none of it ([CASE-125](../cases.d/CASE-125.md)).

## Note of 2026-10-25: the matched-populations test, proposed three times

A38, A43 and A44 of the exchange of 2026-10-24, continued, proposed pairs
of organizations "with matched collective interpretation and policy
distributions but different internal governance", exposed to the same
intervention. That tests whether the collective description is
governance-response sufficient in this term's sense. None was run. A40's
and A41's interventions on access change outcomes by construction (where
operators differ, changing who acts where must change the output), and do
not test it. The term is unchanged.
