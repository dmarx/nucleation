---
status: Read
paper: LIT-tmpctdnu
title: 'Applications of the theory of Boolean rings to general topology'
version: 1
history:
- version: 1
  date: '2026-09-29'
  note: >-
    Read in full (The full paper, *Transactions of the AMS* 41(3), May 1937,
    pp. 375–481 (107 pp.), from the Internet Archive's scan of volume 41
    (January–June 1937). Trans. AMS issues are renewed only from July 1944,
    so the 1937 volume is in the US public domain. The AMS's own PDF (DOI
    landing) returned a 403 challenge here. I read the whole text through
    the scan's OCR layer, which is good for prose but garbles script letters
    (Stone's German-letter names for spaces and families) and some inline
    symbols; these were resolved from context and theorem numbering. I read
    the Introduction, Chapter I "Boolean spaces" (§§1–3, Theorems 1–13,
    Definitions 1–2), Chapter II "Maps in Boolean spaces" (§§1–5, Theorems
    14–59, Definitions 3–18), Chapter III "Stronger separation conditions"
    (§§1–3, Theorems 60–93, Definitions 19–22) and all footnotes. Nothing
    was skipped. Proofs were followed at the level of their steps, not
    re-derived (for instance the long Theorem 29 and Theorem 36
    constructions). The volume's errata page (p. 482) concerns other papers.
    No anthology entry exists for this paper (literature.d searched by title
    and author).). The first NOTE on this paper, which was seeded from its
    abstract alone.
date: '2026-09-29'
summary: >-
  Stone topologises the set 𝔈 of prime ideals of a Boolean ring by taking
  the sets 𝔈(a) as a basis. 𝔈 is then a totally disconnected, locally
  bicompact Hausdorff space, bicompact exactly when the ring has a unit
  (Thm 1), and every such space arises this way (Thm 2). Theorem 4 states
  that "the algebraic theory of Boolean rings is mathematically equivalent
  to the topological theory of Boolean spaces": isomorphism ↔
  homeomorphism, ideals ↔ open sets, quotients ↔ closed subsets, unit ↔
  bicompactness, and subrings ↔ continuous images (Thm 7). The same paper
  also contains what are now called the Stone–Čech compactification (Thms
  78–79, 88), the Stone–Weierstrass theorem (Thm 82), the Banach–Stone
  theorem (Thm 83) and closed ideals of C(X) ↔ closed sets (Thm 85).
---

# NOTE-tmpulz62: Applications of the theory of Boolean rings to general topology

## Contribution

The paper does three things.

- **Chapter I.** It turns the 1936 representation of Boolean rings ([LIT-353](../literature.d/LIT-353.md)) into a two-way equivalence between Boolean rings and a class of topological spaces, which Stone names Boolean spaces.
- **Chapter II.** It uses bicompact Boolean spaces as universal targets for "maps", in which the points of an arbitrary T₀-space are represented by closed subsets. From this it concludes that "the algebraic theory of Boolean rings (with unit) is mathematically equivalent to the topological theory of T₀-spaces" (Thm 27). It then applies the machinery to extension problems, including two open problems of Alexandroff and Urysohn (Thms 52, 53).
- **Chapter III.** It specialises the theory to semi-regular (a class Stone introduces here), regular and completely regular spaces. For the completely regular case it develops the ring of bounded continuous real functions. That development produces the maximal compactification (Thms 78–79, 88), a generalised Weierstrass approximation theorem (Thm 82), the isometry theorem (Thm 83) and the ideal–closed-set correspondence (Thm 85).

## Key insight

Give the prime ideals of a Boolean ring the topology whose basic open sets are 𝔈(a) = {p : a ∉ p}. The elements of the ring are then exactly the compact open sets. Everything algebraic about the ring becomes something topological about the space: ideals become open sets, quotients become closed subsets, and a unit becomes compactness. The translation runs both ways, because the ring can be recovered from any such space as the ring of its compact open sets (Thm 2). Stone's later remark (p. 476) that the same pattern holds for compact Hausdorff spaces and their rings of continuous functions (Thms 85–87 against Thms 4, 7, 9, 10) is the germ of the "one algebraic origin" view of these dualities. He offers it as a surmise.

## Assumptions

- **Boolean rings** in the sense of R ([LIT-353](../literature.d/LIT-353.md)): rings in which every element is idempotent, possibly without unit. Notation ·, ∨, +, <, ′ is carried over from R (p. 378).
- **Topological spaces** are T₀-spaces throughout. Stone argues that these are "essentially the most general spaces which are of real interest" (p. 377). "H-space" means Hausdorff and "bicompact" means compact in the covering sense. A Boolean space is "a totally-disconnected locally-bicompact H-space" (Def. 1), with "totally-disconnected" defined as separation of distinct points by a clopen partition (footnote, p. 378).
- **Choice.** The existence of enough prime ideals is imported from R Theorem 63 (well-ordering). Transfinite induction is used again for minimal X-sets (Thm 31) and for the bicompactness criterion in Thm 53.
- **Chapter III** assumes the classical facts it cites from Alexandroff–Hopf, *Topologie I* (AH), and Tychonoff 1930. Theorem 75's function-ring facts are "left to the reader" as familiar from elementary analysis. Theorem 83 uses the Mazur–Ulam theorem, cited from Banach's book.

## Key results

**Chapter I: Boolean spaces (pp. 378–394)**

- **Theorem 1.** Let 𝔈 be the prime ideals of a Boolean ring A, topologised by either of two equivalent neighbourhood systems: the sets 𝔈(𝔞) for ideals 𝔞, or the sets 𝔈(a) for elements a. Then 𝔈 is a totally disconnected, locally bicompact H-space. The 𝔈(𝔞) are exactly its open sets and the 𝔈(a) exactly its bicompact open sets. Its character equals the cardinal of A when A is infinite, and "𝔈 is bicompact if and only if A has a unit e".
- **Theorem 2.** Conversely, the bicompact open subsets of any totally disconnected, locally bicompact H-space form a Boolean ring whose prime-ideal space is homeomorphic to the original space.
- **Theorem 3.** Closed and open subsets of Boolean spaces are Boolean spaces. A continuous image of a bicompact Boolean space is a Boolean space iff it is totally disconnected.
- **Theorem 4 (the equivalence).** (1) Every Boolean ring has a representative Boolean space, every Boolean space represents some ring, and two rings are isomorphic iff their representatives are homeomorphic. (2) The automorphism group of the ring is isomorphic to the homeomorphism group of the space. (3) Ideals of A correspond to open subsets, with 𝔈(𝔞) representing 𝔞. (4) Homomorphic images of A correspond to closed subsets, with 𝔈′(𝔞) representing A/𝔞. (5) Rings with unit correspond to bicompact spaces.
- **Theorem 5.** The classes of ideals from R Definition 8 are characterised topologically. Arbitrary ideals give open sets, normal ideals regular open sets, simple ideals clopen sets, semiprincipal ideals bicompact or co-bicompact open sets, and principal ideals bicompact open sets. **Theorem 6.** A prime ideal p is normal iff p is an isolated point.
- **Theorem 7.** Subrings B of A, under a cofinality condition, correspond to the Boolean spaces that are continuous images of the representative of A. For A with unit, the subrings containing e correspond exactly to its totally disconnected continuous images.
- **Theorem 8.** The non-bicompact Boolean spaces are exactly the non-closed open subsets of bicompact ones, obtained by deleting one non-isolated point. Algebraically, every Boolean ring without unit is a non-principal prime ideal in an essentially unique ring with unit.
- **Theorems 9–13 (universal objects).** 𝔅_c = {0,1}^A, with |A| = c and a basis of finite Boolean combinations of coordinate cylinders, is a bicompact Boolean space of character c (Thm 9). Every Boolean space of character ≤ c embeds in it, and every Boolean ring with unit of cardinal ≤ c is a homomorph of its ring 𝔄_c (Thm 10). 𝔄_c and its prime ideals are the free Boolean rings with and without unit on c generators (Thms 11–12). For c = ℵ₀ the space is the Cantor discontinuum (Thm 13), which "explains in some measure the frequent occurrence of the Cantor discontinuum" (p. 393).

**Chapter II: Maps in Boolean spaces (pp. 394–441)**

- **Theorem 14 and Definitions 3–9.** A family 𝔛 of distinct closed sets in a T₁-space 𝔖 becomes a T₀-space when the subfamilies {𝔛 ⊂ 𝔊}, for 𝔊 open, are taken as neighbourhoods. It is a T₁-space iff no member contains another. A "map" m(ℜ, 𝔖, 𝔛) represents ℜ by such a family, and a "Boolean map" is one into a bicompact Boolean space.
- **Theorem 22 (after Kolmogoroff).** The map exhibits ℜ as a continuous image of ∪𝔛 iff 𝔛 is a continuous family.
- **Theorem 26.** Every T₀-space has a Boolean map. Take a "basic ring" A of subsets containing ℜ, whose interiors form a basis, and represent each point r by the closed set 𝔛(r) = 𝔈′(𝔞(r)) in 𝔈(A), where 𝔞(r) = {a : r ∉ a⁻}.
- **Theorem 27.** "The algebraic theory of Boolean rings (with unit) is mathematically equivalent to the topological theory of T₀-spaces." Stone glosses this as reducing the construction of T₀-spaces to "a kind of tactical game with the closed subsets of bicompact Boolean spaces" (p. 407).
- **Theorems 28–37.** The nowhere-dense sets of a basic ring give a set of redundancy (Thm 28). All algebraic maps give equivalent reduced maps and a canonical continuous image ℜ* (Thm 29). X-sets and minimal X-sets are introduced and characterised (Thms 30–37).
- **Theorems 38–50 (extensions).** Every immediate extension is obtained from the complete algebraic map by adjoining X-sets (Thm 41), with specialisations for strict, T₁- and H-extensions. Theorem 50 is the covering criterion for absolute closure under H-extension: every open cover has a finite subfamily whose closures cover.
- **Theorem 51.** The T₀-space Ω_c of all closed subsets of 𝔅_c is universal for T₀-spaces of character ≤ c.
- **Theorem 52.** Every T₀-space has a strict H-extension of the same character that is absolutely closed with respect to H-extension. This answers a question of Alexandroff and Urysohn (1929).
- **Theorem 53.** An H-space is bicompact iff every closed subset is absolutely closed with respect to H-extension. Alexandroff and Urysohn had proposed this, but proved it only for separable spaces (footnote, p. 436).
- **Theorems 54–59.** Totally disconnected T₀-spaces are the spaces with a one-to-one continuous image inside a Boolean space (Thm 54). Discrete (Alexandroff) spaces are partially ordered sets (Thms 56–58), and the embedding of posets in Boolean rings is credited to MacNeille. Finite T₀-spaces are subspaces of abstract n-simplices (Thm 59).

**Chapter III: Stronger separation conditions (pp. 441–481)**

- **Definition 19 and Theorems 60–67.** A semi-regular (SR) space is one whose regular open sets form a basis. SR-spaces are exactly those with a densely distributed Boolean map (Thm 63), and T₀-, T₁- and H-spaces need not be SR (Thm 64).
- **Theorems 68–73.** Regular ⇒ SR and H (Thm 68). A space is regular iff it has a continuous Boolean map (Thm 69). Among H-spaces, "the bicompact spaces are characterized topologically as the continuous images of bicompact Boolean spaces" (Thm 72). There is an SR H-space that is not regular (Thm 73, built on the Cantor set).
- **Theorems 74–77.** Completely regular (CR) spaces are defined, and 𝔐, the ring of bounded continuous real functions with the sup norm, is set up (Thm 75). An ideal is maximal ("divisorless") iff 𝔐/𝔄 ≅ ℝ; the proof goes through an archimedean ordering of the quotient field (Thm 76). Every T₀-space has a CR continuous image ℜ* with an analytically isomorphic function ring (Thm 77).
- **Theorems 78–79.** For a CR-space ℜ, the maximal ideals of 𝔐, realised as closed sets in a Boolean space, form a bicompact H-space Ω. Ω is a strict H-extension of ℜ to which every bounded continuous function extends, and the extension is an analytic isomorphism of function rings.
- **Theorem 80.** For bicompact ℜ, every maximal ideal is {f : f(r) = 0} for some point r.
- **Theorem 82 (generalised Weierstrass).** For bicompact H-space ℜ, a closed subring 𝔑* containing the constants equals 𝔐 iff its functions separate ℜ as 𝔐 does. Stone presents this as generalising part (1) of the Weierstrass theorem, with |x| ≈ polynomial as the "analytical kernel" (p. 467).
- **Theorem 83.** For bicompact H-spaces, an isometry between 𝔐 and 𝔐* is equivalent to a homeomorphism, with explicit form f*(r*) = φ*(r*) f(ρ(r)) + θ*(r*) and |φ*| = 1. Stone generalises Banach's separable case and uses Mazur–Ulam.
- **Theorem 85.** Closed ideals of 𝔐 correspond one-to-one with closed sets 𝔉, as the functions vanishing on 𝔉. The quotient 𝔐/𝔑 is isomorphic to the function ring of 𝔉, and every closed ideal is the product of the maximal ideals containing it.
- **Theorem 86.** Two bicompact H-spaces are homeomorphic iff their function rings are analytically isomorphic. One is a continuous image of another iff its ring embeds as an analytical subring.
- **Theorem 87.** Tychonoff's cube [0,1]^A is universal for bicompact H-spaces of character ≤ c (stated without proof).
- **Theorem 88.** Every continuous map from ℜ to a CR-space 𝔗 extends from Ω to any bicompact H-extension of 𝔗. In particular, every bicompact H-extension of ℜ is a continuous image of Ω. This is the universal property now attached to the Stone–Čech compactification.
- **Theorems 90–93.** A CR-space of infinite character c has a bicompact extension of the same character (Thm 90). A space is CR iff it has a Boolean map extendable to a continuous covering family (Thms 91–93).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The prime-ideal space of a Boolean ring, topologised by the 𝔈(a), is a totally disconnected, locally bicompact H-space whose compact open sets are exactly the 𝔈(a); it is bicompact iff the ring has a unit | strong | Theorem 1, proof pp. 379–380 (compactness via R Thm 17) |
| C2 | Every totally disconnected, locally bicompact H-space is the prime-ideal space of the ring of its compact open sets | strong | Theorem 2, proof pp. 380–381 via R Thm 69 |
| C3 | Isomorphism ↔ homeomorphism; automorphisms ↔ homeomorphisms; ideals ↔ open sets; quotients ↔ closed subsets; unit ↔ bicompactness | strong | Theorem 4, assembled from R and Thms 1–2 (pp. 383–384) |
| C4 | Subrings (containing the unit) ↔ totally disconnected continuous images | strong | Theorem 7, pp. 385–386 |
| C5 | {0,1}^c is the universal Boolean space and its ring the free Boolean ring; for c = ℵ₀ it is the Cantor set | strong | Theorems 9–13, proofs pp. 388–394 |
| C6 | "The algebraic theory of Boolean rings (with unit) is mathematically equivalent to the topological theory of T₀-spaces" | moderate | Theorem 27 is a summary of Thms 23 and 26 (pp. 406–407). "Equivalent" here means every T₀-space is represented by a family of closed sets (ideals); it is not an equivalence of categories |
| C7 | Among H-spaces, the bicompact ones are exactly the continuous images of bicompact Boolean spaces | moderate | Theorem 72, given "without further formal discussion" as a rearrangement of Thm 71's proof (p. 452) |
| C8 | Every CR-space ℜ has a bicompact H-extension Ω to which all bounded continuous functions extend, and every bicompact extension of ℜ is a continuous image of Ω | strong | Theorems 78–79 and 88, pp. 461–477 |
| C9 | A closed subalgebra of C(ℜ) containing constants that separates points as 𝔐 does is all of 𝔐 (ℜ compact Hausdorff) | strong | Theorem 82, proof pp. 467–468 |
| C10 | Isometric function rings of compact Hausdorff spaces imply homeomorphic spaces | strong | Theorem 83, proof pp. 469–472, using Mazur–Ulam from Banach's book |
| C11 | The Boolean-space theorems and the function-ring theorems "have the same, essentially algebraic, origin" | weak | a surmise from the parallel between Thms 85–87 and Thms 4, 7, 9, 10 (p. 476); Stone says finding the origin would need "an abstract characterization of function-rings" |
| C12 | The free-ring / power-set duality is "a special instance" of the duality between discrete abelian groups and subgroups of toroidal groups | weak | assertion with a citation to Alexander–Zippin, not pursued (p. 393) |

## Method

The method is algebraic topology in the literal sense: every topological question is translated into one about ideals in a Boolean ring, and the translation is justified by R's representation theorems. The key devices are:

1. The prime-ideal space with basis 𝔈(a) (Chapter I).
2. Families of closed sets in a bicompact Boolean space, topologised by the "contained in an open set" relation (Thm 14). These represent arbitrary spaces, as "maps".
3. The *basic ring* of a space: a Boolean ring of subsets, containing the space, whose interiors form a basis. The *complete basic ring* is generated by the open sets together with the nowhere-dense sets (Thm 24, Def. 10).
4. The ring of bounded continuous functions and its maximal ideals (Chapter III).

Proofs are written out except where noted: Theorem 3 is also given an indirect proof, Theorem 12's characterisation of free rings is informal, and Theorems 33, 56, 57, 72 and 87 are stated without full proof.

## Concepts

- **Boolean space** — a totally disconnected, locally bicompact H-space (Def. 1), with "totally disconnected" in the strong clopen-partition sense (p. 378). The representative of a ring A is any space homeomorphic to its prime-ideal space 𝔈(A) (Def. 2).
- **𝔈(a), 𝔈(𝔞)** — the prime ideals not containing the element a, respectively not dividing the ideal 𝔞 (R Chapter IV). They are the compact open and the open sets of the space.
- **map m(ℜ, 𝔖, 𝔛)** — a representation of the points of ℜ by the members of a family 𝔛 of closed subsets of 𝔖, with the topology of Thm 14 (Def. 7). A *Boolean map* has 𝔖 a bicompact Boolean space.
- **basic ring, algebraic map** — defined in Defs. 10–11 via Thm 26.
- **X-set** — a nonempty closed set every open neighbourhood of which contains a member of 𝔛 (Def. 12). X-sets are the raw material for extensions.
- **strict / immediate / T₁- / H-extension; absolutely closed** — Defs. 13–17.
- **SR-space** — a space whose regular open sets form a basis (Def. 19). The notion is introduced here.
- **function ring, analytical subring, analytical isomorphism** — the bounded continuous real functions with the sup norm (Thm 75); a closed subring containing the constants; a ring isomorphism preserving |f| and ‖f‖ (Def. 22).
- **divisorless ideal** — a maximal ideal.

## Connections

The paper is the sequel promised in [LIT-353](../literature.d/LIT-353.md) (Stone 1936, cited here as "R"). The representation there, of a Boolean ring by the sets 𝔈(a) of prime ideals, is here given its topology, and R Theorems 1, 17, 36–38, 49, 67–69 are used throughout.

For the "duality tripod" of the map's §2 item 2:

- **Pontryagin.** Stone himself points at Pontryagin duality. His only use of "duality" (pp. 392–393) calls the free-ring/power-set relation a special case of the discrete abelian group / toroidal subgroup duality, citing Alexander and Zippin. That duality's compact–discrete form is [LIT-333](../literature.d/LIT-333.md) (Pontryagin 1934).
- **Gelfand.** Theorems 80, 85 and 86 (points = maximal ideals of C(X); closed ideals = closed sets; X determined by C(X) as a normed, lattice-ordered ring) anticipate the commutative case of Gelfand–Naimark, [LIT-313](../literature.d/LIT-313.md) (1943). The correspondence is only for real bounded functions and relative to a given space; there is no abstract characterisation of which rings are function rings, and Stone names that as the missing step (p. 476).

Chapter II's use of families of closed sets to represent arbitrary T₀-spaces, and its finite case (Thm 59: finite T₀-spaces are posets and embed in abstract simplices), are topological, not logical. They do not connect to the presheaf-over-contexts reading of Kochen–Specker in [LIT-325](../literature.d/LIT-325.md).

Among this batch, Stanley's arrangement notes (2006/2007) supply the region/intersection-poset side that this paper lacks. Nothing in Stone mentions hyperplanes.

## Bearing on the record

- **Map row 8 ("Stone duality").** This is the citation the map needs, not [LIT-353](../literature.d/LIT-353.md). Specifically, cite Theorems 1, 2 and 4 (and 7 for morphisms). [LIT-353](../literature.d/LIT-353.md) should stay cited only for the representation theorem itself. [NOTE-272](NOTE-272.md)'s recommendation is confirmed by the text.
- **"Ultrafilters ↔ topes".** Stone 1937 supplies no support. Its points are prime ideals, it never mentions ultrafilters, and it has no geometry of hyperplanes. The only finite-case content is that a finite Boolean ring's space is discrete (p. 380). [NOTE-272](NOTE-272.md)'s point stands that the identification is the owner's and needs its own argument: the atoms of a half-space-generated Boolean algebra are all faces, not only the full-dimensional regions. The tope side has to come from arrangement or oriented-matroid sources. Of those, [LIT-332](../literature.d/LIT-332.md) is unreachable, and Stanley (this batch) is read.
- **The "tripod" (§2 item 2).** The paper gives the map a primary-source hook for its "one duality" framing. Stone's own surmise (p. 476) is that the Boolean-space and function-ring theorems "have the same, essentially algebraic, origin". His aside (p. 393) links Boolean duality to the group-character duality. Both are surmises in the text, so they can be cited as Stone's intuition, not as a result.
- **Machine-learning practice.** Nothing here carries an instruction for ML practice. No anthology entry exists or is warranted.

## Limitations

- The headline "mathematical equivalence" is not stated as a correspondence of morphisms in one theorem. It is assembled from the object-level Theorem 4 and the subring/image and ideal/quotient statements (Thms 4(3)–(4), 7). A reader wanting "Hom(A, B) ≅ C(𝔈(B), 𝔈(A))" must put it together.
- Theorem 27's "equivalence" of Boolean rings with T₀-spaces is weaker than its wording. It says every T₀-space is represented by a family of closed sets in some Boolean space, which is a representation, not an equivalence.
- Several results are given without proof or with proof "left to the reader" (Thms 12's characterisation of free rings, 33, 56–57, 72, 75, 87).
- Chapter III's function ring is the ring of *bounded real* functions. Nothing complex, no involution and no abstract normed-ring axioms appear.
- The OCR layer garbles Stone's Fraktur notation. Theorem statements were checked against the page structure, but formula details in some proofs (e.g. Thms 29, 36, 83) were followed from the prose, not the symbols.

## Open questions

- Stone's own open question (p. 476): an abstract characterisation of function rings, which would reveal the common algebraic origin. That became the commutative Gelfand–Naimark theorem ([LIT-313](../literature.d/LIT-313.md)), which the record already holds.
- Whether an SR-space all of whose subspaces are SR must be regular, and what restrictions on SR-spaces imply regularity (p. 453, left open).
- For the map: whether "concepts are ultrafilters" is meant for the Boolean algebra generated by an arrangement's half-spaces (whose atoms are all faces) or for the arrangement's regions alone (topes). Stone supplies nothing on either side, so the owner must state which, and prove the identification from arrangement theory.

## Corrections to the seeded skim

- none (there was no seed or dossier)
- The batch brief's title, volume and year are confirmed. Crossref gives Trans. AMS 41:375–481, DOI 10.1090/S0002-9947-1937-1501905-7. The running heads carry "[May", which dates the issue. The paper was received on 1 June 1936 and presented in part on 25 February 1933 and 5 September 1936.
- The paper confirms what [LIT-353](../literature.d/LIT-353.md)'s reading ([NOTE-272](NOTE-272.md)) said it would contain: the topology on prime ideals, deferred there to "another paper", is done here. Stone cites the 1936 paper as "R" throughout, and Chapter I is built on R Theorems 67–69.
- "Duality" is not Stone's word for this correspondence. He calls it a mathematical equivalence (Thms 4 and 27). He uses "duality" once, for a different relation: between the free Boolean ring with unit on c generators and the ring of all subsets of a c-set. He calls this "a special instance" of the duality "between discrete abelian groups and the subgroups of toroidal groups" (pp. 392–393, citing Alexander and Zippin 1935). Nothing is stated in the language of categories. The correspondence of morphisms is split across Theorem 4(3)–(4) (ideals and homomorphic images) and Theorem 7 (subrings and continuous images). No single theorem states that ring homomorphisms correspond contravariantly to continuous maps.
- The duality is broader than the usual textbook statement. Stone treats Boolean rings without a unit, which correspond to *locally* bicompact spaces. Rings with a unit (Boolean algebras) are the special case of bicompact spaces (Thm 1, Thm 4(5)). He also proves that every non-bicompact Boolean space is a one-point-deleted bicompact one (Thm 8).
- "Ultrafilters ↔ topes" (map row 8 and §2 item 2): the word "ultrafilter" does not occur, and nor does "filter". The points are prime ideals, as in [LIT-353](../literature.d/LIT-353.md). Nothing in the paper concerns hyperplanes, arrangements, regions or sign vectors. The only finite statement is that a Boolean ring with 2^m elements has a space of m isolated points (p. 380). So the paper supplies the "points = prime ideals, topologised" half of the owner's analogy and nothing on the tope half.
- "Totally-disconnected" is defined in a footnote on p. 378. It means that any two distinct points are separated by a partition of the space into two disjoint closed sets, which is stronger than the modern "totally disconnected". The observation that the two notions agree for compact Hausdorff spaces is mine, not the paper's.
