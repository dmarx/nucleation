---
status: Read
paper: LIT-tmpfy5q0
title: 'Life as we know it'
version: 1
history:
- version: 1
  date: '2026-10-02'
  note: >-
    Read in full: the author's posted copy of the published article (12
    pp., from fil.ion.ucl.ac.uk/~karl/; text and equations extracted with
    PyMuPDF), checked against the PMC full text (PMC3730701, Europe PMC
    XML, whose equations are images). I read §1 (Introduction), §2
    (heuristic proof, Eqs. 2.1–2.9, Lemma 2.1, Remarks 2.2), §3 (the
    primordial soup, Eqs. 3.1–3.3, §§3.2–3.5), §4 (Conclusion), Table 1,
    Figs. 1–5 with legends, and the 62 references. I followed each step
    from Eq. (2.1) to Eq. (2.9) and recomputed the p-value in the Fig. 4
    legend. The SPM simulation code was not run, so the simulation results
    are taken as reported.
date: '2026-10-02'
summary: >-
  The flow of internal and active states in an ergodic system with a
  Markov blanket, written in Helmholtz form, can be redescribed as gradient
  descent on a variational free energy once the variational density is set
  equal to the posterior over external states. On that redescription such
  systems "appear" to infer and to bound their own entropy, which the paper
  calls the marks of life. One simulated soup shows a blanket-enclosed
  cluster that predicts external motion and falls apart under lesions. The
  free energy is variational, not thermodynamic. The candle flame is
  excluded by a one-sentence assertion. The paper's own reported p-value is
  not reproduced by the null it describes.
---

<!-- inactive-ok-file: THEORY-026 THEORY-043 — Proposed; named as the accounts this reading is placed against, not as support -->

<!-- inactive-ok-file: LIT-tmpncmdx — Deferred: Schrödinger is unread; named because the paper takes its epigraph and question from it, not leaned on -->

# NOTE-tmpokduu: Life as we know it

## Contribution

Before this paper, the free energy principle was argued as a necessity:
systems that did not minimize free energy would not keep their sensory
entropy bounded, so living systems must. This paper inverts the argument.
Any ergodic system with a Markov blanket can be *described* as minimizing
a variational free energy, so inference-like and self-maintaining behaviour
is "(almost) inevitable" wherever blankets form. It adds a simulation that
operationalizes four marks of the lifelike: ergodicity, a blanket,
predictive coupling across the blanket, and dispersion under lesion.

## Key insight

If internal states are shielded from external states by a blanket, their
time-averaged flow can depend on external states only through the
posterior given the blanket. So their motion can be read as if they encoded
beliefs about what lies outside. Self-maintenance is then the same flow
seen as bounding the entropy of the blanket and internal states.

## Assumptions

- **Dynamics (Eq. 2.1).** ẋ = f(x) + ω, with the partition x = (ψ, s, a,
  λ): external, sensory, active, internal. Sensory and external flows
  depend on (ψ, s, a); active and internal flows depend on (s, a, λ).
- **Ergodicity.** The system converges to a random global attractor with
  an ergodic density p(x|m) solving the Fokker–Planck equation (Eq. 2.2).
- **Helmholtz form (Eq. 2.3).** f = (Γ + R)·∇(−G), with Γ the diffusion
  tensor and R antisymmetric. Eq. (2.4) then takes p = exp(−G) as the
  stationary solution "using this standard form". For state-dependent Γ
  or R that solution needs a correction term the paper does not write; it
  holds as written when they are constant.
- **Eq. (2.6) moves (Γ + R) outside the integral over ψ.** That requires
  the relevant blocks of Γ + R not to depend on ψ. This is not stated.
- **The variational density is parametrized by internal states only,**
  q(ψ|λ), but the proof sets it equal to the posterior p(ψ|s, a, λ),
  which in general depends on s and a too. The step needs the posterior to
  depend on the blanket only through λ, or q to be read as q(ψ|s, a, λ).
  This is not stated.
- **Short-range coupling makes blankets (almost) inevitable.** Asserted:
  "if the coupling between dynamical systems can be neglected … the
  intervening systems will necessarily form a Markov blanket". Not shown
  for any physical system.
- **A blanket's couplings must change slowly** relative to the states.
  This is introduced to exclude the candle flame and used again in the
  conclusion.

## Key results

- **Eqs. (2.5)–(2.6).** Internal and active flows are a "circuitous
  gradient ascent" on ln p(s, a, λ|m), the marginal over blanket and
  internal states, once averaged over external states.
- **Lemma 2.1 (Eqs. 2.7–2.8).** F(s, a, λ) = E_q[G] − H[q] = −ln p(s, a,
  λ|m) + D_KL[q(ψ|λ) ‖ p(ψ|s, a, λ)]. Eq. (2.6) "requires the gradients of
  the divergence to be zero", so q equals the posterior, D_KL = 0, and the
  flows are −(Γ + R)·∇F. Given the assumptions above this is consistent,
  but it is a redescription: F equals −ln p(v) by construction at that
  point, so "minimizing free energy" says no more than Eq. (2.6) already
  said.
- **Eq. (2.9).** F ≥ −ln p(s, a, λ|m), so the time average of F
  upper-bounds the entropy H[p(s, a, λ|m)]. Read as action "plac[ing] an
  upper bound on their dispersion". The entropy is fixed by the ergodic
  density the system already has; nothing in Eq. (2.9) is controlled.
- **Simulation (§3).** 128 subsystems, forward Euler with step 1/512 s,
  unit-variance noise. Ergodic behaviour is reported "for most values of
  the parameters", after about 1000 s. The principal eigenvector of B = A
  + Aᵀ + AᵀA, with A taken over the last 256 s of 2048 s, picks k = 8
  internal subsystems; their blanket is recovered as [B·χ]. Functionally
  closed subsystems end up at the periphery, and "no simulation ever
  produced a functionally closed internal state".
- **Prediction across the blanket (§3.4, Fig. 4).** Canonical variates
  analysis of 32 eigenvariates of lagged internal states against the
  motion of each external subsystem; 5 of 82 exceed the largest χ² of a
  time-reversed null. Reported p = 0.00052.
- **Lesions (§3.5, Fig. 5).** Making active, sensory or internal
  subsystems functionally closed makes the cluster disperse within 512 s.
  The intact cluster holds its "quasicrystalline arrangement".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | In an ergodic system with a Markov blanket, internal and active flows can be written as gradient descent on a variational free energy | moderate | Lemma 2.1, given unstated conditions on Γ, R and q (Assumptions); a redescription, not a new dynamical fact |
| C2 | Such systems therefore appear to perform Bayesian inference about external states | interpretation of C1 | Remarks 2.2; "appear" is the paper's own hedge |
| C3 | Action places an upper bound on the entropy of the blanket and internal states, i.e. self-maintenance | weak as a causal claim | Eq. (2.9) is an inequality about a fixed ergodic density |
| C4 | Markov blankets are (almost) inevitable under short-range coupling, so lifelike behaviour is (almost) inevitable | assertion | no argument beyond the sentence; the conclusion concedes it does not address "the conditions … necessary for the emergence of ergodic Markov blankets" |
| C5 | A simulated soup shows a blanket whose internal states predict external motion | moderate, for one run | Fig. 4; 5/82 above a single time-reversed null; the p-value is not reproduced (Corrections) |
| C6 | Lesioning blanket or internal states destroys structural integrity (autopoiesis) | weak to moderate | Fig. 5; one run per lesion type, assessed by eye |
| C7 | A candle flame cannot possess a Markov blanket | assertion | one sentence (§2); no model of a flame |
| C8 | Minimum-entropy Markov blankets may characterize biological systems | conjecture | §4, labelled "speculative" |

## Concepts

- **Markov blanket.** A set of states separating internal from external
  states in the conditional-independence sense: parents, children and
  parents of children (Pearl). Here it is split into sensory states
  (children of external states) and active states (not).
- **Ergodic density.** The occupancy measure of the random attractor, read
  as the probability of finding the system in a state.
- **Gibbs energy G.** −ln p(x|m), the potential in the Helmholtz form.
- **Variational free energy F.** E_q[G] − H[q], the bound from variational
  Bayes (Feynman; Hinton & van Camp; Beal). It is not a thermodynamic free
  energy, and the paper does not claim it is.
- **Active inference.** Internal states appear to infer external causes;
  active states, through the blanket, change the external states that
  cause sensations.
- **Autopoiesis (operational).** Self-organized dynamics are necessary to
  maintain structural integrity, tested by lesion.

## Connections

- **Schrödinger (1944), the paper's epigraph and ref. [1].** It takes
  Schrödinger's question, how events "within the spatial boundary of a
  living organism" are accounted for by physics. Its answer locates the
  boundary in statistics rather than in a membrane. Filed beside it in
  this batch as [LIT-tmpncmdx](../literature.d/LIT-tmpncmdx.md) (Deferred).
- **Dissipative structures.** §3 compares the soup with Turing
  instabilities, Bénard cells and the Belousov–Zhabotinsky reaction, and
  calls the ensemble "dissipative at two levels": viscous friction, and
  non-divergence-free functional dynamics. Neither sense is entropy
  production.
- **Conant & Ashby, the good regulator theorem (ref. [13]).** Invoked as
  "exactly consistent". Not held in the record.
- **Predictive information (Bialek, Nemenman & Tishby; Ay et al.; refs.
  [22–24]).** Named as related; the information bottleneck lineage is
  [LIT-338](../literature.d/LIT-338.md).
- **Still et al., [LIT-327](../literature.d/LIT-327.md) ([NOTE-295](NOTE-295.md)), and [THEORY-026](../theory.d/THEORY-026.md).** See "Bearing on
  the record".
- **Seth, [LIT-135](../literature.d/LIT-135.md) ([NOTE-169](NOTE-169.md)).** Seth's route from the free energy
  principle to autopoiesis passes through a claimed equivalence of
  variational and thermodynamic free energy. This paper does not provide
  it.
- **Levin, [LIT-439](../literature.d/LIT-439.md) ([NOTE-341](NOTE-341.md)).** Blankets nest (animal, organ, cell,
  nucleus), as Levin's Selves do.

## Bearing on the record

- **[THEORY-026](../theory.d/THEORY-026.md) (Proposed): a different and weaker claim, not a second
  source.** [THEORY-026](../theory.d/THEORY-026.md) is a physical identity, dissipated work equals
  nonpredictive memory, for a system driven *without* feedback. Friston's
  internal states "predict" external states in a system defined by
  feedback (active states change external states). His "prediction"
  carries no work or heat. Where it touches the THEORY, it falls on the
  feedback side, where [THEORY-026](../theory.d/THEORY-026.md) (from [LIT-041](../literature.d/LIT-041.md)) says prediction is no
  longer what efficiency requires. This paper should not be cited as
  thermodynamic support for "living systems are efficient predictors".
- **[THEORY-043](../theory.d/THEORY-043.md) (Proposed).** Nested blankets, each inducing "active
  (Bayesian) inference", are a case of minded parts inside a minded whole.
  The paper takes no position on anti-nesting, and its conjecture (C8)
  would pick one blanket out by entropy. That is a candidate architectural
  criterion of the kind [THEORY-043](../theory.d/THEORY-043.md) says is not yet principled. It is
  conjectured here, not argued.
- **[LIT-192](../literature.d/LIT-192.md) / [NOTE-094](NOTE-094.md), the demarcation question.** The only text in this
  batch that names the candle flame and draws a line against it (C7). The
  line, persistence of a conditional-independence structure, is principled
  in form but asserted, not shown, and the conclusion's "uncountable number
  of Markov blankets" puts the burden back on a conjecture (C8).
- **[LIT-021](../literature.d/LIT-021.md) / [NOTE-007](NOTE-007.md) C8.** [NOTE-007](NOTE-007.md) recorded, secondhand and
  unassessed, the claim that life is emergent in any random dynamical
  system with a Markov blanket. Assessed here: it is the paper's claim, and
  its support is C1 (a redescription) plus C5–C6 (one simulation).
- **No ML instruction.** The paper uses variational Bayes to describe
  organisms; it recommends nothing for building or training models. The
  anthology does not hold it.

## Limitations

- The inference reading depends on the choice q(ψ|λ) = posterior. Any
  ergodic system with the stated sparsity can be redescribed this way, so
  the description does not separate living from non-living systems with
  blankets. The paper concedes this in §4.
- Γ and R are taken as constant without saying so, and the q(ψ|λ) versus
  p(ψ|s, a, λ) mismatch is unaddressed (Assumptions).
- The free energy is variational. The paper computes no heat, work or
  entropy production. Its contact with thermodynamics is the
  introduction's appeal to the fluctuation theorem.
- The simulation is one parameter setting, with internal states fixed at k
  = 8 by the analyst, a blanket recovered from an adjacency matrix
  aggregated over 256 s, and lesion effects judged visually.
- Ergodicity is assumed for living systems, and the conclusion concedes
  that real systems are "only locally ergodic".

## Open questions

- Is there a formal criterion that separates a candle flame from a cell
  on the blanket account, and does a model of a flame actually lack one?
- Does the minimum-entropy blanket conjecture (C8) pick out the systems we
  call living in any worked case?
- Under what conditions on the coupling does a sparse coupling graph give
  a blanket in the *stationary density* (which the lemma needs), and not
  only in the instantaneous dynamics?

## Corrections

- none to a seeded skim (there was no seed)
- **The reported p-value does not follow from the stated null.** The Fig. 4
  legend says the largest null statistic protects against false positives
  "at a level of 1/82", and that five true statistics above it give p =
  0.00052. Under that per-element rate, P(≥ 5 of 82) is binomial: I compute
  0.0034, about six times larger. The result is still small, but the
  figure printed is not reproduced by the stated procedure, and the paper
  does not say how 0.00052 was obtained.
