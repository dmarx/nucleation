---
number: 538
status: Active
formerly:
- CLAIM-tmplvc8b
title: 'On a finite graph of contexts whose overlaps carry preferred real offsets a and tolerances δ_e ≥ 0, an assignment within every tolerance, |Dx − a| ≤ δ, exists exactly when no cycle''s holonomy exceeds the sum of its tolerances; with every δ_e > 0 the least uniform enlargement of the tolerances that admits one is the largest ratio, over simple cycles, of holonomy to summed tolerance, so the obstruction is certified by a cycle; the feasible allocations of tolerance depend on the offsets only through their class in H¹, so local adjustment can move a mismatch among the overlaps of a cycle and never remove it; and an evaluation that omits one overlap of every witnessing cycle reports a compatibility that does not hold'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A connected finite graph, offsets and tolerances for which every simple
  cycle meets the inequality and no assignment exists, or for which the
  least uniform enlargement differs from the largest simple-cycle ratio,
  or for which two offset vectors in the same H¹ class have different
  feasible tolerance allocations.
tags:
- mathematics
- behavioral-integration
date: '2026-11-03'
line:
- distributed-agency
- formal-apparatus
rests_on:
- CLAIM-153
uses:
- TERM-060
- TERM-093
complements:
- CLAIM-347
- CLAIM-365
- CLAIM-361
- CLAIM-495
grounds:
- THEORY-1082
- THEORY-894
- LIT-1659
- LIT-1439
bears_on:
- QUESTION-133
summary: >-
  The owner's U27 of the exchange "Assess SDT Coverage" (2026-11-02),
  "compatibility of tolerance bounds", with U28's pointer to the record's
  sheaf tools, worked out at A28 §3 and A29 §§3–4, 7 and A32's Claim A.
  The feasibility criterion is the classical feasible-differential
  theorem of network flows (Rockafellar 1984; no checked identifier, not
  registered), and the ratio is LP duality, so the result is granted, not
  the record's discovery. What the record adds is the reading: the
  frontier is an invariant of the obstruction class, governance chooses
  where on it the mismatch falls, and omission can fake compatibility.
  Checked by linear programming against brute-force cycle enumeration on
  random graphs.
---
<!-- inactive-ok-file: NOTE-1588 — Proposed or new; the constraint-architecture readings of 2026-11-05, cited as open -->
<!-- inactive-ok-file: CLAIM-588 — Proposed or new; the resource-bounded realizability readings of 2026-11-05, cited as open -->

# CLAIM-538: On a finite graph of contexts whose overlaps carry preferred real offsets a and tolerances δ_e ≥ 0, an assignment within every tolerance, |Dx − a| ≤ δ, exists exactly when no cycle's holonomy exceeds the sum of its tolerances; with every δ_e > 0 the least uniform enlargement of the tolerances that admits one is the largest ratio, over simple cycles, of holonomy to summed tolerance, so the obstruction is certified by a cycle; the feasible allocations of tolerance depend on the offsets only through their class in H¹, so local adjustment can move a mismatch among the overlaps of a cycle and never remove it; and an evaluation that omits one overlap of every witnessing cycle reports a compatibility that does not hold

## The claim

Contexts are the vertices of a finite graph with incidence matrix D. Each
context sets a local value x_v, each overlap e = (u, v) has a preferred offset
a_e between them, and a tolerance δ_e within which a demand on that overlap
counts as met ([TERM-060](../terms.d/TERM-060.md)'s threshold demands, in additive form). The question
the owner's U27 asks is whether all the tolerances can be met at once.

- **The cycle criterion.** By Farkas, some x has |Dx − a| ≤ δ exactly when
  |cᵀa| ≤ Σ_e δ_e|c_e| for every circulation c (Dᵀc = 0). Conformal
  decomposition reduces this to simple cycles: the holonomy of a around each
  cycle must not exceed the cycle's summed tolerance. A28 §3's triangle shows
  it. The residuals sum around the cycle to minus the holonomy whatever x is,
  so the cycle total cannot be moved, only shared.
- **The certificate.** For δ > 0, the least ρ such that ρδ admits an
  assignment is ρ_δ(a) = max{|cᵀa| : Dᵀc = 0, Σ δ_e|c_e| ≤ 1}, the distance
  from a to im D in the δ-weighted ℓ∞ norm. The extreme points of the dual set
  are normalized simple cycles, so ρ_δ(a) = max over simple cycles C of
  |holonomy_C(a)| / Σ_{e∈C} δ_e. In A29's triangle, holonomy 1.2 against
  summed tolerance 0.9 gives 4/3.
- **An invariant of the class.** Under a → a + Dh the substitution x → x + h
  leaves every inequality unchanged. So the feasible tolerance allocations, the
  cycle inequalities and ρ_δ depend on a only through [a] ∈ H¹(G; ℝ). Local
  re-centring redistributes an obstruction and never removes it. On the
  frontier the residual is forced (r_e = ∓δ_e), so which overlap bears the
  mismatch is fixed by the allocation alone. That allocation is a choice, and
  whose choice it is is [CLAIM-361](CLAIM-361.md)'s question.
- **Omission.** Delete one edge of a witnessing cycle from what is evaluated
  and the evaluated graph may have no cycle there, so every offset can be met
  exactly on it. Feasibility on the whole graph implies it on any evaluated
  subgraph, not conversely, and on a forest it always holds. Adding overlaps
  to what is evaluated can only shrink the feasible allocations (A29 §9).

**Checked** by linear programming on 300 random graphs of six vertices
against the dual, and against brute-force enumeration of simple cycles on
random graphs of three to six vertices: no mismatch, largest gap 1.3 × 10⁻¹⁵.

For a linear cellular sheaf with coordinatewise box tolerances the duality
holds verbatim with ker δᵀ in place of the circulations. What fails beyond
the constant sheaf is only the reading of the witnesses as graph cycles.

## What it does not say

- **Anything about circle-valued or nonabelian offsets.** Those are [CLAIM-153](CLAIM-153.md)
  and [THEORY-1082](../theory.d/THEORY-1082.md), the exact cases.
- **That a minimal non-face of [CLAIM-347](CLAIM-347.md)'s complex is a cycle obstruction.**
  [CLAIM-347](CLAIM-347.md) itself declines that link.
- **That an allocation is fair or warranted.** Tolerances are declared; who may
  revise them, and against what reference, is [CLAIM-361](CLAIM-361.md)'s.
- **That low measured mismatch is compatibility.** That is the omission
  clause, and [CLAIM-357](CLAIM-357.md).

## Note of 2026-11-04: the cycle as a flow, and two ways to remove a cycle, from "Organizational Nucleation and SLT"

The owner's U25: "visualization needs more dynamics/flow, maybe instead of a simplex you try to motivate a sheaf". This claim already answers that request. The reader's construction below draws it as a flow.

- **The flow.** Take a 3-cycle with a = (0.5, 0.4, 0.3), so the holonomy is 1.2, and δ = (0.3, 0.3, 0.3).
  - Local re-centring is the gradient flow ẋ = DᵀW(a − Dx).
  - Along the flow the residuals keep their cycle sum at exactly 1.2, the holonomy.
  - The flow ends at the weighted harmonic residual, r*_e ∝ 1/w_e ([THEORY-1141](../theory.d/THEORY-1141.md)'s limit). That is (0.4, 0.4, 0.4) for equal weights and (0.686, 0.343, 0.171) for weights (1, 2, 4).
  - So the weights decide where the mismatch settles, which is [CLAIM-534](CLAIM-534.md)'s allocation part. They never decide whether it exists.
  - Feasibility needs ρ ≥ 4/3, this claim's A29 number.
  - Checked by simulation.
- **What A drew instead.** A25's animated figure covers a line with three patches, U₁ ∩ U₃ = ∅. Its nerve is a path, so the "mismatch" A shows can never be structural ("on a forest it always holds"). A says so itself: "a mismatch among the currently selected local proposals doesn't prove that no global section exists".
- **A26** says a cyclic obstruction needs "a torsor and specified transition offsets. Ordinary set incompatibility does not supply that automatically." That is right for [CLAIM-153](CLAIM-153.md). This claim is the real-offset version with tolerances, and A did not cite it.
- **Cut against cover** (the reader of U1–U7, from the owner's U3: "I think you need to take a closer look at the sheaf theoretic account in the discussion I linked."). Besides enlarging δ or changing [a] in H¹, a reorganization can remove a witnessing cycle in two ways:
  - it can *cut* the cycle by decoupling an overlap ([CASE-115](../cases.d/CASE-115.md)'s differentiation);
  - it can *cover* it with a context in which the three are coherent ([CLAIM-153](CLAIM-153.md): the triple overlap makes Φ a coboundary).

  Cutting the overlap is different from omitting it from evaluation. Omission fakes compatibility, by this claim's omission clause, while the coupling still acts. That difference is unchecked beyond the definitions.
- **Terms of art.**
  - (a) A's "tolerance" τ_i (A22–A24) is the slack on one demand's threshold. That is [CLAIM-347](CLAIM-347.md)'s threshold demand, not δ_e on an overlap. It needs no entry of its own.
  - (b) Read as this claim means it, A would have drawn a cycle of contexts, each overlap carrying an offset and a tolerance band, with holonomy against summed tolerance. A25's gluing test is exact equality, where this claim's test is |Dx − a| ≤ δ.
  - (c) The owner's U25 is in effect the correction.

No status changes.

## Note of 2026-11-05: the constraint-architecture readings

Two readings from the pasted synthesis on constraint architectures bear on the claim. Akitaya et al. ([NOTE-1579](../notes.d/NOTE-1579.md)) qualify it, on the reader's inference, since the paper names neither holonomy nor sheaves. In logarithms its face-closure condition is the claim's cycle condition with δ = 0, and its tolerance a multiplicative one on the same cycle. But the offsets come from a discrete choice of mode at each vertex, and deciding whether some choice closes every face is NP-hard, so exact cycle certificates do not make the global problem easy once the offsets are chosen discretely. Connelly and Whiteley ([NOTE-1588](../notes.d/NOTE-1588.md), read in part) give a second Farkas-type certificate: a first-order flex of a tensegrity framework fails to extend exactly when some proper self-stress gives it positive energy. That parallel is formal, an analogue only; no result is shared. No status changes.

## Note of 2026-11-05: the resource-bounded realizability readings

The second paste of the pasted synthesis on resource-bounded realizability glosses this claim as showing that "the obstruction can remain invariant even as the mismatch is redistributed among edges". That is the claim's own result: local re-centring "redistributes an obstruction and never removes it". [CLAIM-588](CLAIM-588.md) makes redistribution a design target of its own. A adds a caution for origami: rigid origami closure involves noncommuting spatial rotations and is not the additive scalar cohomology of this claim. The reading of Akitaya et al. ([NOTE-1579](../notes.d/NOTE-1579.md)) holds both sides: loop closure is a product of rotations about different crease axes equal to the identity, and near flat the paper's face condition, in logarithms, is this claim's cycle condition with δ = 0, on the reader's inference. A credits the record with the warning that "A shared vocabulary of gluing does not make them one mathematical obstruction." No status changes.
