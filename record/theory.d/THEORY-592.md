---
number: 592
status: Active
formerly:
- THEORY-tmpnon3g
title: "Every unital Banach *-algebra satisfying Gelfand and Naimark's norm conditions is isometrically *-isomorphic to a norm-closed algebra of operators on a Hilbert space, built from positive functionals by what is now the GNS construction, and a commutative one is the algebra of all continuous functions on its compact maximal-ideal space"
version: 1
tags:
- mathematics
- quantum-foundations
date: '2026-10-16'
source:
- LIT-313
summary: >-
  Gelfand & Naimark (1943), [LIT-313](../literature.d/LIT-313.md), read in full in [NOTE-303](../notes.d/NOTE-303.md). Theorem 1
  embeds every normed *-ring in B(H) for a Hilbert space not assumed
  separable; Lemma 1 is the commutative case, resting on Gelfand's 1941
  paper and Šilov's boundary. The paper never says "C*-algebra" or "GNS".
  It assumes two axioms it suspected redundant, and notes that a single
  norm identity may replace two others. It gives the object-level
  isomorphism R ≅ C(𝔐), not a categorical duality, and nothing on
  uniqueness or irreducibility of the representation.
---

# THEORY-592: Every unital Banach *-algebra satisfying Gelfand and Naimark's norm conditions is isometrically *-isomorphic to a norm-closed algebra of operators on a Hilbert space, built from positive functionals by what is now the GNS construction, and a commutative one is the algebra of all continuous functions on its compact maximal-ideal space

## Source

Gelfand & Neumark (1943), "On the imbedding of normed rings into the ring of
operators in Hilbert space", *Matematicheskii Sbornik* 12(54):197–217,
[LIT-313](../literature.d/LIT-313.md), read in full in [NOTE-303](../notes.d/NOTE-303.md) from the Math-Net.Ru text, with the
theorem statements checked against the Russian résumé.

## What was actually shown

**The axioms.** A normed *-ring is a complex Banach algebra with unit e,
‖e‖ = 1, and an involution with x** = x, (xy)* = y*x*, ‖x*x‖ = ‖x*‖·‖x‖,
‖x*‖ = ‖x‖, and e + x*x invertible. The authors note that the third and
fourth may be replaced by ‖x*x‖ = ‖x‖², and suspect the last two follow
from the others (p. 198 footnote).

**Theorem 1 (p. 198).** Every normed *-ring maps isomorphically onto a closed
subring of the bounded operators on a Hilbert space, isometrically and
preserving *. The space is not assumed separable.

**The construction (§3).** For each maximal left ideal M, a positive
functional f with f(e) = 1 vanishing on M is obtained by Banach's separation
lemma and Krein's extension theorem. Setting (ξ, η) = f(y*x) on R/M gives a
Hilbert space on which left multiplication acts by bounded operators. The
direct sum over all M is faithful, because the maximal left ideals intersect
in 0. Corollary 6, that a *-isomorphism of normed *-rings is isometric, makes
the image closed. This is the GNS construction, under no name.

**Lemma 1 (p. 199).** A commutative normed ring with the involution axioms
is isometrically *-isomorphic to the ring of all continuous complex
functions on its compact maximal-ideal space 𝔐, with x* sent to the
conjugate function.

**§4.** The simple weakly closed rings on separable Hilbert space are exactly
the factors of types I_n, II₁ and III (Theorem 3). As a special case, the
compact operators are the only non-trivial closed ideal of B(H) for
separable H (Calkin).

**What could have come out otherwise.** Some abstract normed *-ring could
have failed to be an operator algebra, or a commutative one could have been
a proper subalgebra of C(𝔐). Neither happens.

## What this does not say

- **That Gelfand duality is a categorical duality.** The paper gives the
  object-level isomorphism R ≅ C(𝔐), not functoriality or an equivalence of
  categories ([NOTE-303](../notes.d/NOTE-303.md)).
- **That the commutative machinery is proved here.** It rests on Gelfand's
  "Normierte Ringe" (1941) and Šilov's boundary. For the maximal-ideal space
  itself, that 1941 paper is the primary source.
- **Uniqueness or irreducibility of the representation.** States versus pure
  states are not discussed. [THEORY-004](THEORY-004.md)'s uniqueness up to unitary of a
  minimal realisation is not proved here.
- **That Gelfand, Stone and Pontryagin are one duality.** Lemma 1 is one leg.
  Neither this paper nor the other legs' primary sources ([LIT-353](../literature.d/LIT-353.md), [LIT-333](../literature.d/LIT-333.md))
  state a common duality; that framing is later literature and the owner's
  synthesis.
- **That the extra axioms are needed.** Later work showed them redundant,
  according to standard histories; the reading did not verify it.

## Connections

- [THEORY-020](THEORY-020.md), Stone's representation of Boolean algebras as clopen algebras,
  is the Boolean counterpart of Lemma 1; for a commutative algebra generated
  by projections the two coincide ([NOTE-303](../notes.d/NOTE-303.md)).
- [THEORY-645](THEORY-645.md), Pontryagin duality, is the characters leg.
- [THEORY-004](THEORY-004.md) names the kernel-to-Hilbert-space construction as GNS. This
  paper is where it first appears.
- [THEORY-042](THEORY-042.md) uses §4's factors: an algebra with superselection sectors has a
  non-trivial centre and is not a factor.
- [THEORY-652](THEORY-652.md): Theorem 3 here descends from Wedderburn's trivial-centre
  corollary for simple algebras.
