---
number: 806
status: Proposed
formerly:
- CLAIM-tmp9a83b
title: 'Linear preferential attachment is itself balanced at a boundary, between the stretched-exponential tails of weaker attachment and the condensation of stronger, so rich-get-richer processes and criticality are not opposite routes to a power law: both reach one at a marginal point, and differ in what is balanced'
version: 2
history:
- version: 2
  date: '2026-11-22'
  note: >-
    Revised in place after the readings of 2026-11-22 of Krapivsky, Redner
    and Leyvraz (NOTE-tmp2z733) and Barabási's chapter (NOTE-tmpnpqc8).
    The ground moves from the unread LIT-2974 to the reading
    THEORY-tmpmsncg (ARG-tmpqxprw). The boundary exponent k^(−3) is
    restricted to A_k = k; the aside on shifted kernels, "not checked
    here", is checked (ν = 1 + μ/a∞); the superlinear side is a cascade of
    transitions; the chapter's measured attachment exponents are added as
    the empirical side. Title and status unchanged.
role: thesis
warrant: demonstrated
defeated_if: >-
  A growing-network or Yule-type model giving a power-law tail over an
  open range of attachment exponents α around 1, without a compensating
  ingredient tuned with it, so that linear attachment is not marginal; or
  an argument that the balance in criticality (offspring mean against
  extinction) and the balance in attachment (the kernel's exponent
  against linear) are not the same kind of thing, so that "both marginal"
  is a pun.
tags:
- complex-systems
- network-science
- probabilistic-modeling
date: '2026-11-21'
line:
- formal-apparatus
objects_to:
- CLAIM-796
rests_on:
- CLAIM-817
- CLAIM-830
grounds:
- THEORY-tmpmsncg
- CASE-303
summary: >-
  An objection to A's A8 §8 contrast ([CLAIM-796](CLAIM-796.md)), filling a gap the
  ledger of the exchange "Rich Get Richer Power Laws" names. A's own A1 §4
  table shows a power law only at α = 1, with a stretched exponential
  below and condensation above; the assistant's runs ([CLAIM-817](CLAIM-817.md))
  confirm both sides. So linear attachment is a marginal point, as
  R = 1 is for a cascade. What differs is what is balanced: a kernel's
  exponent against linearity, or reproduction against extinction. And in
  the attachment model the exponent is a ratio of two rates
  ([CLAIM-830](CLAIM-830.md)), which a balance sets. The wording is the assistant's
  (Claude, in this session); adopting it is the owner's call.
bears_on:
- QUESTION-505
---
<!-- inactive-ok-file: THEORY-tmpw4qgu THEORY-tmphcnj3 — Proposed; the readings of 2026-11-22 cited in the notes -->
<!-- inactive-ok-file: CLAIM-796 CLAIM-817 CLAIM-830 CASE-303 — Proposed or new; the claim objected to and the claims and case this rests on, filed from the same exchange -->
<!-- inactive-ok-file: THEORY-tmpmsncg THEORY-tmpzmy66 ARG-tmpqxprw — Proposed; the readings of 2026-11-22 and the argument that says how they bear -->
<!-- inactive-ok-file: LIT-3007 — Deferred when cited; Reed and Hughes, read in this round by another filer -->

# CLAIM-806: Linear preferential attachment is itself balanced at a boundary, between the stretched-exponential tails of weaker attachment and the condensation of stronger, so rich-get-richer processes and criticality are not opposite routes to a power law: both reach one at a marginal point, and differ in what is balanced

## The objection

A8 §8 ([CLAIM-796](CLAIM-796.md)) sets "advantage feeds on advantage" against
"dynamics … balanced at a boundary between qualitatively different
regimes". But A's own table at A1 §4 puts rich-get-richer at such a
boundary. With attachment ∝ k^α, α < 1 gives a stretched-exponential
tail, α > 1 condensation onto one unit, and only α = 1 a power law
(Krapivsky, Redner and Leyvraz, LIT-2974, read on 2026-11-22 in
NOTE-tmp2z733, who call γ = 1 "the borderline case"). The assistant's
simulations ([CLAIM-817](CLAIM-817.md)) show both sides. At α = 0.5 the largest of
100,000 nodes has degree 42. At α = 1.5 one node holds 99,354 links and the
next 12. A power law appears only at the boundary, just as a cascade's
law s^(−3/2) appears only at R = 1 ([CASE-303](../cases.d/CASE-303.md)).

So the two are not opposites in the respect A names. Both are tuned to a
marginal point between a regime with a characteristic scale and a regime
with a macroscopic winner. That is a giant cluster, or a condensate. The
parallel runs further:

| | below the boundary | at it | above it |
|---|---|---|---|
| cascade, mean offspring R | cutoff s_c ≈ 2/(1 − R)^2 | s^(−3/2) | positive chance of no end |
| attachment, kernel k^α | stretched exponential | k^(−3) for A_k = k; k^(−ν), ν > 2, for A_k → a∞k | one node takes almost all, with a cascade of transitions at α = (m+1)/m |

## The empirical side (added 2026-11-22)

Barabási's chapter reports attachment exponents measured from network
snapshots: "For the Internet and citation networks we have α ≈ 1", and
"For the co-authorship and the actor network the best fit provides
α=0.9±0.1" (NOTE-tmpnpqc8, §5.7). By that measure real systems sit at or
just below the boundary. The measurement conditions on degree alone, so
fitness and age are confounded (CLAIM-803), and below the boundary
Krapivsky, Redner and Leyvraz warn that for 0.8 ≲ γ ≲ 1 a stretched
exponential and a power law are hard to tell apart up to k = 1000: the
boundary is sharp in the model and blurred in data.

## What does differ

What is balanced. In the cascade, reproduction balances extinction. In
attachment, the kernel's growth with k is exactly proportional. That
proportionality makes each unit's growth exponential in logarithmic
time, and entry turns that into a Pareto tail. The exponent, 2 for the
survival function, is then the ratio of the entry rate to the growth
rate ([CLAIM-830](CLAIM-830.md)). So in both, a power law comes from a balance of
two rates. The difference A points to, a privileged unit against an
unprivileged event, is real. It is a difference in *what* becomes
extreme, which A3 §3 already draws (entities against events), and not a
difference in how the scale is removed.

## What it does not say

- Not that the power law in attachment is fragile in every respect. A
  shifted linear kernel k + a keeps a power law and moves its exponent,
  so the boundary is a line in a larger space of kernels, not a point.
  The claim is that the exponent of k must be one. (Checked 2026-11-22:
  Krapivsky, Redner and Leyvraz give, for any asymptotically linear
  kernel A_k → a∞k, "ν = 1 + µ/a∞", and for A_1 = 1, A_k = a∞k,
  ν = (3 + √(1 + 8/a∞))/2, tunable "to any value larger than 2"; a∞ = 1
  gives 3, recomputed with python3 -I.)
- Not that the two mechanisms share a universality class or exponent.
- Not an answer to what fixes the exponents ([QUESTION-505](../questions.d/QUESTION-505.md)), though it
  bears on it.

## Note of 2026-11-22: Clauset, Shalizi and Newman, read

Clauset, Shalizi and Newman ([LIT-2987](../literature.d/LIT-2987.md), read in [NOTE-tmphbwdu](../notes.d/NOTE-tmphbwdu.md); the reading is [THEORY-tmpw4qgu](../theory.d/THEORY-tmpw4qgu.md)) **qualifies the claim's empirical use**. The stretched exponential is
plausible beside the power law for nine of their data sets, and they
note "the indistinguishability of power laws and stretched exponentials"
(p. 26). The sublinear-against-linear distinction the claim draws is a
model distinction that a finite cross-section often cannot make. No edge.

## Note of 2026-11-22: Broido and Clauset, read

Broido and Clauset ([LIT-2963](../literature.d/LIT-2963.md), read in [NOTE-tmpleyjh](../notes.d/NOTE-tmpleyjh.md); the reading is [THEORY-tmphcnj3](../theory.d/THEORY-tmphcnj3.md)): **background**. The Weibull (stretched exponential) is favoured over
the power law for 47% of network data sets (Table 1), though the paper
does not tie this to sublinear attachment. No edge. Status unchanged.

## Note of 2026-11-22: Krapivsky, Redner and Leyvraz, read

Krapivsky, Redner and Leyvraz (LIT-2974, NOTE-tmp2z733; the reading is
THEORY-tmpmsncg) **support the marginality** and qualify the table, as
corrected in place above. γ = 1 is "the borderline case", γ > 1 "akin to
gelation", and no γ ≠ 1 tail is a power law, so the `defeated_if` is not
met. THEORY-tmpmsncg replaces LIT-2974 in the grounds (ARG-tmpqxprw).

## Note of 2026-11-22: Barabási and Albert, and Barabási's chapter, read

**Support** (LIT-3004, NOTE-tmpwgw8e; LIT-2968, NOTE-tmpnpqc8). Barabási
and Albert: "scaling is present only for α = 1" (preprint p. 7). The
chapter gives the regimes on both sides and "Π(k) needs to depend strictly
linearly on the degrees for the resulting network to have a pure power
law" (§5.8), and the measured exponents above. Neither draws the analogy
to criticality. THEORY-tmpzmy66 corroborates the claim.

## Note of 2026-11-22: Reed and Hughes, read

Reed and Hughes (LIT-3007), as read in this round by another filer:
**a contrast**. Their killed birth-and-death process changes form at
λ = δ: a power law above, a stretched exponential at the balance point,
and a geometric factor times a power below. There, balance kills the power
law rather than producing it. So "a power law at a marginal point" is not
a general rule of balanced rates; it holds for the cascade and for the
attachment kernel, and fails for this one. No edge.

