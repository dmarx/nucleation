---
number: 417
status: Proposed
formerly:
- CASE-tmpskejj

title: 'The BERT anaphora study''s published figures, reanalysed by its signalling-corrected sheaf test and by Contextuality-by-Default 2.0: the per-instance probabilities are not published, the two verdicts are thresholds on signalling alone, and every instance on which they differ is CbD-contextual and not sheaf-contextual'

version: 1

standing: documented

kind: executed-study

tags:
- contextuality
- probabilistic-modeling
- linguistics

date: '2026-11-23'

line:
- pragmatic-transport
- formal-apparatus

illustrates:
- CLAIM-1176

reported_in:
- LIT-844

draws_on:
- THEORY-623
- THEORY-722

summary: >-
  Run for [LEAD-191](../leads.d/LEAD-191.md). [LIT-844](../literature.d/LIT-844.md)'s 51,966,480 PR-like models of the binary
  3-cycle were to be reanalysed by the sheaf test it applies (CF > 2|M|·SF)
  and by CbD 2.0. The per-instance BERT probabilities are not published, so
  the full reanalysis was not possible. Linear programs confirm that the
  sheaf verdict is SF < 1/6 and the CbD 2.0 verdict Δ < 2, and that the
  first set lies inside the second. The published counts then fix the
  divergence: 36,861,830 instances (70.9%), all CbD-contextual and not
  sheaf-contextual. The 25 printed instances split 9 / 8 / 7 / 1. Code,
  tests and results are in scratch/studies/lead-191/. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-037 — Proposed; the claim whose promotion condition this study was run for, cited as under test -->
<!-- inactive-ok-file: CLAIM-1176 CLAIM-1164 CLAIM-1166 CLAIM-1207 — new; filed by the lead run of 2026-11-23 -->

# CASE-417: The BERT anaphora study's published figures, reanalysed by its signalling-corrected sheaf test and by Contextuality-by-Default 2.0: the per-instance probabilities are not published, the two verdicts are thresholds on signalling alone, and every instance on which they differ is CbD-contextual and not sheaf-contextual

## What was done

[LEAD-191](../leads.d/LEAD-191.md) asks for [LIT-844](../literature.d/LIT-844.md)'s data to be reanalysed by two routes and the
verdicts compared. [CLAIM-037](../claims.d/CLAIM-037.md)'s note of 2026-10-29 names that comparison as
its promotion condition. The two routes:

- **The sheaf route that allows signalling.** This is the one [LIT-844](../literature.d/LIT-844.md)
  applies: "a criterion of contextuality for signalling models that reads
  CF > 2|M| SF" (§3a). [LIT-844](../literature.d/LIT-844.md) takes it from Vallée et al., which the
  record has not read.
- **Contextuality-by-Default 2.0** ([LIT-831](../literature.d/LIT-831.md)).

Everything is in `scratch/studies/lead-191/`: `routes.py`,
`test_routes.py`, `study.py`, `results.json` and a README. The run is CPU
only and takes about 25 seconds; 249 tests pass.

### The data

[LIT-844](../literature.d/LIT-844.md) publishes three kinds of figure:

- aggregate counts (§6b, §6c, §8);
- (SF, Δ) for 15 random instances (Table 1) and 10 similar-noun
  instances (Table 2);
- histograms (Figs 5–7).

It does not publish the three BERT probabilities per instance. Its §9
says: "The code for the experiments in this paper can be found in the
following GitHub repository: https://github.com/kinianlo/Contextuality-in-LLM."
On 2026-11-23 that repository held one commit (2024-05-28, tag v0.1.0)
with a README and a .gitignore. There was no code and no data. Its release
page returned HTTP 403 through the session proxy and was not retried. A
Zenodo search found no deposit. **So the reanalysis of the 51,966,480
instances was not possible.**

Both verdicts on this support turn out to be functions of (SF, Δ). So the
published figures support three narrower things: a recheck of the counts,
the exact divergence count, and both verdicts on the 25 printed instances.

### The tests, as linear programs

The scenario is [LIT-844](../literature.d/LIT-844.md)'s binary 3-cycle with the support of the PR prism.
A model is ε = (ε1, ε2, ε3), with ε_i = 2P_i(O1) − 1. The programs compute
the following, and each was checked against a closed form on 120 random
models:

- **CF and SF** by [LIT-844](../literature.d/LIT-844.md)'s definitions (3.1) and (3.3). CF ≡ 1, as in
  Proposition 3.3, and SF = max|ε_i|, as in Proposition 3.4. The corrected
  criterion therefore holds iff SF < 1/6.
- **CbD 2.0 noncontextuality**: whether the six variables R_q^c admit a
  coupling with the model's bunches and multimaximally coupled
  connections. Each connection here has two binary variables, so
  multimaximal is maximal, and CbD 2.0 agrees with CbD 1.0 ([THEORY-722](../theory.d/THEORY-722.md)).
  The program's verdict is Δ < 2 for contextuality, with
  Δ = |ε1 − ε2| + |ε2 − ε3| + |ε3 + ε1|. This is [LIT-844](../literature.d/LIT-844.md)'s CNT1 = 2 − Δ.
- **Two further sheaf-side readings**, the assistant's own:
  - *ns-part*: the no-signalling part of a minimal-SF decomposition is
    contextual. This holds iff SF < 1, since that part is always the PR
    box.
  - *nearest-NS*: the model is farther from the noncontextual set than
    from the no-signalling set. The distance is the sum, or the max, over
    contexts of the total-variation distance.

## Results

**The published counts.** They check:

- 866,108 pairs × 60 ordered adjective triples = 51,966,480;
- 77,118 / 51,966,480 = 0.148%, so §6c's "0.0148%" is a slip;
- 36,938,948 / 51,966,480 = 71.08%;
- 8,661 pairs × 60 = 519,660, the similar-noun subset.

Every sheaf-contextual instance is CbD-contextual, because Δ ≤ 6·SF < 1
when SF < 1/6. So the instances on which the verdicts differ are exactly
36,938,948 − 77,118 = **36,861,830** (70.9% of all instances). All of them
are CbD-contextual and not sheaf-contextual, and the sheaf test misses
99.8% of the CbD-contextual instances. Δ ≥ 2·SF, so every CbD-contextual
instance has SF < 1. The ns-part reading therefore calls at least
36,938,948 contextual.

**The 25 printed instances.** All 25 (SF, Δ) pairs can be realised
(2SF ≤ Δ ≤ 6SF).

| verdicts | Table 1 | Table 2 |
|---|---|---|
| contextual by both | fire/relief, person/photographer, track/rule, memory/saint, island/architect | railroad/railway, journalist/reporter, station/hospital, creature/snake |
| CbD only (diverging) | fox/passenger, dwarf/bass, dancer/scene, series/sheep | television/tv, grandmother/grandfather, supplier/producer, assassin/journalist |
| neither | scholar/opposition, apprentice/side, camera/telescope, tea/tree, prey/day | painting/sculpture, artist/facility |
| left open by rounding | videos/text (Δ = 2.000) | |

In the sum norm, the nearest-NS reading calls every printed instance
contextual, on every ε triple sampled consistent with its printed values.
In the max norm, its verdict varies with ε beyond (SF, Δ): on dwarf/bass,
for example, it is contextual on 28% of the consistent triples.

**The uniform family.** Take ε = (p, p, p), which is (1 − p)·PR box +
p·D, with D deterministic and fully signalling. The routes give:

| route | contextual for |
|---|---|
| CbD | every p < 1 |
| ns-part | every p < 1 |
| corrected sheaf test | p < 1/6 only |
| nearest-NS, max norm | p up to at least 0.5, not at p = 0.8 |

At p = 1 the model is D itself: CF = 1 and SF = 1, and CNT1 = 0 sits on
CbD's boundary.

**A cube sample.** 3,000 random PR-like models fall as follows. The
sum-norm nearest-NS and the ns-part readings say contextual on all of them.

| verdicts | models |
|---|---|
| CbD only | 2,298 |
| all routes | 228 |
| neither sheaf nor CbD | 474 |

The max-norm nearest-NS reading crosses CbD in both directions: 66
CbD-contextual models it calls noncontextual, and 439 CbD-noncontextual
models it calls contextual.

## What it can show

The study is documented as an analysis of published figures. It cannot
show:

- **anything about individual instances beyond the 25 printed**;
- **which verdict is right about language.** The support is fixed by the
  schema, and both verdicts are thresholds on how BERT's three choices
  signal ([NOTE-648](../notes.d/NOTE-648.md), [THEORY-623](../theory.d/THEORY-623.md)).

It shows the following. The 0.148%-against-71.1% gap is the gap between a
threshold on SF and a threshold on Δ. The sheaf figure is the verdict of a
sufficient test, and two exact sheaf-side readings give different figures.
[CLAIM-1176](../claims.d/CLAIM-1176.md) states the demonstrated part. [CLAIM-1164](../claims.d/CLAIM-1164.md),
[CLAIM-1166](../claims.d/CLAIM-1166.md) and [CLAIM-1207](../claims.d/CLAIM-1207.md) are three alternative readings of which
verdict is right.

The nearest-NS results are LP samples, not proofs. Vallée et al.'s own
statement of the criterion was not read, so whether it intends the
ns-part reading, the nearest-NS reading or another is not settled here.
