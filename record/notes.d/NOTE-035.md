---
number: 35
status: Read
formerly:
- NOTE-tmp55ned
paper: LIT-073
title: 'Plávala, General probabilistic theories: An introduction'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (full text of arXiv:2103.07469v2 (23 Aug 2021), 76 pp. I
    read §1–9 (pp. 2–64), the acknowledgement, the reference list [1]–[149]
    (pp. 64–69) and Appendices A–C (pp. 69–76). I extracted the text with
    PyMuPDF into raw4/2103.07469.txt. The string diagrams (quantikz) came
    through as scattered wire labels. I followed each diagrammatic proof
    through its prose and its inline equivalents (e.g. Eq. 5.35
    (id⊗f_B)(x_AB), Eq. 6.43), not by redrawing it. Figures 1–4 are plots of
    state spaces and effect algebras for S2, S3, S4 and the square; I read
    them from their captions and coordinates (Eqs. 4.6–4.11, 9.2–9.4). I did
    not compare this version with the Physics Reports version (DOI
    10.1016/j.physrep.2023.09.001). The page range 1033:1–64 comes from the
    dossier and I have not verified it. Nothing was skipped.). Upgraded from
    `Skimmed` to `Read`: the claims table, assumptions and results are new,
    and the skim is corrected where the full text disagreed.
date: '2026-09-25'
summary: >-
  A self-contained textbook on finite-dimensional GPTs whose central
  results are that state spaces and effects are dual (K = {φ ∈ A(K)*+ :
  ⟨φ, 1_K⟩ = 1}, Thm 3.19) and that optimal two-state discrimination
  succeeds with probability ½(1 + ‖λx₀ − (1−λ)x₁‖) in base norm (Thm
  3.43). Every composite lies between the minimal and maximal tensor
  products (Prop. 5.6), and four statements are equivalent: id_K is
  measure-and-prepare, id_K is self-compatible, K admits a universal
  broadcasting channel, and K is a simplex (Thm 7.7); minimal = maximal
  iff one factor is a simplex is cited to [134], not proved.
---


# NOTE-035: Plávala, General probabilistic theories: An introduction

## Contribution

This is a review. It adds a single consistent path through finite-dimensional GPTs, built from the state space outward. Two choices distinguish it:
- **Channels first.** Measurements are channels K → S_n (Def. 6.11), instruments are channels K → S_n ⊗̃ K (Def. 6.15), and preparations are channels S₁ → K (§6.4). One compatibility notion therefore covers measurements and channels (Def. 7.1).
- **Diagrams.** Proofs are written in a quantikz-style diagrammatic notation (§3.8, §5.3), which aligns the framework with operational-probabilistic and categorical treatments.

The original material is modest: the uniform channel-level formulation of steering and Bell nonlocality as entanglement-assisted incompatibility tests (§7.3, after the author's [5]), and an explicit parametrisation of the maximal tensor product of two squares by positive maps (Props 9.4–9.5).

## Key insight

Every operational notion here is convex geometry on a compact convex set K and its dual cone. Effects are affine functionals 0 ≤ f ≤ 1_K. Channels are affine maps, which equivalently form a base of a cone in A(K_A) ⊗ A(K_B)* (Prop. 6.9), so channels, superchannels and ensembles are themselves state spaces (p. 37). "Classical" means exactly "K is a simplex". Several independent-looking nonclassical phenomena are each equivalent to that one geometric failure:
- entanglement with some partner (Thm 5.21);
- inability to broadcast (Thm 7.7);
- identity not measure-and-prepare (Thm 7.7);
- existence of incompatible measurements (Thm 7.11);
- nonexistence of a post-processing-greatest measurement (Prop. 7.16).

## Assumptions

- **(S1–S5), Def. 2.1.** A state space is a closed, bounded, convex set in a *real, finite-dimensional* vector space with the Euclidean topology. S5 is flagged as a simplification (p. 5). Every result is finite-dimensional.
- **Mixtures are preparable** by classical randomisation (p. 6), with Popescu's caveat [109] acknowledged and set aside.
- **No-restriction hypothesis (§3.7).** Every affine f: K → [0,1] is a physical effect. It is assumed throughout except in §3.7.
- **Composites (BP1–BP5), Def. 5.1.** BP5 is local tomography: product effects separate joint states. It is what gives K_AB ⊂ A(K_A)* ⊗ A(K_B)* (Lemma 5.2) and the uniqueness step in the monogamy theorem (Thm 5.19). The review notes that theories without it are "actively researched" [130, 131].
- **Associativity of ⊗̃ (Def. 5.9)**, with the product "always defined whenever needed" (p. 28).
- **Complete positivity is relative to the chosen composite** (Def. 6.21). A channel is CP "with respect to K_A ⊗̃ K_B → K_A ⊗̃ K_C", and "since in general there is no unique choice of ⊗̃, we have to always specify" it (p. 41).

## Key results

- **Prop. 2.2**: every state space is compact and convex in R^n.
- **Thm 3.19 / Prop. 3.20**: K = {φ ∈ A(K)*+ : ⟨φ, 1_K⟩ = 1}, with dim A(K)* = dim aff(K) + 1 (R1). This is the "GPT dimension" used elsewhere in the record.
- **Framework equivalence (§3.4)**: convex effect algebras ≅ linear effect algebras ≅ order unit spaces ≅ the state-space framework (Thm 3.26 cites Gudder–Pulmannová for the first step; Prop. 3.28 and Eq. 3.22 cover the rest).
- **Thm 3.43**: optimal discrimination of x₀, x₁ with priors λ, 1−λ succeeds with p_succ = ½(1 + ‖λx₀ − (1−λ)x₁‖). The base norm is ‖ψ‖ = inf{λ+μ : ψ = λx − μy} (Prop. 3.42). In QT it is the trace norm (§8.1).
- **Prop. 5.6**: K_A ⊗̇ K_B ⊆ K_A ⊗̃ K_B ⊆ K_A ⊗̂ K_B. Effects of the maximal product are only separable (p. 25), citing [1] for the consequence that teleportation and dense coding fail there.
- **Thm 5.19** (monogamy): if the marginal of x_AB is pure, then x_AB = y_A ⊗ z_B. The proof uses BP5.
- **Prop. 5.20 / Thm 5.21**: K ⊗̇ S_n = K ⊗̂ S_n; and ⊗̇ = ⊗̂ iff a factor is a simplex. The converse is from [134].
- **Prop. 6.9**: C(K_A, K_B) = {Φ ∈ A(K_A)+ ⊗̂ A(K_B)*+ : Φ*(1_{K_B}) = 1_{K_A}}.
- **Props 6.23, 6.27, 6.28 / Cor. 6.24**: measurements and measure-and-prepare channels are CP for every composite. *Every* channel is CP with respect to the minimal product, and also with respect to the maximal product. So the partial transpose of |φ⁺⟩⟨φ⁺| lies in D(H) ⊗̂ D(H) but not in D(H⊗H), and both inclusions in Eq. 8.9 are strict (§8.2).
- **Thm 7.7**: (NB1) id_K is measure-and-prepare ⇔ (NB2) id_K is self-compatible ⇔ (NB3) a universal broadcasting channel exists ⇔ (NB4) K is a simplex. Cor. 7.8: every non-simplex K has incompatible channels. Cor. 7.9: not all channels on it are measure-and-prepare.
- **Thm 7.11** (cited): incompatible two-outcome measurements exist whenever K is not a simplex. **Prop. 7.16**: a post-processing-greatest measurement exists iff K is a simplex.
- **§7.3**:
  - Affinely independent test states never certify incompatibility (Prop. 7.20). The set of all pure states always decides it (Prop. 7.21).
  - Separable states cannot reveal channel steering (Prop. 7.24) or Bell nonlocality (Prop. 7.34).
  - A state is steerable by channels iff two copies of id_K steer it (Prop. 7.30).
  - For channels, steering is not necessary for Bell nonlocality (asserted, citing [5]).
- **§9 boxworld (square S)**: s₁₁ = s₁₀ + s₀₁ − s₀₀ (Eq. 9.3), and E(S) = conv{0, f_x, 1−f_x, f_y, 1−f_y, 1_S} (Eq. 9.5). Every x ∈ S ⊗̂ S equals (id ⊗ Ψ)(x₀) for a positive Ψ with ½⟨Ψ(s₁₀) + Ψ(s₀₁), 1_S⟩ = 1 (Prop. 9.5). The symmetry group is generated by a rotation R (R⁴ = id) and a reflection M (§9.3).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | States and effects are mutually dual; starting from state spaces, effect algebras or order-unit spaces gives the same framework | strong | proofs, Thm 3.19, Props 3.20, 3.28, Eq. 3.22; Thm 3.26 cited |
| C2 | Optimal two-state discrimination probability is ½(1 + ‖λx₀ − (1−λ)x₁‖) in base norm | strong | proof, Eqs. 3.38–3.43 (Prop. 3.42 sketched, full proof in [116]) |
| C3 | Any admissible composite lies between the minimal and maximal tensor products | strong | proof, Prop. 5.6 under BP1–BP5 |
| C4 | Minimal = maximal tensor product iff one factor is a simplex | strong (in the literature) / not shown here | only the "if" direction is proved (Prop. 5.20); the "only if" is cited to [134] |
| C5 | Identity is measure-and-prepare ⇔ self-compatible ⇔ broadcastable ⇔ K a simplex | strong | proof, Thm 7.7 and supporting Props 7.4, 7.6, Thm 5.19 |
| C6 | Every non-classical theory has incompatible two-outcome measurements | strong (in the literature) / not shown here | cited to [20, 25] |
| C7 | Complete positivity is not intrinsic: every channel is CP with respect to both the minimal and the maximal composite | strong | proof, Props 6.27–6.28 |
| C8 | Steering and Bell nonlocality can be defined for channels as entanglement-assisted incompatibility tests, and separable states reveal neither | strong | proof, Props 7.23–7.24, 7.31, 7.34 |
| C9 | In QT two channels are incompatible iff they steer some state; whether this holds in all GPTs is open | weak | assertion, p. 54, no citation given at that point |
| C10 | Axiomatic reconstructions typically land on Euclidean Jordan algebras, which "contain only quantum and quantum-like theories" | weak | assertion with citation [103], §1 |

## Concepts

- **State space K**: a compact convex subset of a real finite-dimensional space. **Pure state**: an extreme point. **Face**: a convex F ⊂ K closed under decomposition.
- **Effect algebra E(K)**: the affine f: K → [0,1], equivalently the order interval [0, 1_K] in A(K).
- **A(K), A(K)*, GPT dimension**: affine functions on K and their dual, with dim A(K)* = dim aff(K) + 1.
- **Order-unit norm / base norm**: sup-norm on A(K), and its dual on A(K)*. The base norm gives optimal discrimination.
- **No-restriction hypothesis**: every mathematically valid effect is physically available. A **restricted theory** is (K, E) with E ⊊ E(K), equivalently a pair K ⊆ S(E).
- **Minimal / maximal tensor product**: K_A ⊗̇ K_B, the convex hull of products; K_A ⊗̂ K_B, everything positive on product effects. A theory must fix its own ⊗̃ between them.
- **Local tomography (BP5)**: local effects separate joint states.
- **Channel**: an affine map K_A → K_B. Measurements, instruments and preparations are special channels. **Measure-and-prepare**: Φ = P ∘ m.
- **Complete positivity (relative)**: id ⊗ Φ maps K_A ⊗̃ K_B into K_A ⊗̃ K_C for the stated composites.
- **Compatibility**: the existence of a joint channel with the given marginals. **Self-compatible**: compatible with itself. **Broadcasting channel**: a joint channel for id_K with itself.
- **Channel steering**: no y_BCD reproduces both (Φ_i ⊗ id)(x_AD) (Def. 7.25). This follows [5], not the Wiseman–Jones–Doherty or Barnum–Gaebler–Wilce ensemble notions.
- **Boxworld**: GPTs of black boxes. The one-bit-in, one-bit-out system is the square S.

## Connections

This is the vocabulary layer beneath several of the record's closer readings. [LIT-003](../literature.d/LIT-003.md), cited here as [32], states its structure theorem for tomographically local GPTs and counts ontic states by "GPT dimension". Those are this review's BP5 and dim A(K)* from Prop. 3.20 (R1). A reader of [LIT-003](../literature.d/LIT-003.md) who wants the definitions should come here. The review does not cover [LIT-003](../literature.d/LIT-003.md)'s diagram-preserving maps or its simplex-embedding criterion, and it states noncontextuality results only as a §1 citation list ([28]–[32]).

Spekkens' toy theory, the subject of [LIT-054](../literature.d/LIT-054.md) and the root of [LIT-007](../literature.d/LIT-007.md) and [LIT-019](../literature.d/LIT-019.md), is cited ([29]) but not modelled. Since the toy theory's measurement set is restricted, §3.7's single paragraph and [120, 121] are the only relevant pointers.

[LIT-081](../literature.d/LIT-081.md) (Barnum, Gaebler & Wilce, "Ensemble steering, weak self-duality…") is cited as [2] in the §1 list on steering in GPTs. As noted in the corrections, the review's own steering (§7.3) is a different, channel-level notion. The reader who wants [LIT-081](../literature.d/LIT-081.md)'s results needs [LIT-081](../literature.d/LIT-081.md).

The review has nothing on ψ-ontology. PBR ([LIT-062](../literature.d/LIT-062.md)) and the ontological-models framework do not appear, so it cannot adjudicate [LIT-090](../literature.d/LIT-090.md)'s terminological point.

For [LIT-037](../literature.d/LIT-037.md) (Cuffaro & Hartmann), §6.5 makes a point that sharpens their complete-positivity discussion: whether a channel is CP depends on which composite is chosen. Every positive channel is CP with respect to the minimal and the maximal tensor product (Props 6.27–6.28). The quantum composite is what makes the transpose fail (§8.2). Their fn 61 appeal to purification as distinguishing quantum theory is a GPT-level principle that this review does not treat; operational-probabilistic theories are mentioned only in §1.

## Bearing on the record

It carries no ML-practice instruction. The one transferable tool is the base-norm characterisation of optimal binary discrimination (Thm 3.43), which in the classical case reduces to total-variation distance. That is textbook material, not a practice source. Within this record, the review should be what THEORY documents on the Spekkens/GPT cluster cite for definitions (GPT dimension, local tomography, simplex = classical, measure-and-prepare), in preference to re-deriving them. It should not be cited for Thm 5.21 or Thm 7.11 as proofs, since it defers both. It should not be cited for anything about restricted theories.

## Limitations

- It is finite-dimensional only (S5). Nothing covers infinite-dimensional or continuous-variable theories. That matters for [LIT-007](../literature.d/LIT-007.md)'s R^{2n} case.
- The no-restriction hypothesis is assumed nearly everywhere. Restricted theories get a single paragraph.
- Local tomography (BP5) is built into the definition of a composite, so non-locally-tomographic theories, including real-amplitude QT, fall outside the bipartite results.
- Several headline characterisations are cited rather than proved (see corrections). Dynamics, reversibility, entropy, thermodynamics, spectral decompositions and axiomatic reconstructions appear only as §1 pointers.
- Boxworld is treated only for the single square system. The maximal-incompatibility and CHSH claims are cited.
- v2 has the typos listed above.

## Open questions

- Whether channel incompatibility is equivalent to steering some state in every GPT, as it is in QT (p. 54).
- The general theory of consistent restrictions on effects, measurements and transformations (§3.7, pointing to [121]).
- Which ⊗̃ physical principles select for hypothetical theories like boxworld (§9.2 notes that "there is no physical principle that would select a specific tensor product").
- How entanglement, compatibility and steering results change without local tomography ([130, 131]).

## Corrections to the seeded skim

- The dossier calls §7.1 "a direct proof of no-broadcasting" and lists Theorem 5.21 among the "standard results" the review "proves". Only some of its headline theorems are proved in the text:
  - **Proved in-house:** Theorem 7.7 (from Thm 5.19, whose proof is transcribed from Barnum–Barrett–Leifer–Wilce [17], plus a linear-independence argument on a basis of pure states, Eqs. 7.21–7.23) and Theorem 3.43.
  - **Deferred:** Theorem 5.21 ("Proof. See [134]", Aubrun–Lami–Palazuelos–Plávala) and Theorem 7.11, that incompatible two-outcome measurements exist iff K is not a simplex ("See [20]").
  - **Half-proved:** Theorem 7.10 (partial broadcasting); only one direction is proved.
  - **Asserted:** the maximal incompatibility of f_x, f_y in boxworld (§9.4) is cited, not shown. So is the claim that "in quantum theory two channels are incompatible if and only if they steer some state" (p. 54).
- The dossier expects §3.7 to say how the no-restriction hypothesis affects "restricted theories like Spekkens'". It does not. §3.7 is one paragraph. It defines a restricted theory as a pair (K, S(E)) with K ⊆ S(E) (Eq. 3.45), warns that consistency "is not trivial", and refers to [120, 121]. Spekkens' toy theory is cited only in the §1 list of noncontextuality work ([29]). The review never treats it as a GPT, restricted or otherwise, and it has no bearing on [LIT-054](../literature.d/LIT-054.md)'s formalism.
- The dossier calls the review the reference for "c17's self-duality and steering results". The review's steering is a different notion: *channel* steering, meaning that no y_BCD reproduces both marginals (Defs 7.25–7.27, following Plávala 2017 [5]). It is not the ensemble steering of Barnum–Gaebler–Wilce ([LIT-081](../literature.d/LIT-081.md), cited as [2]). Self-duality is never defined. The nearest the review comes is noting an order isomorphism A(K)+ ≅ A(K)*+ for quantum theory (§8.1) and for the square (Eq. 9.33), and using it for a state–map correspondence (Prop. 9.5).
- Typos in v2 that a reader will trip on:
  - Def. 3.3 (face) omits "∈ F" after "λx + (1−λ)y".
  - Prop. 6.8 states Φ*: E(K_A) → E(K_B); the direction is reversed.
  - Prop. 6.13 has Σ f_i = 1_{S_n} where 1_K is meant.
  - Eq. 7.33 has Φ₂ ∈ C(K_A, K_B) where K_C is meant.
  - Eq. 9.13 repeats (1_S − f_x) where (1_S − f_y) is meant.
  - Thm B.9 has "max … ≤ 0 ≤ max" where the second should be a min.
  I have not checked whether the journal version corrects them.
