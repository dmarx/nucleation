# LEAD-112: search log

Every query run for LEAD-112, with its service, date and what it turned up.
No email address was sent to any service: Europe PMC and arXiv were queried
with a generic user agent and no `email=` or `mailto=` parameter. Helper
script: a small Python client kept in the session scratchpad (not committed).

Kinds of evidence (QUESTION-048): report, no-report, deficit, architectural.
Named targets: superblindsight (deficit); inconspicuous rivalry recorded
intracranially (no-report); a marker both sides accept in advance (marker);
QUESTION-061's one content present to one consumer and absent from another
at the same time (architectural).

## Queries, 2026-11-22

| # | Service | Query | Kind | Hits | What it turned up |
|---|---------|-------|------|------|-------------------|
| E1 | Europe PMC | `superblindsight OR "super-blindsight" OR "super blindsight"` | deficit | 2 | Kauffmann 2004, a BBS commentary on Block (not a case); Guillot 2017 (philosophy). No empirical superblindsight case. |
| E2 | Europe PMC | `blindsight AND (training OR trained) AND (awareness OR "acknowledged awareness") AND (deny OR denial OR unaware)` | deficit | 114 | Recent reviews and training work (Kronemer 2025 eye metrics in cerebral blindness; Kiefer & Kammer 2024 on subjective vs objective measures). No case of trained access with denied experience. |
| E3 | Europe PMC | `"binocular rivalry" AND (inconspicuous OR unreportable OR "no-report") AND (intracranial OR electrocorticography OR neurons OR microelectrode OR prefrontal)` | no-report | 955 | Stockart et al. 2026 eLife review of human intracranial work; Vanhoyland 2025 single neurons in LOC. Ranked by date, not relevance; no inconspicuous-rivalry intracranial study in the first page. |
| E4 | Europe PMC | `"split-brain" AND (consciousness OR awareness) AND (divided OR undivided)` | architectural | 125 | Pinto et al. 2023 Front Hum Neurosci (automatic processes split, conscious ones unified). |
| O1-O4 | OpenAlex | four relevance searches (superblindsight; inconspicuous rivalry prefrontal; split brain; prefrontal rivalry decoding) | all | - | **HTTP 429 Too Many Requests on the first call**, 2026-11-22, `https://api.openalex.org/works?search=...`. Stopped; OpenAlex not used again in this run. |
| E5 | Europe PMC | `TITLE:"split brain" AND TITLE:(conscious OR consciousness)` | architectural / deficit | 12 | Pinto et al. 2017 Brain (divided perception, undivided consciousness); Pinto, de Haan & Lamme 2017 TICS; de Haan et al. 2020 review; Schechter & Bayne 2021; Volz et al. 2018 (cross-cueing). |
| E6 | Europe PMC | `AUTH:"Panagiotaropoulos TI" AND (rivalry OR "no-report" OR conscious)` | no-report (intracranial) | 24 | Kapoor et al. 2022 Nat Commun (decoding no-report rivalry transitions in macaque PFC, PMC8940963); Dwarakanath et al. 2023 Neuron (bistable PFC states gate access); Bellet et al. 2022 Neurosci Conscious (decoding without report nor post-perceptual processing); Panagiotaropoulos 2024 Neuron review. |
| E7 | Europe PMC | `TITLE:blindsight AND TITLE:(conscious OR awareness OR degraded)` | deficit | 34 | Phillips 2021 Psych Rev and its PsyArXiv preprint (blindsight is degraded conscious vision); Overgaard et al. 2008 PLoS One; Mazzi, Savazzi & Silvanto 2019; de Gelder et al. 2025; Koivisto 2021 (TMS blindsight is degraded vision). |
| E8 | Europe PMC | `(inconspicuous OR unnoticed OR "undetected switches" OR unreportable) AND (rivalry OR bistable) AND (switch OR switches)` | no-report | 81 | Brascamp, Blake & Knapen 2015 Nat Neurosci (PMC4603386); Canales-Johnson et al. 2023 PLoS Biol (bistable perception without report, EEG feedback); Duman et al. 2022 review. No intracranial recording of inconspicuous rivalry found. |
| E9 | Europe PMC | `TITLE:"no-report" AND (neurons OR intracranial OR electrocorticography OR "single-unit" OR iEEG)` | no-report | 42449 | Malformed: the parser matched "report" broadly (case reports). Discarded. |
| E10 | Europe PMC | `(marker OR signature) AND consciousness AND ("independent of report" OR "without report" OR "theory-neutral" OR "test for consciousness" OR "tests for consciousness")` | marker | 79 | Beni 2026 (against theory-neutral method); Hutchinson, Dehaene, Slagter & Pitts 2026 preprint (late code of access without report); no marker accepted in advance by both sides. |
| E11 | Europe PMC | `TITLE:"tests for consciousness"` | marker | 3 | Bayne et al. 2024 TICS, Tests for consciousness in humans and beyond. |
| E12 | Europe PMC | `TITLE:"relative blindsight" OR (AUTH:"Persaud N" AND blindsight)` | deficit / report | 8 | Lau & Passingham 2006 PNAS (relative blindsight, PMC1693736); Persaud et al. 2011 NeuroImage (awareness-related activity in GY beyond performance); Jannati & Di Lollo 2012 (criterion confound); Balsdon & Azzopardi 2015. |
| A1 | arXiv | `abs:"phenomenal consciousness" AND abs:"access consciousness" AND abs:dissociation` | all | 0 | Nothing. |
| A2 | arXiv | `abs:"no-report" AND abs:consciousness` | no-report | 8 | AI-consciousness and falsification papers (Kleiner & Hoel 2020); no empirical dissociation. |

## Held-check, 2026-11-22

Every candidate was searched in record/literature.d by DOI fragment and
title words. None of the ten registered works was held. Brascamp et al.
2015, Frässle et al. 2014 and Panagiotaropoulos's group are named, not held,
in LIT-637 and THEORY-094.
