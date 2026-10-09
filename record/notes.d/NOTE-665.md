---
number: 665
status: Read
formerly:
- NOTE-tmp86ssm
paper: 'LIT-863'
title: 'On the Emergence of Linear Analogies in Word Embeddings'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the arXiv PDF of v2 (arXiv:2505.18651v2, 23 October
    2025, 21 pp.), text extracted with pdftotext and kept as paper.txt in
    the scratchpad download directory: abstract, §§1–10, Limitations, the
    reference list and Appendices A1–A5. The Kronecker theorem's induction
    (A1), the d = 2 worked example and Table 1, the bilinear form of the
    PMI (§6, A2), the noise, pruning and deletion arguments (§§7–9, A4) and
    the correlated-attribute extension (A5) were followed step by step;
    the eigenvalue products of §5 and the sign of the PMI's constant mode
    were re-derived (see Key results). Figures were read from captions,
    axis labels and text, not from the plotted values. v1 and the authors'
    code were not read.
date: '2026-10-09'
summary: >-
  Derives the parallelogram analogies of word embeddings from a generative
  model of co-occurrence in which words are bundles of independent binary
  attributes: the co-occurrence ratio is then a Kronecker product, and its
  logarithm, the PMI, is a bilinear form of rank at most d + 1 whose
  eigenvectors are affine in the attributes, so a spectral PMI embedding
  is a linear image of the attribute hypercube. Robustness to noise,
  pruning and deletion of a relation's own pairs is argued from eigenvalue
  bounds and simulated; Wikipedia agrees in shape. Every embedding is an
  eigendecomposition, none is trained.
---
<!-- inactive-ok-file: THEORY-185 THEORY-182 THEORY-183 THEORY-019 THEORY-001 THEORY-002 THEORY-159 CLAIM-082 — Proposed; cited as what this reading produced or bears on -->

# NOTE-665: On the Emergence of Linear Analogies in Word Embeddings

## Contribution

Earlier accounts of word-embedding analogies either postulated the ratio
condition p(χ|king)/p(χ|queen) ≈ p(χ|man)/p(χ|woman) (Ethayarajh et al.,
Allen and Hospedales) or assumed an isotropic latent semantic space (Arora
et al., [ANTH-LIT-613](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-613.md)). This paper gives a generative model of the
co-occurrence matrix itself, words as bundles of independent binary
attributes, and computes its spectrum exactly. That turns four empirical
observations into consequences of one assumption: analogies appear in the
top eigenvectors, improve and then saturate with embedding dimension, are
better with the PMI than with the raw ratio, and survive deleting the
relation's own word pairs. It also says which eigenvector carries which
attribute and at what dimension each analogy becomes available.

## Key insight

If each attribute acts on a word's contexts independently and
multiplicatively, the logarithm turns the product into a sum. The PMI is
then a bilinear form in the attribute vectors, log M = const + ηᵀα_i +
ηᵀα_j + α_iᵀDα_j, so every one of its eigenvectors is an affine function
of the attributes. An embedding built from it is a linear image of the
hypercube of attributes, and a linear image of a parallelogram is a
parallelogram. The raw ratio M is a product, not a sum. Its eigenvectors
include products of attributes, and they interleave with the attribute
modes unless the signals are weak and alike.

## Assumptions

- **Binary attributes, all 2^d words.** Word i is α_i ∈ {−1, +1}^d.
  The main analysis assumes every combination is a word; §8 relaxes this to
  a random subset of m ≫ d words.
- **Independent multiplicative effects.** P(i) = ∏_k p_k or (1 − p_k), and
  P(i, j) = P(i)P(j) ∏_k P^(k)(α_i^k, α_j^k), with
  P^(k) = [[1 + s_k, 1 − q_k s_k], [1 − q_k s_k, 1 + q_k² s_k]],
  s_k ∈ [0, 1], q_k = p_k/(1 − p_k) ≤ 1. The parametrisation is forced by
  Σ_j P(i, j) = P(i) (checked). Under it the ratio condition holds
  exactly; the model builds it in.
- **Embedding = truncated eigendecomposition.** W_i = Σ_{S ≤ K} √λ_S v_S(i) u_S,
  the L2-optimal rank-K factorisation M ≈ WᵀW (Eq. 5), and the same for
  log M. No gradient training of any model anywhere in the paper.
- **Weak, narrow signals** for the M results: first order in s_k, and the
  spread of the s_k small enough that the bands do not mix.
- **Symmetric case** q_k = 1 (p_k = ½) for §8, for most simulations, and for
  A5.
- **The robustness sections** take d large with the perturbation's scale
  fixed.

## Key results

- **Theorem (§5, proof in A1).** M = ⊗_k P^(k) in lexicographic word order,
  so its eigenvectors are v_S = v_{a1}^(1) ⊗ … ⊗ v_{ad}^(d) and its
  eigenvalues λ_S = ∏_k λ_{ak}^(k). The proof is a clean induction on d with
  the standard eigen-property of Kronecker products.
- **Bands of M (§5, A4).** At q_k = 1 the factors have eigenvalues 2 and
  2s_k with eigenvectors (1, 1) and (1, −1). So M has λ₀ = 2^d on the
  constant vector, d attribute modes v_k(i) ∝ α_i^k with eigenvalue
  2^(d−1)·s_k(1 + q_k)²/2 = 2^(d−2)s_k(1 + q_k)², then modes ∝ s_k s_k′,
  and so on. The extracted text prints the attribute eigenvalue as
  2^(−(d−2))s_k(1 + q_k)². The product of the factor eigenvalues gives
  2^(d−2), and the d = 2 example (λ₁ = 4s₁) cannot tell them apart.
  Appendix A1 also labels the q = 1 eigenvalues "2 and 2s for the − and +
  cases", the reverse of Eq. 9. Both are slips that change nothing.
- **Analogy from M (§5).** If the s_k are small and narrowly spread and
  K ≤ d + 1, the kept eigenvectors span the constant and attribute modes,
  embeddings are affine in the attributes, and α_D = α_A − α_B + α_C gives
  W_A − W_B + W_C = W_D (Eq. 11). Figure 6 shows accuracy reaching 1 exactly
  when a whole band is included; Figure 7 shows that broadly spread s_k
  never reach it.
- **The PMI (§6, A2).** For a, b ∈ {±1}, log P^(k)(a, b) = δ_k + η_k(a + b) +
  γ_k ab exactly, so log M = δ11ᵀ + ADAᵀ + Aη1ᵀ + 1ηᵀAᵀ (Eq. 12). Result 1:
  rank ≤ d + 1. Result 2: the eigenvectors lie in the span of 1 and the
  attribute columns, so they are affine in the attributes. Result 3: Eq. 11
  holds exactly, whatever the s_k. Result 4: with η = 0, eigenvalues 2^dδ on
  the constant and 2^dγ_k on the attribute modes.
  *My check:* at q_k = 1, δ_k = ½ log(1 − s_k²) < 0 and
  γ_k = ½ log((1 + s_k)/(1 − s_k)) > 0. The constant mode, which the paper
  calls the "top eigenvalue λ₀ = 2^dδ", is negative, and a factorisation
  WᵀW can only keep the d positive attribute modes. That fits the
  simulations' perfect accuracy at K = d (Fig. 2d), not d + 1.
- **Noise (§7, A4).** With symmetric i.i.d. noise ξ of scale σ_ξ,
  ‖ξ‖ ≈ 2σ_ξ2^(d/2), which is small against the attribute eigenvalues
  (order 2^d) and their gaps (order 2^d/d). Weyl's inequality keeps the
  eigenvalues in place, and the paper concludes the eigendecomposition is
  unaffected. Analogies break once the admitted noise modes add up to the
  semantic norm, at K ≈ 2^(d/2)/σ_ξ, and the rescaled curves collapse
  (Fig. 10c).
- **Vocabulary pruning (§8, A4).** For m random words, the nonzero
  spectrum of ADAᵀ restricted to them equals that of the d × d Gram matrix
  D^(1/2)A_SᵀA_SD^(1/2), whose normalised form tends to D as m/d → ∞
  (Marchenko–Pastur). The eigenvalues scale by m/2^d and the eigenvectors
  return to the attribute vectors (Fig. 9). In simulation, 15% of the words
  at d = 12 with multiplicative noise σ_ξ = 0.1 still give perfect accuracy
  for K ≥ d (Fig. 2f).
- **Deleting a relation (§9).** Setting log M′ = 0 on the 2^(d−1) pairs
  that differ only in attribute 1 is a perturbation of Frobenius norm about
  2^(d/2), small against 2^d, so the attribute-1 direction stays. In the
  model, pruning the strongest or the weakest attribute leaves accuracy
  perfect at K = d (Fig. 3c). On Wikipedia, zeroing each family's own pairs
  in the PMI costs little accuracy (Fig. 3b).
- **Ternary attributes (A3).** With a neutral value 0 of frequency f_k,
  first-order perturbation gives eigenvalues 3, 2s_k and 6f_k: the polar
  contrast keeps its binary eigenvalue and a weak neutral-vs-polar mode
  appears.
- **Correlated attributes (A5).** With pairwise factors 1 + s_kk′α^kα^k′,
  normalisation is handled to second order in s, and PMI = δ + AγAᵀ with γ
  not diagonal. The rank is still ≤ d + 1 and eigenvectors are still affine,
  but each one now mixes attributes. The paper calls this "the central
  result".
- **Wikipedia (§§5–6, 9).** For 10,000 words, accuracy on Mikolov et al.'s
  analogy set rises with K, and log(M + 10⁻²) beats M and saturates. The
  PMI spectrum is broad, fitted by a log-normal like the model's with
  broadly spread s_k. The text says the set has 13 families; Figure 3's
  legend lists 14, adding adj-antonym, which Figure 2a lacks.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Under independent multiplicative binary attributes, the co-occurrence ratio M is a Kronecker product with product eigenvectors and eigenvalues | strong (proof) | Theorem, A1 |
| C2 | Under the same model the PMI has rank ≤ d + 1 and eigenvectors affine in the attributes, so its spectral embedding satisfies parallelogram analogies exactly for any signal strengths | strong (proof; elementary) | Eq. 12, Results 1–3 |
| C3 | Embeddings of M give exact analogies only for weak, narrowly spread signals and K ≤ d + 1; broad signals interleave product modes and analogy accuracy rises then falls with K | moderate | first-order expansion §5; simulations Figs. 2c–d, 6, 7 |
| C4 | The analogy subspace survives i.i.d. noise until K ≈ 2^(d/2)/σ | moderate | Weyl bound and scaling argument §7; collapse in Fig. 10 |
| C5 | Eigenvectors, not only eigenvalues, are stable under the noise, pruning and deletion perturbations | weak as argued | asserted from Weyl's eigenvalue inequality; no eigenvector (Davis–Kahan) bound; supported by simulation |
| C6 | Pruning to m ≫ d random words preserves the PMI's semantic spectrum up to scale | moderate | Marchenko–Pastur argument §8; Fig. 9 |
| C7 | Linear analogies survive deletion of all pairs of the relation, in the model and in Wikipedia PMI | moderate | §9 argument; Fig. 3 (deletion at matrix level, not from the corpus) |
| C8 | Real co-occurrence statistics are approximately of this form | weak | visual similarity of matrix blocks (Fig. 1a–b), spectral shape (Fig. 1c), accuracy-curve shapes |

## Method

Two moves. First, write the co-occurrence ratio as a product over
attributes. In lexicographic word order, that makes M a Kronecker product
of 2 × 2 matrices, and its logarithm a sum of rank-one-in-attribute terms,
so both spectra are explicit. Second, treat departures from the model
(noise, missing words, deleted pairs, correlations) as perturbations. Their
operator norm is compared with the semantic eigenvalues, which grow like
2^d (or like m after pruning), and each comparison is checked by simulation
at d = 5 to 12.

## Concepts

- **semantic attribute**: a binary property of a word, after
  feature-listing studies in psychology (Rumelhart and Abrahamson 1973;
  McRae et al. 2005). Its value is ±1, its incidence p_k and its strength
  s_k, the contrast in co-occurrence between matching and opposite values.
- **M**: the co-occurrence ratio P(i, j)/P(i)P(j), not Karkada et al.'s M*
  ([LIT-855](../literature.d/LIT-855.md)); **PMI**: log M.
- **attribute eigenvector** v_k: the eigenvector whose entry for word i is
  proportional to α_i^k. With q = 1 the eigenvectors of M are Walsh
  functions of the attributes.
- **eigenband**: the group of eigenvalues of M of the same order in the
  s_k (attributes, pairs, triples).
- **top-1 analogy accuracy**: how often the nearest vocabulary vector to
  W_A − W_B + W_C is W_D (Eq. 13). The query words are not excluded, as
  written.

## Connections

The four observations it explains come from Karkada et al. ([LIT-855](../literature.d/LIT-855.md), cited
under its v1 title) for (i)–(ii), Pennington et al. and Torii et al. for
(iii), and Chiang et al. (2020) for (iv). It argues against Arora et al.'s
random-walk model ([ANTH-LIT-613](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-613.md)): an isotropic latent space would give a
PMI with d nearly equal eigenvalues, but the measured spectrum is broad.
Its PMI result is the exact version of the ratio argument of Ethayarajh,
Duvenaud and Hirst, which needs the full-rank PMI. The reference list
misattributes that paper to "Kawin Ethayarajh, Dan Jurafsky, and Ranjay
Krishna … EMNLP 2019"; Crossref gives Ethayarajh, Duvenaud and Hirst, ACL
2019, DOI-10.18653/v1/p19-1315. Its sequel, Karkada, Korchinski, Nava, Wyart and Bahri
([LIT-860](../literature.d/LIT-860.md), read in [NOTE-664](NOTE-664.md)), replaces binary attributes by positions on a
continuum and Kronecker products by circulant and Toeplitz blocks. Its
Appendix D puts both into one PMI and shows the two subspaces are
orthogonal. Hierarchical attributes are left to the random hierarchy model
of Cagnetta et al., which the authors name as future work.

## Bearing on the record

- **It produces [THEORY-185](../theory.d/THEORY-185.md)**: under independent multiplicative
  binary attributes, a spectral PMI embedding is an affine image of the
  attribute hypercube, so linear analogies hold exactly, while the raw
  ratio keeps them only for weak, alike signals. The record held this for
  continuous attributes ([THEORY-183](../theory.d/THEORY-183.md)) but not for binary ones.
- **[THEORY-182](../theory.d/THEORY-182.md)**: [NOTE-660](NOTE-660.md) asked whether [LIT-855](../literature.d/LIT-855.md)'s spiked-random-matrix
  picture of analogy vectors could be derived from M* rather than fitted.
  This paper derives parallelogram structure from the spectrum, but for a
  generative model of M, not of M*, and for an eigendecomposition, not a
  trained model. M* agrees with the PMI to third order ([NOTE-660](NOTE-660.md)). So the
  chain "word2vec factorises M* ≈ PMI; the PMI under this model is affine
  in the attributes" is plausible but is not closed by either paper. Nothing
  here bears on [THEORY-182](../theory.d/THEORY-182.md)'s promote_when.
- **[THEORY-183](../theory.d/THEORY-183.md)**: the binary-attribute counterpart of that account. Both
  explain a geometry by a structure of the co-occurrence statistics, read
  off by a spectral embedding. Both share the same gap: no intervention on
  the statistics.
- **[THEORY-019](../theory.d/THEORY-019.md)**: at q_k = 1 each factor is invariant under exchanging
  the two values of its attribute, so M commutes with (ℤ/2)^d acting by
  sign flips. Its eigenvectors are the group's characters, the Walsh
  functions, which are one-dimensional real irreducibles, so no degeneracy
  is forced. With q_k ≠ 1 the symmetry is broken and the eigenvectors
  deform (Eq. 10) but remain Kronecker products. This is my reading, not
  the paper's.
- **[THEORY-001](../theory.d/THEORY-001.md)**: that the skip-gram optimum is shifted PMI is the reason
  the log-domain target is the one that matters. This paper shows why that
  target, unlike the ratio itself, is linear in additive attributes.
- **[THEORY-002](../theory.d/THEORY-002.md)**: with nearly equal γ_k, the attribute eigenvectors rotate
  freely within their span, and the analogies survive because they depend
  only on the span. The model's prediction is a Gram matrix up to rotation,
  as that account says.
- **[CLAIM-082](../claims.d/CLAIM-082.md) and [THEORY-159](../theory.d/THEORY-159.md)** (for the coordinator; no claim edited): the
  model is a formal case of identity by opposition within a system. Each
  word is nothing but a bundle of binary contrasts (±1 on each attribute),
  and its embedding is an affine image of its place in the hypercube of
  those contrasts. It is closer to Saussure's opposition than the
  co-occurrence similarity [THEORY-159](../theory.d/THEORY-159.md) warns against, and it resembles the
  binary-feature analyses of structural linguistics, though the paper cites
  feature norms from psychology, not structuralism. §9 adds that a contrast
  (masculine/feminine) is still recovered when every pair that differs only
  in it is deleted, so it is carried by each word's relations to the rest
  of the vocabulary. Two qualifications, as with [LIT-860](../literature.d/LIT-860.md): the attributes
  are posited as primitives of the generative model, so the relata are
  given in advance ([THEORY-032](../theory.d/THEORY-032.md)'s point about "determined by relations"),
  and many are properties of what the words denote (gender, royalty,
  country and capital). It supports "fixed within a system" without setting
  relation against reference.
- **ML practice**: none. The paper gives no instruction. Its Discussion
  points to linear subspaces in language models, but tests nothing there.
  The anthology's `concept-geometry` topic could hold it, hence the flag.

## Limitations

- No trained model. Every embedding, in simulation and on Wikipedia, is a
  truncated eigendecomposition of M or log(M + ε). That word2vec or GloVe
  behaves this way rests on other work ([LIT-855](../literature.d/LIT-855.md), Levy and Goldberg).
- The attributes are posited, not recovered. Nothing fits d, the s_k or
  any word's attribute vector to the Wikipedia data. The agreement is in
  the shapes of spectra and of accuracy-versus-K curves, and in a visual
  likeness of matrix blocks.
- The ratio condition holds exactly in the noiseless model. It is
  assumed, then shown to survive perturbation, not derived from anything
  more basic about language. The authors call the model "a great
  simplification" and name polysemy and hierarchy as missing.
- Perturbation arguments bound eigenvalues (Weyl), and the conclusion
  about eigenvectors is asserted. No gap-dependent eigenvector bound is
  given, though the attribute subspace as a whole is what matters, and
  that is better protected than individual eigenvectors.
- The "removal" experiments set PMI entries to zero, which means
  independence, in the matrix. That is not Chiang et al.'s removal of
  sentences from the corpus, which would also change other words'
  counts.
- The Wikipedia set-up is thinly described in the text: corpus size and
  window are not given, and are left to the code.
- Small slips: the attribute eigenvalue's exponent sign, the swapped ±
  labels in A1, the constant PMI mode called the top eigenvalue though
  δ < 0 at q = 1, "13 families" against a 14-family legend, and the
  misattributed reference [30].

## Open questions

- Do real co-occurrence statistics satisfy the model's additivity in the
  log domain? A direct test would measure, for word quadruples of an
  analogy family, how far the PMI rows depart from additivity across all
  context words, and whether that departure predicts which families a
  spectral embedding completes. The paper's evidence does not do this.
- Does a trained word2vec, with untied weights and its own negative
  sampling, show the same attribute-affine subspace at moderate K? This is
  where it would meet [THEORY-182](../theory.d/THEORY-182.md)'s promote_when.
- Removal from the corpus rather than from the matrix: does the relation
  survive when the sentences are deleted, as in Chiang et al.? That would
  test the robustness claim on the data rather than on the matrix.
- Hierarchical and polysemous attributes: what spectrum does a random
  hierarchy model give the PMI, and does it keep the affine property?
