---
status: Read
paper: LIT-tmpj4ix1
title: 'Ashwin, Wieczorek, Vitolo & Cox — Tipping points in open systems'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Read in full from the arXiv preprint 1103.0169v5 (13 February 2013,
    22 pp.), not the journal text. The text was extracted with
    `pdftotext -layout`. I read the abstract, all five sections, the
    eight figure captions, both tables, both footnotes, the
    acknowledgements and the 28 references. v5 carries a correction: its
    footnote 1 says it "includes a correction to Section 2.1", and
    footnote 2 says the first part of §2.2 "is a revised and corrected
    version" of the journal's, "based on the published correction". So
    §§2.1–2.2 as read here are the corrected ones and may differ from
    Phil. Trans. R. Soc. A 370: 1166–1184. Pages cited are the
    preprint's (1–22), not the journal's. Equations survive extraction
    with sub- and superscripts flattened; I checked each one quoted below
    against its derivation in the text.
date: '2026-10-27'
summary: >-
  A classification and a criterion, not an empirical study. Tipping in an
  open system ẋ = f(x, λ(t)) is split into B-tipping (a bifurcation of the
  quasi-static attractor), N-tipping (noise carries the system out of its
  neighbourhood) and R-tipping, where "the system fails to track a
  continuously changing quasi-static attractor". In a linear model with a
  fixed stable M and a tipping radius R, the attractor never changes
  stability, yet steady drift r tips the system when ‖M‖⁻¹|r| > R and
  cannot when ‖M⁻¹‖|r| < R. Three examples, one with a unique globally
  stable equilibrium, and a global energy balance model show each type
  alone. Neither N- nor R-tipping needs any change of stability, so there
  is no reason to expect critical-slowing warnings for them.
---
<!-- inactive-ok-file: QUESTION-tmpl1yih CLAIM-157 CLAIM-tmpmx2ql CLAIM-405 THEORY-214 THEORY-tmp07o3p — Open or Proposed; the entries the reading bears on, cited as open -->

# NOTE-tmp429c3: Ashwin, Wieczorek, Vitolo & Cox — Tipping points in open systems

## Contribution

It names and separates a third mechanism of tipping beside bifurcation and
noise: rate-dependent tipping (R-tipping), the failure of an open system to
track an attractor that continues to exist. It gives a linear model with a
"tipping radius" in which R-tipping occurs with no bifurcation and no noise,
and sufficient conditions on the drift rate for it to occur or not (§2). It
works three low-dimensional examples (saddle-node and subcritical Hopf
normal forms, and a fast-slow system with a single globally stable
equilibrium; §3), and shows each of B-, N- and R-tipping in isolation in the
Fraedrich–Sutera global energy balance model (§4).

## Key insight

An attractor can be lost without being destroyed. If the parameter moves,
the quasi-static equilibrium x̃(λ(t)) moves with it, and the state lags
behind by an amount set by how fast it moves relative to how fast the system
relaxes. When the lag reaches the threshold for leaving, the system tips,
although at every frozen value of λ the equilibrium is there, stable, and
(in the Hopf example) of unchanged basin. "R-tipping that reduces to a
bifurcation problem in a co-moving system should not be confused with
B-tipping: observe that the bifurcation parameter r does not vary in time,
and it is 'the ability to track the QSE', rather than the QSE itself, that
bifurcates" (§3.2.1, p. 11).

## Assumptions

- **An open system** dx/dt = f(x, λ(t)), eq. (1), p. 2, read as a
  low-dimensional subsystem forced by "observables" λ(y) of a
  high-dimensional system (Fig. 1, p. 4). "Real-world systems are never
  closed except to some degree of approximation" (§1.1, p. 4).
- **The linear tipping-radius model** (§2, p. 5): dx/dt = M(x − x̃(λ)) for
  |x − x̃(λ)| < R, eq. (4), with M "a fixed stable linear operator". Beyond
  the radius the model is "unphysical". The radius "may be related to the
  basin of attraction boundary for the nonlinear problem … but it need not
  be" (p. 5).
- **For the integrations by parts** (p. 6): M invertible and exponentially
  stable, an arbitrarily long past near the QSE, and dˡx̃/dλˡ and dˡλ/dtˡ
  bounded for l = 1, 2.
- **Deterministic except in N-tipping.** The R-tipping results assume no
  noise; the N-tipping example uses dT = f(T)dt + √ν dW, eq. (41).
- The setting is narrower than the title: every example is one- to
  three-dimensional, and the climate model is zero-dimensional. The paper
  makes no claim about any real climate subsystem tipping by rate.

## Key results

### The three types (§1, p. 3; Fig. 2, p. 5)

- "'B-tipping' where the output from an open system changes abruptly or
  qualitatively due to a bifurcation of a quasi-static attractor."
- "'N-tipping' where noisy fluctuations result in the system departing
  from a neighbourhood of a quasi-static attractor."
- "'R-tipping' where the system fails to track a continuously changing
  quasi-static attractor."
- "each mechanism on its own can produce a tipping response. Furthermore,
  any open system may exhibit tipping phenomena that result from a
  combination of several of the above" (p. 3).
- Background (p. 2): Thompson and Sieber's time-series analysis of
  B-tipping relies on the separation κ_drift ≪ κ_crit ≪ κ_stab, eq. (3)
  (parameter drift, slowest decay of the QSE, faster decays); the authors
  add that κ_drift is hard to define coordinate-free and "there is no a
  priori reason for inequality (3) to hold for a given system".

### The linear model (§2, pp. 5–6)

- Tracking and tipping: if |x(t) − x̃(λ(t))| < R the solution "tracks (or
  adiabatically follows)" the QSE; if |x(t₀) − x̃(λ(t₀))| = R "the solution
  tips (adiabatic approximation fails) at t₀" (p. 5). "System (4) shows
  only R-tipping - because M is fixed there is no bifurcation in the system
  and no noise is present."
- Solution, eq. (6): x(t) − x̃(λ(t)) = −∫₀^∞ e^{Mu} (dx̃/dt)(λ(t − u)) du.
  Integrated again by parts it is L(t) + E(t), with the linear
  instantaneous lag L(t) = M⁻¹ r(t), eqs. (7)–(9), where the drift of the
  QSE is r(t) := dx̃/dt = (dx̃/dλ)(dλ/dt), eq. (8); E(t) is a
  history-dependent error in d²x̃/dt².

### Criteria (§§2.1–2.2, pp. 7–8; the corrected text)

- **Steady drift** (r constant): E = 0 and |x − x̃| = |M⁻¹r|, eq. (10).
  Since ‖M‖⁻¹|r| ≤ |M⁻¹r| ≤ ‖M⁻¹‖|r|, R-tipping is avoided if
  ‖M⁻¹‖·|r| < R, eq. (11), and occurs if ‖M‖⁻¹·|r| > R. "In the
  intermediate case, the path of parameter variation will determine
  whether or not there is any R-tipping" (p. 7).
- **Varying drift**: with r_max(t) = sup_{s≤t} |dx̃/dt| and ‖e^{Mu}‖ ≤
  c e^{−βu}, eq. (12), tipping is avoided by time t if (c/β) r_max(t) < R,
  eq. (13); for scalar M, ‖M⁻¹‖ r_max(t) < R, eq. (14). The approach "does
  not seem to easily give any sufficient condition to undergo R-tipping in
  terms of r_max(t)" (p. 8).
- **Timescales** (p. 8): a natural timescale for the QSE's motion is
  R/|r(t)|; "For an R-tipping to occur, this natural timescale may be
  comparable to the slowest timescale (e.g. the reciprocal of the leading
  eigenvalue of M) of the parametrized system." With |dx̃/dλ| ≈ 1 and
  R ≈ 1, R-tipping is expected when |dλ/dt| ≈ ‖M‖; "if |dx̃/dλ| ≈ 1/ε, then
  clearly we can have R-tipping even when |dλ/dt| ≈ ε‖M‖."
- For a nonlinear system an "effective tipping radius" can be defined, but
  "There is however no exact analogy possible", since it depends on the
  basin's shape, the nonlinearities and "the exact path taken in parameter
  space" (p. 8).

### Examples (§3, pp. 8–16)

- **Saddle-node normal form, steady drift** (§3.1): dx/dt = (x + λ)² − µ,
  dλ/dt = r, eqs. (15)–(16). For 0 < r < µ a repelling invariant line
  B(µ, r) is the tipping threshold; at r = µ it merges with the attracting
  line A and disappears. The critical rate depends on the initial
  condition: r_c = µ − (λ₀ + x₀)² if −x₀ < λ₀ < −x₀ + √µ, and r_c = µ if
  λ₀ ≤ −x₀, eq. (17), p. 10. The linear model with R = 2√µ overestimates
  r_c "because the linear attraction weakens on moving away from the
  stable QSE"; the effective radius is R_c = √µ/2. In the co-moving
  coordinate y = x + λ the problem is a saddle-node bifurcation at r = µ.
- **Subcritical Hopf, steady drift** (§3.2.1): dz/dt = F(z − λ), F(z) =
  (−1 + iω)z + |z|²z, eq. (18), one QSE at z̃ = λ(t). In the co-moving
  frame dw/dt = F(w) − r, eq. (19), the stable equilibrium that "represents
  the ability to track" disappears in a saddle-node when ω² < 1/4 and loses
  stability in a subcritical Hopf when ω² > 1/4; r_c(ω) = √((1 + 4ω²)/8)
  in the latter case, eq. (23); Bogdanov–Takens points at (±1/2, ±1/2)
  (Fig. 4, p. 12).
- **Subcritical Hopf, unsteady drift** (§3.2.2): λ moves from 0 to ∆ by
  dλ/dt = ρλ(∆ − λ), eq. (24), maximum rate ∆²ρ/4. "Observe that there is
  no change in stability or basin size of the QSE as t changes" (p. 12).
  For ∆ = 8, ρ_c = 4.78: at ρ = 4.76 the system tracks, at ρ = 4.8 it
  tips (Fig. 5, p. 13). Sieber (pers. comm.) suggests ρ_c is a heteroclinic
  connection in the extended system; there is no reduction to a
  bifurcation.
- **Fast-slow system** (§3.3): εẋ₁ = x₂ + λ + x₁(x₁ − 1), ẋ₂ = −Σ_{n=1}^N
  x₁ⁿ, eqs. (26)–(27), N odd. The equilibrium x̃(λ) = (0, −λ) is unique,
  asymptotically stable for every fixed λ "and globally asymptotically
  stable if N ≥ 5". The fold of the critical manifold "defines a tipping
  threshold that is not associated with any basin boundary" (p. 13). With
  steady drift, r_c = Σ 2⁻ⁿ as ε → 0, eq. (33) (r_c = 1/2 for N = 1,
  Fig. 6a). With dλ/dt = ρe^{−λ}, eq. (34), ρ_c depends on the initial
  condition, eq. (37). "only when the parameter variation is very slow with
  respect to the slow variable and there are three timescales is tracking
  guaranteed. In this sense, the rate dependent tipping occurs when the
  slow and very slow timescales are no longer separable" (p. 16).

### The climate model (§4, pp. 16–19; Tables 1–2, Fig. 7)

- Fraedrich's zero-dimensional energy balance c dT/dt = R↓ − R↑, with
  ice-albedo α_p(T) = a₂ − b₂T², eqs. (38)–(40), and Sutera's noisy form
  dT = f(T)dt + √ν dW, eq. (41). For µ above a critical 0 < µ_c < 1 there
  are two equilibria, T⁺ stable and T⁻ unstable, merging in a saddle-node
  at µ_c.
- **R-tipping** (Fig. 7a–b): parameters move smoothly between two steady
  settings by dλ/dt = ρλ(1 − λ), with a₂ chosen to hold b_µ² − 4d_µ
  (the discriminant of (40) as a quadratic in T²) constant (p. 17, Table
  2); the paper does not say why that quantity is held. At ρ = 0.18 "the system returns to the QSE after a transient";
  at ρ = 0.19 it "becomes unbounded", so ρ_c ≈ 0.185 yr⁻¹.
- **N-tipping** (Fig. 7c): all parameters fixed, noise ν = 1.0 yr⁻¹.
- **B-tipping** (Fig. 7d): µ decreased from 1 at −0.0004 yr⁻¹ through the
  saddle-node.

### Conclusions (§5, pp. 17–19; Fig. 8, p. 20)

- Mixed cases: B-tipping "may turn into R-tipping upon increasing the rate
  of change", but also "B-tipping may be suppressed for fast enough
  variation of parameters", or R-tipping may come first (p. 19; Fig. 8a–c).
- "We emphasise that neither N-tipping and R-tipping require any change of
  stability. Hence there is no reason to assume that the techniques of
  [4], based on a de-trended autoregressive model for B-tipping, should
  deliver useful predictions in such cases" (p. 19). R-tipping reducible to
  a co-moving bifurcation "may be expected to be predictable using similar
  methods"; others may be quantifiable by heteroclinic bifurcations of an
  extended system.
- Applications suggested, not shown: cell fate (Nene and Zaikin), "from
  mechanics and ecology to economics and social sciences" (p. 19).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | R-tipping occurs with no bifurcation and no noise: a system can leave an attractor that exists and keeps its stability at every frozen parameter | strong | the linear model with fixed M (§2, p. 5); the Hopf example with unchanged stability and basin (§3.2.2); the globally stable fast-slow example (§3.3) |
| C2 | With steady drift, ‖M⁻¹‖·|r| < R suffices to avoid R-tipping and ‖M‖⁻¹·|r| > R suffices for it, in the linear model | strong | derivation, eqs. (10)–(11), in the corrected §2.1 |
| C3 | With steady drift, R-tipping is a bifurcation of the ability to track in a co-moving frame, not of the QSE | strong | §3.1 (y = x + λ) and §3.2.1 (eq. 19), worked exactly |
| C4 | The critical rate depends on the initial condition and, outside steady drift, on the path | strong | eqs. (17) and (37); p. 7 on the intermediate case |
| C5 | R-tipping can occur where the equilibrium is unique and globally asymptotically stable, at a threshold that is no basin boundary | strong | §3.3, N ≥ 5, in the singular limit ε → 0 |
| C6 | Each of B-, N- and R-tipping occurs alone in the Fraedrich–Sutera model | moderate | simulations, Fig. 7 and Table 2; ρ_c ≈ 0.185 yr⁻¹ read from two runs |
| C7 | Critical-slowing early warnings have no reason to work for N- or R-tipping | moderate | argued from the absence of a change of stability (p. 19); no test is run |
| C8 | Tracking is guaranteed only when parameter change is slow relative to the slowest dynamics; R-tipping is a failure of that separation | moderate | sufficient condition (13)–(14) in the linear model; stated for the fast-slow example (p. 16); for nonlinear systems "no exact analogy possible" (p. 8) |
| C9 | The classification applies widely beyond climate | weak | suggested in §5, with no example outside climate and normal forms |

## Concepts

- **Open system** — one with inputs λ(t) that "can change the fate of
  system trajectories" (§1.1, p. 4); a closed one's future depends only on
  its current state.
- **Quasi-static attractor / QSE** — the stable solution, here an
  equilibrium x̃(λ), of the system with λ held constant (p. 2).
- **Tracking** — staying within the tipping radius of the moving QSE,
  "adiabatically follows" (p. 5).
- **Tipping radius R** — the distance from the QSE at which the system is
  taken to have tipped; may but need not be a basin boundary (p. 5).
  **Effective tipping radius** — the radius that makes the linear criterion
  match a nonlinear system (p. 8; §3.1, §3.2.1).
- **Drift of the QSE** — r(t) = dx̃/dt = (dx̃/dλ)(dλ/dt), eq. (8); **steady
  drift** when r is constant.
- **Linear instantaneous lag** — L(t) = M⁻¹r(t), eq. (9).
- **Critical rate** r_c or ρ_c — the rate of change above which the system
  tips.
- **B-, N-, R-tipping** — as quoted under Key results (p. 3).

## Connections

- **Wieczorek, Ashwin, Luke and Cox 2010** (ref. [28], the compost-bomb
  instability, "Excitability in ramped systems"), not held, is where
  R-tipping was "identified … as an important tipping mechanism" (p. 3)
  and the source of the fast-slow theory used in §3.3.2.
- **Thompson and Sieber** (refs. [25], [26]), on bifurcation- and
  noise-induced tipping and the separation κ_drift ≪ κ_crit ≪ κ_stab, and
  their safe, explosive and dangerous bifurcations (p. 3).
- **Dakos et al. 2008** and **Ditlevsen and Johnsen 2010** (refs. [4],
  [5]) on early warning; Lenton et al. (refs. [16], [17]) on tipping
  elements; Kuehn 2011 (ref. [15]) on fast-slow critical transitions; none
  held.
- **Scheffer and Carpenter** ([LIT-726](../literature.d/LIT-726.md), read in [NOTE-571](NOTE-571.md)), the record's
  standard of evidence for alternative stable states ([THEORY-136](../theory.d/THEORY-136.md)), is not
  cited by the paper.
- **Falmagne, Stephenson and Levin** ([NOTE-731](NOTE-731.md), [THEORY-214](../theory.d/THEORY-214.md)) use the B/S/R
  classification in a social system and find rate-induced tipping preceded
  by speeding up, not slowing: the empirical counterpart of C7.

## Bearing on the record

- **[QUESTION-tmpl1yih](../questions.d/QUESTION-tmpl1yih.md): A14's gloss is right in its first half and stronger
  than the paper in its second.** "Not because its equilibrium ceases to
  exist" matches: R-tipping is the failure to track "a continuously
  changing quasi-static attractor" (p. 3); in the linear model M is fixed
  and "there is no bifurcation" (p. 5); in §3.2.2 "there is no change in
  stability or basin size" (p. 12). "Cannot reorganize fast enough" needs
  three corrections. (i) The paper's quantity is relaxation, not
  reorganization: the lag M⁻¹r against the radius R (§2.1), so the
  distance to the threshold counts as much as the rate. (ii) "Destroyed" is
  stronger than "tips": in the climate model at ρ just below ρ_c the
  system "returns to the QSE after a transient" (Fig. 7a), and in §3.3 the
  equilibrium is unique and globally stable, so a tip is a large excursion
  whose permanence the paper does not state. A form is lost by R-tipping
  for good only if something lies past the threshold to catch it (the
  unbounded runs of §3.1 and Fig. 7b). (iii) Rate can also preserve:
  "B-tipping may be suppressed for fast enough variation of parameters"
  (p. 19, Fig. 8a). The question's "pass away" route gets a precise form:
  what bifurcates is "'the ability to track the QSE', rather than the QSE
  itself" (p. 11). The paper says nothing on how forms arise.
- **[CLAIM-157](../claims.d/CLAIM-157.md): the duration clause, read on frozen dynamics, cannot see
  R-tipping.** In the paper's own model the dynamics matrix M is the same
  at every instant (eq. 4), so any spectral or gap verdict computed from
  it is constant across the tip. "It lasts as long as that block persists"
  then says the form lasts while the system has left it. The clause holds
  up only if "persists" is read on the trajectory, or in the co-moving
  frame where the tracking solution is what bifurcates (§3.1, §3.2.1). The
  dated note of 2026-10-27 ("which bears on 'it lasts as long as that
  block persists'") is confirmed and can be made exact: a block can keep
  clearing its threshold at every frozen parameter while the form tips by
  rate. The paper does not address individuation or decomposability.
- **[CLAIM-tmpmx2ql](../claims.d/CLAIM-tmpmx2ql.md): rate-induced tipping is the failure of the separation
  the claim relies on, and the paper says so.** "only when the parameter
  variation is very slow with respect to the slow variable and there are
  three timescales is tracking guaranteed … rate dependent tipping occurs
  when the slow and very slow timescales are no longer separable" (p. 16).
  So the quasi-static attractor is a constraint only over the window
  between the drift time R/|r| and the slowest relaxation (p. 8), which is
  the claim's "over the window between the two time scales" for the
  attractor itself. Two sharpenings. The relevant drift is the QSE's in
  state space, not the parameter's: with |dx̃/dλ| ≈ 1/ε, a parameter
  moving at ε‖M‖ still tips the system (p. 8). And R-tipping needs no
  slowing of modes (p. 19), so it is separation lost by the input speeding
  up, not by the system slowing near an instability, the route in the
  claim's second half. Filed as [THEORY-tmp07o3p](../theory.d/THEORY-tmp07o3p.md).
- **[THEORY-136](../theory.d/THEORY-136.md): a third route to abrupt change without alternative
  states.** [THEORY-136](../theory.d/THEORY-136.md) holds that jumps also arise from a stepwise driver
  or a simple threshold. §3.3 adds a smooth but fast driver acting on a
  system with one globally stable equilibrium, at a threshold that "is not
  associated with any basin boundary" (p. 13). That supports [THEORY-136](../theory.d/THEORY-136.md)'s
  caution. Where the frozen system is bistable, as in the climate model, a
  shift that depends on the rate of an otherwise identical parameter path
  is a form of initial-state or history dependence, which [THEORY-136](../theory.d/THEORY-136.md)
  counts as near-diagnostic; the paper does not discuss evidence.
- **[THEORY-214](../theory.d/THEORY-214.md) and [CASE-111](../cases.d/CASE-111.md).** The paper's argument that early warnings
  have "no reason" to work for R-tipping (p. 19) is the theoretical
  counterpart of [THEORY-214](../theory.d/THEORY-214.md)'s finding that rate-induced tipping in r/place
  is preceded by speeding up, and it supports [CASE-111](../cases.d/CASE-111.md)'s caveat that
  "rate-dependent effects" make early-warning signals unreliable.
- Filed: [THEORY-tmpksbqt](../theory.d/THEORY-tmpksbqt.md) (Active), [THEORY-tmp07o3p](../theory.d/THEORY-tmp07o3p.md) (Proposed). No
  instruction for machine-learning practice is carried.

## Limitations

- The journal's §§2.1–2.2 were corrected after publication, and I read
  only the corrected preprint; I cannot say what the original criteria
  were or whether any later citation relies on them.
- R-tipping is defined by a tipping radius chosen by the analyst, and for
  nonlinear systems "no exact analogy possible" (p. 8). The definition of
  when a system has "tipped" is therefore model-relative; the paper gives
  no general definition of R-tipping for nonlinear systems.
- No sufficient condition for R-tipping with varying drift (p. 8).
- The climate example is a zero-dimensional toy, and ρ_c ≈ 0.185 yr⁻¹ is
  bracketed by two runs; no claim about a real climate subsystem is made.
- Whether a tipped system is lost for good is not treated: Fig. 7b is
  "unbounded", and §3.3's divergence "in the fast x₁ direction" in a
  globally stable system is left without its sequel.
- Small slips in the text: §2.2 cites "the elegant estimates of Godunov
  [27, Eq.(13)]" where reference [27] is Veselić; §5 names "(15) and (24)"
  for a heteroclinic computation that §3.2.2 attaches to (18) and (24).
  Neither affects the results. The extraction flattens super- and
  subscripts (b_µ² prints as "b2µ"; the initial λ in §4 prints as "10 …
  6", read as 10⁻⁶).

## Open questions

- A general theory of R-tipping for nonlinear systems, giving the critical
  rate from the system and the path; the paper expects "significant
  mathematical development" (p. 19).
- Predictive techniques for R-tipping that does not reduce to a co-moving
  bifurcation (p. 19).
- How the three mechanisms combine in realistic models (p. 19).
