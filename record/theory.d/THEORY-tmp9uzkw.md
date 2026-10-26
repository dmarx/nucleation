---
status: Active
title: 'In a two-layer attention-only transformer trained on the Pile, the weight-refined local learning coefficients of individual attention heads start alike and diverge over training, and clustering the curves groups the heads by the functional types that ablation assigns them at the end of training, previous-token, current-token, induction and n-gram-memorizing; among layer-1 heads, those running simple algorithms end with the lowest values and those memorizing the most n-grams with the highest'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Active from NOTE-tmpueby3, the reading in full of Wang et al.
    (2024). One study and one model, but the title claims no more than
    the paper measured, the head types are assigned by a method independent
    of the coefficient, and nothing in the record contradicts it
    (ADR-047 v3).
tags:
- learning-theory
- representation-learning
- loss-landscapes
date: '2026-10-26'
source:
- LIT-tmpa32mr
summary: >-
  Wang, Hoogland, van Wingerden, Furman and Murfet (2024), LIT-tmpa32mr,
  read in NOTE-tmpueby3: §4.1, Figs. 1–2 and 11, appendices B, F.5 and G.
  Per-head curves of how degenerate the loss is in that head's weights
  separate the heads by what they end up doing, and the separation is in
  the curves' shapes over training, not only their end values. It is one
  small model, cluster counts chosen by eye, and estimates whose ordering,
  not value, the authors trust. It does not show that the coefficient
  predicts a head's type before the type is visible.
---
<!-- inactive-ok-file: THEORY-tmp1dufu — Proposed; the companion account from the same reading, cited as open -->
<!-- inactive-ok-file: LIT-354 — Unavailable; Watanabe's book, named as the source of the quantity -->
# THEORY-tmp9uzkw: In a two-layer attention-only transformer trained on the Pile, the weight-refined local learning coefficients of individual attention heads start alike and diverge over training, and clustering the curves groups the heads by the functional types that ablation assigns them at the end of training, previous-token, current-token, induction and n-gram-memorizing; among layer-1 heads, those running simple algorithms end with the lowest values and those memorizing the most n-grams with the highest

## Source

Wang, Hoogland, van Wingerden, Furman and Murfet (2024, ICLR 2025),
LIT-tmpa32mr, read in full in NOTE-tmpueby3. The account rests on §3 (the
definitions and limitations), §4.1, Figs. 1, 2 and 11, and appendices B
(classification), F (model, SGLD settings, clustering) and G (seeds).

## What was actually shown

**The quantity.** For a split of the weights W = U × V, with V one head's
weights, the weight-refined LLC is
λ(w*; V) = −lim_{t→0⁺} log₂[vol(t/2)/vol(t)], where vol(t) is the volume of
v near v* whose loss, with u held at u*, is within t of its minimum. It is
estimated as nβ(E[ℓ_n] − ℓ_n(w*)) under a localized tempered posterior over
V, sampled by SGLD. As a check on what the number means: for a regular
model of d parameters near a nondegenerate minimum, vol(t) ∝ t^{d/2}, so
λ = d/2; more degenerate directions give less.

**The model.** A two-layer attention-only transformer, 8 heads per layer,
about 3M parameters, trained about 50,000 steps on a filtered Pile subset;
the run analysed by Hoogland et al. (2024).

**The types.** Independently of the LLC, each head is mean-ablated at the
end of training and its most affected tokens in context are matched to
templates (induction, bracket matching, skip n-gram, n-gram), with manual
inspection. Previous-token heads, a current-token head, two induction heads
and multigram heads result.

**The finding.** The per-head curves are similar early and diverge with
training. Coloured by type, same-type heads share scale, shape and the
location of critical points, and K-means on the curves recovers the types.
In layer 1, the induction and bracket-matching heads end lowest and the
heads that memorize the most n-grams end highest (Fig. 11 plots the
correlation). Clusters fitted to this run, applied to three further seeds,
mostly recover their heads' types, with exceptions the appendix lists.

**What could have come out otherwise.** The curves could have differed only
in level, not in shape, or grouped heads by layer rather than function. The
final ordering could have been unrelated to how many n-grams a head
memorizes.

## What this does not say

- **Not a prediction.** The types are fixed at the end of training and the
  curves are clustered after the fact. Whether early curves foretell a
  head's later type is not tested.
- **Not exact values.** The estimator presumes a local minimum, which a
  checkpoint mid-training is unlikely to be; the authors trust only the
  ordering of estimates.
- **Not a measured clustering quality.** The cluster counts were chosen by
  eye, and the standard cluster metrics "did not appear to work well" with
  eight heads per layer.
- **Not general.** One architecture without MLPs, a 5,000-token vocabulary,
  one run in the main text.
- **Not that the coefficient beats ablation.** Ablation scores over
  training also separate the types, and their final ordering is close to
  the coefficient's (appendix E).

## Connections

- **QUESTION-tmpivbso.** The reply's "functional differentiation" is
  measured here, per component, over training. It is a baseline the
  question's coupled model would have to beat on prediction.
- **QUESTION-039.** It times differentiation, not acquisition; it adds a
  per-component measure to the question's list of what can be timed.
- **THEORY-tmp1dufu.** The same reading's account of heads changing role.
