---
number: 17
status: Proposed
formerly:
- THEORY-tmpscxh5
promote_when: >-
  The Coecke–Pavlovic–Vicary condition is met: LIT-274 is read
  (NOTE-247), and it proves the basis–Frobenius correspondence, for
  complex spaces. What remains is a check, in each placement below, that
  the invariance or dependence claimed was measured or proved in the
  source, not inferred by the reader. At present LIT-273's covariance and
  LIT-272's rotation sensitivity are the readers' numerical checks, not
  the papers' claims. The kind of result that would refute this is a
  Hilbert-space model in the record whose parts or features are recovered
  from unitarily invariant data alone, with no operator, stipulated basis
  or factorisation supplied.
title: 'In a Hilbert-space model only unitarily invariant structure is intrinsic; a basis or tensor factorisation, and so any parts or features, is extra data supplied from outside the space, and the record''s Hilbert-space works differ in where they get it'
version: 3
history:
- version: 2
  date: '2026-09-27'
  note: >-
    LIT-274 (Coecke, Pavlovic & Vicary) filed and read, and added to
    source. The correspondence is restated as the paper proves it:
    orthogonal bases for commutative †-Frobenius algebras, orthonormal bases
    for special ones, on complex spaces only. A caveat on real spaces is
    added, the first promote_when condition is recorded as met, and the
    status stays Proposed on the second.
- version: 3
  date: '2026-09-27'
  note: >-
    Abramsky & Heunen (LIT-275) filed and read, and added to source.
    The finite-dimensional caveat is narrowed: discrete orthonormal bases
    correspond to commutative special †-Frobenius algebras satisfying the
    H*-axiom in any dimension, over ℂ. Continuous observables remain
    outside, and the real-scalar caveat is extended to every dimension. The
    status stays Proposed.
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
- LIT-274
- LIT-275
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
its eigenvalue list. Coecke, Pavlovic & Vicary ([LIT-274](../literature.d/LIT-274.md), read in [NOTE-247](../notes.d/NOTE-247.md)) make the basis
side exact, for complex spaces. On a finite-dimensional complex Hilbert
space, the commutative †-Frobenius algebras are in bijection with the
orthogonal bases, the basis being the vectors the comultiplication copies
(Thm 5.1). The special ones correspond exactly to the orthonormal bases, with
the vectors fixed exactly, phases included (§6). The paper calls this
"classical data"; the later categorical literature calls these algebras
"classical structures".

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
  equivalently (on a complex space) a single commutative special
  †-Frobenius algebra, supports one global
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
- **That the basis–Frobenius correspondence holds on real spaces.**
  [LIT-274](../literature.d/LIT-274.md)'s theorem is for complex Hilbert spaces, and it fails over
  the reals. On ℝ², the complex numbers, with multiplication scaled by
  1/√2, form a commutative special †-Frobenius algebra with no nonzero
  copyable vector. The reader of [NOTE-247](../notes.d/NOTE-247.md) found this, and I checked it
  numerically when filing. [LIT-273](../literature.d/LIT-273.md), [LIT-272](../literature.d/LIT-272.md) and [THEORY-004](THEORY-004.md) all work over the
  reals. There a basis still induces a Frobenius algebra, which is all
  [LIT-272](../literature.d/LIT-272.md) uses, but a Frobenius algebra need not come from a basis. So the
  table's placements stand, and "basis" and "Frobenius algebra" are one
  notion only in the complex case.
- **Anything about continuous observables, or about infinite-dimensional
  spaces beyond discrete bases.** Abramsky & Heunen ([LIT-275](../literature.d/LIT-275.md), read in
  [NOTE-248](../notes.d/NOTE-248.md)) show that a unital Frobenius algebra exists in Hilb only in
  finite dimension (Lemma 3). Dropping the unit, they prove that on a
  complex Hilbert space of any dimension, separable or not, a commutative
  special †-Frobenius algebra is induced by an orthonormal basis exactly
  when it satisfies Ambrose's H*-axiom, equivalently when it is semisimple
  (Thm 22). So a discrete basis is still extra structure supplied as an
  algebra on the space, in any dimension. Whether the H*-axiom is automatic
  was left open there (Prop. 23).
  - *Continuous observables* have no eigenbasis and are outside that
    result (its §6). There, Carroll notes, an algebra of observables must be
    supplied from the start (Haag, [LIT-123](../literature.d/LIT-123.md) p. 5). That is the setting of the
    GNS strand ([LIT-241](../literature.d/LIT-241.md), [THEORY-004](THEORY-004.md)).
  - *Scope of this document.* The table stays finite-dimensional, as its
    sources are. The real-scalar caveat above holds in every dimension: over
    ℝ the H*-axiom does not force copyable vectors, since ℂ regarded as a
    real algebra satisfies it and has none ([NOTE-248](../notes.d/NOTE-248.md)).
- **That Carroll's selection criteria work.** The local-factorisation
  uniqueness is a cited theorem. The quasi-classical criterion rests on
  numerical examples in a companion paper, and emergent fields on a hope
  ([NOTE-134](../notes.d/NOTE-134.md)).
- **That a tensor factorisation is just a basis.** A factorisation is
  coarser than a basis, since many bases respect it, and it carries more
  structure than a list of basis vectors. It is also what "parts" means in
  Carroll's mereology. The table puts them in one column because both are
  structure beyond the space, not because they are the same structure.
