---
number: 902
status: Active
formerly:
- THEORY-tmp6h1sd
title: 'In Friedkin, Jia and Bullo''s study of 30 four-person student groups discussing 15 choice dilemmas, a member''s self-reported closure to influence on the next issue rose with their influence centrality on the previous issue, an effect constant along the sequence, and with their average centrality over all prior issues, an effect that grew along it; influence networks thinned and discussions shortened while the rate of consensus did not change. Closure and centrality both come from the members'' own chip allocations, and prior closure is not controlled'
version: 2
history:
- version: 2
  date: '2026-10-30'
  note: >-
    Narrowed and promoted by the status review of 2026-10-30, at the status
    review's ruling (the owner delegated these rulings; ADR-065, ADR-057;
    ADR-047's evidence ruling), the source read in full in NOTE-1126.
    Narrowed: attributed to the study, its measures and its uncontrolled
    prior closure stated, and the "increasingly so" clause split into the
    constant prior-issue effect and the growing time-averaged one, as
    NOTE-1126 reads Table 2 (a mis-statement corrected, ADR-047 kind 3).
    Dropped: "evidence for a reflected-appraisal step by which influence
    concentrates in deliberating groups", which the authors assert and which
    NOTE-1126 rates weak (C5, C6). The old title: In 30 four-person student
    groups discussing 15 choice dilemmas, a member's self-reported closure
    to influence on the next issue rose with their influence over prior
    outcomes, increasingly so along the sequence, and the groups' influence
    networks thinned and their discussions shortened while the rate of
    consensus did not change: evidence for a reflected-appraisal step by
    which influence concentrates in deliberating groups. The old
    promote_when: A replication in other groups, with influence measured
    otherwise than by the members' own allocations (observer coding, or
    opinion movement alone), showing that a member's closure to influence on
    the next issue rises with their prior influence even when their own
    prior closure is controlled for; and an experiment that manipulates the
    feedback members receive about their influence and moves their later
    closure. It is refuted if, with prior closure controlled, prior
    influence no longer predicts later closure, or if feedback about
    influence leaves closure unchanged. More issue-sequence data from
    self-reports alone cannot settle it. The wide form, which the source
    asserts, is kept as THEORY-1212, Proposed, which extends this entry
    and inherits the promote_when word for word (ADR-047, kind 1).
tags:
- social-science
- network-science
date: '2026-10-24'
source:
- LIT-1482
summary: >-
  Friedkin, Jia & Bullo (2016), [LIT-1482](../literature.d/LIT-1482.md), read in full from the CC BY
  version of record and its supplement in [NOTE-1126](../notes.d/NOTE-1126.md). Friedkin–Johnsen
  dynamics on each issue, not DeGroot. Closure and centrality both come
  from members' post-discussion chip allocations, and prior closure is not
  controlled. Supports the individual step and some structural trends; the
  predicted end state, one closed member and consensus on that member's
  view, was not reached.
supports:
- CLAIM-448
---
<!-- inactive-ok-file: THEORY-1212 — Proposed; the wide form kept beside this narrowed reading (ADR-047, kind 1) -->
<!-- inactive-ok-file: CLAIM-448 CLAIM-403 THEORY-916 LIT-1146 — Proposed or Deferred; the claim, account and companion work this bears on, named, nothing here rests on them -->

# THEORY-902: In Friedkin, Jia and Bullo's study of 30 four-person student groups discussing 15 choice dilemmas, a member's self-reported closure to influence on the next issue rose with their influence centrality on the previous issue, an effect constant along the sequence, and with their average centrality over all prior issues, an effect that grew along it; influence networks thinned and discussions shortened while the rate of consensus did not change. Closure and centrality both come from the members' own chip allocations, and prior closure is not controlled

## Source

Friedkin, Jia & Bullo, [LIT-1482](../literature.d/LIT-1482.md), read in full in [NOTE-1126](../notes.d/NOTE-1126.md) from
the version of record: pp. 452–471, Tables 2–6 and Figures 4–13, with
supplement Sections S1–S4.

## What was actually shown

120 undergraduates in groups of four discussed 15 choice dilemmas each.
After every discussion each member split 100 chips between how far the
discussion had and had not influenced their final opinion, and the first pile among the others. That gives each
member's closure (the second pile) and, through the Friedkin–Johnsen
model, each member's influence centrality on the outcome.

- **The individual step.** Prior centrality predicted closure on the next
  issue (Table 2, n = 1,680). The effect of time-averaged centrality grew
  along the sequence. The chance of complete closure rose with it
  (Fig. 6).
- **Structure.** Discussion time fell by about 0.9 minutes per issue
  (Table 4). Network density fell from 84% to 67% by issue 11 (Fig. 11).
  The dominant eigenvalue of the influence matrix and its trace declined
  (Figs 10, 13).
- **Not shown.** "In our data, the probability of reaching consensus does
  not alter along the issue sequence" (p. 467). About a third of
  discussions each ended in disagreement, consensus on an initial opinion,
  and compromise.

What could have come out otherwise: closure on the next issue could have
been unrelated to prior influence, as a fixed-personality view expects,
and networks could have densified with interaction, as the usual
sociological expectation has it. Neither happened.

## What this does not say

- **That reflected appraisal is the cause.** Closure and centrality come
  from one self-report, closure persists across issues, and Table 2 does
  not control for prior closure. Stable individual differences could
  produce part of the association. Nothing manipulated perceived
  influence.
- **That groups become autocracies.** That is the model's attractor
  (all 14,000 simulated systems, S1) and the authors' extrapolation. The
  data give "signals".
- **That the dynamics are DeGroot–Friedkin.** The single-issue model here
  is Friedkin–Johnsen, with anchoring. [THEORY-916](THEORY-916.md) holds the DeGroot
  version's theorems, whose end state differs.
- **That concentration is bad or good.** The authors decline to say
  whether the efficiency gained goes with more or less collective
  intelligence (S11).

## Connections

- **[CLAIM-448](../claims.d/CLAIM-448.md).** Supports its baseline, self-reinforcing
  authority, with data, and its point that faster settlement is not
  better integration. The thinning is of uptake: members stop weighting
  some others, rather than a regime keeping contests off the record
  ([CLAIM-403](../claims.d/CLAIM-403.md)'s ladder). The supplement's untested "reserved authority"
  argument complicates the claim's prediction for a protected challenge
  channel.
- **[THEORY-916](THEORY-916.md).** The same mechanism under DeGroot dynamics, proved
  rather than measured.
