---
status: Read
paper: LIT-tmp1vdb9
title: 'Hébert-Johnson, Kim, Reingold & Rothblum — Multicalibration: calibration
  for the computationally-identifiable masses'
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full on 2026-10-15 from the authors' arXiv preprint, the latest version,
    v2 (arxiv.org/pdf/1711.08513, "arXiv:1711.08513v2 [cs.LG] 16 Mar 2018"; the
    abstract page lists v1 of 22 November 2017 and v2 of 16 March 2018). The copy
    is 40 PDF pages: an unnumbered title and abstract page, then printed pages 1–39
    (sections 1–5, acknowledgements, references). Its title is "Calibration for
    the (Computationally-Identifiable) Masses", without the "Multicalibration:"
    prefix. Text extracted with pdftotext. The extraction drops absolute-value bars
    and scatters displayed formulas, so Definitions 2.1, 2.2 and 2.6 were checked
    against page images (printed pp. 14 and 16), and every other formula quoted
    below was reconstructed from the extraction and its context. Read: every section,
    definition, algorithm, lemma, theorem and the proofs that are given. Several
    proofs are not given in the paper and so were not read: Theorem 3.8 is cited
    from Hardt and Rothblum (2010); Theorem 3.9 is said to follow "from tailoring
    the proof" of Bassily et al. (2016), with no proof written out; Claim 3.11 (running
    time) and the cryptographic lower bound after Theorem 4 are argued at a high
    level only. The proofs that are written (Claims 2.10 and 3.1, Lemmas 3.2, 3.6
    and 5.2, Theorems 3.12, 4.2, 4.4 and 5.1) were followed step by step but not
    re-derived independently; the inconsistencies found are listed under Key results.
    The ICML version (PMLR 80:1939–1948, proceedings.mlr.press/v80/hebert-johnson18a/hebert-johnson18a.pdf,
    10 pp., and its 7-page supplement) was fetched and skimmed, not read: its definitions
    and Theorems 1–5 were compared with the arXiv statements. It uses a general
    distribution D over individuals, writes predictors as f and the property as
    "(C, α)-multicalibrated", and states the same bounds. Every verbatim quotation
    below was checked against the extracted text by script, with whitespace normalised.
    Places looked, 2026-10-15: arxiv.org/abs/1711.08513 (abstract page and version
    history, fetched); arxiv.org/pdf/1711.08513 (v2 PDF, fetched, sha256 4291c498…);
    proceedings.mlr.press/v80/hebert-johnson18a.html (fetched; gives PMLR 80:1939–1948);
    the PMLR PDF and supplementary PDF (both fetched).
date: '2026-10-15'
summary: >-
  A predictor is α-multicalibrated on a collection C of subpopulations if, within
  every set S in C, the individuals given (roughly) the same prediction v have true
  probabilities averaging within α of v, except on an α-fraction of S. For any C
  whose sets have size at least γN, a simple iterative patching algorithm reaches
  multicalibration from O(log|C|/α^{11/2}γ^{3/2}) samples in time linear in |C|,
  and the result is a circuit only O(s/α⁴γ) in size when the sets of C are computed
  by size-s circuits. Learning it is equivalent, up to polynomial factors, to weak
  agnostic learning of C, so it is hard for rich C under cryptographic assumptions.
  Calibrating any predictor h on its own level sets as well as on C costs at most
  6α in squared error. All guarantees are relative to the benchmark p*, which is
  itself defined relative to the features available, and they hold only for large
  sets; the paper offers no uniqueness for the predictor and does not state a theorem
  in indistinguishability form.
---

# NOTE-tmprrwdk: Hébert-Johnson, Kim, Reingold & Rothblum — Multicalibration: calibration for the computationally-identifiable masses

## Contribution

The paper defines multicalibration: calibration required on every set in a given collection C at once, not on a few protected groups. C is meant to be the sets a bounded class of computations can pick out ("conjunctions of four attributes, bounded-depth decision trees, or any other bounded complexity class"). It gives an algorithm that reaches it for any C and any truth p*, bounds its sample complexity using differential privacy as a tool for adaptive data analysis, and shows the result has a small circuit. It shows learning a multicalibrated predictor is as easy, and as hard, as weak agnostic learning of C. It shows calibration costs almost nothing in accuracy against any reference class of predictors. The stated motivation is fairness: preventing discrimination that a learning procedure introduces, not discrimination already in the data.

## Key insight

Calibration on a large group is easy to satisfy while ignoring structure inside it: predicting the group mean for everyone is calibrated. Requiring calibration on every subpopulation is impossible from a sample, because it would need p* exactly. The compromise is to require it on the subpopulations a fixed class of computations can identify in advance. The paper's justification is epistemic: "we can only expect a learner to produce a predictor that is calibrated on sets that could have been identified efficiently" and "it is unreasonable to expect accuracy on a subgroup that is only identifiable a posteriori". Whenever calibration fails on some category, an additive correction on that category moves the predictor closer to p* in squared distance by a fixed amount, so the patching must stop after a bounded number of steps. That bound, not |C|, sets the size of the final predictor.

## Assumptions

- **A finite universe X of N individuals, each with a binary outcome o_i drawn independently as Bernoulli(p*_i).** p*_i is "the probability of outcome oi = 1, conditioned on all the information which is available to the algorithm". Features enter through a fixed map φ from individuals to features, which the paper then drops from the notation. Independence is used only for concentration; the authors say any model with suitable tail bounds would do.
- **The uniform distribution over X** in the arXiv version ("mostly syntactic"); a general distribution D in the ICML version.
- **Every set in C is large: |S| ≥ γN.** All sample, time and circuit bounds scale with 1/γ. Theorems 3 and 4 apply to C′ = {S ∈ C : |S| ≥ γN}.
- **Sets are given implicitly, as circuits c_S with S = c_S⁻¹(1).** This is how computational identifiability is made precise: the complexity of C is the size or running time of these circuits.
- **Unlabelled individuals are cheap; only labelled samples (i, o_i) are counted.**
- **Calibration is against p*, not against realised outcomes.** Observable calibration against o is a separate notion, linked by Claim 2.3 (Hoeffding).
- **No structure on p*.** p* may be adversarial; the positive results do not need it to be learnable.

## Key results

Definitions, in the paper's notation (x a predictor, S_v = {i ∈ S : x_i = v}):

- **α-accurate in expectation (α-AE), Definition 2.1.** |E_{i∼S}[x_i − p*_i]| ≤ α. **α-multi-AE, Definition 2.7:** α-AE for every S ∈ C. This is the notion later called multiaccuracy. The arXiv paper never uses that word; the ICML version cites Kim, Ghorbani and Zou (2018, arXiv 1805.12317, "Multiaccuracy: Blackbox post-processing for fairness in classification") as further work on multi-accuracy in expectation. The paper's own example of why AE is too weak: if p*_i = 1/2 throughout S, predicting 1 on half of S and 0 on the other half is accurate in expectation, yet "the predictor has artificially created two categories within this population".
- **α-calibration with respect to S, Definition 2.2.** There is S′ ⊆ S with |S′| ≥ (1 − α)|S| such that for all v ∈ [0, 1], |E_{i∼S_v∩S′}[x_i − p*_i]| ≤ α. The error is relative to |S_v|, not N, to block a predictor from evading the condition by spreading individuals over many tiny prediction values. α-calibration on S implies 2α-AE on S.
- **α-multicalibration, Definition 2.6.** "A predictor x is α-multicalibrated on C if for all S ∈ C, x is α-calibrated with respect to S."
- **(α, λ)-multicalibration, Definition 2.9,** the working form: predictions are bucketed into 1/λ intervals λ(v); for every S ∈ C and every bucket category S_v(x) with |S_v(x)| ≥ αλ|S|, |Σ_{i∈S_v(x)} (x_i − p*_i)| ≤ α|S_v(x)|. Claim 2.10: rounding each bucket to its mean turns this into (α + λ)-multicalibration.

Algorithms and bounds:

- **Algorithm 3.1 (multi-AE).** Start at x ≡ 1/2. For each S ∈ C, query an estimate of Σ_{i∈S} p*_i with tolerance τ < αγ/4; if it differs from Σ_{i∈S} x_i by more than α|S| − τN, shift x on S by the difference divided by |S| and project to [0, 1]. Stop when no set updates. Lemma 3.2: each update reduces ‖p* − x‖² by at least 3α²|S|/16, and ‖p* − x‖² ≤ N, so there are O(1/α²γ) updates. Theorem 3.3: O(|C|/α²γ) statistical queries. Corollary 3.4: Õ(log(|C|/ξ)/α²γ) samples, because the queries are fixed in advance. The paper says this part "was originally discovered by [TTV09]" and that it "can be viewed as a restatement of the boosting-based proof due to [TTV09] that every high-entropy distribution is indistinguishable by small circuits from an efficiently-samplable distribution of the same entropy".
- **Algorithm 3.2 (multicalibration).** The same patching, applied to bucket categories S_v = S ∩ {i : x_i ∈ λ(v)} with |S_v| = βN ≥ αλ|S|, through a "guess-and-check" oracle with window αβ/4 that answers only when the current guess is far off; a final step rounds each bucket to its mean. Lemma 3.6: at most O(1/α³λγ) answered queries (updates); each update gains at least α³λγN/16 in squared distance. Theorem 3.7: O(|C|/α³λ²γ) statistical queries; with λ = α the output is 2α-multicalibrated after O(|C|/α⁵γ) queries.
- **Sample complexity.** The categories depend on the current predictor, so queries are adaptive and a union bound over C does not suffice. The paper answers the guess-and-check queries with a differentially private mechanism (private multiplicative weights, Hardt and Rothblum 2010) and transfers privacy to generalization (Bassily et al. 2016). Theorem 3.10: (α, λ)-multicalibration on C with probability 1 − ξ from n = O(log(|C|/αλγξ)/(α⁴λ^{3/2}γ^{3/2})) samples. With λ = α this is Theorem 2's O(log(|C|)/α^{11/2}γ^{3/2}). The naive resampling approach would need 1/α⁶γ⁶.
- **Running time.** Claim 3.11 and Theorem 2: O(|C| · t · poly(1/α, 1/λ, 1/γ)), t the time to test membership in a set of C. Linear in |C|, because the algorithm loops over C looking for a violated set.
- **Circuit size.** Theorem 3.12 (Theorem 1): if each S ∈ C has a circuit of size O(s), some α-multicalibrated predictor has a circuit of size O((s + b)/α⁴γ), b the bits of precision, and Algorithm 3.2 learns it. Each update adds one copy of a c_S plus a comparison and an addition. In the paper's words, "the cardinality of C is not the operative parameter in determining the circuit complexity of a predictor x that is multicalibrated on C".
- **The truth is always multicalibrated.** "The benchmark predictor is, itself, multicalibrated with respect to every collection of subsets C." So multicalibration is a necessary condition for being p*, weakened to what C can check.

The class C and weak agnostic learning (Section 4):

- **Definition 4.1 (Feldman 2010).** A (ρ, τ)-weak agnostic learner for C under D: given samples (i, y_i) with y_i ∈ [−1, 1], if some c ∈ C has ⟨c, y⟩_D > ρ, it returns some h : X → [−1, 1], not necessarily in C, with ⟨h, y⟩_D > τ.
- **The reduction.** For each bucket X_v, label individuals by Δ_i = (x_i − o_i)/2 on X_v and 0 elsewhere. Claim 4.3: if a category S_v of size at least βN has Σ_{i∈S_v}(x_i − p*_i) ≥ α|S_v|, then ⟨c_S, Δ⟩ ≥ ρ (ρ = αβ/2), or the same holds for −Δ. So a calibration violation is exactly a member of C correlating with the predictor's residual on a level set. The learner's h is then used as a gradient step, x_i → v − ηh_i, which gains τ²N in squared distance.
- **Theorem 4.2 (Theorem 3).** A (ρ, τ)-weak agnostic learner for C running in time T yields (α, λ)-multicalibration on C′ in time O(T · poly(1/α, 1/λ, 1/γ)), provided ρ ≤ α²λγ/2 and τ = poly(α, λ, γ).
- **Theorem 4.4 (Theorem 4), the converse.** An algorithm learning an α-multicalibrated predictor on C′ in time T gives a (ρ, τ)-weak agnostic learner for C in time O(T · poly(1/τ)) for any ρ, τ with τ ≤ min{ρ − 2γ, ρ/4 − 4α}. The learner's output is h_i = sgn(x_i), where x is multicalibrated on C′ ∪ {X} with respect to the labels y in place of p*. Small sets are handled by a constant hypothesis.
- **Consequence, asserted not proved here.** Under cryptographic assumptions (pseudorandom functions), "there is some constant t > 0, such that any algorithm that learns an α-multicalibrated predictor requires" Ω(|C|^t) time. The paper sums up: "the complexity of learning a multicalibrated predictor with respect to a class C is equivalent to the complexity of weak agnostic learning on C."

Accuracy (Section 5):

- **Lemma 5.2.** If x is α-multicalibrated on the level sets S_v(y) of any predictor y, then ‖y − p*‖² − ‖x − p*‖² ≥ ‖x − y‖² − (4α + λ)N. So where calibration moves y a lot, the move is an improvement.
- **Theorem 5.1 (Theorem 5).** For any C and any class H of predictors there is an x, α-multicalibrated on C, with ‖x − p*‖² − ‖h* − p*‖² < 6αN, where h* is the best in H; with set sizes at least γN and circuits of size at most s for C and H, x has a circuit of size O(s/α⁴γ). The proof calibrates on C together with every λ-level set of every h ∈ H, ignoring level sets smaller than αλN. The paper reads this as fairness without an accuracy cost.

Inconsistencies in the arXiv v2 text, noted while reading: Lemma 3.6 states O(|C|/α⁴λγ) X-responses, its proof gives O(|C|/α³λ²γ), and Theorem 3.7 uses the latter. Section 3.2's overview gives O(1/α^{5/2}γ^{3/2}) samples, which matches neither Theorem 3.9's per-β form nor Theorem 3.10. The proof of Theorem 3.12 says O(α⁴γ) updates where 1/α⁴γ is meant. Lemma 5.2's proof ends with (4α − λ), its statement has (4α + λ). The proof of Theorem 4.4 writes |S| < γ for |S| < γN. Footnote 2 refers to "Supplementary Materials A", a leftover from the ICML version. None changes a headline result.

## Bearing on the record

**On [QUESTION-tmpadry4](../questions.d/QUESTION-tmpadry4.md): the paper supplies the relative-to-a-class-of-observers structure, but not in the form the question attributes to it.**

- The question groups this paper with outcome indistinguishability and says "a predictor is adequate relative to a class of distinguishers if none of them can tell its outcomes from nature's". This paper does not say that. It never defines a distinguisher, a distinguishing advantage, or indistinguishability of a predictor from nature; "indistinguishable" appears only in its description of Trevisan, Tulsiani and Vadhan (2009) and in an informal example. That framing belongs to Dwork et al. (2021, [LIT-tmpoyjmt](../literature.d/LIT-tmpoyjmt.md)), which should be cited for it.
- What the paper does supply is close to it in correlation form. Claim 4.3 shows that a multicalibration failure on a large set is a set in C whose indicator, restricted to a level set of x, correlates with the residual (x − o)/2, and Theorem 4.2 searches for exactly such correlations. In my own reading, not the paper's: α-multi-AE on C says that every test of the form average-over-S, S ∈ C, gives nearly the same value on x as on p*, and multicalibration says the same for tests averaging over S ∩ {x ≈ v}. These are first-moment tests that see the individual and the prediction, not the outcome. Their advantage is a difference of means on a subset, not a hit rate minus a false-alarm rate, and there is no ROC, likelihood ratio or criterion anywhere in the paper.
- So for the question's first part (which SDT quantity corresponds to advantage), this paper gives a quantity, the calibration error on a C-identifiable category, without connecting it to SDT. The correspondence would have to be built. The link the paper does draw is to learning theory: a bounded observer's failure to find a violation is the failure of weak agnostic learning on C. That is relevant to [CLAIM-tmpvdl53](../claims.d/CLAIM-tmpvdl53.md), since it ties what a class of observers cannot detect to a learning problem known to be hard for rich classes.

**On [CLAIM-152](../claims.d/CLAIM-152.md): consistent with it, and it adds a second relativity without removing the first.**

- The target is explicit and fixed. Everything is calibration against p*, the probability of one binary outcome. Change the outcome and p*, the violated sets and the learned predictor all change. And p* is itself defined "conditioned on all the information which is available to the algorithm", so the benchmark is relative to the feature map as well as to the outcome.
- The paper adds relativity to the observer class. Its toy example (Section 2.3): x = 1/2 on S is calibrated on S, but if a subset S′ with p* = 1 is in C, calibration forces the split. Which cells a predictor must separate is set by C. In the paper's words, "The more powerful the family, the stronger the guarantee becomes; no subpopulation that can be identified by the family will be overlooked."
- It does not supply a unique partition even with target and class fixed. p* is multicalibrated for every C, and the algorithm's output depends on its starting point and the order of updates; the paper claims existence and learnability, not uniqueness. This sides with [CLAIM-152](../claims.d/CLAIM-152.md)'s "no boundary drawn this way is universal" and strengthens it: within a stated target and a stated class there is a set of adequate predictors, not one.
- The defeat condition of [CLAIM-152](../claims.d/CLAIM-152.md) (a privileged target) is not touched: the paper chooses the outcome by application (loan repayment, disease) and makes no claim that any target is privileged.

**On [QUESTION-tmpdzpy2](../questions.d/QUESTION-tmpdzpy2.md): a formal instance of a budget-relative sufficiency, with two budgets that come apart.**

- Read as the question asks, the level sets of a multicalibrated x form a partition into at most about 1/λ cells that is approximately sufficient for the outcome relative to C: within any S ∈ C, knowing which cell an individual is in leaves the average of p* within α of the cell's value. That is sufficiency relative to a class of tests, not sufficiency in the statistical sense. The paper does not use the word.
- The representation budget is mild. Theorem 3.12: if the observer class is circuits of size s, an adequate predictor exists at size O(s/α⁴γ), independent of |C|. A bounded observer can always be matched by a predictor only modestly larger than the observer.
- The finding budget is not mild. Theorems 4.2 and 4.4: learning such a predictor is equivalent to weak agnostic learning of C, and for rich C takes time polynomial in |C| under cryptographic assumptions. So that an adequate partition exists within the budget and that a bounded agent can find it come apart. The question should say which budget it means.
- The paper does not answer the question's main demand, "a system and a family of budgets for which the optimal sufficient partition provably changes with the budget". It has no notion of an optimal partition. The toy example shows that adding a set to C can force a finer partition, which is the direction the question expects, but it is an example, not a theorem about optima.
- A14's caution, that computational convenience does not show a unit exists independently of the observer, is untouched. The paper's sets are whatever C contains, and it claims nothing about them beyond identifiability.

**Limits that bear on all three.** Sets smaller than γN are not protected, and all bounds grow with 1/γ. Calibration holds on all but an α-fraction of each set. The outcome is binary and the individuals independent. The paper says that if the features cannot identify a group, "the data may be insufficient for multicalibration to provide meaningful guarantees". There are no experiments.
