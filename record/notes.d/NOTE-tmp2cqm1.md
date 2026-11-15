---
status: Read
paper: LIT-tmp42zgt
title: 'Tu — Nonequilibrium thermodynamics for biochemical networks'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Read in full on 2026-11-15 from the publisher's PDF (28 pp., CC
    BY-NC-ND 4.0), which the owner uploaded after this session's
    permission system had refused the fetch. Text extracted with
    pdftotext; equations were read through the extraction's garbling
    against their context and figure captions. Read: the abstract, §§1–6,
    the summary points and the figure captions. The reference list was
    looked up for refs. 5, 45, 54, 98, 116 and 117 only. The lead
    reimplemented the four-state adaptation model and checked the
    energy–speed–accuracy relation numerically (see "A check of the ESA
    relation"). Page numbers are the journal's (225–252).
date: '2026-11-15'
summary: >-
  A pedagogical review built on one network motif, a four-state "magic
  square" of two binary variables. With detailed balance it is allostery;
  driven in one pair of edges it gives ultrasensitivity, in the other
  pair adaptation, and as the core of coupled clocks synchronization.
  Each function is impossible or bounded at equilibrium and needs
  dissipation, often above a threshold, and performance is traded against
  cost, as in the energy–speed–accuracy relation for adaptation. It ends
  by proposing a "nonequilibrium thermodynamic law" Ẇ ≥ F(P₁, P₂, …) for
  living systems, with F unspecified in general.
---

<!-- inactive-ok-file: CLAIM-616 — Proposed; named as a synchronization claim the review bears on, no note filed -->

# NOTE-tmp2cqm1: Tu — Nonequilibrium thermodynamics for biochemical networks

## Contribution

The review organizes a body of the author's and others' results around
two questions: why dissipation is needed for biochemical function, and
how its cost bounds performance. Three of its results are its own
syntheses:

- **One motif for several functions.** The four-state magic-square
  network is allostery at equilibrium, ultrasensitivity when driven on
  its activation edges, adaptation when driven on its binding edges, and
  the core of clock synchronization when driven on its diagonal.
- **Thresholds.** Adaptation and synchronization need driving above a
  finite critical value, not merely some driving.
- **A proposed law.** The cases are generalized into a proposed
  "nonequilibrium thermodynamic law" (NTL) for living systems.

## Key insight

"In equilibrium systems, steady-state distributions are dictated solely
by their free energy landscapes in the state space; altering reaction
rates affects only transient dynamics, not their steady states. In
contrast, nonequilibrium systems—fueled by continuous energy
dissipation—can use changes in reaction rates to modulate both dynamics
and steady-state distributions" (§5, p. 246). Dissipation is what lets
kinetics, and so regulation, set where a system sits.

## Assumptions

- **Thermodynamically consistent Markov networks.** Each reaction is
  reversible, and the dissipation rate is the sum over cycles of the
  current times the log rate-product ratio (Hill's cycle rule, §2.2).
- **Leading-order asymptotics.** The adaptation results assume a
  timescale separation (ω± ≫ γk±) and the regime c ≪ r ≪ 1. The
  synchronization results take the continuum limit and a mean-field
  limit (m → ∞).
- **Exactly two binary variables** in the core motif. Multistate
  extensions (methylation ladders) are described qualitatively.
- **kBT = 1** throughout.

## Key results

- **Proofreading has a price** (§2.3, p. 230). "Regardless of the
  underlying mechanisms, energy dissipation sets a bound for error
  reduction: ηmin/η0 ≥ e−G0. Kinetic proofreading is impossible if
  G0 = 0." Hopfield's scheme reaches ηmin = η0².
- **Equilibrium sensitivity is capped by the coupling** (§3.1, p. 232):
  the Hill coefficient of the equilibrium four-state model is about the
  allosteric coupling e_c. Driven, the uncoupled network (c = 1) responds,
  with Heff ≈ 1 − 2√c e^(−ΔW) (§3.2.1, p. 234): "a clear
  cost–performance trade-off".
- **A signature of driving in dwell times** (§3.2.2, p. 236): the
  duration-time distribution of an equilibrium system "is always a
  monotonically decreasing function", so a peaked distribution, as in the
  bacterial flagellar motor's switching intervals, shows the system is
  driven.
- **Adaptation needs dissipation, above a threshold** (§3.3.2,
  pp. 239–240). At equilibrium p0(r) decreases with r, "therefore,
  adaptation is impossible". Adaptation appears when γ ≥ γc, with
  γc ≈ ra/c ≫ 1 for c ≪ 1: "a minimum amount of free energy dissipation
  is required for adaptation". "The adapted state is an NESS, which needs
  to be maintained by constantly consuming free energy" (p. 240).
- **The energy–speed–accuracy relation** (Eq. 39, p. 240):
  Ẇ = c1·Va·ln(c2·Aa), where Va is adaptation speed, Aa = 1/εa its
  accuracy, c1 = 2S0(1 − S0) and c2 = (1 − S0)r/c. It "serves as the
  Pareto front separating the performance space (Aa, Va) into an
  achievable regime and a forbidden regime" (p. 241). Cost grows linearly
  in speed and logarithmically in accuracy.
- **Range against sensitivity** (§3.3.4, p. 241): in the four-state
  model, adaptive range grows as 1/c while sensitivity falls as √c. More
  internal states (M methylation levels) extend the range to c^M ≪ r ≪ 1
  at sensitivity √c. E. coli's Tar receptor has M = 4.
- **Synchronization costs beyond running the clocks** (§§4.2–4.4,
  pp. 243–245). Exchange reactions between clocks break detailed balance
  in mixed local cycles, so "additional energy (in excess of that used
  for driving individual clocks) must be dissipated". Synchronization
  appears only above a critical exchange frequency Ωc = 2k/(E0 − 2),
  which fixes a minimum dissipation Wc(E0). For a given dissipation there
  is an optimal design that maximizes the order parameter.
- **The Kai clock** (§4.5, p. 246): about 16 ATP per KaiC monomer per
  period are consumed against 2 needed for the phosphorylation cycle. The
  surplus is attributed, on a model, to synchronization by monomer
  shuffling.
- **The proposed law** (§5, Eq. 50, p. 246): "Ẇ (= Ṡ) ≥ F (P1, P2, . . .)",
  F "a function of relevant performance metrics". Equality is
  achievable by design, "reminiscent of the Carnot cycle". Living systems
  "are likely evolved to operate near—though not exactly on—the
  trade-off equality line" (p. 247).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Proofreading below the equilibrium error needs dissipation: ηmin/η0 ≥ e^(−G0) | strong | derivation in the three-state model; Hopfield, Bennett |
| C2 | Perfect or near-perfect adaptation is impossible at equilibrium and needs γ ≥ γc | strong | derivation in the four-state model, Eqs. 32–35; checked numerically here |
| C3 | Ẇ = c1Va ln(c2Aa) in the adaptive regime | moderate | leading-order derivation, Eqs. 31–39; reproduced numerically here within its regime |
| C4 | Synchronization of noisy clocks costs dissipation beyond driving each clock, with a minimum | moderate | mean-field continuum model (ref. 116), not rederived here |
| C5 | Peaked dwell-time distributions imply driving | strong | equilibrium dwell distributions are sums of exponentials with positive weights (ref. 98) |
| C6 | Living systems obey Ẇ ≥ F(P1, P2, …) | weak, as a law | a schema generalized from C1–C4; F is not specified in general |

## Method

The review uses chemical master equations on small networks:

- **Steady states** from Hill's spanning-tree method.
- **Dissipation** as cycle current times affinity.
- **Dwell times** by first-passage analysis.
- **Coupled clocks** through a Fokker–Planck continuum limit and a
  self-consistent mean field.

It presents derivations, not new experiments.

## A check of the ESA relation

The lead reimplemented the four-state adaptation model of Fig. 2c, with
rates read from the figure and the text, and solved its exact steady
state numerically. The rates were:

- activation ω+ = rω− in both bound states;
- deactivation ω− (unbound) and cω− (bound);
- binding γk+ (inactive) and k+/c (active);
- unbinding k− (inactive) and γk− (active).

Hill's cycle ratio is γ², as in the text. Parameters: c = 10⁻³, ra = 1,
r = 0.03, ω− = 1 and k− = 10⁻⁹. Results:

- **At equilibrium** (γ = 1) the steady activity tracks the input: 0.83,
  0.94, 0.98 and 0.99 at r = 0.01, 0.03, 0.1 and 0.3. **At γ = 10⁵** it
  stays near S0 = 0.5 (0.48 to 0.56). Adaptation appears only under strong
  driving, as the review says.
- **Dissipation and speed** agree with the review's leading-order
  expressions, Ẇ ≈ 2k̃ra ln γ/(1 + ra) and Va ≈ (1 + ra)k̃, within 5% for
  γ from 10³ to 10⁶.
- **Accuracy** follows εa ≈ (1 − S0)r/(cγ) only while that term exceeds
  the error left at infinite driving. That residual is set by r and c:
  R∞ = r(r + ra)/(r + cra) gives εa ≈ 1.6 × 10⁻³ here, and the computed
  error settles there (1.6 × 10⁻³ at γ = 10⁶).
- **The relation as a whole**: Ẇ/(c1Va ln(c2Aa)) is 0.72, 0.94 and 0.87
  at γ = 10², 10³ and 10⁴. Beyond that it rises (1.3 at γ = 10⁵, 2.0 at
  10⁶), because accuracy stops improving while dissipation keeps growing.

So the relation holds to leading order in its stated regime. Past a
point set by the network's own parameters, more dissipation buys speed
but no accuracy, which the review does not say. The reimplementation is
in the session's scratchpad and is not committed.

## Concepts

- **Hill's cycle rule.** A network is at equilibrium if and only if, for
  every cycle, the product of rates is the same in both directions. The
  log of the ratio is the cycle's driving force Δμ, and dissipation is
  the sum of JΔμ over irreducible cycles.
- **NESS.** A nonequilibrium steady state: a stationary distribution
  with persistent probability currents.
- **The magic-square (MS) model.** Four states of two binary variables.
  Which edges the driving acts on decides the function.
- **Adaptation accuracy Aa = 1/εa and adaptation speed Va.**
- **The ESA relation**, a Pareto front of speed against accuracy at
  fixed dissipation.
- **The NTL.** Dissipation rate is bounded below by a function of
  performance metrics.

## Connections

- **Lineage.** Hopfield (1974) and Ninio on proofreading; Bennett (1978)
  on its dissipation; Hill on cycles; Lan et al. (2012) for the ESA
  relation; Tu (2008) for the flagellar switch; Zhang et al. (2020, 2025)
  for synchronization.
- **The thermodynamic uncertainty relation.** The review does not
  mention it. In the record it is THEORY-1268, a different bound
  of the same family: it prices a current's precision as 1/ε², where the
  ESA relation prices adaptation accuracy as ln(1/ε).

## Bearing on the record

- **QUESTION-452** (does keeping a maintained organization precise cost
  dissipation in proportion to the precision, and does that separate
  maintained from merely lasting structures?). The review supplies, for
  one network, what the question's answer asks for.
  - **A maintained state with a current.** The adapted state is a NESS
    with a persistent current J, and its accuracy is priced.
  - **The price is logarithmic, not proportional.** Ẇ grows with ln Aa
    at fixed speed. It is the speed that is paid for proportionally.
  - **The discrimination.** An equilibrium network holds a steady state
    at no cost, but that state follows the input. Holding a state
    against changing conditions (adaptation) is what dissipation buys,
    and below γc it cannot be had at all. On this showing, what marks
    maintenance is not precision of the state but its independence from
    conditions.

  It does not map any of the record's own organizations (CLAIM-604's
  flame, CLAIM-516's capacities). Dated note filed.
- **THEORY-1268** (the thermodynamic uncertainty relation). The ESA
  relation is a second, model-specific price on a different precision.
  Precision of a counted current costs 1/ε²; accuracy of an adapted
  steady state against input costs ln(1/ε) at fixed speed. The two are
  not in conflict, since they bound different quantities. Dated note
  filed.
- **CLAIM-616** (synchronization as a laboratory for organizational
  distinctions). The review adds that, for noisy molecular clocks,
  coupling has a thermodynamic price above that of running each clock,
  with a threshold. No note filed: the claim does not speak of cost.

## Limitations

- **The "law" is a schema.** With F unspecified, Ẇ ≥ F(P) holds trivially
  for F = 0. Its content is in the system-specific instances: the
  proofreading bound and the ESA relation, the latter proved in one
  four-state model to leading order. The review calls it a proposal.
- **Leading-order results.** The ESA relation fails outside its regime,
  as the check above shows. Accuracy saturates at a residual set by r and
  c, which the review does not discuss.
- **Small models standing for large systems.** The flagellar motor, the
  chemotaxis array and the Kai clock are discussed through minimal models
  whose parameters are not fitted in the review.
- **A review of the author's own programme.** Rival frameworks (the
  thermodynamic uncertainty relation, speed limits, information-theoretic
  costs) are mentioned only in passing, if at all.

## Open questions

- Does the ESA relation's logarithmic price in accuracy hold for
  adaptive networks beyond the four-state model, or only for this motif?
- Could one of the record's maintained organizations be written as such
  a network, so that QUESTION-452's comparison could be made?
