---
status: Active
status_note: 'read 2026-10-09 ([NOTE-tmpbm8lu](../notes.d/NOTE-tmpbm8lu.md)); worth reading as the theorem the real-space mutual-information programme ([LIT-873](LIT-873.md), [LIT-881](LIT-881.md), [LIT-878](LIT-878.md)) cites for its claim that the optimal coarse-graining picks out the most relevant operators. What it proves is narrower than that claim: for a short-range lattice model on a cylinder, with the block and the environment taken as whole slabs of the cylinder separated by a buffer, the information-bottleneck encoder just past its first transition depends on the block only through the boundary weak value of the leading transfer-matrix eigenvector, and the transition sits at β_c = (λ0/λ1)^(2L_B); for large circumference that eigenvector is the lowest-dimension primary. The planar block-in-a-shell geometry the algorithms use, the fixed-alphabet β → ∞ limit that is RSMI, and the regime beyond the first transition are not covered. A second result: past the first transition, with a large enough alphabet and no fine-tuning, the optimal encoder carries a representation of the data''s symmetry, and a two-symbol example with Z4 symmetry breaks it.'
title: 'Relevance in the Renormalization Group and in Information Theory'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Filed at the owner's request on 2026-10-09, as one of the works cited
    by the batch on hierarchy and hyperbolic geometry and its cited works
    (nucleation#113 and #114) that neither record held; the citing work
    is Gökmen, Ringel, Huber and Koch-Janusz 2021 (LIT-878), which relies
    on this paper's theorem without proving it. Read in full the same day
    (NOTE-tmpbm8lu) from the arXiv PDF of v1 (arXiv:2012.01447v1, 2
    December 2020, 16 pp.: main text pp. 1–4, references pp. 5–6,
    Appendices A–F pp. 6–16), text extracted with pdftotext. arXiv lists
    no later version, so the text read is the preprint as first posted,
    six and a half months before publication; the published text was not
    read, and differences cannot be ruled out. The publisher's page and
    the open-access PDF link OpenAlex gives (link.aps.org) both returned
    HTTP 403. Checked against the arXiv abstract record (v1 only,
    submitted 2 December 2020; primary class cond-mat.stat-mech; four
    authors; journal reference Phys. Rev. Lett. 126, 240601 (2021) and
    DOI 10.1103/PhysRevLett.126.240601), against the PDF's first page
    (same title and authors), and against Crossref for that DOI (Physical
    Review Letters 126(24), article 240601, published online and issued
    17 June 2021; Amit Gordon, Aditya Banerjee, Maciej Koch-Janusz, Zohar
    Ringel). The identification the owner gave is correct. `published:`
    is the arXiv v1 date, 2 December 2020, the earliest any source gives
    (ADR-002). Not held in nucleation before this filing: a grep of
    record/ for the arXiv id, the DOI, the title and "Gordon" found only
    LIT-878 and NOTE-681 naming it as not held (other hits are unrelated
    Gordons). Not held in the Anthology of the SOTA as far as its clone
    shows: a grep of its record/ (clone at commit d8b5ba5, 9 October 2026,
    possibly stale) for the arXiv id, the title and the authors found
    nothing. Not flagged `anthology-candidate`, for the reason given for
    LIT-881: it trains nothing and makes no claim about learning; its
    results are an exact reduction and a perturbative solution of the
    information-bottleneck equations for lattice models, checked by an
    iterative solver on a three-site cylinder.
tags:
- natural-sciences
- information-theory
- representation-learning
date: '2026-10-09'
published: '2020-12-02'
arxiv: '2012.01447'
doi: '10.1103/PhysRevLett.126.240601'
first_author: 'Gordon'
keywords:
- 'information bottleneck'
- 'renormalization group'
- 'relevance'
- 'scaling operators'
- 'transfer matrix'
- 'conformal field theory'
- 'real-space mutual information'
- 'symmetry'
implementations: []
extends:
- LIT-873
summary: >-
  Gordon, Banerjee, Koch-Janusz and Ringel (2020; Phys. Rev. Lett. 126,
  240601, 2021). On a cylinder, with block and environment as slabs
  separated by a buffer of length L_B, the information-bottleneck encoder
  just past its first transition depends on the block only through the
  boundary weak value of the leading transfer-matrix eigenvector, the
  lowest-dimension primary at large circumference, and the transition is
  at β_c = (λ0/λ1)^(2L_B). Checked on a three-site critical Ising
  cylinder. With a large enough alphabet the encoder respects the data's
  symmetry near that transition; a small one can break it.
---
<!-- inactive-ok-file: THEORY-194 THEORY-198 THEORY-tmpne099 QUESTION-025 CLAIM-092 — Proposed or open; cited as the accounts this reading underpins or is set beside, the account it produced, and the question and claim it does not answer -->

# LIT-tmp6shyv: Relevance in the Renormalization Group and in Information Theory

Amit Gordon, Aditya Banerjee, Maciej Koch-Janusz and Zohar Ringel (2020),
*Physical Review Letters* 126(24):240601 (2021) — [ARXIV-2012.01447](https://arxiv.org/abs/2012.01447),
DOI-10.1103/PhysRevLett.126.240601

## Key takeaways

- **The theorem, in its geometry.** A short-range lattice model on an
  infinite cylinder of circumference L; the block V and the environment E
  are whole slabs of the cylinder, separated along its axis by a buffer of
  L_B slices. Through the transfer matrix T, the joint law reduces to
  P(v|e) = P(v)[1 + ε r_v r_e] up to terms of order (λ2/λ0)^(L_B), with
  ε = (λ1/λ0)^(L_B) and r_v = ⟨1|∂V_R⟩/⟨0|∂V_R⟩ the weak value of the
  leading excited eigenvector on V's boundary slice facing E. The
  information-bottleneck (IB) encoder then satisfies
  P(h|v) ∝ P(h) exp(β ε² r_v ⟨r_v⟩_h): it sees V only through r_v.
- **The first transition, in closed form.** The trivial encoder loses
  stability at β_c⁻¹ = ε², and just above, for a binary H,
  P(h|v) = e^(h m r_v)/2cosh(m r_v) with m growing as √(β − β_c). As
  L → ∞ with L_B ≫ L, ε → exp(−2πΔ₁L_B/L) and r_v belongs to the primary of
  lowest scaling dimension Δ₁: IB-relevant is RG-relevant. The
  identification with a CFT is used only to interpret the transfer-matrix
  result, which the authors stress holds at any L once L_B ≫ L.
- **One numerical check.** Critical 2D Ising on a cylinder of
  circumference 3, |V| = 2 × 3, |E| = 1 × 3, L_B = 9, the joint law
  computed exactly: an iterative IB solver finds the transition between
  146.340 and 146.350 against a predicted 146.34458, and the encoder
  follows the boundary magnetization. The prediction is reproduced
  exactly in [NOTE-tmpbm8lu](../notes.d/NOTE-tmpbm8lu.md).
- **Symmetry.** If P(e, v) is invariant under a group S acting by
  permutation, then for β below the second transition, with an alphabet
  large enough that one more symbol does not help, a second-order first
  transition and no fine-tuning, the optimal encoder carries a
  permutation representation of S. With V = E = Z4 and |H| = 2, at
  β → ∞, the optimum breaks the Z4 symmetry (checked by hand in
  [NOTE-tmpbm8lu](../notes.d/NOTE-tmpbm8lu.md)). A procedure for reading an unknown symmetry off a
  solved encoder is sketched.
- **What is asserted, not shown.** That RSMI ([LIT-873](LIT-873.md)) is the β → ∞
  limit of IB at fixed |H|, so that the theorem underwrites it; that the
  whole IB curve of the continuum Gaussian theory is computable (cited to
  work in preparation); and that the symmetry result holds at all β
  (stated as a conjecture).

## Standing in the record

Filed on 2026-10-09 at the owner's request, as one of the works cited by
the batch on hierarchy and hyperbolic geometry (nucleation#113, [LIT-865](LIT-865.md) to
[LIT-877](LIT-877.md)) and its cited works (nucleation#114) that neither record held.
It is cited by Gökmen, Ringel, Huber and Koch-Janusz, *Statistical Physics
through the Lens of Real-Space Mutual Information* ([LIT-878](LIT-878.md)), which takes
from it that the RSMI-optimal filters are the most relevant operators and
calls the result "proven in part". Read on its own merits
([NOTE-tmpbm8lu](../notes.d/NOTE-tmpbm8lu.md)), after [LIT-878](LIT-878.md) and [NOTE-681](../notes.d/NOTE-681.md), [LIT-873](LIT-873.md) and [LIT-881](LIT-881.md).

**Does the proof hold?** In its own setting, yes, and more exactly than
the paper says: in the slab geometry the factorization through the
boundary slices is exact, so β_c⁻¹ = ε² and the critical direction r_v
hold with no corrections, which a transfer-matrix computation reproduces
to every printed digit. What it assumes is that setting: a real symmetric
transfer matrix, block and environment spanning the whole circumference,
a non-degenerate leading eigenvalue, the neighbourhood of the first IB
transition, and, for the scaling-dimension reading, L → ∞ with L_B/L → ∞.
It does not reach the planar block surrounded by a buffer shell that
[LIT-873](LIT-873.md) and [LIT-878](LIT-878.md) use, nor RSMI's fixed-alphabet, β → ∞ optimum, which
the paper relates to IB by assertion. So [LIT-878](LIT-878.md)'s reliance is on a
theorem for a neighbouring geometry and regime; "proven in part" is fair.
[NOTE-tmpbm8lu](../notes.d/NOTE-tmpbm8lu.md) gives a leading-order argument, the reader's and not the
paper's, that closes the RSMI gap in the slab geometry, and says why the
planar case is still open.

It is filed with [THEORY-tmpne099](../theory.d/THEORY-tmpne099.md), the formal counterpart of the
empirical account [THEORY-194](../theory.d/THEORY-194.md) and a different statement from [THEORY-198](../theory.d/THEORY-198.md)'s
full-capture factorization. It bears on [QUESTION-025](../questions.d/QUESTION-025.md) only by analogy, and
on [CLAIM-092](../claims.d/CLAIM-092.md) only as an instance of what an information bottleneck keeps
being characterized spectrally: see [NOTE-tmpbm8lu](../notes.d/NOTE-tmpbm8lu.md).
