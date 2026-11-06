---
status: Open
title: "Does an independent simulation, or a rerun of the released code on the authors' data, reproduce the Markov preparedness policy's lower mean allocation cost against nine published ambulance dispatch policies in most simulated Rio de Janeiro configurations?"
version: 1
tags:
- operations-research
- probabilistic-modeling
date: '2026-11-06'
line:
- readiness
summary: >-
  Moved from THEORY-1412's promotion condition at the thirtieth status
  review (ADR-065). Guigues, Kleywegt and Nascimento (LIT-2066) report
  that their policy had the lowest mean allocation cost in most of their
  simulated configurations; read from their figures, at 38 of 46 fleet
  sizes. They report no dispersion, assume the costs, and implement the
  comparators themselves. They state that code and data are on GitHub
  and Zenodo. An answer is a rerun or an independent simulation that
  reports the comparison with its variability.
---

# QUESTION-tmpfh08i: Does an independent simulation, or a rerun of the released code on the authors' data, reproduce the Markov preparedness policy's lower mean allocation cost against nine published ambulance dispatch policies in most simulated Rio de Janeiro configurations?

## Why it is a question

One study, an unrefereed preprint, scored every policy on the allocation
cost that the proposed policy optimizes, with costs the authors call
examples, and reported no replication counts or intervals (THEORY-1412,
NOTE-1567). The promotion condition THEORY-1412 carried until the
thirtieth status review read: "An independent simulation, or the
authors' released code rerun on their data, reproduces lower mean
allocation cost for the Markov preparedness policy than for the nine
comparators in most of the configurations the paper reports."

A rerun of the released code (§6 of the paper: GitHub
vguigues/Heuristics_Dynamic_Ambulance_Management, directory esma2;
Zenodo DOI 10.5281/zenodo.18487224) would settle whether the figures
reproduce. An independent implementation, or another city's data, would
say more.
