---
status: Read
paper: 'LIT-tmpa48v2'
title: 'Leung, Chen, Yadav and Gallien: inventory policy and stock-outs in Zambia'
version: 1
history:
- version: 1
  date: '2026-11-23'
  note: >-
    Read on 2026-11-23 by the lead run of that date in full, from the PMC
    XML of PMC4882057 fetched through NCBI E-utilities efetch (db=pmc),
    the repository's documented interface (ADR-101). Read as a stand-in
    (ADR-114) for Vledder et al. 2019, which was not reached. Not read:
    supplement S1, which holds the primary analysis's table for
    artemether-lumefantrine, and the figure images; numbers here are from
    the text.
date: '2026-11-23'
summary: >-
  Stock cards photographed in 145 Zambian clinics during the government's
  2009/10 supply chain pilot show stock-outs of artemether-lumefantrine
  falling to 5 % or less late in 2009 and rising to about 20-30 % early in
  2010, while the national warehouse held ample stock. A discrete-event
  simulation validated against those records traces them to max-min
  replenishment targets based on past monthly issues, which miss seasonal
  demand and rainy-season lead times. The paper restates the pilot's two
  arms and its primary result, not its costs.
---
<!-- inactive-ok-file: LIT-tmpuedwt — new and Unfetched; the pilot's primary evaluation, filed by the lead run of 2026-11-23 -->
<!-- inactive-ok-file: CASE-tmpjfl6r — new; the coding study this reading informs, filed by the lead run of 2026-11-23 -->

# NOTE-tmpmco2w: Leung, Chen, Yadav and Gallien: inventory policy and stock-outs in Zambia

## Contribution

A secondary analysis of Zambia's 2009/10 supply chain pilot, which asks
why stock-outs returned in early 2010 though central stock was ample, and
answers with a validated simulation of the inventory policy every
facility used.

## Key results

- **The pilot (Introduction).** "a quasi-randomized field experiment in 16
  districts to evaluate two supply chain models". "Intervention A
  maintained intermediary stock with picking and packing activities in
  district stores; Intervention B converted district stores into
  cross-docking points for shipments pre-packaged for the clinics at the
  national warehouse." In 12 intervention districts "a new employee
  (commodity planner) was solely dedicated to inventory management".
  Vledder et al. report "a substantial reduction of the average number of
  days without stock for these products in intervention B compared with
  intervention A and control facilities", and on that basis the
  government "decided later in 2010 to progressively deploy district
  cross-docking to the entire country".
- **Stock-outs with a full warehouse (Results).** Stocked-out clinics fell
  from about 20 % (30 % for AL 6) in May 2009 to 5 % or less in
  October-November 2009, then rose to about 20 % (30 % for AL 6) in
  February-March 2010; central stock was "always higher than 800,000
  adult regimens equivalent".
- **The cause (Discussion).** "These stock-outs can therefore be
  attributed to that inventory policy, as opposed to procurement or
  training issues." The policy's targets use past issues, so the December
  shipment is small, the larger ones arrive in April because of rainy-
  season lead times, and the clinic stocks out at peak demand.
- **Parameter fixes help little.** Raising the target from 4 to 5 and 6
  months of issues raises service from 88 % to 95 % and 97 % at roughly
  1:1 and 2:1 increases in average and maximum stock; the recommended
  changes in averaging window move service between 87.5 % and 92 %.

## Assumptions

- Infinite central supply, consistent with warehouse records.
- Lognormal weekly demand, coefficient of variation 50 %; geometric lead
  times with a seasonal access interruption.

## Concepts

- **Max-min (periodic-review base-stock) policy**: order up to a multiple
  of average past monthly issues.
- **Cross-docking**: the district passes on packages made centrally,
  holding no stock of its own.

## Bearing on the record

- **LEAD-044**, as a stand-in for Vledder et al. (LIT-tmpuedwt). The pilot's
  two arms act at different tiers of one supply chain: picking, packing
  and stock at the district, or at the national warehouse. Leung et al.
  report that B did better; they give no costs per arm, so the pilot
  cannot be coded at equal budget from this reading. See
  CASE-tmpjfl6r.
- **CLAIM-562**, as a parallel. The paper's own finding is that a
  rule shared by both arms, the order-up-to target, binds at the clinic:
  raising the amount held ("increasing the target multiple") buys service
  at a steep price in stock, while the authors place the remedy in central
  forecasting. That is a placement argument, made by the authors about a
  capability, not tested as an intervention.

## Limitations

- A secondary analysis of artemether-lumefantrine only, in a subset of
  clinics; the primary analysis is in supplement S1 and in Vledder et al.,
  neither read.
- "quasi-randomized", in these authors' words.
