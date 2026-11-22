# LEAD-066: a commutator bound for level-by-level acquisition off exact symmetry

Run on 2026-11-22. numpy/scipy on CPU, BLAS threads 1; no downloads.

The reading half of the lead was already done: Nadler, Lafon, Coifman and
Kevrekidis (LIT-1250) is read in NOTE-986, and gives no bound of this kind
(its gap-to-cluster link is heuristic). NOTE-985 names the bound to attempt.
LEAD-052 (branch `claude/lead-052-acquisition-phases`, not yet on staging)
proved the exact case: on tree-symmetric data every kernel of inner
products and norms commutes with the level projectors, so kernel flow
acquires each level at its own rate μ_ℓ. This study bounds what happens
when the commutator is not zero.

## Setting and notation

- n items; P_0, …, P_L mutually orthogonal projectors on R^n with
  Σ P_ℓ = I (the levels: P_ℓ projects onto level ℓ's span, here the Haar
  vectors of a binary tree at depth ℓ); Q_ℓ = I − P_ℓ.
- A symmetric positive semidefinite: the learner's operator on the
  residual. For kernel gradient flow on the loss (1/2n)‖F − Y‖², A = K/n
  and the residual e = F − Y obeys ė = −A e. For a network trained by
  gradient flow on that loss, ė = −A_t e holds exactly with A_t = Θ_t/n,
  Θ_t the empirical tangent kernel on the items.
- η_ℓ = ‖[A, P_ℓ]‖ (spectral norm). D = Σ_ℓ P_ℓ A P_ℓ, the pinching of A to
  the levels: the same operator with every cross-level coupling deleted.
  A_ℓ = P_ℓ A P_ℓ restricted to ran P_ℓ, with extreme eigenvalues
  λ_ℓ ≤ Λ_ℓ. a = λ_min(A).
- Level risk, as in QUESTION-217 and LEAD-052 (the network's own output as
  decoder): r_ℓ(t) = ‖P_ℓ e(t)‖² / ‖P_ℓ e(0)‖², and the acquisition time
  T_ℓ(δ) = inf{t : r_ℓ(t) ≤ δ}.
- The comparison flow e^D: ė^D = −D e^D from the same start. It is
  level-decoupled: P_ℓ e^D(t) = exp(−A_ℓ t) P_ℓ e(0), so
  e^{−Λ_ℓ t} ≤ ‖P_ℓ e^D(t)‖/‖P_ℓ e(0)‖ ≤ e^{−λ_ℓ t}.

## Lemma 0 (what the commutator is)

[A, P] = QAP − PAQ, a block off-diagonal operator whose two blocks are
transposes, so ‖[A, P_ℓ]‖ = ‖P_ℓ A Q_ℓ‖: the commutator is exactly the
coupling between level ℓ and the rest. [A, P_ℓ] = 0 for every ℓ iff A = D.
Two consequences:

- ‖A − D‖ ≤ √(L+1) · max_ℓ η_ℓ (A − D = Σ_ℓ P_ℓ A Q_ℓ, a sum of operators
  with orthogonal ranges).
- If A₀ is any operator commuting with every P_ℓ (for instance the kernel
  of tree-symmetric data, LEAD-052), then [A, P_ℓ] = [A − A₀, P_ℓ] and
  η_ℓ ≤ ‖A − A₀‖. So the commutator is bounded by the distance of the
  operator from the nearest symmetric one.

## Theorem 1 (level-wise deviation, fixed operator)

For every t ≥ 0,

    ‖P_ℓ e(t) − P_ℓ e^D(t)‖ ≤ η_ℓ ‖e(0)‖ φ_ℓ(t),
    φ_ℓ(t) = (e^{−a t} − e^{−λ_ℓ t}) / (λ_ℓ − a)   (= t e^{−λ_ℓ t} if λ_ℓ = a),

and φ_ℓ(t) ≤ 1/λ_ℓ. Hence, writing s_ℓ = ‖P_ℓ e(0)‖/‖e(0)‖ for the level's
share of the initial residual (its share of the target, from zero output),

    | √r_ℓ(t) − ‖P_ℓ e^D(t)‖/‖P_ℓ e(0)‖ | ≤ ε_ℓ(t) := η_ℓ φ_ℓ(t) / s_ℓ
                                          ≤ ε_ℓ := η_ℓ / (λ_ℓ s_ℓ).

*Proof.* P_ℓ ė = −P_ℓ A (P_ℓ + Q_ℓ) e = −A_ℓ P_ℓ e − P_ℓ A Q_ℓ e. By
variation of constants on ran P_ℓ,
P_ℓ e(t) = e^{−A_ℓ t} P_ℓ e(0) − ∫₀^t e^{−A_ℓ (t−s)} P_ℓ A Q_ℓ e(s) ds,
and the first term is P_ℓ e^D(t). Bound the integrand by
‖e^{−A_ℓ τ}‖ ≤ e^{−λ_ℓ τ}, ‖P_ℓ A Q_ℓ‖ = η_ℓ (Lemma 0) and
‖Q_ℓ e(s)‖ ≤ ‖e(s)‖ ≤ e^{−a s}‖e(0)‖ (A ⪰ aI), and integrate. a ≤ λ_ℓ by
the Rayleigh quotient, so φ_ℓ ≤ ∫₀^t e^{−λ_ℓ(t−s)} ds ≤ 1/λ_ℓ. ∎

The bound is time-uniform: the deviation does not accumulate, because
level ℓ's own block damps what leaks in at rate λ_ℓ. It is sharp to first
order (Example 2 below): η_ℓ/λ_ℓ is attained when the start sits in a slow
level and leaks into a fast one.

## Corollary 2 (acquisition times and their order)

If ε_ℓ < √δ, then

    ln(1/(√δ + ε_ℓ)) / Λ_ℓ  ≤  T_ℓ(δ)  ≤  ln(1/(√δ − ε_ℓ)) / λ_ℓ,

(the lower bound holds for any ε_ℓ, read as 0 when √δ + ε_ℓ ≥ 1). So level ℓ
is acquired strictly before level m whenever

    ln(1/(√δ − ε_ℓ)) / λ_ℓ  <  ln(1/(√δ + ε_m)) / Λ_m.          (★)

With an exactly symmetric baseline A₀ = Σ μ_ℓ P_ℓ and A = A₀ + E
(‖E‖ = ε_op): η_ℓ ≤ ε_op, and by Weyl's inequality on the compressions
μ_ℓ − ε_op ≤ λ_ℓ ≤ Λ_ℓ ≤ μ_ℓ + ε_op. So every quantity in (★) is a function of
the symmetric rates μ, the perturbation size ε_op and the target shares
s_ℓ, and (★) holds for all small enough ε_op whenever μ_ℓ > μ_m: **the
symmetric order survives a perturbation of operator size**

    ε_op  ≲  min over ordered pairs of  (gap in rates) × (√δ s, δ-dependent factor),

explicitly whatever makes (★) true after the substitutions.

## Corollary 3 (data perturbation)

For the linear kernel, A = X Xᵀ/(n d). With X = X₀ + Δ and X₀ tree-symmetric,
‖E‖ ≤ (2‖X₀‖‖Δ‖ + ‖Δ‖²)/(n d). For a kernel k(x, y) = κ(⟨x,y⟩/d, ‖x‖²/d, ‖y‖²/d)
with κ L-Lipschitz in each argument on the range in play, each entry of
K − K₀ is at most L(|ΔG_ij| + |ΔG_ii| + |ΔG_jj|), G the Gram matrix over d,
so ‖E‖ ≤ ‖K − K₀‖_F/n ≤ L √(3(2n+1)) ‖G − G₀‖_F / n. A perturbation of the
data enters only through how far it moves the Gram matrix from a
tree-symmetric one; a perturbation that leaves G tree-symmetric (a common
rotation, say) leaves every commutator zero.

## Corollary 4 (the resolution limit of the order)

Theorem 1 says nothing once δ < ε_ℓ², and that is not slack. If A's
smallest eigenvalue a is simple, with eigenvector v, and ⟨v, e(0)⟩ ≠ 0,
then ‖P_ℓ e(t)‖ = |⟨v, e(0)⟩| ‖P_ℓ v‖ e^{−a t}(1 + o(1)) for every level with
P_ℓ v ≠ 0, so T_ℓ(δ) = ln(1/δ)/(2a) + O(1) and T_ℓ(δ)/T_m(δ) → 1 as δ → 0.
Under exact commutation v lies in one level, the other levels decay at
their own faster rates, and the order persists at every δ. Off commutation
v generically has a part in every level, and **every level's late residual
is the slowest mode's leakage: at fine enough δ all levels are acquired
together.** The commutator therefore sets a resolution, δ of order ε_ℓ²,
above which the level order is the symmetric one and below which it is
the slowest mode's.

## Theorem 5 (moving operator: Conjecture A's integral, made exact)

Let A_t be symmetric positive semidefinite and bounded, measurable in t,
ė = −A_t e, and e^D the flow under D_t = Σ P_ℓ A_t P_ℓ from the same
start. Then for every t,

    ‖P_ℓ e(t) − P_ℓ e^D(t)‖ ≤ ‖e(0)‖ ∫₀^t ‖[A_s, P_ℓ]‖ exp(−∫_s^t λ_ℓ(u) du) ds
                            ≤ ‖e(0)‖ ∫₀^t ‖[A_s, P_ℓ]‖ ds.

*Proof.* As in Theorem 1, with the propagator of A_ℓ(t) on ran P_ℓ, which
contracts at rate λ_ℓ(u) (d‖x‖²/dt = −2xᵀA_ℓx ≤ −2λ_ℓ‖x‖²), and
‖e(s)‖ ≤ ‖e(0)‖ (d‖e‖²/dt = −2eᵀA_t e ≤ 0). ∎

QUESTION-217 records A2's proposal of ∫‖[A_t, P_ℓ]‖ dt ≪ 1 as the measure
for a moving operator. Theorem 5 makes it a bound, pathwise: for a network
trained by gradient flow on squared loss, whatever its feature learning,
the level risks stay within ‖e(0)‖∫‖[Θ_s/n, P_ℓ]‖ds/‖P_ℓe(0)‖ of a flow in
which no level ever talks to another. The first form is sharper: a
commutator incurred early is forgotten at the level's own rate. What the
theorem does not give is the order of the decoupled flow itself, which
depends on how each block A_ℓ(t) moves; Corollary 2 needs fixed blocks or
bounds on λ_ℓ(t), Λ_ℓ(t).

For gradient descent with step h and h‖A_k‖ ≤ 1 the same argument gives

    ‖P_ℓ(e_K − e^D_K)‖ ≤ Σ_{k<K} ( h ‖[A_k, P_ℓ]‖ ‖e_k‖ + ‖P_ℓ ρ_k‖ ),

with ρ_k = e_{k+1} − (I − hA_k)e_k the step's departure from linearity.

## What it implies for the acquisition order

1. **Conjecture A holds, in the kernel regime and for any moving operator
   in the comparison form.** "If the learning operator nearly commutes with
   every P_ℓ and its effective eigenvalues fall as finer distinctions are
   added, acquisition is nearly coarse to fine, with deviations set by the
   cross-level coupling and the spectral gaps": Theorem 1 and (★) are that
   sentence with constants. The deviation in level ℓ is the commutator
   over the level's own slowest rate, divided by the level's share of the
   target.
2. **Target strengths re-enter through the mixing.** On exact symmetry the
   kernel order depends on the inputs alone (LEAD-052). Off symmetry,
   ε_ℓ ∝ 1/s_ℓ: a level carrying little of the target is the most easily
   reordered, at first order in the commutator.
3. **The order has a resolution.** Above δ ≈ ε², the symmetric order; below
   it, every level is acquired with the slowest mode (Corollary 4). A
   claim that acquisition is coarse-to-fine must say at what δ.
4. **What breaks the order is the operator's distance from the symmetric
   one, measured against the rate gaps,** not the data's distance as such
   (Corollary 3).

## Files and how to rerun

(Filled in as the computations land; see PROGRESS.md.)
