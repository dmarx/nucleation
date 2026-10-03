---
status: Read
paper: LIT-tmpk0t5p
title: 'Uncertainty-based competition between prefrontal and dorsolateral striatal systems for behavioral control'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full: the published PDF from the Gatsby Unit, all eight pages
    (introduction, Results, Discussion, Methods, figures and references).
    The Supplementary Methods with the full Bayesian update equations were
    not read, so the form of the uncertainty updates is known only from the
    Methods summary. The figure panels were read from their captions and the
    text, not from the plotted values. The behavioural and lesion results
    the paper summarizes (refs 14-17, 23-31) are taken as it reports them.
date: '2026-10-03'
summary: >-
  Habit and goal-directed action are model-free (cached values) and
  model-based (tree search) reinforcement learners, arbitrated by which
  controller's Bayesian posterior over action value has the lower variance.
  Over-training shifts control to the cache because tree search accrues
  computational noise per step. Task complexity and proximity to reward keep
  the tree in control. It also predicts that incentive learning should
  become unnecessary when the caching system is lesioned.
---
<!-- inactive-ok-file: THEORY-056 — Proposed theories and Deferred seeds, named as accounts this reading bears on; written from the lint report -->

# NOTE-tmpishc1: Uncertainty-based competition between prefrontal and dorsolateral striatal systems for behavioral control

## Contribution

Before this paper, animal learning theory described when behaviour is
habitual and when it is goal-directed, and neuroscience had dissociated the
substrates. This paper offers a normative reason for having both, and a
rule for choosing between them. Each is a different approximation to the
intractable Bayes-optimal controller. Each is trusted when its
approximation is likely to be the more accurate.

## Key insight

Caching and searching fail in opposite circumstances. A cache bootstraps
from its own estimates, so it needs much experience. But once trained it
recalls values without computing them. A tree uses each observation
everywhere at once, so it learns fast. But each step of search through a
deep tree adds error. If each system tracks its own uncertainty, deferring
to the less uncertain one gives the observed pattern with no extra
assumption. The tree controls early in training. The cache controls distal
actions after over-training. The tree keeps control where data are spread
thin, as with more actions and outcomes, or where search is shallow, as for
an action next to the reward.

## Assumptions

- **Absorbing Markov decision processes** with outcomes only in terminal
  states and binary rewards. The probability that reward is 1 in a terminal
  state stands in for that outcome's utility (Methods).
- **Strict separation** of the two controllers for the purpose of modelling,
  although the text says their substrates are "clearly intertwined".
- **Expected task change.** Both systems assume values may change, which puts
  a time horizon on past data. So uncertainties asymptote at finite levels,
  and values asymptote "well short of the true payoffs".
- **Computational noise** in tree search, modelled as uncertainty that
  "accumulates with each search step". The cache has "little computational
  'noise'".
- **Hard arbitration**: take the mean from the controller with the smaller
  posterior variance. "Softer integration schemes, such as a
  certainty-weighted average, are also possible."
- **Softmax choice**: P(a | s) ∝ e^{βQ(s,a)}.
- **Uncertainty is ignorance, not risk**: "posterior uncertainty quantifies
  ignorance about the true probability of reward, not inherent stochasticity
  in reward delivery".

## Key results

- **Tree more certain early** in all simulations, "even though both systems
  had matched initial uncertainty", because experience "immediately
  propagates" through the model (Fig. 5).
- **One action, one outcome** (Fig. 5). For the distal lever press, the
  cache wins asymptotically, because the extra search step adds uncertainty.
  So over-trained pressing is devaluation-insensitive. For the proximal
  magazine entry, the tree stays more certain "even asymptotically", so
  entry stays sensitive.
- **Two actions, two outcomes** (Fig. 6). Experience is spread over more
  states, fewer relevant data constrain each value, and the tree's early
  advantage persists even for the distal press. So over-trained actions stay
  sensitive, as in Holland (2004) and Colwill and Rescorla (1985).
- **Lesions.** Dorsolateral-striatal or dopamine lesions block habit
  formation, and prelimbic, dorsomedial-striatal, basolateral-amygdala,
  insular or orbitofrontal lesions abolish devaluation sensitivity. Both
  patterns are read as one controller left alone.
- **Predictions.**
  - Recordings should show behaviour correlating with whichever system
    controls it.
  - Strenuous concurrent demands should favour the cache.
  - Unexpected contingency changes should favour the tree.
  - Fan-out task structure should favour caching, and linear or fan-in
    structure should favour search.
  - In a strong claim "contrary to the standard account", incentive
    learning (re-experiencing the devalued outcome) works by reducing the
    tree's uncertainty. Its necessity "should vanish in animals with lesions
    disabling the caching system".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Habitual and goal-directed control correspond to model-free and model-based reinforcement learning | moderate: a mapping argued from devaluation behaviour and lesion dissociations | Results; refs 5, 8, 14–17 |
| C2 | Arbitration by relative uncertainty reproduces the effects of over-training, task complexity and reward proximity on devaluation sensitivity | moderate: qualitative fits to stylized tasks, "rather than focusing on a quantitative fit to rather qualitative data" | Figs. 5–6 |
| C3 | Both controllers pursue the same ends; neither is the irrational one | argued (normative framing) | Discussion |
| C4 | Competition is probably between dorsomedial and dorsolateral corticostriatal loops rather than cortex versus striatum | suggested from the anatomy | Discussion, refs 8, 43 |
| C5 | Infralimbic cortex or ACC may implement arbitration | speculative ("limited evidence") | Discussion, refs 16–17, 47–48 |
| C6 | Incentive learning is uncertainty reduction in the tree, and should be unnecessary after cache lesions | a prediction, untested in the paper | Discussion |

## Concepts

- **caching**: "the association of an action or situation with a scalar
  summary of its long-run future value". It is model-free, and its hallmark
  is the transfer of the dopamine response to predictive stimuli.
- **tree search**: building predictions "on the fly, by chaining together
  short-term predictions about the immediate consequences of each action".
  It is model-based.
- **habitual / goal-directed**: insensitive / sensitive to outcome
  devaluation (the psychological definitions, refs 5 and 22).
- **arbitration**: choosing whose value estimate drives behaviour, here by
  posterior variance.

## Connections

- **Dayan and Berridge ([LIT-tmpmlzuo](../literature.d/LIT-tmpmlzuo.md), [NOTE-tmpruoh7](NOTE-tmpruoh7.md))** carry the distinction
  to Pavlovian prediction. They reread this paper's account of incentive
  learning: the instrumental model-based system knows the new value but is
  uncertain about it because the motivational state is novel.
- **Botvinick, Niv and Barto ([LIT-tmpkcnyi](../literature.d/LIT-tmpkcnyi.md))** adopt the same mapping of
  habit and planning onto model-free and model-based RL. The PMC text strips
  the author names from its citations, so whether they cite this paper for
  it was not checked. They place hierarchical RL in the cache-based system
  and note that options can also be given models for search.
- **Shenhav, Botvinick and Cohen ([LIT-tmpncuk4](../literature.d/LIT-tmpncuk4.md))** put the decision about
  control in dACC as a cost-benefit computation. This paper names ACC only
  as a candidate arbitrator, citing conflict monitoring (Botvinick, Cohen &
  Carter 2004).
- **Ainslie ([LIT-tmpne8q4](../literature.d/LIT-tmpne8q4.md))** also rejects the reason-versus-impulse picture,
  but from intertemporal conflict between controllers of one kind. Here the
  controllers differ in method, not in their time horizons or their ends.
  The two pictures do not conflict, because they address different
  divisions.

## Bearing on the record

- **[THEORY-056](../theory.d/THEORY-056.md).** The theory's clause that there is "no distinct regulating
  system above them" fits this paper. The two controllers are peers, and the
  winner is the one whose estimate is more reliable, not the one a higher
  system prefers. But the arbitration rule is itself computed somewhere, and
  the paper names IL and ACC as candidates. If a structure computes
  arbitration, the theory needs to say whether an arbitrator counts as a
  "regulating system". The paper also extends the theory's question from
  emotion to action. See the report.
- **A candidate THEORY.** This paper and [LIT-tmpmlzuo](../literature.d/LIT-tmpmlzuo.md) together support an
  account in which instrumental and Pavlovian behaviour each draw on
  model-based and model-free predictions, combined by reliability. That is
  proposed in the report, not filed.
- **No ML instruction.** The paper uses reinforcement-learning algorithms to
  explain brains and behaviour, so it belongs here and not in the anthology.

## Limitations

- **Stylized tasks and qualitative fits.** The paper says so itself.
- **Arbitration is assumed, not derived.** Choosing the lower-variance
  estimate is a simplification, and the paper notes that softer combinations
  are possible.
- **The computational-noise term carries the over-training result.** Without
  per-step search noise, the tree would stay more certain everywhere. Its
  size is a modelling choice, and the main text does not justify its value.
- **The substrate of arbitration is unknown**: "There is limited evidence".
- **The role of dopamine in the tree system** is "wholly unresolved".

## Open questions

- Does incentive learning become unnecessary after caching-system lesions,
  as C6 predicts?
- Is arbitration hard or weighted? Which experiment distinguishes the two?
- What implements arbitration: IL, ACC, neuromodulators, or nothing beyond
  the controllers' own output strengths?
