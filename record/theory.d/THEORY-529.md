---
number: 529
status: Proposed
formerly:
- THEORY-tmpgshxz
promote_when: >-
  A workable measure of coder complexity, so that a representational
  surface can be estimated for some real neural or artificial system, and a
  test of the criterion against cases chosen to break it: paradigm
  representations that are far from rate–distortion–complexity efficient,
  and efficient signalling systems nobody would call representational. The
  account is promoted if the states cognitive scientists call
  representations sit near the estimated surface and the comparison cases
  are excluded by something the account states in advance, and refuted if
  efficiency fails to separate them or if only the teleofunction does the
  separating. More examples of scientists attributing representation on
  grounds of compression or linear decodability cannot settle it, since
  they were selected to fit.
title: "A state is shown to be a representation by adaptation for transmitting information efficiently, near the optimal trade-off of rate, distortion and coder complexity under a teleofunctionally fixed distortion measure, rather than by correlation or mutual information alone, which nearly any causal link supplies and which cannot increase along a processing chain"
version: 1
tags:
- cognition
- information-theory
- neuroscience
date: '2026-10-16'
source:
- LIT-149
summary: >-
  Martínez (2025), [LIT-149](../literature.d/LIT-149.md), read in [NOTE-165](../notes.d/NOTE-165.md): a position paper with no new
  theorem or data. Its sharpest point is a standard result: by the
  data-processing inequality, mutual information about a car/no-car
  decision can only fall from retina to IT, so a mutual-information
  criterion would place the decision at the earliest stage; explicitness is
  better read as ease of decoding. The rest is a proposal supported by
  selected examples. Complexity has no operational measure, teleofunctions
  are needed to fix the distortion measure or every system is efficient
  for some loss, and misrepresentation and engineered systems are not
  addressed.
---
<!-- inactive-ok-file: THEORY-036 THEORY-089 THEORY-593 — Proposed; named as related or rival accounts in Connections and prose, not leaned on as settled -->

# THEORY-529: A state is shown to be a representation by adaptation for transmitting information efficiently, near the optimal trade-off of rate, distortion and coder complexity under a teleofunctionally fixed distortion measure, rather than by correlation or mutual information alone, which nearly any causal link supplies and which cannot increase along a processing chain

## Source

Martínez (2025), *The information-processing perspective on
representation*, [LIT-149](../literature.d/LIT-149.md), read in full in [NOTE-165](../notes.d/NOTE-165.md) (Philosophy and the
Mind Sciences vol. 6).

## What was actually shown

**The two theses (p. 1).** *Transmission*: representations are primarily
signals whose function is to transmit information for its own sake.
*RDC Trade-Off*: they aim at an efficient trade-off of rate (transmission
and storage cost), distortion (fidelity, which is what ML calls the loss)
and the computational complexity of the coders. The Pareto frontier of the
three is the "representational surface" (p. 4).

**The criterion.** Nonzero mutual information is a by-product of almost any
causal connection. Information flow near a rate–distortion optimum, or
coders near a complexity–distortion optimum, is "excellent evidence of
design or adaptation for the transmission of information for its own sake"
(p. 10). The inference is to the best explanation and is not defended
against alternatives ([NOTE-165](../notes.d/NOTE-165.md), C2).

**The one result that is demonstrated (pp. 16–17).** By the
data-processing inequality, information about a car/no-car decision can
only fall from the retina to IT. A mutual-information heuristic would
therefore locate the decision at the earliest stage, which is wrong. The
paper reads the ventral stream as trading rising distortion for falling
decoder complexity until the decision is linearly decodable, which is what
neuroscience means by "explicit" (Kriegeskorte & Diedrichsen 2019; Hong et
al. 2016).

**The mappings (§§4–5, §7).** Compression corresponds to cognitive economy
(Palmer et al. 2015 on ganglion cells predicting the future; Rosch);
channel coding's "safety bubbles" to representational vehicles (sparse
coding, synchronised assemblies); complexity management to explicitness.
The classical-versus-4E dispute is recast as a disagreement about the
shape of the surface (§6), which footnote 14 concedes is partly
terminological.

**Teleosemantics (fn. 7, p. 11).** Without teleofunctions, "any
information processing system can be seen as rate-distortion efficient …
with respect to some … distortion function". Teleofunctions fix the
distortion measure.

**What could have come out otherwise.** Only the data-processing point is
a result, and it could not have; it is a theorem. The rest makes no
prediction yet, because the complexity leg cannot be computed (fn. 9).

## What this does not say

- **That RDC adaptations generate the properties of representation.** The
  abstract says so; the body offers three illustrative mappings and leaves
  others "for another time" ([NOTE-165](../notes.d/NOTE-165.md), C8).
- **That efficiency alone marks representation.** Without teleofunctions it
  marks nothing, by the paper's own footnote. The account is a version of
  teleosemantics, and inherits its open questions.
- **What a representation is about, or how it can misrepresent.** Neither
  is addressed.
- **Anything about engineered or learned systems.** Only evolved systems
  are treated. Bengio et al. 2013 appears once, in a list "presented
  without discussion". Whether a trained autoencoder's latent code counts
  is open, and so is whether "linearly probeable" means "represented"; the
  paper's footnote 13 cites Ritchie et al. 2020 against that inference.
- **That a representational surface has been estimated for any system.**
  Complexity is gauged by heuristics (free parameters, nonlinearity,
  recurrence), and classical and Kolmogorov complexity are set aside as
  unusable (fn. 9).

## Connections

- **Content.** Block's two-factor account ([THEORY-089](THEORY-089.md)) is the record's
  account of what fixes the content of a representation, and it argues
  that a teleological account cannot be naturalised because selection need
  not aim mechanisms at truth. That bears on the teleofunctional premise
  here; the two accounts answer different questions (what a representation
  is about; what shows a state is one), so no relation is declared.
- **Real patterns.** Dennett's compressibility criterion ([THEORY-036](THEORY-036.md)) is
  the record's other compression-based test; it is about which patterns
  are real, not which states are signals.
- **Information bottleneck.** [NOTE-165](../notes.d/NOTE-165.md) notes the kinship with the
  information-bottleneck line of deep-learning theory in the anthology
  ([ANTH-LIT-531](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-531.md)). The paper does not draw it.
- **Frames.** [NOTE-150](../notes.d/NOTE-150.md) notes that Ivy & Mroczko-Wąsowicz's frame account
  ([THEORY-593](THEORY-593.md)) presupposes some theory of representation and states
  none; this is one it could use.
