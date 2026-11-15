---
number: 425
status: Active
formerly:
- THEORY-tmp369dq
title: "A connecting path trained only on clean data keeps only the behaviour the clean data ask for: between two backdoored or error-injected image classifiers, models near the ends of such a path keep most clean accuracy and lose the attack, and a path flat in ordinary loss can carry a barrier in adversarial loss that tracks the input Hessian's top eigenvalue"
version: 2
history:
- version: 2
  date: '2026-11-14'
  note: >-
    Bears on QUESTION-069, from the reading review of 2026-11-14 (by
    topic, part B). The question asks "Is the connectedness of trained
    solutions a property of the solutions, or of the path family
    searched", says each result "was measured with a particular
    instrument", and asks "what does a residual barrier between two
    trained networks tell us about the networks themselves?" Here a
    path fitted to clean data and flat in clean loss carries a barrier
    in adversarial loss and sheds the endpoints' backdoor, so
    connectedness is relative also to the loss and data the path is
    fitted and measured on. No other change.
tags:
- loss-landscapes
- anthology-candidate
date: '2026-10-16'
source:
- LIT-668
summary: >-
  Zhao, Chen, Das, Ramamurthy & Lin (2020), [LIT-668](../literature.d/LIT-668.md), read in [NOTE-530](../notes.d/NOTE-530.md). A
  quadratic Bezier path trained on 50–2,500 clean samples between two
  backdoored VGG-16s on CIFAR-10 has, at t = 0.1, 88% clean accuracy and
  1.1% backdoor success with 2,500 samples, and 63% and 2.5% with 50;
  injected weight errors fail at every point of such paths. Paths trained
  with the standard loss between regular and adversarially trained models
  are flat in standard loss with a PGD-loss barrier correlated with the
  input Hessian's top eigenvalue (0.71–0.88). The proposition offered for
  that correlation rests on an assumption that would remove the barrier.
bears_on:
- QUESTION-069
---
<!-- inactive-ok-file: THEORY-109 THEORY-116 — Proposed; the connectivity account whose path family this uses, and the mechanism account it anticipates, named, not leaned on -->

# THEORY-425: A connecting path trained only on clean data keeps only the behaviour the clean data ask for: between two backdoored or error-injected image classifiers, models near the ends of such a path keep most clean accuracy and lose the attack, and a path flat in ordinary loss can carry a barrier in adversarial loss that tracks the input Hessian's top eigenvalue

## Source

Zhao, Chen, Das, Ramamurthy & Lin (2020), [LIT-668](../literature.d/LIT-668.md) (ICLR 2020), read in
[NOTE-530](../notes.d/NOTE-530.md).

## What was actually shown

**The path.** A quadratic Bezier curve
φ_θ(t) = (1 − t)²w₁ + 2t(1 − t)θ + t²w₂ is trained by minimising the
cross-entropy averaged over t uniform on [0, 1] (Garipov et al.'s
objective), on a small clean set the attacker cannot touch.

**Backdoors (Table 2).** Two models backdoored with the same poisoned data
(BadNets-style triggers on 10% of training data). On CIFAR-10 VGG-16 the
model at t = 0.1 has 88% clean accuracy and 1.1% backdoor success with
2,500 clean samples, falling to 63% and 2.5% with 50; fine-tuning with 50
samples gives 46% clean accuracy. On SVHN ResNet at t = 0.2, 96% and 2.5%
with the most data, 82% and 16% with the least.

**Injected errors (Table 3).** On paths between two fault-sneaking-attacked
models, injection success is 0% at every data size, with clean accuracy
88–96%.

**An adaptive attacker (Appendix J).** Against a backdoor designed with the
path in view, the repaired region shrinks to about t ∈ [0.25, 0.75] but
remains.

**Robustness along a path (Fig. 4).** On paths trained with the standard
loss between two regular models, a regular and an adversarially trained
model, or two adversarially trained ones, standard loss is flat and PGD
robustness loss rises mid-path. Its shape correlates with the largest
eigenvalue of the input Hessian, Pearson 0.71, 0.88 and 0.86.

**What could have come out otherwise.** The trigger response could have
been carried along the path with the clean behaviour. It was not, at the
data sizes and attacks tested.

## What this does not say

- **Why the trigger response vanishes.** The input-gradient similarity
  analysis (Appendix I) describes it and does not explain it.
- **That λ_max governs robustness loss.** As a correlation, yes. Proposition
  1's proof differentiates "l(w + Δw, x) = l(w, x)" in x, which needs the
  loss constant along the path for all inputs near the data; if that held,
  the robustness loss would be constant too and there would be no barrier
  to explain. It also uses the ℓ₂ first-order attack against ℓ∞ PGD
  ([NOTE-530](../notes.d/NOTE-530.md), Corrections).
- **That it holds for large models or stronger triggers.** VGG-16 and
  ResNet on CIFAR-10 and SVHN, BadNets-style triggers.
- **That path connection beats every baseline.** Pruning has higher clean
  accuracy on CIFAR-10 VGG at every data size, at the cost of 43–82%
  backdoor success.
- **What to do with a suspect model.** Repair by path connection is an
  instruction for practice, which belongs in the anthology.

## Connections

- **[THEORY-116](THEORY-116.md)** (Lubana et al., [LIT-669](../literature.d/LIT-669.md)) holds that a barrier surviving
  symmetry removal marks a difference in the input attributes two models
  rely on. This paper's repair anticipates it from the other side:
  leaving a basin along a path fitted to clean data sheds a mechanism the
  clean data did not ask for.
- **[THEORY-109](THEORY-109.md).** The path family and objective are Garipov et al.'s
  ([LIT-673](../literature.d/LIT-673.md)); here the endpoints are tampered.
- **The record has no topic word** for adversarial robustness or model
  tampering ([NOTE-530](../notes.d/NOTE-530.md)); `loss-landscapes` is the subject here.
