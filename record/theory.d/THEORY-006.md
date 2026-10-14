---
number: 6
status: Active
formerly:
- THEORY-tmpl293u
title: 'InfoNCE is a lower bound on mutual information for every critic and can never exceed the log of the batch size'
version: 4
history:
- version: 2
  date: '2026-10-14'
  note: >-
    Poole et al. (LIT-246) read closely (NOTE-739). The §2.3 proof
    (Eqs. 8–10) and its assumption that the negatives are drawn
    independently from the marginal are confirmed, which is what
    promote_when named, so the status moved from Proposed to Active and
    promote_when is removed. Eq. 10 is printed with its indices transposed
    relative to the derivation; this is now said. "The optimal critic does
    not depend on K" is now attributed as stated on Ma & Collins's
    authority, not proved. The caveat on in-batch negatives misread Eq. 10,
    whose expectation over K i.i.d. pairs is the in-batch construction. It
    now names what is uncovered: non-i.i.d. batches (Tschannen et al.,
    LIT-247, App. D, read in NOTE-749) and two-sided losses with
    same-view negatives. From NOTE-749, Tschannen et al.'s first
    experiment is restated (the estimate rises while the true MI is
    constant), and "tighter bounds can give worse representations" is
    limited to I_NWJ with an MLP critic. From NOTE-754, CEB's CatGen
    is noted to take its negatives from the same minibatch. Stale
    inactive-ok comments for LIT-246 and LIT-247 removed.
- version: 3
  date: '2026-10-14'
  note: >-
    A Connections section added for two accounts filed today:
    THEORY-237, the family of critic-based MI bounds from Poole et
    al. (LIT-246) of which this bound is the InfoNCE member, and
    THEORY-227, Tschannen et al.'s (LIT-247) estimator-free point
    that the true MI does not fix representation quality.
- version: 4
  date: '2026-10-14'
  note: >-
    After the close reading of LIT-256 (NOTE-tmp8mfe9). "Tight exactly at"
    is qualified: the paper says "whenever", "exactly" is the converse
    inference, and the supremum is attained only under mutual absolute
    continuity. The Deferred comment on LIT-256 removed.
tags:
- information-theory
- representation-learning
date: '2026-09-26'
source:
- LIT-246
- LIT-247
- LIT-256
- LIT-226
summary: >-
  Poole et al. (2019), [LIT-246](../literature.d/LIT-246.md), §2.3, Eqs. 8–10 — an exact proof (CPC's
  own derivation, [ANTH-LIT-589](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-589.md), passes through an approximation). Tschannen et
  al. ([LIT-247](../literature.d/LIT-247.md)) show that tightening the bound does not explain what
  makes the representations good.
answers:
- QUESTION-052
---
<!-- inactive-ok-file: THEORY-237 THEORY-227 — Proposed; the accounts filed from LIT-246 and LIT-247, named in Connections and not leaned on -->

# THEORY-006: InfoNCE is a lower bound on mutual information for every critic and can never exceed the log of the batch size

## Source

Poole et al. (2019), [LIT-246](../literature.d/LIT-246.md), §2.3, Eqs. 8–10. Supporting: Belghazi et al. (2018), [LIT-256](../literature.d/LIT-256.md), Eqs. 1, 3–4 and App. 8.2.1 (mutual information as E[log dP_XZ/d(P_X⊗P_Z)], and the Donsker–Varadhan bound tight exactly at the log Radon–Nikodym derivative plus a constant; Belghazi et al. say "whenever"; "exactly" is the converse, which follows from their Eq. 25 but is not stated, and the supremum is attained only when P_XZ and P_X⊗P_Z are mutually absolutely continuous, otherwise it is approached in the limit); Tschannen et al. (2020), [LIT-247](../literature.d/LIT-247.md); Fischer's conditional entropy bottleneck, [LIT-226](../literature.d/LIT-226.md), which relies on the bound (§6.3): its CatGen decoder is InfoNCE with the other examples of the same minibatch as negatives ([NOTE-754](../notes.d/NOTE-754.md)).

## What was actually shown

With K samples and negatives drawn independently from the marginal, I(X;Y) ≥ I_NCE for every critic, proved exactly as the multi-sample NWJ bound with the batch estimate of the partition function ([LIT-246](../literature.d/LIT-246.md) Eqs. 8–10). The expectation in Eq. 10 is over K i.i.d. pairs from the joint, with each y_i's negatives the other pairs' x_j, so the proof covers in-batch negatives drawn this way ([NOTE-739](../notes.d/NOTE-739.md)). Eq. 10 is printed with its indices transposed: the denominator sums over y_j for fixed x_i, while the derivation, Table 2 and Eq. 12 sum over x_j for fixed y_i. The printed form also holds, by symmetry, but the optimal critic's free term c(y) is right only for the derived form. By construction I_NCE ≤ log K. That the optimal critic, log p(y|x) + c(y), does not depend on K is stated in the paper on Ma & Collins's (2018) authority, not proved there. Belghazi et al. state the underlying identity: mutual information is the expected log Radon–Nikodym derivative of the joint with respect to the product of marginals, and the variational bound is tight at that log-derivative plus a constant. That it is tight exactly there is the record's converse inference, and it holds only under mutual absolute continuity ([NOTE-tmp8mfe9](../notes.d/NOTE-tmp8mfe9.md)).

Tschannen et al. show experimentally that representations can improve while the true MI does not change: with invertible encoders the true MI is constant, while the estimate and linear-probe accuracy both rise (§3.1, Fig. 1). They also show that a tighter bound can give worse representations, but for I_NWJ with an MLP critic (§3.2, Fig. 3). For I_NCE every critic saturates near log K, and the critic changes accuracy at nearly equal bound values ([NOTE-749](../notes.d/NOTE-749.md)). So the bound's value is not what the objective's success tracks.

## What this does not say

- That I_NCE approaches I(X;Y) at any stated rate as K grows (not proved in what was read).
- That maximizing I_NCE maximizes the representation's information in a useful sense (Tschannen et al. argue against this reading).
- Anything for batches whose pairs are not i.i.d. With identically distributed but dependent pairs, I_NCE is neither a lower nor an upper bound on MI (Tschannen et al., [LIT-247](../literature.d/LIT-247.md), App. D); Hénaff et al.'s CPC, with negatives from the same image, is their example.
- Anything for symmetric or two-sided losses, such as NT-Xent, that also draw negatives from the same view. Johnson et al. ([LIT-258](../literature.d/LIT-258.md)) App. B.1 treats NT-Xent with negatives drawn i.i.d. from the marginal; whether the bound extends to the two-sided loss is not checked here.

## Connections

- **[THEORY-237](THEORY-237.md)** places this bound in its family. Poole et al.
  ([LIT-246](../literature.d/LIT-246.md)) derive Donsker–Varadhan, NWJ, MINE's gradient and InfoNCE as
  relaxations of one unnormalized Barber–Agakov bound. InfoNCE is NWJ
  applied to a K-sample problem with the batch mean as normalizer, and its
  optimal critic is the log density ratio up to a function of y.
- **[THEORY-227](THEORY-227.md)** states the estimator-free point beneath Tschannen et
  al.'s experiments summarized above ([LIT-247](../literature.d/LIT-247.md)). Invertible encoders keep
  the true MI exactly, yet under a linear probe some do better than the raw
  input and some worse. So it is MI itself, not only this bound on it, that
  does not fix the quality of a representation.
