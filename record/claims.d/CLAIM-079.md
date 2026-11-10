---
number: 79
status: Active
formerly:
- CLAIM-tmpm39cj
title: 'Stability does not entail viability: a system can occupy a stable regime while losing access to trajectories that keep satisfying its constraints'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A notion of viability on which present constraint satisfaction under a
  stable regime guarantees viable trajectories over the relevant horizon.
tags:
- agency
- complex-systems
date: '2026-10-04'
line:
- will-organization
- formal-apparatus
works:
- organization-of-will
grounds:
- THEORY-134
- THEORY-132
summary: >-
  Applied from viability theory ([THEORY-134](../theory.d/THEORY-134.md)) and the stability/resilience
  distinction ([THEORY-132](../theory.d/THEORY-132.md)) (Section 6.3).
complements:
- CLAIM-521
- CLAIM-566
- CLAIM-577
- CLAIM-612
- CLAIM-625
---
<!-- inactive-ok-file: NOTE-1562 — Skimmed; Freidlin and Wentzell's front matter, cited from the reading of 2026-11-04 as open -->

# CLAIM-079: Stability does not entail viability: a system can occupy a stable regime while losing access to trajectories that keep satisfying its constraints

## The claim

"A system can currently satisfy the relevant constraints without possessing a
trajectory that continues to satisfy them over the relevant horizon."

## What it does not say

That more options are better: "A narrow path can be viable. A large option set
can be nonviable." (Section 6.4.) Who fixes the constraint set is the open
mapping question on [ARG-007](../arguments.d/ARG-007.md).

## Note of 2026-10-12: evidence now linked

[THEORY-142](../theory.d/THEORY-142.md) (March) now grounds this claim: without turnover, "the converged beliefs stay put while reality moves, and knowledge falls to chance". The evidence is a stylized simulation only.

## Note of 2026-10-13: a second line

Under [ADR-040](../decisions.d/ADR-040.md) (group C, decided by the owner) this claim also holds
`formal-apparatus`. It rests on no claim and is a claim about dynamical systems in general. It stays in will-organization and in the will paper. The second value means that setting will-organization aside would not take it from [CLAIM-195](CLAIM-195.md), which rests on it.

## Note of 2026-10-27: the edge says what the claim uses

The status review of this date ([ADR-057](../decisions.d/ADR-057.md), [ADR-058](../decisions.d/ADR-058.md)) moved [THEORY-142](../theory.d/THEORY-142.md) from `grounds` to `corroborated_by`. March's stylized simulation was linked as evidence on 2026-10-12. The demonstration rests on Aubin's viability kernel ([THEORY-134](../theory.d/THEORY-134.md)) and the stability/resilience split ([THEORY-132](../theory.d/THEORY-132.md)), both Active.

## Note of 2026-11-04: Freidlin and Wentzell, "Random Perturbations of Dynamical Systems"; Berglund, "Kramers' law"; Kuehn, "A mathematical framework for critical transitions", read

Freidlin and Wentzell (front matter only, [NOTE-1562](../notes.d/NOTE-1562.md)) and Berglund's survey ([NOTE-1590](../notes.d/NOTE-1590.md)) qualify the claim. Under small noise every stable state is only metastable, and the process leaves the domain of attraction almost surely on long horizons, so occupying a stable regime is itself temporary. Kuehn ([NOTE-1598](../notes.d/NOTE-1598.md)) supports the claim with a specific mechanism: a system on an attracting slow manifold is stable at every frozen parameter value, yet drifts to a point where normal hyperbolicity is lost and jumps far away (Def. 2.4). None of these is about constraint satisfaction or viability kernels as such. No status changes.

## Note of 2026-11-05: the constraint-architecture readings

Four readings from the pasted synthesis on constraint architectures bear on the claim. Obayashi et al. ([NOTE-1586](../notes.d/NOTE-1586.md)) support it in part: a passive walker's gait is asymptotically stable, yet its basin is "very small and thin" and a slow increase of slope destroys it by crisis; states inside the basin keep their access, so the fragility is thinness, not lost access. Asano's rimless wheel ([NOTE-1578](../notes.d/NOTE-1578.md)) is stable only within a slope window, a fit conditional on the parameter and less sharp. DeLuca et al. ([NOTE-1561](../notes.d/NOTE-1561.md)) support it by analogy: trapped configurations of simulated DNA origami "do not have a viable path to correct folding or have escape times which may be very slow". Damavandi et al. ([NOTE-1570](../notes.d/NOTE-1570.md)) show structural and energetic rigidity each holding without the other under prestress, a gap of the claim's logical shape; but that is local rigidity, not dynamical viability, an analogy only. No status changes.

## Note of 2026-11-07: survival-conditioned statistics, and a decaying capacity, from "Individuation, Possibility, and Disposition"
<!-- inactive-ok-block: CASE-231 CLAIM-612 CASE-227 — filed from the same exchange, Proposed -->

In the exchange "Individuation, Possibility, and Disposition" (2026-11-06 to 07; https://chatgpt.com/share/6aee7a9b-f13c-83e9-a865-6a29c2c3ff7e), A22 §1 cites this claim rightly, as the "distinction between stability and viability". A22 §5 adds a further case, [CASE-231](../cases.d/CASE-231.md) and [CLAIM-612](CLAIM-612.md): statistics conditioned on survival can be stationary, and reached on the mixing time, while absorption is certain. That extends this claim's note of 2026-11-04 from deterministic stability to the statistics of survivors. A29 §2's adaptive HKB system, [CASE-227](../cases.d/CASE-227.md), is another mechanism: a mode stable now, with the capacity that keeps it stable decaying. No status changes.
