---
number: 1202
status: Active
formerly:
- CLAIM-tmpz8q70
title: 'In the two-institution meaning–influence model, the loop between an evaluator and the party it evaluates can capture the evaluator''s reading when each institution is stable alone, when neither has a loop inside it, and when the evaluator''s conferral reads no interpretation at all; informational independence does not prevent it while a resource channel runs, and what does is a return channel too weak to close the loop, the evaluator''s reading not moving the party''s standing or evidence'
version: 3
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-015, from the
    executed study CASE-401.
- version: 2
  date: '2026-11-23'
  note: >-
    Joins the work governance-of-possibility (ADR-144) at its
    membership pass of 2026-11-23, under ADR-104's rule: the revised
    manuscript in scratch/manuscripts/governance-of-possibility/ states
    its proposition or uses it as a step, in §13.6. No other change.
- version: 3
  date: '2026-11-24'
  note: >-
    Promoted to Active at the owner's word of 2026-11-24 ("handle the
    fixes for the twelve ... use your best judgement", under the
    dialectic regime; ADR-057). Its stated fix was only that CLAIM-1000
    go first: its premise CLAIM-1000 and its ground CASE-401 are
    promoted in this pass (CASE-401 rerun 2026-11-24 by a session other
    than the filer's: 14 tests pass, every results file identical but
    timings), no objection targets it, and nothing meets its
    defeated_if, which asks only for a rerun of CASE-401's code that
    contradicts the four cases. No change of title.
role: thesis
warrant: demonstrated
defeated_if: >-
  A rerun of CASE-401's code (scratch/studies/lead-015/) in which, with
  each institution stable alone, the coupled map with the evaluator's
  conferral independent of its interpretation (g_E = 0), or with θ = 0 and
  a directional resource channel, stays at symmetry from a small push
  while the stated condition holds; or in which, with ψ = χ = 0, it leaves
  symmetry. A different reading of the channels does not count: the claim
  is stated for the directional channels of CASE-401, and the
  capacity reading of resources is CLAIM-1021.
tags:
- complex-systems
- society-and-governance
- self-governance
date: '2026-11-22'
line:
- distributed-agency
rests_on:
- CLAIM-1000
grounds:
- CASE-401
corroborates:
- CLAIM-404
complements:
- CLAIM-340
bears_on:
- QUESTION-100
- QUESTION-071
summary: >-
  What [CLAIM-1000](CLAIM-1000.md)'s condition says about [CLAIM-404](CLAIM-404.md)'s third part. In
  [CASE-401](../cases.d/CASE-401.md)'s model: two institutions with no inner loop are captured by
  the loop between them (round trip 1.11); an evaluator in Regime B, its
  conferral reading no interpretation, ends with its authority exactly
  balanced and its reading at m_E = 0.367 on a balanced corpus; with the
  evidence channel cut (θ = 0) a resource channel alone captures it
  (round trip 1.24); with the return channel cut nothing the party
  supplies does (θ = ω = 3, spectral radius 0.958). At agent level, 87% of
  200 runs were captured at round trip 1.42 and none with the return
  channel cut. It answers [CLAIM-404](CLAIM-404.md)'s second defeat condition in the
  negative for this model: the loop between the institutions adds what the
  loops within them do not. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
works:
- governance-of-possibility
---
<!-- inactive-ok-file: CLAIM-1021 — new; the study and the condition this claim rests on, and its alternative, filed in the same batch -->
<!-- inactive-ok-file: CLAIM-545 — Proposed; cited as the claim CLAIM-404 is a premise of -->

# CLAIM-1202: In the two-institution meaning–influence model, the loop between an evaluator and the party it evaluates can capture the evaluator's reading when each institution is stable alone, when neither has a loop inside it, and when the evaluator's conferral reads no interpretation at all; informational independence does not prevent it while a resource channel runs, and what does is a return channel too weak to close the loop, the evaluator's reading not moving the party's standing or evidence

## The claim

[CLAIM-404](CLAIM-404.md)'s third part: "where the organization's role is to evaluate another that affects its evidence or resources, the interpretation–authority loop can close between the two institutions, so that formal independence of the evaluator's procedure does not make its evaluation independent". Its second defeat condition: "a showing that an evaluator whose evidence or resources the evaluated party affects cannot be destabilized by that coupling when each institution's own interpretation–authority loop is stable, so that the loop between them adds nothing to the two loops within them." [LEAD-015](../leads.d/LEAD-015.md) says a model "in which no such instability exists defeats it".

In [CASE-401](../cases.d/CASE-401.md)'s model the instability exists, at [CLAIM-1000](CLAIM-1000.md)'s condition (θ + σ_E ω)(χ + σ_P ψ) > Δ_E Δ_P, and four of its cases speak to the claim's words.

1. **The loop between adds something.** With g = 0 in both institutions, neither has a loop inside it; with each at Δ = 0.76, θ = 1 and ψ = 1.6 captured both (m_E = 0.360). With inner loops present but sub-threshold (Δ = 0.44), A21's chain alone (θ = 0.6, ψ = 1) captured both. Each institution stable alone is not enough.
2. **Formal independence does not make the evaluation independent.** In Regime B the evaluator confers authority by independently assessed relevance, so its procedure reads no interpretation (g_E = 0, γ_E = 0, the one-institution remedy of [CLAIM-330](CLAIM-330.md)). Under θ = 1, ψ = 1 its authority stayed exactly balanced (a_E = 0) and its reading settled at m_E = 0.367 on a balanced corpus. Nothing in the evaluator's own structure shows the capture: its procedure and its allocation of authority are as independence requires; its reading is not. The capture is visible only in the pair.
3. **Informational independence alone does not prevent it.** With θ = 0, the evaluator's evidence untouched by the party, a resource channel (ω = 1.5, tilting which of the evaluator's specialists gains authority) and ψ = 1 captured both (m_E = 0.239, a_E = 0.455). Here the party governs the evaluator by the authority inside it, not by its evidence, as [CLAIM-404](CLAIM-404.md)'s first part says the routes come apart.
4. **The return channel decides.** With ψ = χ = 0, the evaluator's reading moving neither the party's standing nor its evidence, the round trip is zero and the pair stays symmetric whatever the party supplies: θ = ω = 3 left the spectral radius at 0.958. A21's criterion, "whether the processes conferring epistemic authority can themselves be corrected by evidence independent of the authority they confer", is here the condition that one leg of the loop be weak: either the party's hold on the evaluator's evidence and resources (θ + σ_E ω), or the evaluator's hold on the party's standing (χ + σ_P ψ), small against the margins.

Below threshold the loop still matters: a standing bias of the party's corpus moves the evaluator's reading by 1/(1 − L_E L_P) times what it would without the return channel (from 0.041 to 0.082 at a round trip of 0.5).

So, for this model, [CLAIM-404](CLAIM-404.md)'s second defeat condition fails, and its third part, which [CLAIM-404](CLAIM-404.md) calls interpretive, has a worked model in which it is demonstrated. That bears on [CLAIM-545](CLAIM-545.md), which has [CLAIM-404](CLAIM-404.md) as a premise. Whether this moves [CLAIM-404](CLAIM-404.md)'s warrant is the owner's call; the claim as stated is about institutions, and this is one model of them.

For [QUESTION-071](../questions.d/QUESTION-071.md): case 2 is an evaluator whose present structure, its procedure and its distribution of authority, shows nothing, while its reading is held by a loop through another institution. What would tell it apart is the pair's state, not the evaluator's.

## What it does not say

- That the channels are the right reading of [CLAIM-404](CLAIM-404.md)'s "evidence or resources" and "standing". They are directional: each tilts the other institution toward the side its own meaning leans. Under the capacity reading of resources a resource channel alone cannot destabilize symmetry ([CLAIM-1021](CLAIM-1021.md)), and point 3 then holds only above the linear threshold or from a large push.
- That any evaluator is captured, or that a captured reading is wrong. The party's lean could be the evidence's; on a balanced corpus here it is not.
- That corrective oversight is safe. With the evaluator's reading working against the party's lean the pair can oscillate, as [CLAIM-340](CLAIM-340.md) found for one institution.
