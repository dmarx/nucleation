---
status: Active
title: 'Role-indexed against scalar grants, and operators bound by the two grant conditions against unbound ones, in a population built on the coupled meaning–influence model'
version: 2
history:
- version: 2
  date: '2026-11-23'
  note: >-
    Promoted to Active at the status review's ruling (the owner delegated
    these rulings; ADR-057): the study in scratch/studies/lead-190/ was
    rerun on 2026-11-23: its tests pass and its result files reproduce
    exactly, so it is demonstrated (status-review README section 2).
standing: documented
kind: executed-study
tags:
- complex-systems
- self-governance
- game-theory
date: '2026-11-23'
line:
- distributed-agency
variant_of:
- CASE-363
bears_on:
- QUESTION-089
- QUESTION-090
- QUESTION-100
summary: >-
  The study [LEAD-190](../leads.d/LEAD-190.md) asks for. Twenty operators, half on each side, each a
  reader with a meaning and a specialist retrieving for the others, as in
  [CASE-363](CASE-363.md)'s model, which is loaded unchanged. Critic weights (whose
  evidence one reads) are scored by agreement, by observed relevance, or a
  mix; decision grants set authority under one-hop, leave-one-out or
  recursive aggregation, and operators move them for realized policy or
  for authority held. Five grant schemes and six grant games, on 30
  populations, in mean field and at agent level. Role indexing with the
  critic role scored by relevance leaves no factions and no capture;
  scalar grants fail either way; operators bound by both conditions
  delegate everything, all of it to their own side, beyond one hop too,
  and within their side to its extremes. A fictional model, by
  construction; the numbers are of this model. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-363 CLAIM-281 CLAIM-285 CLAIM-947 — Proposed; the built model this study extends and the claims it tests, cited as open -->
<!-- inactive-ok-file: CLAIM-tmp5wozo CLAIM-tmppm30v CLAIM-tmpdpnid CLAIM-tmpoc6mo — new; filed by the lead run of 2026-11-23 -->

# CASE-tmpw3vii: Role-indexed against scalar grants, and operators bound by the two grant conditions against unbound ones, in a population built on the coupled meaning–influence model

## What was done

[LEAD-190](../leads.d/LEAD-190.md) asks to "compare populations with role-indexed grants against scalar ones, and populations whose operators are bound by the two grant conditions against unbound ones, recording to whom they delegate beyond one hop." The code, its 27 tests and six experiments are in scratch/studies/lead-190/ (model.py, test_model.py, run.py, results/*.json; the README says how to rerun). model.py loads [CASE-363](CASE-363.md)'s model from scratch/studies/lead-090/model.py by path and does not modify it. A test checks that one reader with two sources is that model's mean field to 1e-12, in Regime A and Regime B. Everything ran on one thread in about twenty minutes.

**The population.** N = 20 operators (40 in one check), half on each side, s = ±1, in random order. Each has a preferred policy s·U(0.3, 1) and a relevance r ~ U(0.4, 0.9), its competence as a critic, drawn independently of side.

**The meaning layer.** This is [CASE-363](CASE-363.md)'s step, run once for each reader. Reader i frames its query by its own meaning. Source j's items lean to j's side by σ, and by j's own meaning by φ_s (φ_s = 0 makes each reader an independent copy of [CASE-363](CASE-363.md)). The meaning m_i moves toward the critic-weighted share of A-items. Critic weights W_i run over every source, i included. They relax with memory δ toward softmax(g·score), where score = ζ·agreement + (1 − ζ)·relevance. Agreement is [CASE-363](CASE-363.md)'s Regime A score against i's own meaning. Relevance is Regime B's independently observed score. ζ is [CASE-092](CASE-092.md)'s "independence of evaluation". The parameters are ρ = 0.2, σ = 0.4, φ = 0.3, ε = 0.2, g = 12 and δ = 0.9. That puts the loop above [CLAIM-947](../claims.d/CLAIM-947.md)'s threshold when ζ = 1 (gσ²/2 = 0.96 > 1 − φ′ = 0.76).

**The decision layer.** Grants E_ij ≥ 0, with E_ii = 0 and rows summing to at most 1. Authority comes from one of three rules, each with damping η = 0.5: one-hop ([CLAIM-375](../claims.d/CLAIM-375.md)'s rule), leave-one-out damped delegation ([CLAIM-502](../claims.d/CLAIM-502.md)), or damped recursive delegation ([CLAIM-282](../claims.d/CLAIM-282.md)). The decision p* is the authority-weighted mean of preferences ([CLAIM-375](../claims.d/CLAIM-375.md)). There are two objectives: realized policy, −(p* − p_i)², or authority held, log g_i. Each carries a quadratic grant cost (λ = 0.02), and a linear cost was run as a check. Operators move their rows by projected gradient ascent with exact gradients, which a test checks against finite differences for every rule, objective and cost. **Bound** means the first condition holds (one-hop or leave-one-out: g_i does not respond to E_i·, tested) together with the realized-policy objective. **Unbound** means recursive delegation with the authority objective.

**The grant schemes, for [CLAIM-281](../claims.d/CLAIM-281.md).**

- **scalar-agree.** One row, scored by agreement. It weights evidence and confers decision authority.
- **scalar-comp.** One row, scored by relevance.
- **scalar-policy.** One row, moved by the realized-policy objective: [CLAIM-285](../claims.d/CLAIM-285.md)'s operator with a single grant. The share it does not grant is weight on its own retrieval.
- **role.** Two rows. The critic row is scored by relevance (ζ = 0) and the decision row is moved by realized policy. This is A2's E_i(j, r, c, t) with two roles.
- **role-agree.** Two rows, with the critic row scored by agreement.

**The linearization.** At symmetry, in (m_i, a_i) with a_i = Σ_j W_ij s_j (the net side of i's reading), the uniform mode is unstable iff gζσ²/2 > 1 − φ′ − φ_s′. In that mode the population is captured as one. Every differentiating mode is unstable iff gζσ²/2 > 1 − φ′. This was checked against finite differences and against the eigenvalues on 300 random parameter sets.

## Results

**e1: the schemes, mean field, 30 populations, 1,000 rounds.** Belief factions are measured by the gap between the two sides' mean meanings and by own-side reading, the mean of a_i·s_i (0 means both sides read evenly, 1 means each reads only its own). Capture is one-sidedness, the mean of |a_i|.

| scheme (φ_s = 0) | b = 0, polarized start: gap / own-side / one-sided | b = 0.05: one-sided / share right | decision grants to opponents |
|---|---|---|---|
| scalar-agree | 0.76 / 0.72 / 0.72 | 0.84 / 1.00 | 0.51 |
| scalar-comp | 0.00 / 0.00 / 0.26 | 0.26 / 0.50 | 0.53 |
| scalar-policy | 1.05 / 1.00 / 1.00 | 1.00 / 0.50 | 0.00 |
| role | 0.00 / 0.00 / 0.26 | 0.26 / 0.50 | 0.00 |
| role-agree | 0.76 / 0.72 / 0.72 | 0.84 / 1.00 | 0.00 |

Under role, a reader's critic weight on opponents tracks their relevance (correlation 0.83), and half its critic weight crosses sides, which is chance. From a near-symmetric start on a balanced corpus, scalar-agree captures the population as one (one-sided 0.72, own-side 0.10). With φ_s = 0.2 its factions from a polarized start are harder (gap 1.05, own-side 0.91). Role-agree's meaning layer is scalar-agree's exactly in every condition.

**e2: agent level, k = 50 items, 20 seeds, 1,500 rounds.** Sampling noise dissolves scalar-agree's factions into capture as one: at b = 0 the gap was 0.00 ± 0.15 with one-sidedness 0.56; at b = 0.05, one-sidedness was 0.79 and every operator was right. Scalar-policy kept hard factions (gap 1.06, own-side 1.00). Role had gap 0.01 ± 0.05, one-sidedness 0.29, and gave no decision grants to opponents.

**e3: how independent the critic score must be.** ζ was swept in the role scheme from a polarized start, 10 populations each.

- With φ_s = 0 both thresholds fall at ζ* = 0.79. No population formed factions up to ζ = 0.8. At 0.85 two of ten did, at 0.9 four, at 0.95 nine and at 1.0 all ten. One-sidedness rose from 0.25 at ζ = 0 to 0.50 at ζ = 0.8.
- With φ_s = 0.2, the uniform threshold is ζ = 0.71 and the differentiating one ζ = 0.875. Between ζ = 0.7 and 0.9 there were no factions, but the population was captured as one, with one-sidedness 0.51 to 0.76. Factions appeared at ζ = 0.95 (four of ten) and ζ = 1.0 (ten of ten).

**e4: the grant game, 30 populations, 2,000 steps.**

| aggregation, objective | budget delegated | to own side (chance 0.47) | indirect share of reach / to own side | authority returned to oneself |
|---|---|---|---|---|
| one-hop, policy (bound) | 1.00 | 1.00 | 0 / — | 0 |
| leave-one-out, policy (bound) | 1.00 | 1.00 | 0.43 / 1.00 | 0 |
| recursive, policy | 1.00 | 1.00 | 0.47 / 1.00 | 0.03 |
| recursive, authority (unbound) | 0.96 | 0.52 ± 0.14 | 0.27 / 0.51 | 0.15 |
| one-hop or leave-one-out, authority | 0.00 | — | — | 0 |

"Reach" is the authority at k per unit of i's budget. "Indirect" is the part not carried by i's own grants, that is, what travels two hops or more. Within their own side, bound operators' grants correlate with how extreme the grantee is (0.88 one-hop, 0.90 leave-one-out), not with how near it is (0.07, 0.22). With linear cost the game cycles. Its time averages show the same pattern (aligned share 1.00, correlation with extremity 0.45 to 0.60, with nearness −0.07 to −0.11).

**e5: N = 40, 10 populations.** The same pattern held. Bound one-hop operators were aligned 1.00 with extremity correlation 0.92. Unbound operators were aligned 0.43 against chance 0.49, with self-return 0.15. Among the schemes, scalar-policy had gap 1.05 and role gap 0.

**e6: where the shared meaning goes under role.** At ζ = 0 the meaning settles at m* = (b + σa_r)/(1 − φ′) for every population, to 2e-15. Here a_r is the net side of the relevance-weighted softmax over specialists. The share of populations whose shared meaning matched the evidence is below.

| relevance range | b = 0.02 | b = 0.05 | b = 0.1 | b = 0.2 |
|---|---|---|---|---|
| 0.4 to 0.9 | 0.50 | 0.50 | 0.73 | 0.93 |
| 0.6 to 0.7 | 0.63 | 0.90 | 1.00 | 1.00 |
| equal | 1.00 | 1.00 | 1.00 | 1.00 |

Scalar-agree from a polarized start was right in every population for every b ≥ 0.02. It got there by capture.

## What it can show

That, in this model, the comparisons [LEAD-190](../leads.d/LEAD-190.md) names come out as the four claims filed with it say: [CLAIM-tmp5wozo](../claims.d/CLAIM-tmp5wozo.md) (the schemes), [CLAIM-tmppm30v](../claims.d/CLAIM-tmppm30v.md) (where a relevance-scored meaning goes), [CLAIM-tmpdpnid](../claims.d/CLAIM-tmpdpnid.md) (bound and unbound operators) and [CLAIM-tmpoc6mo](../claims.d/CLAIM-tmpoc6mo.md) (delegation to the extremes).

It cannot show that the model's choices are the right ones. The choices that matter most are these: relevance is observed without error and independently of side; a decision is a weighted mean; operators follow exact gradients of their own objective; and there are two roles and one policy dimension. A different decision rule, scoring with error, or bounded learners could change any of the results. Nothing here is about persons or organizations; [CLAIM-288](../claims.d/CLAIM-288.md)'s objection to [CASE-092](CASE-092.md), that the objectives are the modeller's, applies unchanged.
