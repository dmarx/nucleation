---
status: Read
paper: LIT-2249
title: 'Stewart — The lattice of balanced equivalence relations of a coupled cell network'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Read on 2026-11-22 for LEAD-023 from the author's accepted version in
    the University of Warwick repository (WRAP,
    https://wrap.warwick.ac.uk/id/eprint/651/1/WRAP_Stewart_Lattice_Balanced.pdf),
    posted "in accordance with publisher policies", 20 pages, lawful under
    ADR-074. The introduction, definitions, Sections 5 to 7 and Example 5·5
    read in full; the proofs of Section 3 followed for their statements;
    Section 8 (chains with feedback) read for its theorem. Quotations
    checked by script.
date: '2026-11-22'
summary: >-
  On any coupled cell network of finite type the balanced equivalence
  relations, which are exactly the patterns of synchrony invariant under
  every dynamics the architecture admits, form a complete lattice under
  refinement. Its join is the join of equivalence relations, but its meet is
  not intersection: two balanced colourings can have an unbalanced common
  refinement. A unique coarsest balanced relation always exists, is
  characterized by input trees on the universal cover, and is computable in
  polynomial time.
---

# NOTE-tmp14xdi: Stewart — The lattice of balanced equivalence relations of a coupled cell network

## Contribution

Structure on the set of robust synchrony patterns of a network: it is a
complete lattice, ordered by refinement, with a top element that answers
whether any nontrivial robust synchrony exists.

## Key results

1. **Background (Introduction).** "all 'robust' patterns of synchrony—those
   determined by the network architecture rather than any specific choice
   of dynamic—correspond to 'balanced equivalence relations' on the set of
   cells"; "balance means that synchronous cells must have synchronous
   input sets, up to a type-preserving isomorphism."
2. **Main theorem (§5).** For networks of finite type, which include all
   locally finite ones, the balanced equivalence relations form a complete
   lattice, proved through an order-reversing bijection with the
   flow-invariant polydiagonals (§3).
3. **Meet is not intersection (Example 5·5).** "the intersection of two
   balanced equivalence relations need not be balanced", so the lattice
   "is not a sublattice of the lattice of all equivalence relations", though
   "these two lattices share the same join operation".
4. **Coarsest relation (§6–7).** "on every network there exists a unique
   coarsest balanced equivalence relation. Here, the number of synchronous
   sets of cells is as small as possible." It is characterized by
   isomorphism of input trees on the universal cover; Aldis's algorithm
   computes it in polynomial time.
5. **An example (§8).** For a chain of r + s identical cells with feedback
   the lattice is the product of the divisor lattice of r with a chain.

## Assumptions

The groupoid (multiarrow) formalism of coupled cell networks; admissible
vector fields, those respecting cell and arrow types; networks of finite
type. Nothing is assumed or proved about stability.

## Concepts

Coupled cell network; input set and input isomorphism; balanced
equivalence relation (balanced colouring); polydiagonal; flow-invariant
subspace; complete lattice; coarsest balanced relation; universal cover and
input tree; quotient network.

## Bearing on the record

- **QUESTION-147.** The question compares observed clusters with orbits
  computed in advance. The lattice is the full menu of candidates computed
  from structure alone, wider than the orbits (THEORY-1065), with a top
  element computable in polynomial time. As A said at A20 §2, which of its
  elements are realized as attractors is a separate matter: the paper says
  nothing on stability, so it supplies the candidates and not the
  prediction of which desynchronizes where.
- **THEORY-1065.** Extends its account: the balanced partitions are not a
  loose collection but a complete lattice, whose meet is not intersection.
  It confirms that the invariance carries no claim about attraction.
- **THEORY-2014** (background). Gili and colleagues' use of coarsest
  balanced colourings rests on this paper's top element.

## Limitations

Pure combinatorics and invariance; no dynamics beyond admissibility, no
stability, no weights beyond arrow types. The meet has no simple
combinatorial description, as the author notes.
