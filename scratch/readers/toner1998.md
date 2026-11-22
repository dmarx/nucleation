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
