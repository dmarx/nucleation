---
status: Proposed
title: 'Geometric separation, decodability and spectral detectability are distinct qualities of a learned representation that need not agree: a semantic direction can be decodable while related points are almost orthogonal, and a covariance spike yields a PCA outlier only above the BBP threshold √(D/N), which marks when that estimator can see the signal, not when the network acquired it'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A proof that in the spiked-covariance model the three qualities must
  agree, for instance that a direction decodable with fixed accuracy at
  large D must also produce a separated PCA eigenvalue at the same sample
  size, contradicting the construction in its grounds; or an error in the BBP
  formulas used. Not met by trained networks in which the three happen to
  coincide: the claim is that they need not.
tags:
- representation-learning
- mathematical-statistics
- learning-theory
date: '2026-11-21'
line:
- learned-structure
bears_on:
- QUESTION-tmpvu6cb
grounds:
- CASE-tmp59xy5
- LIT-tmpipm3o
- LIT-tmpfmeic
- LIT-tmpevgqj
- LIT-tmpk5ull
summary: >-
  A31 and A32 §1–§4, §6 and §7 of the exchange "Rich Get Richer Power
  Laws" (2026-11-21). Concentration "can happen without learning";
  spectral differentiation, a direction separating from the random bulk,
  "reflects the emergence of statistical structure", and its threshold is a
  property of the estimator and the sample. "The BBP transition is a
  spectral detectability transition, not automatically a thermodynamic or
  dynamical critical point." The wording is A's (the other assistant in
  the exchange "Rich Get Richer Power Laws", A31 and A32); adopting it is
  the owner's call.
---
<!-- inactive-ok-file: CASE-tmp59xy5 CLAIM-tmpk33au CLAIM-tmp8mvx8 LIT-tmpipm3o LIT-tmpfmeic LIT-tmpevgqj LIT-tmpk5ull THEORY-078 — new and Proposed, filed from the exchange "Rich Get Richer Power Laws" on 2026-11-21; Deferred works registered from that exchange and not read; Proposed entries the record already held, cited for context -->

# CLAIM-tmp5y856: Geometric separation, decodability and spectral detectability are distinct qualities of a learned representation that need not agree: a semantic direction can be decodable while related points are almost orthogonal, and a covariance spike yields a PCA outlier only above the BBP threshold √(D/N), which marks when that estimator can see the signal, not when the network acquired it

## The claim

A32 opens by separating "two distinct kinds of organization": **geometric
concentration** ("high-dimensional probability concentrates embeddings onto a
typical radial or angular region", which "can happen without learning") and
**spectral differentiation** ("learning creates collective directions that
become distinguishable from the random background").

For a spiked covariance Σ = I + βvvᵀ estimated from N samples at γ = D/N, the
top sample eigenvalue separates from the Marchenko–Pastur bulk only for
β > β_c = √γ, opening as (β − √γ)²/β, and only then does its eigenvector
carry information about v ([LIT-tmpipm3o](../literature.d/LIT-tmpipm3o.md), Deferred: registered, not read).
A32 §2: "This is not necessarily the moment when the network first learns
anything. The signal existed below the threshold. Rather, it is the moment
when that signal becomes detectable by this particular spectral estimator", a
distinction "between **the emergence of information** and **the emergence of
observable spectral separation**." And §3: near threshold the gap opens
quadratically and the overlap linearly, "critical-like scaling", but "it does
not by itself imply a power-law distribution of events or a diverging
physical correlation length."

Hence three qualities (A32 §4):

| property | question |
|---|---|
| geometric separation | are semantically related points obviously close? |
| decodability | can a suitable readout recover semantic information? |
| spectral detectability | can an unsupervised estimator identify the informative direction? |

"They need not agree. That's a major reason not to equate concentration,
clustering, and learning." [CASE-tmp59xy5](../cases.d/CASE-tmp59xy5.md) is the construction in which all three
differ. A32 §7 adds a fourth onset, global angular order, and concludes
that "the onset of global order, the onset of semantic information, and the
onset of spectral detectability are three distinct phenomena"; the
assistant's [CLAIM-tmpk33au](CLAIM-tmpk33au.md) sets them on one scale.

A32 §6 cites work tying learned features to spiked random-matrix models
(Wang, Wu and Fan, [LIT-tmpfmeic](../literature.d/LIT-tmpfmeic.md); Dandi and colleagues, [LIT-tmpevgqj](../literature.d/LIT-tmpevgqj.md); a 2026
preprint on spectral phase transitions in training, [LIT-tmpk5ull](../literature.d/LIT-tmpk5ull.md)): "the
spectral perspective is not merely an analogy. But they don't establish that
DNN representations generally behave as active matter, or that their learning
dynamics are critical." All three are registered and unread, and the ledger
could not verify the 2026 preprint's identifier offline.

## What the record holds

[THEORY-078](../theory.d/THEORY-078.md) (class means of a trained classifier carried by the Fisher's
eigenvalues beyond the bulk edge), [THEORY-420](../theory.d/THEORY-420.md) (a random-matrix null for
weight spectra) and [CLAIM-164](CLAIM-164.md) (a spectral gap makes a subspace definite)
are adjacent. None holds the BBP threshold or separates detectability from
decodability.

## What it does not say

- Not that learning is a phase transition, or that it is not.
- Not that a supervised learner faces the same threshold: "a supervised
  learner with labels faces a different estimation problem" (A32 §4).
- N here is the number of probe samples on which PCA is run, not the
  amount of training data; see [CLAIM-tmp8mvx8](CLAIM-tmp8mvx8.md).
