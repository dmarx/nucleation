---
status: Read
paper: LIT-308
title: 'Stochastic Thermodynamics of Learning'
version: 1
history:
- version: 1
  date: '2026-09-29'
  note: >-
    Read in full (The full text of arXiv 1611.09428 v1 (the only version, 28
    Nov 2016; PDF dated 30 Nov 2016), from the arXiv PDF, 11 pp.: a 5-page
    letter plus a 7-page Supplemental Material (§I stochastic thermodynamics
    of the network, §II derivation of Eq. 16, §III Hebbian learning in the
    thermodynamic limit). I read all of it, including the figures' captions,
    footnotes [26], [28], [39], [40] and [50], and both reference lists. The
    text was extracted with PyMuPDF. The figure axes came through only as
    tick labels. I recomputed the N = P = 1 toy model numerically: ΔS(ω), ΔQ
    from Eq. (13), I(σ_T:σ) from the stability integral, and η. I did not
    read the PRL version of record or its published supplement.). The first
    NOTE on this paper, which was seeded from its abstract alone.
date: '2026-09-29'
summary: >-
  For a perceptron whose weights follow overdamped Langevin dynamics and
  whose predicted labels are fast two-state processes, the information
  learnt about fixed random labels is bounded by the weights' total
  entropy production: Σ_μ I(σ_T^μ:σ^μ) ≤ Σ_n [ΔS(ω_n) + ΔQ_n] (Eq. 16, k_B
  = T = 1). This defines a learning efficiency η ≤ 1. The cost side
  includes the change in the weights' own Shannon entropy, and in the
  paper's toy model η → 0.99 as the heat ΔQ → 0 (slow driving). So the
  bound is not a heat floor of k_BT ln 2 per bit learnt.
---

# NOTE-tmpk0axc: Stochastic Thermodynamics of Learning

## Contribution

Earlier second-law-with-information results relate the mutual information between one degree of freedom and another to that degree's own entropy production (Sagawa–Ueda, Horowitz–Esposito, Hartich–Barato–Seifert, refs [29–34]). This paper sets up a neural network as a stochastic-thermodynamic system: weights as Langevin particles, predicted labels as fast two-state jump processes. It proves that the mutual information between true and predicted labels, summed over samples, is bounded by the entropy production of the weights alone (Eq. 16). From this it defines a learning efficiency η (Eq. 11), computes η for Hebbian learning in two settings (one weight and one sample, Fig. 2, and the thermodynamic limit N, P → ∞ with α = P/N fixed, Fig. 3), and shows that Hebbian η̃ never reaches 1.

## Key insight

Learning is information flow from fixed labels into weights. Horowitz's refined second law for a subsystem (S29) charges that flow to the weights' total entropy production: the change in the weights' marginal Shannon entropy plus heat to the bath. Data processing (σ_T → ω → σ) then carries the bound from I(ω:σ_T) down to what the network's predictions actually reveal about the labels. The efficiency trade-off follows. Storing a label needs a strongly label-dependent weight (large ν), and not wasting heat needs slow driving (large τ).

## Assumptions

- **Model.** A single-layer perceptron. The inputs ξ^μ ∈ {±1}^N are fixed, and the labels σ_T^μ = ±1 are i.i.d., equiprobable and static (p. 1). Predicted labels σ^μ are two-state processes with detailed balance k⁺/k⁻ = exp(A^μ/k_BT), A^μ = ω·ξ^μ/√N (Eqs. 1–2), and symmetric rates k^± = γ exp(±A/2) (Eq. 4).
- **Weight dynamics.** Overdamped Langevin, ω̇_n = −ω_n + f(·) + ζ_n, with a harmonic confinement V = ω²/2, independent unit-temperature white noises and a "learning force" f (Eqs. 3, 14, 15).
- **Units.** k_B = T = 1 throughout (p. 2), so information and entropy are in nats and heat is in units of k_BT.
- **Initial state.** The weights are in equilibrium (p(ω) ∝ e^{−ω·ω/2}), and the labels and predictions are uncorrelated (S6–S8).
- **Bipartite/multipartite dynamics.** Independent noise per subsystem, so the probability currents split linearly (S4, S12–S18).
- **Time-scale separation** γ ≫ 1: predictions are much faster than learning (p. 2, S46).
- **No feedback** from predictions to the learning force: f depends on (ω_n, ξ, σ_T, t) only. The conclusion says "any learning algorithm without feedback".

## Key results

- **Eq. (10), N = P = 1.** I(σ_T:σ) ≤ ΔS(ω) + ΔQ, and so η ≡ I(σ_T:σ)/(ΔS(ω) + ΔQ) ≤ 1 (Eq. 11).
- **Eq. (13), toy-model heat.** For the linear-ramp Hebbian force f = νFt/τ (t ≤ τ), νF (t > τ), with F = σ_Tξ, the total heat is ΔQ = ν²F²(e^{−τ} + τ − 1)/τ². This goes to 0 as τ → ∞ and to ν²F²/2 as τ → 0.
- **Fig. 2.** η over (ν, τ). Contours reach 0.99 at large ν and large τ. My recomputation agrees. At ν = 8, τ = 10⁵: ΔS(ω) = 0.6931, ΔQ = 0.0006, I(σ_T:σ) = 0.6885 nats, η = 0.992. At ν = 8, τ = 10⁻⁶: ΔQ = 32.0 and η = 0.021.
- **Eq. (16), the main result.** Σ_{μ=1}^{P} I(σ_T^μ:σ^μ) ≤ Σ_{n=1}^{N} [ΔS(ω_n) + ΔQ_n] = Σ_n ΔS^tot_n, for batch and online learning. The proof (Supp. §II) runs as follows. Horowitz's inequality (S29), ∂_tS(ω_n) + Q̇_n − l_n(ω_n;σ_T) ≥ 0, is integrated in time. Then Σ_n ΔI(ω_n:σ_T) is related to I(ω:σ_T) (S32–S37; see corrections). Then I(ω:σ_T) ≥ Σ_μ I(ω:σ_T^μ) for independent labels (S38–S45). Finally data processing I(σ_T^μ:ω) ≥ I(σ_T^μ:σ^μ) is applied to first order in 1/γ (S46–S47).
- **Hebbian learning in the thermodynamic limit** (Eqs. 17–22, Supp. §III). F_n = N^{−1/2} Σ_μ ξ_n^μ σ_T^μ ~ N(0, α). ⟨ω_n²⟩ = 1 + αν², so ΔS(ω_n) = ½ ln(1 + αν²). The main text prints ln(1 + αν²), without the ½, which is inconsistent with a Gaussian of that variance (unverified which is intended). The stability Δ^μ ~ N(ν, 1 + αν²). p_C = ∫ p(Δ) e^Δ/(e^Δ + 1) dΔ (Eq. 20), and I = ln 2 − S(p_C) (Eq. 21). Monte Carlo at N = 10000 agrees (Fig. 3). The analytic approximation p_C ≈ P(Δ > 0) with ν → ν/2 (S64–S71) rests on tanh(x/2) ≈ erf(γ'x/2) with γ' = 4/5 "by inspection".
- **Fig. 3 inset.** The Hebbian efficiency η̃ = α·I/(ΔS(ω_n) + ΔQ_n) "never reaches the optimal value 1, even in the limit of vanishing dissipation". The paper attributes this to thermal noise and to Hebbian learning's known inefficiency.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Information learnt ≤ total entropy production of the weights (Eq. 16), for batch learning | strong (proof), in the γ → ∞ limit | Supp. §II; built on Horowitz's subsystem second law [30]; the equality at S35 should be an inequality, which the proof survives |
| C2 | The same bound for online learning | moderate | Asserted alongside batch; conditional independence of the weights given σ_T under a shared random μ(t) is not argued (footnote [50] is a gesture) |
| C3 | The bound holds "for arbitrary learning algorithm … at all times t > t_0" | moderate | True for any feedback-free f given the assumptions, but exact only to first order in 1/γ (S46–S47) |
| C4 | Single-weight Hebbian learning can approach η → 1 with large ν and slow driving | strong (calculation) | Eq. (13), Fig. 2; recomputed (η = 0.992 at ν = 8, τ = 10⁵) |
| C5 | Hebbian learning in the thermodynamic limit never reaches η̃ = 1 | moderate (numerics) | Fig. 3 inset, from Eqs. (20)–(22), with Monte Carlo agreement on I |
| C6 | Neural networks are a new paradigm for studying the thermodynamic efficiency of learning | assertion (programmatic) | Conclusion |

## Method

This is analytic stochastic thermodynamics: a Langevin plus master-equation model, a multipartite decomposition of entropy production and information flow (Horowitz 2015), information inequalities (chain rule, data processing), and the statistical mechanics of learning (Gardner stabilities, central limit theorem in the N, P → ∞ limit). The mutual information in the thermodynamic limit is checked by Monte Carlo integration at N = 10000.

## Concepts

- **Total entropy production of a weight**, ΔS^tot_n = ΔS(ω_n) + ΔQ_n. The **thermodynamic learning rate** / information flow l_n(ω_n;σ_T) (S22, S27) is explicitly distinct from the algorithmic learning rate ν.
- **Learning efficiency** η = I(σ_T:σ)/ΔS^tot (Eq. 11). The per-sample-per-weight form is η̃ (Eq. 22).
- **Stability** Δ^μ = ω·ξ^μσ_T^μ/√N (Eq. 19; Gardner 1987).

## Connections

- [LIT-327](../literature.d/LIT-327.md) (Still et al. 2012) is the sibling result. It bounds dissipation by *nonpredictive* memory for a system driven by a signal, where this paper bounds *acquired* information by entropy production in a system driven by a learning force. Neither yields a per-bit heat floor on acquisition.
- [LIT-328](../literature.d/LIT-328.md) (Landauer 1961). This paper's bound can be met with vanishing heat, the information being paid for in increased weight entropy ΔS(ω) → ln 2. The heat is then due when that entropy is removed, i.e. when the weights are reset, which is Landauer's erasure floor.
- [LIT-348](../literature.d/LIT-348.md) (McCandlish et al. 2018, critical batch size) is the ML-side anchor of the owner's §5 "batch = SNR" story. This paper has no batch-size or gradient-noise content. Its "batch learning" means a force depending on all samples, not minibatch SGD.
- [ANTH-LIT-340](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-340.md) (Goldt et al. 2019, teacher–student SGD dynamics) is a different Goldt paper on the dynamics of learning, with no thermodynamic cost accounting.

## Bearing on the record

**What it supplies for map row 13.** The map cites this paper with [LIT-327](../literature.d/LIT-327.md) as the "thermodynamics of learning" field that owns the physics behind the §5 floor. The owner's gradient-channel-thermodynamics §5B states that floor as Q_train ≥ k_BT ln 2 · I(θ;D), and per step Q ≥ k_BT ln 2 · C_step. This paper does own a bound of the *form* "information learnt ≤ thermodynamic cost". But its cost is total entropy production, ΔS(ω) + ΔQ, and not heat. That difference is decisive.

- In the paper's own toy model the bound is nearly saturated with almost no heat. At ν = 8, τ = 10⁵, I ≈ 0.689 nats is learnt for ΔQ ≈ 0.0006 k_BT. The cost is carried almost entirely by the growth of the weight distribution's entropy (ΔS(ω) → ln 2). So "heat ≥ k_BT ln 2 per bit learnt" is *false* in the paper's own framework. Heat per bit can be made arbitrarily small by driving slowly.
- What the paper does support, restated in the map's variables, is k_BT·I(θ;labels) ≤ T·ΔS(θ) + Q, with information in nats. The k_BT ln 2 per bit is a bound on *entropy production*, and the heat must be paid in full only when the weights' extra entropy is later erased ([LIT-328](../literature.d/LIT-328.md)). A per-judgment *heat* floor at the moment of writing does not follow.
- The paper bounds I(σ_T:σ) and I(ω:σ_T), information about labels. It is not I(θ;D) for a dataset of real-valued inputs, nor a per-step gradient-channel capacity C_step. Nothing in it concerns SGD steps, batch size or precision.
- It says nothing about the cost of *evaluating* a predicate. The predicted-label jump processes σ^μ have their own heat Q̇_μ (S17), and it is excluded from the bound.

The map's verdict ("KNOWN physics, the field owns it; the bridge is NOVEL-NARROW") should therefore be sharpened. The field owns "learning costs entropy production ≥ information learnt", and it owns Landauer for erasure. The §5 per-step *heat* inequality is not owned by this paper, and in this paper's own model it fails for slow driving. If the bridge is kept, it should be stated as entropy production per bit written, or as heat per bit erased, not as heat per judgment.

For ML practice: nothing directly. The model is a single perceptron with Langevin weights and Hebbian forces, and real accelerators operate far above these bounds.

## Limitations

- The results rely on a biophysical toy: a single-layer perceptron, Hebbian forces, random ±1 inputs and a harmonic weight confinement. Gradient-based learning, and generalisation as opposed to memorising fixed labels, are not treated.
- The bound is exact only as γ → ∞, although the main text states it without that qualifier (C3).
- The derivation's weight-independence step is stated as an equality it does not have. The needed inequality holds for batch learning; online learning is not argued (C2).
- A factor of ½ appears to be missing in the main text's ΔS(ω_n) = ln(1 + αν²) (unverified which is intended). If it is a typo, the Fig. 3 inset's η̃ curves may carry it.
- The analytic approximation to p_C uses a fitted constant chosen "by inspection" (S66).

## Open questions

- What is η for learning with feedback, or with auxiliary memory? The paper names this as future work ([42]).
- Does a version of Eq. (16) hold for gradient descent on a loss, rather than a prescribed learning force, and what plays the role of ΔS(ω) there?
- How is the cost split between heat and weight-entropy growth once the full cycle, including resetting the weights for the next task, is accounted for? That is where a Landauer-type heat floor would enter.

## Corrections to the seeded skim

- Seeded from metadata; the text confirms the seed summary ("information acquired … bounded by the thermodynamic cost of learning … η ≤ 1"). "Thermodynamic cost" here means the total entropy production ΔS(ω) + ΔQ of the weights (Eq. 9), not heat or dissipated work. The distinction is what matters for map row 13 (see Bearing).
- Identification: arXiv lists only v1 (28 Nov 2016), cond-mat.stat-mech. The PDF gives the authors' affiliation as II. Institut für Theoretische Physik, Universität Stuttgart. The seed's PRL DOI and publication date (2017-01-06) are taken as given; I did not check them against the journal.
- The main text says Eq. (10) holds "for arbitrary learning algorithm f(ω, ξ, σ_T, t) at all times t > t_0". The supplement's last step (S46–S47) makes σ_T → ω → σ a Markov chain only "to first order" in 1/γ. So the result is exact only in the time-scale-separation limit γ → ∞, which the paper chooses on physiological grounds.
- Supplement step (S34)→(S35) asserts that "individual weights are uncorrelated" and writes Σ_n ΔI(ω_n:σ_T) = ΔI(ω:σ_T) as an *equality*. Marginally, the weights are correlated through their common dependence on σ_T, so the equality is not right as written. The inequality the proof needs, Σ_n I(ω_n:σ_T) ≥ I(ω:σ_T), does hold whenever the weights are conditionally independent given σ_T (by subadditivity of entropy), and that is true for batch learning with independent noises. For online learning with a shared random schedule μ(t), conditional independence given σ_T is not argued. Footnote [50] gestures at this case. So Eq. (16) is proved for batch learning and plausible, but not shown, for online learning.
