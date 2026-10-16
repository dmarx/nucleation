---
number: 705
status: Read
formerly:
- NOTE-tmpijpu3
paper: LIT-911
title: 'Orseau, McGill & Legg — Agents and Devices'
version: 1
history:
- version: 1
  date: '2026-10-11'
  note: >-
    Read in full by the assistant from the arXiv PDF (v1, 7 pp.), text
    extracted with pdftotext. The equations survived only partly in
    extraction and were read for their structure. The values in the result
    panels of Figures 1–7 (negative log-likelihoods and posteriors) did not
    survive, so the outcomes below are taken from the prose describing each
    figure. Quotations were checked against the extracted text by script.
date: '2026-10-11'
summary: >-
  A formal counterpart of Dennett's physical and intentional stances. A
  device is a mixture of input-output mappings; an agent is a mixture of
  goal-optimizing ε-greedy policies, by inverse RL. Bayes' rule gives the
  posterior probability that a system is an agent. It is illustrated in a
  toy gridworld, with no human comparison. Agency is explicitly relative
  to the observer's prior. A clearly identified system is assumed.
---
<!-- inactive-ok-file: CLAIM-010 — Rejected; cited as the permissiveness objection any admission test must meet, not as standing -->
<!-- inactive-ok-file: CLAIM-157 CLAIM-166 CLAIM-168 CLAIM-174 THEORY-036 — Proposed; claims and the real-patterns reading this note connects to, open -->

# NOTE-705: Orseau, McGill & Legg — Agents and Devices

## Contribution

It turns Dennett's choice of stance into a computation. Given an interaction
history, compare the evidence for "this is an agent pursuing some goal"
against "this is a device mapping inputs to outputs", with priors over both
mixtures.

## Key insight

"devices" are described "in terms of an input-output mapping, while 'agents'
are described in terms of the function they optimise". Agency is then
whichever description compresses the behaviour better, for this observer.

## Assumptions

- **An identified system.** "we assume a clearly identified system that takes
  a sequence of inputs and returns a sequence of outputs at discrete time
  steps". Where the system ends is given, not found.
- **Observer-relative priors.** The question "is observer-relative, since it
  depends the observer's prior knowledge". The paper offers Solomonoff and
  speed priors, and "A more observer-dependent prior could also be
  considered".
- **Approximately rational agents.** Agents are ε-greedy toward an optimal
  policy for some utility, with ε integrated out.

## Key results

- **Dennett's three examples, informally.** A stone is best predicted
  physically. The thermostat is "on the knife edge", describable "either as
  a reactive device ... or as an agent ... using descriptions of comparable
  simplicity". AlphaGo's policy network invites the intentional stance even
  though "it is entirely reactive".
- **Gridworld results, from the prose.**
  - Running in circles and following walls are better described as devices.
  - Going straight to a goal, or reaching one suboptimally, is better
    described as an agent.
  - Random behaviour is poorly explained by both.
  - With a switching prior, a system that changes goals mid-trajectory is
    still an agent: "agents can change their mind and switch goals—and
    still be considered agents, as long as the switches are rare".
- **A prior that makes everything an agent.** Under the speed prior, "if any
  device can be represented as an agent then everything may look like an
  agent because the penalty for devices is too large". The fix proposed is
  to penalize agents more.
- **The conclusion.** "Every physical system can be described as either an
  agent (which pursues goals) or a device (which responds mechanically to
  its inputs)".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Agency can be defined as posterior probability under agent-versus-device model comparison | definitional, well-formed | the formalism, Section 3 |
| C2 | The verdict is observer-relative, through the prior | follows from C1 | stated, Sections 1 and 3.1 |
| C3 | Goal-directed trajectories score as agents and reactive ones as devices | illustrated | toy gridworld, seven trajectories, no human study |
| C4 | Rare goal switches are compatible with agency | illustrated | switching prior, Fig. 5–6 |
| C5 | The choice of prior can make everything look like an agent | argued | speed-prior discussion |

## Connections

- **The admission test** ([CLAIM-174](../claims.d/CLAIM-174.md)). C1 is its model-comparison
  half, and [CLAIM-154](../claims.d/CLAIM-154.md) supplies the Occam pricing in the record's own
  terms.
- **The circularity objection** ([CLAIM-168](../claims.d/CLAIM-168.md)). The identified-system
  assumption is the presupposition that the threshold criterion
  ([CLAIM-157](../claims.d/CLAIM-157.md)) would discharge.
- **Time-varying drive** ([CLAIM-166](../claims.d/CLAIM-166.md), now [CLAIM-316](../claims.d/CLAIM-316.md)). C4 says an agent can change what
  drives it, rarely, and stay an agent. That is the owner's non-constancy,
  bounded.
- **C5 is the permissiveness objection ([CLAIM-010](../claims.d/CLAIM-010.md)) in formal dress.** Whether
  everything is an agent depends on the prior.
- **Dennett** ([LIT-398](../literature.d/LIT-398.md)) is the source of the stances. [THEORY-036](../theory.d/THEORY-036.md) records that
  his compression criterion "admits almost every non-random pattern", the
  same worry as C5.
