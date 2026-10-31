---
number: 1272
status: Proposed
formerly:
- THEORY-tmptkuok
promote_when: >-
  A test in which the displacement exponent is predicted rather than
  fitted: d_s measured independently of displacement (from the volume of
  visited states, or from the spectrum of the dynamics' generator), λ
  measured by the LLC estimator, and the late-training exponent of weight
  displacement compared with d_s/(2λ) across architectures and learning
  rates, including rates large enough that Kunin et al.'s regular model
  predicts super-diffusion. What would refute it: displacement exponents
  that track the learning rate and damping as a quadratic model predicts
  and not the LLC, or a fitted d_s that exceeds λ in converged networks.
  More fits of log R on log t with d_s defined by the fit cannot settle it.
title: "Late in training, SGD weights drift sub-diffusively, with displacement growing as a power of training time set by a spectral dimension and the local learning coefficient"
version: 1
tags:
- learning-theory
- loss-landscapes
date: '2026-10-31'
source:
- LIT-1879
summary: >-
  Hennick and De Baerdemacker (2025; ICLR 2026), [LIT-1879](../literature.d/LIT-1879.md), read in
  [NOTE-1467](../notes.d/NOTE-1467.md). Late-training displacement fits R(t) ∝ t^α with α below ½
  on MNIST MLPs, TinyStories models and ImageNet convnets fine-tuned with
  SGD, read through the Alexander–Orbach relation as α = d_s/(2λ) with
  d_s ≤ λ. Proposed: d_s is obtained by fitting that same relation, so the
  fits test the power law and not its link to the LLC; Kunin et al. report
  super-diffusion in another regime.
---
<!-- inactive-ok-file: THEORY-209 QUESTION-039 — Proposed or Open; Kunin's account of the same motion, and the question about timing -->

# THEORY-1272: Late in training, SGD weights drift sub-diffusively, with displacement growing as a power of training time set by a spectral dimension and the local learning coefficient

## Source

Hennick and De Baerdemacker (2025), [LIT-1879](../literature.d/LIT-1879.md), §§3.1–3.3, §4.1
(Table 1, Fig. 2), Appendices B, D.3, H–J of arXiv 2503.22478v2; read in
[NOTE-1467](../notes.d/NOTE-1467.md).

## What was actually shown

**The model.** Late training is diffusion on a porous medium whose mass
dimension near w is the local learning coefficient λ(w). The walk
dimension follows the Alexander–Orbach relation, d_walk = 2λ/d_s
(Theorem 3.1, carried over from Hambly et al.), so displacement grows as
R(t) ∝ t^(d_s/2λ). Lemma 3.4 argues d_walk > 2 and hence d_s ≤ λ, a
sub-diffusive exponent below ½.

**The measurements.** d_s is obtained by regressing log R(t) on log t with
slope d_s/(2λ̂) (Eq. 17). Table 1: TinyStories-1M α = 0.33,
TinyLlama-15M 0.32, TinyStories-33M 0.49 (r² 0.98), ResNet18 and ResNet34
0.004, VGG16 0.001 (r² ≈ 1). I checked α = d_s/(2λ) in every row. On
MNIST every fitted d_s in Tables 7–8 (17 architectures, 50 seeds of one)
lies below λ̂, and two are negative, which the authors attribute to early
super-diffusion.
Early super-diffusion precedes the sub-diffusive regime and grows with
model size on CIFAR-10 (App. I.3).

**What could have failed.** Displacement could have grown as t^½ or
faster late in training. In these runs it grew more slowly.

## What this does not say

- **That the exponent is set by the LLC.** d_s is defined by the fit, so
  α = d_s/(2λ) holds by construction, and d_s ≤ λ is equivalent to α ≤ ½,
  which is sub-diffusion itself. The link to λ is tested only through
  correlations (Fig. 2b, Fig. 17), which are confounded by batch size, as
  the paper notes for the LLC estimator (App. H).
- **That it holds at ordinary learning rates.** The language models ran
  at 10⁻⁵, the vision models' SGD phase at 10⁻⁵ after Adam, MNIST at 10⁻³.
  Kunin et al. ([THEORY-209](THEORY-209.md)) find super-diffusive drift in resumed ImageNet
  training at the original schedule, explained by damping in a quadratic
  model.
- **That the vision fits mean much.** With α ≈ 0.001–0.004 the
  displacement is nearly constant, and r² ≈ 1 says little about the form.
- **Anything about the order of transitions.** Jumps in weights and LLC
  during grokking need a space-fractional term the paper does not develop
  (App. F), so stagewise development is outside this account.
