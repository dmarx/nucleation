---
number: 778
status: Read
formerly:
- NOTE-tmpda897
paper: LIT-958
title: 'Rasooly and Rozzi — How manipulable are prediction markets?'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from arXiv:2503.03312v1 (53 pages), text extracted with
    pdftotext: sections 1–7, Appendix A (the proofs of Lemmas 1–3),
    Appendix B (Tables A1–A5 and the figure captions) and Appendix C
    (spillovers, Table A6). The figures were read from captions and the
    text reporting them. The pre-registrations and replication package
    linked from the paper were not opened.
date: '2026-10-14'
summary: >-
  A randomised field experiment on 817 Manifold markets moved prices by
  ±5 percentage points. The yes–no gap of 10 points was 7.5 after a week,
  6.9 after 30 days and 5.9 after 60 days in unresolved markets, so about
  60% of an arbitrary shock was still there. Reversion is fast in the
  first week and then slows. A price-impact model with finite, risk-averse
  traders predicts lasting partial persistence even when no trader learns
  from the price. Markets with more traders, more activity or a Metaculus
  twin revert more, but those splits are correlational and only
  marginally significant.
---
<!-- inactive-ok-file: THEORY-267 — Proposed; the account filed from this reading -->

# NOTE-778: Rasooly and Rozzi — How manipulable are prediction markets?

## Contribution

It is the first large randomised field test of whether a trade made for
no informational reason moves a prediction market's price for long. It
does, for at least 60 days. Before it, the received view (Wolfers and
Zitzewitz 2004) was that manipulation has little effect "except during a
short transition phase". The paper also gives a model in which the
price's path after a shock can be traced, because traders take their
own price impact into account rather than being price-takers.

## Key insight

A market price is not a fixed point that sound traders restore after
any disturbance. With finitely many traders of finite wealth and risk
aversion, a shock is partly absorbed: each trader rebalances only partly,
and the price settles between the old value and the shocked one. Any
learning from the price makes the shock stick further. So the price can
carry a value that no trader's information supported.

## Assumptions

The model (§2):

- Finitely many traders i ∈ {0, …, m} with heterogeneous priors
  π_i ∈ [0, 1]. Common wealth w and a common vNM utility u with u′ > 0,
  u″ < 0, lim_{w→0+} u′(w) = ∞, and decreasing absolute risk aversion.
  The authors call DARA "unnecessarily strong". Without it a bound on
  the income effect is needed.
- Pricing by the constant-product automated market maker:
  (y + x − q)(n + x) = yn. A spend of x buys q = x(n + x + y)/(n + x)
  yes shares, and C(q) = [√((n − q + y)² + 4nq) + q − n − y]/2.
- No competitive equilibrium. Traders know their trades move the price.
- Simulations: u = ln w, m = 10 (11 traders), w = 100,
  (n, y) = (1000, 1000), uniform beliefs π_i = i/m, and one randomly
  chosen trader re-optimises per period. Variations: m up to 60; a
  learning rate λ with π_i′ = λp + (1 − λ)π_i; and prior agreement α with
  π_i = α(i/m) + (1 − α)·0.5.

The experiment (§§3–4):

- Manifold, around 10,000 active users, play money ("Mana") redeemable
  only as charity donations. Binary markets with at least 10 traders,
  resolving by the end of 2025, at most 200 Mana to move 5 points, not
  opened in the last 7 days and not closing within 30. Closely related
  markets were excluded.
- Each market was assigned with equal probability to yes (+5 points),
  no (−5 points) or control. Pre-registered (AEA RCT Registry), with
  power for a 3-point gap after one week.

## Key results

- **Lemma 1.** Under the constant-product rule the marginal cost is
  MC(0) = n/(n + y), rises in q, and tends to 1. The same holds for the
  average cost.
- **Lemma 2.** With p = n/(n + y): if π_i > p the trader buys yes; if
  π_i = p the trader holds nothing; if π_i < p the trader buys no. (This
  extends Arrow's local risk-neutrality argument to non-linear
  pricing.)
- **Lemma 3.** If the marginal price rises from p to p + Δ: traders with
  π_i ≥ p + Δ cut their yes holdings; traders with π_i ∈ (p, p + Δ)
  switch to no; traders with π_i ≤ p add to their no holdings. So every
  trader's adjustment pushes the price back. The proof is by the implicit
  function theorem on the first-order condition
  π_i u′(w + q − C(q)) / [(1 − π_i) u′(w − C(q))] = C′(q)/(1 − C′(q)),
  using DARA, with dq/dn < 0.
- **Simulations (Table A1).** Long-run reversion is the share of a
  0.05 shock undone by t = 100.
  - Baseline: about 40%.
  - Learning: reversion falls with λ, to 0% at λ = 1.
  - Agreement: a common prior raises it to 52%.
  - Number of traders: m = 60 raises it to 82%.
  - Even with no learning (λ = 0), 60% of the shock remains.
- **Main experiment (§5, n = 817).** The regression is
  p_{t,i} = β0 + β1·1_Y + β2·1_C + β3·p_{−1,i} + u_i.
  - β̂1 is 0.0748 at one week, about 25% reversion (Table 3).
  - It is 0.0686 at 30 days: 25% reversion in the first week and "just
    an additional 6%" over the next three.
  - At 60 days it is 0.0559 for the full sample and 0.0586 [0.0114] for
    the 771 markets not yet resolved, about 41% reversion (Table 2).
    The 46 resolved markets show no effect.
  - All estimates have p < 0.01. Yes and no shocks are symmetric
    (F-test of β1 = 2β2, p = 0.124).
- **Heterogeneity (Table 4, one-week effects, median splits).**
  - Metaculus twin: 0.053 against 0.077 (p = 0.096).
  - 24-hour volume: 0.049 against 0.081 (p = 0.041).
  - Total volume: 0.069 against 0.081 (p = 0.191).
  - Comments: 0.069 against 0.084 (p = 0.071).
  - Total traders: 0.067 against 0.083 (p = 0.056).
  - Reversion is 37% in the top quartile by traders, and still
    p < 0.01 there (Table A3).
  - The authors warn that, because these traits were not randomised,
    "one cannot be sure that any observed heterogeneities reflect the
    causal impact of these characteristics".
- **Follow-up (§6, 110 "Sweepcash" markets, real-money-convertible,
  ±4 points).** The gap is 0.080 on day 0, 0.0463 on day 6 and 0.0348 on
  day 7 in the 89-market subset (Table A5). Reversion is faster than in
  the main sample, but similar once both are restricted to markets with
  positive 24-hour volume (51% Mana, 43% Sweepcash).
- **Spillovers (Appendix C).** Random assignment cancels spillovers in
  expectation. Dropping the markets GPT-4 flagged as related leaves β̂1
  unchanged (0.075 on 556 and on 482 markets).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | A one-off 5-point shock to a prediction-market price is still largely present 60 days later | strong | randomised, pre-registered field experiment, n = 817, Table 2 |
| C2 | Reversion is fast in the first week and then slows | strong | Fig 4, Fig A6, Table 3 |
| C3 | In a price-impact model with finite risk-averse traders, a shock is undone only in part even when no trader learns from the price | moderate | Lemma 3 (qualitative, proved) and simulations, Table A1 (quantitative, one parameterisation) |
| C4 | Learning from the price makes shocks stickier, to no reversion at λ = 1 | moderate | simulation only; not identified in the data |
| C5 | Markets with more traders, more activity or an outside estimate are harder to manipulate | weak | median splits, p from 0.04 to 0.19, not randomised |
| C6 | Replacing play money with near-real money does not change manipulability much | weak | 110 markets, no control group, 6–7 days |

## Method

Randomised assignment at the market level, hourly prices from 24 hours
before to 30 days after, and a 60-day snapshot added after the fact. OLS
of price on treatment dummies and the pre-trade price, with robust
standard errors. Pre-registered, with the deviations listed in an
updated analysis plan.

## Concepts

- **Manipulation.** Here any trade made to move the price rather than on
  information; operationally, the experimenters' random trades.
- **Reversion.** The share of the initial yes–no gap undone by later
  trading, 1 − β̂1(t)/β̂1(0).
- **Learning rate λ.** How far a trader's belief moves toward the market
  price (Manski 2006).
- **Price-theory model.** A model of price formation from traders' demand
  that drops competitive equilibrium (in the tradition of Manski,
  Gjerstad, Wolfers and Zitzewitz).

## Connections

The paper builds on Manski's (2006) and Gjerstad's (2005) price-theory
models, and departs from the rational-expectations tradition (Hanson and
Oprea 2009). It sets itself against Camerer's (1998) racetrack bets, which
vanished within about 20 minutes, and against Rhode and Strumpf's (2006)
15 bets on the Iowa Electronic Markets.

## Bearing on the record

- **[QUESTION-047](../questions.d/QUESTION-047.md).** This paper gives the record's clearest *measured*
  case of a community-level estimate holding a value that no member's
  information supported. The price is the market's aggregate probability.
  Two features matter.
  - The shock was set at random, so no trader reasoned to it.
  - In the model, the price keeps most of it even with λ = 0, when no
    trader's belief has moved: persistence comes from finite wealth and
    risk aversion, not from anyone coming to believe the shocked value.
  It is filed as [THEORY-267](../theory.d/THEORY-267.md). The data cannot say whether the
  persistence in the field came from learning (beliefs moved) or from
  thin, budget-limited rebalancing (beliefs did not). For [QUESTION-047](../questions.d/QUESTION-047.md)
  that is the decisive difference, and it is open.
- **The LIT's seeded claim, checked.**
  - [LIT-958](../literature.d/LIT-958.md)'s body says the shocks "persist for up to 60 days". They
    persisted *at least* 60 days, which was the last measurement, and
    about 59% of the gap remained in unresolved markets.
  - "How long they persist depends on trader count, volume and outside
    information" overstates the evidence. Those splits are observational
    and mostly significant only at the 10% level, as the authors
    themselves caution (footnote 22).
  - Calling these "community-level mechanisms" is the record's gloss. The
    paper treats them as market characteristics.
- **The price is not a belief.** [QUESTION-047](../questions.d/QUESTION-047.md) asks about a belief a
  community settles on. A price is an aggregate of positions weighted by
  wealth and risk attitude, not a shared belief, and the paper never
  calls it one. The record should hold the case as an aggregate estimate
  coming apart from members' information, not as a group belief.
- No instruction for machine-learning practice; nothing for the
  anthology. The finding bears on prediction-market design and is
  economics, not ML.

## Limitations

- Manifold is unusual: play money redeemable as charity, a
  rationalist-leaning user base, and many bots. The authors argue
  its calibration is comparable to other platforms, but the Sweepcash
  check is small.
- One shock size. The authors expect a U-shaped relation between shock
  size and persistence (very large shocks are not "credible"), but do
  not test it.
- The 60-day result rests on a single snapshot that was not
  pre-registered.
- The model's quantitative reversion numbers come from one 11-trader
  parameterisation and are illustrative.
- Heterogeneity is correlational.

## Open questions

- In the field, is persistence driven by learning from the price or by
  limited rebalancing capacity? Surveying traders' beliefs before and
  after a shock would separate the two.
- Does persistence scale with market value? The authors predict that
  costlier shocks stick more and convey stronger signals.
- How does persistence depend on shock size, and is there an optimal
  manipulation?
- Can comments ("manipulation through buzz") move prices as trades do?
