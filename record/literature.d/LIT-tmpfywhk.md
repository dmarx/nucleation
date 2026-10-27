---
status: Active
status_note: >-
  read in full 2026-10-27 ([NOTE-tmplvblh](../notes.d/NOTE-tmplvblh.md)), from arXiv v2; worth reading
  as a compositional account in which the coupling data (wiring,
  potential, response) and the dynamical regime are separate choices:
  one arrangement of harmonic particles gives a discrete wave equation or
  a discrete heat equation depending only on whether the integrator
  stores momentum, and gradient descent with backpropagation is the same
  construction applied to a parameterized map. Rigorous for its
  categorical core and its worked examples; many further examples are
  reported from Claude-written code the author did not audit.
title: 'Compositional Dynamics in Learning and Mechanics'
version: 2
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed, not read. Checked against the arXiv API on 2026-10-27: David
    I. Spivak, arXiv 2606.28984, v1 submitted 27 June 2026, which is
    `published:` per ADR-002; v2 is current.
- version: 2
  date: '2026-10-27'
  note: >-
    Read in full from arXiv 2606.28984v2 (22 August 2026, 91 pp., math.CT);
    the first NOTE on the work (NOTE-tmplvblh). v1 was not seen. Status
    set from the reading: Active. Title, author and `published:` (the v1
    date) stand. The companion code the paper names is added under
    `implementations:`, and `anthology-candidate` is added last, since
    the paper recovers gradient descent, backpropagation and weight decay
    and conjectures Adam as an integrator, which an anthology topic on
    training could hold. The summary is replaced by one from the text.
    The registration's summary was right in substance: one arrangement of
    interconnected harmonic particles, with the same potential (and the
    same wiring and response), yields a heat equation or a wave equation
    (Proposition 7.4.1, Remark 7.4.2, pp. 86–87). Four corrections. The
    paper's words are "first-order, descent" and "second-order,
    symplectic", not dissipative and conservative, and the phase step
    preserves the symplectic pairing but "need not conserve H exactly"
    (p. 70). The choice between the two is the integrator's, a semantic
    choice of whether momentum is stored, not anything in the coupling.
    The heat case is a remark, not a numbered result. And it is one of
    seven listed contributions; the paper's subject is learning and
    mechanics as functorial semantics, and its main technical result is
    lens internalization. The exchange's gloss, that the same relational
    organization need not imply the same temporal hierarchy, is not in
    the paper, which never discusses time scales. Two THEORYs are filed
    from it (THEORY-tmp09707, THEORY-tmp3wlcq).
tags:
- compositionality
- learning-theory
- mathematics
- anthology-candidate
date: '2026-10-27'
published: '2026-06-27'
arxiv: '2606.28984'
first_author: 'Spivak'
keywords:
- 'compositional dynamics'
- 'harmonic systems'
- 'heat and wave equations'
- 'category theory'
- 'lenses'
- 'polynomial functors'
- 'gradient descent'
- 'graph Laplacian'
implementations:
- 'https://github.com/dspivak/dap'
summary: >-
  Spivak (2026). An operad ArrSm of "smooth adaptive arrangements"
  (a responsive parameter space, a lens of output and input maps between
  manifolds, and a real potential) with two operad functors into
  polynomial coalgebras, discrete-time input-output machines, built by
  lens internalization (Corollary 3.3.4). The functors differ only in
  the integrator: Φconf stores position and steps down the sharpened
  gradient, Φphase stores position and momentum and takes a
  symplectic-Euler step. Φconf gives gradient descent with
  backpropagation, weight decay and Newton's method. One arrangement of
  harmonic particles on a finite directed graph gives the discrete wave
  equation under Φphase and the discrete heat equation under Φconf, both
  governed by the symmetrized graph Laplacian, and for harmonic closed
  systems the phase step preserves the symplectic pairing exactly.
---
<!-- inactive-ok-file: CLAIM-tmpfw510 — Rejected; the conjecture the exchange cited this work against -->

# LIT-tmpfywhk: Compositional Dynamics in Learning and Mechanics

Spivak, D. I. (2026). Compositional dynamics in learning and mechanics. arXiv:2606.28984.

Read in full on 2026-10-27 ([NOTE-tmplvblh](../notes.d/NOTE-tmplvblh.md)).

## Why this is here

A22 §6 called it "almost a controlled demonstration" that "The same
relational organization need not imply the same temporal hierarchy",
which is the objection to the owner's U20 that coupling induces scale
separation ([CLAIM-tmpywecm](../claims.d/CLAIM-tmpywecm.md)). It bears on [CLAIM-tmpfw510](../claims.d/CLAIM-tmpfw510.md).
