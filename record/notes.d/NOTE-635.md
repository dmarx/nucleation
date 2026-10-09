---
number: 635
status: Read
formerly:
- NOTE-tmpp785f
paper: 'LIT-800'
title: 'The Combinatorics of Causality'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read from the arXiv v4 PDF (2206.08911v4, 27 July 2023, 65 pages),
    extracted with pdftotext. Read in full: Sections 1 (introduction), 2
    (causal orders, operations, hierarchy, lattice of lowersets, with the
    proofs of Propositions 2.2 and 2.4) and 3.1–3.7 (operational
    scenarios, partial functions, input histories, spaces, causally
    complete spaces, the hierarchy, the search), and the reference list.
    Proofs followed in 3.8: Propositions 3.21, 3.23 and 3.24, Theorem
    3.37 and the opening of Theorem 3.34; the remaining proofs were not
    read. The Hasse diagrams and the hierarchy figures are images that
    did not survive extraction and were followed from the prose and the
    captions. The supplementary "Classification of causally complete
    spaces on 3 events with binary inputs" was not read. The v1/v2 text
    (394 pages, "The Topology and Geometry of Causality") was not
    compared.
date: '2026-10-09'
summary: >-
  Replaces causal orders by spaces of input histories (join-prime sets
  of partial input assignments), which can express causal constraints
  that depend on inputs. Defines free choice, tip events, causal
  completeness and tightness, three kinds of composition, and a lattice
  of spaces; proves that the maximal causally complete spaces are
  exactly the causal switch spaces; and finds 2644 complete spaces on 3
  binary-input events, against 19 from definite orders.
---

<!-- inactive-ok-file: LIT-813 — Superseded; the withdrawn predecessor, named to say what this paper replaces -->
<!-- inactive-ok-file: THEORY-171 — Proposed; the account this trilogy warrants, named not leaned on -->

# NOTE-635: The Combinatorics of Causality

## Contribution

Before this paper, operational treatments of causal structure in quantum
foundations used a causal order, definite (a partial order) or indefinite
(a preorder), possibly mixed. This paper replaces the order with a space of
input histories: the set of partial input assignments on which the output
at some event may depend. That makes causal constraints conditional on
inputs a first-class object. It works out the combinatorics of these spaces:
their order, their lattice operations, composition, causal completeness and
tightness. It then shows by exhaustive search that even 3 events with
binary inputs admit 2644 causally complete spaces, where the literature had
used 25.

## Key insight

Causality is "no signalling from outside the past", so what matters is not
which events precede which but which input data an output is allowed to
see. Once that is the primitive, the order of events can itself depend on
inputs. Whether event B sees event C's input can depend on what was chosen
at A. A causal order is then a special, rigid case of a much larger space.

## Assumptions

- Finitely many events, each with finite non-empty input and output sets.
  Inputs are freely chosen, so every joint input must be reachable (the
  free-choice condition, Definition 3.9).
- Black-box devices act locally at events. Any dependence on other events
  goes through the causal structure.
- The object of study is a conditional distribution on joint outputs given
  joint inputs. How it is obtained (experiment or theory) is outside the
  paper.
- A space of input histories is a finite set of partial functions that is
  join-prime: no history is the compatible join of others in the set.
  This is the normal form that makes spaces correspond to constraints.
- Causal completeness, the main object of study, is built on top of free
  choice by definition (Remark 3.2).

## Key results

- **Proposition 2.2.** Ω ≤ Ω′ ⇔ Λ(Ω) ⊇ Λ(Ω′). **Corollary 2.3.**
  Λ(Ω) ∪ Λ(Ω′) ⊆ Λ(Ω ∧ Ω′), strictly in general: the union need not be
  closed under intersection (a four-event counterexample is given).
  **Proposition 2.4.** Λ(Ω) ∩ Λ(Ω′) = Λ(Ω ∨ Ω′): the join's constraints
  are exactly those common to the orders.
- **Propositions 3.2, 3.6, 3.8.** Order-induced spaces Hist(Ω, I) are
  join-prime and satisfy free choice, and Ω ≤ Ξ ⇔ ExtHist(Ω, I) ⊇
  ExtHist(Ξ, I). The spaces themselves are not ordered by inclusion (a fork
  and a total order on 3 events give incomparable spaces), which is why
  the order on spaces goes through extended histories (Definition 3.10).
- **Proposition 3.10.** All spaces form an infinite lattice, with
  Θ ∨ Θ′ = Prime(Ext Θ ∩ Ext Θ′) and Θ ∧ Θ′ = Prime(Ext Θ ∪ Ext Θ′). Spaces
  with fixed inputs form a finite lattice, and those satisfying free
  choice form a lattice between the discrete and indiscrete spaces.
- **Propositions 3.11–3.12.** Ω ↦ Hist(Ω, I) commutes with joins, and
  order-induced spaces are not closed under meets.
- **Propositions 3.13–3.18.** Parallel, sequential and conditional
  sequential compositions are spaces and match the compositions of orders.
  Conditional sequential composition satisfies free choice iff each part
  does and all branches share their input sets.
- **Proposition 3.20, Definition 3.14, Proposition 3.21.** Every history
  has at least one tip, and a non-history extended history has none.
  Causally complete means exactly one tip each. An order-induced space is
  complete iff the order is definite, since the tips of a history over ω↓
  are ω's equivalence class.
- **Theorem 3.26–Corollary 3.28.** The causal completions of parallel and
  (conditional) sequential compositions are the compositions of the
  completions. Example: total(A, {B, C}) has four completions, two with a
  fixed order of B and C and two with A's input choosing it.
- **Proposition 3.29.** Causally complete spaces with fixed inputs are
  closed under meet, not join.
- **Proposition 3.32, Theorem 3.33.** Order-induced spaces are tight. The
  meet of two order-induced spaces on the same events is tight iff for each
  event one causal past contains the other.
- **Theorems 3.34, 3.36, Corollary 3.35.** A space equal to its own
  extension, with single tips, is a conditional sequential composition
  {ω₁} ⇝ (Θ′_i), recursively. Causal switch spaces are exactly the complete
  spaces with Θ = Ext(Θ), and they are exactly the maximal complete spaces.
  With n events and k inputs each, S_{n,k} = Π_{j=1..n} j^{k^{n−j}}.
- **Theorem 3.37.** Θ is causally complete iff every extended history with
  at least two events stays an extended history after deleting some one
  event. This drives the enumeration.
- **The census (Section 3.6–3.7).** 7 complete spaces on 2 binary events;
  2644 on 3, in 102 symmetry classes. 5 classes are order-induced (19
  spaces), 13 classes admit no fixed definite order, and 58 classes are
  non-tight. On 4 events, 869,529,223 spaces had been found after 106 days,
  with about 10⁹ in about 3 × 10⁶ classes projected from a fitted power
  law.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The constraints common to several causal orders are exactly those of their join, but jointly satisfying several orders is not the same as satisfying their meet | strong (proof and counterexample) | Propositions 2.2, 2.4, Corollary 2.3 |
| C2 | An order-induced space is causally complete iff the order is definite | strong (proof) | Proposition 3.21 |
| C3 | The maximal causally complete spaces are exactly the causal switch spaces, built by recursively letting one event's input choose the rest | strong (proof) | Theorems 3.34, 3.36, Corollary 3.35 (3.36's proof not read) |
| C4 | Causal completeness has a one-event deletion characterisation | strong (proof) | Theorem 3.37 |
| C5 | There are exactly 2644 causally complete spaces on 3 binary-input events, in 102 symmetry classes | moderate (exhaustive computation, not reproduced) | Section 3.6; the classification is a supplementary work |
| C6 | There are about a billion on 4 events | weak (extrapolation) | power-law fit to a search in progress |

## Method

Order theory on partial functions: restriction order, compatible joins,
join-prime subsets as normal forms and join-closure as their extension.
Spaces are compared through their extensions, and composition is defined by
joining histories. The census uses an enumeration algorithm based on Theorem
3.37, with a symmetry-reduced variant for 4 events. Both are in the
supplementary classification, which was not read.

## Concepts

- **causal order**: a finite preorder. Definite if it is antisymmetric, and
  indefinite if two distinct events are each ≤ the other.
- **lowerset**: a set of events closed under the causal past. It is the
  operational unit, since outputs in a lowerset cannot depend on inputs
  outside it.
- **input history**: a partial function assigning inputs to some events,
  on which the output at its tip event(s) may depend.
- **space of input histories (Θ)**: a finite join-prime set of input
  histories. **Ext(Θ)**: all compatible joins of its histories.
- **refinement (Θ′ ≤ Θ)**: Ext(Θ′) ⊇ Ext(Θ); more causal constraints.
- **free-choice condition**: every total input assignment is an extended
  history.
- **tip event**: an event in a history's domain covered by no history
  below it.
- **causally complete**: free choice plus exactly one tip per history.
  **Causal completion**: a maximal causally complete refinement.
- **tight**: under every extended history, each event is the tip of only
  one history below it.
- **causal switch space**: one event first, then, for each of its inputs, a
  causal switch space on the rest.

## Connections

The motivation runs from Robb's 1914 order-theoretic relativity and
Malament's theorem (causal order fixes conformal structure) to quantum
indefinite causality: Hardy's causaloid, the quantum switch, and the
process matrices of Oreshkov, Costa and Brukner. The canopy of switch
spaces is consistent with Oreshkov and Giarmatzi's causal separability.
The paper replaces the input structure of the authors' withdrawn
sheaf-theoretic paper ([LIT-813](../literature.d/LIT-813.md)), although it does not cite that paper.
Its own reference list names only the two sequels and the classification.
The sheaf of causal functions and empirical models built on these spaces
are in *The Topology of Causality* ([LIT-808](../literature.d/LIT-808.md)), and the causal polytopes
in *The Geometry of Causality* ([LIT-788](../literature.d/LIT-788.md)).

## Bearing on the record

- **[LIT-813](../literature.d/LIT-813.md).** Its NOTE found the "locale of inputs" (Definition 3,
  Proposition 5) defective: the given meet can leave the poset, and the
  poset is not distributive. Here the poset is replaced. Inputs are no
  longer families of input sets on lowersets but partial functions, and the
  topology is not asserted on them. In [LIT-808](../literature.d/LIT-808.md) the topology is the
  lowerset topology of the space, which is a genuine topology and so a
  locale. The repair is a change of object, not a corrected proof of
  Proposition 5.
- **The order-theoretic point in C1** is a clean, general fact: the
  constraints of several causal orders combine by join, but joint
  satisfiability is not the meet. It is worth having, but it is too narrow
  to be a THEORY on its own.
- The record holds no THEORY on causal structure. The one this trilogy
  warrants is drawn from [LIT-808](../literature.d/LIT-808.md) ([THEORY-171](../theory.d/THEORY-171.md)), and this paper
  supplies its definitions.
- No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- Finite events and finite inputs only, and all examples have binary
  inputs.
- The census results rest on a supplementary computation that was not
  read or reproduced. The 4-event figure is an extrapolation from a search
  still running when the paper was written.
- Causal completeness is defined together with free choice, so spaces
  without free choice get no causal reading.
- Causal incompleteness is treated as missing information to be completed,
  not as a physical delocalisation of events. That is an interpretive
  choice, which the paper argues for and does not prove.
- No probabilities and no empirical models appear here. Those are in the
  sequels.

## Open questions

- The exact number of causally complete spaces on 4 events, and an
  enumeration method that reaches 5. The authors say theirs cannot.
- A structural description of the non-tight classes, which are the
  majority on 3 events.
- Whether the meet of causally complete spaces, which can be non-tight,
  has a natural operational meaning beyond "satisfies both".
