---
number: 830
status: Proposed
formerly:
- CLAIM-tmply70l
title: 'The mean-field derivation of the Barabási–Albert power law is the age mechanism in logarithmic time, so what separates linear preferential attachment from Gibrat''s lognormal growth is the continual entry of new units and not the proportionality of growth'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the change of variables: uniform birth times on [0, t] not
  giving exponentially distributed log-ages ln(t/t_i), or k ∝ (t/t_i)^(1/2)
  not being exponential growth at rate 1/2 in ln t; or a linear-attachment
  model without entry of new units, a fixed set of nodes sharing links in
  proportion to degree, whose degree tail is a power law; or the objection
  that this only restates CLAIM-795's item 6.
tags:
- probabilistic-modeling
- network-science
- complex-systems
date: '2026-11-21'
line:
- formal-apparatus
grounds:
- LIT-3004
- LIT-3007
summary: >-
  Fills a gap in the exchange "Rich Get Richer Power Laws". A says that
  linear preferential attachment "involves proportional expected growth"
  (A3 §4), contrasts it with Gibrat growth, which gives a lognormal, and
  separately gives the age mechanism (A5 §6), but never connects the
  two. In logarithmic time a Barabási–Albert node grows as e^(a/2), where
  a = ln(t/t_i) is its log-age. Uniform births make a exponential with
  rate 1, so P(K ≥ k) = k^(−1/(1/2)) = k^(−2), which is Reed's s^(−λ/g).
  Proportional growth is common to both. Entry is what makes the Pareto:
  without it, linear attachment among fixed nodes is a Pólya urn with a
  near-exponential spread.
  Checked by simulation with python3 -I: log-ages have mean 1.000, the
  CCDF slope is −1.98, and the 100 largest hubs were all born in the first
  1% of the growth. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
bears_on:
- QUESTION-505
---
<!-- inactive-ok-file: THEORY-tmp6jdas THEORY-tmpw4qgu THEORY-tmphcnj3 TERM-tmpg1vx2 — Proposed; the readings of 2026-11-22 and the term filed as the other alternative -->
<!-- inactive-ok-file: LIT-tmp7g7aj — Deferred; Simon (1955), registered and unread -->
<!-- inactive-ok-file: LIT-3004 LIT-3007 — Deferred; registered from this exchange and not read -->
<!-- inactive-ok-file: CLAIM-795 CLAIM-824 CLAIM-817 CLAIM-806 THEORY-2150 ARG-144 — Proposed or new; claims and the question filed with this one from the same exchange -->

# CLAIM-830: The mean-field derivation of the Barabási–Albert power law is the age mechanism in logarithmic time, so what separates linear preferential attachment from Gibrat's lognormal growth is the continual entry of new units and not the proportionality of growth

## The gap

A3 §4: "Preferential attachment itself involves proportional expected
growth. Multiplicative growth can interact with preferential
attachment." A3 §2: pure multiplicative growth gives a lognormal. A3 §1:
"the arrival of new participants keeps introducing small nodes, while
cumulative advantage allows some older nodes to become exceptionally
large." A5 §6: a common exponential growth rate with exponentially
distributed ages gives P(S > s) ∝ s^(−λ/g) (Reed, [LIT-3007](../literature.d/LIT-3007.md)). A does
not say that the first is an instance of the last, or which ingredient
makes the power law.

## The derivation

A1 §3's mean-field solution is k_i(t) = (t/t_i)^(1/2) (Barabási and
Albert, [LIT-3004](../literature.d/LIT-3004.md)). Write it in logarithmic time, u = ln t:

    k_i = exp((u − u_i)/2) = exp(a_i/2),   a_i = ln(t/t_i).

So every node grows exponentially at the same rate g = 1/2 in u. Degree
is proportional growth with no spread of rates. Birth times are uniform on
[0, t], so P(a > x) = P(t_i < t e^(−x)) = e^(−x). The log-ages are
exponential with rate λ = 1. Reed's formula then gives

    P(K ≥ k) = P(a ≥ 2 ln k) = k^(−2),

which is A1's P(K ≥ k) ∝ k^(−2), and the exponent is λ/g = 1/(1/2).

**So**: with no entry, every node is the same age and proportional growth
gives no spread in this mean-field picture. Stochastically, a fixed set
of nodes that share new links in proportion to degree is a Pólya urn.
From equal starts its shares tend to a flat Dirichlet law, so degrees
divided by their mean are close to exponential, not Pareto. Checked: 500
nodes, 200,000 links, exact sequential draws. The shares above 1, 2 and 3
times the mean are 0.366, 0.140 and 0.048, against e^(−1), e^(−2) and
e^(−3) = 0.368, 0.135 and 0.050. Pure Gibrat growth, with independent
returns, gives a lognormal that only widens ([CLAIM-824](CLAIM-824.md)). With entry
at a constant rate, the spread of ages turns proportional growth into a
Pareto tail. Linear attachment and Gibrat
growth agree on proportionality and differ on entry. Simon's model has the
same structure, with new words entering at a fixed rate.

## Checked (with python3 -I)

A tree grown to N = 300,000 by linear attachment, one link per node:

- Log-ages a = ln(N/t_i): mean 1.000 against 1, P(a > 2) = 0.1353
  against e^(−2) = 0.1353.
- CCDF of degree over k = 4 to 128: slope −1.98, against −2.
- The 100 largest hubs were all born in the first 1% of the growth.
- But the correlation between log k and the mean-field log-prediction
  ½·ln(N/t_i) is only 0.635. At a given age, degrees spread widely,
  because the early random gains compound. The age mechanism accounts for
  the exponent, which the exact master-equation solution confirms (A1's
  k^(−3)), and not for any one node's degree.

## What it does not say

- Not that the age mechanism is all of preferential attachment. Within an
  age cohort the stochastic advantage still sorts nodes, which is the
  rich-get-richer part proper.
- Not that every Pareto tail from growth comes from entry. A floor does
  it too (Kesten, [CLAIM-824](CLAIM-824.md)).
- On the objection that this restates [CLAIM-795](CLAIM-795.md)'s item 6: it does
  use that result. What it adds is the identification, which A does not
  make, and the consequence for telling attachment from Gibrat growth
  ([CLAIM-817](CLAIM-817.md)'s correction, [CLAIM-806](CLAIM-806.md)'s ratio of rates).

## Note of 2026-11-21: Mitzenmacher, read

Mitzenmacher's review ([LIT-3003](../literature.d/LIT-3003.md), read in [NOTE-2237](../notes.d/NOTE-2237.md); the reading is
[THEORY-2150](../theory.d/THEORY-2150.md)) **supports the age half and leaves the identification
open**. §7 gives multiplicative growth observed at an exponentially
distributed time as a power law ("we examine the random variable X_T where
T itself is a random variable"), with Huberman and Adamic's exponentially
distributed site ages on a growing Web as the example and Reed's double
Pareto as the exact law: for zero drift, density ∝ x^(−1−√(2λ)) above 1.
§3's attachment model always has entry, a new page at each step, and its
exponent with a uniform share α, (2 − α)/(1 − α) in density, is 3 at
α = ½, the Barabási–Albert k^(−3). But the paper keeps §3 and §7 apart and
never casts attachment in log-time, so the identification this claim makes
is not in it. It moves from `grounds` to `corroborates` ([ARG-144](../arguments.d/ARG-144.md)).
Status unchanged.

## Note of 2026-11-22: Newman, read

Newman's review ([LIT-2976](../literature.d/LIT-2976.md), read in [NOTE-tmpa7yd2](../notes.d/NOTE-tmpa7yd2.md); the reading is
[THEORY-tmp6jdas](../theory.d/THEORY-tmp6jdas.md)) **supports the entry point implicitly**: every Yule
variant founds a new unit each step and gives α = 2 + (k0 + c)/m (§IV.D,
pp. 17–19), so entry is built in wherever he gets a power law from
proportional gains. He does not cast the process in logarithmic time.

## Note of 2026-11-22: the name "Gibrat" (alternative b)

This note is **alternative (b)** of two, for the owner to choose; it
stands alone if the owner prefers no term. Alternative (a), the lean, is
[TERM-tmpg1vx2](../terms.d/TERM-tmpg1vx2.md), which gives the senses of "Gibrat's law" with sources.

Newman reports that Simon "dubbed this type of “rich-get-richer” process
the Gibrat principle" ([LIT-2976](../literature.d/LIT-2976.md), p. 18; Simon 1955, [LIT-tmp7g7aj](../literature.d/LIT-tmp7g7aj.md),
unread), naming the rule of gains in proportion to size in the very
setting, with entry, that gives the Yule–Simon power law. This claim's
title uses "Gibrat's lognormal growth" for proportional growth without
entry. The two uses agree on the rule and differ on the setting, which
is this claim's own thesis: proportionality is shared, and entry
separates the power law from the lognormal. Read "Gibrat growth" here as
"proportional growth without entry or a floor"; a reader coming from
Simon or Newman would otherwise take "Gibrat" to mean the attachment
rule itself. The wording is the assistant's (Claude, in this session);
adopting it is the owner's call.

## Note of 2026-11-22: Clauset, Shalizi and Newman, read

**Background** ([LIT-2987](../literature.d/LIT-2987.md), [NOTE-tmphbwdu](../notes.d/NOTE-tmphbwdu.md), [THEORY-tmpw4qgu](../theory.d/THEORY-tmpw4qgu.md)). At realistic
sample sizes a lognormal and a power-law tail are "very closely equal"
(p. 26), so whether entry is at work cannot be read from a fitted
cross-section; it has to be read from the dynamics. No edge.

## Note of 2026-11-22: Broido and Clauset, read

**A parallel** ([LIT-2963](../literature.d/LIT-2963.md), [NOTE-tmpleyjh](../notes.d/NOTE-tmpleyjh.md), [THEORY-tmphcnj3](../theory.d/THEORY-tmphcnj3.md)). Lognormal-like
degree tails are common (at least as good a fit as the power law for
88%), and the paper calls for "mechanisms that produce non-scale-free
structural patterns, e.g., those with degree distributions better fitted
by a log-normal". It names neither Gibrat nor multiplicative growth. No
edge. Status unchanged.
