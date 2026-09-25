---
number: 71
status: Skimmed
formerly:
- NOTE-tmpr57rx
paper: LIT-094
title: 'Shabrina, Arcaute & Batty 2021, Airbnb and London housing'
version: 1
date: '2026-09-25'
summary: >-
  Using 2018 Airbnb data, the authors estimate that more than 2% of London properties, and up to 7% in some areas, are likely "misused" as short-term lets. Such misuse clusters where dwelling-type diversity is low (flats) and private renting is high. At borough level, a 100% increase in misuse density is associated with up to an 8% rise in rent per bedroom per week, about £90 a year.
---

<!-- inactive-ok-file: LIT-094 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-25 -->

# NOTE-071: Shabrina, Arcaute & Batty 2021, Airbnb and London housing

## Contribution

The article builds proxies for Airbnb's impact on Greater London housing by relating likely Airbnb misuse to local housing attributes. Misuse is defined as whole-property listings that break local regulation and are offered by hosts with multiple listings. The authors examine dwelling type, tenure (owned or rented) and the spatial pattern of rent changes. They find more than 2% of London properties, and up to 7% locally, likely misused. Misuse correlates negatively with dwelling-type diversity and positively with flats in areas with high private renting. A doubling of misuse density is associated with up to 8% higher rent per bedroom per week, and they discuss the policy implications.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- Data: Airbnb listings (more than 69,000 in 2018, about 72% with at least one review, used as an activity proxy; Fig. 1 shows cumulative snapshots since 2008), Zoopla rental listings (via the Urban Big Data Centre), and MHCLG net additional dwellings. Analysis is at LSOA and borough level.
- Entropy of dwelling types is used as a diversity measure, following Batty et al. (2014).
- Regression (Eq. 4, Table 1): the change in rent 2015–2017 at borough level is regressed on Misuse2015, additional housing 2015–16, distance to centre, and the owned-to-rented ratio. VIF and Shapiro-Wilk checks lead to log transforms.
- Discussion: at LSOA level up to 23% of properties are listed. About 0.15% of total stock (about 5,300 properties) are multi-listing misuse available more than 180 days. The authors compare with Barcelona (+7% rents), Boston and US estimates, and call for enforcement of legitimate use.

## Open questions

- A spatial case study of platform effects on housing, using entropy-based urban-complexity measures from the Batty school. Its relevance to the anthology is mostly as social-science background.
- The rent result is associational, with borough-level aggregation (London has 33 borough-level units; I did not check the regression's actual n). Check the model's sample size and specification before using the 8% figure.
- The "misuse" operationalization (days available, multi-listing) is the key assumption, so check its thresholds.
