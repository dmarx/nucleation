---
status: Read
paper: 'LIT-1235'
title: 'Power et al. — What can ecosystems learn?'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Read in full on 2026-10-29 from the publisher's version as deposited
    in PubMed Central (PMC4672551, CC BY), fetched as full-text XML from
    Europe PMC's REST service
    (https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4672551/fullTextXML),
    with the erratum (doi 10.1186/s13062-016-0132-7, PMC4915155) read the
    same way and its corrected equation read from the erratum's image on
    PMC. The arXiv v1 (1506.06374) was fetched and used only to check
    equation (1), which carries the same error there. Read: the abstract,
    background, methods parts I and II, results i–iv, discussion,
    conclusions, both reviewer reports with the authors' replies, and
    Appendices A–H, with the captions of Figures 1–11 and Table 1. Figures
    were read from captions and text only; no number was taken from a
    chart. Equations (2) and (3) were checked by hand. The simulations
    were not rerun.
date: '2026-10-29'
summary: >-
  In a competitive Lotka–Volterra community where individual selection
  lowers the competitive effect ω_ij of species j on species i at a rate
  proportional to x_i x_j, and a normalising trade-off holds each row and
  column sum of ω fixed, interactions change as Hebbian learning does. In
  simulation (400 species, symmetric ω) the community comes to hold
  attractors for two past forcing patterns, completes them from fragments
  and switches with hysteresis. The memory needs the imposed trade-off,
  and in the long run it degrades.
---
<!-- inactive-ok-file: CLAIM-288 — Proposed; its caveat is cited as open, nothing here rests on it -->

# NOTE-tmpc6gy4: Power et al. — What can ecosystems learn?

## Contribution

It shows a correspondence between individual-level selection on
interspecific interactions and unsupervised Hebbian learning, and uses a
Hopfield-style simulation to show that a community with no
community-level selection can store and recall more than one past
composition. It offers this as a third option beside "no system-level
organisation" and group selection.

## Key insight

Selection makes each species less sensitive to the competitors it meets
most, and meeting is proportional to joint density, so "species that
occur together wire together". If a species cannot reduce all competition
at once, because of a fixed budget, the relative pattern of who competes
with whom comes to encode the compositions the community has been forced
into, and those compositions become attractors.

## Assumptions

- **Ecology** (eq. 1 as corrected by the erratum): dx_i/dt = (m_i x_i /
  k_ie)(k_ie + Σ_j ω_ij x_j), ω_ii = −1, all ω_ij ≤ 0 (competition only).
- **Selection** (eqs. 2–3): a mutant in i with ω_ij′ raised by g has
  selection coefficient s = (m_i/k_ie) g x_j′; with fixation probability ∝
  s, the rate of change is v_ij = (m_i/k_ie) g µ x_i x_j. Only changes to
  ω_ij (how j affects i) are selected; side-effects are ignored
  (Appendix A).
- **Trade-off** (Appendix C): after each update every row and column sum
  of the off-diagonal ω is renormalised to its initial value Q_i.
- **Simulation**: symmetric ω, N = 400, ecology run to equilibrium (τ =
  5000 steps) between evolutionary updates; environments E1 and E2 shift
  carrying capacities k0 ± α (k0 = 10, α = 0.1) in two 20 × 20 pictogram
  patterns, switching every update (T = 1).

## Key results

- **Hebbian rule.** v_ij ∝ x_i x_j, Table 1(g); robust in sign pattern to
  two models with linkage or rare outcrossing (Appendices B, D, Figs. 7–8).
- **One memory** (Experiment 1): after 800 cycles in E1 the community
  returns to the E1 pattern under E0 or E2 forcing, "some distortion" in
  E2 (Fig. 3).
- **Two memories** (Experiment 2): with E1 and E2 alternating, the evolved
  community without forcing has two attractors, E1 and E2, and not their
  union; it completes patterns from small parts, repairs corrupted ones
  and goes to the nearer of the two from mixtures (Fig. 5).
- **Hysteresis.** Before evolution the response to forcing moving from E1
  to E2 is proportional; after, it is switch-like with hysteresis, and
  only for forcing along remembered directions; arbitrary forcing stays
  linear (Fig. 6, Appendix E, Fig. 9).
- **Breakdown.** The two-attractor state appears around generation 525,
  then one attractor outcompetes the other and, after about 575
  generations, the remaining one degrades (Figs. 10–11, Appendix F).
- **The trade-off is necessary**: without it, selection "make[s] high
  density species fitter in all conditions" and no memory forms
  (Appendix H).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Individual selection changes ω_ij at a rate proportional to x_i x_j | moderate | eq. 3 under strong-selection, weak-mutation fixation; robust in sign (App. B, D) |
| C2 | With normalising trade-offs these changes have the sign pattern of Hebb's rule | moderate | Figs. 4, 8, for the simulated cases |
| C3 | A community can hold and recall several past compositions without community-level selection | moderate | simulation, symmetric ω, one parameter set |
| C4 | The memory persists | weak | contradicted in the long run by the paper's own Figs. 10–11 |
| C5 | Critical transitions may be the recall of remembered states | weak | interpretive, from Fig. 6 |

## Concepts

- **Ecological memory** (after Thompson et al.): past conditions and
  selection encoded in the current structure of a community.
- **Unsupervised correlation learning**: changing connections to
  reinforce frequent co-activations, with no reward signal.
- **Normalising constraint**: a fixed total of competitive interaction per
  species, so lowering one raises others.

## Connections

The neural side is Hopfield's associative memory (LIT-918), whose
symmetric weights give a Lyapunov function, as symmetric ω does here.
Watson and Szathmáry's "evolution can learn" programme, of which this is
the ecological instance, is not registered. The symmetric Lotka–Volterra
community is the setting of CLAIM-369.

## Bearing on the record

- **QUESTION-083** asks whether processes sharing one rule can come to
  hold differentiated, mutually regulated organization with no
  governance role coded in. This paper is a positive instance in its own
  domain, but with a coded-in constraint: the normalising trade-off. The
  authors say the result depends on it (Appendix H), and it is imposed
  as a renormalisation step, not derived. The question's caveat, that a
  positive answer shows organization from fixed local objectives and not
  self-constitution (CLAIM-288), applies here too.
- **CLAIM-369**: the simulations keep ω symmetric, which gives the
  community a potential, and the paper relies on that ("the dynamics have
  only fixed point equilibria"). It is CLAIM-369's class with the
  interaction matrix evolving slowly. Evolution here reshapes the
  objective the community descends, which the claim's fixed-U setting
  does not cover.
- **QUESTION-132**: the long-run breakdown, one attractor outcompeting
  the other, is an instance of the question's "entrenched asymmetry"
  outcome emerging from initially balanced memory.
- No instruction for machine-learning practice; nothing for the
  anthology.

## Limitations

- **Equation (1)** as published has a stray "+": "dx_i/dt = (m_i x_i /
  k_ie) + (k_ie + Σ ω_ij x_j)". The erratum corrects it to the product.
  The arXiv v1 has the same error.
- **The renormalisation equations (10)–(11)** divide each entry by its
  row (or column) sum, which sets the sums to 1 and flips the sign of
  negative entries, while the text says the sums are held at Q_i < 0. The
  factor Q_i is missing from the printed formulas.
- **Parameter inconsistencies.** Appendix C gives g = 0.01 and α = 0.1;
  the Figure 7 caption uses g = 0.1 and the Figure 8 caption g = 0.1 and α
  = 3.5, without saying these runs differ.
- **Text slips.** In result iv, the forcing moves "from E1 to E1" and the
  system "switch[es] to E1"; E2 is meant in two of those places. The
  Figure 5 caption labels its fourth panel "e".
- **Symmetry** is imposed in simulation though individual selection acts
  on ω_ij only; the authors argue the selective pressures are symmetric
  "except for the influence of individually-varying carrying capacities"
  (Appendix H), which are exactly what the forcing varies.
- **Fixation probability** is taken equal to s; the usual approximation
  is 2s. A constant, so the direction of the results is unaffected.
- **Transience.** The two-memory state lasts a bounded window of
  evolutionary time before collapse.

## Open questions

- Does a stoichiometric or resource-explicit model, which the authors
  suggest, produce the normalising trade-off endogenously?
- Do the results survive asymmetric ω, where cycles are possible?
