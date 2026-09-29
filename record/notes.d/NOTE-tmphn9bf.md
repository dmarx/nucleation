---
status: Read
paper: LIT-tmpyzpb3
title: 'Understanding image representations by measuring their equivariance and equivalence'
version: 1
history:
- version: 1
  date: '2026-09-29'
  note: >-
    Read in full (Full text of arXiv 1411.5908 v2 (20 Jun 2015), from the
    arXiv PDF, 9 pp.: abstract, §1 with related work, §2 (definitions of
    equivariance, invariance and equivalence; the HOG and convolutional
    examples; §2.1 structured-sparsity regression; §2.2 transformation
    layers; §2.3 stitching layers), §3 (3.1 shallow/HOG equivariance; 3.2
    deep/AlexNet equivariance and invariance; 3.3 equivalence; 3.4
    structured-output regression), §4 summary, footnotes 1–5 and references
    [1]–[35]. Nothing was skipped. Text extracted with PyMuPDF. Figures 1–9
    are plots and filter or HOG visualisations that survive only as axis
    labels and captions, so their content is taken from captions and prose;
    Tables 1–5 survive and their values are quoted from the extraction. The
    v2 PDF carries no venue line; the CVPR 2015 publication was verified on
    Crossref. The extended IJCV 2018 version (doi 10.1007/s11263-018-1098-y,
    same title) was not read. `published:` is the arXiv v1 date (21 Nov
    2014). No anthology LIT entry exists (grep of record/literature.d for
    the arXiv id and title: no hit); the anthology's reading of The Platonic
    Representation Hypothesis (ANTH-LIT-458) names "Lenc and Vedaldi" in
    prose.). The first NOTE on this paper, which was seeded from its
    abstract alone.
date: '2026-09-29'
summary: >-
  Given a fixed representation φ (HOG, or AlexNet Conv1–Conv5 before ReLU)
  and a transformation g of the input image chosen by the experimenter
  (flips, 90° and other rotations, rescaling by 2^{±1/2}, affine warps),
  it fits a linear map M_g on the representation space with φ(gx) ≈ M_g
  φ(x), by sparse or structured-sparse regression or by a "transformation
  layer" trained through the rest of the network, and fits "stitching
  layers" E with φ′(x) ≈ E φ(x) between different networks. In AlexNet,
  learned M_g recover most of the classifier's accuracy for vertical flips
  and 90° rotations (top-1 error 0.75 uncompensated vs 0.43–0.51 and
  0.44–0.53 across Conv1–Conv5, original 0.43), channels scored invariant
  rise to 99.61% for horizontal flips at Conv5, and Conv1–Conv2 are
  interchangeable between AlexNet and networks trained on ImageNet, Places
  or both. It detects no group and uses no spectrum.
---

# NOTE-tmphn9bf: Understanding image representations by measuring their equivariance and equivalence

## Contribution

The paper proposes studying image representations empirically through three properties of the map φ: x ↦ φ(x) ∈ R^d (§2). **Equivariance** with a transformation g: there is M_g with φ(gx) ≈ M_g φ(x) for all x (eq. 1), and the interest is in M_g being simple, ideally linear. **Invariance**: M_g, or part of it, is the identity. **Equivalence** of two representations: there is E with φ′(x) ≈ E φ(x). It gives algorithms to estimate M_g and E from data: regularised regression with row-sparsity (eq. 3) or structured spatial sparsity (eq. 4), a task-oriented objective that trains M_g through the rest of a pretrained network (eq. 5), and CNN-specific "transformation layers" (a permutation of feature sites by g followed by m × m × D filters, §2.2) and "stitching layers" (§2.3). It applies them to HOG (§3.1), to AlexNet's convolutional layers (§3.2), to stitched "Franken-CNNs" across AlexNet, a second ImageNet network and Places networks (§3.3), and uses learned M_g to speed up structured pose regression (§3.4). The authors "believe to be the first to functionally characterise and quantify these properties in a systematic manner, as well as being the first to investigate the equivalence of different representations" (§1).

## Key insight

A representation's geometric behaviour can be read off by asking what linear map on the representation space reproduces a known transformation of the input. For convolutional representations and affine g the map is itself convolutional up to a permutation of sites, so it can be learned cheaply as one extra layer; the rows of the learned map then say which channels are carried to themselves (invariant) and which are mixed. The same regression, with a second network's features as target, tests whether two differently trained networks encode the same information up to a linear change of coordinates.

## Assumptions

- **The transformation is given.** g is chosen by the experimenter and applied to input images (§2: "The nature of the transformation g is in principle arbitrary; in practice … geometric transformations such as affine warps and flips of the image"). Each g is treated separately.
- **Paired data.** Estimating M_g needs images x and their transformed versions gx (eq. 2), or labelled images for the task-oriented loss (eq. 5).
- **Linear or affine M_g.** M_g = (A_g, b_g) (§2.1). Justified by HOG, where flips act exactly by a permutation.
- **Sparsity priors.** Row-sparsity with at most k non-zeros per row (eq. 3), or support restricted to an m × m neighbourhood Ω_{g,m}(u, v) of the back-projected site (eq. 4). An l2 regulariser "was found to be inadequate".
- **Losses.** Hellinger for HOG, l2 or the network's own classification loss for CNN layers.
- **CNN layers before ReLU.** Maps are learned on Conv1–Conv5 "right after the linear filters"; after the ReLU was "found to be harder due to the non-negativity of the features" (§3.2).
- **Affine g acts uniformly** on the image domain, so M_g is convolutional up to sampling artefacts (§2.2, fn. 3).

## Key results

- **HOG, sparse regression (Fig. 3a–b).** For rotations and scalings of a 5 × 5 HOG array predicted from 9 × 9, least squares overfits (M_g has about 1M parameters), ridge is better, forward selection with k = 5 is best (0.2% of coefficients non-zero). FS error is zero for 180° rotation, which is exact; LS and RR "fail to recover it".
- **HOG, structured sparsity (Fig. 3c, Table 1).** With m = 3 neighbourhoods on 15 × 15 arrays, LS, RR and FS perform nearly equally; FS k = 5, m = 3 is best. Structured sparsity cuts learning time sharply (Table 1: for 9 × 9 HOG, 281.18 s unstructured vs 5.91–30.93 s with m = 1–5).
- **HOG, task check (Fig. 4, Fig. 5).** An SVM for cat vs dog faces (400 train, 1,000 test) keeps its performance when inputs are rotated or rescaled and compensated by M_g, while the uncompensated classifier "rapidly fails, particularly for rotation"; HOGgle visualisations of φ(gx) and M_g φ(x) are "nearly identical".
- **AlexNet, regression methods (Fig. 6, Fig. 7).** For vertical flips, all methods recover "most if not all" of the original classifier's performance (about 75% top-1 error uncompensated vs 43% original). FS is better up to Conv2 (best m = 3, k = 25, "substantially less sparse" than HOG); from Conv3 the task-oriented transformation layer reaches much lower classification error, though FS still has lower reconstruction error. Error rises with depth.
- **AlexNet, which transformations (Table 2, top-1 / top-5 on ILSVRC12 val; original 0.43 / 0.20).**
  - Horizontal flip: none 0.44 / 0.21; Conv1–Conv5 0.43–0.45.
  - Vertical flip: none 0.75 / 0.54; Conv1 0.43, Conv2 0.46, Conv3 0.46, Conv4 0.48, Conv5 0.51.
  - Scale 2^{−1/2}: none 0.61 / 0.37; Conv1 0.45 rising to Conv5 0.50.
  - Rotation 90°: none 0.75 / 0.54; Conv1 0.44 rising to Conv5 0.53.
- **AlexNet, invariant channels (Table 3).** A channel's invariance score is the ratio of the norm of its row of M_g to the norm after suppressing the "diagonal" entry; the top-p rows are replaced by identity rows while performance stays within 5% relative of M_g. Invariant channels (number, %): horizontal flip Conv1 52 (54.17%), Conv2 131 (51.17%), Conv3 238 (61.98%), Conv4 343 (89.32%), Conv5 255 (99.61%); vertical flip 53, 45, 132, 124, 47 (55.21%, 17.58%, 34.38%, 32.29%, 18.36%); scaling 95 (98.96%), 69 (26.95%), 295 (76.82%), 378 (98.44%), 252 (98.44%); 90° rotation 42 (43.75%), 27 (10.55%), 120 (31.25%), 101 (26.30%), 56 (21.88%). Invariance to horizontal flips and scaling is "obtained largely in Conv3 or Conv4", is not monotone in depth, and is much lower for the "unexpected" vertical flips and rotations.
- **Equivalence (Table 4, top-1 / top-5).** Identity stitching gives top-1 error > 99%. With learned stitching layers, IMNET → ALEXN: 0.43 at Conv1, 0.46 at Conv2–Conv4, 0.50 at Conv5; PLCS → ALEXN: 0.43, 0.47, 0.50, 0.54, 0.65; PLCS-H → ALEXN: 0.43, 0.46, 0.47, 0.49, 0.52. Conv1–Conv2 are "interchangeable in all cases"; Conv5 is not, especially from Places.
- **Structured-output regression (Table 5).** Cat-face pose on VOC07 (300 train, 300 test), M_g pre-learned on generic images: equivariant scoring ⟨M_gᵀw, φ(x)⟩ is as good or nearly as good as direct scoring and 8.6–21.9× faster (e.g. HOG rotation error 17.0° vs 14.9° direct, 0.8 vs 18.2 ms per transformation; Conv4 rotation 11.1° vs 10.5°).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | HOG and early CNN layers transform under image warps by simple (sparse, local) linear maps | experiment | §3.1 Figs 3–5; §3.2 Fig. 6, Table 2 |
| C2 | Learned M_g let a CNN classifier handle vertically flipped and 90°-rotated images nearly as well as upright ones, better at shallow layers | experiment, one network | Table 2, Fig. 7; single runs, no error bars |
| C3 | AlexNet is largely invariant to horizontal flips and mild rescaling, with invariance obtained mostly by Conv3–Conv4 | experiment plus a heuristic score | Tables 2–3; the invariance score is per channel and thresholded at 5% relative accuracy loss |
| C4 | Invariance does not increase monotonically with depth | experiment | Table 3 (Conv1 more invariant than Conv2 for several g); explanation offered (next layer's pooling) is informal |
| C5 | Conv1–Conv2 of networks trained on different data are equivalent up to a learned linear map; Conv5 is task-specific | experiment | Table 4; three source networks, one target |
| C6 | Structured sparsity is "highly preferable" to generic sparsity for learning M_g | experiment | Fig. 3c, Table 1 (HOG) |
| C7 | The authors are the first to characterise these properties systematically and the first to investigate equivalence of representations | assertion | §1 related work |
| C8 | Equivariant regression speeds up structured-output pose estimation at little accuracy cost | experiment | Table 5, Fig. 8; 300 test images |

## Method

Empirical probing by regression. For a representation φ and an input transformation g: sample natural images, compute φ(x) and φ(gx), and fit M_g by regularised regression (eq. 2 with the row-sparsity or neighbourhood-sparsity regulariser, eqs 3–4), or train a transformation layer (site permutation by g plus m × m × D filters) inserted into a pretrained CNN to minimise the original classification loss on g⁻¹-transformed images (eq. 5). Read invariant channels off the rows of M_g. For equivalence, train a stitching layer (a filter bank, with resampling if needed) between the first part of one network and the second part of another. Evaluate by Hellinger or l2 reconstruction, HOGgle visualisation and downstream classification or regression error.

## Concepts

- **Equivariance** — existence of M_g with φ(gx) ≈ M_g φ(x) for all x (eq. 1); interesting when M_g is simple, ideally linear.
- **Invariance** — M_g, or a subset of its rows, is the identity.
- **Equivalence** — existence of E with φ′(x) ≈ E φ(x) between two representations.
- **Transformation layer** — permutation of feature sites (u, v) → g(u, v) followed by D linear m × m × D filters (§2.2).
- **Stitching layer / Franken-CNN** — a learned linear layer joining the first part of one network to the rest of another (§2.3).
- **Task-oriented loss** — fitting M_g or E through the downstream network's classification loss rather than by feature reconstruction (eq. 5).
- **Invariance score** — norm of a row of M_g relative to the same norm with the diagonal suppressed (§3.2).

## Connections

- **Cohen & Welling 2016 ([LIT-314](../literature.d/LIT-314.md), read in [NOTE-288](NOTE-288.md)).** [NOTE-288](NOTE-288.md) found this paper through [LIT-314](../literature.d/LIT-314.md)'s related work and called it "the closest in spirit to the owner's detection test". Read in full, it is the closest for *measuring symmetry in trained representations*, but its transformations are hypothesised and applied to inputs (see corrections and Bearing).
- **Cohen & Welling 2014 (sup5 in this batch).** The two are complementary halves of the prior art on the detect side. Cohen & Welling 2014 learn the irreducible decomposition of an assumed abelian group from transformation pairs on raw data; this paper learns one linear map per named transformation on a trained network's features and never forms a group or its irreps.
- **Geometric Deep Learning ([LIT-319](../literature.d/LIT-319.md), [NOTE-274](NOTE-274.md)) and Kondor & Trivedi ([LIT-305](../literature.d/LIT-305.md), [NOTE-282](NOTE-282.md)).** [NOTE-274](NOTE-274.md) and [NOTE-282](NOTE-282.md) sharpen row 7 to "domain symmetry imposed on inputs vs representation-space symmetry detected in trained weights". This paper complicates that distinction: its M_g is a linear operator *on the representation space* of a trained, unconstrained network, estimated from data. What it keeps from the domain side is that g is defined on the input. The remaining difference from the owner's programme is therefore not where the operator acts but where the group comes from: here from a hypothesis about input transformations, with paired inputs; in row 7, from the spectra of operators extracted from the representation, with no hypothesis and no paired inputs.
- **Engels et al. ([LIT-322](../literature.d/LIT-322.md), [NOTE-273](NOTE-273.md)).** Both papers find structure in a trained network by first supplying the symmetry: Engels et al. from the task (mod 7, mod 12), this paper from the chosen image transformation. [NOTE-273](NOTE-273.md)'s open question, whether an unsupervised symmetry detector would rediscover the weekday circles, applies equally here: nothing in this paper finds a transformation it was not given.
- **[THEORY-017](../theory.d/THEORY-017.md).** Two points, both mine. (i) The paper's invariance score is basis-dependent: it asks whether a *channel* maps to itself, i.e. it reads the diagonal of M_g in the network's channel basis. The basis-free counterpart would be the dimension of the +1 eigenspace of M_g (for an exact flip, an involution, eigenvalues ±1). A network could be invariant on a subspace no channel spans and score low; the paper does not consider this. (ii) Stitching tests equivalence up to a *general learned linear* map E, not an orthogonal one, and the identity map fails completely (> 99% error). That is [THEORY-017](../theory.d/THEORY-017.md)'s "a basis is extra data" in empirical form: two networks' channel bases are unrelated even when their features are linearly interchangeable. Nucleation's [THEORY-004](../theory.d/THEORY-004.md) and [THEORY-008](../theory.d/THEORY-008.md) (representations fixed by the kernel up to orthogonal transformation; which comparison measures are invariant) are the invariant-measure side of the same question; stitching uses a larger, non-orthogonal group.
- **O'Donnell ([LIT-346](../literature.d/LIT-346.md), [NOTE-291](NOTE-291.md)).** No direct link; this paper does no harmonic analysis.
- **Anthology of the SOTA.** The anthology's reading of The Platonic Representation Hypothesis ([ANTH-LIT-458](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-458.md)) names "Lenc and Vedaldi on cross-dataset transferability" among the alignment results it gathers; that is this paper's §3.3. The anthology holds no LIT for it and no model-stitching practice or theory (grep for "stitching" finds only image-stitching and unrelated hits).

## Bearing on the record

- **What the map needs, and what this paper supplies.** Row 7 says "they impose symmetry; you *detect* it via spectral degeneracy". The misattribution it repairs is by omission: the map cites only impose-side works, so the contrast reads as if no one had measured symmetry in trained networks. This paper had, in 2014: it measures, per named transformation, whether a trained network's representation carries the transformation linearly, which channels are invariant, and whether two networks' representations are linearly equivalent. The map should cite it on the detect side.
- **Exactly what it detects, from what, and what it needs to know first.**
  - *Detects:* for each transformation g supplied, whether a linear map M_g on representation space reproduces g's effect (by reconstruction error or recovered task accuracy), and which channels are approximately fixed by M_g.
  - *From:* activations of a trained network (and HOG) on natural images and their g-transformed copies, or labels for the task-oriented loss.
  - *Must know in advance:* the transformation itself. Nothing in the paper searches for an unknown transformation, and nothing asks whether the M_g for several g form a group representation.
  - *Spectral degeneracy:* no role. The eigenvalues of M_g are never computed; there are no irreps, characters, or multiplicities.
  - **Verdict.** It supplies the "measure symmetry in trained representations" prior art row 7 must cite, and so "you detect" cannot stand unqualified. It does not pre-empt the degeneracy diagnostic. The defensible positioning is: prior detection work (this paper) tests a *hypothesised input transformation* using *paired transformed inputs* and fits one map per transformation; prior irreps-learning (Cohen & Welling 2014) learns the decomposition of an *assumed group class* from transformation pairs; the owner's proposal is to infer group structure and irreps *without a hypothesised group and without transformed inputs*, from *eigenvalue multiplicities* of operators extracted from the representation. The `NOVEL-NARROW` label survives with that wording.
- **ML practice (anthology-candidate).** Yes. Model stitching (§2.3, §3.3) is an established probe of representational similarity, and this is its standard origin citation; learned equivariance maps are a standard probe of what invariances a network has acquired. Neither is currently held in the anthology. It would enter as a theory or method source for representation comparison beside the Platonic Representation Hypothesis, with the caveat that its deep-layer claims rest on one network and single runs. The anthology might prefer the extended IJCV version (not read).
- **For filing.** `representation-learning` first, `anthology-candidate` second. `mathematics` is not justified: the paper defines its properties informally and uses no group or representation theory.

## Limitations

- **Transformations are named in advance and tested one at a time.** No composition, no inverse, no group; "equivariance" is to a single g.
- **Task-oriented M_g has high capacity** (m × m × D filters per layer), so recovering accuracy through it shows compensability, not a clean equivariant structure; the paper itself notes reconstruction error and classification error disagree from Conv3 on.
- **One network, single runs.** Tables 2–5 report single numbers with no seeds or error bars; equivalence uses one target network (ALEXN) and three sources.
- **Invariance score is a heuristic** tied to the channel basis and a 5% relative-accuracy threshold.
- **Pre-ReLU layers only** for the CNN; after ReLU the maps were "harder" to learn and are not reported.
- **Training augmentation is not discussed**, so the horizontal-flip invariance cannot be attributed to the architecture or the data from the text.

## Open questions

- If the learned M_g for a set of transformations were checked for the group law (M_g M_h ≈ M_{gh}), and decomposed into irreducible blocks, would they reproduce the irreps a degeneracy test finds in the same layer? That would join this paper's per-transformation probe to row 7's diagnostic.
- Are the invariant subspaces of M_g (its +1 eigenspaces) larger than the channel counts in Table 3 suggest, i.e. is invariance in AlexNet partly distributed across channels?
- Does the extended IJCV version (not read) test group structure or non-geometric transformations? Unverified.

## Corrections to the seeded skim

- none (there was no seed or dossier)
- [NOTE-288](NOTE-288.md) reports, from Cohen & Welling 2016's related work, that this paper shows "the AlexNet CNN … trained on imagenet spontaneously learns representations that are equivariant to flips, scaling and rotation". The body is narrower. (i) "Rotation" is 90° (Table 2, Table 3) and 0–90° for the task-oriented method (Fig. 7); intermediate angles are "slightly harder". (ii) For horizontal flips and scaling by 2^{−1/2}, the paper finds that learning M_g "is not better than leaving the features unchanged" because the network is already largely invariant to them (Table 2: uncompensated top-1 0.44 for horizontal flips vs 0.43 original). It is vertical flips and 90° rotations for which learned maps help (0.75 → 0.43–0.53). (iii) "Spontaneously" is Cohen & Welling's word, not the paper's; the paper says the CNN "is implicitly learned to be invariant to such factors" (§3.2) and does not discuss training augmentation. The standard AlexNet recipe it cites ([10]) augments with horizontal reflections, so horizontal-flip invariance is at least partly imposed through the data; whether the paper's MatConvNet ALEXN was trained that way is not stated (unverified).
- "Equivariance" here is a regression property: a linear (in practice affine, (A_g, b_g)) map exists that predicts φ(gx) from φ(x) well, or that lets the downstream network classify g-transformed images (eq. 5). For Conv3 onward the task-oriented loss is better than feature reconstruction, and "feature reconstruction is not always predictive of classification performance" (§3.2). So the deep-layer results show that a learned m × m × D convolutional layer can compensate for g, not that φ(gx) = M_g φ(x) holds closely.
- For the map's row 7 (see Bearing): the paper never checks group structure (M_{gh} = M_g M_h, M_{g⁻¹} = M_g⁻¹), never forms a representation, and never looks at the eigenvalues of M_g. Spectral degeneracy plays no role.
