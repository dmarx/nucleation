---
status: Proposed
promote_when: >-
  A check of the constant in Theorem 4's proof, which applies Lemma 3 under
  a looser condition than the lemma states (λ/n < 1.36 against 0.68), and a
  numerical evaluation of the bound for a trained encoder with a prior
  that does not use the ghost data, showing whether it is non-vacuous. The
  first settles the theorem as stated. The second settles whether the
  quantity accounts for generalization in practice, which the account
  claims only in principle. It is refuted by a counterexample to Theorem 4,
  an encoder–decoder learner whose expected generalization error exceeds
  the bound for some type-III symmetric prior. What cannot settle it: test
  accuracies of regularizers built from the bound, such as CDVIB, since a
  better regularizer does not show that the bound holds or is tight.
title: "The expected generalization error of an encoder–decoder learner is bounded by the encoder alone, through the KL divergence of its train-and-ghost latents to a prior symmetric under label-preserving permutations, for any decoder, and the bound stays finite for deterministic continuous encoders under lossy compression"
version: 1
tags:
- learning-theory
- information-theory
- representation-learning
date: '2026-10-14'
source:
- LIT-245
summary: >-
  Sefidgaran, Zaidi & Krasnowski (2023), [LIT-245](../literature.d/LIT-245.md), read in [NOTE-tmpftody](../notes.d/NOTE-tmpftody.md).
  Theorem 4: E[gen] ≤ inf 2√((2·MDL + K + 2)/n) + ε, where MDL is the
  expected KL of the joint law of the latents of the training set and an
  independent ghost set to any prior invariant under label-preserving
  permutations, and ε is the distortion allowed by lossy compression. It
  holds for any decoder. With a product prior it reduces to sample-wise
  mutual information. The bound is never evaluated, the prior may depend on
  unseen ghost data, and a 2√((K+2)/n) floor remains. It does not prove that
  I(X;U) cannot bound generalization.
---
<!-- inactive-ok-file: THEORY-035 LIT-240 — Rejected or Deferred; the account this one sits beside, and the IB bound it argues against, cited for context -->

# THEORY-tmpxydgv: The expected generalization error of an encoder–decoder learner is bounded by the encoder alone, through the KL divergence of its train-and-ghost latents to a prior symmetric under label-preserving permutations, for any decoder, and the bound stays finite for deterministic continuous encoders under lossy compression

## Source

Sefidgaran, Zaidi & Krasnowski (2023), [LIT-245](../literature.d/LIT-245.md), read in [NOTE-tmpftody](../notes.d/NOTE-tmpftody.md):
§2 (Theorems 1–3, Eqs. 3–4), §3 (Theorem 4 and its proof, App. E.5,
Theorem 7), App. B.2 and App. C.3. Of the proofs, Theorem 4's was read;
the others were not checked.

## What was actually shown

**The setting.** K-class classification with 0–1 loss. An encoder maps X
to a latent U, and a decoder maps U to a label. A ghost set S′ of n
samples is drawn i.i.d. like the training set S, and appears only in the
analysis.

**Theorem 4.** For any prior Q on the 2n latents that is invariant under
permutations preserving the labels (type III), which may depend on
(X^{2n}, Y^{2n}) and on the compressed encoder,

E[gen(S,W)] ≤ inf 2√((2·E D_KL(P(U, U′ | X, X′, Ŵe) ‖ Q) + K + 2)/n) + ε,

with the infimum over lossy compressions Ŵe of the encoder whose
generalization error differs by at most ε. "This bound is valid for any
choice decoder". The KL term is read as the rate of a block code for the
rearranged latents, a minimum description length of the latents, not of
the parameters. Theorem 7 gives the tail form.

**Relation to mutual information.** With a product prior the KL term
becomes n times a sample-wise KL. With the marginal as prior it is n times
the empirical mutual information (Eqs. 3–4). The symmetric prior can
exploit joint structure across the 2n latents that a product prior cannot,
which is how the bound can be tighter than mutual-information bounds.

**Finiteness.** For deterministic continuous encoders I(X;U) is infinite.
The lossy form keeps the bound finite. In a constructed example
(App. C.3), U = ±1 + X/5 has I(U;X) = ∞, while a compression with
distortion below 0.05 has I(Û;X) = 1.

What could have failed: the bound needs no property of the decoder. A
decoder-dependent term would have made the encoder's compressibility
insufficient, and none appears.

## What this does not say

- **Not that the bound is small for real networks.** It is never computed.
  The experiment (one small CNN on CIFAR-10, 62–65% accuracy) tests a
  regularizer inspired by it, not the bound.
- **Not that the prior is available.** The type-III prior may depend on the
  ghost set. In practice it is approximated by moving averages, and only
  approximately symmetric for more than one Gaussian per label.
- **Not that I(X;U) cannot bound generalization.** The paper argues that
  existing I(X;U) bounds (Shamir et al., Vera et al. [LIT-240](../literature.d/LIT-240.md), Kawaguchi et
  al.) are vacuous, infinite or restricted to finite alphabets. It does not
  prove that no such bound exists.
- **Not tight in K.** A 2√((K+2)/n) floor remains however compressible the
  latents are, from label-histogram mismatch between S and S′.
- **Not Kolmogorov complexity.** "MDL" here is a Shannon coding rate under
  a prior.
- **Not advice.** Regularizing toward label-dependent learned priors is a
  training instruction and belongs in the anthology.

## Connections

- **[THEORY-035](THEORY-035.md) (Rejected).** That account said compression of I(X;T)
  during SGD explains generalization. This one names an information
  quantity that does bound generalization, and it is neither I(X;T) nor a
  compression phase. It does not revive [THEORY-035](THEORY-035.md).
- **[THEORY-028](THEORY-028.md).** The input–output bound √(2σ²·I(S;W)) concerns the whole
  learner's dependence on its sample. This bound concerns only the
  encoder's latents, and holds whatever the decoder does with them.
- **The information bottleneck.** Its I(X;U) is replaced, as a complexity
  that controls generalization, by a coding rate of the latents relative to
  a symmetric prior. The paper notes that its label-dependent priors connect
  to Fischer's conditional entropy bottleneck ([LIT-226](../literature.d/LIT-226.md)).
