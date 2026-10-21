---
status: Read
paper: LIT-tmp0p7xl
title: 'Beckers, Eberhardt and Halpern — Approximate causal abstraction'
version: 1
history:
- version: 1
  date: '2026-10-21'
  note: >-
    Read in full from arXiv:1906.11583v2 (29 June 2019), titled there
    "Approximate Causal Abstraction", text extracted with pdftotext. Read:
    the abstract, §1 with the El Niño example, §2 (Definitions 2.1–2.6),
    §3 (Definitions 3.1–3.2, Propositions 3.3–3.4), §4 (Definitions
    4.1–4.8, Propositions 4.5–4.6, the comparison with structural
    Hamming and structural intervention distance), §5 (Propositions
    5.1–5.2, Examples 5.3–5.4, Theorems 5.5–5.6), §6 and the appendix
    with every proof. Formulas were garbled by extraction and are
    reconstructed from the prose; Propositions 3.3, 5.1 and 5.2 and
    Example 5.3 are re-derived in THEORY-tmpe391l. The figures were read
    from their captions. The PMLR 115 version was not compared.
date: '2026-10-21'
summary: >-
  Turns τ-abstraction into a graded relation. Given a metric on high-level
  states, the distance of a high-level model from a low-level one is the
  worst case, over allowed interventions and contexts, of how far the
  coarse-grained low-level outcome is from the high-level outcome, for the
  best context map; zero is exact abstraction. Probabilistic versions
  average over contexts and, with an intervention distribution, over the
  low-level ways of implementing each high-level intervention. An
  abstraction followed by an approximation is an approximate abstraction,
  the reverse order costs a distortion factor, and an approximate
  abstraction need not decompose into the two.
---
<!-- inactive-ok-file: TERM-tmpf5k7x TERM-tmpdxajb — Proposed; terms filed from the same exchange that this reading bears on, cited as open -->

# NOTE-tmpqfl95: Beckers, Eberhardt and Halpern — Approximate causal abstraction

## Contribution

It supplies the approximate notion Beckers and Halpern ([LIT-tmp6hpx6](../literature.d/LIT-tmp6hpx6.md)) left as
future work, and with it a distance between causal models that compares
their answers to interventions rather than their graphs. The choice of what
counts as close is left to the user, on purpose. "We maintain that, in
general, high-level models in science are only approximate abstractions."

## Key insight

Approximate abstraction measures, context by context and intervention by
intervention, the gap between two routes to a high-level state: run the
low-level model and coarse-grain, or lift the context and the intervention
and run the high-level model. Everything about what matters is in the
metric on high-level states and in which interventions and contexts are
counted, worst case or on average.

## Assumptions

- Finite signatures; deterministic recursive causal models with allowed
  interventions (Definitions 2.1–2.2); probabilistic models add a
  distribution on contexts.
- **τ-consistency** (Definition 2.4): τ surjective, I_H = ω_τ(I_L), and
  |R_L(U_L)| ≥ |R_H(U_H)|.
- A metric d_V on each model's endogenous states, "typically
  straightforward to define" and left unspecified.
- Theorem 5.5's appendix statement adds that U_L and I_L are finite.

## Key results

- **Definition 2.5.** τ-abstraction: τ-consistent, and a surjective τ_U with
  τ(M_L(u⃗_L, X⃗←x⃗)) = M_H(τ_U(u⃗_L), ω_τ(X⃗←x⃗)) for every context and allowed
  intervention. **Definition 2.6:** constructive when τ is a product over a
  partition of V_L and I_L = I_L^τ.
- **Definition 3.1.** For two similar models (same signature),
  d_max(M₁, M₂) = max over allowed interventions and contexts of
  d_V(M₁(u⃗, X⃗←x⃗), M₂(u⃗, X⃗←x⃗)).
- **Definition 3.2.** For τ-consistent (M_L, M_H),
  d_τ(M_L, M_H) = min over surjective τ_U of max over X⃗←x⃗ ∈ I_L and u⃗_L of
  d_{V_H}(τ(M_L(u⃗_L, X⃗←x⃗)), M_H(τ_U(u⃗_L), ω_τ(X⃗←x⃗))). M_H is a τ-α
  approximate abstraction when d_τ ≤ α. "We take the minimum over all
  functions τ_U because the function that lifts the low-level contexts up to
  the high-level contexts does not play a major role."
- **Propositions 3.3–3.4.** d_τ = 0 iff τ-abstraction; with τ the identity on
  similar models, d_τ is d_max.
- **§4.** Probabilistic d_max averages the distance over contexts (Definition
  4.1); d_β takes the probability of a distance of at least β (Definition
  4.2). Probabilistic τ-abstraction (Definition 4.3) is equality of
  push-forward distributions. Definition 4.4's d_τ is the expected distance
  over Pr_L, worst case over interventions, minimized over τ_U with
  τ_U(Pr_L) = Pr_H. An **intervention distribution** Pr_I (Definition 4.7)
  puts probability on each low-level implementation X⃗←x⃗ of a high-level
  intervention Y⃗←y⃗, positive exactly when ω_τ(X⃗←x⃗) = Y⃗←y⃗; d_τ^{Pr_I}
  (Definition 4.8) is worst case over high-level interventions and expected
  over contexts and implementations. The motivation is Spirtes and Scheines'
  ambiguous manipulations: setting a room to 70°F without superheating one
  corner.
- **Comparison with SID.** Peters and Bühlmann's structural intervention
  distance counts pairs (X, Y) whose interventional distributions differ;
  the authors want arbitrary joint interventions, a size of the difference,
  and models that are not similar.
- **Propositions 5.1–5.2.** A τ-abstraction followed by a d_max-α
  approximation at the high level is a τ-α approximate abstraction. An
  α-approximation at the low level followed by a τ-abstraction is a τ-kα
  one, with k the worst-case ratio of high-level to low-level distances.
- **Examples 5.3–5.4 and Theorems 5.5–5.6.** An approximate abstraction need
  not be an exact abstraction of any model similar to M_L (Example 5.3,
  with τ(a, b, c) = (a ⊕ b, b ⊕ c) and distance √2), nor, even when
  constructive, an approximation of an exact abstraction of M_L (Example
  5.4). Deciding either decomposition is in nondeterministic polynomial
  time in |I_L| × |R_L(U_L)| (Theorem 5.5). For constructive τ an M_L′ similar
  to M_L, of which M_H is an exact abstraction, can be found in polynomial
  time (Theorem 5.6).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | d_τ generalizes both exact abstraction and approximation between similar models | strong | Propositions 3.3–3.4, 4.5–4.6 (immediate from the definitions) |
| C2 | Errors compose: abstraction then approximation gives α; approximation then abstraction gives kα | strong | Propositions 5.1–5.2, proved; k can be undefined (see Limitations) |
| C3 | An approximate abstraction need not decompose into an exact abstraction and an approximation in either order | strong | Examples 5.3–5.4 |
| C4 | For constructive τ the low-level decomposition always exists and is found in polynomial time | strong | Theorem 5.6, proved |
| C5 | The intervention distribution is how knowledge of a high-level intervention's mechanism enters an approximate abstraction | moderate | Definitions 4.7–4.8 and the heater example; no result uses it |
| C6 | High-level scientific models are in general only approximate abstractions | weak, as a thesis | the El Niño example (Chalupka et al. 2016) and the ideal gas law, asserted |

## Concepts

- **Similar models:** same signature, differing only in their equations.
- **τ-consistent pair:** Definition 2.4.
- **Intervention distribution** Pr_I: Definition 4.7.

## Connections

It builds on Beckers and Halpern ([LIT-tmp6hpx6](../literature.d/LIT-tmp6hpx6.md), [NOTE-tmp1bdcu](NOTE-tmp1bdcu.md)) and through
them on Rubenstein et al. ([LIT-tmptzsyg](../literature.d/LIT-tmptzsyg.md), [NOTE-tmp6b7dr](NOTE-tmp6b7dr.md)), on Chalupka,
Bischoff, Perona and Eberhardt (2016) for the El Niño macro variables, and
compares itself with structural Hamming distance (Acid and de Campos 2003)
and structural intervention distance (Peters and Bühlmann 2015).

## Bearing on the record

- **[CLAIM-tmppi0xf](../claims.d/CLAIM-tmppi0xf.md) and [TERM-tmpf5k7x](../terms.d/TERM-tmpf5k7x.md).** The deficiency Γ is not d_τ for any
  choice of metric. d_τ minimizes over τ_U, so the high-level context may
  carry what the coarse endogenous state drops: for the hidden bit
  ([CASE-tmpdc0tl](../cases.d/CASE-tmpdc0tl.md)) the coarse-graining that drops K is an exact τ-abstraction
  when only H is intervened on ([NOTE-tmp1bdcu](NOTE-tmp1bdcu.md), Bearing on the record, item
  3), so d_τ = 0 while Γ(Y_t) = ρ(h = 1) bits. Three further differences:
  d_τ takes the worst case over interventions where Γ averages them by ρ;
  it is a metric distance between states where Γ is a conditional mutual
  information between the micro state and the response given the coarse
  state; and its probabilistic intervention distribution weights the
  low-level implementations of one high-level intervention, where ρ weights
  distinct governance interventions. A16's warning that Γ values under
  different ρ are not on one scale has its counterpart here: d_τ is defined
  relative to the metric, and "the choice of distance function makes a
  crucial difference".
- **[TERM-043](../terms.d/TERM-043.md).** D_causal = Σ_a π(a) d(T_# P_o(Y | do(a)), P_t(Y′ | do(τ(a))))
  sits between this paper's notions. It averages over interventions by π, as
  none of them does; it compares push-forward distributions, as Definition
  4.3 does, rather than context-wise outcomes, as Definitions 3.2 and 4.4
  do. The paper's composition results (C2) are a template for [TERM-043](../terms.d/TERM-043.md)'s
  componentwise comparison of transports composed in sequence, which the
  record has not stated.
- **[QUESTION-005](../questions.d/QUESTION-005.md).** It asks how corresponding interventions can be made
  operational. The intervention distribution is one formal answer for the
  causal component: a high-level intervention corresponds to a declared
  distribution over its low-level implementations, positive only on those ω_τ
  sends to it. It does not say where the distribution comes from, which is
  the question's worry.
- **[TERM-tmpdxajb](../terms.d/TERM-tmpdxajb.md).** The metric d_V and the gender/height example ("One
  researcher might not be interested in gender ... another researcher might
  care about gender and not about height") are the regime's query family and
  tolerance in another notation; d_τ ≤ α is Adequate(T; …, ε) with ε = α.
- **[CLAIM-tmpshzxc](../claims.d/CLAIM-tmpshzxc.md).** Nothing here orders d_τ along refinements of τ; the
  monotonicity of Γ has no counterpart in this paper.

No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **k in Proposition 5.2 can be undefined.** It is a maximum of a ratio
  whose denominator is d_{V_L} between M_L′ and M_L, zero wherever they
  agree; the statement does not say how such terms count.
- **Slips.** Example 5.3 concludes "Thus, M_H cannot be recursive" where the
  argument shows that no M_L′ can be. The caption of Fig. 4 speaks of "the
  distance between the expectations of these distributions", while
  Definition 4.8 takes an expectation of distances. Proposition 5.2's
  conclusion writes (M_L′, I_L′) for a model whose interventions are I_L.
- **No guidance on the metric,** deliberately. A small d_τ under one metric
  says nothing under another.
- **Worst case over interventions,** even in the probabilistic version, so a
  single rare intervention can dominate; the intervention distribution
  averages only within one high-level intervention.
- **The context map is free** (up to surjectivity and the cardinality bound),
  as in Beckers and Halpern.
- **No estimation.** Nothing is said about computing d_τ from data, and
  Theorem 5.5's procedure is a guess-and-check over context maps.

## Open questions

- With τ_U required to factor through τ, what is the graded notion, and is
  it Γ-like? For the hidden bit it would be positive where d_τ is zero.
- Does d_τ, or a variant, decrease along refinements of τ, as Γ does for a
  fixed target?
