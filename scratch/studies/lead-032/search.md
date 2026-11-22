# LEAD-032: search log

Run on 2026-11-22 by the lead worker (Claude, in this session), on branch
`claude/lead-032-dismantling-trials`.

## What was sought

LEAD-032, for QUESTION-045's "What would answer it":

- **(a) Dismantling.** "An experiment that cuts one maintaining link, such
  as safety behaviour, while holding the regime's content fixed, and
  produces lasting change that the same exposure without the cut does
  not." Operationally: the same exposure given to two arms, one with the
  safety behaviour removed (or never offered) and one with it kept,
  compared at post-treatment and, for "lasting", at follow-up.
- **(b) Individual data showing hysteresis.** Intensive time series in one
  person (or modelled person by person) in which the state depends on the
  path: the regime persists after the condition that brought it on has
  returned, or the switch back occurs at a different level of the driver
  than the switch in. Critical slowing down (rising autocorrelation and
  variance before a transition) is a sign of approaching a tipping point,
  not hysteresis itself; it was searched as the nearest available
  individual-level evidence and is labelled so below.

## Service and route

Europe PMC REST search (`webservices/rest/search`, `resultType=core`), no
email address or other contact detail sent (ADR-008). Script:
`search.py` (rerun with `python3 -I scratch/studies/lead-032/search.py
[LABEL ...]`). Results: `results/hits.jsonl` (892 records, deduplicated,
with the queries that found each), `results/counts.tsv`. Abstracts were
fetched into `results/abstracts.jsonl`, which is not committed.

A first run without a field restriction matched full texts (1,623 to
11,947 hits a query) and was discarded. Every query below is wrapped in
`TITLE_ABS:( … )`.

Identifier and open-copy checks used Crossref (no `mailto=`) and OpenAlex
(no `mailto=`, no key). OpenAlex answered "Rate limit exceeded" on
2026-11-22, asking for an email address to obtain a key; none was sent,
and OpenAlex was not used again (see "Obstacles").

## Queries and counts

`SB` = `("safety behavior" OR "safety behaviour" OR "safety behaviors" OR
"safety behaviours" OR "safety-seeking")`.

| Label | Query (inside `TITLE_ABS:( … )`) | Hits |
|---|---|---|
| D1_exposure_sb_trial | SB AND (exposure) AND (randomized OR randomised OR "controlled" OR "dismantling" OR "component") AND (eliminat* OR drop* OR fading OR removal OR "without safety" OR abandon* OR "use of safety" OR judicious) | 12 |
| D2_sb_reviews | SB AND (exposure) AND ("meta-analysis" OR "meta-analytic" OR "systematic review" OR review) | 24 |
| D3_dismantling | (dismantling OR "component analysis" OR "additive design" OR "component study") AND (exposure) AND (anxiety OR panic OR "social phobia" OR "social anxiety" OR "obsessive" OR phobia) | 83 |
| H1_csd_individual | ("critical slowing down" OR "early warning signal(s)" OR "critical transition(s)") AND (depression OR depressive OR anxiety OR psychopathology OR "mental disorder" OR psychiatric) AND (individual OR "single patient" OR "single-subject" OR "n-of-1" OR idiographic OR "within-person") | 38 |
| H2_hysteresis | (hysteresis) AND (depression OR depressive OR anxiety OR psychopathology OR "mental disorder" OR psychiatric OR panic OR "symptom network") | 174 |
| H3_bistability_ts | ("alternative stable states" OR bistability OR bistable OR "tipping point(s)" OR "sudden gains" OR "sudden transitions") AND (depression OR anxiety OR psychopathology) AND ("time series" OR "experience sampling" OR "ecological momentary" OR "daily diary") | 3 |
| D4_sb_disorders | SB AND (panic OR agoraphobia OR "social phobia" OR "social anxiety" OR claustrophobi* OR "spider" OR "contamination" OR "obsessive") AND (experiment* OR randomi* OR trial OR condition) | 102 |
| H4_hysteresis_psych | (hysteresis OR hysteretic) AND (affect OR mood OR emotion OR psychological OR "experience sampling" OR "symptom" OR "network theory") | 761 (first 400 kept) |
| H5_csd_personalized | ("critical slowing down" OR "early warning") AND (depression OR depressive OR "mood") AND (personalized OR personalised OR "single" OR patient OR "n = 1" OR "n=1") | 84 |

D4, H4 and H5 were added after the first six: D1 missed the classic
trials, whose abstracts do not use the word "exposure" with the D1 terms,
and H2's "depression" mostly matched ST-segment depression and
antifreeze-protein hysteresis. "Depression" in H2/H4 is noisy throughout;
screening was by hand from titles and abstracts.

## Screening

Most hits are off topic (occupational and sun-safety "safety behaviour",
cardiac and materials "hysteresis", clinical "early warning" systems).
The works below are those that meet, or come nearest to, (a) or (b).

### (a) Exposure held fixed, safety behaviour cut versus kept

| Work | Design | Meets (a)? | Copy | Action |
|---|---|---|---|---|
| Meulders, Van Daele, Volders & Vlaeyen 2016, Clin Psychol Rev, 10.1016/j.cpr.2016.02.002 | meta-analysis of exposure with vs without safety behaviour | the synthesis of (a) | accepted manuscript, KU Leuven Lirias | registered, read |
| Meckes, Cole, Gee & Lancaster 2025, Cogn Ther Res, 10.1007/s10608-025-10667-1 | RCT, exposure with vs without judicious safety behaviour | yes (most recent RCT) | accepted manuscript, PMC13245588 | registered, read |
| Wells et al. 1995, Behav Ther, 10.1016/S0005-7894(05)80088-7 | within-subject, one session of exposure with vs without in-situation safety behaviours, social phobia | yes, one session, no follow-up | not checked (OpenAlex refused) | registered |
| Salkovskis, Clark, Hackmann, Wells & Gelder 1999, BRAT, 10.1016/S0005-7967(98)00153-3 | exposure with safety-behaviour drop vs exposure with habituation rationale, panic with agoraphobia | yes, brief | closed (OpenAlex: no open location) | registered |
| Powers, Smits & Telch 2004, J Consult Clin Psychol, 10.1037/0022-006X.72.3.448 | placebo-controlled, exposure with SB available, SB used, or neither, claustrophobia | yes, with follow-up | closed; Radboud and CiteSeerX entries not open | registered |
| Blakey, Abramowitz, Buchholz et al. 2019, BRAT, 10.1016/j.brat.2018.11.010 | RCT, exposure with vs without judicious SB, contamination fear | yes, with follow-up | closed | registered |
| Sloan & Telch 2002, BRAT, 10.1016/S0005-7967(01)00007-9 | exposure with SB vs guided threat reappraisal vs control, claustrophobia | yes | closed | in this log only |
| Sy, Dixon, Lickel, Nelson & Deacon 2011, BRAT, 10.1016/j.brat.2011.02.005 | failed replication of deleterious SB effect, claustrophobia | yes | closed; Wollongong entry not checked | in this log only |
| Kemp et al. 2019, Cogn Behav Ther, PMC6693977 | SB availability vs utilization, inhibitory learning | yes, analogue | PMC | in this log only |
| Cobb et al. 2026, J Anxiety Disord, 10.1016/j.janxdis.2026.103244 (preprint osf.io/qy7bd) | RCT, fear-antagonistic actions vs safety behaviours, acrophobia | partly (adds an action, not only a cut) | PsyArXiv preprint | in this log only |
| Blakey & Abramowitz 2016, Clin Psychol Rev, 10.1016/j.cpr.2016.07.002 | narrative review, inhibitory-learning view | review | closed | in this log only (cited by LIT-1491's reading) |

The works "in this log only" are covered by the meta-analysis read, or
are later than it and of the same design; registering each would add
codes the record does not yet use (ADR-072).

### (b) Individual-level hysteresis or tipping-point signs

| Work | Design | Meets (b)? | Copy | Action |
|---|---|---|---|---|
| de Jong, Ryan, van der Maas et al. 2023, PsyArXiv, 10.31234/osf.io/zrcft | HysTAR model: a method for detecting hysteresis in single-person time series | the method (b) needs, with demonstration | PsyArXiv, CC BY | registered, read |
| Wichers, Groot, Psychosystems, ESM Group & EWS Group 2016, Psychother Psychosom, 10.1159/000441458 | one patient, 239 days of experience sampling while tapering an antidepressant; critical slowing down before a shift | nearest individual data; a tipping-point sign, not hysteresis | open (publisher, CC BY-NC-ND) | registered |
| Smit, Helmich, Bringmann, Oldehinkel, Wichers & Snippe 2025, Clin Psychol Sci, 10.1177/21677026241305136 | 41 individuals tapering antidepressants, critical slowing down before transitions | nearest individual data, replicated across persons; not hysteresis | open (CC BY) | registered |
| Wichers, Smit & Snippe 2020, J Person-Oriented Res, PMC7842626 | confirmatory single-subject replication | as above | PMC | in this log only |
| Helmich et al. 2021 TRANS-ID protocol; Curtiss et al. 2023; Bos et al. 2022 (bipolar); Schreuder et al. 2022 | early-warning-signal studies | not hysteresis | various | in this log only |
| Cramer et al. 2016 (network model of depression, simulated hysteresis) | simulation | not individual data | not in these hits | not pursued |

## Obstacles

- OpenAlex, `api.openalex.org/works?search=…`, 2026-11-22: "Rate limit
  exceeded … Insufficient budget", asking for an email address to obtain
  a key. No address sent; not retried. Open-copy checks before that point
  are in the table; the rest rely on Crossref and Europe PMC.
- Semantic Scholar and Google Scholar were not used.

## Reading choice

Three reads, the limit the brief set: the meta-analysis of (a), the most
recent RCT of (a) with an open copy, and the one work in the hits that
addresses (b), hysteresis, rather than its precursor signs.
