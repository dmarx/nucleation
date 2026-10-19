---
number: 758
status: Read
formerly:
- NOTE-tmp484na
paper: LIT-986
title: 'Shai et al. — Transformers learn factored representations'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv PDF of 2602.02385v1 (preprint dated 3
    February 2026), text extracted with pdftotext: main text §§1–6 and
    Appendices A–I, including the GHMM framework (A), the minimal example
    (B), the processes and noise construction (C), the extended
    experiments (D), training details (E) and the analysis methods (F–H).
    Figures were read through their captions only.
date: '2026-10-14'
summary: >-
  If a generator's token-labelled operators are tensor products, the
  predictive state stays a product state, and a linear map carries it
  losslessly into orthogonal per-factor subspaces of total dimension
  Σ(d_n − 1). Small transformers trained on five such factors settle near
  that dimension, about 10 against 242, in approximately orthogonal
  subspaces. With token noise that makes factoring lossy they collapse to
  it first and expand only later. RNNs and LSTMs show it less sharply.
---
<!-- inactive-ok-file: THEORY-197 — Proposed; the accounts this reading bears on, and the one filed from it, open -->

# NOTE-758: Shai et al. — Transformers learn factored representations

## Contribution

A framework that predicts the geometry of a sequence model's activations
from the latent structure of the process that generated its training
data, and three experiments that test it. When the generator factors
into conditionally independent parts, the predicted representation is a
direct sum of per-factor belief geometries in orthogonal subspaces, with
dimension linear rather than exponential in the number of factors.
Transformers trained by next-token prediction land close to that
prediction, and land there early even when the data make it lossy.

## Key insight

What a next-token predictor needs is the predictive vector, the belief
over the generator's latent state. If the latent dynamics are tensor
products, that belief stays a product of per-factor beliefs, so a
direct sum of the parts loses nothing. The cheap representation is then
also the sufficient one, and the experiments show trained transformers
reach for it even when it is only nearly sufficient.

## Assumptions

- The data come from a finite-dimensional generalized hidden Markov model
  (GHMM), M = (X, S, η^(∅), (T^(x))). The authors note that any process has
  a GHMM representation, but the experiments use five small known ones.
- Conditional independence (Definition 2.1): each T^(x) = ⊗_n T_n^(x),
  which includes dependency chains (DAGs) between factors.
- Product-state preservation needs the initial state to be a product state
  as well (App. A.3); otherwise the state approaches the product manifold
  "generically" under repeated product-preserving maps (footnote 8).
- The scope statement: each factor's predictive vector is in one-to-one
  correspondence with its next-subtoken distribution in these processes.
- Experiments: GPT-2-style, 4 layers, d_model = 120 in the main figures
  (up to 480 in App. D.3), Adam, no weight decay, context length 8 (also 33
  and 101), batch 25,000.

## Key results

- **Proposition 2.2 / eq. (11).** Under conditionally independent
  operators, a product predictive vector stays a product vector after
  every token. *Holds when:* T^(x) = ⊗T_n^(x) and η^(∅) is a product state.
- **Theorem 2.3 / App. A.4.** A linear map carries the product-state
  submanifold invertibly into a direct sum of per-factor vectors in
  orthogonal subspaces, of dimension Σ_n (d_n − 1), against (Π_n d_n) − 1
  for the joint representation. The proof is the explicit embedding
  ι_n of eq. (13) combined with partial traces (eq. 17).
- **App. A.5.** Off the product manifold the joint-to-factored map is not
  invertible; the closest product state in relative entropy is the product
  of reduced states (eq. 14–15), and the loss is the total correlation
  C[η] = D[η ‖ ⊗η_n] (eq. 16).
- **§4.1 (independent factors).** Five factors (three Mess3, two Bloch
  Walk): the joint prediction is 242 dimensions, the factored one 10.
  Dimensions for 95% variance fall from about 100 at initialization to a
  plateau at 11; linear regression recovers each factor's belief geometry.
  Vary-one subspaces: the sum of per-factor dimensions falls to 14 against
  a union of 12, "approximate but not exact orthogonality"; pairwise
  overlaps drop only in the first two principal components. The embedding
  matrix ends with about 12 non-negligible singular values (App. D.6).
- **§4.2 (conditionally independent chain).** Same result on a chain in
  which each factor's dynamics depend on the earlier factors' outputs
  (Fig. 9, 10 dimensions at 95%).
- **§4.3 (noise).** Each token is replaced uniformly with probability ε,
  which breaks conditional independence (eq. 33). For every ε tested
  (0 to 0.5), activations first collapse to about 10 dimensions within
  hundreds of steps and then expand; for ε ≤ 0.05 the curve barely departs
  from ε = 0 (App. D.5).
- **§4.4 / App. D.4 (RNNs and LSTMs).** A d_model = 32 RNN matches the
  transformer (10 components at 95%); at 64 it settles near 16; an LSTM
  smooths at 32; an RNN with d_model = 256 still sits far below the 136
  needed for the joint representation.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Under tensor-product operators the predictive state stays a product state and has a lossless linear embedding in Σ(d_n − 1) orthogonal dimensions | strong | Proposition 2.2, Theorem 2.3, App. A.3–A.4 (elementary linear algebra) |
| C2 | Small transformers trained on five conditionally independent factors use about the factored dimension, not the joint one, even with room for the joint | moderate | §4.1–4.2, App. D.3; one family of synthetic processes, PCA thresholds |
| C3 | Their per-factor subspaces become approximately orthogonal | moderate | vary-one dimension additivity (14 vs 12) and overlap metric, first two PCs only |
| C4 | When factoring is lossy, training reaches the factored representation first and leaves it only under sustained loss pressure | moderate | §4.3, App. C.4, D.5; one noise construction |
| C5 | This is an inductive bias of the architecture | weak | inferred from C4; App. D.4 itself leaves open whether the differences are "due to training dynamics or inductive bias" |
| C6 | Recurrent networks also factor | weak | four small configurations, less sharp (App. D.4) |

## Method

Train on integer tokens that encode the Cartesian product of the
factors' sub-tokens, so nothing in the data marks the factors. Measure
effective dimension as the number of principal components reaching 95%
cumulative explained variance (App. F); recover beliefs by
cross-validated linear regression (App. G); find per-factor subspaces by
varying one factor's sub-sequence while freezing the others and taking
PCA of mean-centred activations; test orthogonality by dimension
additivity (eq. 42) and a principal-angle overlap (eq. 43).

## Concepts

- **Predictive vector η^(x₁:ℓ).** The normalized belief over the
  generator's latent space after a context; contexts with equal vectors
  make equal predictions.
- **Conditionally independent generator.** Token-labelled operators are
  tensor products of factor operators; factors may still depend on one
  another's outputs and be correlated if history is marginalized.
- **Product-state manifold.** The Segre-like set of joint states equal to
  the tensor product of their marginals, of intrinsic dimension Σ(d_n − 1).
- **Factored World Hypothesis.** Transformers prefer the direct-sum
  geometry "even when higher-dimensional representations would be more
  faithful".

## Connections

It extends the authors' earlier finding that belief-state geometry
appears linearly in transformer residual streams (Shai et al. 2024) and
uses processes from that line (Mess3, and the qubit-driven Bloch Walk of
Riechers et al.). Boyd et al. (2025) give the information theory of
decomposing transducers into modules; this paper is its representational
counterpart.

## Bearing on the record

- **[QUESTION-060](../questions.d/QUESTION-060.md) (answered in part; filed as [THEORY-256](../theory.d/THEORY-256.md)).** It
  supplies one case with known relevant variables, the per-factor
  beliefs, and shows the learned variables coincide with them when
  factoring is lossless. With noise it separates the objective, which
  rewards the joint representation, from what training reaches first.
  But the objective is never varied (next-token cross-entropy
  throughout), and the paper does not separate architecture from
  optimization: it calls the preference an "inductive bias of the
  architecture" (§4.3) while App. D.4 says the source is open. The
  question's "what its architecture can represent cheaply" is the
  framing the paper tests, so the evidence is real but partial.
- **The LIT's seeded claim.** "Next-token training yields factored
  variables in orthogonal subspaces even when that costs predictive
  fidelity" holds for early training and for small ε. For large ε the
  converged representation departs from the factored form (Fig. 12). "On
  this evidence representational cheapness, not only the objective, fixes
  the learned variables" is stronger than shown: cheapness predicts the
  first representation reached, and the objective wins later.
- **The paper's orthogonality inference.** Eq. (42) is read as
  "dimensionalities ... are additive only when A ∩ B = {0}, i.e., when the
  subspaces are orthogonal". Trivial intersection gives additivity but not
  orthogonality, so the additivity test supports linear independence; the
  overlap metric (eq. 43) is the actual orthogonality evidence.
- **[THEORY-206](../theory.d/THEORY-206.md).** A complementary case on the representation side: there,
  products of many inputs are costly to represent in one layer; here a
  tensor product of beliefs is avoided in favour of a sum.
- **[THEORY-197](../theory.d/THEORY-197.md).** The paper's noise result is the opposite pattern to the
  RBM counterexample: there the objective wastes units, here the training
  path holds a cheap representation the objective disfavours.
- The paper carries no instruction for ML practice beyond an
  interpretability suggestion; it is held here for [QUESTION-060](../questions.d/QUESTION-060.md) and keeps
  its anthology-candidate flag.

## Limitations

- Five small synthetic factors and one noise construction; no natural
  data.
- Effective dimension depends on a 95% threshold; the plateau is 11, not
  10, and the joint 95% figure is given as 135 in Fig. 2 and 136 in App.
  D.4.
- Orthogonality is approximate and shown in the first two principal
  components only.
- No measurement of the loss gap between the factored and joint
  representations at each ε, so "costs predictive fidelity" is argued
  from the construction, not quantified on the trained models.
- Whether the preference is architectural or a property of training
  dynamics is left open by the paper itself (App. D.4).

## Open questions

- Does the same preference appear under a different objective on the
  same data, which would separate objective from architecture as
  [QUESTION-060](../questions.d/QUESTION-060.md) asks?
- At what ε, model width and training length does the converged
  representation leave the factored form, and is the switch sharp?
- Does it survive on processes where factors are not marked by a fixed
  product token code?
