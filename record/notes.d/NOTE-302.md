---
number: 302
status: Read
formerly:
- NOTE-tmprnyr0
paper: LIT-304
title: 'The Linear Representation Hypothesis and the Geometry of Large Language Models'
version: 1
history:
- version: 1
  date: '2026-09-29'
  note: >-
    Read in full (The full text of arXiv 2311.03658 v2 (17 Jul 2024, the
    ICML 2024 / PMLR 235 camera-ready), from the arXiv PDF, 24 pp. I read
    the abstract, §§1–5, Appendix A (summary figure), Appendix B (the proofs
    of Thms 2.2, 2.5, 3.2 and 3.4 and of Lemma 2.4), Appendix C (Tables 2–4
    and the experimental details) and Appendix D.1–D.6, and the references.
    Nothing was skipped. The figures (Figs 2–5 and 7–13) are histograms,
    heatmaps and arrow plots. They survive extraction only as axis labels,
    so what they show is taken from the captions and the text, and I give no
    values read off the plots. I checked one mathematical point numerically
    myself (the Theorem 3.4 point under Corrections and Bearing). I read the
    anthology's holding of this paper first, ANTH-LIT-606 and its reading
    (anthology NOTE-328), with the account ANTH-THEORY-090 and the practice
    ANTH-SOTA-378. Disagreements with them are reported below under ADR-013,
    and nothing in the anthology was edited.). The first NOTE on this paper,
    which was seeded from its abstract alone.
date: '2026-09-29'
summary: >-
  Three readings of "concepts are directions" are made precise with
  counterfactual pairs, and proved to line up. The shared direction of
  word-pair differences in the unembedding space is a logit-linear probe
  (Thm 2.2). The embedding-space direction is a steering vector that
  leaves causally separable concepts unchanged (Thm 2.5). Under any inner
  product making separable concepts orthogonal, the Riesz map sends the
  first to the second (Thm 3.2). Softmax training fixes the representation
  only up to γ ↦ Aγ + β, λ ↦ A⁻ᵀλ, so no inner product is identified, and
  the paper chooses M = Cov(γ)⁻¹ by setting a free diagonal D to the
  identity (Thm 3.4). Evidence: 27 concepts on LLaMA-2 7B (26 show a
  common direction; thing⇒part does not), read from histograms and
  heatmaps with no test statistic, plus a Gemma-2B heatmap comparison.
---

# NOTE-302: The Linear Representation Hypothesis and the Geometry of Large Language Models

## Contribution

Before this paper, "linear representation" named three things with no stated relation between them (§1).

- **Subspace.** Word-pair differences share a direction.
- **Measurement.** A linear probe reads the concept.
- **Intervention.** Adding a vector changes the concept and nothing else.

The paper defines the first precisely, in two spaces, and proves how the three relate. The unembedding-space direction is a probe (Thm 2.2). The embedding-space direction is a steering vector (Thm 2.5). An inner product under which causally separable concepts are orthogonal maps one onto the other (Thm 3.2).

It also makes a point about geometry that the rest of the interpretability literature had mostly passed over. The softmax objective is invariant under γ ↦ Aγ + β, λ ↦ A⁻ᵀλ for any invertible A (eq. 3.1). So no inner product, the Euclidean one included, is fixed by training, and cosine similarity between concept directions has no meaning until one is chosen.

## Key insight

Choosing an inner product is choosing which concepts count as orthogonal. The paper chooses it so that concepts that can vary freely of each other (causally separable ones) are orthogonal. Under that choice, and only then, "the direction word pairs share" and "the vector that steers" are the same vector, related by the Riesz map of the chosen inner product. The inner product is not a fact training delivers. It is structure the analyst supplies, from a judgement of causal separability plus an assumption about word statistics.

## Assumptions

- **Model form.** P(y | x) ∝ exp(λ(x)ᵀγ(y)), with λ the context (embedding) vector and γ the unembedding vector (§1). Only the final-layer context vector and the unembedding are studied.
- **Concepts are binary, ordered, and causal (§2.1).** A concept W is a latent variable caused by the context and causing the output, specified by counterfactual output pairs (Y(0), Y(1)). Its value is read deterministically off the output word.
- **Causal separability.** W and Z are causally separable if Y(W = w, Z = z) is well defined for every w and z. English⇒French and male⇒female are; English⇒French and English⇒Russian are not. Which concepts are separable is the authors' judgement.
- **Exact cones.** Def. 2.1 requires γ(Y(1)) − γ(Y(0)) ∈ Cone(γ̄_W) almost surely, where Cone(v) = {αv : α > 0}. Def. 2.3 requires λ₁ − λ₀ ∈ Cone(λ̄_W) for every context pair that raises W's probability and leaves every separable concept's conditional distribution fixed.
- **Enough separable concepts.** The converse of Lemma 2.4 and Thm 3.2 assume that for each W there are d − 1 concepts, each separable from W, whose directions complete a basis with γ̄_W. Thm 3.4 assumes d *mutually* separable concepts whose directions form a basis. With d = 4,096 for LLaMA-2 7B, this is an idealisation that no experiment checks.
- **Assumption 3.3.** For a word drawn uniformly from the vocabulary (not from text), λ̄_Wᵀγ and λ̄_Zᵀγ are independent for separable W and Z. Footnote 3 says only uncorrelatedness is used.
- **Experimental scope.** Single-token words only (App. C). Some counterfactual pairs and all intervention contexts were written by ChatGPT-4.

## Key results

- **Thm 2.2 (measurement).** logit P(Y = Y(1) | Y ∈ {Y(0), Y(1)}, λ) = α λᵀγ̄_W, with α > 0 depending on the pair. The proof is two lines: the softmax log-odds of the pair is λᵀ(γ(Y(1)) − γ(Y(0))), and Def. 2.1 makes that difference a positive multiple of γ̄_W. The paper notes that this "ideal probe" does not absorb correlated off-target concepts, unlike a fitted probe.
- **Lemma 2.4.** An embedding representation satisfies λ̄_Wᵀγ̄_W > 0 and λ̄_Wᵀγ̄_Z = 0 for every separable Z. The converse holds under the basis assumption.
- **Thm 2.5 (intervention).** Adding cλ̄_W leaves the pairwise probability of any separable concept constant in c and raises W's.
- **Unidentifiability (§3, eq. 3.1).** The softmax is unchanged by g(y) = Aγ(y) + β and l(x) = A⁻ᵀλ(x). So the representation is identified at best up to an invertible affine map, the concept directions up to A, and ⟨γ̄_W, γ̄_Z⟩ ≠ ⟨Aγ̄_W, Aγ̄_Z⟩ in general.
- **Def. 3.1, Thm 3.2 (unification).** A causal inner product makes separable concepts orthogonal. Under one, the Riesz isomorphism γ̄ ↦ ⟨γ̄, ·⟩_C maps γ̄_W to λ̄_Wᵀ. With A = M^{1/2}, embedding and unembedding representations coincide, and the Euclidean product in the transformed space is the causal one.
- **Thm 3.4 (explicit form).** If a causal inner product ⟨γ̄, γ̄′⟩_C = γ̄ᵀMγ̄′ exists and d mutually separable concepts give a basis G, then under Assumption 3.3, M⁻¹ = GGᵀ and GᵀCov(γ)⁻¹G = D for a positive diagonal D. With D = I, M = Cov(γ)⁻¹ (eq. 3.3). The implication runs one way only; see Corrections for what it does and does not constrain.
- **Experiments (§4, App. D; LLaMA-2 7B, 32K vocabulary, d = 4,096).** All of these are read from plots, with no test statistic.
  - *Common direction.* Leave-one-out projections of counterfactual pair differences onto the concept direction sit well to the right of 100K random word pairs for 26 of 27 concepts. thing⇒part "does not appear to have a linear representation" (Fig. 2, Fig. 7).
  - *Orthogonality.* The |⟨γ̄_W, γ̄_Z⟩_C| heatmap is mostly near zero, with blocks of related concepts: verb forms, and language pairs. lower⇒upper overlaps the language pairs other than French⇒Spanish (Fig. 3).
  - *Probe.* The French⇒Spanish direction separates random French and Spanish Wikipedia contexts, and male⇒female does not (Fig. 4, Figs 10–11).
  - *Steering.* Adding α·Cov(γ)⁻¹γ̄_W moves log P(queen)/P(king) and not log P(King)/P(king) (Fig. 5, Fig. 12). For "Long live the", "queen" is top-1 from α = 0.2 (Table 1). In Table 6 "queen" never reaches top-1, though the top words shift to "woman", "queen", "her" and "female".
  - *The inner product.* On LLaMA-2 the Euclidean product "somewhat works" (App. D.2). The causal product removes frequent⇒infrequent's spurious overlaps and shows the real overlaps of language pairs that share French. On Gemma-2B the Euclidean product fails and the causal product works, which the authors attribute to tied embeddings (Fig. 9).
  - *Sanity check.* Whitened directions are uncorrelated over the vocabulary for one separable pair (male⇒female, English⇒French) and correlated for one non-separable pair (verb⇒3pSg, verb⇒Ving) (App. D.6, Fig. 13).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The unembedding representation of a concept is a logit-linear probe for it, with the same direction for every counterfactual pair | strong (proof) | Thm 2.2; near-immediate from the softmax and Def. 2.1 |
| C2 | The embedding representation is a steering vector that changes W and leaves every separable concept unchanged | strong (proof) | Lemma 2.4, Thm 2.5, under exact-cone definitions |
| C3 | Softmax training does not identify an inner product on the representation space; Euclidean cosine is arbitrary | strong (proof) | eq. 3.1, an invariance argument |
| C4 | Under a causal inner product, the Riesz map sends each concept's unembedding representation to its embedding representation | strong (proof), under strong premises | Thm 3.2; needs d − 1 separable concepts completing a basis for each W |
| C5 | Cov(γ)⁻¹ is a causal inner product | moderate (proof of a necessary condition + a stipulated choice) | Thm 3.4 with D = I chosen; the theorem constrains M only once the true directions G are known (my check) |
| C6 | "We can rule out most inner products", e.g. the Euclidean one | weak (as stated) | §3.2 remark; by my check no M is ruled out by Cov(γ) alone, only by the unknown G |
| C7 | LLaMA-2 represents 26 of 27 tested concepts linearly in the unembedding space | moderate (experiment, qualitative) | Figs 2 and 7, projections against a random-pair reference, no statistic |
| C8 | Separable concepts are near-orthogonal under Cov(γ)⁻¹, and better so than under Euclidean | weak–moderate | heatmaps (Figs 3, 8, 9) read by eye; 27 concepts, 2 models; Euclidean "somewhat works" on LLaMA-2 |
| C9 | Directions built from word pairs steer generation as predicted | weak | one quadruple, 15 generated contexts, 27 directions (Figs 5, 12), and three top-5 tables |

## Method

1. Estimate each concept's unembedding direction as the normalised mean of its counterfactual pair differences (single-token pairs from BATS 3.0, a capitals list, and ChatGPT-4-written pairs; 4–63 pairs per concept, Table 2).
2. Whiten by Cov(γ)^{−1/2}, the covariance of the 32K unembedding rows.
3. Test the three notions:
   - *subspace:* leave-one-out projections against random pairs;
   - *orthogonality:* a heatmap of pairwise inner products;
   - *measurement:* project Wikipedia contexts in two languages onto a direction;
   - *intervention:* add α·Cov(γ)⁻¹γ̄ to λ(x) and watch two log-ratios and the top-5 tokens.

## Concepts

- **Concept** — a binary, ordered latent variable caused by the context and causing the output, specified by counterfactual output pairs (§2.1).
- **Causally separable** — Y(W = w, Z = z) is well defined for all w, z: the two can be varied freely and in isolation.
- **Unembedding representation γ̄_W** — the direction whose positive cone contains every pair difference γ(Y(1)) − γ(Y(0)), almost surely (Def. 2.1). Unique up to positive scaling.
- **Embedding representation λ̄_W** — the direction whose cone contains every context-embedding difference that raises W and leaves separable concepts fixed (Def. 2.3).
- **Causal inner product** — an inner product on the difference space Γ̄ under which separable concepts' unembedding representations are orthogonal (Def. 3.1).
- **Canonical representation** — the unit-norm element of the cone under the chosen inner product (§3).

## Connections

- **Identifiability.** Its §3 symmetry, f = A f′ and g = A⁻ᵀ g′, is the same one Nielsen et al. ([LIT-253](../literature.d/LIT-253.md)) take as their Thm 2.2 starting point for softmax models. [LIT-253](../literature.d/LIT-253.md) adds that the identification is not stable in KL. Park et al. do not discuss stability.
- **Downstream readings in this record.** [NOTE-240](NOTE-240.md) reads Xiong ([LIT-267](../literature.d/LIT-267.md)) as building on this paper's intervention definition while its experiments use the measurement (probe) reading. The text here confirms that the two are distinct objects in distinct spaces, joined only through a chosen inner product. [NOTE-240](NOTE-240.md)'s observation that Xiong's Fisher-LDA incidence is invariant under v ↦ Av in the λ → 0 limit is exactly the invariance §3 says training leaves free.
- **Cited antecedents.** Mikolov et al. and GloVe (the subspace notion), Wang et al. 2023 (the causal formalisation of concepts, for diffusion models), and Elhage et al. 2022 ([LIT-323](../literature.d/LIT-323.md)) among the LRH sources in §1. Nothing here depends on superposition. Park et al.'s concepts are binary and one-dimensional by definition, and Engels et al. ([LIT-322](../literature.d/LIT-322.md)) take this paper as the statement of the one-dimensional LRH they dispute.
- **Anthology.** [ANTH-LIT-606](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-606.md), read as anthology [NOTE-328](NOTE-328.md), with account [ANTH-THEORY-090](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-090.md) and practice [ANTH-SOTA-378](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/practices.d/SOTA-378.md). Disagreements are under Corrections.

## Bearing on the record

- **What it supplies for the prior-art map's role (§0, §2.1, row 1, §4 must-cite).** The map names this paper, with Xiong, as "the LRH program" that its response diagnoses as "the single-context, Boolean shadow" of the quantum-cognition, quantum-IR and topos structures. What the text supplies for that diagnosis:
  - *It owns the formal statement.* Concepts are oriented directions (cones), measured by linear functionals and moved by additive steering. It does own the machinery the map attributes to it.
  - *It has no Boolean or lattice structure.* There are no projectors, no negation, no meet or join, and no algebra of concepts at all. A concept is a linear functional plus a sign (Thm 2.2's logit). This matches [NOTE-240](NOTE-240.md)'s "observables vs. thresholded functionals" point. The "Boolean shadow" is therefore the map's reconstruction, not something Park et al. assert or deny. A response should say "we read the LRH as…", not "Park et al. assume a Boolean algebra".
  - *"Single context" fits by construction, for the separable family only.* The causal inner product is chosen so that a family of mutually separable concepts is orthonormal. The Thm 3.4 setting is literally a single orthonormal basis G of d mutually separable concepts, and in [THEORY-017](../theory.d/THEORY-017.md)'s terms that is one frame, supplied from outside the space. The non-separable concepts are exactly where the paper's own data show non-orthogonal directions: the blocks in Fig. 3, and English⇒French against French⇒German and French⇒Spanish in App. D.2. Rank-one projectors onto non-orthogonal directions do not commute. So the paper's own heatmap already contains non-commuting pairs. The paper handles them only by excluding them from the orthogonality requirement ("not causally separable"). Whether they are *incompatible* in the quantum-logical sense, rather than merely correlated, is not addressed. Non-orthogonality alone is not contextuality ([THEORY-012](../theory.d/THEORY-012.md)). This is my reading, and it is the most direct hook the response has into this paper.
- **[THEORY-017](../theory.d/THEORY-017.md) (basis and unitary invariance).** A worked example from ML, and a stronger one than the table's. For a softmax model the intrinsic symmetry group is GL(d), not O(d). Training fixes the representation only up to γ ↦ Aγ, λ ↦ A⁻ᵀλ (eq. 3.1). So not even an inner product is intrinsic, let alone a basis. The paper supplies one from outside, in two stages: a judgement of which concepts are separable, and Assumption 3.3 plus the choice D = I. And as shown under Corrections, even that choice is pinned down only by the stipulation D = I, not by the data. [THEORY-017](../theory.d/THEORY-017.md)'s table could carry a row: *Park, Choe & Veitch — intrinsic: nothing beyond the softmax's GL(d) orbit; supplied: an inner product, from causal-separability judgements and the stipulation D = I.* That needs [LIT-304](../literature.d/LIT-304.md) read (now done) and a decision by the owner. I have not changed [THEORY-017](../theory.d/THEORY-017.md).
- **[THEORY-004](../theory.d/THEORY-004.md) / [THEORY-008](../theory.d/THEORY-008.md).** [THEORY-004](../theory.d/THEORY-004.md) says a representation is fixed by its kernel up to O(d). This paper is the reminder that for a softmax model's final layer the kernel itself is not identified: the context kernel λ(x)ᵀλ(x′) changes under A⁻ᵀ. So [THEORY-004](../theory.d/THEORY-004.md)'s premise, a given kernel, is an extra choice there.
- **The map's R2 (the "Universal Convergence (Riesz-forced unique factorization)" theorem, row 10).** The one Riesz step in this literature is Thm 3.2. It is the textbook Riesz isomorphism of a finite-dimensional inner product space, and it depends entirely on which inner product is chosen, which training does not fix. So this paper is evidence *against* a Riesz argument forcing uniqueness. Riesz transports whatever inner product is supplied, and supplies none. If the owner's Convergence argument leans on Riesz to force a unique factorisation, this paper's §3 is the counterexample a referee would cite.
- **[LIT-267](../literature.d/LIT-267.md) (Xiong).** Confirmed. Xiong's half-spaces are this paper's cones plus a threshold, and Xiong's Def. 2 is this paper's Def. 2.3 and Thm 2.5. [NOTE-240](NOTE-240.md)'s description of the dependence is accurate.
- **ML practice.** Already held in the anthology ([ANTH-LIT-606](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-606.md), [ANTH-SOTA-378](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/practices.d/SOTA-378.md)). Nothing new for practice here, beyond the disagreements above, which bear on how [ANTH-SOTA-378](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/practices.d/SOTA-378.md)'s evidence is summarised.
- **For filing.** Tags as seeded: `representation-learning` first, then `mathematics` (identifiability, the Riesz argument). Not proposed: `logic`, since the paper has no concept algebra; `philosophy-of-language`, since concepts are operationalised, not analysed.

## Limitations

- **Only two spaces.** Only the output and final-layer context spaces are covered (§5, the authors' own statement). Intermediate layers, where most probing and steering are done, are left open.
- **The idealisations are never tested.** Exact cones, deterministic concept readout, and d − 1 (or d) separable concepts completing a basis are all unchecked. thing⇒part shows that some concepts fail even the approximate version.
- **The inner product is chosen, not found.** The choice D = I is unjustified, and "rule out most inner products" does not hold against the covariance alone.
- **The evidence is qualitative.** Every experimental claim is read from a histogram, a heatmap or an arrow plot. There is no statistic against a null, and no count of pairs meeting a threshold.
- **LLM-generated inputs and tokenizer noise.** Several concepts' pairs and all intervention contexts were written by ChatGPT-4. Subword collisions add noise the authors say they "cannot" handle (App. C).
- **Separability is the authors' call,** and the orthogonality check tests the same judgement it assumes.

## Open questions

- Do the concept directions G of a real model satisfy GᵀCov(γ)⁻¹G ≈ diagonal? That is the testable content of Thm 3.4. The paper checks only one uncorrelatedness scatter plot (App. D.6).
- Is the non-orthogonality of non-separable concepts (the Fig. 3 blocks) mere correlation, or is it incompatibility in the quantum-logical sense? A test would look for order effects or failures of joint readout between the directions of a block. This is the experiment the prior-art map's diagnosis needs.
- Does any analogue of the causal inner product exist at intermediate layers? There the softmax symmetry is not the relevant one. [LIT-253](../literature.d/LIT-253.md)-style identifiability results for hidden layers would say.

## Corrections to the seeded skim

- Seeded from metadata; the text agrees with the seed's summary in substance. Two precisions. The evidence is not LLaMA-2 alone: App. D.2 (Fig. 9) adds a Gemma-2B heatmap comparison, in which the Euclidean product "doesn't capture semantics" and the causal one does. And the probing and steering connections are proved only for the final-layer context embedding λ(x) and the unembedding γ(y). The paper says it does not "address interpretability of either model parameters, nor the activations of intermediate layers" (§5).
- Venue verified: the v2 PDF carries "Proceedings of the 41st International Conference on Machine Learning, Vienna, Austria. PMLR 235, 2024". Authors and affiliation verified: Kiho Park, Yo Joong Choe, Victor Veitch, University of Chicago.
- Theorem 3.4 is weaker than both the paper's gloss and the anthology's summary make it. The theorem is one-directional. If a causal inner product M exists and d mutually causally separable concepts have canonical directions G forming a basis, then M⁻¹ = GGᵀ and GᵀCov(γ)⁻¹G = D. Two consequences follow, and the paper states neither.
  - *From Cov(γ) alone, (3.2) constrains nothing.* For every symmetric positive-definite M there is a G satisfying both equations: take G = LO, with LLᵀ = M⁻¹ and O diagonalising LᵀCov(γ)⁻¹L. So the paper's remark that the Euclidean product "is not a causal inner product if M = I_d does not satisfy (3.2) for any D" (§3.2) never bites against the covariance. M = I is satisfied by taking G to be the eigenvectors of Cov(γ). What rules out an inner product is knowledge of the actual concept directions G, not the covariance. I derived this and checked it numerically (d = 6, random covariance and random M; both equations hold to about 1e-15).
  - *Given G, M has no freedom.* M = (GGᵀ)⁻¹ is then fixed. The "d degrees of freedom" in choosing a causal inner product (§3.2) is a parameter count, not a property of either reading.
  - What does single out M = Cov(γ)⁻¹ is the stipulation D = I: every separable concept direction, whitened, has unit variance over the vocabulary. The paper says so ("We do not have a principle for picking out a unique choice of D").
- Anthology disagreements ([ADR-013](../decisions.d/ADR-013.md): reported, not fixed).
  - *"Exactly those" overstates Thm 3.4.* [ANTH-LIT-606](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-606.md) says "the causal inner products are exactly those with M⁻¹ = GGᵀ", and [ANTH-THEORY-090](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-090.md) says "one member of that family is the inverse unembedding covariance". Thm 3.4 is a necessary condition only, and "that family" is not identified from data (see the previous item).
  - *One quadruple, not four.* [ANTH-LIT-606](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-606.md) ("four quadruples (Fig 5, App D.4)") and [NOTE-328](NOTE-328.md)'s claim C5 ("four quadruples") say four quadruples. The text and figure axes show one quadruple, (king, queen, King, Queen), used for W = male⇒female and Z = lower⇒upper, on the 15 ChatGPT-4-written contexts of Table 4. Fig. 5 shows three intervening directions C, and Fig. 12 shows all 27 C against the same two log-ratios. The intervention evidence is therefore one quadruple, 27 directions and 15 contexts, plus the top-5 tables (Tables 1, 5 and 6).
  - *[NOTE-328](NOTE-328.md) omits two limits.* The counterfactual pairs for concepts 13, 17, 19 and 23–27 (Table 2) were generated by ChatGPT-4 (App. C), and App. C calls subword collisions "a lot of noise to our results". These bear on [NOTE-328](NOTE-328.md)'s C4.
  - *The rest agrees.* The rest of [NOTE-328](NOTE-328.md), [ANTH-LIT-606](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-606.md)'s summary, [ANTH-THEORY-090](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-090.md) and [ANTH-SOTA-378](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/practices.d/SOTA-378.md) agree with the text as I read it.
- Slips in the paper, none of which affects a result. In App. B.3 the second computation, (B.17)–(B.18), writes λᵀγ̄_Z where λᵀγ̄_W is meant. App. D.6 refers to "Assumption D.6" for Assumption 3.3. Assumption 3.3 is stated as independence, and footnote 3 says only uncorrelatedness is used.
