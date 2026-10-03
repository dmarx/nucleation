---
number: 538
status: Read
formerly:
- NOTE-tmprwelh
paper: LIT-669
title: 'Mechanistic Mode Connectivity'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read from arXiv v3 (40 pages) through the PDF text layer. Sections 1–8
    and Appendices C–F read in full, including the proofs; Appendices A,
    B, G and H skimmed. Figures were read from captions and text. Table 1
    and Table 4 numbers come from the text layer; Table 3 (the CBFT
    ablation) is described in prose only. Results taken from Simsek et al.
    (2021) and Shah et al. (2020) are taken as the paper states them.
date: '2026-10-03'
summary: >-
  Mechanistic similarity = invariance to the same unit interventions on the
  latents of the data-generating process. Cue-reliant and cue-invariant
  ResNet-18 and VGG-13 models are quadratic- but not linear-connected, even
  after activation matching. Conjecture 1 (no LMC up to symmetry ⇒
  mechanistic dissimilarity) is not what Appendix F.3 proves. For a
  one-hidden-layer ReLU net with interpolating minimizers, Lemma 2 (LMC
  forces identical activation patterns) with Theorem 1 (mechanisms of
  different complexity force different patterns) proves the converse:
  dissimilar mechanisms of different complexity ⇒ no LMC under any
  permutation. The paper presents this as verifying the conjecture. CBFT (cross-entropy + barrier loss + class-mean invariance
  loss) removes the cue on synthetic CIFAR-10/100 and Dominoes.
---


# NOTE-538: Mechanistic Mode Connectivity

## Contribution

Before this paper, mode connectivity was measured only on the loss of the
data the models were trained on. It adds a second axis, what each model
relies on, measured by its response to counterfactual data, and shows that
the two axes come apart: two models can be joined by a low-loss curve on the
training data while every point on that curve responds differently to
counterfactuals. It ties the absence of a straight low-loss path to a
difference in mechanism, proves that link in one small case, and uses it to
build a fine-tuning method.

## Key insight

A linear path between two models is a strong constraint: in a ReLU network
that interpolates its data, staying at zero loss along a line forces both
endpoints to switch the same units on and off for every input. Two models
that rely on different input attributes cannot do that, so the line between
them must climb. A curve can still go round, because a curve fitted to the
training data only has to agree on that data. Read the other way round, a
fine-tuned model that stays linearly connected to its parent is still using
its parent's mechanism.

## Assumptions

- **Data-generating process.** Latents z are drawn from a factorized
  distribution P(z) = Πᵢ P(zᵢ) and mapped to inputs by an invertible
  generator G_X (§3). Unit interventions set one latent to a fixed value;
  counterfactuals map the intervened latent back to input space
  (Definition 2).
- **Invariance (Definition 3).** f(·; θ) is invariant to intervention Aᵢ if
  the expected loss on counterfactuals equals the loss on D.
- **Proposition 2 (mode connectivity of dissimilar minimizers)** rests on
  Simsek et al. (2021)'s Lemma 1: an activation φ with φ(0) ≠ 0 and
  infinitely many non-zero odd and even derivatives, at least one neuron per
  layer beyond the minimum needed for zero loss, and cross-entropy or
  mean-squared loss. ReLU does not satisfy the analyticity condition; the
  paper points to a smooth surrogate.
- **Conjecture 1 proof (Appendix F.3).** One hidden layer, f(x; W) =
  (1/N) 1ᵀ ReLU(Wᵀx), binary labels, every minimizer global and
  interpolating, and a data process of n attributes with spline complexity
  K plus noise dimensions. Lemma 3 (simplicity bias, that gradient descent
  uses only the simplest predictive attribute) is restated from earlier work,
  not proved.
- **Experiments.** Synthetic cues: 3×3 boxes placed by label on CIFAR-10,
  coloured and placed by label digits on CIFAR-100, and Fashion-MNIST halves
  on Dominoes. The cue is easier to learn than the natural attribute, so
  simplicity bias makes the cue-trained model rely on it.

## Key results

- **Fig. 4 (ResNet-18, synthetic CIFAR-10).** θ_C (trained with cue) and
  θ_NC (trained without) are connected by quadratic paths on the data used to
  fit them. Linear paths, with and without permutation, show barriers, and no
  path keeps accuracy on all counterfactual datasets: mechanistic
  connectivity (Definition 5) fails.
- **Fig. 5 (VGG-13, ResNet-18; fine-tuning on cue-free data for 100
  epochs).** With small (0.001) or medium (0.01) initial learning rate, θ_FT
  stays linearly connected to θ_C on cue data and behaves like θ_C on
  counterfactuals. With a large rate (0.1), or a cue perfectly correlated
  with the label, there is a barrier and θ_FT becomes invariant to the cue.
- **Lemma 2 (Appendix F.3).** If interpolating minimizers W_α, W_β are
  linearly mode connected on D, then ϕ′(W_αᵀx) = ϕ′(W_βᵀx) for all x ∈ D:
  they share activation patterns. With Lemma 3, two models that rely on
  attributes of different complexity cannot share activation patterns, so
  they cannot be linearly connected.
- **Table 1 (CBFT, 2,500 clean samples, mean of three seeds).** CIFAR-10 at
  60% cue data: CBFT NC 74.1, C 71.5, RC 73.4, RI 8.75; medium-LR fine-tuning
  75.7, 98.4, 23.6, 83.4. CIFAR-100 at 90% cue data is the weakest case:
  CBFT's RI accuracy is 46.0, above small-LR fine-tuning (30.9) and LPFT
  (19.6), so there it is not the most cue-free method on that column. Training from scratch
  on the 2,500 clean samples reaches only 47.5% on CIFAR-10 (Table 4).
- **CBFT ablation (Appendix E).** Without the barrier loss the model keeps
  the cue. Without the invariance loss it can become anti-correlated with
  the cue, which still produces a barrier.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Mechanistically dissimilar minimizers can be mode connected | strong as a corollary, for analytic activations and one extra neuron per layer | Proposition 2, via Simsek et al. Lemma 1 |
| C2 | Cue-reliant and cue-invariant models are quadratic- but not linear-connected, even after permutation | moderate: two architectures, three synthetic datasets | Fig. 4, App. G |
| C3 | Lack of LMC (up to symmetry) implies mechanistic dissimilarity | conjectured; App. F.3 proves only the converse (dissimilar mechanisms of different complexity ⇒ no LMC) for a one-hidden-layer ReLU net with interpolating minimizers; the stated direction rests on the fine-tuning experiments | Conjecture 1, Lemma 2, App. F.3 |
| C4 | Naive fine-tuning on clean data that stays LMC with the pretrained model keeps its mechanism | moderate: synthetic cues, one fine-tuning protocol | Fig. 5, App. H |
| C5 | Forcing a barrier and penalising representation shift removes a spurious cue more effectively than LLR or LPFT | moderate on synthetic benchmarks; weaker on CIFAR-100 at high cue proportion | Table 1, App. E |

## Method

CBFT minimises L_CE(f(D_NC; θ), y) + L_B + (1/K) L_I. The barrier loss
L_B = E_t |λ_B − L_CE(f(D_C; γ_{θ→θ_C}(t)), y)| samples t from a truncated
Gaussian on [0, 1] with mean 0.5 and raises the loss on the linear path to
the pretrained model θ_C up to λ_B = 1. The invariance loss L_I is the
squared distance between class-mean penultimate representations on cue and
cue-free data. Only a small cue-free dataset D_NC is assumed; paired images
with and without the cue are not.

## Concepts

- **unit intervention**: setting one latent of the data-generating process
  to a chosen value.
- **mechanistic similarity**: invariance to the same set of unit
  interventions.
- **mechanistic connectivity**: mode connectivity along a path that holds on
  every counterfactual dataset, so every point on the path is mechanistically
  similar.
- **cue**: a synthetic attribute whose latent is conditioned on the label,
  standing in for a spurious attribute.

## Connections

- **Garipov et al. ([LIT-673](../literature.d/LIT-673.md)).** The quadratic paths here are their
  Bezier curves, trained by sampling points along the curve (Appendix C.1).
  This paper's point is that such a curve is a function of the data used to
  fit it.
- **Frankle et al. ([LIT-654](../literature.d/LIT-654.md)).** The linear test and the choice to plot
  accuracy along paths follow them.
- **Git Re-Basin ([LIT-661](../literature.d/LIT-661.md)) and Entezari et al. ([LIT-652](../literature.d/LIT-652.md)).** Linear
  paths are evaluated after Git Re-Basin's activation matching. Remark 1
  reads Lemma 2 as the condition under which the permutation conjecture
  holds. Shared activation patterns up to permutation imply linear
  connectivity after unpermuting.
- **Zhou et al. ([LIT-674](../literature.d/LIT-674.md))** cite this paper and push in the same
  direction from the other side: when two models are linearly connected,
  their features are linearly connected layer by layer.
- **Bo Zhao et al. ([LIT-655](../literature.d/LIT-655.md))** cite it as evidence that a missing linear
  path marks a difference in what the models rely on.

## Bearing on the record

- Bears on the anthology's [ANTH-THEORY-010](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-010.md), which is Proposed and asks for
  the residual barrier after alignment to be shown to be noise, not
  disagreement. This paper supplies controlled cases where a barrier
  survives permutation and is disagreement. They are not two seeds on one
  dataset, so this is a boundary on that theory, not a refutation of it.
- A THEORY candidate here: *a linear barrier between two minimizers, after
  symmetries are removed, marks a difference in the input attributes they
  rely on*. Its evidence would be this paper plus Zhou et al.'s layerwise
  linearity.
- It carries an instruction for practice. Do not trust naive fine-tuning on
  clean data to remove a spurious mechanism; check linear connectivity to
  the parent. That belongs in the anthology, so the LIT is flagged.

## Limitations

- **The proof covers one hidden layer.** It assumes interpolating global
  minimizers and leans on an unproved simplicity-bias lemma.
- **Asymmetric scope.** The authors note (Table 2's asterisk, §8) that
  mechanistically dissimilar models *can* be linearly connected when their
  mechanisms are of similar complexity. So what is proved is narrow:
  dissimilar mechanisms of *different complexity* ⇒ no LMC. Dissimilarity
  in general does not imply a barrier, and the conjectured direction
  (no LMC ⇒ dissimilar) is supported by experiment, not proof.
- **Synthetic mechanisms.** The cues are easy, artificial and placed by
  design. Natural spurious features are not tested; the authors point to
  generative counterfactuals as future work.
- **Different datasets.** The endpoints in Fig. 4 are trained on different
  data, cue and no cue, so they are not the independent seeds on one
  dataset that the permutation conjecture is about.

## Open questions

- Does the implication hold for deep networks without interpolation, and for
  natural shortcut features?
- How should "similar complexity" be measured so that the converse
  (dissimilar ⇒ no LMC) can be stated where it holds?

## Corrections

- none to a seeded skim (there was no seed)
- **Typo in Definition 1.** The barrier condition reads L(γ(t)) ≤ t·L(θ₀) +
  (1 − t)·L(θ₁), but the endpoints are θ₁ and θ₂ (γ(0) = θ₁, γ(1) = θ₂).
  θ₀ should be θ₂. With that change it is the usual statement that the loss
  on the path stays below the linear interpolation of the endpoint losses.
