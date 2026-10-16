---
status: Proposed
promote_when: >-
  Measurement, in trained networks that pass the stability test for
  tracking a property, of a feature the hypothesis names: for example,
  whether competence changes where inputs cross the boundaries between a
  ReLU network's linear regions under perturbations that preserve the
  target's structure, compared across training regimes that do and do not
  press the network to unify. The hypothesis is promoted if such fracturing
  appears where it predicts and shrinks under the pressures it names. It is
  refuted if networks that pass the stability test show no such fracturing.
  More toy cases that meet the definition of understanding, or catalogues of
  known failures under distribution shift, cannot settle it.
title: "The understanding deep networks reach is characteristically fractured: it can be real, by the test of stable tracking under structure-preserving perturbation, but it is symbolically misaligned, non-reductive, locally fractured, proxy-dependent and representationally fragmented, because the loss rewards any predictive patchwork and does not press it to unify"
version: 1
tags:
- philosophy-of-science
- cognition
- epistemology
date: '2026-10-16'
source:
- LIT-131
summary: >-
  Freeborn (2026), [LIT-131](../literature.d/LIT-131.md), read in [NOTE-123](../notes.d/NOTE-123.md). The Fractured Understanding
  Hypothesis is argued from four small demonstrations and cited literature,
  with no test of how common the five features are. The abstract names
  three features and §7.5 five. The paper also applies its own criteria
  inconsistently: its Othello verdict uses post hoc probes that it excludes
  from the agent. The definition of understanding it rests on is an
  explication, not a finding.
---
<!-- inactive-ok-file: LIT-148 — Unavailable; named as a neighbour by the close reading, not as a result -->

# THEORY-tmp4r7t7: The understanding deep networks reach is characteristically fractured: it can be real, by the test of stable tracking under structure-preserving perturbation, but it is symbolically misaligned, non-reductive, locally fractured, proxy-dependent and representationally fragmented, because the loss rewards any predictive patchwork and does not press it to unify

## Source

Freeborn (2026), [LIT-131](../literature.d/LIT-131.md) (arXiv 2604.04171v1), read in full in [NOTE-123](../notes.d/NOTE-123.md). The
companion notebooks were not run.

## What was actually shown

**The criterion (§4.2, p. 15).** A system S systematically understands a
property p of a target T insofar as (1) S contains a subsystem M that is an
adequate model of some aspect of T; (2) M tracks p without memorizing it; (3)
bridge principles connect M's terms to T's; and (4) S can use M to derive
properties of p. Bridge principles count as part of S only if fixed at
deployment, executed automatically, part of closed-loop competence and
functionally integrated (p. 19). Non-memorization needs stability of the
prediction under a family Π of structure-preserving perturbations (Eq. 7).

**The demonstrations (§6).** A 4,481-parameter ReLU network trained on local
values of a torus function yields a closed surface with Euler characteristic
0, hence genus 1. A network with Kepler's hypothesis space built in fits
Mars's eccentricity at about 0.096 (modern about 0.093). A small transformer
groks addition mod 113, and the Fourier spectrum of its logits concentrates
on few frequencies. Othello-GPT is reported from Li et al. 2023.

**The hypothesis (§§7.4–7.5, pp. 45–46).** Understanding in deep networks is
symbolically misaligned (loss-driven coordinates), non-reductive (patchwork
is a stable resting point), locally fractured (piecewise structure),
proxy-dependent (any predictive dependence is rewarded) and representationally
fragmented (no pressure to factorize). Patchwork solutions are common because
they exist, local gradient descent finds them, and they are stable once the
loss is low. The paper offers this as one cause of the "jagged frontier".

**What could have come out otherwise.** The demonstrations could have failed
the criterion. They mostly did not, but they bear on whether networks can
understand, not on whether their understanding is fractured. Nothing in the
paper tests the hypothesis.

## What this does not say

- **That networks often understand.** "Often" in the abstract is not measured.
  Every demonstration is a toy, a single run, with no seeds or ablations.
- **That Othello-GPT understands the board by the paper's own test.** The
  bridge principles cited (activation to decoded board) are post hoc probes,
  which fn. 50 and p. 19 exclude from the agent. By its own criteria the case
  shows only that board information is present and used.
- **That the Kepler result is about deep learning.** The conic form,
  heliocentrism and the area law were built in, and the author concedes it is
  "debatable" whether this is deep learning at all (p. 34).
- **That weight decay is needed for grokking.** Footnote 47 says that without
  it the model "remains in the memorization regime indefinitely". The
  anthology's reading of the grokking literature ([ANTH-LIT-538](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-538.md)) records weight
  decay as the strongest intervention, changing how much data is needed, not
  whether grokking happens.
- **That understanding verdicts are observer-free.** The perturbation family Π
  is "necessarily interest-relative" (fn. 19).
- **Anything about large language models.** They are excluded by design.

## Connections

- The reading names the bridge-principle conditions (p. 19) and the
  stability test (Eq. 7) as the paper's most usable export, more than this
  hypothesis ([NOTE-123](../notes.d/NOTE-123.md)).
- Angius et al. ([LIT-153](../literature.d/LIT-153.md)) pair naturally with it on explaining network
  competence, as does López-Rubio ([LIT-148](../literature.d/LIT-148.md)) on computational functionalism.
