---
status: Active
title: 'Latent features made dependent through a layer of categories, each observation''s features being a function of how many of its categories carry each feature, stay finite on finite data when a feature carried by none of an observation''s categories is always off; under that condition a category can switch features on and never off, so features depend on one another by sharing a category, or, where an observation has a single category, by excluding one another, and no feature or category suppresses another'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Active from NOTE-tmpn08ry. Proposition 1 and the bound (4) are
    the paper's, re-derived below. That the condition admits only
    positive dependence is drawn from the condition and from the paper's
    own future-work list; the argument, including the exclusion the DP-IBP
    produces, is set out below. That meets the
    condition for Active under ADR-047 v2.
tags:
- probabilistic-modeling
- mathematical-statistics
date: '2026-10-26'
source:
- LIT-tmplyhgz
summary: >-
  Doshi-Velez and Ghahramani (2009), LIT-tmplyhgz, read in NOTE-tmpn08ry.
  Z = f(CM) with f(0) = 0 gives correlated nonparametric feature models
  with O(log log N) expected features for the DP-IBP and IBP-IBP. The
  correlations are motifs, sets of features switched on together, plus,
  in the DP-IBP, exclusion between categories; suppression is outside
  them, and negative correlation is left as future work. The models' predictive
  advantage over the IBP is mixed in the paper's own table.
---

# THEORY-tmpwm0kx: Latent features made dependent through a layer of categories, each observation's features being a function of how many of its categories carry each feature, stay finite on finite data when a feature carried by none of an observation's categories is always off; under that condition a category can switch features on and never off, so features depend on one another by sharing a category, or, where an observation has a single category, by excluding one another, and no feature or category suppresses another

## Source

Doshi-Velez and Ghahramani (2009), UAI, PMLR R7: 143–150, arXiv:1205.2650,
LIT-tmplyhgz, read in full in NOTE-tmpn08ry; §2 (Proposition 1), §3 (the
DP-IBP, IBP-IBP and noisy-or models, and (4)) and §6, which names
"exploring methods to model negative correlations" as future work.

## What was actually shown

**Proposition 1.** C has finitely many active categories among N
observations almost surely, by the conditions on NP1, and those finitely
many categories carry finitely many features, by the conditions on NP2.
So the first N rows of CM have finitely many nonzero entries. If
f(cnᵀmk) = 0 whenever cnᵀmk = 0, every other entry of Z₁:N is zero, so
finitely many features are active. Re-derived as stated.

**Expected count.** In the DP-IBP, given N_C categories the feature count
is Poisson(αM H_{N_C}), so E[N_f] = αM E[H_{N_C}]. H is concave in its
argument, extended as log n + γ + o(1), so Jensen gives
E[N_f] ≤ αM log E[N_C] + O(1), and E[N_C] = O(αC log N) for a DP, hence
O(log log N). The IBP-IBP has N_C ~ Poisson(αC H_N), also O(log N), and the
same bound.

**On, never off.** Under the condition, for each observation n and
feature k, znk can be 1 only if some category of n carries k, and in all
three models P(znk = 1) does not decrease as more of n's categories carry
it (identity, "or", and 1 − q^{cnᵀmk}). A category's presence can raise
the probability of its features and never lower that of any feature. The
dependence that results is of two kinds.

- *Shared categories.* Two features carried by a common category tend to
  appear together: positive dependence, the paper's motifs.
- *Exclusive categories, DP-IBP only.* There each observation has exactly
  one category and Z = CM, so two features carried by disjoint sets of
  categories are never both present. That is a negative dependence, but
  it comes from competition between categories for the observation, not
  from one feature suppressing another. In the IBP-IBP and noisy-or
  models categories are drawn independently, and features with disjoint
  category sets are independent.

What none of the three can express is a feature, or a category, that
lowers the probability of another feature in observations that would
otherwise have it. The paper lists "exploring methods to model negative
correlations" as future work.

## What this does not say

- That inhibition is impossible in any finite nonparametric model. The
  condition is sufficient, not necessary; a link that switched off only
  features already switched on would keep the count finite. The paper
  does not try one.
- That correlated priors predict better. In its Table 2 the three
  variants beat the IBP in 9 of 15 comparisons and lose all three on the
  UN data.
- That a category is a real cause. The authors say the structures found
  "explain the data" and are not the "'true' or 'real' structure".
