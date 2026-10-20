---
number: 819
status: Active
formerly:
- THEORY-tmpgukcy
title: 'For an invertible map with an invariant measure, projecting onto the closed span of the whole past of chosen functions of the resolved variables (a Wiener projection) turns the exact discrete Mori–Zwanzig equation into one with no memory term: the next resolved value is a causal linear filter of those past functions plus a residual orthogonal to all of them, so the memory is carried by the coarse variable''s own history; a finite NARMAX form follows only by a rational approximation of the filter, uncontrolled in general but exact for a scalar coarse variable of a stable linear Gaussian VAR(1)'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Filed Active from NOTE-1029. The Dyson formula, the discrete
    Mori–Zwanzig equation, the collapse under the Wiener projection and the
    orthogonality of the residual are the paper's §§2.2 and 3.1, re-derived
    below step by step, which meets the condition for Active under ADR-047
    v2. The exactness of the rational form in the linear Gaussian VAR(1)
    class is the record's, derived below from CLAIM-398 and checked
    numerically. The paper's own step to NARMAX is not claimed: it is
    heuristic.
tags:
- mathematics
- probabilistic-modeling
- complex-systems
date: '2026-10-20'
source:
- LIT-1307
answers:
- QUESTION-222
summary: >-
  Lin and Lu (2021), [LIT-1307](../literature.d/LIT-1307.md), read in [NOTE-1029](../notes.d/NOTE-1029.md). Mori–Zwanzig's
  memory is what a projection onto the present leaves out; a projection
  onto the whole past absorbs it, leaving the causal Wiener filter on the
  coarse variable's own history and a residual orthogonal to all of that
  history. Second-order (linear-span) projections, invertible dynamics and
  stationarity only. It gives no finite augmentation with a bounded error
  in general: the NARMAX step is the paper's uncontrolled approximation,
  exact only in the linear Gaussian class shown here.
supports:
- CLAIM-397
---
<!-- inactive-ok-file: THEORY-257 THEORY-818 — Proposed; the criterion whose conditioning set this matches, and the Lorenz 96 finding beside which the paper's examples sit, nothing here rests on their being settled -->
<!-- inactive-ok-file: NOTE-1029 LIT-1307 — new reading, filed together -->

# THEORY-819: For an invertible map with an invariant measure, projecting onto the closed span of the whole past of chosen functions of the resolved variables (a Wiener projection) turns the exact discrete Mori–Zwanzig equation into one with no memory term: the next resolved value is a causal linear filter of those past functions plus a residual orthogonal to all of them, so the memory is carried by the coarse variable's own history; a finite NARMAX form follows only by a rational approximation of the filter, uncontrolled in general but exact for a scalar coarse variable of a stable linear Gaussian VAR(1)

## Source

Lin and Lu (2021), *Journal of Computational Physics* 424:109864,
[LIT-1307](../literature.d/LIT-1307.md), read in full in [NOTE-1029](../notes.d/NOTE-1029.md) from arXiv v5. Steps 1–5 are
the paper's Eqs. 2.2–2.6 and 3.3–3.10, re-derived here. Step 6 is the
record's.

## What was actually shown

Let X_{n+1} = F(X_n) with F invertible and μ an F-invariant probability
measure, X₀ ~ μ. Let H = L²(μ) and Mφ = φ∘F (the Koopman operator),
x = π(X) ∈ ℝᵈ the resolved variables, and Ψ(x) = [ψ₁(x) … ψ_ν(x)] chosen
observables.

**Step 1: the Dyson formula.** For any linear operator P with Q = I − P,
M^{n+1} = Σ_{k=0}^{n} M^{n−k}PM(QM)^k + (QM)^{n+1}.
For n = 0 this is M = PM + QM. If it holds for n, multiply on the left by
M. The sum's terms become M^{n+1−k}PM(QM)^k, and the remainder becomes
M(QM)^{n+1} = PM(QM)^{n+1} + (QM)^{n+2}. Its first part is the k = n + 1
term of the sum for n + 1, and its second part is the new remainder.

**Step 2: the discrete MZ equation.** Let P be a projection (PQ = 0) whose
range consists of functions of x. Apply Step 1 to π and evaluate at X₀.
(M^{n+1}π)(X₀) = x_{n+1}, and (M^{n−k}g)(X₀) = g(X_{n−k}). Put
ξ_k = (QM)^kπ, so M(QM)^kπ = ξ_k∘F, and P(ξ_k∘F) is a function Γ_k of x.
Then
x_{n+1} = PF(x_n) + Σ_{k=1}^{n} Γ_k(x_{n−k}) + ξ_{n+1}(X₀),
with Pξ_k = PQ(Mξ_{k−1}) = 0 for k ≥ 1. With P the orthogonal projection
onto span(Ψ), ξ_n is orthogonal to Ψ(x₀) only.

**Step 3: M is unitary.** ⟨Mu, Mv⟩ = ∫(u∘F)(v∘F)dμ = ∫uv dμ by
invariance, so M is an isometry. It is onto because F is invertible
(u = (u∘F⁻¹)∘F), so M⁻¹ = M*.

**Step 4: the collapse.** Let W be the closed span of
{M^{−k}ψ_i : k ≥ 0, i ≤ ν}. M^{−k}ψ_i = ψ_i∘F^{−k}, so W is spanned by
the observables at every past time. M⁻¹ maps the spanning set into
itself and is bounded, so M⁻¹W ⊆ W, i.e. Q_W M⁻¹P_W = 0. Taking adjoints,
with (M⁻¹)* = M: P_W M Q_W = 0. Then for k ≥ 1,
P_W M(Q_W M)^k = (P_W M Q_W)M(Q_W M)^{k−1} = 0, and Step 1 reduces to
M^{n+1} = MⁿP_W M + (Q_W M)^{n+1}.
Applied to π at X₀:
x_{n+1} = (P_W(π∘F))(X_n) + ξ_{n+1}(X₀).
The first term is an element of W composed with Fⁿ: a limit of finite
combinations Σ_k Ψ(x_{n−k})·h_k. When it is a convergent series, this is
the paper's Eq. 3.6a. There is no memory term, because the past is
inside the projection.

**Step 5: the residual is orthogonal to the whole past.**
P_W M Q_W = 0 means M maps W⊥ into W⊥, so MQ_W = Q_W M Q_W. Hence
(Q_W M)² = (Q_W M Q_W)M = MQ_W M, and by induction (Q_W M)^{n+1} = MⁿQ_W M.
So ξ_{n+1} = ξ₁∘Fⁿ with ξ₁ = Q_W(π∘F) ∈ W⊥. For m ≤ n, by unitarity,
⟨ξ_{n+1}, ψ_i∘F^m⟩ = ⟨ξ₁, ψ_i∘F^{m−n}⟩ = 0, since ψ_i∘F^{−(n−m)} ∈ W.
The residual at n + 1 is orthogonal to Ψ(x_m) for every m ≤ n, past
the initial time included. ⟨ξ_m, ξ_n⟩ and ⟨ξ_m, Ψ(x_n)⟩ depend only on
m − n. That orthogonality is the normal equation of the causal Wiener
filter: the first term is the minimum mean-square linear prediction of
x_{n+1} from the entire past of Ψ.

Checked numerically ([NOTE-1029](../notes.d/NOTE-1029.md)). The Dyson formula held to 3 × 10⁻¹⁶
on random 12 × 12 matrices. For an orthogonal M with a 7-dimensional
M⁻¹-invariant W, P_W M Q_W was 1 × 10⁻¹⁵ and the collapsed formula held
to 3 × 10⁻¹⁵. For a non-normal M with an M⁻¹-invariant W,
P_W M Q_W = 1.58 and the collapsed formula failed by 2.8, so unitarity is
doing real work.

**Step 6: the rational form is exact in the linear Gaussian VAR(1)
class (the record's).** Take X_{t+1} = AX_t + ε_t, A stable, ε Gaussian
white with Σ ≻ 0, as a skew product (Step 3 then applies), with scalar
Y = LX and Ψ(y) = y.

1. By [CLAIM-398](../claims.d/CLAIM-398.md), φ(B)Y = u with φ(w) = det(I − Aw) and u an MA of
   order at most n − 1.
2. On the unit circle Y's spectral density is
   L(I − Ae^{−iω})⁻¹Σ(I − Ae^{−iω})^{−*}Lᵀ ≥ λ_min(Σ)‖L(I − Ae^{−iω})⁻¹‖²,
   and this is positive. So u's spectrum |φ|²S_Y is a positive
   trigonometric polynomial. By Fejér–Riesz, u = θ(B)e, with θ(0) = 1,
   deg θ ≤ n − 1, every root of θ strictly outside the unit disk, and e
   white.
3. Y = (θ/φ)(B)e is causal, and e = (φ/θ)(B)Y has geometrically decaying
   coefficients. So the closed span of Y's past equals that of e's past,
   and e_{t+1} is orthogonal to it.
4. Hence Y_{t+1} = [1 − φ(B)/θ(B)]Y_{t+1} + e_{t+1}, and the first term
   lies in the span of the past. It is therefore the Wiener projection,
   and e is the residual of Step 5.
5. Since θ(0) = φ(0) = 1, 1 − φ/θ = w·b(w)/θ(w) with deg b ≤ n − 1. The
   filter's generating function Σ_k h_k w^k is b(w)/θ(w): exactly the
   paper's B/A, with both degrees at most n − 1.
6. Its poles are the reciprocals of θ's roots, inside the unit circle. So
   the paper's decaying-memory condition holds, and h_k decays at the
   largest uncancelled MA zero.

Checked: h from a 300-lag Toeplitz solve agreed with the series of
b/θ to 1 × 10⁻¹⁶ – 3 × 10⁻¹³ in four models (random n = 3 and n = 4,
[QUESTION-222](../questions.d/QUESTION-222.md)'s example sampled at h = 0.1, [CLAIM-389](../claims.d/CLAIM-389.md)'s counterexample),
and the residual variance equalled the innovation variance (1.139424,
13.605055, 0.097536, 0.750000). In [QUESTION-222](../questions.d/QUESTION-222.md)'s example h₀ = 0.97628
and h_k falls by 0.90088 per lag, the MA zero.

**What the paper could have shown otherwise.** With a non-unitary M, or
with W not invariant under M⁻¹ (a window of the past rather than all
of it), P_W M Q_W ≠ 0 and the memory terms return. Step 4's numerical
counterexample shows the first.

## What this does not say

- **Not a finite augmentation with controlled error, in general.** The
  exact reduced equation uses the entire past. The paper's NARMAX is a
  rational approximation it calls "uncontrolled" and "heuristic". It
  bounds no error, proves no convergence in the orders, and chose its KS
  and Burgers orders by trial. Only in the linear Gaussian class of
  Step 6 is the finite form exact.
- **Not that memory is removed.** It is moved into the projection. The
  Mori kernels (projection onto the present) and the Wiener filter
  (projection onto the past) of the same process differ, as A3 cautioned.
  In the linear class they share the numerator det(I − Aw) and differ in
  the denominator, det(I − K₂₂w) against θ(w) ([NOTE-1029](../notes.d/NOTE-1029.md)).
- **Not independence.** The projections are onto linear spans, so the
  residual is uncorrelated with every past Ψ, not independent of the past.
  With conditional expectation in place of the linear projection, the
  paper's footnote states, and it is immediate, that the residuals are
  martingale differences. Nothing here says that is enough for a
  white-noise NARMAX.
- **Not that a convergent series always exists.** Step 4 gives an element
  of a closed span. The paper's property (i) asserts coefficients h_k,
  unique under linear independence, which needs more than it states.
  Step 6 supplies the series in the linear class.
- **Not that this is a mark of a level.** Every stationary coarse
  variable has such an own-history representation in second order. What
  [THEORY-257](THEORY-257.md) tests is whether the micro past predicts the residual.
- **Nothing for non-invertible maps or non-stationary data.** The paper
  keeps both assumptions, and the collapse fails without unitarity.

## Connections

- [QUESTION-222](../questions.d/QUESTION-222.md): answers the "exact" half, an exact reduced equation built
  from the coarse variable's own history. It leaves open the "finite,
  with controlled error" half outside linear classes.
- [CLAIM-398](../claims.d/CLAIM-398.md): the ARMA state of that claim is a finite realization of
  this Wiener filter. Step 6 identifies the filter's poles with the MA
  zeros. That is why [NOTE-1028](../notes.d/NOTE-1028.md) found the lag-truncation error falling
  at θ² per lag.
- [CLAIM-389](../claims.d/CLAIM-389.md): its kernels M_j are the paper's Γ_k for the finite-rank
  projection. [NOTE-1029](../notes.d/NOTE-1029.md) shows that they, like the Wiener filter, are
  fixed by Y's autocovariance alone.
- [THEORY-257](THEORY-257.md): the Wiener projection conditions on exactly the coarse
  variable's own past. In the linear Gaussian case the Wiener residual
  variance is the numerator of the transfer entropy (0.75 in [CLAIM-389](../claims.d/CLAIM-389.md)'s
  counterexample).
- [LIT-1304](../literature.d/LIT-1304.md) and [THEORY-818](THEORY-818.md): Chorin and Lu's NARMAX, which this
  paper reinterprets as an approximate Wiener projection, with the
  Mori–Zwanzig link now stated exactly rather than by analogy.
- [NOTE-989](../notes.d/NOTE-989.md) and [NOTE-975](../notes.d/NOTE-975.md): the continuous-time MZ readings. There the noise
  is orthogonal to the present resolved variables only, which is the
  finite-rank case of Step 2.
