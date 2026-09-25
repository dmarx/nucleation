---
status: Deferred
status_note: seeded from the abstract and a skim on 2026-09-25; not read in full
title: 'The ergodicity solution of the cooperation puzzle'
version: 1
tags:
- complex-systems
- probabilistic-modeling
- social-science
date: '2026-09-25'
published: '2022-05-23'
doi: '10.1098/rsta.2020.0425'
first_author: 'Peters'
keywords:
- 'cooperation'
- 'ergodicity'
- 'evolution'
implementations: []
summary: >-
  Peters et al. (2022), DOI-10.1098/rsta.2020.0425. If resources grow multiplicatively with noise, then pooling and sharing among N cooperators cuts the effective variance from σ² to σ²/N. That raises each member's time-average growth rate from μ−σ²/2 to μ−σ²/(2N), so cooperators out-grow non-cooperators with no complementarity or threshold benefit needed. Cooperation is then the baseline to expect, and its absence is what needs explaining.
---

# LIT-tmp390ie: The ergodicity solution of the cooperation puzzle

Ole Peters, Alexander Adamou (2022), *Philosophical Transactions of the Royal Society A 380(2227), 20200425. Theme issue "Emergent phenomena in complex physical and socio-technical systems: from cells to societies"* — DOI-10.1098/rsta.2020.0425

## Key takeaways

- If resources grow multiplicatively with noise, then pooling and sharing among N cooperators cuts the effective variance from σ² to σ²/N. That raises each member's time-average growth rate from μ−σ²/2 to μ−σ²/(2N), so cooperators out-grow non-cooperators with no complementarity or threshold benefit needed. Cooperation is then the baseline to expect, and its absence is what needs explaining.

*Seeded from the abstract and a skim, not a reading. What follows is what the work says about itself.*

Sharing resources looks altruistic, and classical accounts explain it through immediate benefits such as complementarity or thresholds. The authors ask whether cooperation is predictable without those. They model resources as geometric Brownian motion (self-multiplying with fluctuations). In this model the ensemble-average growth rate is higher than the time-average growth rate a single trajectory actually achieves, by a term that depends on the size of the fluctuations. Repeatedly pooling and sharing shrinks the fluctuations and raises the time-average growth rate toward the ensemble rate as cooperators are added. So cooperators simply grow faster, which the authors offer as an explanation for cooperation in simple environments and as a behavioural baseline.

## Standing in the record

Filed from the survey of 2026-09-25 of work the anthology set aside as out of scope (tier C): 450 seconds of active reading over 2 sessions in the papers-feed tracker. `Deferred` because nobody has read it closely here yet, not on merit.

**Priority for a deeper reading: medium — 450 s over 2 sessions and part of the held theme issue. The core result is one equation that the skim fully captures, so a deeper read adds value only through the generalizations and the comparison with bet-hedging.**

What a deeper reading should check:

- Time averages versus ensemble averages matter well beyond cooperation, for example the Kelly criterion, log-utility, and multiplicative dynamics in training such as weight growth and variance of returns in RL. A deeper read should check the correlated-fluctuation case, where the benefit shrinks.
- The claim that this solves the cooperation puzzle depends on self-multiplying resources and cheap enforcement. Check whether the generalizations section shows when the premium goes away, for example with ρ → 1 or very unequal members.
- Ergodicity economics is contested within economics, and the paper gives no survey of counter-arguments. A deeper read should weigh the claim against the geometric-mean-fitness and bet-hedging literatures the authors cite.

Access when seeded: Crossref (online 2022-05-23) and the full text as Europe PMC XML (PMC9125229, open access), which I read: abstract, introduction, model sections, the "ergodicity solution" and group-selection sections, generalizations, and discussion. The Royal Society PDF returned 403. The journal records it as received 30 Apr 2021 and accepted 20 Oct 2021. Related: arXiv:1506.03414, "An evolutionary advantage of cooperation" (same authors, v1 10 Jun 2015, v2 24 May 2018), states the same argument in an earlier abstract. It has a different title and no journal reference on arXiv, so I have not treated it as this work's first appearance (unverified whether the RSTA paper is its published form).
