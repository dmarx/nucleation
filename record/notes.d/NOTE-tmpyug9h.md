---
status: Skimmed
paper: LIT-tmp88vcm
title: 'Scheffer et al. — Early-warning signals for critical transitions'
version: 1
history:
- version: 1
  date: '2026-11-03'
  note: >-
    Read on 2026-11-03 from the version reprinted as chapter 2 ("Early-
    warning signals for critical transitions: A review", pp. 17–32) of
    Vasilis Dakos's 2011 Wageningen PhD thesis, *Expecting the
    Unexpected*, which the university deposits openly at
    edepot.wur.nl/168815. Dakos is the paper's sixth author; the chapter
    says it "is based on the paper" (p. 17) and lists the ten authors and
    Nature 461: 53–59. The Nature text itself was not reached, so how far
    the chapter differs from it is unknown; the chapter numbers its boxes
    and figures 2.x. The running text, figure captions and Box 2.2 were
    read in full. Boxes 2.1 (the fold catastrophe) and 2.3 (the formal
    derivation of rising autocorrelation and variance) are vector
    graphics that pypdf could not extract, and were not read. Figures were
    read from their captions. Hence Skimmed. Box 2.3's content was
    re-derived and simulated instead (Key results).
date: '2026-11-03'
summary: >-
  A review of generic early-warning signals for critical transitions. At a
  fold bifurcation the dominant eigenvalue goes to zero, so recovery from
  small perturbations slows (critical slowing down). Under ongoing
  perturbation that shows as rising lag-1 autocorrelation and rising
  variance. Skewness and flickering are further signals, not caused by
  slowing down. Spatial systems add rising cross-correlation and specific
  pattern sequences. Evidence from climate, ecosystems, epilepsy, asthma
  and finance is reviewed. The signals mark proximity to a broad class of
  thresholds, not only catastrophic ones, so they do not say which kind;
  false positives and negatives are named. Cyclic and chaotic systems are
  "less well studied".
---
<!-- inactive-ok-file: LIT-720 CLAIM-478 CLAIM-tmpex9rg — Unavailable or Proposed; neighbours cited as open -->

# NOTE-tmpyug9h: Scheffer et al. — Early-warning signals for critical transitions

## Contribution

It collects, across fields, the case that the approach to a tipping point
has generic symptoms, "regardless of differences in the details of each
system" (p. 18), because systems near a bifurcation share their local
dynamics. It names the main indicators, the theory behind each, the
empirical cases then known, and the ways the indicators fail.

## Key insight

Near a fold, the restoring rate goes to zero, so a system becomes slow
before it tips. A slow system remembers its perturbations, so its
fluctuations become more correlated in time and larger. Slowness can be
read from noise the system already has, without pushing it: "Because it is
the rate of change close to the equilibrium that matters, such
perturbations may be very small, posing no risk of driving the system over
the threshold" (p. 21).

## Assumptions

- **The base case is a stochastically forced system with a stable point**
  approaching a fold bifurcation (p. 24). Critical slowing down "can be
  proven" to occur "in any continuous model approaching a fold
  bifurcation" (Wissel 1984; p. 19).
- **The approach is gradual.** The signals presuppose a slowly changing
  condition that moves the system towards the threshold (pp. 31–32).
- **The perturbation regime is stationary.** A changing regime "may distort
  or counteract the expected signals" (p. 31).

## Key results

- **Three signals of critical slowing down (pp. 19–21).** Slower recovery
  from perturbations, increased autocorrelation (Ives 1995) and increased
  variance (Carpenter and Brock 2006). Slowing "typically starts far from
  the bifurcation point", and recovery rates "decrease smoothly to zero"
  (van Nes and Scheffer 2007; p. 19). Variance could in principle fall,
  because a slowed system tracks fluctuations less well (Berglund and
  Gentz 2006), but "an increase in the variance usually arises" (p. 21).
- **Box 2.2 (p. 23), checked.** dx/dt = γ(x − a)(x − b), equilibria a and
  b. The eigenvalues are λ₁ = −γ(b − a) and λ₂ = γ(b − a), so both vanish at
  the transcritical bifurcation b = a, and the recovery rate is linear in
  the basin size (b − a) in this model. *Checked*: f′(a) = γ(a − b).
- **Box 2.3 (not read), re-derived.** For a linearized stable point
  dx = λx dt + σ dW with λ < 0, the stationary variance is σ²/(2|λ|) and
  the lag-Δ autocorrelation is e^{λΔ}; as λ → 0⁻ the first diverges and the
  second tends to 1. *Simulated* (σ = 1, dt = 0.01, Δ = 1, 360,000 steps
  after burn-in): λ = −2, −1, −0.5, −0.1 gave variances 0.26, 0.53, 1.03,
  5.16 against exact 0.25, 0.50, 1.00, 5.00, and autocorrelations 0.14,
  0.40, 0.62, 0.91 against 0.14, 0.37, 0.61, 0.90.
- **Signals not from slowing down (pp. 22–24).** Skewness rises because the
  unstable point bounding the basin approaches from one side, where rates
  are lower (Guttal and Jayaprakash 2008). Flickering is noise-driven
  switching between alternative states once the system is in the bistable
  range, seen as variance, skewness and bimodality.
- **Cyclic and chaotic systems (p. 24).** Transitions there are "less well
  studied". A Hopf bifurcation shows critical slowing down. For
  basin-boundary collisions "we know of no explicit work on early-warning
  signals". Phase locking of coupled oscillators is associated with
  critical slowing down, which is offered as why variance and flickering
  precede epileptic seizures.
- **Spatial signals (pp. 24–25).** Increased cross-correlation among
  coupled units, scale-invariant patch sizes near a transition; but in
  locally disturbed systems power laws vanish near the transition, and in
  Turing-patterned vegetation the sequence of patterns changes. "There is
  no 'one-size-fits-all' spatial pattern."
- **Empirical cases (pp. 25–30).** Rising autocorrelation in each of eight
  abrupt climate shifts (Dakos et al. 2008), including the greenhouse to
  icehouse transition of 34 Myr ago; flickering before the end of the
  Younger Dryas; spotted vegetation and truncated power laws before
  desertification; increased variance in harvested fish stocks, attributed
  to higher intrinsic growth rates; rising EEG variance minutes before a
  seizure (McSharry et al. 2003); in finance, volatility measures and
  rising cross-correlation, but also "a 'volatility calm'" before some
  shifts, and erratic lead–lag relations.
- **Failure modes (p. 31).** False negatives: no gradual approach (a rare
  extreme event or a fast change of conditions), short series, a changing
  perturbation regime. False positives: chance, or a confounding trend.
- **The scope result (p. 31).** "The same signals may even occur, albeit in
  a less pronounced way, as the system approaches a threshold that is not
  related to catastrophic bifurcations." So "most early-warning signals are
  indicators of proximity to a broad class of thresholds, where small forces
  can cause major changes in the state of a complex system".
- **Timing (p. 31).** "Perturbations will often trigger a transition well
  before a bifurcation point is reached", so "the actual moment of a
  transition remains difficult to predict".

## Concepts

- **Critical transition** — a fundamental shift when a system passes a
  bifurcation, catastrophic (fold) or to a cyclic or chaotic attractor
  (p. 18).
- **Critical slowing down** — the dominant eigenvalue at the equilibrium
  approaching zero near the bifurcation, so recovery slows (p. 19).
- **Flickering** — back-and-forth switching between basins before the
  bifurcation, when noise is strong enough (p. 24).

## Connections

- **Scheffer et al. 2001** (LIT-720, Unavailable) and **Scheffer and
  Carpenter 2003** (LIT-726) are cited as the ecological case for
  alternative stable states (p. 28).
- **Kelso's HKB** (LIT-588, THEORY-1227) is the other held case of critical
  fluctuations and slowing as early warning, in motor coordination; this
  review does not cite it, though its phase-locking paragraph (p. 24) is
  about the same class of transition.

## Bearing on the record

- **CLAIM-478, second half: a statement and a caution.** The claim says
  modes slow near an instability and can become order parameters. This
  review supplies the generic result behind "slow near an instability"
  (pp. 19–21) and its measurable marks. It also limits the claim's use of
  slowness as a sign of new structure: the same slowing appears, "less
  pronounced", before thresholds that are not bifurcations (p. 31), so
  slowness alone does not tell that a new organization is forming.
- **CLAIM-tmpex9rg, the slow-mode point.** Near a transition, small inputs
  have larger and longer-lasting effects, since perturbations decay at the
  vanishing rate. That is a second mechanism, beside chaos, by which small
  efforts could be amplified, and one in which the amplification is
  durable because the mode is slow. The review gives no early-warning
  theory for chaotic systems (p. 24), which is where Kane's case sits.
- **CLAIM-tmpptgk8.** The variance result is the stable-side mirror of the
  claim's scalar case: with λ < 0, noise variance σ²/(2|λ|) grows as
  λ → 0, so the signal-to-noise ratio of a constant input against noise
  entering the same direction, b u/|λ| over σ/√(2|λ|), is
  (bu/σ)√(2/|λ|). It rises as the system slows. Near a fold, then, an
  open-loop input is more decisive against noise, not less. With the
  claim's unstable case, the ratio goes as 1/√|λ| on both sides, so it is
  largest near marginal stability, where the horizon rather than λ bounds
  it. That is a derivation by this reader, not the paper's, and it holds
  only in the linear regime, before the input tips the system.
- **No instruction for machine-learning practice.**

## Limitations

- **Read from the thesis chapter**, not the Nature text; Boxes 2.1 and 2.3
  not read.
- A review: the empirical cases are reported from the cited papers, which
  were not checked.
- The signals' statistics (window widths, detrending, significance) are
  flagged as unsettled by the authors themselves (p. 31).

## Open questions

- What are the early warnings for transitions in chaotic systems, and for
  basin-boundary collisions (p. 24)?
- Can a slowing that precedes a bifurcation be told from one that precedes
  a non-catastrophic threshold (p. 31)?
