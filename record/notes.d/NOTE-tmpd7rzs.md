---
status: Read
paper: LIT-tmpbcd3f
title: 'Nishida and colleagues — Measuring Task-Agnostic Training Data Influence Across Language Model Pretraining'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    Read on 2026-11-19 by a delegated reader from arXiv 2608.13515v1 (PDF,
    COLM 2026): §§1–6 and appendices A and B.1–B.5 in full; references
    skimmed; values in the stacked-area figures not read. Running notes on
    the branch claude/readers/scheduling-followups (the procedure proposed
    in pull request 537). Quotations rechecked by the filer by script
    against the downloaded text.
date: '2026-11-19'
summary: >-
  Endpoint-alignment influence across Pythia and PolyPythia training:
  literature-classified data relatively prominent early, STEM later, hard
  text mid-training. Attribution only; no intervention, no Reddit or forum
  breakdown.
---
<!-- inactive-ok-file: CLAIM-756 THEORY-tmp0lbb1 THEORY-tmpd6smn — Proposed or newly filed; entries this reading bears on -->

# NOTE-tmpd7rzs: Nishida and colleagues — Measuring Task-Agnostic Training Data Influence Across Language Model Pretraining

## Contribution

A target-free influence measure, an example's update scored by "how much
its gradient update reduces the squared distance to the final parameters"
(abstract), applied across public checkpoints, with checks against exact
computation, reference endpoint, size, seed and a TracIn-style score.

## Key results

1. **Domains over training.** "literature-related data are relatively more
   prominent early in training, whereas STEM-related data become
   increasingly prominent in later stages" (§4.4). Domains are classifier
   topics: "we use the NeMo Curator Domain Classifier" (§4.4), not Pile
   sources.
2. **Difficulty.** "the share of the highest-PPL bin increases from
   approximately 20% to 25% in the middle stage" (§4.3).
3. **The conversational example.** One illustrative excerpt: "whereas the
   high-contribution example is conversational and closer to natural
   discourse" (App. B.1).
4. **Fragility.** "the contribution score is endpoint-dependent" (§5.2);
   across sizes "we do not observe a single directional pattern that is
   shared across all six models" for the top contributors (§5.3); "the
   domain-specific TracIn analysis does not consistently recover the
   Literature-to-STEM crossover" (§5.4).
5. **No intervention.** The analyses "characterize how contribution varies
   across training rather than directly establishing the causal" effect of
   changing the data mixture (App. A). On easy-to-hard curricula, "Our
   results do not fully support this simple progression" (§5.5).

## Assumptions

The run's own endpoint is the target; parameter distance measures
progress; an SGD decomposition is applied to adaptive optimizers.

## Concepts

Trajectory-level influence; contributors and opponents; endpoint
dependence; the literature-to-STEM crossover.

## Bearing on the record

- **[LEAD-tmpjdtrl](../leads.d/LEAD-tmpjdtrl.md)**, the owner's recollection: not found here. No Reddit,
  forum or Pile-source breakdown; "conversational" rests on one excerpt.
- **[CLAIM-756](../claims.d/CLAIM-756.md)**, background: no later acquisition's cost is measured, and
  endpoint alignment cannot credit an update that only eases later ones.
- **[QUESTION-039](../questions.d/QUESTION-039.md)**, weak bearing: when each data type aligns with the
  trajectory, and transitions later in smaller models; alignment, not the
  acquisition of a structure.
- **[THEORY-tmp0lbb1](../theory.d/THEORY-tmp0lbb1.md)**, interpretation only: hard text matters most
  mid-training, not last; an attribution pattern, not a curriculum test.
- **[THEORY-tmpd6smn](../theory.d/THEORY-tmpd6smn.md)** (Liu and colleagues), parallel with some tension:
  late STEM alignment matches late-specialization recipes; Liu finds early
  code best by intervention.
- **[TERM-131](../terms.d/TERM-131.md)**, a caution: the measure has no counterfactual in the term's
  sense, so it measures alignment, not learning from the experience.
- **[THEORY-279](../theory.d/THEORY-279.md)** and **[CASE-294](../cases.d/CASE-294.md)**, parallel and method neighbour.

## Limitations

Endpoint-dependent; validated at 70M only; one run per configuration; one
model family and corpus; domain effects confounded with difficulty, as the
authors say.
