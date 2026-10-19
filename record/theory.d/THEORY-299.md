---
number: 299
status: Active
formerly:
- THEORY-tmp2q47k
title: 'Structured and translational knowledge-graph embeddings are 0-cochains of a cellular sheaf of vector spaces pulled back from the schema, each triple scored by a norm of the coboundary on its edge and, in the squared-Euclidean form, the whole graph by the sheaf Laplacian; since the zero cochain is always a global section, what they learn is a contrastive margin, not the existence of a section'
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Narrowed and promoted from Proposed to Active at the owner's direction,
    carrying out the promotion audit's decision
    (record/promotion-audit/decisions/THEORY-299.yaml, batch 013, ADR-047).
    The title said the embeddings are "scored by its Laplacian". That is
    exact for the squared-Euclidean scores LIT-232 writes throughout, but
    several of the original models use an unsquared or ℓ1 norm of the same
    coboundary, for which the per-triple score is still a function of the
    coboundary while the summed score is not the Laplacian form. The title
    now says so. The identifications, the zero section and the degeneracy
    of a positive-only objective are re-derived below. The promote_when's
    request for a proof or counterexample about bilinear scores tests a
    claim the title does not make. It moves to QUESTION-tmpvxp0f. Under the
    owner's rule of 2026-10-19 (ADR-047), the re-derivation meets the
    request for a second check of the identifications. The promote_when is
    removed.
tags:
- mathematics
- representation-learning
date: '2026-10-14'
source:
- LIT-232
summary: >-
  Gebhart, Hansen and Schrater (2021; AISTATS 2023), [LIT-232](../literature.d/LIT-232.md), §4 and
  Appendices A and C, read in [NOTE-843](../notes.d/NOTE-843.md). A direct identification,
  covering Structured Embedding, the Unstructured Model, TransE, TransR
  and RotatE and not bilinear models. That existence of a section is
  trivial here, and that the only gluing question is whether fixed data
  extend, is the paper's own remark taken further by the record; it is
  what separates this use of sheaves from the contextuality line.
---
<!-- inactive-ok-file: QUESTION-tmpvxp0f — Open; the bilinear question moved out of this account's promote_when, named as open -->
<!-- inactive-ok-file: LIT-276 THEORY-024 — Rejected; named for contrast, not leaned on: LIT-276 for NOTE-249's finding that it has no connection to this paper, THEORY-024 as a neighbouring use of global sections -->

# THEORY-299: Structured and translational knowledge-graph embeddings are 0-cochains of a cellular sheaf of vector spaces pulled back from the schema, each triple scored by a norm of the coboundary on its edge and, in the squared-Euclidean form, the whole graph by the sheaf Laplacian; since the zero cochain is always a global section, what they learn is a contrastive margin, not the existence of a section

## Source

Gebhart, Hansen and Schrater (2021; AISTATS 2023), [LIT-232](../literature.d/LIT-232.md), read in full
in [NOTE-843](../notes.d/NOTE-843.md): Definitions 1–11, §§4.1–4.5, Appendix A (other models),
Appendix C (harmonic extension with translations).

## What was actually shown

**The identification.** A knowledge sheaf assigns a vector space to each
entity type and relation type of the schema, and to each relation two
linear maps, head and tail, into the relation's space (Definition 6).
Pulling it back along the typing morphism gives a sheaf on the knowledge
graph in which every edge of one relation type shares that type's maps
(Definition 7). Entity embeddings are a 0-cochain of the pullback. Then
the Structured Embedding score of a triple is the norm of the coboundary
on that edge, ‖F_{h⊴r} x_h − F_{t⊴r} x_t‖², and its sum over the graph is
the sheaf Laplacian form xᵀLx (Eq. 1, Appendix A). A pulled-back
1-cochain of relation vectors gives TransR's score, identity maps give
TransE's and the Unstructured Model's, and a diagonal complex map gives
RotatE's. Bilinear models (RESCAL, ComplEx and HolE, the Neural Tensor
Network, QuatE) are not covered (Appendix A.1).

**Consistency is free.** The paper notes that the all-zero embedding is
consistent "but useless" (after Definition 8). A sheaf of vector spaces
always has the zero section, so every content-bearing condition is
contrastive: true triples consistent, chosen negative subgraphs not
(Definition 9), relaxed to a score gap γ (Definition 11), which the
margin ranking loss enforces exactly (Eq. 4). Such an embedding ranks a
true triple above a paired false one, and "given a single relation,
there is no way to identify whether it lies in G or G̃". "Approximate
global section" means no more than small Laplacian energy (Definition
10).

**Where gluing does enter.** A multi-hop or conjunctive query fixes some
entity embeddings on a template graph and asks how cheaply they extend
to the rest. The answer is the Schur complement L/L[U, U] evaluated on
the boundary values (§4.5; Appendix C adds translations), zero exactly
when the boundary data extend to a section. This is the paper's
inference method; its reading as an extension question is the record's.

What could have come out otherwise: the identifications are checkable
term by term, and a model whose score is not a function of the
transformed difference would fall outside them, as the bilinear models
do.

## What this does not say

- **It does not unify all knowledge-graph embedding.** Bilinear models,
  among the strongest, are outside the framework as given. Whether
  sheaves in other categories would take them in is an open suggestion
  (Appendix E).
- **It does not say the sheaf view improves embeddings.** The experiments
  are preliminary and untuned, harmonic extension beats naive TransE
  summation mainly on ip and pi queries, and the extension models fall
  well below query-embedding baselines (Table 2).
- **It is not contextuality, and it does not connect the record's two
  uses of "sheaf".** In the contextuality line ([LIT-016](../literature.d/LIT-016.md), [THEORY-012](THEORY-012.md)) the
  phenomenon is that no global section exists. Here a global section
  always exists, and the paper cites no contextuality work. The only
  shared question is whether fixed local data glue. That a learned
  embedding is "an approximate global section" says it nearly satisfies
  linear constraints, not that anything nonclassical is avoided.
- **It does not give "approximate section" a precise sense** beyond a
  small score.
- **It does not make every original model's score the Laplacian.** The
  paper writes each score as a squared Euclidean norm. Where an original
  model uses an unsquared or ℓ1 norm, the triple's score is still that
  norm of the same coboundary, but the summed score is not xᵀLx.
- **It is not an instruction.** Which restriction-map structure to use is
  practice, and belongs in the anthology.

## Connections

- **[THEORY-012](THEORY-012.md).** The contextuality account's criterion is gluing of
  context distributions into one global distribution. This account marks
  the difference: for vector-space stalks gluing of arbitrary local data
  is never the issue, only gluing of prescribed boundary values.
- **[THEORY-024](THEORY-024.md) (Rejected).** A neighbouring use of global sections and
  sheafification in the record, rejected; nothing here revives it.
- **[QUESTION-026](../questions.d/QUESTION-026.md).** Harmonic extension is a small linear instance of a
  composite's score fixed by its parts' maps (the Schur complement of the
  assembled Laplacian). It does not concern utterances or empirical
  models, and is noted, not offered as an answer.
- **[NOTE-016](../notes.d/NOTE-016.md)'s lineage finding,** that sheaf neural networks descend
  from cellular sheaves and Hansen and Ghrist's Laplacians rather than
  from Abramsky and Brandenburger, covers this paper too. [NOTE-249](../notes.d/NOTE-249.md) finds
  that [LIT-276](../literature.d/LIT-276.md) has no connection to it.
- **[QUESTION-tmpvxp0f](../questions.d/QUESTION-tmpvxp0f.md).** Whether bilinear scores admit a sheaf-coboundary
  representation at all: the request this account's promote_when carried
  until 2026-10-19.

## Note of 2026-10-19: the identifications, derived directly

Restriction maps depend only on the relation type, so every edge e of
relation r has F_{h⊴r} and F_{t⊴r}, and for a 0-cochain x,
(δx)_e = F_{h⊴r} x_h − F_{t⊴r} x_t.

- **Structured Embedding:** F_{h⊴r} = R_r^lhs and F_{t⊴r} = R_r^rhs, with
  score ‖(δx)_e‖.
- **Unstructured Model:** F = I, with no translation.
- **TransE:** F = I, plus a pulled-back 1-cochain r_r, with score
  ‖(δx)_e + r_r‖.
- **TransR:** F_{h⊴r} = F_{t⊴r} = M_r, plus r_r.
- **RotatE:** F_{h⊴r} = diag(r) with |rᵢ| = 1, a real 2 × 2 block rotation
  on ℂ^d ≅ ℝ^{2d}, and F_{t⊴r} = I.
- **The Laplacian.** With L = δᵀδ, xᵀLx = ‖δx‖² = Σ_e ‖(δx)_e‖², the
  summed squared score. With translations it is ‖δx + r‖², the affine form
  of Appendix C.
- **The zero section, and why negatives carry the content.** δ0 = 0, so
  x = 0 is a global section of any sheaf of vector spaces. A positive-only
  objective, the summed score over true triples, has minimum 0, and a
  degenerate embedding attains it in every model above:
  - x = 0 with r = 0 for SE, UM and TransR;
  - all entities equal and r = 0 for TransE under its unit-norm
    constraint;
  - x = 0 for RotatE.

  Such an embedding gives every triple the same score, so it ranks
  nothing. A margin ranking loss is zero exactly on γ-gapped embeddings
  (Definition 11, Eq. 4).
