---
status: Read
paper: LIT-tmpfjk24
title: 'Generalized Linear Mode Connectivity for Transformers'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read from arXiv v2 (21 pages). Main text and Appendices A–D read in
    full; Appendices E and F read for statements. Table 2 and the
    appendix model accuracies read from the text layer; Figures 3–9 from
    captions and text.
date: '2026-10-03'
summary: >-
  Symmetry hierarchy S1 permutation ⊂ S2 semi-permutation ⊂ S3 orthogonal ⊂
  S4 invertible. Transformer alignment = P_FF per layer, semi-permutation
  P̃_H over heads (matched on QK and OV circuits), one orthogonal O on the
  residual stream after LayerNorm → RMSNorm. Test-loss barriers (Table 2):
  vanilla 1.69–4.34, weight matching 0.34–1.56, learned matching 0.00 (ViT
  ×3), 0.02 (Tiny Shakespeare), 0.42 (BookCorpus); permutation-only learned
  0.29–1.60. Learned matching mainly refines O. Small models only.
---


# NOTE-tmpue8zy: Generalized Linear Mode Connectivity for Transformers

## Contribution

Re-basin methods had brought linear mode connectivity to MLPs, VGGs and wide
ResNets, but transformers kept a barrier after permutation alignment. This
paper names the larger symmetry group a transformer has, writes alignment
algorithms over it, and gets zero or near-zero barriers between
independently trained ViTs and small GPT-2s, for pairs, triples and models
of different widths.

## Key insight

Permutations are the symmetries of an elementwise nonlinearity, but most of
a transformer is not elementwise. Its residual stream passes only through
normalisation and linear maps, so any rotation of that stream, undone in
the next layer, leaves the function unchanged. Two runs differ by such a
rotation, as well as by a relabelling of units and heads. Aligning only the
labels leaves the rotation in place, and the straight line between the
models goes through the mismatch.

## Assumptions

- **Exact functional equivalence** for the hard classes; soft (doubly
  stochastic) permutations are only approximately equivalent (§3.1,
  Appendix D).
- **Reparameterisation**: LayerNorm is rewritten as RMSNorm(ZM)·diag(α)√D +
  1βᵀ, with M and diag(α)√D absorbed into adjacent linear layers, and
  attention heads are represented by their QK and OV products. The
  authors note this changes the architecture while preserving the function
  (Appendix A).
- **Models (Appendix B)**: ViT with 6 layers, 8 heads and embedding 256 for
  CIFAR (83.81% CIFAR-10 test accuracy), and with 8 layers and embedding 384
  for Tiny ImageNet (44.19%). GPT-2 with 6 layers and embedding 256 for Tiny
  Shakespeare (test loss 5.28), and with 6 layers and embedding 512 for
  BookCorpus (test loss 3.55, 5 epochs). AdamW throughout.
- **Barrier**: Eq. 1 on the test split; learned matching optimises the
  alignment on training data.

## Key results

- **Table 2 (pairwise test-loss barrier, mean ± s.e.)**:

  | method | CIFAR-10 | CIFAR-100 | Tiny ImageNet | Tiny Shakespeare | BookCorpus |
  |---|---|---|---|---|---|
  | vanilla | 1.69 | 2.46 | 2.84 | 2.02 | 4.34 |
  | activation matching | 1.27 | 2.11 | 1.86 | 1.43 | 4.05 |
  | weight matching (theirs) | 0.36 | 0.69 | 0.47 | 0.34 | 1.56 |
  | learned, permutations only | 0.45 | 0.53 | 0.29 | 0.63 | 1.60 |
  | learned (theirs) | 0.00 | 0.00 | 0.00 | 0.02 | 0.42 |

- **Width-heterogeneous alignment (Fig. 3c)**: smaller GPT-2s (embedding
  1/16 to 1/2 of 512) aligned to a 512-wide one by a rectangular orthogonal
  map give paths "at or near zero barrier".
- **Three-way merge (Fig. 4)**: over the simplex of three CIFAR-10 ViTs,
  learned matching gives the widest region of near-zero deviation from the
  linear baseline.
- **Fig. 5**: O_WM has eigen-angles spread over [0, 2π]; O_LM O_WMᵀ has them
  near 0, so learned matching makes small corrections to the rotation.
- **Ablations (Appendix C)**: λ ∼ U(0.4, 0.6) beats U(0, 1), N(0.5, 0.1) and
  fixed 0.5 for consistency across seeds (Fig. 6). Orthogonal weight
  matching converges within about five iterations while permutation
  matching does not improve (Fig. 7). Learned matching from identity rather
  than from weight matching keeps positive barriers after 15 epochs (Fig. 8).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Transformer components admit permutation, semi-permutation, orthogonal and invertible symmetries as listed | strong (algebra) | §3, App. E |
| C2 | Independently trained small ViTs and GPT-2s can be brought to zero or near-zero test-loss barrier | strong for the sizes tested, with learned matching | Table 2, Fig. 3 |
| C3 | Permutation-only alignment does not suffice for transformers | moderate: permutation-only learned matching stays at 0.29–1.60 | Table 2, Fig. 7 |
| C4 | The remaining gap is in the residual-stream orthogonal map | moderate: eigen-angle analysis on learned vs weight-matched O | Fig. 5 |
| C5 | Multi-model and width-heterogeneous transformers share a low-loss region | moderate: three CIFAR-10 models; one width sweep on Tiny Shakespeare | Figs. 3c, 4 |

## Method

Weight matching: for each feed-forward layer, a permutation maximising
⟨W_ℓᴬ, PW_ℓᴮOᵀ⟩ + ⟨W_ℓ₊₁ᴬ, OW_ℓ₊₁ᴮPᵀ⟩ (Eq. 3) by coordinate descent. For
heads, a linear assignment on ‖QKᵢᴬ − QKⱼᴮ‖² + ‖OVᵢᴬ − OVⱼᴮ‖². For the
residual stream, Procrustes O = argmin ‖Rᴬ − RᴮO‖ (Eq. 4), solved by SVD.
Learned matching: latent Z matrices projected to permutations (Hungarian,
straight-through) and to orthogonal matrices (UVᵀ), trained with Adam on
the cross-entropy at the interpolation (Algorithm 1). Multi-model merging
builds a universe U by iterated alignment and averaging, then refines with
Dirichlet-sampled mixtures.

## Concepts

- **semi-permutation**: an M × N matrix with stochastic columns and at most
  one positive entry per row; allows splitting a unit across several.
- **QK and OV circuits**: W_Q W_Kᵀ and W_V W_O per head, invariant to any
  invertible map inside the head.
- **generalised LMC**: LMC after alignment by any function-preserving map in
  the hierarchy, not only permutations.
- **multi-model barrier**: the supremum over the simplex of loss minus the
  mixture of endpoint losses (Eq. 2).

## Connections

- **Git Re-Basin ([LIT-tmpd6bma](../literature.d/LIT-tmpd6bma.md))**: weight matching and STE learned matching
  are its methods widened to orthogonal maps. Its 32× ResNet-20 is the
  comparison point for how connected these transformers are.
- **Entezari et al. ([LIT-tmp2uwzo](../literature.d/LIT-tmp2uwzo.md))**: the single-basin conjecture, restated.
- **Zhou et al. ([LIT-tmpqazdt](../literature.d/LIT-tmpqazdt.md))**: cited for layerwise linearity under LMC.
- **Bo Zhao et al. ([LIT-tmp3x9zc](../literature.d/LIT-tmp3x9zc.md))**: the same GL symmetry of attention
  products, used there to build failure cases of LMC and here to align.
- **Tran et al. ([LIT-tmpl7hwn](../literature.d/LIT-tmpl7hwn.md))**: the MoE analogue, with expert-order
  permutations added; there the backbone is shared, here nothing is.

## Bearing on the record

- **[ANTH-THEORY-010](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-010.md)** asks for its account to be demonstrated on a
  transformer before promotion. This is that demonstration with a caveat:
  the symmetries that carry the barrier on a transformer are mostly not
  permutations. Report to the anthology rather than edit it.
- **[ANTH-SOTA-217](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/practices.d/SOTA-217.md)** (align permutations before averaging) is insufficient
  for transformers on this evidence; the residual-stream rotation has to be
  aligned too.
- A THEORY candidate: *the barrier between independently trained networks
  is the mismatch under the architecture's full function-preserving
  symmetry group, and for transformers that group is dominated by the
  orthogonal symmetry of the residual stream*.

## Limitations

- **Small models**: 6- to 8-layer ViTs at 44–84% accuracy, and 6-layer
  GPT-2s, as the authors note (Appendix A).
- **Learned matching optimises the quantity it reports.** It trains the
  alignment to minimise loss at the path midpoint region (λ ∈ [0.4, 0.6]) on
  training data. The test-loss barrier is still a held-out measurement, but
  a zero barrier from learned matching is weaker evidence of a pre-existing
  shared basin than a zero barrier from data-free weight matching. Sampling
  λ over [0, 1] gave higher barriers (Fig. 6).
- **BookCorpus keeps 0.42.** The authors leave open whether that is
  imperfect alignment or distinct solutions, citing Juneja et al. on NLP
  models with different generalisation strategies.
- **Architecture changes**: the RMSNorm rewrite is function-preserving but
  not the model as trained.

## Open questions

- Can a data-free estimate of O close the gap to learned matching?
- Do large pretrained language models, trained from different seeds, share
  a basin under the full symmetry group?

## Corrections

- none to a seeded skim (there was no seed)
