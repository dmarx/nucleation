---
number: 824
status: Proposed
formerly:
- CLAIM-tmpiervv
title: 'Multiplicative growth with independent, identically distributed returns gives a lognormal cross-section, not a power law, but the same growth with an additive floor gives a stationary power-law tail whose exponent κ solves E[A^κ] = 1, a condition that requires the process to contract on average in logarithm'
version: 2
history:
- version: 2
  date: '2026-11-22'
  note: >-
    Edited in place on 2026-11-22 after Kesten (LIT-3005) was found
    Unfetched and two neighbours were read in its place, Kevei
    (LIT-tmpk12vu, THEORY-tmpsmrhx) and Alsmeyer and Mentemeier
    (LIT-tmpt282z, THEORY-tmpocjqv). `defeated_if` now carries the
    theorem's conditions as Kevei states them; the title's "even when the
    process contracts on average" becomes "a condition that requires" it,
    since E[A^κ] = 1 forces E log A < 0; `grounds` swaps the unread
    LIT-3005 for THEORY-tmpsmrhx (ARG-tmpn6ufb). The thesis and status
    are unchanged.
role: thesis
warrant: demonstrated
defeated_if: >-
  A process W' = AW + B with (A, B) i.i.d. and independent of W, A ≥ 0,
  meeting the theorem's conditions (E[A^κ] = 1 for some κ > 0,
  E[A^κ log⁺A] < ∞, log A non-arithmetic given A ≠ 0, E|B|^κ < ∞, and
  non-degeneracy, P(Ax + B = x) < 1 for every x) whose stationary law
  does not have P(W > x) ∼ c+ x^(−κ) and P(W < −x) ∼ c− x^(−κ) with
  c+ + c− > 0 (the tail may sit on one side only); or pure i.i.d.
  multiplicative growth with finite-variance log returns whose
  cross-section after many steps is not close to lognormal. E[log A] < 0
  and P(A > 1) > 0 are not further conditions: they follow from
  E[A^κ] = 1 with κ > 0 and A ≢ 1.
tags:
- probabilistic-modeling
- complex-systems
- mathematics
date: '2026-11-21'
line:
- formal-apparatus
grounds:
- THEORY-tmpsmrhx
- THEORY-696
summary: >-
  A's, from A3 §2 and §4 of the exchange "Rich Get Richer Power Laws"
  (2026-11-20). W_{t+1} = A_t W_t gives log W as a sum, hence a lognormal
  by the central limit theorem, with every unit facing the same returns.
  Adding B_t (W_{t+1} = A_t W_t + B_t, Kesten, LIT-3005, known through
  Kevei's restatement, THEORY-tmpsmrhx) gives P(W > x) ∝ x^(−κ) with
  E[A^κ] = 1, which forces E[log A] < 0, so "a process with an overall
  stabilizing tendency can still generate extreme outcomes". Checked by
  simulation in this session: with log A ~ N(−0.05, 0.3²), κ = 1.111 and
  the Hill estimate is 1.10 to 1.12. A3 §4's "these mechanisms are not
  mutually exclusive" is made concrete in the body. Kesten's paper is
  Unfetched; its theorem is held at second hand through two neighbours
  read in its place. The wording is A's (the other assistant in the
  exchange "Rich Get Richer Power Laws", A3); adopting it is the owner's
  call.
bears_on:
- QUESTION-505
---
<!-- inactive-ok-file: THEORY-tmp6jdas THEORY-tmpw4qgu THEORY-tmphcnj3 — Proposed; the readings of 2026-11-22 cited in the notes -->
<!-- inactive-ok-file: TERM-tmpg1vx2 — Proposed; the term filed on the name Gibrat -->
<!-- inactive-ok-file: LIT-3005 — Unfetched; Kesten, located and not read -->
<!-- inactive-ok-file: THEORY-tmpsmrhx THEORY-tmpocjqv NOTE-tmpv02cb NOTE-tmpy4hcs ARG-tmpn6ufb — Proposed, Skimmed or new; the neighbours' readings of 2026-11-22 and the argument on them -->
<!-- inactive-ok-file: LIT-tmpn76uh — Deferred; Goldie (1991), registered and unread -->
<!-- inactive-ok-file: CLAIM-830 CLAIM-795 CLAIM-803 THEORY-2150 ARG-140 — Proposed or new; claims filed with this one from the same exchange, and the reading and argument of 2026-11-21 -->

# CLAIM-824: Multiplicative growth with independent, identically distributed returns gives a lognormal cross-section, not a power law, but the same growth with an additive floor gives a stationary power-law tail whose exponent κ solves E[A^κ] = 1, a condition that requires the process to contract on average in logarithm

## The claim (A3 §2)

"**Multiplication becomes addition on a logarithmic scale.**" With
W_{t+1} = W_t A_t and i.i.d. finite-variance log A, log W_t is a sum, so W_t
is approximately lognormal. "Everyone might face exactly the same
distribution of returns. Yet large inequalities still emerge because
compounding amplifies differences across trajectories." But "A pure
multiplicative process generally produces a lognormal distribution at a
fixed time, rather than a true power-law tail."

With an additive term, W_{t+1} = A_t W_t + B_t, "Under suitable conditions,
including an overall tendency toward contraction but occasional growth
multipliers greater than one", the stationary law has P(W > x) ∝ x^(−κ)
with "**E[A^κ] = 1**" (Kesten, LIT-3005; the theorem as Kevei restates it is
THEORY-tmpsmrhx). "Rare sequences of favorable
multipliers compound into exceptionally large values."

The record holds geometric Brownian motion and its time-average growth
μ − σ²/2 ([THEORY-696](../theory.d/THEORY-696.md)), but not the lognormal cross-section or the
Kesten tail.

## Checked (the assistant, with python3 -I)

- **Kesten.** log A ~ N(μ, σ²) with μ = −0.05 and σ = 0.3, and B = 1.
  Then E[A^κ] = exp(κμ + κ²σ²/2) = 1 gives κ = −2μ/σ² = 1.111.
  400,000 paths run 3,000 steps give Hill estimates of 1.102, 1.116 and
  1.100 from the top 400, 1,000 and 4,000. The process contracts on
  average (E[log A] < 0), as A says it may.
- **Gibrat.** The same multipliers without B, over 300 steps: log W has
  skewness −0.001 and excess kurtosis 0.003. Normal, so W is lognormal.
- **A3's fixed-rate table.** $100 at 2%, 6% and 12% for 30 years gives
  $181, $574 and $2,996. Checked, and A labels it an illustration.

## Not mutually exclusive, made concrete (the assistant's)

A3 §4 asserts that the mechanisms "are not mutually exclusive" and gives
no combined model. Two exist in what is checked here:

- **Gibrat plus entry is Reed's mechanism.** A common growth rate with
  exponential ages gives a Pareto tail ([CLAIM-795](CLAIM-795.md), item 6). Linear
  preferential attachment is the same thing in logarithmic time
  ([CLAIM-830](CLAIM-830.md)).
- **Gibrat plus a floor is Kesten.** The additive B is a floor that stops
  log W from drifting off to −∞, so the lognormal spreading reaches a
  stationary state with a Pareto tail.

So the three ways a power law comes out of proportional growth are entry
(a spread of ages), a floor or reinjection, and both. A pure Gibrat
process with neither gives a lognormal that only widens.

## What it does not say

- Not that any real wealth or firm-size tail comes from either. A3 §2's
  policy reading, "reducing privileged access to opportunities addresses
  one mechanism, while changing the structure of compounding, shocks, or
  wealth floors addresses another", has no support in the exchange
  ([CLAIM-803](CLAIM-803.md)).
- Not the conditions in full. Kesten's theorem needs more than A states
  (see `defeated_if`, which since 2026-11-22 follows Kevei's statement).
  They are checked against Kevei's restatement, not against Kesten's
  paper, which is Unfetched.
- Not that a Pareto stationary tail shows the A-driven mechanism. By
  Grey's result, as Kevei reports it, with E[A^κ] < 1 the tail of W is
  regularly varying "if and only if the tail of B is": the tail can come
  from B alone.

## Note of 2026-11-21: Mitzenmacher, read

Mitzenmacher's review ([LIT-3003](../literature.d/LIT-3003.md)) was read in full ([NOTE-2237](../notes.d/NOTE-2237.md);
the reading is [THEORY-2150](../theory.d/THEORY-2150.md)). It **corroborates** the claim and
**qualifies** its floor; it is not a ground for the Kesten half.

- **Supports the lognormal half.** "if the ln Fk are independent and
  identically distributed variables with finite mean and variance, then
  asymptotically Xj will approach a lognormal distribution" (§5, p. 236).
- **Supports a floor turning it into a power law, in another form.** "As
  long as there is a bounded minimum that acts as a lower reflective
  barrier to the multiplicative model, it will yield a power law instead
  of a lognormal distribution" (§5.1, p. 238). The paper's floor is a
  **reflecting barrier**, a minimum income below which one cannot fall,
  not Kesten's additive B. The title's "additive floor" is one kind of
  floor; a reflecting minimum is another, and either stops log W from
  drifting to −∞. The section "Not mutually exclusive, made concrete"
  above should be read with both.
- **Does not state the exponent or the conditions.** Neither
  E[A^κ] = 1 nor Kesten's conditions appear; the paper defers to Kesten
  (1973) and Gabaix (1999). Its Champernowne example (F = 1/2 with
  probability 2/3, 2 with probability 1/3, a lowest class) instantiates
  the equation, though the paper does not say so: (2/3)·2^(−κ) +
  (1/3)·2^κ = 1 at κ = 1, its Pr[X ≥ x] = m/x, with E[ln F] = −0.231 < 0
  and E[F] = 1. Checked by the filer (python3 -I): two million steps of
  the chain with its floor give Pr[class ≥ k] = 0.500, 0.251, 0.063 and
  0.0079 at k = 2, 3, 5 and 8, against 2^(−(k−1)).
- **The three-way account.** §8 names two of this claim's routes, "once
  the observation time is random or a lower boundary is put into effect";
  the random observation time is the entry route (§7, Reed's double
  Pareto).

So [LIT-3003](../literature.d/LIT-3003.md) leaves this claim's `grounds` and [THEORY-2150](../theory.d/THEORY-2150.md)
`corroborates` it ([ARG-140](../arguments.d/ARG-140.md)). The Kesten half still rests on Kesten
([LIT-3005](../literature.d/LIT-3005.md)), unread, and the "What it does not say" caveat on the
conditions stands. Status unchanged.

## Note of 2026-11-22: Newman, read

Newman's review ([LIT-2976](../literature.d/LIT-2976.md), read in [NOTE-tmpa7yd2](../notes.d/NOTE-tmpa7yd2.md); the reading is [THEORY-tmp6jdas](../theory.d/THEORY-tmp6jdas.md)) **supports both halves qualitatively**. Products of random numbers
give a lognormal that can look straight on log scales over orders of
magnitude, and "random multiplication processes can also generate perfect
power-law distributions with only a slight modification: if there is a
lower bound on the value that the product of a set of numbers is allowed
to take" (§IV.G, p. 24, citing Sornette and Cont, Sornette, and Gabaix).
It gives no exponent condition (no E[A^κ] = 1). [THEORY-tmp6jdas](../theory.d/THEORY-tmp6jdas.md)
`corroborates` the claim. On the name, see [TERM-tmpg1vx2](../terms.d/TERM-tmpg1vx2.md) and the note of
this date on [CLAIM-830](CLAIM-830.md).

## Note of 2026-11-22: Clauset, Shalizi and Newman, read

Clauset, Shalizi and Newman ([LIT-2987](../literature.d/LIT-2987.md), read in [NOTE-tmphbwdu](../notes.d/NOTE-tmphbwdu.md); the reading is [THEORY-tmpw4qgu](../theory.d/THEORY-tmpw4qgu.md)) **qualifies the claim's empirical reach**. At realistic n the
lognormal and the power-law tail are "very closely equal" (p. 26) and the
lognormal is excluded for one data set of 24, so a floor has to be read
from the dynamics, not from the fitted cross-section; this is [CLAIM-803](CLAIM-803.md)'s
demand for dynamics. The US-cities row is in the note of this date on
[QUESTION-506](../questions.d/QUESTION-506.md). No edge.

## Note of 2026-11-22: Broido and Clauset, read

Broido and Clauset ([LIT-2963](../literature.d/LIT-2963.md), read in [NOTE-tmpleyjh](../notes.d/NOTE-tmpleyjh.md); the reading is [THEORY-tmphcnj3](../theory.d/THEORY-tmphcnj3.md)): **a parallel**. Lognormal-like degree tails are common, and the paper
names neither Gibrat nor multiplicative growth. No edge. Status
unchanged.

## Change of 2026-11-22

After Kesten (LIT-3005) was found Unfetched and Kevei (LIT-tmpk12vu) and
Alsmeyer and Mentemeier (LIT-tmpt282z) were read in its place:

- **`defeated_if`** now carries the theorem's conditions as Kevei states
  them (p. 1): E|B|^κ rather than E[B^κ], since B may be signed;
  non-degeneracy, P(Ax + B = x) < 1 for every x; and a two-sided tail
  with c+ + c− > 0, so "Pareto with exponent κ" can hold on one side
  only. E[log A] < 0 and P(A > 1) > 0 are dropped as separate
  conditions: "The assumption EAκ = 1 together with A ≢ 1 imply that
  E log A < 0" (p. 6), and P(A > 1) > 0 follows too, since with A ≤ 1
  a.s. and A ≢ 1, E[A^κ] < 1.
- **The title.** "Even when the process contracts on average" understated
  the case: log-contraction is required, not merely allowed. It now reads
  "a condition that requires the process to contract on average in
  logarithm". E[A] itself is at least one whenever κ ≤ 1 (by Jensen,
  E[A] ≥ E[A^κ]^(1/κ) = 1); in the checked example above κ = 1.111 and
  E[A] = e^(−0.05 + 0.045) = 0.995.
- **`grounds`** swaps LIT-3005, unread, for THEORY-tmpsmrhx, Kevei's
  restatement (ARG-tmpn6ufb). Version 2. The thesis and status are
  unchanged.

## Note of 2026-11-22: Kevei; Alsmeyer and Mentemeier, read in Kesten's place

Kevei (LIT-tmpk12vu, skimmed in NOTE-tmpv02cb; the reading is
THEORY-tmpsmrhx) and Alsmeyer and Mentemeier (LIT-tmpt282z, NOTE-tmpy4hcs,
THEORY-tmpocjqv) were read because Kesten's paper is behind a WAF
challenge.

- **Supports the Kesten half, at second hand.** Kesten "proved that if
  EAκ = 1, EAκ log+ A < ∞, log A conditioned on A ≠ 0 is nonarithmetic,
  and E|B|κ < ∞ for some κ > 0 ... then the solution of (1) has
  Pareto-like tail" (Kevei, p. 1). "Kesten proved a similar statement in
  d dimension"; the scalar case is Goldie's re-proof. Alsmeyer and
  Mentemeier give the matrix form (Theorem 1.1, p. 2), with κ fixed by
  lim n^(−1) log E‖Π_n‖^κ = 0.
- **Joins the two floors under one exponent equation.** The note of
  2026-11-21 above separates an additive floor (Kesten's B) from a
  reflecting minimum (Mitzenmacher's). The reflecting form X = AX ∨ B
  has its own theorem, Goldie's Theorem 5.2 (LIT-tmpn76uh), with the same
  conditions and the same κ: "P{X > x} ∼ cx−κ with some c ≥ 0, and c > 0
  if and only if P{B > 0} > 0" (Kevei, p. 4). So the claim's two kinds of
  floor give the same exponent; what differs is only the construction.
  The section "Not mutually exclusive, made concrete" holds for both.
- **Qualifies: a Pareto tail can come from B alone** (Grey, via Kevei,
  p. 2), now in "What it does not say". This sharpens CLAIM-803's demand
  for dynamics: the stationary tail does not name its source.
- **Leaves the lognormal half untouched.**

THEORY-tmpsmrhx is added to `grounds` and LIT-3005 removed
(ARG-tmpn6ufb). Status unchanged.
