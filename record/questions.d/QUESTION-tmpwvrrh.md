---
# Don't copy this file by hand — run `luria new question`. A QUESTION is an
# open question the record's own argument is organised around. Claims and
# THEORY readings name it in `answers`, and its page shows both (ADR-032).

# Open | Answered | Dissolved | Deferred | Superseded
status: Open

# The question, as a question. Repeat it as the `# QUESTION-…:` heading.
title: "Does Coifman and Lafon's α-normalized diffusion limit hold on a compact manifold with boundary, in L² on band-limited functions at a stated rate, and does the iterated operator P_{ε,α}^{t/ε} converge to the semigroup of the limit operator?"

version: 1
tags:
- mathematics
- probabilistic-modeling
date: '2026-10-20'

# REQUIRED: the line of inquiry, from `lines` in luria.yaml.
line: 'formal-apparatus'

summary: >-
  The boundary and semigroup halves of the promotion condition formerly on
  [THEORY-744](../theory.d/THEORY-744.md). [THEORY-744](../theory.d/THEORY-744.md) was narrowed to compact manifolds without
  boundary and promoted on 2026-10-20 ([ADR-047](../decisions.d/ADR-047.md) v2), with the source's
  kernel expansion re-derived. What it does not settle: the limit near a
  boundary, at the rate the source prints, and the heat-kernel limit that
  the source's Proposition 11 claims.

---

# QUESTION-tmpwvrrh: Does Coifman and Lafon's α-normalized diffusion limit hold on a compact manifold with boundary, in L² on band-limited functions at a stated rate, and does the iterated operator P_{ε,α}^{t/ε} converge to the semigroup of the limit operator?

## Why it is a question

[THEORY-744](../theory.d/THEORY-744.md) holds Coifman and Lafon's α-normalized limit on a compact
manifold without boundary: (I − P_{ε,α})/ε → Δf + 2(1 − α)⟨∇U, ∇f⟩
uniformly on smooth functions at rate O(ε). That is minus the generator of a
reversible diffusion with invariant density q^{2(1−α)}. [LIT-1246](../literature.d/LIT-1246.md) also
claims two things the promotion review could not grant.

- **The boundary.** On a manifold with boundary, the source bounds the
  operator by O(1) on a strip of measure O(ε^γ) and concludes an L²
  remainder of O(ε^γ). The bound gives O(ε^{γ/2}). Convergence survives,
  but the printed rate does not.
- **The semigroup.** Proposition 11 replaces
  (I − εΔ)^{−1}(I − εΔ − εR_ε) by I − εR_ε. That needs R_ε to commute with
  Δ. It also drops a factor ‖(I − εΔ)^{−t/ε}‖ that grows like e^{tν_K²}, and
  it does not show that P_{ε,1} keeps the band-limited space invariant. So
  P_{ε,1}^{t/ε} → e^{−tΔ} is not proved as written.

An answer is a complete proof of either, from a later paper read in full or
re-derived step by step, or a counterexample. Numerical agreement on
manifolds without boundary does not bear on it, since the interior
expansion is settled.
