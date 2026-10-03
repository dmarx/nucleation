---
number: 451
status: Read
formerly:
- NOTE-tmp9xfix
paper: LIT-581
title: 'Hierarchically organized behavior and its neural foundations: A reinforcement learning perspective'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full: the PMC author manuscript (PMC2783353), all sections,
    footnotes and figure captions. The online appendix with the
    implementation's equations (Eqs. 1-9) and simulation details was not
    read, so the update rules are described from the main text only. The
    retrieved text strips author names from most citations. The figures'
    plotted values were not seen. The numbers quoted come from the text
    and footnote 10.
date: '2026-10-03'
summary: >-
  The paper introduces hierarchical RL (options) to psychology and
  neuroscience as a response to RL's scaling problem. An actor-critic
  options model learns faster with useful options (doorways in the rooms
  task) and slower or worse with unhelpful ones (windows; a shortcut
  ignored). It proposes DLPFC for option identity, DLS for option-specific
  policies, and OFC for option-specific values and option-level prediction
  errors. It predicts phasic dopamine at subtask boundaries and a possible
  neural pseudo-reward. Option discovery is named as the central problem.
---
<!-- inactive-ok-file: THEORY-056 — Proposed theories and Deferred seeds, named as accounts this reading bears on; written from the lint report -->

# NOTE-451: Hierarchically organized behavior and its neural foundations: A reinforcement learning perspective

## Contribution

The paper carries hierarchical reinforcement learning, then a recent machine
learning development, into psychology and neuroscience. It gives three
things:

- a tutorial on the options framework;
- a new actor-critic implementation built to be mapped onto brain
  structures;
- an inventory of what HRL implies for behavioural research (transfer,
  option discovery) and for neural function (four extensions, each with a
  candidate substrate).

## Key insight

The cost of learning by trial and error grows steeply with the number of
states and actions. Organisms nonetheless learn complex tasks, so something
must cut the problem down. Grouping actions into reusable subroutines does
this, by making exploration and credit assignment happen at a few
higher-level choice points. But a subroutine helps only if it fits the
problem. The question a hierarchical learner must answer is therefore which
subroutines to have, and the same question applies to people.

## Assumptions

- **The options framework** (its citation is stripped in the retrieved
  text): options with initiation sets, termination functions and
  policies. Options are pre-trained in the illustrations, "simulating
  transfer of knowledge from earlier experience" (footnote 8).
- **Actor-critic** structure, with the actor's policy as action strengths
  and the critic's value function updated by temporal-difference prediction
  error. "Discounting is ignored in the main text" though the implementation
  uses it (footnote 4).
- **Pseudo-reward at subgoals** shapes option policies. Other HRL frameworks
  (HAM) do without it, and some (MAXQ) decompose value functions
  differently. The neural predictions depend on which is assumed.
- **The cache-based (model-free) system** is the setting. Model-based option
  models are discussed but not implemented.

## Key results

- **Rooms task** (Fig. 4). With doorway options and primitive actions, the
  agent learns to reach the goal faster than with primitive actions alone.
- **Negative transfer** (Fig. 5).
  - Options with "window" subgoals slow learning.
  - With a shortcut opened, primitive-only agents find the shortest path on
    "75% of training runs". Agents with doorway options learn to use only
    the main doorways. Footnote 10 gives mean solution times over the last
    10 of 500 episodes: 11.79 steps with doorway options (passageway visited
    on 0% of episodes) against 9.73 with primitives only (79% of episodes).
  - HRL systems tend to "satisfice" except under very slow learning.
- **Neural mapping** (Fig. 2C–D):
  - **Extension 1** (option identity) maps to DLPFC, which represents task
    sets. Pre-SMA, SMA and premotor cortex are candidates too.
  - **Extension 2** (option-specific policies) maps to DLS, which receives
    frontal input and shows context-dependent action coding, as in
    grooming-sequence neurons.
  - **Extension 3** (option-specific values) maps to OFC, whose value
    representations shift with strategy.
  - **Extension 4** (prediction errors over whole options) maps to OFC's
    sustained reward-predictive activity and to semi-Markov accounts of
    dopamine.
- **Predictions**: phasic dopamine at subtask boundaries scaling with
  option-level prediction errors, a possible neural correlate of
  pseudo-reward, and PFC coding of discrete subtask segments (for which
  evidence is "only indirect").

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Temporal abstraction eases RL's scaling problem by reducing the decisions to explore and learn | strong in the computational setting, illustrated by simulation | Figs. 1, 4 |
| C2 | Unsuitable options slow learning or lock in suboptimal paths, an analogue of negative transfer | moderate: toy simulations | Fig. 5, footnote 10 |
| C3 | DLPFC holds option identifiers, DLS option-specific policies, OFC option-specific values | weak–moderate: proposed mappings from correlational findings; "call for further experimental scrutiny" | Neuroscientific Implications |
| C4 | Dopamine should fire at subtask boundaries in proportion to option-level prediction error | a prediction, untested | Discussion |
| C5 | Option discovery is a central problem for both HRL and human learning | argued | The Option Discovery Problem |
| C6 | Human behaviour is only quasi-hierarchical: overlap and context-sensitivity resist strict options | argued; cites a computational model of routine sequential behaviour (authors stripped in the retrieved text) | Strict versus Quasi-Hierarchical Structure |

## Concepts

- **option**: a temporally abstract action, "in a sense, a 'mini-policy'",
  defined by an initiation set, a termination function and an
  option-specific policy.
- **pseudo-reward**: reward credited for reaching an option's subgoal, which
  shapes the option's policy, distinct from external reward.
- **scaling problem**: the steep growth of learning time with the number of
  states and actions.
- **option model**: a model of an option's outcome, reward and duration, for
  look-ahead that "skips over" primitive steps.
- **option discovery problem**: how a learner comes to have options that will
  be useful for future problems.

## Connections

- **Daw, Niv and Dayan ([LIT-580](../literature.d/LIT-580.md)).** The paper adopts their model-free
  versus model-based mapping and sets HRL in the cache. It notes that option
  models make look-ahead "saltatory", like everyday planning.
- **Self-determination theory and intrinsic motivation.** The intrinsic-reward
  route to option discovery is linked in the text to "psychological theories
  suggesting that human behavior is motivated by a drive toward exploration
  or toward mastery". That is the territory of the record's SDT readings
  ([LIT-559](../literature.d/LIT-559.md), [LIT-561](../literature.d/LIT-561.md)), though the paper does not cite SDT by name in the
  retrieved text.
- **Production systems.** Soar and ACT-R chunks are "the strongest parallels"
  in psychology. HRL differs in organizing everything around reward
  maximization.

## Bearing on the record

- **Behavioural integration.** This is the record's account of how one
  agent's many action routines are composed into a hierarchy and learned. It
  pairs with [LIT-436](../literature.d/LIT-436.md) (Brooks), whose layers are designed rather than
  learned.
- **[THEORY-056](../theory.d/THEORY-056.md).** Not directly. But HRL is control without a distinct
  regulator: the "controller" at each level is just a policy over options,
  learned by the same prediction-error rule as the level below. That is the
  shape the theory claims for emotion regulation, reached in a different
  domain.
- **No ML instruction.** The paper explains behaviour and brains. It belongs
  here.

## Limitations

- **Toy simulations.** The rooms domain is small and the options are
  pre-trained.
- **Mappings are proposals.** The neural correspondences are drawn from
  existing correlational findings, not tested.
- **Model-free only.** HRL with option models is described but not
  implemented.
- **Strict hierarchy is too strict** for everyday tasks, as the paper says
  itself (shared structure, context-sensitivity).

## Open questions

- Is there a neural pseudo-reward at subgoal attainment?
- Do dopamine neurons fire at subtask boundaries in proportion to
  option-level prediction errors?
- How do people discover subgoals: by bottlenecks, intrinsic salience,
  impasse, or social inference?

## Corrections

- **75% and 79%.** The main text says primitive-only agents found the
  shortcut on "75% of training runs". Footnote 10 says the passageway was
  visited on "79% of episodes" over the final episodes. These measure
  different things (runs that converge to the shortest path, versus
  episodes visiting the passage), so they are not in conflict, but they are
  easy to conflate.
