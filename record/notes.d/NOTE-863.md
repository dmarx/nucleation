---
number: 863
status: Skimmed
formerly:
- NOTE-tmp0pfk1
paper: LIT-1061
title: 'Goldreich — Foundations of Cryptography, Vol. 1 (1995 fragments): computational
  indistinguishability and pseudorandom generators'
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read on 2026-10-15 from the author's draft, not from the 2001 Cambridge text.
    No open copy of the printed volume exists: Unpaywall and OpenAlex both report
    DOI 10.1017/CBO9780511546891 as closed, with no OA or repository location. Goldreich's
    own pages (www.wisdom.weizmann.ac.il/~oded/foc-book.html, foc-drafts.html, foc.html,
    frag.toc.html) could not be fetched from this environment: the proxy got an
    empty reply or a 502/503. The Internet Archive's availability API reports a
    capture of foc-book.html dated 2026-10-05, but web.archive.org and archive.ph
    reset every connection from here and WebFetch refuses web.archive.org, so the
    capture could not be opened. The copy used is the one Goldreich posted through
    ECCC, the Electronic Colloquium on Computational Complexity at Weizmann. Its
    landing page is eccc.weizmann.ac.il/static/books/Foundations_of_Cryptography_Fragments_of_a_Book/
    and the PDF is eccc.weizmann.ac.il/resources/pdf/foc.pdf. The landing page is
    signed "Oded Goldreich, Tel-Aviv, February 1995" and says it gives "access to
    the old fragments that are currently superseeded by a book in preparation (by
    O.G.)". The PDF (305 pp., SHA-256 c0c6dece…08d0ac, distilled 2009-01-11 from
    main.dvi) holds two things: "Foundations of Cryptography (Fragments of a Book)",
    dated 23 February 1995 and written mainly June 1991 to November 1992, with later
    italic "Author's Notes"; and "an Additional Fragment (Nr. 1)", dated 9 February
    1996, which adds §6.10 on non-interactive zero-knowledge. This is the precursor
    of Volume 1, not the printed text. Crossref gives the printed chapters as Introduction
    pp. 1–29, Computational Difficulty pp. 30–100, Pseudorandom Generators pp. 101–183
    and Zero-Knowledge pp. 184–330. In the fragments the same chapters run pp. 11–34,
    35–84 and 85–138, with zero-knowledge numbered Chapter 6, so the printed version
    is substantially expanded and renumbered. Every section, definition and page
    number below refers to the fragments. None was checked against the printed book.
    Cambridge Core's open summary of the printed Chapter 3 keeps the same opening
    and the same order of sections 3.1–3.5, with the hybrid technique still introduced
    in §3.2.3. Text was extracted with pdftotext page by page; the extraction drops
    the fi/ff/ffi ligatures and scrambles displayed formulas, so the formulas of
    Definition 3.2, Proposition 3.3 and the statistical-difference bound of §3.3.1
    were checked against page images (PDF pp. 89, 90, 96). What was read: the front
    matter and contents; Chapter 1 in full (pp. 11–34); Chapter 2 in full (pp. 35–84),
    including the hard-core predicate results of §2.5, the expander amplification
    of §2.6, the notes and the exercises; Chapter 3 in full (pp. 85–138), including
    all proofs, notes and exercises. Not read: Chapter 6 on zero-knowledge (pp.
    143–254), the annotated 1989 reference list (pp. 263–293), and the 1996 additional
    fragment beyond its first three pages. Chapters 4, 5, 7–10 are empty stubs in
    the fragments. Every quotation below was checked by script against the extracted
    text, after normalising whitespace and removing ligature residue on both sides.
date: '2026-10-15'
summary: >-
  In the 1995 draft of Volume 1, computational indistinguishability is a strictly
  coarser equivalence than statistical closeness, and the book proves this two ways.
  Proposition 3.3 does it unconditionally: a counting argument shows there are ensembles
  supported on at most 2^(n/2) strings that no circuit of size 2^(n/8) tells from
  uniform with gap 2^(−n/8) or more, but such an ensemble cannot be sampled efficiently.
  §3.3.1 shows that the output of any pseudorandom generator is statistically far
  from uniform yet, by definition, indistinguishable from it. That witness is efficiently
  samplable, and it needs pseudorandom generators, which exist if and only if one-way
  functions do (Theorem 3.29, stated without proof). That efficient post-processing
  preserves indistinguishability is set as Exercise 1 of §3.8.4, not proved in the
  text. All of this is asymptotic, about ensembles indexed by n, not about single
  pairs of distributions.
---

# NOTE-863: Goldreich — Foundations of Cryptography, Vol. 1 (1995 fragments): computational indistinguishability and pseudorandom generators

## Contribution

The book builds cryptography on complexity theory. It replaces "the ciphertext contains no information" with "the information cannot be efficiently extracted". It then supplies the definitions that make this precise: negligible functions, probabilistic polynomial-time adversaries, one-way functions and hard-core predicates (Chapter 2), and computational indistinguishability, pseudorandom generators and pseudorandom functions (Chapter 3). Chapter 3 opens by naming the stance. Against Kolmogorov's "ontological" approach to randomness, it takes a "behavioristic" one: "The underlying postulate is that objects that cannot be told apart by efficient procedures are considered equivalent, although they may be very different in nature". Section 3.2 puts it as: "Objects are considered to be computationally equivalent if they cannot be told apart by any efficient procedure."

## Key insight

Equivalence is fixed by the class of tests allowed. If the class is all tests, the equivalence is statistical closeness. If it is the tests a probabilistic polynomial-time machine can run, the equivalence is much coarser. Two ensembles can differ on a statistic that is defined but not efficiently computable, such as membership in the support of one of them, and still agree on every statistic that can be computed. Of the separating test after Proposition 3.3 the book says "yet f is (necessarily) impossible to compute in polynomial-time." A pseudorandom generator is a deterministic, efficient way of producing such a pair.

## Assumptions

- **Efficient means probabilistic polynomial time.** The "Thesis" of §1.3.2 states this. Non-uniform polynomial size (circuits) is used only "in the negative way", to make hardness statements stronger (§1.3.3).
- **Negligible** (Definition 1.5, p. 26): μ is negligible if for every polynomial p and all sufficiently large n, μ(n) < 1/p(n). The draft writes the type as μ: ℕ → ℕ, which is a typo for a real-valued function.
- **Ensembles, not distributions.** Every indistinguishability statement is about a sequence {X_n} indexed by n (Definition 3.1), and the quantifier "for all sufficiently large n" carries it. For any single n nothing is claimed.
- **Intractability assumptions.** All positive results have the form "if ⟨assumption⟩ then ⟨consequence⟩". They are about average-case hardness, and in the present state of knowledge they cannot be had without some assumption at least as strong as NP ⊄ BPP (§1.3.4).
- **Draft status.** The author's preface says: "I expect them to be full of various mistakes ranging from spelling and grammatical mistakes to minor technical inaccuracies."

## Key results

- **Computational indistinguishability (Definition 3.2, §3.2.1, p. 88).** Ensembles X = {X_n} and Y = {Y_n} are indistinguishable in polynomial time if for every probabilistic polynomial-time algorithm D, every polynomial p and all sufficiently large n, |Pr[D(X_n, 1^n) = 1] − Pr[D(Y_n, 1^n) = 1]| < 1/p(n). The probability is over X_n or Y_n and D's coins. The definition is equivalent to a negligible distinguishing gap. A second variant is indexed by strings, for later chapters.
- **Statistical difference (§3.2.2, p. 89)** is defined as Δ(n) = Σ_α |Pr[X_n = α] − Pr[Y_n = α]|, with no factor ½. It is therefore twice total variation in the usual convention. The page image confirms that no factor ½ was lost in extraction. Statistically close means Δ is negligible, and statistically close ensembles are computationally indistinguishable (Exercise 5).
- **Proposition 3.3 (p. 89), the unconditional separation.** There is an ensemble X that is not statistically close to U = {U_n} yet is polynomial-time indistinguishable from it, with X_n supported on at most 2^(n/2) strings. The proof is a Chernoff bound plus a union bound over the at most 2^(2^(n/4)) circuits of size 2^(n/8). It shows that 2^(n/2) uniformly chosen strings fool every such circuit with gap below 2^(−n/8). The proof is non-constructive. §3.8.2: "One of the two ensembles is not constructible in polynomial-time." The notes credit Yao with the observation and Goldreich–Krawczyk with this proof: "Yao also observed that pseudorandom ensembles can be very far from uniform, yet our proof of Proposition 3.3 is taken from" [GK89a].
- **Efficiently samplable separation, iff one-way functions exist (§3.8.2, stated and cited, not proved):** "Goldreich showed that a pair of polynomial-time constructible ensembles having the above property (i.e., being both computationally indistinguishable and having a non-negligibly statistical difference) exists if and only if one-way functions exist" (G90, IPL 34, pp. 277–281).
- **Pseudorandom ensemble (Definition 3.7, p. 94):** an ensemble indistinguishable in polynomial time from a uniform ensemble {U_l(n)}.
- **Pseudorandom generator, standard definition (Definition 3.9, §3.3.2, p. 96).** A deterministic polynomial-time G with an expansion factor l(n) > n such that |G(s)| = l(|s|) for all s, and {G(U_n)} is pseudorandom. The general Definition 3.8 asks only |G(s)| > |s|. Stretch 2n is the case l(n) = 2n, which the book uses in Proposition 3.13 and in the GGM construction (3.33). By Theorem 3.11 (Construction 3.10, a hybrid argument), a generator with l(n) = n + 1 yields one with any polynomial stretch. So for existence, the choice between stretch n + 1, 2n and p(n) does not matter.
- **The counting bound (§3.3.1, p. 95).** The output of a pseudorandom generator "must be polynomial-time indistinguishable from uniform, although it cannot be uniform (or even statistically close to uniform)." The displayed computation is Σ_x |Pr[U_l(n) = x] − Pr[G(U_n) = x]| ≥ Σ over x outside the image {G(s)} of the same terms, which equals (2^l(n) − 2^n)·2^(−l(n)), which is at least ½. The "=" should strictly be "≥" when G is not injective on {0,1}^n. The book states only the bound ½ for general l ≥ n + 1.
- **The same counting inside a proof (Proposition 3.13, p. 101).** If G has l(n) = 2n, then f(x, y) = G(x) is strongly one-way. The distinguisher accepts when an inverter finds a preimage, and at most 2^n "different 2n-bit long strings have a preimage under f", so on U_2n it accepts with probability at most 2^(−n).
- **Post-processing (§3.8.4, p. 132).** Exercise 1 is "computational indistinguishability is preserved by efficient algorithms": if {X_n} and {Y_n} are polynomial-time indistinguishable and A is probabilistic polynomial-time, then {A(X_n)} and {A(Y_n)} are too. Exercise 2 is the statistical analogue: "statistical closeness is preserved by any function". Exercises 10–11 ask whether h(G(s)) is still a generator when h is an efficiently computable permutation (yes) and when h need not be efficiently computable (left open for the reader, with a hint to assume one-way permutations).
- **Repeated samples (Theorem 3.6, p. 91).** If two efficiently constructible ensembles are indistinguishable, their polynomial products are too. The proof is the hybrid argument. Without constructibility the multi-sample statement is given for circuits only (Exercise 7).
- **Existence (§§3.4–3.5).** One-way permutation plus hard-core predicate gives a generator G(s) = f(s)b(s) (Theorem 3.14). Every one-way function g(x, r) = (f(x), r) has the inner-product hard-core bit (Theorem 2.15, Goldreich–Levin, in Rackoff's proof). 1-1 one-way functions suffice (Theorem 3.23), as do regular ones (Theorem 3.28). For arbitrary one-way functions (Theorem 3.29, Håstad–Impagliazzo–Levin–Luby) the proof is not given: "It is known that one-way functions exist if and only if pseudorandom generators exist." The converse, that a generator gives a one-way function, is Proposition 3.13.
- **Why the definition is robust (§3.3.4):** "if some efficient algorithm suffers noticeable degradation in performance when replacing the random sequences it uses by pseudorandom one, then this algorithm can be easily modified into a distinguisher".

## Bearing on the record

For [CASE-083](../cases.d/CASE-083.md), all four things the record leans on are in the book, in the fragments' numbering.

1. **Indistinguishability.** Computational indistinguishability is Definition 3.2.
2. **The generator.** A secure generator G: {0,1}ⁿ → {0,1}²ⁿ with negligible advantage for every probabilistic polynomial-time distinguisher is Definition 3.9 with l(n) = 2n, read through Definitions 3.2 and 3.7.
3. **Post-processing.** That efficient common post-processing preserves indistinguishability is Exercise 1 of §3.8.4. It is set as an exercise, not proved, and the proof is the one-line composition A15 gives.
4. **The counting point.** The statistical separation is the computation of §3.3.1, which the book states only as a lower bound of ½. The record's sharper bound follows from the same displayed line with l = 2n: Pr[U₂ₙ ∈ image(G)] ≤ 2ⁿ/2²ⁿ, so under the usual convention TV = max over sets A of |P(A) − Q(A)| ≥ 1 − 2⁻ⁿ. The same 2⁻ⁿ count appears verbatim in the proof of Proposition 3.13.

The record's TV is the usual one, half the book's Δ. In the book's convention the bound reads Δ ≥ 2(1 − 2⁻ⁿ). The record's statement is correct as written, but a reader moving between the two should know they differ by a factor of 2.

This reading narrows [CLAIM-302](../claims.d/CLAIM-302.md) in two places, and in one place strengthens it.

- **Strengthens: the separation does not need pseudorandom generators.** Proposition 3.3 proves without any assumption that there are ensembles almost disjoint from uniform that no polynomial-time test, or even any circuit of size 2^(n/8), tells apart. X_n is supported on at most 2^(n/2) strings, so in the record's convention TV ≥ 1 − 2^(−n/2). What needs an assumption is that the far-but-indistinguishable pair be efficiently samplable. That holds if and only if one-way functions exist (G90, cited in §3.8.2). So the claim's headline, "equivalence under feasible tests can be much coarser than statistical equivalence", is unconditional. Its `defeated_if` overstates what the non-existence of secure generators would do. That would remove only the efficiently constructible witness. Proposition 3.3's witness would remain.
- **Narrows: the objects are ensembles, not pairs.** The claim speaks of "pairs of distributions … that no efficient test tells apart". In the book, "efficient" and "negligible" have meaning only for a sequence indexed by n. For any fixed n, the test "is y in G's image" is a finite circuit, of size exponential in n, that separates G(Uₙ) from U₂ₙ almost perfectly. [CASE-083](../cases.d/CASE-083.md) writes "≤ negl(n)", which is right. The claim's wording should read "families of pairs indexed by n" or "ensembles".
- **Narrows: the generator is not exhibited.** The book does not show that any particular G is secure. Theorem 3.29 gives existence from any one-way function, and the existence of one-way functions is itself an assumption that implies P ≠ NP (Chapter 2, Exercise 2). This matches the claim's own conditional, and [CASE-083](../cases.d/CASE-083.md)'s quotation of A15 says the same.

For [CLAIM-304](../claims.d/CLAIM-304.md), the book supplies the ingredients but not the construction. The rendering of a bit as G(Uₙ) or U₂ₙ is the record's own. The reduction is sound by Definition 3.2: a receiver that guesses a uniform b with probability ½ + ε is a distinguisher with gap 2ε. The book makes the same kind of predictor-to-distinguisher conversion in the proof of Theorem 3.14 and in Exercises 14–15.

Two cautions on wording:

- **"Than chance".** "No efficient receiver does better than chance" should read "no efficient receiver does non-negligibly better than chance". The guarantee is asymptotic.
- **"Error at most 2⁻ⁿ".** The unbounded receiver's error is conditional on b = 0. With a uniform prior on b, its overall error is at most 2⁻ⁿ⁻¹.

The caveat in [CLAIM-302](../claims.d/CLAIM-302.md) that the gap depends on the representation, since an expensively computed label makes the pair separable, is close to Exercise 11 of §3.8.4. That exercise asks whether a generator stays a generator under a permutation that is not efficiently computable. The book's position is the claim's: the equivalence is relative to what can be computed, and the separating statistic after Proposition 3.3 is "(necessarily) impossible to compute in polynomial-time".

The LIT entry's summary describes the printed volume correctly as to topics. Its claim that the book supplies the definitions the record codes rest on is confirmed. All of this is from the 1995 draft. The printed 2001 text expands each chapter by roughly a half to three quarters in pages. It may state these results with different numbering (the printed chapter is pp. 101–183) and possibly a different statistical-difference convention. That was not checked.
