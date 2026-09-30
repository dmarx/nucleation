---
number: 320
status: Read
formerly:
- NOTE-tmpz37g5
paper: LIT-372
title: 'On the Information Bottleneck Theory of Deep Learning'
version: 1
history:
- version: 1
  date: '2026-09-30'
  note: >-
    Read in full (Full text of the ICLR 2018 conference paper, 27 pp. (main
    text §§1–6, references, Appendices A–I with all figure captions; the
    figures are images and were read from captions, axis labels and text).
    Source is the PDF linked as "pdf" for the ICLR 2018 entry on co-author
    Artemy Kolchinsky's publications page (artemyk.github.io); it is a
    ResearchGate export whose cover page says it was uploaded by co-author
    Joel Dapello on 8 May 2018, followed by the paper as "Published as a
    conference paper at ICLR 2018". Also read in full for differences: the
    updated J. Stat. Mech. (2019) 124020 version of record, 34 pp., linked
    as "pdf" for the JSTAT entry on the same author page (it carries "This
    article is an updated version of" the ICLR paper; received 15 July 2019,
    published 20 December 2019). Text extracted with PyMuPDF. Nothing
    skipped. OpenReview itself (forum ry_WPG-A-) returned 403 / a bot
    challenge, so the reviews and the Tishby comment thread there were not
    read. `published:` is 2018-02-15, the publication date Semantic Scholar
    gives for the ICLR record (DBLP key conf/iclr/SaxeBDAKTC18), which
    matches OpenReview's posting date for ICLR 2018 accepted papers; I could
    not open OpenReview to confirm it, and the anonymous submission was
    probably public earlier (late 2017), which is unverified. Already held
    in the Anthology of the SOTA as ANTH-LIT-509 (read there, from the ICLR
    version, in the anthology NOTE on that LIT). Dual holding (nucleation
    ADR-013): nucleation needs it as the independent test of the account
    THEORY-035 rejects, which that draft says was "not in this record
    and was not read here"; the anthology holds it for ML practice
    (information-plane measurement).). The first NOTE on this paper, which
    was seeded from its abstract alone.
date: '2026-09-30'
summary: >-
  Replicating Shwartz-Ziv & Tishby with their own code, the paper shows
  the information-plane "compression phase" appears only for
  double-saturating nonlinearities measured through an imposed
  binning/noise model: tanh compresses, ReLU/softplus/linear do not
  (binning, KDE, Kraskov; SZT task and MNIST), and re-binning the same
  tanh run evenly in net input removes it. Compression and generalisation
  dissociate in all four combinations, full-batch GD compresses as much as
  SGD, and the drift→diffusion gradient-SNR transition occurs in networks
  that cannot compress (ReLU, MNIST, a 1-1-1 linear net), so it is real
  but unrelated to compression.
---

# NOTE-320: On the Information Bottleneck Theory of Deep Learning

## Contribution

The paper tests the three claims of the information-bottleneck (IB) theory of deep learning as stated by Shwartz-Ziv & Tishby ([LIT-324](../literature.d/LIT-324.md)): (1) training has an initial fitting phase and then a compression phase in I(X;T); (2) compression is causally related to generalisation; (3) compression is caused by the diffusion-like behaviour of SGD. It replicates [LIT-324](../literature.d/LIT-324.md) with the original code and then changes one thing at a time: the nonlinearity, the estimator, the binning scheme, the training set size, and SGD versus full-batch gradient descent. It adds an exact deep-linear student–teacher analysis. Its conclusion is that "none of these claims hold true in the general case" (abstract). The information-plane trajectory is "predominantly a function of the neural nonlinearity employed" together with the binning or noise assumption needed to make I(X;T) finite.

## Key insight

For a deterministic network, h = f(X) has H(h|X) = −∞, so the continuous I(h;X) is infinite (App. C, eqs. 17–20). A finite number exists only after the analyst adds noise T = h + Z or bins h. On a finite input set with binning, I(X;T) = H(T) exactly (eqs. 1–3), so "compression" means only that the binned activity pattern takes fewer distinct values. A tanh unit whose weights grow drives its activity into the two extreme bins. The binned entropy then falls toward about 1 bit even though the network's input–output map is getting richer (Fig. 2C). The compression phase is what weight growth in a saturating network looks like through a fixed-width binning estimator. It is not a separate learning process.

## Assumptions

- **Replication setting (§2).** The SZT architecture 12-10-7-5-4-3-2 with tanh and a 2-unit sigmoid output layer, trained by SGD (batch 256 in the replication) on the 12-bit, 4,096-pattern task. Activity is binned into 30 equal bins in [−1, 1]. The ReLU version uses 100 equal bins between the minimum and maximum activity over all units and all epochs of the completed run (§2; App. C).
- **Estimators (App. B).**
  - The KDE upper bound (eq. 7) assumes T = h + ε, ε ~ N(0, σ²I) with σ² = 0.1, over the empirical input distribution.
  - The Kraskov k-NN estimator (k = 2, ε = 10⁻¹⁶) estimates H(T), which equals I(X;T) up to a constant only under homoscedastic noise.
- **Linear student–teacher (§3).** X ~ N(0, I/Nᵢ), Y = W₀X + ε₀, teacher weights i.i.d. N(0, σ²_w), SNR = σ²_w/σ²₀. The student is a deep linear network trained by MSE. Its generalisation error is exact: E_g(t) = ‖W₀ − W_tot(t)‖²_F + σ²₀ (eq. 5). MI is computed exactly under an imposed per-layer noise σ²_MI = 1.0 (eq. 6).
- **Isotropic inputs.** All input dimensions have equal variance, and teacher weights are drawn independently, so "there are no special directions in the input" (§3). The authors flag that real tasks may put the signal in high-variance directions and say they have not investigated it.
- **Weight growth.** Weights start small and grow during training. App. D argues this is "a virtual necessity" for tanh networks to compute nonlinear functions, and shows it empirically (weight-norm lines in Figs. 9, 10, 20, 21).

## Key results

- **Nonlinearity decides compression (§2; Figs. 1, 8, 12).**
  - The tanh replication reproduces [LIT-324](../literature.d/LIT-324.md)'s fitting-then-compression paths (Fig. 1A).
  - ReLU: "The mutual information with the input monotonically increases in all ReLU layers" (Fig. 1B). Only the sigmoid output layer compresses (Fig. 17).
  - MNIST, 784-1024-20-20-20-10, KDE: tanh compresses and ReLU does not, except the final sigmoid layer (Fig. 1C–D).
  - Across activations (KDE, SZT task, 50 repeats): tanh compresses, softsign "modest compression", ReLU and softplus none (Fig. 8). The Kraskov entropy estimate gives the same split (Fig. 12).
- **Minimal model (§2, eqs. 1–4, Fig. 2).** Three neurons, X ~ N(0,1), h = f(w₁X), T = bin(h). Then I(T;X) = H(T) = −Σ pᵢ log pᵢ, with pᵢ exact from the Gaussian CDF.
  - tanh: I rises and then falls as w₁ grows, tending to about 1 bit as the unit saturates ("more or less a coin flip").
  - ReLU: half the mass sits in the zero bin and the rest spreads, so I increases without bound.
- **The binning scheme decides compression too (App. C, Figs. 13–15).**
  - Bin edges at tanh(linspace(−50, 50, N)), i.e. evenly spaced in net input: the minimal model's MI keeps rising (Fig. 13), and the same tanh run shows "no compression in most layers" (Fig. 14).
  - Binning at full machine precision pins most layers at log₂(P) = 12 bits. Only the highest, smallest tanh layers compress, near the end of training (Fig. 15).
  - Two consequences follow. The data-processing inequality does not hold for these per-layer estimates, because the analysis noise does not propagate through the network. MI is not invariant under invertible reparametrisation: with w̃₁ = w₁/c and w̃₂ = c·w₂ (the same function, so the same generalisation), I(T;X) = log(w₁²/c² + σ²_MI) − log σ²_MI (eq. 21).
- **Deep linear networks do not compress (§3; Figs. 3, 18).**
  - 100-100-1, batch GD, P = 100, SNR = 1: no compression, good generalisation, minimal overtraining.
  - A 5×50 deep linear net also shows no compression.
- **Compression and generalisation dissociate (§3; Fig. 4).**
  - Linear, Nᵢ = P = 100 (batch size 5): substantial overtraining, no compression, and I(T;Y) falls during overtraining.
  - tanh on 30% of the SZT data: "modest overfitting" with "continued compression" (Fig. 4C–D).
  - Together with Fig. 1A (compresses, generalises) and Figs. 1B/3 (no compression, generalises), this fills all four cells.
- **Stochasticity is not the cause (§4; Figs. 5, 19).** tanh and ReLU nets trained by single-example offline SGD and by full-batch GD show "largely consistent information dynamics", with "robust compression in tanh networks for both methods". The same holds for a linear net (Fig. 19).
- **Theoretical objection to the diffusion mechanism (§4).** A maximum-entropy stationary distribution over weights describes variability *across training runs*. H(X|T) is uncertainty about *inputs* for one set of weights. "There is no general reason" a single draw maximises H(X|T).
- **The gradient-SNR transition is general and unrelated (§4; App. I; Figs. 9–10, 20–21).**
  - SNR per layer is m_l/s_l, with m_l = ‖⟨∂E/∂W_l⟩‖_F and s_l = ‖STD(∂E/∂W_l)‖_F over all training samples (eqs. 26–27).
  - It shows a "step-like transition to a lower value" in tanh and ReLU nets on the SZT task, on MNIST, and in a 1-1-1 linear network (P = 100, teacher SNR = 1, lr 0.001) that cannot compress while its weight grows.
  - Mechanism offered: early gradients agree because all weights must grow; near the minimum the mean gradient goes to zero while per-example spread stays finite.
- **Simultaneous fitting and compression (§5; Fig. 6).** Linear network, SGD (batch 5), 30 task-relevant and 70 task-irrelevant inputs (teacher weights zero on the latter).
  - Overall I(X;T) shows no compression, and information about the relevant subspace rises.
  - Information about the irrelevant subspace "does compress after initially growing", at the same time as fitting, not in a later phase.
- **Saturation explains the slowdown (§2, App. E).** Activation histograms show the last three tanh layers saturating into the extreme bins during training (Fig. 16). This also explains the slowdown [LIT-324](../literature.d/LIT-324.md) attributes to compression: saturated units pass back smaller gradients.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Compression in the information plane is produced by double-saturating nonlinearities under binning/homoscedastic-noise MI; ReLU, softplus and linear networks do not compress | experiment + exact minimal model | §2, Figs. 1, 2, 8, 12; three estimators, with the thin spots noted in corrections (Kraskov is H(T) only; MNIST is one run) |
| C2 | The true I(h;X) of a deterministic network is infinite, so finite values reflect an analyst-imposed noise model; different binnings of one run disagree about compression | proof (elementary) + experiment | App. C eqs. 17–21; Figs. 13–15 |
| C3 | Compression and generalisation are dissociated: all four combinations occur | experiment (four small settings) | Figs. 1A, 1B, 3, 4; linear MI is exact given σ²_MI = 1 |
| C4 | SGD stochasticity is not necessary for compression | experiment | BGD vs SGD, Fig. 5 (tanh, ReLU), Fig. 19 (linear) |
| C5 | The drift→diffusion gradient-SNR transition is a general feature of gradient descent near a minimum and is not causally related to compression | experiment + informal argument | Figs. 9–10, 20–21; App. I; prior literature cited |
| C6 | The IB diffusion argument conflates entropy of weights across runs with H(X|T) for one network | informal argument | §4 |
| C7 | Task-irrelevant input information is compressed concurrently with fitting, while total I(X;T) rises | experiment (one linear setting) | §5, Fig. 6 |
| C8 | "None of these claims hold true in the general case" (abstract) | counterexamples, which is the right support for a negation of generality | the whole paper; it does not show the claims fail in [LIT-324](../literature.d/LIT-324.md)'s own tanh setting except claim 3 |

The abstract's reach is matched by the body for a *general* negation. It does not show that compression never accompanies generalisation. The IB-bound claim (converged layers near the IB curve) and the depth/diffusion-time claim of [LIT-324](../literature.d/LIT-324.md) are not tested.

## Method

1. Rerun the original IB code with activation, estimator and binning swapped one at a time.
2. Use an analytically solvable one-unit model to show what binned MI does as weights grow.
3. Use deep linear student–teacher networks, where generalisation error and MI (under a stated noise σ²_MI) are exact.
4. Train with SGD and with batch gradient descent on the same data.
5. Track per-layer gradient mean and standard deviation (Frobenius norms over all samples) and weight norms.

## Concepts

- **Information plane / compression phase.** As in [LIT-324](../literature.d/LIT-324.md).
- **Double- vs single-sided saturation.** tanh/softsign against ReLU/softplus.
- **Binning as implicit noise.** T = bin(h) ≈ h + ε with fixed-variance ε (§2, citing Laughlin 1981).
- **Net-input binning.** Bin edges f(linspace(...)), evenly spaced before the nonlinearity (App. C).
- **Gradient SNR.** m_l/s_l over training samples; its "drift" (high) and "diffusion" (low) phases.
- **Task-relevant / task-irrelevant subspaces** (§5).

## Connections

- **[LIT-324](../literature.d/LIT-324.md) (Shwartz-Ziv & Tishby 2017), [NOTE-298](NOTE-298.md).** This is the test of that paper. [NOTE-298](NOTE-298.md)'s C1 is refuted as a general statement: the phases depend on the nonlinearity and the binning. C3 is refuted: BGD compresses, and there is the weights-vs-inputs objection. C5 is refuted by the dissociation. C2 (the SNR transition coincides with the bend) is reinterpreted as generic: it occurs without compression and has an elementary cause. [NOTE-298](NOTE-298.md)'s point that the paper uses "two noise models" and concedes in its §2.4 that information "is insensitive to the complexity of the function" is exactly the lever Saxe et al. pull in App. C. [NOTE-298](NOTE-298.md)'s C4 (layers on the IB bound by fitted β) and C6 (depth) are untouched here.
- **[THEORY-035](../theory.d/THEORY-035.md) (rejected: generalisation by SGD-diffusion compression of I(X;T)).**
  - The draft rests only on [LIT-324](../literature.d/LIT-324.md)'s internal evidence and says this paper was not read. It is now read, and it corroborates every one of the draft's three reasons with independent experiments.
  - Reason 2 ("the measured quantity belongs to the estimator"; I(X;T) = H(T) for a deterministic network on finite equiprobable inputs) is this paper's eqs. 1–3 and App. C, with the decisive demonstration that re-binning one tanh run erases its compression (Fig. 14). The draft labels this "this document's inference, not the paper's"; it can now cite Saxe et al. for it.
  - Reason 1 ([LIT-324](../literature.d/LIT-324.md)'s own 5%-data result) is paralleled by Fig. 4C–D: tanh with 30% of the data compresses and overfits.
  - The draft's promote_when asks for compression "measured with a noise model that belongs to the network" that "survive[s] a change of estimator". This paper shows the tanh effect does not survive a change of binning, and that no network in the IB experiments has such a noise model.
  - One caveat for the draft's "What this does not say": it keeps the gradient-SNR transition as "not spurious" and ties it to McCandlish's noise scale. Saxe et al. agree it is real but show it is generic (it occurs in a 1-1-1 linear net and under per-sample statistics with BGD) and explain it as the mean gradient vanishing near a minimum, with prior names (Murata 1998; Chee & Toulis 2017). It survives, but as a property of approaching a minimum, not as a discovery of the IB programme.
- **[LIT-345](../literature.d/LIT-345.md) (Nanda et al.), [NOTE-283](NOTE-283.md).** A contrast on what a "later phase" simplifies.
  - Nanda's cleanup phase is a measured simplification of *weights* (the sum of squared weights falls, Fourier sparsity rises) that coincides with the test-loss drop.
  - Here the tanh compression phase coincides with weight norms *rising* (App. D; Figs. 9, 10, 20), and it is a coarsening of *binned activity*, not of the function. The two "second phases" are different kinds of thing.
  - The only representational simplification this paper finds, discarding task-irrelevant input directions (§5), happens concurrently with fitting, not afterwards.
- **[LIT-341](../literature.d/LIT-341.md) (Power et al.).** No direct link. Saxe et al. do not discuss delayed generalisation.
- **Anthology of the SOTA.** Held as [ANTH-LIT-509](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-509.md) (Active; read in the anthology NOTE on it). The anthology also holds [LIT-324](../literature.d/LIT-324.md)'s counterpart as [ANTH-LIT-508](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-508.md), and a critique of the ReLU binning as [ANTH-LIT-507](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-507.md), which was not read here.

## Bearing on the record

- **For [THEORY-035](../theory.d/THEORY-035.md).** The rejection no longer needs to rest on [LIT-324](../literature.d/LIT-324.md) alone.
  - Claim (i), the two phases, holds only for double-saturating units under a particular binning. It is refuted as a general property of deep learning, while the tanh observation itself is replicated.
  - Claim (ii), compression causes generalisation, is refuted by the dissociation (Figs. 1, 3, 4).
  - Claim (iii), SGD noise drives compression, is refuted by BGD compressing as much (Fig. 5) and by the across-runs vs within-run objection (§4).
  - The draft's source list can add this paper, and its "What was actually shown" reason 2 can be attributed rather than inferred.
- **On the phase question.** The phase structure this paper establishes is twofold.
  - *In the gradients:* a high-SNR phase then a low-SNR phase, in every setting tried, measured by per-layer gradient mean/STD norms over samples.
  - *In the information plane:* an I(X;T) rise-then-fall only for tanh-like units, measured by binning/KDE/Kraskov with imposed noise.
  - The later phase is a *saturation* of tanh units as weights grow, which the estimator reads as lower entropy. It is not a simplification of weights (norms grow), not shown to be a simplification of the function, and not IB compression in any sense a network could have.
  - The one genuine representational simplification (§5) is subspace-specific and concurrent with fitting.
- **ML practice.** Held by the anthology for that. The practical content is methodological: do not read information-plane plots of deterministic networks without the noise model, and not across architectures.

## Limitations

- **Small settings.** The SZT 12-bit task, one MNIST MLP (one run for KDE), and linear networks. No convolutional or transformer networks, and no modern training recipes (Adam, weight decay, normalisation).
- **The linear results carry the noise assumption they criticise.** The analysis noise σ²_MI = 1.0 is fixed and arbitrary. Eq. 21 shows the linear MI depends on per-layer scale. The "no compression" in linear nets is therefore measured with the same kind of instrument, though no binning artefact of the tanh kind can arise there.
- **Isotropic inputs.** The linear analysis uses isotropic inputs and independent teacher weights. The authors name the anisotropic case, where signal sits in high-variance directions, as uninvestigated.
- **ReLU binning.** The ReLU binning uses one global range over all units and epochs. Its resolution in early layers is contestable (the anthology holds a critique as [ANTH-LIT-507](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-507.md); not read here). The KDE and Kraskov results do not depend on it.
- **Dissociation demonstrated, not quantified.** Four cells, each from one small setting. Nothing measures how often compression and generalisation co-occur.
- **Untested IB claims.** [LIT-324](../literature.d/LIT-324.md)'s IB-bound claim (converged layers near the IB curve) and its depth claim are not tested.
- **Minor.** Fig. 4C's "(N = 8)" is not explained. The ICLR PDF read is a ResearchGate export; the JSTAT PDF is the IOP version of record hosted by a co-author.

## Open questions

- With anisotropic inputs, where signal occupies the high-variance directions, does a linear network show a compression-like phase in total I(X;T)? The authors flag this and leave it open. It is the one route by which "compression" could come from the data rather than the instrument.
- Is there a network-intrinsic noise model, such as stochastic units, dropout at test time or finite precision, under which a compression phase is well defined and still tracks generalisation? The paper points to explicitly stochastic IB-regularised networks as where the principle may still pay.
- Does the gradient-SNR transition coincide with McCandlish's B_simple crossing the batch size? That is [NOTE-298](NOTE-298.md)'s open question, and this paper's per-sample SNR definition makes it testable in the 1-1-1 linear model where everything is exact.

## Corrections to the seeded skim

- There was no nucleation seed or dossier. Corrections to the anthology's [ANTH-LIT-509](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-509.md) and its NOTE (anthology [NOTE-253](NOTE-253.md), the reading of [ANTH-LIT-509](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-509.md)), reported per nucleation [ADR-013](../decisions.d/ADR-013.md) and not fixed:
- **"No open route to it exists" ([ANTH-LIT-509](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-509.md) Standing; the anthology NOTE on [ANTH-LIT-509](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-509.md) summary) is wrong.** Co-author Kolchinsky's publications page links PDFs of both the ICLR 2018 paper and the JSTAT 2019 version of record. OpenReview does 403, as the anthology says.
- **`published: '2018-04-30'`** is the first day of the ICLR 2018 conference, not the paper's first appearance. Semantic Scholar gives 2018-02-15 for the ICLR record; the anonymous OpenReview submission is earlier still (unverified).
- **"Confirmed by three independent MI estimators" ([ANTH-LIT-509](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-509.md); the anthology NOTE on [ANTH-LIT-509](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-509.md) C1) overstates two of them.** The Kraskov estimator is used only for the layer entropy H(T), not I(X;T) or I(T;Y), and only on the SZT task (App. B.3; valid as I(X;T) up to a constant only under homoscedastic noise, eqs. 13–15). The MNIST KDE result is "a single training run" "because of computational expense" (App. B.1). Softsign and softplus are shown only with KDE (Fig. 8C–D). The qualitative agreement holds; "independent confirmation" is thinner than stated.
- **The anthology NOTE on [ANTH-LIT-509](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-509.md) says the linear setting computes MI "in closed form with no binning at all", and C3 cites "exact MI in the linear cases".** No binning, but not noise-free: the linear results impose Gaussian noise σ²_MI = 1.0 on each hidden layer for analysis (§3, eq. 6), which the paper stresses is not present in training or testing. The JSTAT version says "we exactly compute mutual information given the noise assumption". So the linear panels are subject to C2's own objection (the reparametrisation example, eq. 21, is in exactly this setting).
- **The full-machine-precision result (Fig. 15) is not flat everywhere.** The anthology NOTE on [ANTH-LIT-509](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-509.md) says information is "pinned at log₂(P) = 12 and barely moves"; the caption adds that the highest, smallest tanh layers do compress "near the very end of training, when the saturation of tanh is strong enough to saturate machine precision".
- **The paper explains the gradient-SNR transition, which the anthology NOTE on [ANTH-LIT-509](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-509.md) omits.** App. I: weights start small, so early gradients agree (high mean); near a minimum the mean gradient "by definition goes to zero" while per-example spread stays finite. It also names prior descriptions of the same two phases (Murata 1998, "transient and stochastic"; Chee & Toulis 2017, "search and convergence"). The SNR here is computed over all training samples, not minibatches, and is shown for BGD as well (Fig. 21D).
- **JSTAT differs from ICLR in framing, not results**, which [ANTH-LIT-509](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-509.md)'s "slightly expanded" undersells a little: the abstract adds that the claims "instead reflect assumptions made to compute a finite mutual information metric in deterministic networks"; §1 and §6 add that the binning/noise assumption "is a distinct question from that of the method used to estimate mutual information", so the results "do not simply reflect the need for more accurate MI estimation"; §6 softens ICLR's "ReLUs do not compress in general" to "do not always compress" and concedes binned MI "could still provide a useful metric that connects to generalization"; Fig. 1D (MNIST ReLU) is described separately. No new experiment was found.
- Everything else in the anthology NOTE on [ANTH-LIT-509](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-509.md) matches the text, including the minimal-model numbers, the four-cell dissociation with its figure numbers, the BGD result, the weight-distribution-vs-H(X|T) objection and the §5 task-irrelevant subspace concession.
