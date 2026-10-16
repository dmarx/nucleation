---
status: Active
title: "For dynamics obeying detailed balance in a heat bath, the heat released in a transition between observer-defined macrostates is bounded below by the log-odds against its reversal less the internal entropy change; where a replicator's likeliest way back is a copy decaying within one generation, the bound grows with the copy's durability and the speed of copying, not with the information copied"
version: 1
tags:
- thermodynamics
- natural-sciences
date: '2026-10-16'
source:
- LIT-515
summary: >-
  England (2012; J. Chem. Phys. 2013), [LIT-515](../literature.d/LIT-515.md), read in [NOTE-419](../notes.d/NOTE-419.md). The general
  bound, β⟨ΔQ⟩ + ln π(II→I) + ΔS_int ≥ 0, is a coarse-grained second law and
  was re-derived. Applied to replication it gives a heat cost of about
  2n ln(n τ_decay/τ_div) per copy, which falls away as division slows. The
  numbers for E. coli (within a factor of three of the bound) and RNA rest
  on an upper bound on the reverse probability that is argued from biology,
  not proved, and on an internal-entropy term set "arbitrarily". It prices
  finite-time irreversibility, not information, and draws no line between
  living and non-living replicators.
presupposed_by:
- THEORY-tmp1lcfx
---

<!-- inactive-ok-file: THEORY-026 THEORY-030 THEORY-072 THEORY-tmp1lcfx THEORY-tmpbo41u — Proposed; named as accounts this bound is checked against or contrasted with, not leaned on -->

# THEORY-tmpy68ek: For dynamics obeying detailed balance in a heat bath, the heat released in a transition between observer-defined macrostates is bounded below by the log-odds against its reversal less the internal entropy change; where a replicator's likeliest way back is a copy decaying within one generation, the bound grows with the copy's durability and the speed of copying, not with the information copied

## Source

England (2012; *J. Chem. Phys.* 139:121923, 2013), [LIT-515](../literature.d/LIT-515.md), read in full in
[NOTE-419](../notes.d/NOTE-419.md) from arXiv v1, the only arXiv version. The published text was not
seen. [NOTE-419](../notes.d/NOTE-419.md) re-derived Eq. (6) and recomputed every numerical estimate.

## What was actually shown

**The general bound (Eq. 6).** Take stochastic dynamics in a heat bath with
detailed balance, π(j→i)/π(i→j) = exp(−βΔQ_{i→j}) (Eq. 2), and "by
stipulation" no external drive. Let I and II be ensembles fixed by an
observer's classification of microstates. Then β⟨ΔQ⟩ + ln π(II→I) +
ΔS_int ≥ 0. It follows from an exact average (Eq. 5) by Jensen's
inequality. Since π ≤ 1 it implies ⟨ΔS_tot⟩ ≥ 0, and the paper calls it
"simply a precise statement of the Second Law". [NOTE-419](../notes.d/NOTE-419.md) re-derived it and
finds it correct given the definitions.

**The replication bound (Eqs. 7–8).** The paper argues that the likeliest
way back from two cells to one is a daughter hydrolysing completely, which
gives ln π(II→I) ≤ 2 ln p_hyd (Eq. 7). With Poisson statistics for bond
hydrolysis, β⟨Q⟩ ≥ 2n_pep ln[(n_pep τ_hyd)/τ_div] − ΔS_int (Eq. 8). A
copy that lasts longer, or is made faster, must shed more heat.

**The estimates.**

- *E. coli.* With n_pep = 1.6×10⁹, τ_div = 20 min and τ_hyd = 600 years,
  the irreversibility term is about 75 n_pep ([NOTE-419](../notes.d/NOTE-419.md) recomputes 75.6).
  The measured heat is 220 n_pep (Rothbaum & Stone 1961), a ratio of about
  2.9: "less than three times as large as the absolute physical lower
  bound".
- *RNA and DNA.* For a ligase-type RNA replicator with a 1-hour doubling and
  a 4-year half-life the bound is printed as 7 kcal/mol, against a reaction
  enthalpy near 10. [NOTE-419](../notes.d/NOTE-419.md) recomputes 6.2–6.5 kcal/mol. The same speed in
  DNA would need about 16 kcal/mol (15.6–16.2 recomputed), more than the
  reaction releases.

**What could have come out otherwise.** The measured heat of E. coli could
have fallen below the bound. That would have refuted either the bound or
the argued reverse probability. It came out 2.9 times above. The RNA bound
could have exceeded the RNA reaction's enthalpy; it did not.

## What this does not say

- **That copying information has an intrinsic thermodynamic cost.** The
  heat priced is the irreversibility of making a durable copy in finite
  time. The term ln(τ_hyd/τ_div) falls away as τ_div grows, as a reversible
  copying limit requires ([NOTE-419](../notes.d/NOTE-419.md)).
- **That the E. coli figure is a measurement of efficiency.** The reverse
  probability in Eq. (7) comes from an argument about which path back
  dominates, not a bound proved over all paths. The internal-entropy term,
  −ΔS_int ≤ 10 n_pep, is set "arbitrarily" and "generous[ly]". So the
  factor of three could reflect adaptability, as the author suggests, or
  the looseness of the reverse probability.
- **That it holds for driven systems.** The text says the same form holds
  for time-symmetric driving, by Crooks's relation, but does not derive it
  here.
- **That RNA came before DNA.** That rests on one comparison with assumed
  enthalpies and half-lives (C5 in [NOTE-419](../notes.d/NOTE-419.md), weak).
- **Where a living replicator ends.** "Self-replication is something that
  happens relative to an observer." The bound works for any coarse-graining
  with a reliable population model. It supplies no physical mark of a
  living replicator, and that framing is an assertion, not a result (C6).
- **A cost per operation.** Like the other second-law bounds in the record,
  it is a bound on averages.

## Connections

- **Landauer's scope ([THEORY-030](THEORY-030.md)).** The paper calls its bound "closely
  related to the well-known Landauer bound". On [THEORY-030](THEORY-030.md)'s reading,
  copying onto a blank register has no minimum cost. England's bound is
  consistent with that, because what it prices vanishes in the slow limit.
  Reading England as evidence for a per-bit cost of replication is the
  mistake [THEORY-030](THEORY-030.md)'s "What this does not say" warns against.
- **[THEORY-026](THEORY-026.md).** No direct bearing: England's system is undriven and has
  no memory variable.
- **The fluctuation theorems ([THEORY-tmp3uu1d](THEORY-tmp3uu1d.md))** are the family this bound
  belongs to; its driven case leans on Crooks ([LIT-522](../literature.d/LIT-522.md)).
- **Dissipative adaptation ([THEORY-tmp1lcfx](THEORY-tmp1lcfx.md))**, the sequel, [LIT-518](../literature.d/LIT-518.md),
  takes this macrostate relation, adds a drive and drops replication.
- **Metabolism first ([THEORY-tmpbo41u](THEORY-tmpbo41u.md)).** Morowitz and Smith put selection
  on metabolism before replication. England's comparison concerns which
  replicator is thermodynamically possible, not whether replication came
  first, so the two do not meet head on.
- **The demarcation question.** Nahas and Sachs's dispute ([LIT-192](../literature.d/LIT-192.md),
  [NOTE-094](../notes.d/NOTE-094.md)) is over whether living systems can be told apart from
  dissipative structures. This paper takes the deflationary side by
  locating the "self" in the observer's coarse-graining. [THEORY-072](THEORY-072.md) is the
  record's account of where the line falls.
