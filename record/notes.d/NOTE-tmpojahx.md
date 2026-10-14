---
status: Read
paper: LIT-995
title: 'Noroozizadeh et al. — Deep sequence models tend to memorize geometrically'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read from the arXiv PDF of 2510.26745v3 (18 May 2026, ICML 2026
    camera-ready), text extracted with pdftotext. Read in full: §§1–7, and
    Appendices A (path-star background), B (setup and the tests for
    geometric storage), C (Mamba, tree-star and tiny-graph results,
    including C.3.1 on regularizers and initialization), D (reverse
    edges, pause tokens, phased training), E (the succinctness
    propositions) and F (the Node2Vec spectral analysis). Figures were
    read through their captions; the heatmaps and 3D plots were not
    inspected.
date: '2026-10-14'
summary: >-
  Transformers and Mamba trained only on a graph's edge bigrams embed
  nodes so that multi-hop relations are readable, and solve an in-weights
  path-finding task built to defeat next-token learning. The authors argue
  that supervision, capacity, ease of optimization and succinctness each
  fail to explain why this geometry wins over an associative lookup. In a
  wide two-layer weight-tied model under unregularized cross-entropy the
  embeddings settle into the top Laplacian eigenvectors without a rank
  bottleneck, shown empirically, with an informal partial proof. Why
  deeper models prefer geometry is left open.
---
<!-- inactive-ok-file: THEORY-229 THEORY-tmpn31af — Proposed; the account this reading bears on, and the one filed from it, open -->

# NOTE-tmpojahx: Noroozizadeh et al. — Deep sequence models tend to memorize geometrically

## Contribution

The paper isolates a case of implicit reasoning over facts stored in
weights that the usual "associative memory" picture cannot explain:
path-finding on a fixed path-star graph whose edges were memorized as
bigrams. It names the alternative, "geometric memory", in which node
embeddings encode global graph structure. It argues that obvious
pressures do not explain why this geometry forms, and it traces the
geometry, in the simplest two-layer model, to a spectral bias of
cross-entropy training that needs no bottleneck.

## Key insight

Storing a graph as embeddings whose inner products track multi-hop
closeness turns an ℓ-fold composition into one-step navigation. That
store is not cheaper, not faster to find and not required by the
supervision, yet gradient descent reaches it. In the two-layer case it is
the top of the graph spectrum: training filters out the lower
eigenvectors of the random-walk Laplacian.

## Assumptions

- Data: edge bigrams of a fixed graph (forward and reverse for the large
  path-star graphs), plus path-finding examples on a subset of leaves;
  test paths share no edges' worth of path supervision with training paths.
- Large-graph models: 12-layer GPT-style transformer, width 384 or 784,
  tied embeddings, AdamW with weight decay 0.01, pause tokens; Mamba of
  similar size (App. B).
- Tiny-graph models: one hidden layer between tied (un)embeddings; the
  "associative" control freezes the embeddings (App. B.2.2).
- The Node2Vec analysis: full-softmax 1-hop objective, weight-tied,
  embedding width 100 on graphs of at most 16 nodes, learning rate 0.01,
  2000 steps.
- The partial proof in App. F assumes near-orthogonal initialization
  (Assumption 1), equal embedding norms and roughly equal degrees
  (Assumption 2), and an empirical Observation 9 taken "without even an
  intuitive proof".

## Key results

- **Observation 1 (§2.2).** On path-star graphs up to 5×10⁴ nodes,
  trained on edges plus the first token only of 75% of paths, both the
  transformer and Mamba predict the first hop of unseen paths, up to 100%
  accuracy against a chance level of 1/d (Fig. 3, Fig. 14).
- **Refutation 3a (§3.1).** Training on edges alone already yields
  leaf-to-first-node clustering (Fig. 5, Fig. 15b); an edge-pretrained
  model briefly reaches high path accuracy when finetuned (App. D.3).
- **Refutation 3b (§3.2).** The same tiny architectures fit the edges
  associatively when embeddings are frozen; a geometry still forms without
  weight decay or dropout under the default initialization N(0, 0.02²)
  (App. C.3.1). Under unit-normal initialization the outcome is sensitive,
  and one setting produces associative storage (Fig. 28).
- **Refutation 3c.** For wide models associative storage forms in about 2
  steps and geometric storage in about 100 (Fig. 6, Figs. 21–22).
- **Refutation 3d / App. E.2.** For sparse graphs with |E| ≈ |V| the bit
  and ℓ₂-norm costs of the two stores are within a factor of about 2
  (Propositions 1–2). The bit estimate for a path-star embedding,
  |V|·d·log ℓ, exceeds the associative cost.
- **Observation 3–4 (§4.3).** A wide weight-tied two-layer model trained
  by cross-entropy concentrates its embedding on the top "Fiedler-like"
  eigenvectors of −L, even more skewed than the eigenvalues (Fig. 7; only
  2 directions for cycle and grid), while the coefficient matrix C(t) in
  V̇ = ηC(t)V acquires those vectors in its null space (Fig. 8). L is the
  symmetrized random-walk Laplacian (I − D⁻¹A) + (I − D⁻¹A)ᵀ (App. F).
- **Propositions 6–10 (App. F.3).** Informal: given Observation 9, the
  eigenvectors of C, P + Pᵀ and VVᵀ stay those of −L throughout training,
  C's eigenvalues start negative and rise to zero top-first, and the column
  space of V converges to the top eigenvectors "independent of the
  embedding dimensionality". Remark 6: with this asymmetric normalization
  the degenerate top eigenvalue is slightly positive, so long training
  would collapse onto it and early stopping is needed.
- **§4.4.** Untied or deeper models add negative-eigenvalue
  ("zigzag", bipartite) directions; adding self-edges removes them
  (Fig. 25).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Transformers and Mamba solve in-weights path-star path-finding on graphs up to 5×10⁴ nodes from first-token supervision alone | moderate | §2.2, Figs. 3, 12, 14; one topology plus tree-star variants |
| C2 | A global embedding geometry forms from edge memorization alone | moderate | Fig. 5, Fig. 15b, App. C.3 heatmaps, App. D.3 |
| C3 | Associative storage is expressible in the same set-up and found faster | moderate | frozen-embedding controls, Fig. 6, Figs. 21–22 |
| C4 | Succinctness does not separate the two stores on sparse graphs | moderate | Propositions 1–2, App. E.2 (bounds up to constants) |
| C5 | In a wide two-layer tied model, cross-entropy training itself yields a low-rank spectral bias onto the top Laplacian eigenvectors | moderate | Fig. 7–8 on four tiny graphs; informal propositions resting on an unproved observation (App. F) |
| C6 | Transformer memory is a spectral geometry "adulterated" by associative storage | weak | Conjecture 1, from visual comparison |

## Concepts

- **Associative memory (Def. 2a).** Logit f(u)[v] high only on adjacent
  pairs; arbitrary near-orthogonal embeddings with the adjacency stored in
  a middle matrix.
- **Geometric memory (Def. 2b, §2.5).** Logits, or a probe, reflect
  multi-hop closeness; at its simplest a low-rank factorization
  Φ(u)·Φ(v) skewed to the top eigenvectors.
- **Fiedler-like vectors.** The second and next few top eigenvectors of
  −L.
- **Memorization puzzle.** Why gradient descent prefers geometric storage
  when associative storage is expressible, easier to find and as succinct.

## Connections

It consolidates earlier findings that node embeddings encode distances
in in-weights reasoning tasks (Jiang et al., Khona et al., Ye et al.) and
that factorized parameterizations enable two-hop inference (Huang et al.,
Saxe et al.). On the Node2Vec side it sets itself against analyses that
obtain the spectrum from a bottleneck, explicit regularization, early
stopping or a multi-hop objective (Levy and Goldberg, Karkada et al.).
The path-star task is Bachmann and Nagarajan's.

## Bearing on the record

- **[QUESTION-060](../questions.d/QUESTION-060.md) (answered in part; filed as [THEORY-tmpn31af](../theory.d/THEORY-tmpn31af.md)).** The
  paper gives a case where neither the supervision nor what the model can
  represent fixes the learned variables: the associative store is
  representable, as cheap and faster to reach, and the supervision is
  local. The variable that wins is set by the dynamics of cross-entropy
  training, and in deeper models by initialization scale, learning rate
  and regularization as well (App. C.3.1). The LIT's seeded body names
  this "a third candidate the question does not yet name", and that is
  fair. Two cautions. The "spectral bias" is shown only for the two-layer
  model, with an informal proof resting on an empirical assumption; for
  the transformer the authors say outright that it is unclear why. And
  the main transformer runs used weight decay 0.01: the
  no-regularization evidence is from the tiny graphs.
- **The LIT's summary.** "Cannot be put down to supervisory,
  architectural or optimization pressure" is the paper's wording for
  "straightforward versions" of each (§3.2); it lists more nuanced
  pressures, such as flatness, as possible explanations (§6).
- **[QUESTION-052](../questions.d/QUESTION-052.md).** A side connection. The two-layer model's signature is
  the top eigenspace of a Laplacian built from a non-symmetric
  normalization D⁻¹A, symmetrized in the gradient; it is the same object
  as the pair-operator eigenspace, reached here by training dynamics, not
  by a variational optimum. Untied models learn singular directions
  instead (§4.4). This is a data point, not an answer.
- **[THEORY-229](../theory.d/THEORY-229.md).** Kindred: eigenvectors acquired in order of eigenvalue
  under gradient flow. That account is for a symmetrized Barlow Twins loss
  from small initialization; this one is for cross-entropy from large
  near-orthogonal initialization, and its proof is informal.
- It carries a suggestion for practice ("headroom to make Transformer
  memory more strongly geometric"), which belongs to the Anthology; the
  LIT keeps its anthology-candidate flag.

## Limitations

- Symbolic tasks, one main graph topology; natural language untested
  (§6).
- Small to mid-sized models trained from scratch.
- All arguments "empirical and informal" by the authors' own account
  (§6, item 4); App. F's propositions rest on Observation 9, unproved.
- The global-versus-local geometry tests each have known false positives
  or negatives (App. B.5).
- Reverse edges were needed for the large path-star result (App. D.1).
- The geometric margin and heatmap evidence were not checked here beyond
  captions.

## Open questions

- Open Question 2 of the paper: why, and to what solution, does the wide
  two-layer cross-entropy model converge, and at what rate?
- Open Question 3: what controls the balance of associative and geometric
  storage in deeper models?
- Does the same spectral preference hold for a directed graph trained on
  forward edges only, where D⁻¹A has distinct left and right singular
  vectors?
