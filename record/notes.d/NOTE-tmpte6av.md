---
status: Read
paper: LIT-tmpsa6iy
title: 'Toner & Tu — How birds fly together'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Read in full from the arXiv preprint adap-org/9506001v1 (8 June 1995),
    11 pp., titled there "How birds fly together: Long-range order in a
    two-dimensional dynamical XY model" and with the authors in the order
    Tu and Toner. The text was extracted with `pdftotext -layout`. I read
    the abstract, the whole letter (it has no section headings), equations
    (1)–(16), the acknowledgements, the footnote and the nine references.
    Pages are the preprint's. The published PRL version (75: 4326–4329)
    was not read, so differences between the two are unknown. The
    extraction garbles fractions and sub- and superscripts; where an
    expression below is reconstructed from it, the reconstruction was
    checked against the equations it must agree with, and is said so.
date: '2026-10-27'
summary: >-
  A continuum theory of a flock: a coarse-grained velocity field with a
  convective term, a preferred speed and noise, coupled to a conserved
  density. Its linearized theory loses order in d ≤ 2, as the equilibrium
  XY model does, but the convective nonlinearity is relevant below d = 4,
  and in d = 2 symmetry fixes the exponents at z = 6/5, ζ = 3/5, χ = −1/5.
  Since χ < 0 the transverse velocity fluctuations stay bounded as the
  flock grows, so a flock has true long-range orientational order in two
  dimensions. The exactness rests on a cubic vertex staying irrelevant,
  which the authors "strongly suspect"; a fallback argument gives χ < 0
  from z < 2, which they "expect on physical grounds".
---
<!-- inactive-ok-file: QUESTION-tmpl1yih QUESTION-218 CLAIM-157 CLAIM-tmpmx2ql CLAIM-327 CLAIM-280 CLAIM-331 THEORY-703 THEORY-tmpzaxy0 — Open or Proposed; the entries the reading bears on, cited as open -->

# NOTE-tmpte6av: Toner & Tu — How birds fly together

## Contribution

It gives the first hydrodynamic (coarse-grained, continuum) theory of
flocking, meant to cover "a large universality class of microscopic rules,
including those recently simulated by Viscek et. al." (abstract, p. 1). It
explains why the ordered phase Vicsek et al. observed in two dimensions is
possible at all, when the 2D XY model, which their rule reduces to in the
limit of zero speed, has no long-range order at T > 0. And it computes
scaling exponents for the ordered phase, claimed exact in d = 2, with a
testable prediction for the density–density correlation function (eq. 14).

## Key insight

The equilibrium model and the flock differ by one term: the convective
derivative (v · ∇)v, which "makes the dynamics non-potential and further
stabilizes the ordered phase" (p. 3). The heuristic is in Lagrangian
coordinates, where that term drops out and the interaction is local at each
instant: "However, at different times, the "neighbors" of one particular
"bird" will be different depending on the velocity field itself. Therefore,
two originally distant "birds" can interact with each other at some later
time. It is exactly this time dependent variable ranged interaction which
stabilizes the ordered phase" (p. 3). Motion mixes the members, the mixing
suppresses the long-wavelength fluctuations that destroy order in the
equilibrium case, and the order is a property of the field, not of any fixed
group of members.

## Assumptions

- **A continuum description.** The flock is a coarse-grained velocity field
  v(r, t) and a number density ρ(r, t), with the birds conserved (eq. 2,
  p. 3). Nothing below the coarse-graining scale appears.
- **The equation of motion (1), p. 3**: ∂ₜv + (v · ∇)v = αv − β|v|²v − ∇P
  + D_L∇(∇ · v) + D₁∇²v + D₂(v · ∇)²v + f, with β, D₁, D₂, D_L > 0, α < 0
  in the disordered phase and α > 0 in the ordered one. The pressure is
  P(ρ) = Σₙ σₙ(ρ − ρ₀)ⁿ. The noise is Gaussian, white and short-ranged,
  ⟨fᵢ(r, t)fⱼ(r′, t′)⟩ = Δδᵢⱼδᵈ(r − r′)δ(t − t′).
- **Speed fluctuations are fast and dropped.** In the ordered phase "We will
  ignore fluctuations in the magnitude |v| from its optimal value of
  √(α/β) since they decay in a finite time (of order 1/α)" (pp. 3–4). With
  units so that √(α/β) = 1, v = (v⊥, √(1 − |v⊥|²)), expanded for |v⊥|² ≪ 1.
- **One term is neglected and justified only a posteriori**: the cubic
  vertex ½|v⊥|²∂∥ v⊥ from the convective term in the co-moving frame (p. 4;
  the extraction leaves unclear whether the derivative is ∂∥ or ∂∥²; it is
  written ∂∥ on p. 8). Its linearized eigenvalue is 3 − d, positive below
  d = 3, and the authors argue by analogy with φ⁶ in φ⁴ theory that
  graphical corrections keep it irrelevant down to d = 2: "we strongly
  suspect that it does" (p. 8).
- **The reduced model (6, 7) describes birds only in d = 2.** There v⊥ has
  one component, written vₓ = ∂ₓh. The model is analysed in general d "with
  the goal of understanding it in the physical case d = 2" (p. 5).
- **The ordered phase only.** The order–disorder transition is not treated
  (pp. 9–10).

## Key results

### Linear theory (p. 4)

- Under x⊥ → bx⊥, x∥ → b^ζ x∥, t → b^z t, v⊥ → b^χ v⊥, δρ → b^{χ_ρ} δρ
  (eq. 5), keeping D₁, D∥, D⊥ = D₁ + D_L and Δ fixed, the linear exponents
  are z = 2, ζ = 1, χ = 1 − d/2, χ_ρ = χ. So "v⊥ fluctuations grow without
  bound (like L^χ) as L → ∞ for d ≤ 2 … This implies the loss of long range
  order in d ≤ 2" (p. 4). The linear theory reproduces the equilibrium
  result.
- The equal-time correlation in the linear theory is a sum of a
  longitudinal part with denominator (D⊥q⊥² + D∥q∥²)q⊥² and a transverse
  part with (D₁q⊥² + D∥q∥²)q⊥² (p. 4; reconstructed from the extraction).

### The nonlinearities are relevant below four dimensions (p. 5)

- λ ~ b^{γ_λ}λ with γ_λ = χ + 1 = 2 − d/2, and σₙ ~ b^{γₙ}σₙ with
  γₙ = n + (1 − n)d/2. The first to turn positive are γ_λ and γ₂, both at
  d < 4, so "the linearized hydrodynamics will break down" there; d_c = 4.
  (The text writes γₙ = z − χ + nχ, which does not give n + (1 − n)d/2 for
  the linear exponents; z + (n − 1)χ − 1, as in eq. 8, does. A typo.)

### Exact exponents in d = 2 (pp. 5–8)

- **"Galilean invariance"** of the reduced equations (3, 4): v⊥ → v⊥ + v⊥,₀
  with x⊥ → x⊥ − λv⊥,₀t leaves them invariant, so λ has no graphical
  renormalization (p. 5; footnote 6 compares the forced Navier–Stokes
  equation, which also has d_c = 4).
- **In d = 2 only**, D∥ and Δ are also unrenormalized. Δ, because in the
  h-model (6, 7) the effective noise η has long-ranged correlations
  ∝ 1/q⊥², which local nonlinearities cannot generate; D∥, because any
  correction carries a power of q⊥ (pp. 5–6).
- **The RG equations (8)** and the three exact constraints χ + z = 1,
  z = 2ζ, d + ζ + 2χ = z + 1 (eq. 9) give
  z = 2(d + 1)/5, ζ = (d + 1)/5, χ = (3 − 2d)/5 (eq. 10, p. 6).
- **Flow of the couplings (11)–(13), p. 7.** g₁ and g₂ become relevant
  below d = 4; all gₙ>₂ are irrelevant near d = 4 and are dropped. Γ
  "only becomes relevant below d = 1.5 where χ > 0, i.e., when the ordered
  phase disappears". At one loop, G₂ = 0 and G⊥ = (11/192π²)(g₁/2 + g₂)(g₁/2)
  (reconstructed from the extraction; it agrees with eq. 12's fixed-point
  condition G⊥ = 2ε/5 and the stated fixed line), giving "a fixed line
  (actually a fixed hyperbola)" (g₁/2 + g₂)g₁ = 768π²ε/55. "We do not know
  whether the vanishing of G₂ to this order is the result of some symmetry
  … or if it is purely coincidental" (p. 7). Either way, line or point,
  the exponents are eq. (10), "since those results depended only on the
  symmetries of the model" (p. 7).
- **In d = 2: z = 6/5, ζ = 3/5, χ = −1/5** (p. 7).
- **Density correlation, eq. (14), p. 7**: ⟨|ρ(q, ω)|²⟩ =
  Δq⊥²ρ₀² / [(ω² − c²q⊥²)² + ω²(D⊥ᴿ(q, ω)q⊥² + D∥q∥²)²], with
  c = √(σ₁ρ₀) "the speed of sound". It has two sharp peaks at ω = ±cq⊥ of
  width D⊥ᴿq⊥² + D∥q∥², as do "all of the correlation and response
  functions for this problem" (p. 8).
- **Eq. (15), p. 8**: D⊥ᴿ(q⊥, q∥, ω ∼ cq⊥) = q⊥^{z−2} f(q∥/q⊥^ζ).
- **Eq. (16), p. 8, the result**: ⟨|v⊥(r, t)|²⟩ = constant −
  L⊥^{2χ} g(L∥/L⊥^ζ) = constant − L⊥^{−2/5} g(L∥/L⊥^{3/5}), with L⊥ and
  L∥ the flock's extent across and along the mean motion. "Since this goes
  to a finite constant as L → ∞, we see that long ranged order is stable in
  this model in d = 2" (p. 8).

### If the cubic vertex is relevant after all (p. 9)

- Exact exponents are lost, but Δ is still unrenormalized, and rotational
  invariance requires (v⊥ · ∇)v⊥ and |v⊥|²∂∥v⊥ to renormalize together, so
  2χ − 1 = 3χ − ζ, i.e. χ = ζ − 1. With the last relation of (9),
  χ = (z − d)/3. "Now we expect on physical grounds that z < 2 for all
  dimensions d < 4, since physically, the motion of the "birds" enhances
  the mixing … Hence we expect hyperdiffusive behavior, which implies
  z < 2. Then the scaling relation χ = (z − d)/3 implies χ < 0, i.e., true
  long range order in d = 2" (p. 9).
- Vicsek et al.'s simulations "indeed find a long range ordered state in
  the low "temperature" regime, in agreement with our predictions" (p. 9).

### What is left (pp. 9–10)

- The ordered phase in d > 2 (no exact exponents; an ε-expansion "should
  give quite accurate exponents in d = 3").
- The transition: without the convective vertex the model "is just model A
  dynamics for a φ⁴ theory, as studied by Halperin et al.", but the
  convective vertex "becomes relevant at the transition in d = 4 as well";
  a study is "currently underway" (p. 10). A longer account is promised as
  ref. [9], "in preparation".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The linearized hydrodynamic theory of a flock loses long-range order in d ≤ 2, as the equilibrium XY model does | strong | exact linear calculation, p. 4 |
| C2 | The convective and σ₂ nonlinearities are relevant below d_c = 4, so the flock differs from the equilibrium model there | strong | power counting, p. 5 |
| C3 | In d = 2 the exponents are exactly z = 6/5, ζ = 3/5, χ = −1/5 | moderate | symmetry (Galilean invariance; non-renormalization of Δ and D∥ in d = 2), conditional on the cubic vertex staying irrelevant, argued by analogy with φ⁶ in φ⁴ theory (p. 8) |
| C4 | A two-dimensional flock has true long-range orientational order | moderate | follows from C3 via eq. 16; independently from χ = (z − d)/3 plus z < 2 "on physical grounds" (p. 9); consistent with Vicsek et al.'s simulations, which are cited, not shown |
| C5 | The convective term, through motion-driven change of neighbours, is what stabilizes the order | moderate | the formal result is that the convective vertex is what separates the model from the equilibrium one (pp. 3, 5); the change-of-neighbours mechanism is a stated heuristic (p. 3) |
| C6 | The model describes a large universality class of microscopic rules, Vicsek et al.'s among them | weak | asserted (abstract, p. 2); the reduction from a microscopic rule to eqs. (1, 2) is not derived |
| C7 | Speed fluctuations relax in a finite time of order 1/α and can be ignored at long wavelengths | strong | the α, β terms give |v| a stable fixed value; stated, p. 4 |

## Concepts

- **Flock (here)** — a continuum of self-propelled "birds" (the paper's
  scare quotes throughout) described only by a coarse-grained velocity
  field and a conserved density (eqs. 1, 2).
- **Dynamical XY model** — the analogy: the bird's velocity, like an XY
  spin, has fixed length and continuous rotational symmetry; at zero speed
  Vicsek's rule "reduces precisely to the Monte Carlo dynamics of a two
  dimensional XY model" (p. 2, credited to Vicsek in ref. 3).
- **Long-range order** — ⟨v⟩ ≠ 0 with the fluctuations ⟨|v⊥|²⟩ bounded as
  the system grows (eq. 16); its loss in the linear theory is fluctuations
  growing like L^χ with χ > 0.
- **Convective term** — (v · ∇)v, the transport of the velocity field by
  itself; the "essential difference" from the equilibrium model (p. 3).
- **"Galilean invariance"** — the symmetry of the reduced equations under a
  shift of v⊥ with a compensating boost (p. 5), in quotes in the paper.
- **Hyperdiffusive** — z < 2: fluctuations spread faster than by diffusion,
  which the authors attribute to motion-enhanced mixing (p. 9).

## Connections

- **Vicsek et al.** (ref. [2], cited as a preprint; the paper spells the
  name "Viscek"), the simulation whose two-dimensional ordered phase is the
  puzzle. Neighbour-averaging with noise at constant speed (p. 2). The
  record holds no LIT for it.
- **Mermin and Wagner** (ref. [5]) and **Kosterlitz and Thouless** (ref.
  [4]): the equilibrium results the flock evades. The paper's inference is
  that the order "must depend on fundamentally dynamical, non-equilibrium
  aspects of the model" (p. 2).
- **Forster, Nelson and Stephen** (ref. [8]): the dynamical renormalization
  group and the forced Navier–Stokes analogy (footnote 6).
- **Reynolds' boids** (ref. [1]), among earlier flocking simulations; the
  boids model is the one Seth measures (THEORY-703, NOTE-935).

## Bearing on the record

- **QUESTION-tmpl1yih: a worked case in which creating a form and
  stabilizing it are separate achievements, with the question's own
  bifurcation in it.** The α and β terms of eq. (1), αv − β|v|²v, are the
  normal form ẋ = μx − x³ the question opens with, and they create the
  ordered state's local magnitude √(α/β) when α changes sign (p. 3). But in
  d = 2 that bifurcation does not by itself give a persistent ordered
  state: the linear theory around it loses long-range order (p. 4), as the
  equilibrium XY model does. What stabilizes the form at large scales is a
  different mechanism, the convective nonlinearity (pp. 5–9). So the paper
  supplies the question's "a case in which two of the three come apart", for
  creation against stabilization: in the equilibrium XY model the same
  bifurcation creates local order that is not stabilized. The third
  achievement, a constitutive role, the paper does not touch: its order is
  a broken symmetry of a field, and it says nothing of agency, which bears
  out A14's "while avoiding the assumption that every coordinated flock is
  an autonomous agent". The transition itself, which the question would
  want named, is left open (pp. 9–10).
- **CLAIM-tmpmx2ql: support for "separation makes a constraint", and a
  mechanism for slowness its list lacks.** Speed fluctuations "decay in a
  finite time (of order 1/α)" and are dropped (pp. 3–4), so the fixed speed
  √(α/β) becomes a constraint, v = (v⊥, √(1 − |v⊥|²)), on the slow
  dynamics: the claim's fast variable settling into a relation, in a flock.
  The slow modes left are the transverse velocity, slow because rotational
  symmetry is broken, and the density, slow because birds are conserved
  (eq. 2), which propagate as sound at ω = ±cq⊥ (p. 8). The claim's "Not one
  mechanism" names conservation and transport with τ_k = 1/(Dk²); this
  paper has conservation, and also broken continuous symmetry, which is not
  among A13's five, and its scaling is not diffusive: ω ~ q^z with z = 6/5
  in d = 2, hyperdiffusive (pp. 7, 9). It is also the claim's second half
  in a new form: the ordered state makes the slow transverse modes, which do
  not exist in the disordered phase, by symmetry breaking rather than by
  slowing near an instability.
- **CLAIM-157: a coherent form with no block of members and no gap.** The
  order is the mean velocity of a field, and the mechanism stabilizing it
  is that neighbourhoods keep changing (p. 3), so no fixed grouping of
  members persists while the order does. Its fluctuations are gapless: the
  hydrodynamic modes' frequencies go to zero as q → 0 (eqs. 14, 15). So
  the gap-isolated block the claim names is not what this theory finds; it
  finds a broken-symmetry mode. That is QUESTION-218's mode found without
  a grouping, of a different kind from CLAIM-388's uniform-coupling sum.
  It does not defeat the claim, which is relative to a target and can name
  a mode; it is a case where the members cannot be the grouping.
- **CLAIM-280: turnover not only survived but stabilizing.** The claim
  holds that a pattern can persist while its constituents are replaced. In
  the flock, change of neighbours is the stated reason the order is stable
  (p. 3), so the turnover of a member's neighbourhood does work for the
  pattern rather than merely failing to destroy it. The heuristic is the
  authors', not a calculation.
- **CLAIM-327: the members read a local average, not the collective
  variable.** In Vicsek's rule each bird averages "the direction of its
  neighbors in certain area" (p. 2); no bird reads the mean velocity ⟨v⟩,
  and the order is still maintained. So the global collective variable is
  regenerated by members who read only a local estimate of it. Whether
  that meets the claim's second stage ("members recognize it and use it")
  depends on whether a local field value counts as reading the variable;
  the paper does not take up the question.
- **CLAIM-331.** Higher-level variables slower: here the order parameter's
  long-wavelength fluctuations are the slowest modes (ω → 0 as q → 0), and
  the fast magnitude mode is eliminated. Consistent; no more than that.
- **THEORY-703 (Seth, boids).** The paper's order is defined by
  ⟨v⟩ ≠ 0 and bounded fluctuations, not by any predictive measure, so it
  is not a criterion of weak emergence in THEORY-703's sense and does not
  bear on its `promote_when`. Noted because the record's only other flock
  is Seth's.
- **No instruction for machine-learning practice.**

## Limitations

- **The exponents' exactness is conditional.** The neglect of the cubic
  vertex rests on an analogy with φ⁶ in φ⁴ theory ("we strongly suspect",
  p. 8), and the fallback rests on z < 2 "on physical grounds" (p. 9). The
  first is an argument, the second an expectation.
- **The universality claim is asserted.** No microscopic rule is
  coarse-grained into eqs. (1, 2); the terms are written down by symmetry.
- **The simulation support is cited, not shown**, and was then a preprint.
- **Infinite-flock results.** Eq. (16) is a statement about L → ∞; a real
  flock is finite, and the paper does not say at what sizes the order is
  observable.
- **Typos in the preprint**: the "recursion relations (16)" on p. 7 must
  mean (8) or (11)–(13); "the rescalings eq.(3)" on p. 8 must mean eq. (5);
  the γₙ formula on p. 5 (see Key results).
- **Not in this text, and not checked in this reading**: it is standardly
  reported that Toner's later reanalysis (Phys. Rev. E, 2012) found the
  2D exponents not exact, because of nonlinear terms the reduced model
  leaves out, while the long-range order stands; and that the longer
  account promised as ref. [9] is Toner and Tu, Phys. Rev. E 58 (1998).
  Neither is held by the record; both should be read before C3 is leaned
  on.
- The published PRL text was not compared with the preprint.

## Open questions

- Does the cubic vertex stay irrelevant in d = 2? A controlled calculation,
  or simulation finite-size scaling of ⟨|v⊥|²⟩ in L⊥ and L∥, would say
  (THEORY-tmpzaxy0).
- What is the order–disorder transition: continuous, as for model A, or
  changed by the convective vertex (p. 10)? That is the creation half of
  QUESTION-tmpl1yih for this case.
- Is G₂ = 0 at one loop a symmetry or a coincidence (p. 7)?
