---
status: Active
title: 'A Lipschitz map from a subset of a metric space whose points are at least ε apart and whose diameter is D extends to the whole space into Hilbert space with Lipschitz constant at most 6D/ε times its own, and, by Benyamini''s argument in the same paper, into any Banach space with at most 4D/ε, with no dependence on the number of points'
version: 1
tags:
- mathematics
date: '2026-10-16'
source:
- LIT-tmp7skui
summary: >-
  Johnson and Lindenstrauss (1984), [LIT-tmp7skui](../literature.d/LIT-tmp7skui.md), read in [NOTE-tmpmv42v](../notes.d/NOTE-tmpmv42v.md).
  Theorem 2 gives 6D/ε for maps into ℓ₂, through ℓ₁ and a weak form of
  Grothendieck's inequality; Benyamini's appendix gives 4D/ε for any Banach
  target, through a retraction of ℓ∞(Γ) with Lipschitz constant at most 2.
  The bound trades the count of points for the spread of the set. Whether
  either constant is best possible is not discussed.
---

# THEORY-tmpub08y: A Lipschitz map from a subset of a metric space whose points are at least ε apart and whose diameter is D extends to the whole space into Hilbert space with Lipschitz constant at most 6D/ε times its own, and, by Benyamini's argument in the same paper, into any Banach space with at most 4D/ε, with no dependence on the number of points

## Source

Johnson and Lindenstrauss (1984), [LIT-tmp7skui](../literature.d/LIT-tmp7skui.md), Theorem 2 (p. 195) and
Benyamini's appendix (p. 205), read in [NOTE-tmpmv42v](../notes.d/NOTE-tmpmv42v.md). Filed for later use;
it answers no question of the record's yet.

## What was actually shown

**Theorem 2.** If A ⊂ X has d(x, y) ≥ ε > 0 for all x ≠ y in A and
diameter D, every Lipschitz f: A → ℓ₂ extends to f̃: X → ℓ₂ with
‖f̃‖_lip ≤ (6D/ε)‖f‖_lip. The proof factors the map through ℓ₁ on the
points of A and, by a weak form of Grothendieck's inequality, through ℓ∞
with ‖H‖ ≤ 3‖G‖.

**Benyamini's version.** The same holds with any Banach space Z in place
of ℓ₂, with ‖f̃‖_lip ≤ (4D/ε)‖f‖_lip. Lemma 6 gives a retraction of ℓ∞(Γ)
onto the positive part of the ℓ₁(Γ) ball with Lipschitz constant at most
2, and a map H into {αe_γ} with ‖H‖_lip ≤ 4.

**What could have come out otherwise.** A separated set and a map into
some Banach space with no extension of constant 4D/ε would refute the
appendix. Both proofs were read in the reading.

## What this does not say

- **That the constants are best possible.** The paper does not discuss
  it.
- **Anything for sets that are not separated.** As ε goes to 0 the bound
  is vacuous; the bound in n is [THEORY-tmp7nqd6](THEORY-tmp7nqd6.md)'s.
- **Anything about random projections.** Neither proof uses Lemma 1.

## Connections

- [THEORY-tmp7nqd6](THEORY-tmp7nqd6.md): the paper's bound in terms of the number of points.
  The two together say an extension constant can be paid for either by
  how many points there are or by how spread out they are.
