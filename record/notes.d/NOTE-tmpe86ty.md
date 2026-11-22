---
status: Read
paper: LIT-3010
title: 'Crutchfield & Feldman — Regularities Unseen, Randomness Observed: Levels of Entropy Convergence'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    From the arXiv PDF of cond-mat/0102181 (v1 of 9 February 2001, the
    only version; SFI Working Paper 01-02-012; 35 pp.), fetched 2026-11-22
    without obstacle, text extracted with pdftotext. Read in full: §§I–VIII,
    Tables I–III, Appendix A (proofs of Props. 1–8 and Lemmas 1 and 3) and
    the opening of Appendix B. Skimmed: the rest of Appendix B, Appendix C
    (proof of Theorem 1), the references. Figures from captions only. The
    2003 journal text (Chaos 13, 25–54, doi 10.1063/1.1530990, paywalled)
    was not seen; differences from the preprint are unknown. Read by a
    reader subagent; filed by a second one, which rechecked every quote
    used here against the extracted text and checked the Thue–Morse growth
    of the record's TERM-141 quantity numerically. No email address sent.
date: '2026-11-22'
summary: >-
  The block entropy's discrete derivatives and integrals give one
  hierarchy: entropy rate, predictability gain, excess entropy (equal to
  the subextensive part of the block entropy and to the past–future
  mutual information) and a new transient information. Excess entropy is
  one kind of memory, not structure: processes with equal excess entropy
  differ in transient information, and a source with small excess entropy
  can need an infinite-state predictor.
---
<!-- inactive-ok-file: THEORY-tmpl7rgc TERM-141 THEORY-2151 CLAIM-805 THEORY-784 CLAIM-849 ARG-152 ARG-154 SYNTHESIS-119 — Proposed or new; the account this reading files and the entries it bears on -->

# NOTE-tmpe86ty: Crutchfield & Feldman — Regularities Unseen, Randomness Observed: Levels of Entropy Convergence

## Contribution

A synthesis of known quantities (entropy rate hµ, total predictability G,
excess entropy E under its many names) into one derivative-and-integral
hierarchy of the block entropy H(L), with one new quantity, the transient
information T, and one new theorem relating T to synchronization. The
authors say so: the narrative "touches on and restates results and
intuitions known to a number of researchers" (§I).

## Key results (arXiv preprint; sections as numbered there)

- **E, two identities** (§IV). E ≡ Σ_L [hµ(L) − hµ] (Eq. 48). Prop. 7:
  "The excess entropy is the subextensive part of H(L): E = lim [H(L) −
  hµL]". Prop. 8: E is "the mutual information between the left and right
  (past and future) semi-infinite halves of the chain", when the limit
  exists; read as historical "information stored in the present that is
  communicated" to the future, and as the cost of amnesia (credited to Dan
  Upper).
- **Finite-L estimates** (§IV): E(L) = H(L) − L hµ(L) (Eq. 60), E′(L) the
  mutual information between the halves of an L-block (Eq. 61, = 2H(L/2)
  − H(L)); Lemma 3: "E′(L) ≤ E(L) ≤ E". TERM-141's I_pred(T) is E′(2T).
- **Finitary and infinitary** (§IV): "A process is finitary if its excess
  entropy is finite" (Def. 1); finitary processes have hµ(L) − hµ < A/L
  (Prop. 9); "For infinitary processes hµ(L) decays at or slower than
  1/L", and H(L) may grow like c1 + c2 log L + hµL.
- **Closed forms**: period p, E = log2 p (Prop. 10); order-R Markov,
  E = H(R) − Rhµ (Prop. 11). "To our knowledge, there is not a direct
  proof of exponential decay for more general finitary processes."
- **Transient information** (§V, Thm 1): for block-Markov processes
  S = T + ½R(R + 1)hµ; "The transient information measures a structural
  property of the system — a property not captured by the excess entropy
  E." The three period-5 processes have E = log2 5 and T = 4.073, 5.273
  and 4.873 bit-symbols (Table II).
- **Entropy rate does not fix memory** (§VI): golden mean, RRXOR and even
  process share hµ = 2/3 and have E ≈ 0.2516, 2 and 0.902 bits.
- **Information measures can understate structure** (§VI): the simple
  nondeterministic source has E ≈ 0.147 bits and T ≈ 0.175, but its
  optimal deterministic representation "has an infinite number of
  states"; "relying only on information theoretic quantities, one is
  misled as to the process's actual complexity."
- **Thue–Morse** (§VI): "there is no finite-state process that can
  generate the Thue-Morse sequence"; hµ = 0, "the excess entropy diverges;
  E(L) ∝ log2 L, indicating an infinite-memory process"; T(L) diverges
  linearly.
- **Reported infinitary cases** (§VI, others' results): cellular automata
  rules 30 and 45 (α = 0.6 ± 0.1) and 120 (α = 1.0 ± 0.1, Grassberger);
  written texts, "hµ(L) − hµ ∼ L^α with α ranging from 0.4 to 0.6" (a
  decay, so L^(−α) is meant; the sign is as printed); a Beethoven sonata,
  α ≈ .75; Bialek and colleagues' Ising exponents.
- **Ignored memory becomes randomness** (§VII): synchronized,
  h′µ(L) − hµ = E/L (Prop. 13), "E bits of memory are converted into
  additional, apparent randomness"; assuming synchronization too early
  understates hµ and E (Prop. 15).
- **Against disorder-based complexity** (§IV): measures "based on
  multiplying G by hµ" fail "to capture structure or memory, since they
  are only a function of disorder hµ", citing Feldman and Crutchfield's
  "Discovering noncritical organization" among others.
- **The frame's own limit** (§IV, §VIII): how memory "is organized cannot
  be done within the framework of information theory; a more structural
  approach based on the theory of computation must be used"; the
  ε-machine "captures all of a source's structure"; Bialek and colleagues'
  result "holds in a slightly different context than ours"; in two
  dimensions the expressions for E "yield different results".

## Assumptions

A stationary process on a finite alphabet; block probabilities known
exactly (estimation set aside); H(0) = 0 and hµ(0) = log2|A| as boundary
conditions; Theorem 1 for directly observed block-Markov processes only;
exponential convergence for finitary hidden Markov processes assumed or
empirical. One dimension.

## Concepts

Block entropy H(L); entropy gain hµ(L); predictability gain Δ²H(L);
redundancy and total predictability G; excess entropy E (stored
information, effective measure complexity, predictive information);
transient information T; synchronization information S; finitary and
infinitary processes; measure sofic process; nondeterministic hidden
Markov model; weak Bernoulli.

## Check

The filer computed TERM-141's 2H(T) − H(2T) for the Thue–Morse sequence
from a 2²¹-symbol prefix with `python3 -I`: 0.59, 2.09, 3.34, 4.46 and
5.52 bits at T = 2, 4, 8, 16 and 32, about 1.1 bits per doubling,
logarithmic growth as the paper reports for E(L).

## Bearing on the record

- **LIT-3010**: the exchange invoked it for "excess entropy as the measure
  of a process's stored structure": fair for stored information,
  overstated for "the measure". E is "a measure of one kind of memory".
  Corrected in the LIT and in TERM-141.
- **TERM-141**: supports the definition and its identities; adds Lemma 3;
  qualifies the regimes (Thue–Morse: logarithmic growth with no parameter,
  under condition 2); corrects "the measure of structure". Made in place
  there (version 2).
- **THEORY-2151, LIT-3008, NOTE-2243**: parallel, with a stated contrast.
  The paper treats E and Bialek and colleagues' predictive information as
  one quantity (its alias list), reports their Ising exponents, and says
  their parameter-count result "holds in a slightly different context".
  It corroborates NOTE-2243's identification of S₁ with E when finite; it
  does not take up their divergence-at-criticality assertion.
- **CLAIM-805**: supports the separation of entropy and memory (equal hµ,
  unequal E; hµ·G measures rejected as functions of disorder);
  THEORY-tmpl7rgc `corroborates` it. Silent on criticality.
- **QUESTION-507**: background; measures a capacity study could use, and
  the finite-window warning (Props. 13–15) for point 2.
- **QUESTION-517, LEAD-208**: two-dimensional excess entropies differ by
  definition, so LEAD-208's step 3 must choose one.
- **NOTE-689, THEORY-784**: parallel. Their Hypothesis 1, H_n − H_∞ ≍
  n^(−γ) with γ ≈ 0.27–0.33, is this paper's power-law entropy
  convergence, which makes the token process infinitary.
- **NOTE-1372** (Shalizi and Crutchfield): parallel; "Excess entropy is a
  lower bound on stored memory, not a measure of it" is the lesson of the
  simple nondeterministic source.
- **CLAIM-849, ARG-152, ARG-154, SYNTHESIS-119**: background, the same
  quantity; no bearing beyond TERM-141's; no notes filed.
- **NOTE-978**: its "Eq. (106) of Feldman and Crutchfield" is not this
  paper's (whose equations stop near 105 and none bounds Cµ); unidentified,
  reported to the lead.

Not held, relevant, not registered: Feldman and Crutchfield, "Discovering
noncritical organization" (1998, cited as submitted to J. Stat. Phys.; no
arXiv record or DOI found); Ebeling and Pöschel (1994) on literary
English; Grassberger (1986).

## Limitations

A synthesis paper; most results are restated. Exact block probabilities
assumed, nothing on estimation. Theorem 1 only for observed Markov
chains. Many numbers (γ fits, E, T) are numerical estimates; the text and
Ising exponents are cited, not derived. A printed sign slip (L^α for a
decay) and garbled indices in Eq. 53 as extracted. Read from the 2001
preprint, not the 2003 journal text.
