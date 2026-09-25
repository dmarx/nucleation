---
number: 59
status: Skimmed
formerly:
- NOTE-tmpj57st
paper: LIT-035
title: 'Peters & Adamou 2022, the ergodicity solution of cooperation'
version: 1
date: '2026-09-25'
summary: >-
  If resources grow multiplicatively with noise, then pooling and sharing among N cooperators cuts the effective variance from σ² to σ²/N. That raises each member's time-average growth rate from μ−σ²/2 to μ−σ²/(2N), so cooperators out-grow non-cooperators with no complementarity or threshold benefit needed. Cooperation is then the baseline to expect, and its absence is what needs explaining.
---

<!-- inactive-ok-file: LIT-035 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-25 -->

# NOTE-059: Peters & Adamou 2022, the ergodicity solution of cooperation

## Contribution

Sharing resources looks altruistic, and classical accounts explain it through immediate benefits such as complementarity or thresholds. The authors ask whether cooperation is predictable without those. They model resources as geometric Brownian motion (self-multiplying with fluctuations). In this model the ensemble-average growth rate is higher than the time-average growth rate a single trajectory actually achieves, by a term that depends on the size of the fluctuations. Repeatedly pooling and sharing shrinks the fluctuations and raises the time-average growth rate toward the ensemble rate as cooperators are added. So cooperators simply grow faster, which the authors offer as an explanation for cooperation in simple environments and as a behavioural baseline.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §2 Noisy multiplicative growth: GBM is used as a universal null model ("from viral spread to financial investment"). There are two growth rates: the ensemble rate μ and the time-average rate μ−σ²/2. Their gap is the non-ergodicity.
- §3–4 Cooperation protocol and main result (Fig. 2): grow, pool, share. The effective variance falls to σ²/N (the extracted text renders the volatility as "σ/N", but the stated rate implies variance σ²/N), so the time-average rate becomes μ−σ²/(2N). The premium scales as 1−1/N, with the biggest marginal gains going from 1 to 2 to 3 members. Cooperating pairs out-grow even the average of the non-cooperators, so "cooperation and averaging are not equivalent operations".
- §4 Group selection: the authors place the result within individual selection, since what is good for the group is good for each member. Defectors gain in the short term, and an "ignore-for-tat" exclusion policy suffices to protect the cooperative.
- §5 Generalizations: with idiosyncratic drifts and volatilities, the question becomes when leaders should share with laggards. Correlated fluctuations (covariance ρ) reduce the benefit. They cite partial cooperation (taxation-like) and network versions by other authors.
- §6 Discussion: when resources self-reproduce, the absence of cooperation needs special explanation (coordination costs, groupthink, skill differences). Risk management raises long-run growth, which they argue is an overlooked rationale for insurance, pensions and taxation. The paper is presented as part of the "ergodicity economics" programme.

## Open questions

- Time averages versus ensemble averages matter well beyond cooperation, for example the Kelly criterion, log-utility, and multiplicative dynamics in training such as weight growth and variance of returns in RL. A deeper read should check the correlated-fluctuation case, where the benefit shrinks.
- The claim that this solves the cooperation puzzle depends on self-multiplying resources and cheap enforcement. Check whether the generalizations section shows when the premium goes away, for example with ρ → 1 or very unequal members.
- Ergodicity economics is contested within economics, and the paper gives no survey of counter-arguments. A deeper read should weigh the claim against the geometric-mean-fitness and bet-hedging literatures the authors cite.
