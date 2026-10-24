---
status: Active
title: 'Authority as a replicator population: for a distribution π of control over processes with mean qualities q, the expected Maynard-Cross update is π_a q_a / v, Bayes'' rule when q is each process''s likelihood; the Maynard dynamic is the Taylor dynamic slowed by 1/v, so the two share their orbits; mean quality climbs at the rate Var_π(q); and when a process''s score rises with its own share, ℓ′ = ℓ + h + c(2π − 1) has an unstable threshold π* = (1 − h/c)/2, above which a process the evidence disfavours captures the organization'
version: 1
standing: stipulated
kind: construction
tags:
- learning-theory
- self-governance
- game-theory
date: '2026-10-24'
line: distributed-agency
illustrates:
- CLAIM-tmp1xoac
- CLAIM-tmp0qupq
variant_of:
- CASE-099
summary: >-
  Filed at the owner's direction, 2026-10-24, after asking whether the tools
  of Soma et al. ([THEORY-tmp3oyxw](../theory.d/THEORY-tmp3oyxw.md)) or related work could formalize the
  record's abstract governance dynamics. Four results, each checked when
  filed, two by script. It reads authority as the population vector of a
  replicator dynamic. Evidence-tracking authority is then Bayesian, and
  authority-dependent scoring gives lock-in with an explicit correction
  threshold.
supports:
- CLAIM-tmp1xoac
variants:
- CASE-tmpffs67
---
<!-- inactive-ok-file: THEORY-tmp3oyxw CLAIM-tmp1xoac CLAIM-tmp0qupq CLAIM-tmp8z857 CASE-tmpydmf8 — Proposed, filed in this pull request -->

# CASE-tmpw4r7u: Authority as a replicator population: for a distribution π of control over processes with mean qualities q, the expected Maynard-Cross update is π_a q_a / v, Bayes' rule when q is each process's likelihood; the Maynard dynamic is the Taylor dynamic slowed by 1/v, so the two share their orbits; mean quality climbs at the rate Var_π(q); and when a process's score rises with its own share, ℓ′ = ℓ + h + c(2π − 1) has an unstable threshold π* = (1 − h/c)/2, above which a process the evidence disfavours captures the organization

## The case

An organization's processes a = 1, …, n hold shares π_a of practical
authority, a point on the simplex. Authority passes between them by a
revision protocol of the kind [THEORY-tmp3oyxw](../theory.d/THEORY-tmp3oyxw.md) treats: in the weighted-voter
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
[CASE-tmpydmf8](CASE-tmpydmf8.md) filter in its simplest form, a scoring channel that admits
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
protective lock-in ([CLAIM-tmp8z857](../claims.d/CLAIM-tmp8z857.md)) needs no bias in any process, only
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
  vector ([CLAIM-tmp1xoac](../claims.d/CLAIM-tmp1xoac.md)).
- That any organization's scoring has this form.

## Note of 2026-10-24: what the learning-in-games readings change

Read the same day (curation entry of 2026-10-24, 2nd).
- **Expectation, not runs.** Börgers and Sarin ([THEORY-tmphhvqf](../theory.d/THEORY-tmphhvqf.md),
  [THEORY-tmpbq2nj](../theory.d/THEORY-tmpbq2nj.md)) show that Cross learning follows the replicator dynamic
  in expectation, and in actual runs only over finite horizons as learning
  slows. At every learning speed, a learner ends on one pure profile with
  probability one, matching pennies included. So part 4's lock-in has a
  cousin that needs no self-scoring c at all: reinforcement of whatever
  was chosen, with no way back.
- **Bandit feedback breaks the reduction.** Where only the governing
  process's score is updated, as in plain Q-learning, the expected change
  carries an extra factor x_i ([THEORY-tmpar5jw](../theory.d/THEORY-tmpar5jw.md)). The dynamic is then not a
  replicator on π. Part 1's Bayes reading assumes every process is scored
  on every step, BoostTheVote's full-information case.
- **Forgetting is exploration.** In Sato and Crutchfield's softmax
  learners with decaying memory ([THEORY-tmp3wkwk](../theory.d/THEORY-tmp3wkwk.md), [THEORY-tmpev90a](../theory.d/THEORY-tmpev90a.md)), the
  forgetting rate becomes an entropy term pulling toward equal shares. The
  rest points are then logit equilibria, and the edges stop being
  absorbing. That is the principled form of the mutation this case left as
  a next step.
- **α-Rank cannot express part 4.** Its fitness does not depend on a
  strategy's share ([NOTE-tmpxufhw](../notes.d/NOTE-tmpxufhw.md)).
