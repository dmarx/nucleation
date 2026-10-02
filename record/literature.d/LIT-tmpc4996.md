---
status: Active
status_note: 'read in full 2026-10-02 ([NOTE-tmp3j7zx](../notes.d/NOTE-tmp3j7zx.md)); worth reading as the short paper that turned the entropy-production fluctuation theorem into a finite-time, trajectory-level statement for stochastic, microscopically reversible dynamics, P_F(+ω)/P_R(−ω) = e^{ω}, and derived the Jarzynski equality from it in a line. It also defines the trajectory entropy production ω = ln ρ(x_{−τ}) − ln ρ(x_{+τ}) − βQ that the record''s stochastic-thermodynamics papers inherit. Read it knowing that its conditions are stated exactly (finite classical system, constant-intensive-parameter baths, Markovian microscopically reversible dynamics, ω odd under time reversal), and that the steady-state version is formally exact but, by the author''s own account, of little practical use.'
title: 'Entropy production fluctuation theorem and the nonequilibrium work relation for free energy differences'
version: 1
history:
- version: 1
  date: '2026-10-02'
  note: >-
    Read in full (arXiv cond-mat/9901352 v4, 29 Jul 1999, the last
    revision, "Typos removed, references added. Includes an expanded
    introduction"; v1 29 Jan 1999. 7 pp. from the arXiv PDF; text extracted
    with PyMuPDF). I read every section (I–V), the five figure captions and
    all 34 references, and checked the derivation of Eq. 2 from Eqs. 5–7
    and of Eq. 10 from Eqs. 6 and 9. The Physical Review E version of
    record (60(3):2721–2726, 1 September 1999) was not seen. Not held in
    the Anthology of the SOTA: a grep of its literature.d for "Crooks", the
    DOI and the arXiv id found nothing. `published:` is the arXiv v1 date.
    Filed with the critics of Prigogine's extremum principles and the
    fluctuation theorems, at the owner's request to fill out the record's
    coverage of dissipative structures.
tags:
- thermodynamics
- natural-sciences
- information-theory
date: '2026-10-02'
published: '1999-01-29'
doi: '10.1103/PhysRevE.60.2721'
arxiv: 'cond-mat/9901352'
first_author: 'Crooks'
keywords:
- 'fluctuation theorem'
- 'Crooks fluctuation theorem'
- 'entropy production'
- 'microscopic reversibility'
- 'nonequilibrium work relation'
- 'nonequilibrium steady state'
implementations: []
summary: >-
  Crooks (1999), DOI-10.1103/PhysRevE.60.2721. For finite classical systems
  with stochastic, Markovian, microscopically reversible dynamics, the
  entropy production ω of a forward process and of its time reverse satisfy
  P_F(+ω)/P_R(−ω) = e^{ω} for any finite time, provided ω is odd under
  reversal. That holds for processes that start and end in equilibrium,
  where ω = β(W − ΔF), and for time-symmetric nonequilibrium steady states.
  The Jarzynski equality follows in one line, and for long times the
  theorem gives a heat fluctuation theorem and a Gaussian with variance
  twice the mean.
---
<!-- source-ok-file: cond-mat/9901352 — the arXiv version is titled "The Entropy Production Fluctuation Theorem and the Nonequilibrium Work Relation for Free Energy Differences"; the published PRE title, recorded here, drops the article -->
<!-- inactive-ok-file: THEORY-026 — Proposed; named as the account this reading bears on, not leaned on -->

# LIT-tmpc4996: Entropy production fluctuation theorem and the nonequilibrium work relation for free energy differences

Gavin E. Crooks (1999), *Physical Review E 60(3), 2721–2726* — DOI-10.1103/PhysRevE.60.2721 (preprint arXiv:cond-mat/9901352, 29 January 1999)

## Standing in the record

Filed on 2026-10-02 with the critics of Prigogine's extremum principles, the
maximum-entropy-production literature and the fluctuation theorems, at the
owner's request to fill out the record's coverage of dissipative
structures. The anthology does not hold it, and no anthology topic can.

[NOTE-tmp3j7zx](../notes.d/NOTE-tmp3j7zx.md) is the close reading of 2026-10-02, and it placed the work:
**Active**. It is the paper that joined the two exact far-from-equilibrium
results of the late 1990s: the entropy-production fluctuation theorem of
Evans, Searles, Gallavotti and Cohen, and Jarzynski's work equality
([LIT-tmp47vbz](LIT-tmp47vbz.md)). It derives the second from a generalized form of the
first. Seifert's review ([LIT-tmpcfjz8](LIT-tmpcfjz8.md)) names its work relation the Crooks
fluctuation theorem and builds its unification on the same time-reversal
argument. The quantum thermodynamics review [LIT-010](LIT-010.md) gives its classical and
quantum (Tasaki–Crooks) forms.

For the record's thermodynamics-of-prediction line, it is the cited
background, not the source. Still et al. ([LIT-327](LIT-327.md)), whose authors include
Crooks, cite this paper as one of the fluctuation theorems that assume a
known protocol. Their setup is that of a different paper, Crooks's 1998
Journal of Statistical Physics article on microscopically reversible Markov
systems, which the record does not hold. [THEORY-026](../theory.d/THEORY-026.md) rests on an
average-level identity and uses no fluctuation theorem. This paper's ω,
though, is the trajectory-level quantity a single-trajectory version of
[LIT-327](LIT-327.md)'s Eq. 14, the open question [NOTE-295](../notes.d/NOTE-295.md) raises, would have to start
from.

On Prigogine's programme it bears only indirectly. Its steady-state
theorem, and the Green–Kubo relations it recovers for Gaussian entropy
production, are statements about fluctuations in a nonequilibrium steady
state that do not assume near-equilibrium. The paper's opening contrast is
exactly that: most relations of nonequilibrium statistical dynamics hold
"only in the linear, near-equilibrium regime", and the fluctuation theorems
are the exception. The paper does not discuss extremum principles, Prigogine's
or any other.
