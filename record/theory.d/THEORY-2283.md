---
number: 2283
status: Proposed
formerly:
- THEORY-tmp8j9f4
promote_when: >-
  An independent analysis of facility stock records from a public supply
  chain using max-min replenishment on past issues, in Zambia or
  elsewhere, finds stock-outs of a seasonally demanded medicine that rise
  at the start of its high season while central stock is ample, and
  traces them to replenishment targets set from past issues. Not met by
  the authors' own simulation re-run, nor by a finding of stock-outs
  caused by central shortage.
title: 'Zambian stock-outs came from replenishment rules'
statement: >-
  Leung, Chen, Yadav and Gallien find, from stock cards in 145 Zambian
  clinics and a validated simulation, that stock-outs of
  artemether-lumefantrine rose to about 20-30 % of clinics in early 2010
  while the national warehouse held ample stock, caused by max-min
  replenishment targets set from past monthly issues, which miss seasonal
  demand and rainy-season lead times
version: 1
history:
- version: 1
  date: '2026-11-23'
  note: >-
    Filed by the lead run of 2026-11-23 from the reading NOTE-2401
    (full text; supplement S1 not read).
tags:
- operations-research
- society-and-governance
date: '2026-11-23'
source:
- LIT-3155
summary: >-
  During Zambia's 2009/10 supply chain pilot, with dedicated staff
  enforcing the max-min policy and central stock above 800,000 adult
  regimens, stocked-out clinics fell to 5 % or less late in 2009 and rose
  to about 20 % (30 % for one product) early in 2010. A discrete-event
  simulation of one clinic, validated out of sample, reproduces the rise:
  targets from the last three months' issues make the December order
  small and the larger orders arrive after peak demand. Raising the
  target buys service at roughly proportional extra stock; the recommended
  averaging changes help little.
---

# THEORY-2283: Zambian stock-outs came from replenishment rules

## The account

Leung and colleagues ([NOTE-2401](../notes.d/NOTE-2401.md)): "Inventory control policies widely
recommended and used for distributing medicines in sub-Saharan Africa
directly account for a substantial fraction of stock-outs observed in
common situations involving demand seasonality and facility access
interruptions. Developing central capabilities in peripheral demand
forecasting and inventory control is critical."

## What it rests on

- Stock-card photographs transcribed by double keying; lead times from
  commodity planners' reports; access interruptions from staff surveys.
- A one-clinic simulation with infinite central supply, checked against
  field stock-out proportions.

## What it does not say

- Anything about the costs of the pilot's two arms, or which arm the
  sampled clinics belonged to in the stock-out series.
- That the result carries to products without seasonal demand; the
  authors expect excess stock rather than stock-outs there.
