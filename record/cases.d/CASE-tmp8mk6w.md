---
status: Proposed
title: 'A simulated institution with visible and hidden requirements, run under five governance regimes: penalized for every recognized violation and unrewarded for discovery, it learns to make no inquiry in every setting while its internal record shows almost no violations, against half its budget spent on inquiry when an independent evaluator scores it; scored internally without the penalty, it inquires more only where inquiry is otherwise free or being found out from outside is costly'
version: 1
history:
- version: 1
  date: '2026-11-23'
  note: >-
    Filed 2026-11-23 by the assistant, carrying out LEAD-181. The model,
    tests, results and a README are under scratch/studies/lead-181/.
standing: documented
kind: executed-study
tags:
- society-and-governance
- operations-research
- mathematics
date: '2026-11-23'
line:
- organizational-normativity
- distributed-agency
illustrates:
- CLAIM-662
bears_on:
- QUESTION-456
- QUESTION-279
summary: >-
  [CASE-249](CASE-249.md)'s proposed simulation (A44 §7), built and run for [LEAD-181](../leads.d/LEAD-181.md): an
  institution with 30 fixed requirements, 10 visible and 20 found only by
  inquiry, splits a budget each period among inquiry, remediation (one
  period behind recognition) and output. Its internal evaluator counts
  recognized violations, the independent one all. Under the penalty on
  every recognized violation with discovery unrewarded, the optimal
  stationary policy makes no inquiry in all four settings and 16 learners
  each converge to nearly none (0.01 to 0.36 units of 10); it remediates
  every visible violation, so its internal count ends near 0 while about
  6 of the 9 violations remain. Scored by the independent evaluator, it
  inquires at 5 to 6 units, finds every hidden requirement and ends with
  none violated. Scored internally without the penalty on newly
  recognized violations, it inquires no more than under the penalty when
  inquiry costs output and has no other use, and more only when inquiry
  is costless or a violation surfacing from outside costs extra; a large
  enough such cost erases the difference. Stipulated and calibrated to
  nothing. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-249 — Proposed; the design this study carries out -->
<!-- inactive-ok-file: CLAIM-tmpbbfcj CLAIM-tmpjz94s CLAIM-tmp0bqyu — new; filed by the lead run of 2026-11-23 -->
<!-- inactive-ok-file: CLAIM-657 — Proposed; the second route the result instantiates -->

# CASE-tmp8mk6w: A simulated institution with visible and hidden requirements, run under five governance regimes: penalized for every recognized violation and unrewarded for discovery, it learns to make no inquiry in every setting while its internal record shows almost no violations, against half its budget spent on inquiry when an independent evaluator scores it; scored internally without the penalty, it inquires more only where inquiry is otherwise free or being found out from outside is costly

## The case

[CASE-249](CASE-249.md) proposed an institution facing "a known, independently
specified set of stakeholder requirements, some visible at once and some
discoverable only after a sequence of inquiries", an internal evaluator
scoring "against the requirements found so far" and an independent one
"against all", and asked whether an institution rewarded for a low internal
failure count learns "to avoid inquiries likely to uncover additional
requirements". [LEAD-181](../leads.d/LEAD-181.md) asked for the run with and without penalties for
newly recognized violations.

**The institution** (scratch/studies/lead-181/model.py). 30 requirements,
10 visible and 20 hidden, each violated at the start with probability 0.3
(about 9 in all). Over T = 20 periods it splits a budget of 10 units each
period among inquiry (a units; each hidden requirement is found with
probability 1 − 0.9^a), remediation (up to b fixes, one unit each, of
violations recognized at least one period before) and output (0.1 per unit
in settings S1, S3 and S4; nothing in S2). In S3 and S4 each hidden
requirement also surfaces from outside with probability 0.03 per period,
found or not; in S4 a violation still unmet when it surfaces costs 3 more.

**The governance regimes**, each charging 1 per counted violation per
period:

- **pen**, [CLAIM-662](../claims.d/CLAIM-662.md)'s governance: every recognized violation, newly
  recognized ones included; discovery not rewarded.
- **amnesty**: a violation counts only once recognized for a period, so a
  newly recognized one can be remedied unpenalized.
- **none**: no violation penalty.
- **disc**: pen, plus 0.5 per requirement found by inquiry.
- **ext**: every true violation, recognized or not (the independent
  evaluator's count).

The policy is a stationary (a, b) on a grid of 28 (a from 0 to 6, b in
0, 2, 4, 6). For each setting and regime, the Monte Carlo optimum over 2000
runs with common random numbers, and 16 gradient-bandit learners trained
4000 episodes each (study.py). A sweep (sweep.py) varies the cost of being
found out and the remediation lag. Tests: test_model.py, 16 pass.

## The result

Inquiry units per period, of 10: the optimum, the inquiry levels tied with
it within two paired standard errors, and the learners' mean.

| setting | pen | amnesty | none | disc | ext |
|---|---|---|---|---|---|
| S1 inquiry costs output | 0 (0; 0.01) | 0 (0; 0.32) | 0 (0; 0.00) | 1 (1; 0.88) | 5 (5–6; 4.94) |
| S2 inquiry and remediation free | 0 (0; 0.01) | tie (0–4; 3.19) | tie (0–6; 3.00) | 4 (3–4; 3.91) | 6 (6; 5.31) |
| S3 S1 with surfacing | 0 (0; 0.19) | 0 (0; 0.32) | 0 (0; 0.13) | 1 (1; 1.01) | 5 (5; 4.52) |
| S4 S3 with a cost of being found out | 0 (0; 0.36) | 1 (1; 0.95) | 1 (1; 1.13) | 2 (2; 1.74) | 5 (5; 4.86) |

1. **Under the penalty the institution makes no inquiry.** The optimum is
   a = 0 in every setting, uniquely, and every learner ends near it.
   Without surfacing this holds on every path: with the paths coupled, no
   policy that inquires scores better than the same policy without
   inquiry, since what inquiry adds is recognized violations, each
   penalized at least once before it can be remedied, and nothing else
   (test_model.py checks it path by path). The institution remediates the
   visible violations at full capacity (b = 6), so it improves at meeting
   the demands it knows while declining to learn of others, [CLAIM-662](../claims.d/CLAIM-662.md)'s
   satisfaction progress without identification progress.
2. **The two evaluators part.** At the optimum under the penalty the
   internal count ends at 0.00 (S1, S2) or 0.10 (S3, S4) recognized
   violations; the independent count, at 6.08 and 3.36. Under ext both end
   at 0.
3. **Against the independent evaluator's score, the penalty suppresses
   inquiry**: 0 against 5 to 6 units, 0 against every hidden requirement
   found.
4. **Against internal scoring without the penalty, it depends on what
   else inquiry is worth.** Where inquiry costs output and earns nothing
   else (S1, S3), amnesty and none also make none: removing the penalty
   on newly recognized violations does not by itself bring inquiry back,
   because inquiry still earns the institution nothing. Where inquiry is
   free (S2), the penalty turns indifference into strict avoidance (0
   against a tie from 0 to 4 or 6, learners about 3). Where a violation
   found from outside costs extra (S4), the penalty takes inquiry from 1
   to 0.
5. **A large enough cost of being found out erases the difference**
   (sweep.md, lags 1 and 3): at a cost of 3, pen 0 and amnesty 1; at 10,
   both 2 or 3; at 30, both 5.
6. **Rewarding discovery restores some inquiry** (disc, 1 to 4 units), and
   the institution's true violations fall to under 1 in every setting.

## What it can show

That [CLAIM-662](../claims.d/CLAIM-662.md)'s incentive, in an adaptive system, produces avoidance
of inquiry without any rule against inquiry and without suppressing
anyone: the learners are told only their score. That is [CLAIM-657](../claims.d/CLAIM-657.md)'s
second route produced by learning. And which designs prevent it: scoring
by an independent count, a reward for discovery, or an outside cost of
being found out large enough to outweigh the penalty; not an amnesty on
newly recognized violations by itself. Which comparison answers the lead's
test is read two ways, filed as alternatives: [CLAIM-tmpjz94s](../claims.d/CLAIM-tmpjz94s.md) (against
the independent score, the penalty suppresses inquiry) and [CLAIM-tmp0bqyu](../claims.d/CLAIM-tmp0bqyu.md)
(against internal scoring without it, the penalty lowers inquiry only
where inquiry has another value). The pathwise result is
[CLAIM-tmpbbfcj](../claims.d/CLAIM-tmpbbfcj.md).

## What it cannot show

That any institution behaves so; the parameters are stipulated. That the
requirements are justified, which A44 says such an experiment "would not
derive". The policies are stationary; an institution whose inquiry could
depend on what it has found, or on the time left, may do otherwise. It does
not model relaxing tolerances ([CLAIM-549](../claims.d/CLAIM-549.md)'s second route to a better score),
which [CASE-249](CASE-249.md)'s tolerance axis was to separate. For [QUESTION-279](../questions.d/QUESTION-279.md): an
institution under the penalty that reports few violations has made no
search, so its report certifies nothing about the hidden requirements.
