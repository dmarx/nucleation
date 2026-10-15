---
status: Read
paper: LIT-tmp10av1
title: Håstad, Impagliazzo, Levin & Luby — A pseudorandom generator from any one-way
  function
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full from the authors' copy that Johan Håstad posts on his KTH page
    (www.csc.kth.se/~johanh/prgfromowf.pdf, linked from ~johanh/papers.html as "SIAM
    Journal on Computing, Vol 28, 1999, pp 1364--1396"), fetched 2026-10-15. It
    is a 46-page A4 typescript with the authors' own warning that "Essentially this
    paper has been published in SIAM Journal on Computing"; it is not the typeset
    SIAM version, and its section, theorem and page numbers were not checked against
    the printed pages 1364–1396. Searched first: Unpaywall reports the DOI closed
    with no OA location; OpenAlex reports it closed, listing the DOI and two CiteSeerX
    records (10.1.1.35.3930, 10.1.1.36.6283, both submittedVersion); a guessed Berkeley
    path for Luby (people.eecs.berkeley.edu/~luby/PAPERS/hill.ps) gave 404; Håstad's
    KTH copy returned 200 and is the one used. Text extracted with pdftotext -layout;
    the extraction drops ligatures ("de nition") and most mathematical symbols (≥,
    ⊕, ⊙, ∈), so Definitions 3.1.1, 3.2.1, 3.3.1, 3.3.3, 3.4.1–3.4.3 and Theorem
    6.2.2 were checked against page images (pp. 12–15, 33). PyMuPDF gave worse text
    and was not used. Read: all eight sections, every definition, proposition, lemma,
    theorem and proof, including the proof of Lemma 6.3.2 and the direct construction
    of Section 7, and the reference list. Proofs of results the paper imports (Goldreich–Levin,
    Proposition 4.1.2; Goldwasser–Micali's hybrid, Proposition 4.6.2; Shannon's
    Proposition 4.5.2) are not given in the paper and were not read. Goldreich's
    note [G : 89] (LIT-tmp5gb4p) was not read; what it shows is known here only
    through this paper's one-sentence account in Section 8. Every quotation from
    the paper below was checked against the extracted text by script, with whitespace
    and punctuation normalised and the extraction's dropped "fi"/"ff" ligatures
    allowed for; the four that contain formulas (Definitions 3.2.1, 3.3.3, 3.4.1
    and the sentence on 1/sp′ trials) cannot match the garbled extraction and were
    checked by eye against the page images, and the two sentences containing f′
    matched once the extraction's rendering of the prime as "0" was allowed for.
    Phrases quoted from the record were checked against the record files.
date: '2026-10-15'
summary: >-
  There is a pseudorandom generator if and only if there is a one-way function (Theorem
  6.2.2), in the uniform setting: adversaries are algorithms, and every reduction
  is an oracle Turing machine that turns an adversary for the constructed generator
  into an inverter for the given function. The route runs one-way function → false
  entropy generator → pseudoentropy generator → pseudorandom generator, where "computational
  entropy" is the Shannon entropy of some P-samplable distribution that no adversary
  of the given strength tells apart from the output. The general reduction is only
  weak-preserving: composed literally it needs seeds of length n^34, and the paper's
  direct construction n^10. The paper attributes to Goldreich [G : 89] the equivalence
  of pseudorandom generators with P-samplable pairs that are computationally indistinguishable
  but statistically very different; with Theorem 6.2.2 that gives the one-way function
  form, but the paper never writes that combined sentence.
---
<!-- inactive-ok-file: CLAIM-199 — Proposed; open claims and accounts cited as open, nothing here rests on their being settled -->
<!-- inactive-ok-file: LIT-tmp5gb4p — Unavailable; held without a reading, cited as such -->

# NOTE-tmpscadg: Håstad, Impagliazzo, Levin & Luby — A pseudorandom generator from any one-way function

## Contribution

Before this paper pseudorandom generators were known from one-way permutations (Yao; Goldreich–Levin), from one-way functions that stay one-way under iteration (Levin), and from regular one-way functions (Goldreich, Krawczyk and Luby). "However, the general question of how to construct a pseudorandom generator from a one-way function with no structural properties was left open. This paper resolves this question." It combines the conference papers of Impagliazzo, Levin and Luby (STOC 1989), which gave a non-uniform reduction, and Håstad (STOC 1990, "Pseudo-Random Generators under Uniform Assumptions"), which made it uniform. The paper also introduces computational entropy, pseudoentropy generators and false entropy generators as intermediate primitives, and a quantitative account of how much security a reduction preserves.

## Key insight

A generator need not look uniform at first; it is enough that its output looks as if it had more entropy than it really has. "We say the computational entropy of g(X) is at least the Shannon entropy of Y if g(X) and Y are computationally indistinguishable." Once some output carries entropy that efficient observers cannot tell from the real thing, independent copies and universal hashing turn that surplus into bits that look uniform. The construction gets the surplus from a one-way function by hashing out about as many bits of the input as the function loses (its degeneracy), so that the Goldreich–Levin bit x·y is hidden and yet almost determined by the rest of the output. A determined bit that looks random is false entropy.

## Assumptions

- **Asymptotic, over ensembles.** "We present all of our definitions and results in asymptotic form." Lengths are polynomial parameters of n, and every distribution is a probability ensemble indexed by n (Definitions 2.3.1–2.3.7).
- **Security as a time–success ratio.** An adversary is "a function ensemble"; its time-success ratio is R = T_n/sp_n(A), T_n "the worst case expected running time of A over all instances parameterized by n", sp_n(A) its success probability. A primitive is R-secure if there is no R-breaking adversary (Definition 3.1.1). The paper calls this a refinement of the convention in which "an adversary was considered to be breaking if it ran in polynomial time and had inverse polynomial success probability." The unqualified "one-way function" and "pseudorandom generator" of Theorem 6.2.2 are not given separate definitions; they are read as security against all polynomial ratios.
- **Uniform adversaries and uniform reductions.** Adversaries are by default uniform: a "mildly non-uniform adversary" is one given the advice a_n, and its success measures are "the same as for uniform adversaries." A reduction (Definition 3.6.1) is a pair of oracle Turing machines (g^(·), M^(·)): g^(f) builds the new primitive from f, and M^(A) turns any adversary A against g^(f) into one against f. No circuits appear anywhere in the paper; it has no definition of non-uniform one-way function. Because M is a fixed oracle machine, the proofs would carry over to non-uniform adversaries, but the paper does not say so.
- **Samplability is load-bearing.** The step from one copy to many (Proposition 4.6.2, after Goldwasser and Micali) needs both distributions P-samplable: "It is crucial that D and E are P-samplable because the sampling algorithms are used by M." This is why computational entropy is defined with a P-time f′ (Section 3.4, quoted below).
- **Mild non-uniformity, removed at the end.** Intermediate constructions need a quantity that may not be computable in polynomial time (an approximation of H(f(X)), or of p_n = Pr[I ≤ D̃_f(f(X))]), supplied as advice taking polynomially many values. Proposition 4.8.1 removes it by XORing the generators for every candidate value.
- **Shannon and Rényi entropy only.** Entropy is Shannon's (Definition 2.2.1); Rényi (collision) entropy is used for hashing (Definition 2.2.2, Lemma 4.5.1), and Shannon entropy is converted to Rényi entropy by taking many independent copies (Proposition 4.5.2). Min-entropy does not appear.
- **Statistical distance** is total variation: L1(D, E) = Σ_x |D(x) − E(x)|/2 (Definition 2.1.1).

## Key results

Definitions (exact):

- **Statistical distance (2.1.1)**: as above, with the factor ½. Proposition 2.1.2: no function increases it.
- **One-way function (3.2.1).** "Let f : {0,1}^t_n → {0,1}^ℓ_n be a P-time function ensemble and let X ∈_U {0,1}^t_n. The success probability of adversary A for inverting f is sp_n(A) = Pr[f(A(f(X))) = f(X)]. Then, f is a R-secure one-way function if there is no R-breaking adversary for f." Inversion means finding any preimage. There is one definition, for uniform adversaries; the only variant is the mildly non-uniform one (advice a_n), not a circuit version.
- **Computationally indistinguishable (3.3.1).** Success probability sp_n(A) = |Pr[A(X) = 1] − Pr[A(Y) = 1]|; "D and E are R-secure computationally indistinguishable if there is no R-breaking adversary for distinguishing D and E." The paper introduces it as "the computationally restricted adversary definition of statistical distance." An alternative (3.3.2) squares the success probability, "because it takes 1/sp′_n(A) trials in order to approximate sp_n(A) to within a constant factor."
- **Pseudorandom generator (3.3.3).** "Let g : {0,1}^t_n → {0,1}^ℓ_n be a P-time function ensemble where ℓ_n > t_n. Then, g is a R-secure pseudorandom generator if the probability ensembles g(U_t_n) and U_ℓ_n are R-secure computationally indistinguishable." One bit of stretch suffices; Proposition 3.3.4 (Goldreich–Micali) stretches to any polynomial length, linear-preserving.
- **Computational entropy (3.4.1).** "f has R-secure computational entropy s_n if there is a P-time function ensemble f′ : {0,1}^m_n → {0,1}^ℓ_n such that f(U_t_n) and f′(U_m_n) are R-secure computationally indistinguishable and H(f′(U_m_n)) ≥ s_n." H is Shannon entropy, and the comparison distribution must be P-samplable.
- **Pseudoentropy generator (3.4.2).** f has pseudoentropy s_n if f(U_t_n) has computational entropy t_n + s_n: more than its input. Every pseudorandom generator is one with pseudoentropy at least 1.
- **False entropy generator (3.4.3).** f has false entropy s_n if f(U_t_n) has computational entropy H(f(U_t_n)) + s_n: more than its own output. "A false entropy generator doesn't necessarily amplify the input randomness, it just has the property that the output randomness is computationally more than it is statistically."
- **Non-uniform computational entropy.** "There is also a non-uniform version of computational entropy where f′ is not necessarily P-time computable." It is easier to get from a one-way function, and with it [ILL : 89] "describe a non-uniform reduction from a one-way function to a pseudorandom generator. However, a uniform reduction using Proposition 4.6.2 requires that f′ be P-time computable." Here "non-uniform" refers to the comparison distribution, not to the adversaries.
- **Hidden bit (3.5.1).** b(X) is hidden given f(X) if ⟨f(X), b(X)⟩ and ⟨f(X), β⟩, β a uniform bit, are computationally indistinguishable.

Theorems:

- **Proposition 4.1.1 (Goldreich–Levin).** For a one-way f, X·R (inner product mod 2) is hidden given ⟨f(X), R⟩.
- **Proposition 4.3.1.** For a one-to-one one-way f, g(x, r) = ⟨f(x), r, x·r⟩ is a pseudoentropy generator with pseudoentropy 1, but need not be a pseudorandom generator (example f(x) = ⟨0, f′(x)⟩).
- **Lemma 4.5.1 (leftover hashing).** If D has Rényi entropy at least m_n and h is a universal hash to m_n − 2e_n bits, then L1(⟨h_Y(X), Y⟩, ⟨Z, Y⟩) ≤ 2^−(e_n+1).
- **Proposition 4.6.2.** For P-samplable D and E, computational indistinguishability of one copy gives it for k_n copies; weak-preserving.
- **Theorem 4.6.4.** Pseudoentropy generator → pseudorandom generator (hash k_n copies of f, Construction 4.6.3). Weak-preserving.
- **Lemma 4.7.2.** False entropy generator → mildly non-uniform pseudoentropy generator with pseudoentropy 1. Weak-preserving.
- **Proposition 4.8.1.** Mildly non-uniform → uniform pseudorandom generator. Weak-preserving.
- **Theorem 5.1.4.** A pseudorandom generator from a one-way function whose approximate preimage size D̃_f is P-time computable. Theorem 5.1.5: from any α_n-regular one-way function (earlier result of Goldreich, Krawczyk and Luby).
- **Theorem 6.2.1.** For any one-way f, the g of equations (1)–(8) "is a mildly non-uniform false entropy generator with false entropy 10n^2. The reduction is weak-preserving." The key steps are Lemma 6.1.1 (with i ≤ D̃_f(f(x)) the bit x·y looks random given f′ and y), Lemma 6.3.1 (H(E) ≥ H(D) + 10n²) and Lemma 6.3.2, whose oracle machine distinguishes the hidden bit with probability at least δ_n/(16k_n) by a non-standard hybrid that cannot sample the set T directly and instead keeps the sample that maximises A's estimated advantage.
- **Theorem 6.2.2 (main).** "There are one-way functions iff there are pseudorandom generators." Proof: the forward direction "follows from [Levin : 87]"; the converse from Theorem 6.2.1 and the reductions of Section 4. Under the paper's definitions this is a statement about uniform adversaries, proved by uniform (oracle Turing machine) reductions, with the mild non-uniformity removed by Proposition 4.8.1.
- **Theorem 7.0.5 (direct construction).** A mildly non-uniform pseudorandom generator from any one-way function with seed length O(n^7), O(n^10) after removing non-uniformity. Composing the reductions of Sections 4–6 literally gives seed length n^34. "A sharper analysis can reduce this to n^8."
- **Efficiency.** "the reduction for general one-way functions is only weak-preserving": security R′ against seeds of length n^O(1) only implies security about R′^O(1) for f on length n, so a generator from a one-way function secure at length n is secure only at much greater length. Poly-preserving reductions exist for regular or nearly regular one-way functions (Luby 1996).
- **On samplable statistically-far ensembles (Section 8).** "Using the notion of a false entropy generator, [G : 89] shows that the existence of pseudorandom generators is equivalent to the existence of a pair of P-samplable distributions which are computationally indistinguishable but statistically very different." [G : 89] is cited as "ICSI Tech Report TR-89-051, July 1989." The paper does not prove this, does not quantify "very different", and does not restate it with one-way functions; combined with Theorem 6.2.2 it yields that form.

## Bearing on the record

**On [LIT-tmp5gb4p](../literature.d/LIT-tmp5gb4p.md).** This paper supports the reading of Goldreich's note recorded in [LIT-tmp5gb4p](../literature.d/LIT-tmp5gb4p.md)'s status_note (from an unchecked search summary): by HILL's account, [G : 89] proves equivalence with *pseudorandom generators*, using false entropy generators. The book's "if and only if one-way functions" (as [LIT-tmp5gb4p](../literature.d/LIT-tmp5gb4p.md)'s summary and [CLAIM-tmpvdl53](../claims.d/CLAIM-tmpvdl53.md) report it) is that equivalence composed with this paper's Theorem 6.2.2; HILL implies it but does not state it in one sentence. Two details for the entry: HILL cites the note as ICSI technical report TR-89-051, July 1989, not a Technion report of January 1990 as the search summary said (the two may both exist; neither is checked here); and the samplable pair is "statistically very different", with no bound given. Since one direction of Goldreich's result (generators give such a pair) is the elementary counting argument [CLAIM-tmpvdl53](../claims.d/CLAIM-tmpvdl53.md) already uses, the substantive content attributed to him is the converse: a samplable indistinguishable pair far apart in statistical distance yields a false entropy generator and hence, through Section 4 of this paper, a generator.

**On [CLAIM-tmpvdl53](../claims.d/CLAIM-tmpvdl53.md).** Supports and sharpens it; nothing contradicts it.
- Its condition "if pseudorandom generators exist" can be stated as "if one-way functions exist" on the strength of Theorem 6.2.2, in the uniform setting the paper works in. The claim's own wording, which needs only the generator direction, is correct as it stands.
- The paper's statistical distance carries the factor ½, so it is total variation, matching the claim's TV(P_n, Q_n) ≥ 1 − 2^−n.
- The paper's own gloss on computational indistinguishability, "the computationally restricted adversary definition of statistical distance", is the claim's thesis in one phrase: the same sup over tests, restricted to a feasible class.
- Proposition 4.6.2 shows why the samplable half is the stronger one: indistinguishability survives polynomially many independent samples only when both ensembles are P-samplable, because the reduction runs the samplers. The unconditional Goldreich–Krawczyk ensemble in the claim is not samplable, so nothing here says it stays indistinguishable under repeated sampling.

**On [CLAIM-tmpzk2fj](../claims.d/CLAIM-tmpzk2fj.md).** Consistent; adds a measure for the gap the claim constructs.
- The receiver's rendering is G(U_n) versus U_2n. In this paper's terms, G(U_n) has Shannon entropy at most n and computational entropy 2n (witness f′ the identity on U_2n, which is P-time), so it is a false entropy generator with false entropy at least n. A18's "Recoverable in principle ≠ recoverable within budget" is, in this vocabulary, the gap between statistical and computational entropy. This is the record's application of Definitions 3.4.1 and 3.4.3, not a statement of the paper.
- "If pseudorandom generators exist" can again read "if one-way functions exist" (Theorem 6.2.2).
- The guarantee is asymptotic and, for generators built from an arbitrary one-way function, quantitatively weak (weak-preserving, seeds n^10). The claim relies on no particular generator, so this narrows nothing in it, but any concrete instance would come from a structured function, not this construction.

**On [QUESTION-tmprdpkh](../questions.d/QUESTION-tmprdpkh.md) (recovery complexity).** The paper supplies a worked instance of what the question asks for, with one difference of form.
- Its security measure is a cost of recovery relative to a task and a success criterion: the time-success ratio T_n/sp_n(A), minimised over adversaries (Definition 3.1.1). The task is fixed per primitive (find a preimage; tell two ensembles apart), the cost model is expected running time, and the success criterion is folded into the ratio rather than fixed as an error bound ε. A18's C_ε(D | M) fixes ε and minimises cost; the paper trades the two in one number, and offers a second exchange rate (success squared, Definition 3.3.2) when success must be estimated by sampling.
- Computational entropy is the candidate the question's summary in [QUESTION-tmpadry4](../questions.d/QUESTION-tmpadry4.md) points to, but in this paper it is relative to three things the question asks to have fixed: a security level R, a uniform model of computation, and a samplable comparison distribution. It is Shannon entropy, not min-entropy; the version usually cited under the name HILL entropy, with circuit adversaries and min-entropy, is not the definition this paper gives; it was not checked here where that version comes from. A definition built on it inherits its asymptotic form.
- The paper's reductions measure how recovery cost transfers between representations: linear-, poly- and weak-preserving (Definition 3.6.1) say how a cost bound for one primitive becomes one for another. That is a ready vocabulary for the question's requirement that the definition place [CLAIM-199](../claims.d/CLAIM-199.md)'s and [CLAIM-tmpzk2fj](../claims.d/CLAIM-tmpzk2fj.md)'s cases on one scale, though the paper offers nothing for rule-class restrictions like [CLAIM-199](../claims.d/CLAIM-199.md)'s.

**On [QUESTION-tmpadry4](../questions.d/QUESTION-tmpadry4.md).** Supports the formal half; silent on the empirical half.
- Definition 3.3.1's success probability |Pr[A(X)=1] − Pr[A(Y)=1]| is the record's hit rate minus false-alarm rate for a one-bit observer, and the paper presents indistinguishability as the restricted-adversary form of statistical distance. So the correspondence in the question's formal link is the paper's own framing.
- The alternative definition (3.3.2) rests on a sampling cost: about 1/sp² trials to estimate an advantage sp. That is the same arithmetic as estimating a small d′ in psychophysics, and it is the nearest the paper comes to an empirical measure. It says nothing about ideal-observer efficiency, criterion, or real observers.
- Indistinguishability here is criterion-free in the sense the question asks about: it is a bound on every test's advantage, so no criterion shift has a counterpart within a single adversary's definition.
- The record's summary of the work in [LIT-tmp10av1](../literature.d/LIT-tmp10av1.md) ("a distribution with more entropy than it has, as far as efficient observers can tell") describes false entropy. Pseudoentropy in this paper is more entropy than the generator's *input*; the two notions are distinct and the paper needs both.
