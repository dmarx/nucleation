---
number: 67
status: Read
formerly:
- NOTE-tmpn3pug
paper: LIT-034
title: 'The sound of an axon''s growth'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (Full text of arXiv:1807.04799v3 (17 Apr 2019; dated 18 Apr
    2019), 5 pp.: all text, Figs. 1–4 captions and refs 1–34
    (raw4/1807.04799.txt, extracted with PyMuPDF). From the arXiv source
    tarball (raw4/c69src/) I also read the 2-page Supplementary Material in
    full (Folzetal_SM.pdf: linear stability derivation Eqs. S1–S13, dynein
    variation Fig. S1, stochastic delay Fig. S2, lossy transport Eqs.
    S14–S15 and Fig. S3), and searched the LaTeX source for parameter
    values. I did not read the published PRE version (99, 050401, 2019).
    Figures came through only as labels, so I relied on captions and
    prose.). Upgraded from `Skimmed` to `Read`: the claims table,
    assumptions and results are new, and the skim is corrected where the
    full text disagreed.
date: '2026-09-25'
summary: >-
  The paper proposes that an axon can set its length from motor-generated
  oscillations without reading their frequency. Two Hill-type stages turn
  the period (which grows with length L) into a shape change and then into
  a change in the mean of a contractility signal R. Coupling growth-cone
  protrusion (v_g c_I) against R-driven contraction (v_s c_R) then gives a
  stable length: about 125 µm with sub-µm (< 1 %) oscillation for the Fig.
  4a parameters. In part of parameter space the final length rises as
  kinesin influx J0 falls, or as dynein coupling J_O falls, qualitatively
  as in experiments.
---

# NOTE-067: The sound of an axon's growth

## Contribution

The paper closes a gap left by earlier motor-oscillation proposals (Rishal et al. 2012; Karamched & Bressloff 2015). Those proposals give a length-dependent frequency but no demonstrated way to turn it into length control. The authors first show that a single sigmoidal response cannot read frequency from its mean. They then give a two-stage filter that can, and embed it in a closed growth dynamics (Eqs. 2, 5, 6, 10) with a delay τ = L/v that depends on the state. The result is a stable length set point, with a non-monotonic dependence on motor influx that can match the counterintuitive experimental finding that fewer motors give longer axons.

## Key insight

A threshold (Hill) response averages to the same value whatever the period of a fixed-shape periodic input. What changes with period is the *waveform* after a first low-pass stage. A second threshold stage then reads that waveform change as a change in mean. Two cascaded sigmoidal filters therefore convert frequency into a DC level, and a DC level can drive the balance of protrusion against contraction. The axon measures its length through the spectrum, not the frequency, of its own motor oscillation.

## Assumptions

- **Hill response.** f_κ(c) = cⁿ/(κⁿ + cⁿ) (Eq. 1), with n = 4 or 50 in the figures. The same f_κ is used at every stage, although Fig. 4 introduces a separate κ_R = 5×10⁻³ µm⁻¹ not defined in the text.
- **Linear production and decay.** ċ_R = J_R(1 − f_κ(c_I)) − γ_R c_R (Eq. 2), and likewise for I (Eq. 4).
- **Delayed feedback loop (after Karamched & Bressloff 2015).** ċ_I = J0 − J_I f_κ(c_O(t−τ)) − γ_I c_I and ċ_O = J_O f_κ(c_I(t−τ)) − γ_O c_O (Eqs. 5–6).
- **Delay.** τ = L/v, with the same velocity v for kinesin and dynein.
- **Simplifications.** γ_I = γ_O = γ_R = γ and J0 = J_I = J_O = J for the analysis.
- **Growth law.** L̇ = v_g c_I − v_s c_R (Eq. 10). Protrusion is set by I alone, with membrane tension explicitly neglected. Contraction is active stress ζΔμ with ζ = ζ1 c_R, balanced by friction, and the soma is anchored.
- **Parameters.** One set: J = 55×10⁻⁵ µm⁻¹ s⁻¹, J_R = 26×10⁻⁵ µm⁻¹ s⁻¹, κ = 2×10⁻² µm⁻¹, γ = 10⁻² s⁻¹, v_g = 0.1 µm² s⁻¹, v_s = 0.5 µm² s⁻¹ (Fig. 4). The motor velocity v is unstated.
- **Model scope.** Spatially lumped: signals are concentrations at the growth cone and soma only. The authors say a spatial description of contractility is "most likely" needed (p. 4).

## Key results

- **Period independence (after Eq. 2).** (1/T)∫0^T f1(c_I(t))dt = (β/T)∫0^{T/β} f1(c_I(βt))dt for any β > 0, so ⟨c_R⟩ = J̄_R(1 − ⟨f1(c_I)⟩) does not depend on T for a fixed waveform. For n → ∞, ⟨c_R⟩ = J̄_R(1 − t×/T) (Eq. 3).
- **Two-stage readout (Eq. 4, Fig. 2).** With an oscillating O feeding I, ⟨c_R⟩ increases with T. For n → ∞, ⟨c_R⟩ → J̄_R(1 − t>/T), where t> > 0 requires J̄_I > 1. The transcendental equation for t> is omitted.
- **Hopf threshold for fixed L (Eq. 7).** J̄ sin(γτ√(J̄² − 1)) = 1, with J̄ = √α J/(κγ) and α = ⟨f′1(c_O)⟩⟨f′1(c_I)⟩. It requires J̄ > 1 and gives a minimum oscillating length L_min = vτ_min. At onset cot(ω_min τ_min) = ω_min/γ (Eq. 8; SM Eqs. S12–S13).
- **Frequency–length relation (Eq. 9, Fig. 3b).** ω ∼ 1/√[(L/v)(L/(3v) + γ⁻¹)]. This gives ω ≈ √3 v/L for Lγ ≫ v and ω ≈ √(vγ/L) in the opposite limit, and it matches the full nonlinear simulations (Fig. 3b).
- **Length dynamics (Fig. 4).**
  - From L = 0 the length grows and settles with oscillation amplitude < 1 % of the mean (Fig. 4a).
  - The mean length falls as J_R rises (Fig. 4b).
  - For small J0 the stationary length rises as J0 falls; above a critical J0 it rises with J0 (Fig. 4c).
  - Lowering J_O (dynein coupling) lengthens the axon (SM Fig. S1).
- **Robustness (SM).** Gaussian delay noise with σ = 0.1τ0 leaves the stationary length "almost identical" (Fig. S2). Lossy transport with factor exp(−L/λ), λ = 1000 µm, preserves the non-monotonic J0 dependence (Fig. S3).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The mean of a Hill response to a periodic signal is independent of the period for a fixed waveform | strong | proof by change of variables (p. 2); Eq. 3 in the Heaviside limit |
| C2 | Two cascaded sigmoidal filters make the mean response depend on the input frequency | moderate | numerics (Fig. 2b, n = 4 and 50) plus the Heaviside-limit expression; the t> equation is not given |
| C3 | The delayed I–O loop oscillates only above a minimum length, with ω ≈ √3 v/L for long axons | strong (linear), moderate (nonlinear) | linear stability analysis (SM Eqs. S1–S13); Eq. 9 is described as an approximation fitting the numerics (Fig. 3b) |
| C4 | Coupling the readout to protrusion and contraction yields a stable length with < 1 % oscillation (≈ 125 µm) | moderate | numerical solution for one parameter set (Fig. 4a); the µm conversion depends on the unstated v |
| C5 | Reducing kinesin influx (J0) or dynein coupling (J_O) can lengthen the axon, consistent with experiments | moderate (in-model), weak (as biology) | Fig. 4c and Fig. S1. It holds only below a critical J0 (p. 4); mapping J0 and J_O to motor concentrations is an assumption; the comparison with refs 20 and 22 is qualitative |
| C6 | The mechanism is robust to 10 % delay noise and to lossy transport | moderate | single simulations each (SM Figs. S2–S3) |
| C7 | The steady state is a laser-like gain–loss balance with frequency selection and phase-locking | assertion | analogy only (p. 4); phase-locking is not computed |
| C8 | Gradient-based length sensing is "unlikely to operate over more than a few micrometers" | assertion | stated in the Introduction with no citation or calculation given for the claim |

## Method

The paper uses deterministic delay-differential equations with a state-dependent delay τ(t) = L(t)/v:
- linear stability of the fixed-length loop about its (time-averaged) steady state, with the ansatz y_j ∝ e^{λt} (SM Eqs. S5–S13);
- numerical integration of the coupled system (Eqs. 2, 5, 6, 10) with lengths scaled by L_min and concentrations by κ;
- parameter sweeps over J_R, n, J0 and J_O, plus stochastic-delay and lossy-transport variants in the SM.

## Concepts

- **Incoming signal I / outgoing signal O / response R.**
  - I is carried soma → growth cone by kinesin. It activates O-transport, protrusion and inhibition of R.
  - O is carried back by dynein and suppresses I-release at the soma.
  - R drives actomyosin contraction.
- **L_min.** The shortest axon length at which the I–O loop oscillates (Eq. 7).
- **Spectral readout.** Length information carried by the oscillation's waveform after filtering, not by its frequency directly.
- **Adaptive delay.** The feedback delay set by the controlled variable itself, L/v.

## Connections

The model builds on the delayed-feedback oscillator of Karamched & Bressloff (Biophys. J. 2015) and the motor-oscillation length-sensing proposal of Rishal et al. (Cell Rep. 2012). It answers Bressloff & Karamched (2015), who posited a frequency-dependent average plus a switch, by supplying an explicit transduction. It contrasts with gradient-based length control of filaments (Varga, Howard; Johann & Kruse; Melbinger & Frey) and with Laughlin's resonant chemical waves (PNAS 2015). The active-gel contractility term follows Kruse et al. (PRL 2004). Within this batch, c36 is the other paper where a delay drives a Hopf bifurcation, there in random ecological communities.

## Bearing on the record

This is physics-of-living-systems theory with **no instruction or theory for ML practice**, so there is nothing for the Anthology of the SOTA. The two-stage sigmoidal frequency-to-DC conversion is a small, general signal-processing observation. It explains why threshold nonlinearities cannot demodulate frequency alone. Nothing in the paper connects it to learning systems, and I would not file it as a theory there.

## Limitations

- The paper uses a single parameter set, with no sensitivity analysis beyond J_R, n, J0 and J_O. How finely tuned the length set point is remains unknown, which was the dossier's question and is still open.
- The motor velocity v is unstated, so the paper's absolute lengths and frequencies cannot be reproduced.
- The model is lumped, with no spatial transport or diffusion along the axon. Equal kinesin and dynein speeds are assumed, and membrane tension is neglected.
- The agreement with experiment is qualitative and regime-dependent: fewer motors give longer axons only below a critical J0. The paper does not argue which side of that threshold real axons sit on.
- The authors note that sub-µm length oscillations "would likely be masked by fluctuations in a real axon" (p. 4). The mechanism's most direct signature may therefore be unobservable, and the paper proposes no alternative test.
- The comparison with gradient mechanisms rests on an uncited assertion (C8).

## Open questions

- What experiment distinguishes spectral readout from gradient or frequency-threshold mechanisms? For example: impose an external periodic modulation of motor transport at a chosen frequency and see whether the steady length shifts as the model predicts.
- How robust is the set point to the Hill coefficients and to unequal kinesin and dynein velocities? This could be tested by a parameter sweep with v stated.
- Does a spatially resolved version with transport and diffusion along the axon keep the length regulation? The authors flag this as needed.

## Corrections to the seeded skim

- **The motor velocity is never stated.** The dossier gives "about 125 µm" as the settled length. The paper does state this ("the average axon length would be 125 µm", p. 4). But lengths are computed in units of L_min = vτ_min, and I found no value of the motor velocity v in the text, the figure captions, the SM or the LaTeX source. Neither the 125 µm figure nor the frequencies in Fig. 3b can be reproduced from the paper as written.
- **The "laser" balance is an analogy, not a derivation.** The dossier reports that the length "settles... through a laser-like balance of gain and loss with phase-locking". The paper presents this explicitly as an analogy: "Even though a mapping from the present model to reaction-diffusion equations is not evident, let us exploit the similarity…" (p. 4). No phase-locking is computed or shown.
- **The period-independence claim has a narrow scope.** The dossier says the time-averaged Hill response "does not depend on the period, only on the fraction of the period spent above threshold". The paper's general proof (the rescaling identity after Eq. 2) covers only signals that differ by a time rescaling, c_I(t) → c_I(βt), with the same waveform. The "fraction above threshold" form (Eq. 3) is the n → ∞ Heaviside case. The whole mechanism rests on the waveform *changing* with period after one filtering stage (Eq. 4).
- **The title differs between versions.** The SM's title is "Can you hear an axon growing?"; arXiv's is "The sound of an axon's growth"; PRE's (per the dossier, via Crossref) is "Sound of an axon's growth". The "sound" refers to the long-axon limit ω ≈ √3 v/L, which the authors liken to a wave equation with rescaled sound velocity (p. 3).
- The dossier is otherwise accurate: the kinesin/dynein delayed-feedback set-up, L_min, the growth equation with state-dependent delay, and the non-monotonic dependence on J0.
