---
number: 28
status: Proposed
formerly:
- SYNTHESIS-tmpexmgz
title: 'Whether the solutions training reaches are connected is asked of the solutions, the path family, the shared history and the regime: one construction shows two realizations of one function joined by a curve and separated by the straight line and by any budget below √2 times their cost; the record''s steps from pairs to many-model averages and to depth after alignment are Proposed; and whether the measured onsets, alignments and feature interpolation hold beyond the settings measured is open'
version: 2
history:
- version: 2
  date: '2026-11-18'
  note: >-
    At the synthesis review of 2026-11-18 (learned-structure). The
    readings of 2026-11-15 changed two components: CLAIM-498's note says
    Zhou et al. (2024) measure its averaging step for soups, and
    QUESTION-318's note records Zhou et al. and Zhu (2026) on both its
    halves. The account's "Each says that no reading measures it" and
    "Proposed and unmeasured" are corrected to match. CASE-273
    (orthogonal task updates that interact), filed the same day, is
    integrated. Two links the account called unstated were stated after
    it was written: CLAIM-263 bears on QUESTION-069 (its note of
    2026-11-11), and CLAIM-633, drafted at the review of 2026-11-10, was
    filed, resting on CLAIM-524 and bearing on QUESTION-069. Both
    sections are corrected. The title is unchanged.
defeated_if: >-
  A component misstated or misattributed here; an in-force component of
  this part of the learned-structure line (the connectedness of trained
  solutions and what a barrier between them shows) left out without a
  reason given; or a link this account states that no component states.
  Its standing is its components'.
tags:
- loss-landscapes
- representation-learning
- learning-theory
date: '2026-11-10'
line:
- learned-structure
integrates:
- QUESTION-069
- CLAIM-524
- QUESTION-164
- QUESTION-312
- QUESTION-317
- QUESTION-316
- QUESTION-318
- CLAIM-498
- CLAIM-499
- CASE-273
bears_on:
- QUESTION-069
---
<!-- inactive-ok-file: ADR-047 — Superseded by ADR-057, which keeps its evidence rulings; cited for the kind-2 rule its components were filed under -->
<!-- inactive-ok-file: CASE-273 CLAIM-633 ADR-075 ADR-083 CLAIM-263 CLAIM-498 CLAIM-499 THEORY-107 THEORY-108 THEORY-109 THEORY-110 THEORY-209 — Proposed; components, citations and the decisions this account follows, with their standing -->

# SYNTHESIS-028: Whether the solutions training reaches are connected is asked of the solutions, the path family, the shared history and the regime: one construction shows two realizations of one function joined by a curve and separated by the straight line and by any budget below √2 times their cost; the record's steps from pairs to many-model averages and to depth after alignment are Proposed; and whether the measured onsets, alignments and feature interpolation hold beyond the settings measured is open

*A part account of the learned-structure line ([ADR-083](../decisions.d/ADR-083.md)); the line's account is built over it and its sibling parts.*

## The account

- **The root.** [QUESTION-069](../questions.d/QUESTION-069.md) (filed in the fourth synthesis pass, the
  record's; Open) asks whether connectedness belongs to the solutions or
  to "the path family searched, the shared history that produced them
  and the regime they were trained in" (its title). Its body lists what
  each reading measured and with which instrument: curves ([THEORY-109](../theory.d/THEORY-109.md)),
  onset in training ([THEORY-114](../theory.d/THEORY-114.md)), a centre ([THEORY-110](../theory.d/THEORY-110.md)), the convex hull
  from one start ([THEORY-105](../theory.d/THEORY-105.md)), sign conflicts ([THEORY-107](../theory.d/THEORY-107.md)), phase III
  ([THEORY-108](../theory.d/THEORY-108.md)) and SGD's stationary distribution ([THEORY-209](../theory.d/THEORY-209.md)). What would
  answer it: phase III runs aligned by permutation and measured on
  several path families, and a pair known to share a mechanism.
- **The path family.** [CLAIM-524](../claims.d/CLAIM-524.md) (from the owner's remark at U17 of
  "Analyze nucleation concepts", A17's curve and A18's budget, the general
  bound the reader's; demonstrated, Active) bears on [QUESTION-069](../questions.d/QUESTION-069.md). For
  f = u₁v₁ + u₂v₂ the realizations (1, 1, 0, 0) and (0, 0, 1, 1) are
  joined by a curve at f = 1, the straight line between them falls to ½,
  and under a budget below √2 no path at f = 1 joins them. Its reading of
  the question: "This construction answers one part: for a fixed function
  and fixed endpoints, the answer changes with the path family admitted,
  and a resource bound is one way to restrict it."
- **The regime.** [QUESTION-164](../questions.d/QUESTION-164.md) (the promotion condition of [THEORY-211](../theory.d/THEORY-211.md);
  Open) refines [QUESTION-069](../questions.d/QUESTION-069.md) as its "regime" alternative: whether the
  law of balance holds in a deep network on real data. Its body says it
  bears on [QUESTION-080](../questions.d/QUESTION-080.md) (the collapse family), "since motion along a
  symmetry changes no function".
- **Onset, alignment, merging and feature interpolation, beyond the
  settings measured.** Four questions hold the promotion conditions of
  the readings narrowed at the tenth and eleventh status reviews:
  [QUESTION-312](../questions.d/QUESTION-312.md) ([THEORY-114](../theory.d/THEORY-114.md), linear connectivity emerging in training
  outside image classification) and [QUESTION-317](../questions.d/QUESTION-317.md) ([THEORY-112](../theory.d/THEORY-112.md), alignment
  at standard width, what the residual barrier is, and depth) refine
  [QUESTION-069](../questions.d/QUESTION-069.md); [QUESTION-316](../questions.d/QUESTION-316.md) ([THEORY-113](../theory.d/THEORY-113.md), whether task difference makes
  merging fail) and [QUESTION-318](../questions.d/QUESTION-318.md) ([THEORY-111](../theory.d/THEORY-111.md), layerwise feature
  connectivity beyond image classification and for many-model averages)
  name [QUESTION-312](../questions.d/QUESTION-312.md) only as the pattern their move followed.
- **Two steps the record took.** [CLAIM-498](../claims.d/CLAIM-498.md) (Proposed) is the averaging
  clause of [THEORY-111](../theory.d/THEORY-111.md)'s old title, the record's step from pairs to
  many-model averages, and bears on [QUESTION-318](../questions.d/QUESTION-318.md), whose averaging half is
  its defeater. [CLAIM-499](../claims.d/CLAIM-499.md) (Proposed) is the depth clause of [THEORY-112](../theory.d/THEORY-112.md)'s
  old title, composed from Entezari et al.'s unaligned curves and
  Ferbach et al.'s width bound, and bears on [QUESTION-317](../questions.d/QUESTION-317.md). Both once said
  that no reading measures them. [CLAIM-498](../claims.d/CLAIM-498.md)'s note of 2026-11-15 now says
  Zhou et al. (2024) measure its averaging step for soups of 5 and 10
  same-task fine-tunes from one pretrained start, and leaves SWA iterates
  and decoder-only language models open. [CLAIM-499](../claims.d/CLAIM-499.md) is still unmeasured.
- **[QUESTION-318](../questions.d/QUESTION-318.md)'s halves, partly measured.** Its note of 2026-11-15
  records Zhou et al. (2024) measuring layerwise linearity in CLIP
  transformers and T5, and Zhu (2026) replicating it in decoder-only
  language models merged from one base. For the averaging half it records
  Zhou et al.'s soups. It says "neither half is settled".
- **Why parameter angles do not settle composition.** [CASE-273](../cases.d/CASE-273.md)
  (A's construction from the exchange "Explain String Theory", Proposed)
  shows two orthogonal task updates whose joint effect exceeds the sum of
  their separate effects. In its words, in models fine-tuned from one
  start "layerwise feature linearity often holds approximately", "so the
  cross term can be small in practice". It bears on [QUESTION-318](../questions.d/QUESTION-318.md).

## The components

- [QUESTION-069](../questions.d/QUESTION-069.md), the record's (2026-10-12), Open.
- [CLAIM-524](../claims.d/CLAIM-524.md), the owner's prompt with A17's and A18's constructions and
  the reader's general bound, thesis, demonstrated, Active; second line
  formal-apparatus.
- [QUESTION-164](../questions.d/QUESTION-164.md), [QUESTION-312](../questions.d/QUESTION-312.md), [QUESTION-316](../questions.d/QUESTION-316.md), [QUESTION-317](../questions.d/QUESTION-317.md) and
  [QUESTION-318](../questions.d/QUESTION-318.md), promotion conditions moved from [THEORY-211](../theory.d/THEORY-211.md), [THEORY-114](../theory.d/THEORY-114.md),
  [THEORY-113](../theory.d/THEORY-113.md), [THEORY-112](../theory.d/THEORY-112.md) and [THEORY-111](../theory.d/THEORY-111.md), Open.
- [CLAIM-498](../claims.d/CLAIM-498.md) and [CLAIM-499](../claims.d/CLAIM-499.md), kept by the [ADR-047](../decisions.d/ADR-047.md) sweep of 2026-10-30 (kind
  2) as the record's own steps, thesis, interpretive, Proposed; both
  tagged anthology-candidate.
- [CASE-273](../cases.d/CASE-273.md), A's construction (2026-11-15), stipulated, Proposed.

## Links tested as claims

- **[CLAIM-524](../claims.d/CLAIM-524.md)'s two realizations as one symmetry orbit.** Not stated by
  any entry. Swapping the two paths maps each of [CLAIM-524](../claims.d/CLAIM-524.md)'s endpoints to
  the other and each budgeted piece of its zero-loss set onto the other,
  so in the quotient [CLAIM-263](../claims.d/CLAIM-263.md) prescribes the budgeted set is connected.
  It passes [ADR-075](../decisions.d/ADR-075.md)'s derivation route, and it was filed as [CLAIM-633](../claims.d/CLAIM-633.md)
  (Proposed), which rests on [CLAIM-524](../claims.d/CLAIM-524.md) and bears on [QUESTION-069](../questions.d/QUESTION-069.md). The
  line's account ([SYNTHESIS-030](SYNTHESIS-030.md)) integrates it.
- **The four promotion-condition questions as one question.** A
  classification, not a claim: their common pattern is their filing
  history, which their summaries state.

## Not stated on the record

- **[CLAIM-263](../claims.d/CLAIM-263.md) ([SYNTHESIS-026](SYNTHESIS-026.md)) and this part's three conditions.** [CLAIM-263](../claims.d/CLAIM-263.md)'s protocol is assembled
  from [THEORY-111](../theory.d/THEORY-111.md), [THEORY-112](../theory.d/THEORY-112.md) and [THEORY-113](../theory.d/THEORY-113.md), whose open conditions are
  [QUESTION-318](../questions.d/QUESTION-318.md), [QUESTION-317](../questions.d/QUESTION-317.md) and [QUESTION-316](../questions.d/QUESTION-316.md), and its body names
  [THEORY-108](../theory.d/THEORY-108.md)'s phase III as "a ready case for the protocol", which is
  what [QUESTION-069](../questions.d/QUESTION-069.md) says would answer it. Since its note of 2026-11-11,
  [CLAIM-263](../claims.d/CLAIM-263.md) bears on [QUESTION-069](../questions.d/QUESTION-069.md), for that reason, so that link is
  stated. The same note says [QUESTION-316](../questions.d/QUESTION-316.md), [QUESTION-317](../questions.d/QUESTION-317.md) and [QUESTION-318](../questions.d/QUESTION-318.md)
  "would test this claim rather than be borne on by it, and take no
  relation". What stays unstated is how a test of those three would bear
  on [CLAIM-263](../claims.d/CLAIM-263.md)'s protocol.
- **[QUESTION-164](../questions.d/QUESTION-164.md) and [QUESTION-081](../questions.d/QUESTION-081.md) ([SYNTHESIS-034](SYNTHESIS-034.md))**: one law of balance, no
  relation ([SYNTHESIS-034](SYNTHESIS-034.md)).

## What it does not say

- That trained networks are disconnected under realistic budgets
  ([CLAIM-524](../claims.d/CLAIM-524.md)).
- That averaging weights averages features in general, or that the
  aligned barrier rises with depth. [CLAIM-498](../claims.d/CLAIM-498.md) is Proposed and measured
  only for soups from one start; [CLAIM-499](../claims.d/CLAIM-499.md) is Proposed and unmeasured.
- That a barrier surviving alignment marks a different mechanism; that is
  [CLAIM-263](../claims.d/CLAIM-263.md)'s step 2, in [SYNTHESIS-026](SYNTHESIS-026.md).
- Anything with standing of its own.
