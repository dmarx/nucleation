---
number: 135
status: Read
formerly:
- NOTE-tmpiu4w9
paper: LIT-143
title: 'Kleiner & Ludwig — Mathematical structure of experience'
version: 2
history:
- version: 2
  date: '2026-09-26'
  note: >-
    Read in full (full text of the Synthese version of record (Synthese
    (2024) 203:89, 23 pp., CC BY; received 20 Feb 2023, accepted 18 Jan
    2024, published online 5 Mar 2024), from Springer's open-access PDF. I
    read the abstract and keywords, the introduction, §§1–6, footnotes 1–14,
    Fig. 1's caption, the acknowledgements and the reference list. I also
    compared the whole text against arXiv:2301.11812v1 (24 pp.; v1 is the
    only version listed) and read v1's §4 "Metric Structure" (pp. 13–16) and
    its conclusion in full, because the Synthese version removes them.
    Section and page references below are to Synthese unless marked "v1". I
    did not use any other arXiv material.). Upgraded from `Skimmed` to
    `Read`: the claims table, assumptions and results are new, and the skim
    is corrected where the full text disagreed.
date: '2026-09-26'
summary: >-
  The paper proposes a definition, (MSC). A mathematical structure S =
  ((A_i), (S_j)) is a structure *of* conscious experience iff (S1) its
  domains are sets of experiential aspects, and (S2) every relation or
  function S_j has an "S_j-aspect". An S_j-aspect is an aspect that a
  variation of experience changes exactly when the variation fails to
  preserve S_j. The older condition (MDC), that a structure is "of"
  experience if its domains are aspects and its axioms hold, survives only
  as the necessary condition for *describing* experience, because as a
  sufficient condition it admits incompatible structures (discrete and
  non-discrete topologies on the same set), arbitrary re-definitions
  (every C·d for C > 0) and consciousness-indifferent structures. Worked
  examples: experienced relative similarity is a strict partial order that
  satisfies (MSC), given transitivity (assumed). Visual regions form a
  topology that satisfies (MSC), given Bayne and Chalmers's subsumptive
  unity thesis.
---
<!-- inactive-ok-file: LIT-190 — Proposed: read in full and unproven; cited by a close reading as a related account, not as an established result -->

# NOTE-135: Kleiner & Ludwig — Mathematical structure of experience

## Contribution

Before this paper, "mathematical structure of conscious experience" (quality spaces, Q-spaces, Φ-structures, phenomenal spaces) was used without a definition. The implicit standard, which the authors reconstruct as (MDC), was that domains are aspects and axioms hold. The paper shows that (MDC) cannot be sufficient, and it supplies a necessary-and-sufficient replacement, (MSC). (MSC) ties each relation or function of a structure to a specific experiential aspect through *variations*: changes of one experience into another, whether induced, natural or imagined. The criterion is stated axiomatically, so that it is neutral between qualia, qualities, phenomenal properties and IIT's phenomenal distinctions (fn. 3). It is also neutral between introspective, laboratory and theory-driven variations (§6).

## Key insight

A structure belongs to experience only if something in experience *behaves like the structure under change*. Formally, an aspect a is an S-aspect iff, for all variations and all relata, the variation fails to preserve S with respect to b₁…b_m exactly when it changes a relative to b₁…b_m (p. 12). Satisfying axioms on a set of qualia is cheap, since any set carries a discrete topology. Having a counterpart aspect that co-varies with the structure is not cheap.

## Assumptions

- **Set-up (§2.1).** There is a set E of experiences of one subject (all nomologically possible ones, or all inducible in the lab or in introspection). Each e has a well-defined set of aspects A(e), with A = ⋃_{e∈E} A(e). Aspects may be "instantiated relative to" other aspects.
- **Variations.** A variation e → e′ is a *partial* map v : A(e) → A(e′), not necessarily surjective, so aspects can disappear or appear (p. 8).
- **Mathematical structure** as in model theory: S = ((A_i)_{i∈I}, (S_j)_{j∈J}), domains plus relations or functions, usually with axioms (§2.2).
- **Relative similarity example (§3).** The experience set is a three-colour-chip display with a fixed reference b₀ (Fig. 1). **Transitivity of "less similar to b₀ than" is assumed**: "whether or not transitivity holds … is, ultimately, an empirical question. For the purpose of this example, we're going to assume that transitivity holds" (p. 14).
- **Topology example (§4).** The example assumes (i) the subsumptive unity thesis (Bayne & Chalmers 2003): for any set of phenomenal states at a time there is a state subsuming them; (ii) that "any set" means any set *experienced as unified*, to block the regress a_X, a_{X∪{a_X}}, … (fn. 12); (iii) that positions are aspects of visual experience (fn. 13); (iv) that visual regions are closed under intersection and finite union, which is introspective ("it seems to be the case", p. 18); and (v) that ∅ ∈ T by convention, because no aspect is needed for a relation with no relata.
- **Problem-1 resolution (§5).** Incompatible structures are characterised as ones where some automorphism of one is not an automorphism of the other (p. 18). The argument treats that automorphism as a variation A(e) → A(e) of an actual experience.

## Key results

- **(MDC) (p. 3).** A structure is of conscious experience iff (D1) its domains are sets whose elements correspond to aspects, and (D2) its axioms are satisfied.
- **Problem 1, incompatible structures (p. 4).** Any aspect set X carries both the discrete topology and {∅, A, A^⊥, X}, so (MDC) certifies incompatible structures on the same domain.
- **Problem 2, arbitrary re-definitions (pp. 4–5).** If (M, d) passes (MDC), so does (M, C·d) for every C > 0 ("uncountably infinite"). So does (f(a)+f(b))·d(a,b) under a modified set of axioms, which can break the triangle inequality.
- **Problem 3, indifference (p. 5).** Problems 1–2 are established without any input about experience beyond "some set of aspects".
- **(MSC) (p. 10).** S is of conscious experience iff (S1) every domain A_i ⊆ A, and (S2) for every S_j there is an S_j-aspect in A. The axioms of a claimed structure type must still hold, so (MSC) ⇒ (MDC): every structure *of* experience also *describes* it.
- **Change and preservation (p. 11).** v changes a relative to b₁…b_m iff a is instantiated relative to b₁…b_m in A(e) but not relative to v(b₁)…v(b_m) in A(e′). v preserves S with respect to relata iff (P1) R(b₁…b_m) = R(v(b₁)…v(b_m)) for a relation, or (P2) v(f(b₁…b_{m−1})) = f(v(b₁)…v(b_{m−1})) for a function.
- **Relative similarity (§3, pp. 13–15).** Let C be the colour qualities and bᵢ < bⱼ iff bᵢ is experienced as less similar to b₀ than bⱼ. If transitivity holds, (C, <) is a strict partial order, and the relative-similarity aspect is a <-aspect. So (C, <) satisfies (MSC).
- **Topology (§4, pp. 15–18).** Each phenomenal unity aspect a_X is an X-aspect for the unary relation X. So (A, T) satisfies (MSC) for any T of sets experienced as unified. With M the visual position aspects and T the regions of visual experience, (M, T) is a topology in closed-set form (∅, M ∈ T; closed under arbitrary intersections and finite unions), and hence "a topology of the visual content of subjective experience" (p. 18; cf. Tallon-Baudry 2022).
- **Resolution of the three problems (§5).** (1) No aspect can be both an S-aspect and an S′-aspect of incompatible S, S′, because a single variation cannot both change it and not change it. (2) C·d defines different relata, so whether a C·d-aspect exists is a substantive question and not automatic. (3) (MSC) cannot be applied without examining experience.
- **v1 only (removed in Synthese): metric structure is not a structure of experience** (v1 §4, pp. 13–16). See corrections.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | (MDC) as a sufficient condition admits incompatible, arbitrarily re-defined and consciousness-indifferent structures. | strong | explicit constructions (discrete vs {∅, A, A^⊥, X}; C·d), §1 |
| C2 | (MSC) implies (MDC), so earlier approaches keep their condition as a necessary one. | strong | direct from the definition (p. 10) |
| C3 | Experienced relative similarity (with respect to a reference) is a mathematical structure of experience. | moderate | short proof (pp. 14–15), conditional on assumed transitivity. The proof is near-definitional: < is defined from the experienced aspect, so the aspect tracks < by construction (reader's observation) |
| C4 | Visual regions carry a topology that is a mathematical structure of experience. | weak–moderate | proof that a_X is an X-aspect (pp. 16–17), conditional on the subsumptive unity thesis. The topology axioms for regions rest on how things "seem" (p. 18) |
| C5 | (MSC) resolves Problem 1: incompatible structures cannot share an S-aspect. | moderate | informal proof via automorphisms (pp. 18–19). It shows only that no single aspect serves both, not that both structures cannot pass (MSC) through different aspects. It also assumes the automorphism is realised by a variation of some e ∈ E, which is not argued (reader's check) |
| C6 | (MSC) resolves Problem 2: rescaled structures do not automatically qualify. | moderate | argument by relata (p. 19); it shows non-automaticity, not exclusion |
| C7 | The definition is conceptually and methodologically neutral. | moderate | the axiomatic set-up (§2.1, fn. 3); asserted in §6 |
| C8 | (MSC) may open new perspectives on measuring consciousness via the Representational Theory of Measurement. | weak | stated as an open question (p. 21) |
| C9 (v1 only) | Metric spaces are not structures of conscious experience. | weak | v1 §4: an argument from the construction of ℝ, and a doubt that "having distance n" is experienced. Withdrawn from the published version |

## Method

The paper uses conceptual analysis with model-theoretic tools. (1) It reconstructs the implicit criterion (MDC) and counterexamples its sufficiency. (2) It defines experiences, aspects (possibly relative) and variations as partial maps. (3) It adapts the notion of homomorphism to a single tuple of relata, giving "preservation". (4) It defines an S-aspect as an aspect whose change under variations coincides exactly with non-preservation of S. (5) It checks (MSC) on two cases by hand-proof. (6) It revisits the three problems with automorphism and relata arguments.

## Concepts

- **Aspect**: a placeholder for qualia, qualities, mental qualities, instantiated phenomenal properties, or IIT's phenomenal distinctions (fn. 2–3). It may be *instantiated relative to* other aspects.
- **Variation**: a change e → e′ with a partial map v : A(e) → A(e′) saying where each aspect goes. It may be induced, natural, or imagined (Husserl's "imaginary variations").
- **Describes conscious experience**: satisfies (MDC). This is reframed as the pragmatic, language-like use of mathematics (p. 6).
- **Of conscious experience**: satisfies (MSC).
- **S-aspect**: an aspect that changes under exactly those variations that fail to preserve S, for all variations and relata.
- **Phenomenal unity aspect a_X**: the experience that the aspects in X are unified; instantiated relative to X.

## Connections

The account of consciousness is **none in particular**; the paper is deliberately neutral. It presupposes realism about experiential aspects, meaning that every experience has a well-defined set of them, and it treats introspection and imaginary variation as legitimate evidence about structure. That puts it on the side of taking phenomenal structure as a real target. An illusionist such as Frankish ([LIT-103](../literature.d/LIT-103.md)) would read "aspects" as quasi-phenomenal properties. The definition does not need to take a side, and fn. 2 says so.

- [LIT-185](../literature.d/LIT-185.md) (IIT): (MSC) accepts IIT's phenomenal distinctions as one choice of aspect (fn. 3), and Problem 2 cites IIT's asymmetric distance function as an example of an arbitrarily re-axiomatised structure (p. 5). (MSC) gives a test that IIT's Φ-structures would have to pass to count as structures *of* experience rather than descriptions. The paper does not apply the test.
- [LIT-190](../literature.d/LIT-190.md) (Winkielman et al.) and this paper both take the unity of consciousness as a target. This paper derives structure from the subsumptive unity thesis. Winkielman et al. propose a mechanism (integration through processing-quality experiences). Neither engages the other.
- [ANTH-LIT-458](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-458.md) (the Platonic Representation Hypothesis) makes convergence claims about learned representation spaces. (MSC)'s distinction between a structure that *describes* a domain and one that is *of* it is the kind of test needed before any such space is said to mirror phenomenal structure. This is an analogy only; the paper does not discuss ML.

**Consciousness tag: justified.** The paper's subject is the formal structure of conscious experience.

## Bearing on the record

- A THEORY document that claims a formal space (similarity space, embedding, Φ-structure) captures the structure of experience should meet (MSC), or say that it only describes experience in (MDC)'s sense.
- Documents citing this paper for "metric spaces cannot model experience" are citing arXiv v1, not the published paper, and should say so or drop the claim.
- **ML practice: none.** There is no instruction for the Anthology of the SOTA. The only contact is the analogy above.

## Limitations

- Both worked examples are conditional on premises the authors flag but do not establish: transitivity (§3) and subsumptive unity plus the introspective closure of visual regions (§4).
- (MSC) is quantified over *all* variations of *all* experiences in E (p. 12). In practice no one can check that; any empirical application checks a finite sample. The paper does not say how to certify an S-aspect from finite data.
- The Problem-1 resolution does not rule out two incompatible structures both qualifying through different aspects. It assumes that mathematical automorphisms are realised as variations of experience.
- The "surprising" topology result depends on reading every subset as a unary relation, so the "structure" is the collection of unified sets. Whether that collection deserves the name *topological* depends on closure properties the paper supports only by how things seem.
- The published version gives no negative example. v1's metric case, the only one showing (MSC) excluding a widely used structure, was removed, so the published paper never shows the definition ruling a popular structure out.

## Open questions

- Do actual similarity judgements satisfy transitivity? The authors call it "ultimately, an empirical question", and a psychophysics test on the three-chip paradigm would settle it for that case.
- Is there a d-aspect for any metric? That is v1's withdrawn argument, and its withdrawal leaves it open.
- How would (MSC) connect to the Representational Theory of Measurement (Krantz et al. 1971) so as to yield measurement of consciousness (p. 21)?

## Corrections to the seeded skim

- **The metric result is not in the published paper.** The dossier reports "§§3–5 … Metric structure does not [qualify], partly because the real numbers … correspond to no aspect of experience", and it asks a deeper reading to check "the second reason for rejecting metrics". Both reasons are in arXiv v1 §4 only (pp. 13–16). The *immediate* reason: ℝ is constructed from equivalence classes of Cauchy sequences, which match no aspect. The *deep* reason: even an integer-valued path-length metric d(x,y) = length_<(x,y), built on relative similarity, would need a "d-aspect", an experience of two qualities being "a specific number apart", and "we doubt that they are experienced as being a specific number apart" (v1 p. 16). The Synthese version (2024) removes the whole section. §1 still uses metrics only to illustrate Problem 2, and the conclusion no longer says metric spaces fail (Synthese p. 21: relative similarity and topology only). Any note claiming "Kleiner & Ludwig show metric spaces are not structures of experience" is citing a preprint argument that the authors did not publish.
- **Section numbers differ between versions.** The dossier's map is v1's: §3 relative similarity, §4 metric, §5 topology, §6 problems revisited, §7 conclusion. Synthese has §1 status quo (pp. 2–6), §2 the definition (pp. 7–12), §3 relative similarity (pp. 12–15), §4 phenomenal unity and topology (pp. 15–18), §5 the three problems revisited, with the automorphism argument (pp. 18–20), and §6 conclusion (pp. 20–21).
- **The unification claim was dropped.** The dossier's abstract says the definition "may unify approaches across fields". That phrase is in v1's abstract and conclusion (v1 p. 21, "A new opportunity … is the unification"). The Synthese abstract and conclusion omit it. The published claim is narrower: a foundation for construction and identification of such structures, and a hoped-for "common formal language".
- **Keywords.** The dossier says "the paper lists no keywords". The Synthese version lists "Quality spaces · Qualia spaces · Phenomenal spaces · Perceptual spaces · Q-spaces · Structuralism" (p. 1).
- The dossier describes the topology as coming "via phenomenal unity". More exactly, it comes via the *subsumptive* unity thesis (Bayne & Chalmers 2003), restricted to sets "experienced as being unified" to block an infinite regress (p. 17, fn. 12). The worked case is visual regions, whose closure properties "appear to" and "seem to" hold (p. 18).
