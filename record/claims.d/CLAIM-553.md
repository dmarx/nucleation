---
number: 553
status: Proposed
formerly:
- CLAIM-tmpu69za
title: 'Give each of an individual''s perspectives a scalar intervention threshold on its discrepancy from the will it wants effective: the intervention that can be observed is the propensity to mobilize times the chance that the discrepancy is legible and a channel carries the intervention, so a perspective that does not intervene has not thereby endorsed; and read through Frankfurt, wholeheartedness is the will that moves the individual to act lying within every perspective''s tolerance, a full face of the requirement complex and not of the quiet one, so a structurally frustrated individual cannot act wholeheartedly unless its demands change'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A case the record accepts of an individual who acts wholeheartedly in
  Frankfurt's sense while some perspective it maintains is past its
  threshold on the will it acts on, whether or not that perspective has a
  channel; or a showing that the propensity to
  intervene cannot be told apart from channel loss under any intervention,
  as CASE-129's two alarms would be if no new hazard ever separated them.
  Not defeated by the lack of a measured propensity in any real agent,
  which the claim does not assert.
tags:
- free-will
- self-governance
- agency
date: '2026-11-04'
line:
- will-organization
rests_on:
- CLAIM-347
- CLAIM-417
- CLAIM-534
complements:
- CLAIM-364
- CLAIM-552
- CLAIM-548
- CLAIM-550
- CLAIM-549
grounds:
- THEORY-120
- THEORY-152
- CASE-119
- CASE-129
uses:
- TERM-060
- TERM-064
- TERM-103
- TERM-102
bears_on:
- QUESTION-041
- QUESTION-071
- QUESTION-270
summary: >-
  The owner's U15 of the exchange "Organizational Nucleation and SLT"
  (2026-11-04), as the owner corrected it at U17. U15 asked for a scalar
  tolerance per perspective "that identifies likelihood of communicating a
  complaint", an individual as a structure over its perspectives, and the
  compatibility structure. U17 recast "complaint" as "intervention
  threshold" or "activation threshold", and U18 added that an intervention
  need not be predicted to work to be motivating ([CLAIM-548](CLAIM-548.md)). This
  claim states the corrected construct. A15 was lost in the export; A16
  carries the construction, in U15's terms. Narrowed: the complex is
  [CLAIM-347](CLAIM-347.md)'s, and the individual as a structure over perspectives is
  [CLAIM-417](CLAIM-417.md)'s. What is new is the per-perspective threshold factored from
  the channel, and the reader's reading of it as Frankfurt's satisfaction
  ([THEORY-120](../theory.d/THEORY-120.md)). The construct is the owner's. The wording is A's,
  sharpened by the reader; adopting it is the owner's call.
---
<!-- inactive-ok-file: TERM-053 — Superseded by ADR-070; named as the former word for conferral -->
<!-- inactive-ok-file: CLAIM-364 CLAIM-417 LIT-695 THEORY-054 THEORY-120 THEORY-152 — Proposed, Deferred, Unavailable or new; cited from the exchange "Organizational Nucleation and SLT" of 2026-11-04 as open -->

# CLAIM-553: Give each of an individual's perspectives a scalar intervention threshold on its discrepancy from the will it wants effective: the intervention that can be observed is the propensity to mobilize times the chance that the discrepancy is legible and a channel carries the intervention, so a perspective that does not intervene has not thereby endorsed; and read through Frankfurt, wholeheartedness is the will that moves the individual to act lying within every perspective's tolerance, a full face of the requirement complex and not of the quiet one, so a structurally frustrated individual cannot act wholeheartedly unless its demands change

## The claim

**The owner's construct, as corrected.** U15 asked for a tolerance per
perspective that measures its "likelihood of communicating a complaint".
U17 recast that as an "intervention threshold" or "activation threshold".
U18 then said that an intervention need not be predicted to be effective
to be motivating ([CLAIM-548](CLAIM-548.md)). The construct is therefore a threshold
on mobilizing to intervene, not on objecting in words, and not on
expecting success.

**The construction (A16 §§1–2, in U15's terms).** P is an individual's
perspectives and W its candidate effective wills. Each perspective i has
a discrepancy d_i(w) ≥ 0 from the will it wants to be effective, its
target. A16 gave it one scalar threshold τ_i and acceptance set
A_i(τ_i) = {w : d_i(w) ≤ τ_i}, and called this "a tolerance condition on a Frankfurtian-style volition,
rather than a definition of Frankfurtian identification itself."

**Several tolerances on one divergence (the owner, at review).** The
intervention threshold is one tolerance among several that a perspective
holds on the same divergence d_i from its target. A16's single τ_i ran
them together. Kept apart:

| tolerance | crossing it means | held in |
|---|---|---|
| τ_i^acc, acceptance | i no longer accepts w; the sign of its conferral turns | [CLAIM-552](CLAIM-552.md) |
| τ_i^act, activation | i is active, without necessarily acting | [CLAIM-550](CLAIM-550.md); [TERM-053](../terms.d/TERM-053.md)'s note of 2026-11-04 |
| τ_i^int, intervention | i takes an action on the current state | U17, as the owner clarified at review |

[CLAIM-550](CLAIM-550.md) is the formalization in this neighbourhood: from one
activation threshold θ it derives, for each response level ε, a
different tolerance on the same discrepancy, (θ + κ⁻¹ logit ε − b)/α. So
a ladder of tolerances on one divergence is what a graded response
already gives. Nothing fixes their order. A perspective with
τ_i^acc < d_i(w) ≤ τ_i^int no longer accepts w but does not mobilize,
and is quiet with its channel working, which is [CASE-129](../cases.d/CASE-129.md)'s third quiet
arm, the raised threshold.

The acceptance set is A_i = {w : d_i(w) ≤ τ_i^acc}. The propensity to
intervene is graded on the intervention tolerance:

  q_i(w) = σ(κ_i[d_i(w) − τ_i^int]),

the probability that i mobilizes to intervene, given that it has
recognized the discrepancy and has a channel. τ_i^int is the discrepancy
at which q_i = ½.

**The channel is separate (A16 §2).** The intervention that can be
observed is p_i(w) = s_i(w) q_i(w). Here s_i is the chance that the
discrepancy is legible ([TERM-064](../terms.d/TERM-064.md)) and a channel carries the intervention.
A16: "This factorization is an assumption about the communication
mechanism; it is not a general identity." It "lets us distinguish a
tolerant perspective from a silenced perspective." A15's opening:
"silence cannot automatically count as endorsement." An intervention that is taken up and lowers the current will's influence
is negative conferral ([TERM-103](../terms.d/TERM-103.md), formerly [TERM-053](../terms.d/TERM-053.md)'s endorsement). An intervention with no channel is
not, and neither is its absence.

**The complex (A16 §5).** 𝒦_τ = {S ⊆ P : some attainable history's will
lies within τ_i^acc for every i in S}. It is downward closed, as in
[CLAIM-347](CLAIM-347.md). Pairwise compatibility does not give joint compatibility, as
in [CASE-119](../cases.d/CASE-119.md). The budget form, three perspectives sharing two units, is in
[CASE-119](../cases.d/CASE-119.md)'s note of 2026-11-04.

**Observed against required (A16 §7).** A second complex, of the wills at
which observed intervention rates stay below set bounds, can be larger
than 𝒦_τ. Disabling a channel enlarges it with no change in any
acceptance condition. Threshold and channel part only under
intervention: a changed threshold "should shift the response to
discrepancies under a fixed channel; suppression should change the
channel's efficacy while the underlying rejection remains". This is
[CLAIM-364](CLAIM-364.md) and [CASE-129](../cases.d/CASE-129.md), and [THEORY-152](../theory.d/THEORY-152.md)'s voice as a feedback channel.

**Read through Frankfurt (the reader's).** [THEORY-120](../theory.d/THEORY-120.md) holds Frankfurt's
2004 condition first-hand: "no conflict in us between this motive and any
desire at any higher order" ([LIT-293](../literature.d/LIT-293.md), p. 178), with identification as
willing acceptance. It reports his later "satisfaction", "an absence of
'restlessness or resistance'" ([LIT-296](../literature.d/LIT-296.md), n. 1, by report). Both are about
the will that moves the agent to act, not about whether the agent acts or
complains. In this construct:

- an individual is wholehearted at w when w, the will it acts on, lies
  within every maintained perspective's acceptance tolerance, relative to
  its target: d_i(w) ≤ τ_i^acc for all i. That is the full face of 𝒦_τ, the requirement complex at the
  declared tolerances. A wholehearted individual can act vigorously; what
  it lacks is a perspective set against the will it acts on;
- quiet is not wholeheartedness. A perspective past τ_i^acc does not
  intervene if it is below τ_i^int or its channel is lost (s_i ≈ 0), yet the conflict Frankfurt's
  condition excludes is there. Quiet counts as evidence only when the
  channel is known ([CASE-129](../cases.d/CASE-129.md)). Mapping wholeheartedness onto the quiescent
  complex would have contradicted this claim's own point, that not
  intervening is not endorsing; by [CLAIM-549](CLAIM-549.md) the two complexes can
  differ;
- an individual whose 𝒦_τ lacks the full face cannot act wholeheartedly
  with any attainable will, whatever higher-order volition
  ([TERM-102](../terms.d/TERM-102.md)) it forms. Its minimal non-faces are its minimal
  ambivalences;
- it can become wholehearted only by changing a demand: a raised τ_i^acc,
  or a new target. Frankfurt's willing acceptance "may be resigned"
  ([THEORY-120](../theory.d/THEORY-120.md)). In this construct resignation is a raised tolerance, a
  perspective that now accepts w, not one that has been silenced. By
  [CLAIM-347](CLAIM-347.md) that is a change of demand, not relief. Whether it still
  counts as identification is the dispute [THEORY-120](../theory.d/THEORY-120.md) records between
  [LIT-291](../literature.d/LIT-291.md) and [LIT-293](../literature.d/LIT-293.md) (p. 173);
- the graded q_i gives a graded form of what [THEORY-120](../theory.d/THEORY-120.md) makes all or
  nothing: how far past its tolerance each dissenting perspective is.
  That meets [THEORY-054](../theory.d/THEORY-054.md)'s objection inside Frankfurt's own criterion.

Wholeheartedness is thus judged on the acceptance tolerance alone. The
intervention and activation tolerances say whether a perspective that has
stopped accepting will show it.

The filing of 48d2ca5 mapped wholeheartedness onto quiescence below both
thresholds. The owner questioned that at review, and it is withdrawn: it
read an absence of conflict as an absence of signal.

## What it does not say

- **That the perspectives' acceptance is the person's identification.** A
  perspective's volition is not the person's. A14 §5: "That attribution
  is precisely the ownership problem we haven't settled." That is
  [QUESTION-071](../questions.d/QUESTION-071.md) and [CLAIM-022](CLAIM-022.md).
- **That the satisfaction reading is Frankfurt's.** [LIT-695](../literature.d/LIT-695.md), where
  satisfaction is introduced, is unread. The reading rests on report.
- **That a full face makes an individual.** A16 §8: a population can share
  a jointly acceptable will with no maintained organization, and an
  individual can stay unified with an incomplete complex.
- **That raising a threshold relieves frustration.** By [CLAIM-347](CLAIM-347.md), it
  changes the demand.
- **That the logistic is a psychological law.** A16 calls it "a modeling
  convention, not an empirically established psychological law."

## Note of 2026-11-07: cited for silence, without legibility, from "Individuation, Possibility, and Disposition"

A47 §4 cites this claim for "observed acquiescence does not establish dispositional agreement", which is its "a perspective that does not intervene has not thereby endorsed". A47 drops the legibility factor ("the chance that the discrepancy is legible") and adds a stage of granted authority, which is [CLAIM-283](CLAIM-283.md)'s, not this claim's. No change.
