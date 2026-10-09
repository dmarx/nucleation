---
number: 624
status: Skimmed
formerly:
- NOTE-tmpht8fg
paper: 'LIT-788'
title: 'The Geometry of Causality'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Skimmed from the arXiv v2 PDF (2303.09017v2, 27 July 2023, 86 pages),
    extracted with pdftotext. Read: Section 1 (introduction, background on
    no-signalling and indefinite causality), Section 2.3 (causaltopes,
    Theorems 2.18, 2.19, 2.25), Section 2.4 (standard causal
    inseparability, Proposition 2.29, Conjecture 2.30), the BFW example
    (2.6.6) and the quantum-switch examples (2.7 preamble, 2.7.1–2.7.2 in
    full, the conclusions of 2.7.3–2.7.4). Skimmed for statements only:
    2.1–2.2 (polytopes and constrained conditional distributions), 2.5
    (causal equations for 3-event standard causaltopes), 2.6.1–2.6.5,
    2.8 (equations for arbitrary covers) and 2.9 (non-standard
    separability). Not read: the proofs (2.10). The landscapes are
    images and were followed from the prose. Skimmed, not Read, because
    most of the main text's worked material was not followed.
date: '2026-10-09'
summary: >-
  Empirical models on any cover of a space of input histories are
  exactly the points of a causaltope, a product of simplices sliced by
  linear causality equations, which makes supported and causally
  separable fractions linear programs. Defines causal separability
  relative to an ambient space and shows, with entangled and
  contextually controlled quantum switches, that the causally separable
  fraction is bounded below by the separable local fraction and can
  equal it.
---

<!-- inactive-ok-file: LIT-813 — Superseded; the withdrawn predecessor whose polytope and causal-fraction claims this paper proves -->
<!-- inactive-ok-file: THEORY-171 — Proposed; named to say this reading does not test it -->
<!-- inactive-ok-file: THEORY-165 — Proposed; named to say this reading does not test it -->

# NOTE-624: The Geometry of Causality

## Contribution

It gives the geometric counterpart of the topological framework of
[LIT-808](../literature.d/LIT-808.md). The empirical models on any cover of any space of input
histories form a polytope, the causaltope, described compactly as a
product of simplices cut by causality equations rather than by its
exponentially many facets. Fractions supported by sub-spaces, and the
causally separable fraction, become linear programs. Causal separability
becomes relative to an assumed ambient causal structure. Worked quantum
examples tie the separable fraction to the contextual (local) fraction.

## Key insight

A causal constraint is a marginal equation: two contexts that share a
lowerset of input histories must agree on it. So instead of characterising
causal correlations by inequalities (facets), slice the easy polytope of
conditional distributions with equations read off the space's topology.
Then every question of the form "how much of this model can that causal
structure explain" is a linear program.

## Assumptions

- Finite events, inputs and outputs, and a space of input histories with a
  cover, as in [LIT-800](../literature.d/LIT-800.md) and [LIT-808](../literature.d/LIT-808.md).
- Comparison of causaltopes (Proposition 2.26) needs spaces on the same
  events and inputs with the same maximal extended histories, for instance
  both satisfying free choice. Section 2.9 extends separability beyond the
  standard cover.
- Theory-independent: quantum realisability is not characterised. The
  quantum examples are used as inputs.

## Key results

- **Theorems 2.18–2.19.** Distributions on extended causal functions over
  a context correspond convex-linearly to distributions on output
  histories, with one output per tip-equivalence class.
- **Definition 2.12, Propositions 2.21–2.22.** The causality equations
  equate marginals of context pairs on common lowersets. A chain of
  adjacent pairs suffices, and on the standard cover equations indexed by
  histories suffice.
- **Theorem 2.25.** Empirical models on a cover correspond convex-linearly
  to points of the causaltope.
- **Proposition 2.26.** Refinement of spaces gives inclusion of standard
  causaltopes. The no-signalling polytope lies inside every one, and the
  indiscrete one is the full pseudo-empirical polytope (Observations
  2.27–2.28).
- **Definitions 2.14–2.16.** Supported fraction, causal fraction over a
  family, causally separable fraction (over the causal completions).
- **Proposition 2.29.** The causally separable fraction is at least the
  separable local fraction. **Conjecture 2.30.** Local and causally
  separable implies local in a causally separable way.
- **Examples.** BFW: 0% on all causally complete 3-event spaces, 0% on the
  no-signalling causaltope (26-dimensional), and 100% on each of the three
  "one party first, two indefinite" orders and on their 38-dimensional
  intersection. Fixing Alice's output leaves deterministic inseparable
  functions requiring two-way signalling between Bob and Charlie.
  Switch with Bell-entangled control: a causally separable fraction of
  about 63.2% for the model shown. The local fraction lower-bounds it at
  every angle, not always tightly. GHZ control: about 41.2%. Two switches
  with Bell-entangled control: about 47.7%, with the separable fraction
  equal to the separable local fraction. Two contextually controlled
  classical switches: 75%, equal to the local fraction of the controlling
  Bell model. Every example is fully separable once the no-signalling
  constraints to the measuring parties are dropped.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Empirical models on any cover of any space of input histories are exactly the points of the causaltope | strong (proof, not read) | Theorem 2.25 |
| C2 | Supported and causally separable fractions are computable by linear programming | strong (by construction) | Definitions 2.14–2.16 and the computed examples |
| C3 | The causally separable fraction is bounded below by the separable local fraction | strong (proof, not read) | Proposition 2.29 |
| C4 | Local and causally separable implies local in a causally separable way | conjecture | Conjecture 2.30 |
| C5 | Entangled or contextually controlled quantum switches witness indefinite order relative to an ambient space with known no-signalling constraints, but not relative to the indiscrete space | moderate (computed examples) | Section 2.7 |
| C6 | Causal inseparability in BFW stems from a cyclic order structure | weak (the authors' "intuition", supported by the conditioned models) | Section 2.6.6 |

## Method

Convex geometry and linear programming. Polytopes are given as solution
sets of linear equations within products of simplices. Fractions are
maximal-weight decompositions, computed by LP. The landscapes in 2.7 are
computed numerically over grids of measurement angles, and one takes 15
hours on 30 cores.

## Concepts

- **pseudo-empirical model**: a family of conditional distributions, one
  per context, with no cross-context constraint.
- **causality equations**: equalities of marginals on a common lowerset of
  two contexts.
- **causaltope**: the pseudo-empirical models satisfying the causality
  equations. *Standard* on the standard cover, *solipsistic* on the
  solipsistic one.
- **supported fraction / causal fraction**: the largest weight of a
  component of the model lying in a sub-space's causaltope, or in the
  convex hull of several.
- **causally separable fraction**: the causal fraction over a space's
  causal completions.
- **contextual causality**: the authors' name for causal inseparability
  correlated with, or implied by, non-locality or contextuality.

## Connections

It generalises the no-signalling polytopes of Barrett and co-authors and
Popescu–Rohrlich-style theory-independent no-signalling. It sets itself
against causal Bayesian networks (Fritz) and multipartite locality with
factorisable sources, where convexity can fail. It refines the
causal-inequality approach to indefinite order (Oreshkov, Costa and
Brukner; Branciard et al.; Oreshkov and Giarmatzi) by making separability
relative. It treats the OCB and BFW processes. A version of its first
switch example was studied by others with facet inequalities computed in
PANDA. It uses the contextual fraction of Abramsky and co-authors. It
proves the polytope and causal-fraction statements that the withdrawn
[LIT-813](../literature.d/LIT-813.md) made with proofs deferred, which it does not cite.

## Bearing on the record

- **[LIT-813](../literature.d/LIT-813.md).** Its Proposition 16 (a polytope cut by linear causality
  equations) is Theorem 2.25 here, in general. Its Section 9 claim (BFW has
  causal fraction 0 for every definite order and 1 for four pre-orders),
  which its NOTE marked "not supported here (proof deferred)", is now
  computed. The model has 0% support on every causally complete space and
  100% on each of three indefinite orders where one party acts first. The
  fourth pre-order of the earlier count is presumably the indiscrete one,
  which supports everything trivially. The paper does not say this, and
  it is my reconciliation.
- **[THEORY-171](../theory.d/THEORY-171.md)** rests on [LIT-808](../literature.d/LIT-808.md). This paper's examples are all
  on the standard cover, where solipsistic contextuality does not show, so
  they neither support nor test it.
- **[THEORY-165](../theory.d/THEORY-165.md)** (contextual fraction Lipschitz within a scenario):
  the fractions here are LP values over polytopes, which fits that
  THEORY's setting. The reading does not test it.
- No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- Skimmed: proofs not read, and Sections 2.8–2.9 followed only for their
  statements.
- Quantum realisability is outside scope, so the causaltopes over-approximate
  what quantum theory allows.
- The relative notion of separability depends on assuming part of the
  causal structure. The witnesses of indefinite order are witnesses
  conditional on that assumption, as the authors say.
- The causal fractions in 2.7 are read from grids of angles at finite
  resolution, and the minima are reported "at the angular resolution" used.
- Remark 2.4 and the text before Proposition 2.29 cite "Theorem 4.51
  p.77" and "Definition 4.38 p.70" of *The Topology of Causality*. Neither
  number exists in that paper's current version (v2), whose results are
  numbered 2.x. They look like leftovers from the combined v1 of
  2206.08911.

## Open questions

- Conjecture 2.30.
- A characterisation of the quantum-realisable subset of a causaltope, by
  semidefinite hierarchies or otherwise.
- Whether the tight correlation between separable and local fractions in
  the contextually controlled switch is generic or by construction. The
  authors say it holds "by construction" in that example.
