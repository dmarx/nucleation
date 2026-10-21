---
status: Proposed
refines:
- TERM-043
title: 'governance-response profile, of a state for a declared family of interventions on the mechanisms that govern efficacy: the tuple of its response kernels, J_I(s) = (K_i(· | s))_{i∈I} with K_i(y | s) = P(Y^(i) = y | S = s); a description is governance-response sufficient for (I, Y) when the profile factors through it'
version: 1
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
  fidelity". So it narrows TERM-043's causal component to one system,
  with the identity correspondence and interventions restricted to the
  mechanisms of governance. Proposed: recorded, not adopted. It names
  what CLAIM-tmppi0xf is stated in; it replaces nothing.
used_by:
- CLAIM-tmppi0xf
---
<!-- inactive-ok-file: CLAIM-122 — Proposed; the supervisory test this profile parameterizes, open -->

# TERM-tmpf5k7x: governance-response profile, of a state for a declared family of interventions on the mechanisms that govern efficacy: the tuple of its response kernels, J_I(s) = (K_i(· | s))_{i∈I} with K_i(y | s) = P(Y^(i) = y | S = s); a description is governance-response sufficient for (I, Y) when the profile factors through it

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
states of positive probability ([CLAIM-tmppi0xf](../claims.d/CLAIM-tmppi0xf.md)). For one ρ and one
outcome it cannot rise under refinement ([CLAIM-tmpshzxc](../claims.d/CLAIM-tmpshzxc.md)).

**Why it narrows [TERM-043](TERM-043.md).** [TERM-043](TERM-043.md)'s causal component is "Differences in
responses to corresponding interventions", Σ_a π(a) d(T_# P_o(Y | do(a)),
P_t(Y′ | do(τ(a)))). A coarse-graining of one system is the case with the
correspondence τ the identity, π the declared ρ, and the interventions
restricted to the mechanisms of governance. A16 §14 declined a new
dimension: "I would be reluctant to add a new term such as governance
fidelity as an entirely separate dimension without checking whether it is
already a specific instance of causal fidelity". [CLAIM-122](../claims.d/CLAIM-122.md)'s supervisory
test, "intervene on the governance relations", is what the profile records.

**What would settle it.** Whether claims about will-organization that now
say "behaviourally equivalent but differently governed" ([CLAIM-122](../claims.d/CLAIM-122.md),
[QUESTION-086](../questions.d/QUESTION-086.md), [QUESTION-092](../questions.d/QUESTION-092.md)) are clearer stated in it, and whether the
owner wants the will line to carry a formal term.

## What it is not

- **Not a measure of will, or of self-governance.** A16: "It would not
  automatically be a judgment about self-governance." It records the
  response to governance set from outside, P(Y | do(i)), not whether the
  system changes its governance itself ([CLAIM-tmppi0xf](../claims.d/CLAIM-tmppi0xf.md)'s "What it does not
  say", and A27 §3: "An ordinary machine can respond dramatically to a
  technician rewiring it").
- **Not a new kind of fidelity.** A16 and A17 both declined that.
- **Not identifiable from passive data.** A16: "Ordinary passive data may
  not identify \(\Gamma\)."
- **Not the behavioural profile.** A description can be exactly closed for
  the ordinary dynamics and keep none of it ([CASE-tmpdc0tl](../cases.d/CASE-tmpdc0tl.md)).
