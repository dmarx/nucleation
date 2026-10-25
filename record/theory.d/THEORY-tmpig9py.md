---
status: Active
title: 'In the normal linear model with known error variance and a conjugate normal prior of precision R/σ², the design that maximizes the expected Shannon information of the posterior is the one maximizing det(nM(η) + R), Bayes D-optimality, and the design that minimizes expected quadratic loss with weight matrix A is the one minimizing tr A(nM(η) + R)^-1, Bayes A-optimality; both criteria depend on the design and not on the data, so in this model a sequential design gains nothing over the best fixed one'
version: 1
history:
- version: 1
  date: '2026-10-25'
  note: >-
    Filed Active from NOTE-tmpj2iwk. The reductions are Chaloner and
    Verdinelli's §2.2 (after Lindley, Stone, DeGroot and Bernardo), and
    the remark on sequential design is their §5.5. The displayed formulas
    were lost in the extraction of the technical report, so all three are
    re-derived below step by step, which meets the condition for Active
    under ADR-047 v2.
tags:
- mathematical-statistics
- probabilistic-modeling
date: '2026-10-25'
source:
- LIT-tmpi60b0
summary: >-
  Chaloner and Verdinelli (1995), LIT-tmpi60b0, read in NOTE-tmpj2iwk. The
  alphabetical criteria are utilities in disguise, and the utility fixes
  the criterion. This holds exactly only in the normal linear model with
  known variance. With unknown variance only Bayes A keeps its simple form,
  and in nonlinear models the criteria are approximations
  (THEORY-tmpg6jfa). E- and G-optimality have no utility behind them.
---
# THEORY-tmpig9py: In the normal linear model with known error variance and a conjugate normal prior of precision R/σ², the design that maximizes the expected Shannon information of the posterior is the one maximizing det(nM(η) + R), Bayes D-optimality, and the design that minimizes expected quadratic loss with weight matrix A is the one minimizing tr A(nM(η) + R)^-1, Bayes A-optimality; both criteria depend on the design and not on the data, so in this model a sequential design gains nothing over the best fixed one

## Source

Chaloner and Verdinelli (1995), *Statistical Science* 10(3):273–304,
LIT-tmpi60b0, §§2.1–2.2 and §5.5. Read in NOTE-tmpj2iwk from the authors'
technical report. The derivations below are the record's, written because
the report's displays did not survive extraction.

## What was actually shown

Model: y | θ ~ N(Xθ, σ²I_n), σ² known, θ ∈ ℝ^k, and prior θ ~ N(θ₀, σ²R⁻¹).
A design η puts proportion η_i of the n observations at x_i, so
XᵀX = nM(η) = n Σ η_i x_i x_iᵀ.

**The posterior.** By conjugacy, θ | y ~ N(θ*, σ²D(η)) with
D(η) = (nM(η) + R)⁻¹ and θ* = D(η)(Xᵀy + Rθ₀). The posterior covariance
does not involve y.

**Shannon information.** The prior does not depend on η, so maximizing the
expected Kullback–Leibler divergence from prior to posterior is maximizing
U₁(η) = E[log p(θ | y, η)], the expectation over θ and y jointly. For a
k-variate normal density with covariance Σ, E[log p] = −½ k log(2πe) − ½
log det Σ. Here Σ = σ²D(η) for every y, so
U₁(η) = −½ k log(2πeσ²) + ½ log det(nM(η) + R). The design maximizing U₁
maximizes det(nM(η) + R).

**Quadratic loss.** For loss (θ − θ̂)ᵀA(θ − θ̂) with A ⪰ 0, the Bayes
estimate is the posterior mean, and the posterior expected loss is
tr(A Cov(θ | y)) = σ² tr(A D(η)), again for every y. So the expected
utility is U₂(η) = −σ² tr{A(nM(η) + R)⁻¹}. A = ccᵀ gives Bayes
c-optimality, −σ² cᵀD(η)c.

**No gain from sequencing.** Let n be fixed and let a sequential rule
choose each x_t from the data so far. Whatever it does, the realized design
η̂ is some measure in ℋ. The posterior utility given all the data is, up
to constants, ½ log det(nM(η̂) + R) or −σ² tr AD(η̂), a function of η̂
alone. Its expectation is therefore at most max_η U(η), which a fixed
design attains.

**The prior's weight.** D(η) = n⁻¹(M(η) + n⁻¹R)⁻¹. As n grows or R shrinks
the Bayesian criteria approach the non-Bayesian det M and tr AM⁻¹. A proper
prior keeps nM + R invertible when nM is singular, so a design need not
identify every parameter from data alone.

What could have failed: the utility could have depended on the data through
the posterior, in which case a design criterion would need an average over
y and would depend on θ₀. In this model the posterior covariance is free of
y, which is why D, A and c-optimality are exact here and approximations
elsewhere.

## What this does not say

- **Not for unknown variance.** With a normal–inverse-gamma prior the
  Shannon and predictive utilities have no closed form (§2.5). Bayes A
  reduces to tr(nM + R)⁻¹ times a constant independent of y, and is
  "insensitive to the knowledge of σ²".
- **Not for nonlinear models**, where the information matrix depends on θ
  and the criteria are approximations (THEORY-tmpg6jfa).
- **Not for E- or G-optimality**, which "appear not to correspond to any
  utility function".
- **Not that the criteria agree.** D, A and c generally select different
  designs. The purpose of the experiment selects among them.

## Connections

- **QUESTION-031.** The note of 2026-10-25 uses log det G_ξ with
  G_ξ = Σ_c ξ(c)G_c. In a linear Gaussian probe model that is exactly U₁
  up to constants. A29's preference for a criterion that targets one
  contrast is c- or Ds-optimality.
- **CASE-152.** Its intervention do(b = b₀) gives G_aa = b₀². In a linear
  model, adding that observation adds b₀² to the information about a,
  which raises all three criteria.
- **CASE-tmplg5jg** is not linear in this sense. Its information depends on
  the share being estimated (THEORY-tmpg6jfa).
