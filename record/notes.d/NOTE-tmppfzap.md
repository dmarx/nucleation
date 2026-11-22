---
status: Skimmed
paper: LIT-tmpbgf6y
title: 'Gelfert and Nolting, skimmed for Mermin and Wagner''s procedure and its extension to graphs of low spectral dimension, as a stand-in for Mermin and Wagner'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Read in part on 2026-11-22 by a delegated reader from arXiv
    (arxiv.org/pdf/cond-mat/0106090, v1 of 5 June 2001, the authors'
    accepted manuscript), as a stand-in for Mermin and Wagner (1966),
    LIT-2985 (ADR-114): §§1–2.3, §3 to §3.2, §3.4, the opening of §4 and
    §5. Skipped: §2.4 (generalized inequalities), the detail of §§3.1 and
    3.3 (films, Hubbard and periodic Anderson models) and most of §4, so
    Skimmed. Every quotation below rechecked by the filer by script
    against the downloaded text. No email address sent.
date: '2026-11-22'
summary: >-
  A review of the Mermin–Wagner theorem. Its §3 outlines Mermin and
  Wagner's procedure for the Heisenberg model step by step: Bogoliubov's
  inequality with operators chosen to put the order parameter on the
  left, a double commutator bounded by the exchange's second moment, and
  a 2D bound whose denominator diverges logarithmically as the field
  goes to zero, for ferro- and antiferromagnetic order alike. §3.4
  reports Hattori, Hattori and Watanabe's spectral dimension of general
  networks and Cassi's theorem that spectral dimension at most 2 excludes
  spontaneous magnetization. The reading is THEORY-tmp1nvjs.
---
<!-- inactive-ok-file: THEORY-tmp1nvjs — Proposed; this reading's account -->
<!-- inactive-ok-file: LIT-2985 — Unavailable; the original this reading stands in for -->
<!-- inactive-ok-file: LIT-tmpu2kk5 LIT-tmp309tx — Deferred; Cassi and Hattori et al., registered from this reading -->
<!-- inactive-ok-file: CLAIM-842 CLAIM-841 TERM-136 ARG-tmpx5evn — Proposed or new; the entries the reading bears on -->

# NOTE-tmppfzap: Gelfert and Nolting, skimmed for Mermin and Wagner's procedure and its extension to graphs of low spectral dimension, as a stand-in for Mermin and Wagner

## Contribution

A survey of the theorem across many-body models, with new cases (Hubbard
films, the periodic Anderson model). What the record uses is its outline
of Mermin and Wagner's proof and its report of the theorem on graphs.
The reading is THEORY-tmp1nvjs.

## Key results

1. **Bogoliubov's inequality** (§2.3, eq. 9):
   |⟨[C, A]⟩|² ≤ (β/2)⟨{A, A†}⟩⟨[[C, H], C†]⟩.
2. **Mermin and Wagner's procedure** (§3, eqs. 41–52): the Heisenberg
   model in a field b coupling to e^(−iK·R_i)S_i^z (K covers
   antiferromagnetism), A = S⁻(−k − K), C = S⁺(k); the double commutator
   is bounded through the exchange's second moment; in 2D the k-integral
   gives M² ≤ ξ₄β / ln(1 + ξ₃k₀²/|B₀M|). "As B0 → 0, the denominator
   diverges logarithmically, thus forcing the magnetization to vanish",
   independently of K, so ferro- and antiferromagnetic order are both
   ruled out; 1D by "a similar divergence". The bounds are stated "as has
   been shown by Mermin and Wagner", not re-derived.
3. **The integral** (§3.2): the scheme "ultimately rests on the divergence
   of the integral" ∫_{k≤k₀} d^Dk/k² in one or two dimensions.
4. **Classical spins** (§3): "Mermin showed that a classical
   Bogoliubov-type inequality holds" (1967).
5. **Graphs** (§3.4): Hattori, Hattori and Watanabe ask "Why do the spins
   on the lattice 'know' this natural embedding into Euclidean space that
   should govern their critical phenomena?", since "the only geometrical
   structure that spins can feel is the one given by the Hamiltonian",
   the "network structure of the interaction"; they define the spectral
   dimension of general networks. Cassi, on fractal and disordered
   lattices "whose spectral dimension is less or equal to 2", shows that
   "at finite temperature no spontaneous magnetization can exist for the
   classical O(n) and the ferromagnetic (quantum) Heisenberg model",
   owing to "the infrared divergencies displayed by the corresponding
   Gaussian models".
6. **Approximations** (§4): mean-field-type methods "consistently predict
   finite-temperature phase transitions in one or two dimensions" for
   models that obey the theorem.

## Assumptions

As the reviewed theorem's: an isotropic Hamiltonian, exchange of finite
second moment, a Gibbs state, the quasi-average (field to zero after the
thermodynamic limit).

## Concepts

Bogoliubov inequality; quasi-average; infrared divergence ∫d^Dk/k²;
lower critical dimension 2; spectral dimension of a network.

## Bearing on the record

- **LIT-2985**: stands in for the proof's steps, as an outline (ADR-114).
- **CLAIM-842**: **supports the mechanism, at second hand.** Item 5 is
  "spectral dimension ≤ 2 forbids spontaneous magnetization", for spin
  models with a continuous symmetry in equilibrium, from the Gaussian
  infrared divergence, and Hattori et al.'s point that spins feel only
  the interaction network is A29's point that the governing dimension is
  the interaction graph's. So the graph version exists in the
  literature, as Cassi's theorem, not Mermin and Wagner's, and not for a
  learned representation (ARG-tmpx5evn). Cassi (LIT-tmpu2kk5) and
  Hattori et al. (LIT-tmp309tx) are registered, unread.
- **TERM-136**: **the term's origin for networks.** Hattori et al. define
  the spectral dimension of general networks through a Gaussian field
  theory on them, the sense TERM-136 uses.
- **CLAIM-841**: **consistent.** ∫d^Dk/k² = ∫k^(D−3)dk is the integral the
  claim cites for the 2D logarithm; the rigorous route to it is
  Bogoliubov's bound, not the spin-wave integral.

## Limitations

A secondary outline; Cassi and Hattori et al. are known here only
through two paragraphs of it.
