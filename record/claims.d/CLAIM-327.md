---
number: 327
status: Proposed
formerly:
- CLAIM-tmp11auq
title: 'A slowly changing collective variable, such as a reputation, a rivalry or a standing, is part of a collective''s dynamics and not only an observer''s average when its members read it, condition what they do on it, and by doing so regenerate it'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  In the cases offered for it, the slow variable's predictive role
  vanishes once the common external drivers and the members' own
  histories are modelled; or interventions on members' access to the
  variable (what new members are told, what is published about it) leave
  their later behaviour and the variable's later course unchanged where
  the claim predicts a change.
tags:
- complex-systems
- social-ontology
date: '2026-10-16'
line:
- distributed-agency
grounds:
- CASE-103
- CASE-102
- CASE-116
complements:
- CLAIM-277
- CLAIM-331
summary: >-
  A9 §3 and §10 of the exchange of 2026-10-16, after Flack 2012
  (LIT-1122, unread). Three stages: an observer finds a stable
  statistic of fast interactions; members recognize it and use it; their
  use preserves or regenerates it. Only the third makes the variable an
  endogenous level. It is the general form of [CLAIM-277](CLAIM-277.md), where trust is
  the temporal regularity of endorsement that then steers endorsement. It
  does not say that such a variable individuates one collective: five
  slow variables sharing a referent may be five processes.
illustrated_by:
- CASE-098
---
<!-- inactive-ok-file: LIT-1840 LIT-1828 — Unavailable since 2026-10-29; the two Flack 2006 papers, cited in the note of that date as not reached, nothing here rests on them -->
# CLAIM-327: A slowly changing collective variable, such as a reputation, a rivalry or a standing, is part of a collective's dynamics and not only an observer's average when its members read it, condition what they do on it, and by doing so regenerate it

## The claim

A9 §3, after Flack's macaque work ([LIT-1122](../literature.d/LIT-1122.md), unread): "The critical step
isn't simply that an observer can compute a long-term average. The
animals themselves appear to use information encoded in these more stable
relationships to guide subsequent interactions." A9 separated three
stages:

1. **Statistical regularity.** An observer finds that many fast
   interactions yield a stable aggregate.
2. **Member-accessible structure.** Members recognize or estimate it and
   use it when choosing what to do.
3. **Self-reinforcing organization.** Behaviour conditioned on it
   preserves, transforms or regenerates it.

"A slow variable is not just something that changes slowly. It is
something whose history has become sufficiently stable and accessible
that components can organize their future behavior around it." A
fanbase's reputation ([CASE-103](../cases.d/CASE-103.md)) and a program's standing
([CASE-102](../cases.d/CASE-102.md)) are A9's examples: recruits, donors, visiting fans and
stewards condition on the accumulated past, and their decisions make the
future that sustains or changes it. "The time-averaged history has become
a contemporary causal influence."

The record holds a special case: [CLAIM-277](CLAIM-277.md), where durable trust is the
temporal regularity of endorsement and then directs endorsement. This
claim says what that case has in general, and gives [QUESTION-065](../questions.d/QUESTION-065.md) a
candidate for a target the system supplies itself: what its own members
condition on.

A9 §4 wrote the tests: timescale separation (τ_Z ≫ τ_X, not sufficient),
predictive usefulness over a matched baseline (I(Z_t; X_{t+h} | B_t) > 0,
which depends on the baseline), endogenous maintenance, and causal uptake
under intervention ("giving new students different narratives about a
university's traditional rival").

## What it does not say

- **Not that the variable individuates a collective.** A9 §7: five slow
  variables sharing a referent "could be produced by largely independent
  mechanisms that happen to reference the same sports team." Whether they
  form one collective needs a further test of integration, such as
  interventions on one changing the others through mechanisms internal to
  the collective.
- **Not that the information is new.** A9: if Z_t is computed from a
  history already in the baseline, "there is no additional Shannon
  information to gain"; its value may be economy or accessibility to
  bounded members.
- **Not agency.** A collective organized around a reputation need not be
  able to act.

## Note of 2026-10-18: endogeneity without slowness

The exchange of 2026-10-17 re-derived this claim's separation of slowness
from endogeneity without citing it (A1 §1, A3, A4), and built it as
constructions ([CASE-116](../cases.d/CASE-116.md)). Arm A, a slow register no member reads, is
this claim's "timescale separation (τ_Z ≫ τ_X, not sufficient)" made a
construction. Arm B is the converse, which the claim lacked. Members read a
register and rewrite it (Z_{t+1} = Z_t ⊕ N₁, with N₁ ~ Bernoulli(0.4)).
Its second eigenvalue is 0.2, so it forgets on the members' own timescale,
and do(Z_t) changes the next value (0.4 against 0.6). So timescale
separation is not necessary for the third stage either, for weak
maintenance. A4's limit: "This demonstrates only *weak* endogenous
maintenance. If maintenance is defined to require robust long-term
persistence, this counterexample no longer establishes the separation."
The claim is about slowly changing variables, so arm B does not cut
against it. It says the test list should not read slowness as a
requirement of endogeneity. [CLAIM-331](CLAIM-331.md)'s "slowness is a mark of a level
and not its definition" says the same for levels.

## Note of 2026-10-27: Flack 2017 read, and the third stage is not hers

Flack's general statement ([LIT-1630](../literature.d/LIT-1630.md), read in [NOTE-1216](../notes.d/NOTE-1216.md);
[THEORY-1061](../theory.d/THEORY-1061.md)) changes how this claim's attribution should be read. Stage
two, members recognizing and using the variable, is what she calls apparent
downward causation, with two refinements the claim lacks. Members condition
on their own *estimate*, which may be wrong and need not be shared, and one
member tuning is enough (§§1, 3). Stage one has no separate place: the
variable is computed by the members from the start, "endogenous
coarse-graining" (§2). Stage three, use regenerating the variable, is in
neither of her lists of criteria (§1, §7). What reinforces itself in Flack is
agreement among members' estimates: "positive feedback induced by the
downward causation itself" (§3). And where the claim says only the third
stage makes an endogenous level, Flack says use alone is weak downward
causation, and a new level needs her strong criteria: predictive, robust,
used nearly universally, agreed on, with rising micro–macro mutual
information (§1). So the three stages are the exchange's synthesis of 2026-10-16,
with regeneration where Flack has convergence. The claim's content may still
be right; it is not Flack's. Flack 2012 ([LIT-1122](../literature.d/LIT-1122.md)), which this paper defers
to, stays unread.

## Note of 2026-10-29: Flack 2012 and computational mechanics, read

Flack 2012, [LIT-1122](../literature.d/LIT-1122.md), is now read ([NOTE-1351](../notes.d/NOTE-1351.md)), so the summary's
"unread" and the last sentence of the note of 2026-10-27 no longer hold.
Its words match A9's "appear": that the animals read and condition on the
slow variable is what "the data suggest", argued from earlier studies,
and for relative power not yet worked out. Against the claim's three
stages:

1. Statistical regularity is shown, for the signal network.
2. Member accessibility is asserted, not shown.
3. Regeneration is the paper's §4 argument that fighting lowers after
   signals and so consolidates the relation. No measurement in the paper
   supports it.

So the paper this claim quotes is evidence for the first stage only.

Shalizi and Crutchfield, [LIT-1126](../literature.d/LIT-1126.md) ([NOTE-1372](../notes.d/NOTE-1372.md)), bear on A10's offer of
causal states as "the minimal history a collective must keep to predict
its future". The reading adds two limits to the slow state that offer
names. The theorems need the observed process fixed in advance and
stationary, and the authors call relaxing stationarity "unclear", which a
collective under turnover may need. And the causal states are minimal
only for the whole future: for a finite horizon a coarser state can
predict as well, so "the" slow state depends on the horizon of
prediction.

The claim stays Proposed.

## Note of 2026-10-29: the two Flack 2006 papers, not reached

Two of the earlier studies Flack 2012 argues the second stage from are now
registered, and both are Unavailable: no lawful copy was reached.

- **Flack and Krakauer 2006**, "Encoding power in communication networks",
  [LIT-1840](../literature.d/LIT-1840.md), which builds the power measure from the signalling network
  and relates it to how others solicit and accept intervention. Whether it
  shows members conditioning on the consensus rather than on the signals
  themselves turns on its methods.
- **Flack, Girvan, de Waal and Krakauer 2006**, "Policing stabilizes
  construction of social niches in primates", [LIT-1828](../literature.d/LIT-1828.md), the knockout
  of policing that Flack 2012 rests part of its argument on, and the one
  intervention in the literature this claim draws on.

So the second stage still has no evidence the record has read. One thing
can be said from the descriptions alone. The knockout removed the
policers, an input to the power structure, not members' access to a slow
variable. Even a clean result would bear on the third stage, regeneration,
more directly than on the second, and it is not the intervention the
defeated_if names.

The claim stays Proposed.
