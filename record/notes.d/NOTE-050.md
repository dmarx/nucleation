---
number: 50
status: Read
formerly:
- NOTE-tmpe99kk
paper: LIT-038
title: 'The relativity of causal knowledge'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (Full text of arXiv 2503.11718v2 (30 May 2025, 19 pp.),
    downloaded to raw4/2503.11718.pdf and extracted with PyMuPDF to
    raw4/2503.11718.full.txt and .j.txt. I read everything: §§1–6 and the
    supplementary Appendices A–E, which contain the definitions, the
    linear-SCM example, the invertibility assumption, all proofs, and the
    extended discussion with the toy and "agentic AI" examples. The
    commutative diagrams (eqs. 3, 4, 7 and the Definition 6 cube) came
    through as flattened labels. I reconstructed them from the prose and the
    proofs. I did not check the PMLR proceedings version against v2.).
    Upgraded from `Skimmed` to `Read`: the claims table, assumptions and
    results are new, and the skim is corrected where the full text
    disagreed.
date: '2026-09-25'
summary: >-
  The paper defines SCMs as functors I → Prob and interventions as natural
  transformations (which requires invertible mixing functions). It encodes
  each non-intervened SCM as the convex space Δ(V, Ω) of all probability
  measures on its endogenous space, and puts these spaces on a graph as
  stalks of a network sheaf and cosheaf. The restriction maps are
  interventionally consistent α-abstractions and the extension maps are
  unspecified affine maps. "Relative causal knowledge" is the image of
  alternating restriction and extension along a path (Def. 11). The two
  substantive-looking theorems are either unsound or vacuous. Theorem 1
  (every convex combination of a model's interventional measures is a
  soft-interventional measure of it) rests on a proof step that is false.
  Theorems 2 and 3 hold for any pushforward map, so interventional
  consistency does no work in them. There are no results about the sheaf.
---

<!-- inactive-ok-file: LIT-038 — Deferred: the paper is placed by this reading; the directive lapses when its status changes -->

# NOTE-050: The relativity of causal knowledge

## Contribution

The paper proposes a vocabulary: "relativity of causal knowledge". It builds that vocabulary from four pieces:
- a category SCM(I, Prob), whose objects are SCMs viewed as functors from the walking arrow I = (• → •) to probability spaces with measurable maps, and whose morphisms are natural transformations;
- hard and soft interventions, cast as such natural transformations (Lemma 1);
- Rischel's α-abstractions, recast with an exogenous component (Defs. 5–6);
- a "network sheaf" and "cosheaf" over a graph of subjects, valued in the category CS_prob of convex spaces of probability measures (Defs. 8–9).

Relative causal knowledge (Def. 11) is the set of measures obtained by pushing a node's measures along a path through alternating restriction and extension maps.

Once the definitions are unpacked, what is new is the definitions. The paper establishes no result about the sheaf, cosheaf or RCK. The discussion (§5) lists learning theory, cohomology and Hodge theory as future work.

## Key insight

The model to remember is this. Put each agent's causal model at a node. Put a shared, coarser, interventionally consistent abstraction on each edge. What one agent can know of another's causal knowledge is only what survives projection onto the shared abstraction and re-embedding into its own variables. The result is path-dependent and generally lossy (Fig. 1, eq. 10). A "global section" is a joint choice of measures that agree after projection on every edge (Def. 10).

This is a sensible picture of communication through abstractions. The formal apparatus adds little to it, because the stalks are all measures and the maps are arbitrary affine maps.

## Assumptions

- Markovian SCMs over continuous variables: a DAG G_M, independent node-wise exogenous noise, and product exogenous measure (Def. 1, eq. 1).
- Mixing functions M, with xᵢ = mᵢ(z_{Aᵢ}, zᵢ), are **invertible** as a map from exogenous to endogenous values (§2, App. C). This is needed for Lemma 1.
- Soft interventions replace fᵢ but **do not change parent sets** (p. 4). Hard interventions set constants.
- Prob has probability spaces as objects and measurable maps as morphisms. Measure preservation is not required by the text (p. 4).
- The α-abstraction (Def. 5) uses surjective variable maps a = ⟨a_Z, a_X⟩, and α = ⟨α_Z, α_X⟩ is "a natural transformation". Interventional consistency is commutation of the Definition 6 cube for all macro-interventions.
- The network is a finite graph of 0- and 1-cells (Def. 7). An edge exists iff the two SCMs share an IC abstraction.
- Extension maps β are *any* affine measurable maps landing in the costalk (eq. 9). No construction or existence argument is given.

## Key results

- **Lemma 1.** An intervention I is the natural transformation ⟨Id_{M(I)}, M_I ∘ M⁻¹⟩ : M → M_I. The proof is by construction from invertibility (App. D).
- **Lemmas 2–3.** ⟨Δ(V, Ω), cc_λ⟩ is a convex space in Fritz's sense, and these spaces with affine measurable maps form CS_prob. Both proofs are routine checks against Fritz 2009.
- **Theorem 1.** "Every convex combination of probability measures corresponding to a causal knowledge CK(M) is a valid soft-interventional probability measure for CK(M)." The proof is invalid, and the claim is false in general (see corrections).
- **Theorem 2.** The endogenous component α_X of an IC α-abstraction commutes with cc_λ, so it is affine. It is true, but it holds for any pushforward and needs neither IC nor Theorem 1.
- **Theorem 3.** There is a functor E : NI(I, Prob) → CS_prob with M ↦ Δ(V, Ω) and α ↦ α_X. It is true and near-trivial. The object map ignores CK(M), and the proof's appeal to Theorem 1 for well-definedness is unnecessary.
- **Defs. 8–11.** These define the network sheaf F, the cosheaf F̂, global sections and RCK. No properties are proved.
- **Worked example (§4, p. 8).** It has three subjects with 3, 5 and 3 variables and scalar edge abstractions X and Y. The restriction maps are 1 × n and the extension maps n × 1 matrices, acting on Gaussian covariances. It shows that RCK is Σ ↦ F̂ F Σ Fᵀ F̂ᵀ, which is rank 1, and it states the global-section condition as equality of the projected variances. It is illustrative only.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | SCMs can be written as functors I → Prob and interventions as natural transformations, "as rich as the canonical SCM framework" | moderate | Lemma 1 by construction; needs invertible mixing (App. C); "as rich as" is asserted (p. 5) |
| C2 | The observational and interventional measures of an SCM are closed under convex combination, which yields only soft-interventional measures (Thm. 1) | weak (unsound) | proof in App. D eq. 23 equates a mixture of pushforwards with the pushforward of a mixed map, which is false in general; the statement fails for mixtures that break the DAG's Markov property (see corrections) |
| C3 | IC α-abstractions are affine on measures (Thm. 2) | strong but vacuous | true for every measurable map, by linearity of pushforward; IC is not used |
| C4 | A functor encodes non-intervened SCMs into convex spaces (Thm. 3) | strong but vacuous | the object is Δ(V, Ω), all measures on V, independent of the SCM's mechanisms |
| C5 | The network sheaf and cosheaf "enable the transfer of causal knowledge across the network while incorporating interventional consistency" (abstract) | assertion | definitions only (Defs. 8–11); no theorem about transfer, consistency or sections |
| C6 | A global section corresponds to a set of consistent (non-)interventions, one per connected component, "vanishing" a divergence on edges | informal argument | §4 prose, p. 8 |
| C7 | Cohomology is non-trivial to define because CS_prob is not Abelian | informal argument | §5, correct as far as it goes; no attempt made |
| C8 | Relativity of causal knowledge "can drive a paradigm shift" in AI/ML causality | assertion | §5 and App. E; no result or experiment |
| C9 | The factored alignment in agent communication "aligns closely with" LoRA | assertion | App. E, p. 19; an analogy |
| C10 | Any protocol that uses causal abstraction to translate CK between agents "would be a specific instance of our framework" | informal argument | App. E, "Is RCK Needed?"; true almost by definition, because the framework allows arbitrary affine extension maps |

## Method

This is a definitional and position paper. It has no experiments and no algorithm. The formal route is:
1. SCM as functor (Def. 2);
2. the category SCM(I, Prob) (Def. 3);
3. interventions as natural transformations (Lemma 1);
4. causal knowledge CK(M) as the subcategory of M and its intervened states (Def. 4);
5. convex spaces of measures (Lemmas 2–3, Thm. 1);
6. α-abstraction and IC recast (Defs. 5–6, Thm. 2);
7. the encoding functor (Thm. 3);
8. network, sheaf, cosheaf, global section and RCK (Defs. 7–11).

## Concepts

- **Causal knowledge CK(M):** formally, the subcategory of SCM(I, Prob) generated by M and all its intervened states (Def. 4). "With slight abuse" it is then used to mean the set of endogenous observational and interventional measures (p. 5). At the stalk level it is replaced by all of Δ(V, Ω) (Thm. 3).
- **Stalk / costalk:**
  - the sheaf stalk at a node is E(M_ρ) = Δ(V, Ω)_ρ; at an edge it is E(M_τ), for the shared abstraction M_τ;
  - the costalk at a node is the subset of measures whose restriction equals a given χ_τ (eq. 9). The dependence on the choice of χ_τ is not addressed.
- **Restriction map:** the endogenous component α_X of the IC abstraction from node to edge.
- **Extension map:** an affine map β from edge to node. It is unconstrained beyond landing in the costalk.
- **Relative causal knowledge CK_{ρ₁,σ_k}:** the image of E(M_ρ) under β ∘ α ∘ … ∘ β ∘ α along a path of k edges. It is path-dependent (eq. 10). Figure 2's caption places it in CK(M_σ) and writes χ_{ρ,σ} ∈ CK(M_ρ), an internal inconsistency.
- **"Relativity" vs "relativism":** the paper denies that any "true" SCM is privileged. It also denies that this makes causal claims meaningless (p. 2).

## Connections

- **Builds on:**
  - Pearl's SCM framework and ladder of causation;
  - Rischel's (2020) α-abstraction, and causal-abstraction work (Rubenstein et al. 2017, Beckers & Halpern 2019);
  - Fritz's convex spaces (2009);
  - cellular sheaf theory (Curry 2014, Hansen & Ghrist 2019, Ghrist & Riess 2022 for lattice-valued sheaves).
- **Contrasted with:**
  - Jacobs–Kissinger–Zanasi (2019), a functorial treatment via string diagrams on discrete distributions;
  - transportability (Pearl & Bareinboim), causal transfer learning, and SCM equivalence.

  It claims no result that improves on any of these.
- **Concurrent work:** "Similar definitions to Definitions 1 and 2 appear in the concurrent work [7]" (D'Acunto et al., ICML 2025, causal abstraction learning).
- **Philosophy:** Woodward's manipulability, Psillos's causal pluralism, and Latour's actor-network theory are motivation only.
- **Within nucleation:** this is [LIT-038](../literature.d/LIT-038.md). Apart from its seeded skim (NOTE-050) and the 2026-09-25 curation entry, nothing cites it.

## Bearing on the record

- **[LIT-038](../literature.d/LIT-038.md).** It should leave Deferred for Rejected, with the reason in the status note. The central theorem is unsound, the encoding is vacuous, and §4 contains definitions without results. Its UAI acceptance is a fact about its venue, not a reason to read it. If the record keeps it for its framing, the framing is summarised fully by this note's Key insight.
- **Filing.** The seed filed it under `probabilistic-modeling` with `mathematics` secondary. That is right for what it is about.
- **No THEORY document is supported.** If nucleation holds or acquires a THEORY about causal models being subjective or abstraction-relative, this paper is not a source for it. At most it restates the view.
- **Anthology: none.** The seed was right that it is not `analysis-and-evaluation` material. It proposes no measurement, no practice and no evaluation method. Its only ML contact is the LoRA analogy (C9), which carries no instruction. No ANTH document should cite it.

## Limitations

- The paper's own §5 concedes that there is no learning theory ((co)sheaf inference and discovery), no cohomology (CS_prob is not Abelian), and no Hodge-like theory. Without these, nothing computable is defined over the network.
- Theorem 1 is unsound (see corrections), and Theorems 2–3 are vacuous.
- Mixing functions must be invertible (Lemma 1), and soft interventions must preserve parent sets. Markovian models over continuous variables only.
- Counterfactuals (the third rung) are mentioned (Remark 2) but receive no treatment in the sheaf part, which works only with endogenous observational and interventional measures.
- The extension maps β are not constructed. Their existence, their uniqueness, and whether α ∘ β = id on the edge are not discussed, so "perspective" is a free parameter.
- The worked example acts on Gaussian covariance matrices by linear maps. That is a different object from pushforwards of measures on Δ(V, Ω). For linear Gaussian models the two agree on second moments, but the example does not show the general construction.
- The notation is uneven. Eq. 2 is ill-formed as written, the Figure 2 caption contradicts Def. 11 about which stalk RCK lives in, and "M_H" appears in eq. 7 where M_I is meant.

## Open questions

- **Soft-intervention closure.** Is there a correct version of Theorem 1? The set of soft-interventional measures of a fixed DAG is *not* convex in general, as the Markov-violation counterexample shows. A correct statement would need to enlarge the model class, for example with a latent mixture selector, or to restrict the mixtures.
- **Sheaf-specific results.** Is there any result about global sections of the network sheaf of causal knowledge that uses interventional consistency? A single non-trivial theorem of that kind would give the construction content. The authors' cohomology and Hodge programme (§5) would be one route.
- **Comparison with existing work.** Does the framework subsume or improve on multi-agent causal-abstraction or transportability work in any testable way? A worked problem that the framework solves and existing tools cannot would settle it.

## Corrections to the seeded skim

- **What the convexity result buys: less than the seed says.** The seed summarises it as "observational and interventional measures form convex spaces, so non-intervened SCMs can be encoded as convex spaces of measures". The encoding functor E of Theorem 3 sends M to Δ(V, Ω), the space of *all* probability measures on the endogenous measurable space, not to CK(M) (Theorem 3 statement, p. 6; proof, p. 16). The stalk therefore depends on the SCM only through its variables' value space.

  Theorem 2 ("α_X is affine") holds for *any* measurable map, because pushforward is always affine on measures, and the proof's step (b) is just "linearity of the pushforward". Interventional consistency is used nowhere essential. The seed's deeper-reading question ("what the convexity result actually buys") has a short answer: nothing specific to causality.
- **Theorem 1 is unsound as proved and false as stated.** Its proof (eq. 23, p. 16) equates a mixture of pushforwards, λ m₁(μ) + (1 − λ) m₂(μ), with the pushforward (λ m₁ + (1 − λ) m₂)(μ) of the averaged mixing function. That identity fails in general. Take μ = N(0, 1), m₁(z) = z, m₂(z) = z + 2 and λ = ½: the mixture is bimodal, while the pushforward of z + 1 is N(1, 1).

  The statement itself also fails, as my own counterexample shows. On X₁ → X₂ → X₃ with unit-variance Gaussian noise, the observational model has c₂₁ = c₃₂ = 1. A soft intervention changes both coefficients to −1, which is parent-preserving and so allowed by the paper. The 50/50 mixture of the two joint measures violates X₁ ⊥ X₃ | X₂: at x₂ = 1, E[X₃ | x₁ = 1, x₂] ≈ +0.76 but E[X₃ | x₁ = −1, x₂] ≈ −0.76. That is analytic: the component weights are φ(0) : φ(2). A 2×10⁶-draw simulation gave +0.73 and −0.77. Every soft intervention the paper allows keeps the parent sets and independent node-wise exogenous noise, so it preserves the Markov property with respect to G_M. The mixture is therefore not any soft-interventional measure of M. The seed did not flag this.
- **Eq. 2 is not well-formed as written.** It writes χ = ×ᵢ mᵢ(μᵢ) over measures on overlapping exogenous coordinate sets Uᵢ × U_{Aᵢ}. Read as a product measure, it would make the endogenous variables independent, and the paper's own Appendix B gives the correlated N(0, MMᵀ).
- **"Richens & Everitt's result" is characterised by the paper, not tested by it.** The seed repeats the paper's gloss. The paper cites Richens & Everitt (ICLR 2024) as giving "evidence" that robustness to distribution shift requires an approximate causal model (p. 1), and builds nothing on that result. I have not read Richens & Everitt, so whether the gloss is accurate is unverified.
- **The seed misses the invertibility assumption.** Lemma 1, which makes interventions morphisms at all, requires the mixing map M to be invertible. Appendix C argues this for additive-noise, post-nonlinear and location-scale models. Remark 2 says a result by Brenier polar factorisation in concurrent work (ref. [7]) can drop it, but only at the level of distributions.
- **The seed omits the LoRA and agentic-AI analogy, and that analogy is the only ML content.** Appendix E (p. 19) says that linear restriction and extension give an "alignment matrix" factored as extension × restriction, which "aligns closely with" LoRA. This is an analogy with no argument behind it.
