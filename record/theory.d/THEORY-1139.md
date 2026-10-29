---
number: 1139
status: Proposed
formerly:
- THEORY-tmpe8kmr
promote_when: >-
  An inspection of the restriction maps a sheaf-learning model fits on
  real heterophilic graphs, against a labelling held out from that
  inspection, showing that the learned transports take the class-aligned
  form the separation theory prescribes (sign flips or rotations across
  classes, identity within them) and that accuracy depends on that form,
  for instance by an ablation that keeps the learned maps' magnitudes and
  scrambles their alignment. Benchmark accuracy alone, however high, does
  not settle it.
title: 'A graph network that learns its sheaf restriction maps from node features at each layer reaches the top of the standard small heterophilic node-classification benchmarks and stays within about one point of the best on homophilic ones; on a synthetic balanced bipartite graph it learns the negative transport the theory prescribes, but whether the maps it learns on real graphs have the geometry the theory credits for its success has not been examined'
version: 1
tags:
- representation-learning
- network-science
date: '2026-10-29'
source:
- LIT-1811
summary: >-
  Bodnar et al. (NeurIPS 2022), [LIT-1811](../literature.d/LIT-1811.md), §§5–6 and Appendix F, read
  in [NOTE-1332](../notes.d/NOTE-1332.md). The results are empirical: Table 1 on nine datasets
  of 183 to 18,717 nodes with ten fixed splits, baselines copied from
  earlier papers, spreads of one to nine points; and one synthetic
  bipartite experiment in which the learned maps are inspected. Proposed:
  the paper's explanation of its accuracy, that the model learns the
  right geometry, is tested only on the synthetic case.
---

# THEORY-1139: A graph network that learns its sheaf restriction maps from node features at each layer reaches the top of the standard small heterophilic node-classification benchmarks and stays within about one point of the best on homophilic ones; on a synthetic balanced bipartite graph it learns the negative transport the theory prescribes, but whether the maps it learns on real graphs have the geometry the theory credits for its success has not been examined

## Source

Bodnar et al. (2022), [LIT-1811](../literature.d/LIT-1811.md), §5 (pp. 7–8), §6 (pp. 8–9) and
Appendix F (pp. 27–29) of arXiv 2202.04579v4; read in [NOTE-1332](../notes.d/NOTE-1332.md).

## What was actually shown

**The model.** Each restriction map is F_{v⊴e} = σ(V[x_v‖x_u]), recomputed
at every layer from the current features, in diagonal, orthogonal
(Householder) or general form, inside a residual discretisation of sheaf
diffusion (eqs. 5, 6; p. 8). Stalk dimension is 1 to 5 (p. 8).

**Synthetic.** On a connected balanced bipartite graph with overlapping
Gaussian features, a d = 1 diffusion with learned general maps separates
the classes as diffusion time grows, while learned symmetric maps do not
(Fig. 5, p. 8), as Prop. 9 predicts. The histogram of learned transports
is negative for all edges, as Prop. 10 predicts (p. 9). With three classes
and d = 2 the learned rotations peak near 2 radians on heterophilic edges,
close to 2π/3, but neither the d = 1 nor the d = 2 model reaches the
ideal sheaf's performance (Fig. 7, p. 27).

**Benchmarks.** On nine node-classification datasets, each over the same
ten splits, an NSD variant is first on Texas, Wisconsin, Film, Squirrel
and Cornell, second on Chameleon, and within about 1% of the best on
Citeseer, Pubmed and Cora (Table 1, p. 9). Continuous-time versions do
less well than the discrete ones but beat other continuous models (Table
3, p. 28).

**What could have failed.** The learned maps in the synthetic case could
have stayed positive, or the model could have trailed the heterophily-
specific baselines on the benchmarks.

## What this does not say

- **That the learned maps on real graphs are class-aligned.** No learned
  map is shown for any benchmark dataset. The accuracy is consistent with
  the theory's mechanism and with others: the model is also a feature-
  conditioned message function, "a form of GNN-FiLM layer" (p. 10), and
  such models "have been recently shown to perform well empirically in
  heterophilic settings" (p. 10).
- **That the margins are reliable.** The heterophilic datasets have 183 to
  7,600 nodes, standard deviations run to ±9 points, and the baselines
  are copied from other papers' runs on the same splits (p. 9). Several
  first places are within one standard deviation of the second.
- **That learning recovers a ground truth.** In the synthetic case the
  target sheaf is known because the labels define it. On real data there
  is no such sheaf to compare with, so "learns the geometry" has no test
  here ([QUESTION-130](../questions.d/QUESTION-130.md)).
- **Anything about larger graphs or other tasks.** Only node
  classification on these nine sets is reported.
