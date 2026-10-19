---
number: 274
status: Proposed
formerly:
- THEORY-tmpn31af
promote_when: >-
  A proof, or an independent replication on graphs beyond the paper's
  four tiny ones, that a wide two-layer weight-tied model trained on a
  graph's edges by unregularized full-softmax cross-entropy converges to
  embeddings spanning the top eigenvectors of the random-walk Laplacian
  without a rank constraint; and, for the deep-model half, a controlled
  study in which the same sequence model is shown able to store the edges
  associatively and nonetheless forms a global geometry with weight decay
  and dropout off. It is refuted by a wide two-layer model under that loss
  whose converged embedding keeps substantial weight on the lower
  eigenvectors, or by a deep model that, given associative and geometric
  storage as equally reachable, ends associative under the default set-up.
  What cannot settle it: success on a multi-hop task alone, since that is
  also explained by multi-hop supervision, or results on squared-error or
  negative-sampling losses, which the claim does not cover.
title: "Sequence models trained only on a graph's edge bigrams store it as a global embedding geometry, not as a lookup, although the lookup is expressible, found faster and no less succinct; in a wide two-layer weight-tied model the geometry is the top Laplacian eigenspace, reached by cross-entropy training without a rank bottleneck, regularization or multi-hop supervision"
version: 1
tags:
- representation-learning
- learning-theory
date: '2026-10-14'
source:
- LIT-995
summary: >-
  Noroozizadeh, Nagarajan, Rosenfeld & Kumar (2025), [LIT-995](../literature.d/LIT-995.md), read in
  [NOTE-800](../notes.d/NOTE-800.md). Empirical throughout: path-star graphs up to 5×10⁴ nodes,
  four tiny graphs, frozen-embedding controls; the two-layer spectral
  analysis is informal and rests on an unproved observation (App. F). It
  does not explain why deeper models prefer the geometry, which the paper
  poses as open, and its main transformer runs used weight decay.
answers:
- QUESTION-060
---
<!-- inactive-ok-file: THEORY-229 — Proposed; accounts on the same mechanism or question, open -->

# THEORY-274: Sequence models trained only on a graph's edge bigrams store it as a global embedding geometry, not as a lookup, although the lookup is expressible, found faster and no less succinct; in a wide two-layer weight-tied model the geometry is the top Laplacian eigenspace, reached by cross-entropy training without a rank bottleneck, regularization or multi-hop supervision

## Source

Noroozizadeh, Nagarajan, Rosenfeld & Kumar (2025; ICML 2026), [LIT-995](../literature.d/LIT-995.md),
read in [NOTE-800](../notes.d/NOTE-800.md): §§2–4, Observations 1–4, Refutations 3a–3d, App.
C.3.1, D.3, E.2 and F.

## What was actually shown

**Deep models.** A 12-layer transformer and a Mamba model memorize a
path-star graph's edges and, trained on only the first hop of 75% of
paths, predict the first hop of unseen paths, up to 100% against chance
1/d, on graphs up to 5×10⁴ nodes (Obs. 1). Trained on edges alone, their
leaf and first-node embeddings cluster by path (Refutation 3a). On four
tiny graphs, the same one-hidden-layer architectures fit the edges
associatively when embeddings are frozen, in about 2 steps for wide
models, while geometry takes about 100 (Refutations 3b–3c). For sparse
graphs the bit and norm costs of the two stores differ by a factor of at
most about 2 (Refutation 3d, App. E.2). Under the default small
initialization the geometry forms without weight decay or dropout (App.
C.3.1).

**The two-layer model.** With weight-tied embedding width 100 on graphs
of at most 16 nodes, unregularized full-softmax cross-entropy on 1-hop
edges, the embedding's projection concentrates on the top Fiedler-like
eigenvectors of −L, L = (I − D⁻¹A) + (I − D⁻¹A)ᵀ, more sharply than the
eigenvalues do: two directions for the cycle and grid (Fig. 7). In the
dynamics V̇ = ηC(t)V, those eigenvectors enter C's null space while the
others decay (Fig. 8, Obs. 4). App. F gives an informal account: C starts
near −L, its eigenvalues rise toward zero top-first, and lower components
of V shrink.

What could have come out otherwise: with a lookup expressible, as cheap
and reached first, training could have stayed associative. It did not,
under the default set-up.

## What this does not say

- **Not why deep models prefer geometry.** The paper's title says "it is
  unclear why", and its Open Questions 1 and 3 say so. The spectral
  account is for the two-layer model only, where associative storage is
  architecturally excluded.
- **Not a proof.** App. F's propositions assume equal norms, equal
  degrees, near-orthogonal initialization and an empirical Observation 9
  taken "without even an intuitive proof". The authors call all their
  arguments "empirical and informal" (§6).
- **Not independent of optimization settings.** Unit-normal
  initialization can give associative storage; higher learning rate,
  weight decay and dropout strengthen geometry (App. C.3.1). The claim is
  that no such pressure is required, not that none matters.
- **Not regularization-free at scale.** The large path-star runs used
  AdamW with weight decay 0.01; the no-regularization evidence is from the
  tiny graphs.
- **Not natural language.** Symbolic graphs only; reverse edges were
  needed for the large path-star result (App. D.1).
- **Not about convergence.** With the asymmetric normalization the
  degenerate top eigenvalue is slightly positive, so the authors expect
  collapse under much longer training (Remark 6).

## Connections

- **[QUESTION-060](../questions.d/QUESTION-060.md).** An answer in part, naming a third determinant besides
  objective and cheap representability: the dynamics of training. Here
  the local objective is satisfied equally by both stores, and the
  architecture can represent both at similar cost, yet the learned
  variables are the graph's leading spectral coordinates.
- **[THEORY-229](THEORY-229.md).** The same kind of mechanism, eigenvectors filtered by
  gradient dynamics, for a symmetrized Barlow Twins loss from small
  initialization. This account is for cross-entropy from near-orthogonal
  initialization and is informal.
- **[THEORY-256](THEORY-256.md).** A second case in which training reaches a
  low-dimensional structured representation that the objective alone does
  not select.
- **[QUESTION-052](../questions.d/QUESTION-052.md).** A side connection: the two-layer model's learned
  signature is the top eigenspace of a symmetrized random-walk operator,
  and untied models pick up singular directions instead (§4.4).
