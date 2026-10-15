---
number: 355
status: Proposed
formerly:
- THEORY-tmpwrpnk
promote_when: >-
  A study that holds a task's physical possibilities fixed, varies only how the
  workspace is arranged (grouped against scattered, ordered against unordered,
  marked against unmarked), and measures the agent's search or decision time and
  errors, counting the time spent arranging. It promotes the account if the
  arrangement's saving per later step is positive and its net value grows with the
  number of later choice points it serves; it refutes the scope clause if net value
  does not depend on how many steps the arrangement serves. More observational
  examples, or worst-case search counts like O(N) to O(log N), cannot settle it:
  those show that an arrangement could cut search, which is already held, not by
  how much or when it pays.
title: "Agents arrange their surroundings so that perception and choice take the place of internal search, changing how much thinking a task needs without changing what can physically be done; the set-up is paid once and recovered over the later choice points the arrangement serves, so an arrangement whose scope is the whole task can repay a large set-up and a narrow one must repay within the next few actions, and the arrangement decays unless maintained; the savings are argued and piloted, not measured"
version: 1
tags:
- cognition
- embodied-cognition
date: '2026-10-15'
source:
- LIT-1076
- LIT-1057
answers:
- QUESTION-095
summary: >-
  Kirsh (1995), [LIT-1076](../literature.d/LIT-1076.md), read in [NOTE-871](../notes.d/NOTE-871.md), and Kirsh (1996), [LIT-1057](../literature.d/LIT-1057.md), read in [NOTE-872](../notes.d/NOTE-872.md).
  From video of cooks, assemblers and baggers and from informal observation, Kirsh
  classifies arrangements that simplify choice, perception and internal computation,
  frames their savings in search-complexity terms, and ties set-up cost to the number
  of choice points an arrangement serves. The 1996 paper adds a verbal investment rule
  with an interest factor for risk, one risk being that the change is not still
  present later, and upkeep against scatter. Neither paper gives a cost model or a
  measured saving; the 1995 paper says the savings do not "in general" admit
  meaningful quantitative estimation, and the 1996 paper puts mental cost outside its
  formalism.
---

# THEORY-355: Agents arrange their surroundings so that perception and choice take the place of internal search, changing how much thinking a task needs without changing what can physically be done; the set-up is paid once and recovered over the later choice points the arrangement serves, so an arrangement whose scope is the whole task can repay a large set-up and a narrow one must repay within the next few actions, and the arrangement decays unless maintained; the savings are argued and piloted, not measured

## Source

Kirsh (1995), [LIT-1076](../literature.d/LIT-1076.md) (Artificial Intelligence 73, 31–68), read in [NOTE-871](../notes.d/NOTE-871.md):
§§2–6, footnotes 8, 9 and 11, Table 1. Kirsh (1996), [LIT-1057](../literature.d/LIT-1057.md) (Adaptive
Behavior 4, 415–452), read in [NOTE-872](../notes.d/NOTE-872.md): sections 4 and 5, footnotes 3 and 6.

## What was actually shown

**A classification, from observation.** The 1995 paper sorts uses of space into
"spatial arrangements that simplify choice; spatial arrangements that simplify
perception; and spatial dynamics that simplify internal computation." Its
evidence is "videos of cooking, assembly and packing, everyday observations in
supermarkets, workshops and playrooms, and experimental studies of subjects
playing Tetris"; much is anecdotal. Its agents are experts arranging their own
workspace in the medium and short term; long-term pre-built environments are set
aside.

**Informational, not physical.** An informational arrangement "achieves nothing
that could not equally well be achieved by asking an oracle", and is slower than
one (footnote 8). The 1996 paper makes the same split in its formalism: some
actions change a task graph's topology or metric, others "leave the state space
formally intact but that reduce the number and cost of mental operations needed
for task success".

**Savings stated as search complexity.** A strong cue at each choice point cuts
search "from b^n to n"; knowing an assembly order turns a doubly exponential
problem into an exponential one; hierarchical grouping reduces visual search
"from O(N) to O(log N)". These are worst-case counts for illustration.

**Scope and set-up.** A heuristic cue "normally applies to many choice points".
Of the salad maker's rows, "the set-up costs could be amortized over the whole
task. By contrast, in leaving a plug in the sink, or in placing the next item to
be bagged close by, the cost of set-up must be paid off by the savings in the
next few actions." Footnote 9 points to Tarjan's amortized analysis of
self-adjusting data structures as "a more formal model". The 1996 paper's one
tie of a saving to later uses: a sorted card hand's saving "will reappear every
time a change in intentions is made".

**Investment, risk and upkeep (1996).** Doing work now for later use "depends on
whether the expected benefits to be collected some time in the future outweigh
the current costs multiplied by some interest factor to compensate for risk."
Footnote 3 lists the risks: whether the result is used, whether the changes "will
still be present later", and whether the agent survives. Arrangements decay:
"Entropy teaches us that objects tend to scatter", and the state "must be
maintained or enforced". Labour cost varies over time, so work is best done when
it is cheap, and more of it when the next chance is uncertain.

**The only numbers.** 1996 pilot studies without sample sizes: counting coins,
errors above 50% untouched, about 35% with pointing, "nearly 20 percent" with
free movement; finding the longest of 20 sticks without touching them took "more
than 55 percent more time".

## What this does not say

- **How much any arrangement saves.** "The actual reduction in computation
  achieved by the various methods I shall discuss does not, in general, lend
  itself to meaningful quantitative estimation." The salad cue's cost-benefit is
  named as an empirical matter and not carried out.
- **That arranging is memoization.** Tarjan's amortization spreads the upkeep of
  a structure over operations; Kirsh's analogy is to continual rearrangement. A
  cluster stores an index that makes search cheap, not an answer.
- **That the 1996 economics is a model.** The interest factor is verbal, with no
  rate, formula or reuse frequency; the task graph prices only physical
  transitions, and of congeniality "To date, there is no general theory to
  report". "Amortize" occurs once there, a gloss on chimpanzees leaving
  nut-cracking stones in place.
- **That stale results are a cost.** The named failures are disturbance, clutter
  and decay of the arrangement; a stored result that has become wrong for the
  query does not appear.
- **That it holds when arranger and user differ, or under deadline.** Neither
  paper has such a case.

## Connections

- [QUESTION-095](../questions.d/QUESTION-095.md): this is the "maintain structure that makes search cheap"
  strategy. Kirsh 1995 draws the link to algorithmic amortization, not to
  amortized inference, which postdates it. The time-varying cost of labour is the
  cockpit's reason for setting speed bugs at low workload ([LIT-1066](../literature.d/LIT-1066.md)).
- [THEORY-360](THEORY-360.md) is the moment-of-use case; [THEORY-339](THEORY-339.md) is the stored-result case
  with the store in the head.
- [CLAIM-303](../claims.d/CLAIM-303.md)'s break-even has the same form as the scope rule here, with an upkeep
  term; Kirsh supplies neither its arithmetic nor a test.
- [CLAIM-296](../claims.d/CLAIM-296.md) and [CASE-085](../cases.d/CASE-085.md): "If I can't find the garlic, I am not likely to think
  of rubbing it on the salad bowl—I miss some available actions."
