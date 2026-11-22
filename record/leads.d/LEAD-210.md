---
number: 210
status: Open
formerly:
- LEAD-tmpp88ld
title: "Track a fixed probe set's representations across training checkpoints at several widths and sample sizes, against isotropic, covariance-matched and shuffled nulls, and time a linear probe's onset against PCA outlier detachment, cone enrichment and collective relaxation, to tell concentration, detectability and collective organization apart"
version: 2
history:
- version: 2
  date: '2026-11-22'
  note: >-
    After the reading of LIT-2998 (NOTE-2278, THEORY-2189). The
    TwoNN intrinsic dimension, with a subsampling check, is added in place
    to the per-checkpoint measurements, with the covariance-matched
    Gaussian as its null, after the paper's Fig. 5B, and THEORY-2189 is
    added to advances. The design is otherwise unchanged.
stage: specified
priority: medium
method:
- empirical
tags:
- representation-learning
- learning-theory
- mathematical-statistics
date: '2026-11-21'
line:
- learned-structure
advances:
- QUESTION-515
- QUESTION-512
- CLAIM-799
- CLAIM-800
- CLAIM-827
- CLAIM-848
- THEORY-2189
summary: >-
  The measurement programme the other assistant proposed across A29 §9,
  A30 §9, A32 §9, A33 §8 and A35 §7–§9 of the exchange "Rich Get Richer
  Power Laws" (2026-11-21), gathered into one design. Its sharpest single
  test is A32's: "If a supervised linear probe becomes informative before
  PCA develops a separated eigenvalue, that would provide a clean
  demonstration of learning-associated semantic structure remaining below
  an unsupervised spectral threshold." The design is A's (the other
  assistant in the exchange "Rich Get Richer Power Laws", A29, A30, A32,
  A33 and A35); adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-2174 — Proposed, Deferred or new; the readings of 2026-11-22 and the entries they bear on -->
<!-- inactive-ok-file: CLAIM-799 CLAIM-800 CLAIM-827 CLAIM-848 CLAIM-838 CLAIM-797 CLAIM-798 THEORY-1136 CLAIM-193 — new and Proposed, filed from the exchange "Rich Get Richer Power Laws" on 2026-11-21; Proposed entries the record already held, cited for context -->
<!-- inactive-ok-file: THEORY-2186 THEORY-2188 THEORY-2189 — Proposed, Deferred or new; the readings of 2026-11-22 (Wang, Wu and Fan; Yang, Steinhardt and Hu; Ansuini and colleagues; Cai and colleagues; Martínez-Sánchez and colleagues), their arguments, and the entries they bear on -->

# LEAD-210: Track a fixed probe set's representations across training checkpoints at several widths and sample sizes, against isotropic, covariance-matched and shuffled nulls, and time a linear probe's onset against PCA outlier detachment, cone enrichment and collective relaxation, to tell concentration, detectability and collective organization apart

## Sketch

**Why.** Each claim filed from the exchange's high-dimensional turns
predicts a different signature in the same data, and each has a geometric
null that can fake it. Measured together on one run, they can be told
apart: concentration ([CLAIM-797](../claims.d/CLAIM-797.md), [CLAIM-838](../claims.d/CLAIM-838.md)), spectral detectability ([CLAIM-799](../claims.d/CLAIM-799.md),
[CLAIM-827](../claims.d/CLAIM-827.md)), cone order ([CLAIM-800](../claims.d/CLAIM-800.md)) and collective dynamics ([CLAIM-798](../claims.d/CLAIM-798.md)).

**Design.**

- **Fixed probe set.** One set of inputs, embedded at every checkpoint, "to
  avoid confusing changes in sample composition with genuine movement in
  representation space" (A29 §9). A hierarchy with known coarse and fine
  labels (A33 §8).
- **Vary width D and probe size N** (A30 §9, A32 §9), holding data and task
  fixed, and scale the contrastive temperature or alignment strength with D
  (A30 §9), since fixed hyperparameters move a model between regimes as D
  changes ([CLAIM-838](../claims.d/CLAIM-838.md)).
- **Measure at each checkpoint**: norm distribution; centred covariance
  spectrum, its exponent and participation ratio (fitted directly, not from
  width scaling, [CLAIM-848](../claims.d/CLAIM-848.md)); the TwoNN intrinsic dimension, with a
  subsampling check of its scale, read as a lower bound above about 20
  (added 2026-11-22, version 2, after [THEORY-2189](../theory.d/THEORY-2189.md)); top eigenvalues against a covariance-matched
  Marchenko–Pastur null; linear-probe accuracy per level; cone occupancy and
  enrichment E_t(C) = log[P_t(C)/P₀(C)] (A35 §9); the rotation-invariant
  Gram matrix (A30 §7); velocity correlations of the probe embeddings and
  their polarity p_i = ż_i/‖ż_i‖ (A29 §4, §9); time-reversal asymmetry; and
  the relaxation spectrum after small perturbations.
- **Three nulls** (A30 §9): isotropic Gaussian, Gaussian matched to the
  learned covariance (for the intrinsic dimension this null is not
  benign: Ansuini and colleagues' covariance-matched Gaussian has an ID
  "two orders of magnitude larger", growing with N, Fig. 5B), and shuffled
  embeddings that keep marginals and break
  semantic relations; plus kernel-predicted velocity correlations (A29 §9).
- **Comparisons that discriminate.**
  - Probe onset against PCA outlier detachment, per level: a probe that is
    informative first shows subthreshold structure ([CLAIM-799](../claims.d/CLAIM-799.md)).
  - Cone first-entry against held-out decodability per level: only the
    second is evidence of coarse-to-fine acquisition ([CLAIM-800](../claims.d/CLAIM-800.md)).
  - Occupancy curves across widths against c = κ/√D and κ/D: a collapse is
    the geometric null, not criticality (A35 §7).
  - A detached top eigenvalue that grows before global alignment appears:
    the spectral precursor of an alignment bifurcation ([CLAIM-827](../claims.d/CLAIM-827.md)).
- **Rate of cone refinement** (A33 §10, with A33 §8's "Scale-free
  refinement" row). Define a concept's specificity by the reference mass of
  its admissible region, I_i(t) = −log P₀(C_i(t)), with P₀ a fixed
  geometric reference measure, which "avoids comparing raw Euclidean cone
  volumes across dimensions or using an ill-defined uniform measure on an
  unbounded hyperbolic space". Then ask whether I_i(t) ∼ t^γ over a
  training regime, "or whether the times at which new semantic distinctions
  become stable follow a hierarchical or heavy-tailed distribution", and
  whether different levels of the hierarchy refine on different time
  scales. A33: "Neither scaling relation follows automatically from the
  cone model. But both are concrete hypotheses." Measure both at the
  widths and probe sizes above: a law that holds "over multiple system
  sizes" (A33 §8) is what would distinguish scale-free refinement from a
  geometric null.
- **Locality without circularity.** A29 §9 bins velocity correlations by
  distance on the learned manifold, while A30 §3 argues that meaningful
  locality may be what learning creates. Measuring locality on a geometry the
  dynamics are reshaping is circular, so the distances should come from a
  frozen reference (an early or final checkpoint, held fixed) or from input
  space, and the result compared across the choices.
- **Alignment across checkpoints.** Representations rotate between
  checkpoints, so "apparent temporal cone violations may therefore reflect a
  change of coordinates rather than a genuine loss of knowledge" (A33 §8):
  use shared anchors, an isometric alignment or invariant relations. The
  record holds that Poincaré seeds differ by more than an isometry
  ([THEORY-1136](../theory.d/THEORY-1136.md)) and that linear readouts see a representation only up to
  its kernel's symmetry ([CLAIM-193](../claims.d/CLAIM-193.md), [CLAIM-269](../claims.d/CLAIM-269.md)).

**Blocked on nothing named.** Not costed. A33 §8 also proposes comparing a
Euclidean model, a hyperbolic model with an entailment loss, and one with a
calibrated temporal-refinement loss on the same data; that arm needs the
composite loss of A33 §7, which A33 calls "only a candidate".

## What would close it

A run with the measurements above, reporting which onsets coincide and which
separate, at two or more widths and probe sizes.

## Note of 2026-11-22: Stringer and colleagues, read

Stringer and colleagues ([LIT-2972](../literature.d/LIT-2972.md), [NOTE-2257](../notes.d/NOTE-2257.md), [THEORY-2174](../theory.d/THEORY-2174.md)):
**background, and a method.** Their cross-validated PCA, which estimates a
signal spectrum from two repeats with noise variance excluded, is a way to
fit the exponent this lead asks for without the noise floor biasing the
tail; their fit range (ranks 11 to 500, the head excluded) is a precedent
for not fitting from rank 1. A note, no relation.

## Note of 2026-11-22: Ansuini and colleagues, read

Ansuini, Laio, Macke and Zoccolan ([LIT-2998](../literature.d/LIT-2998.md), [NOTE-2278](../notes.d/NOTE-2278.md),
[THEORY-2189](../theory.d/THEORY-2189.md)): **directly relevant, and a measurement added** (the
change of version 2 above). This lead's Gaussian matched to the learned
covariance is their Fig. 5B control, which they run through TwoNN with
decimation and find "two orders of magnitude larger", growing with N, "as
expected in the case of an ill-defined estimator": an intrinsic dimension
far below the null's says the structure is not fixed by second moments. Their
Fig. 9 is a checkpoint-tracking precedent (one VGG-16, last-layer ID
non-monotonic in training). [THEORY-2189](../theory.d/THEORY-2189.md) would be replicated by this
lead's intrinsic-dimension arm on image networks, so it is added to
`advances`.

## Note of 2026-11-22: Wang, Wu and Fan, read

Wang, Wu and Fan ([LIT-2984](../literature.d/LIT-2984.md), [NOTE-2274](../notes.d/NOTE-2274.md), [THEORY-2186](../theory.d/THEORY-2186.md)): **a
calibration case.** Their Theorem 5 is a solvable model in which this
lead's sharpest ordering is predicted: after a few gradient steps the
weight update exists for any step size, while the test-data kernel's
outlier appears only above a threshold. Their Fig. 2(a) and 3(b) show the
outlier's alignment moving with width and sample size, as this lead's
width and probe-size arms expect. A note, no relation.

## Note of 2026-11-22: Cai and colleagues, read

Cai, Zhang, Liu and Shi ([LIT-2975](../literature.d/LIT-2975.md), [NOTE-2277](../notes.d/NOTE-2277.md), [THEORY-2188](../theory.d/THEORY-2188.md)):
**ready-made observables** for a two-modality version of this lead: the
centroid gap and the energy distance between the two modalities'
marginals, which they track against retrieval on frozen OpenCLIP models. A
note, no relation.

## Note of 2026-11-22: Atigh and colleagues, read

Atigh and colleagues ([LIT-2993](../literature.d/LIT-2993.md)), read in this batch by another filer:
**a contrast.** They use nested cones as a training target and measure
learning by held-out accuracy at each level, at the end of training; the
over-time question this lead asks, when each level's distinction becomes
decodable, is the one the paper leaves aside. Relayed from that reading; a
note, no relation.
