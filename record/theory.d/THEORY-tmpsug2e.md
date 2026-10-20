---
# Don't copy this file by hand — run `luria new theory`, which assigns the
# code and fills in what a machine can compute.
#
# A theory is a claim about WHY something happens, or about what is true of
# these systems. State it as a finding, not as an instruction: "Batch
# normalization helps by smoothing the optimization landscape" rather than
# "Use batch normalization". If what you are about to write tells the reader
# what to do in machine learning, it is a practice, and it belongs in the
# Anthology of the SOTA (ANTH-ADR-031).

# Active | Proposed | Deferred | Superseded | Rejected, optionally " — note".
# What each one means here is in luria.yaml, and it is NOT what the same word
# means on a practice: this status says whether the record believes the
# ACCOUNT, and an explanation can be `Rejected` while the thing it explained
# goes on working exactly as well as it ever did.
status: 'Proposed'

# REQUIRED while the status is Proposed or Deferred; delete it when the
# explanation goes Active. What would settle it — a KIND of result, not a
# quantity of them (ANTH-ADR-014). An explanation that cannot say what would show
# it wrong is a story, and this field is where that shows up.
promote_when: "Three results, none of which the source supplies. First, end-to-end evaluation of points inside the hull of fine-tuned models, not a linear probe refitted on a frozen encoder. Second, the same geometry from other pretrained models and architectures and on generative tasks, with the hull sampled densely enough to estimate it. Third, a direct test of the explanation for averaging. Locate model soups and SWA solutions relative to the region's members and centroid, and show that their gains grow as they sit further inside. It is refuted if hull points lose to their members when evaluated end to end, or if soups and SWA gain while sitting no further inside the region than the members. It is also refuted if the region has no walls in many directions, of which the origin direction of Appendix F is already one. More probe-based hull samples on RoBERTa-base would not move it."

# The claim. Repeat it as the body's `# THEORY-tmpsug2e:` heading; the lint checks
# that the two agree.
title: 'Fine-tuning from one pretrained model typically lands near the edge of a task-specific low-loss region in weight space that contains the convex hull of the fine-tuned models, and averaging their weights, as model soups and stochastic weight averaging do, works by moving inward'

version: 1

# One or more topics from luria.yaml, primary first — the same table the
# reading list uses. Take the topic of what the account is about.
tags:
- loss-landscapes
- anthology-candidate

date: '2026-10-20'

# There is deliberately no `published:` line. It is DERIVED from the first
# entry in `source:` below, and writing it down is a lint violation, because
# the value has one home and this is not it.

# REQUIRED, and a LIST. The papers this account rests on, primary first. An
# explanation with no paper behind it is a hunch, and the lint will say so.
source:
- LIT-658

# What the index table shows. The title already carries the claim, so spend
# this on provenance and on the sharp edge: who said it, and what it does not
# say. Prose, so bare codes in it get linked by `luria link --fix`.
summary: >-
  Gueta, Venezian, Raffel, Slonim, Katz and Choshen (2023), [LIT-658](../literature.d/LIT-658.md), read in
  [NOTE-515](../notes.d/NOTE-515.md), conclude that fine-tuning "typically" yields models on the boundary
  of a region whose centre is better, and read model soups and SWA as picking
  points inside it (§§8–9). The record holds as shown, in [THEORY-105](THEORY-105.md), only the
  probe-loss comparisons of hull points with members and the BitFit result, for
  RoBERTa-base on English classification. This is their geometric thesis, filed
  under [ADR-047](../decisions.d/ADR-047.md) v4 when the narrowing dropped it.
extends:
- THEORY-105
answers:
- QUESTION-069
---
<!-- inactive-ok-file: THEORY-107 — Proposed; the merging result this thesis would have to explain, named in What this does not say -->

# THEORY-tmpsug2e: Fine-tuning from one pretrained model typically lands near the edge of a task-specific low-loss region in weight space that contains the convex hull of the fine-tuned models, and averaging their weights, as model soups and stochastic weight averaging do, works by moving inward

## Source

Gueta et al. (2023), [LIT-658](../literature.d/LIT-658.md), read in full in [NOTE-515](../notes.d/NOTE-515.md) from the arXiv HTML
of v3, claim C3. The extrapolation curves behind the edge claim (§6,
Appendices F and G) were read only from their captions and text.

## What is asserted

That fine-tuning from one pretrained model, in general and not only for
RoBERTa-base classifiers, stops near the edge of a low-loss region specific
to the task and starting point, a region containing the convex hull of the
fine-tuned models; and that weight averaging gains because it moves inward
from that edge.

## What the Active entry establishes toward it

[THEORY-105](THEORY-105.md) holds that sampled hull points lost no more than models
fine-tuned elsewhere and beat the group's own members in 88% to 96.7% of
comparisons, by the loss of a linear probe on the frozen encoder, and that
the general-level centroid was a better BitFit start than the pretrained
model (65.54 against 61.51). That the interior is at least as good as the
members is what the edge reading predicts; it does not show the members sit
at an edge.

## What would confirm or reject it

The promote_when, inherited unchanged from [THEORY-105](THEORY-105.md): end-to-end
evaluation of hull points; the same geometry from other pretrained models
and architectures and on generative tasks; and soups and SWA located
against the region's members and centroid, with gains growing deeper
inside. It is refuted if hull points lose to their members end to end, if
soups and SWA gain without sitting further inside, or if the region has no
walls in many directions, of which the origin direction of Appendix F is
already one.

## What this does not say

- **It does not say the region is convex.** The paper calls it convex but
  shows only that it contains the sampled hull.
- **It does not say averaging always helps.** Cross-task merging loses
  end-to-end accuracy ([THEORY-107](THEORY-107.md)), which this thesis would have to
  explain.
