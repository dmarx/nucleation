---
status: Active
status_note: 'read in full 2026-10-17 (NOTE-tmp8kqax); worth reading as the source of the partial information decomposition the record already leans on through Williams and Beer (2011), Varley and Hoel, the ΦID review and the Shannon-invariants paper: the redundancy lattice of antichains, the Möbius inversion that turns any redundancy function into nonnegative-by-construction atoms once that function is monotone on the lattice, and the I_min redundancy measure. Read it knowing that the lattice and the inversion are general while every number is I_min''s, that I_min credits independent sources with redundancy whenever they reduce surprise about the same outcomes (Harder, Salge and Polani, LIT-tmpgtytt), and that it is an unrefereed arXiv preprint. Filed as THEORY-tmpeogx6.'
title: 'Nonnegative Decomposition of Multivariate Information'
version: 1
history:
- version: 1
  date: '2026-10-17'
  note: >-
    Filed at the owner's request as the source of I_min and of the
    partial information decomposition (PID) that Williams and Beer (2011,
    LIT-tmpsbhb4), Varley and Hoel (NOTE-020), the Shannon-invariants paper
    (NOTE-045) and the readings of transfer entropy depend on. An arXiv
    preprint only: Crossref finds no published version and OpenAlex lists
    only the arXiv DOI 10.48550/arxiv.1004.2515, both checked on
    2026-10-17. Not held in the Anthology of the SOTA: a grep of its
    record/ (clone of 2026-10-12, d1573d2) for the identifier, "Williams
    and Beer", "partial information decomposition" and I_min found
    nothing. Read in full the same day from arXiv 1004.2515v1 (14 April
    2010), 14 pp.: §§I–VI, Appendices A–D with the proofs followed step by
    step through Theorem 5, Appendix E's figures from captions.
tags:
- information-theory
- complex-systems
date: '2026-10-17'
published: '2010-04-14'
arxiv: '1004.2515'
first_author: 'Williams'
keywords:
- 'partial information decomposition'
- 'redundancy'
- 'synergy'
- 'interaction information'
- 'specific information'
- 'redundancy lattice'
- 'multivariate information'
implementations: []
summary: >-
  Williams & Beer (2010), arXiv preprint, [ARXIV-1004.2515](https://arxiv.org/abs/1004.2515). Defines redundancy as I_min(S; A₁…A_k) = Σ_s p(s) min_i I(S = s; A_i), the expected minimum specific information any source gives about each outcome. Restricted to antichains of sources and ordered by α ≼ β iff every source in β contains one in α, the collections form a redundancy lattice (18 nodes for three sources). The Möbius inverse of I_min on it gives partial-information atoms, proved nonnegative, that sum to I(S; R): for two sources, redundancy, two unique terms and synergy. Interaction information is shown to be synergy minus redundancy for three variables and a signed mixture of seven kinds of atom for four, which is why it can be negative and why it gives +1 bit both to 3-parity and to three copies.
compared_against:
- LIT-tmp5b2vz
corrected_by:
- LIT-tmpgtytt
extended_by:
- LIT-tmpgtytt
- LIT-tmpsbhb4
rivals:
- LIT-tmp5b2vz
---

# LIT-tmpmva6y: Nonnegative Decomposition of Multivariate Information

Paul L. Williams and Randall D. Beer (2010), "Nonnegative Decomposition of Multivariate Information", arXiv preprint — [ARXIV-1004.2515](https://arxiv.org/abs/1004.2515)

## Key takeaways

*From the reading, [NOTE-tmp8kqax](../notes.d/NOTE-tmp8kqax.md).*

- **I_min (Eq. 3).** Redundancy is the expected minimum, over sources, of
  the specific information I(S = s; A) = D_KL(p(a|s) ‖ p(a)) about each
  outcome s. It is nonnegative, at most each source's mutual information,
  and equal to it for one source.
- **The lattice (Eqs. 4–5).** Collections of sources with no source a
  superset of another (antichains), ordered by α ≼ β iff every B ∈ β
  contains some A ∈ α. There are 4 nodes for two sources, 18 for three,
  166 for four: the Dedekind numbers.
- **The atoms (Eqs. 6–8).** Π is the Möbius inverse of I_min on the
  lattice. Theorem 5 proves every atom nonnegative for I_min. The
  inversion itself works for any redundancy function; nonnegativity has to
  be shown for each.
- **Interaction information (Eqs. 14–15).** For three variables it is
  synergy minus redundancy. For four it is a signed sum of atoms, with one
  atom counted twice, so pure synergy (3-parity) and pure redundancy
  (three copies) both score +1 bit.
- **Scope.** No estimator, no data, no application. The lattice grows
  super-exponentially; for nine variables it has more than 5 × 10²² nodes.

## Standing in the record

Filed on 2026-10-17 because the record used its decomposition in at
least six documents without holding it, and read the same day. Filed as
[THEORY-tmpeogx6](../theory.d/THEORY-tmpeogx6.md). The lattice and the inversion are what
[THEORY-tmpt4nh7](../theory.d/THEORY-tmpt4nh7.md)'s two-term split and [THEORY-568](../theory.d/THEORY-568.md)'s redundancy-free
invariants rest on. I_min itself is what [THEORY-581](../theory.d/THEORY-581.md)'s numbers rest on.
Harder, Salge and Polani ([LIT-tmpgtytt](LIT-tmpgtytt.md)) show I_min gives 1 bit of
redundancy to two independent bits copied into the target. It carries no
instruction for machine-learning practice.
