---
status: Read
paper: 'LIT-tmptep4g'
title: 'Silverberg et al. — Square-twist origami: hidden degrees of freedom and a critical transition to bistability'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Read on 2026-11-05 from the published PDF (5 pp., "© 2015 Macmillan
    Publishers Limited") posted by co-author Robert J. Lang on his own
    publications page,
    https://langorigami.com/wp-content/uploads/2016/03/nmat4232.pdf, with
    the Supplementary Information (6 pp.) from the same page,
    https://langorigami.com/wp-content/uploads/2016/03/nmat4232-s1.pdf;
    both extracted by pdftotext. The Cohen group's copy
    (cohengroup.lassp.cornell.edu) failed TLS verification and was not
    retried. Read in full: the whole letter (main text, Figs. 1–4 and
    captions, Methods). Skimmed: SI pp. 1–2 (rigid-facet solutions, the DOF
    count, the modified square twist with 1 DOF). Not read: the rest of the
    SI.
date: '2026-11-05'
summary: >-
  The square twist's crease pattern is isostatic and rigidly admits only
  its unfolded and folded states, yet it folds by bending its facets, a
  hidden degree of freedom with its own energy scale. The competition of
  bending and crease stiffness gives a critical plane angle φ_c ≈ 25°
  that shifts with k_b/k_c: monostable below, bistable and snapping above.
  A self-folding gel twist shows the hysteresis; added creases remove it.
  The authors' thesis: the number of DOF changes with the energy scale
  probed.
---
<!-- inactive-ok-file: THEORY-tmpixfqm CLAIM-478 LIT-tmpa3uim — Proposed, Unavailable or new; cited from the reading of Silverberg et al. (2015) as open -->

# NOTE-tmp0l0mn: Silverberg et al. — Square-twist origami: hidden degrees of freedom and a critical transition to bistability

## Contribution

- An experimental and theoretical demonstration, in a minimal origami
  structure, that the number of degrees of freedom depends on the energy
  scale probed.
- A geometrically driven transition between mono- and bistability, tuned
  by the plane angle φ and by the stiffness ratio k_b/k_c.
- A demonstration that the bistability and its hysteresis carry over from
  centimetre paper to a sub-millimetre self-folding gel, and that added
  creases remove them.

## Key insight

A crease pattern's Maxwell count holds only for the deformations it
admits. Facets that would be rigid at low load bend at higher load, and
that hidden freedom makes a rigidly unfoldable structure foldable. Whether
it then snaps depends on how expensive bending is relative to folding.

## Assumptions

- Simulations give torsional-spring energies to 12 creases, with rest
  angle θ₀ = 10° set by plastic deformation, and to 9 facet diagonals;
  facet corners keep fixed distances.
- Equilibria by Levenberg–Marquardt minimization, averaged over 20
  perturbed initial conditions.
- Samples were folded and unfolded before testing, so the "unfolded" state
  keeps some fold and "responds differently than a ‘pristine’ sheet".
- Strain-controlled tests in paper; stress-controlled (by temperature) in
  gel.

## Key results

- **Abstract.** The square twist's "crease pattern has zero degrees of
  freedom (DOF) and therefore should not be foldable, can nevertheless be
  folded by accessing bending deformations that are not explicit in the
  crease pattern." "These hidden bending DOF are separated from the crease
  DOF by an energy gap that gives rise to a geometrically driven critical
  bifurcation between mono- and bistability."
- **The thesis (introduction).** "systems can be overconstrained and rigid
  with respect to low-energy loading, but underconstrained and compliant
  as higher-energy DOF are accessed. Thus, Nf should be thought of as a
  variable quantity that changes with the experimental energy scale."
- **The crease pattern.** "An analysis of the geometric constraints reveals
  the pattern is isostatic." Rigidly, "the square twist allows two
  isolated states corresponding to the fully unfolded and folded
  configurations".
- **The critical angle.** "below a critical plane angle φc = (25 ± 2.5)◦ ,
  the distinction between folded and unfolded configurations is not
  observed; the structure is monostable".
- **Why it folds.** The hidden deformations "are essential for foldability
  as they enable the structure to access otherwise geometrically forbidden
  configurations."
- **Simulation.** "For kb /kc ≤ 1, monostability was observed for all
  geometries, whereas for kb /kc ≥ 103 , all geometries exhibited
  bistability." ("103" is 10³ in the extracted text.) The simulations
  predict 10 < k_b/k_c < 100; paper measures about 36.
- **Gel.** A sub-millimetre self-folding twist shows hysteresis under
  stress control for φ > φ_c; "the addition of these creases removes the
  hysteresis (Fig. 4d)."
- **SI p. 1, the DOF count.** "For the generic square twist (Fig. 1(a) and
  S1), NE,b = 12, Nf,i = 4 for i = 1, . . . , 9, giving zero DOF."
- **SI p. 2, a geometric skeleton.** With bending allowed only up to 10°
  and no energy cost below it, a purely kinematic model already has "a
  critical point at φc = (23 ± 2)◦ that separates a continuously connected
  region (φ < φc ) from a region with disconnected solutions (φ > φc )".
  The bistability rests on a change in the connectivity of configuration
  space, which the energetics then dress.
- **Outlook.** Further hidden DOF, such as facet stretching and shearing,
  suggest "that an even richer configuration space may be hidden with these
  more energetically expensive deformation modes."

## Concepts

- **Hidden degrees of freedom**: deformation modes, here facet bending,
  "not explicit in the crease pattern", with a higher energy scale than
  crease folding, accessed when the load exceeds it.
- **DOF hierarchy**: "a hierarchy of DOF, each with its own associated
  energy scale"; the Maxwell count depends on which levels are reached.
- **Critical plane angle φ_c**: the geometry at which the response switches
  between mono- and bistable; it depends on k_b/k_c.
- **Virtual creases**: localized bending along the short diagonals of the
  rhombi, with energy ∼ L k_b sin(φ/2) ψ².

## Connections

It cites Silverberg et al. (2014), [LIT-tmpa3uim](../literature.d/LIT-tmpa3uim.md), on reprogrammable Miura-ori
metamaterials, as its ref. 5, without restating its results. Evans,
Silverberg and Santangelo (2015), [LIT-tmpj33xl](../literature.d/LIT-tmpj33xl.md), model facet bending in the
Miura-ori as extra folds, the same move as the virtual creases here. Stern,
Pinson and Murugan (2017), [LIT-tmpjjho1](../literature.d/LIT-tmpjjho1.md), cite this paper for the nonzero
energy of over-determined vertices.

## Bearing on the record

- **The pasted synthesis on constraint architectures.** It cites this as S3:
  "square twist has zero rigid folding DOF; folds via panel bending;
  monostable→bistable transition". All three are right, and A uses no
  quotation marks for them. One precision: the crease pattern is
  *isostatic*, with zero DOF, and rigid geometry admits two isolated
  states; it is not rigid in the sense of having a single state. A misses
  the tuning parameters (φ and k_b/k_c), the hysteresis under stress
  control, the removal of bistability by added creases, the SI's result
  that configuration space goes from connected to disconnected at φ_c, and
  the general thesis that the number of DOF changes with the energy scale.
  The SI result is an instance of A's own distinctions between feasible
  and reachable, and between a geometric disconnection and an energy
  barrier.
- **A's question on effective constraints.** The pasted synthesis asks when
  an effective constraint ceases to be a good approximation because
  previously suppressed degrees of freedom become dynamically important.
  This paper is the most direct answer in A's list, and A did not make the
  link: facet planarity is a constraint only below the bending energy
  scale.
- **[CLAIM-478](../claims.d/CLAIM-478.md) (scale separation makes constraints).** Supports, with an
  energetic rather than a temporal separation. The paper's thesis is that
  the number of DOF is "a variable quantity that changes with the
  experimental energy scale": below the bending scale facet planarity is a
  constraint, above it the "constraint" is a degree of freedom, and the
  ratio of the two scales, k_b/k_c, decides whether the structure is
  bistable. The claim speaks of time scales; the mapping holds where
  stiffer modes also relax faster, which the paper does not discuss. A's
  gloss of [CLAIM-478](../claims.d/CLAIM-478.md), "scale separation creates effective constraints", is
  right.
- **[CLAIM-480](../claims.d/CLAIM-480.md) (composing interactions turns an interior into a
  constraint).** Related: an internal, stiffer mode acts as a constraint
  on low-energy behaviour.
- **[CLAIM-459](../claims.d/CLAIM-459.md) and [CASE-112](../cases.d/CASE-112.md) (bistable authority, ẇ = μw − w³ + h).**
  Related. The critical angle is a physical bifurcation parameter of the
  same kind as μ; here the parameters are geometry and the stiffness ratio.
- **[THEORY-136](../theory.d/THEORY-136.md) (abrupt change is not evidence of alternative stable
  states).** A contrast: the square twist's bistability is shown directly,
  by force curves with negative slope and by hysteresis, the kind of
  evidence [THEORY-136](../theory.d/THEORY-136.md) asks for.
- **[TERM-060](../terms.d/TERM-060.md) and [CLAIM-347](../claims.d/CLAIM-347.md).** Unrelated in sense. The paper's phrase
  "determining whether local kinematic constraints are globally
  compatible" concerns mechanical compatibility, not demands.
- Filed: [THEORY-tmpixfqm](../theory.d/THEORY-tmpixfqm.md). No instruction for machine-learning practice;
  nothing for the anthology.

## Limitations

- **The authors'.** Plastically pre-folded samples; facet bending modelled
  as nine virtual creases; the stress-control claim is a prediction
  confirmed in gel.
- **One unit cell.** Tessellations and coupling between cells are
  proposed, not tested.
- **The SI** was skimmed on pp. 1–2 only.
