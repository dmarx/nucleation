---
status: Read
paper: LIT-324
title: 'Opening the Black Box of Deep Neural Networks via Information'
version: 1
history:
- version: 1
  date: '2026-09-29'
  note: >-
    Read in full (Full text of arXiv 1703.00810 v3 (29 Apr 2017), 19 pp.,
    from the arXiv PDF: abstract, §§1–4, Figs. 1–8 (captions; the plots are
    images) and references. Text was extracted with PyMuPDF. The
    "supplementary material" and "appendix" the text refers to
    (non-symmetric rules; weight norms) are not in the arXiv PDF and were
    not read. I did not read the critiques (Saxe et al. 2018 and others) and
    rely on the anthology's account of them only where I say so.). The first
    NOTE on this paper, which was seeded from its abstract alone.
date: '2026-09-29'
summary: >-
  The paper studies small tanh networks (layer widths down from 12 to 2)
  trained by SGD on a 12-bit, O(3)-symmetric synthetic rule, with mutual
  information estimated by binning each neuron into 30 bins over all 4,096
  inputs. It reports two phases: a short "ERM" phase of a few hundred
  epochs in which I(T;Y) rises, and a long "compression" phase in which
  I(X;T) falls. The phases coincide with a drop in per-layer gradient SNR
  (from high-SNR drift to low-SNR diffusion, at about 350 epochs), and the
  converged layers sit on the IB curve at fitted β. Everything is shown on
  small synthetic tasks, with the explanations argued informally.
---

# NOTE-tmpp6255: Opening the Black Box of Deep Neural Networks via Information

## Contribution

Following Tishby & Zaslavsky (2015), the paper plots each layer T of a trained network as a point (I(X;T), I(T;Y)) in the information plane over training. It reports four things:

- **Two phases.** A fast fitting phase is followed by a long compression phase.
- **Gradient SNR.** The phase change coincides with a change from high to low gradient SNR.
- **The IB bound.** Converged layers satisfy the IB self-consistent equations at some β.
- **Depth.** Added hidden layers shorten training, and the paper offers a diffusion-time argument for why.

It also claims that compression "by diffusion" is the mechanism of generalisation.

## Key insight

Treat each layer as one random variable, characterised only by two numbers that are invariant to invertible reparametrisation (§2): its information about the input and about the label. The paper then reads SGD's two regimes off the gradient statistics:

- **Drift:** mean gradient ≫ fluctuation.
- **Diffusion:** fluctuation ≫ mean.

It reads the diffusion regime as an entropy-maximising relaxation. That relaxation increases H(X|T) under the training-error constraint, i.e. compresses.

## Assumptions

- **A known joint distribution.** P(X,Y) is known exactly: 4,096 equiprobable 12-bit inputs and a spherically symmetric rule, with p(y=1|x) = ψ(f(x) − θ), I(X;Y) ≈ 0.99 bits (§3.1). The information values use this full distribution, so I(T;Y) stands in for test performance (§3.4).
- **The networks.** Fully connected tanh networks with a sigmoid output, trained by SGD on cross-entropy with no explicit regularisation, 50 random initialisations and training splits per setting (§3.1–3.2).
- **The estimator.** Mutual information comes from discretising each neuron into 30 equal bins in [−1, 1] (§3.2). §2.3 says deterministic networks are handled by "consider[ing] the sigmoidal output of the neurons as probabilities". The paper does not reconcile the two noise models.
- **Smooth rules.** For "smooth" P(X,Y) (Y not a deterministic function of X), the IB curve is strictly concave, with a unique slope β⁻¹ at each point (§2.3).
- **Diffusion (§3.5, §3.7).** SGD in the diffusion phase behaves as a Wiener process, with a Fokker–Planck stationary distribution that maximises weight entropy under the error constraint. This is asserted, with "a rigorous analysis … elsewhere".

## Key results

- **Two phases (§3.4, Figs. 2–3).**
  - I(T;Y) rises in a few hundred epochs.
  - I(X;T) then falls over thousands of epochs (to 10⁴), with the order of the data-processing inequality preserved.
  - Paths are similar across the 50 runs, which justifies averaging them.
- **Sample size (§3.4).** With 85% of the data, label information mostly increases during compression. With 5%, compression lowers it, and the paper attributes that overfitting "largely" to compression.
- **Gradient SNR phases (§3.5, Fig. 4).**
  - Per-layer normalised gradient mean and standard deviation across batches show a transition at about 350 epochs, from high SNR (drift) to low SNR (diffusion).
  - The transition coincides with the bend in the information-plane paths.
  - Log SNR approaches a constant across layers at convergence.
- **Diffusion argument (§3.7).** Diffusion entropy grows as log(Dt), so compressing by ΔI_X takes about exp(ΔI_X/D) steps. Splitting the compression across K layers gives exp(ΣΔI_X^k) ≫ Σ exp(ΔI_X^k) (eq. 11), an exponential saving in epochs with depth. This is a heuristic.
- **Depth (§3.6, Fig. 5).** With 6 hidden layers the network reaches full relevant information within about 400 epochs; with 1 it does not by 10⁴. The width-12 first layer never compresses.
- **The IB bound (§3.8, Fig. 6).**
  - For each converged layer, the fitted β*ᵢ = argmin_β E_x D_KL[pᵢ(t|x)‖p^IB_β(t|x)] (eq. 12) places the layers "remarkably close" to the IB curve, with β decreasing in depth.
  - The layers are said to satisfy the IB equations "within our numerical precision".
- **Sample-size sweep (§3.9, Fig. 7).** Converged layers for 3–85% data lie on smooth lines. They are claimed to lie on finite-sample IB curves, which is asserted and not computed in the paper.
- **Generality (§4, Fig. 8).** A committee-machine rule shows the same phases. MNIST shows the SGD diffusion transition, but its information plane was not estimated.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | SGD training has a short fitting phase then a long compression phase in the information plane | moderate (experiment), estimator-dependent | small synthetic tasks, binned MI (§3.4); the estimator is exactly what the critiques contest (per [ANTH-LIT-509](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-509.md), unverified here) |
| C2 | The phase change coincides with a gradient-SNR transition from drift to diffusion | moderate (experiment) | Fig. 4, one architecture, plus a committee machine (Fig. 8) and MNIST gradient statistics (§4) |
| C3 | Diffusion causes compression by maximising H(X|T) under the error constraint | weak (informal argument) | §3.5; the "rigorous analysis" is deferred to "elsewhere" |
| C4 | Converged layers lie on or near the IB bound and satisfy the IB equations | moderate (fit) | Fig. 6; β is fitted per layer to minimise the very divergence the claim is about |
| C5 | Compression by noise explains the absence of overfitting / generalisation | weak (assertion) | "we believe" (§1), "If our findings hold…" (§4); contradicted in the 5% regime by the paper's own §3.4 |
| C6 | Hidden layers' main benefit is computational: an exponential reduction in diffusion time with depth | weak–moderate | the eq. 11 heuristic plus Fig. 5 |
| C7 | Layers converge near critical points of the IB curve (critical slowing down) | assertion (hypothesis) | abstract (v), §3.5, "examined elsewhere" |
| C8 | The mechanism is "unique to Deep Neural Networks and absent in one layer networks" | weak (argument) | §4, by the perceptron arccos argument |

## Method

1. Compute exact information-plane coordinates on a fully enumerable synthetic distribution by binning activations.
2. Average 50 randomised runs.
3. Separately track the per-layer mean and standard deviation of minibatch gradients, normalised by weight norms.
4. Test IB optimality by fitting β per layer so that the IB encoder built from the layer's decoder matches the layer's encoder.

## Concepts

- **Information plane and information path.** A layer's trajectory in (I(X;T), I(T;Y)).
- **ERM and compression phases.**
- **Drift and diffusion phases of SGD.** Gradient SNR above or below 1.
- **Stochastic relaxation.**
- **Approximate minimal sufficient statistics.** IB representations read as such, via T = argmin I(S(X);X) subject to I(S(X);Y) = I(X;Y) (eq. 7).

## Connections

- **[LIT-338](../literature.d/LIT-338.md) (Tishby, Pereira & Bialek).** Eq. (9) reproduces its self-consistent equations. §2.3 makes explicit the minimal-sufficient-statistic reading that [LIT-338](../literature.d/LIT-338.md) only gestures at.
- **[LIT-348](../literature.d/LIT-348.md) (McCandlish et al. 2018).** It cites this paper as [SZT17] for "a signal-dominated and noise-dominated phase of training". The two SNRs are the same object seen from two sides.
  - This paper holds the batch fixed and watches the gradient SNR fall.
  - McCandlish holds the point fixed and asks at what batch the noise equals the signal: B_simple = tr(Σ)/|G|², with E|G_est − G|²/|G|² = B_simple/B.
  - The drift-to-diffusion transition is where B_simple, rising as the loss falls, overtakes the batch in use. That is my reading of the two texts together; neither paper states it.
- **[LIT-247](../literature.d/LIT-247.md) (Tschannen et al.; seeded, not read).** Its point, per its seed summary, that mutual information is invariant under invertible maps, so maximising it does not explain representation quality, is the same invariance this paper puts at the base of its method (§2, eq. 3). This paper flags the cost itself: for deterministic maps, information "is insensitive to the complexity of the function" (§2.4).
- **[LIT-240](../literature.d/LIT-240.md) and [LIT-245](../literature.d/LIT-245.md).** They pick up the "IB term controls generalisation" claim (C5) formally; [LIT-245](../literature.d/LIT-245.md) corrects [LIT-240](../literature.d/LIT-240.md).

## Bearing on the record

**Row 12.** The map cites this paper as a must-cite for "information-bottleneck account of learning dynamics", and it is that account's source. It supplies more to the owner's §5 than the map says, and less.

- **More.** §5's core move, "batch enters as the signal-to-noise ratio of the gradient channel", has a precursor here: SGD dynamics split by per-layer gradient SNR, with the low-SNR regime doing something qualitatively different (§3.5). McCandlish, the paper the owner is said to re-derive, cites this paper for exactly that. Cite both as prior art for "gradient SNR organises training".
- **Less.**
  - *No channel.* This paper has no capacity, no bits-per-step bound and no batch-size law. Its SNR is observed, not derived, and it does not vary the batch.
  - *A contested account.* Its information-plane account of learning is disputed. The anthology holds it as "the claim rather than a result" ([ANTH-LIT-508](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-508.md)), with the rebuttal in [ANTH-LIT-509](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-509.md). On the estimator issue I can say only that this paper's own §2.4 concedes the root of it: information is blind to function complexity unless noise is added.
  - *The fair citation.* Cite it as the proposal, and cite its critique alongside.

**Connections in nucleation.** [LIT-338](../literature.d/LIT-338.md) (IB), [LIT-348](../literature.d/LIT-348.md) (noise scale) and [LIT-247](../literature.d/LIT-247.md) (MI invariance) are covered under Connections above. [LIT-226](../literature.d/LIT-226.md) (CEB) inherits the IB programme and the minimal-necessary-information target that eq. (7) motivates.

**ML practice.** It is held in the anthology ([ANTH-LIT-508](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-508.md), `Active`, "not read as a NOTE"). Disagreements with the anthology's entry, reported per [ADR-013](../decisions.d/ADR-013.md) and not fixed here:
- **The summary says "compression is said to explain generalization" and leaves it there.** The paper's own §3.4 reports that at 5% data the compression phase *loses* relevant information, and it calls the resulting overfitting "largely due to the compression phase". The paper undercuts its own causal claim in the small-sample regime. The anthology's account of the dispute would be stronger for saying so, because it is internal evidence, not only the rebuttal's.
- **"What a full reading would settle is whether the IB-bound claim (iii) survives the estimator objection."** A full reading shows the claim is a fit: β is chosen per layer to minimise the divergence between the layer's encoder and the IB encoder built from the layer's own decoder (eq. 12). "Lie on the IB bound" is therefore "there exists a β for which the layer is close to IB-consistent". That is weaker than the headline, whatever the estimator.
- **Two noise models.** The binning estimator (§3.2) and the "sigmoid outputs as probabilities" model (§2.3) are both in the paper and not reconciled. The anthology's point about "an imposed noise model" can cite the paper's own §2.4.
- **Minor.** The anthology quotes the "30 equal intervals" correctly. The text says "arctan output activations" for tanh units.

## Limitations

- **One synthetic distribution.** Everything is shown on one fully enumerable 12-bit synthetic distribution, the committee machine and MNIST gradient statistics. "It should be verified on larger problems" (§3.4).
- **Two noise models.** The information values depend on the binning; the §2.3 probabilistic reading differs from it.
- **Deferred and missing material.** The causal mechanism (diffusion ⇒ compression ⇒ generalisation), the critical-point hypothesis and the finite-sample IB curves are all deferred "elsewhere". The supplementary material the text cites is not in the arXiv version.
- **The IB-bound test fits β per layer**, which builds agreement in.
- **The headline claims in the abstract are stronger than the body's evidence** (C5, C8).

## Open questions

- Does the drift/diffusion transition quantitatively coincide with B_simple(t) crossing the batch size, in McCandlish's measurement? That is a cheap test that would join [LIT-324](../literature.d/LIT-324.md) and [LIT-348](../literature.d/LIT-348.md) on one axis, and it bears directly on the owner's "batch = SNR".
- If compression depends on the estimator, is there an estimator-free statement of the phase change (e.g. in terms of B_simple or the Fisher spectrum) that survives? That would be what the owner could safely use for row 12.

## Corrections to the seeded skim

- Seeded from metadata. The text confirms the title, arXiv id and co-author. The arXiv v3 PDF prints the first author as "Ravid Schwartz-Ziv" in the byline and running head; the seed's "Shwartz-Ziv" matches how McCandlish et al. ([LIT-348](../literature.d/LIT-348.md)) cite him and his later publications. It is an identification variant only.
- The seed summary is accurate but should carry two things.
  - *Estimator.* The information-plane values come from binning neuron outputs (30 equal bins in [−1, 1]; §3.2). §2.3 instead treats sigmoidal outputs as probabilities. These are two different noise models.
  - *The compression and generalisation claim is hedged in the body and contradicted by its own small-sample result.* At 5% training data the compression phase reduces the layers' label information, and the paper itself calls this "overfitting … largely due to the compression phase" (§3.4).
- The seed says "the representation compression phase … relating layers to the information-bottleneck bound". The fuller statement: at convergence, each layer's encoder is compared with the IB-optimal encoder built from that layer's decoder, with β fitted per layer (eq. 12). The claim of lying "on or very close to" the IB bound rests on that fit (Fig. 6).
- Internal inconsistencies:
  - The architecture is given as 12-10-7-5-4-3-2 (§3.1) but as 12-10-8-6-4-2-1 in Fig. 3's caption.
  - IB curves are called "concave" (§2.3) and "convex" (§3.9).
  - §3.7 cites "section 3.8" for a result that comes later.
  - §3.2 speaks of "arctan output activations" for tanh units.
- Map role (row 12, "IB account of learning dynamics") holds. The paper's gradient-SNR phases are also a direct precursor of McCandlish's noise scale. See Bearing on the record.
