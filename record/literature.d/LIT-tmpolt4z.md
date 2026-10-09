---
status: Active
status_note: 'read 2026-10-09 ([NOTE-tmpavdpk](../notes.d/NOTE-tmpavdpk.md)); worth reading as a whole-network test of whether transcriptional regulation alone can make a bacterium''s state history-dependent. In an ensemble of sign-consistent Boolean rules on the 87-gene core of the largest E. coli regulatory subnetwork (RegulonDB), 51 genes admit a transient knockout or overexpression that leaves the network in a different attractor; every such gene reaches a strongly connected component containing a positive circuit, and the probability grows roughly as a power of the weighted number of paths to one. Model only: the paper runs no transient-perturbation experiment. Its one comparison with data, against strains evolved after a permanent crp knockout, mostly tests the sign structure of the network, and its link to irreversibility is weak (P = 0.03 on small counts).'
title: 'Irreversibility in bacterial regulatory networks'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read on 2026-10-09 (NOTE-tmpavdpk): main text, Materials and
    Methods and the Supplementary Text in full, from the CC BY
    version of record at PubMed Central (PMC11352831) and the arXiv
    copy (2409.04513v1, which carries the supplement). Details checked
    against Crossref (Science Advances 10(35):eado3232; authors Yi
    Zhao, Thomas P. Wytock, Kimberly A. Reynolds, Adilson E. Motter)
    and the arXiv record (submitted 6 September 2024, journal
    reference given). `published:` is 28 August 2024, the publisher's
    own date of online publication, carried in Crossref's publication
    history and by PubMed Central; Crossref's issued and print date is
    the 30 August issue date, and the arXiv copy was posted after the
    journal, so it is not the first appearance. Not held in the
    Anthology of the SOTA: a grep of its record/ for the authors, the
    DOI, the arXiv id and the title found nothing, but that clone is at
    commit d8b5ba5 and may be stale.
tags:
- complex-systems
- network-science
- natural-sciences
date: '2026-10-09'
published: '2024-08-28'
arxiv: '2409.04513'
doi: '10.1126/sciadv.ado3232'
first_author: 'Zhao'
keywords:
- 'irreversibility'
- 'gene regulatory network'
- 'Boolean network'
- 'positive circuits'
- 'multistability'
- 'Escherichia coli'
- 'transient perturbation'
- 'adaptive evolution'
implementations:
- 'https://github.com/yizhao-nu/Irreversiblility-in-GRN'
summary: >-
  Zhao, Wytock, Reynolds and Motter (2024), Science Advances
  10(35):eado3232. In Boolean models of the E. coli transcriptional
  regulatory network, a transient single-gene knockout or overexpression
  often moves the network to a different attractor, so one genotype can
  hold several heritable expression states without epigenetic marks. The
  genes able to do this are those upstream of, or inside, strongly
  connected components with positive circuits, and the more weighted
  paths to them the likelier. A prediction from a model ensemble, with no
  direct experiment.
---

<!-- inactive-ok-file: THEORY-tmpcasth — Proposed; the finding this reading produces, filed with it -->

# LIT-tmpolt4z: Irreversibility in bacterial regulatory networks

Yi Zhao, Thomas P. Wytock, Kimberly A. Reynolds and Adilson E. Motter
(2024), *Science Advances* 10(35):eado3232 — DOI-10.1126/sciadv.ado3232,
[ARXIV-2409.04513](https://arxiv.org/abs/2409.04513)

## Key takeaways

- **What "irreversible" means here.** A transient perturbation is
  irreversible when switching one gene off (knockout) or on
  (overexpression) until the network settles, then releasing it, leaves the
  network in a different attractor from the one it started in. In a
  deterministic model this is permanent by construction; the authors say
  noise and the cell cycle would make it long-lived rather than permanent.
- **The model.** RegulonDB's network (1859 genes, 5119 signed edges, 148
  dual or unknown edges dropped) is cut to its largest origon, rooted at
  phoB (1406 genes), and trimmed to a core of 87 genes and 290 edges. No
  gene outside the core can cause irreversibility. The rules are not
  known, so the paper samples sign-consistent, nested canalizing Boolean
  rules (about 10^61 are possible), with two parameters, nestedness r and
  bias s, and two input orderings ("concentrated" and "diffuse" control).
  Updates are synchronous.
- **The structural result.** 51 of the 87 core genes admit an
  irreversible perturbation for some rules. The other 36 cannot: 32 are
  leaves and 4 feed only autorepressive leaves. Every gene that can
  influence a positive circuit (a cycle with an even number of
  repressions) is irreversible for some rules. A path-weight count K_u of
  routes to strongly connected components containing positive circuits
  accounts for 55–62% of the variance in irreversibility probability
  (p̂_u = aK_u^b, b = 0.68 ± 0.09 diffuse, 0.93 ± 0.14 concentrated).
- **Which way the transitions go.** Weighted by basin size, the rate of
  irreversibility roughly halves, and the initial attractors' basins
  average about one-eighth of the final ones': transient perturbations
  tend to move the network from small basins to large ones.
- **crp knockout is the most irreversible perturbation**, with 68
  irreversible response genes. Against RNA-seq of strains evolved for 10
  days after a permanent crp knockout, the sign predicted by the shortest
  signed path from crp matches the observed change for 10 of 11
  strongly changed genes in batch and 33 of 42 in chemostat (average
  precision 0.99 and 0.85, P < 0.01). Among strongly changed genes, the
  irreversible responders matched the predicted sign 8 of 9 times and the
  reversible ones 2 of 2 in batch, 28 of 34 against 5 of 8 in chemostat;
  P = 0.03 for the two conditions together.
- **A testable prediction.** Transient crp knockdown by inducible CRISPR
  interference should leave self-activating, crp-activated genes (zraR,
  melR, rhaRS) switched on, in growth conditions chosen to put them in a
  bistable range. A Hill-function model says stronger self-activation and
  steeper responses favour it.

## Standing in the record

Filed on 2026-10-09 at the owner's request, with no stated context, and
read on its own merits the same day ([NOTE-tmpavdpk](../notes.d/NOTE-tmpavdpk.md)).

The record's standard for evidence of alternative stable states is
[THEORY-136](../theory.d/THEORY-136.md): only hysteresis, dependence on the initial state, or a lasting
shift after a temporary disturbance, with slow return excluded, comes close.
This paper defines irreversibility as the third of these and predicts it
across a whole regulatory network, but shows it only in models. The finding
is filed as [THEORY-tmpcasth](../theory.d/THEORY-tmpcasth.md), Proposed until an experiment of that kind is
read.
