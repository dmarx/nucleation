---
number: 35
status: Rejected
formerly:
- THEORY-tmpd8w6r
status_note: Saxe et al. show the compression phase appears only for double-saturating units under an imposed binning or noise model, occurs under full-batch GD as under SGD, and dissociates from generalisation in all four combinations; the paper's own small-sample run already showed compression losing label information
promote_when: >-
  To be reinstated, the account needs a compression phase measured with a
  noise model that belongs to the network, not to the analyst. The effect
  would have to survive a change of estimator and of binning, which the tanh
  effect does not: re-binning one tanh run evenly in net input removes it
  (LIT-372, App. C). It would have to appear in networks without
  double-saturating units, and it would have to depend on gradient noise,
  since full-batch GD compresses as much as SGD (LIT-372, §4). The
  compression would also have to predict generalisation across sample
  sizes, including the small-sample regime where LIT-324's own §3.4 finds it
  doing the opposite. A fit of β per layer cannot count as evidence of
  IB-optimality, since the fit builds the agreement in. The refuters this
  document named are now met: LIT-372 shows networks that generalise
  with no fall in I(X;T) (ReLU, deep linear) and a network that compresses
  while overfitting (tanh on 30% of the data).
title: 'Deep networks generalise because the diffusion phase of SGD compresses each layer''s information about the input'
version: 2
history:
- version: 2
  date: '2026-09-30'
  note: >-
    Saxe et al. (LIT-372) filed and read (NOTE-320), and added to
    source after LIT-324. The rejection now cites their evidence first-hand
    in place of saying it was not in the record: the phases depend on
    nonlinearity and estimator, compression and generalisation dissociate,
    full-batch GD compresses as SGD does, and the drift-to-diffusion
    transition is real but generic. The step I(X;T) = H(T) for a
    deterministic network, formerly this document's own inference, is now
    attributed to Saxe et al.'s eqs. 1–3 and App. C. The status stays
    Rejected; the status note and promote_when are updated to match.
tags:
- learning-theory
- information-theory
- representation-learning
date: '2026-09-30'
source:
- LIT-324
- LIT-372
- LIT-338
summary: >-
  Shwartz-Ziv & Tishby (2017), [LIT-324](../literature.d/LIT-324.md), report a fitting phase followed by a
  long compression phase in the information plane, and read compression by
  gradient diffusion as the mechanism of generalisation. Their §3.4 reports
  that with 5% of the data compression lowers I(T;Y). Saxe et al. (2018),
  [LIT-372](../literature.d/LIT-372.md), rerun their code and find the compression phase only in
  double-saturating networks measured through an imposed binning, find it
  under full-batch GD as under SGD, and find compression and generalisation
  in all four combinations. The account is rejected. The IB functional of
  [LIT-338](../literature.d/LIT-338.md), the tanh two-phase observation and the gradient-SNR transition
  are not.
---

# THEORY-035: Deep networks generalise because the diffusion phase of SGD compresses each layer's information about the input

## Source

- Shwartz-Ziv & Tishby (2017), [LIT-324](../literature.d/LIT-324.md), §§2.3–2.4, 3.2, 3.4, 3.5 and 3.8, as read in [NOTE-298](../notes.d/NOTE-298.md). The account's origin.
- Saxe, Bansal, Dapello, Advani, Kolchinsky, Tracey & Cox (2018), [LIT-372](../literature.d/LIT-372.md), §§2–5 and Apps. B–E and I, as read in [NOTE-320](../notes.d/NOTE-320.md). The independent test.
- Tishby, Pereira & Bialek (1999), [LIT-338](../literature.d/LIT-338.md), the IB functional it applies, as read in [NOTE-300](../notes.d/NOTE-300.md).

## What was actually shown

**The account.** [LIT-324](../literature.d/LIT-324.md) trains small tanh networks on a 12-bit synthetic rule whose joint distribution is known exactly. It estimates each layer's information by binning every neuron into 30 bins (§3.2). Over training, I(T;Y) rises within a few hundred epochs, and then I(X;T) falls over thousands (§3.4). The bend coincides with a fall in per-layer gradient SNR, from drift to diffusion, at about 350 epochs (§3.5). The paper reads the diffusion phase as entropy-maximising relaxation under the training-error constraint. It then asserts that "compression by noise" explains the absence of overfitting: "we believe" (§1), "If our findings hold…" (§4). The causal chain from diffusion to compression to generalisation is deferred to "a rigorous analysis … elsewhere" ([NOTE-298](../notes.d/NOTE-298.md), C3, C5).

**Why the record rejects it.** [LIT-372](../literature.d/LIT-372.md) reruns [LIT-324](../literature.d/LIT-324.md)'s code and changes one thing at a time. Each link in the account fails as a general statement ([NOTE-320](../notes.d/NOTE-320.md), C1–C6).

1. **The phases depend on the nonlinearity and the estimator.** The tanh replication reproduces [LIT-324](../literature.d/LIT-324.md)'s fitting-then-compression paths. ReLU, softplus and linear networks do not compress, on the 12-bit task and on MNIST. That holds under binning, a KDE bound and a Kraskov entropy estimate (Figs. 1, 8, 12). Re-binning the *same* tanh run, with edges evenly spaced in net input, removes the compression in most layers (App. C, Fig. 14). The later phase is tanh units saturating as their weights grow, which a fixed-width binning reads as lower entropy (Fig. 2, App. E). Weight norms rise through it.
2. **The measured quantity belongs to the estimator.** For a deterministic network, I(h;X) is infinite, so any finite value comes from noise or binning the analyst adds (App. C, eqs. 17–20). On a finite input set with binning, I(X;T) = H(T) exactly (eqs. 1–3). "Compression" then means only that the binned activity takes fewer distinct values. The same function, reparametrised across two layers, gets a different I(T;X) (eq. 21). [LIT-324](../literature.d/LIT-324.md) itself concedes the root of this in §2.4: for deterministic maps, information "is insensitive to the complexity of the function". It also runs two unreconciled noise models, binning (§3.2) and "sigmoid outputs as probabilities" (§2.3).
3. **Compression and generalisation dissociate.** All four combinations occur (§3, Figs. 1, 3, 4). Tanh on the full task compresses and generalises. ReLU and deep linear networks generalise without compressing. A linear network overtrains without compressing. Tanh on 30% of the data compresses and overfits. That last cell matches [LIT-324](../literature.d/LIT-324.md)'s own small-sample result. With 5% of the data, compression *lowers* I(T;Y), and the paper attributes the overfitting "largely" to compression (§3.4).
4. **Gradient noise does not cause the compression.** Full-batch gradient descent gives "robust compression in tanh networks", as SGD does. It also gives the same information dynamics in ReLU and linear networks (§4, Figs. 5, 19). Saxe et al. also point out a category error in the argument. A maximum-entropy distribution over weights describes variation *across runs*, while H(X|T) is about inputs for one set of weights. "There is no general reason" one draw maximises it (§4).
5. **"Layers lie on the IB bound" is a fit.** β is chosen per layer to minimise the divergence between the layer's encoder and the IB encoder built from the layer's own decoder (eq. 12). The claim says only that some β makes each layer nearly IB-consistent ([NOTE-298](../notes.d/NOTE-298.md), C4). [LIT-372](../literature.d/LIT-372.md) does not test this claim or [LIT-324](../literature.d/LIT-324.md)'s depth claim. This point is the record's own reading of [LIT-324](../literature.d/LIT-324.md).

## What this does not say

- **That the IB method is wrong.** [LIT-338](../literature.d/LIT-338.md) poses a source-coding problem with a known p(x,y) and proves the form of its optimum (Thm 4). It says nothing about SGD, finite samples or generalisation (fn. 1). Nothing here touches it.
- **That the tanh two-phase observation is false.** With tanh units and this binning, the information paths are what [LIT-324](../literature.d/LIT-324.md) reports, consistent across 50 runs. [LIT-372](../literature.d/LIT-372.md) reproduces them with the original code. What fails is their generality and their reading.
- **That the gradient-SNR transition is spurious.** The drift-to-diffusion change is measured from gradient statistics, not from information estimates, and [LIT-372](../literature.d/LIT-372.md) confirms it. It also shows the change is generic (App. I, Figs. 9–10, 20–21). It occurs in ReLU nets, on MNIST, under full-batch GD, and in a 1-1-1 linear network that cannot compress. Its explanation is elementary: the mean gradient goes to zero near a minimum while the per-example spread stays finite. Earlier work described the same two phases (Murata 1998; Chee & Toulis 2017). It is also the precursor of McCandlish's noise scale ([LIT-348](../literature.d/LIT-348.md)), which cites [LIT-324](../literature.d/LIT-324.md). It survives this rejection as a property of approaching a minimum, not as evidence for compression.
- **That no representation discards input information.** In a linear network with task-irrelevant inputs, information about the irrelevant subspace rises and then falls, while total I(X;T) rises ([LIT-372](../literature.d/LIT-372.md), §5, Fig. 6). That happens during fitting, not in a later phase. It is measured under an imposed noise σ²_MI = 1.
- **That no information quantity bears on generalisation.** Input–output information does bound expected generalisation error ([LIT-347](../literature.d/LIT-347.md)), but that quantity is I(S;W), not I(X;T).
- **Anything beyond small settings.** [LIT-372](../literature.d/LIT-372.md) tests the 12-bit task, one MNIST MLP and linear networks. It does not test convolutional or transformer networks. Nor does it test anisotropic inputs, which its authors flag as open ([NOTE-320](../notes.d/NOTE-320.md)).

## Connections

- [LIT-226](../literature.d/LIT-226.md) (CEB) inherits the IB programme. It is Deferred, so it is named here only. [NOTE-300](../notes.d/NOTE-300.md) shows algebraically that its objective is eq. (15) of [LIT-338](../literature.d/LIT-338.md) reparametrised.
- [LIT-240](../literature.d/LIT-240.md) (Vera et al.) and [LIT-245](../literature.d/LIT-245.md) take up "the IB term controls generalisation" formally. Both are Deferred.
- None of the later phases of training reported elsewhere in the record is a measured fall in I(X;T). See [LIT-345](../literature.d/LIT-345.md) ([NOTE-283](../notes.d/NOTE-283.md)), [LIT-371](../literature.d/LIT-371.md) ([NOTE-319](../notes.d/NOTE-319.md)), [LIT-369](../literature.d/LIT-369.md) ([NOTE-317](../notes.d/NOTE-317.md)) and [LIT-370](../literature.d/LIT-370.md) ([NOTE-318](../notes.d/NOTE-318.md)).
