---
number: 114
status: Active
formerly:
- TERM-tmpr3hl8
title: 'resource-bounded constraint system: architectures, the configurations and costed processes each admits, costed changes of architecture and the observations available, with reachability indexed by a partially ordered budget'
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Adopted at the twenty-fifth status review (ADR-057), at the status
    review's ruling (the owner delegated these rulings). Its settle
    condition, a claim of the record's own stated in it, is met by
    CLAIM-560, CLAIM-563 and CLAIM-573. A paragraph, 'Which form', says
    the term means A's six-part form and not the later eight-part form or
    total category its notes record; no claim stated in it uses those. The
    definition is otherwise unchanged.
tags:
- mathematics
- complex-systems
- operations-research
date: '2026-11-05'
line:
- realizability
complements:
- TERM-105
summary: >-
  A's proposal, from the pasted synthesis on resource-bounded realizability
  (three responses, pasted by the owner on 2026-11-05, continuing the
  exchange on constraint architectures), Response 1 §1, Response 2 §§2 and
  4 and Response 3 §§1, 6 and 8: the object 𝔒 = (X, C, M, κ, π), revised to
  a family 𝔒_n = (Z_n, {Q_z}, P_n, R_n, κ_n, Obs_n) of architectures,
  configuration spaces, processes, resource semantics, process costs and
  observation capabilities, with the resource-bounded reachability relation
  q ⇝_b q′ and the budget-indexed family b ↦ G_b(z). Filed as a term, not a
  claim: it names the frame the claims filed beside it are stated in. It
  adds to [TERM-105](TERM-105.md)'s resource types the processes and their
  composition, changes of architecture as costed moves of their own, and
  what an observer can detect. The wording is A's; adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CASE-198 CASE-207 CLAIM-560 CLAIM-563 CLAIM-571 CLAIM-573 CLAIM-582 CLAIM-585 CLAIM-591 TERM-105 TERM-111 THEORY-1435 — Proposed; A's proposals of 2026-11-04 and 2026-11-05, the readings' accounts and partial readings, and the entries filed beside them, cited as filed, nothing here resting on their being settled -->
<!-- inactive-ok-file: CLAIM-477 CLAIM-314 — Proposed or new; the resource-bounded realizability readings of 2026-11-05, cited as open -->

# TERM-114: resource-bounded constraint system: architectures, the configurations and costed processes each admits, costed changes of architecture and the observations available, with reachability indexed by a partially ordered budget

## Definition

A resource-bounded constraint system, in A's final form (Response 3 §8),
is a family indexed by size n,

  𝔒_n = ( Z_n, {Q_z}, P_n, R_n, κ_n, Obs_n ),

whose components A glosses as "architectures, configuration spaces,
processes, resource semantics, process costs, and observation
capabilities". Spelled out from A's earlier sections:

- **An architecture z** is "a particular organization of constraints", and
  fixes its admissible configurations, Q_z = {q ∈ X_z : F_z(q) = 0,
  G_z(q) ≥ 0} (Response 3 §1).
- **Processes** P_z(q, q′) are the admissible ways from q to q′: "a sequence
  of folds, a control trajectory, a proof search, a sequence of
  institutional decisions, or an algorithm transforming one representation
  into another."
- **Costs** κ : P_z(q, q′) → R take values in "a structured space of
  resources", partially ordered by ⪯ and carrying a law for composing the
  costs of processes run in sequence or in parallel (the resource
  semantics).
- **Resource-bounded reachability** is q ⇝_b q′ ⟺ ∃p ∈ P_z(q, q′) :
  κ(p) ⪯ b. Its budget-indexed family b ↦ G_b(z), the graph of transitions
  executable within b, is "an indexed structure over a partially ordered
  resource space" (Response 2 §2). "More generally, retaining entire
  processes and their composition gives a category rather than merely a
  graph."
- **Changes of architecture** z →ρ z′ are moves of their own: "These are not
  ordinary transitions within a fixed configuration space. They modify the
  structure determining which transitions are possible." The full state is
  s = (z, q, m, b, k), with m memory, b reserves and k maintained
  competencies (Response 3 §6), and the two kinds of move are
  (z, q) → (z, q′) and (z, q) → (z′, q′).
- **Observation** Obs_n is what another system can detect about this one
  at a budget (Response 3 §9), and Response 1's π is the "Interpretation of
  states as computational information", the decoding that lets a fold
  stand for a bit: "Not every origami crease pattern has this particular
  computational interpretation."

Response 1's κ was already a vector: "κ(γ)= ( time, memory, energy,
control precision )", so that "two algorithms can have the same
computational complexity while requiring completely different amounts of
physical energy or control."

**Which form.** The term means the six-part form above. The later
eight-part form and the total category of the notes below add structure,
compatibility and correspondence, inquiry and constraint construction,
that claims stated in this term do not use; a claim that needs one of them
says so and cites the note.

## What it adds to what the record holds

- **[TERM-105](TERM-105.md)** sorts resource constraints by what function of a path
  they bound and gives A's earlier dynamic model of q, z, b and k. This
  term keeps the same pieces and adds the processes as objects with a
  composition law, which is where the types differ in kind: [CLAIM-563](../claims.d/CLAIM-563.md)
  shows a peak capacity and a cumulative expenditure compose differently
  enough that only the first gives a category of affordable processes at
  every budget.
- **The budget is partially ordered**, not a number: [CLAIM-585](../claims.d/CLAIM-585.md)'s two
  paths needing (3, 1) and (1, 3) make the sufficient budgets an up-set
  with a two-point frontier.
- **The filtrations it carries** are two, compatibility and reachability,
  and neither fixes the other ([CLAIM-560](../claims.d/CLAIM-560.md)); reachability is directed,
  and a summary of connectivity does not settle it ([CLAIM-591](../claims.d/CLAIM-591.md)).
- **Changes of architecture are costed moves**, as in [CASE-198](../cases.d/CASE-198.md), where
  switching to a staging architecture lowers a threshold, and
  [CASE-207](../cases.d/CASE-207.md), where admitting facet bending widens the declared moves
  at an energy price.

The readings say what the costed process layer is in established terms.
Marsden and Zwart ([NOTE-1602](../notes.d/NOTE-1602.md); [THEORY-1435](../theory.d/THEORY-1435.md)) make costed conversions
the hom-objects of categories enriched in a commutative quantale; the
reader of that paper matched A's "resource-graded process category" to a
graded category, which keeps every process with its cost where the
enriched view keeps only the best cost between two configurations.

## What it is not

- **A claim that any system has this structure.** It is a frame for stating
  claims. Which organizations admit a declared Q_z, P_z and κ is
  empirical, and the record has measured none.
- **A license to read restriction as generation.** A keeps [CLAIM-582](../claims.d/CLAIM-582.md)'s
  guard: "imposing an additional hard constraint within a fixed dynamical
  model cannot enlarge its existential reachable set." Within one z an
  added constraint only removes processes; what can enlarge them is a move
  to another z.
- **One budget.** R is a partial order with its own composition laws;
  [CLAIM-571](../claims.d/CLAIM-571.md)'s scalar threshold is the one-capacity case.
- **A notion of universality.** Comparing two such systems needs a
  translation between them; the senses in which one can be universal are
  [TERM-111](TERM-111.md)'s.

## What would settle it

Adoption by the owner, or a claim of the record's own stated in it.
[CLAIM-560](../claims.d/CLAIM-560.md), [CLAIM-563](../claims.d/CLAIM-563.md) and [CLAIM-573](../claims.d/CLAIM-573.md) are stated in it.

## Note of 2026-11-05: the resource-bounded realizability readings

The second paste of the pasted synthesis on resource-bounded realizability revises the object to 𝔒 = (Z, Q, 𝒞, 𝒫, ℛ, κ, 𝓘, 𝓜). Beside this term's components it adds 𝒞, the compatibility and correspondence structures, which [TERM-093](TERM-093.md) keeps apart from the physical coupling that holds them; 𝓘, the inquiry structure by which a system generates and uses its representations and questions ([TERM-095](TERM-095.md); [CLAIM-475](../claims.d/CLAIM-475.md)); and 𝓜, the processes that construct, modify, maintain or regenerate constraints ([CLAIM-477](../claims.d/CLAIM-477.md)). A's §8 adds recognition and reuse costs to the resource accounting ([CLAIM-314](../claims.d/CLAIM-314.md)). A's caveat: "I would be careful not to assume that every component is necessary for every kind of object." No status changes.

## Note of 2026-11-05: A's fourth paste, and the assistant's contributions

A's fourth paste assembles the categories for each architecture into a Grothendieck total category, objects pairs (z, x) and morphisms an architecture change with a transformation after it, the categorical form of this term's two kinds of move, and warns that "we should not assume every architecture change induces a functor", suggesting that "relations, spans, profunctors, or other process structures may be more appropriate than ordinary functors" where an edit deletes or merges states. No status changes.
