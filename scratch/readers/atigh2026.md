# Reader notes: atigh2026 (LIT-2993)

## Step 1: copies located (2026-11-22)

- https://proceedings.mlr.press/v300/atigh26a.html — PMLR landing page (publisher, open proceedings). HTTP 200. Metadata: authors Mina Ghadimi Atigh, Max van Spengler, Teng Long, Melika Ayoughi, Tejaswi Kasarla, Pascal Mettes; AISTATS 2026, PMLR 300:2674–2682; citation_publication_date 2026/08/30.
- https://raw.githubusercontent.com/mlresearch/v300/main/assets/atigh26a/atigh26a.pdf — the publisher's own PDF (PMLR's citation_pdf_url). HTTP 200, 15 pages (paper, checklist, appendix). Kind: publisher's open-access copy. Read.

No other copy was sought, since the publisher's open PDF was reached first. Code: https://github.com/MinaGhadimiAtigh/hyperbolic-granular-learning (footnote 1; not fetched). No email address was sent to any service.

## Step 2: read (2026-11-22)

Provenance: the PDF above, extracted with pdftotext. Read in full: the main text (§1–§6), appendix A.1–A.4 and Tables 1–9. Skimmed: the references and the AISTATS checklist.

Bibliographic corrections for LIT-2993: the authors are Mina Ghadimi Atigh, Max van Spengler, Teng Long, Melika Ayoughi, Tejaswi Kasarla and Pascal Mettes (all University of Amsterdam). The pages are PMLR 300:2674–2682. PMLR gives the publication date as 2026-08-30, where the LIT has 2026-01-01. The first author's surname as printed is "Ghadimi Atigh"; the PMLR slug and the LIT use "Atigh". The conference is AISTATS 2026, Tangier.

### Summary
A method for image classification when training labels come at any level of a class tree (animal, bird, albatross, Laysan albatross) and evaluation is at the leaves.

- **Prototypes.** The tree is embedded once in a Poincaré ball as prototypes. Leaves are first placed with maximum separation (Kasarla et al. 2022). Then all nodes are fitted by minimising the distortion between hyperbolic and tree distances (Sala et al. 2018, which the record holds as LIT-874).
- **Network.** A ResNet50 maps images into the ball, z_i = exp_0(φ_θ(x_i)).
- **Three losses.**
  - (i) Cross-entropy over the leaf prototypes, with distance logits. A coarse label becomes a uniform target over the leaves under it (Eq. 9).
  - (ii) Ganea et al.'s entailment-cone angle penalty (LIT-866), which pushes the image into the cone of its label's prototype, whether that label is a leaf or an internal node (Eq. 11–13).
  - (iii) A penalised Busemann loss toward the "ideal prototype", which is the label prototype's direction projected onto the boundary. It pulls samples outward, where the leaves lie (Eq. 14–15).
- **Benchmark.** Mixed-granularity data is simulated by replacing a fraction ρ of the leaf labels, each with a non-root ancestor drawn uniformly (§4.2).

### Contribution
It extends hyperbolic prototype classification from leaf-only supervision to supervision at any depth, without a separate head for each level. It also sets a benchmark protocol: a random ancestor of any depth, with ρ up to 0.975.

### Key results
- **Ablation on CIFAR-100** (§5.1, Table 1): "For ρ = 0.95, the baseline is stuck at 20.22%, while our losses progressively improve to 49.25%, 50.42%, and 56.13%." Most of the gain comes from L_CE, which stops discarding the coarse samples. At ρ = 0.5, adding L_Buse lowers accuracy (67.57 → 65.80 with all three losses), so the Busemann term pays only at high ρ.
- **Against a naive leaf-only network and Chen et al. (2022a)** (§5.2, Table 2): on FGVC-Aircraft at ρ = 0.95, the naive network gets 4.14% and the method 62.55%. In the parent-only setting, Chen et al. get 15.65% and the method 65.89%. The paper's lesson: "we cannot afford to simply ignore samples if we don't like the annotations, we have to make use of them."
- **Recovering withheld fine labels on the training set** (§5.3, Table 3): "reaching 69.88% at ρ = 0.95 and 62.50% at ρ = 0.975, compared to just 20.30% and 12.36% for the baseline."
- **Euclidean prototypes** (A.4, Table 5): "Hyperbolic prototypes clearly and consistently outperform their Euclidean counterparts (e.g., 59.93 vs. 47.8 at ρ = 0.90)".
- **CUB-200** (A.2, Table 9): the gains in leaf accuracy are small (21.20 vs 17.77 at ρ = 0.95; 29.82 vs 27.72 at ρ = 0.90). The large gains are in sibling and cousin accuracy (sibling 80.12 vs 43.65 at ρ = 0.95).
- **Design intuition** (§1): "the more specific a sample's label, the more narrowly defined the region in the embedding space should be for optimization."

### Assumptions
- A known, fixed tree (the hierarchies are from Kasarla et al. 2025a), with the prototypes fixed before the network is trained.
- Coarse labels are correct, only less specific.
- Coarsening is simulated uniformly at random, independent of how hard the image is, though the paper motivates it by blur and annotator expertise.
- Some leaf labels always remain, and evaluation is only at the leaves.
- Settings: embedding dimension c − 1; cone aperture constant K = 0.1. The CIFAR-100 Busemann gating thresholds (d_B = 0.4, Ξ_B = 50°) are set by hand.

### Concepts
Multi-granular supervision; hyperbolic class prototypes; maximum class separation; distortion-minimising tree embedding; the entailment cone as the region a coarse label licenses; the ideal prototype and the Busemann function (distance to a boundary point); depth encoded by radius (general concepts near the origin, specific ones near the boundary); sibling and cousin accuracy as measures of error severity; label completion.

### Verdict on the exchange's characterization
LIT-2993 and CLAIM-839 say that "hyperbolic learning with labels at several granularities is nearby" to backward-compatible, temporal cone restriction. That is accurate as far as it goes, with two cautions:
- (a) "Coarse-to-fine" in §3.2's title names the label projection (a label projected to a boundary direction). It is not a training schedule or an order in which concepts are acquired. The paper says nothing about learning dynamics or checkpoints.
- (b) The nesting it uses is semantic: a label's cone contains its descendants' cones, applied to each sample at one time. It is not a filtration over training time.

No entry attributes a result to it wrongly. The LIT's summary ("accepts supervision at any level of a label hierarchy") is right.

### Bearing on named codes
- **CLAIM-839: parallel, and weak support for the semantic half only.** The paper is a working instance of supervision as a region whose narrowness matches the label's specificity. A coarse label confines z_i to the coarse cone and spreads the target over F(y), a set-valued target (§3.2, Eq. 9 and 12). It gives nothing on Blackwell informativeness across checkpoints, on branching, or on temporal restriction U_i(t+Δt) ⊆ U_i(t). Its framing ("images are optimized to the correct region", abstract) fits the claim's rule that narrowing counts only while it stays correct. It leaves the claim's thesis open.
- **CLAIM-800: background.** The paper uses Ganea's nested cones as a training target, not as an occupancy measure. It measures learning by held-out leaf, sibling and cousin accuracy, an independent measure of the kind CLAIM-800 asks for. It has no dynamics, so it says nothing on boundary motion against flow. Its prototypes are fixed while the network trains, so CLAIM-800's boundary term is zero by design.
- **LIT-2957 (Yang 2023): parallel.** Table 3 shows a hierarchy-aware model recovering withheld fine labels on its training set (69.88% at ρ = 0.95). That fits "coarse supervision does not erase finer structure". But it is not a coarse-only setting: 5% of the leaf labels remain, and the uniform target over F(y) and the fixed leaf prototypes put the fine structure in. So it does not test Yang's finding.
- **QUESTION-512** (which CLAIM-839 answers): background.

### Limitations
- Coarsening is simulated, uniform over ancestors, not real annotator behaviour.
- A ResNet50 trained from scratch, on small datasets, over three runs, with no theory.
- One external baseline (Chen 2022a), which handles three levels and whose code supports only the parent-only setting.
- Gains in leaf accuracy on CUB-200 are small.
- The Busemann term hurts at low ρ and needs hand-set gating on CIFAR-100.
- Table 5's "Ours" figures (59.93, 56.13, 50.10) are Table 1's test accuracies, although Table 5's caption says "reclassifying the training set". Either the caption or the numbers are mislabelled.

### Candidate THEORY
"With a class tree embedded as hyperbolic prototypes, an image classifier trained on labels drawn from any level of the tree, with a coarse label as a uniform target over its leaves, an entailment-cone penalty toward the label's cone and a Busemann pull toward the label's boundary direction, reaches far higher leaf accuracy than one that discards non-leaf labels, and recovers withheld fine labels, when most labels are coarse."

promote_when: a replication on a dataset with real (not simulated) mixed-granularity annotations, or an independent reimplementation that reproduces the gap over the discard-coarse baseline on CIFAR-100 or FGVC-Aircraft at ρ ≥ 0.9.

## Step 3: recheck (2026-11-22)

Search terms: busemann, ideal prototype, poincar, entailment cone, Ganea, coarse label, coarse-to-fine, multi-granular, label hierarch, hierarchical classification, Mettes, maximum class separation, Kasarla. Held entries the first search (on LIT-2993) missed:

- **LIT-866** (Ganea et al. 2018, Hyperbolic Entailment Cones; Active). Its cone and angle penalty are used directly as L_entail (Eq. 11–13). Bearing: background, and an application of it. Cite it from the NOTE.
- **LIT-874** (Sala et al. 2018, Representation Tradeoffs for Hyperbolic Embeddings; Active). Its distortion objective is used to embed the prototypes (Eq. 6), and A.4 cites it for hyperbolic beating Euclidean geometry. Bearing: background.
- **CLAIM-816** (in the Poincaré ball, depth is encoded by radius, and dimension narrows the radial range; Proposed). The paper relies on depth by radius ("general concepts lie closer to the origin and more specific concepts closer to the boundary", §3.2) and adds the Busemann term because the other losses leave samples "biased towards internal classes". That is an empirical sign that the radial range has to be enforced, not had for free, which fits CLAIM-816's worry. The paper also uses dimension c − 1 (99 to 195) without remarking on concentration. Bearing: parallel, weakly supports.
- **ARG-153** (the cost of restricting cones carries to the angular part only; Proposed). The paper's L_entail is purely angular, the angle between the geodesic and the cone's axis, while the radial work is done separately by L_Buse. That split matches ARG-153's division between angular and radial structure. Bearing: parallel.
- **LIT-871** (Hyperbolic Representation Learning: Revisiting and Advancing), **LIT-879** (Hyperbolic Neural Networks) and **LIT-1808** (hierarchy matching with OT over hyperbolic spaces): background for the hyperbolic-learning line. The paper cites none of them.
- **LIT-862** (Saxe et al., semantic development in deep networks) and **CLAIM-828** (a parent gate makes acquisition follow a partial order) concern coarse-to-fine acquisition in time. The paper does not touch them; "coarse-to-fine" is a false friend here. Bearing: contrast, by name only.
- **LEAD-210** (track probe-set representations across checkpoints) asks the temporal question the paper does not. Bearing: none beyond contrast.

## Neighbours
Not needed: the work itself was read.
