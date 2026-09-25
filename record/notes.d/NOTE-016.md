---
number: 16
status: Read
formerly:
- NOTE-tmpgv359
paper: LIT-016
title: 'The sheaf-theoretic structure of non-locality and contextuality'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (full text of arXiv 1102.0264v7 (29 Nov 2011, the revised
    version noted as the NJP 13 113036 text), 33 pp. — §§1–10, Appendix and
    all 60 references, every proof read. Text extracted with PyMuPDF
    (pdftotext unavailable). The 16×16 incidence matrix on p. 11 came
    through as a column of digits and was not re-checked entry by entry. The
    iopscience page was not fetched. Also read, to check Connections: the
    bibliography and introduction (pp. 4–5) of Belfiore & Bennequin
    2106.14587v3; all of Hansen & Gebhart 2012.06333; and the text of Bodnar
    et al. 2202.04579, searched for citations.). Upgraded from `Skimmed` to
    `Read`: the claims table, assumptions and results are new, and the skim
    is corrected where the full text disagreed.
date: '2026-09-25'
summary: >-
  For finite measurement scenarios, an empirical model has a factorizable
  (local / non-contextual) hidden-variable realization iff its compatible
  family of distributions extends to a global section (Thm 8.1). Over the
  reals every no-signalling model has such a section (Thm 5.9:
  "negative-probability LHV" ⇔ no-signalling, because both span the same
  subspace, of dimension D = Σ_{U∈𝒰}(l−1)^{|U|}, Thm 5.4). Contextuality
  comes in three strictly nested strengths (probabilistic ⊋ possibilistic
  ⊋ strong), with the Bell, Hardy and GHZ(n≥3) models as witnesses of each
  level.
---

# NOTE-016: The sheaf-theoretic structure of non-locality and contextuality

## Contribution

The paper gives a single, Hilbert-space-free formalism for Bell non-locality and Kochen–Specker contextuality. Measurements, contexts (a "measurement cover") and outcome sections form a sheaf ℰ. Empirical models are compatible families of the presheaf D_R ℰ of R-distributions, with R a commutative semiring. Within it the paper proves:
- non-locality/contextuality is exactly the non-existence of a global section;
- the question is linear-algebraic, via an incidence matrix;
- there are three strictly nested strengths of contextuality;
- over the reals every no-signalling model has a global section;
- strong contextuality coincides with maximal contextuality (non-contextual fraction 0) and reduces to CSP/SAT;
- Kochen–Specker results are generic strong contextuality, which Bell-type covers can never exhibit;
- quantum mechanics satisfies no-signalling for arbitrary commuting families (a generalized no-signalling theorem).

## Key insight

No-signalling is the sheaf compatibility condition. Locality and non-contextuality are the gluing (global-section) condition. Contextuality is the gap between the two: data that agree on every overlap of contexts but do not glue to one joint distribution over all measurements. The "incompatibility" of measurements is then *derived*, as the provable non-existence of a joint distribution, rather than postulated (§10). Changing the semiring R (booleans, ℝ≥0, ℝ) changes the strength of the question, and semiring homomorphisms carry solutions only one way (ℝ≥0 → 𝔹), which is what makes the hierarchy.

## Assumptions

- A finite set of measurements X and a finite outcome set O, the same O for every measurement (§2.2; footnote § says the generality is not needed).
- A measurement cover 𝓜: a family of subsets of X with ⋃𝓜 = X that is an anti-chain (maximal contexts only) (§2.4).
- Empirical models are **no-signalling by definition**: a family {e_C}_{C∈𝓜}, e_C ∈ D_R ℰ(C), with e_C|_{C∩C′} = e_{C′}|_{C∩C′} (§2.5). "We shall only consider no-signalling models in this paper."
- Distributions: finite-support functions d: X → R with Σd = 1, over a commutative semiring R. The three used are ℝ≥0 (probabilistic), 𝔹 = ({0,1},∨,∧) (possibilistic) and ℝ (signed or "negative" probabilities) (§2.3).
- Hidden-variable models (§8) assume λ-independence (h_Λ does not depend on the context) and parameter independence (compatibility of {h^λ_C} for each λ). Factorizability is h^λ_C(s) = ∏_{m∈C} h^λ_C|_{m}(s|_m).
- Quantum representations (§9): finite-dimensional Hilbert space, dichotomic observables for simplicity, and a context is a maximal pairwise-commuting subset.
- The notion of contextuality is Kochen–Specker / measurement-contextuality. It is **not** Spekkens' generalized (preparation/transformation) noncontextuality, and the paper does not address that notion.

## Key results

- **Prop 3.1** — A global section of e gives a local/non-contextual *deterministic* hidden-variable model realizing e (a distribution on the global assignments O^X).
- **Prop 4.1** — Solutions over R of the augmented system M′X = V′ (the incidence matrix plus a row of 1s) are in bijection with the global sections of e. For Bell-type (n,k,l) covers the augmentation is unnecessary (stated, not proved).
- **Incidence matrix size** (§4.2) — for (n,k,l) Bell scenarios the matrix is (kl)^n × l^{kn}, with l^{(k−1)n} ones per row. The (2,2,2) matrix is 16×16 of rank 9.
- **Prop 4.2 (Bell)** — The model with rows (a,b): ½,0,0,½; (a′,b), (a,b′): ⅜,⅛,⅛,⅜; (a′,b′): ⅛,⅜,⅜,⅛ has no global section over ℝ≥0. Proof: four of the 16 equations give LHS ≥ ½ against 3/8.
- **Prop 4.3 (Hardy)** — The possibilistic Hardy model (zeros at (a′,b)(0,0), (a,b′)(0,0) and (a′,b′)(1,1)) has no boolean global section. Proof: 4 clauses.
- **Prop 4.4** — If MX = V has a solution over ℝ≥0, then MX = V̂ (the support) has one over 𝔹, because ℝ≥0 → 𝔹 is a semiring homomorphism. The converse fails: the Bell model's support *is* extendable, by [25] (Mansfield–Fritz: Hardy models are complete for (2,2,2), and at least 3 zeros are needed). Hence **possibilistic non-extendability is strictly stronger than probabilistic**.
- **Prop 5.1** — Every probabilistic model is linearly determined by e^{(0)}, its values on sections with no outcome equal to 1, over partial contexts 𝒰 = {U : ∃C∈𝓜, U ⊆ C}.
- **Prop 5.2** — The span of the no-signalling models has dimension ≤ D := Σ_{U∈𝒰} (l−1)^{|U|}. **Prop 5.3** — The span of the non-contextual (global-section) models has dimension ≥ D, via explicit linearly independent columns v_{U,s}.
- **Theorem 5.4** — For any cover, the linear spans of the non-contextual models and of the no-signalling models coincide, with dimension D. **Thm 5.5** — For every (no-signalling) probabilistic model, MX = V has a real solution. **Prop 5.6** — rank M = D.
- **Theorem 5.9** — "Probability models have local hidden-variable realizations with negative probabilities if and only if they satisfy no-signalling." (⇐ is Thm 5.5; ⇒ is Prop 5.8, since restrictions of a global section are always compatible.) Corollary drawn: negative probabilities alone cannot characterize QM, because they give the whole no-signalling set, including PR boxes (explicit signed solution in §5.2).
- **Prop 5.7** — For a homogeneous cover (all contexts of size n, each j-subset in N_j contexts, p = |𝓜|): D = Σ_{j=0}^{n} C(n,j)·p(l−1)^j / N_j. Worked values:
  - (n,k,l) Bell scenarios: D = (k(l−1)+1)^n. This matches Pironio's D−1; the difference is marginalization over ∅.
  - 18-vector KS cover: D = 118, against ambient dimension 144.
  - Peres–Mermin square: D = 34, against ambient 48.
  - (n,2,2) scenarios: rank 3^n.
- **Strong contextuality** (§6) — Define S_e := {s ∈ O^X : ∀C, s|_C ∈ supp(e_C)}. The model e is strongly contextual iff S_e = ∅. Strong contextuality implies possibilistic non-extendability, because extendability implies S_e ≠ ∅. Hardy is not strongly contextual (witness {a↦1, a′↦0, b↦1, b′↦0}), and neither is Bell.
- **Prop 6.1** — The GHZ models of type (n,2,2) are strongly contextual for all n ≥ 3. Full proof for n = 4k; n = 4k+2 and odd n ≥ 5 "proceed similarly"; n = 3 via Mermin's instruction-set argument, sketched. This gives the strict hierarchy **Bell < Hardy < GHZ**.
- **Prop 6.2 (Lal, private communication)** — The only strongly contextual no-signalling (2,2,2) models are the PR boxes. Stated without proof.
- **Prop 6.3** — Strongly contextual ⇔ maximally contextual, i.e. the non-contextual fraction (the sup of λ over decompositions e = λL + (1−λ)q, with L local and q no-signalling) is 0. **Props 6.4–6.5** — Maximal contextuality (and maximal non-locality in Bell scenarios) ⇔ the CSP (X, O, {supp e_C}) has no solution. For dichotomic outcomes this is ⇔ φ_e = ⋀_C ⋁_{s∈supp e_C} ψ_s is unsatisfiable.
- **Monotonicity** (§7) — supp e ⊆ supp e′ and e′ strongly contextual ⇒ e strongly contextual. This is the basis of generic (model-independent) results.
- **Prop 7.1 (parity condition)** — If φ_𝓜 = ⋀_C ONE(C) has a global section, then every common divisor of {|𝓜(m)|} divides |𝓜|. For example, each measurement in an even number of contexts with |𝓜| odd means no section. This generalizes "parity proofs" (e.g. the 18-vector cover: 9 contexts, each vector in 2).
- **Prop 7.2** — For the maximal-clique cover 𝓜_G of a graph G, φ_𝓜 has a global section ⇔ G has a stable transversal. **Kochen–Specker graph**: a faithful orthogonal co-representation in ℝ^d, all maximal cliques of size d, and no stable transversal. **Thm 7.3** is cited from Lovász–Saks–Schrijver, not proved here: a graph on n nodes whose complement is (n−d)-connected has a faithful orthogonal co-representation in ℝ^d.
- **Theorem 8.1** — For any D_R, e has a realization by a factorizable hidden-variable model ⇔ e has a global section. Proof: the product of single-measurement marginals is a distribution on O^X for each λ; averaging over h_Λ gives the section.
- **Prop 9.2 (generalized no-signalling)** — For any quantum state ρ and any contexts C, C′ of commuting projective observables, ρ_C|_{C∩C′} = ρ_{C′}|_{C∩C′}. The paper also notes a reduction to the standard theorem via Tsirelson's Thm 9.1, which it credits to a referee.
- **Prop 9.3** — A cover is of Bell type iff it is the maximal-clique family of the complement of an equivalence relation (so incompatibility is transitive). **Prop 9.4** — For any quantum representation of a Bell-type cover and any section s, some product state has s in its support. So **there is no Kochen–Specker-type (state-independent) strong contextuality theorem for Bell-type scenarios**. Only model-specific ones exist, such as GHZ.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | An empirical model has a factorizable hidden-variable realization iff it has a global section of D_R ℰ over the cover | strong | Thm 8.1 + Prop 3.1, full proofs |
| C2 | For any finite cover, the non-contextual and no-signalling models span the same real subspace, of dimension D = Σ_{U∈𝒰}(l−1)^{|U|} | strong | Thm 5.4 via Props 5.1–5.3, full proofs |
| C3 | "Negative-probability" local HV realizations exist iff the model is no-signalling, so negative probabilities cannot single out QM | strong | Thm 5.9 (Thm 5.5 + Prop 5.8); PR-box signed solution in §5.2 |
| C4 | Possibilistic non-extendability is strictly stronger than probabilistic non-extendability | moderate | Prop 4.4 proved; strictness rests on the Bell model's support being extendable, which is asserted as "easy to show directly" and via [25] |
| C5 | Strong contextuality is strictly stronger than possibilistic non-extendability | strong | §6 argument + explicit Hardy witness assignment |
| C6 | GHZ models are strongly contextual for all n ≥ 3, completing the hierarchy Bell < Hardy < GHZ | moderate | Prop 6.1: full proof for n = 4k; other cases "similarly" or sketched (n = 3 via Mermin) |
| C7 | Strongly contextual ⇔ maximally contextual (non-contextual fraction 0) ⇔ the associated CSP/SAT instance is unsatisfiable | strong | Props 6.3–6.5, proofs (6.3 relies on Thm 8.1) |
| C8 | The only strongly contextual (2,2,2) no-signalling models are the PR boxes | weak | Prop 6.2, private communication from R. Lal, no proof given |
| C9 | A common divisor of the \|𝓜(m)\| not dividing \|𝓜\| rules out a Kochen–Specker assignment (generalized parity proof) | strong | Prop 7.1, proof (sufficient condition only) |
| C10 | Kochen–Specker graphs realized by quantum observables give state-independent strong contextuality | moderate | Props 7.2, 9.2 and §9.2 argument; realizability condition via Thm 7.3, cited not proved |
| C11 | Quantum mechanics obeys no-signalling for arbitrary families of commuting observables, not just tensor factors | strong | Prop 9.2, direct trace computation (finite-dimensional, projective) |
| C12 | No Kochen–Specker-type (generic) theorem exists for Bell-type covers | strong | Props 9.3–9.4, proofs |
| C13 | The sheaf formalism "opens the door" to powerful sheaf-theoretic (e.g. cohomological) methods | weak | assertion + pointer to preliminary cohomology work [53] (§10) |

## Method

Mathematical. The paper formalizes the operational scenario as a sheaf of events ℰ: P(X)^op → Set, ℰ(U) = O^U, which is trivially a sheaf. It composes ℰ with the distribution functor D_R to get the presheaf of distributions, whose restriction maps are marginalization. The question "does e glue?" becomes the linear system MX = V, where M is the 0/1 incidence matrix of the restriction map O^X → ∐_C O^C. The system is read over ℝ≥0 (a linear programme), over 𝔹 (SAT/CSP) or over ℝ (unconstrained). Dimension counting (Props 5.1–5.3) settles the real case in general. Explicit small sub-systems give the Bell and Hardy no-go proofs, and parity/graph combinatorics give the Kochen–Specker ones.

## Concepts

- **measurement cover 𝓜** — an anti-chain of subsets of X covering X. Its elements are the maximal contexts of jointly performable measurements.
- **section / event** — s: U → O. ℰ is the sheaf of events.
- **empirical model** — a compatible family {e_C ∈ D_R ℰ(C)}_{C∈𝓜}. Compatibility *is* no-signalling here, so the term always means a no-signalling model.
- **global section** — d ∈ D_R ℰ(X) with d|_C = e_C for all C. It is the same thing as a joint distribution over all measurements that marginalizes correctly (Fine-style extendability).
- **probabilistically / possibilistically non-extendable** — no global section over ℝ≥0 / the support has none over 𝔹. The paper also says "probabilistic / possibilistic non-locality".
- **strongly contextual** — S_e = ∅: no global assignment is consistent with the support in every context.
- **non-contextual (local) fraction; maximally contextual** — the sup of λ in e = λL + (1−λ)q; maximally contextual means that sup is 0.
- **factorizable hidden-variable model** — λ-independent, parameter-independent (compatible) and product-form per λ. It subsumes Bell locality and "non-contextuality at the level of distributions".
- **Kochen–Specker graph** — a graph with a faithful orthogonal co-representation in ℝ^d, all maximal cliques of size d, and no stable transversal.
- **generalized no-signalling** — marginals of a quantum state on a commuting family do not depend on which compatible family it is measured with.

## Connections

Builds on: Fine 1982 (joint distributions ⇔ Bell inequalities), which it puts into sheaf form. It also builds on Abramsky's "Relational hidden variables and non-locality" [18] (the possibilistic case), Brandenburger–Keisler and Brandenburger–Yanofsky on hidden-variable properties, and Pironio's / Basoalto–Percival's transfer matrices and dimension count, which it generalizes from Bell scenarios to arbitrary covers. It credits Isham–Butterfield [57] for the insight that Kochen–Specker is non-existence of global sections of a presheaf, and it separates itself from the topos approach (Isham, Döring, Heunen–Landsman–Spitters). The topos approach uses the operator-algebraic spectral presheaf, has no distribution functor or measurement covers, and does not treat locality or extendability. The paper compares itself with Cabello–Severini–Winter [8] (the graph-theoretic approach, events rather than measurements). Descendants it points to: the Čech-cohomology obstruction of Abramsky–Barbosa–Mansfield [53]. Its notion is not Spekkens' generalized noncontextuality (dossier items 14, 17, 71). The two should be kept apart.

**ML descendants: checked, and much weaker than the dossier implies.**
- *Belfiore & Bennequin, "Topos and Stacks of Deep Neural Networks" (2106.14587v3; [ANTH-LIT-698](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-698.md)).* Its bibliography contains this paper as [AB11], "Samson Abramsky and Adam Brandenburger … New Journal of Physics, 13(11):113036, 2011". The single in-text citation (Introduction, p. 4) is in a list of prior uses of sheaves and cosheaves for information networks: Ghrist–Hiraoka, Curry, Robinson–Joslyn, "and Abramsky et al. specially for Quantum Information [AB11]". A text search of the whole 152-page monograph for "Abramsky", "contextuality", "non-local", "Kochen" and "Isham" finds no other occurrence. The monograph's machinery is Grothendieck topoi, fibrations/stacks over a DNN's site, Martin-Löf type theory and homotopy. It uses nothing specific to this paper: no measurement covers, no distribution presheaf, no global-section obstruction. **So it cites this paper as related work; it does not build on it.**
- *Sheaf neural networks.* Hansen & Gebhart, "Sheaf Neural Networks" (2012.06333), was read in full (6 pp.). Bodnar et al., "Neural Sheaf Diffusion" (2202.04579, 29 pp.), was text-searched. Neither mentions Abramsky or contextuality. Both descend from cellular sheaves and sheaf Laplacians (Hansen–Ghrist, Curry), not from this paper. Other sheaf-NN papers were not checked; any claim of a lineage there is unverified.
- What is genuinely shared is the abstract "local consistency without global consistency" pattern (compatible families vs. global sections). That is common to all sheaf theory; it did not originate here.

## Bearing on the record

This is a quantum-foundations / applied-category-theory paper, and it carries **no instruction for ML practice**. It should not be cited from any anthology practice or theory. The one existing cross-link is the anthology's reading of Belfiore–Bennequin ([ANTH-LIT-698](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-698.md)), which lists "Abramsky-Brandenburger (item 75)" among related work. That is accurate as a description of B&B's related-work paragraph, and it should not be read as a technical dependency. If a record document or curation entry calls this paper "the bridge" between the quantum cluster and topos/sheaf ML, that overstates a single related-work citation and should be softened. The substantive content (Thms 5.4/5.9, 8.1; the hierarchy; Prop 9.4) bears on the quantum-foundations cluster in this reading record (nucleation [LIT-016](../literature.d/LIT-016.md) / NOTE-016). A reading of the Spekkens items should note that the two senses of "contextuality" differ.

## Limitations

- **Finite only**: finite X and O, one outcome set for all measurements. The measure-theoretic case is flagged as future work (§10.1).
- **No-signalling is built into the definition** of an empirical model, so the framework says nothing about signalling data, e.g. real experimental data with disturbance. (Handling that is the aim of later work such as Contextuality-by-Default; this paper does not address it.)
- Several headline results rest on less than a full proof:
  - Lal's PR-box characterization (Prop 6.2) is unproved here.
  - The Bell model's support being possibilistically extendable, which is needed for the strictness of C4, is asserted and referred to [25].
  - GHZ strong contextuality is fully proved only for n = 4k; the other cases are sketched.
  - The realizability of KS graphs leans on a cited graph-theory theorem.
- The abstract's "sheaf theory" is mostly vocabulary: ℰ is trivially a sheaf, D_R ℰ is a presheaf, and all proofs are elementary linear algebra and combinatorics. The "powerful methods of sheaf theory" (cohomology) are promised, not used (C13).
- The quantum side (§9) is restricted to finite-dimensional, projective, mostly dichotomic observables.
- The hierarchy is between three qualitative levels. The paper gives no quantitative measure beyond the non-contextual fraction, which it uses only at its extreme value 0.

## Open questions

- A measure-theoretic (infinite-outcome) generalization of Thms 5.4, 5.9 and 8.1 (flagged in §10.1).
- Whether cohomological invariants can detect strong contextuality completely. [53] gives witnesses for salient examples only, and this paper does not ask whether the obstruction is also necessary. What later work found is unverified here.
- A necessary-and-sufficient combinatorial condition for KS-type covers. Prop 7.1 is only sufficient for non-existence.
- A quantitative theory interpolating between the levels (the contextual fraction as a graded measure), and a characterization of which covers admit quantum strongly contextual models.
- A published proof of Lal's result, and its extension beyond (2,2,2).

## Corrections to the seeded skim

- None of substance: the dossier's outline matches the text. Refinements: (a) the paper's own term is the "non-contextual fraction", and it appears here only as a tool to prove strong ⇔ maximal contextuality (Prop 6.3). The quantitative "contextual fraction" programme is later work, not this paper. (b) The hierarchy is stated in the Introduction as holding between *properties* ("strong contextuality implies possibilistic non-locality, which implies probabilistic non-locality") and between *models* (Bell < Hardy < GHZ). The dossier gives only the model-level version.
- The dossier says Kochen–Specker graphs give generic strong contextuality "(§6–7)". The quantum realizability that makes them *quantum* witnesses is in §9.2, and only for vector sets in which every vector lies in an orthonormal basis drawn from the set. §7 alone gives only the combinatorial half.
- The dossier's "ML link: item 69 cites this paper" (item 69 = Belfiore–Bennequin, [ANTH-LIT-698](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-698.md)) is verified, but it is thinner than "bridge" suggests. The paper is cited exactly once, in a related-work list (p. 4), and nothing in that monograph uses it technically. Neither of the two main sheaf-neural-network papers checked cites it at all (see Connections).
