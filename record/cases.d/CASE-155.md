---
number: 155
status: Active
formerly:
- CASE-tmpw4r7u
title: 'Authority as a replicator population: for a distribution π of control over processes with mean qualities q, the expected Maynard-Cross update is π_a q_a / v, Bayes'' rule when q is each process''s likelihood; the Maynard dynamic is the Taylor dynamic slowed by 1/v, so the two share their orbits; mean quality climbs at the rate Var_π(q); and when a process''s score rises with its own share, ℓ′ = ℓ + h + c(2π − 1) has an unstable threshold π* = (1 − h/c)/2, above which a process the evidence disfavours captures the organization'
version: 3
history:
- version: 2
  date: '2026-10-25'
  note: >-
    A dated note added: with c = 0 part 4 is the SPRT walk and its limit the
    drift-diffusion model (CLAIM-453); A47's conformity arm is the
    self-scoring c (CASE-158). The case is unchanged.
- version: 3
  date: '2026-10-25'
  note: >-
    The note of 2026-10-25 sharpened after the reading of Wald 1945 from a
    copy the owner supplied: the walk is Wald's Z_m (THEORY-952),
    started from the prior log odds as in his §3.1, and the SPRT proper adds
    fixed bounds; the drift-diffusion limit is not stated by Wald, though
    his overshoot-free formulas are exactly the diffusion's
    (THEORY-951). The case is unchanged.
standing: stipulated
kind: construction
tags:
- learning-theory
- self-governance
- game-theory
date: '2026-10-24'
line: distributed-agency
illustrates:
- CLAIM-444
- CLAIM-443
variant_of:
- CASE-099
summary: >-
  Filed at the owner's direction, 2026-10-24, after asking whether the tools
  of Soma et al. ([THEORY-899](../theory.d/THEORY-899.md)) or related work could formalize the
  record's abstract governance dynamics. Four results, each checked when
  filed, two by script. It reads authority as the population vector of a
  replicator dynamic. Evidence-tracking authority is then Bayesian, and
  authority-dependent scoring gives lock-in with an explicit correction
  threshold.
supports:
- CLAIM-444
- CLAIM-453
variants:
- CASE-157
- CASE-tmpr1vuv
---
<!-- inactive-ok-file: THEORY-899 CLAIM-444 CLAIM-443 CLAIM-446 CASE-156 — Proposed, filed in this pull request -->
<!-- inactive-ok-file: THEORY-928 — Proposed; cited in the note of 2026-10-25, nothing here rests on their being settled -->

# CASE-155: Authority as a replicator population: for a distribution π of control over processes with mean qualities q, the expected Maynard-Cross update is π_a q_a / v, Bayes' rule when q is each process's likelihood; the Maynard dynamic is the Taylor dynamic slowed by 1/v, so the two share their orbits; mean quality climbs at the rate Var_π(q); and when a process's score rises with its own share, ℓ′ = ℓ + h + c(2π − 1) has an unstable threshold π* = (1 − h/c)/2, above which a process the evidence disfavours captures the organization

## The case

An organization's processes a = 1, …, n hold shares π_a of practical
authority, a point on the simplex. Authority passes between them by a
revision protocol of the kind [THEORY-899](../theory.d/THEORY-899.md) treats: in the weighted-voter
form, each unit of control goes to a process with probability proportional
to the score it has just earned. With q_a the expected score and
v = Σ π_b q_b, the mean dynamic is the population's.

**1. Evidence-tracking authority is Bayesian.** The expected Maynard-Cross
update is

    π_a + π_a(q_a − v)/v = π_a q_a / v.

If q_a is the likelihood process a assigns to the evidence just observed,
this is Bayes' rule over the processes as hypotheses. Authority allocated
by success-weighted recruitment is then, in expectation, Bayesian model
averaging. This was checked numerically when filed. It is the replicator
dynamic read as inference, which Harper and Shalizi have made before for
other purposes.

**2. Speed, not direction.** In a single population the Maynard dynamic is
the Taylor dynamic divided by v > 0, a scalar, so the two trace the same
orbits at different speeds. Which protocol the organization uses changes
how fast authority settles, not where. The equivalence fails for coupled
populations, each with its own v.

**3. Climb rate is variance.** For fixed q, along the Taylor dynamic
dv/dt = Σ q_a π_a(q_a − v) = Var_π(q) ≥ 0, which is Fisher's fundamental
theorem. Mean quality improves only as fast as the processes differ, and
not at all where they agree. This is cardinal: q must be a score whose
differences mean something ([ADR-052](../decisions.d/ADR-052.md)).

**4. Authority-dependent scoring gives lock-in.** Two processes, A and B.
Let ℓ be the log-odds of A's share π, h the log likelihood ratio per step
of evidence scored independently (h < 0 favours B), and c > 0 the part of
A's score advantage that grows with A's own share. That is the
[CASE-156](CASE-156.md) filter in its simplest form, a scoring channel that admits
more of what favours the process already in charge. Then

    ℓ′ = ℓ + h + c(2π − 1).

The increment rises with π, so the one interior rest point,
π* = (1 − h/c)/2, which lies in (0, 1) when |h| < c, is unstable. Below
π*, B wins as the evidence says. Above it, A's share goes to one against
the evidence. With h = −0.2 and c = 1, π* = 0.6: runs from 0.55 and 0.59
went to B, and runs from 0.61 and 0.65 to A, checked by script when filed.
The threshold is a correction threshold. An intervention that leaves h and
c alone works only if it pushes A's share below π*. Raising |h|, more
diagnostic evidence, or lowering c, independent scoring, moves the
threshold, and |h| ≥ c removes the lock-in altogether.

## What it can show

That the record's evidence-tracking authority has an exact form (1); that
protective lock-in ([CLAIM-446](../claims.d/CLAIM-446.md)) needs no bias in any process, only
scoring that depends on who governs (4); and where a correction has to
reach.

## What it cannot show

- Anything about finite populations. There every pure state is absorbing,
  which is the absorbing lower state of [TERM-078](../terms.d/TERM-078.md)'s revision, and leaving
  needs mutation or exploration. Stochastic-stability results (Young; and
  Kandori, Mailath and Rob), named here and not registered, would give the
  escape time from each regime, of order exp(N × barrier). That is the
  next step, not derived here.
- A separate meaning or legibility state. Here belief and authority are one
  vector ([CLAIM-444](../claims.d/CLAIM-444.md)).
- That any organization's scoring has this form.

## Note of 2026-10-24: what the learning-in-games readings change

Read the same day (curation entry of 2026-10-24, 2nd).
- **Expectation, not runs.** Börgers and Sarin ([THEORY-938](../theory.d/THEORY-938.md),
  [THEORY-934](../theory.d/THEORY-934.md)) show that Cross learning follows the replicator dynamic
  in expectation, and in actual runs only over finite horizons as learning
  slows. At every learning speed, a learner ends on one pure profile with
  probability one, matching pennies included. So part 4's lock-in has a
  cousin that needs no self-scoring c at all: reinforcement of whatever
  was chosen, with no way back.
- **Bandit feedback breaks the reduction.** Where only the governing
  process's score is updated, as in plain Q-learning, the expected change
  carries an extra factor x_i ([THEORY-932](../theory.d/THEORY-932.md)). The dynamic is then not a
  replicator on π. Part 1's Bayes reading assumes every process is scored
  on every step, BoostTheVote's full-information case.
- **Forgetting is exploration.** In Sato and Crutchfield's softmax
  learners with decaying memory ([THEORY-928](../theory.d/THEORY-928.md), [THEORY-936](../theory.d/THEORY-936.md)), the
  forgetting rate becomes an entropy term pulling toward equal shares. The
  rest points are then logit equilibria, and the edges stop being
  absorbing. That is the principled form of the mutation this case left as
  a next step.
- **α-Rank cannot express part 4.** Its fitness does not depend on a
  strategy's share ([NOTE-1156](../notes.d/NOTE-1156.md)).

## Note of 2026-10-25: two processes as a drift-diffusion decider, and the conformity arm

- **The SPRT walk.** For two processes, part 1's Bayes form gives
  ℓ′ = ℓ + log(q_A/q_B) for the log odds of A's share. With q the
  likelihood each process gives a fresh observation, the increment is that
  observation's log likelihood ratio h. That is Wald's sequential
  probability ratio walk (Wald's Z_m, [THEORY-952](../theory.d/THEORY-952.md); starting from the
  prior log odds, it is his §3.1 posterior form; the SPRT proper adds
  fixed bounds), and its continuum limit is [THEORY-068](../theory.d/THEORY-068.md)'s
  drift-diffusion model (not stated by Wald; his overshoot-free formulas
  are exactly the diffusion's, [THEORY-951](../theory.d/THEORY-951.md)). For Gaussian evidence N(±δ, σ²), h has mean
  2δ²/σ² and variance 4δ²/σ², so the drift is half the variance. Part 4's
  ℓ′ = ℓ + h + c(2π − 1) is the same walk with feedback from the share.
  Since 2π − 1 = tanh(ℓ/2), it is ℓ′ = ℓ + h + c·tanh(ℓ/2), whose linear
  part (c/2)ℓ is the self-reinforcement of A35's dial
  dL = [μ + (β − λ)L]dt + σ dW. With forgetting that shrinks ℓ by (1 − α)
  per step (a form suggested by the Sato–Crutchfield note above, assumed
  here and not derived from [THEORY-928](../theory.d/THEORY-928.md)), the symmetric state loses
  stability at c = 2α. In a finite population of N, resampling adds noise
  of order 1/(Nπ(1 − π)) to the log odds, the voter-model term. Checked
  when filed, with δ = 0.3 and σ = 1: increment mean 0.178 and variance
  0.360 against 0.18 and 0.36; the logit variance of a binomial share
  matches 1/(Nπ(1 − π)) at N = 100 and 1,000; and the forgetting threshold
  at α = 0.1 between c = 0.15 and c = 0.25. This answers the owner's U34
  hypothesis of the exchange of 2026-10-24, continued, inside the record's
  own model ([CLAIM-453](../claims.d/CLAIM-453.md)). The exchange did not see it, though U28 had
  asked for this material.
- **The conformity arm.** A47's conformity scoring, which rewards agreement
  with the prevailing collective proposal, is part 4's self-scoring c, and
  it held the old allocation after a reversal of expertise, as part 4
  predicts ([CASE-158](CASE-158.md); reported, not reproduced).

The case is unchanged.
