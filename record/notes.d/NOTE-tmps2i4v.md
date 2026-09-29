---
status: Read
paper: LIT-313
title: 'On the imbedding of normed rings into the ring of operators in Hilbert space'
version: 1
history:
- version: 1
  date: '2026-09-29'
  note: >-
    Read in full (The original article, *Matematicheskii Sbornik* 12(54):2
    (1943), pp. 197–217, from the free full-text PDF on Math-Net.Ru (paper
    sm6155). It has a text layer. I read the English text in full (§1
    Fundamental notions; §2 Some lemmas, with Lemmas 1–2 and Corollaries
    1–6; §3 Proof of Theorem 1; §4 Weakly closed rings, with Lemmas 3–5,
    Corollaries 7–9, Theorems 2–3 and the Remark), the references, and the
    Russian résumé (pp. 213–217), which I checked against the English for
    the theorem statements. Nothing was skipped. The text layer garbles some
    symbols, and I resolved them from context. I did not read the 1994
    *Contemporary Mathematics* 167 reprint, which is the DOI in the seed.).
    The first NOTE on this paper, which was seeded from its abstract alone.
date: '2026-09-29'
summary: >-
  Theorem 1 is the first abstract characterisation of C*-algebras. Every
  normed *-ring (a unital Banach *-algebra with ‖x*x‖ = ‖x*‖·‖x‖, ‖x*‖ =
  ‖x‖, and e + x*x invertible) is isometrically *-isomorphic to a
  norm-closed *-subalgebra of the bounded operators on some, not
  necessarily separable, Hilbert space. The proof builds, for each maximal
  left ideal M, a positive functional f vanishing on M. The inner product
  is (ξ, η) = f(y*x) on R/M, and the construction takes the direct sum
  over all M. This is the GNS construction. Lemma 1 is the commutative
  case: such an algebra is isometrically *-isomorphic to C(𝔐) for its
  compact maximal-ideal space. §4 adds that the simple weakly closed rings
  on separable Hilbert space are exactly the factors of types I_n, II₁ and
  III (Theorem 3).
---

# NOTE-tmps2i4v: On the imbedding of normed rings into the ring of operators in Hilbert space

## Contribution

The paper characterises intrinsically, by norm and involution axioms alone, the Banach algebras that are (isometrically, *-preservingly) algebras of Hilbert-space operators (Theorem 1). Along the way it proves:

- **Lemma 1.** The commutative case, as the full algebra of continuous functions on a compact Hausdorff space.
- **Corollaries 1–5.** Spectral facts: Hermitian elements have real spectrum, positive elements have square roots, and positives form a cone.
- **Corollary 6.** Automatic isometry of *-isomorphisms.

§4 applies the embedding to von Neumann's weakly closed rings. It shows which factors are simple (Theorems 2–3), and, as a remark, recovers Calkin's result that the compact operators are the only closed ideal of B(H) for separable H.

## Key insight

A positive linear functional on the algebra turns the algebra itself into a pre-Hilbert space via (x, y) = f(y*x). Left multiplication then acts by bounded operators, bounded because ‖a‖²e − a*a is positive. Taking enough such functionals (one per maximal left ideal) makes the representation faithful. Corollary 6 makes it isometric: for Hermitian elements the norm is the spectral radius, which an injective *-homomorphism cannot change.

## Assumptions

- **Normed ring (§1).** A complex Banach space with an associative bilinear multiplication, ‖xy‖ ≤ ‖x‖‖y‖, and a unit e with ‖e‖ = 1.
- **The *-axioms.** 2′–6′ as listed in the corrections. The commutative Lemma 1 assumes 2′, 3′ in the form (xy)* = x*y*, and 4′.
- **External results used.** Gelfand's "Normierte Ringe" (1941) for the Gelfand representation and its Theorems 6, 8′, 8, 10 and 17; Šilov's minimal boundary; Banach's separation lemma; Krein's extension theorem for positive functionals on cones with interior points; Murray–von Neumann for §4.
- **§4.** Separable Hilbert space.

## Key results

- **Theorem 1 (p. 198, verbatim).** "Every normed *-ring can be isomorphically mapped onto a closed subring R₁ of the set B of all bounded operators in a Hilbert space 𝔥 in such a manner that, if x ∈ R and X ∈ R₁ correspond to each other, then ‖x‖ = ‖X‖ and x*, X* also correspond to each other by this mapping."
- **Lemma 1 (p. 199).** A commutative normed ring with an operation satisfying 2′, 3′ ((xy)* = x*y*) and 4′ can be isomorphically mapped onto the ring of *all* complex continuous functions x(M) on a bicompact space 𝔐, with ‖x‖ = max|x(M)| and x* ↦ the conjugate function. The proof has two steps. First, ‖x²‖ = ‖x‖², so there are no generalised nilpotents and the Gelfand transform is isometric. Second, the Šilov boundary is shown to be *-invariant and hence equal to 𝔐, and Stone–Weierstrass-type Theorem 6 of [3] gives all of C(𝔐). Lemma 1 implies 5′ and 6′ in the commutative case.
- **Corollaries 1–5 (pp. 201–202).** (1) Hermitian elements have real spectrum. (2) A positive h has a positive square root. (3) If h₁ > 0 is invertible then h₁ + ih₂ is invertible. (4) If h₁, h₂ ≥ 0 and h₁ is invertible, then h₁h₂ has positive spectrum. (5) The sum of positives is positive. Also, x*x is positive for all x (from 6′).
- **Lemma 2 (p. 202).** An algebraic isomorphism from a Lemma-1 ring onto a normed ring without generalised nilpotents is automatically continuous, and the target is complete.
- **Corollary 6 (p. 203).** A *-isomorphism between normed *-rings is isometric, so its image is closed. This does not use 6′.
- **§3, the proof of Theorem 1.** Take M a maximal left ideal and H the Hermitian elements. P = {m + m*} is at distance 1 from e. Banach's lemma gives f on ℝe + P̄ with f(e) = 1 and f(P̄) = 0, and Krein's theorem extends it positively. Setting (ξ, η) = f(y*x) on R/M gives a Hilbert space, positive definite by maximality of M. Left multiplication gives φ(a) with ‖φ(a)‖ ≤ ‖a‖ and φ(a*) = φ(a)*. If R is simple this is already faithful. Otherwise take the direct sum over all maximal left ideals. Faithfulness follows because the intersection of all maximal left ideals is 0 (via the spectrum of a*a).
- **Consequences (p. 209).** Steen's rings are operator rings, so Steen's results follow from Murray–von Neumann. Quotients of closed *-subrings of B(H) embed in B(H′).
- **Lemma 3.** In a weakly closed ring, a left ideal containing no non-zero projections is 0.
- **Lemma 4.** In a factor, ideals are closed under equivalence of projections.
- **Corollary 7.** Ideals of a factor on separable H contain no infinite projections.
- **Corollaries 8 and 9.** Factors of type III and of finite type are simple.
- **Lemma 5.** Simple weakly closed rings are factors.
- **Theorem 2.** Factors of class I_∞ or II_∞ in separable H are not simple. They have exactly one non-trivial uniformly closed two-sided ideal, generated by the finite projections.
- **Theorem 3 (p. 212).** "The only simple weakly closed rings in the separable Hilbert space are the factors of the classes I_n, II₁ and III."
- **The Remark (p. 212).** For R = B, I₀ is the compact operators, and B/I₀ (simple, a *-ring) embeds by Theorem 1. This recovers Calkin's result.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Every normed *-ring embeds isometrically and *-preservingly in B(H) | proof | Theorem 1, §§2–3 |
| C2 | A commutative ring satisfying 2′, 3′, 4′ is isometrically *-isomorphic to C(𝔐) | proof (relies on Gelfand 1941 and Šilov) | Lemma 1 |
| C3 | Axioms 5′, 6′ follow from 1′–4′ | conjecture (authors' footnote) | p. 198 footnote; proved later by others (unverified here) |
| C4 | 4′ and 5′ are jointly replaceable by ‖x*x‖ = ‖x‖² | proof (one line) | p. 198 footnote |
| C5 | *-isomorphisms of normed *-rings are isometric | proof | Corollary 6 |
| C6 | Simple weakly closed rings on separable H = factors of types I_n, II₁, III | proof, using Murray–von Neumann | Theorem 3 |
| C7 | The compact operators are the unique closed ideal of B(H), H separable (Calkin) | proof, as a special case | Theorem 2 and the Remark |

## Method

Banach-algebra spectral theory (maximal ideals, Gelfand transform); positive-functional extension (Banach, Krein); construction of a representation space from a functional (GNS); Murray–von Neumann dimension theory for §4.

## Concepts

- **Normed ring.** A unital Banach algebra.
- **Normed *-ring.** In modern terms, a unital C*-algebra, under the stated axioms.
- **Hermitian, positive element.** h* = h; real, non-negative spectrum.
- **Generalised nilpotent.** lim ‖xⁿ‖^{1/n} = 0.
- **Weakly closed ring, factor.** A von Neumann algebra, and one with trivial centre.

## Connections

- **[LIT-241](../literature.d/LIT-241.md) (GNS construction, Wikipedia).** The Hilbert space R/M with (ξ, η) = f(y*x) is the GNS construction for the state f. [LIT-241](../literature.d/LIT-241.md) is a secondary account, and this paper is the primary source of its first form.
- **[THEORY-004](../theory.d/THEORY-004.md).** It names the kernel-to-Hilbert-space construction as GNS, citing [LIT-259](../literature.d/LIT-259.md). This paper is the origin of that construction. [THEORY-004](../theory.d/THEORY-004.md)'s uniqueness-up-to-unitary for minimal realisations is not proved here; the paper does not discuss uniqueness of the representation.
- **[LIT-274](../literature.d/LIT-274.md) (Coecke–Pavlovic–Vicary).** Its key step is "the spectral theorem for finite-dimensional commutative C*-algebras", i.e. the finite case of Lemma 1: a commutative C*-algebra is ℂⁿ = C(n points). The basis vectors are the characters, i.e. the points of 𝔐.
- **[LIT-353](../literature.d/LIT-353.md) (Stone) and [LIT-333](../literature.d/LIT-333.md) (Pontryagin).** Lemma 1 is the C*-algebraic counterpart of Stone's representation. Stone represents a Boolean algebra as the clopen sets of its spectrum; Lemma 1 represents a commutative C*-algebra as C(spectrum). For a commutative C*-algebra generated by projections, the two coincide. The paper does not say this.
- **[LIT-321](../literature.d/LIT-321.md) (Haag), [LIT-339](../literature.d/LIT-339.md) (WWW).** §4's factors are the algebras with trivial centre. Superselection sectors correspond to a non-trivial centre, which is exactly what makes an algebra *not* a factor.

## Bearing on the record

- **Map §2 item 2, "the Gelfand leg of the Gelfand/Stone/Pontryagin duality tripod (operator face ↔ spectrum)".** Lemma 1 supplies the commutative "operator face ↔ spectrum" leg exactly, with two cautions.
  - *The map's wording.* "Gelfand duality" as a categorical duality (contravariant equivalence between commutative C*-algebras and compact Hausdorff spaces) is not stated here. The paper gives the object-level isomorphism R ≅ C(𝔐), not the functoriality.
  - *Where the commutative result is.* Much of the commutative machinery is Gelfand's 1941 "Normierte Ringe" (reference [3]), which the seed notes as the unregistered alternative. If the owner wants the spectrum/maximal-ideal space itself, that paper is the primary source. If the owner wants the C*-identity-based characterisation, this one is.
- **The "tripod" as one duality.** The paper gives no support for unifying the Gelfand, Stone and Pontryagin results as one duality; that framing is the owner's (and standard in later literature). Lemma 1 is the operator-algebra leg of it.
- **Map rows 5–6 (sectors = centre).** §4's factor/non-factor distinction is the algebraic setting of superselection. Here it is used only to classify simple rings, not physics.
- **ML practice.** It carries nothing, and does not belong in the Anthology.

## Limitations

- **Unital algebras only.** The axioms are redundant (5′, 6′), as the authors suspected.
- **Heavy reliance on cited results.** The commutative part depends on [3] and Šilov. §4 depends on Murray–von Neumann, and holds for separable H only.
- **No uniqueness.** Nothing is said about uniqueness of the representation or about irreducibility (states versus pure states).

## Open questions

- Posed by the paper: whether 5′ and 6′ follow from 1′–4′. Later answered affirmatively in the literature, according to standard histories; not verified here.

## Corrections to the seeded skim

- Seeded from metadata; the text confirms the summary, with three precisions. (1) The paper does not use the term "C*-algebra" (the term is later); it says "normed *-ring". The axioms are 2′ x** = x, 3′ (xy)* = y*x*, 4′ ‖x*x‖ = ‖x*‖·‖x‖, 5′ ‖x*‖ = ‖x‖, and 6′ x*x + e invertible, with a unit assumed. The footnote to p. 198 says the authors "suppose the last two axioms to be corollaries of 1′–4′ but have not succeeded in proof". It adds that 4′ and 5′ may be replaced by ‖x*x‖ = ‖x‖². (2) The commutative "Gelfand duality" statement is *Lemma 1* (p. 199), not a main theorem. It rests on Gelfand's "Normierte Ringe" [3] and Šilov's boundary, and it uses the commutative form 3′ (xy)* = x*y*. (3) The Hilbert space is explicitly not assumed separable (footnote, p. 198).
- On the venue and identifiers. The original is *Mat. Sb.* 12(54), no. 2, pp. 197–217, received 22 August 1941. I verified this on the Math-Net.Ru copy, which the seed could not reach. The seed's DOI (10.1090/conm/167/16) is the 1994 AMS reprint and is correct as a DOI, but it identifies the reprint. The authors are printed "I. Gelfand (Moscow) and M. Neumark (Moscow)", and in Russian И. М. Гельфанд и М. А. Наймарк.
- The paper does not name a "GNS construction", and Segal is later. What it contains is the construction of a representation from a positive functional f with f(e) = 1 vanishing on a maximal left ideal, via Krein's cone-extension theorem (pp. 204–207).
