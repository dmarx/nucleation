---
number: 275
status: Active
formerly:
- THEORY-tmpo4fgq
title: "In two optically trapped beads with a symmetric hydrodynamic coupling, one trap moved by a recorded noise drive, time-delayed mutual information and transfer entropy follow the drive's path rather than the coupling's symmetry: the flow between the beads reads two-way under moderate drive, in experiment and numerics, and one-way under strong drive, in numerics of the fitted model only"
version: 4
history:
- version: 2
  date: '2026-10-17'
  note: >-
    A bullet added to What this does not say: "flow" is directed predictive
    improvement, per CLAIM-335, and the paper's transfer entropy uses a
    single target value (TERM-057). The account is unchanged.
- version: 3
  date: '2026-10-19'
  note: >-
    Narrowed and promoted, carrying out the promotion audit's decision for
    THEORY-275 (batch 039, ADR-047 v3). The title moves from "two
    symmetrically coupled units" to the one bead system LIT-947 studied,
    read in full in NOTE-788. The strong-drive regime is marked as
    numerics of the fitted model. The promote_when, a second system with
    strong drive measured, moves unchanged to QUESTION-186.
- version: 4
  date: '2026-10-20'
  note: >-
    Dated note added under ADR-047 v4 (the narrowing-loss sweep, batch
    067). The wider claim this entry's narrowing dropped, the
    generalization beyond this system, that directional information
    measures between reciprocally coupled units follow a one-sided drive
    and not the coupling. The source makes no general claim, so it is
    filed as the record's own interpretive claim, is now carried by
    CLAIM-tmp3gd3i, which names this entry in its grounds. Status and
    title are unchanged.
tags:
- information-theory
- causality
- natural-sciences
- thermodynamics
date: '2026-10-14'
source:
- LIT-947
answers:
- QUESTION-063
summary: >-
  Das, Manikandan and Banerjee (2025), [LIT-947](../literature.d/LIT-947.md), read in [NOTE-788](../notes.d/NOTE-788.md).
  Two colloids are coupled by the fluid through a symmetric tensor, and
  recorded noise moves one trap. Time-delayed mutual information and
  transfer entropy give drive → driven → other, with backflow at moderate
  drive. In numerics only, flow is one-way at strong drive. With no drive
  the coupled particles are independent at steady state. The paper does
  not test an unrecorded drive shared by both units, and it does not
  claim that the measures reveal coupling architecture. Whether the
  same holds in other reciprocally coupled systems is QUESTION-186.
supports:
- CLAIM-tmp3gd3i
---
<!-- inactive-ok-file: CLAIM-172 CLAIM-167 THEORY-129 — Proposed; the architecture claims this account qualifies and the shared-cue account set beside it, open -->
<!-- inactive-ok-file: CLAIM-tmp3gd3i — Proposed; the record's generalization this entry's narrowing dropped, filed apart under ADR-047 v4 with this entry in its grounds -->

# THEORY-275: In two optically trapped beads with a symmetric hydrodynamic coupling, one trap moved by a recorded noise drive, time-delayed mutual information and transfer entropy follow the drive's path rather than the coupling's symmetry: the flow between the beads reads two-way under moderate drive, in experiment and numerics, and one-way under strong drive, in numerics of the fitted model only

## Source

Das, Manikandan and Banerjee (2025), *Physical Review Applied* 24,
034039, [LIT-947](../literature.d/LIT-947.md), read in full in [NOTE-788](../notes.d/NOTE-788.md) (arXiv:2504.10124v2).

## What was actually shown

- **The system.**
  - Two 1.5 µm beads in separate optical traps, coupled
    hydrodynamically with strength ε = 3a/(2d) − (a/d)³ (0.49 or 0.29).
  - The coupling tensor is symmetric, H = [[1, ε], [ε, 1]]/γ, and the
    fluid also correlates the thermal noises.
  - The mean position of trap 1 is moved by an Ornstein–Uhlenbeck signal
    λ of strength θ (0.14–0.56 in the experiment). λ is recorded.
- **Direction recovered.**
  - At θ = 0.56 and ε = 0.49, in experiment and numerics:
    MI_{λ→x₁}(τ) > MI_{x₁→λ}(τ), MI_{x₁→x₂}(τ) > MI_{x₂→x₁}(τ) and
    MI_{λ→x₂}(τ) > MI_{x₂→λ}(τ).
  - TE gives the same order, with TE_{λ→x₁} ≫ TE_{x₁→λ}.
  - The measures pick out the driven particle and the order
    λ → x₁ → x₂. The paper calls this "a signature of hierarchical
    interaction".
- **But not one-way.** MI_{x₂→x₁}(τ) and TE_{x₂→x₁}(τ) also peak, so the
  flow between the particles is two-way at moderate drive. The paper
  draws the pathway as λ → x₁ ⇄ x₂.
- **One-way under strong drive.** At θ = 5.6, in numerics only, the flow
  becomes one-way: TE_{x₁→x₂} ≫ TE_{x₂→x₁}.
  - The coupling is the same symmetric tensor in every case, so what
    changed the reading was the strength of the one-sided drive.
- **No drive.**
  - The coupled particles are statistically independent at steady state,
    P(x₁, x₂) = P(x₁)P(x₂), so the steady-state MI is zero.
  - The delayed measures are symmetric:
    MI_{x₁→x₂}(τ) ≈ MI_{x₂→x₁}(τ) and TE_{x₁→x₂}(τ) ≈ TE_{x₂→x₁}(τ).
- **What could have failed.**
  - The measures could have pointed from x₂ to x₁, or failed to separate
    λ's effect on x₂ from x₁'s. They did not.
  - The two-way reading at moderate drive is an observation in the
    experiment.
  - The one-way reading under strong drive is a simulation of the fitted
    linear model.

## What this does not say

- **It does not say information measures can tell a shared drive from
  coupling.** The drive here acts on one unit and is recorded. The
  measures locate where it enters. An unrecorded cue acting on both units
  was not studied. That is [QUESTION-063](../questions.d/QUESTION-063.md)'s main case, and it remains open.
- **It does not say that directional flow reveals the coupling.** It says
  the opposite. A symmetric coupling read as two-way at moderate drive
  and one-way at strong drive.
- **It does not say information moves from one particle to the other.**
  "Flow" here is the direction of predictive improvement. Transfer entropy
  is unique plus synergistic information, not information attributable to
  the source alone ([CLAIM-335](../claims.d/CLAIM-335.md)), and the paper's transfer entropy uses a
  single target value ([TERM-057](../terms.d/TERM-057.md)).
- **It does not establish the strong-drive result experimentally.** θ ≫ 1
  is "beyond our experimental regime".
- **It does not say "two-way" against a symmetric null.** The
  significance threshold is computed on shuffled trajectories. It tests
  against independence, so "two-way" means both directions clear it.
- **It is one linear, Gaussian, two-body system** with an analytically
  known covariance. Nothing is shown for nonlinear units or for more than
  two.
- **Its account of the irreversibility trend is a parallel of trends**,
  TE asymmetry against partial entropy production. That is not filed
  here.

## Connections

- **[QUESTION-063](../questions.d/QUESTION-063.md): answers in part.**
  - The question asks what measurement tells which architecture produced
    a collective outcome. This account says what one family of
    measurements can and cannot see.
  - Transfer entropy and delayed MI, with the drive recorded, locate where
    a drive enters.
  - They do not read the symmetry of the coupling, since that reading
    changes with the drive's strength.
  - So separating a symmetric coupling with one-sided input from an
    asymmetric coupling needs an intervention on a member, as the
    question's "perturb one member and measure the others" proposes.
- **[CLAIM-172](../claims.d/CLAIM-172.md) and [CLAIM-167](../claims.d/CLAIM-167.md).**
  - These read peer or hierarchical architecture from whether coupling
    runs both ways or one.
  - Here a mutually coupled pair shows a one-way "hierarchical"
    information flow once one member is driven hard.
  - So an observational direction test would class this pair as
    hierarchical. [CLAIM-172](../claims.d/CLAIM-172.md)'s "each side's timing shifts with the
    other's" needs an intervention to be applied, not observational flow.
- **[THEORY-129](THEORY-129.md).** Coral colonies synchronized by a shared light cue are
  the case this account does not reach: a common, unrecorded drive on
  every member.

## Note of 2026-10-19: scope at promotion

Promoted on one study read in full ([ADR-047](../decisions.d/ADR-047.md) v3). Each ordering in the
title is stated in [LIT-947](../literature.d/LIT-947.md)'s text: the moderate-drive orderings beside
Figs. 3–4 and in App. F, strong drive in App. D, no drive in App. H. [NOTE-788](../notes.d/NOTE-788.md) read the figures from their
captions, so the title gives orderings and no values. The general claim,
that directional information measures between reciprocally coupled units
follow a one-sided drive, is [QUESTION-186](../questions.d/QUESTION-186.md). In the linear Gaussian
pair it could be settled exactly, because delayed-MI asymmetry there is
c_xy(τ)² − c_yx(τ)², computable from the stationary covariance.

## Note of 2026-10-20: the wider claim, filed apart

Under [ADR-047](../decisions.d/ADR-047.md) v4, what this entry's narrowing dropped is filed as its own
Proposed entry, so that evidence can later confirm or reject it as a
thesis. [CLAIM-tmp3gd3i](../claims.d/CLAIM-tmp3gd3i.md) carries the generalization beyond this system, that
directional information measures between reciprocally coupled units follow
a one-sided drive and not the coupling. The source makes no general claim,
so it is filed as the record's own interpretive claim. It names this entry
in its grounds, as its evidence. Nothing here changes.
