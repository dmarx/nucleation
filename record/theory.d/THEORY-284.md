---
number: 284
status: Active
formerly:
- THEORY-tmpsvlpi
title: "If a feature's values form a compact metric space carried continuously and injectively onto the unit sphere, and cosine similarity is locally a C² decreasing function of squared feature distance, then every path on the representation manifold is √(−2g′(0)) times as long as the feature path it images, so on-manifold shortest paths recover the feature's intrinsic length metric up to one scale; a homeomorphism alone does not fix it"
version: 2
history:
- version: 2
  date: '2026-10-20'
  note: >-
    Promoted, carrying out the promotion audit's decision for
    THEORY-284 (batch 051, ADR-047 v2). The dated note below
    re-derives Theorem 1 in both directions, so infinite and finite
    lengths correspond, and the shortest-path conclusion for the
    intrinsic length metric. That is the line-by-line check the
    promote_when asked for, and it shows the named counterexample
    cannot exist under the hypotheses. The title is unchanged.
tags:
- representation-learning
- mathematics
date: '2026-10-14'
source:
- LIT-935
summary: >-
  Modell, Rubin-Delanchy & Whiteley (2025), [LIT-935](../literature.d/LIT-935.md), Theorem 1, read in
  [NOTE-802](../notes.d/NOTE-802.md). Under Hypothesis 1 (continuous injective ϕ_f from a
  compact feature space to the sphere) and Hypothesis 2
  (CosSim = g(d²) locally, g ∈ C², g′(0) < 0), path lengths scale by
  √(−2g′(0)). So geodesics on the representation measure the feature,
  without knowing g. Both hypotheses are assumed, not derived from
  training. GPT-2's years are homeomorphic to both a linear and a
  logarithmic scale, and only the metric test told them apart.
answers:
- QUESTION-058
---
<!-- inactive-ok-file: THEORY-022 THEORY-019 CLAIM-135 CLAIM-193 — Proposed; accounts this one bears on -->

# THEORY-284: If a feature's values form a compact metric space carried continuously and injectively onto the unit sphere, and cosine similarity is locally a C² decreasing function of squared feature distance, then every path on the representation manifold is √(−2g′(0)) times as long as the feature path it images, so on-manifold shortest paths recover the feature's intrinsic length metric up to one scale; a homeomorphism alone does not fix it

## Source

Modell, Rubin-Delanchy and Whiteley (2025), [LIT-935](../literature.d/LIT-935.md), read in
[NOTE-802](../notes.d/NOTE-802.md): Definitions 1–2, Hypotheses 1–2, Proposition 1,
Theorem 1 with its proof and Lemma 1 (App. B), and the tests of §§2.3 and
3.1.

## What was actually shown

**The setting.** A feature is a compact metric space (Z_f, d_f). Its unit
representation direction is v_f(x) = ϕ_f(z_f(x)) on S^{D−1}.

**Proposition 1.** If ϕ_f is continuous and invertible (Hypothesis 1), it
is a homeomorphism onto its image M_f. So the representation has the
feature's topology: an interval gives a curve, a circle a loop, m points m
points.

**Theorem 1.** Suppose also that CosSim(ϕ_f(z), ϕ_f(z′)) = g_f(d_f(z, z′)²)
whenever d_f(z, z′) ≤ ε, with g_f ∈ C² and g_f′(0) < 0 (Hypothesis 2).
Then for every path η of finite length, L(ϕ_f ∘ η) = √(−2g_f′(0)) L(η).
The proof partitions the path finely. On unit vectors,
½‖γ_{t_i} − γ_{t_{i−1}}‖² = g(0) − g(d²) = −g′(0)d² − ½g″(c)d⁴, and
|α − β| ≤ |α² − β²|^{1/2} bounds each step's error by |g″(c)|^{1/2}d². The
summed error is at most C·L(η)·max d, which vanishes with the mesh.

What could have failed: locally reliable cosines might have recovered
geometry only up to a distortion that accumulates along a path. They do
not, because the error per step is of second order in the step.

**The tests.** These are the hypotheses checked on models, not the
theorem.
- GPT-2-small's years, rank along a neighbour graph: Kendall 0.97,
  Spearman above 0.99. That supports homeomorphism to an interval.
- Geodesic against |x − y| fails. Against log(2019 − year): ρ = 0.99,
  ξ = 0.84.
- Dates in a text-embedding model against the circular metric: ρ = 0.97.
- Colours: "weakly plausible".

## What this does not say

- **Not that models satisfy the hypotheses.** Both are posited. The
  paper's account of why manifolds curve (§2.4) is informal. Its tests are
  correlations on three features, after SAE extraction or projection onto
  a few principal components.
- **Not that the metric can be read off without a candidate.** Theorem 1
  makes the intrinsic geometry available in the representation. The paper
  tests it only against metrics it supplies by hand, and says this does
  not scale.
- **Not d_f itself.** What path length recovers is the length metric d_f
  induces. Where Z_f is not a length space, the chord metric of a circle
  for example, the representation recovers arc length instead. This is
  the record's precision; the paper states the theorem for path lengths
  and draws the shortest-path conclusion informally.
- **Not a group.** A loop comes back as a circle with arc length. Nothing
  says whether it carries ℤ/12, SO(2) or no action at all.
- **Not that topology fixes geometry.** The years example is the paper's
  own: linear and logarithmic scales are homeomorphic, and only the metric
  test separates them.

## Connections

- **[QUESTION-058](../questions.d/QUESTION-058.md).** Answers its "read off without supplying the group" in
  part, for topology and metric only, and only under the two hypotheses.
- **[THEORY-022](THEORY-022.md).** The months and weekdays it reads as 2-D irreducibles weave
  through a third principal component in Mistral 7B ([LIT-935](../literature.d/LIT-935.md), Fig. 2).
- **[THEORY-018](THEORY-018.md).** Hypothesis 2 presupposes an inner product. Where training
  fixes none, the theorem holds for the one the analyst picks, if its
  hypothesis holds for it.
- **[THEORY-019](THEORY-019.md).** Both make the same point from two sides. Degeneracy
  does not identify a symmetry, and geometry recovered here does not
  identify one either.
- **[CLAIM-135](../claims.d/CLAIM-135.md) and [CLAIM-193](../claims.d/CLAIM-193.md).** Identification up to a homeomorphism, then
  a scale, with the candidate space supplied by the analyst.

## Note of 2026-10-20: Theorem 1 and the shortest-path step, re-derived

Re-derived for the promotion audit (batch 051, [ADR-047](../decisions.d/ADR-047.md) v2), under
Hypotheses 1 and 2. Write c = √(−2g′(0)) > 0.

1. **One step.** For d = d_f(z, z′) ≤ ε, put u = ϕ(z) and v = ϕ(z′) on the
   unit sphere. A vector's cosine with itself is 1, so g(0) = 1, and
   ‖u − v‖² = 2(1 − g(d²)) = c²d² − g″(ξ)d⁴ for some ξ in (0, d²). With
   α = ‖u − v‖, β = cd and K = max |g″| on [0, ε²]: |α² − β²| ≤ Kd⁴, and
   since |α − β|² ≤ |α − β|(α + β), |α − β| ≤ √K·d².
2. **Paths.** For a path η and γ = ϕ ∘ η, refinement raises both sums of
   step lengths. Uniform continuity of η makes every step at most δ ≤ ε on
   fine partitions, and then |Σα_i − cΣd_i| ≤ √K·δ·Σd_i. Along common
   refinements of near-optimal partitions, with δ → 0, L(γ) = c·L(η) when
   L(η) is finite. When it is infinite, α_i ≥ cd_i − √K·d_i² ≥ (c/2)d_i
   for small steps, so L(γ) is infinite too.
3. **Shortest paths.** A continuous injection from a compact space into a
   Hausdorff one is a homeomorphism onto its image (Proposition 1). So every
   path in M_f is ϕ ∘ η for a path η in Z_f, and its length is c·L(η). The
   on-manifold geodesic distance is c times the length metric that d_f
   induces. That metric is d_f itself only on a length space, as the body
   says.
