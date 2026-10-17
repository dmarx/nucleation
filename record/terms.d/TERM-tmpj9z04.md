---
status: Active
title: 'transfer entropy: how much the last l values of a source reduce uncertainty about a target''s next value beyond the target''s own last k values, I(X_{t+1}; Y_t^{(l)} | X_t^{(k)}), a directed predictive quantity that depends on k, l and any conditioning series, not a measure of information flow and not an intervention effect'
version: 1
tags:
- information-theory
- causality
date: '2026-10-17'
line: formal-apparatus
summary: >-
  The record names transfer entropy in its readings of Granger causality,
  causal emergence, colloid dynamics, IIT and the global workspace, and
  the documents use different history conventions ([NOTE-053](../notes.d/NOTE-053.md)'s k-histories,
  [NOTE-788](../notes.d/NOTE-788.md)'s single target value at lag τ). This fixes the word from
  Schreiber ([NOTE-tmplm3la](../notes.d/NOTE-tmplm3la.md)), with the history lengths explicit, and says
  what it must not be confused with: flow ([CLAIM-tmpu9ivq](../claims.d/CLAIM-tmpu9ivq.md)), directed
  information, time-delayed mutual information, interventional flow and
  Granger causality.
---

# TERM-tmpj9z04: transfer entropy: how much the last l values of a source reduce uncertainty about a target's next value beyond the target's own last k values, I(X_{t+1}; Y_t^{(l)} | X_t^{(k)}), a directed predictive quantity that depends on k, l and any conditioning series, not a measure of information flow and not an intervention effect

## Definition

Schreiber's Eq. 4 ([NOTE-tmplm3la](../notes.d/NOTE-tmplm3la.md)), in the record's notation:

T_{Y→X}^{(k,l)} = Σ p(x_{t+1}, x_t^{(k)}, y_t^{(l)}) log [p(x_{t+1} | x_t^{(k)}, y_t^{(l)}) / p(x_{t+1} | x_t^{(k)})]
= I(X_{t+1}; Y_t^{(l)} | X_t^{(k)}),

with x_t^{(k)} = (x_t, …, x_{t−k+1}). It is the Kullback entropy of the
assumption that Y's past leaves X's transition law unchanged, and is zero
exactly when it does. A conditional form adds the past of further series Z
to both conditionals. Stated with it, always:

1. **k and l.** Schreiber leaves both free and uses k = l = 1 in his
   examples. Lizier et al. argue k → ∞ is the right limit, since a short
   destination history credits the source with what the destination's own
   past would have predicted ([THEORY-tmp22xor](../theory.d/THEORY-tmp22xor.md)). [NOTE-053](../notes.d/NOTE-053.md) uses
   k-histories. [NOTE-788](../notes.d/NOTE-788.md)'s TE_{x→y}(τ) = I(y_{t+τ}; x_t | y_t) is the k = l = 1
   case at τ = 1. For τ > 1 it conditions on y_t, not y_{t+τ−1}, and is a
   delayed variant Schreiber does not define.
2. **The conditioning set.** Apparent transfer entropy conditions on the
   target's past only. Complete transfer entropy also conditions on the
   target's other causal parents, which must then be known (Lizier et al.,
   Eq. 14).
3. **Average or local.** The transfer entropy is the average of a local
   quantity, log of the same ratio at one time step, which can be negative
   where the source misleads ([THEORY-tmp22xor](../theory.d/THEORY-tmp22xor.md)).
4. **The estimator**, for any number reported. Under a well-specified
   parametric model it is a likelihood-ratio statistic with a χ² null
   ([THEORY-641](../theory.d/THEORY-641.md)). Nearest-neighbour estimates inherit the bias of
   Kraskov et al.'s construction ([THEORY-tmpj670e](../theory.d/THEORY-tmpj670e.md)), and that χ² null does
   not apply to them.

## What it must not be confused with

- **Information flow**, if flow means information in the target attributable
  to the source alone. Transfer entropy is unique plus synergistic
  information ([CLAIM-tmpu9ivq](../claims.d/CLAIM-tmpu9ivq.md), [THEORY-tmpijy6i](../theory.d/THEORY-tmpijy6i.md), [THEORY-tmpt4nh7](../theory.d/THEORY-tmpt4nh7.md)). The words
  "transfer" and "flow" in Schreiber and in Williams and Beer are the
  authors' usage. The record reads them as directed predictive information.
- **Time-delayed mutual information**, I(X_{t+1}; Y_t). It drops the
  target's past, so it counts redundancy and misses synergy, where transfer
  entropy does the reverse ([THEORY-tmpt4nh7](../theory.d/THEORY-tmpt4nh7.md)).
- **Directed information** (Massey), Σ I(X^n; Y_n | Y^{n−1}). It conditions
  on the current source value. Full-history transfer entropy is its lagged
  part; the instantaneous remainder is what transfer entropy misses
  ([THEORY-tmppkvwa](../theory.d/THEORY-tmppkvwa.md)).
- **Interventional information flow** (Ay and Polani), the same formula with
  interventional probabilities. It coincides with transfer entropy only when
  conditioning on the pasts is as good as setting them and every
  configuration has positive probability ([THEORY-tmpkovi2](../theory.d/THEORY-tmpkovi2.md)).
- **Granger causality** ([TERM-tmpq0ms2](TERM-tmpq0ms2.md)). For jointly Gaussian processes,
  Geweke's Granger causality is twice the transfer entropy
  ([THEORY-tmp0xaeq](../theory.d/THEORY-tmp0xaeq.md)). What [CLAIM-tmp6nu4a](../claims.d/CLAIM-tmp6nu4a.md) says of Granger causality and
  interventions holds for transfer entropy too.
