---
status: Read
paper: 'LIT-tmp0lkpg'
title: 'A Mathematical Theory of Communication'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read from the reprint "with corrections" of the two BSTJ parts (55
    pages, text layer), as posted by the Harvard mathematics department
    (people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf);
    its pagination is the reprint's, not the journal's, and section and
    theorem numbers are as in the reprint. Introduction, Part I (§§1–10,
    Theorems 1–9) and Part II (§§11–17, Theorems 10–12) read closely;
    Appendices 1–4 skimmed for what they prove, not checked line by line.
    Parts III–V (§§18–29: band-limited ensembles, continuous entropy, the
    continuous channel, the rate for a continuous source) and Appendices
    5–7 skimmed for their theorem statements (13–23) and the surrounding
    argument. Text extraction lost most minus signs, fractions and
    displayed formulas; the formulas below are given where the prose or a
    worked example fixes them, and are otherwise described.
date: '2026-10-09'
summary: >-
  Shannon defines a discrete source as an ergodic Markov process and its
  information rate as H = −Σ p log p per symbol, proves that typical long
  sequences number about 2^{HN} (Theorems 3–4) and that a source can be
  sent over a noiseless channel at C/H − ε symbols per second and no
  faster (Theorem 9). For a noisy channel he defines R = H(x) − H_y(x)
  and C = max R, and proves by averaging over random codes that any
  rate below C can be sent with arbitrarily small error frequency, while
  above C the equivocation is at least H − C (Theorem 11). The continuous
  parts add the sampling representation, C = W log(1 + P/N) for white
  noise, and a minimum rate for a source at a given fidelity.
---

# NOTE-tmpduzgr: A Mathematical Theory of Communication

## Contribution

Before this paper there were measures of channel speed (Nyquist, Hartley)
and the observation that coding can trade bandwidth for signal-to-noise
ratio. After it, information produced by a stochastic source has a single
measure, entropy, which is operationally the minimum rate needed to
transmit the source; a noisy channel has a single number, its capacity,
which is the maximum rate at which information can cross it with
arbitrarily small error; and these two numbers are shown to be the
whole story for matching a source to a channel. The paper also defines,
for continuous sources, the minimum rate needed to reproduce a source to a
stated fidelity, which is rate-distortion theory in its first form.

## Key insight

Count the typical long sequences. A source of entropy H produces, over N
symbols, about 2^{HN} sequences that carry nearly all the probability; a
channel of capacity C can make about 2^{CT} signals distinguishable in time
T despite noise. Communication is then the matching of one set to the
other, and it works exactly when the first set is the smaller. Errors do
not force the rate to zero: the redundancy needed to defeat noise is a
fixed fraction, paid once, not a cost that grows as the error requirement
tightens.

## Assumptions

- **Discrete source** (§§2–5): a finite-state Markov process emitting a
  symbol per transition, assumed **ergodic** (the graph is connected and
  the circuit lengths have greatest common divisor one), so that time
  averages along a sequence equal ensemble averages. Mixed sources are a
  weighted sum of ergodic components.
- **Noiseless channel** (§1): sequences of symbols of given durations,
  with allowed sequences describable by a finite-state graph.
- **Noisy discrete channel** (§11): a finite-state channel with
  transition probabilities p_{α,i}(β, j); in the memoryless case, a
  matrix p_i(j).
- **Transducers** (§8): encoder and decoder have finite internal memory.
- **Semantics excluded** (Introduction): meaning is "irrelevant to the
  engineering problem"; what matters is that the message is selected from a
  set of possible messages, and the system must work for every selection.
- **Continuous case** (§§18–29): ensembles of band-limited functions;
  noise additive and independent of the signal for Theorem 16 onward;
  white thermal noise for Theorem 17; a fidelity criterion expressible as
  the average of a distance function ρ(x, y) for Part V.

## Key results

- **Theorem 1** (§1). The capacity of a constrained noiseless channel,
  C = lim log N(T)/T, is log W for W the largest real root of a
  determinant equation in the symbol durations. Telegraph example:
  C ≈ 0.539 bits per unit time.
- **Theorem 2** (§6, Appendix 2). The only H continuous in the p_i,
  increasing in n for equal probabilities, and additive over successive
  choices is H = −K Σ p_i log p_i. Shannon says this theorem "and the
  assumptions required for its proof, are in no way necessary for the
  present theory"; the justification of the definitions "will reside in
  their implications".
- **Properties** (§6). H(x, y) ≤ H(x) + H(y) with equality only under
  independence; H(x, y) = H(x) + H_x(y); H_x(y) ≤ H(y); averaging the
  p_i by a doubly stochastic matrix increases H.
- **Theorems 3–4** (§7, Appendix 3). For an ergodic source, long
  sequences split into a set of total probability below ε and a set
  whose members satisfy |log(1/p)/N − H| < δ; the number n(q) of most
  probable sequences needed to reach probability q satisfies
  log n(q)/N → H for any q other than 0 or 1. *Holds when:* the source
  is ergodic.
- **Theorems 5–6.** H is the limit of the block entropy G_N per symbol
  and of the conditional entropy F_N of the next symbol given N − 1
  before it; both decrease monotonically in N, and F_N is the better
  approximation.
- **Theorem 7** (§8). A finite-state transducer cannot increase entropy
  per unit time, and a non-singular one preserves it.
- **Theorem 8.** Choosing transition probabilities on a constrained
  channel's graph appropriately makes its symbol entropy equal its
  capacity.
- **Theorem 9** (§9, the noiseless coding theorem). A source of entropy
  H bits per symbol can be encoded for a channel of capacity C to run at
  C/H − ε symbols per second, and not faster than C/H. Two proofs: a
  typical-set argument, and an explicit code from the binary expansion of
  cumulative probabilities (ordered by decreasing probability), noted as
  substantially Fano's method. Excess over the ideal is at most 1/N plus
  G_N − H for blocks of N symbols.
- **Rate and equivocation** (§12). R = H(x) − H_y(x) = H(y) − H_x(y) =
  H(x) + H(y) − H(x, y). Worked example: 1000 binary symbols per second
  with 1% errors carry about 919 bits per second, not 990, because the
  equivocation is about 81 bits per second.
- **Theorem 10.** H_y(x) is exactly the capacity a correction channel
  needs to let the receiver correct all but an arbitrarily small
  fraction of errors; less does not suffice.
- **Capacity** (§12): C = max (H(x) − H_y(x)) over input sources.
- **Theorem 11** (§13, the noisy coding theorem). If H ≤ C there is a
  code with arbitrarily small error frequency or equivocation; if H > C
  the equivocation can be brought to H − C + ε and no lower. Proof by
  averaging the error over random assignments of messages to the
  high-probability channel inputs, then noting that some code is at least
  as good as the average; Shannon adds that almost all such random codes
  are near the ideal.
- **Theorem 12** (§14). log N(T, q)/T → C, where N(T, q) is the largest
  number of signals distinguishable with error probability at most q,
  for any q other than 0 or 1.
- **Special cases** (§16). For a channel whose rows and columns are
  permutations of one another, C = log m + Σ p_i log p_i. For groups of
  symbols never confused with one another, C = log Σ 2^{C_n}.
- **§17.** Hamming's seven-bit code, with four message bits and three
  parity checks, exactly matches a channel that corrupts at most one bit
  per block of seven, at its capacity of 4/7 bit per symbol.
- **Continuous parts, skimmed.** Theorem 13: a function band-limited to W
  is fixed by samples 1/(2W) apart, so band W and duration T give 2TW
  dimensions; its proof is referred to the 1949 paper. Theorems 14–15
  (entropy power through filters and of sums). Theorem 16: with additive
  independent noise, R = H(y) − H(n). Theorem 17: band W, white noise
  power N, average signal power P gives C = W log((P + N)/N). Theorems
  18–20: bounds for arbitrary noise and for peak-power limits. Theorem 21:
  a source with rate R_1 at fidelity v_1, where R_1 is the minimum rate
  over all joint distributions meeting the fidelity, can be sent over a
  channel of capacity C at that fidelity if and only if R_1 ≤ C. Theorems
  22–23: for a white-noise source of power Q under mean-square error N,
  R = W_1 log(Q/N); for any source it is bounded between the entropy-power
  and the power versions of that expression.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Entropy is the minimum average rate at which an ergodic source can be encoded | strong (proof) | Theorems 3, 4, 9; Appendix 3 |
| C2 | A noisy channel has a capacity C such that any rate below it is achievable with arbitrarily small error, and no rate above it is | strong for the statement; the achievability proof is a sketch at the typical-set level, not a full epsilon-delta argument | Theorem 11, §13 |
| C3 | Equivocation H_y(x) is the exact information a receiver lacks | strong (proof) | Theorem 10 |
| C4 | The axiomatic uniqueness of H is not what justifies it; the coding theorems are | stated by the author | §6, after Theorem 2 |
| C5 | English has redundancy of roughly 50% over spans up to about eight letters | weak to moderate: three methods "in this neighborhood", none reported in detail | §7 |
| C6 | Explicit codes approaching capacity were not known, and this is "probably" related to the difficulty of explicitly constructing near-random sequences | conjecture | §14 |
| C7 | White-noise channels have capacity W log(1 + P/N), and approaching it requires signals that resemble white noise | strong for the formula, skimmed | Theorem 17, §25 |

## Concepts

- **entropy H** — of a set of probabilities, −K Σ p_i log p_i; of a
  source, the state-weighted average of per-state entropies, per symbol or
  per second (H′).
- **relative entropy** — *in this paper*, the ratio of a source's entropy
  to the maximum it could have on the same alphabet, the maximum possible
  compression into that alphabet. It is not the Kullback–Leibler
  divergence that the phrase means now.
- **redundancy** — one minus relative entropy, in the sense above.
- **equivocation** — H_y(x), the conditional entropy of what was sent
  given what was received.
- **rate of transmission** — R = H(x) − H_y(x); now called mutual
  information, a term this paper does not use.
- **capacity** — for a noiseless channel lim log N(T)/T; for a noisy one
  max R over input sources.
- **ergodic source** — statistical homogeneity: almost every long sequence
  has the same limiting frequencies.
- **non-singular transducer** — one with an inverse transducer.
- **rate R_1 for fidelity v_1** — minimum of R over joint distributions
  P(x, y) meeting the fidelity constraint; the later rate-distortion
  function.
- **bit** — the binary digit as unit, a word credited to J. W. Tukey.

## Connections

Shannon builds on Nyquist (1924, 1928) and Hartley (1928) for the
logarithmic measure; on Fréchet for Markov chains and on Wiener for the
statistical view of communication and his filtering and prediction work,
which the acknowledgements credit. The coding of §9 is credited as
substantially the same as Fano's, found independently; the code of §17 is
Hamming's. The sampling theorem's proof is referred to Shannon's 1949
"Communication in the Presence of Noise" ([LIT-317](../literature.d/LIT-317.md)), which the paper cites
in a footnote to Theorem 13. Formulas like Theorem 17's are noted as found
independently "by several other writers, although with somewhat different
interpretations": N. Wiener, W. G. Tuller and H. Sullivan (§25).

## Bearing on the record

- **[LIT-317](../literature.d/LIT-317.md) (Shannon 1949).** That LIT is Deferred and its summary credits
  the 1949 paper with the sampling theorem and C = W log₂(1 + P/N). Both
  already appear in this paper, as Theorems 13 and 17; this paper states
  the sampling theorem and defers its proof to the 1949 paper. So "where
  the capacity formula first appears" is this paper, and what the 1949
  paper adds is the geometric treatment and the sampling proof. This is
  worth a line in [LIT-317](../literature.d/LIT-317.md) when it is read; I did not edit it.
- **[LIT-338](../literature.d/LIT-338.md) (information bottleneck) and [NOTE-300](NOTE-300.md).** [NOTE-300](NOTE-300.md) reads the IB
  paper as opening with Shannon having left meaning out and as a
  rate-distortion problem. Both premises are in this paper: the
  Introduction sets semantic aspects aside explicitly, and Part V defines
  the rate for a source at a fidelity as a minimum of the transmission
  rate over joint distributions, which is the form IB inherits.
- **THEORY.** None of the record's THEORY documents is an account of
  Shannon's theorems; [THEORY-006](../theory.d/THEORY-006.md) (InfoNCE bounds on mutual information)
  and [THEORY-035](../theory.d/THEORY-035.md) (Rejected, compression in SGD) use mutual information but
  rest on nothing this paper says. No THEORY is filed. A candidate, not
  filed: "Shannon's entropy is justified operationally, by the coding
  theorems, and its axiomatic uniqueness is offered only as plausibility",
  which matters when an argument leans on the axioms to say that some
  other quantity cannot measure information. Source this paper; promote
  if a later paper is read that rests a claim on the axioms alone.
- **Anthology.** No instruction for machine-learning practice; nothing for
  the anthology.

## Limitations

- **Proofs at sketch level.** Theorem 11's achievability is an averaging
  argument stated in terms of "about" and "small", with the limits
  asserted; the strong converse is not proved. Shannon himself calls the
  demonstration "not a pure existence proof" but with "some of the
  deficiencies of such proofs".
- **No explicit good codes.** Apart from trivial cases and Hamming's
  example, no construction approaching capacity is given (§14).
- **Ergodicity and finite state.** The discrete theorems assume ergodic
  finite-state sources and channels; mixed sources are handled only by
  decomposition.
- **Continuous entropy is coordinate-dependent** (§20): Shannon notes this
  and that rates and capacities, as differences of entropies, are not.
- **Delay.** Approaching the limits generally requires long block delays
  (§§10, 14), which the theorems do not bound.

## Open questions

- Explicit codes that approach capacity (§14): left open here.
- Rates for sources and fidelity criteria other than white noise under
  mean-square error, which Part V says had been computed "in only a few
  very simple cases".
- Whether the discrete results extend beyond ergodic finite-state models
  without the decomposition into components.
