---
status: Active
status_note: >-
  read in full 2026-10-31 ([NOTE-tmphrg34](../notes.d/NOTE-tmphrg34.md)) from the PMC copy; worth reading
  as the clearest worked case of a maintained chemical state that is
  metastable at finite size: bistability needs the chemostats out of
  equilibrium, long-run occupancy does not depend on the starting state,
  the slow eigenvalue is the sum of the escape rates
  ([THEORY-tmpwystk](../theory.d/THEORY-tmpwystk.md)), and entropy production does not pick the stable state
  ([THEORY-tmpshz26](../theory.d/THEORY-tmpshz26.md)). Its large-volume rate formula carries a spurious 1/V,
  so its reported breakdown of asymptotics is mostly that factor.
title: 'Stochastic dynamics and non-equilibrium thermodynamics of a bistable chemical system: the Schlögl model revisited'
version: 2
history:
- version: 1
  date: '2026-10-31'
  note: >-
    Filed, not read, from A13 of the exchange "Analyze nucleation
    concepts" (2026-10-30 to 31). Citation checked against Crossref
    (online 2008-12-18, print 2009). A13 linked PMC2838355 with a
    shortened title. No arXiv version was found. The summary follows
    the abstract and the exchange's description; a reading should
    check it first.
- version: 2
  date: '2026-10-31'
  note: >-
    Read in full in NOTE-tmphrg34 from the PubMed Central HTML of the
    version of record (PMC2838355), equations read from its images; the
    PMC and Royal Society PDFs were refused to this client. Status
    Deferred → Active. The citation stands. The summary is rewritten
    from the text; the registration's description (switching, its time
    scale, the driving bistability needs) was accurate. Produces
    THEORY-tmpwystk and THEORY-tmpshz26, and with LIT-tmpm46ks
    THEORY-tmpkze5s.
tags:
- thermodynamics
- natural-sciences
date: '2026-10-31'
published: '2008-12-18'
doi: '10.1098/rsif.2008.0476'
first_author: 'Vellela'
keywords:
- 'Schlögl model'
- 'bistability'
- 'chemical master equation'
- 'nonequilibrium steady state'
- 'entropy production'
- 'Keizer paradox'
implementations: []
summary: >-
  Vellela & Qian (2009). The Schlögl model A + 2X ⇌ 3X, B ⇌ X by rate
  equation, chemical master equation and open-system thermodynamics.
  Bistability requires the two chemostats out of equilibrium. The master
  equation has one two-peaked stationary distribution, so the long-run
  occupancy of the two states is set by parameters and volume, not by the
  initial condition, and which state dominates can change with volume
  alone. The slow eigenvalue, exponentially small in volume, is the sum of
  the two escape rates. The more stable state can carry the higher or the
  lower entropy production, and the Fokker–Planck approximation can pick
  the wrong dominant state.
---
<!-- inactive-ok-file: THEORY-671 — Proposed; the maximum entropy production account this reading counts against, named as open -->


# LIT-tmpkp8vh: Stochastic dynamics and non-equilibrium thermodynamics of a bistable chemical system: the Schlögl model revisited

Vellela, M., & Qian, H. (2009). Stochastic dynamics and non-equilibrium thermodynamics of a bistable chemical system: the Schlögl model revisited. *Journal of the Royal Society Interface*, 6, 925–940.

Read in full in [NOTE-tmphrg34](../notes.d/NOTE-tmphrg34.md).

## Why this is here

A13's worked example of a bistable dissipative system whose maintained state has a finite stochastic lifetime. It is the chemical counterpart of the saddle-node constructions in [CASE-tmpwxags](../cases.d/CASE-tmpwxags.md), and of [CASE-111](../cases.d/CASE-111.md). The reading bears that out and says what the deterministic cases leave out: at finite size a maintained regime is metastable, it is lost by fluctuation on a time exponential in size, and the barrier setting that time closes at the fold, as (distance)^{3/2} in this model ([THEORY-tmpwystk](../theory.d/THEORY-tmpwystk.md)). It is also a clean counterexample to ranking steady states by entropy production ([THEORY-tmpshz26](../theory.d/THEORY-tmpshz26.md)), against [THEORY-671](../theory.d/THEORY-671.md).
