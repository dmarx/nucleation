---
number: 342
status: Proposed
formerly:
- CLAIM-tmpt568z
title: 'What keeps a judgement–observation loop from confirming itself is evidence whose arrival or scoring does not pass through the interpretation it tests; action is one source of such evidence, not a necessary one, and a loop that selects its own evidence can lock in with action available'
version: 2
history:
- version: 2
  date: '2026-10-21'
  note: >-
    Note of 2026-10-21 added, from the exchange of 2026-10-20 on effective
    description, agency and legibility: A20–A23 restated this claim's anchor
    for public knowledge and institutions (its second to fifth appearances),
    and A26 built a performative toy with two stable self-confirming
    classifications (CLAIM-402, CLAIM-404). Extended the same day from the readings of Weatherall, O'Connor and Bruner and of Espeland and Sauder. The claim is
    unchanged.
role: thesis
warrant: interpretive
defeated_if: >-
  A loop whose evidence is scored independently of the interpretation it
  tests, or whose per-context marginals are fixed from outside, shown to
  lock in all the same. Or a showing that the only evidence an agent can
  receive that does not pass through its own interpretations arrives
  through its own action on the world. A showing that action is a common
  or efficient source of such evidence does not defeat it.
tags:
- cognition
- probabilistic-modeling
- psychopathology-and-treatment
date: '2026-10-16'
line:
- distributed-agency
- pragmatic-transport
rests_on:
- CLAIM-330
- CLAIM-141
grounds:
- THEORY-285
- THEORY-324
- LIT-1181
objects_to:
- CLAIM-339
complements:
- CLAIM-341
- CLAIM-338
- CLAIM-357
- CLAIM-359
- CLAIM-427
summary: >-
  The assistant's synthesis, A3 and A4 of the exchange of 2026-10-16,
  filed at the owner's request at U5. Three results the record already
  holds. [CLAIM-330](CLAIM-330.md): capture in the operator model needs both arrows of
  [CLAIM-297](CLAIM-297.md)'s circuit, and scoring operators independently of the
  dominant interpretation removes it. [CLAIM-141](CLAIM-141.md): a loop always has a
  distributional fixed point, so what binds it is a constraint that
  prescribes marginals. [THEORY-285](../theory.d/THEORY-285.md) ([NOTE-766](../notes.d/NOTE-766.md)): an active-inference agent
  locks in with action available, because its own sampling policy
  withholds the evidence that would correct it. The claim does not say
  action is unimportant, only that it is not what does the anchoring.
supports:
- CLAIM-402
- CLAIM-404
- CLAIM-413
---
<!-- inactive-ok-file: THEORY-854 — Proposed; Espeland and Sauder's loop stated generally, cited in the note of 2026-10-21, nothing here rests on it -->
<!-- inactive-ok-file: CLAIM-402 CLAIM-404 TERM-066 — Proposed; cited in the note of 2026-10-21, nothing here rests on them -->

# CLAIM-342: What keeps a judgement–observation loop from confirming itself is evidence whose arrival or scoring does not pass through the interpretation it tests; action is one source of such evidence, not a necessary one, and a loop that selects its own evidence can lock in with action available

## The claim

[CLAIM-339](CLAIM-339.md) objects to [CLAIM-341](CLAIM-341.md) that a judgement–observation loop
with no action has a self-confirming minimum: judge so that what is
observed confirms what is expected. The record already holds three results
that bear on that minimum.

- **It exists for every loop.** [CLAIM-141](CLAIM-141.md): "Passing from values to
  distributions creates solutions." A loop that feeds its outputs back as
  inputs has a self-consistent distribution whether or not it acts. What
  makes a fixed point wrong is a constraint from outside it that prescribes
  marginals, the kind a contextual empirical model imposes ([TERM-042](../terms.d/TERM-042.md)).
- **Action does not prevent it.** In the active-inference model of
  [THEORY-285](../theory.d/THEORY-285.md), the agent can act, and still "as long as the sensory
  attenuation policy is selected, no amount of observations will render
  prior beliefs obsolete" ([NOTE-766](../notes.d/NOTE-766.md)). The policy "withholds the only
  observations that could lower that precision", and what it attenuates
  is a "sensory or cognitive periphery". Lock-in comes from the loop
  selecting its own evidence, and action is one of the ways it selects.
  Friston et al. say so of action in general: it is "sampling selectively
  what one expects to experience", and the weakness this brings "becomes
  the strength" ([LIT-1181](../literature.d/LIT-1181.md), [NOTE-960](../notes.d/NOTE-960.md)).
- **Independent scoring prevents it.** [CLAIM-330](CLAIM-330.md) (Active, demonstrated): in
  the linearized operator model, capture starting at symmetry needs both
  arrows of [CLAIM-297](CLAIM-297.md)'s circuit, authority shaping interpretation and
  interpretation shaping endorsement. "Scoring operators independently of
  the dominant interpretation (Regime B, γ ≈ 0) removes the
  coupling-driven instability."

So what anchors the loop is evidence whose arrival or scoring does not run
through the interpretation it tests. Action on the world is one source of
such evidence: it brings in what the agent did not ask for. Others are a
source the agent does not select, such as an interlocutor, a scheduled
probe or a body state, and a scoring rule fixed independently of the
current interpretation. Ashby's ultrastability has the same structure: a
second channel, from the essential variables to the parameters of the
first loop, that the first loop's behaviour does not set ([THEORY-324](../theory.d/THEORY-324.md)).

## What it does not say

- It does not say an agent without action has independent evidence. The
  locked-in case asks whether one does ([CASE-107](../cases.d/CASE-107.md)). Damasio's
  re-enacted body states ([THEORY-500](../theory.d/THEORY-500.md)) and the visceromotor regulation
  that survives paralysis ([NOTE-434](../notes.d/NOTE-434.md)) are candidates.
- [CLAIM-330](CLAIM-330.md) is a linearization at symmetry. It shows what independent
  scoring removes near that point, not that it prevents every form of
  lock-in.
- It does not say what in a single mind plays the part of Regime B's
  independent scoring. [QUESTION-121](../questions.d/QUESTION-121.md) asks, with five candidates from
  the record: unselected input, the body, commitment before evidence,
  processing signals and other people. A paralysed person keeps the first,
  the second and the fifth inbound, so losing action need not mean losing
  the anchor.

## Note of 2026-10-18: re-derived as independent audit

The exchange of 2026-10-17 proposed this claim's thesis four times as a
design requirement, without citing it.

- A36 §4, on cryptographic commitments as "**independent endorsement
  audits**": a commitment protocol lets an auditor check that a prediction
  "was not changed retroactively", but "it only solves one problem: **the
  timing and integrity of the prediction**. It does not establish that the
  outcome is interpreted correctly, that the scoring rule is appropriate, or
  that the operator was exposed to representative evidence." That is
  [CLAIM-340](CLAIM-340.md)'s limit: commitment fixes when the prediction is made, not how
  the evidence is read.
- A39's second case study: "endorsement based on independent performance
  evidence versus endorsement scored through the interpretations whose
  authority is being evaluated", which A39 called "the best candidate for
  an early discriminating experiment".
- A40's Study C, key control: "Evaluate the demands using evidence
  independent of the processes whose authority is being assessed."
- A41's security table, whose row for independent audit reads "Prevent the
  actor being evaluated from controlling all the evidence of its
  competence", and its
  variant that would "compromise the processes responsible for evaluating
  other processes' competence. That tests whether the organization has any
  genuinely independent means of checking its own allocation of authority."
  That variant is in [CASE-108](../cases.d/CASE-108.md). It puts this claim under attack: the
  evidence that does not pass through the tested interpretation is itself
  scored by a process an insider may hold.

## Note of 2026-10-21: re-derived three more times, and a performative instance

**For public knowledge and institutions.** A21's criterion for media
capture in the exchange of 2026-10-20, "whether the processes conferring
epistemic authority can themselves be corrected by evidence independent
of the authority they confer", is this claim's anchor stated for public
knowledge. So is A20's "A formally independent review procedure does not
guarantee independent evaluation when the evidentiary standard itself is
controlled by the interests being evaluated". A22 added that the evidence
channel may be "governed by what it is evaluating". A23 §7 restated the
claim again without citing it: "An expert may gain influence because
their interpretations track independent evidence well. Alternatively, an
interpretation may acquire apparent evidential support because it
increasingly controls how evidence is selected and evaluated", so
"**independent evaluation requires attention to the legibility and
scoring of evidence, not merely formal separation between a decision-maker
and its evaluator**". Its audit table listed "Governance can make its own
evidence and authority self-reinforcing" as a new "Proposed institutional
interpretation". These are the second to fifth appearances. The
institutional form is filed as [CLAIM-404](CLAIM-404.md), which rests on this claim,
with [TERM-066](../terms.d/TERM-066.md) for capture.

**A performative instance.** A26 §2 built a toy in which a classification
fixes the policy that generates its own evidence:
θ_{t+1} = 1[P(Y = 1 | θ_t) > 0.5] with P(Y = 1 | θ) = 0.1 and 0.9. "Both
θ = 0 and θ = 1 are stable fixed points", each "consistent with the
behavioral evidence generated under that classification" (checked). It is
this claim's loop with no independent evidence: every observation passes
through the category under test. A26 tied it to Perdomo et al.'s
performative prediction ([LIT-1336](../literature.d/LIT-1336.md)) and Espeland and Sauder's
reactivity ([LIT-1330](../literature.d/LIT-1330.md)), both registered unread then and read the same day (below), and drew this claim's
conclusion: "stability and accuracy under the prevailing intervention
regime do not establish correctness under alternative regimes". A27
carried it into [QUESTION-028](../questions.d/QUESTION-028.md), filed as [CLAIM-402](CLAIM-402.md), which rests on
this claim.

**Two readings of the same day.** Weatherall, O'Connor and Bruner
([NOTE-1038](../notes.d/NOTE-1038.md)): their main remedy for a propagandist's selective sharing
is to hear more scientists, evidence that reaches the audience without
passing through the propagandist ([THEORY-855](../theory.d/THEORY-855.md)). Their audience's state
is one number, cumulative successes minus failures, fed by both channels
([THEORY-845](../theory.d/THEORY-845.md)), so the independent channel helps exactly as far as it
outweighs the selected one. Espeland and Sauder ([NOTE-1050](../notes.d/NOTE-1050.md)) report a
loop whose evidence passes through the interpretation it tests: the
reputation survey, in which raters score schools in part by the rank the
scores feed (Stake 2006 as they cite it; Schmalbeck 2001 contra), the
quantitative link cited, not shown ([THEORY-854](../theory.d/THEORY-854.md)). Perdomo et al.,
read the same day, are in [CLAIM-402](CLAIM-402.md).
