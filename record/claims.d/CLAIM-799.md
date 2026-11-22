---
number: 799
status: Proposed
formerly:
- CLAIM-tmp5y856
title: 'Geometric separation, decodability and spectral detectability are distinct qualities of a learned representation that need not agree: a semantic direction can be decodable while related points are almost orthogonal, and a covariance spike yields a PCA outlier only above the BBP threshold √(D/N), which marks when that estimator can see the signal, not when the network acquired it'
version: 3
history:
- version: 2
  date: '2026-11-22'
  note: >-
    After the readings of LIT-2983 (NOTE-tmpdac0o, THEORY-tmpcij35) and
    LIT-2990 (NOTE-tmpzethm, THEORY-tmphbp5a). The sentence saying the
    ledger could not verify the 2026 preprint's identifier is removed: the
    arXiv API confirms 2606.28486 and its authors. Two qualifications are
    added in place: learned structure can show spectrally as a reshaped
    bulk, not only as an outlier crossing a threshold (Dandi and
    colleagues); and the signal is in the weights before the outlier
    appears (Park and colleagues). The two LITs are replaced in the
    grounds by their readings (ARG-tmp2mzk1, ARG-tmps8aog). The thesis and
    status are unchanged.
- version: 3
  date: '2026-11-22'
  note: >-
    After the reading of LIT-2984 (NOTE-tmpa8a45, THEORY-tmp9ltxi). Wang,
    Wu and Fan's trained two-layer network is added in place as a third
    case of signal before outlier, with a caveat: it shows the separation
    on the spectral side only. The sentence calling the work unread is
    updated, and LIT-2984 is replaced in the grounds by its reading
    (ARG-tmppbt1o). The thesis and status are unchanged.
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
- QUESTION-515
grounds:
- CASE-301
- THEORY-tmp9ltxi
- THEORY-tmpcij35
- THEORY-tmphbp5a
- THEORY-2149
- THEORY-2153
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
<!-- inactive-ok-file: THEORY-tmpcij35 THEORY-tmphbp5a ARG-tmp2mzk1 ARG-tmps8aog CLAIM-837 TERM-tmpf5ymd LIT-tmp4kae5 LIT-tmph5ano LIT-tmp810d2 — Proposed, Deferred or new; the readings of 2026-11-22, their arguments and the works registered from them -->
<!-- inactive-ok-file: THEORY-2148 THEORY-2149 THEORY-2153 THEORY-2152 ARG-145 ARG-151 ARG-143 — Proposed; the readings and arguments of 2026-11-21 -->
<!-- inactive-ok-file: CASE-301 CLAIM-827 CLAIM-804 THEORY-078 — new and Proposed, filed from the exchange "Rich Get Richer Power Laws" on 2026-11-21; Deferred works registered from that exchange and not read; Proposed entries the record already held, cited for context -->
<!-- inactive-ok-file: ARG-tmppbt1o THEORY-tmp9ltxi — Proposed, Deferred or new; the readings of 2026-11-22 (Wang, Wu and Fan; Yang, Steinhardt and Hu; Ansuini and colleagues; Cai and colleagues; Martínez-Sánchez and colleagues), their arguments, and the entries they bear on -->

# CLAIM-799: Geometric separation, decodability and spectral detectability are distinct qualities of a learned representation that need not agree: a semantic direction can be decodable while related points are almost orthogonal, and a covariance spike yields a PCA outlier only above the BBP threshold √(D/N), which marks when that estimator can see the signal, not when the network acquired it

## The claim

A32 opens by separating "two distinct kinds of organization": **geometric
concentration** ("high-dimensional probability concentrates embeddings onto a
typical radial or angular region", which "can happen without learning") and
**spectral differentiation** ("learning creates collective directions that
become distinguishable from the random background").

For a spiked covariance Σ = I + βvvᵀ estimated from N samples at γ = D/N, the
top sample eigenvalue separates from the Marchenko–Pastur bulk only for
β > β_c = √γ, opening as (β − √γ)²/β, and only then does its eigenvector
carry information about v (the BBP transition, [LIT-2986](../literature.d/LIT-2986.md), read 2026-11-21:
the eigenvalue for complex data; the real case is Baik and Silverstein's,
[LIT-2988](../literature.d/LIT-2988.md), and the eigenvector clause Paul's, [LIT-3006](../literature.d/LIT-3006.md); see the note
of 2026-11-21 below).
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
clustering, and learning." [CASE-301](../cases.d/CASE-301.md) is the construction in which all three
differ. A32 §7 adds a fourth onset, global angular order, and concludes
that "the onset of global order, the onset of semantic information, and the
onset of spectral detectability are three distinct phenomena"; the
assistant's [CLAIM-827](CLAIM-827.md) sets them on one scale.

A32 §6 cites work tying learned features to spiked random-matrix models
(Wang, Wu and Fan, [LIT-2984](../literature.d/LIT-2984.md); Dandi and colleagues, [LIT-2983](../literature.d/LIT-2983.md); a 2026
preprint on spectral phase transitions in training, [LIT-2990](../literature.d/LIT-2990.md)): "the
spectral perspective is not merely an analogy. But they don't establish that
DNN representations generally behave as active matter, or that their learning
dynamics are critical." All three were read on 2026-11-22 (Wang, Wu and
Fan as [THEORY-tmp9ltxi](../theory.d/THEORY-tmp9ltxi.md); [THEORY-tmpcij35](../theory.d/THEORY-tmpcij35.md), [THEORY-tmphbp5a](../theory.d/THEORY-tmphbp5a.md)), and the arXiv API confirms the 2026
preprint as 2606.28486, by Park, Bocchi, D'Amico, Lucini and Aarts.

**Two qualifications** (added 2026-11-22, version 2):

- **Spectral detectability is not the only spectral signature.** After one
  maximal-update step, Dandi and colleagues find learning in the feature
  covariance chiefly as a reshaped bulk, "a wider support and longer
  tails", beside outliers from the feature means ([THEORY-tmpcij35](../theory.d/THEORY-tmpcij35.md),
  [ARG-tmp2mzk1](../arguments.d/ARG-tmp2mzk1.md)). So "spectral detectability" in the table means an outlier
  separating from the bulk; a direction below that threshold may still
  leave a mark on the bulk's shape (the bulk by count, [TERM-tmpf5ymd](../terms.d/TERM-tmpf5ymd.md)).
- **The signal is in the weights before the outlier.** In Park and
  colleagues' solvable teacher–student model the teacher is in the weights
  from the first step and the student converges for every step size below
  one, while the weight spectrum's outlier appears only at a critical time
  ([THEORY-tmphbp5a](../theory.d/THEORY-tmphbp5a.md), [ARG-tmps8aog](../arguments.d/ARG-tmps8aog.md)): a second instance of this claim's
  separation, with the weight matrix's own spectrum as the estimator.

**A third case** (added 2026-11-22, version 3):

- **Two thresholds in series.** In Wang, Wu and Fan's two-layer network
  after a few gradient steps, the rank-one weight update exists for any
  step size η > 0; the weights' top singular value separates from the bulk
  only if θ1 > γ0^(1/4) (Proposition 35); and the test-data conjugate
  kernel's outlier needs, in addition, z′(−1/λ1) > 0 (Theorem 5)
  ([THEORY-tmp9ltxi](../theory.d/THEORY-tmp9ltxi.md), [ARG-tmppbt1o](../arguments.d/ARG-tmppbt1o.md)). At random weights, depth adds a BBP-type
  test per layer. The caveat: the paper proves the spectral side only. Its
  "the input signal diminishes as the depth of the NN increases" is about
  outliers and their alignment, not about decodability; what an absorbed
  spike leaves for a readout is not studied.

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
  amount of training data; see [CLAIM-804](CLAIM-804.md).

## Note of 2026-11-21: Baik, Ben Arous and Péché, read

The BBP paper ([LIT-2986](../literature.d/LIT-2986.md)) was read ([NOTE-2241](../notes.d/NOTE-2241.md); the reading is
[THEORY-2148](../theory.d/THEORY-2148.md)), with three works beside it. It **supports the threshold**
and **qualifies the attribution**.

- **Supported.** Corollary 1.1 gives the threshold β > √γ and the outlier
  (1 + β)(1 + γ/β) in this claim's notation (γ_BBP⁻¹ = √γ, ℓ = 1 + β); the
  opening (β − √γ)²/β is (1 + β)(1 + γ/β) − (1 + √γ)² by algebra. BBP's
  "phase transition" is a change in the law of the top eigenvalue, from
  Tracy–Widom fluctuations of order M^(−2/3) to Gaussian-type ones of
  order M^(−1/2): a transition of an estimator, which fits A32's
  "spectral detectability transition, not automatically a thermodynamic or
  dynamical critical point".
- **Re-attributed.** BBP proves it for complex Gaussian samples, with at
  least as many samples as variables, and only for the largest
  eigenvalue; the real case is its "Conjecture". For real data, this
  claim's setting, the threshold and location are Baik and Silverstein's
  ([LIT-2988](../literature.d/LIT-2988.md), [THEORY-2149](../theory.d/THEORY-2149.md)). "Only then does its eigenvector carry
  information about v" and the overlap are Paul's Theorem 4
  ([LIT-3006](../literature.d/LIT-3006.md), [THEORY-2153](../theory.d/THEORY-2153.md)), with Benaych-Georges and Nadakuditi's
  (10) for the additive model ([LIT-2964](../literature.d/LIT-2964.md), [THEORY-2152](../theory.d/THEORY-2152.md)).

[LIT-2986](../literature.d/LIT-2986.md) leaves `grounds` ([ARG-145](../arguments.d/ARG-145.md)), and [THEORY-2149](../theory.d/THEORY-2149.md) and
[THEORY-2153](../theory.d/THEORY-2153.md) join it ([ARG-151](../arguments.d/ARG-151.md), [ARG-143](../arguments.d/ARG-143.md)); [THEORY-2148](../theory.d/THEORY-2148.md) and
[THEORY-2152](../theory.d/THEORY-2152.md) corroborate. The claim's content is unchanged.

## Note of 2026-11-22: Dandi and colleagues, read

Dandi, Pesce, Cui, Krzakala, Lu and Loureiro ([LIT-2983](../literature.d/LIT-2983.md)) were read
([NOTE-tmpdac0o](../notes.d/NOTE-tmpdac0o.md); the reading is [THEORY-tmpcij35](../theory.d/THEORY-tmpcij35.md)). **Supports A32 §6's narrow
point and qualifies the claim** ([ARG-tmp2mzk1](../arguments.d/ARG-tmp2mzk1.md)). Lemma 3.1 proves, for one
maximal-update step on Gaussian single-index data, that "the hidden layer
weights after one GD step are approximately low rank", W¹ ≈ W⁰ + u(w⋆)ᵀ: the
spiked picture is a theorem there, not an analogy. The spike is in the
weights; in the features the headline is a bulk "modified from the
unspiked RF spectrum", with Θ(d) outliers "arising from the means", and the
test error depends on the whole deterministic equivalent. The paper has no
BBP threshold or detectability transition, and its outliers are far above
any. It says nothing of active matter or criticality, which fits A32's
"don't establish". Moniri and colleagues' finitely many spikes beside an
unchanged bulk at smaller steps ([LIT-tmp4kae5](../literature.d/LIT-tmp4kae5.md), registered) are the regime
in which this claim's outlier picture is closest to the whole story.

## Note of 2026-11-22: Park and colleagues, read

Park, Bocchi, D'Amico, Lucini and Aarts ([LIT-2990](../literature.d/LIT-2990.md)) were read
([NOTE-tmpzethm](../notes.d/NOTE-tmpzethm.md); the reading is [THEORY-tmphbp5a](../theory.d/THEORY-tmphbp5a.md)). **Supports, from inside
the work, and shows the conflation the claim warns against**
([ARG-tmps8aog](../arguments.d/ARG-tmps8aog.md)). In the linear model W(t) = (1−ε)^t W(0) + (1−(1−ε)^t)W*, "the
optimisation always converges to the correct ground state", yet the
outlier appears only at t_c: "the signal existed below the threshold". The
paper nonetheless says "the emergence of informative representations is
then realised by isolated eigenvalues detaching from the random spectral
bulk", reading the spectral event as the learning event; by its own caveat
the boundary εc "is associated with a spectral phase transition" and εo "is
an optimisation threshold". On "critical": the outlook speaks of "the
notion of criticality arising during optimisation itself", but what is
shown is a BBP threshold, and "the precise universality class of the
transition in practical deep learning systems remains unclear", so A32's
"don't establish ... critical" is fair in the thermodynamic sense. Prior
work it cites on the same event is registered: Coeurdoux, Ferré and
Bouchaud's transient BBP ([LIT-tmph5ano](../literature.d/LIT-tmph5ano.md)) and Ben Arous and colleagues'
spectral alignment of SGD ([LIT-tmp810d2](../literature.d/LIT-tmp810d2.md)). [CLAIM-837](CLAIM-837.md) makes the parallel
point for sample PCA.

## Note of 2026-11-22: Wang, Wu and Fan, read

Wang, Wu and Fan ([LIT-2984](../literature.d/LIT-2984.md)) were read ([NOTE-tmpa8a45](../notes.d/NOTE-tmpa8a45.md); the reading is
[THEORY-tmp9ltxi](../theory.d/THEORY-tmp9ltxi.md)). **Supports, a third case of signal before outlier, on
the spectral side only** ([ARG-tmppbt1o](../arguments.d/ARG-tmppbt1o.md); the change of version 3 above).
A32 §6's "the spectral perspective is not merely an analogy" is fair for
this paper: Theorem 5 proves a label-aligned outlier in the test-data
kernel of trained weights. Its "phase transition" is the BBP outlier
criterion, applied layer by layer: spikes failing it "are absorbed into the
bulk spectrum". Nothing on active matter, criticality, or dynamics beyond a
few steps, which fits "don't establish". Its regime, η of order one, is the
one in which learning shows as one outlier beside an unchanged bulk, the
regime the Dandi note above calls closest to this claim's outlier picture.
