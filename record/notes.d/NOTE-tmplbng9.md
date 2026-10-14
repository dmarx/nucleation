---
status: Read
paper: LIT-232
title: 'Gebhart, Hansen and Schrater — Knowledge Sheaves'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv PDF (2110.03789v2, 18 March 2023, the
    AISTATS 2023 version, 23 pages), text extracted with pdftotext:
    §§1–6, Definitions 1–11, and appendices A (other embedding models),
    B (worked examples), C (harmonic extension with translations, whose
    derivation was checked), D (the Gaussian reading), E (sheaves in other
    categories) and F (experimental details and Tables 1–3). Figures 2 and
    5–9 are plots without a text layer and were read from their captions
    and the text that describes them. Replaces the seeded skim NOTE-211.
date: '2026-10-14'
summary: >-
  A knowledge-graph embedding is a knowledge sheaf on the schema (one
  pair of restriction maps per relation type) with a 0-cochain of its
  pullback to the graph. The summed Structured Embedding score is the
  sheaf Laplacian form xᵀLx; adding a relation vector gives TransR, and
  identity maps TransE. Since the zero cochain is always a section,
  training needs negative triples and a margin. A multi-hop query is
  scored by harmonic extension, a Schur complement of the query graph's
  Laplacian, which beats summing TransE vectors on ip and pi queries.
---
<!-- inactive-ok-file: NOTE-211 — Superseded; the skim this reading replaces -->
<!-- inactive-ok-file: THEORY-tmp2q47k — Proposed; the account filed from this reading, open -->
<!-- inactive-ok-file: LIT-276 — Rejected; the measurement-as-sheafification paper, named for NOTE-249's comparison, not leaned on -->

# NOTE-tmplbng9: Gebhart, Hansen and Schrater — Knowledge Sheaves

## Contribution

The paper recasts knowledge-graph embedding in the language of cellular
sheaves. Relation types become restriction maps of a sheaf on the schema
graph, entity embeddings become a 0-cochain of the sheaf pulled back to
the knowledge graph, and the familiar scoring functions become the sheaf
coboundary and Laplacian. The recasting covers Structured Embedding, the
Unstructured Model, TransE, TransR and RotatE, and excludes bilinear
models. It gives a training-free way to score multi-hop and conjunctive
queries by harmonic extension.

## Key insight

A fact (h, r, t) is a consistency constraint: the head and tail
embeddings, each sent into a comparison space by the relation's two
linear maps, should agree there. The whole knowledge graph is then a
system of such constraints, and its total violation is a Laplacian
quadratic form. A composite query is the same system on a small template
graph with some vertices fixed, and the best achievable violation is a
Schur complement.

## Assumptions

- **Vector-space stalks and linear restriction maps** in the main text.
  Affine maps (torsors) and metric-space stalks are sketched in
  Appendix E.
- **Every edge of a relation type shares that type's two maps** (the
  pullback, Definition 7). This is parameter sharing, and it means not
  every sheaf on G is a knowledge sheaf.
- **A single entity type** in the experiments, for both datasets.
- **Exact sections are not expected.** "In practice, it is often
  difficult to find an exact section of a sheaf, if one even exists", so
  the definitions are relaxed to scoring functions and a margin.
- **Experiments without hyperparameter tuning**: margin γ = 1, 250
  epochs, embedding dimension in {8, 16, 32, 64}, explicitly "not
  intended to achieve state-of-the-art performance".

## Key results

- **Definitions 1–3.** A schema Q = (S, R, h, t) is a directed multigraph
  of entity types and relation types. A knowledge graph G instantiates it
  when the typing map G → Q is a graph morphism.
- **Definition 4 and Eq. 1.** A cellular sheaf F on a graph assigns a
  stalk to each vertex and edge and a linear map F_{v⊴e} from each vertex
  stalk to each incident edge stalk. The coboundary is
  (δx)_e = F_{v⊴e} x_v − F_{u⊴e} x_u, global sections are H⁰ = ker δ, and
  the sheaf Laplacian L = δᵀδ gives
  xᵀLx = Σ_{e=u∼v} ‖F_{u⊴e} x_u − F_{v⊴e} x_v‖².
- **Definitions 6–7.** A knowledge sheaf is a cellular sheaf on Q (stalk
  dimension d_s per entity type, d_r per relation type, maps d_r × d_s).
  A sheaf embedding of G is a knowledge sheaf with a 0-cochain of its
  pullback k*F to G.
- **Definitions 8–11: consistency is not enough.** A consistent sheaf
  embedding is a section of k*F, but "a trivial entity embedding with
  x_e = 0 for every entity e would be consistent, but useless". A
  contrastive embedding is a section over G that is not a section over
  chosen subgraphs of a negative graph G̃ (Definition 9; the closed,
  open and local closed world assumptions are choices of G̃). A
  γ-gapped contrastive embedding requires V(x_H̃) − V(x_H) > γ for chosen
  pairs (Definition 11), and the margin ranking loss
  L_m = Σ max(0, V_H(x_H) + γ − V_H̃(x_H̃)) (Eq. 4) is zero exactly when
  that holds. The authors note that such an embedding only tells which
  of a pair is true; "given a single relation, there is no way to
  identify whether it lies in G or G̃".
- **"Approximate global section"** has no definition beyond this: a
  0-cochain with small sheaf score (Definition 10), V ≥ 0 and V = 0
  exactly on sections.
- **Subsumed models (§4.2, Appendix A).**
  - Structured Embedding: f_SE(h, r, t) = ‖F_{h⊴r} x_h − F_{t⊴r} x_t‖²,
    and Σ f_SE² = xᵀLx over the graph.
  - Unstructured Model: both maps the identity.
  - Translational: f_TransX = ‖F_{h⊴r} x_h + r_r − F_{t⊴r} x_t‖² (Eq. 3),
    TransR's score when head and tail maps coincide, and TransE's with
    both maps the identity. The relation vector is a 1-cochain pulled back
    from Q.
  - RotatE with complex stalks, the head map diagonal with r_r and the
    tail map the identity; TorusE as its fixed-modulus case.
  - *Not covered:* bilinear models (RESCAL, ComplEx and HolE, the Neural
    Tensor Network, QuatE), TransH except after projection, and
    query-embedding models (BetaE, Query2Box) (Appendix A.1).
- **Translational sections (§4.1.1).** A consistent translational sheaf
  embedding exists exactly when a standard one does, since one can
  subtract a preimage of the translation. With negative constraints the
  two differ.
- **Priors as restriction-map structure (§4.4).** A symmetric relation by
  equal head and tail maps; dim F(r) < dim F(h) lets one head extend to
  many tails; orthogonal maps make comparison a rotation; stalk
  dimensions may vary by entity type. In the worked example (Appendix
  B.2), equal maps for "friends" also force it to be transitive.
- **Harmonic extension (§4.5, Appendix C).** For a query template H with
  boundary vertices B (known and candidate entities) and interior U, the
  relaxed problem min_y yᵀL_H y with y_B fixed is convex and quadratic.
  When L[U, U] is invertible, y_U = −L[U, U]⁻¹ L[U, B] y_B, and the
  optimal value is y_Bᵀ (L[B, B] − L[B, U] L[U, U]⁻¹ L[U, B]) y_B, the
  Schur complement L/L[U, U]; otherwise the pseudoinverse. With
  translations the optimal cost is the linear Schur-complement term plus
  one linear in x_B (Appendix C). The cost is zero exactly when the fixed
  boundary values extend to a section over H.
- **A Gaussian reading (Appendix D).** If entity embeddings are jointly
  Gaussian, the Schur complement is a conditional precision, and the
  sheaf Laplacian plays the part of an inverse covariance. Offered as
  motivation; the Laplacian is singular in general, which the analogy
  passes over.
- **Experiments (§5, Appendix F).** NELL-995 and FB15k-237, queries 1p,
  2p, 3p, 2i, 3i, ip, pi, "easy" and "hard" answers.
  - Square restriction maps generally beat compressive ones, and the
    generalized Structured Embedding variants did best on complex
    queries (Fig. 2). More sections or larger entity dimension helps,
    which the authors attribute to capacity. Orthogonal regularization of
    multiple sections hurt (Fig. 5).
  - Harmonic extension against summing TransE vectors (Table 1, MRR,
    dimension 32, one section): on NELL-995 easy, ip 0.296 against 0.104,
    pi 0.340 against 0.271, 2p 0.237 against 0.164; 2i and 3i about
    equal or slightly worse (0.280 against 0.281; 0.198 against 0.205).
    On hard answers the margins are small, largest on ip (0.079 against
    0.049, NELL-995).
  - Against query-embedding models trained on complex queries (Table 2),
    the extension models are far below: FB15k-237 1p MRR 0.197–0.207
    against 0.350–0.406, 3i 0.103–0.110 against 0.346–0.425, with 0.5–2.8
    million parameters against 6.8–53.4 million.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | SE, UM, TransE, TransR and RotatE scores are sheaf coboundary norms; their summed SE score is the sheaf Laplacian form | strong | direct identification, §4.2, Appendix A |
| C2 | Bilinear models do not fit the framework in this form | moderate | stated, Appendix A.1, not proved impossible |
| C3 | A margin ranking loss is zero exactly on γ-gapped contrastive sheaf embeddings | strong | Definition 11 and Eq. 4, by construction |
| C4 | Harmonic extension scores composite queries from triple-trained embeddings, its cost a Schur complement | strong | §4.5 and Appendix C, standard linear algebra |
| C5 | Harmonic extension beats naive summation on ip and pi queries for TransE | moderate | Table 1, one configuration, no tuning, no error bars |
| C6 | Square maps beat compressive ones; generalized SE does best on complex queries | weak | Fig. 2, untuned |
| C7 | With a stronger base model the method might match query-embedding baselines | weak | conjecture; "We leave proper experimental validation … to future work" |

## Method

Train a knowledge sheaf (restriction maps per relation type, optionally
orthogonal or with a translation 1-cochain) and entity 0-cochains, one or
several per entity, by margin ranking on true and corrupted triples, in
PyKEEN. At query time, build the query's template graph, pull the
learned sheaf back to it, fix the source entities' embeddings, and rank
each candidate target by the Schur-complement cost of extending to it.

## Concepts

- **Knowledge database schema.** A directed multigraph of entity types
  and relation types (Definition 1).
- **Knowledge sheaf.** A cellular sheaf of vector spaces on the schema
  (Definition 6).
- **Sheaf embedding.** A knowledge sheaf plus a 0-cochain of its
  pullback to the knowledge graph (Definition 7).
- **Consistent, contrastive, γ-gapped.** A section over the positive
  graph; additionally a non-section on chosen negative subgraphs; and a
  score gap of more than γ between paired positive and negative
  subgraphs (Definitions 8, 9, 11).
- **Sections (plural), §4.3.** Several 0-cochains learned at once, an
  entity being a d_v × k matrix. "Sections" here means cochains with
  small score, not exact sections.
- **Harmonic extension.** The minimum-energy extension of boundary
  values to the interior of a graph under the sheaf Laplacian.

## Connections

The construction rests on Curry's cellular sheaves (2014) and Hansen and
Ghrist's spectral theory of sheaf Laplacians (2019), and its authors'
"Sheaf Neural Networks" (Hansen and Gebhart). [NOTE-016](NOTE-016.md) already places that
line: sheaf neural networks "descend from cellular sheaves and sheaf
Laplacians … not from" Abramsky and Brandenburger, and neither paper
checked mentions contextuality. This paper fits that account. It cites no
contextuality work. The query benchmarks and baselines are Ren and
Leskovec's BetaE and Query2Box and Hamilton et al.'s GQE. [NOTE-249](NOTE-249.md), a
reading of [LIT-276](../literature.d/LIT-276.md), already records that that paper has no connection to
this one.

## Bearing on the record

- **The sheaf and contextuality line.** The seeded entry called the
  framing "load-bearing if the record wants a sheaf or consistency view
  of relational embeddings". The reading supports a narrower statement.
  - The shared vocabulary hides a difference. In the contextuality line
    ([LIT-016](../literature.d/LIT-016.md), [THEORY-012](../theory.d/THEORY-012.md)) the question is whether a global section
    exists, and its failure is the phenomenon. In a sheaf of vector
    spaces the zero cochain is always a section, as the paper itself
    says, so existence is never in question. What carries content is
    whether *given* data extend: negative triples must fail to be
    sections (Definition 9), and a query's fixed boundary values extend
    with zero Schur-complement cost only if they glue. That is an
    extension question for fixed local data, the closest point of
    contact with [THEORY-012](../theory.d/THEORY-012.md)'s gluing, and it is the record's own
    observation, not the paper's.
  - Filed as [THEORY-tmp2q47k](../theory.d/THEORY-tmp2q47k.md).
- **[QUESTION-026](../questions.d/QUESTION-026.md).** It asks whether a compositional semantics fixes how
  a whole's observables are carried by how its parts' are. Harmonic
  extension is a small instance in a linear setting: the score of a
  composite query is fixed by the parts' restriction maps, through the
  Schur complement of the Laplacian assembled from them. The composite is
  a quadratic form on the boundary, not a relation of the same kind, and
  nothing here concerns utterances or empirical models. Weak bearing;
  noted, not leaned on.
- **For practice.** The experiments are preliminary and untuned, and the
  advice they suggest (square restriction maps, harmonic extension for
  ip and pi queries) is machine-learning practice, which belongs in the
  anthology. The entry's `anthology-candidate` flag stands. The
  anthology was not checked for this paper in this reading.
- **The skim's checks.**
  - "How the contrastive definitions turn into the margin loss": the
    margin ranking loss is zero exactly when the γ-gapped condition of
    Definition 11 holds for the chosen pairs.
  - "Whether 'approximate global section' has a precise sense beyond a
    small Laplacian energy": it does not.
  - "Compare against later sheaf-network and query-embedding work": the
    paper's own Table 2 already shows it well below the query-embedding
    models; later work was not read.

## Limitations

- **Bilinear models are outside it**, including some of the strongest
  embedding families. The framework is a unification of the
  coboundary-type scores only.
- **The experiments are preliminary by the authors' account**: one
  entity type, no tuning, figures without error bars, and a
  harmonic-extension advantage confined mainly to ip and pi queries.
- **The Gaussian reading is heuristic**, and the category-theoretic
  generalization (Appendix E) is a sketch without results.
- **Typing is barely used.** The schema machinery is general, but every
  experiment collapses it to a single entity type.

## Open questions

- What is the representational capacity of a knowledge sheaf with given
  stalk dimensions, the authors' first named direction?
- Do sheaves valued in other categories bring bilinear or query-embedding
  models into the framework?
- Does the harmonic-extension advantage survive tuning and comparison
  with later sheaf-based query methods?
