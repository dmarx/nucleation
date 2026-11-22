# Reader notes: azizpour2026 (LIT-2980, arxiv:2602.09491)

## Step 1: copies located (2026-11-22)

- https://arxiv.org/abs/2602.09491 : arXiv abstract page, 200. Authors Sahel
  Azizpour, Viola Priesemann, Johannes Zierenberg, Anna Levina; v1 only,
  10 Feb 2026.
- https://arxiv.org/pdf/2602.09491 : arXiv preprint PDF (v1, 11 pp.), author's
  manuscript, lawful (arXiv). Fetched, 200, application/pdf.
- doi:10.1038/s42005-026-02584-w (Communications Physics): published version,
  per the LIT's history; not fetched (arXiv copy suffices).

## Step 2: read (2026-11-22)

Read in full: arXiv v1 PDF (dated "February 11, 2026"), main text pp. 1-4,
Methods pp. 5-7, references pp. 7-9, Supplementary Information pp. 10-11
(Fig. S1, Kramers-Moyal recap). Nothing skipped. Text extracted with
pdftotext; figures read from their captions and axis labels only. The
Communications Physics version (doi:10.1038/s42005-026-02584-w) was not
compared; the journal details in LIT-2980 are not confirmed by the arXiv copy,
which names no journal. Code: GitHub sahelazizpour/Finite-Observation-Dynamic-Range
(named in the paper, not fetched).

## Step 3: recheck (2026-11-22)

Second grep of record/ for: Kinouchi/Copelli, dynamic range, reverberating,
Priesemann/Zierenberg/Levina, Wilting, Toyoizumi, quasicriticality, edge of
chaos, avalanche, branching, critical slowing, speed-accuracy, integrated
Ising, Larremore/Shew, Muñoz, Boedecker. Most hits are false (holography
"dynamic range", Larremore's bipartite SBM, Muñoz on deep brain stimulation).
Held entries the first search missed, with bearing, are in the report below.
No neighbour needed: the work itself was read.

## Step 4: report

### Provenance
- Read: https://arxiv.org/pdf/2602.09491 (arXiv v1, PDF, 11 pp., cond-mat.dis-nn,
  submitted 10 Feb 2026 by J. Zierenberg), fetched 2026-11-22, HTTP 200. Kind:
  arXiv preprint, the authors' manuscript; lawful. Whole text read, SI included.
- Located, not read: the Communications Physics version,
  doi:10.1038/s42005-026-02584-w (from LIT-2980's history). Not attempted, since
  the arXiv copy suffices; no obstacle met.
- Authors (arXiv metadata and title page): Sahel Azizpour, Viola Priesemann,
  Johannes Zierenberg, Anna Levina (Tübingen / MPI Biological Cybernetics; MPI
  Dynamics and Self-Organization / Göttingen). LIT-2980's author list is right.
- No email address sent anywhere.

### Summary
A random sparse network of N = 10^4 binary probabilistic spiking neurons
(rectified-linear activation probability, weights w_ij = λ/K_i, so λ is the
largest eigenvalue and the branching parameter) receives Poisson input at rate h
on a subset (μ = 0.2) and is read out from another subset (ν = 0.2) by a leaky
integrator with timescale T plus Gaussian noise σ. The transition is the
absorbing-to-active one at λ_c = 1 for h → 0. The authors define two measures of
discriminability from the ideal-observer overlap error E(h1,h2) of output
distributions: the number n_d of ε-discriminable inputs, and a generalized
dynamic range Δ(ε). They solve the limits T → ∞ (mean field) and T → 0
(Fokker-Planck after a Kramers-Moyal expansion), and fill in finite T from
simulations fitted with Beta distributions whose parameters a small neural
network interpolates. Both measures peak at a subcritical λ* < 1 for finite T,
and λ* moves toward 1 as T grows.

### Contribution
A worked trade-off of the form λ* = argmax {G(λ) − γL(λ)} (Eq. 1) for one
system: the gain is the sensitivity critical systems are known for (Kinouchi and
Copelli's dynamic range, ref. 11), the loss is the confidence lost to correlated
critical fluctuations over a finite readout window. It turns "criticality
maximizes dynamic range" into "it does so only in the limit of infinite
integration time".

### Key results
1. Optimum subcritical for finite T (p. 3, Fig. 2a): "n_d exhibits a maximum at
   a T-dependent subcritical λ < 1, above which it decays for λ → 1 ... every
   finite integration time will have an optimal 0 < λ < 1, while for infinite
   integration time, n_d is bound by the Gaussian noise of the readout."
2. Dynamic range likewise, with a different optimum (p. 3, Fig. 2b): "a finite
   T results in a substantial reduction of the dynamic range in the vicinity of
   the critical point ... the dynamic range develops a T-dependent maximum,
   which is, however, different from the maximum of n_d".
3. Direction of the shift (Fig. 2 caption, p. 4): "With increasing timescale T,
   the maximum λ* moves closer to the critical point". Abstract and p. 2:
   "a safety margin from the precise critical point for all finite integration
   times".
4. Monotonicity at fixed λ (p. 4): "both measures of discriminability increase
   monotonically with T"; "For finite T, the optimal balance is achieved by
   subcritical networks."
5. Mechanism (p. 4): "emergent temporal fluctuations close to a critical phase
   transition can smear out the signal if they are aligned with the readout
   ... this implies a trade-off between sensitivity and discriminability."
6. Scope disclaimed (p. 4): "On which side of the transition this optimum lies
   will, however, depend on both the task and the type of phase transition,
   e.g., absorbing-to-active, transition to chaos, or a bifurcation"; for the
   transition to chaos, citing Toyoizumi and Abbott (ref. 40), "deviations
   toward the supercritical side ... are thus beneficial in the presence of
   noise".
7. Reservoir computing (p. 4): "an instantaneous readout would require a larger
   distance to criticality for optimal discriminability. However, leaky readout
   units could allow the reservoir to be tuned closer to criticality".
8. Biological timescales (p. 4): with τ ≈ −Δt/ln λ the optima "correspond to
   τ ≈ 10 − 100 ms, assuming a timestep Δt = 1 ms, or to τ ≈ 50 − 500 ms for a
   timestep Δt = 5 ms", "consistent with" cortical timescales of 50 ms - 1 s.

### Assumptions
- Stationary input of fixed rate h; the task is discriminating input rates
  (magnitude), not temporal patterns, memory or nonlinear functions.
- Ideal observer, equal priors; error is distribution overlap (Eq. 3).
- Excitatory-only network; mean-field and second-order Kramers-Moyal
  approximations for the analytic limits; the coupled Fokker-Planck equations
  decoupled by substituting mean-field relations (Eqs. 15-16).
- Finite-T distributions approximated as Beta, interpolated by a neural network
  with a physics-informed penalty on the mean.
- A greedy algorithm for the set of discriminable inputs (close packing has no
  unique solution); n_d is the average of left and right passes.
- Readout noise σ = 10^-2, added partly "to be able to technically treat
  δ-distributed outputs".

### Concepts
Branching parameter / largest eigenvalue λ; absorbing-to-active transition;
dynamic range (Kinouchi-Copelli, 10%-90%) and its ε-generalization;
ε-discriminable inputs; ideal-observer discrimination error; leaky readout
integration timescale T; critical slowing down and correlated fluctuations;
sensitivity-confidence-integration-time trade-off; reverberating (subcritical,
near-critical) regime (ref. 21, Wilting et al.).

### Verdict on the exchange's characterization
Accurate in substance, with three qualifications. LIT-2980 and QUESTION-507 say
a finite window moves the best discrimination off the critical point; CLAIM-809
strand 3 says "A finite integration window moves the best discrimination of
inputs away from the critical point". The paper says exactly that (results
1-3). Qualifications: (a) the shift is to the subcritical side and shrinks as T
grows, the critical optimum recovered only as T → ∞; (b) the transition is
branching (absorbing-to-active) criticality, not the edge of chaos, and the
paper itself says side and result depend on the transition type (result 6);
(c) "sensitivity" is input-rate discriminability and dynamic range, not memory
or computation in general. The exchange's "three-way tradeoff of sensitivity,
reliability and speed" matches the paper's sensitivity / confidence /
integration time (result 5), "speed" being the readout window, not reaction
time. LIT-2980's summary is fair for this model; its "Communications Physics
(2026)" is not confirmed by the arXiv copy. "Fisher information" does not occur
in the paper; its measure is overlap error.

### Bearing on the named codes
- **CLAIM-809: supports strand 3, and qualifies it.** Results 1-3 support "the
  best distance from the transition depends on ... the integration window";
  results 1-2 (n_d and Δ peak at different λ) support "depends on the task",
  here the measure. Qualify: one transition (branching), one task family (rate
  discrimination). The paper's "On which side ... will depend on both the task
  and the type of phase transition" independently states the thesis's final
  sentence. Silent on strands 1, 2, 4, 5. Does not meet `defeated_if`; the
  defeater's "every finite integration window" fits result 3, since at T → ∞
  the critical optimum returns.
- **QUESTION-507: supports one part, leaves the rest open.** Point 2 (which
  measure): a case with two discriminability measures whose optima differ.
  Point 1 (which transition): the paper is on branching criticality, and says
  the chaos transition can differ (Toyoizumi and Abbott, supercritical side).
  It gives performance against distance from the transition, which "What would
  answer it" asks for and Dambre did not give, but for one measure family and
  with no conserved total being redistributed. Point 3 (environment): input is
  a stationary rate, so silent.

### Recheck: held entries the first search missed
- **QUESTION-091** (organizations at different distances from criticality, by
  branching ratio): same transition; a case where a subsystem's best distance
  is set by its readout window, and "living systems need to adjust their state
  ... depending on the specific processing tasks" (p. 4) fits its control
  framing. Parallel/supports.
- **CLAIM-850** (chaos, criticality, cascades distinct): supports, by the
  paper's distinction of absorbing-to-active, chaos and bifurcation as giving
  different optima (result 6).
- **CLAIM-814** (scalar linear reservoir; readout noise makes capacity rise
  monotonically toward a = 1): contrast. There readout noise pushes the optimum
  to the transition; here readout noise plus a finite window over critically
  slowed internal fluctuations pushes it away. In this network internal
  fluctuations grow relative to the signal near λ = 1 and are not averaged out
  within T; in CLAIM-814 signal and noise share one filter. Worth a sentence
  when CLAIM-809 is revised.
- **ARG-148**: contrast/background as for CLAIM-814; the paper shows no bound.
- **CLAIM-626** (critical slowing has no single organizational meaning):
  parallel; here slowing is the loss term.
- **CASE-303** (Poisson branching cascades below and at criticality):
  background, the same branching regime.
- **NOTE-054** (whole-brain models; "The brain operates near criticality, where
  dynamic range and information capacity are maximal", cited not re-examined):
  qualified: the dynamic-range maximum at criticality holds only for infinite
  integration time, in this model.
- **LIT-569 / LIT-576** (two-alternative decision models, speed-accuracy):
  parallel; the paper's ref. 20 (integrated Ising decision model, Tapinova et
  al. 2025) frames the same reaction-time/error trade-off; not held.
- Not held, candidates if CLAIM-809 or QUESTION-507 is to name them: Kinouchi
  and Copelli 2006 (ref. 11, the gain qualified here); Toyoizumi and Abbott 2011
  (ref. 40, the chaos-side counterpart); Wilting et al. 2018 (ref. 21,
  reverberating regime).

### Limitations
- One model class (excitatory branching network, stationary Poisson input), one
  task family (rate discrimination); generality is expected ("We expect", p. 4),
  not shown.
- Intermediate T rests on Beta fits and a neural-network interpolator; the
  analytic limits are mean-field and second-order. With ν = 0.2 the numerics sit
  less well between the analytic bounds than with full readout (Fig. S1: "in
  this case the numerical results interpolate better").
- n_d comes from a greedy, non-unique packing; Δ depends on ε and σ, which are
  "tuned to recover the typical 10%-90% bounds".
- The biological mapping hangs on the assumed timestep (1 ms vs 5 ms).
- Short letter; no uncertainty on λ* is discussed.
- Only arXiv v1 read; the journal version may differ.

### Candidate THEORY sentence
Azizpour, Priesemann, Zierenberg and Levina show, analytically in the limits and
by simulation between them, that in a random network of stochastic spiking
neurons with a branching (absorbing-to-active) transition at λ = 1, a leaky
readout with finite integration time T makes both the number of ε-discriminable
input rates and a fluctuation-aware dynamic range peak at a subcritical λ* < 1,
at different λ* for the two measures, with λ* approaching the critical point as
T grows, because critically slowed population fluctuations not averaged out
within T blur the readout.

`promote_when`: an independent study (a replication with the authors' released
code, or another model with an absorbing-to-active transition and a finite-time
readout) finds discriminability maximal at a subcritical coupling that moves
toward criticality as the readout's integration time grows.
