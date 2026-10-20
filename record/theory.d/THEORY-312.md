---
number: 312
status: Active
formerly:
- THEORY-tmpijp65
title: 'The large-batch InfoNCE loss is the negative HSIC between representations and image identity plus a nonnegative log-mean-exp of the centred critic, so it bounds a kernel dependence loss from above'
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Promoted from Proposed to Active at the owner's direction, carrying out
    the promotion audit's decision (record/promotion-audit/decisions/THEORY-312.yaml,
    batch 014). The promote_when asked for a second, independent derivation
    of eq. 28 and Theorem B.1 that settles the sign of the remainder. It is
    met by a step-by-step re-derivation, written out below and in the
    decision file, under the owner's rule of 2026-10-19 (ADR-047): a checked
    re-derivation recorded in the decision file meets a promote_when that
    asks for a proof the record does not hold. The sign is plus, as the
    THEORY already said. The promote_when is removed. The claim is
    unchanged.
tags:
- representation-learning
- mathematics
date: '2026-10-14'
source:
- LIT-248
summary: >-
  Li, Pogodin, Sutherland & Gretton (2021), [LIT-248](../literature.d/LIT-248.md), eq. 28 and Theorem
  B.1, read in [NOTE-830](../notes.d/NOTE-830.md). On a finite dataset of N images with one-hot
  identity labels, the large-batch InfoNCE loss equals −HSIC(Z,Y) +
  E_Z log E_Z′ exp(k − μ₁) exactly. The second term is nonnegative by
  Jensen (the record's step), and for a bounded kernel it is at least
  γHSIC(Z,Z) less a second-order remainder (Theorem B.1, printed with the
  remainder's sign reversed). It does not say InfoNCE is HSIC, and it says
  nothing of the finite-batch estimator.
---
<!-- inactive-ok-file: THEORY-001 THEORY-227 — Proposed; the MMD reading of the same HSIC term, and the accounts of InfoNCE's optimum and of mutual information it is set beside -->

# THEORY-312: The large-batch InfoNCE loss is the negative HSIC between representations and image identity plus a nonnegative log-mean-exp of the centred critic, so it bounds a kernel dependence loss from above

## Source

Li, Pogodin, Sutherland & Gretton (2021), [LIT-248](../literature.d/LIT-248.md), read in [NOTE-830](../notes.d/NOTE-830.md):
Theorem A.1 (eq. 14), App. B.1 (eqs. 27–28, Lemma B.0.1, Theorem B.1),
and the main-text eqs. 6–8.

## What was actually shown

The setting is N images, each with probability 1/N, and Y the one-hot
identity. The label kernel has the form l = Δl·1[y = y′] + l₀ with
Δl = N. Positive pairs are two views of one image drawn independently
given the image. The critic k(z,z′) is read as a kernel on the
representation. InfoNCE is taken in its large-batch form,
L_InfoNCE = E_Z log E_Z′ exp k(Z,Z′) − E_(Z,Z′∼pos) k(Z,Z′) (eq. 27).

1. **HSIC in closed form (Theorem A.1, proved).** HSIC(Z,Y) =
   E_pos k(Z,Z′) − E_Z E_Z′ k(Z,Z′).
2. **Exact decomposition (eq. 28).** With μ₁(Z) := E_Z′ k(Z,Z′),
   L_InfoNCE = −HSIC(Z,Y) + E_Z log E_Z′ exp(k(Z,Z′) − μ₁(Z)). This is
   algebra. It needs no smallness and holds for any integrable critic. It
   reads as HSIC when k is positive definite, as the dot product and the
   scaled cosine are.
3. **Nonnegativity (the record's step).** By Jensen,
   E_Z′ exp(k − μ₁) ≥ exp E_Z′(k − μ₁) = 1. So the log-mean-exp term is
   ≥ 0 and −HSIC(Z,Y) ≤ L_InfoNCE exactly. Equality holds iff k(Z,·) is
   a.s. constant in Z′, which is a critic that sees nothing.
4. **A variance-penalized bound (Theorem B.1, proved).**
   - If |k| ≤ k_max and γ ∈ (0, 1/4] solves min{−2, −2k_max} =
     −(1 + √(1 − 4γ))/(2γ), Lemma B.0.1 gives
     exp(x) ≥ 1 + x + γx² on the range of k − μ₁.
   - That gives E_Z log E_Z′ exp(k − μ₁) ≥ E_Z log(1 + γV), with
     V = Var_Z′ k(Z,Z′). With HSIC(Z,Z) ≤ E_Z V, this yields
     −HSIC(Z,Y) + γHSIC(Z,Z) ≤ L_InfoNCE + E_Z[(γV)²/(1 + γV)].
   - The paper prints the remainder with a minus sign. Its own inequality,
     log(1 + x) ≥ x − x²/(1 + x), gives the plus. Main-text eq. 8 ("+
     o(variance)") agrees with the plus.
   - For the cosine critic at temperature τ = 0.1, k_max = 10 and
     γ = 0.0475.
5. **The Taylor form (eq. 7), approximate.** L_InfoNCE ≈ −HSIC(Z,Y) +
   ½E_Z Var_Z′ k(Z,Z′) when k stays near μ₁.

What could have come out otherwise: step 2 is exact, so the only claim at
risk is the direction and size of the remainder in step 4. The record's
rederivation and the paper's eq. 8 agree on the plus sign.

## What this does not say

- **Not that InfoNCE is HSIC, or SSL-HSIC.** The log-mean-exp term is a
  regularizer of its own. The penalty in Theorem B.1 is γHSIC(Z,Z) with a
  small γ, not SSL-HSIC's γ√HSIC(Z,Z), and the paper says the two losses
  "in general don't quite bound each other" (§3.1).
- **Nothing about the finite-batch estimator.** The bound is for the
  large-batch form, from which log K has already been subtracted. The
  K-negative estimator, and its log K ceiling ([THEORY-006](THEORY-006.md)), are not
  analysed. Whether a finite-K version of eq. 28 holds is open.
- **Not that InfoNCE "works because" it estimates kernel dependence.**
  That is the authors' interpretation. The identity holds for every
  encoder, good or bad, so it cannot by itself explain why trained
  representations are good. No experiment in the paper isolates the HSIC
  term from the log-mean-exp term.
- **Nothing outside identity labels.** The closed form for HSIC(Z,Y) uses
  the one-hot structure and equal image probabilities.
- **Not a mutual-information statement.** The account sits beside
  [THEORY-006](THEORY-006.md) and [THEORY-237](THEORY-237.md), which read the same loss as a bound on mutual
  information. It does not contradict them. The same loss can be read
  both ways, and neither reading excludes the other.

## Connections

- **[THEORY-003](THEORY-003.md).** It holds the MMD reading of the same HSIC(Z,Y) term:
  (1/2N²)Σ_ij MMD²(i,j) = (N/Δl)·HSIC(Z,Y). Together, the two say that
  the large-batch InfoNCE loss is bounded below by minus the mean squared
  distance between per-image mean embeddings, up to the constant.
- **[THEORY-006](THEORY-006.md) and [THEORY-237](THEORY-237.md).** The mutual-information reading of
  InfoNCE. [THEORY-227](THEORY-227.md)'s point that mutual information does not fix quality
  is the motivation Li et al. give for the kernel reading (their Figure 3).
- **[THEORY-001](THEORY-001.md).** It holds that InfoNCE's population optimum on a finite
  augmentation space is the positive-pair density ratio. This account
  concerns the loss's value at every encoder, not its optimum.

## Note of 2026-10-19: eq. 28 and Theorem B.1, re-derived

Written for the promotion audit (batch 014). The full version is in
record/promotion-audit/decisions/THEORY-312.yaml.

- **Theorem A.1.** With l = N·1[y = y′] + l₀, the constant l₀ adds
  nothing to HSIC. P(Y = Y′) = 1/N, and given Y = Y′, (Z, Z′) is a
  positive pair. So the three terms of HSIC are (1/N)E_pos k,
  (1/N)E_Z E_Z′ k and (1/N)E_Z E_Z′ k, and HSIC(Z,Y) = E_pos k − E_Z E_Z′ k.
- **Eq. 28.** log E_Z′ exp k = μ₁(Z) + log E_Z′ exp(k − μ₁(Z)). Taking E_Z
  and subtracting E_pos k gives the decomposition exactly.
- **Lemma B.0.1.** For γ ∈ (0, 1/4], 1 + x + γx² has roots
  x_min = −(1 + √(1 − 4γ))/(2γ) and r = −2/(1 + √(1 − 4γ)) ∈ [−2, −1].
  - On [x_min, r] the quadratic is ≤ 0 < eˣ.
  - On [r, 0] it is at most (1 + x/2)² ≤ eˣ, since 0 ≤ 1 + x/2 ≤ e^(x/2).
  - On [0, ∞), eˣ ≥ 1 + x + x²/2.
  So eˣ ≥ 1 + x + γx² on [x_min, ∞), which contains the range of k − μ₁
  when x_min ≤ −2k_max. With k_max = 10, x_min = −20 gives γ = 0.0475.
- **Theorem B.1.**
  - Averaging the lemma gives E_Z′ exp(k − μ₁) ≥ 1 + γV.
  - By log(1 + x) ≥ x/(1 + x) = x − x²/(1 + x), E_Z log(1 + γV) ≥
    γE_Z V − E_Z[(γV)²/(1 + γV)].
  - E_Z V − HSIC(Z,Z) = Var μ₁(Z) ≥ 0.
  - So −HSIC(Z,Y) + γHSIC(Z,Z) ≤ L_InfoNCE + E_Z[(γV)²/(1 + γV)].
  The remainder enters with a plus sign. The printed minus would be a
  stronger claim, and this derivation does not give it.
