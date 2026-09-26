---
number: 39
status: Read
formerly:
- NOTE-tmp84684
paper: LIT-089
title: 'Orosz 2025, software job openings at a five-year low'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (The full blog post (blog.pragmaticengineer.com; published
    20 Feb 2025, "Last updated 05 May 2025"), including its chart images. -
    I viewed the US software-development chart and the four-sector
    comparison chart. The other charts were read from their captions. - I
    did not read the paid "The Pulse" #124 issue it excerpts. - To check the
    data I downloaded Indeed Hiring Lab's own published series
    (github.com/hiring-lab/job_postings_tracker; the US sector and aggregate
    files, plus CA/GB/FR/DE/AU sectors; current vintage, data to
    2026-09-18). This is the source FRED republishes. FRED itself refused
    connections from this sandbox. - Values are compared at 2025-02-13,
    about when the Pulse issue went out.). Upgraded from `Skimmed` to
    `Read`: the claims table, assumptions and results are new, and the skim
    is corrected where the full text disagreed.
date: '2026-09-25'
summary: >-
  Orosz reports that US software-development postings on Indeed stood at
  65% of the pre-pandemic baseline, "3.5x" below the 2022 peak and 8% down
  year on year, while all postings were +10%. He attributes most of the
  fall to the end of zero interest rates, gives GenAI a secondary "wait
  and see" role, and doubts Indeed's coverage. - Against Indeed's current
  data the headline US figures reproduce: 65.2, peak ratio 3.59×, −8.3%
  y/y, all postings 109.5. - Several side figures and one comparative
  claim do not reproduce (see corrections).
---

# NOTE-039: Orosz 2025, software job openings at a five-year low

## Contribution

A widely read practitioner framing of Indeed's postings data for software development in early 2025. It sets out the size of the 2020–25 boom and bust and weighs explanations: interest rates, Section 174, pandemic over-hiring, GenAI and smaller teams.

## Key insight

Software-development postings had the most extreme swing of any Indeed sector, up more than 2.3× and then down to about 0.65× baseline. The post reads this mainly as a rates cycle, with AI as a possible damper on hiring that the data cannot isolate.

## Assumptions

Premises and authorities:
- Indeed postings track the market "directionally". The author himself doubts coverage of Big Tech and startups: Microsoft showed 663 jobs on Indeed against 1,000+ "software" jobs on its own site, and Workatastartup jobs were missing.
- FRED/Indeed series as shown in the charts.
- The author's earlier analyses of ZIRP and Section 174, and his own 2024 survey (about 75% of engineers use AI tools).
- Salesforce's statement of a 30% AI productivity gain and a flat engineering headcount, via his January issue.

## Key results

What the post argues and reports:
- **US figures:** 65% of baseline; "3.5x fewer vacancies than the mid-2022 peak"; −8% y/y; "as low as in mid-2020".
- **Other countries:** similar falls in the UK, France and Germany; Canada is like the US; Australia is the only country above 2020.
- **Section 174 is not the main driver.** The author's reasons: the timing (see corrections) and the non-US falls.
- **Sector changes since 2020:**
  - All postings +10%.
  - Banking −7%, sales −8%, marketing −19%, software −34%, hospitality −18%.
  - Construction +25%, accounting +24%, electrical engineering +20%.
- **Explanations, as the author ranks them:**
  - Interest rates "explain most of the drop".
  - Over-hiring in 2021–22.
  - GenAI "wait and see". He writes "I don't really buy this logic" about anticipatory hiring cuts, yet later says "I'm sure that LLMs contribute somewhat".
  - Small-team efficiency (Linear, 25 engineers; Bluesky, 13).
- **Scenarios:** productive small teams; stagnation, which he doubts; and non-developers building software, creating later demand for developers.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | US software-dev postings are at 65% of baseline | author's data; reproduces (65.2 on 2025-02-13) | Indeed via FRED; checked against Hiring Lab data |
| C2 | Postings are 3.5× below the 2022 peak | author's data; reproduces (3.59×), though the peak was Feb 2022 | same |
| C3 | Postings are down 8% y/y | reproduces (−8.3%) | same |
| C4 | Baseline is January 2020 | contradicted | own chart axis; Hiring Lab README (1 Feb 2020) |
| C5 | No other segment more than doubled; banking came closest | holds only among the 4 charted sectors; false across all sectors | Hiring Lab sector file |
| C6 | Hospitality postings are down 18% | not reproduced (−7.0% current vintage) | same |
| C7 | Section 174 took effect in 2023 | contradicted by my background knowledge (tax years after 2021); unverified here | none given in the post |
| C8 | Interest rates explain most of the drop | informal argument | timing coincidence; no analysis |
| C9 | GenAI contributes "somewhat" | assertion, hedged | Salesforce anecdote; survey |
| C10 | Indeed under-represents Big Tech and startup postings | anecdote | Microsoft count; Workatastartup |

## Concepts

- Job postings index vs. vacancies vs. hires
- Seasonal adjustment and 7-day trailing average
- ZIRP
- IRC §174 R&E amortization
- Sectoral boom-bust

## Connections

- The source data are Indeed Hiring Lab's Job Postings Index, republished on FRED as IHLIDXUSTPSOFTDEVE and related series.
- Since the post, US software-dev postings have recovered somewhat: 77.3 on 2026-09-18, against all postings at 103.5 (current vintage).

## Bearing on the record

It is labour-market commentary about software engineering, adjacent to AI's economic effects. It carries no claim about ML practice. Any AI-labour claim here is the author's hedged speculation and should not be cited as evidence.

## Limitations

- Postings are a proxy. Indeed coverage may shift over time, and the author says so.
- The comparisons are sector-selective.
- Causal attributions are informal.
- My checks use the current data vintage. The February 2025 vintage the author saw may differ somewhat.

## Open questions

- How much of the software-dev decline is compositional (sector classification of AI/ML and data roles) rather than a fall in demand?
- Does the 2025–26 partial recovery bear on the AI hypothesis?

## Corrections to the seeded skim

- **The baseline is 1 Feb 2020, not January 2020.** The post says Indeed takes "January 2020 to be 100%". Its own chart's axis reads "Index Feb, 1 2020=100". Hiring Lab defines the index as the "% change in seasonally-adjusted postings since February 1, 2020, using a seven-day trailing average".
- **The chart measures postings, not vacancies.** It is an index of active job postings on Indeed: a 7-day trailing average, seasonally adjusted, relative to baseline. It is not a count of vacancies, openings or hires, but the post uses "vacancies", "hiring" and "jobs" interchangeably. The dossier's "Indeed's aggregated postings index (January 2020 = 100)" repeats the baseline error.
- **The peak came in early 2022, not mid-2022.** The software-development series peaked at 233.8 on 2022-02-28 in the current vintage. It was still 228 in May 2022.
- **"No other segment saw hiring more than double in 2022; only banking came close" is false across Indeed's sectors.** Several sectors peaked above 200: Human Resources 243.3, Logistic Support 219.2, Accounting 213.7, Civil Engineering 204.8, Data & Analytics 202.7 and Production & Manufacturing 202.2. Banking & Finance peaked at 190.2. The claim holds only among the four sectors charted. What does hold is that software development has the largest peak-to-Feb-2025 fall (3.59×, next Data & Analytics 3.07×) and the lowest level (65.2).
- **Several sector figures differ from the current data (post vs data):**
  - Hospitality −18% vs −7.0%
  - Banking −7% vs −4.6%
  - Sales −8% vs −6.2%
  - Construction +25% vs +27.6%
  - Accounting +24% vs +22.0%

  Marketing (−19% vs −19.8%) and electrical engineering (+20% vs +19.1%) match. The data are re-seasonally-adjusted weekly and were revised in Nov 2024, so some gap may be vintage. The hospitality gap is too large for that to be assumed.
- **Only Australia exceeds baseline, as claimed.** In the current data: CA 73.6, GB 55.5, FR 68.9, DE 66.7 (its series low on that date), AU 111.7. Canada is "virtually the same graph" in shape (peak 229), but sits higher than the US. The UK is lower than the US.
- **Section 174 timing is misdated (background knowledge, not verified this session).** The post says the amortization rule was "effective from 2023", with impact "only ... from early 2024". My understanding is that it applies to tax years beginning after 31 Dec 2021, i.e. from 2022. If so, it undercuts the post's timing argument that the 2022 drop "can in no way be attributed to it". The post's cross-country argument (UK and France fell too) is unaffected.
