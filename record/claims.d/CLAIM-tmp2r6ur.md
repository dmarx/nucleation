---
status: Proposed
title: "The most informative signal in a learned spectrum lies in a truncated band: the top directions carry common, weakly discriminating structure, as stop words do in a corpus, the extreme bottom carries low-signal outliers, as rare words do, and once both are cut, the bottom of the retained band holds the most discriminating directions"
version: 2
history:
- version: 2
  date: '2026-11-22'
  note: >-
    Dated notes added from the readings of Stringer and colleagues
    (LIT-2972), Dandi and colleagues (LIT-2983) and Park and colleagues
    (LIT-2990), and two rival readings filed in the assistant's voice,
    each against one part of the claim (CLAIM-tmp9atj9, CLAIM-tmpufbx6).
    The owner's wording, the claim and its status are unchanged.
role: thesis
warrant: interpretive
defeated_if: >-
  A trained model whose top spectral directions are as discriminating per
  unit as its lower retained band, or whose extreme bottom, once
  separated, is as discriminating as the band above it, so that cutting
  either end removes as much signal as noise; or a showing, for the
  unembedding, that its top singular directions do not track common,
  weakly discriminating structure such as token frequency.
tags:
- representation-learning
- information-theory
- linguistics
date: '2026-11-22'
line:
- learned-structure
grounds:
- THEORY-tmpu3iio
summary: >-
  The owner's, 2026-11-22, on the U-shaped picture in Xu's reading
  ([THEORY-tmpu3iio](../theory.d/THEORY-tmpu3iio.md)): 'this connects to classic NLP pre-processing for topic modeling, e.g. where both the most common (stop words) and least common (low signal outliers) are often eliminated to distill signal in a text corpus. i.e. the most informative signal is in the truncated spectrum, and the bottom of that spectrum is often characterized by highly discriminating directions.' The analogy is to the
  preprocessing that drops the most frequent words, which discriminate
  little, and the rarest, which carry little signal, so that what is
  left distils the corpus's signal. Spectrally, the top directions carry
  common structure, the extreme bottom carries low-signal outliers, and
  the bottom of the retained band holds the most discriminating
  directions. Xu's Qwen comparison supports the truncation half
  ([ARG-tmpabk16](../arguments.d/ARG-tmpabk16.md)): excluding the near-zero directions roughly doubles the
  bottom band's discriminating effect. The stop-word half, that the top
  directions track token frequency, is untested ([LEAD-tmptgrc7](../leads.d/LEAD-tmptgrc7.md)). The idea
  is the owner's; the evidence relayed is the assistant's (Claude, in this
  session).
---
<!-- inactive-ok-file: THEORY-tmpwtoad THEORY-tmpcij35 THEORY-tmphbp5a CLAIM-tmp9atj9 CLAIM-tmpufbx6 ARG-tmpun4nl ARG-tmptvp76 — Proposed or new; the readings of 2026-11-22 and the rival readings filed from them -->
<!-- inactive-ok-file: THEORY-tmpu3iio ARG-tmpabk16 TERM-tmpf5ymd CLAIM-835 — Proposed or new; the reading, its argument, its test and the term it uses -->

# CLAIM-tmp2r6ur: The most informative signal in a learned spectrum lies in a truncated band: the top directions carry common, weakly discriminating structure, as stop words do in a corpus, the extreme bottom carries low-signal outliers, as rare words do, and once both are cut, the bottom of the retained band holds the most discriminating directions

**The owner's claim.** "this connects to classic NLP pre-processing for topic modeling, e.g. where both the most common (stop words) and least common (low signal outliers) are often eliminated to distill signal in a text corpus. i.e. the most informative signal is in the truncated spectrum, and the bottom of that spectrum is often characterized by highly discriminating directions."

**What it predicts, spectrally.**
- **The top directions** carry common structure that matters in bulk, in [TERM-tmpf5ymd](../terms.d/TERM-tmpf5ymd.md)'s sense of the bulk by weight, but discriminates little: the analogue of stop words.
- **The extreme bottom** carries low-signal outliers: the analogue of rare words.
- **Between them,** once both ends are cut, the bottom of the retained band is where the most discriminating directions lie.

**What the record holds that bears on it.**
- **Xu ([THEORY-tmpu3iio](../theory.d/THEORY-tmpu3iio.md), [NOTE-tmp454fw](../notes.d/NOTE-tmp454fw.md)).** Across ten models, the unembedding's bottom 5% band is the most discriminating per unit of logit distance: prediction change several times random, because the two leading candidate tokens differ disproportionately there ([CLAIM-835](CLAIM-835.md)). The top band costs as much total loss or more in nine of ten models, which fits common structure that matters in bulk.
- **The truncation, in Xu's own data** (App. E.1, checked against the paper's text). In the two Qwen models, "a few coordinates on which the normalization weight γ is close to zero give directions with near-zero singular values". Those directions carry 38% and 43% of the band change's squared length. With them excluded, "K is 7.7 and 8.5 times random instead of 3.5 and 4.1". The floor dilutes the signal, and below it lies the most discriminating band. [ARG-tmpabk16](../arguments.d/ARG-tmpabk16.md) argues this support.

**What is untested.** Whether the top singular directions track token frequency, as stop words would. Xu does not test it. [LEAD-tmptgrc7](../leads.d/LEAD-tmptgrc7.md) would.

The idea is the owner's; the evidence relayed is the assistant's (Claude, in this session).

## Note of 2026-11-22: Stringer and colleagues, read

Stringer and colleagues (LIT-2972, NOTE-tmp923nm, THEORY-tmpwtoad), mouse
V1: **a parallel, partly in tension.** Parallel: the top components carry
coarse, broadly shared structure ("Dimensions 1-2 reveal a coarse,
1-dimensional organization") and "Successive PC dimensions encode finer
stimulus features", which fits "top = common, lower = discriminating".
Tension: Stringer has no low-signal floor in the model. Below about half
the number of stimuli the cross-validated eigenvalues fall to zero because
"the remaining eigenvectors correspond to or are corrupted by additive
noise"; that is the estimator's noise floor, which cross-validation removes
rather than locates. And Stringer's reason the fine end carries little
variance is different from the owner's: more variance there would make
the code non-smooth and impair generalization, not that those directions
are noise. A neuroscience and kernel analogue, not evidence about
unembeddings. Filed from it, as an alternative to the claim's second and
third parts: CLAIM-tmpufbx6 (ARG-tmptvp76).

## Note of 2026-11-22: Dandi and colleagues, read

Dandi and colleagues (LIT-2983, NOTE-tmpdac0o, THEORY-tmpcij35): **leaves
the claim open, with a contrast.** After one large step the feature
covariance's top outliers come from the features' means, common structure
in one sense, but those means are functions of the target projection and
carry the gain in test error: the top directions carry task signal, not
stop-word-like structure. The paper measures no per-direction
discrimination and has no floor analogue. A contrast, so no relation.

## Note of 2026-11-22: Park and colleagues, read

Park and colleagues (LIT-2990, NOTE-tmpzethm, THEORY-tmphbp5a): **a
parallel that qualifies the stop-word half for a different object.** In
first-layer weights of ReLU MLPs on UTKFace, the leading learned direction
overlaps the data's first principal component at 0.681 and 0.642 in the
large-step regimes, which converge to a worse minimum, and at 0.056 in the
well-trained ferromagnetic phase, whose leading modes "capture nontrivial
structure in the data that deviates from the principal components". So
"the top directions carry common structure" is regime-dependent there. It
is a first layer, not an unembedding, and it neither confirms nor defeats
the claim. Filed from it, as an alternative to the claim's first part:
CLAIM-tmp9atj9 (ARG-tmpun4nl). LEAD-tmptgrc7 now records training regime
and stage.

## Alternatives on file

Two rival readings in the assistant's voice, each marked as an alternative
to part of this claim; the owner chooses.

- **(a) CLAIM-tmp9atj9**, against the first part (the stop-word half): top
  directions tracking common high-variance structure may mark under-trained
  or large-step regimes that learning reorganizes away from.
- **(b) CLAIM-tmpufbx6**, against the second and third parts (the floor
  and the band): the fine end may be damped for smoothness, and the
  measured floor may be estimator noise rather than low-signal outliers
  bounding a band.
