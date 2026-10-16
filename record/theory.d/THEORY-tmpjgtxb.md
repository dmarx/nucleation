---
status: Proposed
promote_when: >-
  Several independently trained pairs per model, for models that are not
  supervised image classifiers (diffusion, contrastive, graph or latent
  variable models), joined by a fixed low-loss curve found by optimising a
  path, with the loss measured densely along the whole path against the
  endpoints, with error bars. It is refuted by such a pair, trained by the
  same standard procedure, between which neither curve fitting nor a
  nudged-elastic-band search with an adequate budget finds a path whose
  barrier is small. A chain of retrained anchors cannot settle it, since
  it shows that retraining works rather than that a path exists, and
  neither can a paper that describes paths without reporting them.
title: "Low-loss paths between independently trained solutions are found outside supervised image classifiers: graph neural networks trained from different seeds on one graph are joined by quadratic Bezier curves where the straight line has a barrier, and one pair each of diffusion and contrastive models by chains of low-loss checkpoints"
version: 1
tags:
- loss-landscapes
- anthology-candidate
date: '2026-10-16'
source:
- LIT-676
- LIT-660
extends:
- THEORY-109
answers:
- QUESTION-069
summary: >-
  Li et al. (2025), [LIT-676](../literature.d/LIT-676.md), read in [NOTE-529](../notes.d/NOTE-529.md): GCN node classifiers from
  different seeds, on 12 real graphs and synthetic CSBM graphs, show linear
  barriers that a fitted quadratic Bezier curve removes. Yao, Zhang & Tian
  (2026), [LIT-660](../literature.d/LIT-660.md), read in [NOTE-534](../notes.d/NOTE-534.md): one pair of DDPMs and one pair of
  small CLIP models joined by chains of checkpoints whose training loss
  stays under a threshold, where AutoNEB's paths rise steeply on CLIP. The
  evidence is plots without barrier numbers in the first, one pair per
  model and retrained anchors in the second. Zhang & Blei's claim of flat
  paths between LDA's ELBO maxima ([LIT-677](../literature.d/LIT-677.md)) reports no results.
---
<!-- inactive-ok-file: LIT-660 LIT-676 — Proposed; the two readings this account rests on, which is why it is Proposed -->
<!-- inactive-ok-file: LIT-677 — Proposed; named as a claim without reported results, not leaned on -->
<!-- inactive-ok-file: THEORY-109 — Proposed; the account this one extends, and no firmer than it -->
<!-- inactive-ok-file: THEORY-210 THEORY-tmpxxllh — Proposed; neighbouring accounts named in Connections, not leaned on -->

# THEORY-tmpjgtxb: Low-loss paths between independently trained solutions are found outside supervised image classifiers: graph neural networks trained from different seeds on one graph are joined by quadratic Bezier curves where the straight line has a barrier, and one pair each of diffusion and contrastive models by chains of low-loss checkpoints

## Source

- Li, Chen, Han, Zeng, Liu & Tang (2025), [LIT-676](../literature.d/LIT-676.md), read in full in
  [NOTE-529](../notes.d/NOTE-529.md): §3.1, Figs. 1–5 and the appendix figures.
- Yao, Zhang & Tian (2026), [LIT-660](../literature.d/LIT-660.md), read in full in [NOTE-534](../notes.d/NOTE-534.md): §5, Figs.
  3–6, Appendices B and E.

## What was actually shown

**Graph neural networks ([LIT-676](../literature.d/LIT-676.md)).** GCNs for node classification are
trained on one graph with different seeds or data orders, three seeds
averaged. On the straight line between two solutions there is often a
loss barrier: small on Cora and Citeseer, large on Coauthor-CS and
Squirrel. A quadratic Bezier curve fitted as in Garipov et al. removes most
of it (Observation 1, Figs. 1–2). GCN, GraphSAGE and GAT give similar
barriers on a graph, and an MLP on the same features differs markedly
(Fig. 4).

**Diffusion and contrastive models ([LIT-660](../literature.d/LIT-660.md)).** One pair of DDPMs on
Flowers102 and one pair of NanoCLIP models on Flickr30k, from different
seeds, with no shared training and no permutation alignment. A chain is
built by moving groups of layers toward the far mode, correcting each
layer's variance, and retraining with AdamW until the loss is under a
threshold. Training loss stays below 0.04 (DDPM) and 0.09 (NanoCLIP)
along it (Fig. 3). Dense interpolation between consecutive NanoCLIP
checkpoints raises the maximum loss by under 5.3% (App. B). AutoNEB,
adapted to these models, reaches a maximum NanoCLIP training loss of 6.69
and training accuracy as low as 0.05 (Fig. 4).

**What could have come out otherwise.** The curve or the chain could have
failed to stay low. On these pairs it did not.

## What this does not say

- **That the evidence matches the classifier evidence.** [LIT-676](../literature.d/LIT-676.md) gives
  no barrier numbers for the real graphs, and its proofs are missing.
  [LIT-660](../literature.d/LIT-660.md) has one pair per architecture, and its path is a walk of
  retrained anchors, each trained back under the threshold (up to 500
  AdamW rounds for DDPM), checked between anchors for NanoCLIP only.
- **That low loss along the path means a good model.** Intermediate DDPM
  checkpoints generate worse images (higher FID) at endpoint-level
  training loss (Fig. 6).
- **That the straight line works.** In the graph networks it often does
  not.
- **That latent-variable models share the property.** Zhang & Blei
  ([LIT-677](../literature.d/LIT-677.md), [NOTE-522](../notes.d/NOTE-522.md)) claim that maxima of LDA's ELBO from two SVI runs are
  joined by essentially flat paths found with the string method, and that
  statistical degeneracy explains it. The workshop paper reports no path,
  no ELBO value and none of the synthetic experiments it describes, so it
  is not a source here.
- **Why the paths exist.** [LIT-660](../literature.d/LIT-660.md) cites singular learning theory for
  expecting connected minima, and [LIT-677](../literature.d/LIT-677.md) degeneracy; neither tests it.

## Connections

- **Extends [THEORY-109](THEORY-109.md)**, whose promote_when asks for connectivity on
  tasks beyond CIFAR classifiers. These are such tasks, on thin evidence:
  the widening that account asks for, not yet the evidence it asks for.
- **[THEORY-tmpxxllh](THEORY-tmpxxllh.md)** takes [LIT-676](../literature.d/LIT-676.md)'s other result: on one graph the linear
  barrier depends on the graph's density, separability and homophily.
- **[THEORY-210](THEORY-210.md)** gives one reason to expect connected minima: continuous
  parameter symmetries stretch minima into connected manifolds. [LIT-677](../literature.d/LIT-677.md)'s
  "statistical degeneracy" is that idea for a topic model.
- **[QUESTION-069](../questions.d/QUESTION-069.md)** asks whether connectedness belongs to the solutions or
  to the path family searched. [LIT-660](../literature.d/LIT-660.md)'s AutoNEB comparison bears on the
  second: on NanoCLIP AutoNEB's path peaks at a training loss of 6.69
  where the staged chain stays below 0.09, so the search matters at least
  to what is found.
