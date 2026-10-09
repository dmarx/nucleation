---
number: 652
status: Read
formerly:
- NOTE-tmp54kkt
paper: 'LIT-849'
title: 'Relative representations enable zero-shot latent space communication'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the arXiv PDF of v2 (7 March 2023, 26 pp., "Published
    as a conference paper at ICLR 2023"), text extracted with pdftotext.
    Read: abstract, §§1–6, acknowledgements, reproducibility statement,
    the reference list, and Appendix A.1–A.6 with Tables 7–18. Nothing was
    skipped. Figures 1, 3–11 are plots or image grids that survive only as
    captions and axis labels, so their content is taken from captions and
    prose; every table survives and its values are quoted from the
    extraction. The v1 of 30 September 2022 was not read. ASIF (Norelli et
    al. 2022), which the paper credits for parallel anchors, was not read.
date: '2026-10-09'
summary: >-
  Represents each sample by its cosine similarities to a fixed set of
  anchor samples. That vector is invariant by construction to every
  cosine-preserving map of the latent space (rotations, reflections,
  global and even per-sample positive rescaling), not to translations or
  general linear maps. With anchors matched across encoders it lets a
  decoder trained on one encoder run untrained on another, across seeds,
  architectures, latent sizes and languages: far better than raw latents,
  but with large and uneven losses. The assumption that such spaces differ
  by an angle-preserving map is never tested directly, and the evidence
  supports it only approximately.
---
<!-- inactive-ok-file: THEORY-175 THEORY-004 THEORY-008 THEORY-112 CLAIM-125 CLAIM-082 — Proposed; cited as the accounts and claims this reading bears on, not as settled -->

# NOTE-652: Relative representations enable zero-shot latent space communication

## Contribution

A fixed, parameter-free re-encoding of a network's latent space: each
sample becomes the vector of its cosine similarities to a set of anchor
samples. Downstream modules trained on that vector can be attached, with no
training or fine-tuning, to a different encoder that computes the same
vector, where "the same" needs a correspondence between the two sides'
anchors. The authors claim, "for the first time", zero-shot stitching of
components from different seeds, architectures, latent widths and
languages, and show it on images, text and graphs. Before this, stitching
(Lenc & Vedaldi, [LIT-363](../literature.d/LIT-363.md); Bansal et al.; Csiszárik et al.) used a trained
stitching layer.

## Key insight

If two latent spaces differ only by a map that preserves angles, then each
point's angles to a shared set of reference points are the same in both,
so those angles are a coordinate system both spaces share. The anchors are
the reference points, and coordinates relative to them replace absolute
coordinates. What moves between models is the profile of similarities, not
the vectors.

## Assumptions

- **The core assumption (§3).** Changing the training factors φ (seed,
  shuffling, hyperparameters) transforms the latent space by some T with
  ∠(e_x, e_y) = ∠(Te_x, Te_y) for every pair of training samples. The paper
  says it "might seem too restrictive" and offers the experiments as
  evidence. In §§5.2–5.3 it is extended, without comment, to changes of
  architecture, of training data and of language. For encoders of
  different width (384, 768, 1280), T must be a map between spaces of
  different dimension, so the assumption becomes "the two encoders' cosine
  kernels agree on the data". That is my restatement, not the paper's.
- **Centred latents.** Cosine is not translation-invariant. The paper
  assumes "NNs commonly employ normalization techniques (e.g.,
  InstanceNorm)" to centre the space. Whether the encoders used actually do
  so (RoBERTa and BERT [CLS] states, ViT features) is not checked.
- **Anchors.** Within one domain, anchors are a subset of training data,
  drawn uniformly at random in the main experiments (300 for word
  embeddings and Cora; 500 for the AEs, whose latents are also 500-wide;
  768 for cross-lingual text). The count used in §5.3 is not stated, except
  that it is below RexNet's 1280 and, by implication, at least 768. Across
  domains, a partial correspondence Γ between subsets of X and Y supplies
  **parallel anchors** A and Γ(A). **OOD anchors** come from outside the
  training distribution, and need the same encoder on both sides or a
  correspondence.
- **No backpropagation through anchors** when training end-to-end
  (A.5.4).

## Key results

Proved:

- **Invariance (eq. 4).** S_C(a, b) = a·b / (‖a‖‖b‖) = cos θ, and "cos θ
  does not change if we apply the same angle-preserving transformation T
  to two vectors". So r_x is unchanged under rotations, reflections and
  rescaling. This is the paper's only formal statement, and it is
  immediate. The paper uses "guarantee" for it ("guarantee, in practice,
  invariance to latent isometries and rescalings", abstract), and the
  guarantee is conditional on the latent space changing by such a map.

Shown empirically (all means ± std over seeds as stated):

- **Word embeddings (Table 1; Table 7).** FastText vs Word2Vec, ≈20k
  shared words, 300 parallel anchors (the same words), 10 seeds, K = 10.
  Absolute: Jaccard 0.00, MRR 0.00, cosine 0.01. Relative, FT→W2V: Jaccard
  0.34 ± 0.01, MRR 0.94, cosine 0.86; W2V→FT: 0.39, 0.98, 0.86. Anchor
  selection by uniform, farthest-point, k-means or frequency gives similar
  numbers; the 1,000 most frequent words (after 400 stopwords) are worst
  (Jaccard 0.27).
- **CIFAR-10, ViT-base vs ViT-small (Table 8).** 500 anchors. Relative:
  Jaccard 0.10–0.12, MRR 0.25–0.39, cosine 0.96–0.97. Absolute comparison
  is undefined (dimensions 768 vs 384).
- **Performance proxy (§4.2, Fig. 3).** ≈2,000 Cora GCNs over a sweep of
  seed, epochs, depth, dropout, activations, optimiser, learning rate and
  convolution type (Table 10). Mean cosine of a model's relative node
  embeddings to the reference model's tracks accuracy; "mean Pearson
  correlation over all models is 0.955, after filtering out the models
  having best validation accuracy below 0.5".
- **Cost of training on relative vectors (Table 2).** Weighted F1 over 6
  seeds, relative vs absolute: MNIST 97.91 vs 97.95; F-MNIST 90.19 vs
  90.32; CIFAR-10 87.70 vs 87.85; CIFAR-100 66.72 vs 68.88; Cora 0.89 vs
  0.90; CiteSeer 0.77 vs 0.78; PubMed 0.91 vs 0.91.
- **Stitching across seeds (Table 3).** Reconstruction MSE, 5 seeds,
  averaged over four datasets. AE: absolute 1.58 unstitched, 100.56
  stitched; relative 2.78 unstitched, 8.16 ± 3.53 stitched (CIFAR-100:
  18.03 ± 12.46). VAE: absolute 2.84 / 91.27; relative 5.22 / 14.97 ±
  6.37.
- **Stitching across architectures (Table 5).** Four 768-wide English
  transformers, weighted F1, 5 seeds. Relative, unstitched vs stitched:
  TREC 88.08 vs 75.89 ± 5.38; DBpedia 97.42 vs 80.47 ± 21.14; Amazon
  coarse 85.08 vs 72.37 ± 7.32; Amazon fine 48.92 vs 33.24 ± 7.21.
  Absolute stitched: 21.49, 6.96, 49.58, 19.01.
- **Stitching across languages (Table 4; all pairs in Tables 15–16).**
  Language-specific RoBERTas (en, es, fr, ja), Amazon reviews, binary
  task. English decoder: en 90.06, es 82.78, fr 78.49, ja 65.72 F1 with
  translated anchors; 90.45, 78.53, 70.41, 66.31 with WikiMatrix anchors.
  Absolute: 91.54, 43.67, 54.41, 48.72. Japanese is the weakest pair in
  both directions (Japanese decoder reading Spanish: 70.37 ± 6.94
  translated, 58.54 Wikipedia). On the five-class task stitched F1 is
  33–52 against 51–62 unstitched.
- **Multilingual control (Table 17).** On XLM-R, relative is below
  absolute in every one of the 16 decoder–encoder pairs (e.g. Japanese
  decoder, English encoder: 39.46 vs 59.53).
- **Stitching across image encoders (Table 6, Table 18).** Three ViTs
  (768, 384, 768) and RexNet (1280), frozen, pretrained on ImageNet;
  decoders trained on CIFAR-100 coarse or ImageNet1k. Diagonal: relative
  within 2.1 points of absolute. Off-diagonal on ImageNet: 30.78–62.21 F1,
  against 72.61–81.88 on the diagonal. Absolute stitching between the two
  768-wide ViTs: 0.07–6.21. With RexNet's decoder, 37.39–43.75 on
  ImageNet against 72.61. The paper ties this to RexNet being the only
  encoder whose dimension exceeds the number of anchors.
- **Anchor count (Fig. 6).** With a frozen encoder (CIFAR-100) accuracy
  rises monotonically with the number of anchors. Trained end to end
  (Cora) it does not, and some runs collapse.
- **Quantised similarity (A.3, Fig. 7).** Agglomerative clustering of the
  absolute embeddings before computing similarities lowers a pairwise
  distance score between FastText and Word2Vec from 1.24 to 1.02.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Cosine relative representations are invariant to any map applied to the latent space that preserves cosines (rotations, reflections, rescaling) | strong (immediate from the definition) | eqs 3–4 |
| C2 | Different trainings of the same model on the same data produce latent spaces related by an approximately angle-preserving map | moderate, indirect | Figs 1, 5 (pictures); Table 3 (stitching works); never tested by fitting an orthogonal map |
| C3 | The same holds across architectures, training corpora and languages, given matched anchors | weak to moderate | Tables 1, 4–6, 8; neighbourhood overlap 0.10–0.39; stitched accuracy well below unstitched in many pairs |
| C4 | Relative representations enable zero-shot stitching that raw latents cannot | strong, as a comparison | Tables 3–6: relative stitching beats absolute in every pair where absolute can be run, except on XLM-R (Table 17) |
| C5 | Training with relative representations is not detrimental to performance | moderate | Table 2: losses ≤ 2.2 F1; but relative AEs/VAEs reconstruct worse unstitched (Table 3) |
| C6 | Similarity of relative spaces to a good reference model predicts performance | moderate, one task | Fig. 3, Cora only, Pearson 0.955 after filtering weak models |
| C7 | Vector quantisation gives "invariance with guaranteed bounds" to bounded distortion | not supported here | A.3 states no bound and proves nothing; one score on one pair of embeddings |
| C8 | The paper is the first to show zero-shot stitching across seeds, architectures or languages | assertion | §1, §5.2 |

## Method

Compute absolute embeddings with a frozen or trained encoder; embed the
anchors with the same encoder; take cosine similarity of each embedding to
each anchor embedding; feed that |A|-vector to the downstream module. To
stitch, train decoder D on encoder E₁'s relative vectors, then at test time
compute relative vectors with encoder E₂ against E₂'s embeddings of the
corresponding anchors (the same samples, or Γ of them), and pass them to D
unchanged. Variants: OOD anchors; quantised similarity (A.3).

## Concepts

- **absolute representation**: e_x = E_θ(x), the encoder's latent vector.
- **relative representation**: r_x = (sim(e_x, e_{a₁}), …, sim(e_x,
  e_{a_|A|})), with sim the cosine similarity throughout the experiments.
- **anchors**: a fixed subset A of samples whose embeddings serve as
  reference points; each anchor is one coordinate of r_x.
- **parallel anchors**: anchors A ⊆ P_X in one domain and Γ(A) in another,
  given by a partial correspondence Γ: P_X → P_Y (credited to Norelli et
  al. 2022, ASIF).
- **OOD anchors**: anchors from outside the encoder's training
  distribution.
- **zero-shot stitching**: composing an encoder with a decoder trained on
  a different encoder, with no training or fine-tuning of either.
- **latent communication**: comparing or exchanging latent embeddings
  between separately trained models.
- **angle-preserving transformation**: the paper's term for the T it
  assumes; it names rotations, reflections and rescaling and does not
  define the class further.

## Connections

The paper places itself after model stitching (Lenc & Vedaldi 2015, which
the record holds as [LIT-363](../literature.d/LIT-363.md) with [NOTE-309](NOTE-309.md); Bansal et al. 2021; Csiszárik
et al. 2021) and after work on representational similarity (Kornblith et
al.'s CKA, Li et al.'s convergent learning, Vulić et al. on whether word
vector spaces are isomorphic). It compares itself to kernel methods: it
uses inner products, but explicitly and with no learnable parameters.
Parallel anchors come from ASIF (Norelli et al. 2022). Olah's 2015 blog is
credited with first noticing that retrained latent spaces differ by a
near-isometry.

## Bearing on the record

- **The invariance, made exact (my derivation, filed as [THEORY-175](../theory.d/THEORY-175.md)).**
  The paper's class "angle-preserving" can be stated exactly. r_x is
  unchanged by a map f of the latent space exactly when cos(f(u), f(v)) =
  cos(u, v) for every sample u and anchor v. Any per-sample positive
  rescaling, x ↦ c(x)x with c > 0, does this, and it is non-linear, so the
  invariance is larger than "isometries and rescalings". The linear maps of
  a space onto itself that preserve every cosine are exactly the orthogonal
  maps times a positive scalar (with finitely many anchors, more maps
  preserve the finitely many cosines used). It excludes translations (the paper says so) and general
  invertible linear maps (the paper does not say so). Conversely, by
  [THEORY-004](../theory.d/THEORY-004.md)'s theorem (a representation is fixed by its kernel up to an
  orthogonal map), two encoders whose relative vectors agree with the
  whole data set as anchors have normalised representations that differ by
  an orthogonal map. With |A| below the latent dimension, as for RexNet
  here, equal relative vectors fix much less.
- **[THEORY-018](../theory.d/THEORY-018.md).** That account says a final-layer softmax representation is
  identified only up to an invertible linear map, so no inner product, and
  so no cosine, is intrinsic there. Cosine relative representations do not
  remove a GL(d) ambiguity; they remove only its conformal-orthogonal part.
  There is no conflict with the paper's results. The paper reads [CLS] or
  pooled hidden states and autoencoder bottlenecks, not the
  softmax-identified final layer, which [THEORY-018](../theory.d/THEORY-018.md) confines itself to.
  Taken with [THEORY-018](../theory.d/THEORY-018.md), its empirical success says only that, for these
  encoders, training did not use the linear freedom the softmax leaves
  open. It does not say the freedom is absent.
- **[LIT-363](../literature.d/LIT-363.md) (Lenc & Vedaldi; [NOTE-309](NOTE-309.md)).** There, stitching fits a general
  linear map E from paired data, and the identity map fails completely.
  Here no map is fitted, but parallel anchors are paired data (300–768
  pairs), and the method can only absorb cosine-preserving maps. "Zero-shot"
  moves the correspondence from a training set into the anchor set; it does
  not remove the need for one.
- **[THEORY-112](../theory.d/THEORY-112.md).** At a single layer, the hidden-unit permutations and the
  residual-stream orthogonal map that [THEORY-112](../theory.d/THEORY-112.md) factors out of weight space
  act on activations as orthogonal maps, so relative representations at
  that layer are blind to them by construction. The GL symmetries of linear
  networks that the same account cites (Bo Zhao et al., [LIT-655](../literature.d/LIT-655.md)) are not
  absorbed. My connection, not the paper's.
- **[LIT-302](../literature.d/LIT-302.md) (Platonic Representation Hypothesis) and [THEORY-008](../theory.d/THEORY-008.md).** Relative
  vectors are rows of a cosine kernel between data and anchors. The paper's
  cross-model comparisons (Tables 1, 8) are kernel-alignment measurements
  of the kind [LIT-302](../literature.d/LIT-302.md) gathers, and they show the same split: global
  similarity profiles agree (cosine 0.86–0.97) while nearest-neighbour
  identity mostly does not (Jaccard 0.10–0.39). This is evidence of
  convergence at the level of similarity profiles, not of exact sameness
  of neighbourhoods. [THEORY-008](../theory.d/THEORY-008.md) says what a regularised linear readout can
  decode is a function of the normalised kernel, which is consistent with a
  decoder that reads only kernel rows transferring when the kernels agree.
- **On the line `pragmatic-transport` (for the coordinator; claims not
  edited).**
  - [CLAIM-082](../claims.d/CLAIM-082.md) (significance by contrasts within a system): the paper is a
    working instance of identifying a sample by its similarities to other
    samples rather than by its own coordinates. But the construction
    succeeds across systems only when the anchors are matched by an
    external correspondence (translation, the same images, the same
    words). It is contrast plus a fixed correspondence on the reference
    points, the same qualification [CLAIM-082](../claims.d/CLAIM-082.md) already records from Bergen,
    Goodman and Levy ([LIT-809](../literature.d/LIT-809.md)). On XLM-R, where a shared absolute space
    exists, the relational encoding loses information.
  - [CLAIM-125](../claims.d/CLAIM-125.md) (when directed transport preserves decision-relevant
    information): the paper gives an empirical case of transport between
    representation spaces through a partial correspondence, with the
    preserved information measured by downstream task performance. It
    gives no characterisation and no informativeness order, so it does not
    meet that claim's `defeated_if`.
- **ML practice.** The method is an ML technique for reusing and comparing
  trained components, and an anthology topic on representation learning
  could hold it; `anthology-candidate` is on the LIT.

## Limitations

- The core assumption is never tested directly (for example, by
  orthogonal Procrustes between two spaces and its residual). The evidence
  is downstream success and pictures.
- No error analysis of when stitching fails: the Japanese pairs, RexNet as
  decoder, DBpedia's ± 21 F1 and the CIFAR-100 AE's ± 12.5 MSE are
  reported but not explained, beyond the anchor-count remark.
- The anchor count for §5.3 is not stated; Fig. 6 is the only analysis of
  count, and it is "preliminary".
- Translation invariance is assumed from normalisation without checking
  the encoders used.
- "Our work proves …" (§6) refers to experiments. A.3's "guaranteed
  bounds" states no bound.
- Table 6's text calls RexNet a transformer; Table 14 lists it as a
  RexNet, a convolutional network.
- Single tasks per claim in places: the performance proxy is shown on
  Cora only.

## Open questions

- How far from angle-preserving are the maps between independently trained
  spaces? The residual of the best orthogonal map, against the best
  general linear map, on the same pairs would answer it, and would say how
  much of the stitching loss is non-conformal distortion and how much is
  anchor coverage.
- Do encoders whose identifiable symmetry is larger than O(d) ([THEORY-018](../theory.d/THEORY-018.md)'s
  softmax output) defeat cosine relative representations, and does a
  similarity invariant to that larger group (for example, cosine after
  whitening by the data covariance) recover stitching there?
- What anchor set suffices: is |A| ≥ latent dimension the threshold the
  RexNet result suggests, and how many parallel anchors does a language
  pair need?
