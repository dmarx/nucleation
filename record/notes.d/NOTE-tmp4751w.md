---
status: Read
paper: 'LIT-tmpocqly'
title: 'Hyperbolic Representation Learning: Revisiting and Advancing'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the arXiv PDF of v1 (arXiv:2306.09118, 15 June 2023,
    21 pages; the ICML 2023 camera-ready, PMLR 202:39639–39659), text
    extracted with pdftotext. Sections 1–6 and Appendices A–H read:
    every equation, both theorems and the proof of Theorem 4.2 followed.
    Theorem 4.1's proof is a citation to Shimizu et al. (2020) and Law et
    al. (2019), neither of which was read. Figures 2, 4, 6 and 7 read from
    their captions, the inset statistics (ROOT/HC, MIN, MEAN, MAX) and the
    text; the histogram shapes are taken from the authors' descriptions.
    Tables 1–5 and 7–10 read from the extracted text, where column
    alignment had to be reconstructed by hand. The OpenReview discussion
    and the cited prior work were not read.
date: '2026-10-09'
summary: >-
  Shows, by tracking each node's hyperbolic distance to the origin, that
  hyperbolic graph models trained on task losses do not by themselves
  place a tree's root nearest the origin or spread its levels outward: on
  synthetic 3-ary trees the root sits well off the minimum and level order
  is recovered for only 69–75% of node pairs. A centroid recentring plus
  an outward-push loss (HIE), using no level information, raises this to
  75–84% and improves link prediction and node classification, most on
  the least tree-like graphs.
---
<!-- inactive-ok-file: QUESTION-025 THEORY-185 CLAIM-119 LIT-267 — Open or Proposed; cited as the question this reading was filed for and the accounts it joins -->

# NOTE-tmp4751w: Hyperbolic Representation Learning: Revisiting and Advancing

## Contribution

Earlier hyperbolic embedding work (Nickel and Kiela; Chami et al.'s HGCN;
Ganea et al.'s hyperbolic neural networks) took for granted that training
on a task loss would put a hierarchy's root near the origin and its leaves
near the boundary, since that is the low-distortion layout the geometry
offers. This paper checks that assumption on trees whose levels are known.
It finds the layout only partly realised: the root is not innermost and
levels are not cleanly separated by radius. It then gives a parameter-free
add-on loss that moves the embedding toward that layout and improves
downstream scores.

## Key insight

Hyperbolic space gives a tree room, but a loss that only scores links or
labels gives the optimiser no reason to use that room in the hierarchical
way. Nothing in a link-prediction or cross-entropy objective pins the root
to the origin. A translation of the whole embedding changes no distance
between nodes, so the origin is arbitrary under any loss built only on
pairwise distances. "Distance to the origin as level" is therefore a
reading the trained embedding has no reason to support until the origin is
tied to the data. HIE's recentring on the centroid ties it.

## Assumptions

- **Hierarchy is read as radius.** A node's level is identified with its
  hyperbolic distance to the origin (HDO), after Krioukov et al.'s
  placement of tree level r at radius ∝ r. Every diagnostic in the paper
  rests on this reading. Other encodings of hierarchy, such as angular
  containment or entailment cones, are not considered.
- **The root is the hyperbolic centroid.** HIE takes the root to be the
  minimiser of Σ v_i d_H²(z_i, z_a) (Theorem 4.1), with all v_i = 1. That
  is the "node with the smallest sum of distances" in a regular tree, and
  it stands in for a supernode when there are several roots.
- **Setting.** Graph data with node features. Models are a Poincaré-ball
  shallow embedding, HNN, and HGCN/LGCN/HGAT, with curvature κ < 0. The
  synthetic trees are 3-ary, eight levels, 1,093 nodes, with 32-dimensional
  Gaussian features per class. TREE-H labels by top-level subtree
  (homophily 0.998); TREE-L labels by level (homophily 0.018).
- **Evaluation.** 12 runs with the maximum and minimum dropped,
  hyperparameters searched on a validation set, and λ for the added loss
  chosen from {1, 0.1, 0.01, 0.001}.

## Key results

- **Position tracking (§3.2, Figure 2).** HGCN on the synthetic trees,
  HDO statistics (ROOT / MIN / MEAN / MAX): TREE-L link prediction
  3.1 / 2.0 / 3.3 / 5.5; TREE-L node classification 1.8 / 1.2 / 2.8 / 4.3;
  TREE-H link prediction 3.3 / 2.1 / 3.4 / 4.5; TREE-H node classification
  2.7 / 2.4 / 3.7 / 5.2. The authors draw three conclusions. The root is
  not at or near the highest level. The HDO distribution is roughly normal,
  where a tree's level counts would make it leaf-heavy. The embedding does
  not spread out to use the space.
- **HIE (§4, Eqs. 4–9).** z̄ = z ⊕_κ (−z_c) (root alignment);
  z_hdo = (1/|V|) Σ w_i d_H(z̄_i, o) with w_i = d_H(z̄_i, o) (the identity
  is the chosen f); L_hyp = σ(−z_hdo), σ monotone increasing; the total
  loss is L_task + λ L_hyp. A tangent-space version replaces the centroid
  with the arithmetic mean of log_o(z). It can be applied as a hard
  replacement of the embeddings or only inside the loss; the two are
  reported as comparable.
- **Theorem 4.1.** The Möbius gyromidpoint (Poincaré) and the Lorentzian
  centroid minimise the weighted sum of squared hyperbolic distances. The
  proof is by citation. **Theorem 4.2.** In the tangent space the weighted
  mean minimises the weighted sum of squared Euclidean distances, proved
  by completing the square.
- **Shallow models (Table 1, DISEASE link prediction, AUC).** With 75% of
  links for training, Euclidean / Poincaré / HIE at dimension 256 give
  73.5 / 77.0 / 82.5. With 25%, they give 54.1 / 55.0 / 66.8 (+21.4%, the
  headline figure). At 25% the plain Poincaré model falls to or below the
  Euclidean one at dimensions 8 and 64.
- **HNN (Table 2, node classification).** HIE beats HNN and HNN++ at all
  three dimensions on DISEASE and Citeseer (e.g. Citeseer 64: 57.2 HNN,
  59.1 HNN++, 67.0 HIE).
- **HGNNs (Table 3).** HIE on HGCN is best or tied for best in every column: DISEASE
  94.4–95.4, Airport 89.8–94.7, Citeseer 72.5–74.2, Cora 81.8–83.0. On
  Citeseer and Cora the plain hyperbolic models are below the Euclidean
  GCN, GAT and SGC, and HIE lifts them above.
- **Ablation (Tables 4, 8).** Stretching alone loses on DISEASE and
  Airport; alignment alone helps DISEASE but loses on Citeseer and Cora;
  both together are best. Pushing nodes toward the origin instead (Eq. 29)
  collapses Citeseer to 18.1 and Cora to 31.9.
- **Root choice (Table 5).** Using the node of highest betweenness,
  closeness or degree centrality as root instead of the centroid gives
  lower scores everywhere except Airport, where all are within error.
- **Level ordering (Table 9).** On 5,000 random node pairs of the
  synthetic trees, the fraction whose HDO order matches the true level
  order: HGCN 72.5% / 68.9% (TREE-L / TREE-H, dimension 16) and
  75.3% / 73.7% (256); with HIE 75.4% / 80.0% and 77.6% / 83.5%.
- **Euclidean analogue (Table 10).** The same recentre-and-push in
  Euclidean space (GAT + EIE) gains at most 4.7 points (DISEASE, dimension
  16), and HGAT + HIE is better on every dataset.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Hyperbolic models trained on task losses do not place a tree's root nearest the origin | moderate | Figure 2 (HGCN, two synthetic trees, four runs shown); "other hyperbolic models have demonstrated comparable results" is asserted without data |
| C2 | Their HDO distribution is roughly normal rather than leaf-heavy, so level is poorly read off radius | moderate | Figure 2 shapes as described; Table 9 gives 69–75% pairwise ordering against 50% for chance |
| C3 | Recentring on the centroid and pushing outward improves the radial level ordering | moderate | Table 9, synthetic trees only; no variance reported |
| C4 | HIE improves link prediction and node classification across shallow, HNN and HGNN models | strong (as benchmarks go) | Tables 1–3, 12 runs with standard deviations, same splits as baselines |
| C5 | The gains come from better hierarchy | weak | the largest gains are on the least tree-like graphs, which the authors themselves credit to separation; the real graphs' levels are never measured |
| C6 | The gyromidpoint and Lorentzian centroid minimise the sum of squared hyperbolic (geodesic) distances | not supported here | proof by citation; as I understand the cited results (Law et al. 2019), the Lorentzian centroid minimises squared *Lorentzian* distance, not squared geodesic distance, so the statement may be loose |

## Method

Train any hyperbolic model as usual. At each step, compute the weighted
hyperbolic centroid z_c of the final-layer embeddings, translate the
embedding by −z_c (Möbius addition, or subtraction in the tangent space at
the origin), and add λ σ(−mean_i d_H(z̄_i, o)²) to the task loss. Because
w_i is the node's own HDO, the added term rewards spreading in proportion
to how far out a node already is. Nodes near the centre are pushed little
and nodes near the rim a lot, which amplifies whatever radial order
training has already produced rather than imposing one.

## Concepts

- **HDO (hyperbolic distance to origin)**: d_H(x, o), which the paper also
  calls the induced hyperbolic norm. Read as hierarchical level: smaller is
  higher.
- **HC (hyperbolic embedding centre)**: the weighted Möbius gyromidpoint or
  Lorentzian centroid of the embeddings, taken as the root.
- **Root alignment**: translating the embedding so that HC sits at the
  origin.
- **Hierarchical (level-aware) stretching**: the loss σ(−z_hdo), which
  pushes nodes outward with weight equal to their current HDO.
- **Homophily (Pei et al.)**: the mean over nodes of the fraction of
  neighbours sharing the node's label.
- **Hyperbolicity δ**: Gromov's δ, lower meaning more tree-like. The
  paper reports DISEASE 0 (node classification) or 1.0, Airport 1.0,
  Citeseer 2.5 and Cora 11.0.

## Connections

The analogy between a tree and hyperbolic space, with level r at radius
∝ r, is taken from Krioukov et al. (2009, 2010), filed in the same batch.
The shallow-model loss is Nickel and Kiela's Poincaré and Lorentz
embeddings. The neural models are Ganea et al.'s HNN, Shimizu et al.'s
HNN++, Chami et al.'s HGCN and Zhang et al.'s LGCN. The use of HDO as a
post-hoc reading of level follows Nickel and Kiela (WordNet), Khrulkov et
al. (image uncertainty near the origin) and Sun et al. (popularity).
Sala et al. (2018), also in the batch, is cited among works on hyperbolic
embedding but not used. The authors relate HIE to tree-fitting methods
(neighbour joining, Sonthalia and Gilbert's TreeRep) only in prose, as
topology-only alternatives that could be combined with it.

## Bearing on the record

- **[QUESTION-025](../questions.d/QUESTION-025.md)** asks whether hierarchical attributes in co-occurrence
  still give linear attribute directions and a non-Boolean concept
  lattice. This paper does not answer it. It neither works with
  co-occurrence or PMI nor uses linear directions: hierarchy is encoded
  as radius in a curved space, and models are trained graph networks. Its
  bearing is methodological and indirect. A space suited to a hierarchy
  does not show that a trained representation in it holds the hierarchy;
  that had to be measured on data with known levels, and here the
  measurement found it only partly present. The same holds for any
  answer to the question's measurement arm: a probe's success on a known
  hierarchy (WordNet hypernymy, say) has to be measured, not inferred
  from the embedding's form.
- **A second encoding of hierarchy.** [THEORY-185](../theory.d/THEORY-185.md) and the Lattice
  Representation Hypothesis ([LIT-267](../literature.d/LIT-267.md)) put attributes on linear directions
  and read implication as containment of thresholded half-spaces. Here
  generality is radius (nearer the origin is more general) and descent is
  outward. Which encoding, if either, co-occurrence statistics with
  implications would produce is part of what [QUESTION-025](../questions.d/QUESTION-025.md) leaves open.
  This paper offers no evidence either way, because its hierarchies are
  graph adjacency, not attribute implication.
- **[CLAIM-119](../claims.d/CLAIM-119.md)** (categories form a concept lattice rather than a
  hierarchy) is not touched: the paper only treats trees and tree-like
  graphs, never lattices with shared attributes.
- No THEORY filed. The one finding that might stand as one is that task
  losses do not produce radial hierarchy in hyperbolic models. It rests on
  one architecture's HDO figures and a single pairwise-ordering table on
  two synthetic trees, and it is a finding about ML training. It is better
  held, if anywhere, in the anthology.
- An anthology topic could hold the paper (graph representation learning,
  a method with practice advice), hence `anthology-candidate` on the LIT.

## Limitations

- **Diagnosis on two synthetic trees and one model.** Figure 2 shows HGCN
  only; that other hyperbolic models behave alike is asserted. Level
  information exists only for the synthetic trees, so on DISEASE, Airport,
  Citeseer and Cora "better hierarchy" is inferred from the shape of the
  HDO distribution, not measured.
- **The fix supplies no hierarchy.** The weights w_i are the nodes' own
  current HDO and the root is the centroid, so HIE spreads and recentres
  whatever the task loss produced. Its gains being largest on the least
  tree-like graphs, which the authors credit to separability, suggests
  much of the benchmark improvement is spreading rather than hierarchy.
- **The figures do not fully match the text.** After HIE the centroid's
  HDO is still above the minimum on several panels (e.g. Airport,
  dimension 64: ROOT 2.9, MIN 2.4), against the claim that the root is
  "optimized to close the highest position". The reported root is the
  centroid of the unaltered embedding under partial alignment, which may
  explain it, but the paper does not say so.
- **Inconsistencies.** "Alignment only" on DISEASE is 94.5 in Table 4 and
  95.5 in Table 8, which are meant to be the same setting. The Appendix G
  text names the wrong column for the opposite-stretching results. The
  dataset list in §5.1 says four datasets and has a dangling "and".
- **No variance on Table 9** and no statement of how pairs at the same
  level are scored.
- **Theorem 4.1 as stated** may be loose for the Lorentz model (see C6).
  It is not used in any proof that matters to the results.

## Open questions

- Why task losses leave the root off-centre. Since pairwise-distance
  losses are invariant under hyperbolic isometries, the origin is
  arbitrary for the shallow model. An account that separates this gauge
  freedom from a real failure to order levels would say how much of the
  diagnosis survives recentring alone. Table 4's alignment-only column
  hints that on the most tree-like data (DISEASE) recentring is most of
  it.
- Whether the radial ordering, after HIE, is level ordering or just
  degree or centrality ordering. A tree whose level and degree are
  decoupled would separate the two.
- Whether the same diagnosis holds for hierarchies of implication among
  attributes (a poset or concept lattice) rather than graph trees, which
  is the form [QUESTION-025](../questions.d/QUESTION-025.md) needs.
