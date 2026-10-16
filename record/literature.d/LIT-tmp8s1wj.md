---
status: Active
status_note: 'read 2026-10-14 ([NOTE-tmp4mti8](../notes.d/NOTE-tmp4mti8.md)) in full; worth reading as the proof that the Johnson–Lindenstrauss order ε⁻² lg n cannot be beaten by any map, linear or not, on a worst-case point set, and as a lower bound that is itself a count of sparse supports. Read it knowing that the bound is Ω(ε⁻² lg(ε²n)) and holds only for lg^0.5001 n/√min{n, d} < ε < 1; that it is tight up to an unstated constant, not a sharp threshold; that the guarantee is on squared distances; and that it says nothing about random features, expansion or typical inputs.'
title: 'Optimality of the Johnson-Lindenstrauss Lemma'
version: 2
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Filed, not read, at the owner's request after a survey found the record
    meets random projections from three directions without holding the
    result they share. Citation checked against arXiv on 2026-10-14. Not held in the Anthology of the SOTA: a grep of its record/ (clone at commit d1573d2) for the title, the identifier and the result's name found nothing. Published at FOCS 2017.
- version: 2
  date: '2026-10-14'
  note: >-
    Read in full (NOTE-tmp4mti8) from the arXiv PDF, 1609.02094v2 of 9
    November 2017, fetched from arxiv.org/pdf/1609.02094: §§1–3 and §3.1.
    The status moved from Deferred to Active. The summary is rewritten from
    the reading: the range of ε was wrong ("within the lemma's range"), the
    bound is Ω(ε⁻² lg(ε²n)), and the guarantee is on squared distances.
    The standard-statement takeaways are replaced with the reading, and
    Standing in the record is corrected: the result is a matching lower
    bound up to a constant, not a threshold. The copy does not state the
    FOCS venue, so that detail was not checked against it; nothing in the
    copy contradicts the other bibliographic fields.
tags:
- mathematics
date: '2026-10-14'
published: '2016-09-07'
arxiv: '1609.02094'
first_author: 'Larsen'
keywords:
- 'Johnson-Lindenstrauss lemma'
- 'dimensionality reduction'
- 'lower bound'
- 'optimality'
- 'encoding argument'
- 'distributional JL lemma'
- 'incoherence'
extends:
- LIT-tmp7skui
implementations: []
summary: >-
  Larsen & Nelson (2017), FOCS 2017, [ARXIV-1609.02094](https://arxiv.org/abs/1609.02094). For integers n, d ≥ 2 and lg^0.5001 n/√min{n, d} < ε < 1, some n points in R^d need m = Ω(ε⁻² lg(ε²n)) dimensions under any map, linear or not, that keeps all squared distances within 1 ± ε. For ε > 1/min{n, d}^0.4999 this is Ω(ε⁻² lg n), so the Johnson–Lindenstrauss bound is optimal up to a constant, and the distributional lemma with a union bound cannot be improved on. The proof is an encoding argument over k-sparse vectors with k = ε⁻²/256, ending in m = Ω(k lg(d/k)).
---

# LIT-tmp8s1wj: Optimality of the Johnson-Lindenstrauss Lemma

Kasper Green Larsen and Jelani Nelson (2017), "Optimality of the Johnson-Lindenstrauss Lemma", FOCS 2017 — [ARXIV-1609.02094](https://arxiv.org/abs/1609.02094)

## Key takeaways

*From the reading, [NOTE-tmp4mti8](../notes.d/NOTE-tmp4mti8.md).*

- **Theorem 2.** For integers n, d ≥ 2 and
  ε ∈ (lg^0.5001 n/√min{n, d}, 1) there is X ⊂ R^d with |X| = n such that
  any f : X → R^m with (1 − ε)‖x − y‖₂² ≤ ‖f(x) − f(y)‖₂² ≤
  (1 + ε)‖x − y‖₂² for all x, y ∈ X has m = Ω(ε⁻² lg(ε²n)).
- **Optimal up to a constant.** In the abstract's form, m = Ω(ε⁻² lg n) for
  1/min{n, d}^0.4999 < ε < 1. The upper bound is
  O(min{n, d, ε⁻² lg n}), so some lower limit on ε is necessary. Constants
  are not tracked.
- **Any map.** f may be nonlinear and may depend on X. The earlier
  Ω(ε⁻² lg n) bound of the same authors held only for linear maps; the
  best bound for general maps was Ω(ε⁻² lg n/lg(1/ε)).
- **The union bound is optimal.** The paper concludes that obtaining the
  lemma from the distributional JL lemma (m ≲ ε⁻² lg(1/δ)) with
  δ < 1/C(n, 2) and a union bound over pairs cannot be improved.
- **The proof counts sparse supports.** The hard sets are 0, e₁ … e_d and
  k-sparse vectors y_S = Σ_{j∈S} e_j/√k with k = ε⁻²/256 and
  d = n/lg(1/ε). Any valid embedding can be written in O(nm) bits and
  determines every S, so nm = Ω(kn lg(d/k)).
- **Incoherence is easier.** Unit vectors with pairwise |⟨x, y⟩| = O(ε)
  fit in m = o(ε⁻² lg n) when ε < 2^{−ω(√lg n)}, by Reed–Solomon codes, so
  nearly orthogonal hard sets could not prove the result.
- **Conjecture 1.** The optimal dimension is
  Θ(min{n, d, ε⁻² lg(2 + ε²n)}). Alon and Klartag later proved the lower
  bound for all parameters, as §1.2 reports.

## Standing in the record

Filed on 2026-10-14 with [LIT-tmp7skui](LIT-tmp7skui.md) for [QUESTION-tmpa0dq9](../questions.d/QUESTION-tmpa0dq9.md), and
read the same day in [NOTE-tmp4mti8](../notes.d/NOTE-tmp4mti8.md). It makes ε⁻² lg n the right order
for keeping the squared distances of a worst-case set of n points, for ε
above about 1/√min{n, d}. The registration said it makes ε⁻² log n "a
threshold rather than an upper bound". The reading corrects that: it is a
matching lower bound up to an unstated constant, shown by existence, not a
sharp threshold of the Donoho–Tanner kind.

For the question it bears on two threads. On distances, it shows that
the union bound over pairs is optimal, which is the shape the question
proposes. On superposition, its lower bound is a count of k-sparse
supports, m = Ω(k lg(d/k)) with k ≈ ε⁻², the form of the
compressed-sensing bound in [NOTE-278](../notes.d/NOTE-278.md) (my observation, not the paper's).
It also states that almost-orthogonal sets fit in fewer dimensions than
ε⁻² lg n for small ε, so the JL lower bound is not a bound on superposition
capacity. It says nothing on random features or on maps that go up in
dimension.

Filed as [THEORY-tmpfo89o](../theory.d/THEORY-tmpfo89o.md).
