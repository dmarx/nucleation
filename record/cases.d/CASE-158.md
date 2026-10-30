---
number: 158
status: Active
formerly:
- CASE-tmpjmerx
title: 'Audited governance against a contextual router after a reversal of expertise: specialist denoisers with frozen, separately trained operators propose for one shared latent at each step, and spatial grants are revised from independent held-out probes of every proposal, available only from the next episode, against a fixed allocation, a conformity-scored allocation and a contextual mixture-of-experts router; the question is whether governance does anything a router does not, and under full-information audits the record predicts it cannot'
version: 2
history:
- version: 1
  date: '2026-10-25'
  note: >-
    Filed from A46–A47 of the exchange. Amended the same day after the
    readings of MultiDiffusion and Multi-LoRA composition: the fixed arm has
    published prior art, and the governed and router arms are what the
    case adds.
- version: 2
  date: '2026-10-26'
  note: >-
    A dated note added: a working group and a conventional router with
    the same information and authority tie in the Northstar study
    reported at T20 of the exchange "Experimental Infrastructure Review"
    (CASE-166), not reproduced. The case is unchanged.
standing: stipulated
kind: proposed-study
tags:
- self-governance
- complex-systems
- learning-theory
date: '2026-10-25'
line: distributed-agency
variant_of:
- CASE-144
summary: >-
  Proposed at A46 and reported at A47 of the exchange of 2026-10-24,
  continued, after the owner's "close the loop". It is [CASE-144](CASE-144.md)'s design,
  run without citing it, with competence frozen so that only the
  allocation learns, and with a conventional router added as the rival
  that [CLAIM-278](../claims.d/CLAIM-278.md) requires. A47 reported that the router won on every seed.
  Its results come from a sandbox the share does not carry, and the record
  has not run it. What would make it informative is one arm per failure of
  [QUESTION-271](../questions.d/QUESTION-271.md).
variants:
- CASE-162
---
<!-- inactive-ok-file: CLAIM-278 CLAIM-277 TERM-066 — Proposed; the objection this design is built to meet and the claim and term it bears on, nothing here rests on their being settled -->

# CASE-158: Audited governance against a contextual router after a reversal of expertise: specialist denoisers with frozen, separately trained operators propose for one shared latent at each step, and spatial grants are revised from independent held-out probes of every proposal, available only from the next episode, against a fixed allocation, a conformity-scored allocation and a contextual mixture-of-experts router; the question is whether governance does anything a router does not, and under full-information audits the record predicts it cannot

## The design (A47)

- Each perspective holds a low-rank denoising operator, trained beforehand
  on its own synthetic distribution and then frozen: "the LoRA parameters
  θᵢ are trained beforehand and frozen while governance adapts".
- Receivers keep trust, audited estimates of competence and spatial
  grants. Authorized proposals are combined, and the scheduler steps once.
- "**The current episode's audit cannot determine that episode's
  influence allocation**. Its results become available for future
  decisions." Probes are held-out images with known injected noise, and
  the audit has an explicit cost "so the governance mechanism doesn't get
  free information" (A47's progress note).
- 12 paired seeds of 84 episodes. The specialist each region requires
  changes halfway through.
- Four arms: fixed allocation; audited governance; conformity scoring,
  which "measures whether contributions resemble the prevailing collective
  proposal"; and a contextual mixture-of-experts router.
- A counterfactual that resets only the learned grants, keeping operators,
  trust estimates, environment and exploration fixed.

## Reported, not reproduced

Post-reversal held-out mean squared error:

| Arm | MSE |
|---|---|
| contextual mixture-of-experts router | 0.02216 |
| audited governance | 0.02521 |
| fixed allocation | 0.06476 |
| conformity scoring | 0.07259 |

Audited governance beat fixed and conformity-scored allocation on 12 of 12
seeds, and the router beat audited governance on 12 of 12. A47: "**We have
evidence that learned governance adapts, but not that it outperforms
conventional learned routing.**" And: "A learned governance mechanism
should not be considered explanatory simply because it changes the
allocation of influence. An ordinary contextual router can accomplish that
too." The software (v1.0 and `sd15_routed_lora.py`, the latter not run on a
real model) is not held.

## What the record predicts

- Every proposal is probed, which is full-information feedback. Audited
  governance should then recover with inertia and no lock-in, as in
  [CASE-157](CASE-157.md)'s extension (finding 1).
- The conformity arm has an endogenous metric, so it should hold the old
  allocation: [CASE-157](CASE-157.md)'s finding 2, [CASE-155](CASE-155.md)'s self-scoring c,
  and [TERM-066](../terms.d/TERM-066.md) built in by design.
- A router trained on the same audits is a mixture of experts whose
  experts earn responsibility by fitting better ([THEORY-937](../theory.d/THEORY-937.md)). Under
  full information, governance should not beat it.

All three of A47's outcomes are what the record predicts. [CASE-157](CASE-157.md)'s
extension, committed at 03:54 UTC on 2026-10-25, 42 minutes after A47 was
reported, found the first two in a different model, independently.

**Prior art for the fixed arm.** Frozen LoRA operators whose proposals are
combined in one scheduler step is LoRA Composite ([LIT-1529](../literature.d/LIT-1529.md),
[NOTE-1160](../notes.d/NOTE-1160.md)) with spatial grants, which is MultiDiffusion's fusion with
LoRA-modified models as the views ([LIT-1522](../literature.d/LIT-1522.md), [THEORY-958](../theory.d/THEORY-958.md)). Neither
paper learns, audits or routes the allocation, so the governed and router
arms are what this case adds. That merging LoRAs degrades as their number
grows ([THEORY-955](../theory.d/THEORY-955.md)) motivates combining per step. It is no evidence
about governance.

## Two caveats

- **The router may have had more information.** Governance is barred from
  the current episode's audit. A47 does not say whether the router also
  was, what context it saw, or whether it paid the audit cost. If it saw
  the region and an undelayed signal, "the router beats governance 12/12"
  partly measures information, not mechanism.
- **Competence is frozen.** So the design cannot show the loop A42 called
  crucial, access → experience → competence → future access, which "can
  also preserve an early advantage" ([CLAIM-277](../claims.d/CLAIM-277.md); [THEORY-927](../theory.d/THEORY-927.md)'s
  self-reinforcing gate). A47's claim to have "closed the **capability →
  evaluation → authority → deployment** loop" overstates this, as its own
  §4 concedes.

## What would make it informative

Arms in which governance could beat a router, one per failure of
[QUESTION-271](../questions.d/QUESTION-271.md):

1. **Cycles:** specialists whose wins against one another are
   intransitive.
2. **No common scale:** specialists scored on incommensurable criteria.
3. **Capture:** probe sets that the highest-trust specialists can add to,
   filter or duplicate.
4. **Bandit feedback:** probes only of the proposals that were heeded.

Plus one arm in which specialists keep training on the opportunities they
are given, for the entrenchment loop. The router faces the same audit
delay and cost in every arm. Outcomes are scored against held-out truth,
never against an arm's own metric. If governance beats the router only in
arms 1–4, [CLAIM-278](../claims.d/CLAIM-278.md) is answered in those regimes. If it never does, the
objection stands for this model class. A47 pointed the same way: "we need
tasks where the evaluation process itself becomes contested, incomplete,
selectively observed, or historically entrenched."

## What it cannot show

Anything about real organizations or real diffusion models: the operators
are small synthetic denoisers, and no pretrained model was run.

## Note of 2026-10-26: the third prediction in another model (reported)

<!-- inactive-ok-file: CASE-166 — Proposed; the reported study, cited as open -->

This case's third prediction: "A router trained on the same audits …
Under full information, governance should not beat it." T20 of the
exchange "Experimental Infrastructure Review" reports a working group with
delegated authority and a conventional router given "the same information
and authority" at the same regret, 0.00499 ([CASE-166](CASE-166.md)). It is a tie,
not a loss as here, and T20 does not say whether the router shares the
working group's code. Every arm is full-information, so none of this
case's arms 1–4 is present, and the result is what the prediction
expects. Reported, not reproduced: T20's "PerspectiveLab v2.11" is not
held, and dmarx/PerspectiveLab holds no v2.10 or v2.11 (its latest import
is c54617e, v2.9). The case is unchanged.
