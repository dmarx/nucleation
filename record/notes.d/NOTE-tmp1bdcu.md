---
status: Read
paper: LIT-tmp6hpx6
title: 'Beckers and Halpern — Abstracting causal models'
version: 1
history:
- version: 1
  date: '2026-10-21'
  note: >-
    Read in full from arXiv:1812.03789v4 (9 July 2019, the latest
    version, which carries the AAAI-19 copyright line), text extracted
    with pdftotext. Read: the abstract, §1, §2 (Definitions 2.1–2.3,
    Lemma 2.4), §3.1–3.4 (Definitions 3.1, 3.5, 3.7, 3.12, 3.13, 3.15,
    3.19; Proposition 3.6; Theorems 3.8–3.9; Proposition 3.14; Examples
    3.2–3.4, 3.10, 3.11, 3.16–3.18), §4 and the appendix with every proof.
    Subscripts and arrows were garbled by extraction and are reconstructed
    from the prose. Theorem 3.8 is re-derived in THEORY-tmpjtnjd. The
    AAAI typeset version was not compared.
date: '2026-10-21'
summary: >-
  Shows that Rubenstein et al.'s exact transformation is too permissive,
  because a distribution or a sparse intervention set can hide essential
  differences, and strengthens it in four steps: uniform transformation
  (exact for every distribution, equivalent to a map on contexts that
  commutes with every allowed intervention), τ-abstraction (τ surjective,
  the map on interventions fixed by τ), strong abstraction (every
  intervention τ can translate is allowed) and constructive abstraction
  (τ acts variable-cluster by variable-cluster), which it says all three
  of Rubenstein et al.'s examples are.
---
<!-- inactive-ok-file: CLAIM-122 — Proposed; the supervisory test this reading bears on, open -->
<!-- inactive-ok-file: LIT-038 — Rejected; named only for its status note's pointer to Beckers–Halpern -->

# NOTE-tmp1bdcu: Beckers and Halpern — Abstracting causal models

## Contribution

It takes the question "when is a high-level causal model a faithful
abstraction of a low-level one?" from a single definition to a ladder of
definitions, each closing a loophole the previous one leaves, with an
example for each loophole. It identifies the two sources of permissiveness
in exact transformation: "because RW+ consider probabilistic causal models,
some differences that are intuitively significant are overlooked by
considering just the right distributions. Second, besides a function that
maps low-level states to high-level states, RW+ define a separate mapping
of interventions that can mask what we view as essential differences". It
characterizes the first strengthening exactly (Theorem 3.8).

## Key insight

Making exactness hold for every distribution on contexts turns a statement
about distributions into a statement about individual contexts: there must
be a map τ_U on contexts such that, for every context u and allowed
intervention i, coarse-graining the low-level outcome gives the high-level
outcome in context τ_U(u). The map τ_U is existential. The high-level model
may have exogenous variables of its own, and they may carry whatever
low-level detail the endogenous coarse-graining τ drops.

## Assumptions

- Deterministic, recursive (acyclic) causal models M = (S, F, I) with
  signature (U, V, R), a set I of allowed perfect interventions X⃗ ← x⃗ with
  the natural order, and, for the probabilistic notions, a probability on
  contexts R(U). Recursiveness is "only to simplify the exposition";
  footnote 1 says unique solvability would do.
- Rubenstein et al.'s unique-exogenous-variable assumption is shown to be
  harmless in the probabilistic setting (Lemma 2.4) and is not assumed
  otherwise.
- Proposition 3.6 needs I_L countable.

## Key results

- **Definition 3.1.** Rubenstein et al.'s exact (τ-ω)-transformation,
  restated: Pr_H^{ω(Y⃗←y⃗)} = τ(Pr_L^{Y⃗←y⃗}) for every allowed low-level
  intervention.
- **Example 3.4.** Two unrelated models, each with only the empty
  intervention and a point-mass distribution, are exact transformations of
  each other. "a high-level model M_H can be arbitrary in contexts that do
  not lead to settings v⃗_H that have positive probability for some allowed
  low-level intervention."
- **Definition 3.5 (uniform transformation).** For every Pr_L there is a
  Pr_H making the pair exact.
- **Proposition 3.6 and Theorem 3.8.** With I_L countable, M_H is a uniform
  (τ-ω)-transformation of M_L iff there is τ_U : R_L(U_L) → R_H(U_H)
  compatible with τ: τ(M_L(u⃗_L, Y⃗←y⃗)) = M_H(τ_U(u⃗_L), ω(Y⃗←y⃗)) for all u⃗_L and
  allowed interventions; and then Pr_H can be taken to be τ_U(Pr_L).
  **Theorem 3.9:** uniform transformations compose.
- **Examples 3.10–3.11.** Uniformity still lets M₁ and M₂ be abstractions of
  each other when ω is chosen freely (X₁ ← x₁ mapped to
  (X₁, X₂) ← (x₁, x₁)), and lets the high level be more detailed than the low
  (a new variable X* that, with Pr(U* = 0) = 0, switches every equation to
  arbitrary behaviour only off the support).
- **Definition 3.12 (ω_τ).** τ fixes the map on interventions:
  ω_τ(X⃗←x⃗) = Y⃗←y⃗ when τ(Rst(V_L, x⃗)) = Rst(V_H, y⃗), and is undefined
  otherwise. **Definition 3.13 (τ-abstraction):** τ surjective, a surjective
  τ_U compatible with τ, and I_H = ω_τ(I_L). **Proposition 3.14:** a
  τ-abstraction is a uniform (τ, ω_τ)-transformation.
- **Definition 3.15 (strong τ-abstraction).** I_H is every high-level
  intervention and I_L is every low-level intervention on which ω_τ is
  defined. **Example 3.16:** energy from (velocity, height, mass) is not a
  strong abstraction, because M ← m maps to the empty high-level
  intervention (every energy pair is still reachable) while changing the
  outcome; dropping such interventions gives a τ-abstraction. **Example
  3.17:** counts of black pixels in the upper and left halves can only be
  set jointly; **Example 3.18:** τ(x₁, x₂, x₃) = (x₁ ∨ x₃, x₂ ∨ x₃) sends both
  X₃ ← 0 and the empty intervention to the empty one, with different
  effects.
- **Definition 3.19 (constructive abstraction).** A strong τ-abstraction in
  which τ is a product of maps on the cells of a partition of V_L, one cell
  per high-level variable plus one marginalised away. Rubenstein et al.'s
  three examples are constructive; that every strong abstraction is
  constructive under "a few minor technical conditions" is conjectured.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Exact transformation is too permissive: suitable distributions or intervention maps let models that differ essentially be exact transformations of each other | strong | Examples 3.4, 3.10, 3.11 |
| C2 | Exactness for every distribution is equivalent to a context map commuting with every allowed intervention | strong, given countable I_L | Proposition 3.6 and Theorem 3.8, proved; re-derived in [THEORY-tmpjtnjd](../theory.d/THEORY-tmpjtnjd.md) |
| C3 | Letting τ determine the map on interventions, and requiring τ surjective, removes the remaining counterexamples | moderate | Definitions 3.12–3.13; checked against Examples 3.10–3.11 |
| C4 | Strong abstraction is the clean relation between basic causal models, but some useful abstractions are only τ-abstractions | strong by example | Examples 3.16–3.18 |
| C5 | Combining micro-variables into macro-variables is constructive abstraction, and all of Rubenstein et al.'s examples are constructive | moderate | asserted for their examples; shown in detail for Example 3.3 only |
| C6 | Every strong abstraction is constructive up to minor conditions | weak | conjecture, "we have not proved this result yet" |

## Concepts

- **Context**: a setting u⃗ of all exogenous variables. A deterministic model
  maps (context, intervention) to a state, M(u⃗, X⃗←x⃗).
- **Allowed interventions** I: those "we care about for some reason or
  other", for example "the interventions that involve variables and values
  that are under our control".
- **Compatible context map** τ_U: commutes with every allowed intervention
  as in Theorem 3.8.
- **Rst(V, x⃗)**: the states of V that agree with x⃗ on the intervened
  variables; ω_τ sends X⃗←x⃗ to the high-level intervention whose Rst is the
  image of this one.

## Connections

It builds directly on Rubenstein et al. ([LIT-tmptzsyg](../literature.d/LIT-tmptzsyg.md), [NOTE-tmp6b7dr](NOTE-tmp6b7dr.md)), whose
Definition 3 is its starting point, and on Halpern (2016) and Halpern and
Pearl (2005) for the models. It cites Chalupka, Eberhardt and Perona
(2015, 2016) and Iwasaki and Simon (1994) for clustering micro-variables.
Its "approximate abstraction" future work is [LIT-tmp0p7xl](../literature.d/LIT-tmp0p7xl.md) ([NOTE-tmpqfl95](NOTE-tmpqfl95.md)).
[LIT-038](../literature.d/LIT-038.md)'s status note sends a reader wanting causal abstraction here, and
this reading confirms the pointer.

## Bearing on the record

**Governance-response sufficiency and the τ-abstraction ladder**
([CLAIM-tmppi0xf](../claims.d/CLAIM-tmppi0xf.md), [CLAIM-tmpshzxc](../claims.d/CLAIM-tmpshzxc.md), [TERM-tmpf5k7x](../terms.d/TERM-tmpf5k7x.md)). What follows is the
record's derivation; the paper does not treat governance or a deficiency.

1. *The exact relation.* Take the low-level context to be the
   pre-intervention micro state S (with any further noise independent of S),
   the outcome Y, the allowed interventions the declared governance family
   I, and ω the identity on I. In the deterministic case, governance-response
   sufficiency of T = f(S) is exactly Theorem 3.8(b)'s compatibility
   condition, compared on Y, with the context map required to be T itself:
   Y^(i)(s) = g_i(T(s)) for every s and i, that is,
   τ(M_L(s, i)) = M_H(τ_U(s), i) with τ_U = T. In the probabilistic case it
   is the kernel form: P(Y^(i) | S = s) = G_i(· | T(s)), a high-level model
   whose context is T and whose remaining noise is independent of S given T.
2. *So it is not a special case of exact transformation, uniform
   transformation or τ-abstraction, nor they of it.* It is stronger in one
   respect: Theorem 3.8 only asks that some τ_U exist, and τ_U may encode
   what T drops into high-level exogenous variables. It is weaker in others:
   no high-level structural model need exist beyond the kernels g_i or G_i,
   nothing is required of composed interventions, only one outcome is
   compared, and (for Γ) only states of positive probability and the
   interventions ρ charges.
3. *The hidden bit passes every rung up to τ-abstraction.* In [CASE-tmpdc0tl](../cases.d/CASE-tmpdc0tl.md),
   with K an endogenous variable fixed by U_K and interventions on H only,
   τ dropping K is a τ-abstraction: take τ_U(u) = (u_t, u_H, (u_K, u_{t+1})),
   and let the high level read Y_{t+1} from the first or second component of
   its noise according to H. With K exogenous instead (a "hidden mechanism
   parameter", as A16 calls it), τ is the identity on endogenous variables
   and the model is trivially a strong, indeed constructive, abstraction of
   itself. Either way Γ(Y_t) = ρ(h = 1) bits.
4. *Strong abstraction catches it only through interventions on K.* If K is
   endogenous and every intervention ω_τ translates is allowed, then
   K ← k is allowed and ω_τ(K ← k) is the empty intervention, since every
   high-level state is still reachable; likewise (K ← k, H ← 1) maps to
   H ← 1. For a context with u_K = 0, H ← 1 must give Y_{t+1} = 0 and
   (K ← 1, H ← 1) must give Y_{t+1} = 1 from the same high-level context and
   the same high-level intervention, which no τ_U can do. That is Example
   3.16's pattern (mass) and Example 3.18's (X₃), not the governance point:
   it fails because the parameter can be set, not because states that the
   coarse description merges respond differently to the governance
   intervention.
5. *What the ladder already contains.* The relativity to a declared
   intervention set (Rubenstein et al., and here I_L); the support caveat
   (Example 3.4 and 3.11's behaviour off the support, which is
   [CLAIM-tmppi0xf](../claims.d/CLAIM-tmppi0xf.md)'s "for every intervention ρ charges ... over the states of
   positive probability", and the case ρ(h = 1) = 0); and a macro variable
   merging micro-states with different interventional consequences
   (Rubenstein et al.'s cholesterol case). What it does not contain:
   exact informational closure under the ordinary dynamics together with
   failure for a mechanism intervention, a state-conditional deficiency, or
   Γ's monotonicity under refinement ([CLAIM-tmpshzxc](../claims.d/CLAIM-tmpshzxc.md)); Theorem 3.9's
   composition is a different property.

The consolidator may want this filed as a demonstrated CLAIM; the text is
proposed in the batch report.

- **[TERM-043](../terms.d/TERM-043.md).** Its D_causal is a graded form of Definition 3.1 (see
  [NOTE-tmp6b7dr](NOTE-tmp6b7dr.md)), so it inherits Example 3.4's permissiveness and, like
  Definition 3.1, is zero for the hidden bit.
- **[CLAIM-350](../claims.d/CLAIM-350.md).** Its fibre-wise factorization is the deterministic shape of
  item 1, with T the coarse map and the judgment the response; the paper's
  compatibility condition is the same shape one level up, on contexts.
- **[THEORY-243](../theory.d/THEORY-243.md).** Interchange-intervention tests of a network against a
  causal model are tests of a constructive abstraction's commuting
  condition on chosen inputs; [THEORY-243](../theory.d/THEORY-243.md)'s identifiability gap is a case
  where two alignments both satisfy it.
- **[CLAIM-122](../claims.d/CLAIM-122.md).** Its supervisory test ("intervene on the governance
  relations") is a declared I in the paper's sense; the paper's ladder says
  that whether a coarse model passes depends on whether the test's own
  interventions, or also interventions on the governance parameters, are
  allowed.
- **[TERM-tmpdxajb](../terms.d/TERM-tmpdxajb.md).** Allowed interventions are one coordinate of the regime;
  the ladder shows that how the interventions are fixed (chosen freely,
  fixed by τ, or all that τ can translate) is a further choice the regime
  must state.

No instruction for machine-learning practice; nothing for the anthology. The
paper names explainable AI as a motivation in one sentence.

## Limitations

- **Theorem 3.8 omits a hypothesis its proof uses.** The (a)⇒(b) direction
  goes through Proposition 3.6, which assumes I_L countable; the theorem is
  stated without it.
- **Slips.** In Example 3.11, "regardless of how the equations in M₄ are
  defined if X* = 1" should read X* = 0, the case where they are arbitrary.
  The appendix proof headed "Proof of Theorem 3.3" proves Proposition 3.14.
- **C5 is shown for one example.** Only Example 3.3 is worked as a
  constructive abstraction; the other two of Rubenstein et al.'s are
  asserted.
- **Deterministic and exact.** Probabilities enter only through Definition
  3.1 and uniformity; approximation is left to future work.
- **Perfect interventions only.** A change of mechanism must be modelled as
  setting a variable.
- **The context map is unconstrained** beyond surjectivity (and, in the
  sequel paper, a cardinality bound), which is what lets high-level
  exogenous variables hold low-level detail.

## Open questions

- C6: is every strong abstraction constructive, and under which
  conditions?
- Which notion of abstraction results if τ_U is required to factor through
  τ, so that the high-level context holds nothing the coarse state does not?
  Item 1 above says that for one outcome and identity ω it is
  governance-response sufficiency.
