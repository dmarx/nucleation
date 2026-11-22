---
status: Proposed
title: 'The coupled meaning–influence model built with two hypotheses and two specialists and reduced to its mean field: the symmetric state destabilizes when gσ² > 2(1 − φ(1 − ε)), whatever the conferral memory and the meaning rate; the reduced map is exactly a weighted-averaging opinion model with two stubborn sources whose weights relax toward an agreement kernel, equal to smooth bounded confidence on a balanced corpus; and it gives authority chosen by the initial interpretation and switched by the evidence with hysteresis, which fixed-weight and reflected-appraisal models cannot'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-090. The code,
    tests and result files are committed beside it under
    scratch/studies/lead-090/.
standing: documented
kind: executed-study
tags:
- complex-systems
- self-governance
- network-science
date: '2026-11-22'
line:
- distributed-agency
variant_of:
- CASE-092
bears_on:
- QUESTION-117
- QUESTION-100
draws_on:
- THEORY-1161
summary: >-
  The build [LEAD-090](../leads.d/LEAD-090.md) asks for. [CASE-092](CASE-092.md)'s model is written as an agent-level
  simulation (two hypotheses, a fixed corpus, two specialists, queries framed
  by the dominant interpretation with exploration, conferral from apparent
  retrieval success under Regime A or B) and reduced to its mean field in
  meaning m and authority a. Its linearization at symmetry is [CASE-099](CASE-099.md)'s with
  α = 1 − ρ(1 − φ′), β = ρσ, γ = (1 − δ)gσ/2, so [CLAIM-330](../claims.d/CLAIM-330.md)'s condition
  becomes gσ² > 2(1 − φ′): the meaning rate and the conferral memory cancel,
  and the fixed points are those of a Curie–Weiss equation. The reduced map
  equals, to 1e-12, a weighted-averaging model with two stubborn sources
  whose weights relax toward an agreement kernel; on a balanced corpus that
  kernel is Gaussian bounded confidence. Fixed-weight DeGroot and
  Friedkin–Johnsen, and the reflected-appraisal power maps of
  DeGroot–Friedkin and Friedkin 2011, cannot make the winner of authority
  depend on the initial interpretation, and none of them, nor Gaussian
  bounded confidence, lets corpus imbalance switch authority with
  hysteresis; the reduced model does both. A fictional model, by
  construction; the numbers are of this model. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-tmpgustv CLAIM-tmp6f8w8 CLAIM-tmpw3bak — Proposed or new; the study LEAD-081 filed today, and the claims this filing made -->

# CASE-tmpz4n6b: The coupled meaning–influence model built with two hypotheses and two specialists and reduced to its mean field: the symmetric state destabilizes when gσ² > 2(1 − φ(1 − ε)), whatever the conferral memory and the meaning rate; the reduced map is exactly a weighted-averaging opinion model with two stubborn sources whose weights relax toward an agreement kernel, equal to smooth bounded confidence on a balanced corpus; and it gives authority chosen by the initial interpretation and switched by the evidence with hysteresis, which fixed-weight and reflected-appraisal models cannot

## What was done

[LEAD-090](../leads.d/LEAD-090.md) asks to "Write [CASE-092](CASE-092.md)'s model, linearize it about its symmetric state, and compare a reduced form with the opinion-dynamics models [QUESTION-117](../questions.d/QUESTION-117.md) names at matched complexity." The code, its 13 tests and the experiments are in scratch/studies/lead-090/ (model.py, test_model.py, run.py; results/*.json; the README says how to rerun). Everything ran in under ten minutes on one thread.

**The model, as read from [CASE-092](CASE-092.md).** Two hypotheses A and B; a fixed corpus, balanced except in the hysteresis sweep (imbalance b); two specialists, s_A = +1 and s_B = −1, with specialization σ. The state is p, the collective's weight on A (m = 2p − 1), and w, the A-specialist's share of authority (a = 2w − 1). Each round a query is framed for A with probability q = (1 − ε)p + ε/2 (ε, exploration). Each specialist draws k items; one supports A with probability ½ + (b + s_jσ + φf)/2, f = ±1 the frame, φ the framing effect. Meaning moves toward the authority-weighted share of A-items at rate ρ. Conferral moves w with memory δ toward softmax(g·score). In Regime A the score is the agreement of a specialist's items with an interpretation drawn from the current meaning, p·ê_j + (1 − p)(1 − ê_j); in Regime B it is the share of its items judged relevant, the same in expectation for both.

**Choices made, and why.** [CASE-092](CASE-092.md) leaves three things open.

- *Scoring against the dominant interpretation*: read as agreement weighted by p (soft), because the lead asks for a linearization and the argmax reading (hard, also coded) is not differentiable at symmetry: under it any m ≠ 0 moves authority by a finite step, so the symmetric state is unstable for every g > 0.
- *Conferral with a memory timescale*: read as an exponential moving average, as [LEAD-081](../leads.d/LEAD-081.md)'s build did ([CASE-tmpgustv](CASE-tmpgustv.md)). A multiplicative (replicator) reading, the form of Friedkin's and Ito and Kaneko's updates, was run too.
- *Framing*: linear in p, with [CASE-092](CASE-092.md)'s exploration rate as the control.

**The reduced form.** As k grows and frames are averaged, the map is

  m′ = (1 − ρ)m + ρ(b + σa + φ′m),  a′ = δa + (1 − δ)tanh(gσm/2),  φ′ = φ(1 − ε),

checked against the exact expectation of the agent-level step to 1e-12, and against 4,000 agent-level draws to within 0.01 in m and 0.002 in a.

## Results

**Linearization (e1).** At (0, 0) the Jacobian is [CASE-099](CASE-099.md)'s J with α = 1 − ρ(1 − φ′), β = ρσ, γ = (1 − δ)gσ/2 and δ, checked against finite differences on 200 random parameter sets. [CLAIM-330](../claims.d/CLAIM-330.md)'s βγ > (1 − α)(1 − δ) becomes gσ² > 2(1 − φ′): ρ and (1 − δ) cancel. On 1,916 random parameter sets away from the threshold (|λ+ − 1| ≥ 0.01), the nonlinear map left symmetry exactly when the condition held (1,916 of 1,916). At σ = 0.4, φ = 0.3, ε = 0.2, g = 10, the captured state was a = 0.3795 for every ρ in {0.05, 0.2, 0.8} and δ in {0, 0.5, 0.9, 0.98} (spread 1e-9); only λ+, the speed of escape, changed. The fixed points solve a = tanh(Ja + h), J = gσ²/(2(1 − φ′)), h = gσb/(2(1 − φ′)), the Curie–Weiss equation, and its solution matched (0.3795, J = 1.053).

**Regime B and the replicator reading (e4, e6).** Regime B sets γ = 0: authority from opposite meaning starts was identical to the last digit. Under the replicator reading authority is neutral alone (δ_eff = 1), outside [CLAIM-330](../claims.d/CLAIM-330.md)'s conditions, so every positive loop destabilizes: at η = 0.05, 0.2 and 1, λ+ = 1.005, 1.019 and 1.072, and a went to 1 from m₀ = 0.001.

**Capture chosen by the initial interpretation (e2).** In the mean field, with a₀ = 0, the sign of the final authority was the sign of m₀ in every case, down to |m₀| = 0.001. In the agent-level model at g = 20 (k = 50), from exact symmetry, all 200 seeds captured (mean a over the last 100 of 600 rounds above 0.5 in absolute value), 46% toward A and 54% toward B; the sign of m over the first 50 rounds matched the winner in 94%. The captured meaning averaged |m| = 0.49 on a balanced corpus, whose faithful reading is m = 0. Below threshold (g = 3) the largest final |a| over 50 seeds was 0.09; Regime B at g = 20, 0.15.

**The predecessors (e3, e4, e5).**

- *Smooth bounded confidence with adaptive weights.* With λ = ρ(1 − φ′), stubborn sources at o_j = (b + s_jσ)/(1 − φ′), and weights relaxing with memory δ toward the agreement kernel exp(κ·m·o_j), κ = g(1 − φ′)/2, the reduced map is reproduced to 1e-12 for every b (100 random parameter sets, 50 steps each). On a balanced corpus the agreement kernel equals the Gaussian bounded-confidence kernel exp(−κ(m − o_j)²/2); δ = 0 is memoryless smooth bounded confidence. Off balance the two kernels differ.
- *Matched complexity.* The reduced [CASE-092](CASE-092.md) has six parameters (ρ, σ, φ, ε, g, δ) and four identifiable combinations (λ, o, κ, δ): two different parameter sets with the same four gave trajectories equal to 1e-13. So the adaptive-weight form is the more economical statement of the same dynamics.
- *Hysteresis in the evidence.* Sweeping b from −0.3 to 0.3 and back at g = 20, δ = 0.5, [CASE-092](CASE-092.md) and the agreement-kernel model gave the same loop: authority flips at b = ±0.12, a loop 0.23 wide, and at b = 0 the state is a = −0.97 on the way up and +0.97 on the way down. Gaussian bounded confidence, given the same sources, never flips: its kernel's centre moves with b, so the field h cancels from the authority equation and a stays at −0.97 across the sweep. Fixed-weight DeGroot / Friedkin–Johnsen with the same sources is linear and single-valued.
- *Reflected appraisal.* On the three-member system {collective, A-specialist, B-specialist} with symmetric relative weights, DeGroot–Friedkin (Jia et al., [LIT-1146](../literature.d/LIT-1146.md)) went to (0.82, 0.09, 0.09) and Friedkin 2011 with its Friedkin–Johnsen step ([LIT-1404](../literature.d/LIT-1404.md)) to (1, 0, 0) from every start; the two specialists' powers never separated. Neither power map reads opinions, so no start of the opinions can choose which specialist gains power. [THEORY-1161](../theory.d/THEORY-1161.md)'s point, that the single-issue step decides whether power concentrates, holds here: the anchored step concentrated it, on the collective.

## What it shows

That [CASE-092](CASE-092.md), reduced to its mean field with two specialists and scalar authority, is a known kind of model: weighted averaging with stubborn sources and homophilous adaptive weights. Its linear threshold is [CLAIM-330](../claims.d/CLAIM-330.md)'s with the memory and the meaning rate cancelled, and its attractors are Curie–Weiss. It is outside the content-blind models (fixed weights, DeGroot–Friedkin, Friedkin 2011, persuasion bias), and it is outside Gaussian bounded confidence off a balanced corpus, where authority answers the evidence with hysteresis. [CLAIM-tmp6f8w8](../claims.d/CLAIM-tmp6f8w8.md) states the first part; [CLAIM-tmpw3bak](../claims.d/CLAIM-tmpw3bak.md) the comparison.

## What it does not show

- Anything about role-indexed authority, operator turnover or demands; the reduction has scalar authority and two fixed specialists.
- That no read predecessor uses an agreement kernel. Holme and Newman ([LIT-1128](../literature.d/LIT-1128.md)) and Ito and Kaneko ([LIT-1842](../literature.d/LIT-1842.md)) adapt structure by similarity, with different units and kernels; none was rebuilt here.
- That the agent-level model has no behaviour the mean field lacks. Finite k and one frame per round add noise, which here only chose the direction of capture.
- That the numbers bear on any organization. The model is the assistant's reading of [CASE-092](CASE-092.md), and its parameters are illustrative.
