---
status: Active
title: 'A population of perspectives, each advocating one of two interpretations, makes its collective choice by drift diffusion when the coordinate the decision is read from integrates independent evidence with no net leak or self-reinforcement and commitment is a bound on that coordinate; two interpretations make the reduction one-dimensional, but they do not by themselves give it'
version: 2
history:
- version: 1
  date: '2026-10-25'
  note: >-
    Filed from U34–A44 of the exchange, with both constructions checked.
- version: 2
  date: '2026-10-25'
  note: >-
    After the readings of Wald 1945 and DeGroot 1974 from copies the owner
    supplied: the SPRT link is now read in the primary source (the walk is
    Wald's Z_m, the prior-odds start his §3.1, and the drift-diffusion
    limit the case where his approximations are exact, not his theorem),
    and the connectivity condition is DeGroot's single closed class
    (THEORY-tmpvqkp6). THEORY-tmpeglfj, THEORY-tmpda363 and THEORY-tmpvqkp6
    added to grounds. The claim is unchanged.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in either construction it rests on: a population meeting the
  stated conditions (independent evidence across steps, a readout weighted
  by the influence mode, a single closed class of influence, a linear balance
  of leak against reinforcement in that mode) whose readout shows serial
  dependence or a drift that depends on its own state. Or a population
  that violates them, with feedback from a visible majority or
  self-scoring, whose readout nonetheless shows constant drift and
  diffusion over its whole range.
tags:
- complex-systems
- probabilistic-modeling
- network-science
date: '2026-10-25'
line:
- distributed-agency
- will-organization
corroborates:
- CLAIM-262
grounds:
- CASE-tmpvmjgd
- CASE-155
- THEORY-068
- THEORY-321
- THEORY-tmpeglfj
- THEORY-tmpda363
- THEORY-tmpvqkp6
summary: >-
  The owner's hypothesis at U34 of the exchange of 2026-10-24, continued:
  "if we've set up our simulation appropriately, when n=2 we should see
  drift diffusion dynamics". It is the owner's second statement of
  [CLAIM-262](CLAIM-262.md)'s continuous case, first given on 2026-10-12. A34 qualified
  it, A35 gave the dial, and A36 gave an exact reduction for a network of
  accumulators. The record's own replicator construction gives a second,
  which the exchange did not see. Both were checked when filed. The sharp
  edge: two interpretations are necessary for a one-dimensional reduction,
  not sufficient.
---
<!-- inactive-ok-file: CLAIM-262 — Proposed; the owner's earlier statement this one corroborates in a construction, nothing here rests on it -->

# CLAIM-tmpfd9lk: A population of perspectives, each advocating one of two interpretations, makes its collective choice by drift diffusion when the coordinate the decision is read from integrates independent evidence with no net leak or self-reinforcement and commitment is a bound on that coordinate; two interpretations make the reduction one-dimensional, but they do not by themselves give it

## The claim

The owner, at U34: "let's also model the perspectives as a distribution
over policies. let's say that there are n overarching possible
interpretations, and each perspective advocates for one of these. part of
my hypothesis here is that if we've set up our simulation appropriately,
when n=2 we should see drift diffusion dynamics." On 2026-10-12 the owner
had called Twitch Plays Pokémon an approximation of "the
agent-as-population-subject-to-drift-diffusion-decision-dynamics case"
([CLAIM-262](CLAIM-262.md), [CASE-074](../cases.d/CASE-074.md)).

A34: "**An important qualification:** n=2 alone doesn't imply
drift–diffusion. We get it because of assumptions about the evidence
process, aggregation and access." A35 gave the dial,
dL = [μ + (β − λ)L]dt + σ dW. A36: "a much more discriminating hypothesis
than 'two interpretations imply drift–diffusion.'"

**Two constructions in which it holds exactly.**

- **Interacting accumulators** ([CASE-tmpvmjgd](../cases.d/CASE-tmpvmjgd.md)). Perspectives hold
  continuous supports coupled linearly through a row-stochastic influence
  matrix. The influence-weighted support is an Ornstein–Uhlenbeck process
  with rate κ − λ, and it is pure drift diffusion when coupling balances
  leak. That is [THEORY-068](../theory.d/THEORY-068.md)'s balance of leak and inhibition, for M units on
  a network. Its noise is set by the concentration of influence
  ([THEORY-321](../theory.d/THEORY-321.md)).
- **A replicator population** ([CASE-155](../cases.d/CASE-155.md), part 4 and its note of
  2026-10-25). Two advocate processes hold shares of authority, scored at
  each step by the likelihood each gave a fresh observation. The log odds
  ℓ of their shares then move by that observation's log likelihood ratio.
  Part 4's ℓ′ = ℓ + h + c(2π − 1), with 2π − 1 = tanh(ℓ/2), is at c = 0
  exactly Wald's sequential probability ratio walk: his Z_m, the sum of
  the log likelihood ratios ([THEORY-tmpeglfj](../theory.d/THEORY-tmpeglfj.md)), started from the prior log
  odds as in his own derivation of the test (§3.1). The SPRT proper is
  this walk with fixed bounds on it. Its continuum limit is
  [THEORY-068](../theory.d/THEORY-068.md)'s drift-diffusion model. That limit is not Wald's statement:
  it is the case in which his overshoot-free OC, ASN and first-passage
  density are exact ([THEORY-tmpda363](../theory.d/THEORY-tmpda363.md)). Its drift is half its variance,
  which for Gaussian evidence is Wald's h = −1 under the alternative, and
  A35's "calibrated sequential inference". Self-scoring, c > 0, is the
  reinforcement that breaks it: the linear part of c·tanh(ℓ/2) is (c/2)ℓ,
  A35's β.

**The conditions.**

- Evidence independent across steps.
- A readout weighted by the influence mode: ℓ in [CASE-tmpvmjgd](../cases.d/CASE-tmpvmjgd.md), the shares
  in [CASE-155](../cases.d/CASE-155.md). A uniform average carries a stationary transverse
  term.
- No net leak or self-reinforcement in that mode.
- A single closed class of the influence network. Members outside it
  get no weight (DeGroot's Theorems 2 and 3, [THEORY-tmpvqkp6](../theory.d/THEORY-tmpvqkp6.md)). Several
  closed groups give several balanced modes.
- Continuous support. Members that broadcast only binary positions break
  the linear closure.
- Commitment as a bound on the readout, not on one member or on a
  majority count.
- For a finite population, a second, state-dependent noise of order
  1/(Nπ(1 − π)) in the log odds from resampling: the voter or
  Wright–Fisher term that A34 and A36 named as the rival model.

Checked when filed, by script: the reduction of [CASE-tmpvmjgd](../cases.d/CASE-tmpvmjgd.md) (as recorded
there); and for the replicator, with Gaussian evidence N(±0.3, 1), the
log-odds increment equals the log likelihood ratio exactly, with mean
0.178 and variance 0.360 against 2δ²/σ² = 0.18 and 4δ²/σ² = 0.36;
2π − 1 = tanh(ℓ/2); and the logit of a binomial share has variance
1/(Nπ(1 − π)) at N = 100 and 1,000.

## What it does not say

- That any real collective meets the conditions. That is [CLAIM-262](CLAIM-262.md)'s
  empirical question and [CASE-074](../cases.d/CASE-074.md)'s.
- That the drift-diffusion model is right for [CASE-074](../cases.d/CASE-074.md)'s visible tally,
  where the claim predicts the opposite: positive feedback, faster and
  less accurate decisions.
- That a perspective is a drift-diffusion decider. In [CASE-tmpvmjgd](../cases.d/CASE-tmpvmjgd.md) no
  member is.
- That the result is emergent. A35, of its own app: "we obtain the result
  because Gaussian additive evidence is built into the update rule". The
  constructions show what the conditions are, not that a richer model
  meets them. A42: "We have not yet demonstrated that drift–diffusion
  emerges from the complete nonlinear learning-and-governance system."
