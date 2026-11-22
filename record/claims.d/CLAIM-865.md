---
number: 865
status: Proposed
formerly:
- CLAIM-tmp5hyz1
title: 'Where a support acts on an assembly only by changing its transition rates and is withdrawn for good, the drop in the chance of completing when it is withdrawn at a state equals the expected total, along the course the supported assembly would take from that state, of how much the support changes each rate times how much the unsupported chance of completing turns on that step; for a support that holds a nucleus this is the nucleus''s fragility times its worth, so the assembly becomes independent of the support before it is complete only where what it has built holds the nucleus or no longer needs it'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-095, from the
    model of CASE-308.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the identity: a finite continuous-time Markov chain with
  absorbing target and failure sets, a supported generator Q_S under which
  absorption is certain and an unsupported Q_0, in which q_S(s) − q_0(s)
  differs from the expected integral, along the Q_S path from s up to
  absorption, of ((Q_S − Q_0) q_0)(X_t); or, in CASE-308's model, a
  state (1, n) where that integrand is not d₀θⁿ times
  q_0(1, n) − q_0(0, n). Not defeated by supports that leave something
  behind outside the state, by withdrawals that end, or by non-Markov
  assembly, none of which the claim covers; nor by systems in which D does
  not fall, which the claim allows.
tags:
- complex-systems
- mathematics
- probabilistic-modeling
date: '2026-11-22'
line:
- transient-support
grounds:
- CASE-308
uses:
- TERM-117
complements:
- CLAIM-600
- CLAIM-602
- CLAIM-604
bears_on:
- QUESTION-398
summary: >-
  The assistant's, from carrying out [LEAD-095](../leads.d/LEAD-095.md). A's measure for
  [QUESTION-398](../questions.d/QUESTION-398.md) is D(s) = q_supported(s) − q_withdrawn(s). On the
  transient states, Q_S(q_S − q_0) = −(Q_S − Q_0)q_0, so D(s) is the
  expected integral, along the supported path from s, of the support's
  rate changes weighted by the unsupported committor's differences across
  them. That is a standard perturbation identity for absorption
  probabilities; its use here is the record's. Three things follow.
  The chance after withdrawal depends on the state reached alone, so all
  the support leaves behind is the state. For a scaffold that holds a
  nucleus the integrand is the nucleus's dissolution rate times
  Δ_N⁰ = q_0(with nucleus) − q_0(without), so D becomes small before
  completion only where the units built hold the nucleus or the nucleus
  has stopped mattering. And where neither happens, the support is needed
  until completion however far assembly has gone. In [CASE-308](../cases.d/CASE-308.md)'s
  model D falls below 0.05 a quarter of the way through when bound units
  stabilize the nucleus, and stays at 0.10 or more to the last unit when
  they do not. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-308 — new; the executed study this claim is grounded in, filed with it -->

# CLAIM-865: Where a support acts on an assembly only by changing its transition rates and is withdrawn for good, the drop in the chance of completing when it is withdrawn at a state equals the expected total, along the course the supported assembly would take from that state, of how much the support changes each rate times how much the unsupported chance of completing turns on that step; for a support that holds a nucleus this is the nucleus's fragility times its worth, so the assembly becomes independent of the support before it is complete only where what it has built holds the nucleus or no longer needs it

## The identity

Take a finite continuous-time Markov chain with an absorbing target F and
failure K. Support gives generator Q_S, and its absence gives Q_0.
Withdrawal at s is permanent. Let q_S and q_0 be the committors to F
before K. On the unfinished states T, Q_S q_S = 0 and Q_0 q_0 = 0, so

  (Q_S)_TT (q_S − q_0) = −((Q_S − Q_0) q_0)_T.

When absorption under support is certain, −(Q_S)_TT is invertible and its
inverse is the expected-occupation kernel of the supported chain. Hence

  D(s) = q_S(s) − q_0(s) = E_s^S [ ∫₀^τ f(X_t) dt ],  f = (Q_S − Q_0) q_0.

f(x) adds up, over the transitions out of x, the support's change in each
rate times the change in the unsupported committor across that
transition. That is the identity in the title.

## What follows

1. **What the support leaves behind is the state.** q_withdrawn(s) =
   q_0(s) depends on s alone, by the Markov property. A difference that
   persists after withdrawal is the unsupported committor of the state the
   support brought the system to. Nothing else carries over. A support
   that changes something not in the state, such as a capacity left out
   of it, falls outside the claim. [CLAIM-602](CLAIM-602.md)'s capacity is in its state.
2. **For a support that holds a nucleus**, as in [CASE-308](../cases.d/CASE-308.md),
   f(1, n) = d_n (q_0(1, n) − q_0(0, n)): the nucleus's unsupported
   dissolution rate times its worth under unsupported rates, Δ_N⁰, a
   committor form of [TERM-117](../terms.d/TERM-117.md)'s Δ_N. D is small before completion only
   where this product is small along the supported path. There are two
   ways for that to happen:
   - **held**: the units built make the nucleus stable, so d_n → 0;
   - **not needed**: the nucleus stops mattering to completion, so
     Δ_N⁰ → 0.
3. **Otherwise the support is needed to the end.** If the nucleus stays
   fragile and needed, D stays bounded away from zero however far
   assembly has gone. In the case it is still 0.10 at the last unit with
   the rate effect alone. Where the nucleus is a part the target needs, D
   can even rise with progress.

## What it adds

- **To [QUESTION-398](../questions.d/QUESTION-398.md):** an answer in models of this kind. A partial
  organization becomes independent of the intervention that established
  it when what it has built takes over what the intervention was
  doing, here holding the nucleus, or makes that work unneeded. That is
  a condition on the state reached and the unsupported dynamics, not on
  how much has been built. It is close to [CLAIM-600](CLAIM-600.md)'s first condition,
  support that "started a process that keeps itself going". It gives that
  condition a measure: the integrand f, read along the path.
- **To A's test:** D is measurable only at unfinished states. Timed
  withdrawal mixes in runs already finished, and its drop falls to zero
  even where every state's D is large ([CASE-308](../cases.d/CASE-308.md)).
- **Beside [CLAIM-604](CLAIM-604.md):** there an outage of finite length matters. Here
  withdrawal is for good, so the claim says nothing about duration.

## What it does not say

- That any real assembly's nucleus is held by what it builds.
- That D falls monotonically. In a random sweep it rose in 42 % of
  parameter sets without feedback or a rate effect.
- That the identity is new. It is the standard perturbation formula for
  absorption probabilities, applied to A's measure.
