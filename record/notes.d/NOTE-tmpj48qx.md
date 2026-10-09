---
status: Read
paper: 'LIT-tmpne4ig'
title: 'Larger communities create more systematic languages'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read from the publisher's version in the Radboud Repository
    (hdl.handle.net/2066/205968): abstract, sections 1–5, figures 1–3 and
    their captions, the endnote, the data and ethics statements and the
    reference list. The electronic supplementary material (appendix A on
    stimuli and set-up, B on six additional short-version small groups, C
    with the numbered models 1–18, D with example languages) was not
    read, so model specifications beyond the Methods text, and the extra
    groups, are known only from the main text's account of them.
date: '2026-10-09'
summary: >-
  Varies community size alone in a laboratory language-creation game:
  groups of eight built more systematic, compositional languages than
  groups of four, faster and more uniformly across groups, while reaching
  the same communicative success and convergence. Input variability,
  greater in larger groups, predicted gains in structure; small groups
  differed more from each other on every measure.
---

<!-- inactive-ok-file: THEORY-tmp8h3pe — Proposed; filed from this reading -->
<!-- inactive-ok-file: THEORY-155 — Proposed; named for contrast, not tested here -->

# NOTE-tmpj48qx: Larger communities create more systematic languages

## Contribution

Cross-linguistic work had found that languages of larger communities tend
to be simpler and more regular, but could not separate size from network
density, contact and the share of adult second-language learners. This is
the first experiment, by the authors' account, to vary group size with
human participants while holding network structure and total interaction
fixed. It shows a causal effect of size on the systematicity of an
emerging language, and offers, with correlational support, a mechanism:
the greater variety of forms a member of a larger group must cope with.

## Key insight

Talking with more people means facing more variants and sharing less
history with each. Memorising every partner's idiosyncratic labels then
fails, and what spreads instead is the predictable: labels whose parts map
onto parts of meaning. Size buys structure by making memorisation harder.

## Assumptions

- **Fully connected groups**, members exchanging partners every round, so
  that the only difference between conditions is size (and with it shared
  history per pair).
- **Equal total interaction**: 23 interactions per round per pair, the
  same number of rounds in both conditions.
- **Structure measure**: the Pearson correlation, per participant and
  round, between normalised Levenshtein distances of labels and semantic
  distances (1 for a shape difference plus the angle difference / 180°),
  used raw rather than as a Mantel z-score because the meaning space grew
  over rounds.
- **Meaning space**: 23 scenes, four shapes, continuous angle of motion,
  and a unique fill per scene that allows a holistic strategy.
- Participants: native Dutch adults; Dutch and other languages forbidden,
  enforced by an experimenter present.

## Key results

Mixed-effects models (lme4, Kenward–Roger p-values); full models in the
supplement, not read.

- **Structure** increased over rounds (Model 10: β = 4.55, t = 9.46,
  p < 0.0001), nonlinearly; the increase was faster in larger groups
  (β = 1.92, t = 3.06, p = 0.004); final structure was higher in larger
  groups (Model 11: β = 0.11, t = 2.93, p = 0.006); larger groups varied
  less (Model 12: β = −0.015, p = 0.0002).
- **Communicative success** rose (β = 0.08, p < 0.0001), not significantly
  modulated by size; final accuracy did not differ (p = 0.083). Larger
  groups had lower variance.
- **Convergence** rose (β = 0.007, p = 0.029); no effect of size; larger
  groups less variable (β = −0.04, t = −23.68).
- **Stability** rose; larger groups' languages less stable overall
  (β = −0.08, p = 0.047), not by the end (p = 0.24).
- **Mechanism.** Larger groups had more input variability (Model 13:
  β = 1.45, t = 15.99). Input variability at round n predicted the
  increase in structure at n + 1 (Model 14: β = 0.015, p < 0.0001); less
  shared history did too (Model 15: β = −0.017, p = 0.0004); jointly only
  input variability was significant (Model 16: β = 0.011, p = 0.012;
  shared history β = −0.008, p = 0.17).
- **Function of structure.** Structure predicted convergence (Model 17:
  β = 0.018, p = 0.027) and accuracy (Model 18: β = 0.436, p < 0.0001),
  more strongly in later rounds.
- **Qualitative.** Many groups developed shape-part plus motion-part
  labels; groups differed in how they carved angle (two-axis or
  clock-like systems), and "no two languages were identical".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | With network structure and total interaction fixed, groups of eight develop more systematic languages than groups of four, and faster | moderate | Models 10–11; 12 groups per condition |
| C2 | Larger groups are more alike in outcome; small groups vary more on every measure | moderate | Models 3, 6, 9, 12 |
| C3 | Input variability drives the increase in structure | weak to moderate | lagged correlational Models 14–16; variability was not manipulated independently of size |
| C4 | Group size does not affect final communicative success or convergence | moderate (a null) | Models 1–2, 4–5; p = 0.083 on final accuracy |
| C5 | The results scale to real communities and support size as a driver of language evolution | not supported here | argued in the discussion, with one sign-language comparison cited |

## Concepts

- **community size**: the number of people in a fully connected group,
  four or eight.
- **input variability**: per scene and round, the summed normalised
  Levenshtein distance from the most typical label to all other labels
  produced for it; averaged over scenes.
- **shared history**: how many times a pair has interacted so far.
- **linguistic structure / systematicity**: string–meaning distance
  correlation; compositionality in the paper's sense, with no distinction
  between morphology and syntax (endnote).

## Connections

The paradigm descends from the group-communication and iterated-learning
experiments it cites (Kirby, Cornish and Smith, [LIT-771](../literature.d/LIT-771.md); Kirby, Tamariz,
Cornish and Smith 2015; Raviv, Meyer and Lev-Ari's own "Compositional
structure can emerge without generational transmission", 2019), but there is no generational
turnover here: structure arises by horizontal interaction. The
cross-linguistic correlation it tests is Lupyan and Dale (2010); the
confounds it removes are network density (Trudgill, Wray and Grace) and
second-language learners (Bentz and Winter). The sign-language
comparison cited is Meir et al. (2012) on two young sign languages, one
of a larger community and one of a small one.

## Bearing on the record

- Produces **[THEORY-tmp8h3pe](../theory.d/THEORY-tmp8h3pe.md)**: the size effect and the input-variability
  mechanism, with what the experiment does not show.
- **Against [THEORY-155](../theory.d/THEORY-155.md).** That theory says the endpoint of transmission
  between Bayesian samplers is the shared prior, independent of how much
  data passes. This study is not a chain, so it neither supports nor
  contradicts it; but it shows a social-structural variable changing the
  outcome among learners who presumably share their biases, which a reader
  of [THEORY-155](../theory.d/THEORY-155.md) should not assume away for interacting populations.
- No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- Two sizes only (four and eight), 12 groups each; "larger" is eight.
- Input variability was measured, not manipulated, so the mechanism rests
  on lagged associations within the same data.
- The meaning space was designed to reward compositional structure, and
  the incremental introduction of scenes was "implemented in order to
  introduce a pressure for developing structured and predictable
  languages".
- Participants all spoke Dutch and brought its phonotactics and
  segmentation habits; the written channel and restricted alphabet are
  far from spoken or signed language.
- One large group played one round fewer, and one participant's data were
  lost; both groups' data were kept.
- The claim that results "should scale" to real populations is argued,
  not shown.

## Open questions

- Does the effect hold, or grow, beyond eight, and with sparse rather
  than fully connected networks, where the authors expect network
  structure to modulate size?
- If input variability is manipulated directly in fixed-size groups (for
  example by injected variant labels), does structure follow?
- In a chain with generational turnover, does population size per
  generation change the endpoint, or only the speed, as [THEORY-155](../theory.d/THEORY-155.md) would
  lead one to ask?
