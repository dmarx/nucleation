---
status: Read
paper: LIT-tmpiz975
title: 'The Cohomology of Non-Locality and Contextuality'
version: 1
history:
- version: 1
  date: '2026-09-27'
  note: >-
    Read in full (The full text of arXiv 1111.3620 v2, from the arXiv PDF,
    14 pp. The arXiv abstract page lists two versions, v1 (15 Nov 2011, 27
    KB) and v2 (2 Oct 2012, 30 KB, comment "In Proceedings QPL 2011,
    arXiv:1210.0298"). The v2 PDF carries the EPTCS 95 header, so v2 is the
    published text. I read the abstract, §§1–8 (every example: Hardy, PR
    box, GHZ, the triangle, the 18-vector Kochen–Specker configuration, the
    Kochen–Specker class with Propositions 6.1–6.2, and Peres–Mermin), the
    acknowledgements and all 16 references. Nothing was skipped. `pdftotext`
    was not available in this session, so I extracted the text with PyMuPDF.
    The tables and the linear systems came through legibly. I also
    downloaded v1 and compared the two extracted texts word by word; the
    differences are listed under corrections. I then re-ran every example's
    computation myself, as exact linear algebra over ℤ and over ℤ/2 (results
    under Key results).). The first NOTE on this paper, which was seeded
    from its abstract alone.
date: '2026-09-27'
summary: >-
  For an empirical model e on a measurement cover 𝒰, a section s in the
  support of context C₁ gets a class γ(s) ∈ Ȟ¹(𝒰, F_{C̄₁}), relative Čech
  cohomology of the presheaf F = F_ℤ S_e of formal ℤ-linear combinations
  of support sections. γ(s) = 0 iff s belongs to a compatible family of
  such ℤ-combinations (Prop 4.2), so a non-vanishing γ(s) is a sufficient
  but not necessary witness of contextuality (Prop 4.3). γ is non-zero for
  every section of the PR box, GHZ, the triangle, the 18-vector
  Kochen–Specker set and the Peres–Mermin square, but it vanishes on the
  Hardy model and on one strongly contextual Kochen–Specker cover (§8).
---

<!-- inactive-ok-file: LIT-276 — Rejected: the Ghose paper whose garbled version of this construction this reading adjudicates; the directive lapses when its status changes -->

# NOTE-tmppkatn: The Cohomology of Non-Locality and Contextuality

## Contribution

Abramsky & Brandenburger ([LIT-016](../literature.d/LIT-016.md)) showed that contextuality is the absence of a global section of a presheaf over a measurement cover, and promised "powerful sheaf-theoretic methods". This paper supplies the first such method. It attaches to each section s in a model's support a Čech cohomology class γ(s), whose non-vanishing proves that s cannot be extended to a compatible family of support sections. It works this out on six scenarios and shows that the class is non-zero for every section in the PR box, GHZ, the triangle, the 18-vector Kochen–Specker set and the Peres–Mermin square, i.e. that cohomology certifies their strong contextuality. It also shows exactly where the witness fails: γ vanishes for the non-extendable section of the Hardy model, and for some sections of one strongly contextual Kochen–Specker model. It proves a general link to the parity (GCD) condition for connected Kochen–Specker models (Prop 6.2).

## Key insight

Replace "a family of *sections*" by "a family of *formal ℤ-linear combinations* of sections". Then compatibility is a system of linear equations, and the question "does s extend?" becomes the question whether a Čech 1-cocycle is a coboundary. That question has an answer in a cohomology group, and the answer is computable by linear algebra (over ℤ, or over ℤ/2 as a quick sufficient test).

The price is that the relaxation is too generous. Negative coefficients let formal combinations agree on overlaps where no actual section does. The Hardy family r₂ = s₆ + s₇ − s₈ is one such case (§5). So γ(s) = 0 is weaker than extendability, and the witness can only certify, never refute, contextuality.

The class has to be *relative* to the context of the section. The paper builds the cochain c from s and from sections sᵢ that agree with s on C₁ ∩ Cᵢ, so δ⁰c vanishes on C₁. It then classes δ⁰c in Ȟ¹ of the kernel presheaf F_{C̄₁}, where c itself is not a cochain. In the absolute group Ȟ¹(𝒰, F) the same δ⁰c would be a coboundary, and its class would be zero.

## Assumptions

- **The scenario (§2).**
  - *The measurement space.* X is a finite discrete space of measurement labels.
  - *The cover.* 𝒰 = {C₁, …, Cₙ} is a cover with ⋃𝒰 = X. Its members are the maximal sets of jointly performable measurements.
  - *Outcomes.* O is a finite set of outcomes.
  - *The event sheaf.* ℰ(U) = O^U, with restriction as function restriction.
- **The empirical model (§2, from [LIT-016](../literature.d/LIT-016.md)).** e = {e_C}_{C∈𝒰} is a compatible family of probability distributions e_C on ℰ(C). Compatibility is no-signalling. This is essential: Prop 4.1's lifts sᵢ exist only because of it.
- **The support presheaf.** S_e(U) = {s ∈ ℰ(U) : s ∈ supp(e_U)}, where e_U = e_C|_U for any C ⊇ U. It is well defined because of compatibility. Only the support is used: the construction is possibilistic throughout.
- **Extendability notions (§2).**
  - *Possibilistically extendable.* Every s ∈ S_e(C) belongs to a compatible family {sᵢ ∈ S_e(Cᵢ)}ᵢ₌₁ⁿ.
  - *Strongly contextual.* No s belongs to such a family.
  - *What is taken from [LIT-016](../literature.d/LIT-016.md).* The paper takes from [LIT-016](../literature.d/LIT-016.md) the fact that local or non-contextual implies possibilistically extendable. Later literature calls possibilistic non-extendability "logical contextuality"; this paper does not use that name.
- **The coefficient functor (§4).** For a commutative ring R, F_R(X) is the set of finitely supported functions X → R, i.e. the free R-module on X, with F_R f pushing coefficients forward along f.
  - *The paper takes R = ℤ.* So **F := F_ℤ S_e**, and F(U) is the free abelian group on the support sections over U.
  - *ℤ/2 is only a computational shortcut.* It is used in the GHZ, Kochen–Specker and Peres–Mermin examples: unsolvability mod 2 implies unsolvability over ℤ, via ℤ → ℤ/2ℤ. The paper remarks that this also shows γ ≠ 0 with ℤ/2 coefficients.
  - *Distributions are not the coefficients.* The presheaf is *not* built on ℰ, and not on the distribution presheaf D_R ℰ of [LIT-016](../literature.d/LIT-016.md).
- **Čech cohomology (§3).**
  - *The nerve.* A q-simplex of N(𝒰) is an ordered list (U₀, …, U_q) of cover members with non-empty intersection. Pairs of contexts with empty overlap impose no condition.
  - *Cochains and coboundary.* Cᵠ(𝒰, F) = ∏_σ F(|σ|), and (δ^q ω)(σ) = Σ_j (−1)^j ρ ω(∂_j σ) over the faces of the (q+1)-simplex σ. The paper writes both the face range ("0 ≤ j ≤ q") and the sum's upper limit as q. A (q+1)-simplex has q+2 faces, so both should read q+1. I checked this against the rendered PDF: it is the paper's typo, not an extraction artefact. The worked Prop 3.2 case (q = 0, two faces) is computed correctly.
  - *Groups.* Ȟ^q = Z^q / B^q. Since B⁰ = 0, Ȟ⁰ ≅ Z⁰.
- **The relative presheaf (§3).**
  - *Restriction to U.* For an open U, F|_U(V) := F(U ∩ V), and p: F → F|_U restricts to U ∩ V.
  - *The kernel.* F_{Ū}(V) := ker(p_V), giving the exact sequence 0 → F_{Ū} → F → F|_U of presheaves. This is left exact only; p need not be surjective.
  - *Relative cohomology.* "The relative cohomology of F with respect to U is defined to be the cohomology of the presheaf F_{Ū}" (p. 4).

## Key results

- **Prop 3.1.** δ^{q+1} ∘ δ^q = 0. This is stated, with no proof given.
- **Prop 3.2.** Compatible families {rᵢ ∈ F(Uᵢ)} correspond bijectively to Ȟ⁰(𝒰, F). The proof uses (δ⁰c)(Cᵢ, Cⱼ) = rᵢ|Cᵢ∩Cⱼ − rⱼ|Cᵢ∩Cⱼ.
- **Prop 3.3.** Ȟ⁰(𝒰, F_{Ūᵢ}) corresponds to the compatible families with rᵢ = 0.
- **The construction (§4, p. 5).**
  - *The lifts.* Fix s = s₁ ∈ S_e(C₁). By no-signalling there are sᵢ ∈ S_e(Cᵢ) with s₁|C₁∩Cᵢ = sᵢ|C₁∩Cᵢ for i = 2, …, n.
  - *The cochain.* Let c := (s₁, …, sₙ) ∈ C⁰(𝒰, F) and z := δ⁰(c), with z_{i,j} = sᵢ|Cᵢⱼ − sⱼ|Cᵢⱼ.
  - *Prop 4.1.* z vanishes on restriction to C₁, so z ∈ C¹(𝒰, F_{C̄₁}), and it is a cocycle there because δ¹ on the relative complex is the restriction of δ¹.
  - ***Definition.* γ(s₁) := [z] ∈ Ȟ¹(𝒰, F_{C̄₁}).**
  - *Why it need not vanish.* "Although z = δ⁰(c), it is not necessarily a coboundary in C¹(𝒰, F_{C̄₁}), since c is not a cochain in C⁰(𝒰, F_{C̄₁})" (p. 5): p_{Cᵢ}(sᵢ) = sᵢ|C₁∩Cᵢ ≠ 0.
  - *Well-definedness.* Independence of the choice of lifts sᵢ is not stated. It follows in one line: two choices differ by a cochain in C⁰(𝒰, F_{C̄₁}), whose coboundary is a relative coboundary.
  - *The Remark (p. 5).* "There is a more conceptual way of defining this obstruction, using the connecting homomorphism from the long exact sequence of cohomology; see [5]" (Ghrist & Hiraoka, a network-coding preprint). The concrete definition is chosen as "easier to grasp" and "convenient for computation". The connecting-homomorphism form is not written out.
- **Prop 4.2 (the criterion).** γ(s₁) = 0 **iff** there is a family {rᵢ ∈ F(Cᵢ)} with r₁ = s₁ and rᵢ|Cᵢ∩Cⱼ = rⱼ|Cᵢ∩Cⱼ for all i, j.
  - *Meaning.* s₁ belongs to a compatible family of ℤ-linear combinations of *support* sections. It does not have to belong to a compatible family of sections, and so need not extend to a global section in ℰ(X).
  - *Proof.* Complete. c′ = c − r is a relative 0-cochain with δ⁰c′ = z, and conversely.
- **Prop 4.3 (the contextuality consequence).**
  - *Extendable models.* If e is possibilistically extendable, then γ(s) = 0 for every s in the support.
  - *Models that are not strongly contextual.* Then γ(s) = 0 for some s.
  - *What is necessary and what is sufficient.*
    - γ(s) ≠ 0 for *some* s is **sufficient** for possibilistic non-extendability, and hence ([LIT-016](../literature.d/LIT-016.md)) for contextuality or non-locality.
    - γ(s) ≠ 0 for *all* s is **sufficient** for strong contextuality.
    - Neither is necessary. A "false positive" in the paper's usage (p. 6) is a ℤ-compatible family {rᵢ} through a non-extendable s that "do[es] not determine a bona fide global section in ℰ(X)". It makes γ(s) = 0 although s does not extend. (The paper's "false positive" is thus a false negative of the witness.)
- **Examples (§§5–7), with my re-computation.** For each model I built the full system of Prop 4.2, over all pairs of overlapping contexts, and solved it exactly over ℤ (a lattice-membership test) and over ℤ/2.
  - *Hardy (§5).* The support has zeros at (a,b′)(0,0), (a′,b)(0,0) and (a′,b′)(1,1). s₁ = (a,b ↦ 0,0) is the non-extendable section.
    - *The paper's family.* The paper exhibits r₁ = s₁, r₂ = s₆ + s₇ − s₈, r₃ = s₁₁, r₄ = s₁₅, and so γ(s₁) = 0. It displays two of the four overlap checks. I checked all four; they hold.
    - *My finding: cohomology detects nothing in Hardy.* In the paper's table, 12 of the 13 support sections are extendable. γ = 0 for all 13, over ℤ and over ℤ/2. So with these coefficients cohomology detects no contextuality in the Hardy model at all.
  - *PR box (§5).* The equations force all coefficients equal, so fixing s's coefficient to 1 and its row-mate to 0 gives 1 = 0. γ(s) ≠ 0 for all 8 sections: strong contextuality is witnessed. I confirmed this.
  - *GHZ (§5).* This is "the relevant part", the four contexts ABC, AB′C′, A′BC′ and A′B′C, with 16 unknowns and 12 equations.
    - *The paper's check.* "All cases … machine-checked in mod 2 arithmetic". γ ≠ 0 for every section, so the strong contextuality of GHZ is witnessed.
    - *My check.* Confirmed over ℤ and ℤ/2 for all 16 sections.
  - *Kochen–Specker-type models (§6).* The outcomes are 0 and 1. The support is S_e(C) = {s_{C,m} : m ∈ C}, "exactly one 1" per context.
    - *The triangle {A,B},{B,C},{A,C}.* The equations force all coefficients equal, so γ ≠ 0 for every section. It is not quantum-realisable (p. 8). I confirmed it.
    - *The 18-vector set in ℝ⁴ (Cabello, Estebaranz & García-Alcaine).* It has 9 contexts of 4. Simple equations reduce 36 unknowns to 18, and 18 equations remain. Mod-2 "machine-checked". I confirmed γ ≠ 0 for all 36 sections, over ℤ and ℤ/2.
  - *Prop 6.1, cited from [LIT-016](../literature.d/LIT-016.md) (it is [LIT-016](../literature.d/LIT-016.md)'s Prop 7.1).* A global section implies gcd{d_m : m ∈ X} divides |𝒰|, where d_m is the number of contexts containing m.
  - ***Prop 6.2.*** For a *connected* Kochen–Specker-type model (the nerve's 1-skeleton connected), if γ(s) = 0 for some s then the GCD condition holds.
    - *Proof.* Complete. The equations identify c_{C,m} across contexts. The coefficient sum is preserved under restriction, so by connectedness every rᶜ has coefficient sum 1. Then |𝒰| = Σ_m d_m c_m.
    - *Consequence.* A connected model failing the GCD condition has γ ≠ 0 for every section, so cohomology witnesses its strong contextuality.
    - *An unsupported claim.* The paper says cohomology also "witnesses strong contextuality of some connected models outside of this class". No such example is given, since none of the §6 examples satisfies the GCD condition.
  - *Peres–Mermin (§7).* Rows have odd parity and columns even. There are 24 unknowns and 18 equations. Mod-2 machine-checked: no solution for any starting section. I confirmed γ ≠ 0 for all 24 sections, over ℤ and ℤ/2.
- **§8, the strongly contextual false positive.**
  - *The model.* The Kochen–Specker model on {A,B,C},{B,D,E},{C,D,E},{A,D,F},{A,E,G}. F and G each lie in a single context. The paper blames that: their coefficients can always be chosen to make those contexts' sums equal 1.
  - *My check.* It is strongly contextual (no exactly-one-1 global assignment). γ = 0 for 9 of its 15 sections: every section with A ↦ 1, and every section of {B,D,E} and {C,D,E}. γ ≠ 0 for the 6 sections with A ↦ 0 in {A,B,C}, {A,D,F} and {A,E,G}.
  - *What that means.* Here cohomology still certifies possibilistic contextuality, but not strong contextuality. The paper does not give these counts.
  - *Why the GCD test says nothing here.* The GCD condition holds for this cover: the d_m are 3, 2, 2, 3, 3, 1, 1 and |𝒰| = 5. That is consistent with Prop 6.2.
- **Conjecture 8.1.** "Under suitable assumptions of symmetry and connectedness, the cohomology obstruction is a complete invariant for strong contextuality." It is stated, with no proof.
- **Vorob'ev (§8).** Vorob'ev (1962) characterised the covers on which every model is extendable (they reduce to the empty complex by removing extremal contexts), so one may restrict attention to irreducible covers. The §8 cover is irreducible but has contexts with private measurements.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Compatible families of a presheaf of abelian groups on a cover are exactly Ȟ⁰; those vanishing on Uᵢ are exactly relative Ȟ⁰ | strong (proof) | Props 3.2, 3.3; standard |
| C2 | For s₁ ∈ S_e(C₁), z = δ⁰(s₁, …, sₙ) (lifts chosen by no-signalling) is a relative 1-cocycle, and γ(s₁) = [z] ∈ Ȟ¹(𝒰, F_ℤ S_e relative to C₁) is well defined | strong (proof; independence of the lifts unstated but immediate) | Prop 4.1 and the definition, p. 5 |
| C3 | γ(s₁) = 0 iff s₁ lies in a compatible family of ℤ-linear combinations of support sections | strong (proof) | Prop 4.2 |
| C4 | Possibilistic extendability ⇒ γ ≡ 0; not strongly contextual ⇒ γ(s) = 0 for some s. So γ(s) ≠ 0 witnesses contextuality, and γ ≠ 0 everywhere witnesses strong contextuality | strong (proof) | Prop 4.3, with [LIT-016](../literature.d/LIT-016.md) for "non-contextual ⇒ extendable" |
| C5 | The witness is not necessary: in the Hardy model γ(s₁) = 0 although s₁ is non-extendable | strong (explicit family) | §5, family r₁…r₄. Re-checked; in fact γ = 0 on all 13 support sections |
| C6 | γ ≠ 0 for every section of the PR box, GHZ (the four-context part), the triangle, the 18-vector Kochen–Specker set and Peres–Mermin | strong (proof by hand for PR and the triangle; exhaustive machine check mod 2 for the others) | §§5–7. Independently re-computed over ℤ and ℤ/2 |
| C7 | For connected Kochen–Specker-type models, failure of the GCD condition implies γ ≠ 0 everywhere | strong (proof) | Prop 6.2 |
| C8 | Cohomology captures strong contextuality "more finely than the GCD condition" | weak (assertion) | §6, no example given |
| C9 | A strongly contextual model can have γ(s) = 0 for some s | strong (example; corrected in v2) | §8 cover. The v1 cover was not strongly contextual. The v2 cover is, and has 9 of 15 sections with γ = 0 (my count) |
| C10 | Under symmetry and connectedness, γ is a complete invariant for strong contextuality | conjecture | Conjecture 8.1, unproved and with the assumptions unspecified |
| C11 | γ can be defined via the connecting homomorphism of the long exact cohomology sequence | assertion by citation | Remark p. 5, citing Ghrist & Hiraoka [5]; not constructed |

## Method

- **Encode the model's possibilities.** Take the support presheaf S_e and free it over ℤ.
- **Build the cochain.** Pick a section s₁ and no-signalling lifts sᵢ. Take z = δ⁰(sᵢ), and class it in the cohomology of the kernel presheaf relative to C₁.
- **Compute.** By Prop 4.2, deciding γ(s) = 0 is solving a linear system: one unknown per (context, support section), one equation per overlap and per outcome of the overlap, with s's row fixed to the unit vector. The paper solves it by hand (PR box, triangle) or by exhaustive mod-2 machine check (GHZ, 18-vector, Peres–Mermin). ℤ/2 unsolvability implies ℤ unsolvability.
- **Generalise one class.** Prop 6.2 generalises the Kochen–Specker computations by a coefficient-sum (augmentation) argument.

## Concepts

- **Empirical model, support S_e** — as in [LIT-016](../literature.d/LIT-016.md). S_e is the sub-presheaf of ℰ of sections with non-zero probability.
- **F_R** — the free R-module functor, with finitely supported functions X → R. The paper's coefficient presheaf is F = F_ℤ S_e: formal ℤ-combinations of support sections.
- **Nerve N(𝒰)** — ordered lists of cover members with non-empty common intersection.
- **F|_U, F_{Ū}** — the restriction presheaf F|_U(V) = F(U ∩ V), and the kernel of F → F|_U. "Relative cohomology with respect to U" is the cohomology of F_{Ū}.
- **Cohomological obstruction γ(s)** — [δ⁰(s, s₂, …, sₙ)] ∈ Ȟ¹(𝒰, F_{C̄}) for s ∈ S_e(C).
- **Possibilistically (non-)extendable; strongly contextual** — every / some / no support section extends to a compatible family of support sections, in the per-section form given in §2.
- **False positive** — the paper's term for a compatible ℤ-family through a non-extendable section. It is a false *negative* of the contextuality witness.
- **Kochen–Specker-type model** — outcomes {0,1}, with support "exactly one 1 per context".
- **GCD condition** — gcd{d_m} divides |𝒰|.
- **Connected** — any two contexts are joined by a chain of pairwise-overlapping contexts.

## Connections

- **Abramsky & Brandenburger ([LIT-016](../literature.d/LIT-016.md), read in [NOTE-016](NOTE-016.md)).** This paper is its announced sequel: [NOTE-016](NOTE-016.md) records [LIT-016](../literature.d/LIT-016.md)'s pointer to "preliminary cohomology work [53]", and this is that work.
  - *What it takes.* The whole scenario apparatus (ℰ, empirical models, no-signalling as compatibility), the definitions of possibilistic extendability and strong contextuality, and the GCD condition. AMB's Prop 6.1 is [LIT-016](../literature.d/LIT-016.md)'s Prop 7.1, the generalised parity proof.
  - *What it adds.* A cohomological sufficient test, and Prop 6.2, which shows that it subsumes the GCD test on connected Kochen–Specker covers.
  - *One gap it fills.* [NOTE-016](NOTE-016.md) recorded that [LIT-016](../literature.d/LIT-016.md)'s GHZ strong-contextuality proof is complete only for n = 4k, with n = 3 sketched via Mermin. Here γ ≠ 0 on every section of the four-context GHZ(3) sub-scenario is machine-checked (and re-checked by me). That is a computer proof of strong contextuality for GHZ(3), because a global section of the full model would restrict to one on the sub-scenario.
- **Ghrist & Hiraoka ([5], network coding).** Cited only for the connecting-homomorphism formulation. This is the same applied-sheaf lineage that [LIT-016](../literature.d/LIT-016.md)'s reading found in the ML sheaf papers. There is no ML connection here.
- **Vorob'ev 1962 ([16]).** Cited for the classification of covers on which every model extends.
- **Later work (existence verified from arXiv abstract pages; content unverified, not read).**
  - Abramsky, Barbosa, Kishida, Lal & Mansfield, "Contextuality, Cohomology and Paradox", arXiv 1502.03097 (v1 10 Feb 2015), CSL 2015, LIPIcs, DOI 10.4230/LIPIcs.CSL.2015.211. The DOI resolves at doi.org to Dagstuhl DROPS; it is not in Crossref.
  - Carù, "On the Cohomology of Contextuality", arXiv 1701.00656, QPL 2016, EPTCS 236, 2017, pp. 21–39, DOI 10.4204/EPTCS.236.2 (from the arXiv page).
  - Carù, "Towards a complete cohomology invariant for non-locality and contextuality", arXiv 1807.04203 (2018).
  - Okay, Roberts, Bartlett & Raussendorf, "Topological proofs of contextuality in quantum mechanics", arXiv 1701.01888 (2017).
  - The titles of the Carù papers suggest they pursue this paper's Conjecture 8.1 and §8 refinement of F; that is unverified.
- **Anthology.** Nothing in the Anthology of the SOTA's record mentions contextuality or cohomology (text search). No ANTH- citation is warranted.

## Bearing on the record

- **On the Ghose reading's description of this paper.** The gh1 reading ([NOTE-249](NOTE-249.md), of [LIT-276](../literature.d/LIT-276.md)) described AMB "from general knowledge" as follows: "the image of a local section under the connecting homomorphism of a relative-cohomology sequence, not the class of a 0-coboundary". Against the text:
  - *"Relative cohomology": right.* γ(s₁) lives in Ȟ¹(𝒰, F_{C̄₁}), the cohomology of the kernel of F → F|_{C₁}, which the paper calls the relative cohomology with respect to C₁ (pp. 4–5).
  - *"Connecting homomorphism": right as AMB's own conceptual gloss, not as their definition.* The definition is concrete, and the connecting-homomorphism form appears only in a one-sentence Remark citing Ghrist & Hiraoka, not written out. The underlying sequence 0 → F_{C̄₁} → F → F|_{C₁} is only left exact as presheaves, and the paper does not address this. Whether the CSL 2015 sequel develops the connecting-map form is not verified here.
  - *"Not the class of a 0-coboundary": wrong as worded.* AMB's γ(s₁) is literally [δ⁰c], the class of the coboundary of the 0-cochain c = (s₁, …, sₙ). The paper says so ("although z = δ⁰(c) …"). What makes it non-trivial is that the class is taken in the relative complex, where c is not a cochain because sᵢ|C₁∩Cᵢ ≠ 0. The accurate phrase is: *the relative class of an absolute coboundary*.
  - *[NOTE-249](NOTE-249.md)'s conclusions stand.* Ghose's displayed construction is trivial, and it is not AMB's.
  - *Ghose's [δs] is a garbled γ(s).* It keeps AMB's coefficient choice (the free abelian presheaf ℤ[F], "used explicitly in cohomological contextuality [34]"), keeps the formula δ⁰s up to a sign convention (sⱼ − sᵢ against AMB's sᵢ − sⱼ), and drops the three things that make AMB's class non-trivial:
    - (i) *The relativisation.* Ghose classes δs in the absolute Ȟ¹({Cᵢ}, ℤ[F]), where every δ⁰s is a coboundary and [δs] = 0. AMB class it in Ȟ¹(𝒰, F_{C̄₁}).
    - (ii) *The anchoring.* AMB fix one section s₁ and choose the other sᵢ to agree with it on C₁ ∩ Cᵢ, using no-signalling (Prop 4.1), so that δ⁰c lands in the relative subpresheaf at all. Ghose's s = (sᵢ) is arbitrary local data.
    - (iii) *The presheaf.* AMB free the *support* presheaf S_e of a given empirical model over a cover of the measurement set X. Ghose applies ℤ[·] to an unspecified presheaf F over a cover of "a given context C", which [NOTE-249](NOTE-249.md) already showed cannot exist for a contextual scenario.
  - *What Ghose's prose gets right, and what it overstates.* Ghose's following sentence ("vanishes whenever a global section exists; hence non-vanishing provides a robust sufficient witness") matches Prop 4.3 in substance. "Robust" is Ghose's word, not AMB's. AMB stress that the witness has false positives, including one for a strongly contextual model (§8), and it is per section and possibilistic.
- **[THEORY-012](../theory.d/THEORY-012.md) (Active).** This paper supports it and extends it one step. It does not contradict it.
  - *What it adds.* It gives a computable *sufficient* test for the possibilistic and strong levels of [LIT-016](../literature.d/LIT-016.md)'s hierarchy, and it inherits [THEORY-012](../theory.d/THEORY-012.md)'s no-signalling assumption, which Prop 4.1 needs.
  - *A possible addition to [THEORY-012](../theory.d/THEORY-012.md).* Its "What this does not say" could add that a cohomological witness exists but is incomplete: it fails for Hardy and for a strongly contextual cover (this paper, Prop 4.3 and §§5, 8), with completeness under symmetry and connectedness conjectured (Conjecture 8.1). That needs this paper filed as a LIT first.
- **[THEORY-014](../theory.d/THEORY-014.md) (Proposed).** There is a parallel. It is my inference; AMB never mention negative probability.
  - *The parallel.* [THEORY-014](../theory.d/THEORY-014.md)'s point is that over ℝ every no-signalling model has a signed global section ([LIT-016](../literature.d/LIT-016.md) Thm 5.9), so negativity is universal. AMB's F_ℤ S_e is also a signed relaxation. The Hardy family r₂ = s₆ + s₇ − s₈ uses a negative coefficient to glue what no nonnegative family glues.
  - *The difference.* AMB's relaxation is integral, possibilistic and confined to the support. It still leaves an obstruction in the PR box, GHZ, Kochen–Specker and Peres–Mermin cases, where the real unrestricted relaxation of Thm 5.9 always succeeds.
  - *What follows.* Which coefficient relaxations keep discriminating power is a question the two results pose together, not one either answers. It does not change [THEORY-014](../theory.d/THEORY-014.md)'s statement, which is about real, probabilistic sections.
- **[LIT-265](../literature.d/LIT-265.md) (contextual fraction; Deferred, seeded not read).** Strong contextuality is non-contextual fraction 0 ([LIT-016](../literature.d/LIT-016.md) Prop 6.3), i.e. CF = 1. So γ ≠ 0 on every section certifies CF = 1 for PR, GHZ, Kochen–Specker and Peres–Mermin. The obstruction is qualitative and cannot grade models with CF < 1. The Hardy model has CF < 1, and there γ gives nothing at all. The two tools are complementary.
- **[LIT-263](../literature.d/LIT-263.md) (Budroni et al. review; Deferred, skimmed).** The record's skim lists "logical and strong contextuality" (§IV.A.4) and the sheaf formulation among equivalent definitions. Whether the review discusses the cohomological witness is unverified. This paper's possibilistic non-extendability is what that literature calls logical contextuality.
- **[THEORY-013](../theory.d/THEORY-013.md), [THEORY-015](../theory.d/THEORY-015.md), [THEORY-016](../theory.d/THEORY-016.md).** There is no bearing, only a boundary.
  - *[THEORY-013](../theory.d/THEORY-013.md).* The construction presupposes no-signalling (consistent connectedness), so it says nothing about the context-dependent marginals Contextuality-by-Default handles.
  - *[THEORY-015](../theory.d/THEORY-015.md) and [THEORY-016](../theory.d/THEORY-016.md).* The notion is Kochen–Specker/sheaf contextuality only. Spekkens's generalized contextuality does not appear.
- **[THEORY-017](../theory.d/THEORY-017.md)'s inferences.**
  - *"Contextuality needs more than one basis."* It is consistent, though not addressed. The formalism is Hilbert-space-free. Its quantum examples (the 18 vectors in ℝ⁴ forming 9 bases; the Peres–Mermin two-qubit observables) are multi-basis, but the paper never mentions bases. Its non-quantum ones (the triangle, the PR box) need no Hilbert space at all.
  - *"Boolean structure needs a basis."* There is no bearing.
- **ML practice.** It carries nothing. This is algebraic topology applied to quantum foundations, and it does not belong in the Anthology.
- **For filing.**
  - *Tags proposed.* `contextuality` first, `quantum-foundations`, then `mathematics`. This mirrors [LIT-016](../literature.d/LIT-016.md): the object is contextuality, and the tool is Čech cohomology.
  - *Tags not proposed.* `logic`: there is no logic here; "logical contextuality" is later terminology.
  - *Lineage.* It extends [LIT-016](../literature.d/LIT-016.md). It is the paper [LIT-276](../literature.d/LIT-276.md) cites as [34] and misstates.

## Limitations

- **Sufficient, not necessary.** This is the authors' own first limitation (§8). The Hardy model is missed entirely, since γ = 0 on every section (my count; the paper shows only s₁). A strongly contextual Kochen–Specker model is only partly detected.
- **Only the support is used.** The witness is blind to probabilistic contextuality, as in the Bell/CHSH model with full support, where no possibilistic witness can exist ([LIT-016](../literature.d/LIT-016.md) Prop 4.4).
- **The computations are brute force.** The paper says the results "can only be considered a proof of concept" (§8). The GHZ, 18-vector and Peres–Mermin results rest on unpublished mod-2 machine checks; I reproduced them.
- **The conceptual definition is only pointed to.** The connecting-homomorphism definition, the long exact sequence and any structural theorem are deferred to future work. The exactness issue (p not surjective) is not discussed.
- **Well-definedness is left implicit.** Independence from the choice of lifts sᵢ is not stated (it is immediate).
- **Slips.**
  - *Section numbering.* The introduction points to "Section 7" for limitations, which v2 made §8.
  - *The coboundary sum.* The face range and the sum's upper limit are both printed as q instead of q + 1 (§3, p. 3).
  - *C8.* It is asserted without an example.
  - *The v1 false-positive cover.* It was not strongly contextual. It is corrected in v2, silently.

## Open questions

- **Conjecture 8.1.** Is γ a complete invariant for strong contextuality under symmetry and connectedness, and which assumptions? The Carù papers and the CSL 2015 sequel address this by title; that is unverified.
- **A finer invariant.** Can refining F (the paper's suggestion, §8) remove the Hardy-type false positives? Could other coefficient rings do it? Any ring receiving a map from ℤ can only make γ vanish more often, so a finer invariant needs a different presheaf, not just a different ring. That is my observation.
- **A GCD-satisfying example.** Is there a connected Kochen–Specker-type cover satisfying the GCD condition on which γ ≠ 0 everywhere? That would support C8.
- **The connecting homomorphism.** Does the connecting-homomorphism definition coincide with γ given only left exactness, and does the long exact sequence yield structural results, e.g. vanishing criteria from the topology of the nerve?

## Corrections to the seeded skim

- none (there was no seed or dossier)
- **Identification note for filing.** The journal-ref is EPTCS 95, 2012, pp. 1–14, Proceedings of the 8th International Workshop on Quantum Physics and Logic (QPL 2011), eds. Jacobs, Selinger & Spitters. I verified the DOI 10.4204/EPTCS.95.1 via Crossref (no contact address sent): title, the three authors and pp. 1–14 match, issued 2012-10-01. The arXiv category is quant-ph. The affiliation is the Department of Computer Science, University of Oxford.
- **The abstract's "This class vanishes if the family has a global section" is per section, and possibilistic.** The body's statement (Prop 4.3) is that γ(s) = 0 whenever s extends to a compatible family *within the support*. A global section of the model (a probabilistic one) implies this, by [LIT-016](../literature.d/LIT-016.md), but the obstruction never sees probabilities, only the support.
- **The abstract says "contextual"; the examples show more.** For all the listed examples γ(s) ≠ 0 for *every* section in the support. The paper says (end of the PR-box and GHZ examples) that this witnesses *strong* contextuality. The abstract's "cohomological witnesses for contextuality" undersells that. In the other direction, one γ(s) ≠ 0 only witnesses possibilistic non-extendability, and the abstract does not separate the two levels.
- **v1's strongly contextual false positive was not strongly contextual.** In v1, §7 gives the cover {A,B,C},{A,D,E},{B,D,E},{A,D,F},{A,E,G}. My check: its Kochen–Specker support has two global assignments, so it is not strongly contextual at all. v2 replaces it with {A,B,C},{B,D,E},{C,D,E},{A,D,F},{A,E,G}, which is strongly contextual (checked), and adds the explanation about F and G. The abstract of neither version mentions this example.
- **Other v1→v2 changes.** v2 adds the Peres–Mermin square to the abstract and the introduction's list; the example itself is in v1, unnumbered, inside §6. v2 makes it §7, so "Limitations" becomes §8, but the introduction still says limitations are "discussed in Section 7". v2 also adds the Vorob'ev paragraph and Conjecture 8.1's numbering (7.1 in v1), gives DOIs in the references and cites Liang, Spekkens & Wiseman for the triangle. v1 writes cover elements as C, v2 as U, in §3.
