---
number: 409
status: Active
formerly:
- CLAIM-tmpshzxc
title: 'For one state law, one intervention distribution and one outcome, a deficiency of sufficiency cannot increase under refinement: if T₁ = g∘T₂ then Γ(T₂) ≤ Γ(T₁); informational closure, by contrast, is monotone in neither direction, since in the three-bit chain of Rosas et al. (2024) A is closed, its refinement (A, B) is not and the full state refining that is closed again, while A⊕B, a coarsening of (A, B), is not closed either; closure fails to be monotone because refining a description changes the future it must predict as well as the evidence, so Blackwell dominance, which every deterministic refinement has over its coarsening, does not order closure'
version: 2
history:
- version: 2
  date: '2026-10-21'
  note: >-
    From the readings of 2026-10-21 of the causal-abstraction papers: they
    have no counterpart of Γ's monotonicity; their transitivity is a
    different property. The claim is unchanged.
role: thesis
warrant: demonstrated
defeated_if: >-
  A finite example with T₁ = g∘T₂, one state law, one intervention
  distribution independent of the state and one outcome, in which
  Γ(T₂) > Γ(T₁); or an error in the computation from THEORY-820's exact
  chain (A_{t+1}, C_{t+1} fresh fair bits, B_{t+1} = A_{t+1} ⊕ C_t): a
  transfer entropy from the micro past other than 0 for A, B, (A, C) or
  the full state, or other than 1 bit for (A, B) or A⊕B.
tags:
- information-theory
- complex-systems
- mathematics
date: '2026-10-21'
line:
- formal-apparatus
- distributed-agency
rests_on:
- CLAIM-407
grounds:
- THEORY-820
- THEORY-717
- THEORY-822
uses:
- TERM-068
summary: >-
  Two readers' drafts of one point, from A6, A7, A16 and A17 of the
  exchange of 2026-10-20. A16 §5 and A17's Proposition 2: a fixed-target
  deficiency is refinement-monotone; "Adding information cannot hurt exact
  sufficiency for an unchanged question, but changing what the description
  is expected to explain can expose new dependencies." A6 §6 and A7's
  Proposition 3: "Increasing the information retained by a representation
  can destroy a desirable dynamical property", and "There is no general
  data-processing inequality ordering these quantities, because both the
  predicted variable and the conditioning information change." This claim
  joins them, and corrects A7's slogan "When More Information Reveals Less
  Autonomy": closure is not reversed by refinement, it is unordered by it.
  Checked exactly on 2026-10-21.
illustrated_by:
- CASE-125
- CASE-164
---

# CLAIM-409: For one state law, one intervention distribution and one outcome, a deficiency of sufficiency cannot increase under refinement: if T₁ = g∘T₂ then Γ(T₂) ≤ Γ(T₁); informational closure, by contrast, is monotone in neither direction, since in the three-bit chain of Rosas et al. (2024) A is closed, its refinement (A, B) is not and the full state refining that is closed again, while A⊕B, a coarsening of (A, B), is not closed either; closure fails to be monotone because refining a description changes the future it must predict as well as the evidence, so Blackwell dominance, which every deterministic refinement has over its coarsening, does not order closure

## The claim

**Fixed target: monotone.** Let S carry a law, I be drawn by ρ
independently of S, and Y^(I) be the outcome, as in [CLAIM-407](CLAIM-407.md), with
Γ(T) = I(S; Y^(I) | T(S), I). If T₂ = f(S) and T₁ = g(T₂), then by the chain
rule

I(S; Y^(I) | T₁, I) = I(T₂; Y^(I) | T₁, I) + I(S; Y^(I) | T₂, I),

since T₁ and T₂ are functions of S and T₁ of T₂. The first term is
non-negative, so Γ(T₂) ≤ Γ(T₁), with equality exactly when Y^(I) is
independent of T₂ given T₁ and I. A16 §5 gives the same argument in
entropies: H(Y^(I) | T₂, I) ≤ H(Y^(I) | T₁, I) "because conditioning on
\(T_2\) supplies at least the information in \(T_1\), while
\(H(Y^{(I)}\mid S,I)\) remains unchanged." Nothing in it
is special to governance: it is any fixed-target sufficiency, as in
[CLAIM-152](CLAIM-152.md).

**Closure: monotone in neither direction.** Informational closure
([TERM-068](../terms.d/TERM-068.md), sense 1) of Z_t = g(X_t) is Δ_X(Z) = I(X⃗_t; Z_{t+1} | Z⃗_t) = 0
([THEORY-820](../theory.d/THEORY-820.md)). Take [THEORY-820](../theory.d/THEORY-820.md)'s chain, X_t = (A_t, B_t, C_t) bits, with
A_{t+1} and C_{t+1} fresh fair bits and B_{t+1} = A_{t+1} ⊕ C_t. Computed
from the exact chain with one, two and three steps of history:

| Z | A | B | C | (A, C) | (B, C) | (A, B) | A⊕B | X | constant |
|---|---|---|---|---|---|---|---|---|---|
| Δ_X(Z), bits | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |

- *Up the refinement order.* A ⪯ (A, B) ⪯ X, with Δ = 0, 1, 0. Refining a
  closed description can break closure, and refining further can restore
  it. The full state is always closed.
- *Down the order.* A⊕B ⪯ (A, B), with Δ = 1 and 1; constant ⪯ A⊕B, with
  Δ = 0 and 1. Coarsening a non-closed description can leave it non-closed
  or make it closed.

So the closed coarse-grainings are neither upward- nor downward-closed in
the refinement order. [THEORY-820](../theory.d/THEORY-820.md) has the first half (not closed under
common refinement). [THEORY-822](../theory.d/THEORY-822.md)'s closure under common coarsening holds for
strongly lumpable partitions, and is not a general coarsening property:
the identity is strongly lumpable and its coarsening (A, B) is not closed.

**Why.** Δ_X(Z) conditions on Z's own past to predict Z's own future.
Refining Z enlarges the conditioning set and also changes the target
Z_{t+1}. The data-processing inequality covers the first change alone. A7:
"There is no general data-processing inequality ordering these
quantities, because both the predicted variable and the conditioning
information change." In the chain, by the chain rule,
Δ(A, B) = I(X⃗; A_{t+1} | A⃗, B⃗) + I(X⃗; B_{t+1} | A⃗, B⃗, A_{t+1}) = 0 + 1 bit: the
bit is carried by the pair's future jointly, A_{t+1} ⊕ B_{t+1} = C_t. A16
§6 makes the same point for marginal against joint targets: with
Y₁ = U and Y₂ = U ⊕ K for fair independent U and K, I(K; Y₁) = I(K; Y₂) = 0
and I(K; Y₁, Y₂) = 1 bit. A16: "What fails here is the assumption that
sufficiency for each *marginal target* entails sufficiency for the *joint
target*." And A16 §5's moral: "Adding information cannot hurt exact
sufficiency for an unchanged question, but changing what the description
is expected to explain can expose new dependencies."

**Blackwell.** If Z₁ = h(Z₂), Z₁ is a garbling of Z₂ as an experiment about
X_t, with h as the garbling kernel. By [THEORY-717](../theory.d/THEORY-717.md), Z₂ is then at least as
good as Z₁ in every decision problem. So A ⪯ (A, B) in Blackwell's order,
and closure goes from 0 to 1 bit. A7's corollary: "Decision
informativeness and dynamical closure are not order-compatible." The
order that guarantees an ideal decision-maker can do no worse
([CLAIM-225](CLAIM-225.md)) does not order closure, because closure is not a fixed-target
sufficiency.

**Checked** on 2026-10-21: every entry of the table by exact enumeration of
the chain's path law at history lengths 1, 2 and 3; the XOR values; and
the monotone inequality on 3,000 random finite systems (up to seven
states, three outcomes and three interventions, with random refinement
pairs), with no violation.

## What it does not say

- **Not that richer descriptions are less autonomous.** A7's title, "When
  More Information Reveals Less Autonomy", and its "a description can
  become strictly more informative while becoming less autonomous", are
  true as an existence claim and wrong as a trend: the full state is
  always closed, and (A, C) refines A and stays closed.
- **Not that a finer description is better all told.** A17: refinement
  "does not worsen ideal sufficiency for an unchanged response target,
  although it may increase computational cost."
- **Not that Γ orders descriptions not related by refinement.** The
  inequality holds along refinement chains only. That optimal partitions
  at two budgets need not nest ([CLAIM-387](CLAIM-387.md), [CLAIM-392](CLAIM-392.md)) is about optima, not
  about one description's deficiency.
- **Nothing approximate.** Small Δ is not shown to behave better.
- **Not the causal-abstraction papers' transitivity.** Rubenstein et al.'s
  Lemma 5 and Beckers and Halpern's Theorem 3.9 compose abstractions of
  abstractions; nothing in those papers or in Beckers, Eberhardt and
  Halpern orders a deficiency along refinement ([NOTE-1037](../notes.d/NOTE-1037.md),
  [NOTE-1032](../notes.d/NOTE-1032.md)). The nearest analogue is the latter's composition bounds
  for approximate abstraction ([THEORY-843](../theory.d/THEORY-843.md)).
- **Not that closure marks a system, or its failure a non-system.** Noise is
  closed ([THEORY-820](../theory.d/THEORY-820.md)), and that closure gives no part–whole order on
  candidate units is the open half of [QUESTION-218](../questions.d/QUESTION-218.md).
