---
status: Proposed
promote_when: >-
  A documented REST2 run on one disordered-protein construct in which swap
  acceptance and round-trip times meet the usual targets while the
  demultiplexed replicas disagree in their structural distributions (radius
  of gyration, helicity, contacts) beyond blocking errors, set against a
  reference ensemble from independent or much longer sampling. The account
  is promoted if such cases occur and the demultiplexed comparison is what
  catches them. It loses its point if, across constructs, the two
  diagnostics never disagree. Another run that passes both checks, as the
  chapter's worked example does, cannot settle it.
title: "In REST2 replica-exchange simulations of intrinsically disordered proteins, high swap acceptance and short round trips show that replicas mix along the temperature ladder, not that conformations are sampled, because the upper rungs collapse the chain; sampling shows only when independent demultiplexed replicas agree in their structural distributions"
version: 1
tags:
- natural-sciences
- probabilistic-modeling
date: '2026-10-16'
source:
- LIT-076
summary: >-
  Koneru, Reid & Robustelli (2025), [LIT-076](../literature.d/LIT-076.md), read in full in [NOTE-076](../notes.d/NOTE-076.md). A
  how-to chapter whose one load-bearing methodological point is that high
  swap acceptance "is not, in isolation, sufficient evidence of robust
  conformational sampling or convergence" (p. 18). The reason the reading
  draws out is that REST2's upper rungs are unphysical Hamiltonians on which
  disordered chains over-collapse, so replicas can swap freely without the
  chain rearranging. The chapter argues this and shows a passing example; it
  shows no failed run, and its convergence criteria have no quantitative
  threshold.
---

# THEORY-tmpk3gv0: In REST2 replica-exchange simulations of intrinsically disordered proteins, high swap acceptance and short round trips show that replicas mix along the temperature ladder, not that conformations are sampled, because the upper rungs collapse the chain; sampling shows only when independent demultiplexed replicas agree in their structural distributions

## Source

Koneru, Reid & Robustelli (2025), [LIT-076](../literature.d/LIT-076.md) (arXiv 2505.01860, written as a
book chapter), read in full in [NOTE-076](../notes.d/NOTE-076.md), with a spot-check of the
accompanying repository.

## What was actually shown

**Why few replicas suffice (Eq. 8).** In REST2 only the solute's own
energy and the solute–solvent energy enter the swap criterion. The
water–water energy drops out, so a few replicas span a wide range of
effective solute temperature. This is the standard result of Wang, Friesner
& Berne (2011), and [NOTE-076](../notes.d/NOTE-076.md) rates it strong.

**The price.** The upper rungs are scaled Hamiltonians, not physical
temperatures. Disordered proteins over-collapse there: higher effective
solute temperature gives more compact states, more contacts and less
secondary structure in the chapter's own example (Fig. 3). The over-collapse
is cited to refs. 23–24; the chapter shows only the qualitative trend.

**The diagnostic split (pp. 17–18, Figs. 2–4).** The chapter separates two
kinds of check. Per demultiplexed replica it reports the fraction of time at
the base rung, the mean effective temperature and the round-trip time. Those
measure movement along the ladder. Across demultiplexed replicas it compares
structural distributions with Flyvbjerg–Petersen blocking errors. Its
verdict: "Obtaining high acceptance rates on swap attempts is not, in
isolation, sufficient evidence of robust conformational sampling or
convergence. It is therefore essential to compare the distributions of
conformations sampled in each demultiplexed replica" (p. 18).

**Where it bites.** Ensembles from 1–10 µs per replica "will usually retain
some starting-structure dependence" (p. 10). For chains over about 40
residues some demultiplexed replicas "will occasionally become stuck".

**The example.** The α-synuclein C-terminal 20-mer (residues 121–140), with
a99SB-disp, 10 replicas from 300 to 450 K, swaps every 1.6 ps and a target
of at least about 20% acceptance. The chapter states no numerical outcome
for it.

**What could have come out otherwise.** Nothing in the chapter could. It
shows a run that passes both checks and no run that passes one and fails
the other.

## What this does not say

- **That acceptance is useless.** It is necessary for mixing. The claim is
  that it is not sufficient for sampling.
- **How much agreement is enough.** The criterion, agreement "within
  statistical sampling errors", is a visual comparison with no threshold.
  [NOTE-076](../notes.d/NOTE-076.md) lists a quantitative test as an open question.
- **That REST3 or REHT fix the collapse.** The chapter names them as
  remedies and compares nothing.
- **That the point transfers to tempered MCMC in general.** [NOTE-076](../notes.d/NOTE-076.md) notes
  that the logic would carry over to parallel tempering anywhere, but that
  is its own informal argument. The chapter does not make the link.
- **That the chapter's other claims hold.** Its statement that tREMD's
  replica count "scales exponentially with the degrees of freedom" is
  misstated ([NOTE-076](../notes.d/NOTE-076.md), C2), and its printed sequence is not the simulated
  construct. The repository is authoritative for the example.

## Connections

- The chapter's force field is the authors' own (Robustelli et al. 2018).
  It is the kind of protocol from which reference ensembles for machine-
  learned ensemble generators are made, which is the only bearing [NOTE-076](../notes.d/NOTE-076.md)
  finds on ML. That bearing carries no instruction, so nothing here is for
  the anthology.
- No other THEORY in the record treats sampling convergence.
