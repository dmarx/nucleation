---
number: 114
status: Proposed
formerly:
- THEORY-tmpn2rg2
promote_when: >-
  The onset measured outside image classification, and the aligned half
  measured on more than MLPs. Frankle et al.'s onset covers six vision
  networks, and Git Re-Basin's aligned onset covers MLPs on MNIST and
  CIFAR-10 only. What would promote: in a language model or a transformer,
  the barrier tracked against training time, with seeds, both between copies
  spawned from a shared state and between independently initialized runs
  aligned under the architecture's symmetry group, with each high at step 0
  and falling to near zero later. Or the aligned onset reproduced for
  standard-width convnets or ResNets. What would refute it: independently
  initialized networks of practical width that are linearly connected after
  alignment at step 0, under an alignment computed from the initial weights
  alone. Or copies spawned at initialization of a standard deep network that
  end up linearly connected. More vision networks with the same onset curve
  cannot settle it.
title: 'Linear mode connectivity emerges during training, not at initialization: copies trained from a shared state become stable to SGD noise after 1.5–20% of training, and independently trained networks become linearly connected after alignment only gradually'
version: 1
tags:
- loss-landscapes
- anthology-candidate
date: '2026-10-03'
source:
- LIT-654
- LIT-661
- LIT-680
extends:
- THEORY-109
summary: >-
  Frankle et al. (2020), [LIT-654](../literature.d/LIT-654.md): two copies trained from step k under
  different SGD noise are linearly connected only once k is a little way in,
  at 1.5–3% of training for VGG-16 and ResNet-20 on CIFAR-10 and 16–20% for
  Inception-v3 and ResNet-50 on ImageNet. Git Re-Basin (2023),
  [LIT-661](../literature.d/LIT-661.md): between independently trained MLPs, the barrier after
  permutation alignment is high at initialization and falls gradually over
  training. Entezari et al.'s theorem proves alignment-LMC at random
  initialization; Ferbach et al. (2024), [LIT-680](../literature.d/LIT-680.md), show the width that
  needs grows recursively exponentially with depth, far past practical
  widths, which is why the two are consistent.
presupposed_by:
- THEORY-115
---
<!-- inactive-ok-file: LIT-370 — Proposed; named as a re-measurement of the shared-state onset, nothing here rests on it -->
<!-- inactive-ok-file: THEORY-109 THEORY-112 — Proposed; the account this extends, and the symmetry account filed with it, named in the body -->

# THEORY-114: Linear mode connectivity emerges during training, not at initialization: copies trained from a shared state become stable to SGD noise after 1.5–20% of training, and independently trained networks become linearly connected after alignment only gradually

## Source

- Frankle, Dziugaite, Roy & Carbin (2020), [LIT-654](../literature.d/LIT-654.md), read in
  [NOTE-514](../notes.d/NOTE-514.md): §§2–3, Figs. 2–4 and Appendices B–C.
- Ainsworth, Hayase & Srinivasa (2023), Git Re-Basin, [LIT-661](../literature.d/LIT-661.md), read in
  [NOTE-532](../notes.d/NOTE-532.md): §5.2 and Fig. 3.
- Ferbach, Goujaud, Gidel & Dieuleveut (2024), [LIT-680](../literature.d/LIT-680.md), read in
  [NOTE-543](../notes.d/NOTE-543.md): Lemma 5.1, Theorems 5.2–5.3 and the remark that follows
  them in §5.1.

## The claim, in two halves

**From a shared state, after a short time.** Frankle et al., [LIT-654](../literature.d/LIT-654.md),
train two copies of a network from the same state at step k, with
different data order and augmentation. They measure the error barrier on
the straight line between the results: the highest error along it minus
the mean of the endpoints'. Under 2% counts as none. At k = 0 only LeNet on
MNIST is stable. For the other networks, error on the line reaches chance
(Fig. 2). They become stable early: VGG-16 on CIFAR-10 by iteration 1000
(1.5% of training), ResNet-20 by 2000 (3%), Inception-v3 on ImageNet by
epoch 28 (16%) and ResNet-50 by epoch 18 (20%) (Fig. 3). Resetting the
schedule so that the copies train for the full run changes nothing
(Fig. 4). At that point the network is far from done: ResNet-20 is still at
about 25% test error against 8.3% at the end. Once stable at the end, the
copies are linearly connected at every epoch (Appendices B–C). This could
have come out otherwise: the copies end more than half as far apart as the
whole distance ResNet-20 travels in training, and every point between them
is at full accuracy.

Zhou et al. (2025), [LIT-370](../literature.d/LIT-370.md), an earlier reading in this record, found the
same two phases with a small parameter perturbation in place of fresh SGD
noise. VGG-16 and ResNet-20 on CIFAR-10 sent to different basins before an
early inflection point (about 2,500 and 100–500 iterations) and stayed
linearly connected after it. That is one run each with no error bars, and
its reading notes that it largely re-measures Frankle et al.'s result, so it
corroborates this half and is not a source.

**Between independent networks, after alignment, gradually.** Git Re-Basin,
[LIT-661](../literature.d/LIT-661.md), aligns the hidden units of independently initialized networks
by permutation before interpolating. It tracks the barrier after alignment
through training for MLPs on MNIST and on CIFAR-10. It is high at
initialization and falls over training: "LMC manifests gradually throughout
training" (Fig. 3). The authors conclude that linear mode connectivity "is
an emergent property of training, and we were unable to uncover it early in
training" (§5.2). Here there is no onset step as sharp as Frankle et al.'s,
and nothing but alignment links the two endpoints.

**The tension, and its reconciliation.** Entezari et al. ([LIT-652](../literature.d/LIT-652.md),
Theorem 3.1) prove that two wide one-hidden-layer ReLU networks at uniform
random initialization can be permuted so that the network on the line
computes nearly the line between their outputs. That is connectivity at
initialization, the opposite of Git Re-Basin's finding. Ferbach et al.,
[LIT-680](../literature.d/LIT-680.md), resolve it. They generalize the theorem to deep networks with
i.i.d. neuron weights, which holds exactly at initialization (Theorem 5.2).
The width of layer ℓ must then exceed Õ((T_ℓ/ε)^{m̃_{ℓ−1}}), exponential in
the width of the layer before. A matching lower bound shows the rate is
tight (Theorem 5.3). In their words, the condition "appears excessive as
compared to the typical width of neural networks used in practice", and
they cite Git Re-Basin's finding as consistent with it. So both hold:
connectivity at initialization exists in principle, at widths no one
trains. At practical widths it is training that produces it.

## What this does not say

- **The two halves are different measurements.** Frankle et al.'s copies
  share their initialization and their first k steps, and need no alignment.
  Git Re-Basin's networks share nothing and are aligned. That both find
  connectivity appearing in training does not make the onset one event, and
  neither paper measures one against the other.
- **The aligned half rests on MLPs.** Git Re-Basin's onset curve (Fig. 3) is
  for MLPs only. The authors say the CIFAR-10 MLP is under-powered and noisy.
- **It does not say what sets the onset time.** Frankle et al. connect it to
  the noisy early phase without measuring the link.
- **It does not exclude connectivity at initialization under some
  alignment.** Git Re-Basin cites concurrent work (Benzing et al. 2022, not
  held) that finds LMC at initialization using a permutation found at the
  end of training. The claim is that the barrier under alignment computed
  from the weights falls in training, not that no permutation could ever
  join two initializations.
- **Error, not loss.** Frankle et al.'s barriers are on classification
  error, which saturates at chance.
- **Image classification only.** Neither half has been measured on a
  language model or a transformer in the sources.

## Connections

- **[THEORY-109](THEORY-109.md).** This account extends it. That account says the
  solutions training finds are joined by curves, and that it is a property
  of found solutions, not of every minimum. This one says the straight-line
  version is also made by training, and says when: early for a shared stem,
  gradually for aligned strangers.
- **[THEORY-112](THEORY-112.md)** says that once symmetries are removed most of the
  linear barrier between trained solutions disappears. This account is the
  time axis of its trained-solution restriction. No relation is declared:
  the shared-stem half involves no symmetry, and the symmetry account is
  about where training ends.
- The anthology's [ANTH-THEORY-004](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-004.md), that a rewound lottery ticket wins by
  landing back in the basin its dense run found, rests on Frankle et al.'s
  rewinding. This account is the landscape fact under it.
