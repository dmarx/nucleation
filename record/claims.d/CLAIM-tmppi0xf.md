---
status: Active
title: 'A coarse-graining exactly informationally closed under a process''s ordinary dynamics need not preserve its responses to an intervention on the mechanism: for a declared intervention distribution ρ, independent of the state, the deficiency Γ = I(S; Y^(I) | T(S), I) can be positive, as in the hidden governance bit, where it is ρ(h = 1) bits; and Γ = 0 exactly when, for every intervention ρ charges, the response kernels are constant on T''s fibres over the states of positive probability'
version: 2
history:
- version: 2
  date: '2026-10-21'
  note: >-
    The readings of 2026-10-21 added: the causal-abstraction papers hold
    the declared intervention set, the support caveat and the qualitative
    merge, and accept the hidden-bit coarse-graining (THEORY-tmpjfhcb,
    added to grounds; CLAIM-tmp4r4mi); and Szeidl and Szucs's model as a
    social-science instance of the shape. The claim is unchanged.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the construction: the output Y_t of CASE-tmpdc0tl is not
  informationally closed under h = 0, or Γ(Y_t) differs from ρ(h = 1)
  bits; or, for an intervention distribution independent of the state, a
  Γ = 0 with a ρ-charged intervention whose response kernels differ
  between two states of positive probability with equal T, or a Γ > 0
  with every such kernel constant on T's fibres.
tags:
- causality
- information-theory
- self-governance
date: '2026-10-21'
line:
- formal-apparatus
- will-organization
rests_on:
- CLAIM-350
grounds:
- THEORY-820
- THEORY-424
- CASE-tmpdc0tl
- THEORY-tmpjfhcb
uses:
- TERM-tmpf5k7x
- TERM-023
summary: >-
  A16 §3–4 of the exchange of 2026-10-20 and A17 §4.2–4.3, its paper's
  Proposition 1, reused at A18 and in A23's audit. A16: "a representation
  can be perfectly informationally closed under the ordinary dynamics
  while failing to preserve a governance-relevant counterfactual
  distinction." The witness is [CASE-tmpdc0tl](../cases.d/CASE-tmpdc0tl.md); the proof is in the body,
  checked exactly on 2026-10-21. The qualitative point was on file:
  [CLAIM-350](CLAIM-350.md)'s "What it does not say" (A22's Construction B of 2026-10-17,
  [CLAIM-127](CLAIM-127.md)), and [CLAIM-122](CLAIM-122.md)'s supervisory test, whose note of 2026-10-18
  has it without parameters. New here are the parameters, the deficiency
  Γ and the exact condition for Γ = 0. It is an application of ordinary
  causal sufficiency, not new information theory, and it does not say
  the system governs itself.
illustrated_by:
- CASE-tmpdc0tl
supports:
- CLAIM-tmpshzxc
- CLAIM-tmp4r4mi
---
<!-- inactive-ok-file: CLAIM-122 CLAIM-127 — Proposed; the earlier, unparameterized appearances of this result, cited as its history, nothing here rests on them -->
<!-- inactive-ok-file: CLAIM-336 CLAIM-174 — Proposed; named as what this result does not test, open -->
<!-- inactive-ok-file: THEORY-tmplydnj — Proposed; Szeidl and Szucs's structural split, cited as an instance of the shape, nothing rests on it -->

# CLAIM-tmppi0xf: A coarse-graining exactly informationally closed under a process's ordinary dynamics need not preserve its responses to an intervention on the mechanism: for a declared intervention distribution ρ, independent of the state, the deficiency Γ = I(S; Y^(I) | T(S), I) can be positive, as in the hidden governance bit, where it is ρ(h = 1) bits; and Γ = 0 exactly when, for every intervention ρ charges, the response kernels are constant on T's fibres over the states of positive probability

## The claim

A16 §3: "**A representation can be perfectly informationally closed under
the ordinary dynamics while failing to preserve a governance-relevant
counterfactual distinction.**" A17 §4.2, its Proposition 1: "There exists a
stationary finite-state stochastic system and a spatial coarse-graining
that is exactly informationally closed under its ordinary dynamics, yet
fails to preserve the response profile for a specified intervention on a
governance mechanism."

**The terms.** S is the state, with a law P. I is a family of
interventions, drawn by a declared ρ independently of S. Y^(i) is the
outcome under intervention i, with response kernel
K_i(y | s) = P(Y^(i) = y | S = s). The profile of s is
J_I(s) = (K_i(· | s))_{i∈I} ([TERM-tmpf5k7x](../terms.d/TERM-tmpf5k7x.md)). A16 §4's deficiency of a
coarse-graining T = f(S) is

Γ_ρ(T) = I(S; Y^(I) | T(S), I) = H(Y^(I) | T(S), I) − H(Y^(I) | S, I).

**The witness** ([CASE-tmpdc0tl](../cases.d/CASE-tmpdc0tl.md)). S_t = (K, Y_t), K a fair bit fixed in
time, Y_{t+1} fresh fair noise under h = 0 and Y_{t+1} = K under h = 1;
T = Y_t.

- *Closed.* Under h = 0, Y_{t+1} is independent of every past, so
  I(S_{≤t}; Y_{t+1} | Y_{≤t}) = 0. By [THEORY-820](../theory.d/THEORY-820.md) (a) that is closure at
  every horizon.
- *Γ = ρ(h = 1).* Under h = 0 the response is independent of S, so its
  term is 0. Under h = 1 it is K, with H(K | Y_t) = 1 bit and H(K | S) = 0.
  Averaging, Γ(Y_t) = ρ(h = 1), which is 0.5 bit at A16's ρ = ½.

**When Γ = 0.** Since I is independent of S,
Γ = Σ_i ρ(i) I(S; Y^(i) | T(S)). Each term is non-negative, and zero exactly
when Y^(i) is independent of S given T(S), that is, when K_i(· | s) =
K_i(· | s′) for all s, s′ of positive probability with T(s) = T(s′). So
Γ = 0 is [CLAIM-350](CLAIM-350.md)'s factorization of J_I through T (its probabilistic
version), **for the interventions ρ charges and on the states of positive
probability**, and no more. A17's Appendix A asks for exactly these
"support assumptions under which \(\Gamma=0\) is equivalent to exact
response-profile preservation". With ρ(h = 1) = 0, Γ = 0 for a constant T
while the profile does not factor through it.

**Checked** on 2026-10-21 by exact enumeration of the joint law of
(K, Y_t, h, Y_{t+1}): closure 0 at one to three steps of history; Γ(Y_t) =
Γ(constant) = 0, 0.25, 0.5 and 1 bit for ρ(h = 1) = 0, ¼, ½ and 1;
Γ(K) = Γ((K, Y_t)) = 0 throughout; and the ρ = 0 case above.

## Where it was before

- **[CLAIM-350](CLAIM-350.md)'s "What it does not say":** "That observational adequacy is
  causal adequacy. A state space with a distribution can satisfy the
  probabilistic version while interventions tell its merged states apart
  (A22's Construction B; [CLAIM-127](CLAIM-127.md))." Its causal bullet defines
  intervention-consistent coarse-graining "for a declared family of
  interventions" as a definition, not a theorem. That is this claim's
  qualitative point, on file since the exchange of 2026-10-17.
- **[CLAIM-122](CLAIM-122.md)'s note of 2026-10-18.** A7 §5's supervisory test and A12's
  Proposition 2 of 2026-10-17 ("Construct two systems whose default action
  trajectories are identical"), of which the note says "No parameters were
  given." A15 §1 of 2026-10-20 cited the test, and A15 §2 built it as a
  counterexample. A17 then listed it as "Established by the paper's
  self-contained finite counterexample" without the note.
- **The causal-abstraction literature**, read on 2026-10-21 ([NOTE-tmp6b7dr](../notes.d/NOTE-tmp6b7dr.md),
  [NOTE-tmp1bdcu](../notes.d/NOTE-tmp1bdcu.md), [NOTE-tmpqfl95](../notes.d/NOTE-tmpqfl95.md)). It has relativity to a declared
  intervention set (Rubenstein et al. §5; Beckers and Halpern's I_L), which
  is this claim's I; the support caveat (Beckers and Halpern's Examples 3.4
  and 3.11 leave behaviour off the support unconstrained), which is this
  claim's restriction to the interventions ρ charges and the states of
  positive probability; and a macro variable merging micro-states with
  different interventional consequences (Rubenstein et al.'s cholesterol
  case). It does not have this claim: its criteria compare interventional
  laws, and exact transformation, τ-abstraction and zero approximate
  distance all accept the hidden-bit coarse-graining ([THEORY-tmpjfhcb](../theory.d/THEORY-tmpjfhcb.md),
  [THEORY-tmpjtnjd](../theory.d/THEORY-tmpjtnjd.md), [THEORY-tmpe391l](../theory.d/THEORY-tmpe391l.md)). How sufficiency sits beside them is
  [CLAIM-tmp4r4mi](CLAIM-tmp4r4mi.md).
- **An instance of the shape outside the record.** Szeidl and Szucs's
  model of media capture ([THEORY-tmpwiydx](../theory.d/THEORY-tmpwiydx.md), [NOTE-tmpefpic](../notes.d/NOTE-tmpefpic.md)): the observed
  slant gap can be the same whether it comes from owners' ideology or from
  favor exchange, and a ban on targeted government advertising, an
  intervention on the mechanism, tells them apart ([THEORY-tmplydnj](../theory.d/THEORY-tmplydnj.md)). The
  join is the record's; the paper says nothing of closure or of Γ.

## What it does not say

- **Nothing new as information theory.** A17: "This is a deliberately
  restricted application of ordinary causal sufficiency: the interventions
  have been selected because they concern governance. We should not
  advertise it as a wholly new mathematical concept."
- **Not that Γ can be had from passive data.** A16: "Ordinary passive data
  may not identify \(\Gamma\)."
- **Not a contradiction of [THEORY-820](../theory.d/THEORY-820.md),** which says closure is "Not
  interventional causation unless X is fully observed".
- **Not a measure of will, or a showing of agency** ([CLAIM-116](CLAIM-116.md)). A16: "Nor
  does the example establish agency. \(K\) is simply a hidden mechanism
  parameter."
- **Not that the system governs itself.** The profile records how the
  system would respond if its governance were set from outside,
  P(Y | do(G = g)). A27 §3 of the same exchange: "That is not the same as
  establishing that the system can alter the mechanism itself. An ordinary
  machine can respond dramatically to a technician rewiring it." Whether
  the system produces its own transitions of governance is [CLAIM-174](CLAIM-174.md)'s
  third condition (its policy would adapt if its actions' consequences
  changed), not something Γ measures. A15 §6 had the same limit: identifying
  the causal mechanism of governance "does not settle whether its
  authority is endogenous, historically uncoerced, contestable, or
  normatively justified." Neither establishes ownership ([CLAIM-022](CLAIM-022.md),
  [QUESTION-071](../questions.d/QUESTION-071.md)).
- **Not an instance of causal abstraction, nor a new theory of it.** A25:
  "We should not present governance-preserving coarse-graining as a new
  general theory of causal abstraction." That stands, and the papers'
  notions do not imply the condition for Γ = 0 ([CLAIM-tmp4r4mi](CLAIM-tmp4r4mi.md)).
- **Not a test of [CLAIM-336](CLAIM-336.md).** The construction has no meaning dynamics.
- **Not one scale across regimes.** A16 §5: "one must not compare
  deficiencies numerically across different intervention distributions or
  outcome targets as though they were measurements on a common scale."
