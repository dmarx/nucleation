---
number: 744
status: Active
formerly:
- THEORY-tmp3j6t7
title: 'As the kernel width ε goes to 0, Coifman and Lafon''s α-normalized diffusion operator (I − P_{ε,α})/ε, for data sampled with density q = e^{−U} from a compact manifold without boundary, converges uniformly on smooth functions, at rate O(ε), to Δf + 2(1 − α)⟨∇U, ∇f⟩ with Δ the non-negative Laplace–Beltrami operator, which is minus the generator of a reversible diffusion with drift −2(1 − α)∇U and invariant density proportional to q^{2(1−α)}; α = 0 gives potential 2U and invariant density q², α = 1/2 gives the Langevin dynamics whose invariant density is the sampling density itself, and α = 1 gives Brownian motion on the manifold, with no trace of the density'
version: 2
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Filed Proposed from NOTE-985. The limit is the source's Theorem 2
    (proved there as Proposition 10). The drift form and the invariant
    density are the record's rewriting, derived below. The interior
    algebra (B.4)–(B.10) is re-derived here from the source's Lemma 8,
    which was read and not re-derived. The boundary remainder and the
    semigroup step (Proposition 11) have gaps, listed below, so the
    THEORY is not Active.
- version: 2
  date: '2026-10-20'
  note: >-
    Narrowed and promoted, carrying out the promotion audit's decision
    for THEORY-744 (batch 060, ADR-047 v2). The source's Lemma 8, the
    kernel expansion on a submanifold, is re-derived for a manifold
    without boundary (the note below), which completes the interior
    derivation. The title now says "without boundary" and "minus the
    generator". The boundary rate and the semigroup limit move to
    QUESTION-tmpwvrrh.
tags:
- mathematics
- probabilistic-modeling
date: '2026-10-20'
source:
- LIT-1246
- LIT-981
summary: >-
  Coifman and Lafon (2006), [LIT-1246](../literature.d/LIT-1246.md), read in [NOTE-985](../notes.d/NOTE-985.md), with
  the PNAS announcement [LIT-981](../literature.d/LIT-981.md). The paper states the limit as a
  Schrödinger operator. Written as a drift, it shows what each α keeps of
  the density: the walk's stationary density is q^{2(1−α)}. On a manifold
  without boundary the limit is derived in full, the kernel expansion
  included (re-derived on promotion, 2026-10-20). The paper's own α = 1/2
  display has a sign error. Its boundary rate and heat-kernel proof are
  incomplete and are left to [QUESTION-tmpwvrrh](../questions.d/QUESTION-tmpwvrrh.md).
---
<!-- inactive-ok-file: NOTE-784 — Skimmed; the earlier reading whose phrase is checked here -->
<!-- inactive-ok-file: CLAIM-331 — Proposed; named for context, nothing here rests on it -->

# THEORY-744: As the kernel width ε goes to 0, Coifman and Lafon's α-normalized diffusion operator (I − P_{ε,α})/ε, for data sampled with density q = e^{−U} from a compact manifold without boundary, converges uniformly on smooth functions, at rate O(ε), to Δf + 2(1 − α)⟨∇U, ∇f⟩ with Δ the non-negative Laplace–Beltrami operator, which is minus the generator of a reversible diffusion with drift −2(1 − α)∇U and invariant density proportional to q^{2(1−α)}; α = 0 gives potential 2U and invariant density q², α = 1/2 gives the Langevin dynamics whose invariant density is the sampling density itself, and α = 1 gives Brownian motion on the manifold, with no trace of the density

## Source

Coifman and Lafon (2006), "Diffusion maps", *Applied and Computational
Harmonic Analysis* 21(1): 5–30, [LIT-1246](../literature.d/LIT-1246.md), read in full in
[NOTE-985](../notes.d/NOTE-985.md). The construction is §3.1. The limit is Theorem 2, proved
as Proposition 10 in Appendix B, and the heat kernel is Proposition 3 =
Proposition 11. The same family is announced without proof in the 2005
PNAS paper, [LIT-981](../literature.d/LIT-981.md) ([NOTE-784](../notes.d/NOTE-784.md)).

## What was actually shown

**Setting.** M is a compact C^∞ submanifold of ℝⁿ. The density q > 0 is
smooth, and U = −log q. The kernel is k_ε(x, y) = h(‖x − y‖²/ε), with h of
exponential decay, scaled so that m₀ = 1 and m₂ = 2. Δ is the
Laplace–Beltrami operator, taken positive semi-definite (Δ = −∇² on flat
space). Then q_ε = ∫k_ε(·, y)q(y)dy,
k^(α) = k_ε/(q_ε^α ⊗ q_ε^α), d^(α) = ∫k^(α)(·, y)q(y)dy,
P_{ε,α}φ = ∫k^(α)(·, y)φ(y)q(y)dy / d^(α), and L_{ε,α} = (I − P_{ε,α})/ε.

**The source's Lemma 8 (read, not re-derived).** At points farther than
ε^γ from the boundary, G_εf = f + ε(ωf − Δf) + O(ε²) uniformly. Here G_ε is
the kernel operator normalized by ε^{−d/2}, and ω is a potential set by
the embedding.

**The interior algebra, re-derived.** The constant ε^{−d/2} cancels in
every ratio below, so it is dropped.

1. q_ε = G_ε q = q + ε(ωq − Δq) + O(ε²), so
   q_ε^{−α} = q^{−α}(1 + εα(Δq/q − ω)) + O(ε²).
2. K^(α)φ = q_ε^{−α} G_ε[φ q q_ε^{−α}]
   = q_ε^{−α} G_ε[φq^{1−α}(1 + εα(Δq/q − ω))] + O(ε²)
   = q_ε^{−α} q^{1−α}[φ + ε((1 − α)ωφ + αφΔq/q − Δ(φq^{1−α})/q^{1−α})] + O(ε²).
3. Taking φ ≡ 1:
   d^(α) = q_ε^{−α}q^{1−α}[1 + ε((1 − α)ω + αΔq/q − Δ(q^{1−α})/q^{1−α})] + O(ε²).
4. Dividing, the ω and Δq/q terms cancel:
   P_{ε,α}φ = φ − ε[Δ(φq^{1−α})/q^{1−α} − φΔ(q^{1−α})/q^{1−α}] + O(ε²).
   So L_{ε,α}φ → Δ(φg)/g − φΔg/g with g = q^{1−α}, which is the source's
   Theorem 2.

**The drift form (the record's).** With Δ positive semi-definite, the
product rule is Δ(φg) = gΔφ + φΔg − 2⟨∇φ, ∇g⟩. So
Δ(φg)/g − φΔg/g = Δφ − 2⟨∇φ, ∇log g⟩ = Δφ + 2(1 − α)⟨∇U, ∇φ⟩, since
log g = −(1 − α)U. Writing ρ = e^{−2(1−α)U} = q^{2(1−α)}, the operator is
−ρ⁻¹∇·(ρ∇φ). It is symmetric and non-negative in L²(ρ dvol), and it
annihilates constants. Its negative is the generator of
dX = −2(1 − α)∇U(X)dt + √2 dW, reflected at the boundary, whose invariant
density is ρ ∝ q^{2(1−α)}. The three cases:

- **α = 0:** drift −2∇U, invariant density q². This is [NOTE-784](../notes.d/NOTE-784.md)'s
  "potential 2U". The ordinary graph Laplacian over-weights dense regions.
- **α = 1/2:** drift −∇U, invariant density q. This is the Langevin
  equation (2) of the source, ẋ = −∇U + √2ẇ. If the samples were drawn from
  that dynamics' equilibrium, α = 1/2 recovers the generator of the very
  dynamics that produced them. Acting on f, it is the backward operator,
  [LIT-981](../literature.d/LIT-981.md)'s wording. Its adjoint, conjugated by q, is the forward
  Fokker–Planck equation of §3.3.
- **α = 1:** no drift, uniform invariant density: Brownian motion on M.

The same exponent appears in the discrete stationary measure: by step 3,
d^(α)·q ≈ q^{−α}q^{1−α}q = q^{2(1−α)} to leading order.

**Numerical check.** On the unit circle with q ∝ e^{0.8 cos θ}, the
integrals were computed by quadrature on 4000 points with
h(s) = e^{−s/4}/√(4π) (m₀ = 1, m₂ = 2 in d = 1). Apply the operator to
f = cos 2θ + 0.3 sin θ. The maximum of |L_{ε,α}f − (−f″ + 2(1 − α)U′f′)|
over θ, against a scale of about 5, was:

| ε | α = 0 | α = 1/2 | α = 1 |
|---|---|---|---|
| 4 × 10⁻³ | 5.5 × 10⁻² | 2.9 × 10⁻² | 2.3 × 10⁻² |
| 1 × 10⁻³ | 1.4 × 10⁻² | 7.2 × 10⁻³ | 5.9 × 10⁻³ |

So the error is O(ε). The chain's stationary density matched q^{2(1−α)}
to within 4 × 10⁻⁴ at ε = 10⁻³.

**What the promotion review left open.**

- Lemma 8, the kernel expansion on a submanifold, was read and not
  re-derived when this entry was filed. It is re-derived for a manifold
  without boundary in the note of 2026-10-20 below.
- The boundary step bounds L_{ε,α}φ by O(1) on a strip of measure O(ε^γ),
  and concludes R_ε = O(ε^γ) in L². The L² norm of that piece is
  O(ε^{γ/2}). The convergence survives, but the rate as printed does not.
- Proposition 11's semigroup step replaces
  (I − εΔ)^{−1}(I − εΔ − εR_ε) by I − εR_ε. That needs R_ε to commute with
  Δ. The step also drops ‖(I − εΔ)^{−t/ε}‖, which grows like e^{tν_K²}, and
  it does not show that P_{ε,1} keeps E_K invariant. So the heat-kernel
  limit P_{ε,1}^{t/ε} → e^{−tΔ} is not proved by the source as written.

What could have failed: the curvature potential ω could have survived
into the limit, which would make the α = 1 operator depend on the
embedding and not only on the intrinsic geometry. It cancels in step 4.

## What this does not say

- **Not that finite samples behave this way at a given n.** The
  finite-sample error is O(m^{−1/2}ε^{−d/4−1/2}) by the bounds the source
  cites, which needs m ≫ ε^{−d/2−1}. The source's Criterion 4 states the
  square root of this.
- **Not that α = 1/2 recovers any dynamics from any data.** It recovers the
  reversible gradient (Langevin) dynamics whose equilibrium density is the
  sampling density, with isotropic unit diffusion. Non-equilibrium
  samples, anisotropic noise, or non-gradient drift are not covered.
- **Not that the eigenfunctions converge.** The statement is about the
  operator on band-limited functions. Spectral convergence of the
  finite-sample operator is a further result.
- **Not the source's §3.3 display.** That display,
  Δφ − (‖∇U‖²/4 − ΔU/2)φ, uses the ∇² convention against the paper's own
  convention, and it does not annihilate √q. The correct Schrödinger form
  is Δφ + (‖∇U‖²/4 + ΔU/2)φ with Δ positive, which is −∇²φ + (|∇U|²/4 −
  ∇²U/2)φ.

## Connections

- **[LIT-981](../literature.d/LIT-981.md) and [NOTE-784](../notes.d/NOTE-784.md).** This confirms and makes explicit their α-family
  takeaways ("backward Fokker–Planck" at α = 1/2, potential 2U at
  α = 0), now with the source of the proof.
- **[QUESTION-217](../questions.d/QUESTION-217.md).** An operator-induced order depends on the
  normalization. The same samples give different slow modes at different
  α, so a "spectral order" of data is relative to a choice of how density
  enters.
- **[QUESTION-222](../questions.d/QUESTION-222.md).** At α = 1/2 the slow eigenfunctions of the data's
  operator are those of the generator of the dynamics that produced the
  data. That is the route by which Nadler et al. treat them as reaction
  coordinates, the Markovian slow variables of a reduced model. Whether
  those coordinates close without memory is not addressed here.
- **[CLAIM-331](../claims.d/CLAIM-331.md).** For a reversible Langevin system, the slow modes this
  operator recovers are the system's slow variables, which is one source
  of the timescale hierarchy that the claim's "characteristically" runs
  together.
- **[QUESTION-tmpwvrrh](../questions.d/QUESTION-tmpwvrrh.md).** The boundary rate and the semigroup limit,
  which the title no longer claims.

## Note of 2026-10-20: the kernel expansion, re-derived

The promotion audit (batch 060) re-derived the source's Lemma 8 at interior
points of a compact manifold M without boundary, embedded in ℝⁿ. Take
m₀ = ∫h(|u|²)du = 1 and m₂ = ∫u₁²h(|u|²)du = 2, with
G_εf(x) = ε^{−d/2}∫_M h(‖x − y‖²/ε)f(y)dvol(y).

1. **Localization.** M is compact and embedded, so ‖x − y‖ is bounded
   below by a multiple of the geodesic distance near x, and by a constant
   away from it. Points beyond geodesic distance ε^{1/2−κ} contribute
   O(ε^∞) uniformly, by the exponential decay of h. So work in normal
   coordinates y = exp_x(s).
2. **Expansions.** ‖x − exp_x(s)‖² = |s|² − |II(s, s)|²/12 + O(|s|⁵), with II
   the second fundamental form. dvol = (1 − Ric(s, s)/6 + O(|s|³))ds.
   f(exp_x s) = f + s·∇f + ½sᵀHs + O(|s|³), where the trace of the
   coordinate Hessian H is −Δf at x.
3. **Scaling** s = √ε u removes the factor ε^{−d/2}. The integrand is
   [h − εh′|II(u, u)|²/12][1 − εRic(u, u)/6][f + √ε u·∇f + (ε/2)uᵀHu],
   up to terms of order ε^{3/2} and ε².
4. **Parity.** h(|u|²), |II(u, u)|² and Ric(u, u) are even in u. The √ε term
   and every ε^{3/2} term carry exactly one odd factor, so they vanish, and
   the remainder is O(ε²) uniformly in x.
5. **The order-ε term.** ½∫h uᵀHu du = ½m₂ tr H = −Δf. The terms in f give
   εωf, with ω = −(1/12)∫h′|II(u, u)|²du − (1/6)∫h Ric(u, u)du, a smooth
   function set by the embedding.

So G_εf = f + ε(ωf − Δf) + O(ε²) uniformly, with no first-derivative term.
That is what the interior algebra above needs: ω multiplies the function,
and so it cancels in step 4 whatever its value. The function φq q_ε^{−α}
in step 2 depends on ε, but smoothly and with bounded derivatives, so the
O(ε²) holds for it too, and L_{ε,α}φ converges uniformly at rate O(ε). The
sign is now in the title. With Δ ≥ 0, Δφ + 2(1 − α)⟨∇U, ∇φ⟩ is minus the
generator ∇²φ − 2(1 − α)∇U·∇φ = ρ⁻¹∇·(ρ∇φ), with ρ = q^{2(1−α)}.
