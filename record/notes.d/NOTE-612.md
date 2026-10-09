---
number: 612
status: Read
formerly:
- NOTE-tmp98pr8
paper: 'LIT-808'
title: 'The Topology of Causality'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read from the arXiv v2 PDF (2303.07148v2, 27 July 2023, 85 pages),
    extracted with pdftotext. Read in full: Section 1 (introduction and
    background on contextuality), Sections 2.1–2.5 (causal functions in
    the tight complete and general cases, the presheaf of causal
    functions, empirical models and covers, causally-induced
    contextuality, no non-locality on switch spaces, inseparable
    functions), the Leggett–Garg and BFW examples (2.6.4–2.6.5), and the
    reference list. Skimmed: the causal fork, classical switch and causal
    cross examples (2.6.1–2.6.3), whose tables lost their layout. Not
    read: the proofs in 2.7. Statements are taken as proved by the paper
    and are not checked here. The worked example of a non-gluing pair on
    Θ₃ was followed step by step.
date: '2026-10-09'
summary: >-
  Builds the sheaf-theoretic framework for causality over spaces of
  input histories: causal functions are free assignments of outputs to
  tip events, causality is continuity in the lowerset topology, and the
  presheaf of causal functions is a sheaf exactly when the space has no
  "solipsistic contextuality" (always when tight). Empirical models are
  compatible families on any open cover; standard empirical models on
  causal switch spaces, including total orders, are always local.
---

<!-- inactive-ok-file: LIT-813 — Superseded; the withdrawn predecessor whose construction this paper redoes -->
<!-- inactive-ok-file: THEORY-171 — Proposed; the account this reading is the source of -->
<!-- inactive-ok-file: THEORY-165 — Proposed; named to say this reading does not bear on it -->

# NOTE-612: The Topology of Causality

## Contribution

It extends the Abramsky–Brandenburger sheaf framework from no-signalling
scenarios to arbitrary causal structure: definite, indefinite, and
dynamical, where the order depends on inputs. The causal structure is a
space of input histories ([LIT-800](../literature.d/LIT-800.md)). Causality is shown to be
continuity, causal functions form a presheaf, and empirical models are
compatible families of distributions on arbitrary open covers. Two new
facts follow. Causal constraints can themselves make deterministic local
data unglueable, so the presheaf of causal functions is not always a sheaf.
And on causal switch spaces, total orders included, no standard empirical
model is non-local.

## Key insight

Make the space of input histories a topological space with the lowerset
topology, and a causal function is just a continuous one. All of
Abramsky–Brandenburger's machinery (contexts as opens, empirical models as
compatible families, contextuality as failure of a global section) then
applies with "no-signalling" replaced by "this causal structure". The new
twist is that different contexts can now carry different causal structures.
Then even deterministic assignments that are causal in every context can
fail to be causal together.

## Assumptions

- Finite events, inputs and outputs. A space of input histories as in
  [LIT-800](../literature.d/LIT-800.md). Most results do not need causal completeness or tightness,
  but some do, and the statements say which.
- Distributions are finitely supported and valued in ℝ⁺. The definitions
  extend to commutative semirings (Remark 2.8), but only the probabilistic
  case is developed.
- A cover is a maximal antichain of opens covering the space
  (Definition 2.29). This is narrower than an arbitrary open cover.
- Theorem 2.34's sheaf condition needs at least two outputs at every
  event.

## Key results

- **Proposition 2.1.** On order-induced spaces, causal joint IO functions
  are exactly F(k)_ω = G_ω(k|_{ω↓}).
- **Theorems 2.3 and 2.14, Propositions 2.4 and 2.16.** Causal functions
  correspond one-to-one to free maps from histories to outputs at their
  tips, modulo tip-equivalence (∼_ω) in non-tight spaces. They also
  correspond to extended functions satisfying the consistency (equivalently
  gluing) condition, and to causal joint IO functions.
- **Theorem 2.9.** A causal function is inseparable (arises from no causally
  complete refinement) iff it has an inseparability witness. Example:
  on total(A, {B, C}) with binary inputs, 50,176 of 262,144 causal functions
  are separable.
- **Theorems 2.17–2.19.** CausFun factors over parallel composition (a
  product), sequential composition (a product with a family indexed by the
  first space's maximal histories) and conditional sequential composition.
- **Theorem 2.26.** An extended function is causal iff it is continuous
  Ext(Θ) → PFun(O) for the lowerset topologies. Proposition 2.22: for
  partial orders, continuity in the lowerset topology is monotonicity.
- **Theorem 2.30.** CausFun(Λ(Θ), O) is a separated presheaf. A compatible
  family has a gluing iff its compatible join is causal.
- **Theorem 2.34.** With |O_ω| ≥ 2 for all ω, the presheaf is a sheaf iff
  Θ admits no solipsistic contextuality, and in particular whenever Θ is
  tight. Proposition 2.33 characterises solipsistic contextuality as a
  pair of tip-equivalent histories whose minimal common extensions are not
  all histories.
- **Proposition 2.42.** Covers form a lattice, with SolCov ⪯ StdCov ⪯
  ClsCov.
- **Theorem 2.48, Corollaries 2.47 and 2.50.** A solipsistic contextuality
  witness yields a deterministic solipsistic empirical model that does not
  extend to a standard one. If the presheaf is a sheaf, every deterministic
  model is globally deterministic. Deterministic standard models are always
  globally deterministic.
- **Theorem 2.51, Corollary 2.52.** Every standard empirical model on a
  non-empty causal switch space is local.
- **Proposition 2.54.** On spaces built by composition from indiscrete
  ones, a local model that is a mixture of models each lifting to a causal
  completion is local in a causally separable way. The paper shows the
  converse fails.
- **Examples.** Leggett–Garg: local on total(A, B, C), with an explicit
  12-function decomposition. The model also lifts to a causally complete
  refinement that encodes "no measurement on input 0", but it is not an
  empirical model for two of the three indefinite orders that the paper
  reads macro-realism as imposing. BFW: a 50–50 mixture of two inseparable
  causal functions (circular identity and circular bit-flip) on the
  indiscrete space.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Causality for extended functions is continuity in the lowerset topology | strong (proof, not checked) | Theorem 2.26 |
| C2 | Causal functions form a separated presheaf that is a sheaf iff the space has no solipsistic contextuality; tight spaces always give a sheaf | strong (proof, not checked) | Theorems 2.30, 2.34; worked non-gluing example on Θ₃ followed |
| C3 | Most causally complete 3-event binary spaces (1767 of 2644) admit solipsistic contextuality | moderate (computation, stated in the introduction) | not reproduced; no table of the 1767 in the main text |
| C4 | Standard empirical models on causal switch spaces, total orders included, are always local | strong (proof, not checked) | Theorem 2.51 |
| C5 | The Leggett–Garg violation is a failure of no-signalling constraints, not contextuality | moderate | Theorem 2.51 plus the paper's reading of macro-realism as causal constraints (2.6.4) |
| C6 | Local and causally separable does not imply local in a causally separable way | conjecture, here only in one direction | Proposition 2.54; Conjecture 2.30 of [LIT-788](../literature.d/LIT-788.md) |

## Method

Order theory and sheaf theory. Spaces are given the lowerset topology,
causal data are sections of presheaves over it, and probabilistic data come
from the distribution monad applied to those presheaves. Contextuality is
then the failure of a compatible family to extend to a coarser cover.
Factorisation results are proved by composing spaces, and the examples
compute decompositions into causal functions by hand or linear
programming.

## Concepts

- **causal function**: a map from input histories to outputs at their
  tips, with tip-equivalent histories forced to agree.
- **extended causal function**: its gluing over extended histories, which
  assigns outputs to every event in an extended history's domain.
- **lowerset topology**: the opens of a poset are its lowersets. It is the
  dual of the Alexandrov topology.
- **solipsistic contextuality**: the existence of contexts whose causal
  structures are incompatible, so that locally causal deterministic data
  cannot be glued. Witnessed by a quadruple (k, ω, h, h′).
- **covers**: maximal antichains of opens. *Standard*: the downsets of
  maximal extended histories. *Fully solipsistic*: the downsets of maximal
  histories. *Classical*: the whole space.
- **empirical model**: a compatible family of distributions over extended
  causal functions on a cover.
- **local / non-contextual**: the restriction of a classical empirical
  model.
- **separable causal function**: one arising from a causal function on a
  causally complete refinement.

## Connections

It extends Abramsky and Brandenburger ([LIT-016](../literature.d/LIT-016.md)), to which it reduces on the
discrete space, where causal functions are the "sheaf of events". It
adopts the contextual fraction and related machinery from that line. It
recovers, in this framework, the known result that processes not violating
causal inequalities are local when mixtures of fixed or dynamical total
orders are allowed. It reinterprets Leggett and Garg's macro-realism. It
sets its framework apart from Spekkens's operational contextuality and from
ontological treatments of contextuality in time and indefinite causality.
It redoes, over a new base, the construction of the authors' withdrawn
[LIT-813](../literature.d/LIT-813.md), which it does not cite.

## Bearing on the record

- **[LIT-813](../literature.d/LIT-813.md).** This paper carries the withdrawn paper's content. Its
  Proposition 21 (local iff a mixture of deterministic causal functions)
  reappears as the definition of noncontextual via the classical cover. Its
  sheaf of causal functions over lower sets becomes a presheaf over the
  lowerset topology of a space of input histories. That base is a genuine
  topology and so a locale, which repairs the defect the earlier NOTE
  found. One claim changes: on definite orders the earlier paper's sheaf
  was asserted, while here sheafhood is a theorem for tight spaces only.
  Order-induced spaces are tight ([LIT-800](../literature.d/LIT-800.md), Proposition 3.32), so the
  definite case survives.
- **[THEORY-012](../theory.d/THEORY-012.md)** (noncontextual iff the context distributions glue) holds
  here by definition, generalised to causal covers. This paper adds a
  second, purely causal obstruction to gluing that is present even for
  deterministic data. That is the content of [THEORY-171](../theory.d/THEORY-171.md), filed from
  this reading.
- **[THEORY-165](../theory.d/THEORY-165.md)** (the contextual fraction is Lipschitz within a
  scenario) is stated for fixed measurement scenarios. Here contextual
  fractions are defined relative to a cover of a space of input histories.
  The reading neither tests nor extends that THEORY.
- No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- Proofs were not read here, and the paper is an unrefereed preprint.
- The census figure for solipsistic contextuality (1767 of 2644) is stated
  in the introduction without a table in the main text.
- Covers are restricted to maximal antichains.
- The interpretation of the fully solipsistic cover is operationally thin:
  the paper describes it as settings where distributions exist only over an
  event's past, "witnessed" by that event.
- Internal cross-references to the companion papers point to section
  numbers that do not exist in the current versions (e.g. "Subsubsection
  4.5.5 of [6]" in [LIT-788](../literature.d/LIT-788.md)). They appear to come from the combined
  v1 of 2206.08911.

## Open questions

- An operational experiment, or a quantum example, that displays
  solipsistic contextuality in data rather than in the presheaf.
- Whether "local and causally separable" implies "local in a causally
  separable way" (Conjecture 2.30 of [LIT-788](../literature.d/LIT-788.md)).
- The semiring generalisation (possibilistic, signed), which is stated but
  not developed.
