---
number: 424
status: Read
formerly:
- NOTE-tmprrlww
paper: LIT-516
title: 'Time, Structure and Fluctuations'
version: 2
history:
- version: 1
  date: '2026-10-02'
  note: >-
    Read in full (the Nobel Lecture PDF on nobelprize.org, printed pp.
    263–285, all eight sections, the abstract and the 28 references). The
    PDF's text layer drops several passages and all displayed equations,
    so the page images of pp. 263, 265, 266, 268, 269, 271, 275, 279, 280
    and 282 were read to recover them; the Poisson and Boltzmann formulas
    of pp. 274 and 277–278 were not checked against images. The Science
    reprint (1978) was not seen. Results the lecture cites to Glansdorff
    and Prigogine (1971), Nicolis and Prigogine (1977) and the Brussels
    papers are taken as stated; neither monograph was reachable.
- version: 2
  date: '2026-10-03'
  note: >-
    The candidate THEORY in the bearing section is now covered:
    THEORY-tmpm2o1r, sourced to the organisational readings, cites this
    lecture for the dissipative structures.
date: '2026-10-02'
summary: >-
  Prigogine's Nobel statement. Near equilibrium δ²S < 0 with ½∂δ²S/∂t = P > 0
  makes δ²S a Lyapounov function, and in the strictly linear regime
  (constant L_ρρ′) the steady state minimizes entropy production. Far from
  equilibrium ½∂δ²S/∂t = ΣδJ_ρδX_ρ has no fixed sign, and ΣδJδX ≥ 0 is
  offered only as a sufficient stability condition. The Brusselator goes
  unstable at B > 1 + A². Dissipative structures are instabilities of the
  thermodynamic branch, triggered by fluctuations and sustained by
  exchange with the outside. The microscopic §§6–7 is a programme, linked
  to macroscopic thermodynamics only "in the linear region".
---
<!-- inactive-ok-file: THEORY-tmpm2o1r — Proposed; named as the account that now covers this note's candidate, nothing here rests on it -->
<!-- inactive-ok-file: LIT-537 — Deferred, no lawful full text; Glansdorff & Prigogine, cited as the source the lecture defers its proofs to, and for its own p. 108 sentence quoted in Cross & Hohenberg -->
<!-- inactive-ok-file: LIT-524 — Deferred, no lawful full text; Nicolis & Prigogine, cited as the source of the Brusselator chapter the lecture defers to -->
<!-- inactive-ok-file: THEORY-026 — Proposed; named to say this lecture does not bear on it -->

# NOTE-424: Time, Structure and Fluctuations

## Contribution

The lecture is a survey of the Brussels school's results, not a new result.
It puts three things in one place:

- the thermodynamic stability theory of Glansdorff and Prigogine
  ([LIT-537](../literature.d/LIT-537.md)), with the second-order excess entropy δ²S as a Lyapounov
  function and the excess entropy production as the far-from-equilibrium
  stability test;
- the chemical case, through the Brusselator and its Hopf and "Turing"
  bifurcations (detailed in Nicolis and Prigogine, [LIT-524](../literature.d/LIT-524.md));
- the stochastic case: near an instability the law of large numbers fails
  and fluctuations become long-range correlated.

It closes with a programme (§§6–7) for deriving irreversibility from
dynamics through a non-unitary, "star-unitary" transformation.

## Key insight

Equilibrium thermodynamics has potentials whose extrema are attractors, and
near equilibrium the linear theory keeps one: entropy production is minimized
at the steady state, and every fluctuation decays. Far from equilibrium that
guarantee lapses, because the sign of the excess entropy production depends
on the kinetics. Where it goes negative, a fluctuation can grow into a new
macroscopic state that is maintained only by the flows through the system.
That state is the dissipative structure. Its form depends on global features
such as size, shape and boundary conditions, and which branch it takes at a
bifurcation depends on which fluctuation happened. So the lecture locates
"history" in physics at bifurcations.

## Assumptions

- **Local equilibrium** (§2, p. 265): entropy depends on the same variables
  outside equilibrium as at equilibrium. The lecture says the explicit
  entropy production P = d_iS/dt = Σ_ρ J_ρ X_ρ ≥ 0 (2.3) "can only be
  established in some neighborhood of equilibrium" (p. 266).
- **Linear regime**: J_ρ = Σ L_ρρ′ X_ρ′ (2.5), with Onsager symmetry
  L_ρρ′ = L_ρ′ρ (2.6).
- **Strictly linear regime** for minimum entropy production: "the
  phenomenological coefficients L_ρρ′ may be treated as constants" (p. 266).
- **Macroscopic description** for the stability theory: δ²S < 0, from the
  Gibbs conditions C_v > 0, χ > 0 and Σ μ_γγ′ δN_γ δN_γ′ > 0 (3.2, p. 268),
  is assumed to hold "in the range of macroscopic description" also around
  non-equilibrium states (p. 269).
- **Chemistry**: mass-action kinetics, with the initial and final products
  A, B, D, E of the Brusselator "maintained constant" (p. 271). That is,
  the system is open to matter.
- **Stochastic model** (§5): birth-and-death Markov chains with a master
  equation (5.6) whose transition rates are non-linear in occupation
  numbers.
- **Microscopic programme** (§7): the existence of a positive operator M
  with Ω = tr ρ†Mρ ≥ 0 and dΩ/dt ≤ 0 (7.1–7.2) is assumed. The lecture
  states this "is certainly not always possible" (p. 279) and ties it to the
  spectrum of the Liouville operator (Misra).

## Key results

- **Minimum entropy production (§2, pp. 266–267).** "For steady states
  sufficiently close to equilibrium entropy production reaches its minimum.
  Time-dependent states (corresponding to the same boundary conditions) have
  a higher entropy production." It "requires even more restrictive conditions
  than the linear relations (2.5)". It "is strictly valid only in the
  neighborhood of equilibrium", and far from equilibrium behaviour can be
  "even opposite to that indicated by the theorem". Entropy production is a
  Lyapounov function "in the strictly linear region around equilibrium" only
  (p. 268). No proof is given; ref. 6 is Prigogine 1945.
- **Near-equilibrium stability (§3).** S = S₀ + δS + ½δ²S (3.1). δ²S < 0
  (3.2), and ½ ∂δ²S/∂t = Σ J_ρ X_ρ = P > 0 (3.4). So δ²S is a Lyapounov
  function near equilibrium "independently of the boundary conditions", and
  it "ensures the damping of all fluctuations".
- **Far-from-equilibrium criterion (§3, p. 269).** Around a non-equilibrium
  steady state ½ ∂δ²S/∂t = Σ δJ_ρ δX_ρ (3.5), the "excess entropy
  production", which "has generally not a well-defined sign". If
  Σ δJ_ρ δX_ρ ≥ 0 for all t > t₀ (3.6), δ²S is a Lyapounov function and the
  state is stable. This is a sufficient condition. Its violation is not shown
  to imply instability.
- **Convection (§2, §3).** Beyond a critical adverse temperature gradient the
  Bénard layer convects, and "the entropy production is then increased as the
  convection provides a new mechanism of heat transport" (p. 267). Internal
  convection "cannot be generated from a state at rest which is at
  thermodynamic equilibrium" (p. 270).
- **Chemistry (§4).** Autocatalytic steps are "necessary (but not
  sufficient)" for instability of the thermodynamic branch (p. 271).
  - The Brusselator: A → X, 2X + Y → 3X, B + X → Y + D, X → E (4.1). With
    unit rate constants, dX/dt = A + X²Y − BX − X and dY/dt = BX − X²Y (4.2).
    The steady state X₀ = A, Y₀ = B/A (4.3) is unstable when B > B_c = 1 + A²
    (4.4), beyond which there is a limit cycle (a Hopf bifurcation) whose
    frequency, unlike Lotka–Volterra's, is fixed by the macroscopic
    parameters: "a chemical clock".
  - With diffusion (4.5) there are non-uniform steady states, which the
    lecture calls the "Turing bifurcation" after Turing 1952 ([LIT-535](../literature.d/LIT-535.md)),
    and chemical waves.
  - Dissipative structures generally require the system's size to exceed a
    critical value (p. 272).
- **Fluctuations (§5).** For a non-linear chain (5.8) the stationary
  distribution is not Poisson (Nicolis and Prigogine 1971). Near the critical
  point of the Schlögl model the variance ⟨(δX)²⟩ grows as a higher power of
  the volume than the first (p. 275). In a box model of the Brusselator,
  spatial correlations become long-range near the instability (Figs.
  5.1–5.3), and oscillation onset is described as time-symmetry breaking
  (p. 277).
- **Microscopic irreversibility (§§6–7).**
  - Ω = tr ρ†ρ is conserved by Liouville dynamics (6.6–6.7), so it is not
    a Lyapounov function.
  - Writing M = (Λ⁻¹)†Λ⁻¹ (7.3) and ρ̃ = Λ⁻¹ρ (7.5) gives a new equation of
    motion iρ̃_t = Φρ̃ with Φ = Λ⁻¹LΛ (7.6–7.7). Its even part under L-inversion
    is the "entropy production" (7.17–7.18).
  - "Microscopic entropy production" is the commutator i(ML − LM) (7.9).
  - The link back to macroscopic δ²S is established "at least in the linear
    region" (p. 283, Theodosopulu, Grecos and Prigogine 1978).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Near equilibrium δ²S is a Lyapounov function, so fluctuations are damped | strong (standard), derivation cited | (3.2), (3.4); Glansdorff & Prigogine ch. V |
| C2 | Minimum entropy production holds only for steady states in the strictly linear regime with constant L_ρρ′ | strong as a statement of scope; theorem not proved here | p. 266, ref. 6 |
| C3 | Far from equilibrium the excess entropy production has no fixed sign; ΣδJδX ≥ 0 suffices for stability | moderate: the sufficiency follows from (3.2) and (3.5); generality of (3.5) is cited | (3.5)–(3.6), ch. VII of ref. 7 |
| C4 | Autocatalytic steps are necessary but not sufficient for chemical instability of the thermodynamic branch | asserted, with the Brusselator as a worked case | p. 271 |
| C5 | The Brusselator steady state is unstable for B > 1 + A² | strong (linear stability, checkable) | (4.4) |
| C6 | Dissipative structures are "giant fluctuations" amplified past an instability and stabilized by exchange with the outside | interpretive | p. 267 |
| C7 | Near a non-equilibrium instability the law of large numbers fails and correlations become long-range | moderate: model calculations and simulations cited | §5, refs 17, 19, 20 |
| C8 | Bifurcation introduces "history" into physics | interpretive | p. 273 |
| C9 | Irreversibility can be derived from dynamics by a non-unitary transformation, without coarse-graining | weak here: a programme, with existence of M assumed and the macroscopic link shown only near equilibrium | §§6–7, p. 283 |

## Concepts

- **dissipative structure**: "a new type of dynamic states of matter" that
  irreversible processes may produce (p. 263). In Bénard convection it is "a
  new supermolecular order … which corresponds basically to a giant
  fluctuation stabilized by exchanges of energy with the outside world"
  (p. 267). The lecture always links three aspects: "the function as
  expressed by the chemical equations, the space-time structure, which
  results from the instabilities, and the fluctuations, which trigger the
  instabilities" (p. 272).
- **thermodynamic branch**: the family of steady states continuous with
  equilibrium, from which dissipative structures bifurcate (p. 272).
- **excess entropy production**: Σ δJ_ρ δX_ρ, the perturbation of the
  entropy production about a steady state (3.5).
- **order through fluctuations**: the amplification of a fluctuation at an
  instability into a macroscopic state (p. 272).
- **local equilibrium**: entropy outside equilibrium depends on the same
  variables as at equilibrium (p. 265).
- **star-unitary transformation**: the non-unitary Λ connecting the
  dynamical and "thermodynamic" representations (7.13–7.16).

## Connections

- **Turing 1952 ([LIT-535](../literature.d/LIT-535.md)), read.** The lecture names the stationary
  diffusive instability of the Brusselator the "Turing bifurcation" and cites
  Turing as "the first to notice the possibility of such bifurcations in
  chemical kinetics" (p. 272). Turing had no thermodynamic stability
  criterion, but he did say that his patterns need "a continual supply of
  free energy" (Turing p. 66).
- **The Belousov–Zhabotinsky reaction ([LIT-531](../literature.d/LIT-531.md)), read.** It is not named
  in the lecture. The "chemical clock" of §4 is the Brusselator, a model, and
  the experimental chemical example the lecture gestures at is "oscillatory
  enzymes". Zhabotinsky's own review credits Nicolis and Prigogine 1977 with
  the point that sustained oscillations need distance from equilibrium.
- **Cross and Hohenberg 1993 ([LIT-527](../literature.d/LIT-527.md)), skimmed.** They file "dissipative
  structures" (citing Nicolis and Prigogine) as one name for macroscopic
  steady-state structure under constant non-equilibrium conditions. In their
  conclusion they quote Glansdorff and Prigogine's own admission that "the
  search for a universal kinetic potential has proved to be unsuccessful"
  (1971, p. 108), and find no evidence for a global minimization principle
  beyond a perturbative one near threshold. That matches the lecture's own
  restriction of minimum entropy production to the strictly linear regime.
- **Observational entropy ([LIT-082](../literature.d/LIT-082.md)), read.** The two stand on opposite sides of
  one question. [LIT-082](../literature.d/LIT-082.md) makes entropy relative to a measurement, that is, a
  coarse-graining. The lecture rejects coarse-graining as the source of
  irreversibility ("Can dissipative structures be the result of mistakes?",
  p. 279) and looks for a Lyapounov functional in the dynamics itself.
- **Thermodynamics of prediction ([LIT-327](../literature.d/LIT-327.md)) and [THEORY-026](../theory.d/THEORY-026.md).** No overlap. The
  lecture's entropy production is the macroscopic local-equilibrium sum
  ΣJ_ρX_ρ. [LIT-327](../literature.d/LIT-327.md) computes dissipation for a stochastic system driven
  through a Markov kernel, a different regime and a different quantity, so
  this reading neither supports nor tests [THEORY-026](../theory.d/THEORY-026.md).
- **Emergence surveys ([LIT-021](../literature.d/LIT-021.md), [LIT-141](../literature.d/LIT-141.md)).** [NOTE-007](NOTE-007.md) records that [LIT-021](../literature.d/LIT-021.md)'s
  history of emergence names Prigogine. The lecture supplies what that name
  stands for. [LIT-141](../literature.d/LIT-141.md)'s "self-organisation" characteristic, which it counts
  as subjective, is here given an objective criterion, but only for the
  onset (instability of a steady state), not for the organisation that
  follows.
- **Primitive metabolic cycles ([LIT-036](../literature.d/LIT-036.md)), read.** It is a modern instance of
  the lecture's chemistry: a non-equilibrium, catalytic cycle whose
  homogeneous state goes unstable, giving aggregation or oscillation. It
  uses linear stability of a homogeneous state, as the lecture does, and no
  entropy-production principle.
- **Teleology and the definition of life ([LIT-192](../literature.d/LIT-192.md), [LIT-211](../literature.d/LIT-211.md)).** See Bearing
  on the record.

## Bearing on the record

- **[LIT-192](../literature.d/LIT-192.md)'s demarcation dispute.** The lecture's definition is the
  dissipative-structure side of the line Nahas and Sachs discuss. Its
  criterion is physical: an open system, held away from equilibrium, whose
  steady state has lost stability, maintained by flows across its boundary.
  Bénard cells and the Brusselator meet it. So does a candle flame on the
  same terms (my inference: the lecture does not discuss flames), and so,
  by the lecture's own §1, do living systems. Nothing in the lecture
  separates teleological systems from other dissipative structures. That
  supports the reading in [NOTE-094](NOTE-094.md) that the demarcation has to be drawn by
  something added to thermodynamics (closure of constraints, Deacon's
  teleodynamics), not read off it.
- **[LIT-211](../literature.d/LIT-211.md)'s "Dissipative Self-Organizing Systems" cluster.** The 21
  definitions in it lean on exactly this picture. The lecture shows what the
  picture does and does not supply. It supplies a necessary physical
  condition: far from equilibrium, flux-maintained, instability-born order.
  It does not supply a sufficient one for life, since the canonical
  dissipative structures (convection rolls, chemical clocks) are not alive.
- **No THEORY is indicated by this reading alone.** A candidate, "being a
  dissipative structure in Prigogine's sense is necessary but not sufficient
  for being alive or goal-directed", would need the parallel filings on the
  life-as-dissipation literature to source it. Those filings now source
  [THEORY-tmpm2o1r](../theory.d/THEORY-tmpm2o1r.md), which holds that organisms differ from dissipative
  structures by closure among differentiated constraints, and cites this
  lecture for the structures themselves.
- **No ML instruction.** Nothing here belongs in the anthology.

## Limitations

- **A lecture, not a derivation.** Minimum entropy production, the
  δ²S stability results and the general form (3.5) are stated and cited to
  ref. 6 and Glansdorff and Prigogine, not proved.
- **The far-from-equilibrium criterion is one-sided.** (3.6) is sufficient
  for stability. The lecture does not claim its failure gives instability,
  and gives no positive principle selecting which dissipative structure
  appears; it hands that to the kinetics and to fluctuations.
- **"Functional order" in towns and living systems is asserted in §1**, not
  analysed. No biological system is modelled.
- **The microscopic programme is incomplete by its own account.** The
  existence of M is assumed, and the identification with δ²S is shown only
  for small deviations from equilibrium and only for conserved quantities
  (p. 283).

## Open questions

- Is there a variational principle, of any form, for steady states far from
  equilibrium? The lecture offers none. This is the question the parallel
  filings on entropy-production principles take up.
- Does the failure of (3.6) imply instability in the systems the lecture
  names, or only permit it?
- Does a positive entropy operator M exist for physically realistic
  (non-integrable, large) systems, and does the star-unitary picture reach
  beyond the linear regime?

## Corrections

- none to a seeded skim (there was no seed)
- **Citation.** The Science reprint is titled "Time, Structure, and
  Fluctuations" (with a serial comma), Science 201(4358):777–785, published
  September 1978 per Crossref. The lecture PDF prints it without the comma.
  The brief's citation is otherwise right.
- **Bénard convection.** The lecture describes the Bénard instability as
  buoyancy-driven, a fluid layer heated from below "in a constant
  gravitational field" (p. 267). Cross and Hohenberg ([LIT-527](../literature.d/LIT-527.md), §II.B.3)
  note that Bénard's own 1900 open-dish hexagons were later shown (Pearson
  1958) to be driven by temperature-dependent surface tension. The
  lecture's idealization is Rayleigh's problem, not Bénard's experiment.
- **Reference slips in the printed lecture.** Ref. 7 spells the first author
  "Glandsdorff"; ref. 13 prints "Thorn" for Thom; ref. 3 gives the
  monograph's title as "Thermodynamics of Structure, Stability and
  Fluctuations", where the book's title is "Thermodynamic Theory of
  Structure, Stability and Fluctuations".
