---
number: 854
status: Proposed
formerly:
- CLAIM-tmp2r6ur
title: 'Discrimination peaks in a truncated band'
statement: >-
  The most informative signal in a learned spectrum lies in a truncated
  band: the top directions carry common, weakly discriminating structure, as
  stop words do in a corpus, the extreme bottom carries low-signal outliers,
  as rare words do, and once both are cut, the bottom of the retained band
  holds the most discriminating directions
version: 2
history:
- version: 2
  date: '2026-11-22'
  note: >-
    Dated notes added from the readings of Stringer and colleagues
    (LIT-2972), Dandi and colleagues (LIT-2983) and Park and colleagues
    (LIT-2990), and two rival readings filed in the assistant's voice,
    each against one part of the claim (CLAIM-855, CLAIM-856).
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
- THEORY-2162
summary: >-
  The owner's, 2026-11-22, on the U-shaped picture in Xu's reading
  ([THEORY-2162](../theory.d/THEORY-2162.md)): 'this connects to classic NLP pre-processing for topic modeling, e.g. where both the most common (stop words) and least common (low signal outliers) are often eliminated to distill signal in a text corpus. i.e. the most informative signal is in the truncated spectrum, and the bottom of that spectrum is often characterized by highly discriminating directions.' The analogy is to the
  preprocessing that drops the most frequent words, which discriminate
  little, and the rarest, which carry little signal, so that what is
  left distils the corpus's signal. Spectrally, the top directions carry
  common structure, the extreme bottom carries low-signal outliers, and
  the bottom of the retained band holds the most discriminating
  directions. Xu's Qwen comparison supports the truncation half
  ([ARG-162](../arguments.d/ARG-162.md)): excluding the near-zero directions roughly doubles the
  bottom band's discriminating effect. The stop-word half, that the top
  directions track token frequency, is untested ([LEAD-212](../leads.d/LEAD-212.md)). The idea
  is the owner's; the evidence relayed is the assistant's (Claude, in this
  session).
---
<!-- inactive-ok-file: THEORY-2174 THEORY-2170 THEORY-2171 CLAIM-855 CLAIM-856 ARG-174 ARG-173 — Proposed or new; the readings of 2026-11-22 and the rival readings filed from them -->
<!-- inactive-ok-file: THEORY-2162 ARG-162 TERM-143 CLAIM-835 — Proposed or new; the reading, its argument, its test and the term it uses -->
<!-- inactive-ok-file: LIT-3047 THEORY-2185 THEORY-2186 — Proposed, Deferred or new; the readings of 2026-11-22 (Wang, Wu and Fan; Yang, Steinhardt and Hu; Ansuini and colleagues; Cai and colleagues; Martínez-Sánchez and colleagues), their arguments, and the entries they bear on -->

# CLAIM-854: Discrimination peaks in a truncated band

**The owner's claim.** "this connects to classic NLP pre-processing for topic modeling, e.g. where both the most common (stop words) and least common (low signal outliers) are often eliminated to distill signal in a text corpus. i.e. the most informative signal is in the truncated spectrum, and the bottom of that spectrum is often characterized by highly discriminating directions."

**What it predicts, spectrally.**
- **The top directions** carry common structure that matters in bulk, in [TERM-143](../terms.d/TERM-143.md)'s sense of the bulk by weight, but discriminates little: the analogue of stop words.
- **The extreme bottom** carries low-signal outliers: the analogue of rare words.
- **Between them,** once both ends are cut, the bottom of the retained band is where the most discriminating directions lie.

**What the record holds that bears on it.**
- **Xu ([THEORY-2162](../theory.d/THEORY-2162.md), [NOTE-2249](../notes.d/NOTE-2249.md)).** Across ten models, the unembedding's bottom 5% band is the most discriminating per unit of logit distance: prediction change several times random, because the two leading candidate tokens differ disproportionately there ([CLAIM-835](CLAIM-835.md)). The top band costs as much total loss or more in nine of ten models, which fits common structure that matters in bulk.
- **The truncation, in Xu's own data** (App. E.1, checked against the paper's text). In the two Qwen models, "a few coordinates on which the normalization weight γ is close to zero give directions with near-zero singular values". Those directions carry 38% and 43% of the band change's squared length. With them excluded, "K is 7.7 and 8.5 times random instead of 3.5 and 4.1". The floor dilutes the signal, and below it lies the most discriminating band. [ARG-162](../arguments.d/ARG-162.md) argues this support.

**What is untested.** Whether the top singular directions track token frequency, as stop words would. Xu does not test it. [LEAD-212](../leads.d/LEAD-212.md) would.

The idea is the owner's; the evidence relayed is the assistant's (Claude, in this session).

## Note of 2026-11-22: Stringer and colleagues, read

Stringer and colleagues ([LIT-2972](../literature.d/LIT-2972.md), [NOTE-2257](../notes.d/NOTE-2257.md), [THEORY-2174](../theory.d/THEORY-2174.md)), mouse
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
third parts: [CLAIM-856](CLAIM-856.md) ([ARG-173](../arguments.d/ARG-173.md)).

## Note of 2026-11-22: Dandi and colleagues, read

Dandi and colleagues ([LIT-2983](../literature.d/LIT-2983.md), [NOTE-2258](../notes.d/NOTE-2258.md), [THEORY-2170](../theory.d/THEORY-2170.md)): **leaves
the claim open, with a contrast.** After one large step the feature
covariance's top outliers come from the features' means, common structure
in one sense, but those means are functions of the target projection and
carry the gain in test error: the top directions carry task signal, not
stop-word-like structure. The paper measures no per-direction
discrimination and has no floor analogue. A contrast, so no relation.

## Note of 2026-11-22: Park and colleagues, read

Park and colleagues ([LIT-2990](../literature.d/LIT-2990.md), [NOTE-2260](../notes.d/NOTE-2260.md), [THEORY-2171](../theory.d/THEORY-2171.md)): **a
parallel that qualifies the stop-word half for a different object.** In
first-layer weights of ReLU MLPs on UTKFace, the leading learned direction
overlaps the data's first principal component at 0.681 and 0.642 in the
large-step regimes, which converge to a worse minimum, and at 0.056 in the
well-trained ferromagnetic phase, whose leading modes "capture nontrivial
structure in the data that deviates from the principal components". So
"the top directions carry common structure" is regime-dependent there. It
is a first layer, not an unembedding, and it neither confirms nor defeats
the claim. Filed from it, as an alternative to the claim's first part:
[CLAIM-855](CLAIM-855.md) ([ARG-174](../arguments.d/ARG-174.md)). [LEAD-212](../leads.d/LEAD-212.md) now records training regime
and stage.

## Alternatives on file

Two rival readings in the assistant's voice, each marked as an alternative
to part of this claim; the owner chooses.

- **(a) [CLAIM-855](CLAIM-855.md)**, against the first part (the stop-word half): top
  directions tracking common high-variance structure may mark under-trained
  or large-step regimes that learning reorganizes away from.
- **(b) [CLAIM-856](CLAIM-856.md)**, against the second and third parts (the floor
  and the band): the fine end may be damped for smoothness, and the
  measured floor may be estimator noise rather than low-signal outliers
  bounding a band.

## Note of 2026-11-22: Wang, Wu and Fan, read

Wang, Wu and Fan ([LIT-2984](../literature.d/LIT-2984.md), [NOTE-2274](../notes.d/NOTE-2274.md), [THEORY-2186](../theory.d/THEORY-2186.md)): **leaves the
claim open; in the paper's own settings the top outliers are the signal,
against the stop-word half.** Its conjugate-kernel outliers are inherited
from the input's spikes, which are the class labels or the target
direction, and after training the test-data kernel's top outlier is
aligned with the test labels. The paper measures no per-direction
discrimination and does not discuss the bottom of the spectrum. One
parallel that would bear on the stop-word half is only cited: for non-odd
activations the kernel can have top eigenvalues "even when the input K0
has no spiked structure", "uninformative spike eigenvalues", shown by
Benigni and Péché and assumed away here (E σ″ = 0). Those are top
directions that carry no task signal, which is the shape the stop-word
half needs. Benigni and Péché are registered ([LIT-3047](../literature.d/LIT-3047.md), Deferred) as
the reading that might test it directly, for a random one-layer kernel. A
note, no relation.

## Note of 2026-11-22: Yang, Steinhardt and Hu, read

Yang, Steinhardt and Hu ([LIT-2957](../literature.d/LIT-2957.md), [NOTE-2276](../notes.d/NOTE-2276.md), [THEORY-2185](../theory.d/THEORY-2185.md)): **a
weak parallel that runs both ways; no spectral analysis.** Under coarse
labels the variance-dominant directions of the last layer are the coarse
class means, and the fine-class signal lives in "the small amount of
remaining variation". That fits the shape "top common, lower
discriminating" for a finer distinction. But the top directions are the
most discriminating for the task the network was trained on, the paper
does no spectral decomposition, and it has no floor. Not evidence for or
against the claim; an illustration of where a finer distinction can live.
A note, no relation.
