---
number: 410
status: Proposed
formerly:
- CASE-tmpktyr7
title: 'The Juggernaut line''s route to the reshoot, from production testimony and a circulation-network model: the actor says the director saw the redub online and called a one-line pickup, and the one observation the case gives favours circulation over a list that names the distributors by at most about five to one, and by under two if the case is known for the video''s fame'
version: 1
history:
- version: 1
  date: '2026-11-23'
  note: >-
    Filed by the lead run of 2026-11-23, as a delegated lead worker. The
    coding rules (written before reading), the coded testimony with each
    source's address and the date read, the model, its tests, the results
    and a sensitivity sweep are committed under scratch/studies/lead-188/.
standing: documented
kind: executed-study
tags:
- social-ontology
- agency
- network-science
- model-comparison
date: '2026-11-23'
line:
- distributed-agency
bears_on:
- QUESTION-119
reported_in:
- NOTE-2396
- NOTE-2412
- NOTE-2411
- NOTE-1272
summary: >-
  [LEAD-188](../leads.d/LEAD-188.md) run in two parts. Testimony: a search of interviews and trade
  press, coded by rules written first, found one production voice on the
  route, the actor Vinnie Jones, twice: the director Brett Ratner "found
  that on the internet" (2020), and phoned him after the Vancouver shoot
  to do the line at Elstree for a day, "He'd seen it online, I think"
  (2024). The co-writer, via Polygon, dates it to a reshoot. No production
  voice names a conveyor, a test screening or crew quoting it; Ratner has
  said nothing found on it. Model: on a heavy-tailed contact network,
  fan videos spread by percolation and one decision-maker adopts one
  line. The case's one observation, that the adopted line was a
  top-circulated video's, favours circulation over a list of identifiable
  contributions without distributors by 10 to 32 and over a list that
  names the distributors by 2.3 to 4.7 (exact Bayes factors over stated
  priors, 36 settings); if the case is known partly because the video
  was famous, by 1.3 to 1.6. The case neither meets [CLAIM-332](../claims.d/CLAIM-332.md)'s defeater
  nor discharges it. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-332 — Proposed; the thesis whose defeater this tests -->
<!-- inactive-ok-file: CLAIM-1006 CLAIM-1026 CLAIM-1022 CLAIM-1052 NOTE-2396 NOTE-2412 NOTE-2411 — new; filed by the lead run of 2026-11-23 -->

# CASE-410: The Juggernaut line's route to the reshoot, from production testimony and a circulation-network model: the actor says the director saw the redub online and called a one-line pickup, and the one observation the case gives favours circulation over a list that names the distributors by at most about five to one, and by under two if the case is known for the video's fame

## What was done

[LEAD-188](../leads.d/LEAD-188.md) asks for two things on [CASE-100](CASE-100.md): production testimony of how
the fan redub reached the reshoot, and a circulation-network model
compared with the list of identifiable contributions, the comparison
[CLAIM-332](../claims.d/CLAIM-332.md)'s defeater names. Everything is under
scratch/studies/lead-188/: `CODING.md` (the rules, written before any
testimony was read), `TESTIMONY.md` (the findings, each with its address
and the date read), `model.py`, `test_model.py` (8 tests, passing),
`results.json`, `sensitivity.py` and `sensitivity.jsonl`, and a README
saying how to rerun.

## The testimony

Each finding is coded for voice (V1 production first-hand, V2 production
reported, V3 creator, V4 journalist), route (R0 none, R1 a named
decision-maker saw it, R2 general circulation through crew or cast, R3
test screening or marketing, R4 independent origin), hedging and timing.
Only V1 with a route counts as production testimony on the route.

| finding | source | voice | route | timing |
|---|---|---|---|---|
| Jones: "Brett's line"; the director "found that on the internet and wanted to do that" | [NOTE-2396](../notes.d/NOTE-2396.md), 2020 | V1 | R1 | none |
| Jones: "Brett Ratner phoned me ... He'd seen it online, I think ... we had to go to Elstree for the day and we did that one line" | [NOTE-2412](../notes.d/NOTE-2412.md), 2024 | V1 | R1, hedged | after principal photography |
| Kinberg via Polygon: "that was a reshoot Ratner line"; not in the shooting script | [NOTE-2411](../notes.d/NOTE-2411.md), 2023 | V2 | none | after principal photography |
| ComicBookMovie's writer: "inspired by a parody dub video" | [NOTE-2411](../notes.d/NOTE-2411.md) | V4 | none | none |
| Ratner on Instagram (2020), on the role, not the line; two 2006 Ratner interviews | TESTIMONY.md, F7 to F9 | V1 | none | none |

Not reached on 2026-11-23: Polygon's Kinberg interview (the session's
fetch tool refused the host) and The Playlist's 2020 Jones story (HTTP
403). Neither was worked around. Nothing was found from an editor, a
producer or the studio, or the television segment Nazario recalls
([NOTE-1272](../notes.d/NOTE-1272.md)).

**What the testimony says.** One production voice gives a route, and it
is R1: a named decision-maker saw the redub online and asked for the
line, which was shot on a single pickup day after principal
photography. No finding codes R2, R3 or R4. The actor is first-hand as to
the request and the pickup; as to where the director saw it, he reports
what he was told or supposes ("I think").

**What it leaves open** is the question [CLAIM-332](../claims.d/CLAIM-332.md) turns on. "Online", in
spring 2006, is where the redub's circulation was. The testimony fixes
the last link (one director's own viewing) and is silent on how the
video came to his screen: by its general spread, by a named site or
segment that carried it, or by someone who sent it.

## The model

`model.py`. A contact network of 3,000 people (configuration model,
degree exponent 2.5). In each of twelve worlds, 300 fan videos are
posted by ordinary people and spread by bond percolation, each with its
own transmissibility drawn from Beta(1, 6); s is how many people a video
reached. The H highest-degree people are the identifiable distributors.
One decision-maker adopts one video's line. Three models of which:

- **M0, the list without distributors**: every video equally likely; the
  makers' act and the decision are all that is named.
- **MH, the list with identifiable distributors**: weight 1 + κ times the
  number of named distributors the video reached.
- **MC, circulation**: weight s^α. At α = 0 it is M0, and the model is
  regular there, which is the condition [CLAIM-154](../claims.d/CLAIM-154.md) now carries.

The case supplies one observation: the adopted line was a video among
the most circulated (top 1%, from the creators' "in the millions", not
a measured rank). An ascertainment weight s^γ allows for the case being
known to the record because the video was famous: the owner chose it as
a meme everyone knows. Parameters are priced by the exact marginal
likelihood, α uniform on [0, 2] and κ log-uniform on [10⁻², 10²]. With
one observation [CLAIM-154](../claims.d/CLAIM-154.md)'s large-sample rule does not apply, so the
exact Bayes factor it approximates is used.

## The results

Base setting, top 1%:

| ascertainment | MC over M0 | MH over M0 | MC over MH |
|---|---|---|---|
| none (γ = 0) | 10.8 | 3.8 | 2.8 |
| partial (γ = 0.5) | 2.0 | 1.1 | 1.8 |
| full (γ = 1) | 1.6 | 1.0 | 1.6 |

Across 36 settings (network of 1,500 or 3,000; H of 3, 10 or 30;
transmissibility Beta(1, 6) or Beta(1, 12); three seeds): with no
ascertainment, MC over M0 from 10 to 32 and MC over MH from 2.3 to 4.7;
with full ascertainment, MC over M0 from 1.47 to 1.64 and MC over MH
from 1.33 to 1.60.

In words: the single fact that the adopted line came from a viral video
counts against a bare list, but only if the case was not picked for its
fame; against a list that also names the sites that carried it, it
counts for little either way.

## What it can show, and what it cannot

It shows what [CLAIM-332](../claims.d/CLAIM-332.md)'s defeater can be tested on in this case and
how much the case carries: the defeater compares a network model with a
list of creators, distributors and decision-makers, and with one adopted
video the comparison is at most weak. The testimony fills the gap
[CLAIM-332](../claims.d/CLAIM-332.md)'s note of 2026-10-30 names, in part: a production voice now
gives the route's last link.

It cannot show that circulation, rather than one site or one person,
brought the video to the director; or that the spreaders were X-Men fans
([CLAIM-152](../claims.d/CLAIM-152.md)'s "passing coalition" stands). The model's distributor list
counts hubs reached and not their audiences; a list that also recorded
each named distributor's audience would track circulation more closely
and could close the remaining gap. The rank of the redub among 2006 fan
videos is not measured. What the testimony implies for [CLAIM-332](../claims.d/CLAIM-332.md) admits
two readings, filed as alternatives: [CLAIM-1022](../claims.d/CLAIM-1022.md) (the route runs
through circulation; the lean) and [CLAIM-1052](../claims.d/CLAIM-1052.md) (the route is a list
entry). The findings are [CLAIM-1006](../claims.d/CLAIM-1006.md) (the testimony) and
[CLAIM-1026](../claims.d/CLAIM-1026.md) (the model).

## Note of 2026-11-25: the model rerun, and what holds it back

Rerun on 2026-11-25 by the assistant, a session other than the filer's, in the recomputation pass of LEAD-tmpc0rqa, at the owner's go-ahead of 2026-11-25 ("go ahead with the reruns"). From a copy of `scratch/studies/lead-188/`: the 8 tests pass, and `model.py` and `sensitivity.py`, run with python3 -I, regenerate `results.json` and `sensitivity.jsonl` byte for byte. Every figure of the model was compared and matches: at the top 1 %, 10.8, 3.8 and 2.8 with no ascertainment, 2.0, 1.1 and 1.8 partial, 1.6, 1.0 and 1.6 full; across the 36 settings MC over M0 10.3 to 31.6 and MC over MH 2.26 to 4.72 with none, 1.465 to 1.635 and 1.333 to 1.602 with full ascertainment (the body's 10 to 32, 2.3 to 4.7, 1.47 to 1.64 and 1.33 to 1.60). The testimony half was not rechecked: its sources are outside pages, two of which the filer could not reach, and fetching them is an outside service that waits for the owner. What holds it back: that half, which a rerun of the model does not touch; the case's title states the testimony as well as the model. The note is the assistant's (Claude, in this session). No status change.
