---
status: Proposed
promote_when: >-
  A second recording, not the IBL Brainwide Map, analysed for both halves
  of the claim: neuron types tested against a covariance-matched unimodal
  null in each area, and separability tested over the conditions each
  area distinguishes. It should differ from the source in the way that
  most threatens the claim: several tasks, or one with many more
  variables, or a less-trained animal, or another species such as monkey
  prefrontal cortex, where categorical results have been reported. The
  claim holds if non-sensory areas again fail the null while their
  distinguishable conditions stay separable in nearly every split. It is
  refuted if non-sensory areas there broadly form types beyond the null,
  or if their distinguishable conditions sit in near-degenerate,
  for example collinear, geometry, so that many dichotomies fail. It is
  also weakened if separability falls well below 1 under a stricter
  criterion, such as a fixed accuracy threshold in the large-N limit.
  Further analyses of the IBL data cannot settle it, since they share the
  task, the variables and the animals.
title: 'During a visual decision task, neurons within a single area of mouse cortex rarely form discrete functional types, yet the task conditions the area distinguishes are linearly separable in nearly every way'
version: 1
tags:
- neuroscience
- cognition
date: '2026-10-04'
source:
- LIT-tmpzxkz1
summary: >-
  Posani et al. (2026), [LIT-tmpzxkz1](../literature.d/LIT-tmpzxkz1.md): in about 14,000 cortical units of the
  IBL Brainwide Map, the 8-variable selectivity profiles of 4,617
  selective neurons beat a covariance-matched Gaussian null for clustering
  within a region only in VISp, AUDp and SSp-ul. Elsewhere the profiles
  form an elongated, unclustered cloud. After merging conditions a region
  cannot tell apart (leaving 5 to 16 of 16), ≥ 95% of random balanced
  dichotomies are decodable above a shuffle null in 15 of 16 regions, GU
  being 0.82. Types do appear when regions are pooled, aligned with
  anatomy. One task, overtrained mice, a lenient separability criterion.
---
<!-- inactive-ok-file: THEORY-083 — Proposed; compared in Connections as a different sense of "categorical", no relation declared -->
<!-- inactive-ok-file: THEORY-102 — Proposed; named in Connections for the decoding caution, nothing here rests on it -->
<!-- inactive-ok-file: THEORY-008 — Proposed; named in Connections for why separability cannot see types, nothing here rests on it -->

# THEORY-tmp8wxwa: During a visual decision task, neurons within a single area of mouse cortex rarely form discrete functional types, yet the task conditions the area distinguishes are linearly separable in nearly every way

## Source

- Posani, Wang, Muscinelli, Paninski & Fusi (2026), [LIT-tmpzxkz1](../literature.d/LIT-tmpzxkz1.md), read in
  full in [NOTE-tmp25fhs](../notes.d/NOTE-tmp25fhs.md): Figs 2, 3 and 6, Extended Data Figs 6, 8, 9 and
  11, the Methods on clustering, independent conditions and separability,
  and the Peer Review File.

## What was actually shown

**The setting.** Posani et al. ([LIT-tmpzxkz1](../literature.d/LIT-tmpzxkz1.md)) analysed the International
Brain Laboratory's Brainwide Map: about 14,000 Neuropixels units from 43
regions of mouse cortex, recorded while trained mice turned a wheel to bring
a visual stimulus, shown on the left or right, to the centre of a screen,
in blocks of trials where one side was more likely.
Each neuron's selectivity is eight coefficients from a regression of its
activity on block prior, stimulus side, contrast, choice, outcome, wheel
velocity, whisking and licking, summed over the trial. Only the 4,617
neurons the regression explains better than a trial average are kept.

**The first half: no types within an area.** An area counts as
categorical when k-means finds clusters of these eight-dimensional
profiles with a higher silhouette score than the same number of points
drawn from a Gaussian with the data's own mean and covariance, at
Bonferroni P < 0.05. Of the about 20 areas with at least 50 selective
neurons, only primary visual (VISp), primary auditory (AUDp) and the
upper-limb field of primary somatosensory cortex (SSp-ul) pass. Even
there the clusters are weak: VISp's silhouette is about 0.23 against a
null near 0.14–0.18 (Fig. 3b,d). Other areas show an elongated cloud,
with some variables encoded much more strongly than others, and no
separated groups. The finding holds across selectivity thresholds, a
second clustering algorithm and time-resolved profiles, and two other
tests (clustering raw firing rates over 16 conditions, and ePAIRS) also
find only two categorical areas each (Extended Data Fig. 6).

**Types exist, at a larger scale.** Pooled across an anatomical module or
the whole cortex, profiles do cluster (whole cortex z = 8.0; somatomotor
8.56, medial 7.84, lateral 2.32, prefrontal 0.54, not significant), and the
clusters align with area labels (Fig. 3e,f). A single neuron's area can be
decoded from its profile, and areas with more anatomical connectivity
have more similar profiles (Fig. 2d–f). Specialisation is real *between*
areas. What is rare is discrete types *within* one.

**The second half: separable in nearly every way.** For geometry, four
binarised variables (whisking, block, stimulus side, contrast) define 16
conditions. For each area, conditions are merged until every remaining
pair is linearly decodable at ≥ 0.666. Between 5 (SSp-n) and 16 (MOs)
remain, more in areas higher in the anatomical hierarchy (ρ = 0.77). Over
those conditions, a cross-validated linear readout on a resampled
4,000-neuron population decodes ≥ 95% of 200 random balanced dichotomies
above the 99th percentile of a label-shuffled null in 15 of 16 areas; the
gustatory cortex reaches 0.82 (Fig. 6d, Extended Data Fig. 11e). Mean
accuracy over those dichotomies runs from 0.65 to 0.90.

**Why the halves go together.** The neurons × conditions activity matrix
has the same spectrum read by rows (neurons in conditions space) or by
columns (conditions in neural space). If neurons formed k tight types,
the conditions would span about k dimensions at most; the paper derives
the participation ratio of Gaussian clusters, which tends to min(k, M) as
the clusters tighten, and fits it to the regions (Methods, Extended Data
Fig. 9). Diverse, unclustered profiles leave room for the conditions to
sit in general position, which is what a readout needs to split them
arbitrarily (Cover's theorem, here in cross-validated form). The data
agree: over all 16 conditions, areas with more diverse profiles have
higher-dimensional geometry and higher separability (ρ = 0.67 and 0.69).
Over independent conditions separability is near ceiling everywhere, and
no longer depends on diversity.

**What this says about cognition.** It is the brain-wide version of the
claim behind mixed selectivity: that cortex favours diverse, mixed
responses because they let simple readouts compute many different
functions of the same variables. The authors' own conclusion is that
cortex "prioritize[s] diversity over categorical structure". That is an
interpretation; what is shown is the conjunction in the title.

## What this does not say

- **It does not say cortex has no functional specialisation.** Areas
  differ in what they encode and how strongly. The number of
  distinguishable conditions ranges threefold, and types appear when
  areas are pooled.
- **It does not say there are no neuron types.** It concerns response
  profiles over eight variables of one task. Tuning to anything the task
  does not vary is invisible (Referee 3's point, now in the paper's
  Limitations). Transcriptomic types are not examined, and the authors
  list continuous or only partly separated cell types as one explanation.
- **"Rarely categorical" means failing a Gaussian null.** The authors
  concede this is a narrow class: an elongated cloud with strongly
  selective neurons on its tails fails the null too. A neuron strongly
  selective for a *stimulus category* (Freedman's sense) can sit in such
  a cloud.
- **"Separable" is lenient.** Above a shuffle null near 0.53 accuracy, on
  resampled pseudopopulations. Conditions were first merged until every
  pair was decodable, which removes the commonest route to failure; what
  remains is a test against near-degenerate geometry such as collinear
  conditions (Fig. 6a). The synthetic results show it is blind to
  anisotropy (Extended Data Fig. 8h,i).
- **It does not say the geometry is high-dimensional in absolute terms.**
  The participation ratio over independent conditions is at most 5.3, in
  MOs with 16 conditions.
- **It says nothing about abstraction.** Separability measures how many
  ways a readout can split the conditions, not whether a code generalises
  across conditions. The authors note that a disentangled, abstract code
  can also be maximally separable.
- **The hierarchy trends are weaker than the two halves.** Categoricality
  falls along the hierarchy (ρ = −0.62) in the main pipeline but not in
  the conditions-space one, and ePAIRS flags a high-hierarchy area (MOs).

## Connections

- **[THEORY-083](THEORY-083.md) (neural collapse)** looks like the opposite claim and is
  not. Papyan, Han and Donoho ([LIT-618](../literature.d/LIT-618.md)) found that a classifier trained
  past zero error collapses each class's last-layer features to its mean
  and spreads the means into a simplex equiangular tight frame. That is a
  claim about *conditions* in feature space, and in this account's terms
  it is maximal distinguishable conditions with maximal dimension, the
  arrangement separable in every way. This account's "categorical" is
  about *neurons* forming types, on which neural collapse is silent: it
  is unchanged by rotating the units. By the row/column bound, a
  collapsed C-class layer whose units formed k tight types would need
  k ≥ C − 1. No relation is declared: the two accounts are about
  different phenomena, in different systems.
- **[THEORY-008](THEORY-008.md)** holds that what a regularised linear readout can decode
  depends only on the representation's kernel, which a rotation of units
  leaves unchanged. That is why the second half cannot speak to the
  first: separability is identical whether the same geometry is carried
  by segregated types or by mixed units ("explicit" versus "implicit"
  modularity in the paper's Discussion). The two halves need two tests.
- **[THEORY-102](THEORY-102.md)** rests on decoding image category from human ventral
  temporal cortex (Vishne et al., [LIT-644](../literature.d/LIT-644.md)). The source paper draws a
  warning from the second half: when conditions are pairwise separable,
  nearly any grouping of them is decodable, so decoding one chosen
  variable above chance is weak evidence that it is specifically
  represented. [THEORY-102](THEORY-102.md)'s evidence is near-ceiling, time-generalising
  decoding and exemplar geometry, so the warning qualifies how such
  evidence is read without undercutting it.
