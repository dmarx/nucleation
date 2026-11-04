---
number: 53
status: Superseded
formerly:
- TERM-tmpij1jr
title: 'endorsement, between an organization''s processes: any effect one process has on another''s share of future influence, of which an explicit vote is one case'
version: 2
history:
- version: 2
  date: '2026-11-04'
  note: >-
    Superseded at the owner's decision (ADR-070). The definition is
    renamed conferral (TERM-103), and A14 §4's narrowing, conferral
    through a maintained relation, is adopted as grant (TERM-101).
    "Endorse" is left to the reflective sense (TERM-102). The body
    is kept as the history of the word.
superseded_by:
- TERM-103
- TERM-101
tags:
- self-governance
- social-ontology
date: '2026-10-13'
line: distributed-agency
summary: >-
  The owner's "vote" at U2, generalized at A5 §7 to an effective causal
  relation. Process i endorses process j in region x to the extent that an
  intervention of i raises j's chance of acquiring influence there.
  Opposition is negative endorsement. Attending to j's output, keeping it
  active, passing it resources and suppressing its rivals are all
  endorsement. The term is about authority among processes. It is not
  Frankfurt's identification with a desire.
used_by:
- CLAIM-285
- CLAIM-336
- CLAIM-375
---
<!-- inactive-ok-file: CLAIM-552 CLAIM-553 TERM-006 TERM-102 — Proposed, Deferred, Unavailable or new; cited from the exchange "Organizational Nucleation and SLT" of 2026-11-04 as open -->
<!-- inactive-ok-file: CLAIM-285 THEORY-120 — Proposed or Deferred; open claims, unread works and readings cited as open, nothing here rests on their being settled -->

# TERM-053: endorsement, between an organization's processes: any effect one process has on another's share of future influence, of which an explicit vote is one case

## Definition

The owner's design at U2 had the processes "essentially vote on how much
influence the other denoisers contribute". A2 began with an endorsement
matrix E_ij, a budgeted distribution of i's support over the others with
E_ii = 0. A5 §7 then asked whether endorsement requires explicit
evaluation: "Perhaps endorsement should be understood more generally as any
process that changes another operator's probability of acquiring influence."
Its examples: "Allocating attention to its output", "Maintaining its
activation", "Transferring representational resources", "Increasing its
eligibility to influence a decision", "Suppressing competing processes".

Counterfactually, E_ij(x, t) = ∂I_j(x, t + Δt)/∂u_i(t), where u_i is an
intervention available to i and I_j is j's influence in region x. A5:
"Positive values correspond to effective endorsement, negative values to
opposition." The budgeted vote is the special case in which the effect runs
through an aggregation rule.

The term distinguishes three quantities: the authority a process holds, its
endorsements of others, and how far its preferred policies are realized
([CLAIM-285](../claims.d/CLAIM-285.md)).

## What it is not

- Not identification. Frankfurt's endorsement is a person's higher-order
  attitude toward a desire ([THEORY-120](../theory.d/THEORY-120.md)). This is a relation between
  processes, and it may be subpersonal and not represented. A10 §2.3:
  "constitutive endorsement may be distributed, subpersonal, and not
  propositionally represented."
- Not agreement. A2 §8: a process "may endorse j's role as an error detector
  without endorsing j's authority over final policy selection."
- Not observable from behaviour alone. A7 §14: "Inferring trust or
  endorsement from observed causal facilitation may conflate authorization,
  incidental coupling, and common-cause effects." On r/place, A8 §7:
  "endorsement remains a latent explanatory hypothesis, not an observed
  variable."

## Note of 2026-10-18: being reinforced is not endorsing

The exchange of 2026-10-17 applied this term to training. A32 §4: "being
reinforced ≠ endorsing". "A network component may acquire greater influence
because the external optimizer makes it more effective. That's different
from the component influencing the future authority of other components
through an internally maintained endorsement relation." A32 also: "a gate
weight is not automatically an endorsement". A33 put it as a chain of three
kinds of object: "a gradient is not an update, and an update is not an
endorsement".

So, beside the three items above: **not an external update rule.** An
optimizer that raises a component's influence is not an endorsement of it
by any process of the organization, because the effect does not run from
an intervention available to another process. This is the clause above on
behaviour, applied to training: raised influence is observed, and who
raised it is the question. Where the governance of updates sits is
[CLAIM-367](../claims.d/CLAIM-367.md).

<!-- inactive-ok-file: CLAIM-367 — Proposed; filed or read from the exchange of 2026-10-17 and cited in the note of 2026-10-18 as open -->

## Note of 2026-11-04: a proposed narrowing, two thresholds, and the Frankfurtian sense, from "Organizational Nucleation and SLT"

**What the exchange asked.** The owner's U14: "concretely, I'm wondering if
our current definition satisfies the Frankfurtian sense, or if that is a
different sense we should consider." It does not, and this term says so.
A14 agreed, citing this term. The reflective sense is now coded as
[TERM-102](TERM-102.md), higher-order volition.

**A proposed narrowing (A14 §4).** "A positive influence derivative alone
would establish facilitation, but not necessarily endorsement." "We should
require some evidence that the causal effect is mediated by a maintained
relation of granting, delegation, eligibility, or support before
interpreting it as endorsement." This conflicts with "any effect" above,
which counts suppressing a rival as endorsement. It extends the note of
2026-10-18, which already excludes an external update rule. It is a
proposal for the owner's ruling. The definition is unchanged.

**Two thresholds (the reader of U17–U21).** A18 kept acting apart from
acting on the will: "punching the wall is an action, but it is not
necessarily an *attempt to revise the organization of the will*." A20 §1
said activation coupling "is not automatically endorsement in Nucleation's
causal-governance sense". In this term's sense a perspective has two
thresholds: one for acting at all, the owner's intervention threshold
(any action on the current state, as the owner clarified at review), and
one for endorsing or opposing, acting on another's share of future
influence. Wall-punching crosses the
first and not the second.

**The Frankfurtian misreading.**
- (a) A's earlier turns used "endorse" for the reflective attitude (A12 §1,
  "willing to endorse"; A15, "the will each perspective would endorse";
  A16, "the will it would endorse"). A14's four senses (evaluative, volitional, operative,
  constitutive) are a usable map. Its "constitutive" sense is [TERM-006](TERM-006.md)'s
  definition and the phrase quoted above from A10. A14's 2×2 table puts the
  unwilling addict in the cell with no operative endorsement. By [CASE-112](../cases.d/CASE-112.md)
  that is wrong: his volition can have a positive effect that falls short of
  switching the regime. What he lacks is success, not endorsement.
- (b) Read as intended, the owner's U12 "endorsement criteria" make a
  perspective's tolerance the switching surface of the sign of E_{i→j}
  ([CLAIM-552](../claims.d/CLAIM-552.md)). An intervention that is carried and taken up is
  negative endorsement, so the uptake of an intervention turns the
  reflective sense into this one. U15 first framed it as a complaint, and
  the owner recast that as an intervention threshold at U17 ([CLAIM-553](../claims.d/CLAIM-553.md); [QUESTION-270](../questions.d/QUESTION-270.md)).
- (c) The owner made no correction. At U15 the owner chose the Frankfurtian
  sense deliberately: "apply tolerance as a condition on the Frankfurtian
  sense."

No status changes.

**Tolerance as "local endorsement" (U11).** A11 is lost apart from its opening sentence.

The owner's U11: "what if we interpret these tolerances as measures of local endorsement?"

- **(a) The idea as A stated it.** A11's opening: "a tight tolerance can mean strongly endorsing a requirement, while a generous tolerance can mean endorsing another process's freedom to vary."
  - The first reading is the attitudinal sense, valuing or identifying with a demand. That is Frankfurt's sense ([THEORY-120](../theory.d/THEORY-120.md)), which this term excludes. It is worth recording only as the reading to rule out.
  - The second reading comes close to this term if it is cashed out causally.
  - A9 had already said a tolerance "is neither an endorsement weight", without saying in which sense.
- **(b) Read as intended.** Within i's tolerance at an overlap, E_ij ≥ 0. Beyond it, i may act to lower j's future influence, E_ij < 0. The tolerance is then i's *criterion* of endorsement in this term's causal sense. It is a necessary condition of non-opposition, not a measure of how strongly i endorses j.
- **(c) The owner's correction.** The owner's U12: "i was thinking more along the linesof tolerances expressing endorsement criteria relative to some given perspective's priorities. maybe I'm confusing necessary vs sufficient conditions." This agrees with (b). Being within tolerance is at most necessary for E_ij ≥ 0. It is not sufficient for positive endorsement, which needs an intervention by i that raises j's influence. [CLAIM-552](../claims.d/CLAIM-552.md) holds the owner's reading.
