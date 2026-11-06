---
status: Read
paper: LIT-tmp8ut7r
title: 'Grelu and Akhmediev — Dissipative solitons for mode-locked lasers'
version: 1
history:
- version: 1
  date: '2026-11-06'
  note: >-
    Read in full on 2026-11-06 from the authors' accepted manuscript on HAL,
    hal-04901011v1 (https://hal.science/hal-04901011, file "Dissipative
    Solitons Review Manuscript_NPHOT-2011-06-00518B_2.pdf"), deposited
    2025-01-29 under CC BY 4.0 and found through the HAL search API and
    OpenAlex. It is the author version with revision marks (some sentences
    in blue), not the typeset Nature Photonics article, so its wording may
    differ from the journal's. 32 PDF pages: the HAL cover, 25 manuscript
    pages of text and references, and 6 figure pages. Text extracted by
    pdftotext. The cubic–quintic CGLE on manuscript p. 6 is garbled in
    extraction and is taken here from the rendered page; Fig. 1a (p. 26) was
    read from the rendered image. Read: abstract, text, figure captions.
    Not read closely: the reference list, consulted only for refs. 6, 8 and
    9. Page numbers below are the manuscript's printed numbers (PDF page
    minus one).
date: '2026-11-06'
summary: >-
  A review by two of the concept's main authors. A conservative soliton
  balances nonlinearity against dispersion alone and is one of a family
  selected by the initial data; a dissipative soliton is a single attractor,
  its energy, profile and chirp fixed by the parameters, held by an exact
  gain–loss balance with continuous exchange and an internal energy flow.
  Bound states are robust, exploding solitons return to their shape, new
  solitons nucleate from noise above a fluctuation threshold, and cavity
  solitons are written and erased by a transient beam. No pump existence
  threshold, bistability or hysteresis is discussed.
---
<!-- inactive-ok-file: LIT-1642 LIT-524 LIT-tmp7lcfh LIT-tmpwjm3u THEORY-tmphrwgv THEORY-1429 THEORY-1343 THEORY-072 TERM-088 CLAIM-597 CLAIM-600 CLAIM-604 — Proposed, Unfetched, Unavailable or new; cited from the reading of Grelu and Akhmediev (2012) as open -->

# NOTE-tmp3nwf3: Grelu and Akhmediev — Dissipative solitons for mode-locked lasers

## Contribution

A short statement of what separates dissipative solitons from conservative
ones, applied to passively mode-locked lasers as the experimental testbed. A
dissipative soliton is an attractor fixed by the equation's parameters
rather than an initial-condition-selected member of a family; it needs a
supplied, exact gain–loss balance with an internal flow of energy; and its
bound states are robust where conservative higher-order solitons are not.
It is a review: theory, simulation and experiment surveyed, no new results.

## Key insight

A conservative soliton is one of "a family comprising an infinity of soliton
solutions", which one being chosen by where the system starts; a dissipative
soliton is "a fixed localised solution", the same whatever the start, held
by a "composite balance" in which gain against loss "plays a dominant role"
(pp. 3–4). Its identity is set by the parameters and kept by what flows
through it, not by its history.

## Assumptions

- **The model** (p. 6, taken from the rendered page): iψ_z + (D/2)ψ_tt +
  |ψ|²ψ + ν|ψ|⁴ψ = iδψ + iε|ψ|²ψ + iβψ_tt + iμ|ψ|⁴ψ, the cubic–quintic
  complex Ginzburg–Landau equation. The left side is conservative (the NLSE
  with a quintic Kerr term); the right is dissipative: δ linear loss (if
  negative), ε nonlinear gain (if positive), β spectral filtering, μ gain
  saturation (if negative). It is non-integrable (p. 7).
- **A distributed stand-in for a lumped cavity**: "quantitative when the
  pulse alterations inside each cavity roundtrip are not too large" (p. 7);
  delayed gain-saturation dynamics are left out.
- **Deterministic**: noise enters only in soliton rain, as an observed
  background. Stability is the stability of attractors in an
  infinite-dimensional dynamical system.

## Key results

- **The integrable baseline** (p. 2). The solitons of integrable systems
  "maintain their shape and velocity after colliding with each other, and
  they remain intact when interacting with radiation waves"; in optics they
  "result from the single balance between nonlinearity and dispersion, or
  diffraction."
- **Lineage** (pp. 2–3). The name was given to solitary waves "with
  nonlinear gain or loss mechanisms"; "autosoliton" came from
  reaction–diffusion work; "Reaction-diffusion systems involve supply and
  decay of matter" (citing Purwins et al., LIT-tmp7lcfh). The concept
  "stems from the seminal ideas of Prigogine on open systems far from
  equilibrium" (p. 3, citing Nicolis & Prigogine, LIT-524).
- **Exact balance** (p. 3): "the balance between gain and loss, which should
  be exact in order to produce stationary localised solutions, plays a
  dominant role in the dynamics."
- **Family against attractor** (p. 4): "the attractor in a dissipative
  system is a fixed localised solution. Namely, the dissipative soliton
  energy, profile and chirp are predetermined by the equation parameters,
  rather than by the initial conditions." "A strong attractor naturally
  provides a high degree of stability." Fig. 1a (p. 26) draws a Hamiltonian
  family of solutions as a curve beside a dissipative fixed solution as a
  point, held by nonlinearity, dispersion or diffraction, gain and loss.
- **Bifurcations** (p. 4). As parameters change, a fixed point becomes a
  limit cycle and "a previously stationary soliton becomes a pulsating
  localised formation"; further on the dynamics become irregular and
  chaotic.
- **Supply and internal differentiation** (p. 5): "solitons in dissipative
  systems need to have distinct internal regions which extract energy from
  an external source, as well as other internal regions where energy is
  lost into the environment." The stationary soliton "results from the
  continuous energy exchange with the environment along with its live
  redistribution between the various parts of the soliton." The flow is
  "proportional to the first temporal derivative of the phase", so its sign
  is a non-uniform phase (chirp). Pulsating solitons balance only "inside a
  period of evolution".
- **What the dissipative terms do** (pp. 6–7): "linear loss and nonlinear
  gain account for the required saturable absorber effect"; the quintic
  saturating term "was shown to be essential for the stability of pulsed
  solutions".
- **Shape set by dissipation** (p. 8). Raising ε turns a near-sech pulse
  into a flat-top one, which "can be considered as two mirror-imaged
  interacting fronts" (Fig. 1b: ε = 0.38, 0.52, 0.66).
- **Dissipative soliton resonance** (p. 11). Pulse energy grows without
  bound "when the equation parameters approach a specific hyper-surface in
  the parameter space", with peak power clamped and duration growing.
- **Bound states** (p. 12). Higher-order NLSE solitons "are easily destroyed
  by external perturbations or additional effects such as third-order
  dispersion or Raman scattering", and "The Nth-order soliton requires a
  total energy proportional to N²"; "dissipative soliton molecules are
  robust multi-soliton structures", "whose energy remains proportional to
  the number of single-soliton constituents". Molecules form from separate
  solitons, and "the formation of a soliton molecule requires dissipative
  processes, and entails the existence of a binding energy". Each
  stationary pair is a point attractor.
- **Many solitons** (p. 13). Interactions "open the possibility of control
  over synthesis and dissociation of soliton molecules"; but "regular and
  stable large soliton molecules are not generic".
- **Explosions** (pp. 14–15). Exploding solitons "intermittently suffer
  explosive instabilities, but return to their original shapes after
  bursting"; successive explosions are similar, not identical. Observed in a
  Ti:sapphire laser and reproduced in a CGLE simulation.
- **Soliton rain** (pp. 15–16, experiment). When background "fluctuations
  exceed a threshold over which a new dissipative soliton can be formed",
  new solitons form and "drift back to the condensed phase", repeating
  endlessly, "an illustration of self-excitability". It needs "Watt-level
  pumping power" and a noisy background with tens of solitons.
- **Dimension** (p. 16). Kerr solitons in more than two dimensions "lead to
  either expansion or collapse", whereas "dissipative solitons remain
  stable" (theory and numerics).
- **Transient writing** (p. 17). Cavity soliton lasers work "without the
  need for permanent external driving fields", and "A transient writing
  beam enables on and off switching of cavity solitons" (Fig. 6c).

## Concepts

- **Dissipative soliton**: a localized structure held by a composite balance
  in which gain and loss balance exactly; also **autosoliton**, the
  reaction–diffusion term.
- **Fixed-point attractor against a family**: the dissipative soliton is one
  solution fixed by the parameters; the conservative one a member of a
  continuous family fixed by the initial data.
- **Internal energy flow**: from gain regions to loss regions, marked by the
  phase chirp.
- **Soliton molecule**: a bound state, formed by dissipative processes, with
  a binding energy, held by self-phase locking.
- **Pulsating soliton** (limit cycle), **soliton explosion**, **soliton rain**
  (condensed phase, self-excitability).
- **Cavity soliton**: a dissipative soliton in a driven cavity; the cavity
  soliton laser needs no permanent driving field.
- **Similariton**: an attracting asymptotic state that keeps expanding and so
  does not match the notion of a soliton (p. 9).

## Connections

It names Prigogine's open systems as a source (LIT-524, THEORY-692) and
places "autosolitons" in reaction–diffusion work, the setting of Turing's
instability (THEORY-543, LIT-535) and of the Belousov–Zhabotinsky reaction
(LIT-531, THEORY-508); Cross & Hohenberg's pattern formation (LIT-527) is
the broader frame. Knobloch on spatial localization in dissipative systems
(LIT-1642, Unfetched) covers the same subject and would supply the
subcritical bistability, snaking and existence ranges this review omits, as
would Purwins et al. (LIT-tmp7lcfh) and the Akhmediev–Ankiewicz chapter
(LIT-tmpwjm3u), neither reached. Kuehn's folds and critical transitions
(THEORY-1429, LIT-2048) and rate-induced tipping (THEORY-1079) are the
record's background for thresholds and collapse, none of which this review
treats. THEORY-1343, a slow integral of motion under weak noise, is the
nearest the record comes to the conservative side. Herr et al. (2014),
filed in parallel, reads temporal dissipative solitons in a cw-driven
microresonator, the driven-cavity kind this review sets apart from cavity
soliton lasers, and by its reader's report supplies what this one lacks: a
detuning window of existence and a soliton number set by random seeding.
Its account is THEORY-tmphrwgv.

## Bearing on the record

- **TERM-088 (senses of individuation)**: supports the dynamical sense for an
  externally supplied structure. A parameter-fixed attractor with a "high
  degree of stability", which returns to its shape after explosions, is
  dynamically individuated though sustained from outside; its identity is
  fixed by the parameters, not by its history.
- **TERM-070 (closure)**: nothing directly. The gain and loss regions are a
  redistribution of energy within one structure; no constraints or time
  scales are named, so closure cannot be assessed.
- **THEORY-072 (flame against organism)**: consistent with the demarcation,
  does not test it. It gives an optical dissipative structure with internal
  differentiation, but the cavity, absorber and gain medium are supplied,
  not produced by the soliton.
- **QUESTION-085 (flame or convection cell)**: the review's own contrast
  between solitons in "driven nonlinear optical cavities" and cavity soliton
  lasers without a permanent driving field, and its gain term ε|ψ|²ψ that
  scales with the structure's own intensity, point toward the flame rung;
  the review does not frame them that way.
- **CLAIM-604 (self-sustaining upkeep)**: consistent in form, not a test.
  Gain enters in proportion to the structure's intensity against linear
  loss; new solitons form above a fluctuation threshold; on and off states
  coexist at the same standing parameters. That with δ < 0 the zero field is
  linearly stable, so that a soliton needs a finite seed matching the
  claim's ignition threshold, is the reader's inference from the model, not
  the authors' statement. No collapse point, pump threshold or hysteresis
  loop is given.
- **CLAIM-597 (supplied upkeep)**: consistent. The structure needs continuous
  exchange, and the supply's parameters set its shape. Withdrawal of the
  pump is not discussed.
- **CLAIM-600 (when support can be withdrawn)**: supports one condition. A
  transient writing beam starts a structure that then persists on the
  standing supply, support starting a process that keeps itself going on a
  flux that stays available. Slow reversion is not addressed.
- **CLAIM-516 (cycles and closure)**: none.
- **THEORY-1273 (metastable maintained states)**: qualifies. The picture is
  of deterministic attractors; soliton rain shows noise nucleating new
  solitons above a threshold, which fits fluctuation-driven transitions
  between coexisting states, but no escape times or size scaling are given.
- **QUESTION-398 (independence from the founding intervention)**: bears
  directly. Written cavity solitons persist without the beam that wrote
  them, independent of what founded them but not of what feeds them; and the
  final form is "predetermined by the equation parameters, rather than by
  the initial conditions", so the founding leaves no trace in the shape.
- **QUESTION-399 (becoming a self-maintaining nucleus)**: none. The soliton
  regenerates its shape, not the constraints that make it possible.

**Corrections to the brief this was read against.** Keeping identity through
collisions is said of integrable solitons, not of conservative ones in
general: outside integrability, conservative higher-order solitons are
easily destroyed, and Kerr solitons in more than two dimensions expand or
collapse. Bistability, multistability, hysteresis and a pump existence
threshold are not discussed; the one threshold is on fluctuations, in
soliton rain. Formation from initial data with radiation shed, slow decay
(damped solitons, oscillons) and topological solitons are not discussed.

## Limitations

- A short review focused on lasers: no general existence theory, no
  bifurcation diagram in pump strength, no hysteresis loop, and no treatment
  of collision outcomes (merger, annihilation, passing through) beyond bound
  states and synthesis and dissociation.
- Its reach into biology is a citation of the 2008 volume (LIT-tmpwjm3u),
  not an argument.
- The copy read is the author manuscript with revision marks.

## Open questions

Whether, at fixed CGLE parameters, a soliton exists over a range of pump in
which the zero state is also stable, and whether switching it off and on
traces a hysteresis loop: the reading Purwins et al. or LIT-1642 would
settle.
