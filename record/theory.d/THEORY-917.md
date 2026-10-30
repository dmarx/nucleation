---
number: 917
status: Active
formerly:
- THEORY-tmphx93a
title: 'Chou, Wilson and Smith read about eight computational studies of exploration in reward-based bandit tasks, mostly in sub-clinical samples, with mixed results and none replicated, as suggesting that directed exploration rises with trait or cognitive anxiety and falls with state or somatic anxiety; none they review links random exploration to anxiety'
version: 2
history:
- version: 2
  date: '2026-10-29'
  note: >-
    Promoted by the thirteenth status review (ADR-057; ADR-047's
    evidence ruling, read in full in NOTE-1127). Narrowed: the pattern
    is the authors' hedged reading ("may", "could be seen to suggest"),
    and "shows no relation" becomes what the review reports, no study
    linking them. The old title: Across computational studies of
    exploration in reward-based bandit tasks, mostly in sub-clinical
    samples and not yet replicated, directed exploration tends to rise
    with trait or cognitive anxiety and to fall with state or somatic
    anxiety, and random exploration shows no relation to anxiety. The
    promote_when moves unchanged to QUESTION-330, as THEORY-285's
    did to QUESTION-303. CLAIM-446 no longer lists this reading in
    grounds, and its converse supports is removed (ADR-058): it is a
    reading that narrows its evidence-acquisition clause rather than
    supporting it. The claim's body still cites it.
tags:
- psychopathology-and-treatment
- learning-and-conditioning
- emotion-and-affect
date: '2026-10-24'
source:
- LIT-1483
bears_on:
- QUESTION-330
summary: >-
  Chou, Wilson & Smith (preprint June 2024; NBR 2024), [LIT-1483](../literature.d/LIT-1483.md), read
  in full from the PsyArXiv preprint in [NOTE-1127](../notes.d/NOTE-1127.md). A narrative review;
  the pattern is the authors' reading of about eight studies with
  different tasks, models and anxiety measures, with one failed
  replication and one null. The authors hedge it with "may" and "many
  results could be seen to suggest".
---
<!-- inactive-ok-file: CLAIM-446 — Proposed; the claim and companion reading this bears on, named -->

# THEORY-917: Chou, Wilson and Smith read about eight computational studies of exploration in reward-based bandit tasks, mostly in sub-clinical samples, with mixed results and none replicated, as suggesting that directed exploration rises with trait or cognitive anxiety and falls with state or somatic anxiety; none they review links random exploration to anxiety

## Source

Chou, Wilson & Smith, [LIT-1483](../literature.d/LIT-1483.md), read in full in [NOTE-1127](../notes.d/NOTE-1127.md) from the
PsyArXiv preprint, version 1 (24 June 2024): pp. 15–20 and 28–29. The
version of record is closed.

## What was actually shown

The review reports:

- More directed exploration with trait anxiety in a dynamic bandit (Aberg
  et al. 2022) and with generalized anxiety symptoms (Yan et al. 2023);
  more with cognitive anxiety and less with somatic anxiety in a spatial
  bandit under risk (Witte et al. 2024); less with somatic anxiety in two
  datasets of a two-armed bandit (Fan et al. 2023b).
- In the Horizon Task, less directed exploration with state anxiety,
  partly because anxious participants sought information when it was not
  useful (Smith et al. 2022c).
- Higher directed exploration in anxious depression than in low-anxiety
  controls, reduced to control levels by a breathing-based state-anxiety
  induction (Li et al. 2024; Goldman et al. 2024).
- No study linking random exploration to anxiety (p. 19).

The authors' summary: "many results could be seen to suggest that
trait/cognitive anxiety measures promote exploration, while state/somatic
anxiety deters exploration. However, findings are mixed" (p. 18).

What could have come out otherwise: anxiety could have gone with less
exploration across the board, as an avoidance account would most simply
predict. In these reward tasks it did not.

## What this does not say

- **That the pattern is established.** A positive finding "did not
  replicate in a second sample within a confirmatory study" (p. 18), a
  preliminary report found no association with worry or intolerance of
  uncertainty, and no replication of the main findings is reported.
- **Anything about exploration under threat.** These tasks reward points;
  nothing aversive is at stake.
- **Clinical anxiety.** Most samples are sub-clinical.
- **Why.** The authors' explanations (exaggerated uncertainty in trait or
  cognitive anxiety, felt urgency in state or somatic anxiety) are
  offered, not tested.

## Connections

- **[CLAIM-446](../claims.d/CLAIM-446.md).** Narrows the claim. Its defensive authority over
  evidence acquisition predicts less exploration; that fits the state and
  somatic facets, not the trait and cognitive ones, at least for reward.
  The Horizon result, information sought when it cannot be used, is the
  claim's "poorly governed information seeking" in one study.
- **[THEORY-907](THEORY-907.md).** The foraging half of the same review, where the
  direction is consistent.

## Note of 2026-10-30: the dropped clause

The old title ended "and random exploration shows no relation to
anxiety". That clause is not kept as a Proposed reading (ADR-047, kind
3). It was imprecise: the review reports that "no studies to date have
specifically linked random exploration to anxiety" (p. 19), which is an
absence of evidence, and NOTE-1127 rates it so. The old wording turned it
into a finding of no relation, which the review does not claim. The rest
of the old title, the facet pattern in directed exploration, is kept as a
Proposed reading that extends this one.
