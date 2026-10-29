---
status: Read
paper: 'LIT-tmpksoez'
title: 'Alvarez-Melis et al. — Structured optimal transport'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Read in full from the arXiv preprint 1712.06199v1 (17 December 2017,
    the only version), 24 pp. in a single-column preprint layout, fetched
    2026-10-29. The AISTATS 2018 proceedings version (PMLR 84, 1771–1780)
    was not compared. pdftotext reported a damaged cross-reference table
    and reconstructed it; the text came through whole. Extracted with
    `pdftotext -layout`; page numbers are the arXiv copy's. I read the
    abstract, §§1–6, Algorithms 1–4, Appendices A–H with the proof of
    Lemma 3.1, the captions of Figs. 1–6 and Table 1, and the reference
    list. The figures' images did not survive extraction. I checked
    numerically (numpy and scipy in a scratch environment; my own
    script): whether the threshold function of eq. (12) is concave and
    whether the cost it defines is submodular, by enumerating all
    diminishing-returns inequalities on a five-edge block; and whether
    d_F is symmetric when groups are defined on the source side only, by
    solving min over couplings of the Lovász extension as a linear
    program over all vertices of the base polytope on a 3 × 3 example.
date: '2026-10-29'
summary: >-
  Replaces the linear cost of discrete optimal transport by the Lovász
  extension of a submodular set function on assignments, so that the cost
  of a coupling depends on which assignments are made together. The
  problem stays convex and is a zero-sum game against cost matrices in
  the base polytope, solved by saddle-point mirror prox with Sinkhorn and
  base-polytope projections; it reduces to ordinary OT when the set
  function is modular. Its own example cost, eq. (12), is not concave, so
  the cost it defines is not submodular.
---

# NOTE-tmp42yyb: Alvarez-Melis et al. — Structured optimal transport

## Contribution

It lets the cost of a transport plan depend on combinations of
assignments, not on each assignment alone. A submodular set function F on
the set of source–target pairs encodes which assignments are cheaper
together, for example all the mass of one labelled group going to one
region. Its Lovász extension f gives a convex cost on couplings. The
problem min_γ f(γ) is shown to be a convex–concave game against costs in
the base polytope of F. The paper gives subgradient, saddle-point mirror
descent and mirror-prox solvers with an O(m log m) projection for
concave-of-sum group functions. Experiments: clustered point matching,
colour transfer, MNIST↔USPS adaptation from 100 samples, and a
syntax-aware word mover's distance.

## Key insight

Ordinary OT is linear in the coupling, so every assignment is paid for
independently: the cost "is linear in the mappings γij , γkl of separate
source locations i, k; the mappings are counted independently" (footnote
1, p. 2). Correlated assignments "cannot be induced by standard
formulations of optimal transport whose cost is separable in the mapping
variables; they require nonlinearities" (p. 2). Submodularity is the
nonlinearity that keeps the problem convex. The adversary's base polytope
B_F is a single point, the ground cost, exactly when F is modular, and it
grows as F becomes "more submodular" (p. 7).

## Assumptions

- **Discrete measures** with a ground cost matrix C ∈ ℝ^{n×m} (p. 3).
- **F submodular on 2^{U×V}** (§3, pp. 4–5), so that its Lovász extension is
  convex and equals the support function of B_F (eqs. 8–9, p. 4). For Lemma
  3.1 also F(∅) = 0, F non-decreasing, and F({(i, j)}) > 0 iff C(x_i, y_j) >
  0 (p. 6).
- **Groups supplied in advance.** The example costs (eqs. 10–11, p. 5)
  need a partition of the assignments into blocks E_kl = U_k × V_l. The
  experiments take it from source class labels, superpixels or n-grams.
  The structure is an input, not something the method finds.
- **Concave g.** Eq. (11) requires "scalar monotone increasing concave
  functions" g_kl (p. 5).

## Key results

- **Problem (13), p. 6:** min_{γ ∈ M} f(γ) = min_{γ ∈ M} max_{κ ∈ B_F} ⟨γ, κ⟩.
  It is convex, and its discrete version "is hard to even solve
  approximately" (p. 6). A saddle point exists since M and B_F are
  nonempty compact polytopes (pp. 6–7).
- **Lemma 3.1 (p. 6; proof p. 18):** under the conditions above,
  d_F(µ, ν) = min_γ f(γ) "is a semi-metric". The proof shows d_F ≥ 0, d_F =
  0 when µ = ν, and the converse by a short contradiction. It then says
  "the symmetry of d F (µ, ν) is trivial" (p. 18). It is not trivial: F is
  a function on ordered pairs (source, target), and the paper's own
  domain-adaptation F uses source labels only. In my 3 × 3 example with the
  square-root cost on source groups, d_F(µ, ν) = 0.574. Swapping the roles
  and carrying the groups to the other side gives the same value. Swapping
  the roles with no groups on the new source side, as the paper's setup
  would, gives 0.759. Symmetry holds only if F is built symmetrically. The
  triangle inequality is not claimed.
- **Reduction (p. 7):** if F is modular, "the base polytope collapses to a
  single point", the ground cost, and the problem is ordinary OT.
- **Algorithms (§4, pp. 8–10):** Edmonds' greedy algorithm gives
  subgradients in O(N log N), N = nm. KL projection onto M is Sinkhorn.
  Euclidean projection onto B_F is a min-norm-point problem, O(m log m) for
  concave-of-sum blocks (App. D). Rates: O(1/√t) for mirror descent, O(1/t)
  for mirror prox (p. 9).
- **Experiments (§5, pp. 10–13).** MNIST→USPS with 100 samples per domain
  and source labels only: 62.97% against 57.12% for group-lasso OT and
  55.70% for entropic OT. USPS→MNIST: 58.34% against 49.49% (Table 1, p.
  13). SICK sentence similarity on 100 sentences: MSE 0.59, ρ = .75,
  against WMD's 0.67 and .71 (p. 13). One run each, no error bars.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | OT with the Lovász extension of a submodular cost is a convex problem and a zero-sum game against costs in the base polytope, reducing to OT when the cost is modular | strong | standard submodular analysis, eqs. (8)–(9), (13), pp. 4–7 |
| C2 | d_F is a semi-metric under Lemma 3.1's conditions | moderate | proof p. 18 shows non-negativity and identity of indiscernibles; symmetry is asserted and fails for one-sided F |
| C3 | The example cost of eqs. (11)–(12) is submodular | wrong | g of eq. (12) is not concave at x = α; 84 of 405 diminishing-returns inequalities fail in my enumeration |
| C4 | Mirror prox converges at O(1/t), with cheap projections for concave-of-sum blocks | strong | cited saddle-point theory; App. D algorithm |
| C5 | Structured OT improves unsupervised adaptation and sentence similarity over unstructured and group-regularized OT | weak | one run per setting, 100 samples, no variance (Table 1; p. 13) |

## Method

Algorithm 2 (p. 10), saddle-point mirror prox: alternately take a mirror
step for γ (multiply by e^{−ηκ}, Sinkhorn-project onto M) and a Euclidean
step for κ (add ηγ, project onto B_F), first at the current point and then
at the extrapolated one. Average the iterates and stop on the saddle-point
gap. Initialization γ₀ = µνᵀ, κ₀ the projection of C onto B_F (p. 10).

The threshold function is wrong as printed. Eq. (12), "gkl ( x ) = min{ x,
α} + [ x − α]+" with the square root over the bracket (the experiments call
it "square-root thresholding", p. 11), has slope 1 just below α and slope
1/(2√(x − α)), unbounded, just above it. It is convex at α, not concave.
With α = 1, g(0.9) = 0.9, g(1) = 1 and g(1.1) = 1.316, so g(1) is below the
chord's 1.108. And g(x) > x on (α, α + 1): it charges extra just past the
threshold instead of discounting. In my enumeration on one block of five
edges with costs in [0.2, 0.8], 84 of the 405 diminishing-returns
inequalities failed. With g = √x none failed. With a nonsubmodular F the
Lovász extension is not convex and not the support function of B_F, so the
convexity, the saddle-point equivalence and the min-norm projection all
lose their footing for the costs the experiments say they used. A version
with g concave (√x, or a concave function past the threshold) would
restore them. Whether the reported numbers came from the printed g is not
recoverable from the paper.

Other slips: eq. (8) sums over i with summands in j (p. 4); §4.3.1 says the
mirror-descent iteration needs a "KL-projection onto the base polytope"
where the KL projection is onto M (p. 9); Algorithm 3's input line is
copied from Algorithm 2 (p. 21); Appendix G compares (a) with (b) twice
where (a) and (c) is meant (p. 23).

## Concepts

- **Submodular cost on assignments** — F: 2^{U×V} → ℝ with diminishing
  returns (eq. 7). An assignment costs less when compatible assignments are
  already made.
- **Lovász extension** — the convex extension f of F to nonnegative vectors,
  f(w) = max_{x ∈ B_F} wᵀx (eqs. 8–9).
- **Base polytope B_F** — {y : y(V) = F(V), y(A) ≤ F(A) for all A}. In the
  game it is the adversary's set of cost matrices (p. 7).
- **Concave-of-sum group function** — F_kl(S) = g_kl(Σ_{(u,v) ∈ S ∩ E_kl}
  C_uv) (eq. 11).

## Connections

- **Courty et al. 2017** group-lasso and Laplacian-regularized OT are the
  baselines. The paper's difference is that structure modifies the cost
  itself, with no regularization weight (p. 7).
- **Cuturi 2013** Sinkhorn for the coupling projection; **Bach 2013** and
  **Lovász 1983** for the submodular geometry; **Juditsky and Nemirovski
  2011** for the saddle-point methods.
- **Kusner et al. 2015** word mover's distance.
- Cited by FGW ([LIT-tmpjs7kp](../literature.d/LIT-tmpjs7kp.md)) as an approach that needs "a known and simple
  structure such as class clusters" (p. 2 there).

## Bearing on the record

- **[QUESTION-283](../questions.d/QUESTION-283.md) (higher-order structure).** This is a case where the
  vocabulary of a transport problem is enriched from pairwise to set-wise.
  The cost of a coupling is no longer a sum over single assignments. A
  block's cost g(Σ C) depends on all its assignments together, and no
  sum of per-assignment or per-pair costs reproduces it when g is
  strictly concave. Three points bear on the question's separations. First,
  the richer vocabulary is chosen by the modeller, from groups known in
  advance; nothing in the method discovers that a higher-order relation is
  needed. Second, tractability forces the kind of higher-order relation:
  submodular (economies of grouping), with no complementarity or penalty
  for co-occurrence. "discourage some combinations of assignments" (p. 4)
  would be supermodular and non-convex, and the paper does not treat it,
  though it notes that "any convex function with bounded closed gradient
  maps would work" (p. 14). Third, the relations are among assignments
  between two objects, not among the cues within one. A6's use, pragmatic
  force resting on a configuration of cues, is a relation of the second
  kind. SOT can encode it only as a grouping of the cues fixed in advance,
  whose joint mapping is cheaper. It cannot learn a ternary relation of cue
  values. The "Why this is here" sentence, "The test would be behavioural
  prediction, not expressiveness", is consistent with that: the paper shows
  only that grouped couplings help one prediction task each.
- **[CASE-tmph0fxi](../cases.d/CASE-tmph0fxi.md).** None directly. If the correspondence arm wanted
  utterances of one act to move together, a source-side group function
  would encode it, at the cost of making the measure asymmetric (Lemma 3.1
  above).
- **Instruction for ML practice.** Domain adaptation and sentence
  similarity results are method claims for the Anthology of the SOTA
  (`anthology-candidate` on the LIT).

## Limitations

- **The printed example cost is not submodular** (above). The convexity
  results apply to the framework, not demonstrably to the experiments.
- **Symmetry of d_F is asserted, not shown**, and fails for one-sided group
  functions. No triangle inequality is claimed.
- **Structure must be given.** Groups come from labels, segmentations or
  n-grams.
- **Small experiments without variance**: 100 samples, one run, no
  significance tests.
- **arXiv v1 only.** The AISTATS version may differ.

## Open questions

- Is there a tractable class of supermodular or mixed set costs on
  assignments, so that co-occurrences can be penalized as well as
  rewarded?
- Can the grouping itself be fitted, for example by choosing among
  candidate partitions by held-out prediction? That would turn SOT into a
  test of [QUESTION-283](../questions.d/QUESTION-283.md)'s "forced by the composite or by the class".
