---
number: 175
status: Active
formerly:
- THEORY-tmpcgnsc
title: 'Cosine similarities to matched anchor points are unchanged by exactly the maps that preserve each sample''s cosines to the anchors, among them every orthogonal map times a positive scalar and every per-sample positive rescaling but not translations; in Moschella et al.''s experiments independently trained encoders agreed in them only approximately, enough for a decoder reading them to transfer untrained between seeds, architectures and languages with loss, while their nearest neighbours mostly differed'
version: 2
history:
- version: 2
  date: '2026-10-20'
  note: >-
    Narrowed and promoted, carrying out the promotion audit's decision for
    THEORY-175 (batch 048): the invariance re-derived (ADR-047 v2, dated note)
    and the agreement one study read in full (ADR-047 v3). The invariance
    class is stated as the maps preserving each sample's cosines to the
    anchors, with the members the derivation fixes, and the agreement is held
    to Moschella et al.'s experiments. The promote_when moves to
    QUESTION-tmpqgnk6.
tags:
- representation-learning
- anthology-candidate
date: '2026-10-09'
source:
- LIT-849
summary: >-
  Moschella et al. (2022; ICLR 2023), [LIT-849](../literature.d/LIT-849.md), as read in [NOTE-652](../notes.d/NOTE-652.md). The
  invariance is by construction; its class (the maps preserving each
  sample's cosines to the anchors, which include every orthogonal map times
  a positive scalar and every per-sample positive rescaling, but not
  translations) is the reader's statement, re-derived in a dated note. The
  approximate agreement is the paper's evidence: relative vectors match at
  cosine 0.86–0.97 across encoders, while ten-nearest-neighbour overlap is
  0.10–0.39. It does not say the maps between trained spaces are
  isometries, which the source never measures ([QUESTION-tmpqgnk6](../questions.d/QUESTION-tmpqgnk6.md)), nor that
  the transfer needs no paired data: the anchors are paired data.
supports:
- CLAIM-126
- CLAIM-082
---
<!-- inactive-ok-file: THEORY-008 THEORY-112 — Proposed; cited as the kernel and symmetry accounts this one sits beside -->

# THEORY-175: Cosine similarities to matched anchor points are unchanged by exactly the maps that preserve each sample's cosines to the anchors, among them every orthogonal map times a positive scalar and every per-sample positive rescaling but not translations; in Moschella et al.'s experiments independently trained encoders agreed in them only approximately, enough for a decoder reading them to transfer untrained between seeds, architectures and languages with loss, while their nearest neighbours mostly differed

## Source

Moschella, Maiorca, Fumero, Norelli, Locatello & Rodolà (2022; ICLR 2023),
[LIT-849](../literature.d/LIT-849.md), read in [NOTE-652](../notes.d/NOTE-652.md): §3.1 (eqs 2–4), §§4.1, 5.1–5.3,
Tables 1, 3–8 and 15–18.

## What was actually shown

**The invariance, exact (the reader's statement of the paper's eq. 4).** A
sample's relative representation is r_x = (cos(e_x, e_a))_{a ∈ A}, its
cosine similarities to the embedded anchors. It is unchanged by a map f of
the latent space exactly when f preserves the cosine between each sample
and each anchor. That class contains every orthogonal map times a positive
scalar, which are the only linear maps of a space onto itself that preserve
every cosine. It also contains every per-sample positive rescaling x ↦
c(x)x, which is not linear. It contains no translation and no general
invertible linear map. The paper names "rotations, reflections, and
rescaling" and assumes normalisation removes translations. When the anchor
set is the whole data set, two encoders with equal relative vectors have
equal cosine kernels on the data, so by [THEORY-004](THEORY-004.md)'s theorem their
normalised representations differ by an orthogonal map. With fewer anchors
than latent dimensions, equal relative vectors fix less than that.

**The agreement, approximate (the paper's evidence).** Whether trained
spaces actually differ by such a map is the paper's assumption, tested only
through its consequences, which could have come out otherwise:

- Agreement of relative vectors across encoders, for the same inputs:
  cosine 0.86 for FastText vs Word2Vec, 0.96–0.97 for two ViTs on CIFAR-10.
  Overlap of the ten nearest neighbours: 0.34–0.39 and 0.10–0.12 (Tables 1,
  8). With absolute vectors, overlap is 0.00.
- Untrained transfer of a decoder between encoders through the relative
  vectors: reconstruction error across seeds falls from about 100 to 8–15
  (MSE), against 3–5 unstitched (Table 3). Classification F1 across four
  English transformers is 33–80, against 49–97 unstitched (Table 5). An
  English decoder reads Spanish, French and Japanese encoders at 83, 78 and
  66, against 90 for English (Table 4). Across image encoders of different
  widths it reaches 31–62 on ImageNet, against 73–82 on the diagonal
  (Table 6). Absolute transfer is near chance throughout.
- Where a shared absolute space already exists (XLM-R, Table 17), relative
  vectors transfer worse than the absolute ones in every language pair.

Across languages the anchors must be matched by an outside correspondence:
translated reviews, or sentences aligned in WikiMatrix.

## What this does not say

- **That independently trained latent spaces differ by an isometry.** The
  source never fits a map between two spaces or reports a residual. Its
  evidence fits "approximately cosine-preserving" with distortion large
  enough to scramble most nearest neighbours.
- **That the transfer needs no correspondence.** "Zero-shot" means no
  training. The anchors are 300–768 paired samples, and the method works
  only as well as the pairing. Lenc and Vedaldi's stitching ([LIT-363](../literature.d/LIT-363.md)) fits a
  general linear map from paired data; this replaces the fit with a fixed
  construction that can absorb only the cosine-preserving part.
- **That cosine profiles are intrinsic to a representation.** Where a
  representation is identified only up to an invertible linear map, as a
  softmax output layer is ([THEORY-018](THEORY-018.md)), cosine is not identified and
  relative vectors inherit that. The source's encoders are hidden states and
  autoencoder bottlenecks, outside [THEORY-018](THEORY-018.md)'s scope.
- **Anything about meaning or reference.** The construction encodes a
  sample by its similarities to other samples. The source does not claim
  this is what a representation means, and its cross-system results depend
  on anchors fixed by correspondence, not on similarity structure alone.

## Connections

[THEORY-004](THEORY-004.md) (a representation is fixed by its kernel up to an orthogonal
map) is the exact form of the invariance clause. [THEORY-008](THEORY-008.md) (what a linear
readout decodes is a function of the normalised kernel) is consistent with
a decoder that reads kernel rows transferring when the kernels agree. The
Platonic Representation Hypothesis ([LIT-302](../literature.d/LIT-302.md)) reports the same split between
broad kernel agreement and modest nearest-neighbour agreement. At one layer,
the permutations and residual-stream rotations that [THEORY-112](THEORY-112.md) factors out
of weight space act on activations as orthogonal maps, so relative
representations there are blind to them.

## Note of 2026-10-20: the invariance class, derived

Worked for the promotion audit (batch 048). Write r_x = (cos(e_x, e_a))
over anchors a.

- A map f leaves every r_x unchanged exactly when
  cos(f(e_x), f(e_a)) = cos(e_x, e_a) for every sample x and anchor a.
  That is the definition unwound, and it is the class the title names.
- Per-sample positive rescaling x ↦ c(x)x with c > 0 is in it, since
  cosine ignores positive scale. A translation x ↦ x + t is not, for
  generic t.
- The linear maps of the space that preserve every cosine are the
  orthogonal maps times a positive scalar. Such an L is injective and
  preserves orthogonality; on an orthonormal basis, e_i + e_j ⟂ e_i − e_j
  forces ‖Le_i‖ = ‖Le_j‖, so LᵀL = c²I.

On a finite data set with fewer anchors than dimensions, maps that are
not conformal on the whole space can still preserve every sample-anchor
cosine, so the title names the members of the class that hold in general
rather than listing it.
