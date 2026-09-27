---
number: 17
status: Proposed
formerly:
- THEORY-tmpscxh5
promote_when: >-
  A close reading, in this record, of Coecke, Pavlovic & Vicary's proof that
  commutative special †-Frobenius algebras on finite-dimensional Hilbert
  spaces are exactly orthonormal bases (arXiv 0810.0812). It is cited by
  LIT-272 and not held here. That result is what makes "a basis",
  "a Frobenius algebra" and "classical data" one notion rather than three
  analogies. Also needed: a check, in each placement below, that the
  invariance or dependence claimed was measured or proved in the source,
  not inferred by the reader. The kind of result that would refute this
  is a Hilbert-space model in the record whose parts or features are
  recovered from unitarily invariant data alone, with no operator,
  stipulated basis or factorisation supplied.
title: 'In a Hilbert-space model only unitarily invariant structure is intrinsic; a basis or tensor factorisation, and so any parts or features, is extra data supplied from outside the space, and the record''s Hilbert-space works differ in where they get it'
version: 1
tags:
- mathematics
- quantum-foundations
- mereology
- representation-learning
- linguistics
- information-retrieval
date: '2026-09-27'
source:
- LIT-123
- LIT-262
- LIT-273
- LIT-272
extends:
- THEORY-004
summary: >-
  Carroll (2021), [LIT-123](../literature.d/LIT-123.md): a quantum theory is fixed up to unitary
  equivalence by the Hamiltonian's spectrum, and subsystems come from a
  factorisation that the dynamics must select. Van Rijsbergen ([LIT-262](../literature.d/LIT-262.md))
  computes only traces and inner products, and treats each observable's
  eigenbasis as a "point of view". DisCoCat's ε/η composition ([LIT-273](../literature.d/LIT-273.md)) is
  orthogonally covariant, while its Frobenius sequel ([LIT-272](../literature.d/LIT-272.md)) stipulates a
  basis and composes by elementwise product in it. [THEORY-004](THEORY-004.md) is the same
  point for learned representations. This is a synthesis across the four,
  not a result any one of them states. It does not say that basis-dependent
  models are wrong; it says what they have assumed.
---

<!-- inactive-ok-file: THEORY-008 — Proposed: cited for which comparison measures are the invariant ones, itself awaiting close readings; the directive lapses when its status changes -->
<!-- inactive-ok-file: LIT-241 — Deferred: named only to mark the infinite-dimensional GNS setting this document stays out of; the directive lapses when its status changes -->
<!-- inactive-ok-file: THEORY-004 — Proposed: the representation-learning instance of this account, itself awaiting close readings; the directive lapses when its status changes -->

# THEORY-017: In a Hilbert-space model only unitarily invariant structure is intrinsic; a basis or tensor factorisation, and so any parts or features, is extra data supplied from outside the space, and the record's Hilbert-space works differ in where they get it

## Source

- Carroll (2021), [LIT-123](../literature.d/LIT-123.md), pp. 4–9, as read in [NOTE-134](../notes.d/NOTE-134.md).
- Van Rijsbergen (2004), [LIT-262](../literature.d/LIT-262.md): Prologue p. 6, ch. 1 p. 19, ch. 4 p. 57, ch. 6, as read in [NOTE-239](../notes.d/NOTE-239.md).
- Coecke, Sadrzadeh & Clark (2010), [LIT-273](../literature.d/LIT-273.md), §§3–5, as read in [NOTE-245](../notes.d/NOTE-245.md).
- Kartsaklis, Sadrzadeh, Pulman & Coecke (2014), [LIT-272](../literature.d/LIT-272.md), §§2–4 and 6, as read in [NOTE-246](../notes.d/NOTE-246.md).
- For learned representations: [THEORY-004](THEORY-004.md).

## What was actually shown

**The mathematical core is elementary.** A finite-dimensional Hilbert space
with no further structure is determined by its dimension. The unitary group
acts transitively on its orthonormal bases, so no basis is distinguished,
and neither is any factorisation H ≅ H_A ⊗ H_B of given dimensions. Only
quantities invariant under that group can be read off the space alone:
inner products, traces, and the spectra of operators placed on it. A
non-degenerate self-adjoint operator does single out a basis, its
eigenbasis, up to phases. Its unitarily invariant content, though, is only
its eigenvalue list. Coecke, Pavlovic & Vicary's theorem, cited by [LIT-272](../literature.d/LIT-272.md)
(§4) and not held here, makes the basis side exact. On such a space,
commutative special †-Frobenius algebras correspond to orthonormal bases,
which is why the categorical literature calls them "classical structures".

**Each source takes one position on where the extra structure comes from.**

| Work | What it treats as intrinsic | Where the basis or factorisation comes from |
|---|---|---|
| Carroll, [LIT-123](../literature.d/LIT-123.md) | The spectrum {E_n}: "all the information in the Hamiltonian" (pp. 4–5). Changes of basis have "no physical importance whatsoever" (p. 4). | The dynamics. Among factorisations, the Hamiltonian's form picks out a local one (Cotler et al., unique when it exists) or a quasi-classical one (Carroll & Singh, numerical examples only) (pp. 7–9). |
| Van Rijsbergen, [LIT-262](../literature.d/LIT-262.md) | Traces and inner products. Every quantity the book computes is invariant under a joint unitary change of basis ([NOTE-239](../notes.d/NOTE-239.md)). | The observable. Each observable's eigenbasis is "a particular perspective", and a change of basis "constitutes a change of point of view" (Prologue p. 6; ch. 1 p. 19). |
| Coecke, Sadrzadeh & Clark, [LIT-273](../literature.d/LIT-273.md) | The ε/η composition. Orthogonal changes of the noun and sentence spaces carry the sentence vector covariantly (checked numerically in [NOTE-245](../notes.d/NOTE-245.md)). | Only the self-duality V* ≅ V, which the paper grounds in "a fixed base" (p. 13). The meaning computed does not depend on which base. |
| Kartsaklis et al., [LIT-272](../literature.d/LIT-272.md) | Nothing basis-free beyond the functor's object map. | A stipulation. W is the space of the 2,000 most frequent context lemmas with that basis fixed, and the Frobenius copying map is the one this basis induces. The paper notes that W* ≅ W "is not natural" (§2). A sentence is a Hadamard product in this basis, and one random rotation moved a sentence–subject cosine from 0.008 to −0.53 ([NOTE-246](../notes.d/NOTE-246.md)). |
| [THEORY-004](THEORY-004.md) (representations) | The kernel (Gram matrix). A representation is fixed by it only up to an orthogonal transformation. | Nowhere. That is why the comparison measures (CKA, CCA, Procrustes) are the invariant ones ([THEORY-008](THEORY-008.md)). |

So the same fork appears in physics, retrieval and compositional semantics.
A model either computes only invariants, or it takes on a basis or
factorisation from somewhere: a Hamiltonian, an observable, a corpus's
vocabulary. What it can say about "parts" (subsystems, terms, features,
meaning components) depends on that choice.

**Two consequences follow from the record's other threads. These are this
document's inferences, not claims in the sources.**

- **Contextuality needs more than one basis.** A single orthonormal basis,
  equivalently a single commutative Frobenius algebra, supports one global
  probability distribution over its outcomes. Kochen–Specker contextuality
  ([THEORY-012](THEORY-012.md)) is the failure of the distributions from several
  incompatible bases to glue into one. Van Rijsbergen's "contexts are bases"
  ([NOTE-239](../notes.d/NOTE-239.md)) is the same statement from the retrieval side. A model with one
  stipulated basis, such as [LIT-272](../literature.d/LIT-272.md)'s, cannot be contextual in this sense,
  whatever its categorical dress.
- **Boolean structure needs a basis.** The projections diagonal in one
  orthonormal basis form a Boolean algebra. The full subspace lattice, which
  is basis-free and defined by orthogonality alone, is orthomodular and not
  distributive ([NOTE-240](../notes.d/NOTE-240.md), "two polarities of one inner product"). Distributive,
  set-like concept structure is therefore evidence that a basis has been
  chosen.

## What this does not say

- **That basis-dependent models are wrong.** On [LIT-272](../literature.d/LIT-272.md)'s disambiguation
  task, the basis-dependent models lead: copy-object at ρ = 0.172, and the
  elementwise Kron and Multp at 0.168 and 0.163. The additive baseline, whose
  cosines are rotation-invariant, is at 0.050 ([NOTE-246](../notes.d/NOTE-246.md)). The claim here is
  about what such a model has assumed, not about how it performs. A corpus's
  context words may be exactly the right basis for word meaning. If so, that
  is an empirical fact about the corpus, not a consequence of the formalism.
- **That the extra structure is arbitrary.** Carroll's whole programme is
  that dynamics selects the factorisation, and that the selected one is
  "real, though not fundamental" ([LIT-123](../literature.d/LIT-123.md), pp. 7, 11–12). This document
  records where the structure comes from. It takes no side on whether it is
  thereby real.
- **Anything about infinite-dimensional or non-separable spaces.** There,
  Carroll notes, an algebra of observables must be supplied from the start
  (Haag, [LIT-123](../literature.d/LIT-123.md) p. 5). That is the setting of the GNS strand ([LIT-241](../literature.d/LIT-241.md),
  [THEORY-004](THEORY-004.md)), and this document stays finite-dimensional.
- **That Carroll's selection criteria work.** The local-factorisation
  uniqueness is a cited theorem. The quasi-classical criterion rests on
  numerical examples in a companion paper, and emergent fields on a hope
  ([NOTE-134](../notes.d/NOTE-134.md)).
- **That a tensor factorisation is just a basis.** A factorisation is
  coarser than a basis, since many bases respect it, and it carries more
  structure than a list of basis vectors. It is also what "parts" means in
  Carroll's mereology. The table puts them in one column because both are
  structure beyond the space, not because they are the same structure.
