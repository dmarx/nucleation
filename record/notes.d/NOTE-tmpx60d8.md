---
status: Read
paper: LIT-tmp9dono
title: 'Elhage, Nanda, Olsson et al. — A mathematical framework for transformer circuits'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Read in full on 2026-10-26 from the Transformer Circuits article
    (https://transformer-circuits.pub/2021/framework/index.html,
    "Published Dec 22, 2021"), fetched as HTML and its text extracted. The
    page read is the current one: it carries a "Summary of Follow-Up
    Research" dated "as of February 2023" and a correction of the
    composition diagram. Read: the summary of results, Transformer
    Overview (simplifications, residual stream, virtual weights, heads as
    independent and additive, heads as information movement), zero-,
    one- and two-layer sections (path expansion, QK and OV circuits,
    skip-trigrams, copying and eigenvalues, the three kinds of composition,
    the QK path expansion, induction heads, term importance, virtual
    heads), Where Does This Leave Us, Related Work, Comments &
    Replications with the correction, and the appendices (MLP layers,
    virtual weights and convolution, activation properties, pointer
    arithmetic, identity heads, notation, model details, layer norm,
    low-rank matrices). The equations of the path expansions that are set
    as images, the interactive attention and composition figures, the
    eigenvalue and term-importance plots and the skip-trigram tables were
    not seen; claims from them are taken from the text and captions. The
    record re-derived the logit and QK path expansions and checked them
    numerically (THEORY-tmphm85g). The linked videos and problem set were
    not used.
date: '2026-10-26'
summary: >-
  An exact reformulation of attention-only transformers, and a reading of
  toy models with it. Heads are independent and additive, each a QK
  bilinear form that sets the attention pattern and an OV map that sets
  what moves; with patterns frozen, the logits are a sum of path terms
  (direct, one per head, one per composed pair of heads). Zero-layer models
  are bigram tables, one-layer models bigram and skip-trigram tables
  dominated by copying heads, and in a two-layer model the only substantial
  composition builds induction heads from a previous-token head by
  K-composition. MLP layers, two-thirds of a standard transformer's
  parameters, are left open.
---
<!-- inactive-ok-file: THEORY-tmpkd3fq THEORY-802 THEORY-783 THEORY-tmp1dufu — Proposed; accounts this reading bears on, cited as open -->

# NOTE-tmpx60d8: Elhage, Nanda, Olsson et al. — A mathematical framework for transformer circuits

## Contribution

It gives transformers a form in which circuits can be read. No result
depends on a new architecture: everything follows from rewriting the
standard one. Heads add independently into the residual stream; each head
is two low-rank matrices, W_QK = W_Qᵀ W_K and W_OV = W_O W_V, which never
act apart; and multiplying out the layers turns an attention-only model,
with its attention patterns frozen, into a sum of end-to-end terms from
tokens to logits. With that form the authors read zero-, one- and
two-layer attention-only models off their weights, and find the induction
head.

## Key insight

Which token a head reads from and what it moves are separable: the
attention pattern A comes from the QK circuit, and the effect on the
output from the OV circuit, A ⊗ W_OV. Composition happens in three ways,
by a later head's query, key or value reading what an earlier head wrote.
Q- and K-composition change where a head looks, and are what make depth
more than extra heads. V-composition only chains movements, giving
"virtual heads". An induction head is the minimal case: K-composition with
a previous-token head makes the key of each position carry the token
before it, so a head that matches the present token finds the token after
its last occurrence and copies it.

## Assumptions

- **Attention-only models**, decoder-only, with no MLPs "in most parts of
  this paper". Biases are ignored (they can be folded into weights), and
  layer norm is ignored or folded into adjacent weights up to a per-vector
  scale.
- **Models.** Zero-, one- and two-layer attention-only transformers,
  usually 12 heads with d_head = 64, one one-layer example with 32 heads
  and d_head = 128; context 2048, dense attention; a positional mechanism
  similar to Press et al. that adds sinusoidal embeddings only to queries
  and keys, so no positional information enters the residual stream.
  Training data as in Kaplan et al. Number of runs, steps and parameter
  counts are not given.
- **Frozen attention.** Linearity is in the frozen-pattern sense: run once
  to record patterns, then the logits are linear in the tokens.
- **Copying is summarized by eigenvalues.** Positive eigenvalues of
  W_U W_OV W_E are taken as the "working formalization" of copying, and of
  same-matching in the QK circuit. The authors grant that positive
  eigenvalues are not proof of copying, since eigenvectors need not be
  orthogonal.

## Key results

- **Reformulations (exact).**
  - The concatenate-and-project form of an attention layer equals a sum
    of heads, each with its own W_O.
  - h(x) = (A ⊗ W_O W_V) x, with A = softmax*(xᵀ W_Qᵀ W_K x).
  - The residual stream is linear and has no privileged basis: rotating it
    and every matrix that reads or writes it leaves the model unchanged.
    The only privileged bases are tokens, attention patterns and MLP
    activations.
  - Products of heads behave like heads:
    (A^{h₂} ⊗ W^{h₂}_OV)(A^{h₁} ⊗ W^{h₁}_OV) = (A^{h₂}A^{h₁}) ⊗ (W^{h₂}_OV W^{h₁}_OV).
- **Zero layers.** T = W_U W_E approximates bigram log-likelihoods; the
  same direct-path term appears in every transformer's expansion.
- **One layer.** T = Id ⊗ W_U W_E + Σ_h A^h ⊗ (W_U W^h_OV W_E): a bigram
  term plus one skip-trigram term per head ("A … B C"), read from two
  vocabulary-sized matrices per head, the QK circuit W_Eᵀ W^h_QK W_E and the
  OV circuit W_U W^h_OV W_E. Most heads copy, and "10 out of 12 heads are
  significantly copying" by the eigenvalue statistic. Factoring a
  skip-trigram as f₁(a,b)f₂(a,c) produces "bugs": raising keep … in mind
  and keep … at bay also raises keep … in bay.
- **Two layers, the theory.** The logits gain virtual-head terms
  (V-composition), and the second layer's attention scores gain terms
  A_q ⊗ A_k ⊗ W in which first-layer heads move information on the query
  side, the key side, or both (Q- and K-composition).
- **Two layers, the model.** Composition was measured by a normalized
  Frobenius norm of the product of the relevant matrices, minus the
  expected value for random matrices. As first published, "there is only
  significant K-composition, and only with one layer 0 head", a head that
  attends mostly to the previous token, and the composing second-layer
  heads are induction heads. They attend to the token after an earlier copy
  of the present token on the Harry Potter paragraph and on repeated random
  tokens, and they sit in the corner of positive OV and QK eigenvalues.
  Ablating the second-order virtual-head terms (by a staged
  frozen-attention procedure) costs little loss; the second-layer
  individual head terms matter most.
- **Correction (after publication).** A bug in the authors' low-rank
  library computed the Frobenius norm of a cyclic permutation of the
  product, for instance ‖W^{h₂}_K W^{h₁}_O W^{h₁}_V W^{h₂ᵀ}_Q‖_F instead of
  ‖W^{h₂ᵀ}_Q W^{h₂}_K W^{h₁}_O W^{h₁}_V‖_F. The trace and the eigenvalues are
  invariant under such a permutation; the Frobenius norm is not. The
  corrected diagram keeps the previous-token K-composition and adds more:
  "two of the induction heads also rely on a head which attends to the
  last several tokens".
- **Larger models (asserted, deferred).** Induction heads built by
  K-composition with a previous-token head appear in large models and are
  "a central driver of in-context learning in language models of all
  sizes", to be shown in the next paper (LIT-tmpe7b5o). A second induction
  mechanism, "pointer arithmetic" on positional embeddings through
  Q-composition, was seen once in GPT-2.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | With attention patterns frozen, an attention-only transformer without layer norm or biases is exactly a sum of path terms, and each head separates into QK and OV circuits | strong (algebra) | the reformulations; re-derived and checked numerically by the record (THEORY-tmphm85g) |
| C2 | Zero-layer models approximate bigram statistics; one-layer attention-only models are bigram plus skip-trigram tables | strong for the identity, moderate for the readings | the path expansion and inspected largest entries |
| C3 | Most heads of a one-layer attention-only model copy | moderate | eigenvalue statistic, 10 of 12 heads in one model, agreeing with inspection |
| C4 | In the two-layer model, composition is used mainly to build induction heads, by K-composition with a previous-token head | moderate | one model; composition scores (corrected), attention patterns, eigenvalues (THEORY-tmpb4xka) |
| C5 | Virtual-head (V-composition) terms matter little in small two-layer models | moderate for this model | the term-importance ablation, figures not seen |
| C6 | Induction heads built this way drive in-context learning at all sizes | weak here | deferred to the next paper; the record holds it as THEORY-tmpkd3fq |
| C7 | MLP layers resist this approach for lack of interpretable neurons | the authors' report | stated, not measured |

## Concepts

- **Residual stream**: the running sum of the embedding and every layer's
  output; a communication channel with no privileged basis.
- **Virtual weights**: the product of one layer's output weights and a
  later layer's input weights, W_I² W_O¹.
- **QK circuit, OV circuit**: per head, W_Eᵀ W_QK W_E (how much each query
  token attends to each key token) and W_U W_OV W_E (how each attended
  token changes the logits), in the one-layer case.
- **Path expansion**: multiplying out a product of layers into a sum over
  end-to-end paths.
- **Q-, K-, V-composition**: a head's query, key or value reading a
  subspace an earlier head wrote to.
- **Virtual attention head**: a V-composed pair, with pattern A^{h₂}A^{h₁}
  and OV matrix W^{h₂}_OV W^{h₁}_OV.
- **Skip-trigram**: a [source] … [destination] → [out] adjustment
  implemented by one head.
- **Induction head**: [a][b] … [a] → [b], minimally by K-composition with a
  previous-token head, which gives a QK term Id ⊗ A^{h₋₁} ⊗ W with W
  same-matching.
- **Privileged basis, bottleneck activation**: a basis the architecture
  makes special (tokens, attention patterns, MLP activations); a
  lower-dimensional activation between higher-dimensional ones (the
  residual stream, value vectors).

## Connections

It rethinks the Distill Circuits programme (Zoom In, LIT-tmplq91w) for
transformers, and says why it must: the residual stream has no privileged
basis, so it is studied through the weights that read and write it, not
through its coordinates. It relates its path expansion to Dong et al.'s
paths through self-attention, to Shazeer's multi-way einsums and to the
logit lens, and reads Primer's depthwise convolution over keys as making
induction heads expressible without K-composition, the point Olsson et
al.'s smeared keys then test (LIT-tmpe7b5o, THEORY-tmp8cat0). Wang et al.'s
IOI circuit (LIT-tmpj9tel) uses its notation and its induction and
previous-token heads.

## Bearing on the record

- **THEORY-tmp8cat0 and THEORY-tmpkd3fq.** This is where the induction
  head and its K-composition mechanism come from. The framework shows the
  mechanism in one two-layer model's weights; the next paper ties it to
  in-context learning across training and sizes. The framework's claim for
  all sizes (C6) is the Proposed THEORY-tmpkd3fq, not something this paper
  supports.
- **THEORY-802, QUESTION-234 and THEORY-018.** "The residual stream doesn't
  have a 'privileged basis'; we could rotate it by rotating all the
  matrices interacting with it, without changing model behavior." That is
  the symmetry under which THEORY-802 says mediating directions are
  underdetermined, and the reason THEORY-018 finds no intrinsic inner
  product on a final-layer representation. The framework's answer is to
  study basis-free objects (W_QK, W_OV, path terms), whose values do not
  depend on the rotation. That is a way to choose units that THEORY-802's
  non-uniqueness cannot touch, at the cost of describing heads, not
  features.
- **QUESTION-tmpivbso, THEORY-tmp1dufu, THEORY-tmp9uzkw.** The framework
  reads a trained model at one time. Its composition scores and eigenvalue
  statistics are computable at every checkpoint, which is what the
  question's circuit-only arm needs. The correction shows how fragile such
  a score can be: a cyclic permutation inside a norm changed which heads
  seemed to compose.
- **THEORY-783 and QUESTION-039.** The framework explains why one-layer
  attention-only models cannot form an induction head (no composition) and
  how architectures such as Primer remove the need for it. That is the
  dependency that Olsson et al.'s smeared keys then use to move the
  transition. It says nothing about training time.
- **THEORY-169.** One-layer copying heads are "a kind of very primitive
  in-context learning", and induction heads a more powerful one. Both are
  conditioning on context with fixed weights, the sense of THEORY-169.
- **Accounts filed.** THEORY-tmphm85g (Active, demonstrated): the path
  expansion. THEORY-tmpb4xka (Active): the two-layer model as measured,
  with the correction.

No instruction for machine-learning practice is drawn; the methods are
interpretability practice, the anthology's (`anthology-candidate`).

## Limitations

- **Toys.** Attention-only models of up to two layers. MLPs, "2/3rds of a
  standard transformer's parameters", are left open, and the authors expect
  that many heads interact with them.
- **Layer norm** is ignored, or folded in as a per-path scale, which makes
  paths through different layers hard to compare.
- **Evidence in interactive figures.** The composition diagram, the
  eigenvalue scatter, the term-importance plots and the attention patterns
  are figures, not tables; the text states what they show.
- **One two-layer model** is analysed, with no seeds, sizes or training
  details reported beyond the architecture.
- **The copying statistic** is not a definition of copying, as the authors
  say.

### Errors and inconsistencies found

- **The composition diagram (the authors' correction).** The record checked
  the mathematical point of the correction: for random factors A, B,
  ‖AB‖_F and ‖BA‖_F differ (in one check, 47.4 and 147.6), while the
  nonzero eigenvalues of AB and BA agree. The bug is as described.
- **"transformer weights are organized into convolutions"** (MLP Layers
  appendix, Why This is Useful): the sentence is about the Distill
  Circuits work on InceptionV1, so it should read conv-net weights. A slip.
- **Notation.** The notation table writes W_QK = W_{Q^T} W_K, and the text
  once says "W_O W_V and W_Q W_K always operate together", dropping the
  transpose it uses elsewhere (W_Qᵀ W_K).
- **Checked and correct.** A 50,000-token vocabulary gives an expanded OV
  matrix of 2.5 × 10⁹ entries. Attention has 4d² parameters per layer and
  an MLP with 4d hidden units 8d², so MLPs are two-thirds of the
  parameters. At layer 25 of 50, with MLPs four times the residual width,
  100 times as many neurons write before as there are dimensions.

## Open questions

- How much of a model with MLPs can be expanded this way, given that MLP
  neurons cannot be linearized through?
- Is the minimal induction circuit typical, or, as the correction
  suggests, usually supplemented by heads that look several tokens back?
- Do virtual heads matter more in deeper models, as the authors speculate?
