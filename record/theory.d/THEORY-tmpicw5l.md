---
status: Proposed
promote_when: >-
  A second randomised manipulation experiment on a different prediction
  market, preferably a real-money one with larger markets, that again
  finds most of a one-off random shock present after several weeks.
  Alternatively, a design that measures traders' beliefs before and
  after the shock and shows whether the persistence comes from learning
  from the price or from limited rebalancing. The first would establish
  the persistence beyond Manifold. The second would say whether the
  persistent price is something traders came to believe. More
  simulations of the authors' model cannot settle it, and neither can
  observational studies of historical manipulation attempts, which have
  no counterfactual price path.
title: "A prediction-market price can keep most of an arbitrary shock that no trader's information supported for at least sixty days, because later trading undoes only part of it and undoes it ever more slowly"
version: 1
tags:
- social-science
- epistemology
date: '2026-10-14'
source:
- LIT-958
summary: >-
  Rasooly and Rozzi (2025), [LIT-958](../literature.d/LIT-958.md), read in full in [NOTE-tmpda897](../notes.d/NOTE-tmpda897.md). A
  pre-registered field experiment on 817 Manifold markets found about
  59% of a random ±5-point shock still present after 60 days in
  unresolved markets. Reversion was 25% in week one and 6% more over the
  next three weeks. The paper's model gets partial persistence from
  finite, risk-averse traders even with no learning. The data cannot say
  whether traders came to believe the shocked price. Its evidence that
  more traders or an outside estimate reduce persistence is
  correlational and weak.
---
<!-- inactive-ok-file: THEORY-tmp3gjfu — Proposed; filed from a companion reading the same day -->

# THEORY-tmpicw5l: A prediction-market price can keep most of an arbitrary shock that no trader's information supported for at least sixty days, because later trading undoes only part of it and undoes it ever more slowly

## Source

Rasooly and Rozzi (2025), arXiv:2503.03312, [LIT-958](../literature.d/LIT-958.md), read in full in
[NOTE-tmpda897](../notes.d/NOTE-tmpda897.md).

## What was actually shown

- **The experiment (§§4–5).** 817 binary markets on Manifold were each
  assigned at random to a yes trade (+5 points), a no trade (−5 points)
  or control, and their hourly prices were recorded for 30 days with a
  snapshot at 60. The yes–no gap β̂1 was:
  - 0.0748 at 1 week, about 25% reversion (Table 3);
  - 0.0686 at 30 days, with 25% reversion in the first week and 6% in the
    next three;
  - 0.0586 [0.0114] at 60 days in the 771 unresolved markets, about 41%
    reversion (Table 2).
  All have p < 0.01. Effects were symmetric between yes and no. They
  survived dropping possibly related markets (Appendix C) and appeared,
  with faster reversion, in 110 real-money-convertible markets (§6).
- **The mechanism in the model (§2, Appendix A).** Traders are finitely
  many, each with finite wealth and risk aversion (DARA), and trade
  against a constant-product market maker. Lemma 3 proves every trader
  responds to an upward shock by pushing the price down. Simulations
  show the response is partial: with 11 traders and no learning, about
  60% of the shock remains once prices settle, and reversion slows as
  the price approaches its old value. More traders (82% reversion at
  m = 60) or a common prior (52%) undo more. Learning from the price
  undoes less, down to none at λ = 1 (Table A1).

What could have come out otherwise: the received view (Wolfers and
Zitzewitz) predicts reversion within a short transition, as Camerer
found at the racetrack within about 20 minutes. The randomised design
gives the counterfactual path that historical studies lacked.

## What this does not say

- **Not that traders came to believe the shocked price.** The model
  gives persistence even when no belief moves (λ = 0). The data cannot
  distinguish that from learning. Whether the price that persists is
  anyone's belief is open.
- **Not that a price is a group belief.** A price aggregates positions
  weighted by wealth and risk attitude. The claim is about an aggregate
  estimate departing from what members' information supports, not about
  a belief the community holds.
- **Not that trader count, volume or outside information *cause* lower
  manipulability.** Those differences are median splits on traits that
  were not randomised, at p between 0.04 and 0.19, and the authors flag
  this.
- **Not shown for large real-money markets.** Manifold runs mainly on
  play money redeemable as charity, and its user base is unusual. The
  real-money check is small (110 markets, about 6 days, no control). The
  authors *predict* more persistence in high-value markets, untested.
- **Not about other shock sizes.** The authors expect very large shocks
  to be less persistent, since they are not "credible". One size was
  tested.
- **Not "up to 60 days".** Sixty days was the last measurement, not where
  the effect ended.

## Connections

- **[QUESTION-047](../questions.d/QUESTION-047.md).** A measured case of a community-level estimate holding
  a value that no member reasoned to, because the value was set at
  random. It bears on the question's first clause in a weakened form:
  "settle on" an estimate rather than a belief. The question's second
  clause is answered in the model (number of traders, prior agreement,
  learning rate), but only correlationally in the field. No `answers:`
  relation is declared, because whether any member holds the persisting
  value is exactly what is unknown.
- **[THEORY-tmp3gjfu](THEORY-tmp3gjfu.md) (spiral of silence).** It shares the shape: an
  aggregate signal departs from what members hold, and members then read
  it as information. There the signal is expressed opinion; here it is
  price. In both cases the record lacks an empirical measure of members'
  private states.
