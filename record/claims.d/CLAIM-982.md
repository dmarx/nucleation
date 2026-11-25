---
number: 982
status: Proposed
formerly:
- CLAIM-tmpprgb1
title: 'Ablations tell resolve only in conjunction'
statement: >-
  Under matched information and capacity, ablating an agent's slow structure
  tells resolve from mere persistence only by what the ablation removes and
  only in conjunction: a reset rules out inertia but not imposed protection,
  recovery from a reset rules out imposed protection, revision under a
  defeater as the commitment ages rules out entrenchment, and ablating the
  timescale or yoking the values can read resolve as inertia
version: 2
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-159, from the
    executed study CASE-383.
- version: 2
  date: '2026-11-23'
  note: >-
    Joins the work governance-of-possibility (ADR-144) at its
    membership pass of 2026-11-23, under ADR-104's rule: the revised
    manuscript in scratch/manuscripts/governance-of-possibility/ states
    its proposition or uses it as a step, in §5.2. No other change.
role: thesis
warrant: demonstrated
defeated_if: >-
  A rerun of CASE-383's code (scratch/studies/lead-159/) in which, on
  identical observation streams, the lesion leaves the resolve agent's
  persistence under irrelevant change unchanged or changes the inertia
  agent's, the resolve agent fails to recover from the perturbation or the
  imposed-protection agent recovers, or the timescale or yoked ablation
  makes the resolve agent's persistence fall; or an error showing that the
  ablated and intact runs did not receive the same inputs. A different
  construction in which a timescale or yoked ablation does separate resolve
  from inertia does not count: the claim is that these ablations can
  misread, shown by agents matched in information and capacity, not that
  they always do.
tags:
- self-governance
- behavioral-integration
- learning-and-conditioning
date: '2026-11-22'
line:
- will-organization
grounds:
- CASE-383
bears_on:
- QUESTION-440
summary: >-
  [CASE-383](../cases.d/CASE-383.md) builds [CASE-188](../cases.d/CASE-188.md)'s agents, with imposed protection and inertia
  added from [CLAIM-344](CLAIM-344.md)'s defeated_if, and ablates each one's slow structure
  four ways on identical inputs. A reset makes the persistence of resolve,
  entrenchment and imposed protection fall and leaves inertia's unchanged;
  left free after the reset, resolve re-establishes its structure and
  imposed protection cannot; yoking the slow values from another run
  changes nothing; raising the slow rates leaves resolve unchanged and
  removes inertia's persistence. Only revision under a defeater as the
  commitment ages separates resolve from entrenchment. So the control
  [CLAIM-344](CLAIM-344.md) names as its test, "perturbed or ablated with task information
  and capacity held fixed", has to say which ablation, and needs all three
  tests together. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
works:
- governance-of-possibility
---
<!-- inactive-ok-file: CASE-383 — new, the study this claim rests on, filed in the same batch -->

# CLAIM-982: Ablations tell resolve only in conjunction

## The claim

[CLAIM-344](CLAIM-344.md) holds that "mere slowness or persistence is not resolve", and its
defeated_if names the test: a learner whose preservation and revision of a
commitment "are unchanged when its slow influence structure is perturbed or
ablated with task information and capacity held fixed". [LEAD-159](../leads.d/LEAD-159.md) reads the
outcome the same way: "persistence unchanged by the ablation reads as
inertia."

[CASE-383](../cases.d/CASE-383.md) runs that control on four agents whose governance is known
and who choose alike under ordinary conditions: corrigible resolve,
entrenchment, imposed protection and inertia. On identical inputs and with
the same state variables:

1. **A reset of the slow structure** (to its initial value, frozen) makes
   persistence under an irrelevant change fall for resolve, entrenchment and
   imposed protection, and leaves inertia's unchanged. It rules out inertia,
   and nothing else.
2. **A reset the agent is left to recover from** restores resolve's
   persistence and not imposed protection's, which has nothing that
   re-establishes it. It rules out imposed protection: the "active causal
   maintenance" A36 named as the test of regulated retention (quoted in
   [CLAIM-344](CLAIM-344.md)).
3. **Revision under a defeater as the commitment ages** separates resolve,
   which revises at every age, from entrenchment, which stops revising as
   the defeater stops reaching its evaluator.
4. **Ablating the timescale** leaves resolve's persistence unchanged and
   removes inertia's; **yoking the slow values** from another run leaves
   resolve's unchanged. By the criterion "unchanged reads as inertia", both
   read resolve as inertia, and the timescale ablation reads inertia as
   resolve.

So "perturbed or ablated" names different tests that give different
verdicts, and a single matched-information ablation cannot carry
[CLAIM-344](CLAIM-344.md)'s distinction. The three tests together can.

## What it does not say

- It does not say any trained learner has resolve, or lacks it. The agents
  are constructed; the claim is about what the tests can tell apart.
- It does not say timescale or yoked ablations always misread, only that
  agents matched in information and capacity exist for which they do.
- It does not settle [CLAIM-344](CLAIM-344.md). It bears on how the claim's defeated_if
  would be applied: a lesion alone could not detect "externally imposed
  protection", which the defeated_if lists.
- It does not vary the legitimacy of the commitment; [CASE-383](../cases.d/CASE-383.md) says why
  these agents cannot.

## Relations

It bears on [QUESTION-440](../questions.d/QUESTION-440.md), whether authority goes with the slower variable:
in this construction the authority that protects the commitment is a
maintained level of precedence, and making it fast leaves the protection
in place while making a slow estimator fast removes inertia's. It speaks to
[CLAIM-344](CLAIM-344.md)'s test, not to whether the claim is true, so the relation is
carried in a dated note there.
