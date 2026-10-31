---
status: Read
paper: 'LIT-tmpody6k'
title: 'Kolathaya & Ames — input-to-state safe control barrier functions'
version: 1
history:
- version: 1
  date: '2026-10-31'
  note: >-
    Read in full from the arXiv preprint 1803.03035v3 (11 August 2018),
    7 pp., the accepted version of the IEEE Control Systems Letters paper,
    fetched 2026-10-31. Text extracted with `pdftotext -layout`. I read the
    abstract, §§I–VI, footnotes 1–4, Remarks 1–5, Examples 1–3 and the
    references; Figures 1–4 survive only as captions and axis ticks. The
    published version (3(1):108–113) was not compared. Checked (scipy, my
    own script): in Example 1, ẋ = −x + x²u with h = 2 − x, the zero
    controller under d = 1 from x = 2 diverges (past 10³ by t ≈ 0.69),
    while k(x) = L_g h = −x² keeps x ≤ 2 for d up to 4 and x ≤ 2.36 at
    d = 6, inside the paper's set x ≤ 2 + d²/4; the inequality
    ε|a|² − |a|D ≥ −D²/(4ε) behind Theorem 2; and Example 2's
    counterexample, where u = 0 with d = 10 from x = 0.1 leaves [−2, 2].
    Theorem 1's proof sketch was checked by hand.
date: '2026-10-31'
summary: >-
  Defines input-to-state safety of a set C = {h ≥ 0}: under a bounded
  input disturbance d, the larger set C_d = {h + γ(‖d‖∞) ≥ 0} is forward
  invariant, for a class-K γ. A barrier condition with a disturbance term,
  ḣ ≥ −α(h) − ι(‖d‖), implies it (Theorem 1). Given an ordinary control
  barrier function, adding L_g hᵀ to a safeguarding controller, or the
  constraint term −εL_g h L_g hᵀ in a CLF–CBF quadratic program, yields
  such a function with ι(‖d‖) = ‖d‖²/(4ε) (Theorem 2). The enlargement is
  a class-K function of the disturbance bound in barrier units, quadratic
  in the universal construction; it is not proportional to the bound.
---

# NOTE-tmpjhivv: Kolathaya & Ames — input-to-state safe control barrier functions

## Contribution

A robust version of control barrier functions (CBFs) for affine systems
with matched input disturbances, by analogy with Sontag's input-to-state
stability. Before it there was "no existing literature that allows to
make an estimate of this buffer while providing a means to study safety
under uncertainties" (p. 1). The letter defines input-to-state safe (ISSf)
sets and ISSf barrier functions, gives a sufficient condition (Theorem 1),
a construction from an existing CBF (Theorem 2), a universal formula
(Remark 5), and an ISSf CLF–CBF quadratic program, demonstrated on two
one-dimensional systems and a two-link robot.

## Key insight

Do not ask that the safe set stay invariant under disturbance, which a
nominal CBF controller cannot guarantee. Ask that a slightly larger set,
enlarged by an amount that vanishes with the disturbance, stay invariant.
A Sontag-style damping term, pushing harder along L_g h, buys that
guarantee, and its gain ε trades control effort for the size of the
enlargement.

## Assumptions

- **Affine control system** ẋ = f(x) + g(x)u, f and g locally Lipschitz
  (eq. 9); the disturbance enters through the input, u = k(x) + d(t),
  d ∈ L∞ (eq. 11). Disturbances outside the input channel are not
  treated.
- **Safe set** C = {h ≥ 0} with h continuously differentiable, non-empty
  interior and no isolated points (eqs. 2–4).
- **A domain D = {h + b > 0}** on which the barrier inequality holds, and
  extended class-K functions α on (−b, c) (Definition 1, eq. 8).
- **A disturbance bound d̄ < a**, small enough that C_d stays inside D.
  The definition is local; the global version is "less interesting"
  because large disturbances make C_d large (p. 2).

## Key results

- **Definition 3 (ISSf set).** C is ISSf if there are γ ∈ K and d̄ such
  that for every ‖d‖∞ ≤ d̄ the set C_d = {h(x) + γ(‖d‖∞) ≥ 0} is forward
  invariant (eqs. 12–14).
- **Theorem 1.** If L_f̄ h(x) + L_g h(x)µ ≥ −α(h(x)) − ι(|µ|) on D for
  |µ| ≤ d̄ (an ISSf barrier function, eq. 20), then C is ISSf, with
  γ = β⁻¹∘ι, β(r) = −α(−r). Proof: on ∂C_d, η = h + γ = 0 and
  η̇ ≥ −α(−γ) − ι = β(γ) − ι = 0 (eqs. 21–23); then Nagumo-type
  invariance. With α(h) = λh, C_d = {h + ι(‖d‖∞)/λ ≥ 0} (eq. 25).
- **Theorem 2.** If sup_u [L_f h + L_g h u − L_g h L_g hᵀ] ≥ −α(h) on D,
  then h is an ISSf-CBF, since |L_g h|² − |L_g h|‖d‖ ≥ −‖d‖²/4; with the
  gain ε, the bound is −‖d‖²/(4ε).
- **Remark 5.** A universal ISSf safeguarding formula, Sontag's universal
  formula plus the damping term.
- **Example 1.** ẋ = −x + x²u, C = {x ≤ 2}: k ≡ 0 is safe without
  disturbance, but d = 1 from x = 2 sends the state off to infinity;
  k(x) = −x² gives C_d = {2 − x + ‖d‖²/4 ≥ 0} (checked; the bound is
  conservative).
- **Example 2.** With the ordinary CBF–QP, ISSf fails (x(0) = 0.1,
  u = 0, d = 10, checked); the ISSf-QP keeps the state bounded, and
  "C_d shrinks for larger values of ε" (Fig. 3–4 captions).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | An ISSf barrier inequality implies forward invariance of the enlarged set C_d | strong | Theorem 1, short proof checked |
| C2 | Adding the damping term L_g hᵀ (gain ε) to any CBF controller yields ISSf with enlargement ‖d‖²/(4ε) in h | strong | Theorem 2, completing the square, checked |
| C3 | Ordinary CBF–QP controllers need not be ISSf | strong | Example 2, a counterexample, checked |
| C4 | The ISSf-QP unifies safety and stability under input disturbance on a robot | weak | one simulated two-link example, figures only |

## Method

The ISSf-QP (p. 4): minimize ½uᵀHu + Fᵀu over (u, δ) subject to the CLF
constraint with relaxation δ and the barrier constraint
L_f h + L_g h u − εL_g h L_g hᵀ ≥ −α(h). For relative degree two, an
exponential-CBF version with gains k_p, k_d (eq. 37).

## Concepts

- **Safeguarding controller** — one that renders C forward invariant
  (p. 2).
- **Input-to-state safety (ISSf)** — invariance of C_d ⊇ C whose
  enlargement is a class-K function of ‖d‖∞ (Def. 3). Defined here with
  respect to sets, unlike Romdlony and Jayawardhana's definition with
  respect to systems (Remark 2).
- **ISSf barrier / control barrier function** — eq. (20) / eq. (26).

## Connections

- Nominal CBFs (Ames et al. 2014, 2017) and barrier certificates (Prajna
  and Rantzer 2005) are the base. ISSf is due to Romdlony and
  Jayawardhana (2016, 2017); this letter redefines it for superlevel sets.
- Sontag's ISS and universal formula are the templates (Theorem 2
  follows Sontag 1989's k(x) − L_g Vᵀ).
- In the record, forward invariance of a constraint set is viability's
  invariance (THEORY-134): a barrier inequality is a Nagumo tangency
  condition made quantitative. ISSf adds a statement about what happens
  when the tangency condition is violated by a bounded disturbance: the
  state leaves C but by a bounded amount. Contraction under singular
  perturbation (THEORY-771) is the stability-side analogue of the same
  ISS template.

## Bearing on the record

- **The registration's summary needs one correction.** It says the state
  stays "within a set enlarged in proportion to the disturbance bound".
  The enlargement is a class-K function γ of ‖d‖∞, measured in units of h
  rather than distance, and in the paper's own construction it is
  quadratic, ‖d‖²/(4ε) (or ι/λ for an exponential CBF).
- **CASE-tmpz9u5t** says "Barrier certificates of this kind are Kolathaya
  and Ames's". That is loose. The case's box certificate checks that every
  face's inward margin exceeds the disturbance bound (margins +0.16 to
  +0.568 against disturbances of 0.02 for u and v). That is robust forward
  invariance of the box itself, a Nagumo or nominal barrier condition with
  a disturbance margin, and it is THEORY-134's notion. ISSf is the
  different, weaker guarantee for when the disturbance can exceed the
  margin: the state may leave the box, but only into a set enlarged by
  γ(‖d‖). The case would gain from ISSf exactly where its certificate
  stops, for degradations beyond the stated bounds. The citation should
  read "robust invariance of the box (THEORY-134); Kolathaya and Ames's
  ISSf is the graded version that would apply beyond the margin".
- **Topic.** The letter is control theory. Under the current vocabulary
  mathematics is the right primary tag; complex-systems is weak. The
  vocabulary still has no control-theory topic, which is left to the
  owner.
- No instruction for ML practice.

## Limitations

- Disturbances only through the input channel (matched), bounded in L∞.
- Local: requires d̄ small enough that C_d stays in D.
- The enlargement is in barrier-function units, so how far in state
  space C_d reaches depends on h.
- The examples are illustrations; no comparison with robust or tube MPC.
- Theorem 1's proof is a sketch that defers to Ames et al. 2017's
  Proposition 1, and the statement has a typo (lim_{r→a} γ(a) = b).

## Open questions

- Is there a converse: does every ISSf set admit an ISSf barrier
  function?
- How does ISSf compose for interconnected systems, the small-gain
  question the exchange gestured at without a reference?
