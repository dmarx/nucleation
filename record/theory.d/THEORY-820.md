---
number: 820
status: Active
formerly:
- THEORY-tmpri29w
title: 'For a stationary discrete-valued process X and any coarse-graining Z of its past, informational closure at every horizon is the same condition as zero one-step transfer entropy from the micro past, Barnett and Seth''s dynamical independence, and as causal closure, Z''s ε-machine coinciding with its υ-machine; for a coarse-graining of the present state it also makes Z''s causal states a coarse-graining of X''s, which does not imply closure, and the closed coarse-grainings are not closed under common refinement'
version: 2
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Filed Active from NOTE-1030. Theorem 1 (informational ⟺ causal
    closure), Proposition 1 (minimality of the υ-machine), Proposition 2
    (order part) and Theorem 2 (spatial causal ⟹ computational closure) are
    the paper's; each is re-derived below step by step, which meets
    ADR-047 v2. The reduction of the all-horizon condition to one step, and
    hence the identity with Barnett–Seth dynamical independence, is the
    record's, as are the corrected spatio-temporal counterexample and the
    counterexample to closure under common refinement. All were checked
    numerically.
- version: 2
  date: '2026-10-21'
  note: >-
    Note of 2026-10-21 added, from the exchange of 2026-10-20 on effective
    description, agency and legibility: A7, A12, A14, A16 and A17 restated
    the refinement counterexample as a Blackwell corollary and explained it:
    closure's target is the description's own future, which refinement
    changes (CLAIM-409); the meet/join convention is fixed in
    TERM-068. The reading is unchanged.
tags:
- complex-systems
- information-theory
- causality
- mathematics
date: '2026-10-20'
source:
- LIT-1306
- LIT-979
answers:
- QUESTION-218
summary: >-
  Rosas et al. (arXiv 2024), [LIT-1306](../literature.d/LIT-1306.md), read in [NOTE-1030](../notes.d/NOTE-1030.md), with Barnett and Seth's definition ([LIT-979](../literature.d/LIT-979.md)). For discrete stationary processes, the information-theoretic criterion of emergent closure (dynamical independence), the interventionist one (the macro's own causal states are all the micro distinctions that matter for it) and, for maps of the present state, a computational one are nested as stated. The first two are one condition. It says nothing about approximate closure. It does not make closure a mark of unity. "Causal" is only in the Granger sense unless X is fully observed.
supports:
- CLAIM-405
- CLAIM-407
- CLAIM-409
---
<!-- inactive-ok-file: THEORY-257 — Proposed; the interpretive reading of dynamical independence this bears on, cited as open -->
# THEORY-820: For a stationary discrete-valued process X and any coarse-graining Z of its past, informational closure at every horizon is the same condition as zero one-step transfer entropy from the micro past, Barnett and Seth's dynamical independence, and as causal closure, Z's ε-machine coinciding with its υ-machine; for a coarse-graining of the present state it also makes Z's causal states a coarse-graining of X's, which does not imply closure, and the closed coarse-grainings are not closed under common refinement

## Source

Rosas, Geiger, Luppi, Seth, Polani, Gastpar and Mediano (2024),
arXiv:2402.09090, [LIT-1306](../literature.d/LIT-1306.md), read in full in [NOTE-1030](../notes.d/NOTE-1030.md). The
equivalence of informational and causal closure is the paper's Theorem 1,
the implication to computational closure its Theorem 2, and the
minimality lemma its Proposition 1. Dynamical independence is Barnett and
Seth's definition ([LIT-979](../literature.d/LIT-979.md), [THEORY-733](THEORY-733.md)). The one-step reduction, the
corrected counterexample and the refinement counterexample below are the
record's.

## What was actually shown

X is a stationary process with a discrete alphabet. X⃗_t is its past up
to t and X⃗⁺ a future block (X_{t+1}, …, X_{t+L}). A coarse-graining is
Z_t = g(X⃗_t). It is **spatial** if Z_t = f(X_t). Statements about
conditional laws hold up to null sets.

**(a) Every horizon reduces to one step.** Informational closure
(Definition 4) asks that I(X⃗_t; Z_{t+1}, …, Z_{t+L} | Z⃗_t) = 0 for every
L. By the chain rule this equals

Σ_{ℓ=1}^{L} I(X⃗_t; Z_{t+ℓ} | Z⃗_{t+ℓ−1}).

X⃗_t is a function of X⃗_{t+ℓ−1}, so each term is at most
I(X⃗_{t+ℓ−1}; Z_{t+ℓ} | Z⃗_{t+ℓ−1}). By stationarity, that is
T = I(X⃗_t; Z_{t+1} | Z⃗_t). So closure at every L holds iff T = 0. T is
Barnett and Seth's transfer entropy T(X → Z), with no environment. So
informational closure is exactly dynamical independence. The paper assumes
this identity and does not show it.

**(b) The υ-machine is the coarsest prescient partition** (Prop. 1).
U_t = υ(X⃗_t) groups pasts with equal laws p(z⃗⁺ | x⃗) at every L.

- *U is prescient.* Those laws depend only on U, so
  I(U_t; Z⃗⁺) = I(X⃗_t; Z⃗⁺).
- *U is the coarsest.* Let D = d(X⃗_t) also be prescient. Since D is a
  function of X⃗_t, I(X⃗_t; Z⃗⁺) = I(D; Z⃗⁺) + I(X⃗_t; Z⃗⁺ | D), so the last
  term is 0. Then p(z⃗⁺ | x⃗) = p(z⃗⁺ | d(x⃗)), and pasts in one D-class lie
  in one U-class. So U is a function of D.
- The same lemma with X replaced by Z gives the classical fact for Z's
  causal states E′: they are the coarsest prescient function of Z⃗.

**(c) Informational ⟺ causal closure** (Thm. 1).

- Z⃗_t is a function of X⃗_t, so
  I(X⃗_t; Z⃗⁺ | Z⃗_t) = I(X⃗_t; Z⃗⁺) − I(Z⃗_t; Z⃗⁺) = I(U_t; Z⃗⁺) − I(E′_t; Z⃗⁺).
  So closure holds iff U and E′ carry equal information about Z⃗⁺ at every
  L.
- *If they do,* then E′ is a function of X⃗_t and prescient for Z⃗⁺, so by
  (b) U = h(E′). Then U is a function of Z⃗_t and prescient among
  functions of Z⃗_t. By (b) applied to Z, E′ is a function of U. Each is a
  function of the other, so the two partitions are equivalent: causal
  closure.
- *Conversely,* equivalent partitions carry equal information.

**(d) Spatial maps: the υ-machine is a quotient of the ε-machine**
(Prop. 2).

- With Z_t = f(X_t),
  p(z⃗⁺ | x⃗) = Σ_{x⃗⁺ ∈ f⁻¹(z⃗⁺)} p(x⃗⁺ | x⃗).
  Pasts with equal micro future laws (one causal state E_t) therefore
  have equal macro future laws, so U_t = f′(E_t).
- The same sum shows the map f ↦ U_f preserves order. If f is coarser
  than f̃, U_f is a function of U_f̃.

**(e) Causal ⟹ computational closure for spatial maps** (Thm. 2). By
(c), E′ ≅ U. By (d), U = f′(E). So E′_t = f*(E_t): Z's causal states are a
coarse-graining of X's.

**Neither converse holds.**

- *Computational without causal closure* (the paper's Counterexample 4,
  checked). P has rows (½, ½, 0, 0), (0, 0, ½, ½), (½, ½, 0, 0) and
  (0, 0, ½, ½). Z merges {1, 2} and {3, 4}. Under the uniform stationary
  law Z is i.i.d., so E′ is trivial and trivially a quotient of E. But
  X_t ∈ {1, 3} sends Z to the first block surely, so T = 1 bit.
- *Spatiality is needed for (e).* Take X i.i.d. and non-degenerate, and
  Z_t = (X_t, X_{t−1}). Then Z_{t+1} = (X_{t+1}, X_t), whose second part is
  in Z_t and whose first is independent of every past, so T = 0. Z's
  causal state is X_t, while X's ε-machine is trivial. So E′ is not a
  function of E.
- The paper's own example for this point, Counterexample 5
  (Z_t = X_{t−1}), is wrong. X⃗_t contains Z_{t+1} = X_t and Z⃗_t does not,
  so T = H(X_t | X_{t−1}) > 0.

**Closure is not preserved by common refinement.** Let X_t = (A_t, B_t,
C_t) be bits, with A_{t+1} and C_{t+1} fresh fair bits and
B_{t+1} = A_{t+1} ⊕ C_t.

- Every state sends probability ½ to each value of A and of B. So by
  [THEORY-822](THEORY-822.md) each of A and B is closed.
- The pair is not: A_{t+1} ⊕ B_{t+1} = C_t is known to X_t and
  independent of the past of (A, B).
- Computed from the exact chain: T = 0, 0 and 1 bit for A, B and (A, B),
  with one, two and three steps of history.
- So the closed spatial coarse-grainings do not form a sublattice of all
  coarse-grainings, contrary to the paper's §III E and Theorem 2. The
  υ-machine map does not preserve meets either: U_A and U_B are trivial,
  while U_{(A,B)} is C_t.

What could have failed: informational closure could have been weaker
than causal closure, since equal information need not mean equal
partitions. It is not, because both partitions are the coarsest prescient
ones of their kind.

## What this does not say

- **Not that closure marks a system.** An i.i.d. noise component is
  closed. The paper's own remedy is a computational quotient, not a mark
  of unity. Whether a closed variable is one system is [QUESTION-218](../questions.d/QUESTION-218.md)'s
  open half.
- **Not interventional causation** unless X is fully observed. Otherwise
  "causal closure" is closure in the Granger sense, as the paper says.
- **Not anything approximate.** Small transfer entropy is not shown to
  mean nearly equal machines, or the reverse.
- **Not continuous or non-stationary processes.** For the linear
  Gaussian case, [THEORY-733](THEORY-733.md) holds the corresponding criterion.
- **Not that the closed coarse-grainings form any lattice.** Closure
  under common coarsening is shown for strongly lumpable partitions
  ([THEORY-822](THEORY-822.md)'s note), not for closure in general.

## Connections

- **[THEORY-733](THEORY-733.md).** Its exact dynamical independence is this informational
  closure, for linear maps of a Gaussian VAR. So its criterion
  L A_k = B_k L is also the VAR form of causal closure. [THEORY-257](THEORY-257.md)'s
  reading that the dynamics fix the variables meets the objection that
  closure overcounts (noise components, copies).
- **[THEORY-822](THEORY-822.md).** For Markov chains, closure is strong lumpability
  when the label is Markov.
- **[THEORY-756](THEORY-756.md).** Part (b) is the υ-machine version of [THEORY-756](THEORY-756.md)'s
  coarsest prescient partition.
- **[QUESTION-218](../questions.d/QUESTION-218.md): answers in part.** It confirms that the closure-side
  unit is a function of the whole state, or of the past. It is not a
  subset of members, and its closure does not extend to common
  refinements. It gives the question no criterion of unity.

## Note of 2026-10-21: the refinement counterexample, as a change of question

A12 and A14 of the exchange of 2026-10-20, following A7, proposed a
corollary: "Blackwell dominance under deterministic refinement does not
imply preservation of informational closure", from this entry's A/B/C
chain (Δ(A) = 0, Δ(A, B) = 1 bit, re-checked with one to four steps of
history). For deterministic descriptions of one state, (A, B)
Blackwell-dominating A is the same fact as A being a function of (A, B).
So the corollary is this entry's "not closed under common refinement" in
the refinement order. Closure is not monotone the other way either: X
itself is always closed and its coarse-grainings need not be.

A16 §5 and A17 §4.4 said why. For a fixed target, refining a description
cannot raise its deficiency; closure's target is the description's own
future, which refinement changes. So the three-bit chain (A and B closed,
(A, B) not) is not a failure of "more information helps" but a change of
question. Both halves are filed as [CLAIM-409](../claims.d/CLAIM-409.md), which rests on
[CLAIM-407](../claims.d/CLAIM-407.md). A16 §2 also reconciled a governance-response failure with
this entry by the entry's own "Not interventional causation"; that is
[CLAIM-407](../claims.d/CLAIM-407.md) and [CASE-125](../cases.d/CASE-125.md).

A13 writes the common refinement A ∨ B, where this entry calls it a meet.
[TERM-068](../terms.d/TERM-068.md) fixes the convention as this entry's.
