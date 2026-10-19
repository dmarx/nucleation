---
number: 290
status: Active
formerly:
- THEORY-tmpvtupa
title: "In a two-debater, three-proposition model of deductive debate whose payoff trades true beliefs against changes of mind, the most truth-conducive equilibrium can fall short of the truth-optimal profile because one debater free-rides on the other's belief-disrupting arguments, and in a narrow band of mixed equilibria a higher weight on truth gives lower equilibrium accuracy"
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Narrowed and promoted, carrying out the promotion audit's decision file
    for THEORY-290 (batch 041, ADR-047 v3). The study was read in full, and
    its results are exact computations on one model, so it counts as one
    study, as THEORY-178's model ensemble did. The title now claims no more
    than the model showed: two debaters, three propositions, fixed
    memoryless strategies, the most truth-conducive equilibrium, and the
    accuracy dip confined to the band of mixed equilibria where it was
    found. The promote_when, asking for groups or richer strategies, moves
    unchanged to QUESTION-173.
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
  at high truth weight in short debates there is no dilemma. The title
  claims the model only; groups and richer strategies are QUESTION-173.
---
<!-- inactive-ok-file: THEORY-148 — Proposed; the transient-diversity account this one is set beside -->

# THEORY-290: In a two-debater, three-proposition model of deductive debate whose payoff trades true beliefs against changes of mind, the most truth-conducive equilibrium can fall short of the truth-optimal profile because one debater free-rides on the other's belief-disrupting arguments, and in a narrow band of mixed equilibria a higher weight on truth gives lower equilibrium accuracy

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

## Note of 2026-10-19: what the narrowing keeps and why

The promotion audit reviewed this entry in batch 041. Its title is a model
result, not an argument: "argument" there names what the debaters exchange.
It is not a theorem either. The paper proves nothing, and checking it by
hand would mean recomputing a 2,816-state Markov chain over a 17 × 17
payoff table. So it was judged as one study under [ADR-047](../decisions.d/ADR-047.md) v3, on the
precedent of [THEORY-178](THEORY-178.md).

- **Kept:** the snowdrift equilibrium (§2.6.3, Table 1 at δ = 0.8, Fig 5)
  and the dip in accuracy as the truth weight rises, which Fig 5 shows and
  [NOTE-795](../notes.d/NOTE-795.md) viewed as a rendered page. The dip is small and lies in the band
  without a pure equilibrium, and the title now says where it lies.
- **Dropped:** the unqualified "debaters". Every exact result is for two
  players and n = 3, and the strategy space excludes the targeted "ideal
  cooperative debater". Those extensions are [QUESTION-173](../questions.d/QUESTION-173.md).
- **Still carried by the body:** the dependence on equilibrium selection.
  (Exit, Exit) is always an equilibrium, and the regimes describe the most
  truth-conducive equilibrium left after removing weakly dominated
  strategies.
