---
status: Read
paper: 'LIT-tmpms4ta'
title: 'Rethinking generalization requires revisiting old ideas: statistical mechanics approaches and complex learning behavior'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full from arXiv v2 (31 pages, text layer), Sections 1–5 with
    footnotes. The figures are schematics or reproduced learning curves from
    the cited literature (Figures 2–3) and are read from their captions. The
    perceptron results are the paper's summaries of Seung, Sompolinsky and
    Tishby (1992), Haussler, Kearns, Seung and Tishby (1996) and Engel and
    Van den Broeck (2001), taken as it reports them; none of those sources
    was read.
date: '2026-10-03'
summary: >-
  VSDL model: f = f(x; α, τ), α = m_eff/N lowered by label noise, τ raised
  by early stopping. Thermodynamic limit m, N → ∞ with α = m/N fixed.
  Continuous perceptron: s(ε) ~ ln ε, so 1/ε − α = 0 gives ε ~ 1/α (Eqs.
  6–8). Ising perceptron: s(ε) ~ −(π²/2)ε² ln ε, and −π²ε ln ε = α has no
  solution for large α, so ε falls discontinuously to 0 at αc (Eqs. 9–13).
  Rigorous bound: error ≤ ε* + ε_τ, ε* the rightmost crossing of s(ε) and
  −α log(1 − ε) (Eqs. 14–18). No new theorem, no experiment.
---

<!-- inactive-ok-file: THEORY-087 — Proposed; named for the regular versus singular complexity penalty, with no relation claimed -->

# NOTE-tmpw6wnw: Rethinking generalization requires revisiting old ideas: statistical mechanics approaches and complex learning behavior

## Contribution

A reframing, not a result. It proposes that the two practical knobs in
Zhang et al.'s "rethinking generalization" experiments, label randomization
and early stopping, map onto the load and temperature of the statistical
mechanics of learning. Given that mapping, the long-known phase behaviour
of simple networks (discontinuous learning curves, spin-glass phases)
predicts Zhang et al.'s two observations qualitatively. The identification
of the two knobs with load and temperature is claimed as new.

## Key insight

How a learning curve behaves is decided by how many hypotheses sit near
each error level. If many hypotheses have error slightly above the best,
as on a continuous sphere of weights, error falls smoothly with data. If
almost none do, as on the corners of a hypercube of ±1 weights, the
competition between that entropy and the training-error energy has no
interior optimum past a critical load, and the error jumps. Worst-case
uniform bounds hide this because they depend on the class only through its
size or VC dimension.

## Assumptions

- **Black-box model.** The trained network's behaviour depends only on α
  and τ; every other knob is held at a possibly suboptimal value (Claim 1).
- **Load.** α = m_eff/N with m_eff = m − m_rand. This needs the capacity N
  reached by training to scale with m, not with m_eff. The justification
  given is that the empirical Rademacher complexity of realistic networks is
  near 1, since they fit random labels.
- **Temperature.** SGD treated as relaxational Langevin dynamics, so that a
  temperature exists by the fluctuation–dissipation theorem. τ is taken to
  depend on 1/t* "in some manner that we won't make explicit".
- **Thermodynamic limit.** m, N → ∞ with α = m/N fixed (Claim 2).
- **Perceptron analysis.** Realizable teacher–student learning, the
  zero-temperature Gibbs rule (a random element of the version space), the
  annealed approximation (Eq. 5). The paper notes that the precise results
  need quenched averages and replica methods (footnote 17).

## Key results

- **Hypothesis volume.** Ω_m(ε) = Ω₀(ε)(1 − ε)^m (Eq. 5), so the
  generalization error is set by maximizing s(ε) − e(ε), with s(ε) =
  (1/N) ln Ω₀(ε) and e(ε) = −α ln(1 − ε) ≈ αε.
- **Continuous perceptron** (J on the sphere J² = N; ε = arccos(R)/π):
  Ω₀(ε) ~ exp[(N/2)(1 + ln 2π + ln sin²(πε))], s(ε) ~ ln ε for small ε,
  1/ε − α = 0, ε ~ 1/α (Eqs. 6–8). Smooth, in line with PAC/VC.
- **Ising perceptron** (J ∈ {−1, +1}^N):
  s(ε) ~ −(π²/2)ε² ln ε for small ε (Eq. 10); the condition
  −π²ε ln ε − α = 0 (Eq. 13) has no solution for large α, so the optimum
  moves to the boundary ε = 0 and the error drops discontinuously at αc.
  The (α, τ) diagram has phases of perfect and poor generalization, a spin
  glass phase and metastable regions (Figure 3(d), from Seung et al.).
- **Rigorous route** (Haussler et al.): with Q_j hypotheses at error ε_j,
  the error bound is min{ε_i : Σ_{j≥i} Q_j(1 − ε_j)^m ≤ δ} (Eq. 16).
  Writing log Q_j ≤ N s(ε_j) gives Eq. 18, and in the limit
  Pr[V(S) ⊆ B(ε* + ε_τ)] → 1, with ε* the rightmost crossing of s(ε) and
  −α log(1 − ε). For the Ising perceptron s(ε) = H(sin²(πε/2)) gives the
  drop to zero at αc (Figure 3(g–h)).
- **Finite-class straw man.** |F| < ∞ gives ε(h) ≤ (1/m) ln(|F|/δ), which
  depends on F only through |F| (Eq. 15).
- **Loss surfaces.** The entropy-versus-loss histogram of Choromanska et al.
  is consistent with the random energy model, whose entropy vanishes below
  a critical temperature. That is the same small-entropy-near-the-minimum
  mechanism (Section 4.4).
- **Regularization.** Tikhonov (x̂ = (AᵀA + λ²I)⁻¹Aᵀb, Eq. 21) and TSVD
  can always prevent overfitting by underfitting, because the operator is
  linear. In a nonlinear system in a spin-glass phase no global parameter
  does this, and early stopping is "the only control parameter" that does
  (Section 4.5, Conclusion 2).
- **Energy surface.** In the overtraining phase, randomizing L labels gives
  2^L nearly degenerate problems whose minima are separated by high
  barriers (Figure 4, Section 5).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Label randomization lowers an effective load and early stopping raises an effective temperature | weak: an analogy, argued informally; τ(t*) is not specified | Claim 1, Section 3.1 |
| C2 | The thermodynamic limit, not a fixed class with m → ∞, is the appropriate limit for deep networks | moderate as an argument; it is the standard premise of the cited literature | Claim 2, Section 4.2 |
| C3 | Generalization error can be discontinuous in the load when the entropy of near-optimal hypotheses vanishes | strong for the perceptron models cited (replica, rigorous and numerical results agree, by the paper's report) | Eqs. 9–13, 16–18 |
| C4 | Deep networks have such a phase diagram ("every" DNN) | weak: stated as an "obvious conjecture"; the only evidence is Choromanska et al.'s histogram | Section 4.4, Section 5 |
| C5 | Popular regularizers cannot bring a network out of the overtraining phase, while early stopping can | weak: follows from the model by construction; not measured | Conclusions 1–2, Section 4.5 |

## Concepts

- **control parameter**: a parameter a practitioner can use operationally
  to steer learning (n, n/p, λ, dropout, batch size, iteration count), as
  opposed to a theoretical quantity such as the VC dimension (footnote 1).
- **load α**: effective number of examples per unit of capacity, m_eff/N.
- **temperature τ**: the noise level of the stochastic training dynamics,
  set operationally by learning-rate schedule and iteration count.
- **phase / phase transition / phase diagram**: a region where aggregate
  properties vary smoothly; a point of discontinuity under scaling of the
  control parameters; a plot of the regions (Section 2).
- **thermodynamic limit**: m and N diverge together at fixed α.
- **entropy density s(ε)**: (1/N) log of the volume of hypotheses at error
  ε. It is not a thermodynamic entropy.

## Connections

- **Zhang et al. (2016)** is the target; the paper agrees that
  generalization must be rethought and disagrees on how.
- **Seung, Sompolinsky and Tishby (1992)**, **Haussler, Kearns, Seung and
  Tishby (1996)**, **Engel and Van den Broeck (2001)**: the theory reused.
  None is held in the record.
- **Choromanska et al. (2015)**: the loss-surface evidence, re-read as the
  random energy model.
- **Shwartz-Ziv and Tishby ([LIT-324](../literature.d/LIT-324.md))**: named as concurrent work, not
  engaged.

## Bearing on the record

- **[THEORY-028](../theory.d/THEORY-028.md)** (information-theoretic generalization bound) is a smooth
  upper bound in the information carried about the data. This paper's
  footnote 5 is the relevant caution: "a smooth upper bound on a quantity
  does not imply that the quantity being upper bounded is smooth". The two
  do not conflict; a bound can be valid and blind to phase structure.
- **Singular learning theory ([LIT-616](../literature.d/LIT-616.md), [THEORY-087](../theory.d/THEORY-087.md)).** Both this paper and
  Watanabe replace the regular large-n asymptotics with one that keeps the
  model's geometry. Here the relevant object is the entropy of hypotheses
  near the minimum; in Watanabe it is the volume scaling near the true
  parameter set, which sets the real log canonical threshold. Both are
  volume-near-the-optimum arguments. The paper does not make this
  connection, and the record does not yet hold a reading that does.
- **THEORY candidate (not filed):** "In the thermodynamic limit, a
  generalization error that is discontinuous in the sample-to-capacity
  ratio is produced when the entropy of hypotheses with error just above
  the minimum vanishes faster than the training-error energy grows; a
  continuous weight space gives ε ~ 1/α, an Ising one a jump at αc." Source
  this paper, with Seung et al. 1992 filed to carry it; promote when Seung
  et al. or Engel and Van den Broeck is read.
- **Anthology.** Its practical claim, that early stopping is the one
  effective regularizer for a network fitted to noisy labels, is an ML
  instruction, so `anthology-candidate`.

## Limitations

- **No new theorem and no experiment.** The authors say so: quantitative
  results are left for future work.
- **The load identification rests on N tracking m**, justified only by
  random-label fitting.
- **τ is never defined as a function of training.** Early stopping and
  temperature are related "in some manner that we won't make explicit".
- **The perceptron mechanism is not shown to operate in deep networks.**
  The paper's own word for its extension to them is "conjecture".
- **Reproduction.** The authors report that reproducing Zhang et al.'s
  noisy-label result "was not so easy" (Observation 1), and that empirical
  results in the area are "typically non-reproducible" (Section 5).

## Open questions

- What is the entropy of near-optimal hypotheses in a real network, and
  does it vanish as in the Ising case?
- How does τ depend on iteration count, batch size and learning rate?
  Yang et al. ([LIT-tmpf3sak](../literature.d/LIT-tmpf3sak.md)) take batch size, learning rate and weight
  decay as temperatures operationally.
- Is the spin-glass picture of separate basins under label noise the same
  thing as the poorly connected phases that mode-connectivity measurements
  find?

## Corrections

- none (there was no seed)
