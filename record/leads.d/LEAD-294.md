---
number: 294
status: Open
formerly:
- LEAD-tmpe579v
title: "Replay forgetting policies over the record's history: at past dates, cool by age, standing, recent activity, structural reachability or a combination, using only what was known then, and measure which later-used entries each would have cooled and at what recovery cost"
version: 1
history:
- version: 1
  date: '2026-11-26'
  note: >-
    Filed from A34's sixth pilot, with A33 §§10 and 15, of the exchange
    "Alignment consequences brainstorm" (ChatGPT, 2026-11-26). The
    equal-budget comparison, the outcome definitions and the criteria are
    the assistant's (Claude, in this session).
stage: costed
method:
- empirical
- historical
tags:
- information-retrieval
- design-rationale
- epistemology
date: '2026-11-26'
line:
- record-as-apparatus
advances:
- CLAIM-1394
- QUESTION-552
- CLAIM-1361
presupposes:
- LEAD-305
- LEAD-289
summary: >-
  A34: "reconstruct earlier snapshots of Nucleation and simulate several
  retention policies using only the information available at those
  dates", and "Measure which later-used distinctions would have been
  cooled, how expensive their recovery would have been, and how much
  ordinary retrieval burden might have been avoided." Its payoff is to
  "empirically test the generational hypothesis and calibrate retention
  policies without prematurely adopting them" (CLAIM-1361). A33 §10 adds the survival analysis, with
  recent entries "right-censored". A34's own limit: replay "cannot reveal
  all the inquiries that might have emerged under different retrieval
  policies", so prospective trials ([LEAD-307](LEAD-307.md)) follow it. The pilot is
  A's; the comparison and criteria are the assistant's (Claude, in this
  session), and adopting them is the owner's call.
---
<!-- inactive-ok-file: CLAIM-1361 — Proposed; section 4's entries of the same filing, cited on 2026-11-26 -->

# LEAD-294: Replay forgetting policies over the record's history: at past dates, cool by age, standing, recent activity, structural reachability or a combination, using only what was known then, and measure which later-used entries each would have cooled and at what recovery cost

## The replay

At each weekly snapshot date `t` from [LEAD-305](LEAD-305.md)'s log, each policy
cools a fixed share of the claims alive at `t`, the same share for all, so
that the policies are compared at equal budget. A34's five:

- **age**: the oldest claims with no non-mechanical event in 14 days;
- **standing**: Superseded, Rejected and Deferred first, then Proposed
  claims no Open lead advances;
- **recent activity**: lowest interaction intensity at τ = 30 days;
- **structural reachability**: outside [LEAD-289](LEAD-289.md)'s root closure as it
  stood at `t`;
- **combined**: outside the closure and lowest in activity.

## The outcomes, over the 30 days after `t`

- **Later use** of a cooled claim: a new incoming relation, a substantive
  revision, an ARG concluding it, a synthesis integrating it, or its code in
  the prose of a new entry. Each later use is one recovery.
- **Recovery cost**: the size in tokens of what a recovery reads (the
  claim and the cooled premises it rests on).
- **Avoided burden**: the size in tokens of the cooled claims, a proxy for
  what ordinary retrieval no longer meets.
- A34's failure modes, counted by kind among the later-used cooled claims:
  old foundational results; negative knowledge (Rejected claims used
  again); stable anchors; claims that later seed new directions (new leads
  or questions on them); and claims cooled by several policies at once,
  which is A34's "several apparently independent signals reinforce the
  same historical visibility bias".

Survival by cohort of filing week, right-censored at the last snapshot: the
chance of first downstream use, of integration, and of supersession, by
age. That is the generational hypothesis's test on this record: whether a
nursery period exists, A33's "Perhaps ninety percent of claims that will
acquire downstream dependencies do so in their first month."

## What would count

- **For calibrating a policy:** at least one policy cools 30 % of claims
  with fewer than 5 % of them later used, and beats age-based cooling on
  that rate at every snapshot after the record's third week.
- **Against cooling by these signals:** every policy's later-use rate among
  cooled claims is within a factor of 1.5 of the base rate of later use
  among all claims. History then does not predict use well enough to cool
  by it.
- **For the generational hypothesis:** first downstream use concentrated
  early, most of it in the first two weeks of a claim's life; against: a
  hazard flat or rising with age.

## What it cannot show

What would have been asked under a different policy (A34). And anything
beyond the record's age: on 2026-11-26 the oldest claim was under two
months old, so a nursery period longer than a few weeks cannot be seen.

## Cost

Once [LEAD-305](LEAD-305.md) and [LEAD-289](LEAD-289.md) exist: a day for the replay and the
survival curves.
