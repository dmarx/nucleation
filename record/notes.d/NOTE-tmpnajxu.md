---
status: Read
paper: 'LIT-1145'
title: 'Medrano, Friston and Zeidman — Linking fast and slow'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Read in full on 2026-10-29 in the version of record (Network
    Neuroscience 8(1):24–43, 2024, CC BY) from Europe PMC's full text of
    PMC10861163
    (https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10861163/fullTextXML),
    converted to text; MIT Press's PDF returned a Cloudflare check. Read:
    the abstract, author summary, all sections, the glossary of technical
    terms, the captions of Figures 1–5 and the references. Figures were
    read from captions only. The arXiv v1 of 21 August 2023
    (https://arxiv.org/pdf/2308.10618) was downloaded and not compared
    line by line. Checked: whether the text treats Haken's slaving
    principle and the Haken–Kelso–Bunz model, which the LIT could not
    confirm (it does, in prose, without equations).
date: '2026-10-29'
summary: >-
  A review for neuroimagers: multiscale time series are best tested with
  hierarchical generative models in which each level is a slower
  timescale, justified by centre-manifold and adiabatic reduction (the
  slaving principle) and compared by variational free energy; the worked
  example is adiabatic DCM of NMDA-receptor-antibody mouse LFP (Rosch et
  al. 2018). It states the slaving principle and the HKB model in a
  paragraph each, with no equations, and asserts rather than shows that
  the principle extends to discrete switching models such as HMMs.
---
<!-- inactive-ok-file: LIT-588 LIT-923 LIT-1671 — Unavailable; the HKB paper, Haken's Synergetics and the record's slaving-principle entry, named as open -->

# NOTE-tmpnajxu: Medrano, Friston and Zeidman — Linking fast and slow

## Contribution

It is a primer, not a new result. It gathers three ingredients for
testing hypotheses about slow change in fast neuronal data: state-space
models (with a taxonomy by deterministic or stochastic dynamics and
discrete or continuous states), mathematical grounds for separating
timescales (centre and inertial manifolds, the adiabatic approximation,
the slaving principle, their stochastic versions), and Bayesian
inversion of hierarchical models by variational Bayes and Bayesian model
reduction. It argues that the hierarchy of the model should mirror the
hierarchy of timescales.

## Key insight

If fast variables relax quickly onto a manifold set by slow ones, the
fast dynamics can be replaced by a fixed map from the slow state, and a
generative model can be built level by level: fit the fast model in
windows, treat its parameters as data for a slow model. Whether a second
timescale is worth modelling is then a model-comparison question,
answered by the free energy.

## Assumptions

- **Timescale separation exists**, i.e. a centre or inertial manifold, a
  local result for centre manifolds and case by case for inertial ones,
  as the review says.
- **Variational Bayes** with its approximate posterior; the free energy
  bounds the log evidence and is exact only for general linear models.
- **Bayesian model reduction** applies level by level, so each timescale
  is inverted once.

## Key results

Reported from the literature reviewed:

- **Slaving principle.** "Slow collective parameters, the order
  parameters, govern the dynamics of fast individual variables" (Haken).
- **HKB.** Fingers moving in antiphase switch to synchrony above a
  critical frequency; one slow collective variable, the relative phase,
  serves as order parameter and undergoes a bifurcation (Haken, Kelso
  and Bunz 1985). No equation is given.
- **Stochastic case.** Under separation the state density factorizes as
  p(r, t) p(s | r), slow marginal and time-independent fast conditional
  (Boxler 1989; Knobloch and Wiesenfeld 1983).
- **HMMs.** Slow switching among fast modes is said to "adhere to the
  slaving principle", licensed by fast transitions and long dwell times.
- **Example.** Rosch et al. (2018): windowed canonical-microcircuit DCMs
  of LFP in NMDAr-Ab and control mice under PTZ, with a second level
  relating synaptic time constants to drug concentration; PTZ affected
  the time constants, more so with the antibody.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Timescale separation can be justified by centre-manifold and adiabatic reduction | strong for the theorems cited | Carr 1981; Foias et al. 1988; Boxler 1989 |
| C2 | A model of multiscale data "naturally has a hierarchical structure" | moderate | follows from C1 where separation holds |
| C3 | The slaving principle covers discrete switching models | weak | asserted; "the mathematical arguments … are, for now, restricted to continuous systems" |
| C4 | Free energy decides how many timescales to model | moderate | standard Bayesian model comparison |
| C5 | Bayes factors maximize statistical power | weak | cited (Fowlie 2021), not argued |

## Concepts

- **Adiabatic approximation**: fast variables replaced by their steady
  state as a function of slow ones.
- **Slaving principle**: slow order parameters determine fast variables.
- **Structured flows on manifolds (SFM)**: building a multiscale model by
  prescribing a manifold, a flow on it and a strong normal flow.
- **Bayesian model reduction**: scoring reduced models from a full
  model's posterior without refitting.

## Connections

It rests on Haken's synergetics (LIT-923, Unavailable here), HKB (LIT-588,
Unavailable), Jirsa's SFM, Friston's DCM, and Bayesian model reduction
(LIT-614). The record's own slaving-principle entry is Haken and
Wunderlin's "Slaving principle revisited" (LIT-1671, Unavailable).

## Bearing on the record

- **CLAIM-331.** The LIT filed this as the likeliest candidate for A8's
  "2024" paper "on slow–fast decomposition, Haken's slaving principle and
  the Haken–Kelso–Bunz model", and noted that its treatment of the last
  two was unconfirmed. It is confirmed in substance: both appear, a
  paragraph each, as motivation, with no mathematics. The review is
  consistent with the claim's temporal facet (higher levels of its models
  are slower by construction) but bears on it weakly, for the reason the
  claim's note of 2026-10-20 already gives for slow feature analysis:
  here the levels are chosen by the modeller to be slower, and the review
  says so ("each level of the hierarchy accounts for a different temporal
  scale"), so they are not evidence that levels are slower. What it adds
  is the test the claim lacks for when a slower level earns its place:
  the free-energy comparison of models with and without it. Proposed
  dated note below.

No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **A review**, mostly of its authors' own methods (DCM, SPM).
- **One example**, summarized from another paper.
- **Errors and overstatements.** Figure 2's caption swaps the two axes of
  the taxonomy, calling the dynamics "discrete or continuous" and the
  state space "stochastic or deterministic", where the text has it the
  other way round. The conclusion says "the slaving principle entails
  switching dynamics", which the section it summarizes does not argue;
  the principle permits slow switching, it does not entail it. Attractors
  are glossed as "dense sets of points (i.e., a single point, a circle,
  or a sphere)".

## Open questions

- What, in discrete switching models, plays the role of the centre
  manifold, so that C3 has a proof?
- When levels are not imposed by the modeller, does free-energy
  comparison recover a slower level that a compositional criterion also
  finds?
