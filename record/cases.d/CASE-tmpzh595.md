---
status: Proposed
title: 'Two workshops with the same dependence and the same integration, the part able to withdraw and renegotiate in one and its terms set at the controlling agent''s discretion in the other'
version: 1
standing: fictional
kind: thought-experiment
tags:
- society-and-governance
- ethics
- game-theory
date: '2026-11-13'
line:
- organizational-normativity
- distributed-agency
bears_on:
- QUESTION-461
- QUESTION-460
- QUESTION-tmpyesgg
summary: >-
  The assistant's, the discriminating case for [CLAIM-tmp6p3ki](../claims.d/CLAIM-tmp6p3ki.md), offered at
  step 12 of the filing of "About Plantation Paradise" ([#488](https://github.com/dmarx/nucleation/issues/488)) and accepted
  by the owner on 2026-11-13. Two workshops, sense-1 arrangements
  ([TERM-074](../terms.d/TERM-074.md)) run by a controlling agent R, each with a constituent P. The
  whole needs P as much in both, P needs the whole as much in both, P gave
  up the same capability to join in both, and P is a constituent in both.
  Only control over the terms differs: in A, P can withdraw and
  renegotiate; in B, R sets P's terms and P cannot leave. In a toy
  bargaining model, P's share responds to the whole's need of P by one half
  in A and not at all in B, and in B P's payoff lies anywhere R chooses
  within a range of 7 on a surplus of 10. Fictional, to hold fixed what no
  real case does. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmp6p3ki TERM-tmp169d8 TERM-tmpc9uv8 — filed with this case, Proposed -->
<!-- inactive-ok-file: CLAIM-671 CLAIM-428 CLAIM-603 CASE-256 CASE-257 TERM-083 — Proposed; the record's entries this case is built against, cited with their standing -->

# CASE-tmpzh595: Two workshops with the same dependence and the same integration, the part able to withdraw and renegotiate in one and its terms set at the controlling agent's discretion in the other

## Which sense of "organization"

[TERM-074](../terms.d/TERM-074.md) sense 1: each workshop is an arrangement of roles and terms. It
has a controlling agent, R, an agent or a role that can set terms, because
the case is about who controls them. P is a person, so P has standing
([TERM-083](../terms.d/TERM-083.md)). Neither workshop is assumed to be an agent itself.

## The case

Two workshops, A and B, each produce a joint surplus S = 10 from P's
contribution and R's.

Held fixed in both:

- **The whole's dependence on P.** Without P, R's side can make
  a_R = 2, so the workshop loses 8 if P's contribution is withdrawn. A6
  §2's predicate: "Withdrawing the contribution disrupts or diminishes the
  production".
- **P's dependence on the whole.** Alone, P can make a_P = 0.
- **The integration that produced that dependence.** In both, P gave up
  the same stand-alone capability on joining, because the workshop
  supplies it. That is [CLAIM-603](../claims.d/CLAIM-603.md)'s route to dependence, run the same way
  in both.
- **Membership.** P is a constituent of the workshop in both. [CASE-256](CASE-256.md)
  varies membership with vulnerability held fixed; this case holds
  membership fixed and varies control.

What differs is control over the terms on which the dependence is met:

- **In A**, P can withdraw and can renegotiate. Terms are bargained. With
  the symmetric Nash solution, P's share is
  a_P + (S − a_P − a_R)/2 = 0 + (10 − 0 − 2)/2 = 4, and R's is 6.
- **In B**, R sets P's terms and P cannot leave. R pays the least that
  keeps P working, r = 1, and keeps 9.

## What the numbers show

Checked with exact fractions (`python3 -I`, in the session's scratchpad):

| | A: P can withdraw and renegotiate | B: R sets the terms |
|---|---|---|
| P's share, the whole's need of P = 8 (a_R = 2) | 4 | 1 |
| P's share, the whole's need of P = 10 (a_R = 0) | 5 | 1 |
| Change in P's share per unit of the whole's need | 1/2 | 0 |
| Range of P's payoff that R can choose (a_R = 2) | none: the solution fixes it | from 1 to 8, a width of 7 |

- **Whole on part.** In A the whole's need of P is P's hold on its terms:
  each unit of the workshop's need moves half a unit to P. In B the same
  need gives P nothing. P is as indispensable as in A, and the dependence
  is not P's power.
- **Part on whole.** In A, P's payoff is fixed by the bargain, not by
  anyone's choice. In B it is wherever R chooses to put it, within a
  range of 7 on a surplus of 10. P's dependence on the workshop is, in B
  and not in A, vulnerability to R's discretion. That is the antecedent of
  [CLAIM-671](../claims.d/CLAIM-671.md), which says that under a principle grounding special
  obligations in such vulnerability, R's responsibilities toward P are
  strengthened. B meets it and A does not, at the same magnitude of
  dependence and the same integration.
- **Magnitude.** Raising the workshop's need of P from 8 to 10 raises P's
  share in A and leaves B unchanged. Magnitude sets how much rides on the
  relation; control sets which way it runs. [CLAIM-428](../claims.d/CLAIM-428.md)'s "the same
  dependence can be organized as mutual opportunity, as competitive
  vulnerability or as coercive leverage" is A against B.

## What it does not show

- **That the numbers are the world's.** The case is fictional and the
  model is a toy: symmetric Nash bargaining against a take-it-or-leave-it
  offer. It shows that the outcomes can come apart at equal dependence,
  not how often or by how much they do.
- **That B is exploitation.** Whether R's 9 against P's 1 is exploitation
  needs a standard declared with the judgment ([TERM-tmp169d8](../terms.d/TERM-tmp169d8.md), [CLAIM-363](../claims.d/CLAIM-363.md)).
  B is domination in [TERM-tmpc9uv8](../terms.d/TERM-tmpc9uv8.md)'s sense only once a standard of
  answerability is declared and R's capacity fails it.
- **That control is the only ground of obligation.** [CASE-256](CASE-256.md)'s first
  result, that membership grounds obligations of its own, is not tested
  here: membership is held fixed.
- **Who bears anything where no agent controls the terms.** Without an R,
  for an organism and its cells, the case has nothing to vary.
  [QUESTION-460](../questions.d/QUESTION-460.md) keeps that open.
- **That "dependence" here is everyone's measure.** It is measured as
  what each side would lose by withdrawal, apart from whether it can
  withdraw. A measure that counts the availability of exit inside
  dependence would call B's P more dependent, and the case would then
  vary dependence too. The case says which measure it means.

## Where the real cases fall

[CASE-257](CASE-257.md), the Saint-Domingue theatre, is near B for its enslaved
contributors: dependence of the institution on their labour with no
authority, as its readings report. But it differs from any A in more than
control, so it cannot be the contrast. That is why this case is
fictional.
