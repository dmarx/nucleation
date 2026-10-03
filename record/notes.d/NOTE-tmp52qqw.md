---
status: Read
paper: 'LIT-tmpbfzro'
title: 'Traces of Class/Cross-Class Structure Pervade Deep Learning Spectra'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read from arXiv v1 (58 pages, text layer). Sections 1–10 read in full;
    Appendix A (derivation of Eq. 6.4) and Appendix B (Lemma 8.1, Lemmas
    B.1–B.2, Theorem 8.1) followed in outline; Appendix C (Lanczos tools,
    as in the 2018 preprint) and Appendix D (experimental details) skimmed.
    Figures are read from their captions and the text.
date: '2026-10-03'
summary: >-
  G = Gclass + Gcross + Gwithin + Gc=c′ (Eq. 6.4); knockouts give C outliers
  to Gclass, a C² mini-bulk to Gcross, the bulk to Gwithin, in log-spectra.
  Gˡ = Σ w (hhᵀ) ⊗ (δδᵀ) (Eq. 7.8), so gc ≈ hc ⊗ δc. K-FAC Hˡ ⊗ Δˡ misaligns
  G's outliers; CFAC Ave_c Hˡc ⊗ Δˡc aligns them at deep layers. For
  multinomial logistic regression on a Gaussian model the expected Fisher has
  C outliers, C(C−2) mini-bulk and a bulk (Theorem 8.1).
---

<!-- inactive-ok-file: LIT-354 — Deferred: Watanabe's book is unread; named in the bearing section, with no relation claimed -->

# NOTE-tmp52qqw: Traces of Class/Cross-Class Structure Pervade Deep Learning Spectra

## Contribution

A single account of the bulk, mini-bulk and outliers seen in the spectra of
every deep-learning object people measure, from the index structure that
cross-entropy imposes; a demonstration that the account holds per layer and
across layers through Kronecker and Khatri–Rao products; an exact spectrum
for a toy model; and a better-aligned alternative to K-FAC.

## Key insight

Every quantity in a trained classifier carries two class indices: the class
an example belongs to, and the class the loss is evaluated against. Averaging
along those indices gives a global mean, C class means and C² cross-class
means, and the second moments of those means are low-rank and large. Each
spectral feature is one level of that hierarchy. Because a layer's gradient
is features ⊗ errors, the Fisher inherits the class structure of both, but
only paired class by class.

## Assumptions

- **Balanced classes** (Definition 1.3, footnote).
- **Cross-entropy with softmax**, giving the three-index structure and
  G = Σ w gᵢ,c,c′gᵢ,c,c′ᵀ with w = pᵢ,c,c′/nC (Eq. 6.2, Appendix A).
- **MLP with ReLU** for Section 7 (batch norm before ReLU in practice,
  ignored in the exposition); eight layers of 2048 units.
- **C smaller than the feature dimension**, otherwise no bulk-and-outliers
  shape is visible, though the means still exist (Section 9.2).
- **Section 8 only**: canonical classification model xᵢ,c = t e_c + zᵢ,c,
  z ~ N(0, I), and symmetric probabilities (1 − α on the true class,
  α/(C − 1) elsewhere).

## Key results

- **Definitions 1.3–1.12.** Class and cross-class block structure; global,
  class and cross-class means; between-class second moment, between-cross-class
  covariance, within-cross-class covariance (a MANOVA two-way layout).
- **Definitions 3.1–3.3.** Subtraction knockout A ⊖ B; projection knockout
  (I − BB†)A(I − BB†); attribution = the feature disappears after the
  knockout.
- **Sections 4–5.** Hessian = G + E; outliers attributable to G, bulk
  largely to E (Figures 3–4).
- **Eq. 6.4, Figure 5.** In log G for VGG11 on CIFAR-10 (136 per class),
  knocking out Gclass removes the C outliers, Gcross the left mini-bulk,
  Gwithin the main bulk; Gc=c′ has no visible effect (gradient means vanish
  at convergence).
- **Figure 6.** More epochs separate the Gcross and Gwithin bulks; more data
  merges them; the Gclass–Gwithin distance changes little.
- **Eqs. 7.3–7.8.** gˡᵢ,c,c′ = hˡ⁻¹ᵢ,c ⊗ δˡᵢ,c,c′;
  G = Σ w (hhᵀ) ⊙ (δδᵀ) (Khatri–Rao across layers),
  Gˡ = Σ w (hˡ⁻¹hˡ⁻¹ᵀ) ⊗ (δˡδˡᵀ).
- **Figures 7–8 (features).** Top C outliers of Hˡ attributable to Hˡclass,
  the largest to the global mean; they emerge from the bulk with depth, and
  the ratio of second-largest to smallest class-mean eigenvalue falls with
  depth, i.e. class means become closer to orthogonal.
- **Figures 9–10 (backpropagated errors).** C outliers from Δclass, C²
  from Δcross; class information strong near the output and lost toward the
  input; error class means nearly orthogonal at the last layer.
- **Definition 7.1, 7.2, Figures 11–12.** K-FAC Gˡ_KFAC = Hˡ ⊗ Δˡ;
  CFAC Gˡ_CFAC = Ave_c Hˡc ⊗ Δˡc. CFAC's spectrum aligns with Gˡ much better
  at deep layers; at CIFAR-10 layers 7–8 "almost perfectly"; at some shallow
  layers (CIFAR-10 layer 2) no better than K-FAC.
- **Figure 13 (weights).** With weight decay, Wˡ = −(1/η)Ave δhᵀ at a
  stationary point; top C singular values attributable to Wˡclass.
- **Lemma 8.1, Theorem 8.1.** E G = (s/C)blkdiag(U¹, …, U^C, 0) + I ⊗ Ū,
  s = t², Uᶜ = diag(p·,c) − p·,cp·,cᵀ. Eigenvalues: (α/(C−1))(s(1 − α) +
  (2 − αC/(C−1))) for i ≤ C; (α/(C−1))(s/C + (2 − αC/(C−1))) for
  C < i ≤ C(C−1); (α/(C−1))(2 − αC/(C−1)) up to D(C−1); zero after.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Outliers, mini-bulk and bulk of the Fisher are caused by class means, cross-class means and within-cross-class variation | moderate: knockouts on a few settings, read visually | Figures 5–6 |
| C2 | The same pattern holds in features, errors, weights and the Hessian | moderate: MLP on MNIST, Fashion-MNIST, CIFAR-10; Hessian on VGG11 | Figures 3–4, 7–10, 13 |
| C3 | Per layer, gradient class and cross-class means are approximately Kronecker products of feature and error means | weak to moderate: inferred from CFAC's alignment, not measured directly | Section 7.12 |
| C4 | CFAC approximates the layer Fisher's spectrum better than K-FAC | moderate: one MLP architecture, three datasets, spectra only; no optimization run | Figures 11–12 |
| C5 | For MLR on the canonical model the expected Fisher has C outliers, C(C−2) mini-bulk eigenvalues and a bulk, all separating with SNR | strong (proof), for a stylised model with symmetric probabilities | Lemma 8.1, Theorem 8.1 |
| C6 | Outlier-to-bulk ratios predict misclassification, also in deepnets | weak for deepnets: proved for MLR; for deepnets an interpretation of layer-wise separation | Sections 7.6, 8.2 |
| C7 | Batch norm's suppression of Hessian outliers (Ghorbani et al.) is explained by removal of the feature global mean | weak: argued in prose | Section 9.3 |

## Concepts

- **cross-class c′**: the would-be label against which the loss of an
  example is evaluated.
- **extended gradient gᵢ,c,c′**: ∂ℓ(f(xᵢ,c), yc′)/∂θ = (∂f/∂θ)ᵀ(pᵢ,c − yc′).
- **mini-bulk**: about C² eigenvalues that form a continuous lump rather
  than separate spikes.
- **CFAC**: class-distinct factorized approximate curvature, an average over
  classes of per-class Kronecker products.

## Connections

- **Papyan 2019 ([LIT-tmptvdrl](../literature.d/LIT-tmptvdrl.md))** introduced the hierarchy for G; this
  paper reweights it by probabilities, finds its two hidden components and
  extends it to other objects.
- **Papyan 2018 ([LIT-tmpnmspc](../literature.d/LIT-tmpnmspc.md))**: the Lanczos machinery and the G/E
  attribution.
- **Martens & Grosse 2015 ([LIT-tmpuzob3](../literature.d/LIT-tmpuzob3.md))**: defined as in that paper, then
  measured against the true Fisher and against CFAC.
- **Amari (1998, [LIT-tmp26jbc](../literature.d/LIT-tmp26jbc.md))** is cited for the natural gradient's use
  of G.
- **Sagun et al., Ghorbani et al., Li et al. (2019), Jastrzębski et al.
  (2020), Martin & Mahoney, Pennington & Bahri, Pennington & Worah** are the
  measurements and RMT models it re-reads.

## Bearing on the record

- **The owner's object.** "Fisher-spectrum block structure, the object
  being thresholded": in this paper, a spectral threshold at the bulk edge
  separates three nested sets: the global-mean outlier, C − 1 class
  directions, and the C(C − 1) cross-class mini-bulk. Which of them a
  threshold keeps depends on whether it sits above or below the mini-bulk.
- **THEORY candidates (not filed).** (a) "A trained classifier's Fisher is
  a low-rank class/cross-class component plus a within-class bulk, and the
  class component is what a spectral threshold retains." Sources:
  [LIT-tmpbfzro](../literature.d/LIT-tmpbfzro.md), [LIT-tmptvdrl](../literature.d/LIT-tmptvdrl.md). (b) "Kronecker approximations that average
  over classes before factoring misplace the class directions of the
  Fisher." Sources: [LIT-tmpbfzro](../literature.d/LIT-tmpbfzro.md), against [LIT-tmpuzob3](../literature.d/LIT-tmpuzob3.md).
- **Singular learning.** Not discussed by the paper. Its picture, about C²
  informative directions over a bulk over a large null space, is
  consistent with a degenerate Fisher of the kind Watanabe ([LIT-354](../literature.d/LIT-354.md))
  theorises, but it measures eigenvalue magnitudes, not the local
  geometry that a real log canonical threshold describes.
- `anthology-candidate`.

## Limitations

- Attribution by visual knockout; no quantitative alignment metric.
- The Kronecker approximation of class means is supported indirectly.
- CFAC is not tested as an optimizer.
- Balanced classes only; C less than feature dimension.
- Section 9.1 urges the field to stop studying the Hessian and study
  features and errors instead: a recommendation, not a result.

## Open questions

- Does CFAC make a better optimizer, and at what cost (it needs class labels
  and C pairs of factors per layer)?
- Do the same structures appear in the Fisher of language models, where C is
  the vocabulary size and far larger than many layer widths?
- Why do error class means lose orthogonality as they are backpropagated?

## Corrections

- none (there was no seed)
