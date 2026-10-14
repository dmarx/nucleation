---
number: 816
status: Read
formerly:
- NOTE-tmpw5s6c
paper: LIT-937
title: 'Erogullari et al. — Post-Hoc Concept Disentanglement'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv PDF, v1 of 7 March 2025 (20 pages),
    fetched from arxiv.org/pdf/2503.05522 and extracted with pdftotext:
    §§1–6, Appendices A–C, Tables 1–3 and the captions of Figures 1–12.
    The figures were read only through their captions and the text that
    describes them. The paper states no AUROC or orthogonality value in
    its text, so the numbers below are hyperparameters, set-up
    proportions and the ranges on the figure axes, not results.
date: '2026-10-14'
summary: >-
  Concept activation vectors fitted one concept at a time align for
  CelebA and FunnyBirds attributes that co-occur in the labels. A joint
  fit with a penalty ‖CCᵀ − I‖²_F finds mutually orthogonal directions
  that still separate each concept, with AUROC "largely preserved". So
  correlated attributes keep linear separating directions in these
  CNNs, and the alignment comes from the separate fits. Steering with the
  orthogonal directions changes correlated concepts less.
---
<!-- inactive-ok-file: THEORY-117 THEORY-185 THEORY-292 — Proposed; the accounts this reading bears on, and the one filed from it -->

# NOTE-816: Erogullari et al. — Post-Hoc Concept Disentanglement

## Contribution

The paper shows that concept activation vectors (CAVs) fitted separately
for attributes that co-occur in a dataset come out aligned. Examples are
CelebA's "beard", "necktie" and "mustache", and a controlled beak–tail
correlation in FunnyBirds. It adds a non-orthogonality penalty to the CAV
objective and fits all concepts jointly. Mutually orthogonal directions
then exist that still separate each concept about as well. That shows,
for VGG16 and ResNet18 on two datasets, that the entanglement of
standard CAVs is not forced by how separable the representation is.

## Key insight

The direction a CAV finds for one concept, fitted without regard to the
others, takes in whatever correlates with that concept's label. The
representation has room for more: the latent space has far more
dimensions than there are concepts (m ≫ n), and a joint fit can give
each concept its own orthogonal direction at little cost in separation.
So aligned CAVs for correlated concepts describe the fitting procedure
and the label statistics. They are not a finding that the model encodes
the concepts along one shared direction.

## Assumptions

- **Concepts are linear directions** in one layer's activations,
  learned under supervision from binary labels t ∈ {−1, 1}ⁿ (§3.1).
  The layer is the last convolutional layer of each model (§4.1).
- **m ≫ n.** "There is sufficient room for CAVs to be orthogonal to one
  another" (§3.3). The number of channels is not stated.
- **AUROC is the proxy for "directional correctness".** It is computed
  from the dot products of activations with each CAV, since the CAVs are
  not predictors (§3.5, footnote 2). No other check is made that the
  orthogonalised direction still means the concept, apart from LRP
  heatmaps and steering images.
- **Unit-norm rows.** Eq. (5) reads CCᵀ as "the pair-wise cosine
  similarity matrix". That is true only if the CAV rows are normalised,
  which the paper does not say it does.
- **Two datasets.**
  - CelebA has 40 binary attributes, with "blond hair" as the classifier
    task.
  - FunnyBirds has 50 classes and 5 body parts turned into binary
    concepts. Beak and tail types were made to co-occur with probability
    0.7, and the rest is split 0.15 each (Table 1). Table 1 lists four
    beaks and three tails, with beak03 and beak04 both paired to tail03.

## Key results

- **Baseline CAVs (Eq. 2, Pattern-CAVs).**
  - The objective is argmin_{w,b} ‖Z − t wᵀ − b‖²₂, fitted per concept.
  - The cosine matrix of the 40 CelebA CAVs (Fig. 2, Fig. 10) shows two
    blocks that match two blocks of the label correlation matrix. The
    paper calls them female- and male-associated (Table 3). "High
    cheekbones", "smiling" and "mouth slightly open" are one aligned
    triple.
  - Concepts that rarely co-occur ("mustache", "makeup") point in
    opposite directions.
  - The paper attributes this to "the training of individual concepts in
    isolation without any information on other concepts" (§3.2).
- **The metric and the penalty.**
  - Orthogonality: Oᵢ = 1 − (1/(|C| − 1)) Σ_{c̃≠cᵢ} |cos(cᵢ, c̃)| (Eq. 4).
  - The penalty is L_orth = ‖CCᵀ − Iₙ‖²_F (Eq. 5).
  - The objective is L = L_CAV + α L_orth (Eq. 6).
  - A targeted variant weights chosen pairs by β (Eqs. 7–8).
- **Orthogonality at little cost in AUROC (§4.2, Fig. 3).**
  - The fit was fine-tuned from the baseline CAVs for 300 epochs, at
    learning rate 0.001 and α = 0.01 (0.1 for FunnyBirds with VGG16)
    (Table 2).
  - All four dataset–model pairs reach "near-perfect or complete
    orthogonalization". The cosine matrix after the fit "resembles the
    identity matrix" (Fig. 5).
  - AUROC "remains largely preserved". It typically rises at first, then
    decays and settles "at a slightly lower level".
  - No value is given in the text.
- **Per concept (Figs. 4–5).**
  - Every concept gains orthogonality.
  - AUROC changes differ by concept. "Pale Skin" gained most, "Young"
    lost most and "Black Hair" changed least.
  - Within each block both gains and losses occur, on an axis spanning
    −20% to +20% relative change.
- **α sweep (Fig. 6).**
  - Randomly initialised CAVs on VGG16 for CelebA, with learning rate
    0.1 and 500 epochs, for α from 10⁻¹⁰ to 10¹⁰.
  - For α between 10⁻⁴ and 10⁰, orthogonality is perfect and average
    AUROC is slightly *above* the α = 0 baseline. Larger α drops AUROC
    sharply.
- **Heatmaps (§4.3, Fig. 7).**
  - Baseline CAVs for anti-correlated pairs ("blond hair" and "necktie")
    put negative relevance on each other's regions.
  - After orthogonalisation the heatmaps still mark the concept's own
    region, with less of the cross-relevance.
- **Steering (§5).**
  - **Insertion.** Diffusion-autoencoder latents were moved along the
    "wearing necktie" CAV. The baseline direction also adds "mustache"
    and "eyeglasses", and the orthogonal one adds the necktie alone
    (Fig. 8, qualitative).
  - **Removal.** A timestamp was put on 40% of blond and 0.5% of
    non-blond images. A box was added with probability 0.5 given a
    timestamp and 0.1 otherwise.
  - P-ClArC with the orthogonal timestamp CAV (α = 1, β = 100) does
    better on both clean and attacked test sets than with the baseline
    CAV, which costs clean accuracy (Fig. 9). The numbers are only in
    the figure.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Separately fitted CAVs for co-occurring attributes align, in blocks matching the label correlations | moderate | Figs. 2, 10, 12; two datasets, two architectures |
| C2 | Mutually orthogonal directions exist that separate each concept about as well as the separate fits | moderate | Figs. 3, 5, 6; AUROC only, read from figures, no seeds or error bars |
| C3 | A joint fit with a small orthogonality weight can slightly raise average AUROC | weak | Fig. 6, one dataset–model pair |
| C4 | Steering along orthogonalised CAVs changes correlated concepts less | weak | Fig. 8 qualitative; Fig. 9, one controlled artefact experiment |

## Method

The CAVs are fitted from Eq. (2) and then fine-tuned under Eq. (6) by
gradient descent. Average orthogonality Ō and macro AUROC are monitored
during the fit, and AUROC can serve as an early-exit criterion (§3.5).
The targeted variant multiplies chosen entries of CCᵀ − I by β > 1
before the Frobenius norm.

## Concepts

- **CAV.** The direction in a layer's activations from samples without a
  concept to samples with it, here the pattern w of Eq. (2).
- **Entanglement.** CAVs that "share similar orientations within the
  latent space", measured by cosine. This is a property of the fitted
  vectors, not a test of the representation.
- **Directional correctness.** How well a CAV separates the concept,
  proxied by AUROC.
- **Orthogonality Oᵢ.** One minus the mean absolute cosine of a CAV with
  all others (Eq. 4).

## Connections

The work extends Kim et al.'s CAVs and the Pattern-CAVs of Pahde et al.
It cites Nicolson et al. (TMLR 2025) for the observation that CAVs of
correlated concepts are non-orthogonal. It sets itself against whitening
during training (Chen et al.) and post-hoc PCA or ICA (Chormai et al.).
Its steering uses Preechakul et al.'s diffusion autoencoders and Anders
et al.'s P-ClArC.

**The reader's note on mechanism.** The paper does not derive why
separate fits align. Eq. (2) is a least-squares fit of the activations on
one label, so its solution is w_c ∝ Cov(z, t_c). Suppose the activations
were z = Σ_k t_k u_k + noise, with a distinct direction u_k for each
concept. Then w_c ∝ Σ_k Cov(t_k, t_c) u_k. Each pattern-CAV is a mix of
the true directions, weighted by label covariance. That is the alignment
of Fig. 2, and it arises even when the directions u_k are distinct. The
joint fit with a penalty is one way to undo the mixing. This is the
reader's derivation, not the paper's.

## Bearing on the record

- **[QUESTION-025](../questions.d/QUESTION-025.md).**
  - [LIT-937](../literature.d/LIT-937.md)'s standing says the paper gives "a measured case of
    correlated attributes yielding non-orthogonal, entangled concept
    directions". That is half of what it shows. What is measured is the
    alignment of separately fitted CAVs.
  - The paper's own result is the other half: orthogonal directions exist
    that separate each correlated concept with little loss.
  - So, for supervised CNN features, correlated attributes still have
    linear separating directions. Their apparent entanglement comes from
    fitting each one alone.
  - The setting is not the question's. These are image classifiers and
    labelled attributes, not a co-occurrence embedding.
  - The attributes are correlated, not hierarchical. Implications among
    CelebA labels ("Goatee" and "No Beard", "Mustache" and "Male") are
    present but not analysed. They are orthogonalised like any other
    pair.
  - The paper says nothing about a concept lattice.
- **[THEORY-185](../theory.d/THEORY-185.md).** Its Appendix A5 case, pairwise-correlated
  attributes giving affine eigenvectors that "mix attributes", is the
  co-occurrence counterpart. A direction found from one statistic at a
  time mixes correlated attributes. This paper adds, in a different
  setting, that a joint fit can separate them again while each still
  separates its own attribute.
- **[THEORY-117](../theory.d/THEORY-117.md).** That account has features going from decodable but
  entangled to linearly factored as combinations are covered. Here every
  combination occurs and the correlation is partial (70% in FunnyBirds),
  and each concept is decodable along its own direction. Whether the
  models' features are factored in [THEORY-117](../theory.d/THEORY-117.md)'s sense is not tested.
  The two do not conflict.
- **Filed from this reading:** [THEORY-292](../theory.d/THEORY-292.md).
- **The anthology.** The steering and shortcut-suppression results (§5)
  are ML practice: how to edit a model's behaviour. They belong to the
  Anthology of the SOTA, and the LIT keeps its `anthology-candidate`
  flag.

## Limitations

- **No numbers in the text.** Every AUROC, orthogonality and accuracy
  result is in a figure. There are no seeds, error bars or repeat runs.
- **AUROC is the only check that a direction still means its concept.**
  The heatmaps and steering images are illustrations.
- **"Not forced by the representation" holds only at one layer.** It
  holds at the last convolutional layer, where m ≫ n. It is not shown
  where n approaches m, or in earlier layers.
- **Not about the model's own geometry.** Neither fit says how the
  network itself uses the directions. Orthogonal CAVs are a choice among
  separating directions, not a discovery of the model's axes.
- **Narrow tests.** Two small CNN architectures and one diffusion
  autoencoder, with one controlled artefact experiment for removal.

## Open questions

- How large is the drop in AUROC per concept, with error bars? Does it
  grow with the strength of the label correlation? A table of AUROC
  against label correlation would answer it.
- Would a fit that regresses all labels jointly (multivariate least
  squares) recover the same orthogonal-ish directions without a penalty?
  If so, the penalty only stands in for the joint regression.
- For attributes that imply one another, is an orthogonal direction for
  each still separating? Or does implication force the alignment that
  correlation does not? That would bear directly on [QUESTION-025](../questions.d/QUESTION-025.md).
