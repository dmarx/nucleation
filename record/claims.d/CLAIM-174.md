---
number: 174
status: Proposed
formerly:
- CLAIM-tmpwv313
title: 'A candidate factor is an agent at a level when it is one system there, when a goal-directed description beats a device description by more than the Occam cost, and when its policy would adapt if its actions'' consequences changed; it is a willed agent when, further, a will-organization over several regimes describes it better than none, and what passes that is the jurisdiction of a will-organization'
version: 7
history:
- version: 2
  date: '2026-10-11'
  note: >-
    Split into an agent test (1–3) and a will test (4), after the owner
    distinguished willed agents from agents (CLAIM-155). In version 1,
    test 2 required governance over regimes. That requirement now belongs
    to test 4, so test 2 asks only for a goal-directed description. The
    thermostat verdicts are unchanged: alone it fails test 3; with its
    designers it is an agent but not a willed one, its will being the
    designers'.
- version: 3
  date: '2026-10-14'
  note: >-
    What it does not say now adds that test 3's verdict also depends on
    which changes count as adaptation (LIT-969, Claim 4), prompted by
    NOTE-793. The tests are unchanged.
- version: 4
  date: '2026-10-21'
  note: >-
    Note of 2026-10-21 added, from the exchange of 2026-10-20 on effective
    description, agency and legibility: A27 found a gap between conditions 3
    and 4 that test 3 already covers; its real point is that the
    governance-response profile (TERM-067) cannot stand in for test 3,
    and where authority is fixed from outside this claim's answer is the
    jurisdiction (TERM-047). The claim is unchanged.
- version: 5
  date: '2026-10-29'
  note: >-
    Note of 2026-10-29 added by the eleventh status review (ADR-057):
    CLAIM-154, on which this claim rests, is narrowed to candidates whose
    model stays regular at the switch-off, conceding CLAIM-188. The
    claim is unchanged.
- version: 6
  date: '2026-10-29'
  note: >-
    THEORY-092 moved from grounds to corroborated_by by the thirteenth
    status review (ADR-057, ADR-058). The note of 2026-10-12 added it
    as evidence that grounds test 3 'weakly', and its subject is
    intelligence, not agency; the tests do not stand on it.
    THEORY-092's supports entry for this claim is removed. The claim
    is unchanged.
- version: 7
  date: '2026-10-29'
  note: >-
    Concedes CLAIM-194 and CLAIM-393, at the status review's ruling (the
    owner delegated these rulings; ADR-057, ADR-059). From CLAIM-194:
    test 1 cannot tell a boundary the factor produces from one imposed on
    it, and tests 2 and 3 do not in general either, so an agent in this
    claim's sense (TERM-044) need not make its own boundary; minimal
    agency in Barandiaran, Di Paolo and Rohde's sense (THEORY-1119, the
    rival TERM-063) is a further condition the test does not claim. From
    CLAIM-393: ordinary and legal attributions of agency to an artifact
    are not independent marks where they turn on whether its mechanism is
    known. The defeated_if gains both exclusions, and What it does not
    say gains two bullets. The defeated_if was: "A factor that passes all
    three tests at a level and target and is nonetheless, by independent
    marks, not an agent there. Or a clear agent, such as a person at the
    level of everyday action, that fails one of them. The thermostat with
    its designers coming out an agent does not count: that is the
    intended verdict." LIT-398 stays in grounds: on reading NOTE-353,
    test 2's comparison descends from Dennett's intentional strategy,
    which counts a system a believer by the predictive gain of the
    intentional description over what is antecedently known, and
    Orseau et al. call their test a formal counterpart of his stances
    (NOTE-705); test 2 now cites it as its ancestor. The tests are
    unchanged.
role: thesis
warrant: interpretive
defeated_if: >-
  A factor that passes all three tests at a level and target and is
  nonetheless, by independent marks, not an agent there. Or a clear agent,
  such as a person at the level of everyday action, that fails one of
  them. The thermostat with its designers coming out an agent does not
  count: that is the intended verdict. Attributions of agency to an
  artifact that turn on whether its mechanism is known are not
  independent marks (CLAIM-393). Nor is a passer that does not make its
  own boundary a counterexample: that is agency in a further sense this
  test does not claim (CLAIM-194).
tags:
- agency
- individuation
- model-comparison
date: '2026-10-11'
line: distributed-agency
answers:
- QUESTION-032
rests_on:
- CLAIM-157
- CLAIM-154
objects_to:
- CLAIM-168
complements:
- CLAIM-170
- CLAIM-356
uses:
- TERM-047
- TERM-023
- TERM-049
- TERM-044
- TERM-048
- TERM-046
grounds:
- LIT-911
- LIT-909
- LIT-398
corroborated_by:
- THEORY-092
summary: >-
  The assistant's admission test for the owner's thesis, filed at the
  owner's request. It has three tests on a candidate factor, at a level
  and for a target. (1) System: it clears the threshold criterion. (2)
  Description: a model in which it governs its own regimes for goals beats
  a device model by more than the Occam cost (Orseau et al., priced as in
  [CLAIM-154](CLAIM-154.md)). (3) Adaptation: its governance would change if its
  actions' consequences changed (Kenton et al.). It answers the
  circularity objection by running on candidates whose boundaries come
  from (1), not from agency, and it answers the permissiveness objection
  without the will paper's supposition.
illustrated_by:
- CASE-044
objected_by:
- CLAIM-194
- CLAIM-393
supports:
- CLAIM-367
---
<!-- inactive-ok-file: CLAIM-155 — Proposed; the owner's willed-agency tiers that occasioned this version, open -->
<!-- inactive-ok-file: CLAIM-010 — Rejected; cited as the permissiveness objection any admission test must meet, not as standing -->
<!-- inactive-ok-file: CLAIM-157 CLAIM-168 CLAIM-170 — Proposed; the premise, the objection answered and the thesis made testable, open -->
<!-- inactive-ok-file: TERM-063 — Proposed; the rival sense of agent this claim says it does not claim -->
<!-- inactive-ok-file: THEORY-249 — Proposed; filed today, cited for the frame-dependence of test 3, not leaned on -->

# CLAIM-174: A candidate factor is an agent at a level when it is one system there, when a goal-directed description beats a device description by more than the Occam cost, and when its policy would adapt if its actions' consequences changed; it is a willed agent when, further, a will-organization over several regimes describes it better than none, and what passes that is the jurisdiction of a will-organization

## The claim

Fix a level of description and a target. Take a candidate factor of the
system. It is an **agent at that level** when:

1. **It is one system there.** It clears the threshold criterion
   ([CLAIM-157](CLAIM-157.md)). Its boundary comes from coupling, not from agency.
2. **The intentional description wins.** A model in which the factor
   pursues goals predicts its behaviour better than a device model (an
   input-output mapping), by more than the Occam cost ([TERM-046](../terms.d/TERM-046.md)<!-- ref::uses: TERM-046 -->) of the richer model. This is Orseau et al.'s agent-versus-device
   comparison ([LIT-911](../literature.d/LIT-911.md)), priced in the record's terms
   ([CLAIM-154](CLAIM-154.md)). Its ancestor is Dennett's intentional strategy
   (LIT-398), which counts a system a believer when the intentional
   description predicts it better than what is antecedently known, and
   which Orseau et al. turn into a computation.
3. **Its governance would adapt.** Under an intervention on how its actions
   affect the world, the factor's policy, or what governs its regimes,
   would change. This is Kenton et al.'s criterion ([LIT-909](../literature.d/LIT-909.md)): agents
   are "systems that would adapt their policy if their actions influenced
   the world in a different way".

What passes 1–3 is an **agent** ([TERM-044](../terms.d/TERM-044.md)). It is a **willed agent**
([TERM-048](../terms.d/TERM-048.md)) when it also passes:

4. **Will.** A model with a will-organization, a maintained governance over
   *several* of its regimes deciding which acts, beats the agent model
   without one, by more than its Occam cost.

What passes 4 is the jurisdiction of a will-organization ([TERM-047](../terms.d/TERM-047.md)).
That is the owner's thesis made testable ([CLAIM-170](CLAIM-170.md), [CLAIM-155](CLAIM-155.md)).

## How it handles the cases

- **The thermostat ([CASE-044](../cases.d/CASE-044.md)).**
  - *Alone it fails (3).* "An existing thermostat will not adapt to this
    change, and is therefore not an agent by our account." On (2) it is on
    Orseau's knife edge.
  - *With its designers it passes.* Kenton et al.: "the thermostat with its
    creation process is an agent under our definition". On the jurisdiction
    reading, the thermostat's one regime lies inside the designers'
    will-organization. The agent is the jurisdiction, and its boundary
    includes the process that governs the device. The two accounts agree,
    and this is the strongest outside support for individuating agents by
    jurisdiction.
- **A trained policy against its training process.** Kenton et al. call the
  training process, not the frozen policy, the agent: "simple forms of
  agents often derive much of their goal-directedness from the process that
  creates them". This is the same structure.
- **The microbiome** can pass (1) as part of the combined form ([TERM-049](../terms.d/TERM-049.md)). It fails to be
  *the person's* agent, because nothing in the person's will-organization
  governs it ([TERM-047](../terms.d/TERM-047.md)). Whether the community is an agent at its own
  level is a separate application of the test.
- **The dancing couple.** At the level of the room, during the dance, it may
  pass all three: it is one block, the dance's conventions govern both
  partners' regimes, and the pair re-organizes when the floor or the music
  changes. At the level of the pair, the lead and the follow each pass.
  Kenton et al. find the same kind of plurality: an actor-critic is two
  agents, and the one-agent graph "is also an accurate description of the
  same underlying system, though with less detail".

## The two objections it answers

- **Circularity ([CLAIM-168](CLAIM-168.md)).** The test runs on *candidate* factors whose
  boundaries come from (1). Only after (2) and (3) is a will-organization
  attributed, and then [TERM-023](../terms.d/TERM-023.md)'s agent index is satisfied by the admitted
  factor. The circle becomes a fixed-point condition. Several factorizations
  can satisfy it at once, and on this claim that is the level-relativity the
  owner predicted, not a defect. Whether that is so is the objection's open
  part.
- **Permissiveness ([CLAIM-010](CLAIM-010.md)).** The will paper answered it by supposing the
  agent ([CLAIM-080](CLAIM-080.md)). Here a control system without governance over its own
  regimes, or one whose rule would not adapt, is refused by (2) or (3). The
  bare thermostat is refused, and [CLAIM-080](CLAIM-080.md) is not needed. [CLAIM-080](CLAIM-080.md) stays
  Active for the will paper's own scope.

## What it does not say

- **That the test has been run on any real candidate.** It needs interventional
  data on mechanisms, which Kenton et al. assume is available. For people and
  firms such data is hard to get.
- **That it is prior-free.** Test (2) inherits Orseau et al.'s observer-relative
  prior, and test (3) inherits Kenton et al.'s frame-dependence: their labels
  "are only meaningful relative to the choice of which variables are included
  in the model". Both are the level and target relativity this record already
  states ([CLAIM-152](CLAIM-152.md)). Test (3) also depends on what counts as
  adaptation (Abel et al., [LIT-969](../literature.d/LIT-969.md), Claim 4; [THEORY-249](../theory.d/THEORY-249.md)): Kenton et
  al.'s intervention on how its actions affect the world is one choice of
  meaningful adaptation, not the only one.
- **That an agent makes its own boundary.** Test 1 reads the boundary off
  coupling, and a boundary kept from outside passes it as one the factor
  produces does (CLAIM-194). Tests 2 and 3 do not exclude such a factor in
  general: a policy can adapt inside a boundary someone else keeps. An
  agent here is TERM-044's, at a level of description. Minimal agency in
  Barandiaran, Di Paolo and Rohde's sense (THEORY-1119; the rival
  TERM-063) adds individuality the system produces itself, and this test
  does not claim it. Where the governor of an imposed boundary is found,
  the jurisdiction reading puts it inside the agent (note of 2026-10-21).
- **That what people or courts grant an artifact is an independent mark.**
  Such grants turn on whether its mechanism is known (CLAIM-393). So they
  meet the `defeated_if` only where knowing the mechanism makes a device
  description shorter, which is test 2's own comparison.

## Note of 2026-10-12: evidence now linked

[THEORY-092](../theory.d/THEORY-092.md) (Block) now grounds this claim's third test, weakly. Systems alike in all actual and counterfactual behaviour can differ through the processing, so a behavioural test alone admits a lookup table. Block's subject is intelligence, not agency.

## Note of 2026-10-21: test 3 and an imposed governance

A27 of the exchange of 2026-10-20 found "an important gap between
conditions 3 and 4" and proposed to separate behavioural adaptation from
governance adaptation. Test 3 already covers both ("the factor's policy,
or what governs its regimes, would change"), and A27's thermostat repair
is this claim's own case with its designers. A27's real point concerns
the exchange's governance-response profile ([TERM-067](../terms.d/TERM-067.md)), not this
test. A description that preserves how a system would respond "if its
governance mechanism were externally altered" does not show "that the
system can alter the mechanism itself" ("An ordinary machine can respond
dramatically to a technician rewiring it"). Test 3 is a test of the
second, and the profile cannot stand in for it; [CLAIM-407](CLAIM-407.md) says the
same in its "What it does not say". Where a system's authority
allocation is fixed from outside, this claim's answer is the jurisdiction
([TERM-047](../terms.d/TERM-047.md)): the governor lies inside the willed agent's boundary, and the
system alone is not that agent. A27 did not see this. It also proposed
"epistemically adaptive self-governance" as a further property, and
rightly not as a condition: it "should not silently redefine *willed
agent*".

## Note of 2026-10-29: the narrowed rule

[CLAIM-154](CLAIM-154.md) now holds only where the candidate's model stays regular at its
switch-off. Where it is singular the rule overcharges ([CLAIM-188](CLAIM-188.md)), so a
candidate it rejects may still earn a name.

## Note of 2026-10-29: what holds it back

Its first condition is CLAIM-157, which is Proposed, and the necessary half
of that criterion is unanswered (CLAIM-157's note of 2026-10-29). With
CLAIM-194 and CLAIM-393 written in, nothing else on file holds it back.
