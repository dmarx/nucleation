---
number: 505
status: Open
formerly:
- QUESTION-tmp21jtb
title: 'What fixes the exponent a given mechanism for a power law produces: geometry, dimension, a balance of growth against loss, or the distribution of an underlying parameter?'
version: 1
tags:
- probabilistic-modeling
- complex-systems
date: '2026-11-21'
line:
- formal-apparatus
summary: >-
  A's, from the close of A5 of the exchange "Rich Get Richer Power Laws"
  (2026-11-20): "A particularly important next question is **whether
  there are universal principles that determine which of these mechanisms
  produces which exponent**. Some exponents are determined by geometry,
  some by dimensionality, some by the balance of growth and extinction,
  and others by the distribution of underlying parameters." A raised it
  and left it. The section "A partial pattern" is the assistant's
  (Claude, in this session), checked with python3 -I. The wording is A's
  (the other assistant in the exchange "Rich Get Richer Power Laws", A5);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-tmp6jdas THEORY-tmphcnj3 — Proposed; the readings of 2026-11-22 cited in the notes -->
<!-- inactive-ok-file: CLAIM-795 CLAIM-830 CLAIM-824 CLAIM-815 CLAIM-803 CLAIM-769 THEORY-2141 THEORY-2150 — Proposed or new; claims filed from the same exchange and held claims and readings that give exponents -->
<!-- inactive-ok-file: THEORY-tmpczldx THEORY-tmpcfn5g THEORY-tmphwf0q CLAIM-tmpf9qt9 LIT-3005 — Proposed or Unfetched; the readings of 2026-11-22, the assistant's condition on the spread, and Kesten's work, read through neighbours -->

# QUESTION-505: What fixes the exponent a given mechanism for a power law produces: geometry, dimension, a balance of growth against loss, or the distribution of an underlying parameter?

## The question

A5 lists ten mechanisms ([CLAIM-795](../claims.d/CLAIM-795.md)) and ends: "Some exponents are
determined by geometry, some by dimensionality, some by the balance of
growth and extinction, and others by the distribution of underlying
parameters. That is where the study of power laws connects to
universality classes, renormalization, stochastic-process theory, and the
deeper mathematics of complex systems." Is there a principle, or only a
list? And can the exponent tell the mechanisms apart, which
[CLAIM-803](../claims.d/CLAIM-803.md) doubts?

## A partial pattern (the assistant's)

In every mechanism the exchange works out, the survival exponent is a
ratio of two rates or two dimensions:

| mechanism | survival exponent | ratio of |
|---|---|---|
| growth with a spread of ages (Reed) | λ/g | exit or entry rate over growth rate |
| linear attachment ([CLAIM-830](../claims.d/CLAIM-830.md)) | 1/(1/2) = 2 | entry rate over growth rate, in log time |
| Kesten ([CLAIM-824](../claims.d/CLAIM-824.md)) | κ with E[A^κ] = 1; −2μ/σ² for lognormal A | drift over diffusion of log W |
| gamma mixture of rates | a | the shape of the spread of rates |
| geometry, influence r^(−β) | d/β | dimension over decay exponent |
| critical cascade, first passage ([CLAIM-815](../claims.d/CLAIM-815.md)) | 1/2 | diffusion's square root, after the cycle lemma's 1 |
| rate tree ([CLAIM-769](../claims.d/CLAIM-769.md), [THEORY-2141](../theory.d/THEORY-2141.md)) | ln b/(ln(1/g) − ln b) | log branching over log rate ratio |

Each is the exponent at which a growth term exactly offsets a loss term.
The clearest case is Kesten, where κ solves E[A^κ] = 1: κ is the moment at
which multiplicative growth just balances. The hazard form A's reasoning
noted ("a hazard proportional to 1/x produces power-law survival") is the
same thing: h(x) = α/x, and α is the ratio. Every entry in the table was
checked in this session or in the entry cited.

That is a pattern, not an answer. It says what kind of number an exponent
is in these models, not why a given system has the ratio it has, and it
does not cover the exponents of interacting critical systems (τ = 187/91
in 2D percolation), which come from a renormalization fixed point, the
criticality theme's question.

## What would answer it

A derivation showing that a broad class of mechanisms gives tail
exponents as the root of a balance equation, as Kesten's does, with the
class's boundary stated. Or a counterexample: a non-critical mechanism
whose exponent is not such a root.

## Note of 2026-11-21: Mitzenmacher, read

Mitzenmacher's review ([LIT-3003](../literature.d/LIT-3003.md), read in [NOTE-2237](../notes.d/NOTE-2237.md); the reading is
[THEORY-2150](../theory.d/THEORY-2150.md)) **bears on** the question with three exponent formulas,
each a balance, which is evidence for the partial pattern above:

- preferential attachment with a uniform share α: density exponent
  (2 − α)/(1 − α), set by the mix of uniform and proportional choice (§3);
- a lognormal stopped at an exponential time of rate λ: 1 + √(2λ), set by
  the stopping rate against the variance (§7);
- Champernowne's floor: the cumulative exponent is 1, the root of
  (2/3)·2^(−κ) + (1/3)·2^κ = 1 from the up and down probabilities, though
  the paper does not write the equation (§5.1).

None is a counterexample of the kind "What would answer it" asks for. The
second is also a root of a balance, though the paper does not put it so:
κ = √(2λ) solves κ²/2 = λ, the growth rate of E[X_t^κ] for the
zero-drift log-walk set equal to the stopping rate (the filer's
reading, from the paper's integral). [THEORY-2150](../theory.d/THEORY-2150.md) `bears_on`
this question.

## Note of 2026-11-22: Newman, read

Newman's review ([LIT-2976](../literature.d/LIT-2976.md), read in [NOTE-tmpa7yd2](../notes.d/NOTE-tmpa7yd2.md); the reading is [THEORY-tmp6jdas](../theory.d/THEORY-tmp6jdas.md)) **bears on the question** and fits its partial pattern: each exponent
is a ratio. α = 1 − a/b (two rates), α = 1 + 1/γ (a power), the general
Yule α = 2 + (k0 + c)/m (survival exponent (k0 + c + m)/m), the walk's
3/2, and for Miller's random typing a ratio of logarithms. Candidate rows
for the table: inverse powers (1/γ) and random typing. Newman adds that
the Yule process "can produce a wide range of exponents to match the
observations by suitable adjustments of the parameters" (p. 19), so a
fitted exponent alone does not pin the mechanism's parameters.
[THEORY-tmp6jdas](../theory.d/THEORY-tmp6jdas.md) `bears_on` this question.

## Note of 2026-11-22: Broido and Clauset, read

Broido and Clauset ([LIT-2963](../literature.d/LIT-2963.md), read in [NOTE-tmpleyjh](../notes.d/NOTE-tmpleyjh.md); the reading is [THEORY-tmphcnj3](../theory.d/THEORY-tmphcnj3.md)): **background data**. Across 928 network data sets the median α̂ is
"concentrated around a value of α̂ = 2", with 32% at α̂ ≥ 3, 39% in (2, 3)
and 34% below 2, against the Barabási–Albert 3. [THEORY-tmphcnj3](../theory.d/THEORY-tmphcnj3.md)
`bears_on` this question.

## Note of 2026-11-22: Beck and Cohen; Corominas-Murtra, Hanel and Thurner; Reed and Hughes, read

Three readings **bear on the question**, and each fits the partial
pattern as a root of a balance, though not always as a ratio.
[THEORY-tmpczldx](../theory.d/THEORY-tmpczldx.md), [THEORY-tmpcfn5g](../theory.d/THEORY-tmpcfn5g.md) and [THEORY-tmphwf0q](../theory.d/THEORY-tmphwf0q.md) `bear_on` it.

- **The gamma-mixture row** (Beck and Cohen, [LIT-2962](../literature.d/LIT-2962.md), [NOTE-tmpj8ro5](../notes.d/NOTE-tmpj8ro5.md)). The
  exponent is the gamma's shape c, which Beck reads as half the number of
  squared Gaussian degrees of freedom summed into the fluctuating parameter
  (eq. 12, p. 5), so the exponent counts the fluctuating environment's
  degrees of freedom. Averaging normalized densities instead of Boltzmann
  factors (type B) shifts it, c → c + ½ for E = ½u² (p. 9). The assistant's
  [CLAIM-tmpf9qt9](../claims.d/CLAIM-tmpf9qt9.md) generalizes the row: for any mixture of exponentials the
  exponent is the index of the spread's weight at zero rate (f ~ β^(c−1)
  gives c), and a spread without such weight gives no exponent at all.
- **A candidate row, noisy sample-space reduction** (Corominas-Murtra,
  Hanel and Thurner, [LIT-2997](../literature.d/LIT-2997.md), [NOTE-tmpyqqhq](../notes.d/NOTE-tmpyqqhq.md)): rank exponent λ, frequency
  survival exponent 1/λ, where λ is the share of nested steps among all
  steps. In ratio form, p(i + 1)/p(i) = (1 + λ/i)^(−1), a hazard λ/i in rank.
  **The assistant's observation**: this is the same formula as
  Mitzenmacher's preferential attachment with a uniform share α
  ([THEORY-2150](../theory.d/THEORY-2150.md)), whose density exponent (2 − α)/(1 − α) is a survival
  exponent 1/(1 − α); and the Barabási chapter's directed copying,
  γ = (2 − p)/(1 − p), is the same again. In all three the survival
  exponent is one over the share of the structured choice, the rest being
  uniform (checked: (2 − a)/(1 − a) − 1 = 1/(1 − a) at a = 0.2, 0.5, 0.9).
- **The Reed row qualified** (Reed and Hughes, [LIT-3007](../literature.d/LIT-3007.md), [NOTE-tmpbic9d](../notes.d/NOTE-tmpbic9d.md)).
  Only deterministic growth gives the bare ratio ν/μ. With noise the upper
  exponent α is the positive root of ½σ²s² + (μ − ½σ²)s − ν = 0, √(2ν)/σ at
  zero log drift. **The assistant's reading**: the left side is the growth
  rate of E[X_t^s] for geometric Brownian motion, μs + ½σ²s(s − 1), so α is
  the moment whose growth rate equals the killing rate, a root of a
  balance exactly as Kesten's E[A^κ] = 1 is (checked at μ = 0.3, σ = 0.6,
  ν = 0.4: root 1.1942, moment growth 0.4000). Their killed birth-and-death
  exponent ν/(λ − δ) and killed branching exponent ln[1/(1 − p)]/ln μ fit
  the ratio pattern; at λ = δ the power law becomes a stretched
  exponential.

Bearings relayed from the readings filed in parallel this day (their
notes hold the detail; no edge is written here):

- **Krapivsky, Redner and Leyvraz** ([LIT-2974](../literature.d/LIT-2974.md)): ν = 1 + μ/a∞ for an
  asymptotically linear kernel, but μ depends on the whole kernel, so the
  exponent is not set by the large-degree behaviour alone. Evidence that
  some exponents are roots of a global condition, not local ratios.
- **Barabási's chapter** ([LIT-2968](../literature.d/LIT-2968.md)): γ − 1 = 1/β, the survival exponent the
  reciprocal of the growth exponent of a node's degree; directed copying
  γ = (2 − p)/(1 − p), above.
- **Barabási and Albert** ([LIT-3004](../literature.d/LIT-3004.md)): γ(p) = 3 − p is stated without
  derivation; a candidate row to fit to the pattern or set aside until
  derived.
- **Kesten, read through neighbours** ([LIT-3005](../literature.d/LIT-3005.md)): κ from E[A^κ] = 1
  supports the Kesten row.
