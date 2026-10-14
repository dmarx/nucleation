---
number: 738
status: Read
formerly:
- NOTE-tmp6dvmv
paper: LIT-253
title: 'Nielsen et al. — When Does Closeness in Distribution Imply Representational Similarity?'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv v2 PDF (2506.03784v2, 17 October 2025, 53
    pp., the NeurIPS 2025 camera-ready), text extracted with pdftotext:
    §§1–6, the formal statements and proofs in Apps B, C.1, C.2, E.1–E.7,
    and the experimental details in App. F. The NeurIPS checklist was
    skimmed. Figures were not seen; their content is taken from captions
    and text. The identity between m_SVD and normalized Bures similarity
    under Connections is this reader's, not the paper's; it was checked by
    script on random data (200 samples, 6 dimensions; the two agree to
    about 10⁻⁷).
date: '2026-10-14'
summary: >-
  For softmax models p(y|x) ∝ exp(f(x)ᵀg(y)), equal distributions fix the
  embeddings up to an invertible linear map, but KL closeness does not:
  by making the unembedding norm large, two models' KL divergence goes to
  zero while their embeddings stay fixed and are not linearly related. A
  log-likelihood variance distance does bound a representational
  dissimilarity, d_LLV ≤ ε ⇒ d_f,g ≤ 2Mε. Whether closeness in
  distribution implies similar representations depends on which distance
  is used.
---
<!-- inactive-ok-file: THEORY-002 QUESTION-027 CLAIM-193 — Proposed or Open; the theory, claim and question this reading bears on, open -->

# NOTE-738: Nielsen et al. — When Does Closeness in Distribution Imply Representational Similarity?

## Contribution

Exact identifiability for softmax models was known: equal conditional
distributions fix embeddings and unembeddings up to an invertible linear
map. The paper asks whether this holds approximately, and shows that it
depends on the distance. Under KL divergence it fails. Two models can be
arbitrarily close in KL, and both can be arbitrarily close to zero loss,
while their embeddings are not linearly related. Under a new
log-likelihood variance distance it holds: closeness bounds a
representational dissimilarity built for this model class. This is the
first such upper bound, by the authors' account.

## Key insight

KL divergence weights each difference in log-probability by the
probability of the label. When the softmax saturates, almost every label
has negligible probability, so the two models' log-probabilities on those
labels can differ greatly at almost no cost in KL. But under Lemma 4.1 it
is exactly those log-probability differences, standardized, that fix the
embeddings up to a linear map. A distance that weights them evenly, by
their variance over inputs, controls the representation. KL does not.

## Assumptions

- **Model class (eq. 1).**
  p_f,g(y|x) = exp(f(x)ᵀg(y)) / Σ_y′ exp(f(x)ᵀg(y′)), with f, g into ℝᴹ
  treated as nonparametric, and finitely many labels. The class covers
  autoregressive LMs, BERT, CPC and softmax classifiers. Only the final
  embedding and the unembedding are in view. The paper says that earlier
  layers would need identifiability results that do not yet exist (§6).
- **Diversity (Def. 2.1).** There are x₁…x_M and y₁…y_M such that the
  displaced embeddings f₀(xᵢ) = f(xᵢ) − f(x₀) and the displaced
  unembeddings g₀(yᵢ) = g(yᵢ) − g(y₀) are each linearly independent. It
  needs |Y| > M. The authors note it may fail for image classifiers with
  fewer classes than dimensions.
- **Theorem 3.1 (formal, App. C.1).** M ≥ 2, k = |Y| ≥ M + 1.
  - (i) All unembeddings have norm ρ.
  - (ii) Each f(xᵢ) has a unique label of largest cosine, and that cosine
    is positive.
  - (iii) ‖f′(x)‖ = ‖f(x)‖.
  - (iv) Each f′(x) makes the same angle with g′(argmax) as f(x) does
    with g(argmax).
- **Assumption 4.3 and Theorem 4.7.**
  - Sets X_LLV and Y_LLV are fixed, with Y_LLV holding all labels but one,
    so that log p(y|x) − log p(y|x₀) is not constant in y and
    log p(y|x) − log p(y₀|x) is not constant in x.
  - The L, L′, N, N′ matrices built from these sets are invertible, which
    is stronger than diversity.
  - The covariances Σ_z₁z₁, Σ_w₁w₁ and cross-covariances Σ_z₁z₂, Σ_w₁w₂
    are non-singular.
  - The same pivots and sets must be used for every model compared.

## Key results

- **Theorem 2.2 (linear identifiability, from Khemakhem et al., Lachapelle
  et al., Roeder et al.; proof in App. B).** If (f, g) satisfies
  diversity and p_f,g = p_f′,g′ for all (x, y), then f(x) = Af′(x) and
  g₀(y) = A⁻ᵀg′₀(y), with A = L⁻ᵀL′ᵀ invertible. L has columns g₀(yᵢ).
  The embedding is fixed up to GL(M), and the unembedding up to the paired
  A⁻ᵀ and a translation.
- **Theorem 3.1 (KL closeness is not enough).** Under (i)–(iv),
  d_KL(p_f,gρ, p_f′,g′ρ) → 0 as ρ → ∞, where
  d_KL(p, p′) = E_x∼p_D[D_KL(p(y|x) ‖ p′(y|x))].
  - For k ≥ M + 2 the construction swaps the unembeddings of two labels,
    −ρe₁ ↔ −ρe₂, and rotates the corresponding embedding clusters to
    match. For k = M + 1 it moves one label instead.
  - Two input sequences converge to the same point but map to different
    limits, so any τ with τ(f(x)) = f′(x) is discontinuous and is not an
    invertible linear map.
  - The authors note: "if both f and f′ are injective, then either f or f′
    has to be non-continuous."
  - The mechanism is saturation. Both conditionals tend to one-hot on the
    same argmax label, and the models differ in how they rank the other
    labels.
- **Corollary 3.2 (near-maximum likelihood is not enough; App. C.2).**
  With one label per input and the same conditions, NLL(p_f,g) → 0 and
  NLL(p_f′,g′) → 0 as ρ → ∞, while the embeddings are related as in
  Thm 3.1.
- **How far apart, measured not proved (Table 1).** On the constructed
  2-D models, as ρ goes from 3 to 18:
  - d_KL falls from 0.8866 to 0.0001;
  - d_LLV stays at about 1.317;
  - mean canonical correlation stays between 0.0004 and 0.0010;
  - max d_SVD stays between 0.9995 and 0.9999.
  The theorem itself proves only "not an invertible linear
  transformation". The size of the dissimilarity is shown numerically.
- **Lemma 4.1 (App. E.1).** For any two diverse models,
  f(x) = Ãf′(x) + h_f(x), with Ã = L⁻ᵀS⁻¹S′L′ᵀ and h_f(x) = L⁻ᵀS⁻¹ε_y(x).
  ε_yᵢ(x) is the difference between the two models' standardized log-odds
  log p(yᵢ|x) − log p(y₀|x), each divided by its standard deviation over
  x. Corollary E.2 gives Var_x[ε_yᵢ(x)] = 2(1 − Corr[Lᵢf(x), L′ᵢf′(x)]).
- **Definition 4.4 (log-likelihood variance distance).**
  d^λ_LLV(p, p′) = max{t₁, t₂, λt₃, λt₄}.
  - t₁ is the largest standard deviation over x of a difference of
    standardized log-probabilities, over labels in Y_LLV.
  - t₂ is the same over y, for inputs in X_LLV.
  - t₃ and t₄ are differences of the standardizing ψ's.
  - App. E.2 proves it is a metric. The experiments use λ = 10⁻⁵.
- **Definition 4.5 and Lemma E.7.** For standardized z′, w′,
  m_SVD(z, w) = (1/M) Σᵢ Cov[uᵢᵀz′, vᵢᵀw′], the mean singular value of
  Σ_z′w′, and d_SVD = 1 − m_SVD. The lemma, by Weyl's inequality, gives
  m_SVD ≥ 1 − √(M Σ_l Var[z′_l − w′_l]).
- **Definition 4.6.**
  d_f,g = max{d_SVD(Lᵀf(x), L′ᵀf′(x)), d_SVD(Nᵀg(y), N′ᵀg′(y))}, where
  N has columns f₀(xⱼ). It is constant on ∼L classes (Lemma E.8). It is
  zero iff Lᵀf(x) = S⁻¹OS′L′ᵀf′(x) + a and the matching relation holds
  for the unembeddings, with O orthogonal and S, S′ the diagonal
  standardizers (eq. 234). That is a subset of GL(M), unlike CCA's
  invariance.
- **Theorem 4.7 (App. E.6).** Under the conditions above, for any λ > 0,
  d^λ_LLV(p_f,g, p_f′,g′) ≤ ε ⇒ d_f,g((f, g), (f′, g′)) ≤ 2Mε. The bound
  is non-vacuous only for ε < 1/(2M). The authors call it "not tight":
  in Fig. 16 the dissimilarity grows sub-linearly.
- **Experiments.**
  - *CIFAR-10, 2-D representations, ResNet18 embedding (§5.1).* Two
    retrainings permute some label clusters: "truck" sits between
    "automobile" and "ship" in one and between "automobile" and "horse"
    in the other.
    - Those two have d_KL 1.13 and 1.12, test losses 1.19 and 1.18,
      d_LLV about 1.55 and mCCA 0.55.
    - Neighbour pairs such as automobile–truck and cat–dog are stable
      across all ten seeds. Others vary.
  - *Synthetic 2-D data, 4–18 classes (§5.2).* Wider networks (16 to 256
    units) give lower mean and variance of both d_LLV and d_f,g.
  - *The bound in practice (§5.3, App. F.6).* It holds on every
    constructed pair and every trained synthetic pair where it is
    non-vacuous. For the CIFAR-10 models it is vacuous.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Equal softmax distributions fix embedding and unembedding up to f = Af′, g₀ = A⁻ᵀg′₀ | strong | Thm 2.2, proof in App. B (prior result, restated) |
| C2 | KL divergence between two models can go to zero while their embeddings stay fixed and not linearly related | strong | Thm 3.1, constructive proof, App. C.1 |
| C3 | Two models can both approach zero cross-entropy on deterministic labels with embeddings not linearly related | strong | Cor. 3.2, App. C.2 |
| C4 | In that construction the embeddings are far from linear equivalence, not merely unequal | moderate | Table 1 (mCCA ≈ 0.001, d_SVD ≈ 1); not proved |
| C5 | d_LLV ≤ ε implies d_f,g ≤ 2Mε | strong | Thm 4.7, App. E.5–E.6 |
| C6 | A mechanism like the construction occurs in trained CIFAR-10 classifiers | weak | one pair of 2-D retrainings, Fig. 3; KL there is 1.1 nats, not small |
| C7 | Wider networks learn closer distributions and more similar representations | weak | synthetic 2-D task, ≤ 20 seeds per width, Fig. 3 right, App. F.7 |

## Concepts

- **Identifiability class.** The set of models related by ∼L, eq. 5. Under
  diversity, it is in one-to-one correspondence with distributions in
  P_Θ.
- **Representational similarity.** Closeness to the ∼L relation, not
  closeness under rotation, and not closeness under all of GL(M).
- **d_KL.** The expected conditional KL under the data marginal p_D(x),
  which equals the joint KL when both models share that marginal.
- **ε-non-identifiability.** Cited from Reizinger et al. The paper's
  footnote 13 says it holds "in d_KL (Theorem 3.1) but not in d^λ_LLV
  (Theorem 4.7)".

## Connections

The model class and the identifiability theorem come from Roeder et al.,
Khemakhem et al. and Lachapelle et al. Marconato et al. (AISTATS 2024)
relax diversity to an "extended-linear" equivalence, which the authors
name as the route to comparing models of different dimension. The
symmetry is the same as Park, Choe and Veitch's γ ↦ Aγ + β, λ ↦ A⁻ᵀλ
([LIT-304](../literature.d/LIT-304.md), as read in [NOTE-302](NOTE-302.md)). Huh et al.'s Platonic hypothesis ([LIT-302](../literature.d/LIT-302.md))
is cited once, in the closing paragraph, as one of the works reporting
that learned representations are "surprisingly robust". The paper does
not argue against it. It cites Kornblith et al. ([LIT-254](../literature.d/LIT-254.md)) for the view
that similarity should be invariant only to orthogonal maps. It does not
cite Harvey, Larsen and Williams ([LIT-250](../literature.d/LIT-250.md)) and does not mention kernels,
CKA or Bures distance.

**A link to Harvey et al. that the paper does not draw (this reader's).**
m_SVD is the mean singular value of Σ_z′w′, and standardization makes
Tr Σ_z′z′ = Tr Σ_w′w′ = M. So m_SVD = ‖Σ_z′w′‖_* / √(Tr Σ_z′z′ · Tr Σ_w′w′),
which is [LIT-250](../literature.d/LIT-250.md)'s eq. 7 for the cosine of the Riemannian shape distance.
By [LIT-250](../literature.d/LIT-250.md)'s Theorem 1 that equals the normalized Bures similarity of the
centred linear kernels of z′ and w′. So d_SVD = 1 − NBS, computed on the
per-coordinate standardized vectors z = Lᵀf(x), whose entries are the
log-odds log p(yᵢ|x) − log p(y₀|x). A script check on random data agreed
to about 10⁻⁷. Two consequences follow.

- **Theorem 4.7 bounds a Bures-type kernel dissimilarity.** It does so
  for the kernel of the standardized log-odds coordinates, not for the
  Gram matrix f(x)ᵀf(x′) of the raw embedding.
- **d_f,g is a function of the distributions.** Lᵀf(x) and Nᵀg(y) are,
  up to constants, log-probability differences, so d_f,g can be computed
  from p and p′ given the pivot sets. Theorem 2.2 is what lets it be read
  as a representational measure. Any ∼L-invariant measure is a function
  of the identifiability class, and so of the distribution. Theorem 4.7
  therefore compares two distances on distributions, one of which
  standardizes and rotates.

## Bearing on the record

- **[THEORY-002](../theory.d/THEORY-002.md) cites Thm 2.2, Thm 3.1 and Cor. 3.2 accurately but
  leaves out the paper's positive result.**
  - **The title states one half.** Its title ends "closeness in
    distribution does not imply closeness of representation". The paper
    shows this for KL divergence. It proves the opposite for d_LLV
    (Theorem 4.7), and its stated conclusion is that the answer "depends
    critically on the choice of distributional and representational
    distance". The source section omits Theorem 4.7.
  - **"Does not bound" needs two qualifications.** First, the
    counterexample lives in the saturation regime, ρ → ∞. Second, the
    size of the dissimilarity is shown numerically (Table 1), not proved.
  - **The scope is narrower than [THEORY-002](../theory.d/THEORY-002.md)'s use.** [THEORY-002](../theory.d/THEORY-002.md) applies
    the result to the Platonic hypothesis. The paper's results are for
    the final embedding and the unembedding only, and it says that
    earlier layers are open. Huh et al.'s kernels are pooled hidden
    states, as [THEORY-018](../theory.d/THEORY-018.md) notes. The paper cites the hypothesis only as
    evidence of robustness. Reading it as a warning to the hypothesis is
    the record's inference, not the paper's.
  - **On its promote_when.** It asks for "a proved stability result
    linking a distributional distance to a kernel distance (Bures or
    CKA)" for a family including contrastive or LM objectives.
    Theorem 4.7, with the identity above, comes close. It is proved, it
    covers that family, and its representational side is 1 − NBS. But the
    kernel is that of the standardized log-odds coordinates, not of the
    representation itself, and the distributional distance is d_LLV, not
    KL. Whether that meets the condition is a decision for the record.
- **[THEORY-018](../theory.d/THEORY-018.md).**
  - **The cross-reference is accurate.** "[LIT-253](../literature.d/LIT-253.md) starts from the same
    symmetry" holds: f = Af′ with g₀ = A⁻ᵀg′₀ is Park et al.'s invariance.
  - **The paper is a further instance of its thesis.** To get a
    comparison invariant to ∼L, the authors move to the identified
    coordinates Lᵀf(x), the log-odds against a pivot label y₀. Those
    depend on the choice of y₀, of the label set and of the left-out
    label. In the experiments these are chosen to minimize the distance
    (App. E.3). So a usable geometry again comes from a choice, here of
    basis, not of inner product.
- **[QUESTION-027](../questions.d/QUESTION-027.md).**
  - **Cor. 3.2 is an instance of a decision-sufficient structure that
    does not identify the representation.** Two models make the same
    argmax decision on every training input, with loss tending to zero,
    and their embeddings are not linearly related. That is the question's
    "in-probe decisions are automatic" case.
  - **The paper adds a distinction the question lacks.** Exact
    identification (Thm 2.2) can be unstable. Whether near-equal
    observations nearly identify the model depends on the divergence
    (Thm 3.1 against Thm 4.7). An answer to the question would need to
    say which divergence its "identified from the available probes" is
    stable under.
  - No front-matter relation links the two, and nothing in the question
    cites the paper.
- **[CLAIM-193](../claims.d/CLAIM-193.md)** grounds "kernels fix representations only up to the
  symmetry of what is observed" on [THEORY-002](../theory.d/THEORY-002.md). This paper supports the
  GL(M) half for distributions at the softmax output and says nothing
  about kernels.
- **Anthology.** The paper carries no instruction for machine-learning
  practice. Its `anthology-candidate` flag is about its subject, which is
  representation learning.

## Limitations

- Only the final embedding and the unembedding are covered; nothing is
  said of hidden layers (§6).
- Diversity, and for Theorem 4.7 invertibility on every set used, are
  required. Diversity can fail when there are fewer labels than
  dimensions.
- Theorem 4.7 needs Y_LLV to hold all labels but one. The bound grows
  linearly in M and is vacuous unless ε < 1/(2M). The authors conjecture a
  tighter, non-linear bound.
- d_LLV depends on the chosen pivot and label sets. It is a metric for
  any admissible choice, but the experiments select the minimizing sets
  from 200 random draws.
- The KL counterexample requires the unembedding norm to grow without
  bound. If both embedding maps are injective, one of them must be
  discontinuous.
- The experiments use 2- to 5-dimensional representations. The CIFAR-10
  evidence is one illustrative pair with KL near 1.1 nats, and the bound
  is vacuous there. The width trend is from a synthetic 2-D task.
- The authors do not claim d_f,g is the right similarity measure: "Our
  goal is not to claim our measure is the right one".

## Open questions

- Does a tighter bound exist, and does d_LLV stay a metric on a diverse
  subset of labels rather than all but one? The authors conjecture both.
- How do the results extend to the extended-linear identifiability of
  Marconato et al., which would allow models of different dimension?
- Are there identifiability results for intermediate layers, without which
  none of this reaches the representations most similarity studies
  compare?
- Given the identity under Connections, is there a stability result from
  d_LLV, or from KL restricted away from saturation, to the Bures distance
  between raw embedding kernels? It would have to say which inner product
  on f(x) is meant, which Theorem 2.2 leaves free.
