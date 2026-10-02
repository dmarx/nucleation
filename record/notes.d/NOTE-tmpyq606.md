---
status: Read
paper: LIT-tmptpgzu
title: 'The Chemical Basis of Morphogenesis'
version: 1
history:
- version: 1
  date: '2026-10-02'
  note: >-
    Read in full (the JSTOR scan of the published article on a Caltech
    course page; the Royal Society's PDF refused the session with HTTP
    403). Abstract, §§1–13 and the references. Displayed equations are lost
    in the scan's OCR, so the page images of printed pp. 37, 55, 58 and 60
    were read for (9.4a, b), (9.5)–(9.7), the non-linear amplitude
    equations and the §10 data. The ring equations
    (6.1)–(6.11), the three-morphogen determinants (8.4)–(8.6), the noise
    formulae (9.8)–(9.17) and the §12 spherical-harmonic solution were read
    for their argument, not checked symbol by symbol.
date: '2026-10-02'
summary: >-
  Turing's reaction–diffusion theory of pattern. Linearize about a
  homogeneous steady state of M morphogens on a ring of N cells: each
  Fourier mode grows or decays independently, and the fastest-growing one
  sets the pattern. Six forms of onset are possible. For two morphogens,
  stationary waves of finite wave-length need bc < 0 and
  4√(μ′ν′)/(μ′+ν′) < (d−a)/√(−bc) < (μ′+ν′)/√(μ′ν′) (9.4a), with
  instability if d√(μ′/ν′)/√(−bc) − a√(ν′/μ′)/√(−bc) > 2 (9.4b). These
  cannot both hold when μ′ = ν′. A computed 20-cell ring gives three lobes.
---
<!-- inactive-ok-file: LIT-tmpd737a — Deferred, no lawful full text; Nicolis & Prigogine, named as where the Brusselator's Turing bifurcation is worked out, not leaned on -->

# NOTE-tmpyq606: The Chemical Basis of Morphogenesis

## Contribution

Before this paper, a spherically symmetric blastula developing by chemistry
and diffusion looked as if it must stay symmetric forever (§4). After it,
there is a mechanism by which it need not. Diffusion, usually a smoothing
process, can destabilize a homogeneous steady state of reacting chemicals,
and the instability amplifies whatever small disturbances are present into
a pattern. The paper:

- classifies the linear onset of such instabilities on a ring;
- gives exact conditions for the two-morphogen cases;
- treats noise acting continuously during a slow approach to instability;
- computes a non-linear example to its final pattern on the Manchester
  computer;
- extends the analysis to a sphere.

## Key insight

The homogeneous state is stable to uniform disturbances, but it need not be
stable to disturbances of a particular wave-length. When two substances react
and diffuse at different rates, a mode of finite wave-length can grow while
uniform and very short modes decay. The pattern's spacing is then set by the
chemistry (the "chemical wave-length"), and only its phase or orientation by
the accidental disturbance, "like an upright stick falling over" (p. 66). The
sustained pattern is a dynamic steady state, maintained by free energy
flowing from fuel to waste (p. 66).

## Assumptions

- **Model.** Tissue is either a ring of N cells, each well mixed, or a
  continuous ring (or, in §12, a thin spherical shell). Mechanics and growth
  are set aside; the chemistry is the subject (§1).
- **Kinetics.** Mass-action kinetics, reaction rates f(X, Y), g(X, Y); "fuel"
  substances such as A are held at large constant concentration (§10).
- **Linearity assumption.** Departures from homogeneity are small enough to
  linearize: f ≈ ax + by, g ≈ cx + dy with "marginal reaction rates" a, b, c,
  d (§6). The paper calls this assumption "a serious one" (p. 66).
- **Diffusion.** Cell-to-cell diffusion constants μ, ν (continuous ring μ′,
  ν′). In §9 it is assumed that ν′ ≤ μ′ > 0. If μ′ = ν′ = 0 "there is no
  co-operation between the cells whatever" (p. 55).
- **Disturbances.** In §§6–8 the state at t = 0 is displaced by
  disturbances, which are then ignored. §9(2) drops this and treats white
  noise of constant amplitude while the marginal rates drift slowly.
- **Chance relations excluded.** The analysis assumes no special parameter
  relations making several modes equally unstable (§8).

## Key results

- **Separation of modes (§§6–7).** Fourier transforming round the ring
  separates the 2N equations into pairs. Mode s grows as e^{p_s t}, with
  p_s a root of (p − a + 4μ sin²(πs/N))(p − d + 4ν sin²(πs/N)) = bc (6.8; in
  the continuum (p − a + μ′U)(p − d + ν′U) = bc, 9.1, with U the squared
  wave-number).
- **Six types of onset (§8).** After a lapse of time the mode with the
  largest Re p dominates:
  - (a) stationary, extreme long wave-length: each cell drifts as if
    isolated;
  - (b) oscillatory, extreme long wave-length: synchronized oscillation;
  - (c) stationary, extreme short wave-length: neighbouring cells drift in
    opposite directions;
  - (d) stationary waves of finite wave-length, "the case which is of
    greatest interest";
  - (e) oscillatory, finite wave-length: travelling waves, which need three
    or more morphogens;
  - (f) oscillatory, extreme short wave-length: neighbouring cells about 180°
    out of phase, which also needs three or more.
  Each is shown to occur with explicit parameter values.
- **Conditions for case (d) (p. 55).** bc < 0 and
  4√(μ′ν′)/(μ′+ν′) < (d−a)/√(−bc) < (μ′+ν′)/√(μ′ν′) (9.4a). Instability
  requires in addition (d/√(−bc))√(μ′/ν′) − (a/√(−bc))√(ν′/μ′) > 2 (9.4b).
  - My derivation, not stated in the paper: with μ′ = ν′, (9.4a) requires
    1 < (d−a)/√(−bc) < 2, while (9.4b) requires (d−a)/√(−bc) > 2. So with two
    morphogens, equal diffusibilities cannot give unstable stationary waves.
    The paper's §10 example uses diffusion constants of 5×10⁻⁸ and
    2.5×10⁻⁸ cm² s⁻¹.
- **Noise (§9(2)).** When instability sets in gradually, only disturbances
  near the moment of zero instability matter ultimately. Earlier ones are
  damped; later ones have less time to grow. Turing compares this to the
  superregenerative receiver.
- **Non-linearity (§9(4)).** With quadratic terms the amplitude of the
  leading mode obeys dz₁/dt = p₁z₁ − kz₁³. For k > 0 growth saturates at
  √(p₁/k); for k < 0 it is "catastrophic", and in two dimensions it "is almost
  universal".
- **Worked example (§10).** 20 cells of 0.1 mm diameter; the reaction set
  given in special units; the computed incipient and final patterns (Table 1,
  Fig. 3). With γ = 0, s₀ = 3.333 predicts a three-lobed pattern, the
  four-lobed one being the closest competitor (p₃ − p₄ = 0.0084, about 33 h
  to gain a factor e). Slow "cooking" gives three lobes reliably; fast
  "cooking" gives irregular incipient patterns and sometimes four lobes.
  Growth is halted when Y reaches zero in some cells. The final equilibria
  are "only dynamic equilibria … in order to maintain the wave pattern a
  continual supply of free energy is required" (pp. 65–66).
- **Sphere (§12).** On a growing blastula the degree-1 harmonic is first to go
  unstable, giving an axially symmetric pattern about a random axis, which
  is offered as a mechanism for gastrulation.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Reaction plus diffusion can destabilize a stable homogeneous state into a spatial pattern | strong | linear analysis §§6–9; worked example §10 |
| C2 | On a ring there are exactly six types of onset, (e) and (f) needing three or more morphogens | strong for the linear, generic case | §8 examples; §9 conditions for (a)–(d) |
| C3 | Stationary finite-wave-length patterns (case d) occur under (9.4a, b); with two morphogens this needs unequal diffusibilities | strong (the conditions); the corollary is mine, by substitution | p. 55 |
| C4 | The pattern's spacing is a "chemical wave-length" set by reaction and diffusion constants, not by tissue size | strong in the linear regime | §8, (9.3) |
| C5 | Only disturbances near the moment instability begins have lasting effect | moderate | approximation (9.17) under stated conditions |
| C6 | In two dimensions the non-linear instability is almost always catastrophic | asserted | §9(4), no derivation given |
| C7 | The resulting patterns are dynamic equilibria needing a continual supply of free energy | strong as a physical remark | pp. 65–66 |
| C8 | The mechanism may account for Hydra tentacles, whorled leaves, dappling, phyllotaxis and gastrulation | suggestion | §§11–12; "It must be admitted that the biological examples … are very limited" (p. 72) |

## Concepts

- **morphogen**: a "form producer", any substance whose reaction and
  diffusion figures in the theory. Genes are a special, non-diffusing
  case; hormones and evocators are typical ones (p. 38).
- **marginal reaction rates**: the entries of the linearized reaction matrix
  at the homogeneous equilibrium; dimension of reciprocal time (p. 47).
- **chemical wave-length**: the limiting wave-length as the ring is enlarged,
  or the one giving the largest instability (p. 51).
- **instability (I)**: the real part of the dominant p (p. 51).
- **equilibrium**: Turing's word for a steady state, including the
  non-uniform "dynamic equilibria" of §10. It is not thermodynamic
  equilibrium.

## Connections

- **Prigogine's Nobel lecture ([LIT-tmp452jw](../literature.d/LIT-tmp452jw.md)), read.** The lecture names the
  stationary diffusive instability of the Brusselator the "Turing
  bifurcation" and credits this paper as the first to see it. The two
  frameworks meet at one point. Turing's case (d) is a bifurcation from the
  "thermodynamic branch", and his remark that the pattern needs a continual
  supply of free energy is the defining property of a dissipative structure.
  Turing gives no entropy-production analysis; his criterion is purely
  kinetic, which is in line with the lecture's own conclusion that far from
  equilibrium "the form of chemical kinetics plays an essential role".
- **Nicolis and Prigogine ([LIT-tmpd737a](../literature.d/LIT-tmpd737a.md)), Deferred.** The lecture cites its
  ch. VII for the Brusselator, the Brussels school's standard example of
  Turing's case (d).
- **Cross and Hohenberg ([LIT-tmpht8ga](../literature.d/LIT-tmpht8ga.md)), skimmed.** Their type-I_s
  instability (finite wave-vector, zero frequency) is Turing's case (d), and
  they credit this paper as first to connect macroscopic pattern formation
  with linear instabilities (fn. 1.1). They report the first stationary
  chemical Turing patterns, 1989–1991, and record that the identification of
  actual morphogens "has proved elusive" (§XI.A).
- **The Belousov–Zhabotinsky reaction ([LIT-tmpoej2u](../literature.d/LIT-tmpoej2u.md)), read.** Turing guessed
  at travelling waves (case e) but could cite only a spermatozoon's tail. BZ
  waves are the later chemical realization of travelling concentration
  waves, though of the excitable, strongly non-linear kind his linear theory
  does not describe. Zhabotinsky's review records that BZ in microemulsion
  produces genuine Turing structures.
- **Primitive metabolic cycles ([LIT-036](../literature.d/LIT-036.md)), read.** As [NOTE-079](NOTE-079.md) records, its
  authors contrast their non-reciprocal catalytic mechanism with Turing
  patterning. The method, linearizing about a homogeneous state and reading
  the growing mode off the eigenvalues, is the one this paper introduced.
- **Bioelectric selves ([LIT-439](../literature.d/LIT-439.md)), read.** Levin's account of how cells
  coordinate into larger "Selves" by bioelectric signalling is an
  alternative to diffusing chemical morphogens as the carrier of positional
  information. The two are not in dispute: Turing explicitly sets aside
  "electrical properties" (p. 38).

## Bearing on the record

- **[LIT-192](../literature.d/LIT-192.md) (demarcation).** The paper's mechanism is the same in an embryo
  and in an unstirred reactor. That is a direct case of what Nahas and Sachs
  report: dissipative pattern formation cannot be what demarcates organisms
  from candle flames, because it is shared. It is also a case of the
  "scientific orientation" they describe, an operational model that is
  explicitly "a simplification and an idealization, and consequently a
  falsification" (p. 37) and makes no metaphysical claim about organisms.
- **[LIT-211](../literature.d/LIT-211.md) ("Dissipative Self-Organizing Systems").** The paper supplies one
  of that cluster's paradigm mechanisms (spontaneous order in a
  free-energy-fed chemical system). It also shows the mechanism's limits as
  a mark of life: Turing's own examples are pattern-forming steps inside
  organisms, not definitions of them.
- **No THEORY is indicated by this reading alone. No ML instruction.**

## Limitations

- **Linear and near onset.** Everything except §10 is a linearization about
  homogeneity. The paper says the linearity assumption "is a serious one",
  justified only by the hope that early patterns resemble later ones (p. 66),
  and that most of development is "from one pattern into another, rather than
  from homogeneity into a pattern" (pp. 71–72).
- **Imaginary chemistry.** No real reactions are identified; the §10
  reactions are chosen to give the required rates (p. 60).
- **Biology by suggestion.** Turing concedes the biological examples are
  "very limited" (p. 72). No experiment is reported.
- **One and two dimensions only in part.** The two-dimensional theory is
  "not expounded here" (p. 69), and phyllotaxis is deferred to a later paper.

## Open questions

- Which real morphogens, if any, implement case (d) in development? The
  paper leaves this open, and Cross and Hohenberg report it as still open in
  1993.
- What governs the transition from one pattern to another far from
  homogeneity? Turing proposes digital computation of particular cases
  (p. 72).
- Does the catastrophic non-linear instability (§9(4)) generically select a
  different pattern from the linear one?

## Corrections

- none to a seeded skim (there was no seed)
- **Citation details.** The brief's citation is right: Phil. Trans. R. Soc.
  Lond. B 237(641):37–72, published 14 August 1952; the DOI is
  10.1098/rstb.1952.0012. The full series title is "Philosophical
  Transactions of the Royal Society of London. Series B, Biological
  Sciences".
- **"Turing pattern" requires unequal diffusion.** This is often stated as
  Turing's result. The paper states (9.4a, b) and leaves the corollary
  implicit; the derivation above is mine.
- **A subscript slip on p. 58.** The reduced amplitude equation is first
  printed "dz₁/dt = p₀z₁ − kz₁³" and, a few lines later, "dz₁/dt = p₁z₁ − kz₁³".
  The second is the one consistent with the equations just above it and with
  the saturation value √(p₁/k).
