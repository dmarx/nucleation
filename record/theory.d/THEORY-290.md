---
number: 290
status: Proposed
formerly:
- THEORY-tmpvtupa
promote_when: >-
  An analysis or experiment that measures accuracy and revision costs
  separately and finds the same free-riding structure among more than
  two debaters, or with richer strategies than fixed, memoryless
  premise and conclusion rules. In such a study, a participant facing a
  bold partner must argue less boldly, collective accuracy must fall
  short of what mutual boldness would give, and the shortfall must vanish
  when the cost of revision is removed. It is refuted if, with
  strategies that can target the partner's false beliefs (the paper's
  "ideal cooperative debater"), the truth-optimal profile is an
  equilibrium wherever the truth weight is positive. More runs of the
  two-person, three-proposition model cannot settle it, and neither can
  observational data on debates, which cannot measure revision costs.
title: "When debaters value true belief but also dislike changing their minds, equilibrium argument can fall short of the truth-optimal profile because one debater free-rides on the other's belief-disrupting arguments, and raising the weight on truth can lower equilibrium accuracy"
version: 1
tags:
- epistemology
- game-theory
- social-science
date: '2026-10-14'
source:
- LIT-966
summary: >-
  Handfield, Garcia, Hilbe and Yeo (2025), [LIT-966](../literature.d/LIT-966.md), read in full in
  [NOTE-795](../notes.d/NOTE-795.md). With payoff w·v − d (true beliefs against changes of
  mind), debate between two deductive reasoners is a cooperative dilemma
  at low and moderate truth weights. Typically one argues boldly and the
  other free-rides (a snowdrift), and at low weights both exit. A small
  dip in accuracy as w rises occurs in a narrow band of mixed equilibria.
  It is shown numerically for two players and three propositions. It
  concerns collective accuracy, not a belief the pair settles on, and
  at high truth weight in short debates there is no dilemma.
---
<!-- inactive-ok-file: THEORY-148 — Proposed; the transient-diversity account this one is set beside -->

# THEORY-290: When debaters value true belief but also dislike changing their minds, equilibrium argument can fall short of the truth-optimal profile because one debater free-rides on the other's belief-disrupting arguments, and raising the weight on truth can lower equilibrium accuracy

## Source

Handfield, Garcia, Hilbe and Yeo (2025), arXiv:2504.06485, [LIT-966](../literature.d/LIT-966.md), read
in full in [NOTE-795](../notes.d/NOTE-795.md): §§2.4–2.6, Table 1, Fig 5, and SI C and D.3.

## What was actually shown

- **The setting.**
  - Two debaters hold truth assignments to n = 3 atomic propositions.
  - Valid two-premise arguments eliminate positions.
  - A refuted debater moves to the nearest tenable position.
  - Each picks one of 16 premise × conclusion rules, or Exit.
  - The debate continues with probability δ after each argument.
  - Payoffs are u = w·v − d, with v the number of true beliefs at the
    end and d the total revisions, computed exactly by Markov chain.
- **The dilemma (Table 1, δ = 0.8).**
  - At truth weight 2.5 there is a prisoner's dilemma.
  - At 3.5, a stag hunt and a snowdrift.
  - At 4.5, a snowdrift.
  - At 9.5, none.
  - The cooperative action in each pair is the more epistemically
    productive one.
- **The free-riding equilibrium (§2.6.3).** At moderate truth weight or
  in longer debates, the best reply to the bold S+S− is a compromise
  strategy such as S+O+. That strategy forces a change of mind only on
  propositions where the two disagree. The result is an asymmetric
  equilibrium with "a modest loss of collective accuracy".
- **Disengagement.**
  - At low w, (Exit, Exit) is the selected equilibrium, an "agreement to
    disagree".
  - With error (α = 0.1, 0.3), Exit takes over much of the space.
- **Non-monotonicity (§2.6.5, Fig 5, Fig 9).** At α = 0 and 0.1 there is
  a borderline band with no pure equilibrium. There, in the mixed
  equilibrium, a player who cares more about truth faces an opponent who
  must more often play strategies that frustrate it, so collective
  accuracy dips as w rises. The dip survives a utilitarian
  equilibrium-selection rule.

What could have come out otherwise: mutual boldness could have been an
equilibrium wherever truth is valued, as it is at high w in short
debates. Accuracy could have risen monotonically in w.

## What this does not say

- **Not that a group settles on a belief no member reasoned to.** The
  outcome measured is collective accuracy, the mean of two individual
  accuracies. Consensus is tracked separately and is not the result.
- **Not about communities.** There are two debaters. Whether the
  snowdrift becomes a many-player public-goods problem is untested.
- **Not that truth-seeking motives backfire in general.** The dip is
  local, small and confined to a band of mixed equilibria. At high truth
  weight in short debates the unique equilibrium is truth-optimal.
- **Not about debaters with pure epistemic motives.** Obstinacy is built
  into the utility. The paper argues informally (§3) that obstinacy is
  rational under deductive refutation. The result holds for agents who
  pay a cost to revise.
- **Not robust to the strategy space, as far as shown.** Strategies are
  fixed, memoryless rules over current positions. The targeted
  "ideal cooperative debater" lies outside them, and so does any
  learning.
- **Not independent of equilibrium selection.** (Exit, Exit) is an
  equilibrium everywhere. The regimes describe the truth-optimal
  equilibrium among those left after removing weakly dominated
  strategies.

## Connections

- **[QUESTION-047](../questions.d/QUESTION-047.md).** A named mechanism by which individually rational
  inquirers produce a worse collective epistemic state: the costs of
  being refuted are private and the benefits shared. It bears on the
  question's "which mechanisms", for a pair. No `answers:` relation is
  declared, because the paper does not show a belief that the pair
  settles on.
- **[THEORY-148](THEORY-148.md) (transient diversity).** Both concern how much
  disagreement a group should sustain. There, too little lasting
  diversity loses the better option. Here, refusal to bear revision
  costs leaves disagreement standing where mutual boldness would have
  removed it. The paper cites Zollman for "why expert communities
  sometimes maintain mistaken consensus" without modelling it.
