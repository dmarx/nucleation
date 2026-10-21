---
status: Active
title: 'Causal abstraction in the senses of Rubenstein et al., Beckers and Halpern, and Beckers, Eberhardt and Halpern does not secure governance-response sufficiency: exact transformation, τ-abstraction and zero approximate-abstraction distance all accept the hidden-bit coarse-graining, which loses ρ(h = 1) bits of the response to h, because each lets high-level noise carry what the coarse state drops; for one outcome and the identity correspondence, sufficiency is their compatibility condition with the high-level context fixed to the coarse state, and strong abstraction rejects the case only through interventions on the hidden parameter'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the construction: for the structural model of CASE-tmpdc0tl
  (K = E_K, Y_t = E_t, H = E_H, Y_{t+1} = (1 − H)E_{t+1} + HK) with
  interventions on H only, the map dropping K is not a τ-abstraction under
  the context map τ_U(u) = (u_t, u_H, (u_{t+1}, u_K)), or marginalising K is
  not an exact transformation by Rubenstein et al.'s Theorem 10, or its
  approximate-abstraction distance is not 0; or a compatible high-level
  model whose context is the coarse state Y_t, with remaining noise
  independent of the state, for the response to h = 1.
tags:
- causality
- self-governance
date: '2026-10-21'
line:
- formal-apparatus
- will-organization
rests_on:
- CLAIM-tmppi0xf
grounds:
- THEORY-tmpjfhcb
- THEORY-tmpjtnjd
- THEORY-tmpe391l
- CASE-tmpdc0tl
uses:
- TERM-tmpf5k7x
summary: >-
  The record's join, on 2026-10-21, of its readings of the
  causal-abstraction papers ([NOTE-tmp6b7dr](../notes.d/NOTE-tmp6b7dr.md), [NOTE-tmp1bdcu](../notes.d/NOTE-tmp1bdcu.md), [NOTE-tmpqfl95](../notes.d/NOTE-tmpqfl95.md))
  with [CLAIM-tmppi0xf](CLAIM-tmppi0xf.md). A25 of the exchange of 2026-10-20: "We should not
  present governance-preserving coarse-graining as a new general theory
  of causal abstraction." That stands. But it is not an instance of these papers'
  notions either: their criteria compare interventional laws and let the
  high-level context be any map that works, so they accept the hidden
  governance bit, whose coarse state keeps nothing of the response to h.
  Re-checked step by step against the three THEORYs. It corrects
  [TERM-tmpf5k7x](../terms.d/TERM-tmpf5k7x.md)'s first wording, which read the profile as [TERM-043](../terms.d/TERM-043.md)'s
  causal component with the identity correspondence.
---

# CLAIM-tmp4r4mi: Causal abstraction in the senses of Rubenstein et al., Beckers and Halpern, and Beckers, Eberhardt and Halpern does not secure governance-response sufficiency: exact transformation, τ-abstraction and zero approximate-abstraction distance all accept the hidden-bit coarse-graining, which loses ρ(h = 1) bits of the response to h, because each lets high-level noise carry what the coarse state drops; for one outcome and the identity correspondence, sufficiency is their compatibility condition with the high-level context fixed to the coarse state, and strong abstraction rejects the case only through interventions on the hidden parameter

## The claim

**The terms.** Governance-response sufficiency of a coarse description
T = f(S) for (I, Y) ([TERM-tmpf5k7x](../terms.d/TERM-tmpf5k7x.md)) asks that each response kernel
K_i(· | s) = P(Y^(i) | S = s) depend on s only through T(s). Rubenstein et
al.'s exact transformation ([THEORY-tmpjfhcb](../theory.d/THEORY-tmpjfhcb.md)) asks that a coarse model
reproduce the push-forward of each declared interventional law. Beckers and
Halpern's uniform transformation is the same for every distribution on
contexts, and it holds exactly when some context map τ_U commutes with every
allowed intervention, τ(M_L(u, i)) = M_H(τ_U(u), ω(i)) ([THEORY-tmpjtnjd](../theory.d/THEORY-tmpjtnjd.md));
τ-abstraction adds surjectivity and fixes ω to the map τ induces. Beckers,
Eberhardt and Halpern's distance d_τ is 0 exactly for a τ-abstraction
([THEORY-tmpe391l](../theory.d/THEORY-tmpe391l.md)).

**The relation.** Take the low-level context to be the pre-intervention
state S, with any further noise independent of S; ω the identity on I; and
the comparison on Y alone. In the deterministic case sufficiency is then
the compatibility condition with the context map required to be T itself:
Y^(i)(s) = g_i(T(s)) for every s and i. In the probabilistic case it is the
kernel form, P(Y^(i) | S = s) = G_i(· | T(s)): a high-level model whose
context is T and whose remaining noise is independent of S given T. The
papers' notions only ask that some τ_U exist, so they are weaker than this
in that respect. They are stronger in others, which sufficiency does not
ask for: a structural high-level model, conditions on composed
interventions, more than one outcome. Neither notion is a special case of
the other.

**The witness** ([CASE-tmpdc0tl](../cases.d/CASE-tmpdc0tl.md)). As a structural model: K = E_K,
Y_t = E_t, H = E_H, Y_{t+1} = (1 − H)E_{t+1} + HK, with E_K, E_t, E_{t+1}
fair independent bits, and declared interventions ∅, do(H = 0), do(H = 1).
Let τ drop K.

- *Exact.* K is set by no declared intervention, so marginalising it is
  exact by Rubenstein et al.'s Theorem 10, with the coarse model
  Y_{t+1} = (1 − H)E′₁ + HE′₂ and E′₂ = K ([THEORY-tmpjfhcb](../theory.d/THEORY-tmpjfhcb.md)).
- *A τ-abstraction.* With τ_U(u) = (u_t, u_H, (u_{t+1}, u_K)), for every
  context and every intervention on H the low level gives
  (u_t, h, (1 − h)u_{t+1} + hu_K), and so does the high level from τ_U(u).
  τ and τ_U are surjective, and do(H = h) maps to do(H = h). So it is a
  τ-abstraction ([THEORY-tmpjtnjd](../theory.d/THEORY-tmpjtnjd.md)), and d_τ = 0 ([THEORY-tmpe391l](../theory.d/THEORY-tmpe391l.md)).
- *Not sufficient.* Under do(H = 1) the response of the state (k, y) is the
  point mass at k, which differs between states with the same Y_t. So
  Γ(Y_t) = ρ(h = 1) bits ([CLAIM-tmppi0xf](CLAIM-tmppi0xf.md)). The high-level noise E′₂ is
  where K went.

**Strong abstraction.** If K is endogenous and every intervention ω_τ
translates is allowed, then K ← k is allowed and maps to the empty
intervention, since every high-level state stays reachable; (K ← 1, H ← 1)
maps to H ← 1. In a context with u_K = 0, H ← 1 gives Y_{t+1} = 0 and
(K ← 1, H ← 1) gives Y_{t+1} = 1, from the same high-level context and the
same high-level intervention, which no τ_U can do. So strong abstraction
rejects the coarse-graining ([NOTE-tmp1bdcu](../notes.d/NOTE-tmp1bdcu.md), Bearing on the record, item 4).
It does so because the hidden parameter can be set, the pattern of Beckers
and Halpern's Examples 3.16 and 3.18, not because states the description
merges respond differently to the governance intervention. With K
exogenous, as A16 has it ("a hidden mechanism parameter"), τ is the identity
on endogenous variables and the coarse model is trivially a strong
abstraction.

**What the papers already contain.** Relativity to a declared intervention
set (Rubenstein et al. §5; Beckers and Halpern's I_L), which is
[CLAIM-tmppi0xf](CLAIM-tmppi0xf.md)'s I; the support caveat (Beckers and Halpern's Examples 3.4
and 3.11, behaviour off the support left unconstrained), which is
[CLAIM-tmppi0xf](CLAIM-tmppi0xf.md)'s restriction to the interventions ρ charges and the states
of positive probability; and a macro variable merging micro-states with
different interventional consequences (Rubenstein et al.'s cholesterol
case). Not contained: exact closure under the ordinary dynamics together
with failure under a mechanism intervention, a state-conditional
deficiency, or Γ's monotonicity under refinement ([CLAIM-tmpshzxc](CLAIM-tmpshzxc.md)); the
papers' transitivity results are a different property.

## What it does not say

- **Not a new theory of causal abstraction.** A25: "We should not present
  governance-preserving coarse-graining as a new general theory of causal
  abstraction." The relation above places a fixed-target
  sufficiency beside the papers' notions; it builds no abstraction of its
  own.
- **Not that the papers are wrong.** Their criteria are about models of
  populations under interventions, and they do what they say. The point is
  that a description can pass them while losing the response of each
  individual state.
- **Not about [TERM-043](../terms.d/TERM-043.md)'s causal component in general.** That component
  compares push-forward laws (a graded form of Rubenstein et al.'s
  Definition 3), so it is zero for this case too; the claim says why the
  governance-response profile is not that component with τ the identity.
- **Not cyclic models, uncountable intervention sets, or more than one
  outcome.** [THEORY-tmpjfhcb](../theory.d/THEORY-tmpjfhcb.md) and [THEORY-tmpjtnjd](../theory.d/THEORY-tmpjtnjd.md) hold under their own
  hypotheses (acyclicity; countability).
