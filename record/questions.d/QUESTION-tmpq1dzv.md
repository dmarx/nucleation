---
# Don't copy this file by hand — run `luria new question`. A QUESTION is an
# open question the record's own argument is organised around. Claims and
# THEORY readings name it in `answers`, and its page shows both (ADR-032).

# Open | Answered | Dissolved | Deferred | Superseded
status: Open

# The question, as a question. Repeat it as the `# QUESTION-…:` heading.
title: 'Does the critical delay of a delayed random Lotka–Volterra community still fall with diversity when self-regulation is weak and interactions set the leading eigenvalue, is its Hopf bifurcation supercritical, and is the divergent phase reported past it real under a stiff delay-equation solver?'

version: 1
tags:
- ecology
- complex-systems
date: '2026-10-20'

# REQUIRED: the line of inquiry, from `lines` in luria.yaml.
line: 'nucleating-argument'
summary: >-
  The delay-half promotion condition formerly on [THEORY-548](../theory.d/THEORY-548.md). [THEORY-548](../theory.d/THEORY-548.md)
  was narrowed and promoted on 2026-10-20 ([ADR-047](../decisions.d/ADR-047.md) v2 for the critical
  delay, v3 with a re-run against an averaging null for the variability).
  What it does not settle: the weak-self-regulation regime, whether the
  Hopf bifurcation is supercritical, and whether the divergent phase is
  real.


---

# QUESTION-tmpq1dzv: Does the critical delay of a delayed random Lotka–Volterra community still fall with diversity when self-regulation is weak and interactions set the leading eigenvalue, is its Hopf bifurcation supercritical, and is the divergent phase reported past it real under a stiff delay-equation solver?

## Why it is a question

[THEORY-548](../theory.d/THEORY-548.md) holds the linear result for generalised Lotka–Volterra
dynamics with every interaction delayed: stability is lost at
τ_c = min_j arctan(|Re j|/|Im j|)/|j| over the community eigenvalues j,
where a pair of roots crosses the imaginary axis transversally. It also
holds the variability pattern in Saeedian et al.'s one setting (strong
self-regulation, d_B = 10, σ_B = 0.1, C = 1), which the promotion review
found matches a null of independently oscillating species. Three things
the source reports or implies are not settled. Saeedian et al. show τ_c
falling with diversity at strong self-regulation only. They see sustained
oscillation past τ_c, but supercriticality is not derived. Past a second
threshold τ_c^C their Euler runs diverge, and refining the step did not
remove it. Until 2026-10-20 the first and third were [THEORY-548](../theory.d/THEORY-548.md)'s
promote_when.

## What would answer it

- The same analysis with weak self-regulation, where interactions rather
  than growth rates set the leading eigenvalue, showing whether τ_c still
  falls with S.
- A centre-manifold or normal-form computation of the first Lyapunov
  coefficient at τ_c, or numerical continuation of the cycle.
- A stiff delay-equation solver run past τ_c^C, showing bounded or
  unbounded trajectories.

What would not answer it: more Euler runs at the one strongly
self-regulated setting.
