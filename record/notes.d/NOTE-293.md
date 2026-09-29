---
number: 293
status: Read
formerly:
- NOTE-tmphsy3o
paper: LIT-348
title: 'An Empirical Model of Large-Batch Training'
version: 1
history:
- version: 1
  date: '2026-09-29'
  note: >-
    Read in full (Full text of arXiv 1812.06162 v1 (14 Dec 2018; the only
    version), 35 pp., from the arXiv PDF: abstract, §§1–5, Appendices A–E
    and the reference list. Text was extracted with PyMuPDF. The figures are
    images and were read from their captions only. Table 1 (p. 24) was
    rendered and read directly. I re-derived eqs. 2.5–2.7 from 2.2 and 2.4,
    and the hyperbola 2.11 from D.1 at fixed B. I also checked the γ = 24/25
    value of eq. D.7. Nothing was skipped.). The first NOTE on this paper,
    which was seeded from its abstract alone.
date: '2026-09-29'
summary: >-
  The paper derives a local model in which the loss progress one step can
  make at batch size B is ΔL_max/(1 + B_noise/B), with B_noise =
  tr(HΣ)/GᵀHG (eqs. 2.7–2.8). Averaged over a run at fixed B, the model
  gives the steps/examples hyperbola (S/S_min − 1)(E/E_min − 1) = 1, which
  defines the critical batch B_crit = E_min/S_min (eqs. 2.11–2.12). Across
  eight tasks, B_crit spans about six orders of magnitude (from 20 to over
  10 million, §3), and the Hessian-free B_simple = tr(Σ)/|G|² tracks it to
  about an order of magnitude (Table 1: run-averaged B_simple/B_crit runs
  from 0.05 for the SVHN VAE and autoencoder to 8 for SVHN).
---

# NOTE-293: An Empirical Model of Large-Batch Training

## Contribution

The paper answers a question that practice had been settling by sweeps: how large a batch is worth using, and why the limit differs so much between domains (thousands for ImageNet, millions for Dota).

- **A statistic.** It defines a gradient noise scale that can be measured during an ordinary run at almost no cost (App. A.1).
- **A model.** It derives a local model in which that statistic sets the knee of the batch-size/speed curve.
- **A law.** It turns the model into a steps-versus-examples law with one free scale, B_crit.
- **Tests.** It tests the law on eight tasks spanning supervised learning, RL and generative modelling.

## Key insight

A minibatch gradient is an unbiased estimate of the true gradient G, with covariance Σ/B. Put that noisy estimate into a second-order Taylor step and optimise the step size. The expected improvement is then the noiseless improvement scaled by 1/(1 + B_noise/B), and B_noise is how much the gradient noise costs relative to its signal.

Below B_noise, adding examples to a batch is nearly as good as taking more steps. Above it, extra examples are mostly wasted.

Summed over a run at fixed B, that one factor gives a hyperbolic Pareto frontier between serial steps and total examples. Its corner is B_crit.

## Assumptions

- **Local quadratic model.** L(θ − εV) ≈ L(θ) − εGᵀV + ½ε²VᵀHV (eq. 2.4). The authors call the derivation one with "many unfounded assumptions" (§2.2) and rest the case on the fits.
- **Batch sampling.** Samples are i.i.d. with replacement, or B ≪ dataset size. Otherwise the variance scales as (1/B − 1/D) (fn. 6).
- **Optimal step size.** The step size is tuned to ε_opt (eq. 2.6). The learning rate is grid-searched per batch size in the experiments (App. A.2).
- **The practical estimator.** B_simple assumes H ∝ I. It is claimed to differ from B_noise "only by a small constant multiplicative factor" in practice (§2.2).
- **Train loss only.** The model is about training loss. Generalisation is explicitly outside it (§2.4, item 6), and test-set goals are checked only briefly (App. E.3).
- **Temperature.** The measured noise scale depends on the learning rate through a "temperature" T = ε/ε_max(B), which is ≈ ε/B for small-batch SGD (App. C). A meaningful measurement needs a well-tuned run.
- **Equilibrium (App. C only).** The temperature analysis assumes SGD has reached the stationary distribution of a quadratic toy model (via Mandt–Hoffman–Blei).

## Key results

- **Per-step progress (eqs. 2.6–2.8).**
  - ε_opt(B) = ε_max/(1 + B_noise/B), and ΔL_opt(B) = ΔL_max/(1 + B_noise/B), with ΔL_max = ½|G|⁴/GᵀHG and B_noise = tr(HΣ)/GᵀHG.
  - At B = B_noise, speed is 50% of maximum (Fig. 3).
  - A step larger than 2ε_opt may increase the loss.
- **Simple noise scale (eqs. 2.9–2.10).** B_simple = tr(Σ)/|G|². Its meaning is fixed by E|G_est − G|²/|G|² = B_simple/B: B_simple is the batch size at which the batch gradient's noise equals its signal.
- **Trade-off law (eqs. 2.11–2.12, App. D).**
  - (S/S_min − 1)(E/E_min − 1) = 1 at fixed B, and B_crit ≡ E_min/S_min ≈ B_noise averaged over the run.
  - At B = B_crit a run takes twice the minimum steps and twice the minimum examples.
  - I re-derived the hyperbola from D.1 at fixed B. It holds exactly even when the noise scale varies over the run.
- **Measurement (App. A.1).**
  - Unbiased estimates of |G|² and tr(Σ) come from gradient norms at two batch sizes, e.g. per-device and all-reduced.
  - The ratio of their moving averages estimates B_simple. It is not unbiased, since E[x/y] ≠ E[x]/E[y].
- **Empirical (Table 1; Figs. 4–14).** Run-averaged critical batch versus run-averaged B_simple:

  | Task | B_crit | B_simple |
  |---|---|---|
  | MNIST | 200 | 900 |
  | SVHN | 500 | 4,000 |
  | CIFAR-10 | 900 | 2,000 |
  | ImageNet | 15,000 | 30,000 |
  | SVHN autoencoder | 40 | 2 |
  | SVHN VAE | 200 | 10 |
  | Billion Word (per token) | 100,000 | 150,000 |
  | Atari | 400–8,000 | 1,000–20,000 |
  | Dota 1v1 | 3×10⁶ | 3×10⁵ |
  | Dota 5v5 | >8×10⁶ (est., not measured) | 2.4×10⁷ |

  The two SVHN generative models miss by about 20×, beyond the "order of magnitude" headline, and the paper says so (§3, §5).
- **Noise scale over a run.** It rises by an order of magnitude or more during training (§3.1). For LSTMs of width 512, 1024 and 2048 it is roughly independent of model size at fixed loss (Fig. 8).
- **Temperature (App. C).** B_noise ∝ B_simple ∝ 1/T. Lowering ε/B by 16× raised B_simple by about 16× on SVHN (SGD) and Billion Word (Adam) (Fig. 15).
- **Adaptive batch (App. D).**
  - The optimal schedule is B(s) = √(r·B_noise(s)).
  - The predicted gain is γ = (∫√B_noise)²/(S_min·E_min).
  - For SVHN, B_crit ≈ 10√s gives γ = 24/25, about 4%. The observed gains look larger than predicted.
- **Optimisation (App. E).**
  - Line-search "greedient descent" performs poorly.
  - At a fixed learning rate, training settles where the actual update is about twice the line-search optimum (Figs. 17–18).
  - Adam's optimal learning rate scales as B^α with 0.5 < α < 1 (App. E.2 gives a heuristic for why).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Per-step progress depends on B only through 1/(1 + B_noise/B) | moderate (derivation) | eqs. 2.4–2.8, under a local quadratic model with optimal step size, flagged by the authors as resting on "unfounded assumptions" |
| C2 | At fixed B, steps and examples satisfy (S/S_min − 1)(E/E_min − 1) = 1 | strong for the form (derivation) plus experiment | App. D.1 (exact given C1), and fits in Figs. 6–14 |
| C3 | B_simple predicts B_crit "at the order of magnitude level" | moderate (experiment) | Table 1: holds within ~10× except the two SVHN generative models (~20×); Dota 5v5 B_crit only lower-bounded |
| C4 | The noise scale grows during training | strong (experiment) | measured on every task (§3.1, Table 1 start vs average) |
| C5 | Model size affects the noise scale only through the loss reached | weak–moderate (experiment) | one architecture family, LSTMs at three widths (Fig. 8); stated as a conjecture in §3 |
| C6 | The noise scale ∝ 1/temperature (ε/B) | moderate | quadratic toy model (App. C) plus two interventions (Fig. 15) |
| C7 | Adaptive batch sizing gives modest gains (~4% predicted on SVHN) | weak | one SVHN case study; observed gains exceed the prediction, unexplained |
| C8 | More complex tasks have larger noise scales | moderate (experiment) | cross-task pattern (Fig. 4); "complexity" is informal |

## Method

1. Grid-search learning rates at each batch size, starting from ε_central(B) = ε*/(1 + B*/B)^α.
2. For each goal loss or score, take the fastest run at each B.
3. Fit eq. 2.11 in log space to get S_min, E_min and hence B_crit.
4. Separately, estimate B_simple on one well-tuned run from gradient norms at two batch sizes, smoothed by exponential moving averages.
5. For SVHN/SGD only, also estimate B_noise by line searches.

## Concepts

- **Gradient noise scale.** B_noise, and its Hessian-free proxy B_simple.
- **Critical batch size.** B_crit = E_min/S_min.
- **Time/compute Pareto frontier.** The steps-versus-examples hyperbola of eq. 2.11.
- **Training temperature.** T = ε/ε_max(B) ≈ ε/B. This is an SGD analogy, not a physical temperature.
- **Adaptive batch schedule.** B ∝ √B_noise.

## Connections

- **Shwartz-Ziv & Tishby.** The paper cites them as [SZT17] for "a signal-dominated and noise-dominated phase of training" (§4); that paper's drift/diffusion SNR phases are that citation. In this paper's terms, the drift-to-diffusion transition at fixed batch is the point where B_simple, rising as the loss falls, passes the batch size in use.
- **Earlier batch-size work.** Byrd et al. 2012 and Balles et al. 2016 used the gradient noise scale implicitly for sample-size selection (§4). Smith & Le 2017 and Smith et al. 2017 supply the ε/B temperature.
- **Shallue et al. 2018.** Parallel, and reports no large-batch generalisation gap when hyperparameters are properly tuned.

## Bearing on the record

**What the map's row 12 says this paper owns, and whether it does.**
- *Batch = SNR.* Owned. B_simple is the gradient's noise-to-signal ratio in units of examples (eq. 2.10), and the paper describes it as an SNR measure.
- *The critical batch.* Owned. B_crit is defined and measured here.
- *The time/compute-to-target trade-off.* Owned, as eq. 2.11.
- *Gradient as a channel.* Not owned. The paper has no information theory, capacity or channel.
- *Energy.* Not owned. The costs are steps and examples.
- *The information-theoretic framing.* Its nearest owners in this batch are Xu & Raginsky ([LIT-347](../literature.d/LIT-347.md)), who treat a learning algorithm as a channel P_{W|S}, and the IB papers ([LIT-338](../literature.d/LIT-338.md), [LIT-324](../literature.d/LIT-324.md)).

**Does the owner "re-derive McCandlish"?** In the conclusions, yes; in the formulas, no, and where the two differ this paper is the tested one. §5 of the owner's gradient-channel document writes per-step capacity as C_step = d·log₂(1 + SNR_b(B)) and defines B* as where the information I(B) saturates. It also says information grows "near-linear in B" below B* and "logarithmic" above, with B* ≈ min(2^{p·b}, rank Cov∇L, entropy ratios).

- **Where they agree.** Both have a linear-then-diminishing knee, a critical batch, and a time/compute trade-off. The owner's document already names this paper as "the empirical anchor to cite".
- **The functional form.** Here the per-step progress saturates to a finite ceiling, ΔL_max/(1 + B_noise/B). A Shannon–Hartley log(1 + SNR), with SNR ∝ B, grows without bound. These are different laws, and eq. 2.11's hyperbola was fitted across eight tasks.
- **The knee.** Here it sits at tr(Σ)/|G|² (Hessian-weighted in B_noise). The owner's candidates (a rank, entropy ratios, 2^{p·b}) are different quantities and are untested.

So "re-derives" is right about the claims the owner may not make as new: batch = SNR, a critical batch, and the time/compute knee. It overstates the match of the mathematics. The owner's version is a different, information-theoretic model of the same knee, and its log regime would have to be reconciled with eq. 2.7 before it could be cited as consistent with this paper. Cite this paper as the owner of the phenomenon and its measurement, and present the channel reading as a reinterpretation.

**Two equivocations to avoid.**
- *Temperature.* This paper's "temperature" is ε/B (App. C), an SGD analogy. It is not k_B·T. Row 13's Landauer floor and this temperature must not be conflated.
- *Energy.* Its "compute" is examples processed, not joules.

**Connections in nucleation.**
- [LIT-317](../literature.d/LIT-317.md) (Shannon 1949) owns the log₂(1 + P/N) capacity the owner uses. This paper shows the batch-size knee needs none of it.
- [LIT-324](../literature.d/LIT-324.md): see Connections above.

**ML practice.** Real, and held in the anthology ([ANTH-LIT-017](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-017.md), [NOTE-062](NOTE-062.md)). Disagreements with the anthology's reading, reported per [ADR-013](../decisions.d/ADR-013.md) and not fixed here:
- **"Order of magnitude" ([NOTE-062](NOTE-062.md) C2, "strong", "verified on eight tasks").** This is not met for the SVHN autoencoder (B_crit 40 vs B_simple 2) or the VAE (200 vs 10), both about 20× by Table 1. The paper itself says B_simple was "significantly smaller than B_crit" for generative models. Dota 5v5 has no measured Pareto front.
- **Model size ([NOTE-062](NOTE-062.md) C5 and [LIT-017](../literature.d/LIT-017.md)).** "Model size affects the noise scale only through the loss", called "genuinely non-obvious … the paper isolates it". The evidence is one family, single-layer LSTMs at three widths on Billion Word, and the paper states it as a conjecture it tested there.
- **C3, "the shape is predicted not fitted".** The functional form is derived, but S_min and E_min, and hence B_crit, are fitted per goal (App. A.3). B_crit is a fit parameter, not a prediction.
- **Key insight: "a signal-to-noise question, and nothing else".** This is stronger than the paper. The noise scale depends strongly on learning rate through the temperature (App. C, §2.4 item 4), and short-horizon bias and poor conditioning are listed as caveats (§2.4).
- **Dataset-size independence.** [LIT-017](../literature.d/LIT-017.md) says it is "what lets it transfer between domains". The paper notes the definition is independent of dataset size (§2.2, fn. 4) but does not make that argument.

## Limitations

- **Train loss only.** Everything concerns training loss. The generalisation check is a brief App. E.3, which found a small end-of-training dip in B_crit on test goals.
- **The derivation is local.** It is greedy and second-order. Its justification is the empirical fit, and the ratio B_simple/B_crit varies by about 10× across tasks with no explanation (§5).
- **Only one proxy is measured.** B_noise is measured only for SVHN/SGD. Everything else uses B_simple.
- **2018 scales.** The largest language experiment is a single-layer LSTM on Billion Word. Adam-preconditioned noise scales gave "mixed results" (fn. 7, fn. 10).
- **The figures could not be read.** They are images; the numbers in this note come from the text and Table 1.

## Open questions

- Can the owner's channel-capacity per-step law be made consistent with ΔL ∝ 1/(1 + B_noise/B)? For example, is the information per step about the minimiser, rather than about the loss, what saturates logarithmically? That would settle whether §5 adds a prediction this paper lacks or only renames its knee.
- Is there an information-theoretic reading of B_simple itself? For Gaussian gradient noise, B/B_simple is the per-step SNR, so ½·log(1 + B/B_simple) nats would be the capacity of one scalar projection. Whether that reproduces eq. 2.11 is unverified.

## Corrections to the seeded skim

- Seeded from metadata; the text confirms the title, authors (McCandlish, Kaplan, Amodei and the OpenAI Dota Team), the arXiv id and the date 14 Dec 2018. McCandlish's work was done "as an OpenAI Fellow". Kaplan's affiliation is Johns Hopkins and OpenAI.
- The seed summary is accurate. One thing to add: the paper frames the noise scale as "essentially a measure of the signal-to-noise ratio of gradient across training examples" (§1). B_simple/B is exactly the expected normalised squared error of the batch gradient (eq. 2.10). "Batch = SNR" is therefore the paper's own reading, not a gloss.
- The tag `information-theory` is not supported by the text. No entropy, mutual information, channel or capacity appears anywhere; the paper is second-order optimisation plus measurement. Proposed tags: [learning-theory]. It is held for ML practice in the anthology, and `anthology-candidate` is moot while it is dual-held.
- The map's row-12 wording, "time/energy-to-target", overreaches for this paper. It measures optimiser steps (time) and examples processed (compute), never energy.
- Slips in the text. §3 (Atari) cites a deviation "from 12" where eq. 2.11 is meant. Appendix D.1 says the loss "increases by an amount δL" over a step where decreases is meant. Table 1's caption says the critical batch is reported "early in the run and at the end", but its column is headed "Average".
- Row 12 says the owner "re-derives McCandlish". That holds for the qualitative conclusions and not for the formulas; see Bearing on the record.
