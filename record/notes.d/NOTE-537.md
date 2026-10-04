---
number: 537
status: 'Read'
formerly:
- NOTE-tmprlsgq
paper: 'LIT-652'
title: 'The Role of Permutation Invariance in Linear Mode Connectivity of Neural Networks'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full from the arXiv PDF (v2, 27 pages) through PyMuPDF text
    extraction: §§1–5 and Appendices A–E, including the proof of Theorem 3.1
    (Appendix D), followed for structure and checked at the statement and the
    final rate. Results are carried by plots, read from captions and the
    text. The anthology's reading of the same paper (ANTH-LIT-251, its
    ANTH-NOTE-131) was read for comparison.
date: '2026-10-03'
summary: >-
  Conjecture 1: wide SGD solutions can be permuted into one linearly
  connected basin. Theorem 3.1 proves an output-level version only for a
  one-hidden-layer net at uniform random init, rate Õ(h^{−1/(2d+4)}).
  The evidence is that independent solutions S and permutations S′ of one
  solution show the same barriers across width, depth and data; simulated
  annealing lowers barriers only for shallow nets on easy data.
---

# NOTE-537: The Role of Permutation Invariance in Linear Mode Connectivity of Neural Networks

## Contribution

A precise, bold conjecture about the global geometry of SGD solutions: that
the barriers between them are an artefact of ignoring permutation symmetry.
It comes with a systematic measurement of how barriers depend on width,
depth, architecture and task, a small theorem, and an indirect test that
compares real solution sets with a model in which the conjecture holds by
construction.

## Key insight

Two networks trained from different seeds might differ only as two
relabellings of the same network differ. If so, every barrier on the
straight line between them is the cost of interpolating between mismatched
labels, and the right relabelling removes it. Because the search over
labellings is factorial, the paper does not find the relabelling. It checks
instead that real pairs of solutions behave exactly as relabelled copies of
one solution would.

## Assumptions

- **Barrier** (Eq. 1): B(θ₁, θ₂) = sup_α L(αθ₁ + (1 − α)θ₂) − [αL(θ₁) +
  (1 − α)L(θ₂)], on training loss unless stated, evaluated at α = 1/2 as a
  surrogate for the supremum (the difference was under 10⁻⁴; footnote 3).
- **Invariances considered**: permutations of hidden units in each layer
  only. Rescaling invariance is set aside on the argument that SGD's implicit
  bias balances norms, so it rarely matters for SGD solutions (§3.1).
- **Theorem 3.1**: f_{v,U}(x) = vᵀσ(Ux), ReLU, h hidden units; entries of U,
  U′ uniform on [−1/√d, 1/√d] and of v, v′ uniform on [−1/√h, 1/√h]; input
  with ‖x‖₂ = √d. Random networks, not trained ones.
- **Conjecture 1** is restricted to SGD solutions and to widths at least some
  h; "most" is "with high probability over an SGD solution".
- **Training**: MLP, Shallow CNN (two conv layers), VGG and ResNet on MNIST,
  SVHN, CIFAR-10, CIFAR-100 (and ImageNet in Fig. 4c); 1,000 epochs (3,000
  for MLPs) or cross-entropy 0.01; barriers averaged over 5 random pairs.

## Key results

- **Width** (Fig. 2): barrier rises, peaks near the width needed to fit the
  training data (checked against Fig. 8), then falls. MLPs peak at lower
  width than CNNs. VGG-16 and ResNet-18 barriers stay high at every width.
- **Depth** (Fig. 3): with width fixed at 2¹⁰, adding layers raises the
  barrier quickly for MLPs and Shallow CNNs; VGG(11–19) and ResNet(18–50)
  saturate high.
- **Task and architecture** (Fig. 4): for shallow nets, lower test error goes
  with lower barrier; deep nets cluster at low error and high barrier.
- **Theorem 3.1**: |f_{αv+(1−α)v″, αU+(1−α)U″}(x) − αf_{v,U}(x) −
  (1 − α)f_{v′,U′}(x)| = Õ(h^{−1/(2d+4)}) with probability 1 − δ, for a
  permutation (v″, U″) of (v′, U′). The proof grids the input-weight cube,
  matches rows of U and U′ falling in the same cell, and bounds the rest by
  Hoeffding (App. D).
- **S versus S′** (Figs. 5, 7, 10–13): barrier curves against width and depth
  for real pairs and for permuted copies of one solution nearly coincide,
  before and after search; the aggregate density over 3,000+ networks lies
  near the diagonal (Fig. 1, right).
- **Search** (§4.2, App. A.3): SA over 5 models (averaging permuted weights
  and scoring training error, "SA2") barely helps. SA over 2 models finds
  zero-barrier permutations for MLPs on MNIST at depth 1 (all widths) and
  depths 2 and 4 at width 2¹⁰ (Fig. 7), and lowers barriers for shallow
  nets on all four datasets at small widths. Barrier keeps falling as SA
  steps grow tenfold (Table 2), with 50K steps taking 10K seconds on one
  V100. A greedy "functional difference" matching from He et al. (2018)
  beats SA (App. B, Fig. 15).
- **Ensembling** (App. C, Table 3): on a 1,024-unit MLP, functional-difference
  alignment plus subspace learning gives 98.22% on MNIST and 58.94% on
  CIFAR-10, against 96.85%/52.95% and 97.63%/57.89% for either alone.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Barriers between independent SGD solutions are mostly due to permutation invariance (Conjecture 1) | weak to moderate: indirect evidence; the search that would show it directly fails for deep nets | §4, Figs. 1, 5, 7 |
| C2 | For wide one-hidden-layer nets at random uniform initialization, a permutation removes the barrier in output | strong (proof), narrow setting | Theorem 3.1, App. D |
| C3 | Barrier first rises then falls with width, peaking where the net first fits the data | moderate: MLP and Shallow CNN; deep families saturate | Fig. 2, Fig. 8 |
| C4 | Depth raises barriers sharply | moderate | Fig. 3 |
| C5 | Independent solutions behave like permutations of one solution in barrier terms | moderate: many networks, but similarity is judged by eye from plots | Figs. 5, 7, 10 |

## Concepts

- **barrier**: as in Assumptions; zero when loss is linear along the path.
- **real world (S)**: solutions from different initializations and seeds.
- **our model (S′)**: random permutations of a single SGD solution, for which
  the conjecture holds by construction.
- **winning permutation**: one that removes the barrier to a reference model.

## Connections

- **Frankle et al. 2020 ([LIT-654](../literature.d/LIT-654.md)).** The LMC definition, amended in its
  baseline, and the reading of a linearly connected region as a basin SGD is
  stable in. Frankle et al.'s copies share an initialization; this paper's
  do not.
- **Garipov et al. ([LIT-673](../literature.d/LIT-673.md)), Draxler et al. ([LIT-653](../literature.d/LIT-653.md)).** The
  non-linear connectivity this paper wants to straighten.
- **Draxler et al.'s redundancy argument** (their §5.2) is the toy version of
  the claim: swapping two units costs a barrier, unless capacity is spared.
- **Brea et al. (2019), Şimşek et al. (2021), Tatro et al. (2020)**, not held:
  permutation saddles, adding a neuron to connect permuted minima, and
  neuron alignment before curve finding.
- **Git Re-Basin ([LIT-661](../literature.d/LIT-661.md))** and **Ferbach et al. ([LIT-680](../literature.d/LIT-680.md))** take
  the conjecture up empirically and theoretically.

## Bearing on the record

- Primary source for the THEORY candidate that barriers between SGD
  solutions are mostly permutation artefacts (proposed in the batch report,
  not filed). Its own evidence supports that candidate only weakly; Git
  Re-Basin is the stronger source.
- **Disagreement with the anthology's reading ([ANTH-LIT-251](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-251.md), [ANTH-NOTE-131](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/notes.d/NOTE-131.md)).**
  That reading states the theorem as conditional on "no dead neurons" and as
  a no-loss-barrier statement for networks in general, lists "no dead
  neurons" and "IID training data" as the paper's assumptions, and reports
  that barriers vanish after alignment on "CIFAR-10, ResNets, VGGs". This
  reading finds none of that in the paper. The theorem is about random
  one-hidden-layer networks at initialization, bounds an output difference,
  and has no dead-neuron condition. Barriers were removed only for some MLPs
  on MNIST, and not reduced at all for VGG or ResNet. Under [ADR-013](../decisions.d/ADR-013.md) this is
  reported, not fixed across the boundary.

## Limitations

- **The theorem does not reach trained networks**, which are the
  conjecture's subject. The authors suggest the NTK regime as a next step.
- **The S–S′ argument is indirect.** Similar barrier statistics are necessary
  for the conjecture but not sufficient: S could resemble S′ in its barriers
  without being permutable into one basin. The authors grant that "even if
  the conjecture is not precisely correct as stated", the model is a useful
  simplification.
- **The conjecture is hard to falsify.** A failed search cannot rule out a
  winning permutation, as both this paper and Git Re-Basin say.
- **Image classification only**; the authors name language tasks as future
  work.
- **A small internal slip**: Appendix A.4 refers to "Table 3" for the SA scaling
  result, which is Table 2.

## Open questions

- Is the conjecture true for deep networks, where barriers saturate and the
  search fails? Git Re-Basin answers yes for wide ResNets on CIFAR-10.
- Does a permutation-free initialization remove the randomness that matters?
  The authors propose it.
- Is there a correspondence between lottery tickets and permutations? Raised
  in §5, not studied.

## Corrections

- none to a seeded skim (there was no seed)
