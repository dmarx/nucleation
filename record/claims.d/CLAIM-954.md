---
number: 954
status: Proposed
formerly:
- CLAIM-tmph4j0u
title: 'Only randomized exposure separates class roles'
statement: >-
  In a simulated engagement network, only engagement under randomized
  exposure tells classes inferred, classes used and classes that reshape
  preferences apart: steering exposure by the classes raises concentration,
  fit and stability whether or not preferences move; the randomized-exposure
  gap stays put when preferences are fixed, grows when the classes steer
  exposure while users and creators adapt, and shrinks under the same
  adaptation without them
version: 1
role: thesis
warrant: empirical
defeated_if: >-
  In the laboratory as committed, or in a variant that changes only its
  scales (numbers of users and items, rates of adaptation and turnover,
  the strength of steering, K), the randomized-exposure gap moves when the
  classes steer exposure over fixed preferences, or grows as much under
  adaptation without the classes as with them; or a measure computed from
  the policy's own data (concentration, block-model fit to raw counts,
  stability, the closure defect) separates the three arms in the same
  order as the randomized-exposure gap. Not defeated by a real platform
  whose users do not adapt in this way: the claim is about what the
  measures can tell apart, not about any platform.
tags:
- network-science
- social-science
- individuation
date: '2026-11-22'
line:
- formal-apparatus
- distributed-agency
grounds:
- CASE-367
bears_on:
- QUESTION-028
- QUESTION-276
summary: >-
  From [LEAD-030](../leads.d/LEAD-030.md)'s run of [CASE-296](../cases.d/CASE-296.md)'s laboratory ([CASE-367](../cases.d/CASE-367.md)), four seeds
  in each arm. With genres planted in preferences, the in-class minus
  out-of-class engagement rate under uniform random exposure was 0.35 at
  the start and 0.36, 0.48 and 0.23 after fifteen periods with the classes
  steering exposure over fixed preferences, steering it while users and
  creators adapted, and adaptation without steering. Concentration of
  engagement in the class went from 0.42 to 0.90 in both steered arms. In
  the world where exposure alone made the clusters, the gap moved off zero
  (to 0.024) only when the classes steered exposure with adaptation. The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CASE-296 CLAIM-762 CLAIM-327 — Proposed; the case this study runs and the claims it bears on -->
<!-- inactive-ok-file: CASE-367 — new; the study this claim reports -->

# CLAIM-954: Only randomized exposure separates class roles

## The claim

[CASE-296](../cases.d/CASE-296.md) proposed a laboratory to separate three kinds of class: classes
inferred and never used, classes used to steer exposure while preferences
stay fixed, and classes used while users and creators adapt.
[CASE-367](../cases.d/CASE-367.md) ran it, with a fourth arm the lead's criterion needs:
the same adaptation with the classes not used.

- **Inferred against used.** At the end, against the unsteered arm,
  steering had raised concentration (0.40 to 0.90), the block model's fit
  to raw counts (3.6 to 41.1 millinats per cell) and the stability of
  re-inferred classes (0.49 to 0.89). It left
  the randomized-exposure gap where it was, to every digit, because the
  preferences had not moved. Every observational measure registers use.
- **Used against reshaping.** With adaptation the gap rose from 0.35 to
  0.48, and the true gap in engagement probability rose with it (0.34 to
  0.47). Concentration was 0.90 in both arms and cannot tell them apart.
- **Reshaping by use against adaptation alone.** Without steering, the
  same adaptation lowered the gap to 0.23: users drawn toward what they
  engage with, under exposure that crosses genres, drift across them. The
  closure defect turned negative in both adaptive arms, since it registers
  that preferences homogenized within classes, not that the classes
  separated. Only the randomized-exposure gap separated them.
- **Where exposure made the clusters**, the gap was zero and stayed zero
  under every arm but one: steering with adaptation moved it to 0.024
  [0.015, 0.034], against 0.005 [0.000, 0.012] for adaptation alone.

So in this model the classes reshape preferences only when used, which is
what [LEAD-030](../leads.d/LEAD-030.md) said would count for [CLAIM-762](CLAIM-762.md)'s reading, and the
randomized-exposure arm ChatGPT proposed at its review of [CASE-296](../cases.d/CASE-296.md) is
the measure that shows it. Used with adaptation, the class is in this model
[CLAIM-327](CLAIM-327.md)'s self-reinforcing collective variable: the platform reads it,
conditions exposure on it, and by doing so regenerates it.

## What it does not say

That real genres are reshaped. The simulator was built with users who
drift toward what they engage with and a recommender that channels
exposure; the claim is that the laboratory's measures can tell the cases
apart where the cases are known, and which measures cannot. It does not
say how large the effects are on any platform, or that randomized exposure
of 20 items per user is affordable there. It does not say the reshaped
classes are real kinds: whether a class confirmed through its own use is
one is [CLAIM-402](CLAIM-402.md)'s question, and this result is an instance of
[CLAIM-402](CLAIM-402.md)'s worry, not an answer to it.

## Note of 2026-11-25: where this result sits in [CLAIM-402](CLAIM-402.md)'s decomposition, from the review of the manuscript governance-of-becoming, Part III
<!-- inactive-ok-file: CLAIM-415 SYNTHESIS-062 — Proposed; the claim whose note gives the person-scale forms, and the account that declines neighbouring mappings onto CLAIM-402, cited with their standing -->

The manuscript's Article 7 (§7.5, join J7.3) read [CASE-367](../cases.d/CASE-367.md)'s arms as the
model form of [CLAIM-402](CLAIM-402.md)'s two feedbacks, the fixed-preference arm as
apparent confirmation by the reading regime and the adaptive arm as a
changed referent, and at the person's scale as self-sealing against
self-fulfillment. The review of Part III (2026-11-25, Part B), whose
independent reader tested the joins under [ADR-075](../decisions.d/ADR-075.md), found that this
misstates two components, and that what survives is this claim's title.
The residue, as the review states it:

- **The randomized probe is [CLAIM-402](CLAIM-402.md)'s second separating intervention,
  inside the performative term.** [CLAIM-402](CLAIM-402.md)'s note of 2026-10-24 splits
  the change in what is learned from into Σ K_r dD_u/dθ, performative
  change of the world sampled, and Σ (dK_r/dθ) D_u, endogenous change of
  how it is represented, and names the intervention that separates them:
  "change the policy with raw outcomes observed independently". Engagement
  under randomized exposure is that intervention.
- **The case holds the reading regime fixed, so it has no arm for the
  representational term, and none for interpretive self-sealing.**
  [CASE-367](../cases.d/CASE-367.md)'s classes are "Inferred once … then held fixed", so
  dK/dθ = 0 in every arm, and both arms lie in the performative term: in
  one, exposure changes what is sampled while preferences stay fixed; in
  the other, preferences move too. Mapping the arms onto [CLAIM-402](CLAIM-402.md)'s two
  terms would need exposure counted as part of the reading regime, a free
  parameter of the kind [SYNTHESIS-062](../syntheses.d/SYNTHESIS-062.md) declines for neighbouring mappings
  onto [CLAIM-402](CLAIM-402.md). Interpretive self-sealing ([CLAIM-415](CLAIM-415.md)'s note, A10 §8:
  "Whatever I do is taken as confirmation, regardless of whether my
  character changes") is a changed reading of fixed behaviour; in the
  fixed-preference arm the behaviour, engagement, does change, steered by
  exposure, while the reading is fixed, so that arm is not self-sealing.
  The adaptive arm illustrates self-fulfillment; adversarial constitution
  has no arm.
- **Re-inferring the classes under use would be the representational
  arm.** A rerun of [CASE-367](../cases.d/CASE-367.md) in which the classes are inferred again from
  the engagement the steering produced would vary K_r with θ, and so test
  the term this run holds at zero.

This is consistent with the sentence above, that the result "is an
instance of [CLAIM-402](CLAIM-402.md)'s worry, not an answer to it". No change of status.
The wording is the assistant's (Claude, in this session); adopting it is
the owner's call.
