---
number: 684
status: Read
formerly:
- NOTE-tmpc1el0
paper: 'LIT-880'
title: 'The Sparse Random Hierarchy Model'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the PMLR PDF (ICML 2024, PMLR 235:48369–48389,
    21 pp. with appendices), text extracted with pdftotext and kept as
    paper.txt in the scratchpad download directory
    dl/reg-cited-2404.10727: abstract, §§1–8, Appendices A–G, and the
    reference list scanned for the works the paper builds on. The arXiv v2
    PDF was compared and differs only in typesetting. The one-step gradient
    computation of Appendix C (Eqs. 9–12) was followed step by step, and
    Eq. 5 was re-derived from Eq. 3 (the extraction garbles it). Figures
    were read from captions, axis labels and text, not from plotted values.
    The networks' code and Petrini et al.'s CIFAR-10 study, from which
    Fig. 1A–B is adapted, were not read. LIT-877 and NOTE-677 were read
    first, so this note records what the sparse model adds.
date: '2026-10-09'
summary: >-
  Adds sparsity to the Random Hierarchy Model, so that labels are unchanged
  by discrete displacements of the informative features, and shows by
  experiment that deep networks learn it from a number of examples
  polynomial in the input dimension, (s0 + 1)^L n_c m^L up to a factor
  s^(L/2) without weight sharing and (s0 + 1)^2 n_c m^L with it, and that
  hidden layers become insensitive to synonym swaps and to feature
  displacements at about the same training-set size as test error falls.
  That coincidence is offered as the reason deformation stability tracks
  performance on images, which is not tested on images.
---
<!-- inactive-ok-file: QUESTION-025 THEORY-185 THEORY-186 THEORY-195 THEORY-200 — Proposed or open; cited as what this reading produced or bears on -->

# NOTE-684: The Sparse Random Hierarchy Model

## Contribution

A version of the Random Hierarchy Model ([LIT-877](../literature.d/LIT-877.md), [NOTE-677](NOTE-677.md)) in which most
input positions are empty and the informative features may sit at several
positions without changing the label. That gives a hierarchical task with
an exact, discrete analogue of the stability to small deformations long
proposed as what makes images learnable (Bruna and Mallat), so the two
pictures, compositional hierarchy and deformation invariance, can be
studied in one model. The paper measures how sparsity changes the number of
examples deep networks need, shows that weight sharing makes that cost far
smaller, and finds that synonym invariance, deformation invariance and
low test error arrive at the same training-set size.

## Key insight

If a whole is made of a few informative parts that may each sit at several
nearby places, then the displaced versions of a part, like its synonymous
versions, carry exactly the same statistical association with the label.
A learner that groups lower-level patterns by their association with the
label therefore becomes invariant to both kinds of variation in one step,
and only once it has enough data to see that association through the
noise. Deformation stability is then not a separate achievement but a
by-product of learning the hierarchy, which is why it tracks performance.

## Assumptions

- **Grammar.** The RHM of [LIT-877](../literature.d/LIT-877.md) at maximal multiplicity m = v^(s−1) and
  n_c = v in the main experiments (n_c = m = v = 6 or 8, and n_c = m = 10,
  in some figures), uniform production rules, an uninformative symbol
  added at every level. Sparsity A: each informative child in its own
  sub-patch of s0 + 1 positions with exactly s0 empties, positions chosen
  independently; sparsity B: s children anywhere in the s(s0 + 1) patch, in
  order. Empties generate all-empty patches. d = (s(s0 + 1))^L.
- **Input.** One-hot over v at informative positions; empty positions are
  all-zero columns.
- **Networks.** LCNs and CNNs with L hidden layers, filter size and stride
  s(s0 + 1) matched to the generative tree, 512 channels; fully connected
  networks of L layers (256–512 units); VGG, ResNet and EfficientNet
  variants. SGD with batch size 4, momentum 0.9, learning rates from a grid
  search, cross-entropy stopped at 10⁻³ (10⁻² for the common
  architectures). Experiments at s = 2 and 3, L = 2 and 3, s0 from 0 to 6.
- **The argument's regime.** Appendix C: an LCN with L hidden layers,
  widths H → ∞, readout fixed i.i.d. Gaussian, all weights initialised to
  the uniform vector, so the output is zero at start; one full-batch
  gradient step. The step is then the non-sparse one with P replaced by
  its expected informative share; it relies on Cagnetta et al. for what
  that step does.

## Key results

- **Eq. 3, Figs. 4B, 10.** LCN: P* (test error 10%) ≈ C0(s, L)(s0 + 1)^L
  n_c m^L with C0 ∼ s^(L/2). *Holds in:* s = 2, 3; L = 2, 3; s0 ≤ 4; v up
  to about 12. Empirical.
- **Eq. 4, Figs. 4C, 13.** CNN: P* ≈ C1(s0 + 1)^2 n_c m^L, quadratic in
  s0 + 1 whatever L. *Holds in:* the same ranges, s0 ≤ 6. Empirical; the
  authors say the quadratic dependence "remains to be understood".
- **Eq. 5, Fig. 5.** At fixed d, P*_LCN ∝ F^(log m/log s − 1/2)
  d^(log m/log s + 1/2), F = (s0 + 1)^(−L), increasing in F when m > √s:
  sparser is easier for a fixed input size. A rewriting of Eq. 3, not a
  separate measurement.
- **Figs. 7, 8.** Sparsity B obeys the same scalings as A (L = 2, 3;
  s0 = 1–4; m = v = n_c = 6).
- **Eq. 8, Figs. 6, 11, 14, 16.** P*_S (S_2 below a threshold) ≈ P* and
  P*_D (D_2 below a threshold) ≈ P*, for LCNs, CNNs and fully connected
  networks. Thresholds: S_2 at 30%, 40%, 50% or 20% and D_2 at 10% or 20%,
  "tuned based on the form of S_2 and D_2 versus P".
- **Figs. 12, 15.** S_{k,l} and D_{k,l} fall for k ≥ l + 1 at large P, all
  levels at the same rescaled P. *Holds in:* L = s = 2, m = v = n_c = 8;
  the authors report other s and L as checked but not shown.
- **Figs. 1C–F, 9, 17.** On one SRHM instance (L = s = s0 = 2,
  n_c = m = 10, P = 7400), test error across seven architectures rises with
  the output's (and an 80%-depth layer's) sensitivity to deformations and
  to synonym swaps, mirroring Petrini et al.'s CIFAR-10 correlation for
  deformations (Fig. 1A–B, adapted).
- **Appendix C, Eq. 12.** For an LCN, each first-layer weight sees one input
  position, informative with probability (s0 + 1)^(−L); the first gradient
  step is the non-sparse one with P′ = (s0 + 1)^(−L) P. Exact for that
  model; the jump to P*_LCN is by appeal to [LIT-877](../literature.d/LIT-877.md).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Sparsity in a hierarchical generative model makes the label invariant to discrete displacements of informative features | strong | by construction, §3 |
| C2 | Deep LCNs learn the SRHM from ≈ s^(L/2)(s0 + 1)^L n_c m^L examples, polynomial in d | moderate | Figs. 4B, 10; empirical, s ≤ 3, L ≤ 3 |
| C3 | Weight sharing reduces the sparsity cost to ≈ (s0 + 1)^2, independent of L | moderate | Figs. 4C, 13; empirical, unexplained |
| C4 | Synonym invariance, deformation invariance and task performance are acquired at the same training-set size | moderate | Figs. 6, 11, 14, 16; thresholds tuned by eye |
| C5 | The (s0 + 1)^L factor for LCNs is the dilution of informative data seen by each weight | moderate | Appendix C (exact one-step) plus appeal to [LIT-877](../literature.d/LIT-877.md) |
| C6 | This explains the correlation of deformation stability with test error on real images | weak | analogy; synonym sensitivity not measured on images (§7) |
| C7 | At fixed input dimension, sparser data are easier for LCNs | moderate | algebra on Eq. 3 (Fig. 5), assuming Eq. 3 extrapolates |

## Concepts

- **Sparsity A / B** — the two ways of placing s informative children in a
  patch of s(s0 + 1): one per sub-patch, independently (A); anywhere, order
  kept (B). The SRHM is model A.
- **Discretised diffeomorphism τ** — re-drawing the positions of the
  informative features within their allowed places, values unchanged. Not
  a smooth map; it changes no feature, only where it sits.
- **Synonymic exchange p** — replacing each informative level-1 tuple by
  another of its parent's m tuples, positions unchanged.
- **S_k, D_k (S_{k,l}, D_{k,l})** — layer k's mean squared change under p
  or τ applied at level l, relative to its change between two random test
  inputs (Eqs. 6, 7, 13, 14).
- **Relevant fraction F** — (s0 + 1)^(−L), the share of informative
  positions.

## Connections

The model is [LIT-877](../literature.d/LIT-877.md)'s with empty positions, and the account of why
learning succeeds is [LIT-877](../literature.d/LIT-877.md)'s correlation argument ([THEORY-195](../theory.d/THEORY-195.md)) with the
data diluted. The deformation side comes from Bruna and Mallat's
scattering networks and Petrini et al.'s measurements of relative stability
to diffeomorphisms; neither is held in the record. The locality literature
it cites (Favero et al., Bietti, Mei et al.) and the hierarchical models of
Mossel and Malach and Shalev-Shwartz are [LIT-877](../literature.d/LIT-877.md)'s lineage too. Against the
geometric-deep-learning blueprint ([LIT-319](../literature.d/LIT-319.md)), which takes deformation
stability as a prior to build in, this paper asks when a network that has
it only partly built in (local filters, with or without weight sharing)
acquires it from data.

## Bearing on the record

- **[THEORY-195](../theory.d/THEORY-195.md).** Extends it. The sample-size law there, n_c m^L, gains a
  factor for sparsity that depends on the architecture, and the invariance
  that arrives with learning gains a second kind, to position. The
  identification problem [THEORY-195](../theory.d/THEORY-195.md) names, that the correlation threshold
  and the grammar's size are the same number, is eased only for LCNs: the
  (s0 + 1)^L factor follows from diluting the correlation signal without
  changing the grammar, which is the kind of separation [THEORY-195](../theory.d/THEORY-195.md)'s
  promote_when asks for, though here it is predicted by a one-step
  argument and confirmed by curve collapse rather than tracked level by
  level. The CNN's (s0 + 1)^2 is not predicted by that argument and is
  unexplained.
- **New account.** [THEORY-200](../theory.d/THEORY-200.md), Proposed: on sparse hierarchical data,
  invariance to synonym swaps and to feature displacements and good
  performance arrive at one training-set size.
- **[QUESTION-025](../questions.d/QUESTION-025.md).** No bearing beyond [LIT-877](../literature.d/LIT-877.md)'s. Constituency, not
  attributes; no co-occurrence embedding, no linear directions.
- **[THEORY-186](../theory.d/THEORY-186.md).** Same contrast as for [LIT-877](../literature.d/LIT-877.md): every level is learned at
  one training-set size, not in coarse-to-fine stages over time.
- **Practice.** The paper gives no instruction; the weight-sharing result is
  a measured sample-size ratio on a synthetic task. Its subject, what
  structure of data makes learning possible, is the anthology's
  `signal-structure`, hence the flag on the LIT.

## Limitations

- **Fitted laws over a narrow range.** s ∈ {2, 3}, L ∈ {2, 3}, maximal m
  only; the prefactors s^(L/2) and C1 are fits, and the CNN exponent 2 has
  no account.
- **The coincidence of invariances is measured with tuned thresholds.**
  P*_S and P*_D are read at thresholds chosen per setting from the shape of
  the curves; that the three sizes agree is shown by scatter plots on log
  axes over about two decades, so a constant factor between them would not
  show.
- **Displacement and synonymy are tied by construction.** Both
  transformations keep the parent and so keep its class statistics; that
  one grouping removes both is close to built in, so the experiment tests
  whether trained networks do the grouping, not whether the two
  invariances could have come apart in this model.
- **The image claim is untested.** The authors say they lack a way to
  measure synonym sensitivity on images, and suggest diffusion-based
  resampling (Sclocchi et al.) or text synonyms; neither is done. Fig. 1's
  SRHM panels show the same shape of correlation as CIFAR-10's, which is a
  resemblance, not a test.
- **The discrete deformation is a weak stand-in.** Moving one-hot features
  among empty positions is not a smooth map of a dense signal, and the
  SRHM's informative fraction (as low as 7⁻²) is chosen, not matched to
  images.
- **Architectures are told the tree** (filter size and stride s(s0 + 1)),
  except the fully connected and common architectures, whose sample sizes
  are not reported as scaling laws.

## Open questions

- Why the CNN's sparsity cost is (s0 + 1)^2 and not (s0 + 1)^L or 1: a
  one-step argument with weight sharing, where each filter pools all
  positions at a scale, would be the place to look.
- Whether, on images, a network's sensitivity to swapping low-level parts
  generated by a diffusion model falls at the same training-set size as its
  deformation sensitivity and its test error, which is the test §7
  proposes.
- Whether the invariances can be made to arrive at different sizes, for
  instance with non-uniform displacement probabilities, which would show
  whether they are one grouping or two.
