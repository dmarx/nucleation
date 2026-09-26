---
number: 31
status: Read
formerly:
- NOTE-tmp32bkm
paper: LIT-059
title: 'The Strongest El Niño Ever (Climate Brink)'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (The full post, 1,199 words per the Substack API: public,
    datePublished 2026-07-13T15:01Z, byline Zeke Hausfather. - I read the
    body, all seven figure captions and the three footnotes. - I did not
    open the figure images or the live dashboard. - For the checks I
    downloaded NOAA CPC's published indices on 2026-09-26: -
    detrend.nino34.ascii.txt: monthly ERSSTv5 Niño 3.4 with 30-year base
    periods updated every 5 years; - oni.ascii.txt; - RONI.ascii.txt:
    seasonal; - wksst9120.for: weekly OISST, 1991–2020 base. - I did not
    check HadISST (the 1877–78 value) or the model ensembles (NMME/C3S).).
    Upgraded from `Skimmed` to `Read`: the claims table, assumptions and
    results are new, and the skim is corrected where the full text
    disagreed.
date: '2026-09-25'
summary: >-
  Hausfather reports that the July 2026 runs of 14 seasonal models (667
  members, model-weighted) put the median peak Niño 3.4 anomaly of the
  2026-27 El Niño at 3.6 °C, against his computed record of 2.75 °C
  (2015-16). That gives about a 91% chance of a record, or about 77% on a
  relative index where 1982-83 holds the record at 2.69 °C. He cautions
  that no model has been verified at this intensity. - NOAA's own series
  agree on the rankings but give lower record values: 2.67 monthly for
  2015-16 and 2.6 in ONI. - Observations through mid-September 2026 are on
  a record-setting track: weekly Niño 3.4 +3.0 °C on 16 Sep, and monthly
  ERSSTv5 +2.17 in August. The event has not yet peaked, so the forecast
  cannot yet be verified.
---

<!-- inactive-ok-file: LIT-059 — Deferred: the paper is placed by this reading; the directive lapses when its status changes -->

# NOTE-031: The Strongest El Niño Ever (Climate Brink)

## Contribution

A mid-July 2026 synthesis of the full multi-model seasonal forecast for the developing 2026 El Niño. It sets the forecast against every observed event since 1877, gives per-model spreads, adds a relative-index view, traces how the forecast evolved from March to July, and reports observations to date.

## Key insight

Every model's median peak is at "super" El Niño strength, and the models' successive runs have been revised upward while observations outran them. The author treats the upward revisions as "the classic signature of a real intensifying event rather than model noise". He caveats this: "agreement is not the same thing as skill".

## Assumptions

- **Indices.**
  - Niño 3.4 anomaly relative to a centered 30-year climatology, at monthly resolution. ERSSTv5 is used from 1950 and HadISST before.
  - RONI: Niño 3.4 minus the 20°S–20°N tropical-mean anomaly, with L'Heureux et al. (2024) scaling.
- **Ensemble.** July 2026 initializations of 6 NMME models, 7 C3S centres, and SINTEX-F (June initialization). Members are weighted so that each model counts equally, and each member's peak is its July–December maximum.
- **Observations.** Daily OISSTv2.1 via NOAA CoastWatch ERDDAP, era-adjusted.
- **Global temperature.** It lags ENSO by about 3–5 months.

## Key results

- **The headline forecast.** The median peak is 3.6 °C, about 0.8 °C above 2.75 °C (2015-16). The middle 80% of members is at or above 2.8 °C, and about 91% of members exceed the record.
- **1877-78 as a near-tie.** 1877-78 is a statistical dead heat with 2015-16 (2.73 vs 2.75). The gap between the strongest and fifth-strongest events is "only about 0.5C".
- **Per-model medians.**
  - All are at super strength.
  - All but SINTEX-F (2.2 °C) exceed the record.
  - CMCC (5.3 °C) is an outlier, 1.3 °C above the next model. Discounting it barely moves the median.
- **RONI.** 1982-83 is the record at 2.69. The median of 11 of the 14 models forecasts a record; overall about 77%.
- **Evolution from March to July.** The median peak rose from ~2.8 to 3.6 °C, with decelerating revisions (+0.5, +0.14, +0.14). NCAR-CESM1 called ~4 °C in March.
- **Development speed and starting point.** The event is developing faster than 1997-98, and it launched from "La Niña-ish" conditions in January.
- **Observations at mid-July.** Daily Niño 3.4 was about +2 °C, against +1.6 (1997) and +1.3 (2015) at the same date.
- **Global temperature.**
  - Most of the warming will land in 2027, likely the warmest year on record by a sizable margin.
  - About 28% chance 2026 beats 2024, up from about 13% at the start of July (from his dashboard).
- **Caveat.** "the models have never been verified in this territory."

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The 2015-16 record peak is 2.75 °C (monthly, era-centred) | author's own data (ERSSTv5) | CPC official monthly 2.67, ONI 2.6; the rank agrees |
| C2 | 1877-78 is 2.73 °C, a dead heat | author's own data (HadISST) | not checked |
| C3 | The multi-model median peak is 3.6 °C; ~91% of members exceed the record | author's own analysis of model output | NMME/C3S/SINTEX-F; not reproduced |
| C4 | On RONI, 1982-83 is the record (2.69); ~77% chance of a new record | author's own data; the rank reproduces | CPC seasonal RONI: 1982-83 first (2.40) |
| C5 | Mid-July daily Niño 3.4 ≈ +2 °C; 1997 was +1.6 and 2015 +1.3 at the same date | author's own data (OISST, era-adjusted) | CPC weekly (1991–2020 base): 15 Jul 2026 +2.1, 22 Jul +2.2; mid-Jul 1997 +1.4–1.5; mid-Jul 2015 +1.2–1.4. Consistent |
| C6 | The event launched from La Niña-ish conditions in January | reproduces | CPC monthly ERSSTv5, Jan 2026 −0.52 |
| C7 | Upward revisions signal a real intensifying event | informal argument | forecast evolution figure |
| C8 | 2027 will be the warmest year on record by a sizable margin | informal argument (lag relation) | none quantified in the post |
| C9 | There is a ~28% chance 2026 beats 2024 | author's own model (dashboard) | not checked |

## Concepts

- Niño 3.4
- ONI and era-centred climatology
- RONI (relative Niño index)
- Multi-model ensemble and model-equal weighting
- ENSO seasonal phase-locking
- Forecast verification outside the observed range

## Connections

Status of the forecast at the reading date (2026-09-26), from CPC data:
- Monthly ERSSTv5 Niño 3.4 was +1.78 (Jul) and +2.17 (Aug), already above the 2023-24 monthly peak of 2.02.
- Weekly OISST Niño 3.4 reached +3.0 on 16 Sep 2026, equal to the highest weekly value of 2015-16 (+3.0, 18 Nov 2015) on the same fixed base.
- The seasonal ONI for JJA 2026 was 1.36.

The event is on a record-setting track, but its peak, typically in Nov–Jan, has not arrived.

## Bearing on the record

Climate science commentary. For ML practice the only point of contact is methodological: it is a public example of an ensemble forecast extrapolating outside its verification range, with the author's explicit "agreement is not skill" caveat. That is a general statistical point, not a claim about ML, and nothing in the anthology rests on it.

## Limitations

- This is a blog post built on the author's own processing of model and observational data. The code and data are not given in the post.
- The index choices (era-centred monthly values) make the record values differ from NOAA's official tables.
- The central number is an unverified forecast.
- The dashboard probability is live and not reproducible from the post.

## Open questions

- What were the verified peaks of the 2026-27 event in monthly ERSSTv5 Niño 3.4, in ONI and in RONI?
- Did the models over- or under-shoot at this intensity?

## Corrections to the seeded skim

- **"2.75 °C" is the author's own computation; NOAA's official products give lower values.** His record uses each event measured against "its own era's centered 30-year climatology", at monthly resolution, from ERSSTv5.
  - CPC's official monthly ERSSTv5 anomaly peaks at 2.67 °C (Jan 2016).
  - CPC's official ONI (3-month) record is 2.6 (NDJ 2015-16).
  - A reader comparing the post with NOAA tables will therefore see 2.6–2.67, not 2.75. The ranking of the top events is the same: 2015-16, then 1997-98 (2.42 monthly), then 1982-83 (2.23 monthly).
- **The RONI record-holder is confirmed; the value is his.** CPC's seasonal RONI also ranks 1982-83 first (2.40, DJF 1983), ahead of 1997-98 (2.28) and 2015-16 (2.25). The post's 2.69 is a monthly value with L'Heureux et al. (2024) variance scaling, and I did not reproduce it.
- **The post calls its Niño 3.4 measure "detrended".** Its own captions define it as anomalies against a centered 30-year climatology (the ONI convention), which is not a linear detrend.
- **Otherwise the dossier's figures match the text:** 667 members, 14 models, 3.6, ~91%, ~77%, 11 of 14 on RONI, SINTEX-F 2.2, CMCC 5.3, +0.5/+0.14/+0.14, ~28%.
- **An arithmetic implication the post does not state.** Starting at ~2.8 °C in March and ending at 3.6 °C in July, the three last revisions sum to 0.78, which leaves a March→April revision of only about +0.02 °C.
