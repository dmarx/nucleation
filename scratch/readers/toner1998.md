# Reader notes: toner1998 (LIT-2970)

Toner and Tu (1998), "Flocks, herds, and schools: A quantitative theory of
flocking", arXiv cond-mat/9804180; PRE 58, 4828 (doi 10.1103/PhysRevE.58.4828).

## Step 1: copies located (2026-11-22)

- https://arxiv.org/pdf/cond-mat/9804180 : arXiv preprint (author's
  manuscript), PDF, 89 pages. Fetched 2026-11-22, HTTP 200, no obstacle.
  Kind: arXiv (first in the step-5 order). Lawful.
- Publisher version (doi 10.1103/PhysRevE.58.4828): not sought; the arXiv
  copy suffices.

## Step 2: read (2026-11-22)

Provenance: arXiv v1 PDF (cond-mat/9804180v1, 16 Apr 1998), 89 pp.,
text extracted with pdftotext. Read in full: abstract and §I (pp. 1–14),
§II (pp. 14–19), §III (pp. 19–21), §IV (pp. 21–27), §V.A–B in part
(pp. 28–36: scaling analysis, RG recursions, matching), §V.C (pp. 45–51,
the d = 2 exact exponents), §V.D (pp. 51–53, d > 2), §VII (pp. 62–70),
§VIII (pp. 70–74), references. Skimmed: §V.B's correlation-function
algebra (pp. 36–45) and §VI, the anisotropic model (pp. 53–62), whose
results are read from the summary in §I (pp. 11–13). Figures not viewed.
Page numbers are the preprint's printed ones.

### Summary

A continuum ("hydrodynamic") theory of flocking: coarse-grained velocity
v(r, t) and density ρ(r, t), with the most general equations of motion
allowed by rotation invariance and conservation of bird number, without
Galilean invariance or momentum conservation (eqs. 2.6–2.8, p. 18). In
the ordered phase the speed fluctuation δv∥ is slaved to the density
gradient and dropped (eqs. 3.1–3.2, p. 19); what is left, v⊥ and δρ, is
treated first linearly (§IV) and then by the dynamical renormalization
group (§V). The linear theory loses order in d ≤ 2 as at equilibrium;
the convective nonlinearities, relevant below d = 4, restore it in d = 2,
where symmetry arguments give exact exponents. Testable predictions
(density structure factor, sound-mode dispersion and damping,
hyperdiffusive lateral wandering) and how to measure them (§VII), and a
long list of open problems (§VIII).

### Contribution

The long version of the 1995 PRL (LIT-1670): derivations in full; the
λ2, λ3 terms missed in 1995 (p. 11, ref. [8]), which leave d = 2 intact
but make d > 2 undetermined; a new, symmetry-based argument for the d = 2
exponents; an anisotropic ("easy plane") model with exact exponents for
2 ≤ d ≤ 4, including d = 3; and a measurement protocol.

### Key results

1. **Long-range order in d = 2, out of equilibrium.** Abstract (p. 2):
   "in d = 2, where we can calculate the scaling exponents exactly, flocks
   exhibit a true, long-range ordered, spontaneously broken symmetry
   state, in contrast to equilibrium systems, which cannot spontaneously
   break a continuous symmetry in d = 2 (the "Mermin-Wagner" theorem)."
   §I (p. 4): "this result does not, in fact, violate the Mermin-Wagner
   theorem, since flocks are a non-equilibrium dynamical system."
2. **The linear theory is Mermin–Wagner.** §IV (p. 27): the linear
   infrared divergence "signifies the destruction of long ranged order in
   the linearized model by fluctuations, even for arbitrarily small noise
   ∆, in spatial dimensions d ≤ 2", "very reminiscent of the familiar
   Mermin-Wagner-Hohenberg (MWH) theorem". Power counting: χ = 1 − d/2
   (eq. 5.4, p. 28); λ1, λ2, σ2 relevant for d < 4 (p. 29).
3. **The mechanism.** §I (p. 4): below d = 4 "this slow, diffusive
   transport of information is replaced by direct, convective transport
   ... There is a sort of "negative feedback," in that this improved
   transport actually suppresses the very fluctuations that give rise to
   it, leading to long-ranged order in d = 2."
4. **Exponents.** z = 6/5, ζ = 3/5, χ = −1/5 in d = 2, "exact and
   universal for all flocks with the simple symmetries we discussed"
   (eq. 1.20, p. 10). If λ2 flows to zero, ζ = (d+1)/5, z = 2(d+1)/5,
   χ = (3−2d)/5 for 2 ≤ d ≤ 4 (eq. 1.21, p. 11); for d > 2 "we do not know
   which of the above possibilities holds" (p. 12). Anisotropic model in
   d = 3: χ = −1/2, ζ = 3/4, z = 3/2 (eqs. 1.25, 1.29, pp. 13).
5. **How d = 2 is made exact (new in 1998).** In d = 2 every relevant
   vertex is ∝ q⊥ (L–T cross terms dropped as irrelevant because their
   frequency peaks do not overlap; the L–L term a total derivative), so ∆,
   D∥, Dρ are unrenormalized (z = 2ζ, z = ζ + 2χ + d − 1; eqs. 5.74–5.75,
   pp. 46–47); a "pseudo-Galilean invariance" at λ1 = λρ and exact mass
   conservation give χ = 1 − z at a "type II" fixed point (eq. 5.79,
   p. 48). That the flow reaches type II for all flocks: "We consider it
   highly probable that this is, in fact, the case" (p. 48). Then "So all
   models in d = 2 must have the canonical exponents" (p. 50).
6. **Giant density fluctuations (as a structure factor).** §I (p. 7): "at
   long wavelengths, the fluctuations of the density of birds in a flock
   become infinitely bigger than those in a fluid or an ideal gas";
   Cρ(q) "diverges as |q| → 0, unlike ... any equilibrium condensed matter
   system, which goes to a finite constant (the compressibility)" (p. 8;
   eqs. 1.10–1.11, Cρ ∝ q⊥^(−6/5) for q∥ ≪ q⊥ in d = 2).
7. **"Goldstone modes" by name.** Abstract (pp. 1–2): "The "Goldstone
   modes" associated with this "spontaneously broken rotational symmetry"
   are fluctuations in the direction of motion ... These "Goldstone modes"
   mix with modes associated with conservation of bird number to produce
   propagating sound modes."
8. **Sound modes, anomalous damping.** ω± = c±(θ)q − i q⊥^z f±(...)
   (eq. 1.14, p. 9); z < 2 for all d < 4: "sound modes are much more
   heavily damped at long wavelengths in flocks than in most equilibrium
   condensed matter systems" (p. 9).
9. **Hyperdiffusion of single birds.** w²(t) ∝ t^(2(1+χ/ζ)) = t^(4/3) in
   d = 2 (eq. 7.14, p. 68).
10. **Ordered-phase scaling is not critical scaling.** §VII (p. 64): keep
    ∆ "well below the critical value ∆c ... Otherwise, for distances
    smaller than the correlation length ξ associated with the
    order-disorder transition, the scaling properties of the flock will be
    controlled by the fixed point that controls the order-disorder
    transition, not the low temperature fixed point we have studied here."
11. **An explicit field kills the scaling.** §VII (p. 63): birds "with
    compasses" leave the universality class; "the "compass" will introduce
    a "mass" that makes any fluctuation away from the pre-picked direction
    of flock motion decay rapidly ... there are no interesting fluctuations
    left at long distances and times."
12. **A possible fixed line with order.** §V.D (p. 52), Possibility II:
    continuously varying exponents, "somewhat reminiscent of that of the
    d = 2 equilibrium X − Y model, although ... not associated in any way
    with the absence of true long ranged orientational order".
13. **No Galilean invariance.** p. 16: "birds move through a resistive
    medium, which provides a special Galilean reference frame"; "In
    contrast to the Navier-Stokes equation, there is no conservation of
    momentum" (p. 17).
14. **Tests.** p. 64: Vicsek et al. "took v0 ≪ 1, and, hence, probably
    never explored ... the long length scale regime in which our
    non-linear effects become important." p. 70: "Some of the numerical
    tests ... have been carried out recently, and good agreement with our
    prediction has been reached" (ref. [12], Tu, Toner and Ulm, not read).

### Assumptions

Rotation invariance as the only symmetry; bird number conserved;
short-ranged interactions and short-correlated Gaussian white noise
(eq. 2.9); gradient expansion to lowest order; coefficients treated as
constants though symmetry lets them depend on |v|² and ρ (pp. 19–20);
deep in the ordered phase, far from boundaries (p. 70); the
continuum equations are posited, not coarse-grained from any rule
("burying our ignorance in a few phenomenological parameters", p. 18);
universality asserted, "justified by our renormalization group treatment"
(p. 16). The d = 2 exactness rests on result 5's steps, including the
"highly probable" flow to type II.

### Concepts

Spontaneously broken continuous (rotational) symmetry; Goldstone modes;
breakdown of linearized hydrodynamics (upper critical dimension 4);
dynamical renormalization group; roughness, anisotropy and dynamic
exponents χ, ζ, z; pseudo-Galilean invariance; sound modes with
anisotropic speeds; giant density fluctuations (divergent structure
factor); hyperdiffusion; fixed line; easy-plane anisotropy.

## Step 3: verdict on the exchange's characterization

As held in LIT-2970's summary, CLAIM-841's table row and THEORY-1085's
note of 2026-11-21 (A26 §4, A27 §7):

- "active self-propelled particles in two dimensions can have true
  long-range order": **correct** (result 1), with the qualification that
  it is shown for the posited continuum model, and its exactness rests on
  result 5's steps.
- "with giant number fluctuations", "ΔN ∝ ⟨N⟩^φ with φ > ½": **right in
  substance, not in form.** The paper predicts density fluctuations
  "infinitely bigger than those in a fluid or an ideal gas" as a
  structure factor Cρ(q) that diverges as q → 0 (result 6). It never
  writes ΔN ∝ ⟨N⟩^φ, an exponent φ, or the phrase "giant number
  fluctuations" (searched). The ΔN form is a later restatement, not read
  here; do not cite LIT-2970 for that formula.
- "some initially predicted exponents differ from those obtained in
  large-scale simulations": **not in this paper.** It calls the d = 2
  exponents "exact and universal" and reports "good agreement" (result 14).
  Any revision is later work, not read.
- "In certain active systems, scaling is a property of the phase itself":
  **supported**, and more sharply than the exchange put it: the paper
  separates ordered-phase scaling from the order–disorder fixed point
  (result 10).
- The paper never uses the words "active matter" (searched); "flocks",
  "self-propelled organisms".

## Bearing on the named codes

- **CLAIM-841** (power law ≠ criticality): **supports** its "ordered active
  matter" row. Anomalous scaling (χ, ζ, z; divergent Cρ(q)) holds through
  the ordered phase, "the low temperature fixed point", distinct from the
  transition's fixed point (result 10, p. 64). Also supports the
  folded-in "A symmetry can protect scale-free fluctuations, and
  explicitly breaking that symmetry can introduce a characteristic scale"
  (A27 §6): the compass "mass" (result 11, p. 63). And it qualifies the
  "Line of fixed points (2D XY)" row: a fixed line need not mean
  quasi-long-range order (result 12, p. 52, offered only as one of three
  possibilities). Correct the row's formula and citation as above.
- **THEORY-1085** (1995 reading, Active): **supports** and extends. The
  slaving of δv∥ (eqs. 3.1–3.2, p. 19: δv∥ = −Dρ ∂∥δρ, by neglecting
  ∂tδv∥ "relative to αδv∥") matches its "eliminated degree of freedom".
  **Correction to its "What this does not say":** the 1998 paper does use
  "Goldstone modes" (result 7). The paper's universality claim is still
  posited, not derived from a rule (p. 18), as THEORY-1085 says of 1995.
- **THEORY-1095** (1995, Proposed; not named in the brief, found by grep):
  **qualifies.** Its two unproved steps (a cubic vertex staying
  irrelevant; z < 2 "on physical grounds") are not the 1998 argument; no
  "cubic" found. The 1998 d = 2 argument (result 5) needs instead: L–T
  cross terms negligible, the "highly probable" flow to the type II fixed
  point, and only λ1, λ2, σ2 among nonlinearities. Reader's observation,
  not the paper's: eq. (5.8) gives γn = n + (1 − n)d/2 = 1 for every n in
  d = 2, so every σn(δρ)^n pressure term is relevant by power counting
  there; they are ⊥ gradients, so the unrenormalization of ∆ and D∥
  survives, but the type I/II analysis treats σ2 alone. THEORY-1095's
  promote_when stands; it should cite the 1998 argument too.
- **CLAIM-842** (Mermin–Wagner on a learned graph, supposed): **parallel /
  contrast, and qualifies its scope.** The paper's linear theory has
  exactly CLAIM-842's divergence ("diverges logarithmically in the
  infra-red" in d = 2, p. 27), and the nonlinear, non-equilibrium theory
  removes it (results 1–3). So the d ≤ 2 criterion is a theorem of the
  Gaussian, equilibrium-like premise, not of the geometry alone; this
  backs CLAIM-842's own "Equilibrium" caveat with a worked case where
  relaxing it reverses the conclusion. The mechanism (convective
  transport that changes who interacts with whom) has no stated analogue
  in a training process.
- **CLAIM-798** (active-matter reading of representations): **supports**
  its last clause, that the flocking observable is velocity alignment: the
  order parameter is ⟨v⟩, "precisely analogous to the order parameter ⟨s⟩
  in a ferromagnetic system" (p. 6, eqs. 1.1–1.2). Also background for its
  "strong model": what makes a flock non-equilibrium here is self-
  propulsion through a medium, no Galilean invariance, no momentum
  conservation (result 13), and convection. Bears on nothing about
  networks.
- **QUESTION-515**: **background.** Names what an active-matter model
  would have to carry over (rotation-invariant self-propulsion, a
  conserved density, convection); says nothing about representations.

## Recheck (grep for what the reading surfaced)

Searched record/ for Goldstone, hyperdiffus*, Mermin, Galilean, dynamical
renormali*, fixed line / line of fixed points, structure factor,
self-propelled, sound mode, upper critical dimension. Entries the first
search (by the brief's codes) missed:

- **THEORY-1095** (Proposed): qualifies, as above.
- **QUESTION-508** (Open; why scale invariance without tuning): **bears
  on, partial answer for flocks.** The paper's answer is symmetry plus
  conservation: rotation invariance forbids a mass for v⊥ (a compass
  restores one, p. 63), and number conservation makes δρ slow; the RG
  fixed point is reached without tuning, deep in the ordered phase
  (p. 64). Matches A's "Symmetry removes the restoring term" bullet.
- **LEAD-209** (Open; protocol incl. response to a symmetry-breaking
  field): **supports** the row "a small symmetry-breaking field μ ... opens
  a gap" for the flock case (p. 63), and supplies measurable observables
  (Cρ(q), Cρ(q, ω) peak widths and heights, w²(t); §VII, pp. 62–70).
- **CLAIM-478** (Proposed; rate differences make constraints): **supports**,
  via the δv∥ slaving (p. 19), as THEORY-1085 already records for 1995.
- **CLAIM-846** (Proposed; scale-free correlations without heavy-tailed
  marginals): **parallel.** The flock's scale-free content is in
  correlation functions and structure factors, not in a distribution.
- **TERM-139** (relevant/irrelevant/marginal): background; the paper uses
  the terms in exactly that sense (pp. 18, 29).
- LIT-1670 / NOTE-1228 (the 1995 PRL): the predecessor; the 1998 paper
  says "in d = 2, the results of [4] are sound" (p. 11).
- No hit for "structure factor" or "upper critical dimension". Not
  relevant on inspection: LIT-2789 / NOTE-2134 (topological active
  matter, no Toner–Tu passage), LIT-638 / THEORY-088 (cortical waves).

## Limitations

- The equations are posited from symmetry, not derived from Vicsek's or
  any rule; the bridge is the universality hypothesis.
- d = 2 exactness rests on argued, not computed, steps (result 5); d > 2
  is undetermined by the authors' own account (p. 12).
- Simulations of 1998 are cited ([12]) but not shown; the paper does not
  report disagreement, and later revisions are outside it.
- Scaling functions fv, fρ, f± not calculated ("alas", pp. 7, 9).
- Bulk only: no open boundaries, no transition, no defects (§VIII).
- Reader's limits: §V.B's algebra and §VI skimmed; figures not viewed.

## Candidate THEORY

Sentence: "In Toner and Tu's continuum theory of flocking, the ordered
phase of a rotation-invariant, number-conserving flock without Galilean
invariance has anomalous scaling throughout the phase, not only at its
transition: below four dimensions convective nonlinearities replace
diffusive transport, so that the long-range orientational order the
linearized theory loses in two dimensions, as at equilibrium, survives,
with exponents z = 6/5, ζ = 3/5, χ = −1/5 argued to be exact there, and
density fluctuations whose structure factor diverges as q → 0, unlike
any equilibrium fluid's; an explicit preferred direction removes the
anomalous fluctuations."

promote_when: "A controlled calculation or finite-size simulation of a
Vicsek-class model in d = 2, well below the order–disorder transition,
showing (a) ⟨|v⊥|²⟩ bounded as the system grows and (b) Cρ(q) growing
without bound as q → 0 in the ordered phase; the exactness of the three
exponents is not required for promotion and should be held separately
(cf. THEORY-1095)."

(Alternative, if the filer prefers to keep the 1995 readings narrow: file
only the d = 2 argument of result 5 as a revision note on THEORY-1095 and
the density-fluctuation and ordered-phase-vs-transition results as this
work's THEORY.)

## Copies located (final)

- https://arxiv.org/pdf/cond-mat/9804180 — arXiv preprint, PDF, read
  2026-11-22, no obstacle. Lawful (arXiv).
- doi:10.1103/PhysRevE.58.4828 — publisher version, not sought.
No neighbours were needed or read. No other work was read or quoted;
refs [4], [5], [12] are named from the paper's bibliography only.
No email address was sent anywhere.
