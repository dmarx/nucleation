---
number: 415
status: Read
formerly:
- NOTE-tmpa22le
paper: LIT-533
title: 'Life as a manifestation of the second law of thermodynamics'
version: 1
history:
- version: 1
  date: '2026-10-02'
  note: >-
    Read in full (the authors' formatted text, 32 pp., "© James J. Kay and
    Eric Schneider, 1992", carrying the journal reference; retrieved from a
    University of São Paulo course page; text extracted with PyMuPDF):
    Abstract, Introduction, Classical thermodynamics, The extended laws of
    thermodynamics, Dissipative structures as gradient dissipators, Living
    systems as gradient dissipators, The origin of life, Biological growth
    and development, A thermodynamic analysis of ecosystems, Ecosystems as
    energy degraders, Discussion, Figs. 1–5, Tables 1–3 and the references.
    I recomputed the percentages and ratios in Tables 1–3 and the
    temperature differences in the text. The data behind the figures
    (Silveston 1957, Brown 1973, Luvall & Holbo, Sato et al., the Crystal
    River flows) were taken as reported. The typeset journal version was
    not seen.
date: '2026-10-02'
summary: >-
  Proposes a "restated second law" (systems pushed from equilibrium
  resist the applied gradients by every available means) and reads Bénard
  cells, vortices, life and ecosystem succession as successive gradient
  destroyers, with the second law "necessary but not sufficient" for life.
  The law is asserted, not derived. The physics examples show organized
  structures raising dissipation, not that they must. The ecological
  evidence is one unreplicated marsh comparison and thermal-scanner and
  satellite correlations, one of whose tables is internally inconsistent.
---

<!-- inactive-ok-file: LIT-530 — Deferred: Schrödinger is unread; named because this paper presents itself as taking up his task, not leaned on -->
<!-- inactive-ok-file: THEORY-026 THEORY-030 — Proposed; named only to say they do not overlap this paper -->

# NOTE-415: Life as a manifestation of the second law of thermodynamics

## Contribution

The paper recasts the thermodynamics of life around gradients and exergy
rather than entropy. It proposes one principle meant to hold far from
equilibrium, and applies it in a single sweep from convection cells to
ecosystem succession and evolution. It supplies new calculations of entropy
production and exergy destruction from Silveston's Bénard data, and
proposes surface temperature from airborne thermal scanning as a
measurable index of ecosystem development or "integrity".

## Key insight

Do not ask whether order is consistent with the second law; ask what an
imposed gradient does to a system. The authors' answer is that it calls
up whatever structures destroy it fastest, and on that reading organisms
and ecosystems are elaborate, remembered versions of a vortex in a draining
bottle.

## Assumptions

- **The unified principle** (Hatsopoulos & Keenan; Kestin): an isolated
  system, after constraints are removed, reaches a unique equilibrium
  independent of the order of removal. Kestin's proof gives Lyapunov
  stability of equilibrium.
- **The "restated second law"** is offered as a corollary: "Implicit in
  this conclusion is that a system will resist being removed from the
  equilibrium state." That is a local stability property of equilibrium.
  The step to far-from-equilibrium behaviour ("utilize all avenues") is not
  derived. Le Chatelier's principle is cited as an instance, and it too is
  a near-equilibrium result.
- **Gradients and exergy, not entropy,** are taken as the variables, so as
  to avoid defining entropy away from equilibrium. Yet the Bénard analysis
  computes an entropy production rate.
- **Ecosystem development is read as the second law at work.** The list of
  seven expected successional trends is derived from "the more energy
  that flows … the greater the potential for degradation", not from a
  model.
- **Surface temperature measures exergy degradation:** with incoming K*
  fixed, a cooler surface emits less long-wave L* = εσT⁴, so more net
  radiation Rn is degraded.

## Key results

- **Bénard cells (Figs. 1–2, points 1–9).** From Silveston's data (silicone
  oil, 6.98 mm deep): heat transfer rises linearly with ΔT, entropy
  production and exergy destruction nonlinearly, and both jump at the onset
  of convection, given as Ra ≈ 1760. Nu = Q/Q_c = P/P_c = Ø/Ø_c for pure
  heat transfer. They reject maximum entropy production for "entropy
  production change being positive semi-definite as you increase the
  gradient".
- **Tornado in a bottle.** Draining takes about 6 minutes without a vortex
  and about 11 seconds with one.
- **Crystal River marshes (Table 1).** Stressed against control: biomass
  −34.7%, imports −18.1%, total system throughput −20.7%, food-web cycles
  142 → 69 (−51%), trophic levels 5 and 5. I recomputed the percentage
  changes; they match.
- **Oregon forest thermal scans (Table 2, Luvall & Holbo 1989).** Surface
  temperature falls from 50.7 °C (quarry) and 51.8 °C (clear-cut) to 24.7
  °C (400-year-old Douglas fir). Rn/K* rises from 62% to 90%.
- **Regional energy budgets (Table 3, Sato et al.).** The evapotranspiration
  share is 70% for the Amazon and 2% for the Sahara. A SiB model run
  replacing rainforest by grassland lowers it from 63% to 48%.
- **Origin of life.** Life is "another route for the dissipation of
  induced energy gradients"; the gene is a "memory" that lets the process
  continue without restarting by chance. Eigen's hypercycles are cited as
  the thermodynamic route.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Systems moved from equilibrium use all available means to counter the applied gradients, increasingly so as the gradient grows | assertion | offered as a corollary of Kestin's equilibrium-stability proof; the step beyond equilibrium is not derived |
| C2 | Bénard convection raises heat transfer, entropy production and exergy destruction above conduction | strong, for these data | recalculated from Silveston's experiment (Fig. 2) |
| C3 | The governing principle is not maximum entropy production | moderate | an inference from the Bénard data (point 9); no other system examined |
| C4 | Life arises and persists as a further means of dissipating the solar gradient | assertion | analogy from C2 and the vortex; no model |
| C5 | The second law is necessary but not sufficient for life | stated as a limit on C4 | the authors' own caveat |
| C6 | Ecosystems develop to degrade more incoming exergy (seven predicted trends) | weak | one stressed/control marsh pair, no replicate or statistics; trends said to "subsume" Lotka, H. T. Odum, Lieth |
| C7 | More mature ecosystems are cooler and degrade more net radiation | moderate as a correlation | thermal-scanner transects and one table (Table 2); confounded with evapotranspiration, which the authors say does most of the degrading |
| C8 | Ecosystem surface temperature can index ecosystem health or integrity | proposal | "much more research is needed" |

## Concepts

- **Gradient.** A difference (temperature, pressure, chemical potential)
  holding a system away from equilibrium. The paper's measure of distance
  from equilibrium.
- **Exergy (availability).** The available-work content of energy. Its
  destruction is "degradation".
- **Dissipation vs degradation.** Dissipation moves energy through a
  system; degradation destroys exergy, the ability to set up gradients.
  They coincide only for pure heat transfer. The authors say Prigogine
  "at times mistakenly uses these terms interchangeably".
- **Restated second law.** C1.

## Connections

- **Prigogine and the Brussels school; Paltridge; Swenson; Lotka, H. T.
  Odum, Jørgensen.** The paper's own lineage and foils on dissipative
  structures and on maximum-power and entropy-production principles. These
  are being filed in parallel in this batch, and nothing here relates to
  them by code.
- **Schrödinger, [LIT-530](../literature.d/LIT-530.md) (Deferred).** The stated starting point. The
  paper's reading of him (two processes, "order from order" and "order from
  disorder") is unchecked here.
- **Boltzmann 1886** is quoted on the "struggle for entropy" made available
  by the sun–earth temperature difference.
- **Eigen and Ishida** on hypercycles and quasi-species, quoted for the
  origin of life.
- **[LIT-036](../literature.d/LIT-036.md) (primitive metabolic cycles)** for the autocatalytic cycles
  this paper invokes without modelling.

## Bearing on the record

- **[LIT-192](../literature.d/LIT-192.md) / [NOTE-094](NOTE-094.md), the demarcation question.** The paper deliberately
  makes the line between living and non-living dissipative structures a
  matter of degree ("the most sophisticated (until now) end in the
  continuum"). Its one qualitative marker is heredity ("memory"), and its
  own C5 says thermodynamics cannot supply the line. It therefore
  supplies no principled thermodynamic demarcation, and does not claim
  to.
- **[LIT-211](../literature.d/LIT-211.md) / [NOTE-109](NOTE-109.md).** Paradigm of the "Dissipative Self-Organizing
  Systems" definitions.
- **THEORY documents.** None in the record concerns this. The record's
  thermodynamic THEORYs ([THEORY-026](../theory.d/THEORY-026.md), [THEORY-030](../theory.d/THEORY-030.md)) are about information and
  work and do not overlap.
- **No ML instruction.** Nothing here belongs in the anthology.
- **No new THEORY is indicated.** C1 and C4 are programmatic and too weakly
  supported to source one.

## Limitations

- C1 is a proposal. Its relation to the classical second law is analogy,
  and the paper gives no case in which it predicts something the classical
  law does not.
- The physics examples are chosen because organized structure increases
  dissipation there. No counter-case is examined, such as a structure
  that forms and reduces throughput.
- The ecological evidence is correlational. Table 1 is one pair of
  marshes; Tables 2–3 compare sites that differ in water, canopy and
  climate as well as maturity.
- The paper sets aside genetics on purpose ("We have intentionally not
  discussed the application of these principles to … genetic processes"),
  so the demarcation it would need is out of scope.

## Open questions

- Is there any system in which the "restated second law" makes a
  prediction that differs from the classical second law plus the
  dynamics, and is it borne out?
- Does ecosystem surface temperature track development once water
  availability and canopy structure are controlled?

## Corrections

- none to a seeded skim (there was no seed)
- **Table 2 is internally inconsistent for the 400-year forest.** The
  table defines Rn = K* − L*. For the other four sites the figures agree
  (e.g. 718 − 273 = 445 for the quarry). For the 400-year stand it lists K*
  = 1005, L* = 95 and Rn = 830, but 1005 − 95 = 910. The 90% the text
  quotes is 910/1005 (90.5%); 830/1005 is 82.6%. So the Rn entry, not the
  90%, is probably the misprint.
- **Temperatures in the text.** "The coldest site, 299°K, some 26° colder
  than the clear cut": Table 2 gives 24.7 °C (297.9 K) against 51.8 °C, a
  difference of 27.1 °C. The text's figures are rounded inconsistently with
  the table.
- **The solar figure.** "the 1580 watts/meter² of incoming solar energy"
  is higher than the usual top-of-atmosphere solar constant of about
  1,360–1,370 W/m². The paper gives no source for its number.
- **The onset of convection.** The paper gives the critical Rayleigh number
  as 1760 and cites Chandrasekhar (1961). Chandrasekhar's value for two
  rigid boundaries is about 1708. The paper may mean the experimental
  onset in Silveston's data, but it does not say so.
