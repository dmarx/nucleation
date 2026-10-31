---
number: 1248
status: Active
formerly:
- THEORY-tmp05y8u
title: 'Catalysts cancel out of the stoichiometric matrix, so a cycle of mutual catalytic production among species is not a stoichiometric cycle: the cycles that carry a reaction network''s steady currents and affinities are fuel-to-waste pathways through it, and who catalyses whom enters only the rates, never the thermodynamic driving'
version: 1
tags:
- thermodynamics
- complex-systems
date: '2026-10-31'
source:
- LIT-1897
- LIT-1889
summary: >-
  From the definitions of Dal Cengio, Lecomte and Polettini (2023),
  [LIT-1897](../literature.d/LIT-1897.md) ([NOTE-1476](../notes.d/NOTE-1476.md)), and Rao and Esposito (2016),
  [LIT-1889](../literature.d/LIT-1889.md) ([NOTE-1464](../notes.d/NOTE-1464.md)), neither of which says it in these words.
  It makes exact A13's "a productive cycle need not be a stoichiometric
  cycle" from the exchange "Analyze nucleation concepts". Checked on a
  reversible rewriting of [CASE-189](../cases.d/CASE-189.md)'s first construction. Active:
  definitional and checked. It does not say that catalytic cycles are
  thermodynamically idle. They decide which of the states the driving
  allows is reached, and bistability needs them; but the budget they
  work within is set elsewhere.
---

# THEORY-1248: Catalysts cancel out of the stoichiometric matrix, so a cycle of mutual catalytic production among species is not a stoichiometric cycle: the cycles that carry a reaction network's steady currents and affinities are fuel-to-waste pathways through it, and who catalyses whom enters only the rates, never the thermodynamic driving

## Source

Dal Cengio, Lecomte and Polettini (2023), [LIT-1897](../literature.d/LIT-1897.md): the stoichiometric
matrix of net changes S_ρ = ν^{−ρ} − ν^{+ρ} (eq. 5), cycles as ker S (§III A),
the cycle affinity as the circulation c_α · A, independent of concentrations
(eq. 30), and Gordan's alternative (footnote 6); read in [NOTE-1476](../notes.d/NOTE-1476.md). Rao
and Esposito (2016), [LIT-1889](../literature.d/LIT-1889.md): ∇ = ∇⁻ − ∇⁺ (eq. 2), emergent cycles
(eq. 20), local detailed balance (eq. 50); read in [NOTE-1464](../notes.d/NOTE-1464.md).

## What was actually shown

**The algebra.** A species that is both a reactant and a product of a
reaction, X + C ⇌ Y + C, has net stoichiometric coefficient zero. It appears
in the rates, J⁺ = k⁺[X][C] and J⁻ = k⁻[Y][C], and not in S. Local detailed
balance fixes k⁺/k⁻ by the free energies of X and Y alone, so the catalyst
also drops out of the affinity, A = RT ln(J⁺/J⁻). Cycles are vectors in ker S
and their affinities are circulations of A. Both are therefore blind to
catalysis. The mutual production of two species, each catalysing the other's
synthesis, is a cycle in the graph of catalytic influence, in the rates'
exponents. It is not a vector in ker S.

**The check.** For c₂ catalysing S → c₁ and c₁ catalysing S → c₂, each
decaying to W, with S and W chemostatted, the internal matrix has kernel
spanned by (1, 0, 1, 0) and (0, 1, 0, 1). These are the emergent cycles
fuel → c₁ → waste and fuel → c₂ → waste. The closed network's only cycle,
(−1, 1, −1, 1), is a futile loop with zero affinity. The production cycle
c₁ → c₂ → c₁ is none of these. Net production of both capacities from the
reservoirs, S_X (1, 1, 0, 0)ᵀ = (1, 1) > 0, is Gordan's case (ii), which an
open network can have and a closed one cannot (footnote 6).

**What could have failed.** A catalyst could have entered the net
stoichiometry, or the affinity could have depended on it. It enters neither.

## What this does not say

- **That catalytic cycles do nothing thermodynamically.** They shape the
  rates, and so they decide where in the space the driving allows the
  network sits ([THEORY-1261](THEORY-1261.md)) and whether it is multistable. In the check
  above, deleting either catalysed reaction, or making it uncatalysed,
  leaves a single fixed point. But the
  affinity available, and the cost of the steady state, are set by the
  fuel-to-waste cycles alone ([THEORY-1266](THEORY-1266.md)).
- **That production cycles and stoichiometric cycles never coincide.**
  Stoichiometric autocatalysis, X + S ⇌ 2X, puts the producer in the net
  stoichiometry. A cycle of such reactions does change S, and Dal Cengio et
  al. note that "chemostatted autocatalytic reactions fall in case (ii)".
  The claim is that a cycle of *catalytic* production, the form the
  record's constraint models take, has no stoichiometric counterpart.
- **Anything about sheaf kernels**, the third kind of cycle A13 separated.
- **That closure of constraints ([TERM-070](../terms.d/TERM-070.md)) is thermodynamically invisible
  in every sense.** It is invisible to the budget. Whether a closed set of
  constraints lowers the driving needed to sustain a state is a kinetic
  question this does not touch.
