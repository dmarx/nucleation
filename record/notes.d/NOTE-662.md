---
number: 662
status: Read
formerly:
- NOTE-tmpytz8j
paper: 'LIT-858'
title: 'Towards Understanding Grokking'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the arXiv PDF of v2 (14 Oct 2022, the NeurIPS 2022
    camera-ready, 29 pp.), text extracted with pdftotext. Read: abstract,
    §§1–6, the NeurIPS checklist, Appendices A–L and the reference list.
    Propositions 1–2 and the conservation proofs of App. F checked line
    by line; the derivation of App. L followed, not re-derived. The figures
    are plots and were read from captions, axis labels and the text, so
    the agreement claimed in Figs. 3–5 is taken as the authors state it.
    The v1 PDF (20 May 2022, 20 pp.) was compared section by section: v2
    adds §4.3 and Appendices A, I, J, K and L. The code repository was
    not run.
date: '2026-10-09'
summary: >-
  In a model that decodes the sum of two learned embeddings, a held-out
  pair is answered correctly when its embedding sum coincides with a
  trained pair's, and the training set's same-answer pairs force such
  coincidences. Grokking's critical training fraction is then where those
  equations first fix the embedding up to translation and scale, which a
  posited effective loss predicts for addition with p = 10. Threshold-defined
  phase diagrams over decoder learning rate and weight decay put grokking
  between comprehension and memorization, in the toy and, qualitatively, in
  a transformer and on MNIST.
---

<!-- inactive-ok-file: THEORY-181 — Proposed; the THEORY this reading produced -->
<!-- inactive-ok-file: THEORY-022 — Proposed; the record's account of the modular-addition circuit, which this reading bears on -->
<!-- inactive-ok-file: THEORY-039 — Proposed; the record's account of later training phases, which this reading bears on -->
<!-- inactive-ok-file: THEORY-083 — Proposed; the record's account of neural collapse, which App. I bears on -->
<!-- inactive-ok-file: LIT-369 — Proposed; named because NOTE-317's reading of it cites this paper -->

# NOTE-662: Towards Understanding Grokking

## Contribution

Power et al. ([LIT-341](../literature.d/LIT-341.md)) showed that networks trained on small algorithmic
datasets can generalise long after fitting the training set, with a
critical training fraction below which they never do. This paper gives an
early account of why (May 2022, before Nanda et al.'s circuit), in a toy model where it can be computed: the
generalising solution is a structured embedding, the training set fixes
that structure through linear equations among the embeddings, and the
critical fraction is where those equations stop leaving freedom. It adds an
effective loss whose spectrum predicts the time to structure, and
threshold-defined phase diagrams in which grokking is a band between
generalising promptly and never generalising.

## Key insight

If a model can only see a + b through E_a + E_b, two training examples with
the same answer force their embedding sums to coincide, and every forced
coincidence is a free answer for some unseen pair. Generalisation is
counting what the training set's equations pin down. Once they fix the
embedding up to the two symmetries the loss cannot see, translation and
scale, the representation is a number line and everything generalises.

## Assumptions

- **Architecture.** (a, b) ↦ Dec(E_a + E_b). The operation is hard-coded in
  the architecture: a sum of embeddings for addition, a product of learnable
  3 × 3 matrices for S₃ (App. H). Targets are fixed random vectors
  (regression) or one-hot vectors (classification).
- **Ideal model M\*** (Propositions 1–2): zero training loss and an
  injective decoder. A classifier's decoder is not injective. The paper
  concedes it in "Limitations of the effective theory": a decoder with
  "pizza slices" (Fig. 2d) makes non-Euclidean parallelograms.
- **Effective dynamics.** The normalised embeddings Ẽ_k = (E_k − μ)/σ are
  assumed to follow gradient flow on
  ℓ_eff = ℓ₀/Z₀, ℓ₀ = Σ_{(i,j,m,n)∈P₀(D)} |Ẽ_i + Ẽ_j − Ẽ_m − Ẽ_n|² / |P₀(D)|,
  Z₀ = Σ_k |Ẽ_k|². This is posited (Eq. 4). App. L motivates it only for a
  linear decoder D(r) = Ar + b with weight decay γ. It drops the Ar term in
  db/dt, considers a pair with r′ = −r, and takes the adiabatic limit
  η_A → 0 with AᵀA ≈ I at initialisation.
- **Setting of the quantitative results.** Non-modular addition with p = 10
  (55 unordered pairs), 1D embeddings, and the decoder trained apart from the
  embeddings: Adam on the embeddings, AdamW on the decoder.
- **Phases** (App. A, Table 1) are operational: train and validation
  accuracy above 90% within 10⁵ steps, and a lag of under 10³ steps, give
  comprehension; a longer lag gives grokking. MNIST uses a 60% validation
  threshold. Moving the thresholds moves the boundaries.

## Key results

- **Proposition 1.** At zero training loss, any exact parallelogram
  E_i + E_j = E_m + E_n in the representation has i + j = m + n (almost
  surely, for random regression targets).
- **Proposition 2.** For M\*, two training samples with i + j = m + n force
  E_i + E_j = E_m + E_n.
- **RQI and predicted accuracy** (§3.1, App. D). RQI(R) = |P(R)|/|P₀|, the
  share of permissible parallelograms realised within δ. The predicted
  accuracy Acc^ counts the training pairs plus every pair reachable from one
  by a realised parallelogram. For 1D toy addition, Acc^ ≈ Acc across
  training fractions and seeds (Fig. 3). In high dimension RQI is "too
  restrictive" (App. D), and for S₃, Acc^ is only a lower bound on Acc
  (Fig. 18e): the network generalises by something beyond RQI.
- **Ground states and the critical fraction** (§3.2). ℓ_eff = 0 iff the
  linear system A(P) holds. Its nullity n₀ ≥ 2 always, with equality for the
  full parallelogram set. n₀ = 2 gives E_k = a + kb. The probability that a
  random training set gives n₀ = 2 jumps near r_c = 0.4 for p = 10
  (Fig. 4a). Empirical steps-to-RQI > 0.95 show the same threshold
  (Fig. 4b). For S₃, r_c ≈ 0.5 (Fig. 18b).
- **Conservation** (App. F, proved). Under the effective flow,
  C = Σ_k E_k and Z₀ = Σ_k |E_k|² are conserved. The proof uses Euler's
  identity Σ_k E_k · ∂ℓ₀/∂E_k = 2ℓ₀ for the quadratic ℓ₀, and translation
  invariance. So the flow cannot collapse to zero.
- **Grokking rate** (§3.2). ℓ_eff = ½ RᵀHR, so dR/dt = −HR, and the slowest
  non-trivial mode decays at λ₃. The predicted number of steps is
  n_h = 1/(λ₃η). λ₃ is zero with high probability below r_c and grows with
  data above it (Fig. 5a). Predicted and observed steps agree "qualitatively"
  (Fig. 5b), and trajectories take about 3n_h steps (Fig. 4c–d).
- **App. C** (worked example, p = 6). 8 well-chosen samples of 21 fix the
  linear structure.
- **App. H.** For abelian groups two parallelograms deduce a third. For
  non-abelian groups three are needed (E_b⁻¹E_a = E_c E_d⁻¹ = E_f⁻¹E_e =
  E_g E_h⁻¹ gives E_a E_h = E_b E_g). S₃'s six matrix embeddings form a
  hexagon in PCs 1 and 3 (Fig. 17).
- **Phase diagrams** (§4.1, Fig. 6). Embedding learning rate fixed at 10⁻³,
  decoder learning rate against decoder weight decay. Addition regression,
  addition classification and S₃ regression all show four phases, with
  memorization at a fast and capable decoder, confusion at a fast and
  heavily decayed one, and grokking between comprehension and memorization.
  Over embedding against decoder learning rate (Fig. 6a), comprehension
  needs the representation to learn faster than the decoder, but "not too
  much" faster.
- **App. G.** Small batches give grokking and full batches comprehension
  (Fig. 13). Small initialisation scale gives comprehension (Fig. 14).
  Weight decay on the embeddings matters little (Fig. 15).
- **Transformer** (§4.2). Addition mod 53, 256-D embeddings, decoder-only
  transformer, no operation token. The circle appears in the top two PCs at
  generalisation (Fig. 1), not before; t-SNE showed nothing earlier. The
  effective dimension exp(S) of the PCA spectrum rises until generalisation
  and then falls (Fig. 7 left, 100 seeds). Decoder weight decay speeds
  generalisation, unlike in the toy, and a large dropout rate removes the
  delay (Fig. 7).
- **MNIST** (§4.3, App. J; v2 only). 1,000 training samples, Kaiming-uniform
  weights scaled by a constant above 1 (9.0 in Fig. 8a), depth-3 width-200
  ReLU MLP, MSE on one-hot targets, AdamW. Training fits early and
  validation accuracy rises much later. A weight decay against last-layer
  learning-rate diagram shows the four phases. Time to 60% validation
  accuracy rises sharply below a training-set size (Fig. 20).
- **App. I** (v2 only). ℓ/Z with ℓ = Σ over same-label pairs of
  |f(x) − f(y)|² conserves Z (Eq. 33, proved). On MNIST with 2D embeddings
  and 100 Adam steps, same-class points collapse to class means while the
  means stay apart (Fig. 19).
- **App. K** (v2 only). Embeddings at initialisation, projected onto the
  final principal components, already show much of the final structure.
  Reconstructing from the final top PCs beats the current top PCs (Fig. 22).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | For an ideal model, same-answer training pairs force parallelograms, and parallelograms carry answers to unseen pairs | strong (proof, under the injectivity assumption) | Propositions 1–2, App. D |
| C2 | In 1D toy addition, RQI-predicted accuracy matches measured accuracy | moderate | Fig. 3, one setting (p = 10) |
| C3 | The critical training fraction is where the training set's parallelogram equations reach nullity 2 | moderate | Fig. 4a–b, p = 10 only; S₃ analogue in Fig. 18 |
| C4 | The effective loss conserves Σ E_k and Σ\|E_k\|² | strong (proof) | App. F |
| C5 | Time to structure scales as 1/λ₃ of the effective Hessian | weak to moderate | Fig. 5b, "qualitative" agreement |
| C6 | Grokking lies between comprehension and memorization in decoder learning rate × weight decay | moderate for the toys, weak beyond | Figs. 6–8; threshold-defined phases |
| C7 | Generalisation in the transformer coincides with low-dimensional (circular) embedding structure | weak | PCA pictures and PCA entropy; the authors say no projection is guaranteed to find structure |
| C8 | The ℓ/Z loss is a new self-supervised method that provably avoids collapse | the conservation is proved; "self-supervised" is not supported | App. I uses class labels to form the pairs, and reports no accuracy |
| C9 | Realised parallelograms are a subset of those the training set implies ("Alexander principle") | not supported as a result | stated as a "belief", checked numerically as a bound (Fig. 10) |

## Method

Two levels, after the physics usage. At the micro level, a reduced
description: drop the decoder, write an energy on the embeddings alone (the
parallelogram defect), normalise it to remove scale, and read off ground
states (a null space), conserved quantities and relaxation times (Hessian
eigenvalues). At the macro level, grid searches over optimiser
hyperparameters, with each run labelled by accuracy thresholds, drawn as a
phase diagram.

## Concepts

- **grokking**: generalisation long after fitting the training set. In
  Table 1, validation reaching 90% more than 10³ steps after training does,
  within 10⁵ steps.
- **δ-parallelogram**: (i, j, m, n) with |(E_i + E_j) − (E_m + E_n)| ≤ δ.
  *Permissible* when i + j = m + n.
- **RQI (representation quality index)**: the share of permissible
  parallelograms realised in the representation.
- **linear representation**: E_k = a + kb, RQI = 1.
- **effective theory**: the paper's usage is a reduced model like model
  reduction. It is not a renormalisation-group derivation.
- **grokking rate**: λ₃, the third-smallest eigenvalue of the effective
  Hessian. The first two are the translation and scale zero modes.
- **comprehension / grokking / memorization / confusion**: the four
  threshold-defined phases. Comprehension and grokking together are the
  "Goldilocks zone".
- **Alexander principle**: the belief that a network forms no
  parallelogram its training set does not imply.

## Connections

It builds on Power et al. ([LIT-341](../literature.d/LIT-341.md)) and reproduces its critical fraction.
It cites Nanda and Lieberum's 2022 blog analysis of the modular-addition
circuit, which became Nanda et al. ([LIT-345](../literature.d/LIT-345.md)). Its effective-theory and
phase-diagram vocabulary comes from Roberts, Yaida and Hanin and from
statistical-physics work on generalisation. App. B leans on the Deep Sets
representation f(x₁, x₂) = ρ(φ(x₁) + φ(x₂)) to argue that summed
embeddings are general for commutative operations. App. I places its loss
beside neural collapse (Papyan, Han and Donoho) and non-contrastive
self-supervised learning. Its own follow-up is Omnigrok (Liu, Michaud and
Tegmark, [ANTH-LIT-540](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-540.md), arXiv v1 3 Oct 2022), which v2 cites. v2's MNIST
setup is the one Omnigrok uses.

## Bearing on the record

- **It produces [THEORY-181](../theory.d/THEORY-181.md).** That THEORY states the toy result as a
  finding: a training set fixes the generalising representation when its
  parallelogram equations leave only translation and scale free. Nothing in
  the record held it.
- **[THEORY-022](../theory.d/THEORY-022.md).** This paper (v1 May 2022) is the earliest in the record to
  find the circle in modular-addition embeddings: the toy in Fig. 2d, and
  PCA of a transformer's embeddings in Fig. 1. That is eight months before
  Nanda et al. ([LIT-345](../literature.d/LIT-345.md)). It saw the circle only in PCA, with no Fourier
  analysis and no frequencies. It strengthens [THEORY-022](../theory.d/THEORY-022.md)'s "the group comes
  from the task, not the network": in the toy, the operation itself, a sum
  or a matrix product, is built into the architecture. Its S₃ experiment
  does not touch [THEORY-022](../theory.d/THEORY-022.md)'s open point on non-abelian tasks. The
  embeddings there are learnable 3 × 3 matrices multiplied by hand, so a
  matrix representation is imposed, not found. The coordinator may want to
  add this LIT to [THEORY-022](../theory.d/THEORY-022.md)'s sources as the earlier, weaker observation.
- **[THEORY-039](../theory.d/THEORY-039.md).** It adds one more later-phase instrument: the entropy of
  the embeddings' PCA spectrum, which rises until generalisation and then
  falls (Fig. 7). The paper reads this as the decoder "pruning" unused
  dimensions. It is another quantity, measured by PCA, not a measured
  compression of I(X;T), so it fits [THEORY-039](../theory.d/THEORY-039.md) as stated.
- **[THEORY-083](../theory.d/THEORY-083.md).** App. I's loss on same-label pairs reproduces within-class
  collapse but, by the authors' account, not the simplex equiangular tight
  frame. They conjecture that adding repulsion between classes would give
  it. This is a 2D, 100-step MNIST demonstration with no accuracies, and it
  does not change [THEORY-083](../theory.d/THEORY-083.md).
- **[NOTE-317](NOTE-317.md)** (on [LIT-369](../literature.d/LIT-369.md)) says that paper cites "Liu et al.'s NeurIPS
  2022 'effective theory' paper as [6] for the weight-norm account". This
  paper gives no weight-norm account; the L-shaped/U-shaped norm picture is
  Omnigrok's. Its v2 App. J does contain the same MNIST recipe (1k samples,
  scaled initialisation, depth-3 width-200 MLP, MSE, AdamW), so citing it
  for the setup would be apt. [NOTE-317](NOTE-317.md)'s point stands.
- **[NOTE-283](NOTE-283.md)** lists "Liu et al. 2022 (effective theory)" among its
  connections. It now has a LIT here.
- **ML practice.** The phase diagrams are read as practice: grokking "can
  be remedied with proper hyperparameter tuning", and decoder weight decay
  or dropout "de-delay" generalisation. That belongs to the anthology,
  which holds this line around [ANTH-THEORY-069](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-069.md) ("grokking is a regime…, at
  least three knobs move it") and [ANTH-LIT-540](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-540.md). Hence the
  `anthology-candidate` flag on the LIT. Nothing here should source a
  practice.

## Limitations

- The quantitative theory covers one toy: 1D embeddings, non-modular
  addition with p = 10, and the operation hard-coded. No scaling of r_c
  with p is shown, so the "phase transition" is a finite-size jump at one
  size.
- The effective loss is posited. Its derivation (App. L) assumes a linear
  decoder, drops a term, considers an antisymmetric pair, and freezes the
  decoder. The quantitative gaps in Figs. 4–5 are attributed to the
  decoder without a test.
- Injectivity of the decoder fails for classification, the setting of the
  original grokking result.
- The phases are defined by accuracy thresholds and step budgets. There is
  no order parameter, and "phase" and "universality" are used by analogy.
- The transformer and MNIST evidence is PCA pictures, PCA entropy and
  hyperparameter sweeps. The authors note that no dimensionality reduction
  is guaranteed to reveal structure.
- §4.3 says it shows MNIST grokking "for the first time". That section was
  added in v2, after the same group's Omnigrok (3 Oct 2022) had posted
  MNIST grokking.
- The "intelligence from starvation" analogy in the abstract is not
  developed or tested anywhere in the paper.
- The checklist says error bars are reported. Several figures show seeds as
  scatter points, but the phase diagrams carry no seed variation.

## Open questions

- How r_c behaves as p grows, and whether the nullity-2 threshold tracks
  the empirical one at every p. That would turn C3 from one data point into
  a law.
- What replaces the parallelogram mechanism where Acc exceeds Acc^, as for
  S₃ (Fig. 18e). A decoder-relative RQI, which App. D asks for, would be
  the natural instrument.
- Whether ℓ_eff can be derived for a nonlinear decoder, and whether λ₃ then
  predicts grokking time quantitatively.
- Whether the threshold-defined phase boundaries correspond to any
  singularity, for example in a loss or norm order parameter, or are only
  contours of a smooth time-to-generalise surface.
