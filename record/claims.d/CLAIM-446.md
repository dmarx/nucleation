---
number: 446
status: Proposed
formerly:
- CLAIM-tmp8z857
title: 'Some persistent anxiety may be governance-maintained rather than belief-maintained: anticipated threat grants defensive processes authority over action, attention and evidence acquisition; under the avoidance that authority selects, the hypotheses that the situation is dangerous and that it is safe predict the same observation, so repeated safety need not correct the threat estimate; relief reinforces the defense without being evidence of danger; and the regime can outlast a corrected belief, its pathology, where present, being defensive authority insensitive to corrective evidence at avoidable cost'
version: 6
history:
- version: 2
  date: '2026-10-25'
  note: >-
    A dated note added: the approach–avoid game is locally observable as
    partial monitoring, so the claim's identifiability step is a failure of
    access. The claim is unchanged.
- version: 3
  date: '2026-10-25'
  note: >-
    The partial-monitoring note checked against the reading of Bartók et
    al. (NOTE-1164). The phrase about the avoid-only game is made exact
    (regret in the full game, linear when approach is better). Two variants
    are added: suppressed feedback gives Θ(T) and a dominated check gives
    Θ(T^{2/3}). The floor is sufficient, not required. THEORY-962 is
    added to grounds. The claim is unchanged.
- version: 4
  date: '2026-10-25'
  note: >-
    The partial-monitoring note amended from the reading of Lattimore and
    Szepesvári (LIT-1524, NOTE-1162). The check variant is their
    spam game with general H and c, and its easy case is k ≤ Hc/(H + c): at
    equality the check is degenerate, which their classification for all
    games (THEORY-963) places in the easy class and Bartók et al.'s
    adversarial theorem did not cover. THEORY-963 is added to grounds.
    The claim is unchanged.
- version: 5
  date: '2026-10-29'
  note: >-
    The thirteenth status review (ADR-057, ADR-058) moved THEORY-897,
    THEORY-900, THEORY-907, THEORY-910 and THEORY-912 from grounds to
    corroborated_by: the argument does not rest on them. THEORY-914 and
    THEORY-915 leave grounds as rival accounts the test must exclude, and
    THEORY-917 as a reading that narrows the evidence-acquisition clause;
    the body cites all three. Three body citations are corrected: the
    sentence that avoidance "can interfere with new learning by preventing
    any violation in expectancy" is carried by neither THEORY-914 nor
    THEORY-921 (which holds that fear reduction during exposure does not
    predict follow-up fear), so both citations of it are removed and
    NOTE-1137 stays; and protection from extinction is carried by
    THEORY-901, not THEORY-900 or THEORY-920, whose citations there are
    removed. THEORY-914 is now cited where the test names the
    inhibitory-learning rival. The claim is unchanged.
- version: 6
  date: '2026-10-29'
  note: >-
    THEORY-921 moved from grounds to corroborated_by by the fourteenth
    status review, at the status review's ruling (the owner delegated
    these rulings; ADR-057, ADR-058). Version 5 removed its only body
    citation, which was for a sentence it does not carry. What it does
    carry, that fear falling during exposure does not predict fear at
    follow-up, is an instance of the dissociation between anxious affect
    and what is learned, and the argument does not rest on it. A sentence
    citing it for that is added under "Five quantities, not one".
    THEORY-921's supports entry for this claim is removed. The claim is
    unchanged.
role: thesis
warrant: interpretive
defeated_if: >-
  In a task with objectively specified threat, an intervention on the
  authority or evidence access of the defensive process, with the
  represented threat probability held fixed, that changes neither
  exploration nor later avoidance; or persistent avoidance that a
  belief-maintained model with matched information costs, or a habit model
  with matched memory, reproduces under every intervention the claim
  distinguishes (belief correction, authority correction, evidence-access
  correction, reinforcement correction).
tags:
- psychopathology-and-treatment
- self-governance
- emotion-and-affect
date: '2026-10-23'
line:
- will-organization
- organizational-affect
uses:
- TERM-020
rests_on:
- CLAIM-443
- CLAIM-283
- CLAIM-349
answers:
- QUESTION-045
complements:
- CLAIM-297
- CLAIM-342
- CLAIM-277
grounds:
- THEORY-285
- THEORY-901
- THEORY-920
- THEORY-903
- THEORY-962
- THEORY-963
- LIT-1498
- LIT-1477
- LIT-1479
- LIT-1483
- LIT-1490
- LIT-1491
- LIT-1496
- LIT-1500
corroborated_by:
- THEORY-897
- THEORY-900
- THEORY-907
- THEORY-910
- THEORY-912
- THEORY-921
summary: >-
  The owner's, 2026-10-23, quoting "A governance prior can become
  self-protecting by reducing the access of the processes most likely to
  provide evidence against it": "I think you may have inadvertently landed
  on a formalization of anxiety". Worked through the same day (workbench
  entry of 2026-10-24, U14–U15). A candidate account of avoidance-maintained
  anxiety, not of anxiety in general, filed as a candidate answer to
  [QUESTION-045](../questions.d/QUESTION-045.md). Its evidence is model-level and adjacent; nothing here
  measures authority in patients.
illustrated_by:
- CASE-153
supports:
- CLAIM-445
---
<!-- inactive-ok-file: THEORY-964 — Superseded by THEORY-963; the classification as Bartók et al. state it, cited in the note of 2026-10-25 for the class of each variant beside THEORY-963 (Active), which the reading of Lattimore and Szepesvári proposes supersede it; nothing here rests on it -->
<!-- inactive-ok-file: THEORY-925 — Proposed; cited in the note of 2026-10-25, nothing here rests on their being settled -->

# CLAIM-446: Some persistent anxiety may be governance-maintained rather than belief-maintained: anticipated threat grants defensive processes authority over action, attention and evidence acquisition; under the avoidance that authority selects, the hypotheses that the situation is dangerous and that it is safe predict the same observation, so repeated safety need not correct the threat estimate; relief reinforces the defense without being evidence of danger; and the regime can outlast a corrected belief, its pathology, where present, being defensive authority insensitive to corrective evidence at avoidable cost

## The claim

The owner, 2026-10-23: "I think you may have inadvertently landed on a
formalization of anxiety".

The sentence quoted came from the learned-prior account ([CLAIM-443](CLAIM-443.md)):
a governance prior can protect itself by reducing the access of the
processes most likely to supply evidence against it. Read for anxiety, the
move is from "the agent believes something threatening" to "the agent is
organized so that the threatening belief helps decide which evidence and
corrective actions remain accessible."

**Five quantities, not one.** Threat belief b, threat salience (how
urgently the defensive process claims precedence), defensive authority g
(how much influence it is granted), epistemic access, and anxious affect.
They dissociate: low belief with strong alarm; strong alarm with a valued
action carried through; little felt anxiety with automatic avoidance. A
related dissociation is reported for exposure: how far fear falls during
a session does not predict fear at follow-up (Craske et al., THEORY-921).
This continues [CLAIM-283](CLAIM-283.md) (claimed precedence against granted authority) and
[CLAIM-349](CLAIM-349.md) (access, authority, action).

**Avoidance destroys identifiability.** Let H_D be "dangerous if
approached unprotected" and H_S "safe enough". Under avoidance,
P(no harm | H_D, do(avoid)) ≈ P(no harm | H_S, do(avoid)): nothing bad
happens either way, and the likelihood ratio is one. The hypotheses differ
only under approach. An agent that always avoids can accumulate any number
of safe episodes without evidence between them. The trap is a property of
the observations the policy makes available, not of inferential skill.
[THEORY-285](../theory.d/THEORY-285.md) shows the effect in an active-inference simulation of
post-traumatic context inference; it is a model result, not patient data.

**What closes the loop.** Avoidance by itself mainly suppresses learning:
available avoidance keeps threat expectancy high, and the more effective
the response, the longer it lasts (Mancinelli and Bach's "protection from
extinction", rated A on nine studies). It is not always neutral, though.
Offering avoidance for a stimulus never paired with harm, then
withdrawing it, raised threat expectancy for that stimulus. That finding
is rated B on three studies, and the signal that avoidance is available
may itself read as a danger cue. Self-maintenance needs more: inertia of
authority, relief reinforcing the protective response, interpretation
biased toward threat, or the inference "if I felt compelled to protect
myself, the danger must have been serious." The last makes the governance
system a source of evidence for its own appraisal. A schematic coupling:
P(probe) = σ(α − βg); belief updates only on probes; g_{t+1} = (1 − η)g_t
+ η σ(θ_q q_t + θ_r r_t + θ_h g_t − θ_c c_t), with r relief and c
independently available counterevidence. Whether such a system is
bistable depends on its parameters; the diagram does not guarantee it.

**Relief is not evidence of danger.** A person can learn correctly that
avoidance lowers immediate distress while learning nothing about what
would have happened without it.

**What makes it anxiety.** Three features: the governing representation
is prospective threat; uncertainty itself becomes the reason to keep
defensive authority, while the defense keeps the uncertainty unresolved;
and protection succeeds on its own terms. The defining feature need not be
a high estimate of danger. A low-probability, high-loss threat can
rationally justify precaution, so comparing belief with authority does not
by itself diagnose pathology.

**Belief-maintained and governance-maintained.** In the first, defense
persists because danger is still estimated high or costly. In the second,
it persists partly because the organization gives defensive processes
influence over the actions and observations that could revise that
estimate. They can coexist. The second explains why someone can recognize
that a thing is probably safe and still be unable to act as if that
recognition mattered: belief correction is not behavioural correction.

**Hypervigilance fits.** The failure is not less information seeking but
poorly governed information seeking: checking, reassurance and scanning
that never acquire the information that would discriminate the
hypotheses.

**The stronger loop.** Avoidance can reduce opportunity or capability
(social practice, relationships), making later difficulty real. The
regime becomes locally rational relative to conditions its own history
produced: [CLAIM-277](CLAIM-277.md)'s neglected specialist losing competence, and
[TERM-020](../terms.d/TERM-020.md)'s stronger criterion of a regime changing the conditions that
would otherwise end it.

## The test

A safe decision task with objectively specified threat and two separable
processes. Four interventions, each holding the others fixed: belief
correction, authority correction, evidence-access correction, and
reinforcement correction. Vary actual threat too: a regime that lowers
defensive authority everywhere is not adaptive. The decisive case is a
trained defense that keeps governing after belief correction and becomes
revisable after a manipulation restoring independent evidence or another
process's influence.

The readings of 2026-10-24 add two variables the test has to hold fixed
besides the represented threat probability. One is the estimate of
uncertainty: in Brown, Price and Dombrovski the loop runs wholly through
it, with no authority variable. The other is the belief about one's own
future control: in Zorowitz, Momennejad and Daw the danger is represented
correctly, and a pessimistic belief about later escape does the work.
Each is a belief-maintained rival that holding threat probability fixed
would not exclude. A third rival is memory. On Craske et al.'s
inhibitory-learning account ([THEORY-914](../theory.d/THEORY-914.md)) the fear association survives extinction and
competes for retrieval, so persistence and return of fear need no
governance variable; a governance account has to say what it adds.


**What the readings of 2026-10-24 support and do not.** They support the identifiability step in its clinical form: avoidance "can interfere with new learning by preventing any violation in expectancy" (Craske et al., [NOTE-1137](../notes.d/NOTE-1137.md)), and avoidance protects threat expectancy from extinction ([NOTE-1134](../notes.d/NOTE-1134.md), [THEORY-901](../theory.d/THEORY-901.md)). They support the causal premise that protective behaviour does work on symptoms. In Goodson et al.'s meta-analysis, reducing safety behaviours lowered symptoms (d = 0.43; d = 0.31 after trim-and-fill for publication bias), increasing them raised symptoms (d = 0.65, five studies), and there is a dose-response. The samples are mostly young, non-clinical, and concerned with appearance or social anxiety ([NOTE-1128](../notes.d/NOTE-1128.md), [THEORY-903](../theory.d/THEORY-903.md)). De Kleine et al. ([NOTE-1123](../notes.d/NOTE-1123.md), [THEORY-912](../theory.d/THEORY-912.md)) found more avoidance of the safety cue and higher threat expectancy in OCD and PTSD, and more relief in panic and PTSD. Groups did not differ in avoiding the danger cues, relief was already higher before avoidance was available, and that relief reinforces avoidance is the authors' untested reading. Chou et al. ([NOTE-1127](../notes.d/NOTE-1127.md), [THEORY-917](../theory.d/THEORY-917.md), [THEORY-907](../theory.d/THEORY-907.md)) narrow the evidence-acquisition clause. Less exploration fits state or somatic anxiety and foraging tasks; trait or cognitive anxiety goes with more directed exploration. Brown et al. ([NOTE-1120](../notes.d/NOTE-1120.md), [THEORY-897](../theory.d/THEORY-897.md), [THEORY-910](../theory.d/THEORY-910.md)) and Zorowitz et al. ([NOTE-1136](../notes.d/NOTE-1136.md), [THEORY-915](../theory.d/THEORY-915.md)) supply the rivals named in the test. None of these studies measured authority as this claim defines it, so the claim's distinctive part is still untested. Gangemi et al., on inferring danger from one's own safety behaviour, was sought and is Unavailable ([LIT-1498](../literature.d/LIT-1498.md)).

## What it does not say

- That anxiety is excessive fear, or that this is a complete account of
  anxiety. Appropriate, transient and monitoring-dominated anxiety are
  outside it.
- That any therapy is shown to change the authority variables. Exposure
  research has several candidate mechanisms (expectancy violation,
  inhibitory learning, reduced experiential avoidance, perceived coping),
  and not every safety behaviour blocks learning.
- That the persistence of a protective regime is pathological by itself.
  The general form, across scales, is [CLAIM-445](CLAIM-445.md).

## Note of 2026-10-24: the identifiability step in exact form

From the learning-in-games readings filed the same day. In Q-learning that
updates only the chosen option, evidence about an option arrives only as
often as the option is chosen, and the expected update carries that
frequency as a factor ([THEORY-932](../theory.d/THEORY-932.md)). That is this claim's
identifiability step as an equation, and inverse-frequency weighting is an
exact condition for correcting it. Counterfactual credit does not escape
it: COMA can value an alternative only from the times it was taken, and
keeps every action's probability above a floor for that reason
([THEORY-925](../theory.d/THEORY-925.md)). The floor is protected access, the claim's evidence-access
correction. Börgers and Sarin's lock-in by reinforcement alone
([THEORY-938](../theory.d/THEORY-938.md)) is the null this claim's governance mechanism has to
beat.

## Note of 2026-10-25: a run that reproduces the identifiability step

In the BoostTheVote extension ([CASE-157](../cases.d/CASE-157.md)), outcomes were observed only
when the collective acted. With an independent metric, avoidance alone held
about 60% of runs on the old answer through the whole changed phase. Vote
noise that tipped a decision into acting was the only way out. Age-targeted
renewal removed the effect. A metric partly set by the processes in charge
also produced lock-in under full feedback. So the two routes this claim and
[CLAIM-445](CLAIM-445.md) describe each suffice alone in that model. A stylized
simulation, not evidence about anxiety ([CLAIM-427](CLAIM-427.md)).

## Note of 2026-10-25: the approach–avoid game as partial monitoring

Partial monitoring (Bartók, Foster, Pál, Rakhlin and Szepesvári 2014,
[LIT-1528](../literature.d/LIT-1528.md), read in [NOTE-1164](../notes.d/NOTE-1164.md)) came up three times in the exchange of
2026-10-24, continued (A29, A30, A31). A29 offered it as "the
informational problem behind" this claim. Worked through, the toy shows
the opposite emphasis.

Two outcomes, dangerous and safe. **Avoid** loses 0 if dangerous and c > 0
if safe, and its feedback is one symbol whatever the outcome. **Approach**
loses H > 0 if dangerous and 0 if safe, and its feedback reveals the
outcome. The signal matrices are S_avoid = [1 1] and S_approach = I₂. The
loss difference (H, −c) is not in the row space of S_avoid, which is
spanned by (1, 1), and is in that of S_approach. So the game is locally
observable, and in Bartók et al.'s classification of minimax regret (0,
about √T, T^{2/3} and T) it is in the easy √T class. Checked when filed by
least squares, H = 5 and c = 1: residual 4.24 for avoid alone, 0 for
approach. The reading confirms it. The two actions are neighbours, both
optimal at the boundary p = c/(H + c), and the game is non-degenerate, so
its class is Θ̃(√T) against a stochastic environment and Θ(√T) against an
adversarial one. The condition and the worked case are [THEORY-962](../theory.d/THEORY-962.md),
and the classes are [THEORY-964](../theory.d/THEORY-964.md), and for every finite game
[THEORY-963](../theory.d/THEORY-963.md).

- **Access, not observability.** A learner that keeps playing approach
  learns the comparison. A learner whose governing process removes
  approach from its accessible actions faces a game in which the
  comparison cannot be learned ([THEORY-962](../theory.d/THEORY-962.md)). Its regret, measured in
  the full game, grows linearly when approach is in fact better. Regret in
  the avoid-only game is zero by definition, because regret is measured
  against the actions available. The cost appears only against the
  larger game: when the probability of danger p is below c/(H + c), never
  approaching loses T(c(1 − p) − Hp). The classification bounds the best
  policy, not a constrained one. That is this claim's
  "under the avoidance that authority selects, the hypotheses … predict the
  same observation", in its formal place. A30 drew the line: "A channel may
  be capable of resolving a question yet remain unused because the process
  controlling action prevents it from being selected."
- **Two variants**, both by the same lemma and both the record's
  constructions ([THEORY-962](../theory.d/THEORY-962.md)).
  - *Safety behaviour as suppressed feedback.* Suppose approach is
    performed but shows one symbol whatever the outcome. Then no action
    reveals the outcome, the game is not globally observable, and its
    class is Θ(T), the hopeless one.
  - *Checking as a dominated revealing action.* Suppose the outcome can be
    learned only through a separate check, with loss k under both
    outcomes, and approach is uninformative. If k > Hc/(H + c) the check is
    never optimal. The game is then globally but not locally observable,
    and its class is Θ(T^{2/3}), the revealing-action structure. If
    k ≤ Hc/(H + c) the check is optimal somewhere (its own cell when <,
    the indifference point when =) and the game is easy again.
    This is a formal counterpart to the hypervigilance paragraph above:
    checking that reveals the outcome but costs more than it is worth
    makes the comparison expensive to learn, not impossible. This variant
    is Lattimore and Szepesvári's spam game ([LIT-1524](../literature.d/LIT-1524.md), Example 1) with
    general H and c. With H = c = 1, avoid is "spam", approach is "not
    spam" and the check is "don't know". Their classification for all
    games ([THEORY-963](../theory.d/THEORY-963.md)) places the boundary case k = Hc/(H + c), where
    the check is degenerate and optimal only at p = c/(H + c), in the easy
    class. Bartók et al.'s adversarial theorem did not cover it. So the
    easy case is k ≤ Hc/(H + c), and checking that costs exactly what it
    saves at the indifference point is still cheap to learn from
    ([THEORY-961](../theory.d/THEORY-961.md)). The construction is no longer only the record's:
    its H = c = 1 case is the paper's motivating example.
- **The floor** is [QUESTION-271](../questions.d/QUESTION-271.md)'s exploration floor, the price COMA
  pays as well ([THEORY-925](../theory.d/THEORY-925.md)). A floor is sufficient, not required. Bartók
  et al.'s CBP keeps no fixed floor: in the easy stochastic class it plays
  a suboptimal action only about log T/δ² times, δ its gap in
  expected loss. Kwon and Perchet's
  approachability algorithm does keep one, γ/|I| on every decision with γ
  of order T^{-1/3}, because its signals depend on the decision
  ([THEORY-957](../theory.d/THEORY-957.md)).
- **The guarantees stop** where authority edits the losses or the feedback
  channels during learning. A29: "we should first use the classical setting
  as a baseline, then study controlled changes in H, not attribute those
  changes to Bartók and colleagues' theorem."

It does not show that anxious avoidance has this loss structure. The
claim is unchanged.

## Note of 2026-10-29: what holds it back

Its premise [CLAIM-443](CLAIM-443.md) is Proposed. No result in the record measures
defensive authority apart from threat belief, the uncertainty estimate
and the belief about one's own future control, so the belief-maintained
rivals of [THEORY-910](../theory.d/THEORY-910.md) and [THEORY-915](../theory.d/THEORY-915.md) ([QUESTION-325](../questions.d/QUESTION-325.md)) and the memory
account of [THEORY-914](../theory.d/THEORY-914.md) are not excluded, and nothing yet meets or fails
its defeated_if. The readings promoted on 2026-10-29 hold its laboratory
steps in healthy people ([THEORY-901](../theory.d/THEORY-901.md), [THEORY-920](../theory.d/THEORY-920.md)) and the causal work of
safety behaviour ([THEORY-903](../theory.d/THEORY-903.md)); none measures authority.
