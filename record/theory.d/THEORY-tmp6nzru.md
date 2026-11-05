---
status: Proposed
promote_when: >-
  An independent computation on origami patterns with mixed polygonal
  facets confirms that rigidity can be tuned by enforcing or relaxing the
  planarity of selected facets, and that the critical planarity density at
  which a pattern reaches its minimum degrees of freedom depends on the
  selection rule, the number of candidates sampled per step and the
  fraction of triangular facets as Li and Choi report.
title: 'Li and Choi show that the rigidity of general origami patterns can be tuned by enforcing or relaxing the planarity of selected facets, and that the critical density at which a pattern reaches its minimum number of degrees of freedom depends on the facet-selection rule, the number of candidates sampled per step and the fraction of triangular facets'
version: 1
tags:
- mathematics
- natural-sciences
date: '2026-11-05'
source:
- LIT-tmpiean9
summary: >-
  Li & Choi (2026), LIT-tmpiean9, read in NOTE-tmp52g52 (main text; the
  Supplementary Notes were not read). Proposed: one group's simulations
  on ten patterns. The n − 3 count is proved; the dependence of the
  critical density on rule, pool size and triangular-facet ratio is
  numerical, and the formula for it is fitted, not derived. Rigidity is
  infinitesimal at one folded configuration, and the "critical density"
  is a fixed-size statistic, not a thermodynamic threshold.
---

# THEORY-tmp6nzru: Li and Choi show that the rigidity of general origami patterns can be tuned by enforcing or relaxing the planarity of selected facets, and that the critical density at which a pattern reaches its minimum number of degrees of freedom depends on the facet-selection rule, the number of candidates sampled per step and the fraction of triangular facets

## Source

Li & Choi, "Rigidity control of general origami structures",
Communications Physics (2026), LIT-tmpiean9; read in NOTE-tmp52g52.

## What was actually shown

- **Control.** "the rigidity of a wide range of origami structures can be
  controlled by enforcing or relaxing the planarity condition of selected
  facets." (Abstract.)
- **Counting.** "The number of sub-planarity constraints required to
  control the planarity of an n-sided polygonal facet is exactly n − 3."
  (Methods, proved), so "imposing planarity on triangular facets does not
  reduce the global DOF".
- **What sets the transition.** In 100 runs for each k on each pattern,
  larger k narrows the transition; the Most and Least Efficient rules
  differ, "actively favoring a specific facet type is more difficult than
  simply avoiding it."; and "in all origami structures, the rigidity
  control is highly relevant to the presence of triangular facets."

## What this does not say

- That the formula for ρ* follows from theory. It is a tanh fit, with
  parameters fitted for each pattern and resolution.
- That the transition is a percolation threshold in the thermodynamic
  limit. It is the density at which half the runs on a fixed pattern reach
  minimum DoF.
- Anything about finite folding motions: rigidity is infinitesimal at a
  folding percentage of 25%.
