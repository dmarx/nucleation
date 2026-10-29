---
status: Proposed
promote_when: >-
  A study that varies the number and spread of paired interventions on
  fixed base and abstracted models and measures held-out abstraction error
  for a compatibility-based transport cost against a structure-blind one,
  showing the advantage growing with the intervention set and reversing
  when it is small, on models beyond the two synthetic ones and the one
  dataset reported; or showing that it does not.
title: 'When an abstraction map between two causal models is learned by optimal transport from paired interventional distributions, a transport cost that rewards pairs of states compatible with the same paired interventions gives much lower held-out abstraction error than a Hamming cost when the intervention set is rich, and higher error when it holds only a few, because with few interventions the compatibility cost is nearly uniform'
version: 1
tags:
- causality
date: '2026-10-29'
source:
- LIT-tmpdrddx
summary: >-
  Felekis et al. (CLeaR 2024), [LIT-tmpdrddx](../literature.d/LIT-tmpdrddx.md), §§4.2 and 6 and Appendices C
  and E, read in [NOTE-tmpohrox](../notes.d/NOTE-tmpohrox.md). Two synthetic models (STC, LUCAS) and one
  real two-lab dataset (EBM), all discrete, evaluated by leaving one
  intervention pair out. The ω-cost wins on STC with parent-free
  interventions and on LUCAS, loses on STC with two interventions on tar
  and on EBM. The explanation, a nearly uniform cost when interventions
  are few, is argued and fits the four cases. Proposed.
---

# THEORY-tmpd2jd5: When an abstraction map between two causal models is learned by optimal transport from paired interventional distributions, a transport cost that rewards pairs of states compatible with the same paired interventions gives much lower held-out abstraction error than a Hamming cost when the intervention set is rich, and higher error when it holds only a few, because with few interventions the compatibility cost is nearly uniform

## Source

Felekis et al. (2024), [LIT-tmpdrddx](../literature.d/LIT-tmpdrddx.md), §4.2 (pp. 6–7), §6 (pp. 8–10) and
Appendices C and E (pp. 17, 19–23) of arXiv 2312.08107v1; read in
[NOTE-tmpohrox](../notes.d/NOTE-tmpohrox.md).

## What was actually shown

**The cost.** c_ω(x, x′) = |I| − Σ_ι 1[Cmp(x, ι) ∧ Cmp(x′, ω(ι))]: a base
state and an abstracted state are cheaper to match the more paired
interventions they are both compatible with (eq. 11, p. 6). "By
construction, cω will assign maximum values (|I|) for samples for which it
has no available information from the ω map" (p. 17).

**The comparisons.** Abstraction error of the learned map on a held-out
intervention pair, by JSD and Wasserstein distance, 50 repetitions (p. 9).

- STC with interventions on the parentless smoking variable: the ω-cost
  beats Hamming in every method, e.g. e_JSD 0.010 against 0.087 for the
  best COTA setting and 0.013 against 0.093 for independent plans (Table
  1, p. 10).
- LUCAS: the ω-cost is at least as good, by small margins (Table 4,
  p. 11; Tables 10–11).
- STC with I = {do(T = 0), do(T = 1)}: Hamming better (0.229 against 0.249,
  Table 2, p. 10).
- EBM, the battery data: Hamming better (0.220 against 0.379, Table 3,
  p. 10).

The authors' account: a small intervention set makes the ω-cost
"almost-uniform and uninformative" (p. 9).

**What could have failed.** The ω-cost could have won or lost regardless
of the size of I.

## What this does not say

- **That the gain comes from causal constraints between plans.** The
  do-calculus term is constant on the feasible set ([THEORY-tmp1lvzk](THEORY-tmp1lvzk.md)); the
  cost is what differs between the compared settings, and the cost acts
  the same way in the baselines with no causal term.
- **How rich is rich enough.** Four cases, with sizes not varied
  systematically.
- **Anything for continuous variables or large domains.** All domains are
  small and discrete.
- **That the learned maps are causal abstractions in a strong sense.**
  The target is an approximate one-distribution exact transformation, with
  a stochastic τ ([THEORY-849](THEORY-849.md), [CLAIM-399](../claims.d/CLAIM-399.md)).
