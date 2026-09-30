---
status: Proposed
promote_when: >-
  A test in which B_simple (or B_noise), measured on one tuned run, predicts
  a critical batch that is then measured independently, on tasks and at
  scales outside the original eight. It should include the generative
  models where the 2018 fit missed by about 20×, and either close the gap
  or explain it. More fits of eq. (2.11) do not settle it, because the form
  fits by construction and B_crit is a fitted parameter. A derivation that
  does without the local quadratic model and the optimal-step assumption
  would also move it. Systematic failure of the noise scale to track B_crit
  once the learning-rate temperature is controlled would refute it, as
  would a per-step progress law that keeps growing with B past the knee,
  such as log(1 + SNR).
title: 'The critical batch size is set by the gradient''s noise-to-signal ratio, because per-step progress saturates as 1/(1 + B_noise/B); the measured noise scale predicts it only to within an order of magnitude'
version: 1
tags:
- learning-theory
date: '2026-09-30'
source:
- LIT-348
- LIT-324
summary: >-
  McCandlish, Kaplan, Amodei et al. (2018), [LIT-348](../literature.d/LIT-348.md): under a local quadratic
  model with an optimal step, per-step progress is ΔL_max/(1 + B_noise/B).
  This gives the steps–examples hyperbola and B_crit = E_min/S_min. The
  Hessian-free B_simple = tr(Σ)/|G|² is the batch at which gradient noise
  equals signal, and it tracks B_crit within about 10× on most of eight
  tasks, missing by about 20× on two generative models. The authors call
  the derivation one with "unfounded assumptions". Nothing in it is
  information-theoretic, and its temperature ε/B is not k_BT.
---

# THEORY-tmp9b0vu: The critical batch size is set by the gradient's noise-to-signal ratio, because per-step progress saturates as 1/(1 + B_noise/B); the measured noise scale predicts it only to within an order of magnitude

## Source

- McCandlish, Kaplan, Amodei & the OpenAI Dota Team (2018), [LIT-348](../literature.d/LIT-348.md), §§2–3, Table 1 and Apps. A, C and D, as read in [NOTE-293](../notes.d/NOTE-293.md).
- Shwartz-Ziv & Tishby (2017), [LIT-324](../literature.d/LIT-324.md), §3.5, the drift/diffusion SNR phases [LIT-348](../literature.d/LIT-348.md) cites, as read in [NOTE-298](../notes.d/NOTE-298.md).

## What was actually shown

**The mechanism (derivation).** A minibatch gradient is unbiased for G, with covariance Σ/B. Put it into a second-order step L(θ − εV) and choose the optimal ε. The expected improvement is then ΔL_max/(1 + B_noise/B), with B_noise = tr(HΣ)/GᵀHG (eqs. 2.4–2.8). Below B_noise, examples in a batch substitute almost one-for-one for steps. Above it they are mostly wasted, and at B = B_noise speed is half the maximum. Summed over a run at fixed B, this gives (S/S_min − 1)(E/E_min − 1) = 1, whose corner defines B_crit = E_min/S_min (eqs. 2.11–2.12). [NOTE-293](../notes.d/NOTE-293.md) re-derived the hyperbola, and it holds even when the noise scale varies over the run.

**The noise-to-signal reading is the paper's own.** For B_simple = tr(Σ)/|G|², E|G_est − G|²/|G|² = B_simple/B (eq. 2.10). So B_simple is the batch at which the batch gradient's noise equals its signal. The paper calls it "essentially a measure of the signal-to-noise ratio".

**The evidence (measurement).** Across eight tasks B_crit spans about six orders of magnitude (Table 1). The run-averaged B_simple lies within about 10× of it on most tasks. The SVHN autoencoder (40 vs 2) and VAE (200 vs 10) miss by about 20×, and the paper says so. Dota 5v5 has no measured front. The noise scale rises by an order of magnitude or more during training. It scales as 1/(ε/B): lowering the temperature 16× raised B_simple about 16× (App. C, Fig. 15).

**A link across two readings.** [LIT-324](../literature.d/LIT-324.md) holds the batch fixed and watches per-layer gradient SNR fall from drift to diffusion at about 350 epochs. In [LIT-348](../literature.d/LIT-348.md)'s terms, that is plausibly where the rising B_simple overtakes the batch in use. This reading is [NOTE-298](../notes.d/NOTE-298.md)'s and [NOTE-293](../notes.d/NOTE-293.md)'s. Neither paper states it, and no one has tested it.

## What this does not say

- **That the model is derived from first principles.** The authors call the derivation one with "many unfounded assumptions" (§2.2): a local quadratic, a greedy optimal step, and H ∝ I for B_simple. Its justification is the fit.
- **That B_crit is predicted rather than fitted.** The functional form is derived, but S_min and E_min are fitted per goal (App. A.3). B_simple/B_crit varies about 10× across tasks, and the paper does not explain why (§5).
- **That the noise scale is a property of the task alone.** It depends strongly on learning rate through the temperature. The claim that model size acts only through the loss reached rests on single-layer LSTMs at three widths, and the paper states it as a conjecture ([NOTE-293](../notes.d/NOTE-293.md), C5).
- **Anything about generalisation.** The model concerns training loss only (§2.4).
- **That the knee is a channel-capacity effect.** Per-step progress saturates to a finite ceiling. A Shannon–Hartley log(1 + SNR) with SNR ∝ B grows without bound. These are different laws, and the paper contains no entropy, channel or capacity ([NOTE-293](../notes.d/NOTE-293.md); curation 2026-09-29, 230637).
- **That the temperature ε/B is physical.** It is an SGD analogy and has no connection to Landauer's k_BT.

## Connections

- [LIT-347](../literature.d/LIT-347.md) and [LIT-356](../literature.d/LIT-356.md) own the "learner as a channel" framing that the prior-art map's row 12 attaches to this knee. Whether a per-step information term rises with B/B_simple is an open question in [NOTE-306](../notes.d/NOTE-306.md).
- The IB-compression reading of [LIT-324](../literature.d/LIT-324.md)'s phases is not relied on here. See [THEORY-tmpd8w6r](THEORY-tmpd8w6r.md), which rejects it.
