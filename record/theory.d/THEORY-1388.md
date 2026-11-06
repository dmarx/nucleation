---
number: 1388
status: Active
formerly:
- THEORY-tmpegbva
title: "De Oliveira, de Sá and Martins give multi-period forms of the FLEET and local-reliability expected covering models, letting ambulances move among bases between periods, and trade the number of bases against coverage as a bi-objective problem, for Belo Horizonte's emergency medical service"
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Promoted by the thirtieth status review, at the status review's
    ruling (the owner delegated these rulings); ADR-065. NOTE-1621 v2
    reads the paper in full. Its condition held: §3 gives multi-period
    forms of both FLEET (FLEET-ICt) and LR-MEXCLP (LR-MEXCLP-ICt) in which
    each ambulance's base is chosen per period, §4 adds the number of
    bases as a second objective solved by the ε-constraint method, and §5
    applies both to Belo Horizonte's SAMU. The deleted promote_when read:
    'The multi-period formulations of §3 read, confirming that both the
    FLEET and the local-reliability expected covering models are given
    forms over several periods that let ambulances move among bases
    between periods, and that the number of bases is traded against
    coverage as a second objective, for the emergency medical service of
    Belo Horizonte.' The title is unchanged. A dated note records what
    the abstract's coverage gains compare and that the probabilistic
    coverage rates do not follow from the stated objective.
tags:
- operations-research
- probabilistic-modeling
date: '2026-11-04'
source:
- LIT-2092
summary: >-
  De Oliveira, de Sá and Martins (2020), [LIT-2092](../literature.d/LIT-2092.md), read in full in
  [NOTE-1621](../notes.d/NOTE-1621.md). Active: the account reports the paper's models, and §§3–5
  contain them as stated. Relocation is a per-period allocation with no
  cost or limit, and bases once opened stay open. The coverage gains the
  abstract reports are not part of the account; the relocation gains it
  names mostly come from optimizing the bases (dated note).
---
# THEORY-1388: De Oliveira, de Sá and Martins give multi-period forms of the FLEET and local-reliability expected covering models, letting ambulances move among bases between periods, and trade the number of bases against coverage as a bi-objective problem, for Belo Horizonte's emergency medical service

## Source

De Oliveira, de Sá and Martins (2020), [LIT-2092](../literature.d/LIT-2092.md); read in full in [NOTE-1621](../notes.d/NOTE-1621.md).

## What was actually shown

- **FLEET-ICt (§3.1, eqs. 20–27).** Coverage of each service type's
  demand in each period by an ambulance of that type within its
  standard, with x^t_ju indexed by period and z_j not: "once a base is
  opened, it must remain open until the end of the planning horizon"
  (p. 14).
- **LR-MEXCLP-ICt (§3.2, eqs. 28–38).** The same constraints, with demand
  weighted by q^t_iuk = 1 − (b^t_iuk)^k for k ambulances in the
  neighbourhood.
- **The bi-objective form (§4.1, eqs. 39–44).** Minimize the number of
  bases, scalarized by Σ z_j ≤ ε, ε from 14 to the unconstrained count.
- **The application (§5).** Belo Horizonte, 427 nodes, 1,527 candidate
  sites, 24 hourly periods, 7 ALS and 21 BLS ambulances, at most two per
  base, solved exactly with CPLEX.

## What this does not say

- That relocation raises coverage by the amounts the abstract reports
  (see the note below).
- That relocation has a cost or a limit: the models charge nothing for it.
- That the probabilistic model escapes the independence assumption: by the
  paper's own §2, LR-MEXCLP still assumes independent servers and locally
  constrained service areas.
- Anything about the value of an idle or rarely used ambulance.

## Note of 2026-11-06: what the reported gains compare

The abstract says relocation "might improve coverage levels by up to 21%
for the deterministic approach and up to 15% for the probabilistic
approach". By Tables 2–3 those figures, in percentage points, match only
comparisons that also replace the 2019 bases by optimized ones; two
static runs of the probabilistic model already differ by 15.0 points.
Relocation alone, with the base regime held, adds +0.5 and +1.7 points to
FLEET-ICt and −0.3 and +0.1 to LR-MEXCLP-ICt, and the probabilistic
model's printed coverage rates are not the ratio §5.4 defines
(scratch/formal/oliveira_tables_check.py). The account does not rest on
these figures.
