---
status: Proposed
title: 'A replicator dynamic on the distribution of authority among an organization''s processes is the special case of the meaning–authority–legibility model in which the organization''s interpretation is the authority-weighted mixture of its processes'' and evidence reaches scoring without a maintained regime of its own; the replicator tools (Bayesian reading, potential and harmonic games, stochastic stability) then apply, and the record''s separate interpretation and legibility states earn their place exactly where interpretation departs from that mixture or legibility keeps a memory of past authority'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A case of the record's governance dynamics, lock-in, self-confirming
  authority or legibility that outlasts the authority that set it, whose
  responses to interventions on interpretation, authority and legibility a
  replicator dynamic on authority alone, with population-dependent scores,
  reproduces at matched complexity; or a case where interpretation departs
  from the authority-weighted mixture and the three-variable model predicts
  no better than the replicator.
tags:
- self-governance
- learning-theory
- complex-systems
date: '2026-10-24'
line:
- distributed-agency
rests_on:
- CLAIM-400
complements:
- CLAIM-tmp0qupq
- CLAIM-tmpd6q2w
- CLAIM-369
grounds:
- THEORY-tmp3oyxw
- CASE-tmpw4r7u
- CASE-124
- THEORY-894
- THEORY-896
summary: >-
  Filed at the owner's direction, 2026-10-24. The owner asked whether the
  tools of Soma et al. ([THEORY-tmp3oyxw](../theory.d/THEORY-tmp3oyxw.md)), "or from related work", could
  formalize the record's more abstract version of the dynamics. Their
  population–policy duality fits the record's authority dynamics with one
  identification. Read as a reduction, it says what [CASE-124](../cases.d/CASE-124.md)'s extra
  states are for.
illustrated_by:
- CASE-tmpw4r7u
---
<!-- inactive-ok-file: THEORY-tmp3oyxw CASE-tmpw4r7u CLAIM-tmp0qupq CLAIM-tmpd6q2w — Proposed or new, filed in this pull request -->
<!-- inactive-ok-file: CLAIM-369 THEORY-894 THEORY-896 CLAIM-tmpuxcp6 — cited as the tools the reduction brings in -->

# CLAIM-tmp1xoac: A replicator dynamic on the distribution of authority among an organization's processes is the special case of the meaning–authority–legibility model in which the organization's interpretation is the authority-weighted mixture of its processes' and evidence reaches scoring without a maintained regime of its own; the replicator tools (Bayesian reading, potential and harmonic games, stochastic stability) then apply, and the record's separate interpretation and legibility states earn their place exactly where interpretation departs from that mixture or legibility keeps a memory of past authority

## The claim

The owner, 2026-10-24: "can we use any of the tools here (or from related
work) to formalize our more abstract version of the dynamics?"

**The identification.** In Soma et al. the population vector is the
policy ([THEORY-tmp3oyxw](../theory.d/THEORY-tmp3oyxw.md)). Read the distribution π of practical authority
over an organization's processes as that vector. If the organization's
interpretation is the π-weighted mixture of the processes'
interpretations, then [CASE-124](../cases.d/CASE-124.md)'s meaning m is a function of authority a,
and only a, together with the scores, is state. If evidence reaches the
scores directly, with no maintained regime r, then the model reduces to a
replicator dynamic on π. In the population-dependent version, scores
depend on π.

**What the reduction brings.**
- Evidence-tracking authority is Bayesian model averaging ([CASE-tmpw4r7u](../cases.d/CASE-tmpw4r7u.md),
  part 1).
- Authority-dependent scoring is a coordination game, with an unstable
  threshold and lock-in above it (part 4). That is the self-confirming loop
  of [CASE-099](../cases.d/CASE-099.md) and [CASE-124](../cases.d/CASE-124.md) in one variable, with the correction threshold
  in closed form.
- Where the scores form a potential game, the dynamic is a gradient flow in
  the Shahshahani metric ([CLAIM-369](CLAIM-369.md)'s tool), the cardinal counterpart of a
  persistent potential. Their harmonic part, in Candogan's decomposition
  ([THEORY-894](../theory.d/THEORY-894.md)), cycles. That is [CLAIM-tmpuxcp6](CLAIM-tmpuxcp6.md)'s stable cyclic regime.
  The ordinal versions are finite improvement paths and ordinal potentials
  ([THEORY-896](../theory.d/THEORY-896.md)), as [ADR-052](../decisions.d/ADR-052.md) asks.
- In finite populations every pure state is absorbing, and
  stochastic-stability theory measures how hard each regime is to leave
  ([CASE-tmpw4r7u](../cases.d/CASE-tmpw4r7u.md), limits).

**What the reduction loses, and so what the record's states are for.**
- *Interpretation apart from authority.* When an organization's prevailing
  interpretation is not the authority-weighted mixture, m is state of its
  own. That happens when interpretations combine nonlinearly (List and
  Pettit's agendas), or when meaning persists after authority shifts.
- *Legibility with memory.* [CLAIM-400](CLAIM-400.md)'s maintained r, an exponentially
  weighted history of authority ([CASE-tmpydmf8](../cases.d/CASE-tmpydmf8.md)), is a slow state the
  stateless macro-agent cannot hold. Its signature is a lock-in that
  outlasts the authority that set it.

So the replicator model is the null model for the record's governance
dynamics. A claim that needs m or r should show a response to intervention
that the replicator on authority, with population-dependent scores, does
not reproduce at matched complexity ([CLAIM-427](CLAIM-427.md)'s standard).

## What it does not say

- That organizations are populations of imitators. The identification is
  formal: shares of control play the part of type frequencies.
- That the mixture condition holds in any actual organization.

## Note of 2026-10-24: three conditions the reduction needs

From the readings filed the same day, and the tensions the owner asked
about. The reduction to a replicator on authority holds only under three
conditions, each rejected somewhere in the record's account:
1. **Every process is scored on every step.** That is full-information
   feedback. With bandit feedback, only the governing process updated, the
   dynamic gains a factor x_i and is no longer a replicator on π
   ([THEORY-tmpar5jw](../theory.d/THEORY-tmpar5jw.md)).
2. **One standard scores every process.** A common scale is what [CLAIM-436](CLAIM-436.md)
   and [CLAIM-437](CLAIM-437.md) deny for perspectives with different concerns. Wolpert and
   Tumer's factored utilities ([THEORY-tmpomtdz](../theory.d/THEORY-tmpomtdz.md)) and monotone value mixing
   ([THEORY-tmp56jxv](../theory.d/THEORY-tmp56jxv.md)) give the ordinal, member-by-member condition under which
   no common scale is needed. That is the regime where the reduction is
   safe.
3. **Aggregation is share-weighted, not by pairwise contest.** With fixed
   scores the mean score is a potential, so the replicator cannot produce
   [CLAIM-tmpuxcp6](CLAIM-tmpuxcp6.md)'s Condorcet cycles. Cycles there need scores that depend
   on the population.

Even within the reduction, the replicator describes expected motion. Actual
runs lock on to pure states ([THEORY-tmphhvqf](../theory.d/THEORY-tmphhvqf.md)). Access and authority, which
[CLAIM-349](CLAIM-349.md) keeps apart, are one share here, and a share of zero never
returns without exploration ([THEORY-tmp3wkwk](../theory.d/THEORY-tmp3wkwk.md)).
