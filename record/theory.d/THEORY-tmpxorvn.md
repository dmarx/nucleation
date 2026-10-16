---
status: Active
title: "In the iterated Prisoner's Dilemma with a probability w of meeting again, no strategy does better against an established TIT FOR TAT than TIT FOR TAT does against itself if and only if w ≥ (T−R)/(T−P) and w ≥ (T−R)/(R−S); always defecting is stable for every w, a cluster of reciprocators can invade it, and a nice stable strategy resists clusters, but the stability is only neutral, since always cooperating ties"
version: 1
tags:
- natural-sciences
- game-theory
date: '2026-10-16'
source:
- LIT-498
summary: >-
  Axelrod & Hamilton (1981), [LIT-498](../literature.d/LIT-498.md), read in full in [NOTE-411](../notes.d/NOTE-411.md). Against
  TIT FOR TAT the best reply is always-defect or alternation, which gives
  the condition on w. The cluster result and the "ratchet" are explicit
  payoff comparisons. "Evolutionarily stable" here means no mutant does
  better, which is weaker than Maynard Smith and Price's definition: always
  cooperate does exactly as well. The model is deterministic and error-free.
  Tournament robustness is a separate, empirical claim about the strategies
  people submitted.
extended_by:
- THEORY-tmpkifk7
---

# THEORY-tmpxorvn: In the iterated Prisoner's Dilemma with a probability w of meeting again, no strategy does better against an established TIT FOR TAT than TIT FOR TAT does against itself if and only if w ≥ (T−R)/(T−P) and w ≥ (T−R)/(R−S); always defecting is stable for every w, a cluster of reciprocators can invade it, and a nice stable strategy resists clusters, but the stability is only neutral, since always cooperating ties

## Source

Axelrod & Hamilton (1981), [LIT-498](../literature.d/LIT-498.md) (*Science* 211: 1390–1396), read in full
in [NOTE-411](../notes.d/NOTE-411.md). Two inequalities lost their right-hand sides in extraction and
are reconstructed from the payoff sums the text states; they agree with
condition (1), which survived.

## What was actually shown

**The game.** A two-player Prisoner's Dilemma with T > R > P > S and
R > (S + T)/2, payoffs in fitness. After each move the pair meets again with
probability w. Players recognize a previous partner and remember at least
the last move.

**Stability.** Against TIT FOR TAT only two replies need checking. TIT FOR
TAT against itself earns R/(1 − w). Always-defect earns T + wP/(1 − w).
Alternating defection and cooperation earns (T + wS)/(1 − w²). So no
strategy does better than TIT FOR TAT iff w ≥ (T − R)/(T − P) and
w ≥ (T − R)/(R − S) (condition 1).

**Always-defect** is evolutionarily stable for every w: a single
reciprocator among defectors loses.

**Initial viability.** A cluster of TIT FOR TAT whose members spend a
fraction p of their interactions with one another earns
p[R/(1 − w)] + (1 − p)[S + wP/(1 − w)]. That beats always-defect's
P/(1 − w) for large enough p and w. Kinship is the other route: reckoned in
inclusive fitness, the dilemma can disappear between relatives. That route
is argued verbally.

**The ratchet.** A nice strategy that is evolutionarily stable cannot be
invaded by a cluster of any other strategy.

**Robustness.** TIT FOR TAT won two computer tournaments (14 entries and
then 62) and went to fixation in an ecological replay. [NOTE-411](../notes.d/NOTE-411.md) rates this
moderate: the environment was whatever strategies people submitted.

**What could have come out otherwise.** The best reply to TIT FOR TAT could
have been some cleverer exploiter than the two checked, and clusters could
have failed to beat always-defect at any p. Neither holds.

## What this does not say

- **That TIT FOR TAT is an ESS in the strict sense.** Always cooperate does
  exactly as well against it, so by the two-part definition in Maynard
  Smith & Price ([LIT-505](../literature.d/LIT-505.md)) it is only neutrally stable. Boyd & Lorberbaum
  (1987) proved that no pure strategy is evolutionarily stable in the
  repeated game. That paper was checked on Crossref and not read.
- **That TIT FOR TAT is best with noise.** Strategies here are error-free.
  Nowak ([LIT-501](../literature.d/LIT-501.md)) reports that TIT FOR TAT declines under errors and that
  generous variants and win-stay, lose-shift replace it.
- **That reciprocity is common in nature.** The applications (fig wasps,
  cleaner fish, territorial birds) are illustrations. Those on cancer onset
  and nondisjunction are labelled "pure speculation" by the authors.
- **That the formal proofs are given.** They are deferred to Axelrod's
  forthcoming paper (note 19).
- **Anything about morality.** TIT FOR TAT's properties (nice, provocable,
  forgiving) are behaviours, not judgements.

## Connections

- Trivers ([LIT-510](../literature.d/LIT-510.md), [THEORY-tmpx3n05](THEORY-tmpx3n05.md)) gave the verbal model this formalizes.
  Hamilton had given him the Prisoner's Dilemma framing.
- Hamilton's Part I ([LIT-497](../literature.d/LIT-497.md), [THEORY-tmp15rjw](THEORY-tmp15rjw.md)) supplies the kinship route.
- Nowak ([LIT-501](../literature.d/LIT-501.md), [THEORY-tmpkifk7](THEORY-tmpkifk7.md)) restates direct reciprocity for the
  donation game as w > c/b.
- The continuation probability w is the "shadow of the future" that moral
  disciplining ([LIT-101](../literature.d/LIT-101.md)) needs. Its reading ([NOTE-132](../notes.d/NOTE-132.md), A1) cites Axelrod for
  the claim that reciprocal cooperation requires delayed gratification.
