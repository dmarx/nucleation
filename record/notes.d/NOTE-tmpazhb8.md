---
status: Read
paper: 'LIT-tmpge2xj'
title: 'Chen, Choi & Mahadevan — Deterministic and stochastic control of kirigami topology'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Read on 2026-11-05 from arXiv 1910.07090v2 (2 March 2020), PDF,
    https://arxiv.org/pdf/1910.07090v2, extracted by pdftotext; its journal
    reference is PNAS 117(9), 4511–4517. Not the version of record: Europe
    PMC's full-text XML for PMC7060672 returned HTTP 500, NCBI efetch said
    the publisher does not allow full-text XML download, and the PMC HTML
    page was not tried. The v2 wording may differ from the published text;
    quotes below are from v2. Read in full: the abstract, introduction and
    model, the sections on kirigami with prescribed cuts (minimum
    rigidifying and connecting link patterns, enumeration) and with random
    cuts (connectivity percolation, DoF, redundancy, combining the two
    approaches), and the Discussion. Not read: the SI Appendix, with the
    proofs of Theorems S1–S3, the kagome case and the dual-lattice details.
    Theorem 1, and two passages broken in the extraction by typeset
    formulae, were checked by eye; the quotes below are fragments that
    match the extracted text.
date: '2026-11-05'
summary: >-
  Quad kirigami as a linkage. Exact minimum link counts: δ(L) =
  ⌈(3L²−3)/2⌉ to rigidify an L × L sheet, γ(L) = L² − 1 to connect it,
  proved by construction, so rigidifying always needs more links and no
  pattern is minimal for both; random choice almost never finds either.
  With random links, the maximum of internal DoF (ρ_i ≈ 0.26), connectivity
  percolation (ρ_c ≈ 0.293, 1 − 1/√2 analytically) and a rigidity
  transition (ρ_r ≈ 0.429) fall in that order; each link changes the total
  DoF, changes the internal DoF, or is redundant. Planar, infinitesimal
  rigidity, no experiments.
---
<!-- inactive-ok-file: THEORY-tmp278tq CLAIM-354 THEORY-302 — Proposed or new; cited from the reading of Chen, Choi & Mahadevan (2020) as open -->

# NOTE-tmpazhb8: Chen, Choi & Mahadevan — Deterministic and stochastic control of kirigami topology

## Contribution

- An exact count of the minimum links needed to rigidify (a minimum
  rigidifying link pattern, MRP) and to connect (a minimum connecting link
  pattern, MCP) a quad kirigami sheet of any size, with constructive
  proofs.
- For links placed at random, three thresholds that fall in a fixed order,
  and a classification of each added link into one of four kinds.
- A combination of the two approaches, starting from an MRP or MCP and
  adding or removing links at random, which reaches more combinations of
  DoF and number of connected components.

## Key insight

Choosing cuts is choosing constraints. Each of the 4L(L−1) possible links
pins two corners of neighbouring quads together, and the sheet's
infinitesimal DoF is 8L² − rank(A) for the rigidity matrix A. Counting and
placing links then answers both the topological question (how many pieces)
and the mechanical one (how many motions), and the two answers come apart:
connecting is cheaper than rigidifying, and connecting creates internal
mechanisms before further links remove them.

## Assumptions

- Cuts only on an equally spaced square grid; hinges of infinitesimal
  width.
- Rigid quads rotating freely about corner hinges at no energy cost.
- A planar sheet, with infinitesimal rigidity from the rank of the
  rigidity matrix, not finite motions.
- In the random case, independent and equally likely links; thresholds
  from simulations up to L = 100.

## Key results

- **Abstract.** "both the number of connected pieces and the degrees of
  freedom show percolation transitions as a function of the density of
  cuts (links)."
- **Minimal counts (Theorems 1 and 2).** δ(L) = ⌈(3L²−3)/2⌉, checked by eye
  since the PDF typesets it; "For all positive integer L, γ(L) = L2 − 1."
  Hence: "This implies that there is no MRP which is also an MCP for L ≥ 2.
  It also suggests that in general rigidifying a kirigami requires more
  effort (links) compared to connecting the quads in kirigami."
- **Enumeration.** "there are much more MCPs than MRPs, suggesting that it
  is much easier to connect a kirigami than to rigidify a kirigami." For
  large L it is "almost impossible to" "obtain an MRP (or MCP) by randomly
  picking" the minimum number of links.
- **Why random links.** Microscopic control of each link is "difficult to
  achieve".
- **Internal modes.** "the number of internal DoF must be non-monotonic as
  links are added", with its maximum at ρ_i ≈ 0.26.
- **Redundancy.** "when links are added to the system, they do one of three
  things: change the total DoF, change the internal DoF, or simply be
  redundant." After rigidity percolation most added links are redundant.
- **Thresholds (Discussion).** "We find three critical thresholds: the
  density for maximum internal DoF (ρi ), for connectivity percolation
  (ρc ), and for rigidity percolation (ρr ), with ρi < ρc < ρr";
  ρ_c ≈ 0.293 (1 − 1/√2 analytically, 0.298 numerically) and ρ_r ≈ 0.429.
- **A caution on words.** The paper's "rigidity" "represents the DoF (or
  number of floppy modes) introduced above, which is different from the"
  "“rigidity percolation” transition that describes a global change in the
  network".

## Concepts

- **Link**: a constraint forcing two corners of neighbouring quads to
  coincide; links and uncut hinge segments correspond one to one.
- **MRP / MCP**: a set of δ(L) links leaving only rigid-body motion; a set
  of γ(L) links leaving one connected component.
- **Internal and rigid-body modes**: m_int = m_tot − 3T, T the number of
  connected components.
- **Redundant link**: one that leaves the DoF unchanged. The four classes
  of link, by change in internal and rigid-body DoF, are
  (Δ_i, Δ_r) ∈ {(−2,0), (−1,0), (0,0), (+1,−3)}.

## Connections

It extends the rigidity-matrix counting of Maxwell and of generic rigidity
percolation to a designed linkage, and continues Chen and Mahadevan's work
on rigidity control by planarity in Miura-ori. Li and Choi (2026),
LIT-tmpiean9, cite it as their ref. 39 and carry the method to origami
with general polygonal facets.

## Bearing on the record

- **The pasted synthesis on constraint architectures.** It cites this as
  O7 by title only. Its quoted sentences, "deterministic constructions and
  statistical models in which cuts and remaining connections govern the
  number of connected components and degrees of freedom. It identifies
  percolation-like transitions.", are A's paraphrase, not the paper's
  words, and right in substance. "Percolation-like" is fair: connectivity
  percolation is exact on the dual lattice, while the rigidity transition
  is a peak of a second derivative, compared only qualitatively with
  generic 2D rigidity percolation. A misses the exact minima and the strict
  gap between rigidifying and connecting, the ordering ρ_i < ρ_c < ρ_r, the
  non-monotonic internal DoF, and the authors' warning about their word
  "rigidity".
- **A's question on coupling rigid subsystems.** The pasted synthesis asks
  under what conditions coupling two locally rigid subsystems creates new
  degrees of freedom at their interface. Here the answer is exact, for
  this linkage: a link that joins two components removes three rigid-body
  DoF and adds one internal DoF, (Δ_i, Δ_r) = (+1, −3).
- **CLAIM-480 (composing interactions can turn an interior into a
  constraint, and sometimes into one of a new kind).** Supports, by a
  physical case: composition removes external freedoms and creates a new
  internal one where the parts meet.
- **CLAIM-345 (equal controllability rank does not fix the cost of
  control).** Related, as an analogue for structure rather than control
  cost: equal link counts give very different DoF depending on placement,
  and almost no random choice of δ(L) links rigidifies the sheet.
- **CLAIM-354 (freedom comes in degrees along several dimensions).**
  Related: total, internal and rigid-body DoF, and connectivity, are
  separate counts that move differently as links are added.
- **CLAIM-347 and TERM-060.** Unrelated: there is no conflict among demands
  here, only redundancy of constraints. THEORY-302 is unrelated in content.
  QUESTION-218 is distantly related through internal against rigid-body
  modes.
- The record holds no entry on percolation. Filed: THEORY-tmp278tq. No
  instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **The authors'.** Planar quad kirigami only (kagome in the SI);
  infinitesimal rigidity; microscopic control of links is hard to achieve.
- **A numerical threshold.** ρ_r is a peak of the second derivative of the
  DoF, and the argument offered for it is heuristic.
- **No experiments** on physical sheets.
- **Not the version of record.** Read from arXiv v2; the SI, with the
  proofs, was not read.
