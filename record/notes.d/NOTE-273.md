---
number: 273
status: Read
formerly:
- NOTE-tmp2j21t
paper: LIT-322
title: 'Not All Language Model Features Are One-Dimensionally Linear'
version: 1
history:
- version: 1
  date: '2026-09-29'
  note: >-
    Read in full (The full text of arXiv 2405.14860 v3 (27 Feb 2025, headed
    "Published as a conference paper at ICLR 2025"), from the arXiv PDF, 32
    pp. I read the abstract, §§1–6 with Limitations, the references, and
    Appendices A–K: - A: capacity theorem with Lemma 1 and proofs. - B:
    reducibility intuition and the estimators. - C: alternative
    intervention-based and group-theoretic definitions. - D: SAEs on
    synthetic circles. - E: Mistral SAE training. - F: clustering algorithms
    and sensitivity. - G: other clusters. - H: assets and error bars. - I:
    per-problem results, Tables 2–3. - J: patching. - K: Explanation via
    Regression, with Figs 23–25. Nothing was skipped. Most figures are PCA
    scatter plots and bar or line plots that survive only as labels, so
    their content is taken from captions and text. Table 4 (attention heads)
    survives only as headers, and I give none of its values. Superscripts
    are lost in extraction ("216 dictionary elements" is 2¹⁶ = 65,536, as
    App. E states).). The first NOTE on this paper, which was seeded from
    its abstract alone.
date: '2026-09-29'
summary: >-
  Defines a feature as irreducibly multi-dimensional when no rotation and
  translation makes its distribution either a product of independent parts
  (separable) or a mixture with a lower-dimensional component (Def. 2).
  Softened versions are the separability index S(f) and the ε-mixture
  index M_ε(f) (Def. 3). Clustering sparse-autoencoder dictionary elements
  by cosine similarity then finds circular representations of weekdays and
  months in GPT-2 (also 20th-century years) and in Mistral 7B. Replacing
  the circle coordinates at the day or month token causally changes the
  answer on "N days/months from X" prompts in Mistral 7B and Llama 3 8B,
  and in early layers the circle patch nearly matches patching the whole
  layer. The models' task accuracy is modest on weekdays (29/49 Llama,
  31/49 Mistral), high on months (143/144, 125/144), and near-trivial for
  GPT-2 despite its circles.
---

# NOTE-273: Not All Language Model Features Are One-Dimensionally Linear

## Contribution

The linear representation hypothesis, as the paper states it, has two parts (§1). All representations lie along one-dimensional lines (Park et al., [LIT-304](../literature.d/LIT-304.md)), and states are sparse sums of them (Elhage et al., [LIT-323](../literature.d/LIT-323.md)). The paper disputes the first part and generalises the second. Some features are irreducibly multi-dimensional, and hidden states are sums of low-dimensional irreducible features in δ-orthogonal subspaces (Hypothesis 2). It supplies three things:

- a statistical definition of irreducibility, with two estimators (§3, App. B);
- an SAE-clustering procedure that finds candidates (§4);
- the first causal evidence, the authors claim, that an LLM computes with a circular representation of a latent concept, days and months in modular-arithmetic prompts (§5).

## Key insight

A feature is a *subspace-valued* object, not a direction. It is genuinely multi-dimensional when its distribution in that subspace fills it: it is neither concentrated on lower-dimensional pieces (a mixture) nor a product of independent coordinates (separable). A circle does both jobs, because it is filled but not a product. A sparse autoencoder trying to reconstruct such a feature sparsely will tile it with many near-parallel dictionary elements, so the feature shows up as a *cluster* of high-cosine dictionary elements rather than as one latent.

## Assumptions

- **What a feature is.** A d_f-dimensional feature is a function from a subset of inputs (where it is "active") into R^{d_f} (Def. 1).
- **Reducibility is relative to rigid motions.** Def. 2 allows only f ↦ Rf + c with R *orthonormal*.
  - *Separable:* the transformed distribution factorises, p(a, b) = p(a)p(b).
  - *Mixture:* p(a, b) = w p(a)δ(b) + (1 − w)p(a, b), with the components on disjoint supports.
- **Softened indices (Def. 3).**
  - *Separability:* S(f) = min over rotations of I(a; b), estimated in 2-D over 1,000 angles on a 40 × 40 histogram of data normalised and clipped to a 6 × 6 square.
  - *Mixture:* M_ε(f) = max over v, c of P(|v·f + c| < ε·√E[(v·f + c)²]), with ε = 0.1, maximised by gradient descent on a sigmoid-softened indicator.
  - *In practice:* both are computed on 2-D PCA projections of each cluster's reconstruction (planes 1–2, 2–3, 3–4, 4–5) and averaged.
- **Hypothesis 2.** x = Σ Vᵢfᵢ(t), with the Vᵢ pairwise δ-orthogonal (|x₁·x₂| ≤ δ for unit vectors in the two column spaces, Def. 4).
- **SAE setup.**
  - *GPT-2:* layer-7 SAEs from Bloom (2024), about 25k features, spectral clustering into 1,000 clusters, about 500 inspected by eye.
  - *Mistral 7B:* SAEs trained by the authors on layers 8, 16 and 24, 65,536 elements each, on over a billion tokens of the Pile and Alpaca, with an L^{1/2} penalty. Graph clustering by top-2 neighbours and a cosine threshold of 0.5 gives about 2,700 clusters, about 2,000 inspected (App. E, F).
- **Task prompts.** "Let's do some day of the week math. Two days from Monday is" (49 prompts) and the months analogue (144 prompts). Accuracy is by highest valid-token logit.

## Key results

- **Circles found (Fig. 1, Fig. 15).**
  - *GPT-2 layer 7:* weekdays, months and 20th-century years lie on circles in PCA planes 2–3 (3–4 for years). PCA 1 is an "intensity" direction, so the shape is "perhaps best thought of as a cone".
  - *Mistral layer 8:* weekdays and months, with extra points: a "weekend" between Saturday and Sunday, and seasons between their months.
  - *Automatic ranking:* by the product (1 − M_ε)·S, the Fig. 1 clusters rank 9, 28 and 15 of 1,000 (alternative ranking 8, 105, 12). Weekdays show M_ε = 0.475 and S = 0.951 bits (Fig. 2).
  - *The authors' own caveat:* "we did not find other obviously interesting and clearly irreducible features" in Mistral (App. F.2).
- **Task accuracy (Table 1).** Llama 3 8B scores 29/49 on weekdays and 143/144 on months. Mistral 7B scores 31/49 and 125/144. GPT-2 scores 8/49 and 10/144.
- **Circular representations of α on the task (Fig. 4, Fig. 18).** The top two PCA components at the α token are circular in many, not all, layers of both models.
- **Circle patching (§5.1, eqs 5–6, Fig. 6).**
  - *Probe:* fit a linear probe P from the top-5 PCA subspace to circle(α) = (cos 2πα/m, sin 2πα/m).
  - *Patch:* replace the circle coordinate with that of a different α′, and mean-ablate the rest of the layer.
  - *Scale:* 294 weekday and 1,584 month patchings, with 96% error bars.
  - *Result:* in early layers the circle patch nearly equals patching the whole layer, and usually beats patching the top-5 PCA subspace. The effect drops at layers 15–17, where α is copied to the final token (App. J).
- **Angle, not radius (Fig. 7).** Sweeping (r, θ) inside the circle at Mistral layer 5 changes the predicted day according to θ. "Mistral treats the circle as a multi-dimensional representation with α encoded in the angle."
- **The SAE-found plane works too (§5.2, Fig. 8).**
  - *At layer 8:* the SAE probe gives an average logit difference of −2.01, against −2.58 for the fitted circular probe.
  - *Across layers:* it transfers better. At layer 6 the layer-8 SAE probe gives −2.32, against 0.029 for the layer-8 circular probe.
- **Continuity (§5.3, Figs 9, 22).** At Mistral layer 30, "very early/very late on X" and "morning/evening on X" project between X and its neighbours on the weekday circle.
- **The answer γ is also circular (App. K).** After regressing out one-hot α and β ("Explanation via Regression", EVR), the layer-25 residual in Mistral weekdays is "an incredibly clear circle in γ" (Fig. 23). EVR on Llama months adds a second-harmonic circle ("circle 2γ") and a "γ parity" term (Fig. 25). Attention heads do not compute γ; MLPs after the copy do (App. J).
- **Capacity (App. A, Thm 1).** From Johnson–Lindenstrauss and Alon, (1/d_max)·e^{C₁(d/d_max²)δ²} pairwise δ-orthogonal subspaces of dimension ≤ d_max fit in R^d, and at most e^{C(d − d_max)δ² log(1/δ)} (the proof's form). The authors note "a large exponential gap" between the bounds.
- **Synthetic check (App. D).** Two circles in orthogonal planes of R¹⁰: an m = 64 SAE's live elements align with the two planes, and spectral clustering recovers each circle "almost exactly".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Irreducibility can be defined statistically as "not separable and not a mixture under any rigid motion" | definition | Def. 2; softened in Def. 3; the indices are heuristic estimators (App. B.2) |
| C2 | Clustering SAE dictionary elements recovers irreducible multi-dimensional features | moderate | synthetic success (App. D); in real models the known circles are recovered, but the score ranks them 9th–28th and discovery was by manual inspection |
| C3 | GPT-2 and Mistral 7B contain circular representations of weekdays and months (and GPT-2 of years) | strong (observation) | PCA of cluster reconstructions (Figs 1, 14, 15) and of task activations (Figs 4, 18, 19) |
| C4 | Mistral 7B and Llama 3 8B use these circles causally on the day and month tasks | strong (experiment), for these tasks | subspace patching with mean ablation, 294 + 1,584 patchings, error bars, three baselines (Fig. 6) |
| C5 | The value is carried by the angle | moderate | off-distribution sweep at one layer of one model (Fig. 7) |
| C6 | The SAE-found plane is a more robust intervention target than a fitted probe | weak–moderate | one model, one task, layers 6–10 (Fig. 8) |
| C7 | The circular feature is continuous in time | weak–moderate | two synthetic prompt families, one layer, visual (Figs 9, 22) |
| C8 | These circles are "the fundamental unit of computation" for these tasks (abstract) | weak–moderate | C4 shows they are sufficient to steer the answer at early layers; necessity and the downstream algorithm (App. K suggests "clock" or "pizza") are not shown |
| C9 | "We are the first to find causal circular representations of concepts in a language model" | assertion | §1.1, qualified against GPT-2 position helices and Hanna et al. in §2 |
| C10 | Exponentially many low-dimensional δ-orthogonal subspaces fit in R^d | strong (proof) | App. A, Thm 1 (statement garbled; proof as given) |
| C11 | Their definition matches group-theoretic irreducibility for finite-group multiplication tasks | weak (assertion) | App. C, one sentence, no proof; it speaks of "reducibility into a tensor product representation", whereas reducibility of a group representation is a direct-sum decomposition |

## Method

1. Train or take residual-stream SAEs.
2. Cluster dictionary elements by cosine similarity (spectral clustering for GPT-2; top-k graph plus threshold for Mistral).
3. For each cluster, reconstruct each activation from that cluster's latents alone, keeping points where any is active.
4. PCA the reconstructions and inspect them, or score them with S(f) and M_ε(f).
5. For candidate circles, design tasks, and test causality by subspace patching.
6. Explain later-layer states with EVR, a greedy regression on interpretable functions of the inputs (one-hot α and β, circle(γ), and so on).

## Concepts

- **Irreducible feature** — not separable and not a mixture under any orthonormal-plus-translation change of coordinates (Def. 2).
- **Separability index S(f)** — minimum mutual information between the two coordinate blocks over rotations (Def. 3).
- **ε-mixture index M_ε(f)** — the largest fraction of the feature's distribution that some normalised linear functional puts within ε of zero (Def. 3).
- **δ-orthogonal matrices** — column spaces whose unit vectors have |dot product| ≤ δ (Def. 4).
- **Multi-dimensional superposition hypothesis** — states are sums of many sparse, low-dimensional irreducible features in pairwise δ-orthogonal subspaces (Hypothesis 2).
- **Explanation via Regression (EVR)** — iteratively regress hidden states on hand-built functions of the inputs and inspect the residuals (App. K).

## Connections

- **[LIT-323](../literature.d/LIT-323.md) (Toy Models of Superposition).** Hypothesis 1 here is a paraphrase of its superposition hypothesis, and Hypothesis 2 generalises it from directions to subspaces. [LIT-323](../literature.d/LIT-323.md) itself defers multi-dimensional features to an appendix, "What about Multidimensional Features?", that is referenced but absent from both the arXiv PDF and the HTML I read (see the reading of [LIT-323](../literature.d/LIT-323.md)). This paper is, in effect, that missing appendix done empirically.
- **[LIT-304](../literature.d/LIT-304.md) (Park et al.).** Cited as the statement of the one-dimensional LRH being disputed. This is my inference, not the paper's. A cyclic concept like "next weekday" cannot have an embedding direction in Park et al.'s sense. The differences Monday→Tuesday, Tuesday→Wednesday, … are distinct chords of a circle, not members of one cone. Park et al.'s definitions are for the unembedding and final-layer context spaces, while these circles are in intermediate residual streams, so this is an analogy across layers, not a contradiction of a theorem.
- **[LIT-267](../literature.d/LIT-267.md) (Xiong) and [NOTE-240](NOTE-240.md).** [NOTE-240](NOTE-240.md) records that Xiong's only named limitation (App. D) is "non-linear features (Engels et al.)". Here is what that limitation amounts to, which is my reading. Each day is a vertex of a convex heptagon, so each is cut off by a half-space. A thresholded-probe incidence of the kind Xiong builds could still classify days. But the structure the model computes with, succession mod 7, is a group action on the circle. It is not a meet or join, and it is invisible to a concept lattice. Xiong's lattice would see seven atoms and none of the arithmetic.

## Bearing on the record

- **What it supplies for the prior-art map's role (§5, "scooped again?" item 3).** The map lists "Engels-style non-linear features" among the groups who "could reach the 'sectors = block structure / irrep multiplets' prediction (#6, [#7](https://github.com/dmarx/nucleation/issues/7)) empirically before you". Having read it:
  - *It already contains the germ of [#7](https://github.com/dmarx/nucleation/issues/7), for cyclic groups.* The weekday circle, (cos 2πα/7, sin 2πα/7), is exactly the two-dimensional real irreducible representation of Z/7 at frequency 1. Complexified, it is the conjugate character pair χ₁, χ₋₁. EVR's regressors for Llama months, "circle 2γ" and "γ parity", are the frequency-2 and frequency-6 (sign) characters of Z/12 (Fig. 25). So the paper already regresses LLM hidden states on characters of a cyclic group, and finds a feature that *is* a real irrep. It does not say so in those words: "irreducible" in Def. 2 is statistical. App. C's group-theoretic definition is asserted without proof, and it misdescribes reducibility as tensor-product rather than direct-sum. This is my reading.
  - *It does not reach what the map claims as new.* There is no spectral-degeneracy diagnostic, no operator algebra, no centre or block-diagonalisation, and no discovery of symmetry from spectra. The symmetry is assumed from the task (mod 7, mod 12) and fitted, not detected.
  - *The scoop risk is therefore real but narrow.* A response should cite this paper as having found the cyclic-group case empirically, and position [#7](https://github.com/dmarx/nucleation/issues/7) as the general *detection* method (degeneracy without a known group), with this paper's circles as the first test case. The circles are the natural validation target: a degeneracy-based method should rediscover them unsupervised.
- **The map's #5–#6 (types as sectors, block-diagonalisation).** Hypothesis 2, sums of features in nearly orthogonal subspaces, and the mixture half of Def. 2, components on disjoint supports, are the nearest things here to a sector decomposition: a direct sum of subspaces with no co-activation across them. This is my analogy, not the paper's. It is statistical (supports and independence), not algebraic (a commutant or centre). It is the empirical neighbour a referee will name for #6.
- **[THEORY-017](../theory.d/THEORY-017.md) (basis and unitary invariance).** The separability half of Def. 2 is defined up to *rotations* only, with orthonormal R. So irreducibility here is relative to the residual stream's Euclidean inner product, which [THEORY-017](../theory.d/THEORY-017.md) would call supplied structure, and [LIT-304](../literature.d/LIT-304.md)'s §3 shows is not fixed by the output objective. The mixture index, which maximises over all v, is invariant under any invertible linear reparametrisation. The separability index is not. The SAE clustering (cosine similarity) and Hypothesis 2's δ-orthogonality are Euclidean too. For a continuous circle, *non-separability* survives any invertible linear map, because the support is an ellipse, which is not a product set. It survives for the discrete 7-gon and 12-gon too, since their vertices lie on a conic and a grid's do not. That argument is mine, not the paper's. For other candidate features the dependence on the inner product is unexamined. This is a genuine instance of [THEORY-017](../theory.d/THEORY-017.md)'s point in an ML setting, and worth a line there if the owner adds an ML row.
- **ML practice (anthology-candidate).** Yes, a candidate for the Anthology of the SOTA. It carries an instruction for interpretability practice: before treating individual SAE latents as the units of a circuit, check whether high-cosine clusters of latents jointly span an irreducible multi-dimensional feature, and intervene on the cluster's subspace, not on single latents. §6 raises exactly this, whether "individual SAE features are appropriate 'mediators'". The evidence is two tasks, so it would enter at a provisional status. The anthology does not hold it; its "Engels" hit is co-authorship of [ANTH-LIT-568](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-568.md), per the seed.
- **For filing.** Tags: `representation-learning` first, `anthology-candidate` second, as seeded. Also defensible: `mathematics`, for the capacity theorem and the reducibility definitions.

## Limitations

- **Few features found.** Only days, months and years were found, and the authors do not know why no more (§6). Discovery was mostly by inspecting about 2,500 clusters by eye. The automatic score does not single the circles out.
- **The definitions are purely statistical.** They are "not intervention based", and they had to be softened into indices that return "a possibly subjective 'degree' of reducibility" (§6). The indices are computed only on 2-D PCA planes. Taken exactly, Def. 2 would class the discrete weekday and month point sets as mixtures (see Corrections), so their irreducibility rests entirely on the choice ε = 0.1.
- **Narrow tasks.** Two templated task families. Modest weekday accuracy, trivial accuracy on plain modular prompts, and GPT-2's circles unused. This shows that circles are used on these templates, not that they are the general mechanism for cyclic reasoning.
- **The downstream algorithm is only suggested.** "Clock" or "pizza" is proposed from EVR residuals and not established.
- **The capacity theorem's bounds are exponentially far apart,** and the theorem is stated imprecisely.

## Open questions

- Would an unsupervised symmetry detector, spectral degeneracy of a concept operator or equivariance under a learned group action, rediscover the weekday and month circles without the task telling it the group is Z/7 or Z/12? This is the test that separates the prior-art map's [#7](https://github.com/dmarx/nucleation/issues/7) from this paper.
- Do irreducible features of dimension > 2 exist, as the authors suspect (§6)? What would a representation-theoretic, not statistical, definition of reducibility find in the same SAE clusters?
- Is the separability index stable under a whitening such as [LIT-304](../literature.d/LIT-304.md)'s causal inner product, or do some clusters' irreducibility depend on the Euclidean metric?

## Corrections to the seeded skim

- Seeded from metadata. The seed's summary holds, with three precisions.
  - *Two tasks, modest on one.* "These circles are used to solve modular-arithmetic tasks" is shown on two templated tasks (49 weekday and 144 month prompts). Weekday accuracy is modest (Table 1), and both models "get trivial accuracy on plain modular addition prompts, e.g. '5 + 3 (mod 7) ≡'".
  - *The intervention evidence is Mistral 7B and Llama 3 8B,* not GPT-2. GPT-2 has the circles but gets 8/49 and 10/144.
  - *Two layers of discovery.* The multi-dimensional features were *discovered* in GPT-2 (layer 7) and Mistral 7B (layer 8). Their *use* is shown in Mistral and Llama 3 8B.
- Venue resolved: the v3 PDF is headed "Published as a conference paper at ICLR 2025". The seed's "(a later conference venue is unverified here)" and its identification note can be settled as ICLR 2025, from the PDF header. The title change the seed notes is confirmed by the text's own footnote 1. "Non-linear" in the v1 title meant "not one-dimensional". The features are "linear in the sense that they are contained in a low-dimensional linear subspace".
- Slips in the text. None changes a result.
  - *Theorem 1 (App. A)* states the upper bound as e^{C₂(d − d_max δ log(1/δ))}. The proof gives e^{C(d − d_max)δ² log(1/δ)}. It also writes d′ where the proof uses d_max, and Aᵢ ∈ R^{nᵢ×d′} for what are d × nᵢ matrices.
  - *§5.1 metric.* It defines the metric as a logit difference "between the original correct token (α_j) and the target token (α_j′)", where γ is meant.
  - *Fig. 7's text.* It lists β ∈ [2, 3, 45] for durations 2–5.
  - *Def. 7 (App. C)* quantifies "for all j, j′" over a condition that mentions only j.
  - *§3.2* calls Hypothesis 2 "a stricter version of Hypothesis 1". As stated it is a generalisation (d_f = 1 recovers Hypothesis 1), and the independence between features that the prose says it adds does not appear in the displayed hypothesis.
- A consequence of Def. 2 the paper does not state, which is my observation. Taken exactly, the mixture clause makes *every finitely supported feature reducible*. Take any line through one support point: the points on it form a w·p(a)δ(b) component, and the rest have disjoint support. The weekday and month features are, by the paper's own account, "mostly discontinuous … clustered at the vertices of a heptagon and dodecagon" (§5.3). So under Def. 2 as written they are mixtures. They count as irreducible only by degree, through the softened M_ε with ε = 0.1. The paper notes that continuity "would further decrease the ε-mixture index", but not that exact Def. 2 excludes its own headline examples.
