---
status: Read
paper: LIT-989
title: 'Tissot et al. — An ability to respond begins with inner alignment'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the bioRxiv PDFs (CC BY-NC 4.0), extracted with
    pdftotext -layout. Version 2 (posted 2024-05-17, 28 pages, fetched
    after repeated 429 responses) is the text read closely and quoted
    here: abstract, Introduction, Model (including the new subsection
    "The hard problem of transitions"), Experiments and results,
    Discussion, Conclusions, Box 1, all nine figure captions and Appendix
    A. Version 1 (2024-02-21, 24 pages) was also read in full and
    compared: v2 rewrites the unit equation (Eq. 3), widens the noise
    range, adds the sensitivity–action argument, the hard-problem framing,
    a paragraph on reductionism and a Conclusions section; the results
    and parameters are otherwise the same. No published version was found
    (bioRxiv's API lists none). Figures were read from their captions
    only, so plotted trajectories were not checked. Equations were
    restored by eye where extraction split them.
date: '2026-10-14'
summary: >-
  In a simulated modular coordination game (30 modules of 10 bistable
  units, strong couplings inside modules, weak across), units that adjust
  only the phase of their decision cycle toward partners they currently
  agree with come to synchronise within modules. Each module then switches
  its convention as one unit in response to the others, and all 50 runs
  with the learned phases reach a global optimum, against none without.
  Global synchrony does not do this. Synchrony works by silencing the
  module's internal pull at a shared moment, not by any signal passed
  inside it.
---
<!-- inactive-ok-file: THEORY-tmph3haa — Proposed; the theory filed from this reading -->
<!-- inactive-ok-file: CLAIM-172 CLAIM-157 THEORY-232 THEORY-069 — Proposed; the entrainment mark, block answer and accounts this reading bears on, open -->

# NOTE-tmp9ypte: Tissot et al. — An ability to respond begins with inner alignment

## Contribution

The paper gives a bottom-up mechanism by which a group of minimal
deciders becomes a unit that decides in the same minimal sense. Before,
each module of strongly coupled units settles on a convention and cannot
change it. Afterwards it switches as a block when the other modules pull
it. The mechanism changes only when units decide, never what they decide,
and each change is paid for by an immediate individual gain. The authors
offer it as a solution to what v2 calls "the hard problem of transitions
in agency": a transition that is both "systematic" (driven by individual
incentives) and "meaningful" (it changes outcomes).

## Key insight

A decider that alternates between being sensitive but inactive and being
active but insensitive is held in place by its strongest partners only
while they are acting during its sensitive phase. If the strongly coupled
partners synchronise, they all become sensitive at the same moment, the
internal pull vanishes for that moment, and the only influence left is the
weak pull from outside. "Synchronisation changes the 'attention' from
themselves to their environment - from the ingroup to the outgroup." The
same strong couplings both reward synchrony now and trap the group later,
which is why individually motivated synchrony finds exactly the groups
whose joint switching pays.

## Assumptions

- **The game.** A symmetric modular coordination game, Eq. 1:
  c_ij = 1 within a module (⌊(i−1)/k⌋ = ⌊(j−1)/k⌋), 0.01 across;
  N = 300, k = 10. Energy E(t) = −Σ_ij c_ij s_i(t) s_j(t) (Eq. 2). There
  are 2^30 local optima and two global optima. Constraints are
  consistent, so all can be satisfied at once, and modules do not overlap
  (footnote 2).
- **The unit (v2, Eq. 3).** s_i(t+1) = γ_i(t)(I(∂U_i/∂s_i) + ε_i(t)),
  with ∂U_i/∂s_i = Σ_j c_ij s_j(t) (Eq. 4), I(x) = max(min(100x, 1), −1),
  ε uniform in [−0.01, 0.01], and the decision cycle
  γ_i(t) = (sin(ωt + θ_i) + 1)/2, ω = 0.01. (v1's Eq. 3 had a decay term
  s_i(t)(1 − τ) with τ = 0.1 and γ_max = 0.1.)
- **The timing rule (Eq. 5).** θ_i(t+1) = θ_i(t) + ν Σ_j (π/4) c_ij
  sgn(s_i s_j) sin(θ_j − θ_i), ν = 3·10⁻⁵. Phases attract when the pair's
  states agree with the sign of the coupling and repel otherwise. It is
  derived in Appendix A from a cycle-averaged pair utility
  U_ij ≈ c_ij sgn(s_i s_j)(π/2 + (π/4) cos(θ_i − θ_j)), on the
  approximation that s_i is nearly sinusoidal with constant sign over a
  cycle. The rule is "loosely analogous" to Kuramoto-type entrainment; it
  is a gradient on payoff, not a physical coupling through the units'
  outputs.
- **The evolutionary version.** Adaptive dynamics under strong selection,
  weak mutation: each unit is a homogeneous population with a heritable
  θ, mutations drawn N(θ_i, σ) with σ = 0.5, fixed if the focal
  population's average fitness over a cycle rises.

## Key results

- **Without entrainment (Fig. 4).** Each module reaches internal
  agreement fast; modules agree with each other with probability about
  0.5. "In 50 independent simulations, the global optimum is not found."
  Units "decide many times" but "always re-make the same decision".
- **With entrainment (Fig. 5).** Phases synchronise within modules; the
  "waking-up" of modules is "quite sudden (and less than t=20,000 for most
  modules)", at different times for different modules. With the learned
  phases, 50 runs from random states "all find one of the two globally
  optimal solutions". Blocks of ten switch as one, "acting like a single
  macro-scale unit".
- **The phases move before the benefit (Fig. 5B).** "The theta values of
  a module change systematically in the direction of increased
  synchronisation even before a collective exhibits collective action."
- **Competency rises with entrainment (Fig. 6).** Phases sampled every
  1,300 steps and tested in side runs: without entrainment the system
  mostly lands on the worst local optima (half the countries each way);
  after about 20,000 steps every side run reaches a global optimum.
- **Specific, not global, synchrony (Fig. 7A).** With synchrony imposed
  across all units, the system "does not exhibit transitions or the
  increased energy minimisation behaviour". "Specifically-organised
  synchronisation is required to enable one country to respond to
  another."
- **Transfer (Fig. 7B).** After entrainment the modules solve a
  non-stationary sequence of games that reward a varying middle block of
  countries for disagreeing: "it has learned how to move in a way that
  finds solutions", for "the class of problems with this module
  structure".
- **By selection (Fig. 8).** 7 modules of 7 populations reach the same
  within-module synchrony by mutation and selection alone, about 10⁶
  timesteps against 10⁴ for Eq. 5.
- **Hierarchy (Fig. 9).** N = 343, 7 × 7 × 7, Eq. 6 couplings 1, 0.01,
  0.0001. Modules wake, then meta-modules after about 40,000 steps with ν
  ten times larger. The transition is not scale-invariant: "higher-level
  modules do not have the ability to respond to selection as a single
  unit"; a further transition "would require higher-order traits (e.g.
  meta-phase differences)" (v2).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Payoff-driven phase adjustment synchronises units within strongly coupled modules, using only local information | strong (in the model) | Fig. 5B, Eq. 5; one parameter setting, one game |
| C2 | Within-module synchrony makes each module switch as one unit and the system reach a global optimum | strong (in the model) | Figs. 5C–D, 6; 50 of 50 runs against 0 of 50 |
| C3 | Global synchrony does not produce this; the synchrony must match the module structure | moderate | Fig. 7A, one condition, caption-level report |
| C4 | The learned organisation transfers to other games over the same modules | moderate | Fig. 7B, one non-stationary sequence |
| C5 | The same result arises by individual-level selection on timing | moderate | Fig. 8, one 7 × 7 run reported |
| C6 | The mechanism iterates to a second level, but not scale-invariantly | weak | Fig. 9, one run |
| C7 | Cell-cycle and reproductive synchrony in development and major transitions may work this way | weak | analogy in Discussion, no model of either |

## Method

Simulate N units by Eqs. 3–4 from random states and phases, with or
without the phase rule (Eq. 5); sample the learned phases and test them in
fresh runs; impose global synchrony as a control; switch the game during a
run; replace Eq. 5 by mutation and selection on θ; repeat on a two-level
modular game. Energy at the end of each run is the score.

## Concepts

- **Decision cycle** — the periodic alternation of a unit between an
  undecided, sensitive phase near a saddle point and a decided, acting
  phase, set by γ_i(t) and the unit's phase θ_i.
- **Entrainment** (as used here) — the change of θ_i by Eq. 5 or by
  selection, toward partners whose states currently agree with the
  coupling.
- **Inner alignment** — synchrony of decision cycles inside a group.
- **Transition in agency** — a group gaining the same minimal competency
  its members have: choosing between two (collective) states so as to
  reduce (collective) stress.
- **Hard problem of transitions** (v2) — that a structure created by
  individual incentives either aligns with what individuals already do
  (and is redundant) or opposes it (and would not be created).

## Connections

It is the model behind Watson's agency essay ([LIT-990](../literature.d/LIT-990.md), read in [NOTE-747](NOTE-747.md),
which cites it as "under submission"), and continues the Watson, Buckley
and Mills work on self-modelling Hopfield networks and associative
learning in adaptive networks. The units are Waddington-style bistable
deciders; the energy function follows Hopfield; the timing rule is
offered as an analogue of Kuramoto entrainment (Izhikevich and Kuramoto).
It addresses Okasha's fitness-1/fitness-2 problem in the evolutionary
transitions in individuality.

## Bearing on the record

- **[LIT-989](../literature.d/LIT-989.md)'s seed claim is half right.** "Aligning the timing of
  components makes a higher-level unit that acts as one" is what the paper
  shows. "A case for the mutual-entrainment test of [CLAIM-172](../claims.d/CLAIM-172.md)" needs two
  qualifications. The paper's entrainment is a payoff-gradient rule on
  phase, not timing pulled by the partner's output as in HKB
  ([THEORY-069](../theory.d/THEORY-069.md)). And the result turns on *which* units are synchronised:
  synchrony imposed on all units makes no unit (Fig. 7A).
- **[CLAIM-172](../claims.d/CLAIM-172.md) (mutual entrainment as a sufficient mark).** Support, with a
  sharpening. Within-module entrainment is mutual and does make a unit
  relative to the target of resolving between-module constraints. But
  shared timing alone is not what made it: the control with global
  synchrony has common timing and no unit. Relative to this target, the
  mark that works is synchrony matched to the strong couplings. Whether
  that control counts as mutual entrainment is doubtful, since it is
  imposed, so it is not a counterexample to [CLAIM-172](../claims.d/CLAIM-172.md) as worded. [CLAIM-172](../claims.d/CLAIM-172.md)'s
  `defeated_if` (a model of each side taking the other as input predicts
  as well as the pair model) is met trivially here: the micro equations
  predict everything, and the authors say "the higher-level agent is not a
  variable in any of our equations of motion". Read literally, the defeat
  condition would be met by any fully specified simulation. It needs to
  be read as descriptive economy, or reworded.
- **[CLAIM-157](../claims.d/CLAIM-157.md) (the block criterion).** The game's interaction matrix is
  nearly decomposable throughout: within 1, across 0.01. The block is
  there before entrainment and after it. What changes at the transition
  is not the coupling but the timing, and with it whether the block acts
  as one relative to the other modules. So a block that would clear
  [CLAIM-157](../claims.d/CLAIM-157.md)'s threshold need not behave as a unit. That is consistent
  with [CLAIM-157](../claims.d/CLAIM-157.md), which disclaims agency, and it shows the two come apart
  in a concrete case: one system by coupling strength, and a responding
  unit only after synchrony.
- **[QUESTION-035](../questions.d/QUESTION-035.md).** Here the boundary is set by the modules, and the
  timing process finds it: "the structure of this synchronisation (i.e.
  who is synchronised with whom) implicitly defines the membership of the
  collective". The boundary is given in advance by c_ij (footnote 2), so
  the paper does not show a boundary drawn where none was built in. On
  duration, the learned phases persist once formed and carry over to new
  games; dissolution is not studied.
- **[THEORY-232](../theory.d/THEORY-232.md).** It names this paper as "Tissot et al., under
  submission, not held". It is now held as [LIT-989](../literature.d/LIT-989.md). [THEORY-232](../theory.d/THEORY-232.md) says the
  learned relationships "pick out groups that 'work together'". The
  learned relationship is phase, not coupling weight, and the groups
  match modules the couplings already define. [THEORY-232](../theory.d/THEORY-232.md)'s comparative
  measure is computed here in effect: total energy at equilibrium with the
  old timing against the new (Fig. 6).
- **New THEORY.** [THEORY-tmph3haa](../theory.d/THEORY-tmph3haa.md) holds the model result.
- No instruction for machine-learning practice; nothing for the
  anthology.

## Limitations

- One game with clean, non-overlapping, consistent modules. The authors
  say natural interactions will be "of various different strengths,
  exhibiting complex (sometimes unresolvable) frustrations".
- The phase rule is postulated (or derived from an approximation that
  holds sign constant over a cycle). Appendix A's final equation writes
  ν Σ_j c_ij dU_ij/d(θ_i − θ_j), and dU_ij already carries c_ij, so as
  written it gives c_ij² where Eq. 5 has c_ij. The hierarchical section
  calls the phase rate σ where elsewhere it is ν. Both versions carry
  these slips.
- Single runs or 50-run batches at one parameter setting; no sweep over
  the coupling ratio, ν, ω or noise, and no statistics beyond counts.
- The new level has "no internal computation or information integration",
  no boundary in space and no metabolism; the authors say so.
- The developmental and evolutionary interpretations are analogy.

## Open questions

- Does payoff-driven timing find groups when modules overlap or
  constraints are frustrated?
- Does entrainment through the units' outputs (Kuramoto or HKB coupling),
  rather than a payoff gradient on phase, give the same result?
- What dissolves a woken module: a change in the game, noise in θ, or
  drift? The paper shows formation and transfer, not ending.
