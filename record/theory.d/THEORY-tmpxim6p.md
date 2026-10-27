---
status: Active
title: 'In infinite sparse factor analysis, where a binary mask says whether a source is active at a data point and an independent Gaussian value says how strongly, the evidence of that data point for the source being active, with its value integrated out, is σ̂·exp(μ̂²/(2σ̂²)) for the posterior mean μ̂ and standard deviation σ̂ of the value; when the residual has no component along the source''s loading the ratio is σ̂, below one, so the data favour an inactive source over an active one at zero by a factor that the prior on the value sets'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed Active from NOTE-tmpmxqaw. The ratio is the paper's, §3 of
    Knowles and Ghahramani (2007), from its eq. (9); the reading at μ̂ = 0
    is the record's. Both were checked by numerical integration: with
    D = 5, σ_ε² = 0.7 and random g and ε, quadrature gives 0.310857 and
    the formula 0.310857; with ε projected off g, quadrature gives
    0.259695 and σ̂ = 0.259695 (record script, 2026-10-27).
tags:
- probabilistic-modeling
- mathematical-statistics
date: '2026-10-27'
source:
- LIT-tmpezspt
summary: >-
  Knowles and Ghahramani (2007), [LIT-tmpezspt](../literature.d/LIT-tmpezspt.md), read in [NOTE-tmpmxqaw](../notes.d/NOTE-tmpmxqaw.md). With
  y = g x + ε, x ~ N(0, 1), ε ~ N(0, σ_ε² I): ∫ p(y | x) p(x) dx / p(y |
  x = 0) = σ̂ exp{μ̂²/(2σ̂²)}, σ̂² = σ_ε²/(σ_ε² + g′g), μ̂ = g′ε/(σ_ε² +
  g′g). It is the Gaussian case only; the Laplacian case is the paper's
  (14), checked the same way. It concerns one data point and one source,
  with the loading known.
---
<!-- inactive-ok-file: CASE-165 — Proposed; the construction this bears on, cited as open -->

# THEORY-tmpxim6p: In infinite sparse factor analysis, where a binary mask says whether a source is active at a data point and an independent Gaussian value says how strongly, the evidence of that data point for the source being active, with its value integrated out, is σ̂·exp(μ̂²/(2σ̂²)) for the posterior mean μ̂ and standard deviation σ̂ of the value; when the residual has no component along the source's loading the ratio is σ̂, below one, so the data favour an inactive source over an active one at zero by a factor that the prior on the value sets

## Source

Knowles and Ghahramani (2007), *Infinite sparse factor analysis and
infinite independent components analysis*, [LIT-tmpezspt](../literature.d/LIT-tmpezspt.md), read in full in
[NOTE-tmpmxqaw](../notes.d/NOTE-tmpmxqaw.md): §3, eqs. (9) and (12)–(14).

## What was actually shown

**The ratio.** With the other sources fixed, the residual ε = y_t −
Σ_{j≠k} g_j z_jt x_jt satisfies ε = g_k x + noise when z_kt = 1 and ε =
noise when z_kt = 0. With x ~ N(0, 1), the marginal likelihood ratio is
r_l = σ̂ exp{μ̂²/(2σ̂²)}, where σ̂² = σ_ε²/(σ_ε² + g_k′g_k) and μ̂ =
g_k′ε/(σ_ε² + g_k′g_k) are the posterior variance and mean of x, (9). The
posterior odds of z_kt = 1 multiply r_l by the IBP's prior odds,
m_{k,−t}/(β + N − 1 − m_{k,−t}).

**At zero signal.** If ε has no component along g_k, μ̂ = 0 and r_l = σ̂ <
1. The data then favour z_kt = 0, by the factor σ̂, which is how much the
prior's spread on x exceeds the posterior's. A stronger loading (larger
g′g) or a wider prior on x makes the factor smaller.

**The check.** At D = 5, σ_ε² = 0.7, random g and ε: quadrature 0.310857,
formula 0.310857; with ε projected off g: quadrature 0.259695, σ̂ =
0.259695. The Laplacian version, (14), gave 0.322171 both ways (record
script, 2026-10-27).

## What this does not say

- **Not that the mask is identified in general.** With the loading and
  other sources unknown, splits, rescalings and absorption remain
  ([CASE-165](../cases.d/CASE-165.md), items 3–4).
- **Not that the data decide without the prior.** The factor is the
  prior's: with x fixed at a value near zero instead of integrated out,
  "on" and "off" fit equally.
- **Not about a sequence.** The paper's model has no dynamics; the
  infinite factorial HMM adds them ([LIT-1577](../literature.d/LIT-1577.md)).

## Connections

- **[CASE-165](../cases.d/CASE-165.md), item 3.** Qualifies "availability is told from activation
  only by the prior and the transition, not by the data": true with the
  activation fixed; with the activation integrated out, the data carry an
  Occam factor against holding an unused feature, whose size the
  activation's prior sets.
- **[THEORY-tmpo1cju](THEORY-tmpo1cju.md).** The mask's prior is the IBP; its prior odds term
  is the buffet's m/(N − m) at β = 1.
