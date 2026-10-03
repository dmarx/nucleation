---
number: 529
status: Read
formerly:
- NOTE-tmpia50o
paper: 'LIT-676'
title: 'Unveiling Mode Connectivity in Graph Neural Networks'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full from the arXiv HTML of v1, main text and Appendices A–C.
    The appendix contains figures, settings and dataset descriptions only;
    the proofs the main text points to are absent. Figures were read from
    captions and the text's description of them; barrier values are not
    given as numbers anywhere.
date: '2026-10-03'
summary: >-
  GCN node-classification solutions from different seeds show linear loss
  barriers that vary by graph (small on Cora, Citeseer; large on
  Coauthor-CS, Squirrel) and vanish along fitted quadratic Bezier curves.
  GCN, GraphSAGE and GAT give similar barriers, MLPs different ones. On CSBM
  graphs barriers fall with density and feature separability and peak at
  middling homophily. Stated without proof: a barrier bound through the
  spectral gap, a generalisation bound proportional to the barrier, and a
  Wasserstein distance between graphs' interpolation-loss curves that bounds
  the domain-adaptation gap.
---

<!-- inactive-ok-file: LIT-676 — Proposed by this reading; the note is the reading that placed it -->

# NOTE-529: Unveiling Mode Connectivity in Graph Neural Networks

## Contribution

It is the first systematic look at mode connectivity in GNNs, on 12 real
graphs (13 appear in the appendix figures) and on synthetic CSBM graphs. It
attributes differences in connectivity to graph structure rather than to the
GNN variant, and offers three theoretical statements and two uses: a
generalisation diagnostic and a graph-domain distance.

## Key insight

In a GNN the data's structure is inside the forward pass, so how well two
solutions connect depends on the graph: how dense it is, how cleanly
features separate the classes, and whether edges mostly join same-class or
mostly different-class nodes. Middling homophily, where neither holds, gives
the most rugged landscape.

## Assumptions

- **Node classification with GCN** (Eq. 1) as the main backbone;
  GraphSAGE, GAT and an MLP for comparison. Hyperparameters follow Luo et
  al. (2024); all but one are fixed and the varied one (initialisation or
  data order) generates the modes. 3 seeds, averaged (§3.1).
- **Barrier** (Eq. 9): B = max_α [L(φ(α)) − ((1 − α)L(θ_a) + αL(θ_b))] along
  the line or a quadratic Bezier curve with a learned control point (Eq. 8).
- **CSBM** (Def. 2.1): two classes, Gaussian features N(μ_i, σI), edge
  probabilities p_in > p_out; density p = p_in + p_out; homophily h =
  p_in/(p_in + p_out). The definition requires p_in > p_out, so h > ½, yet
  the paper reports results for heterophilous graphs.
- **Theorem 3.2** (barrier bound) uses an "effective propagation factor"
  λ_eff related to the spectral gap, a curvature constant C_L and a
  Lipschitz constant L_ℓ, none defined precisely.
- **Theorem 4.1** (generalisation) concerns parameters after T iterations
  with m labelled and n − m unlabelled nodes; c(T) and ρ are not defined.

## Key results

- **Observation 1** (Figs. 1–3): linear interpolation produces noticeable
  barriers on many graphs; the quadratic Bezier curve removes most of them.
  Loss contours show Pubmed's minima in one smooth basin and Squirrel's in a
  rugged landscape.
- **Observation 2**: citation graphs interpolate more smoothly than
  co-authorship graphs; graphs from the same domain give similar curves.
- **Observation 3** (Fig. 4, App. A.3): a large gap between MLP and GCN
  barriers; similar barriers across GNN variants.
- **Observation 4** (Fig. 5, CSBM): lower barriers with higher density and
  higher feature separability; higher barriers at middling homophily.
- **Theorem 3.2**: B(θ_a, θ_b) ≤ max_λ {(1 − λ)C_L + λ L_ℓ λ_eff ‖X‖ Σ_l N_l
  ‖W_a^(l) − W_b^(l)‖}, with N_l the smaller product of the two models'
  later-layer weight norms.
- **Corollary 3.4**: with λ_eff = 1 − Δ + C₂√(log n / d_min), B ≤
  O(L_ℓ ‖X‖ [1 − Δ + C₂√(log n / d_min)]), so a larger spectral gap Δ gives a
  smaller barrier.
- **Proposition 3.5** (CSBM): B ≤ O(σ√(d log n) · [C₂√(log n / d_min) − (h −
  ½)² (p_in + p_out)/C₁]).
- **Theorem 4.1**: Δ_gen ≤ O(8 B · n^{3/2}/(m(n − m)) · log(c(T)) T^ρ log
  (1/δ)) with probability 1 − δ. Fig. 6: a training-accuracy barrier
  correlates with the generalisation gap more strongly than validation
  accuracy does.
- **Eqs. 13–14**: d_MC(G¹, G²) = W₁ between the two graphs' loss-along-line
  curves, treated as distributions over α; Δ_da ≤ C · O(d_MC). Fig. 7: d_MC
  correlates positively with source–target gaps for vanilla transfer, DANN,
  DANE, UDAGCN, JHGDA and SpecReg, and alignment methods lower it.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | GNN solutions are usually connected by quadratic Bezier curves but often not by lines | moderate: 12–13 graphs, 3 seeds, plots only | §3.1, Figs. 1–2, App. A |
| C2 | Graph structure, not GNN variant, determines connectivity | moderate: barrier plots across 3 GNNs and an MLP | Fig. 4, App. A.3 |
| C3 | Barriers fall with density and feature separability and peak at middling homophily | moderate on CSBM; "match" to real graphs is asserted | Fig. 5 |
| C4 | The barrier is bounded via the spectral gap | weak: no proof provided, undefined constants | Thm. 3.2, Cor. 3.4, Prop. 3.5 |
| C5 | The barrier bounds, and predicts, the generalisation gap | weak: no proof; one correlation figure | Thm. 4.1, Fig. 6 |
| C6 | A barrier-curve distance bounds and tracks domain-adaptation gaps | weak: no proof; correlation figure | Eqs. 13–14, Fig. 7 |

## Concepts

- **loss barrier B**: the maximum excess of loss along a path over the
  linear interpolation of the endpoint losses.
- **homophily h(G)**: p_in/(p_in + p_out) in the CSBM.
- **effective propagation factor λ_eff**: an undefined quantity "related to
  the spectral gap".
- **mode connectivity distance d_MC**: the Wasserstein-1 distance between
  two graphs' loss-along-interpolation curves.

## Connections

- **Garipov et al. ([LIT-673](../literature.d/LIT-673.md))**: the Bezier-curve method used to show
  non-linear connectivity.
- **Frankle et al. ([LIT-654](../literature.d/LIT-654.md))**: cited both for linear connectivity
  under a shared start and for pruning; the paper's claim that LMC is "a
  common phenomenon in fully connected networks (such as MLPs and CNNs)"
  drops that paper's shared-start condition.
- **Draxler et al. ([LIT-653](../literature.d/LIT-653.md)), Entezari et al. ([LIT-652](../literature.d/LIT-652.md))**: cited
  as the mode-connectivity background.
- **Shchur et al. ([ANTH-LIT-581](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-581.md))**: the source of the Amazon and Coauthor
  graphs.
- **Zhou et al. ([LIT-666](../literature.d/LIT-666.md))**: the federated-learning counterpart, where
  data heterogeneity across clients raises barriers between global modes.

## Bearing on the record

- With the federated reading, evidence for a THEORY candidate that barriers
  are a function of data structure (graph homophily and density here,
  client heterogeneity there). Not filed.
- It touches `network-science` only through CSBM and spectral gap; the
  record's network-science holdings are about networks themselves, and none
  is cited.

## Limitations

- **Missing proofs**; all theoretical statements cite an appendix that is
  not there.
- **Unfinished text**: "[add more experimental details here]" (§3.2);
  "Increasing ρ" where the separability parameter is σ; an unfilled ACM
  header.
- **Homophily definition** excludes heterophily (p_in > p_out), yet
  heterophilous results are discussed.
- **No numeric barriers** for the real-graph comparisons.
- Node classification only; the authors name link prediction and graph-level
  tasks as future work.

## Open questions

- Do the bounds hold, and with what constants?
- Is the middling-homophily peak a property of GCN aggregation or of the
  CSBM's two-class setting?
