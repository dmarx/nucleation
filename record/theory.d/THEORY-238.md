---
number: 238
status: Active
formerly:
- THEORY-tmpxydgv
title: "The expected generalization error of an encoder–decoder learner is bounded by the encoder alone, through the KL divergence of its train-and-ghost latents to a prior symmetric under label-preserving permutations, for any decoder; and under lossy compression the bound can stay finite for deterministic continuous encoders, whose lossless bound is infinite"
version: 3
history:
- version: 2
  date: '2026-10-14'
  note: >-
    LIT-240 is now Unavailable, not Deferred (its status change of
    2026-10-14, under ADR-041); the inactive-ok comment says so. Nothing
    else changed.
- version: 3
  date: '2026-10-19'
  note: >-
    Narrowed and promoted, carrying out the promotion audit's decision
    for THEORY-238 (batch 038, ADR-047 v2). The promote_when asked first
    for a check of the constant in Theorem 4's proof, which applies
    Lemma 3 under λ/n < 1.36 against the lemma's λ/n < 0.68. The proof
    applies the lemma at λ/2, so the two conditions agree; the closing
    steps of the proof and Lemma 3's own proof were re-derived step by
    step, in the dated note below, and the constants stand. Its second
    request, a numerical evaluation showing whether the bound is
    non-vacuous, concerns whether the quantity accounts for
    generalization in practice, which this account does not claim; it
    moves to QUESTION-tmpc9vuq. The last clause is narrowed: lossy
    compression can keep the bound finite for deterministic continuous
    encoders, as the paper's constructed example shows, not in general.
tags:
- learning-theory
- information-theory
- representation-learning
date: '2026-10-14'
source:
- LIT-245
summary: >-
  Sefidgaran, Zaidi & Krasnowski (2023), [LIT-245](../literature.d/LIT-245.md), read in [NOTE-742](../notes.d/NOTE-742.md).
  Theorem 4: E[gen] ≤ inf 2√((2·MDL + K + 2)/n) + ε, where MDL is the
  expected KL of the joint law of the latents of the training set and an
  independent ghost set to any prior invariant under label-preserving
  permutations, and ε is the distortion allowed by lossy compression. It
  holds for any decoder. With a product prior it reduces to sample-wise
  mutual information. The bound is never evaluated, the prior may depend on
  unseen ghost data, and a 2√((K+2)/n) floor remains. It does not prove that
  I(X;U) cannot bound generalization.
---
<!-- inactive-ok-file: THEORY-035 LIT-240 — Rejected or Unavailable; the account this one sits beside, and the IB bound it argues against, cited for context -->

# THEORY-238: The expected generalization error of an encoder–decoder learner is bounded by the encoder alone, through the KL divergence of its train-and-ghost latents to a prior symmetric under label-preserving permutations, for any decoder; and under lossy compression the bound can stay finite for deterministic continuous encoders, whose lossless bound is infinite

## Source

Sefidgaran, Zaidi & Krasnowski (2023), [LIT-245](../literature.d/LIT-245.md), read in [NOTE-742](../notes.d/NOTE-742.md):
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

## Note of 2026-10-19: the constant in Theorem 4, re-derived

[NOTE-742](../notes.d/NOTE-742.md) flagged that the proof of Theorem 4 (App. E.5) applies Lemma 3
"conditioned that λ/n < 1.36", while the lemma is stated for λ/n < 0.68.
Re-read from the arXiv v1 text (pp. 32–38), the proof applies the lemma
to E[exp((λ/2)‖p̂_S − p̂_S′‖₁)], that is at λ/2, so its condition is
(λ/2)/n < 0.68. There is no inconsistency.

**The closing steps of E.5.** Donsker–Varadhan against the law that draws
the 2n latents from the prior Q gives λ·E[gen] ≤ B + log E_R[e^f]. The
decoder kernel is shared by both laws, so only the latents' KL enters, and
no property of the decoder is used. Under Q's label-preserving symmetry,
match the T = n − (n/2)‖p̂_S − p̂_S′‖₁ pairs of equal label across S and S′
and give each matched term an independent random sign. Each matched term
contributes cosh(λ/n) ≤ e^{λ²/(2n²)}, and each of the n − T unmatched
terms at most e^{λ/n}. So E_R[e^f] ≤ e^{λ²/(2n)} E[exp((λ/2)‖p̂_S −
p̂_S′‖₁)]. Lemma 3 at λ/2 bounds the logarithm of the last factor by
(K+2)/2 + 3λ²/(2n), for λ/n < 1.36. Hence E[gen] ≤ (2B+K+2)/(2λ) + 2λ/n,
minimised at λ* = √(n(2B+K+2))/2 with value 2√((2B+K+2)/n). When λ*/n ≥
1.36, that value is 4λ*/n > 1 and the bound holds trivially.

**Lemma 3 (App. E.9).** Poissonize the label counts as Devroye does, with
N, N′ ~ Poisson(n). Then the triangle inequality and Cauchy–Schwarz split
the moment into one for |N − n| + |N′ − n| and one for Σ_k |V_k − V′_k|,
each at t = 2λ/n. The first is at most 4e^{2n(e^t − 1 − t)} and the second
at most 2^K e^{n(e^t + e^{−t} − 2)}. With e^t ≤ 1 + t + t²/1.2 and
cosh t ≤ 1 + 7t²/12, the logarithm is at most (K+2)/2 + (17/3)λ²/n ≤
(K+2)/2 + 6λ²/n. Both inequalities were checked numerically on (0, 1.36],
where they hold, with margins 0.005 and 0.0025 at the endpoint. t < 1.36 is
the lemma's λ/n < 0.68. The paper states the second inequality only for
t < 1.3, a narrower range than the lemma uses. The numerical check covers
the rest.

