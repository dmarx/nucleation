---
status: Read
paper: LIT-353
title: 'The Theory of Representations for Boolean Algebras'
version: 1
history:
- version: 1
  date: '2026-09-29'
  note: >-
    Read in full (The full paper, *Transactions of the AMS* 40(1), July
    1936, pp. 37–111, 75 pp., from the Internet Archive's scan of volume 40.
    Trans. AMS issues are renewed only from July 1944, so this is in the US
    public domain; the AMS's own free PDF was blocked here by a Cloudflare
    challenge. I read the whole text through the scan's OCR layer, which is
    good for prose. Where symbols were garbled I checked against context and
    the theorem numbering. I read the Introduction, Chapter I (§§1–4,
    Theorems 1–13), Chapter II (§§1–6, Theorems 14–53, including the
    Fundamental Proposition and Existence Proposition), Chapter III (§§1–4,
    Theorems 54–62, the Lebesgue illustration), Chapter IV (§§1–3, Theorems
    63–70) and all footnotes. Nothing was skipped. Routine calculations
    (e.g. the Huntington-postulate verifications in Theorems 2–4) were
    followed at the level of their steps.). The first NOTE on this paper,
    which was seeded from its abstract alone.
date: '2026-09-29'
summary: >-
  The paper identifies Boolean algebras with Boolean rings with unit (xx =
  x), and generalized Boolean algebras with Boolean rings (Thms 1–4).
  Theorem 67 proves that every Boolean ring A is isomorphic to the algebra
  B(A) of classes 𝔈(a) = {prime ideals p : a ∉ p}, under symmetric
  difference and intersection. Its ideal lattice is isomorphic to the
  system of classes 𝔈(𝔞) under arbitrary unions and finite intersections.
  The existence of enough prime ideals (Thm 63) is proved by transfinite
  induction, and Theorem 70 shows that "every Boolean ring has an
  isomorphic algebra of classes" and "every ideal is the product of its
  prime divisors" are equivalent without choice. Theorems 68–69 classify
  *all* set-representations as restrictions of B(A) to subclasses of prime
  ideals. The topology, i.e. Stone spaces and duality, is explicitly
  deferred to "another paper".
---

# NOTE-tmp1tfdd: The Theory of Representations for Boolean Algebras

## Contribution

The paper solves the representation problem for Boolean algebras: construct an algebra of classes isomorphic to a given one, and indeed describe *all* algebras of classes homomorphic to it. Stone's analogue is Cayley's theorem for groups. The paper notes the analogy is "considerably more recondite": the representing points must be prime ideals, whose existence needs the well-ordering hypothesis (Introduction). The method is to recast Boolean algebras as rings in which every element is idempotent, so that ideal theory applies.

- **Chapter I.** It proves the identification with Huntington's postulates (Thms 2–4), and treats atoms (Thms 6–13).
- **Chapter II.** Subrings and ideals; orthocomplements of ideals and a classification (principal, semiprincipal, simple, normal); prime ideals (Thms 33–41); homomorphisms (Thms 42–49); and direct sums (Thms 50–53).
- **Chapter III.** Analyses concrete algebras of classes: reduction, equivalence, perfection (Thms 54–62).
- **Chapter IV.** Proves the existence of prime ideals (Thm 63), the Fundamental Proposition of Ideal Arithmetic (Thm 66), the perfect representation (Thm 67), and all other representations (Thms 68–69).

## Key insight

Write a ∨ b = a + b + ab, a′ = a + e. A Boolean algebra is then a commutative ring of characteristic 2 in which every element is idempotent, and ideals, quotients and homomorphisms become available. A two-valued homomorphism A → {0, 1} is the same as a prime ideal (its kernel; Thm 49). Mapping a to the set of prime ideals that omit a turns ring operations into set operations (Thm 67). The only question is whether there are enough prime ideals to separate elements, and that is exactly the Fundamental Proposition (Thm 70).

## Assumptions

- **Boolean ring (Def. 1).** A ring in which every element is idempotent. There is no unit assumption: generalized Boolean algebras are included. One-element rings are admitted.
- **Transfinite methods.** The well-ordering (Zermelo) hypothesis is used for Theorem 63 only. Theorems 65, 66 and 70 carefully isolate what follows from it without further choice.
- **Algebra of classes.** A ring of subclasses of a fixed class E, under symmetric difference and intersection. "Reduced" means points are separated and each point lies in some member (Def. 10).

## Key results

- **Theorem 1.** A Boolean ring is commutative, satisfies a + a = 0, and has zero divisors if it has more than 2 elements. It embeds in an essentially unique Boolean ring with unit. A finite Boolean ring has a unit and 2ⁿ elements.
- **Theorem 2.** Boolean rings with unit are Boolean algebras in Huntington's sense (a ∨ b = a + b + ab, a′ = a + e), and conversely (a + b = ab′ ∨ a′b, ab = (a′ ∨ b′)′). Theorems 3–4 do the same for Stone's lattice-style postulates and for generalized Boolean algebras without unit.
- **Theorems 8, 11 and 12.** A ring with a complete atomic system is isomorphic to the classes 𝔖(b) of atoms under b (Thm 8). A ring with an atomic basis ≅ the finite subclasses of a set (Thm 11). "A finite Boolean ring with at least two elements contains an atomic basis 𝔖 and is therefore isomorphic to the algebra of all subclasses of a finite class" (Thm 12).
- **Theorems 19–32, the ideal lattice.** The ideals form a distributive lattice (Thm 18), with orthocomplement 𝔞′ = annihilator (Def. 7). Normal ideals (𝔞 = 𝔞″) under normalized join form a Boolean algebra whose normal ideals are all principal (Thm 29): a completion-type embedding. Principal ideals ≅ A (Thm 31).
- **Theorem 33.** Divisorless (maximal), prime and primary ideals coincide.
- **Theorem 36.** With a unit, a prime ideal contains exactly one of a, a′.
- **Theorem 38.** A prime ideal is normal iff it is 𝔞′(a) with a atomic.
- **Theorem 40.** A prime ideal dividing a finite product 𝔞𝔟 divides 𝔞 or 𝔟. The paper notes explicitly that this fails for infinite products.
- **Theorem 49.** An ideal p is prime iff A/p is the two-element Boolean ring.
- **Theorem 51.** A ≅ (A/𝔞) ⊕ (A/𝔞′) for a simple ideal 𝔞, and conversely.
- **Theorem 52.** A Boolean ring is reducible iff it has more than two elements.
- **Theorem 53.** A is a direct sum of two-element rings iff A ≅ the algebra of all subclasses of some set. So infinite Boolean rings are "in general" not completely reducible.
- **Theorems 57–62.** For an algebra of classes, the ideal-to-union map 𝔞 ↦ E(𝔞) and its converse. "Perfect" (Def. 12) iff the Fundamental Proposition holds and each prime ideal omits exactly one point (Thm 59). A is isomorphic to a *complete* power-set algebra iff every normal ideal is principal and A has a complete atomic system (Thm 62).
- **§III.4, the Lebesgue illustration.** For Lebesgue-measurable subsets of the plane of finite measure, the ideal classes are all distinct, and no normal prime ideal contains every null set.
- **Theorem 63 (Fundamental Existence Proposition).** "In a Boolean ring A containing at least two elements, there exists at least one prime ideal." Two transfinite-induction proofs are given, the second building a homomorphism onto {0, 1} step by step.
- **Theorem 64.** If a ≤ b is false, there is a prime ideal containing b but not a. Theorem 65 derives this from Theorem 63 without further transfinite methods.
- **Theorem 66 (Fundamental Proposition of Ideal Arithmetic).** "In a Boolean ring A, every ideal other than 𝔢 is the product of all its prime ideal divisors."
- **Theorem 67 (the representation theorem).** With 𝔈 the class of all prime ideals and 𝔈(𝔞) the prime ideals not dividing 𝔞, 𝔞 ↦ 𝔈(𝔞) is an isomorphism of the ideal system (unrestricted joins, finite meets) onto the classes 𝔈(𝔞) (arbitrary unions, finite intersections). With 𝔈(a) = 𝔈(𝔞(a)), a ↦ 𝔈(a) is an isomorphism of A onto the algebra of classes B(A): 𝔈(a + b) = 𝔈(a) △ 𝔈(b), 𝔈(a ∨ b) = 𝔈(a) ∪ 𝔈(b), 𝔈(ab) = 𝔈(a)𝔈(b). B(A) is a *perfect reduced* algebra of classes, the "perfect representation" (Def. 13).
- **Theorem 68.** For any subclass ℌ ⊆ 𝔈, restriction gives a homomorphism B(A) → B(A, ℌ) ≅ B(A/𝔞(ℌ′)). It is perfect iff 𝔈(𝔞(ℌ′)) = ℌ′.
- **Theorem 69.** *Every* algebra of classes homomorphic to A is equivalent to some B(A, ℌ). The only perfect isomorphic representations are those equivalent to B(A).
- **Theorem 70.** Without transfinite methods, these are equivalent: (1) every Boolean ring has an isomorphic algebra of classes; (2) the Fundamental Proposition of Ideal Arithmetic holds in every Boolean ring.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Boolean algebras = Boolean rings with unit; generalized Boolean algebras = Boolean rings | proof | Thms 1–4 |
| C2 | Finite Boolean rings ≅ power sets of their atoms | proof | Thms 11–12 |
| C3 | Prime = maximal = primary ideals; prime ⇔ quotient is {0, 1} | proof | Thms 33, 49 |
| C4 | Prime ideals exist in every Boolean ring with ≥ 2 elements | proof (well-ordering) | Thm 63, two proofs |
| C5 | Every Boolean ring is isomorphic to the algebra of sets 𝔈(a) of prime ideals omitting a; ideals ↔ unions of such sets | proof | Thm 67 (via Thms 40, 64, 66) |
| C6 | All set-representations arise by restricting B(A) to a subclass of prime ideals | proof | Thms 68–69 |
| C7 | Representability of all Boolean rings ⇔ the Fundamental Proposition, choice-free | proof | Thm 70 |
| C8 | Infinite Boolean rings are in general not direct sums of irreducibles | proof (via Thm 53 and non-atomic examples) | Thm 53 and discussion |
| C9 | The representation theory "can appropriately be stated in topological terms" | assertion (deferred) | Ch. IV §1; no topology in this paper |

## Method

Ring-theoretic reformulation; ideal theory (annihilator orthocomplement, normal ideals); transfinite induction; construction of the representation on the set of prime ideals.

## Concepts

- **Boolean ring; generalized Boolean algebra.**
- **Orthocomplement 𝔞′ of an ideal.** Its annihilator.
- **Principal, semiprincipal, simple and normal ideals** (Def. 8).
- **Prime (= divisorless = primary) ideal.**
- **Algebra of classes;** reduced, equivalent and perfect (Defs. 10–12).
- **Perfect representation B(A)** (Def. 13).
- **Fundamental Existence Proposition; Fundamental Proposition of Ideal Arithmetic.**

## Connections

- **[LIT-298](../literature.d/LIT-298.md) (Kochen–Specker).** Their Theorem 0, that embeddability in a Boolean algebra holds iff Z₂-homomorphisms separate points, is Stone's Theorem 49 + 64 + 67 read as a criterion and extended to partial Boolean algebras. Their Theorem 1 says a certain partial Boolean algebra has *no* prime ideals in Stone's sense (no homomorphism to Z₂).
- **[LIT-306](../literature.d/LIT-306.md) (Birkhoff–von Neumann).** BvN cite Stone's 1934 PNAS announcement for "every field of sets is isomorphic with a Boolean algebra, and conversely" (their §§5, 10). This paper is the full version.
- **[LIT-313](../literature.d/LIT-313.md) (Gelfand–Naimark).** Lemma 1 there (commutative C*-algebra ≅ C(maximal ideal space)) is the analogue of Theorem 67 with prime/maximal ideals as points. Stone's introduction says his interest arose from "the spectral theory of symmetric transformations in Hilbert space".
- **[LIT-333](../literature.d/LIT-333.md) (Pontryagin).** A Boolean ring is an exponent-2 abelian group under +. Its prime ideals correspond to certain characters into ℤ/2, namely the multiplicative ones, not all of them. Neither paper draws the connection.
- **[LIT-332](../literature.d/LIT-332.md) (Zaslavsky), [LIT-267](../literature.d/LIT-267.md) (Xiong).** See Bearing.
- **[LIT-337](../literature.d/LIT-337.md) (Wille, Boolean Concept Logic), [LIT-344](../literature.d/LIT-344.md) (Ganter–Wille).** FCA concept lattices are complete lattices, generally not distributive. Stone's representation applies only after passing to a Boolean algebra.

## Bearing on the record

- **Map row 8 and §2 item 2, "the Stone leg of the duality tripod; ultrafilters ↔ topes".**
  - *What the paper owns.* The representation (algebra → sets of two-valued homomorphisms), stated with prime ideals, not ultrafilters.
  - *What it does not own.* The duality with Stone spaces. That is the 1937 paper, which the seed notes as unregistered. If the owner's text says "Stone duality", this entry is the wrong primary, or at least an incomplete one.
- **"Ultrafilters ↔ topes".** For the finite case, which is what a finite hyperplane arrangement gives, Stone's relevant result is simpler.
  - *The finite case.* By Theorems 12 and 38, a finite Boolean algebra is the power set of its atoms. Its prime ideals are exactly 𝔞′(a) for atoms a, so ultrafilters are principal and correspond one-to-one with atoms.
  - *My own observation, not the paper's.* So "ultrafilters = topes" amounts to "topes = atoms of the Boolean algebra generated by the arrangement's half-spaces". Whether that holds depends on the generating sets. If open half-spaces and their complements generate the algebra, its atoms are all the sign-vector cells, i.e. all faces, lower-dimensional ones included, not only the topes (full-dimensional regions). The owner's identification needs to say which algebra is meant.
  - *What to cite.* Stone supplies only the generic "points = two-valued homomorphisms" principle. The tope side is Zaslavsky's ([LIT-332](../literature.d/LIT-332.md), unread here) or the oriented-matroid literature.
- **The single-Boolean-context diagnosis.** Stone's Theorem 67 is exactly why a single Boolean context is always "classical": any Boolean algebra has a set representation, i.e. enough global two-valued valuations. KS ([LIT-298](../literature.d/LIT-298.md)) shows what fails when contexts are glued. That pairing is the owner's point, and it is correct as far as these two papers go.
- **ML practice.** It carries nothing, and does not belong in the Anthology.

## Limitations

- **No topology.** No compactness or Stone space, and no categorical duality.
- **Heavy dependence on the well-ordering hypothesis for existence.** The paper is candid about this (Thm 70 isolates it).
- **Long.** Much of Chapters II–III (normal and simple ideal classification) is not needed for the representation theorem, and several questions are left "to another occasion" (e.g. whether the relations 𝔓 ≠ 𝔓*, 𝔓* = 𝔖 are compatible, Ch. II §3).

## Open questions

- The paper's own: the topological statement of the representation (done in Stone 1937), and the complete classification of ideals. For the record: whether the owner's "ultrafilters ↔ topes" is about the Boolean algebra generated by the half-spaces (atoms = faces) or about maximal covectors (topes). Only the latter matches the oriented-matroid usage.

## Corrections to the seeded skim

- Seeded from metadata; the text shows the summary's first clause is right. "Proves every Boolean algebra is isomorphic to a field of sets (via its prime ideals/ultrafilters)" matches Theorem 67. The second clause, "the representation theorem underlying Stone duality between Boolean algebras and Stone spaces", is a later gloss. This paper contains no topology on the set of prime ideals, no Stone space, and no duality of categories. Chapter IV §1 says the relations "can appropriately be stated in topological terms", and this "will be carried out in another paper".
- The word "ultrafilter" does not occur, and nor does "filter". Everything is done with prime ideals: equivalently maximal ideals (Thm 33) and kernels of homomorphisms onto the two-element ring (Thm 49). A prime ideal contains exactly one of a, a′ (Thm 36). Ultrafilters are the complements, but the paper never says so.
- The printed title is "The Theory of Representations for Boolean Algebras" (plural "Representations"), as the seed notes. The `title:` below is corrected to the printed form; the seed's singular is Crossref's. The paper was received 10 October 1935, and presented in part 25 February 1933. The author's affiliation is Harvard University.
- Footnote to Chapter IV §1: Garrett Birkhoff independently obtained a more general representation for distributive lattices (Proc. Camb. Phil. Soc. 29, 1933, Thm 25.2) "only slightly later". Via MacNeille's embedding of distributive lattices in Boolean algebras, Stone regards it as included here.
