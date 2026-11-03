---
status: Skimmed
paper: LIT-tmpk8i57
title: 'Heymann & Vanden-Eijnden — The geometric minimum action method'
version: 1
history:
- version: 1
  date: '2026-11-03'
  note: >-
    From the published CPAM text, 61: 1052–1117, as posted on a Peking
    University course page (math.pku.edu.cn/teachers/litj/notes/
    stoch_topics2017/lect06/gMAM.pdf; the https address failed TLS, the
    http one served it), 66 pp. Read: the abstract and contents, §1
    (pp. 1053–1061), §§2.1–2.2 (pp. 1061–1066, Propositions 2.1 and 2.3,
    Lemma 2.2, the diffusion case), §4.1 to the start of its accuracy study
    (pp. 1083–1085) and §5 (pp. 1097–1098). Not read: §§2.3–2.4, §3, the rest
    of §4.1, §§4.2–4.3, the appendices and the note added in proof; so
    Skimmed. Text extracted with pypdf; symbols are partly garbled and
    equations were reconstructed and re-derived where used below.
date: '2026-11-03'
summary: >-
  The Freidlin–Wentzell quasi-potential, a double minimization over paths
  and their duration, is rewritten as a single minimization over curves of
  a parametrization-free action, which has minimizers when the end points
  are equilibria and is computed by a string-method-like relaxation
  (gMAM). For a diffusion it is V = 2 inf ∫ |b| sin²(θ/2) ds. In gradient
  systems with identity noise the most likely transition paths are
  parallel to the drift; in the nongradient Maier–Stein model they depart
  from the heteroclinic orbit once the drift is far enough from gradient.
---
<!-- inactive-ok-file: QUESTION-071 — Open; the question whose note the reading bears on -->

# NOTE-tmp6wm7j: Heymann & Vanden-Eijnden — The geometric minimum action method

## Contribution

A geometric reformulation of the quasi-potential (Proposition 2.1), a
probabilistic reading of its minimizer as the maximum-likelihood transition
curve (Proposition 2.3), and an algorithm, gMAM, that applies to
nongradient SDEs, SPDEs and Markov jump processes, where the string method
does not.

## Key insight

Between two equilibria the optimal transition takes infinite time, so
minimizing over paths of fixed duration has no minimizer. Removing time
removes the problem: the action can be written on the space of curves,
invariant under reparametrization, and minimized there (pp. 1058–1059).

## Assumptions

- Small-noise dynamics with a large-deviations action S_T(ψ) = ∫ L(ψ, ψ̇)
  dt, L the Legendre transform of a Hamiltonian H(x, θ) (eqs. 1.1–1.2).
- Two classes: SDEs dX = b(X)dt + √ε σ(X)dW, H = ⟨b, θ⟩ + ½⟨θ, aθ⟩
  (eq. 1.4); Markov jump processes (eqs. 1.5–1.6).
- Assumptions 1–3 (p. 1060): H(x, 0) ≤ 0, H twice differentiable,
  H_θθ uniformly elliptic on compacts.

## Key results

- **Quasi-potential (eq. 1.9):** V(x₁, x₂) = inf_T inf_ψ S_T(ψ); it gives
  Arrhenius-like hopping rates k ≍ exp(−V/ε) (eq. 1.14) and the small-noise
  equilibrium distribution (eq. 1.15).
- **Geometric form for diffusions (eqs. 1.16–1.18).** ½|ψ̇ − b|²_a ≥
  |ψ̇|_a|b|_a − ⟨ψ̇, b⟩_a, with equality when |ψ̇| = |b|, gives V(x₁, x₂) =
  2 inf_γ ∫_γ |b|_a sin²(θ/2) ds, θ the angle between the curve and b.
  Re-derived for this note (AM–GM on the square). For the general case,
  Ŝ(φ) = sup_{H(φ, ϑ) ≤ 0} ∫ ⟨φ′, ϑ⟩ dα (eq. 1.19, Proposition 2.1).
- **Probabilistic meaning (Proposition 2.3).** If the minimizer is unique up
  to reparametrization, then given a transition the process stays within any
  Fréchet distance of the minimizing curve with probability → 1 as ε → 0.
- **Gradient case (p. 1058).** For b = −∇U and σ the identity, "transition
  paths are always parallel to the drift", which the string method exploits;
  the steady state of the gMAM flow is then "the minimum energy path"
  (p. 1085). Re-derived: for such b, ∫ |∇U| (1 − cos θ) ds ≥ ΔU along any
  uphill curve with equality only if the curve runs against b throughout, so
  V(x₁, saddle) = 2(U(saddle) − U(x₁)) and the escape path is the
  time-reversed relaxation path.
- **Maier–Stein (§4.1, Figure 4.1).** du = (u − u³ − βuv²)dt + √ε dW_u,
  dv = −(1 + u²)v dt + √ε dW_v; gradient iff β = 1. For β ≤ β_crit = 4 the
  minimum action path is still the heteroclinic orbit through (0, 0); for
  β > 4 the piece in the basin of (−1, 0) is not; at β = 10 the computed
  path departs visibly from it.
- **Conclusions (§5).** The method also computes quantum-tunnelling
  instantons via the Agmon distance (eq. 5.2).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The quasi-potential equals the infimum of a parametrization-free action over curves | strong | Proposition 2.1, proved in §2.3 and the appendices (not read) |
| C2 | The minimizing curve is the maximum-likelihood transition path in the small-noise limit | strong | Proposition 2.3, under stated uniqueness assumptions |
| C3 | In gradient systems with identity diffusion, transition paths are parallel to the drift | strong | stated (p. 1058); re-derived from eq. 1.18 |
| C4 | Nongradient drift can make the escape path differ from the time-reversed relaxation path | strong | Maier–Stein, β > 4, computed and consistent with Maier and Stein |
| C5 | gMAM is accurate and efficient | moderate | §4.1's convergence study (not read) |

## Concepts

- **Quasi-potential** — the minimal action to go from x₁ to x₂ in any time.
- **Minimum action path / maximum-likelihood transition curve** — the curve
  minimizing Ŝ.
- **Minimum energy path** — a curve along which ∇U is tangent; the gradient
  case's transition path.

## Connections

Freidlin and Wentzell; the original MAM (E, Ren and Vanden-Eijnden); the
string method and nudged elastic band; Maier and Stein. The record's
reading of transition paths in Freidlin–Wentzell is LIT-1881.

## Bearing on the record

- **QUESTION-071's note of 2026-11-02 holds, with two refinements.**
  - *Holds.* "In a gradient system with small isotropic noise, the most
    likely escape follows the time-reversal of the relaxation path from the
    saddle" is the paper's gradient case (p. 1058) and re-derives from
    eq. (1.18). The note's caveat, "only in the frozen-slow-variable limit,
    since the toy is not a gradient system and its noise is degenerate", is
    the right one: the paper's Assumption 3 (ellipticity) fails for
    degenerate noise, and its results need a non-degenerate H_θθ.
  - *Refinement 1: nongradient is not enough to break the reversal.* In the
    Maier–Stein model the minimum action path is still the heteroclinic
    orbit, the reversed relaxation path, for all β ≤ 4, though the drift is
    gradient only at β = 1. So "a gradient system" is sufficient, not
    necessary, for the noise path to be the reversed relaxation path; how far
    from gradient a drift must be is a model-specific threshold.
  - *Refinement 2: what the path can tell is a small-noise, single-path
    statement.* Proposition 2.3 says the noise-driven transition concentrates
    on the minimizing curve as ε → 0, given that a transition occurs. A
    directed transition is distinguishable by its path only to the extent
    that it leaves that tube; one observed path at finite ε is evidence, not a
    test, and the note's "unless the controller imitates the noise path" is
    the whole loophole: the noise path is computable (that is this paper's
    point), so an informed controller can follow it.
- **No instruction for ML practice.**

## Limitations

- Small-noise asymptotics only; prefactors are not computed.
- Uniqueness of the minimizer is assumed in Proposition 2.3.
- Not read: the proofs and most numerics, so the algorithmic claims are
  taken from the statements.

## Open questions

When does a nongradient drift's minimum action path leave the heteroclinic
orbit, in general rather than for Maier–Stein? And for the record: what
statistic of a finite sample of transition paths best separates a
noise-driven from a controlled escape?
