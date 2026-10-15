---
status: Read
paper: LIT-tmpoyjmt
title: Dwork, Kim, Reingold, Rothblum & Yona — Outcome Indistinguishability
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full on 2026-10-15 from the arXiv preprint, arXiv:2011.13426v1 (arxiv.org/pdf/2011.13426,
    61 pp.: 59 numbered pages plus title and contents), submitted 26 November 2020
    by Michael P. Kim. The arXiv listing shows v1 as the only version, so v1 is
    the latest arXiv version. The STOC 2021 version of record (doi:10.1145/3406325.3451064)
    was not read. Unpaywall lists it as green open access, with only submitted-version
    copies: the arXiv PDF and an MIT DSpace copy. Differences between v1 and the
    proceedings text are not known. Text extracted with pdftotext (layout and raw
    modes). The extraction scatters sub- and superscripts in displayed formulas,
    so the bounds below were read from the layout text with that in mind, not from
    page images. Read: §1 (introduction, contributions, technical overview, related
    work), §2 (definitions of the four levels, Proposition 2.5 on lunchtime distinguishers,
    multi-sample OI and Proposition 2.8), §3 (prediction indistinguishability, Propositions
    3.2 and 3.4), §4 (Theorems 4.3 and 4.4 with proofs), §5 (Algorithm 1, Lemma
    5.1, Theorems 5.2, 5.4, 5.7, 5.9, 5.10, §5.4 on samples and run time), §6 (Definition
    6.2, Proposition 6.3, Theorem 6.4 with Claims 6.5–6.6, Theorem 6.7, Corollaries
    6.9 and 6.11), and the reference list. The proofs in §§2–5 and of Claims 6.5–6.6
    were followed line by line. The recurrence algebra in the proofs of Theorems
    5.9 and 5.10 and the proof of Proposition 6.3 (Goldreich–Levin) were checked
    only for structure, not step by step. Theorems 6.8 and 6.10 are imported from
    Goldreich–Rothblum 2018 and Trevisan–Vadhan 2007 and were taken as cited. Nothing
    else was skipped. Every quotation of the paper below was checked by script against
    the extracted text, with whitespace, Unicode composition and quotation-mark
    style normalised. The one quotation of the record (A14, by way of QUESTION-tmpdzpy2)
    was checked the same way against that entry.
date: '2026-10-15'
summary: >-
  A predictor p̃ is outcome indistinguishable (OI) relative to a class A of distinguishers
  when no A ∈ A can tell an individual with Nature's outcome from the same individual
  with an outcome drawn from Ber(p̃_i). The paper sets out four levels by how much
  access the distinguisher has to p̃: none, the prediction on the sampled individual,
  oracle queries, or the code. The lower two levels are equivalent to multi-accuracy
  and multi-calibration over closely related classes. At those levels OI predictors
  exist with size O(s/ε²), whatever Nature's complexity. At the oracle level, under
  fine-grained hardness of clique counting or BPP ≠ PSPACE, some efficient distinguisher
  classes force any OI predictor to be nearly as expensive as Nature's own predictor.
  That gives a strict separation between oracle access and sample access. OI never
  requires p̃ ≈ p*. A predictor is good only relative to A, and with the paper's
  construction a weak A gives a coarse predictor that a richer A would refute. The
  paper covers binary outcomes, a fixed representation of individuals and single
  samples (multi-sample OI is left mostly to future work).
---

# NOTE-tmpvwapz: Dwork, Kim, Reingold, Rothblum & Yona — Outcome Indistinguishability

## Contribution

The paper asks what a predicted individual probability can mean when an outcome is not a repeated event. Its answer is a standard taken from complexity theory and cryptography. A predictor defines a generative model, i ∼ D_X and then õ_i ∼ Ber(p̃_i). The predictor is acceptable if a stated class of observers cannot tell that model's samples from Nature's. "predictors satisfying OI give rise to models of Nature that cannot be falsified based only on observational data." The contributions, as the paper lists them, are:

- a four-level hierarchy of OI by the distinguisher's access to p̃;
- tight equivalences between the two lower levels and multi-accuracy and multi-calibration (Hébert-Johnson, Kim, Reingold and Rothblum 2018, [LIT-tmp1vdb9](../literature.d/LIT-tmp1vdb9.md));
- a direct construction of OI predictors at every level, with complexity bounds that do not depend on Nature;
- conditional lower bounds showing that the upper levels cannot have predictor complexity polynomial in the distinguishers' complexity and 1/ε.

It also separates "tests" in the forecasting sense from "distinguishers" in the complexity sense, and studies a stronger notion, prediction indistinguishability (PI).

## Key insight

Being a good predictor is a property relative to a class of observers, not closeness to the truth. If no efficient observer can tell which individuals Nature sends to 1 and which to 0, then p̃ ≡ 1/2 "captures the best computationally feasible understanding of Nature". The same predictor would fail against an unbounded class: over all subsets of X, no-access-OI already forces statistical closeness to p*. The paper turns this round against pseudorandomness. There a simple deterministic object fools observers who expect randomness. Here "a simple random model of Nature—namely, D(p̃) for an OI predictor p̃—suffices to 'fool' efficient observers", whatever Nature's deterministic laws are. The second insight is that what an observer can see depends on its access as well as its budget. A distinguisher that can query p̃ adaptively can use p̃ itself as a subroutine for expensive computations, so a cheap auditor can force a predictor to be as expensive as Nature.

## Assumptions

- **Binary outcomes and a fixed, discrete representation.** X ⊆ {0,1}^d, Y = {0,1}. Nature is a joint distribution D* on X × Y. p*_i = Pr[o*_i = 1 | i] may be 0 or 1. "we make no assumptions about p∗ other than it defines a valid conditional probability distribution", and it "need not come from any realizable or learnable class of functions". Distinguishers and predictors see only the representation. "Generally, we assume that the representation of individuals is fixed and informative."
- **Single-sample distinguishers** throughout, except in §2.2. Multi-sample OI is defined there but "We leave full exploration of multi-sample-OI to future work".
- **Discretised predictors.** p̃ has finite support. Multi-calibration and its equivalence are stated for the rounding p̃^{1/m} to a grid of m bins.
- **Concrete models of computation for the bounds.** Distinguishers are size-s bounded fan-in circuits, or (s, q)-oracle circuits, or circuits of size s(d, n) when the input includes an n-bit description of p̃. Fixed-precision arithmetic costs w(ε) gates, with s(d) ≥ d ≥ 3w(ε).
- **Existence, not efficient learning.** The constructions in §5 show that small OI predictors exist. They are not efficient learners. Each iteration naively takes time Ω(|A|), and searching for a violated constraint needs agnostic learning (§5.4).
- **Approximate multi-calibration in the HKRR18 sense.** Error is relative to the level set's size, and level sets lighter than α/|supp_S(p̃)| within S are exempt.

## Key results

Notation: Δ_A(p) is A's distinguishing advantage, the absolute difference between its acceptance probabilities on D* and on D(p).

**The definition (Definition 2.1).** For a class of distinguishers A and ε > 0, p̃ satisfies (A, ε)-OI if for every A ∈ A, |Pr_{(i,o*_i)∼D*}[A(i, o*_i; p̃) = 1] − Pr_{(i,õ_i)∼D(p̃)}[A(i, õ_i; p̃) = 1]| ≤ ε. Here (i, õ_i) ∼ D(p̃) means i ∼ D_X and õ_i ∼ Ber(p̃_i).

**The four levels (§2.1).** They differ only in what A receives besides the sample.

- **No-access-OI (Definition 2.2).** A : X × {0,1} → {0,1} sees (i, o_i) and nothing of p̃. The guarantee is weak only because A is restricted. With the class of all subset distinguishers A_S(i, o_i) = o_i·1[i ∈ S], "the only predictors p̃ that satisfy no-access-OI will be statistically close to Nature's predictor p∗."
- **Sample-access-OI (Definition 2.3).** A sees (i, o_i, p̃_i), the prediction for the sampled individual only. It is at least as strong as no-access-OI, since A can ignore p̃_i.
- **Oracle-access-OI (Definition 2.4).** A^{p̃} sees (i, o_i) and may query p̃ on any j ∈ X, adaptively. It can simulate sample access with one query. **Proposition 2.5:** if the oracle use is non-adaptive "lunchtime" preprocessing, summarised in t advice bits, then a class of 2^t·|A| sample-access distinguishers of the same circuit size simulates it. So "the power of oracle-access distinguishers over sample-access distinguishers derives from the ability to query p̃ adaptively, based on the sample in question."
- **Code-access-OI (Definition 2.6).** A sees (i, o_i, ⟨p̃⟩), an n-bit description of a circuit for p̃. To simulate the lower levels, A's size must grow with n, so the class is parameterised by s(d, n). It is the strongest level.
- **Multi-sample OI (Definition 2.7; Proposition 2.8).** For oracle access with preprocessing samples from D*, a hybrid argument gives: (A, ε/m)-OI against single-sample size-s distinguishers implies (A_m, ε)-OI against size-s m-sample distinguishers.

**Equivalence with multi-accuracy (Theorem 4.3).** Multi-accuracy requires |E[p*_i | i ∈ S] − E[p̃_i | i ∈ S]| ≤ α for every S ∈ C (Definition 4.1).

- *MA from OI:* take A_S(i, b) = 1[i ∈ S ∧ b = 1], one per S ∈ C. Then the multi-accuracy violation equals Δ_{A_S}(p̃)/Pr[i ∈ S]. So with γ_C ≤ min_S Pr[i ∈ S] (as printed the condition reads γ_C ≥ min; the proof needs γ_C ≤ Pr[i ∈ S]), (A_C, α·γ_C)-no-access-OI implies (C, α)-multi-accuracy.
- *OI from MA:* for deterministic A, take S_{(A,b)} = {i : A(i, b) = 1}, two sets per A. Then Δ_A(p̃) ≤ ∇_{S(A,0)} + ∇_{S(A,1)}, so (C_A, ε/2)-multi-accuracy implies (A, ε)-no-access-OI.
- The two classes have essentially the same complexity, and repeating the translation reaches "a 'stable point'".

**Equivalence with multi-calibration (Theorem 4.4).** Multi-calibration requires |E[p*_i | p̃_i = v ∧ i ∈ S] − v| ≤ α for every S ∈ C and every v in the support with Pr[p̃_i = v | i ∈ S] ≥ α/|supp_S(p̃)| (Definition 4.2).

- *MC from OI:* take distinguishers A_{u,S}(i, b, v) = 1[i ∈ S ∧ b = 1 ∧ |u − v| ≤ 1/2m], m per set. Then (A_{C,m}, α²γ_C/m)-sample-access-OI of p̃^{1/m} implies (C, α)-multi-calibration.
- *OI from MC:* for deterministic A, take sets S_{A,b,u} = {i : A(i, b, u) = 1}, 2m per distinguisher. Then (C_{A,m}, ε/4)-multi-calibration of p̃^{1/m} implies (A, ε)-sample-access-OI.
- Informally: "sample-access-OI with respect to a set of distinguishers A is 'equivalent' to C-multi-calibration in the sense that each notion can enforce the other, for closely related classes C and A". The losses come from the small-set exemption and the discretisation.

**Construction (Algorithm 1; Lemma 5.1).** Start at p ≡ 1/2. While some A has Δ_A > ε, update p ← π_[0,1](p + (Δ_A/2)·δ_A), with δ_A(·) = A(·, 1; p) − A(·, 0; p). At the oracle and code levels, A is run against the current p^(t), which removes the apparent circularity. The potential E[(p*_i − p_i)²] falls by at least 3ε²/4 per update, so the algorithm stops after T = O(1/ε²) updates. The paper calls it a variant of boosting or gradient descent, after Trevisan–Tulsiani–Vadhan 2009 and HKRR18.

**Upper bounds on predictor size.** None depends on p*.

| Level | Distinguisher class | OI predictor circuit size |
|---|---|---|
| No-access / sample-access (Thm 5.2) | size s | O(s/ε²) |
| Oracle-access (Thm 5.4) | (s, q)-oracle circuits | s · q^{O(1/ε²)} |
| Code-access, sublinear (Thm 5.7) | s(d) + (n/log n)^δ, δ < 1 | O(s(d) · ε^{−2/(1−δ)}) |
| Code-access, quasilinear (Thm 5.9) | s(d) + s·(log s)^c | s(d)·q^{O(1/ε²)}·(1/ε)^{O(1/ε²)}·(log(s(d)q))^{O(1/ε²)} |
| Code-access, polynomial (Thm 5.10) | (s(d) + n)^k | s(d)^{2^{O(1/ε²)}} |

The introduction states the last bound as d^{2^{O(1/ε²)}}. Learning from samples (§5.4): naive resampling uses Ω(log(|A|/δε)/ε⁴) samples in total, and HKRR18's adaptive-data-analysis methods do better.

**Lower bounds: separation of oracle access from sample access (§6).**

- *Theorem 6.4 (generic).* Take an ensemble of Boolean functions f_1, …, f_m. It must have "scalable hardness" (Definition 6.2): each is harder than the last, there is a downward self-reduction from f_i to f_{i−1}, and there is a worst-to-average-case random self-reduction with error rate µ ≤ 0.06. Nature puts p*(i, x) = f_i(x) on disjoint blocks, uniform over i. Distinguisher A_i checks o = f_i(x) by running the downward self-reduction, answering its queries through the random self-reduction applied to the rounded p̃ on block i−1. Then any p̃ computable in time o(ℓ_f(n)/q_R(n) − t_R(n)) fails (A_n, 1/(100m))-OI for infinitely many n. The induction (Claims 6.5 and 6.6) shows that OI against A_1, …, A_i forces the rounded p̃ to agree with f_i on at least 94% of D_i (98% for i = 1).
- *Corollary 6.9 (clique counting).* Assume k-clique counting has no o(ℓ_cc(k, n))-time randomized algorithm. Then there is a Nature computable in time Õ(t_cc(m, n)) and sampleable in Õ(n²), and m distinguishers running in Õ(n³), such that no predictor computable in time ℓ_cc(m, n)·log^{−ω(1)}(n) is (A, 1/(100m))-oracle-access-OI. Under the conjecture that 3k-cliques cannot be counted in n^{ωk−o(1)}, there are 3k distinguishers running in O(n³) such that no (A, 1/300k)-oracle-access-OI predictor runs in time much below n^{ωk}. The introduction states this as Theorem 5: no predictor of time d^{α·k}·log^{−ω(1)}(d) for distinguishers running in Õ(d³) with Õ(d) queries, at ε = 1/100k. The upper and lower bounds use different parameterisations, and the paper reconciles them only informally: it "rules out any predictor p̃ satisfying oracle-access-OI of (uniform) size significantly smaller than" d^{Ω(1/ε)}.
- *Corollary 6.11 (BPP ≠ PSPACE).* Here Nature is computable only in exp(poly(n)) time, the distinguishers are poly(n) in number and time, and ε = 1/m(n) is polynomially small. No poly(n)-time predictor is OI. The proof uses Trevisan–Vadhan's PSPACE-complete problem, which is downward and random self-reducible.
- *What the separation is.* These results hold at the oracle level, and so at the code level by simulation. Against sample-access-OI, Theorem 5.2 always gives O(s/ε²). So, for a fixed budget, adaptive query access lets an auditor run strictly stronger tests. In the paper's words, the separation "provides a rigorous foundation for the argument that auditors should at the very least have query access to the prediction algorithms they are auditing". And: "obtaining oracle-access-OI is as hard, up to sub-polynomial factors, as computing p∗ … even though the running time of the distinguishers can be arbitrarily small compared to the running time of p∗."
- In the proof sketch of Corollary 6.9, the text says "Putting together Theorem 6.4 (which gives scalably hard functions…)". From context this means Theorem 6.7. It reads as a slip in v1.

**Prediction indistinguishability (§3).** PI asks that (i, o*_i, p*_i) be indistinguishable from (i, o*_i, p̃_i).

- *Proposition 3.2:* one simple randomized distinguisher, A_ℓ1, which outputs 0 with probability |o_i − p_i|, forces ‖p* − p̃‖₁ ≤ 4τ + ε whenever p* is within τ in ℓ₁ of a Boolean function. So PI is infeasible wherever ℓ₁ recovery is, for example when p* is pseudorandom.
- *Proposition 3.4:* for distinguishers with the "valid-model property", including forecasting-style tests that rarely reject any natural history, PI and sample-access-OI are equivalent up to a factor of 3 in ε.

**Tests versus distinguishers (§1.4).** "tests have semantics—you want to pass the test, and the higher the probability of passing a test the better. In contrast, distinguishers output 0 or 1 with no semantics". And in forecasting "the Algorithm does not compete with the actual Nature p∗, but only with the hypothetical Nature that passes the test with the lowest probability."

## Bearing on the record

**On [QUESTION-tmpadry4](../questions.d/QUESTION-tmpadry4.md): the paper supplies the formal half the question attributes to it, but says nothing about signal detection, ROC curves or ideal observers.**

- The question's description is accurate. Definition 2.1 says p̃ is adequate relative to A when no A ∈ A can tell its outcomes from Nature's, up to ε. Δ_A is exactly the quantity the question calls distinguishing advantage. For a single Boolean A it is |Pr[accept | Nature] − Pr[accept | model]|, so under the reading of Nature's samples as "signal" it is hit rate minus false-alarm rate. The mapping to SDT is the record's. The paper uses no SDT vocabulary and cites no SDT work.
- The paper confirms the unbounded limit the question needs. With all subset distinguishers, no-access-OI forces ‖p* − p̃‖₁ small, so the ideal-observer end of the scale is statistical distance. With efficient A it is much weaker. The paper's p̃ ≡ 1/2 example is the question's case: the best ROC in the class sits at chance while the ideal one is perfect. There p* is deterministic, and the two halves are computationally indistinguishable.
- On whether efficiency is well defined for a class of observers, the paper has the right object, Δ_A maximised over A ∈ A. It does not define a ratio to the ideal and does not treat human observers. The question's empirical half gets nothing from this paper.
- The paper sides with the question's remark that indistinguishability is criterion-free, and adds something. It contrasts tests, whose acceptance has a valence, with distinguishers, whose outputs come "with no semantics". A distinguisher is a statistic, not a decision with a criterion. Any criterion has to be built into A, for example by thresholding. So whether a criterion shift has a counterpart is a question about the composition of the class A, not about OI.
- A narrowing the question does not anticipate is that access matters as well as budget. Two observers with the same circuit size differ in power depending on whether they can query the model adaptively (§6). Under the hardness assumptions the gap is large. A bounded-observer account built on a single budget parameter leaves this axis out.

**On [CLAIM-152](../claims.d/CLAIM-152.md): the paper is a formal instance of a second relativity, to the observer class, with the target held fixed. It does not touch the claim's point about the target.**

- The target is fixed throughout: one binary outcome o given i. What varies is A. Whether p̃ is good is relative to A. The paper says OI "does not guarantee statistical closeness to Nature (it need not be the case that p∗ ≈ p̃)", and "the feasibility results demonstrate the ability to learn an incorrect model that cannot be detected by efficient inspection." So adequacy depends on the observer class as well as the target. That supports the extension [QUESTION-tmpdzpy2](../questions.d/QUESTION-tmpdzpy2.md) proposes. It is not a new argument for [CLAIM-152](../claims.d/CLAIM-152.md)'s own thesis.
- The multi-calibration equivalence puts this in the language of subpopulations. A predictor passing sample-access-OI against A is one that is calibrated on every set {i : A(i, b, u) = 1}, intersected with its own level sets. The class A fixes which subpopulations the predictor must respect. The paper does not frame this as a partition or as sufficiency. It proves no minimality or uniqueness, and many predictors can satisfy OI for the same A. So calling the OI predictor A's sufficient partition goes beyond the paper.
- The representation is a further parameter, which the paper flags. Enriching the features enlarges the distinguisher class, so p̃ "likely will no longer satisfy OI", and the potential argument bounds how many enrichments can make a significant difference.

**On [QUESTION-tmpdzpy2](../questions.d/QUESTION-tmpdzpy2.md): a partial positive answer at the lower levels and a qualification at the upper ones.**

- *Positive.* The p̃ ≡ 1/2 example is a case where restricting the observers collapses a two-cell partition of X (by p*) into one cell, and the one-cell model passes. It is given informally in the introduction. It assumes the two sets are computationally indistinguishable, and it is not proved as a theorem about partitions. Algorithm 1 builds p̃ only from directions the distinguishers can see. Started from the constant predictor, its level sets are generated by A, and it stops as soon as A is fooled. So with this construction, a weaker class gives a predictor built from fewer, cheaper pieces. The paper bounds that predictor's size as a function of A and ε, independently of Nature: O(s/ε²) at the sample level. That bound is the formal content, for this construction, of a budget changing which units are worth naming. The paper does not show that the coarse predictor is optimal or unique.
- *Qualification.* The question presumes that a bounded observer can always settle for a cheap coarse model. At the oracle and code levels the paper gives evidence against that (Corollaries 6.9 and 6.11). Cheap distinguishers with query access can force any acceptable model to be about as expensive as Nature's own predictor. So whether the budget buys a coarse model depends on the observer's access as well as its budget. An answer to the question has to specify both.
- The question's two cautions stand. The paper describes its models as unfalsifiable by efficient observation, not as true: "attempting to recover the 'true' model of Nature based on real-world observations is futile". That matches A14's "computational convenience does not establish that the resulting unit exists independently of the observer". The paper's cost is circuit size or running time, not a model-evidence term, so it does not bear on [CLAIM-154](../claims.d/CLAIM-154.md)'s Occam penalty.
