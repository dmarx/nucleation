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
- CASE-tmpxqgai
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

<!-- inactive-ok-file: LIT-1122 — Deferred; open claims, readings and works registered unread, cited as open, nothing here rests on their being settled -->
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
constructions ([CASE-tmpxqgai](../cases.d/CASE-tmpxqgai.md)). Arm A, a slow register no member reads, is
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
