---
status: Proposed
promote_when: >-
  Three results, none of which the source supplies. First, end-to-end
  evaluation of points inside the hull of fine-tuned models, not a
  linear probe refitted on a frozen encoder. Second, the same geometry
  from other pretrained models and architectures and on generative tasks,
  with the hull sampled densely enough to estimate it. Third, a direct
  test of the explanation for averaging. Locate model soups and SWA
  solutions relative to the region's members and centroid, and show that
  their gains grow as they sit further inside. It is refuted if hull
  points lose to their members when evaluated end to end, or if soups and
  SWA gain while sitting no further inside the region than the members.
  It is also refuted if the region has no walls in many directions, of
  which the origin direction of Appendix F is already one. More
  probe-based hull samples on RoBERTa-base would not move it.
title: 'Fine-tuning from one pretrained model lands near the edge of a task-specific low-loss region that contains the convex hull of the fine-tuned models, and averaging them moves inward'
version: 1
tags:
- loss-landscapes
- anthology-candidate
date: '2026-10-03'
source:
- LIT-tmp9gt28
extends:
- THEORY-tmpqf08n
summary: >-
  Gueta et al. (2023), [LIT-tmp9gt28](../literature.d/LIT-tmp9gt28.md): RoBERTa-base models fine-tuned on the
  same dataset, the same task family, or any of 12 GLUE and SuperGLUE
  datasets cluster in weight space. Sampled points in the convex hull of
  each group beat the group's own members in 88% to 96.7% of comparisons.
  Extrapolating past the members raises the loss quickly, so the members
  sit near the region's edge and averaging moves inward. The paper calls
  the region convex, but shows only that the hull lies inside it, by a
  probe-based loss. Its reading of model soups and SWA as picking points
  inside the region is argued in its §8, not tested. Moving from the
  centroid towards the origin stays low-loss far past the members, which
  the authors cannot explain.
---
<!-- inactive-ok-file: THEORY-tmpqf08n THEORY-tmpj7zc1 THEORY-tmp7hwgu THEORY-tmpexgld — Proposed; the account this one extends and siblings named in Connections, nothing here rests on their open parts -->

# THEORY-tmp5fzhc: Fine-tuning from one pretrained model lands near the edge of a task-specific low-loss region that contains the convex hull of the fine-tuned models, and averaging them moves inward

## Source

- Gueta, Venezian, Raffel, Slonim, Katz & Choshen (2023), [LIT-tmp9gt28](../literature.d/LIT-tmp9gt28.md),
  read in [NOTE-tmp3gtyn](../notes.d/NOTE-tmp3gtyn.md): §§2–8 and Appendices B, F and G.

## What was actually shown

**Fine-tuning goes where the data send it.** Gueta et al. compared task
vectors, fine-tuned minus pretrained weights, by cosine. They took 280
RoBERTa-base models fine-tuned on 12 datasets with 20 seeds each, and the
vectors cluster by dataset with 98% accuracy. Models from three task
families cluster by family with 90% ([LIT-tmp9gt28](../literature.d/LIT-tmp9gt28.md), §4). Sub-samples of 200
to 3,000 examples cluster by dataset, not by size (§4.1). Starting from a
second RoBERTa-base pretraining, models cluster by pretrained model first
(App. B). So the region belongs to a starting point and a kind of data
together.

**The interior is at least as good as the members.** Loss is a
"generalized loss": the encoder is frozen, a new head is fitted by linear
probing on the target's training set, and test loss is reported (§3).
Points on lines between pairs perform comparably to or better than the
endpoints at all three levels (§5.1). Points sampled from a group's convex
hull have loss no higher than every model fine-tuned elsewhere (100% at
each level). They beat the group's own members in 88% of comparisons for
MNLI, 96.7% for the NLI family and 90% at the general level (§5.2).

**The members are near the edge.** Extrapolating along the lines between
members, past either end, reaches poor loss quickly at all three levels:
"a relatively flat base and steep cliffs" (§6, App. G). Points generated
at random directions from the MNLI centroid perform like the members out
to the members' own spread and degrade beyond it (App. F). The authors
conclude that fine-tuning "typically" yields models on the boundary of
the region and that its centre is better (§9).

**A consequence that was tested.** The centroid of the general-level
models, excluding those trained on the target, is a better start for
BitFit than the pretrained model. Mean accuracy is 65.54 against 61.51,
better on 9 of 12 datasets, equal on 2 and worse on 1 (§7, Table 2).

## What this does not say

- **It does not show the region is convex.** The paper says "this basin
  is a convex region" (§9). What it shows is that sampled points of the
  members' convex hull are low-loss: the region contains the hull. The
  low-loss set itself may be any shape that contains it. The hull is also
  sampled thinly, with as many draws as members, 5 in most settings.
- **It does not show soups and SWA work this way.** §8 reads weight
  averaging of same-dataset models as picking "a model from inside the
  dataset region". That covers model soups, [ANTH-LIT-675](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-675.md). It says the
  success of SWA-based methods "may be partly attributed to its tendency to
  fall within a region, rather than on its borders". That covers SWA,
  [ANTH-LIT-673](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-673.md). Neither is tested: no soup or SWA solution is located
  relative to the region, and no gain is related to depth inside it. The
  account would explain both. Whether it does is the open question.
- **It is a claim about probed representations.** Every loss is that of a
  frozen encoder with a refitted head. A hull point that probes well need
  not be a good end-to-end classifier, and end-to-end accuracy of hull
  points is not reported.
- **The edge is not an edge in every direction.** Moving from the MNLI
  centroid towards the origin stays low-loss even beyond the members'
  distance (App. F). The authors report it without explanation.
  "Near the edge" holds along the members' lines and random directions,
  not universally.
- **One model and one task type**: RoBERTa-base, English classification.
  The authors say the picture "may not hold in general when randomly
  initializing" (§10).

## Connections

- **[THEORY-tmpqf08n](THEORY-tmpqf08n.md)**, which this extends. That account says linear
  connectivity from a shared stable start holds when the objectives share
  structure. This one carries it from a line between two runs to a region
  spanned by many. It grades the shared structure by nesting, dataset
  inside task family inside general language classification. And it adds
  where in the region fine-tuning stops, at the edge.
- **[THEORY-tmpj7zc1](THEORY-tmpj7zc1.md)** says that along a low-loss line each layer's
  features are the blend of the endpoints' features. If that holds for
  many-model averages, moving inward here is blending the members'
  features. That account measured pairs, so the link is open.
- **[THEORY-tmp7hwgu](THEORY-tmp7hwgu.md)** describes what merging across tasks from one
  pretrained start loses: redundant updates and sign conflicts. TIES's
  results are end-to-end accuracy, below the fine-tuned models. Gueta et
  al.'s general-level hull is low-loss by probe. The two are not in
  conflict, because they measure different things, but the region
  picture alone would not predict TIES's losses.
- **[THEORY-tmpexgld](THEORY-tmpexgld.md)**, filed alongside this one, says sets of trained
  solutions are star domains, with a centre linearly connected to the
  rest, even where they are not convex. A low-loss hull, as here, is a
  stronger property than a star domain. Since convexity of the region
  itself is not shown, the star-domain description fits this evidence as
  well as the convex one.
