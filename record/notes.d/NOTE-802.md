---
number: 802
status: Read
formerly:
- NOTE-tmpp9pxe
paper: LIT-935
title: 'Modell, Rubin-Delanchy and Whiteley — The Origins of Representation Manifolds in Large Language Models'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv PDF (arxiv.org/pdf/2505.18235, v1 of
    2025-05-23, the only version, 16 pp.), text extracted with pdftotext:
    §§1–4, the references, Appendix A (code) and Appendix B (definitions,
    the proof of Theorem 1 and Lemma 1). The proof was followed line by
    line. Figure contents were read from captions and the text, since the
    plots have no text layer; the colour correlations in Fig. 3 are not
    stated in the text and are not given here.
date: '2026-10-14'
summary: >-
  If a feature is a compact metric space mapped continuously and
  injectively onto the unit sphere (Hypothesis 1), its representation is
  homeomorphic to it. If, in addition, cosine similarity is locally a C²
  decreasing function g of squared feature distance (Hypothesis 2), every
  path on the representation manifold has √(−2g′(0)) times the length of
  the feature path it images (Theorem 1). The hypotheses are assumed, not
  derived; the tests supply a candidate metric and find homeomorphism for
  GPT-2's years but isometry only after a log rescaling.
---
<!-- inactive-ok-file: THEORY-022 CLAIM-135 CLAIM-193 — Proposed; the accounts this reading bears on, and the one filed from it -->

# NOTE-802: Modell, Rubin-Delanchy and Whiteley — The Origins of Representation Manifolds in Large Language Models

## Contribution

The paper models a feature as a metric space and a representation of it as
a map onto the unit sphere. Under two stated hypotheses it proves that the
representation manifold carries the feature's intrinsic geometry: path
lengths agree up to one constant. It then checks the hypotheses by eye and
by correlation on three features in two models, and finds that the
homeomorphism holds where the guessed metric fails.

## Key insight

Cosine similarity need not be a global distance for a representation to
encode geometry. If it is a smooth decreasing function of feature distance
only locally, the small steps add up: shortest paths along the manifold
measure the feature exactly, up to a unit. So the analyst should measure
geodesics on a neighbour graph, not raw cosines, and should expect the
embedding to curve through more dimensions than the feature's topology
needs.

## Assumptions

- **Multidimensional linear representation (Definition 1).**
  Ψ(x) = Σ_{f∈F(x)} ρ_f(x) v_f(x), with v_f(x) ∈ V_f and ‖v_f(x)‖₂ = 1.
  The results concern one feature's unit direction v_f(x), assumed already
  separated from the rest (in the experiments by an SAE or by the prompt).
- **A feature is a metric space (Z_f, d_f) (Definition 2)**, with Z_f
  compact throughout.
- **Hypothesis 1 (continuous correspondence).** There is a continuous
  invertible ϕ_f : Z_f → S^{D−1} with v_f(x) = ϕ_f(z_f(x)).
- **Hypothesis 2 (cosine similarity reflects distance).** There are g_f
  with continuous second derivative, g_f′(0) < 0, and ε > 0 such that
  CosSim(ϕ_f(z), ϕ_f(z′)) = g_f(d_f(z, z′)²) whenever d_f(z, z′) ≤ ε. So
  the local cosine depends on the pair only through their distance: the
  representation is locally homogeneous and isotropic in the feature.
- Both hypotheses are posited. Nothing in the paper derives them from
  training. The "origins" of the title are the informal argument of §2.4,
  not a theorem.

## Key results

- **Proposition 1.** Under Hypothesis 1, ϕ_f : Z_f → M_f is a
  homeomorphism. This is the standard fact that a continuous bijection
  from a compact space to a Hausdorff space has a continuous inverse.
  *Holds when:* Z_f is compact.
- **Theorem 1.** For a path η of finite length in Z_f and γ = ϕ_f ∘ η,
  L(γ) = √(−2g_f′(0)) · L(η). *Holds when:* Hypotheses 1 and 2. The proof
  (App. B) uses a fine partition, the expansion
  ½‖γ_{t_i} − γ_{t_{i−1}}‖² = −g′(0)d² − ½g″(c_i)d⁴, and Lemma 1,
  |α − β| ≤ |α² − β²|^{1/2}. Each step's error is at most |g″(c_i)|^{1/2}d²,
  and their sum vanishes as the mesh shrinks. The proof checks out.
- **What the theorem recovers.** It gives the length of paths, so the
  metric recovered is the intrinsic (length) metric induced by d_f, up to
  the scale √(−2g′(0)). This equals d_f only when Z_f is a length space,
  as an interval or a circle with arc length is.
- **Why the manifold curves (§2.4, informal).** If z ∈ [0, 1] must be
  linearly readable, an arc in a 2-plane suffices. If every polynomial of
  degree p must be linearly readable, ϕ_f(z) = Σ b_k(z)v_k with
  b_k ∝ z^{k−1} weaves through p + 2 dimensions. The authors offer this as
  "a sensible working hypothesis", not as a result.
- **Homeomorphism tests (§2.3).**
  - Text embeddings from OpenAI's text-embedding model (written
    "text-embedding-large-3"; 3,072-d) for colour names and for the
    365 dates. In 3-D PCA both lie on loops, with hues in colour-wheel
    order.
  - GPT-2-small layer-7 activations for the years 1900–1999, after Engels
    et al.'s SAE extraction and normalisation, form a curve. Rank along a
    K = 10 neighbour graph from 1900 against the year: Kendall 0.97,
    Spearman above 0.99.
  - Mistral 7B layer 8, months and weekdays as in Engels et al. (Fig. 2).
    The 3-D view shows the loops weaving through the third principal
    component, which the published 2-D view hides.
- **Isometry tests (§3.1).** Two diagnostics: cosine against squared
  distance (Chatterjee's ξ), and k-NN geodesic against feature distance
  (Pearson ρ).
  - Years with d = |x − y|: against isometry. Distances between recent
    years are stretched (Fig. 4).
  - Years with z = log(2019 − year): ξ = 0.84 and ρ = 0.99. Both
    candidates are homeomorphic to the data, so only the metric test
    separates them.
  - Dates with the circular metric: ρ = 0.97. Cosine departs from the
    metric at large distances, as Hypothesis 2 allows.
  - Colours with the hue circle: "weakly plausible".
  - For the text embeddings, isometry needed projection onto the first few
    uncentred principal components. The remaining components "often show
    clear structure".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Under Hypotheses 1–2, representation path length is √(−2g′(0)) times feature path length | strong | Theorem 1, proof in App. B |
| C2 | Under Hypothesis 1 alone, the representation is homeomorphic to the feature | strong | Proposition 1 |
| C3 | GPT-2's year representations are in temporal order along a curve | moderate | rank correlations 0.97 / >0.99, one model, one layer |
| C4 | GPT-2 encodes twentieth-century years on a logarithmic scale back from 2019 | weak | one candidate metric fitted after the linear one failed, ρ = 0.99 |
| C5 | Hypothesis 2 is plausible for dates, weakly for colours | weak | correlations on PCA-projected embeddings, figures only |
| C6 | Manifolds curve into extra dimensions so that more functions of the feature are linearly readable | weak | informal argument, §2.4 |

## Concepts

- **Feature.** A metric space (Z_f, d_f). Atomic: a singleton.
  Hierarchical: a finite set with a tree metric. Continuous: an interval,
  a circle, a region of ℝⁿ.
- **Representation manifold M_f.** The image ϕ_f(Z_f) on the sphere.
- **Path length L.** The supremum over partitions of summed distances, in
  d_f on Z_f and in the Euclidean norm on M_f.
- **Homeomorphism and isometry.** The two "levels of geometric fidelity"
  the tests separate. The first is topological; the second is metric up
  to scale.

## Connections

The paper extends Engels et al.'s multidimensional features ([LIT-322](../literature.d/LIT-322.md))
by relaxing their Definition 1 and re-plotting their months, weekdays and
years. It takes the metric-geometry definitions from Burago, Burago and
Ivanov. It positions a metric space between the Euclidean or hyperspherical
latents of identifiability theory and the group-structured manifolds of
disentanglement. It cites Olah and Batson's question of whether feature
manifolds are embedded so as to achieve a distance.

## Bearing on the record

- **[QUESTION-058](../questions.d/QUESTION-058.md)** asks how much of a representation's structure can be
  read off without supplying the group. The paper answers for the metric,
  not the group. Under Hypotheses 1–2 the intrinsic length metric is
  readable from the representation alone, by geodesics, up to scale.
  Nothing algebraic is recovered: a circle comes back as a loop with arc
  length, not as ℤ/12 or SO(2). The tests themselves supply a candidate
  metric. The authors call this "manual" and "clearly not scalable", and
  the years show why: homeomorphism did not distinguish a linear from a
  logarithmic scale. [LIT-935](../literature.d/LIT-935.md)'s filing note said the paper bears on
  how much structure can be read off "without supplying the group". That
  holds only for topology and metric, and only given the two hypotheses.
- **[THEORY-022](../theory.d/THEORY-022.md)** reads Engels et al.'s weekday and month circles as the
  real two-dimensional irreducibles of ℤ/7 and ℤ/12. Fig. 2 here shows the
  same Mistral 7B representations weaving through a third principal
  component. That is consistent with the extra frequency-2 and sign
  characters [THEORY-022](../theory.d/THEORY-022.md) reports for Llama months. It is not consistent
  with a single 2-D irreducible for each. [THEORY-022](../theory.d/THEORY-022.md) should note that the
  loop is not planar when viewed in 3-D. This is a qualification, not a
  refutation: [THEORY-022](../theory.d/THEORY-022.md) does not cite this paper.
- **[THEORY-018](../theory.d/THEORY-018.md)** holds that softmax training fixes no inner product on
  the final layer. Hypothesis 2 assumes that cosine similarity is
  meaningful, at least locally. The paper does not address which inner
  product; its tests use raw Euclidean cosines, on SAE outputs and on
  embeddings trained for cosine retrieval. So the theorem is a statement
  about whatever inner product the analyst picks, and its hypothesis is
  testable only for that choice.
- **[THEORY-175](../theory.d/THEORY-175.md)** concerns relative representations built from cosines.
  Theorem 1 says that only locally reliable cosines are needed to recover
  geometry, by integration along the manifold. It does not say anything
  about agreement across encoders.
- **[CLAIM-135](../claims.d/CLAIM-135.md) and [CLAIM-193](../claims.d/CLAIM-193.md).** Recovery here is identification
  up to stated ambiguities: a homeomorphism, then a global scale. The
  analyst supplies the candidate feature space, which is the "supplied by
  the analyst" clause of [CLAIM-193](../claims.d/CLAIM-193.md).
- **Filed from this reading:** [THEORY-284](../theory.d/THEORY-284.md), Theorem 1 with its
  hypotheses and its limit.
- The paper's suggestion of "manifold-aware" SAEs for steering is
  machine-learning practice and belongs to the anthology, not here.

## Limitations

- Both hypotheses are assumed. The paper offers no mechanism by which
  training would produce a continuous injective map or locally isotropic
  cosines.
- The empirical support is three features, two models plus one figure
  from a third, correlation coefficients, and figures. No null model is
  given for ρ or ξ.
- The metric is hypothesised by hand. The authors say a learned metric is
  unexplored, and that features like emotions may have no reasonable
  starting hypothesis.
- The k-NN geodesics are prone to short circuits. The authors say graphs
  often had to be pruned by hand.
- Isometry in the text embeddings needed a low-rank projection. The
  discarded components carry structure the authors cannot interpret.
- Feature separation is taken from Engels et al.'s SAE or from the prompt
  design. Hypothesis 1 is about v_f, not about the raw activation Ψ.

## Open questions

- A derivation of Hypothesis 2 from a training objective. For a circulant
  co-occurrence structure, the spectral account in [LIT-860](../literature.d/LIT-860.md) may supply
  one.
- A metric learned from the representation rather than supplied, with a
  statement of what it is identified up to.
- Whether the log-year metric survives another model, layer or SAE, or is
  a fit to one curve.
