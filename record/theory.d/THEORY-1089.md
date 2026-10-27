---
number: 1089
status: Active
formerly:
- THEORY-tmpugh7c
title: 'In a passive linear network, eliminating interior nodes by the principle of minimum power, which over a general field with positive elements is stationarity, takes a Dirichlet form to a Dirichlet form on the remaining nodes, linearly in their values; eliminating one node s adds c_is·c_js/Σ_k c_ks to each coupling c_ij, so two resistors in series act at their ends as one of resistance r_AB + r_BC; composing Dirichlet forms by this elimination is associative but lacks identities, because an ideal wire of zero impedance has no power functional'
version: 1
tags:
- mathematics
- compositionality
date: '2026-10-27'
source:
- LIT-1644
summary: >-
  Baez and Fong (arXiv 2015, TAC 2018), [LIT-1644](../literature.d/LIT-1644.md), read in [NOTE-1223](../notes.d/NOTE-1223.md):
  Thm 3.3, Lemma 3.4, Example 2.9 and Sec. 3.3. The elimination is what is
  usually called Kron reduction, a name the paper does not use. Over ℝ(s),
  with inductors and capacitors, the "minimum" is a formal stationarity
  condition, Kirchhoff's current law at interior nodes. The absence of
  identities is computed for a one-element set and asserted as typical
  otherwise.
---

# THEORY-1089: In a passive linear network, eliminating interior nodes by the principle of minimum power, which over a general field with positive elements is stationarity, takes a Dirichlet form to a Dirichlet form on the remaining nodes, linearly in their values; eliminating one node s adds c_is·c_js/Σ_k c_ks to each coupling c_ij, so two resistors in series act at their ends as one of resistance r_AB + r_BC; composing Dirichlet forms by this elimination is associative but lacks identities, because an ideal wire of zero impedance has no power functional

## Source

Baez and Fong, [LIT-1644](../literature.d/LIT-1644.md) (arXiv 1504.05625v6), Sections 2–3, pp. 9–23;
read in [NOTE-1223](../notes.d/NOTE-1223.md).

## What was actually shown

**The setting.** A Dirichlet form on a finite set S is
Q(ψ) = Σ_{i,j∈S} c_ij(ψ_i − ψ_j)² with nonnegative c_ij (Def. 2.11, p. 15),
over a field with positive elements (Def. 2.10). A circuit's extended power
functional P(φ) = ½ Σ_e (1/Z(e))(φ(t(e)) − φ(s(e)))² is one. The principle of
minimum power for a boundary value ψ ∈ F^R asks that ∂P/∂φ(n) = 0 at every
n ∉ R (p. 18). Over ℝ this is a minimum. Over ℝ(s) it is a formal variational
principle: "it is not clear what it means to minimize over the field F"
(p. 18). Either way it is Kirchhoff's current law at the interior nodes
(Prop. 2.5, Thm 3.5).

**Thm 3.3 (p. 18).** A solution exists; all solutions give the same P; they
differ by constants on connected components; there is a unique one f(ψ)
vanishing on components that miss R; it is linear in ψ; and "the power
functional Q : F^R → F given by Q(ψ) = P(f(ψ)) is a Dirichlet form on R."
Existence is proved from nonnegativity: if im Bᵀ ⊄ im A, P could be made −1
(p. 19).

**Lemma 3.4 (pp. 21–22).** Eliminating one node s sets
φ_s = Σ_k c_ks φ_k / Σ_k c_ks and gives
min_{s} P(ψ) = Σ_{i,j} (c_ij + c_is c_js / Σ_k c_ks)(ψ_i − ψ_j)²
(reconstructed from the extraction). The interior value is a weighted average
of its neighbours, and the new coupling c_is c_js / Σ_k c_ks between i and j
exists whether or not i and j were joined.

**Example 2.9 (pp. 14–15).** For A —r_AB— B —r_BC— C, the minimizing
interior potential is x = (r_BC ψ(A) + r_AB ψ(C))/(r_BC + r_AB) and
Q(ψ) = ½ · (1/(r_AB + r_BC)) · (ψ(A) − ψ(C))², the power functional of one
resistor r_AB + r_BC. With conductances k = 1/r this is ½ · k₁k₂/(k₁ + k₂) ·
(ψ(A) − ψ(C))², [CLAIM-480](../claims.d/CLAIM-480.md)'s computation in the paper's variables.

**Composition and its gap (Sec. 3.3, p. 23).** Dirichlet forms on S + T and
T + U compose by (P ∘ Q)(α, γ) = min_T Q(α, β) + P(β, γ). By Thm 3.3 the result
is a Dirichlet form, and composition is associative. For a one-element S, an
identity k(β − γ)² would need c = kc/(k + c) for every c, which "only holds
when c = 0". Large k gives "'approximate identities'", but the ideal wire's
power functional "involves division by zero" (p. 23). Prop. 3.6: Dirichlet
forms form a semicategory. That gap is why the paper's black box lands in
Lagrangian relations ([THEORY-1063](THEORY-1063.md)).

## What this does not say

- **Not a statement about energy at mechanical equilibrium.** The paper's form
  is half the power a resistor network dissipates, minimized at fixed terminal
  potentials. The algebra of Thm 3.3 and Lemma 3.4 holds for any Dirichlet
  form, so it covers a chain of springs at static equilibrium too, but the
  paper does not discuss springs.
- **Not that the elimination is a minimization in the dynamic case.** Over
  ℝ(s) it is stationarity, and the reduced form is a frequency-dependent
  impedance, exact at every frequency with no time-scale separation assumed.
  Zero initial conditions are assumed (p. 16).
- **Not that the reduced form is new information.** It is fixed by the
  parts' coefficients. Prop. 2.12 adds that every real Dirichlet form on ∂N
  is some resistor circuit's power functional, so the map from circuits to
  forms is many-to-one and onto; its proof is a citation to the star-mesh
  transform.
- **Not that no Dirichlet form is an identity for every S.** The computation
  is for one element; for larger sets the paper says "typically" (p. 23).
- **Not named Kron reduction or Schur complement in the paper.** The
  identification is standard but the record's, not the authors'.
