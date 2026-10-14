---
number: 857
status: Read
formerly:
- NOTE-tmp98n0x
paper: LIT-241
title: 'Gelfand–Naimark–Segal construction (Wikipedia)'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the article's wikitext (en.wikipedia.org,
    action=raw, 16,140 bytes), every section, theorem, proof, reference
    and footnote. The revision is oldid 1343628657 of
    2026-03-15T13:10:18Z, which the page history showed as still the
    latest on 2026-10-14, so it is the revision the seed read. Replaces
    the seeded skim NOTE-204.
date: '2026-10-14'
summary: >-
  For a state ρ on a C*-algebra A, the semi-inner product ⟨a, b⟩ = ρ(b*a)
  on A, quotiented by its null left ideal and completed, carries A acting
  by left multiplication, with the class of the identity as a unit cyclic
  vector and ρ(a) = ⟨π(a)ξ, ξ⟩. Any two cyclic representations with
  cyclic vectors reproducing the same state are unitarily equivalent, by
  the unitary π(a)ξ ↦ π′(a)ξ′. The representation is irreducible exactly
  when the state is pure. The article says nothing about kernels.
---
<!-- inactive-ok-file: NOTE-204 — Superseded; the seeded skim this reading replaces -->
<!-- inactive-ok-file: THEORY-017 — Proposed; the two accounts that cite this article, named for what it supports -->

# NOTE-857: Gelfand–Naimark–Segal construction (Wikipedia)

## Contribution

A reference article. It states the correspondence between states and
cyclic *-representations of a C*-algebra, gives the construction (after
Kadison, Thm 4.5.2) and the uniqueness (Kadison, Prop. 4.5.3), sketches
the proof that the GNS representation is irreducible iff the state is
pure, and names the construction's role in the Gelfand–Naimark theorem,
the universal representation and the enveloping von Neumann algebra.

## Key insight

A state is enough to rebuild a Hilbert space and a representation in
which it is a vector expectation, and the result is fixed up to a unitary
that is forced on you: it must send π(a)ξ to π′(a)ξ′. The inner products
⟨π(a)ξ, π(b)ξ⟩ = ρ(b*a) are all the data there is, so any two
realizations of them are isometric on a dense set.

## Assumptions

- **A is a C*-algebra.** Unital or not; in the non-unital case the cyclic
  vector is a limit of an approximate identity. The closing remark
  extends the theorems to B*-algebras with approximate identity.
- **ρ is a state:** a positive linear functional of norm 1, equivalently
  ρ(1) = 1 when A is unital.
- **Representations are nondegenerate *-homomorphisms** into the bounded
  operators on a Hilbert space.
- **Convention.** ⟨a, b⟩ = ρ(b*a) is linear in its first argument; vector
  states are ⟨π(a)ξ, ξ⟩. The scalars are complex.

## Key results

- **Vector states.** For a *-representation π with unit cyclic vector ξ,
  a ↦ ⟨π(a)ξ, ξ⟩ is a state.
- **Existence (Kadison 4.5.2).** For each state ρ there are π on H and a
  unit cyclic ξ with ρ(a) = ⟨π(a)ξ, ξ⟩ for all a.
  1. ⟨a, b⟩ = ρ(b*a) is a semi-definite sesquilinear form. The null
     elements I = {a : ρ(a*a) = 0} form a subspace and a left ideal, "the
     largest left ideal in the null space of ρ". A/I is an inner-product
     space, and H is its completion.
  2. π(a)(b + I) = ab + I is bounded and extends to H, and π is
     *-preserving.
  3. ξ is the class of 1, or the limit of the classes of an approximate
     identity.
- **Uniqueness (Kadison 4.5.3).** If (π, ξ) and (π′, ξ′) both reproduce ρ
  with unit cyclic vectors, there is a unitary U : H → H′ with
  π′(a) = Uπ(a)U* for all a, and U maps π(a)ξ to π′(a)ξ′.
- **Significance.** Enough pure states exist that the direct sum of their
  irreducible GNS representations is faithful, which is the heart of the
  Gelfand–Naimark theorem. The sum over all states is the universal
  representation, which contains every cyclic representation; its
  weak-operator closure is the enveloping von Neumann algebra, identified
  with A**.
- **Irreducibility.** The states of a unital A form a weak-* compact
  convex set (Banach–Alaoglu). For C(X), Riesz–Markov–Kakutani makes the
  positive functionals of norm ≤ 1 the positive Borel measures of mass
  ≤ 1, and the extreme states the point masses (Krein–Milman); a
  representation of C(X) is irreducible iff one-dimensional. In general,
  π with unit cyclic ξ is irreducible iff its state is an extreme point
  of the positive functionals of norm ≤ 1. The proof sketch uses a
  Radon–Nikodym-type lemma: a positive g ≤ f has the form
  g(x*x) = ⟨π(x)ξ, π(x)T_g ξ⟩ with 0 ≤ T_g ≤ 1 in the commutant π(A)′.
- **History.** Gelfand and Naimark (1943); Segal saw the construction
  implicit in their work and sharpened it, and in 1947 showed that
  irreducible representations suffice for a physical system described by
  an operator algebra, a point von Neumann had shown only for
  Schrödinger–Heisenberg theory. Stinespring's theorem on completely
  positive maps generalizes the construction.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Every state on a C*-algebra is a vector state of a cyclic *-representation | strong | standard theorem, proof sketched (Kadison 4.5.2) |
| C2 | That representation is unique up to unitary equivalence, by the unitary π(a)ξ ↦ π′(a)ξ′ | strong | stated with reference (Kadison 4.5.3), not proved |
| C3 | The GNS representation is irreducible iff the state is pure | strong | standard theorem, proof sketched |

## Concepts

- **State.** A positive linear functional of norm 1 on a C*-algebra.
- **Cyclic vector.** ξ with {π(x)ξ : x ∈ A} norm-dense in H.
- **Left kernel of ρ.** I = {a : ρ(a*a) = 0}.
- **Pure state.** An extreme point of the convex set of states.
- **Universal representation.** The direct sum of the GNS representations
  of all states.

## Connections

The article's sources are Kadison and Ringrose, Arveson, Dixmier and
Sakai. Murray and von Neumann's construction of R/M with
(ξ, η) = f(y*x) is the first form of it ([NOTE-303](NOTE-303.md)). The Riesz–Markov–
Kakutani theorem it uses for C(X) is the measure-theoretic Riesz
theorem, not the Hilbert-space one of [LIT-230](../literature.d/LIT-230.md).

## Bearing on the record

- **[THEORY-004](../theory.d/THEORY-004.md)** cites this article as "the GNS statement". The
  article supports the statement used: a state fixes its cyclic
  representation up to a unitary, and the unitary is the one sending
  π(a)ξ to π′(a)ξ′. Two cautions for that citation.
  - The article is about states on C*-algebras. It never mentions
    positive-definite kernels on a set, RKHS or Moore–Aronszajn, and is
    over the complex numbers. The kernel form, k(x, y) = ⟨Φ(x), Φ(y)⟩
    with minimal realizations unique up to a unitary, comes from
    Jorgensen & Tian ([LIT-259](../literature.d/LIT-259.md), Remark 1.34, Cor. 1.35), as the theory
    already says. This article supports only the analogy at the level of
    algebras.
  - The uniqueness's proof idea is the same as the kernel case's: the
    data fix all inner products ⟨π(a)ξ, π(b)ξ⟩, so the map between the
    dense sets is isometric. That is consistent with the theory's
    sentence "the kernel is the invariant and the representation is one
    realization of it", but the passage to real representation matrices
    and orthogonal maps is not here.
- **[THEORY-017](../theory.d/THEORY-017.md)** names this article for the setting where an
  algebra of observables is supplied from the start, beyond discrete
  bases. The article fits that reading: GNS takes an algebra and a state
  as given and produces the Hilbert space, and its history section says
  Segal took the C*-algebra to be "generated by the observables". It
  says nothing about continuous observables or the absence of
  eigenbases, so the citation marks a setting, as [THEORY-017](../theory.d/THEORY-017.md) uses it,
  and should not be read as support for the claims about continuous
  observables. The directive in [THEORY-017](../theory.d/THEORY-017.md) that calls [LIT-241](../literature.d/LIT-241.md) Deferred
  lapses once the LIT is Active.
- **The skim's kernel analogy.** The skim's open questions (kernels as
  states, L²(data) as the commutative case, the Platonic representation
  hypothesis) are the reader's. The commutative example the article
  gives is C(X) with states as probability measures, and it uses it only
  for irreducibility.
- No instruction for machine-learning practice; nothing for the
  anthology.

## Limitations

- The uniqueness theorem is stated with a reference, not proved here.
- Small slips: the left kernel is said to be a subspace "by the triangle
  inequality", where the usual argument is the Cauchy–Schwarz
  inequality for positive functionals; the history's "the C*-algebra is
  generated by the observables" is loose.
- Nothing on real C*-algebras, on unbounded observables, or on
  non-cyclic representations beyond the direct-sum remark.

## Open questions

- Whether the record wants the kernel form of GNS from a primary source.
  [NOTE-303](NOTE-303.md) (Murray & von Neumann) and [LIT-259](../literature.d/LIT-259.md) (Jorgensen & Tian) are
  nearer to it than this article.
