---
number: 85
status: Proposed
formerly:
- THEORY-tmpn24vc
promote_when: >-
  Two measurements that LIT-613 did not make. The first measures
  the per-layer class means of gradients directly against the Kronecker
  products of feature and error class means, g_c against h_c ⊗ δ_c, with
  a stated tolerance; the paper infers this from CFAC's alignment and does
  not measure it. The second gives a quantitative alignment, such as
  principal angles, between the top eigenspaces of the true layer Fisher
  and those of K-FAC and CFAC. Both should be made on convolutional and
  attention layers as well as MLPs. The account is refuted if K-FAC's
  outlier subspace aligns with the true Fisher's at layers where the
  per-class factor statistics differ strongly. It is also refuted if CFAC
  is no better aligned than K-FAC on architectures beyond the one MLP
  tested. Optimizer benchmarks cannot settle it. K-FAC's damping and
  re-scaling can make it a good optimizer with misplaced outliers, and a
  better approximation need not train faster.
title: "A classifier's class-driven Fisher outliers pair each class's feature mean with that class's own error mean, so K-FAC's single Kronecker product of class-averaged factors adds every cross-class pairing and misplaces them, and differs from the class-wise product by the between-class covariance of its two factors"
version: 1
tags:
- information-geometry
- learning-theory
- anthology-candidate
date: '2026-10-03'
source:
- LIT-613
- LIT-622
extends:
- THEORY-078
summary: >-
  Papyan (2020), [LIT-613](../literature.d/LIT-613.md): per layer, the Fisher is a weighted sum of
  Kronecker products of features and backpropagated errors (Eq. 7.5), and
  its class outliers come from class means of gradients that are
  approximately h_c ⊗ δ_c. K-FAC (Martens & Grosse 2015, [LIT-622](../literature.d/LIT-622.md))
  multiplies the class-averaged feature covariance by the class-averaged
  error covariance. Papyan finds its outliers and mini-bulks "drastically
  misaligned", and the class-wise CFAC aligns much better at deep layers.
  The filer adds a line of algebra: CFAC − K-FAC = Ave_c (H_c − H̄) ⊗
  (Δ_c − Δ̄), so the two coincide when one factor's per-class
  statistics do not vary with class. The evidence is one MLP, spectra
  only, judged by eye.
---
<!-- inactive-ok-file: THEORY-078 — Proposed; this account extends it per layer and is no firmer than it -->

# THEORY-085: A classifier's class-driven Fisher outliers pair each class's feature mean with that class's own error mean, so K-FAC's single Kronecker product of class-averaged factors adds every cross-class pairing and misplaces them, and differs from the class-wise product by the between-class covariance of its two factors

## Source

- Papyan (2020, JMLR), [LIT-613](../literature.d/LIT-613.md), read in [NOTE-474](../notes.d/NOTE-474.md): Eqs. 7.3–7.8,
  §§7.10–7.12, Definitions 7.1–7.2, Figures 11–12.
- Martens & Grosse (2015), [LIT-622](../literature.d/LIT-622.md), read in [NOTE-486](../notes.d/NOTE-486.md): Eqs. 1–3,
  Figures 2–3, §13.

## What was actually shown

**The layer Fisher is a sum of Kronecker products.** A layer's gradient
for example i of class c, evaluated as if its label were c′, is
h^{l−1}_{i,c} ⊗ δ^l_{i,c,c′}: the layer's input features times the
backpropagated error ([LIT-613](../literature.d/LIT-613.md), Eq. 7.4). So the layer block of the
Fisher is G^l = Σ w·(hhᵀ) ⊗ (δδᵀ), a weighted sum over examples, classes
and would-be classes (Eq. 7.5). That is exact. Martens & Grosse start from
the same fact, vec(DW_i) = ā_{i−1} ⊗ g_i ([LIT-622](../literature.d/LIT-622.md), Eq. 1).

**K-FAC's assumption.** K-FAC replaces E[āāᵀ ⊗ ggᵀ] by E[āāᵀ] ⊗ E[ggᵀ],
which treats activities and derivatives as independent. Its error is a sum
of third- and fourth-order cumulants ([LIT-622](../literature.d/LIT-622.md), Eq. 3), and the
authors concede it "likely won't become exact under any realistic set of
assumptions". They checked it on one partially trained tanh network on
16 × 16 MNIST, and their optimisation experiments are autoencoders, which
have no classes.

**Papyan's measurement.** Papyan computes K-FAC's layer matrix
G^l_KFAC = H^l ⊗ Δ^l (Definition 7.1), the product of the feature and
error second moments each averaged over all examples. He compares its
spectrum with the true G^l and with a class-wise alternative,
G^l_CFAC = Ave_c H^l_c ⊗ Δ^l_c (Definition 7.2), on an eight-layer MLP
trained on MNIST, Fashion-MNIST and CIFAR-10. In his words: "G_KFAC has
its mini-bulks and outliers drastically misaligned from those of G"
(§7.10). CFAC's spectrum aligns "much better" at deeper layers. At CIFAR-10
layers 7–8 it aligns "almost perfectly". At shallow layers the gain depends
on the dataset, and at CIFAR-10 layer 2 there is none (Figures 11–12).
His account: "In KFAC … the feature mean of one class would be multiplied
by the error mean of another class. In CFAC, on the other hand, the
feature mean of a class would only be multiplied by the error mean of that
class" (§7.12). From this he infers that the gradient class means, which
cause the outliers, are approximately g_c ≈ h_c ⊗ δ_c.

**The algebra behind it.** This step is the filer's. Write H_c and Δ_c
for the per-class second moments, and H̄ and Δ̄ for their averages. Then
K-FAC is H̄ ⊗ Δ̄ = Ave_{c,c′} H_c ⊗ Δ_{c′}, which has all C² pairings, and
CFAC is Ave_c H_c ⊗ Δ_c, which has C. Their difference is

CFAC − K-FAC = Ave_c (H_c − H̄) ⊗ (Δ_c − Δ̄),

the between-class covariance of the two factors in the Kronecker sense.
K-FAC equals CFAC when either factor's per-class second moment does not
vary with class, and otherwise they generally differ. CFAC is K-FAC's
independence assumption made conditional on the class. The class label is a shared cause of features
and errors, so it makes them dependent, and that dependence is the
cumulant K-FAC drops. The trained classifiers of [THEORY-078](THEORY-078.md) are the
case where the per-class means are large and far apart, so the difference
is large.

## What this does not say

- **It does not say K-FAC is a poor optimizer.** No optimizer is run with
  CFAC, and the comparison is of spectra only ([LIT-613](../literature.d/LIT-613.md), §7.10). K-FAC's
  results come from damping and from re-scaling under the exact Fisher as
  much as from its factorisation ([LIT-622](../literature.d/LIT-622.md), §6, Figure 7). Papyan
  cites the large-batch inefficiency of K-FAC and says his paper "does not
  shed light on this phenomenon".
- **The measured part is narrow.** One MLP architecture, three datasets,
  alignment judged by eye. That g_c ≈ h_c ⊗ δ_c is inferred from CFAC's
  better alignment and not measured directly ([NOTE-474](../notes.d/NOTE-474.md), C3).
- **It says nothing about Shampoo.** Shampoo's factors ([LIT-621](../literature.d/LIT-621.md)) are
  accumulated gradient outer products at the training labels. That is a
  different matrix from the model Fisher, and Shampoo needs no statistical
  model to justify its Kronecker shape ([NOTE-480](../notes.d/NOTE-480.md)). Whether class
  structure misplaces its directions is not established by any held
  paper.
- **It does not contradict Martens & Grosse.** Their check was on a
  network without classes, where this source of dependence is absent, and
  they expected the factorisation to be inexact anyway.

## Connections

- **Extends [THEORY-078](THEORY-078.md).** That account locates the Fisher's outliers
  in the class means. This one follows the class means into each layer's
  Kronecker factors and says what a class-blind factorisation does to them.
