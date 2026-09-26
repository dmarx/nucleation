---
number: 42
status: Read
formerly:
- NOTE-tmpbe1oe
paper: LIT-060
title: 'Bonica, "The Mothership Vortex" (Democratic spam PACs)'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (The full text of the post (data4democracy.substack.com,
    datePublished 2025-08-03T13:02Z; subtitle "How a single consulting firm
    extracted $282 million from a network of spam PACs while delivering just
    $11 million to actual campaigns."), about 1,475 words. I also read the
    embedded end-of-post visualisation, a 2958×13524 px infographic, viewed
    in tiles, and the opening GIF. The dossier had not opened either. I also
    read the whole replication repository,
    github.com/abonica/Mothership-Strategies-FEC-Analysis: one file,
    mothership_complete_api_analysis.R, 586 lines, two commits both dated
    2025-08-02. I audited the script against the current OpenFEC API
    documentation (swagger fetched 2026-09-26). I did **not** run it. It
    needs an FEC API key and five local input files that the repo does not
    contain. My attempt to probe the API's parameter behaviour with the
    shared DEMO_KEY was refused (HTTP 429, rate limit). Every statement
    below about what the script would return comes from reading the code and
    the documentation, not from running it. I did not read the "previous
    article" the post links.). Upgraded from `Skimmed` to `Read`: the claims
    table, assumptions and results are new, and the skim is corrected where
    the full text disagreed.
date: '2026-09-25'
summary: >-
  From FEC filings, Bonica reports that a core network of PACs linked to
  Mothership Strategies raised about $678M from individuals since 2018. Of
  that, $159M went to Mothership, out of $282M it received from all
  clients. "At most" $11M reached candidates, campaigns or national party
  committees, a "fundraising efficiency rate of just 1.6 percent". The
  headline numbers cannot be reproduced from the published repo: its
  inputs are missing, it has a fatal undefined variable, and it computes
  several reported figures nowhere. As documented, its disbursement
  queries cover only the latest two-year period and at most 1,000
  disbursements per committee, largest first, which would bias the $11M
  downward rather than cap it. The post's own infographic contradicts
  several of its figures.
---

<!-- inactive-ok-file: LIT-060 — Deferred: the paper is placed by this reading; the directive lapses when its status changes -->

# NOTE-042: Bonica, "The Mothership Vortex" (Democratic spam PACs)

## Contribution

This is an investigative newsletter post. It follows the money through FEC filings from a cluster of Democratic-aligned PACs to one digital fundraising vendor. It puts a single number on the "efficiency" of spam-style small-dollar fundraising, and argues that the Democratic Party should cut ties with such vendors and set efficiency standards.

## Key insight

If a PAC network's disbursements are traced, very little of what it raises from individuals is passed on as contributions or transfers to candidates and party committees. The rest is consumed by the vendor, texting services, payroll and more fundraising. On this reading the "necessary evil" defence ("it works") mistakes gross receipts for political output.

## Assumptions

These are premises and authorities.
- FEC data are the sole evidence: committee summaries (individual contributions), Schedule B disbursements, and Schedule A receipts, pulled through the OpenFEC API.
- The "network" is a hand-coded list of 35 committee-ID entries (31 distinct IDs) in the script. "Clients" is a second list of 17. How membership was decided is not stated beyond "Mothership-linked". End Citizens United's co-founding by Berlin and Starnes is the one specific link the text states (unsourced).
- "Reaching campaigns" is operationalised in code as Schedule B rows in purpose category CONTRIBUTIONS or TRANSFERS to committees outside the two lists. Independent expenditures (Schedule E) are not queried by the script.
- Mothership's founding story (2014; founded by the former DCCC digital director Greg Berlin and his deputy Charles Starnes; "churn and burn") is stated without sources.

## Key results

What the post reports, attributed to the author:
- $678M raised from individuals by the core network since 2018 (excluding candidate clients).
- $159M paid by the network to Mothership, out of $282M Mothership received from all clients.
- $22.5M to Message Digital LLC. About $150M "consulting/fundraising" and $70M payroll. $19M from Progressive Turnout Project to Shawmut Services for canvassing.
- "At most" $11M to candidates, campaigns or national party committees, giving 11/678 ≈ 1.6%; "approximately half" of it to the DNC, DCCC and DSCC.
- Mothership's clients also include House Majority PAC and Jaime Harrison. "None of this, as far as I can tell, is illegal."
- The infographic adds per-client payments to Mothership: PTP $37.8M, Stop Republicans $27.2M, NDTC $22.9M, CHC BOLD $17.0M, Harrison $16.6M, ECU $16.2M, Ossoff $11.9M, and others. It also shows inter-PAC transfers into PTP (from Stop Republicans $25.9M, Progressive Takeover $13.1M, DEM Turnout 2024 $8.4M) and the PTP and Stop Republicans spending panels described above.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The network raised ≈$678M from individuals since 2018 | the author's own data analysis; not reproducible from the repo | computed from committee_summary CSVs that are not published (script lines 278–283, 526) |
| C2 | The network paid Mothership $159M, out of $282M from all clients | the author's own data; partially reproducible in principle | Schedule B search on recipient "MOTHERSHIP"; the `cycle` parameter the script passes is not a documented Schedule B parameter, so the multi-cycle coverage is unverified; the query spans 2016–2026 while the text says "since 2018" |
| C3 | At most $11M reached candidates and party committees | the author's own data; the bound's direction is unsupported | code sums out-of-network CONTRIBUTIONS/TRANSFERS from a per-committee sample capped at 1,000 rows, largest first, ≥$1,000, and (as documented) latest period only; IEs are excluded |
| C4 | Efficiency is 1.6%, and "98 cents" of each dollar goes to consultants and operations | arithmetic on C1 and C3 (11/678 = 1.62%); the "98 cents" gloss overstates | the author's own chart puts $23.2M of PTP spending in field operations |
| C5 | $22.5M Message Digital; $19M Shawmut; $150M consulting/fundraising; $70M payroll | the author's assertion from data; no code in the repo for the first two; the keyword regex for the $150M (e.g. "text", "email", "digital", "donation") may overlap with the others | script lines 536–548 |
| C6 | About half of the $11M went to the DNC, DCCC and DSCC | assertion; contradicted by the infographic ($4.0M) | none in the repo |
| C7 | Mothership's principals co-founded End Citizens United in 2015 | assertion | no source given in the post |
| C8 | Nothing here is illegal | the author's hedged judgement | "as far as I can tell" |

## Method

The pipeline, as committed in mothership_complete_api_analysis.R:
1. Search Schedule B for recipients matching "MOTHERSHIP" (lines 206–244), passing `cycle=2016,…,2026`. The current OpenFEC swagger lists no `cycle` parameter for /schedules/schedule_b/, and says results "default to the most recent two-year period" when `two_year_transaction_period` is absent. Whether the API ignored or honoured `cycle` in August 2025 could not be tested.
2. Join payments to locally stored committee-summary CSVs for 2018–2026 by committee ID (lines 278–290). These files are not in the repo. Line 318 then references `top_100_clients`, which is never defined.
3. Fetch committee details, incoming transfers (Schedule A, ≥$10,000) and outgoing disbursements (Schedule B, `recipient_committee_id_null=FALSE`, which is not a documented parameter, sorted `-disbursement_amount`, `min_amount=1000`, `set_limit=10` pages of 100). No transaction period is passed, so the documented default is the latest period only. `write_csv` is called at line 416 before `readr` is loaded (line 440), so that tryCatch block reports failure even though its data frame has already been assigned.
4. Classify disbursements by regex on the description (lines 536–548). Sum CONTRIBUTIONS and TRANSFERS to committees outside the two hand lists to get "Total spent on outside candidates and committees" (lines 566–577).

## Concepts

- **fundraising efficiency rate**: the author's measure, (contributions + transfers to outside candidates and committees) ÷ (individual contributions raised). It excludes independent expenditures, field and canvassing spending, and advocacy, by construction.
- **"churn and burn"**: high-volume, urgency-driven small-dollar solicitation that trades long-term donor relationships for short-term revenue.
- **core network / connected PAC**: the hand-coded list of committees the author treats as Mothership-linked, as distinct from ordinary clients.

## Connections

It follows the author's earlier post documenting the spam tactics themselves (linked, not read). Don Moynihan (c06) links a different Bonica post on shutdowns. The subject overlaps a long-running journalistic literature on "scam PACs". The post cites none of it, and I have not checked it.

## Bearing on the record

It carries nothing for ML practice and no instruction for the Anthology of the SOTA. As a reading-record item it is a worked example of a headline ratio whose numerator and denominator come from differently scoped queries. It is the shape [ANTH-DP-010](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/DP-010.md) describes: the 1.6% is the sentence that travels, and the published repo does not carry it.

## Limitations

- **Not reproducible as published.** Inputs are missing, the script has a fatal undefined variable, and several reported figures have no code.
- **A mismatch in scope between numerator and denominator** is likely. The denominator is summary data for every cycle from 2018. As documented, the numerator's disbursement pull covers only the latest period and is capped. The infographic's Stop Republicans panel ($17.8M total spending, against $27.2M paid to Mothership) is consistent with the numerator seeing only part of the data. This is an inference from the code, the documentation and the chart; it was not run.
- **The definition of "reaching campaigns"** excludes independent expenditures and field operations. A PAC that spends on IEs or canvassing for candidates scores zero for that spending.
- **The infographic and the text disagree** ($282M vs $159M attributed to the network; $4.0M vs ≈$5.5M to the party; network membership).
- **No response from the named firms** is included. The network lists are hand-coded without stated criteria.

## Open questions

- What is the efficiency ratio when every cycle is queried with full pagination, and with IEs and field spending reported as separate categories? That run would settle C1–C4.
- How does this network compare with Republican and other Democratic small-dollar operations measured the same way? Without a comparison, "1.6%" has no reference point.

## Corrections to the seeded skim

- The dossier says replication is the "only deeper work" and "the claims are fully captured". Auditing the repo (see Method and Limitations) finds that the headline numbers are not reproducible from it as published. The script reads committee_summary_2018–2026.csv files that are not in the repo. It references an undefined object (`top_100_clients`, line 318), which halts a non-interactive run whenever those files are present. It contains no computation at all for the $22.5M (Message Digital), $19M (Shawmut), $150M/$70M split or "about half to the DNC, DCCC and DSCC" figures.
- The dossier gives the $11M as an upper bound ("passed at most about $11M"), following the post. The code gives no upper bound. Outgoing disbursements are fetched sorted by amount descending, capped at 10 pages × 100 records per committee, with `min_amount=1000` and, as documented, only the most recent two-year period, because no `two_year_transaction_period` is passed. Candidate contributions, which are small, are the records such a cap drops first. The $11M is therefore, if anything, a truncated count.
- The dossier omits the infographic, which contradicts the text in four places. (a) "What the Network Gets: $282M in revenue paid to Mothership", whereas the text says the network paid $159M and $282M is all clients. (b) "What the Party Gets: $4.0M in direct donations", whereas the text has "approximately half" of $11M going to the three national committees. (c) The bar chart colours House Majority PAC, AMERIPAC, CHC BOLD PAC and Let America Vote PAC red as "core network", whereas the code lists the first three only as ordinary clients and does not list the fourth at all. (d) Its Stop Republicans panel shows total spending of $17.8M ($10.8M transfers + $7.0M fundraising and media), while the same graphic shows Stop Republicans paying Mothership $27.2M and transferring $25.9M to Progressive Turnout Project. The spending panels evidently cover only part of the data.
- The dossier's check-list asks whether independent expenditures count. The infographic's PTP panel does count "Direct Candidate Support (Contributions & IE)" ($4.0M, 6%). It also shows "Campaign & Field Operations" at $23.2M (36%). The text's "98 cents goes to consultants and operational costs" therefore absorbs field operations that the author's own chart separates out.
