---
status: Read
paper: LIT-tmpl3anv
title: 'Bridging Mode Connectivity in Loss Landscapes and Adversarial Robustness'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read from arXiv v2 (28 pages). Sections 1–4 read in full; Appendix J
    and Appendix L (proof of Proposition 1) read in full; the remaining
    appendices skimmed for setup and extra results. Plotted values were
    read from captions and text, not digitised.
date: '2026-10-03'
summary: >-
  Bezier path (Garipov) trained on 50–2,500 clean samples between two
  backdoored or error-injected models: models near the ends keep most clean
  accuracy and lose the attack (CIFAR-10 VGG, 2,500 samples, t = 0.1: 88%
  clean, 1.1% backdoor; injection 0% throughout). Standard-loss paths
  between regular and adversarially trained models are flat in standard
  loss but have a PGD robustness-loss barrier, correlated with λ_max of the
  input Hessian (PCC 0.71–0.88). Proposition 1's proof assumes the loss is
  constant along the path in a way that, if true for all inputs, would
  remove the barrier.
---

# NOTE-tmpjlvth: Bridging Mode Connectivity in Loss Landscapes and Adversarial Robustness

## Contribution

It is the first paper to turn mode connectivity on adversarial
robustness. It uses connecting paths as a repair tool for tampered models,
and as a probe of how robustness varies across a region where ordinary
loss does not.

## Key insight

A connecting path is trained only on clean data, so it is only asked to
keep clean behaviour. Nothing asks it to keep a hidden trigger response,
and in the middle of the path that response is not kept. So walking a short
way along a clean-trained path from a backdoored model keeps what the clean
data asked for and drops what it did not. The same logic explains the
evasion results. A path flat in clean loss says nothing about loss under
attack, and robustness rises and falls along it with the input-space
curvature.

## Assumptions

- **Path**: quadratic Bezier φ_θ(t) = (1 − t)²w₁ + 2t(1 − t)θ + t²w₂, trained
  by minimising E_{t∼U(0,1)} l(φ_θ(t)) with cross-entropy (Eqs. 2, 4).
- **Threat model (backdoor, error injection)**: the user holds two (or one,
  plus a fine-tuned copy) possibly tampered models and a small bonafide set
  the attacker cannot touch. The bonafide data are drawn from the test
  split, and evaluation uses 5,000 other test samples (§3.1).
- **Attacks**: BadNets-style triggers on 10% of training data (single-target
  T = 1; all-targets T = i + 1 mod 9); fault-sneaking error injection;
  PGD ℓ∞, ε = 8/255, 10 steps, for evasion.
- **Proposition 1**: (a) l(w(t), x) constant in t; (b) second-order Taylor
  model in the input; c = |∇ₓlᵀv|/‖∇ₓl‖ → 1, where v is the top eigenvector
  of the input Hessian.
- **Architectures**: VGG-16 on CIFAR-10 and ResNet on SVHN.

## Key results

- **Untampered paths (Fig. 1)**: with 1,000 or 2,500 CIFAR-10 samples the
  path loses at most 10% or 5% test accuracy against the endpoints; the
  worst model is near t = 0.5.
- **Table 1**: backdoored endpoints have 5.4–19% clean error and 0.07–2%
  attack failure for single-target backdoors.
- **Table 2 (single-target backdoor; clean / backdoor accuracy)**: CIFAR-10
  VGG at t = 0.1: 88/1.1% (2,500 samples) down to 63/2.5% (50); fine-tune
  84/1.5% to 46/2.8%; prune 88/43% to 81/82%. SVHN ResNet at t = 0.2:
  96/2.5% to 82/16%; fine-tune 96/14% to 76/60%.
- **Table 3 (error injection)**: path connection 88–92% clean on CIFAR-10
  and 90–96% on SVHN, 0% injection success at every size; fine-tuning 82–94%
  clean and up to 25% injection success; pruning up to 25%.
- **Fig. 4 (evasion)**: no standard-loss barrier on any path; a
  robustness-loss barrier on all three kinds, most marked for
  regular–robust and robust–robust pairs; PCC with λ_max of 0.71, 0.88, 0.86.
- **Appendix J**: against a path-aware backdoor, the repaired region shrinks
  to about t ∈ [0.25, 0.75] but remains.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Paths trained on small clean sets between tampered models contain repaired models | moderate to strong: two architectures, two datasets, two attack types, several data sizes, an adaptive attack | Tables 2–3, Figs. 2–3, App. J |
| C2 | Path connection beats fine-tuning, retraining, pruning and noise on clean–attack trade-off | moderate: holds against each baseline on attack success or clean accuracy, but pruning has higher clean accuracy on CIFAR-10 VGG at every size | Tables 2–3 |
| C3 | Between regular and adversarially trained models there is a robustness-loss barrier on a standard-loss path | moderate: one architecture and dataset in the main text | Fig. 4 |
| C4 | Robustness loss on the path is governed by λ_max of the input Hessian | weak as theory (see Corrections); moderate as an empirical correlation | Prop. 1, Fig. 4 |

## Concepts

- **bonafide data**: clean labelled data the user trusts.
- **robustness loss**: cross-entropy on PGD adversarial examples with their
  true labels.
- **input Hessian**: the Hessian of the loss with respect to the input x,
  not the weights.
- **path connection (defence)**: training a Bezier path between suspect
  models on bonafide data and deploying a model near an end of it.

## Connections

- **Garipov et al. ([LIT-tmpotq71](../literature.d/LIT-tmpotq71.md))**: the path family and training objective
  are theirs; this paper changes the endpoints and the data.
- **Draxler et al. ([LIT-tmp3kyq9](../literature.d/LIT-tmp3kyq9.md))**: cited with Garipov for flat paths
  between minima.
- **Lubana et al. ([LIT-tmpl64hd](../literature.d/LIT-tmpl64hd.md))**: a mechanistic reading of the same
  effect. A model that leaves its basin along a path fitted to clean data
  can lose a behaviour the clean data did not ask for, while a model that
  stays linearly connected keeps it.

## Bearing on the record

- An instruction for practice, which is to repair a suspect pretrained
  model by connecting it to a fine-tuned copy and deploying a model near the
  end, belongs in the anthology. It sits beside robustness and security
  questions the anthology may hold better than this record does.
- **Vocabulary gap**: no topic covers adversarial robustness, backdoors or
  model tampering.

## Limitations

- **Small, old architectures** (VGG-16, ResNet on CIFAR-10 and SVHN) and
  BadNets-style triggers only.
- **Evaluation on the test split** for both path training and evaluation,
  with disjoint samples.
- **Repair depends on two endpoints that are both tampered the same way**, or
  on fine-tuning a copy; the single-model extension is in Appendix G.
- **Ensembling along a path gives little robustness gain** against evasion,
  as the authors report (Appendix M), because adversarial examples transfer
  between similar models.

## Open questions

- Why does the trigger response vanish mid-path? The input-gradient
  similarity analysis (Appendix I) describes it but does not explain it.
- Does path repair work against triggers designed to survive interpolation
  for large models?

## Corrections

- none to a seeded skim (there was no seed)
- **Proposition 1's proof (Appendix L).** Lemma 1 differentiates
  "l(w + Δw, x) = l(w, x)" with respect to x to conclude that input-gradient
  norms are equal along the path. That needs the loss constant along the
  path for all x near each data point, not only at the data. But if
  l(w(t), ·) were the same function for all t, the robustness loss, which
  is a function of l(w(t), ·) alone, would also be constant, and there
  would be no barrier to explain. The proposition is a heuristic for the
  correlation, not a derivation of it.
- **ℓ∞ vs ℓ₂.** The proof uses δ* = ε∇f/‖∇f‖, the first-order optimum for
  an ℓ₂ ball, while the attacks are ℓ∞ PGD, whose first-order optimum is
  ε·sign(∇f).
- **"Consistently maintains superior accuracy on clean data"** (§3.2) is not
  what Table 2 shows for CIFAR-10 VGG, where pruning has higher clean
  accuracy at every data size, at the cost of 43–82% backdoor success.
- **All-targets labels.** T = i + 1 (mod 9) for ten classes looks like a
  typo for mod 10. As written, class 9 maps to class 1, the same target as
  class 0.
