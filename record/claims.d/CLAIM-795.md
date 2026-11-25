---
number: 795
status: Proposed
formerly:
- CLAIM-tmp1dlyp
title: 'Power laws without positive feedback'
statement: >-
  Power laws arise from many mechanisms with no positive feedback: a
  branching process balanced between extinction and growth, a tuned critical
  point, first-passage times of a random walk, a mixture of exponential
  rates, sample-space reduction, steady growth with a spread of ages, and an
  inverse power of a uniform variable
version: 3
history:
- version: 2
  date: '2026-11-22'
  note: >-
    Edited in place on 2026-11-22 after Newman's review (LIT-2976) was
    read: the review is said to ground items 2, 3, 6 and 7 only, item 3
    notes Newman's first-return derivation, the summary no longer calls
    all the works unread, and THEORY-2169 replaces LIT-2976 in
    grounds (ARG-168). Newman's further mechanisms are in the note
    of that date. The thesis and status are unchanged.
- version: 3
  date: '2026-11-22'
  note: >-
    Edited in place on 2026-11-22 after Beck and Cohen (LIT-2962),
    Corominas-Murtra, Hanel and Thurner (LIT-2997) and Reed and Hughes
    (LIT-3007) were read: items 4, 5 and 6 now name their readings, with
    item 4 qualified by CLAIM-857 (only spreads with power-law weight
    at zero rate), item 5 given the tunable family and the limit of the
    proof, and item 6 marked as Reed's deterministic case with the double
    Pareto beside it; THEORY-2176, THEORY-2175 and THEORY-2177
    replace the three LITs in grounds (ARG-175, ARG-177,
    ARG-176); the summary no longer calls them unread. The thesis and
    status are unchanged.
role: thesis
warrant: demonstrated
defeated_if: >-
  One of the seven constructions shown not to give a power-law tail under
  the conditions A states (a critical branching process with finite
  offspring variance, a symmetric one-dimensional walk, a gamma spread of
  rates, the uniform sample-space-reducing process, exponential ages with
  a common growth rate, X = 1/U), or shown to need a rich-get-richer
  feedback after all.
tags:
- probabilistic-modeling
- complex-systems
- mathematics
date: '2026-11-21'
line:
- formal-apparatus
grounds:
- THEORY-2175
- THEORY-2177
- THEORY-2176
- LIT-2992
- THEORY-2131
- CASE-303
- THEORY-2169
summary: >-
  A's catalogue at A5 of the exchange "Rich Get Richer Power Laws"
  (2026-11-20), answering the owner's U3 ("are there other processes that
  manifest power laws?"), with A3's sandpile and Kesten process making ten
  in A5's summary table. Each of the seven constructions was rechecked in
  this session, analytically or by simulation with python3 -I. A's
  unifying theme, "the absence of a characteristic scale", and its
  reasoning's "a hazard proportional to 1/x produces power-law survival"
  are kept as glosses, not as further claims. Newman's review, read on
  2026-11-22, grounds items 2, 3, 6 and 7 and adds four further
  mechanisms. Beck and Cohen, Corominas-Murtra, Hanel and Thurner, and
  Reed and Hughes, read on 2026-11-22, ground items 4, 5 and 6, item 4
  only for spreads with power-law weight at zero rate ([CLAIM-857](CLAIM-857.md)).
  Bak, Tang and Wiesenfeld's reading bears on the sandpile (note of
  2026-11-22). The wording is A's (the other assistant in the exchange
  "Rich Get Richer Power Laws", A5); adopting it is the owner's call.
bears_on:
- QUESTION-505
---
<!-- inactive-ok-file: THEORY-2169 ARG-168 LIT-3040 LIT-3031 LIT-3030 LIT-3036 — Proposed or Deferred; Newman's reading, the argument for it, and the works it names for the further mechanisms, registered and unread -->
<!-- inactive-ok-file: THEORY-2176 THEORY-2175 THEORY-2177 CLAIM-857 ARG-175 ARG-177 ARG-176 THEORY-2179 — Proposed; the readings of 2026-11-22 for items 4, 5 and 6 and the sandpile, the assistant's condition on the spread, and the arguments for their support -->
<!-- inactive-ok-file: THEORY-2131 CASE-303 CLAIM-769 CLAIM-815 CLAIM-824 CLAIM-803 THEORY-2150 — Proposed or new; held readings and claims, and entries filed with this one -->

# CLAIM-795: Power laws without positive feedback

## The catalogue (A5), each rechecked

A5 opens: "there is a surprisingly large family of processes that generate
power laws, many of which have **nothing to do with rich-get-richer
dynamics, compounding wealth, or self-organized criticality**." Newman's
review ([LIT-2976](../literature.d/LIT-2976.md)) is A's general reference; read on 2026-11-22, it
grounds items 2, 3, 6 and 7 only ([THEORY-2169](../theory.d/THEORY-2169.md), [ARG-168](../arguments.d/ARG-168.md)).

1. **Critical branching** (§1). At R = 1 with finite, nonzero offspring
   variance, P(S = s) ∝ s^(−3/2). Checked for Poisson offspring in
   [CASE-303](../cases.d/CASE-303.md). s^(3/2)·P(S = s) tends to (2π)^(−1/2) = 0.399.
2. **Tuned criticality** (§2). Site percolation on the square lattice,
   p_c ≈ 0.5927, n_s ∝ s^(−τ) with τ = 187/91 ≈ 2.055 in two dimensions.
   The arithmetic checks. The exponent is the standard 2D value, not
   rederived here. The criticality side belongs to the record's
   criticality entries filed from this exchange.
3. **First passage** (§3). A symmetric walk first reaches a boundary at
   time t with probability ∝ t^(−3/2), "connected to the Sparre Andersen
   universality theorem". Checked: (1/t)·P(S_t = −1)·t^(3/2) tends to
   sqrt(2/π) = 0.798 (0.797 at t = 1,001), and simulation matches the
   formula (P(T = 11) 0.0210 simulated, 0.0205 exact). Why the 3/2 is
   shared with item 1 is [CLAIM-815](CLAIM-815.md). Newman (§IV.C) gives the same 3/2
   for the first return of a symmetric walk to the origin, by generating
   functions.
4. **Mixtures** (§4). Exponential waiting times with gamma-distributed
   rates give P(T > t) = (b/(b + t))^a. Checked at a = 1.5, b = 2 by two
   million draws: 0.0680 against 0.0680 at t = 10, 0.00272 against
   0.00275 at t = 100. The record holds this ([THEORY-2131](../theory.d/THEORY-2131.md), [CLAIM-769](CLAIM-769.md)). A
   adds superstatistics (Beck, [LIT-2962](../literature.d/LIT-2962.md)) and the warning that "If a
   dataset displays a power law, that does not necessarily mean any
   individual entity follows power-law dynamics". See the note of
   2026-11-21 on [CLAIM-769](CLAIM-769.md). Beck and Cohen, read ([THEORY-2176](../theory.d/THEORY-2176.md)), give the
   formula as their eq. 13 with energy for time, (1 + bE)^(−c), the
   exponent the gamma's shape. Only some spreads give a power law: their
   uniform density bounded away from zero keeps an exponential tail, and
   the tail is a power exactly when the spread has power-law weight at
   zero rate ([CLAIM-857](CLAIM-857.md), the assistant's; [ARG-175](../arguments.d/ARG-175.md)).
5. **Sample-space reduction** (§5). A walk that jumps uniformly to a lower
   state until it reaches 1 visits state k with probability 1/k, Zipf's
   law (Corominas-Murtra, Hanel and Thurner, [LIT-2997](../literature.d/LIT-2997.md), unnamed by
   A). Checked over 200,000 runs from 100: 0.499, 0.199, 0.101 and 0.0201
   at k = 2, 5, 10 and 50. Their eq. 1 proves it by induction for exactly
   this uniform process ([THEORY-2175](../theory.d/THEORY-2175.md); [ARG-177](../arguments.d/ARG-177.md)). The exponent is
   tunable: mixing each nested step with probability 1 − λ with a uniform
   jump over all states gives occupation ∝ k^(−λ), frequency exponent
   (1 + λ)/λ. Their abstract's "necessarily lead to Zipf's law" is wider
   than the proof, which covers uniform jumps only.
6. **Growth with a spread of ages** (§6). A common growth rate g and
   exponential ages with rate λ give P(S > s) = (s/S_0)^(−λ/g) (Reed,
   [LIT-3007](../literature.d/LIT-3007.md)). Checked at λ = 1, g = 0.5: 0.0101 against 0.0100 at
   s = 10. "Even **identical growth rates** can coexist with highly
   unequal sizes." Reed and Hughes, read ([THEORY-2177](../theory.d/THEORY-2177.md); [ARG-176](../arguments.d/ARG-176.md)):
   the formula is their deterministic "simple case" (p. 1), not their
   result. With noisy growth (geometric Brownian motion of drift μ and
   volatility σ, killed at rate ν) the law is a double Pareto, its upper
   exponent the positive root of ½σ²s² + (μ − ½σ²)s − ν = 0, √(2ν)/σ at zero
   log drift, tending to ν/μ as σ → 0, with a lower power tail too. The
   gloss on identical growth rates is A's.
7. **Change of variables and geometry** (§7). X = 1/U gives P(X > x) =
   1/x, density x^(−2). A point uniform in a d-ball with influence r^(−β)
   gives P(F > f) = P(r < f^(−1/β)) = f^(−d/β).

To these A3 adds the sandpile (Bak, Tang and Wiesenfeld, [LIT-2992](../literature.d/LIT-2992.md))
and the Kesten process ([CLAIM-824](CLAIM-824.md)), and A1 adds preferential
attachment.

## Glosses kept, not filed

- **A's unifier** (A5): "the most productive way to understand the
  diversity of mechanisms is through **the absence of a characteristic
  scale** … Different processes eliminate or obscure characteristic
  scales in different ways." That is close to a definition of a power
  law, so it is kept as a reading aid. Scale invariance as such belongs to
  the record's criticality entries from this exchange.
- **A's reasoning** (A5, not shown): "a hazard proportional to 1/x
  produces power-law survival". Exact: h(x) = α/x gives
  S(x) = exp(−∫α/u du) = (x/x_0)^(−α). It restates the result in hazard
  form, and does not explain why the hazard falls as 1/x.
- **Density and survival exponents.** A moves between P(X = x) ∝ x^(−γ)
  and P(X > x) ∝ x^(−α) without saying α = γ − 1, though its own
  reasoning planned to "separate density from CCDF exponents" (A4). The
  BA model's k^(−3) and k^(−2) (A1) and the cascade's s^(−3/2) and
  s^(−1/2) (A8 §4) are each one law stated both ways.

## What it does not say

- Not that the list is complete, nor that the mechanisms are exclusive
  (A3 §4: "Real complex systems can combine all three").
- Not which mechanism produced any observed tail ([CLAIM-803](CLAIM-803.md)).
- Not what fixes the exponents ([QUESTION-505](../questions.d/QUESTION-505.md)).

## Note of 2026-11-21: Mitzenmacher, read

Mitzenmacher's review ([LIT-3003](../literature.d/LIT-3003.md), read in [NOTE-2237](../notes.d/NOTE-2237.md); the reading is
[THEORY-2150](../theory.d/THEORY-2150.md)) **corroborates item 6** and **finds two omissions**.

- **Item 6.** §7: a lognormal of mean 0 and variance t, stopped at an
  exponential time of rate λ, has density ∝ x^(−1−√(2λ)) above 1 and
  x^(−1+√(2λ)) below, Reed's double Pareto. That is item 6 with zero
  drift instead of a common rate g, and with the exponent then set by the
  variance against the stopping rate. Checked by the filer (python3 -I):
  the integral at λ = ½ gives 0.00500 and 0.0000500 at x = 10 and 100,
  against √(λ/2)·x^(−1−√(2λ)).
- **Left out: random typing.** Miller's monkeys (§6), typing letters and a
  space at random, give Zipf's law in word frequencies with no feedback,
  no criticality and no optimization: with equal letter probabilities the
  frequency of a word falls as a power of its rank. It belongs on this
  list.
- **Left out: optimization.** Mandelbrot's derivation (§4), minimizing the
  cost per unit of information of a code, gives a power law in rank;
  Carlson and Doyle's highly optimized tolerance is cited as a modern
  version. No positive feedback is involved, though an optimizer is.

The catalogue is A's and does not claim completeness ("What it does not
say"), so these are additions, not defeaters. [THEORY-2150](../theory.d/THEORY-2150.md)
`corroborates` this claim. Status unchanged.

## Change of 2026-11-22

Newman's review read: the line calling it A's general reference now says
it grounds items 2, 3, 6 and 7 only; item 3 notes his first-return
derivation; the summary is updated; [THEORY-2169](../theory.d/THEORY-2169.md) replaces [LIT-2976](../literature.d/LIT-2976.md) in
`grounds`. Version 2.

## Note of 2026-11-22: Newman, read

Newman's review ([LIT-2976](../literature.d/LIT-2976.md), read in [NOTE-2261](../notes.d/NOTE-2261.md); the reading is
[THEORY-2169](../theory.d/THEORY-2169.md)) **grounds items 2, 3, 6 and 7**, **leaves items 1, 4 and
5 open**, and **adds four mechanisms** ([ARG-168](../arguments.d/ARG-168.md)).

- **Item 2.** Percolation at p_c = 0.5927462, and a coarse-graining
  argument that the cluster distribution is a power law at the critical
  point (§IV.E); no value of τ.
- **Item 3.** "So the distribution of return times follows a power law
  with exponent α = 3/2" (§IV.C, p. 16), for the first return to the
  origin, not first passage to a boundary.
- **Item 6.** Reed and Hughes as a combination of exponentials (§IV.A):
  y exponential with rate a and x ∝ e^(by) give α = 1 − a/b; with
  a = −λ, b = g this is the density exponent 1 + λ/g, the item's survival
  exponent λ/g (checked, python3 -I).
- **Item 7.** x = 1/y gives p(x) ∝ x^(−2), and x = y^(−γ) gives
  α = 1 + 1/γ (§IV.B); not the d-ball geometry.
- **Not in the review**: critical branching (item 1), mixtures of
  exponential rates (item 4; Newman's "combinations of exponentials" is
  item 6's mechanism, not a mixture), sample-space reduction (item 5).
- **Further mechanisms with no rich-get-richer feedback**, which the
  catalogue lacks: Miller's random typing (§IV.A; [LIT-3040](../literature.d/LIT-3040.md), already
  noted from Mitzenmacher), highly optimized tolerance (§IV.G; Carlson and
  Doyle, [LIT-3031](../literature.d/LIT-3031.md)), coherent noise (§IV.G; Sneppen and Newman,
  [LIT-3030](../literature.d/LIT-3030.md)) and record dynamics, waiting times between records with
  exponent 1 (§IV.G; Sibani and Littlewood, [LIT-3036](../literature.d/LIT-3036.md)). Highly
  optimized tolerance involves an optimizer, as Mitzenmacher's
  optimization does. The catalogue does not claim completeness, so these
  are additions, not defeaters.

Status unchanged.

## Change of 2026-11-22: Beck and Cohen, Corominas-Murtra, Hanel and Thurner, Reed and Hughes, read

Items 4, 5 and 6 name their readings: item 4 with the condition on the
spread ([CLAIM-857](CLAIM-857.md)), item 5 with the tunable family and the limit of
the proof, item 6 as Reed and Hughes's deterministic case with their
double Pareto beside it. [THEORY-2176](../theory.d/THEORY-2176.md), [THEORY-2175](../theory.d/THEORY-2175.md) and [THEORY-2177](../theory.d/THEORY-2177.md)
replace [LIT-2962](../literature.d/LIT-2962.md), [LIT-2997](../literature.d/LIT-2997.md) and [LIT-3007](../literature.d/LIT-3007.md) in `grounds` ([ARG-175](../arguments.d/ARG-175.md),
[ARG-177](../arguments.d/ARG-177.md), [ARG-176](../arguments.d/ARG-176.md)). The summary is updated. Version 3.

## Note of 2026-11-22: Beck and Cohen; Corominas-Murtra, Hanel and Thurner; Reed and Hughes, read

- **Beck and Cohen** ([LIT-2962](../literature.d/LIT-2962.md), read in [NOTE-2265](../notes.d/NOTE-2265.md); [THEORY-2176](../theory.d/THEORY-2176.md))
  **ground item 4, with a qualification.** Their eq. 13 is the item's
  gamma formula; their uniform and two-level densities keep exponential
  tails, and the large-E behaviour "strongly depends on the function
  f(β)" (p. 7). A spread gives a power law exactly when it has power-law
  weight at zero rate, and a lognormal spread gives a tail between every
  power and every exponential ([CLAIM-857](CLAIM-857.md), the assistant's, checked
  by quadrature). The item's `defeated_if` names a gamma spread, so the
  thesis stands; the label "a mixture of exponential rates" reads wider
  than what holds. The caution A quotes fits: each cell is ordinary
  Boltzmann–Gibbs, and only the average departs.
- **Corominas-Murtra, Hanel and Thurner** ([LIT-2997](../literature.d/LIT-2997.md), read in
  [NOTE-2266](../notes.d/NOTE-2266.md); [THEORY-2175](../theory.d/THEORY-2175.md)) **ground item 5** exactly, by their
  induction proof (eq. 1), and add the family k^(−λ). "History-dependent"
  in their title means state-dependent: the walk is a Markov chain with no
  reinforcement, which is the item's "no positive feedback".
- **Reed and Hughes** ([LIT-3007](../literature.d/LIT-3007.md), read in [NOTE-2264](../notes.d/NOTE-2264.md); [THEORY-2177](../theory.d/THEORY-2177.md))
  **ground item 6** as their deterministic case, and **qualify** it: the
  exponent is a bare ratio λ/g only without noise. They also give a second
  branching route, a supercritical Galton–Watson process killed
  geometrically, with exponent 1 + κ, κ = ln[1/(1 − p)]/ln μ, unrelated to
  item 1's critical 3/2; and a killed birth-and-death process whose power
  law gives way to a stretched exponential at λ = δ, where this mechanism
  fails. Both are further cases, not defeaters.

Status unchanged.

## Note of 2026-11-22: Bak, Tang and Wiesenfeld, read

The reading of Bak, Tang and Wiesenfeld ([LIT-2992](../literature.d/LIT-2992.md), read in [NOTE-2269](../notes.d/NOTE-2269.md);
the reading is [THEORY-2179](../theory.d/THEORY-2179.md)), filed in a parallel filing of this date,
**supports the sandpile addition** (A3) with a
**caution**: its chain reaction is "ever amplifying", so this claim's "no
positive feedback" holds for the sandpile only in the rich-get-richer
sense, that no unit's gain grows with its size; the avalanche itself
amplifies. None of its exponents is 3/2, so it does not join item 1's or
item 3's shared exponent ([CLAIM-815](CLAIM-815.md)): its cluster exponents are about
0.98 in two dimensions and 1.35 in three. The quotation was rechecked by
this filer against that reading's download (first page, of noise spreading "to
the neighbors in a chain reaction, ever amplifying"). [LIT-2992](../literature.d/LIT-2992.md) stays in
`grounds`; whether [THEORY-2179](../theory.d/THEORY-2179.md) should replace it is left to that
filing. Status unchanged.

