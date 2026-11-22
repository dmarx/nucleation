---
status: Proposed
title: 'The dependence rule tested on the record''s cases: on Northstar the operative trajectory leaves K while the regime and its criteria hold and a stipulated K sees nothing; on the fold, the tilt and the decaying capacity K comes from what the capacity maintains and its kernel from the capacity''s own dynamics'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-053 as a
    delegated lead worker. Script, tests and results under
    scratch/studies/lead-053/.
standing: documented
kind: executed-study
tags:
- agency
- self-governance
- complex-systems
date: '2026-11-22'
line:
- will-organization
bears_on:
- QUESTION-128
summary: >-
  [LEAD-053](../leads.d/LEAD-053.md) asks for a rule choosing [ARG-007](../arguments.d/ARG-007.md)'s maintenance constraints and a
  test on the record's cases. The rule, [CLAIM-tmpke0ap](../claims.d/CLAIM-tmpke0ap.md), is applied to
  [CASE-036](CASE-036.md) ([ARG-007](../arguments.d/ARG-007.md)'s ground) as a finite toy with a computed viability
  kernel, and analytically to [CASE-111](CASE-111.md), [CASE-112](CASE-112.md) and [CASE-227](CASE-227.md). On
  Northstar the organization leaves K at the second step while the
  emergency and its criteria hold throughout; with maintenance not
  deferred it keeps K and lifts the emergency; the organization's own
  standard as K registers nothing. On the formal cases K is set by what
  the capacity maintains and the kernel by its own dynamics, so the two
  stay apart. The boundary choice parts the readings [CLAIM-tmpnhrot](../claims.d/CLAIM-tmpnhrot.md) and
  [CLAIM-tmp8onwv](../claims.d/CLAIM-tmp8onwv.md) on [CLAIM-367](../claims.d/CLAIM-367.md)'s network and [CASE-227](CASE-227.md)'s outside supply. The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpke0ap CLAIM-tmpnhrot CLAIM-tmp8onwv — new, filed in this pull request for LEAD-053 -->
<!-- inactive-ok-file: CASE-227 CLAIM-367 — Proposed; cases the rule is tested on, cited as open -->

# CASE-tmp6mcpv: The dependence rule tested on the record's cases: on Northstar the operative trajectory leaves K while the regime and its criteria hold and a stipulated K sees nothing; on the fold, the tilt and the decaying capacity K comes from what the capacity maintains and its kernel from the capacity's own dynamics

## The study

The rule under test is [CLAIM-tmpke0ap](../claims.d/CLAIM-tmpke0ap.md): K holds the constraints that realize
the named capacity and every constraint they depend on for their
production, each at the least level at which what depends on it is still
produced, with a union over substitutable routes. The script is
`scratch/studies/lead-053/maintenance_rule.py`, its tests (8, passing)
`test_maintenance_rule.py`, its output `results.txt`; the README there
says how to rerun. The lead names [ARG-007](../arguments.d/ARG-007.md) and its training note; the cases
are those [ARG-007](../arguments.d/ARG-007.md) rests on ([CASE-036](CASE-036.md), through [CLAIM-025](../claims.d/CLAIM-025.md), which [CASE-111](CASE-111.md) and
[CASE-112](CASE-112.md) ground) and [CASE-227](CASE-227.md), which has the same separation with a
maintained capacity.

## [CASE-036](CASE-036.md), Northstar

A finite toy stipulated for this test, since the case gives no dynamics.
State (e, P, L): emergency on or off, maintenance practice P from 0 to 4,
legibility L from 0 to 4. Under the emergency maintenance is deferred and P
falls by one a step; off it, P recovers. L rises when P ≥ 2 and falls
otherwise. Deferred maintenance emits anomalies (P ≤ 2 or L ≤ 1). The
criteria, applied correctly: while an anomaly shows the emergency stays;
lifting is permitted only with no anomaly and L ≥ 2. The organization's
operative policy is cautious: it lifts only on full evidence (P = L = 4).

**The rule's K.** The capacity is leaving the emergency by the
organization's own means. Its realizer is the lifting decision, exercisable
when permitted: L ≥ 2 and no anomaly. The anomaly test depends on P and L,
and L depends on P. Least levels: L ≥ 2, P ≥ 3. So K = {P ≥ 3, L ≥ 2}, and
e is not a member: K is about the capacity, not the regime. Every input
came from the case's own text ("Deferred maintenance and workarounds
accumulate, the system becomes harder to read, and the anomalous signals
it emits satisfy the emergency criteria").

**Result.** From (e, P, L) = (1, 4, 3):

| t | state | emergency | criteria met | in K | in kernel |
|---|---|---|---|---|---|
| 0 | (1, 4, 3) | yes | yes | yes | yes |
| 1 | (1, 3, 4) | yes | yes | yes | yes |
| 2 | (1, 2, 4) | yes | yes | no | no |
| 3–8 | to (1, 0, 0) | yes | yes | no | no |

The operative regime and its governance hold at every step, and the
capacity is lost at step 2 and never regained. At step 1 the lift was
permitted and the cautious policy passed it up. That is [ARG-007](../arguments.d/ARG-007.md)'s
conclusion in a model where "precarious" is fixed by rule: effective action
and the capacity to govern among regimes come apart.

- **Control.** With maintenance not deferred, the same policy stays in K
  throughout and lifts the emergency at step 2. The rule does not find
  every emergency precarious.
- **K and kernel.** In this toy the kernel of K is K itself: from every
  state of K the lift is permitted. What the operative policy loses is K,
  not a margin inside it.
- **The stipulated rival.** Take as K the organization's own standard,
  the criteria met ([CLAIM-195](../claims.d/CLAIM-195.md)'s route, the system fixing its own K,
  carried to an agent). Every state of the run meets it, so its kernel
  holds the whole run, and the rival registers nothing. The criteria are
  what keep the emergency in place ([TERM-020](../terms.d/TERM-020.md), step 4: the effects "satisfy
  conditions that support continued activation"). A stipulated K is the
  lock-in's own standard, and cannot do [ARG-007](../arguments.d/ARG-007.md)'s work. It is not filed as
  a claim.

## [CASE-111](CASE-111.md), the fold

b is the maintaining activity and the capacity; μ the conditions. What b
maintains, the boundary, is not modelled, so its functional level b_f is
left as a parameter. With K = {b ≥ b_f} and μ in the bistable range, the
kernel is [max(b_f, b₋), ∞) when b₊ ≥ b_f, and empty otherwise. At κ = 1,
μ = −0.2: b₋ = 0.2764, b₊ = 0.7236 (the case's 0.276 and 0.724), and for
b_f = 0.1 the states 0.1 ≤ b < 0.276 are in K and outside the kernel,
checked by simulation on either side of the edge. The verdict, precarious
below b₋, is the same for every b_f < b₋, so the unmodelled level does not
decide it.

The two thresholds the rule excludes fail here. At the separatrix, K =
[b₋, ∞) and K is its own kernel, so nothing is ever precarious. At any
positive level, K = {b > 0} is never left by the decay toward 0.

## [CASE-112](CASE-112.md), the tilt

The capacity is revision: switching regime by the agent's own higher-order
volition, bounded by |h| ≤ h_max. It is exercisable while h_c(μ) =
2(μ/3)^{3/2} ≤ h_max, that is while μ ≤ μ_c = 3(h_max/2)^{2/3}. The case
says the will-organization "is what sets μ", so μ is the agent's own
constraint and K = {μ ≤ μ_c}: for h_max = 0.1, 0.2 and 0.385, μ_c =
0.407, 0.646 and 1.000, each checked by inverting h_c. The level is read
off what μ governs, the reach of h, which is step 3 of the rule. An
entrenchment that raises μ past μ_c removes the capacity while both
regimes stay stable.

## [CASE-227](CASE-227.md), the decaying capacity

The capacity c maintains the anti-phase mode, stable iff c > ½. So K =
(½, ∞), a level set by the mode, not by c's dynamics. c's own production,
2.2c²/(1 + c²) − c, gives the kernel [c₋, ∞) with c₋ = 0.64174 and c₊ =
1.55826, as the case has them. The case's c = 0.6 is in K and outside the
kernel, and reaches ½ at t = 2.879/ε. This is the rule working as
intended: K from what the capacity maintains, the kernel from the
capacity's own dynamics, and the gap between them is [CLAIM-079](../claims.d/CLAIM-079.md)'s.

## Where the readings part

The boundary choice the rule leaves ([CLAIM-tmpnhrot](../claims.d/CLAIM-tmpnhrot.md) narrow, [CLAIM-tmp8onwv](../claims.d/CLAIM-tmp8onwv.md)
wide) makes no difference on [CASE-036](CASE-036.md), [CASE-112](CASE-112.md) or [CASE-227](CASE-227.md) without
supply: every dependency there is the agent's own. It parts them on two:

- **[CASE-227](CASE-227.md) with an outside supply u** (A29 §10's arm "c kept by an
  outside controller"). u = 0.02 makes c = 0.6 grow (rate +0.0024).
  Narrow: u is a condition, K is unchanged, and the mode is viable under
  it. Wide: u is a member of K, and the capacity is precarious with u.
- **[CLAIM-367](../claims.d/CLAIM-367.md)'s network.** Narrow: the realizers of the capacity to
  transform lie outside the network, so it has none to maintain. Wide: it
  holds that capacity through the training process, precariously.

## What it cannot show

- **That Northstar has these dynamics.** The toy is the test's
  stipulation; the case is fictional and states its mechanisms in words.
  The result is that the rule, given those mechanisms, fixes K and
  delivers [ARG-007](../arguments.d/ARG-007.md)'s separation, not that any organization behaves so.
- **That dependencies are findable in practice.** In every case here they
  were given by the case's text or equation.
- **Which boundary reading is right.** That is the owner's call.
