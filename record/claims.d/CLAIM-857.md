---
number: 857
status: Proposed
formerly:
- CLAIM-tmpf9qt9
title: 'A mixture of exponentials over a rate or inverse temperature has a power-law tail exactly when the mixing distribution has power-law weight at zero rate; a lognormal mixing density gives a tail falling faster than any power and slower than any exponential, and one bounded away from zero keeps an exponential tail'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 as a gap fill (ADR-137) after Beck and Cohen
    (LIT-2962) was read: the paper gives closed forms and says the large-E
    behaviour "strongly depends on the function f(β)" without saying which
    densities give a power law, and CLAIM-795's item 4 and CLAIM-769 lean on
    that. Checked numerically by the assistant with python3 -I; the script
    is described in the body.
role: thesis
warrant: demonstrated
defeated_if: >-
  A probability distribution F of a nonnegative rate whose mixture
  B(E) = ∫e^(−βE)dF(β) is regularly varying at infinity with index −c
  while F is not regularly varying at zero with index c, or the reverse;
  or a lognormal mixing density whose B(E) decays as a power or as an
  exponential; or a mixing distribution supported on [a, ∞) with a > 0
  whose B(E) decays more slowly than e^(−aE).
tags:
- probabilistic-modeling
- mathematics
- thermodynamics
date: '2026-11-22'
line:
- formal-apparatus
grounds:
- THEORY-2176
- THEORY-2131
complements:
- CLAIM-769
bears_on:
- QUESTION-505
summary: >-
  Which spreads of rates give a power law. B(E) = ∫f(β)e^(−βE)dβ (Beck and
  Cohen's superstatistics, Sozou's discounting, a waiting time with a
  random rate) has a power-law tail exactly when the mixing distribution
  has power-law weight at β = 0: f(β) ~ Kβ^(c−1) gives B ~ KΓ(c)E^(−c).
  This is Karamata's Tauberian theorem, stated here from the assistant's
  knowledge with no source checked in this session; the elementary
  bounds for the lognormal and the bounded-away cases are the assistant's
  derivation. A lognormal density gives a tail faster than any power and
  slower than any exponential; support bounded away from zero, as in Beck's
  uniform case, keeps an exponential tail at the support's lower end. Each
  case checked by quadrature. It fills the gap left by Beck and Cohen's
  "it strongly depends on the function f(β)" (p. 7), which [CLAIM-795](CLAIM-795.md)'s
  item 4 and [CLAIM-769](CLAIM-769.md) lean on. The wording is the assistant's (Claude, in
  this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-2176 THEORY-2131 CLAIM-769 CLAIM-795 CLAIM-803 ARG-175 — Proposed or new; the readings this claim is checked against, the claims it qualifies, and the argument that says how -->

# CLAIM-857: A mixture of exponentials over a rate or inverse temperature has a power-law tail exactly when the mixing distribution has power-law weight at zero rate; a lognormal mixing density gives a tail falling faster than any power and slower than any exponential, and one bounded away from zero keeps an exponential tail

## The gap it fills

Beck and Cohen ([THEORY-2176](../theory.d/THEORY-2176.md)) give B(E) = ∫ f(β) e^(−βE) dβ in closed form
for a gamma f (a power-law tail, (1 + bE)^(−c)) and a uniform f (an
exponential tail when a > 0), and say only that "the large-E behavior is
different for all superstatistics (it strongly depends on the function
f(β))" (p. 7). [CLAIM-795](CLAIM-795.md)'s item 4 says a "mixture of exponential rates"
gives a power law, and [CLAIM-769](CLAIM-769.md) that a spread of rates gives
slower-than-exponential decay. Neither says which spreads. The same
integral is a waiting time's survival with a random rate, P(T > t) =
E[e^(−βt)], and [THEORY-2131](../theory.d/THEORY-2131.md)'s discount function.

## The claim

1. **Power-law weight at zero, and only that, gives a power-law tail.**
   With F the distribution function of β ≥ 0 and L slowly varying,
   F(β) ~ β^c L(1/β)/Γ(c + 1) as β → 0 if and only if
   B(E) ~ E^(−c) L(E) as E → ∞ (c ≥ 0). This is Karamata's Tauberian
   theorem, a known result; the statement here is the assistant's, and no
   source was checked in this session. For a density: f(β) ~ Kβ^(c−1)
   near 0 gives B(E) ~ KΓ(c)E^(−c), whatever f does away from zero (the
   Abelian direction, which needs no condition; going from B back to a
   density, not a distribution function, needs f monotone near 0). The
   exponent is the index of the weight at zero rate, so slow rates, not
   the bulk of the spread, make the tail.
2. **A lognormal f falls faster than any power and slower than any
   exponential.** Faster: for any δ, B(E) ≤ F(δ) + e^(−δE); with
   δ = E^(−1/2), F(E^(−1/2)) = Φ(−ln E/(2s)) falls faster than any power of
   E, and so does e^(−√E). Slower: for any ε > 0, B(E) ≥ F(ε)e^(−εE), with
   F(ε) > 0, so −ln B(E)/E tends to 0. (The assistant's derivation.)
3. **Support bounded away from zero keeps an exponential tail.** If
   β ≥ a > 0, B(E) ≤ e^(−aE); and if F puts weight on every [a, a + ε],
   −ln B(E)/E tends to a. Beck's uniform density on [a, a + b] is the case.
4. **Corollary: the hyperbola's exponent needs only a positive density at
   zero rate.** c = 1 is f(0) = K finite and positive, which gives
   B(E) ~ K/E. An exponential prior gives the exact 1/(1 + kt) at every t;
   a half-normal or a uniform on [0, b] gives the same tail, 1/(bE) for the
   uniform ([THEORY-2131](../theory.d/THEORY-2131.md)'s uniform case).

## The check (python3 -I, by the assistant, 2026-11-22)

Quadrature of B(E) in u = ln β on a grid of 2,000,001 points over
u ∈ [−60, 8], with log-sum-exp; local log-log slopes between decades of E.

- **Gamma**, c = 2, b = 0.5: the quadrature matches −c·ln(1 + bE) to
  1e−11 at E = 10 to 10⁶; the slope runs −1.859, −1.985, −1.998, −2.000.
- **f = 1.5β^0.5 on (0, 1]** (c = 1.5, no gamma shape away from zero):
  slope −1.5000 from E = 100 on; E^c·B/(cΓ(c)) = 0.99983 at E = 10 and
  1.00000 from E = 100.
- **f ∝ β^(−0.3)(1 + β³)^(−2)** (c = 0.7, a different bulk): slope −0.6975
  at E = 100, then −0.7000.
- **Half-normal f** (s = 1, f(0) = 0.798): E·B/f(0) = 0.990, 0.9999,
  0.999999 at E = 10, 100, 1,000.
- **Lognormal**, ln β ~ N(0, 1): the slope steepens without end, −2.64,
  −4.38, −6.29, −8.30, −10.37 per decade from E = 100 to 10⁶, and −22.2
  near 10¹²; ln(E⁶B) falls from +17.8 at E = 100 to −158.8 at 10¹²; while
  −ln B/E falls from 0.099 at E = 100 to 3.2e−10 at 10¹² and ln(e^(0.001E)B)
  turns positive (923 at E = 10⁶).
- **Uniform on [0.2, 1.2]**: −ln B/E = 0.278, 0.246, 0.226, 0.215 at
  E = 50, 100, 200, 400, tending to a = 0.2; B(50) = 9.08e−7, matching
  Beck's eq. 5.

## What it does not say

- Not that a mixture is the mechanism of any observed tail; with a gamma
  spread the exponent is a parameter of the spread, as free as the spread.
- Not that the population's heterogeneity must be large: what matters is
  the weight near zero rate, a few very slow members.
- Not that a tail falling faster than any power is distinguishable from a
  power law in finite data; the lognormal's slope steepens slowly ([CLAIM-803](CLAIM-803.md)'s
  point).

## Bearing

It qualifies [CLAIM-795](CLAIM-795.md)'s item 4, which holds for a gamma spread and any
spread with power-law weight at zero rate, not for every spread
([ARG-175](../arguments.d/ARG-175.md)). It refines [CLAIM-769](CLAIM-769.md)'s "the exact hyperbola needs a
particular spread": the asymptotic exponent one needs only a positive,
finite density at zero rate. For [QUESTION-505](../questions.d/QUESTION-505.md) it says what sets the
mixture row's exponent: the index of the spread's weight at zero rate.
