---
number: 308
status: Read
formerly:
- NOTE-tmpaxdi8
paper: LIT-356
title: 'How much does your data exploration overfit? Controlling bias via information usage'
version: 1
history:
- version: 1
  date: '2026-09-29'
  note: >-
    Read in full (I read the full text of arXiv 1511.05219 v3 (8 Oct 2019),
    the accepted IEEE Transactions on Information Theory version
    ("Manuscript received January 30, 2017; revised May 30, 2018; accepted
    September 12, 2019"; "Part of this work was presented at AISTATS 2016"),
    23 pp., from the arXiv PDF. The text was extracted with PyMuPDF, and p.
    4 was rendered to check Corollary 1. I read all of it: the abstract,
    §§I–VII, Appendices A–I with every proof, the acknowledgement, all 37
    references and the author biographies. I checked the proofs of
    Propositions 1, 2, 5, 8, 9 and 10, Lemmas 1–3 and Proposition 13 line by
    line. For the Proposition 3 lower bound and the threshold Theorems 1–2
    (App. C), I followed the steps but did not re-derive the constants. I
    also compared v3 structurally against v1 (16 Nov 2015, titled
    "Controlling Bias in Adaptive Data Analysis Using Information Theory",
    23 pp.), reading its §§1–2 and the section list; I did not read v1 line
    by line, and I did not read v2 (6 Oct 2016) or the AISTATS 2016
    proceedings version. Page and section numbers are v3's. `published:` is
    the arXiv v1 date. No anthology entry exists for this paper (I grepped
    the arXiv id and both titles in record/literature.d).). The first NOTE
    on this paper, which was seeded from its abstract alone.
date: '2026-09-29'
summary: >-
  Suppose an analyst reports statistic φ_T, chosen by any data-dependent
  rule T from m candidates each σ-sub-Gaussian. Then the selection bias
  obeys |E[φ_T − µ_T]| ≤ σ√(2·I(T;φ)) (Prop. 1), where "information usage"
  I(T;φ) ≤ H(T) ≤ log m. For argmax selection over φ ~ N(µ,I) the squared
  error is Θ(1 + H(T)) (Prop. 3). Adaptive analyses compose additively,
  with I(T_{k+1};φ) ≤ Σ_i I(Y_{T_i};φ_{T_i} | H_{i−1},T_i) (Lemma 1).
  Answering each query with Gaussian noise of variance σ²√j/n therefore
  keeps the k-th answer's error at O(σk^{1/4}/√n) (Prop. 7).
---

# NOTE-308: How much does your data exploration overfit? Controlling bias via information usage

## Contribution

The paper gives a single, distribution-dependent quantity that bounds the bias of *any* data-dependent choice of which statistic to report: the mutual information I(T;φ) between the choice and the realised statistics. Before it, adaptive data analysis had two kinds of tool. Selective inference is exact but needs a tractable, pre-specified selection rule. Differential privacy and max-information are worst-case over adversarial analysts. Information usage sits between them. It applies to arbitrary analysts, is small for benign ones, and shrinks when the data have signal.

The paper shows the bound matches the truth for Gaussian maximum selection and applies it to variance filtering, clustering, rank selection with signal, LARS, FDR-controlled selection, classification, and dependent (Markov) data. It then uses the chain rule to show that randomised answers, whether Gibbs selection or Gaussian noise per query, provably limit the bias of a multi-step analyst.

## Key insight

Selection bias is what the choice has learnt about the *noise*. Only the dependence of T on the part of the data that would change in a replication can bias the reported value.

Mechanically, the proof is one variational step. Donsker–Varadhan applied to P(φ_i | T=i) against P(φ_i), with the test function λ(φ_i − µ_i), gives E[φ_i − µ_i | T=i]² ≤ 2σ²·D(P(φ_i|T=i) ‖ P(φ_i)). Averaging over T gives the bound. Since I(T;φ) = H(T) − H(T|φ), bias can be reduced in two ways: by signal, which lowers H(T), or by randomisation, which raises H(T|φ).

## Assumptions

- **Setting (§§II, IV).** φ = (φ_1,…,φ_m): Ω → ℝ^m and T: Ω → {1,…,m} are any random variables on a common space, with µ = E[φ]. T may use data beyond φ and internal randomness. m is finite but arbitrary.
- **Tails.** Each φ_i − µ_i is σ-sub-Gaussian (Props. 1–2). Extensions cover unequal σ_i (Prop. 8, with √(E[σ_T²])) and sub-exponential (σ,b) statistics (Prop. 9: E[φ_T − µ_T] ≤ b·I + σ²/(2b)).
- **No independence of data points is needed** for Prop. 1 (§III). It is claimed to apply to time-series and network data. i.i.d. structure enters only through σ, for example σ/√n for sample means.
- **Lower bounds (Prop. 3; App. C).** T = argmax_i φ_i with φ ~ N(µ,I), or threshold selection on unit-variance Gaussians or shifted exponentials with a threshold large enough (Theorems 1–2).
- **Multi-step analyst (§VI-B).** Each query T_k depends on φ only through the history H_{k−1}. For Prop. 7: φ is jointly Gaussian with φ_i ~ N(µ_i, σ²/n), and the answer noise W_j ~ N(0, ω_j²/n) is independent.
- **Classification (Prop. 5).** The training inputs x are fixed and the labels Y_i are drawn independently. So this bounds *label-noise* overfitting, not generalisation over random inputs.

## Key results

- **Prop. 1 (p. 3).** |E[φ_T − µ_T]| ≤ σ√(2·I(T;φ)). For sample means of n i.i.d. σ-sub-Gaussian terms this becomes σ√(2I/n).
  - Examples (p. 4): data-agnostic T gives I = 0 and no bias. For argmax of m i.i.d. N(0,σ²), I = H(T) = log m, and the bound σ√(2 log m) is asymptotically tight.
- **Corollary 1 (p. 4).** The mean of the top m_0 of m zero-mean σ-sub-Gaussians is ≤ σ√(2·log(m/m_0)). The claim that it is tight as m/m_0 → ∞ is argued by a grouping construction in App. C.A.
- **Prop. 2 (p. 4).** E|φ_T − µ_T| ≤ σ + c_1σ√(2I), with c_1 < 36. E(φ_T − µ_T)² ≤ 1.25σ² + c_2σ²I, with c_2 ≤ 10.
- **Prop. 3 (p. 4).** For T = argmax, φ ~ N(µ,I), and any m and µ: (1/8)·H(T) − 2.5 ≤ E(φ_T − µ_T)² ≤ 10·H(T) + 1.5. So squared error is Θ(1 + H(T)).
- **Filtering (§V-A).** I(T;φ) ≤ (1 − α)·H(T), with α = I(T;D|φ)/H(T). Variance filtering of i.i.d. Gaussian markers has I(T;φ) = 0 because sample means and variances are independent, so it introduces no bias. Selection on ψ with T–ψ–φ gives I(T;φ) ≤ I(φ;ψ).
- **Prop. 4 (p. 6).** E[φ_T − µ_T] ≤ σ√(2·η_ψφ·I(T;ψ)), with η the strong-data-processing contraction coefficient. Examples: η ≤ k/n for a size-k subsample, and η = (1−2δ)² for a binary symmetric channel.
- **Clustering (§V-B).** If T depends on the data only through the number of clusters K, then I(T;φ) ≤ H(K), which is about 0 when K is stable.
- **Rank selection with signal (§V-C, Fig. 1).** With m = 1000, one mean µ ∈ [1,4] and the rest 0, H(T), the bound √(2I) and the observed bias all fall as µ rises (1000 runs).
- **LARS (§V-D, Fig. 2; App. G).** A 100 × 1000 Gaussian design has 20 signals of size s ∈ {0.04, 0.06, 0.08}, with information estimated by bootstrap. The information bound and the bias track each other and both fall with signal and with path length. This is simulation only.
- **Prop. 5 (p. 8).** E[L(f̂) − L̂(f̂)] ≤ √(I(f̂(x);Y)/(2n)), and I(f̂(x);Y) ≤ d·log₊(ne/d) for VC dimension d, via Sauer's lemma.
- **Markov data splitting (§V-G).** Under a uniform mixing condition max_s D(P(s_τ|s_1=s) ‖ π) ≤ c_0e^{−c_1τ}, selection on the first block and estimation on the last give I(T;φ) ≤ c_0e^{−c_1(n_2−n_1)}.
- **Prop. 6 (p. 9).** For estimation after FDR-controlled selection: I(T;φ) ≤ h(FDR) + (1−FDR)·log(1/(1−β)) + FDR·log(1/α) + ξ, where α and β are the expected type I and type II proportions and ξ is a concentration error term.
- **Gibbs selection (§VI-A, Fig. 3).** The maximum-entropy rule π*_i ∝ e^{βφ_i}, known as exponential weights or the exponential mechanism, gives I < log m unless it is degenerate. In simulation (N_1 = 1000 signals among 10⁵ nulls, β = 2, K = 100) it cuts bias against argmax at some cost in accuracy when 1 < µ < 4. The paper notes that it "does not reduce bias … for all … distributions".
- **Lemma 1, adaptive composition (p. 11).** I(T_{k+1};φ) ≤ I(H_k;φ) = Σ_{i=1}^{k} I(Y_{T_i}; φ_{T_i} | H_{i−1}, T_i). The proof (App. H) is the chain rule plus conditional independence of Y_{T_i} from the other statistics given φ_{T_i}. The paper reads this as an "information budget" that accumulates additively over steps.
- **Lemma 2 (p. 11).** For X ~ N(0,σ_1²) and Y = X + W with W ~ N(0,σ_2²): I(X;Y) = ½·log(1 + β) ≤ β/2, with β = σ_1²/σ_2² "the signal to noise ratio". Lemma 3 (App. H) gives I(X; X+W) ≤ σ_X²/σ_W² for non-Gaussian X.
- **Prop. 7 / Prop. 13 (p. 11; App. H).**
  - General statement (Prop. 13): E|Y_{T_{k+1}} − µ_{T_{k+1}}| ≤ σ/√n + c_1(ω_{k+1}/√n + σ²√(Σ_{j≤k} ω_j^{−2}/n)).
  - Choosing ω_j = σ·j^{1/4} gives c·σk^{1/4}/√n.
  - Without noise the error can be Ω(σ√(k/n)) (App. H, Example 1). So k = o(n²) adaptive queries can be answered accurately, matching the Laplace-noise result of Dwork et al. [28].
- **App. F.** Prop. 11: for uniform p-values, P(p_T < ε) ≤ ε + √(I(T;Z_ε)/log(1/2ε)), with Z_ε,i = 1(φ_i < ε). Prop. 12: Bayesian regret is ≤ σ√(2H(X*)).
- **App. I.** Max-information *increases* as signal makes argmax selection *less* biased. Lemma 4 shows the same for approximate max-information when T is a deterministic function of φ. This is the paper's case that mutual information, not max-information, is the right measure for non-adversarial analysts.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Bias of any data-dependent selection among σ-sub-Gaussian statistics is ≤ σ√(2I(T;φ)) | strong (proof) | Prop. 1, App. B.A (Donsker–Varadhan) |
| C2 | Information usage also bounds absolute and squared error | strong (proof) | Prop. 2, App. B.D; loose constants (36, 10) |
| C3 | "Our mutual information based bound is tight in natural settings" | moderate | Tight for Gaussian argmax (Prop. 3), but as a *squared-error* two-sided bound. Threshold Theorems 1–2 (App. C) give E(φ_T−µ_T)² ≥ H(T) (Gaussian) and bias ≥ H(T)/2 (exponential) under large thresholds. No tightness result for general selection; the Discussion leaves it open |
| C4 | Unlike stability or VC bounds, the bound is data-distribution dependent and falls with signal | strong (proof) plus simulation | I = H(T) − H(T\|φ); §V-C and Fig. 1; App. I contrast with max-information |
| C5 | Classification overfitting (label noise, fixed inputs) ≤ √(I(f̂(x);Y)/(2n)) ≤ √(d·log₊(ne/d)/(2n)) | strong (proof) | Prop. 5, App. D (with the constant slips noted in corrections) |
| C6 | Multi-step adaptive analysis composes additively in conditional per-query information | strong (proof) | Lemma 1, App. H |
| C7 | Gaussian answer noise of variance σ²√j/n bounds the k-th adaptive answer's error by O(σk^{1/4}/√n), versus Ω(σ√(k/n)) without noise | strong (proof) for the upper bound; the Ω comparison is a single example | Prop. 7/13; App. H Example 1 |
| C8 | Max-entropy (Gibbs) randomised selection reduces bias while largely preserving accuracy | moderate (simulation in one setting); the paper itself notes that it can increase I | §VI-A, Fig. 3 |
| C9 | Variance filtering of i.i.d. Gaussian data introduces no selection bias for mean estimates | strong (proof, given Gaussianity) | §V-A |
| C10 | Bounds apply to non-i.i.d. structured data | strong for Prop. 1 as stated; illustrated only for Markov splitting | §§III, V-G |

## Concepts

- **Information usage** ("bad information usage"). I(T;φ): how much the choice of what to report depends on the noise in the candidate statistics (pp. 3–4).
- **Selection rule T.** Any data-dependent choice of which of m statistics to report, possibly a human analyst's (§II).
- **Information budget I_b.** The total mutual information an analyst may spend over adaptive steps, fixed a priori from sample size and bias tolerance (p. 11).
- **Distortion vs selection bias.** The split of the excess answer error into E|Y − φ| and cσ√(2I) (p. 11).
- **Contraction coefficient η_XY.** The strong-data-processing constant (Def. 1).
- **Max-information I_∞** and its approximate version. Worst-case analogues of mutual information (App. I).

## Connections

- **[LIT-347](../literature.d/LIT-347.md) (Xu & Raginsky 2017; [NOTE-306](NOTE-306.md)).** It extends Prop. 1 from a finite candidate set to arbitrary hypothesis spaces by setting φ = the empirical risks and T = W, and it weakens the quantity to I(S;W) by data processing. Its adaptive-composition inequality (eq. 36) is this paper's Lemma 1 transposed from queries to training stages. Its Gibbs algorithm is this paper's Gibbs selection (eq. 2), recast as a learning algorithm. What Xu & Raginsky add is the *channel* vocabulary. This paper speaks of an analyst and a selection rule, and uses "channel" only for the binary symmetric channel example of Def. 1. Xu & Raginsky's P_{W|S} and capacity sup_µ I(S;W) are theirs.
- **[LIT-236](../literature.d/LIT-236.md) and [LIT-233](../literature.d/LIT-233.md) (Sefidgaran et al.).** [NOTE-216](NOTE-216.md) (on [LIT-233](../literature.d/LIT-233.md)) lists Russo–Zou among the mutual-information family those papers position against. This paper's §V-A remark that the bound depends on I(T;φ), not I(T;D), is the first move toward compressing what the selection depends on.
- **[LIT-348](../literature.d/LIT-348.md) (McCandlish et al., critical batch).** No content in common. This paper has no gradients, batches or optimisation dynamics. The only point of contact with the owner's §5 is Lemma 2's ½·log(1+SNR) per noisy query (see Bearing).
- **Differential privacy / reusable holdout (Dwork et al. [18, 19, 28]).** Cited as the worst-case counterpart. This paper's Gaussian noise protocol reproduces their k = o(n²) query count. Not in either record.

## Bearing on the record

**Map row 12 (gradient-as-channel; must-cite "info-theoretic generalization (Xu–Raginsky 2017)").** The brief asked whether this paper is the precursor of the learner-as-channel bound. It is, and it supplies more of §5's per-step accounting than [LIT-347](../literature.d/LIT-347.md) does:

1. **Priority for the bound.** The mutual-information generalisation and bias bound (C1), its Donsker–Varadhan proof, and its reading as "information the output carries about the noise" are here first, in Nov 2015. [LIT-347](../literature.d/LIT-347.md) is an extension. The map's row 12 should cite Russo & Zou (AISTATS 2016, or the 2020 journal version) alongside Xu & Raginsky, not Xu & Raginsky alone. This repairs an omission, not a misattribution: the map does not credit Xu & Raginsky with anything they did not do.
2. **Per-step additive accounting.** The owner's I(θ_T;D) ≤ Σ_t S_grad,t has the shape of Lemma 1: total information is the sum over adaptive steps of the conditional information each step's *answer* carries about the queried statistic, spent against an a priori budget (p. 11). [NOTE-306](NOTE-306.md) found this in [LIT-347](../literature.d/LIT-347.md)'s eq. (36). It originates here.
3. **A Shannon–Hartley-type per-step term already exists, for noisy queries.** Lemma 2 prices one Gaussian-noised answer at ½·log(1 + SNR), with SNR = σ_φ²/σ_W². Prop. 7 then turns the accumulated sum into an explicit error bound. [NOTE-306](NOTE-306.md)'s open question asked whether the capacity reading could ground the owner's C_step = d·log₂(1 + SNR) in a generalisation theorem. This is the nearest existing result. But it is for *scalar statistics answered with added independent noise*, not for minibatch gradients, whose "noise" is the sampling of the data itself. The owner cannot cite it for SGD without an argument that a minibatch gradient is a noisy answer to a query about a population gradient with independent noise. That is exactly the step not made anywhere in the record.
4. **What it does not supply.** It has no channel or capacity framing of the learner (that is [LIT-347](../literature.d/LIT-347.md)'s), no uncountable hypothesis spaces, and nothing on batch size, critical batch or SNR in McCandlish's sense ([LIT-348](../literature.d/LIT-348.md)). The map's `KNOWN` verdict for row 12 is strengthened: the information-theoretic half is owned by this paper plus [LIT-347](../literature.d/LIT-347.md).

**ML practice (`anthology-candidate`).** The practice-shaped content concerns reuse of evaluation data, not training: bias from repeated adaptive queries to a holdout or benchmark is controlled by answering them with calibrated noise (Prop. 7), and randomised (Gibbs) selection among candidates cuts winner's-curse bias (§VI-A). These are tested only in stylised Gaussian settings and one simulation, and adoption belongs to the differential-privacy "reusable holdout" line rather than to this paper. If the anthology holds a practice on benchmark or leaderboard reuse, this paper is its information-theoretic, non-adversarial source. Otherwise it is theory.

## Limitations

- **Finite candidate set and expected bias only.** The main bounds are on expectations. Tail bounds are left to the DP literature and to [LIT-347](../literature.d/LIT-347.md)'s Theorem 3.
- **The headline "tight" is narrow** (C3). Two-sided matching holds for squared error under Gaussian argmax; bias lower bounds hold only for large-threshold rules. The Discussion lists tightness for general exploration as open.
- **The data-processing step in Prop. 1 can be loose.** The Remark in App. B.A gives a deterministic example with I(T;φ) = log m and zero bias. The authors suggest bounding Σ P(T=i)·D(P(φ_i|T=i) ‖ P(φ_i)) directly in such cases.
- **Computing I(T;φ) for a real analyst is not addressed**, beyond bootstrap estimates for LARS. For a human analyst like "Bob", the bound is conceptual unless randomisation is imposed.
- **Prop. 5 bounds label-noise overfitting with fixed inputs**, not generalisation over random inputs.
- **Constants are loose** (36, 10, 2.5), and several proofs carry the typographical slips listed under corrections.

## Open questions

- For which exploration procedures beyond argmax and threshold rules is information usage a tight measure of bias? The authors raise this (§VII).
- Can the Gaussian-noise protocol's accounting (Lemmas 1–2, Prop. 7) be transferred to SGD, treating each minibatch gradient as a noisy answer to a population-gradient query? That would bound I(S;W_T) by Σ_t ½·log(1 + SNR_t) and link row 12's batch-SNR story to a generalisation theorem. The obstacle is that minibatch noise is not independent of the data.
- Can practical analytic workflows be randomised in the way Prop. 7 requires without destroying utility? The authors name this as "another important project" (§VII).

## Corrections to the seeded skim

- none (there was no seed or dossier)
- The title needed verifying, and both titles in the brief are correct for different versions. arXiv v1 (16 Nov 2015) is "Controlling Bias in Adaptive Data Analysis Using Information Theory", the AISTATS 2016 title. v3 and the journal version are "How much does your data exploration overfit? Controlling bias via information usage", *IEEE Trans. Inf. Theory* 66(1):302–323, January 2020, DOI 10.1109/TIT.2019.2945779 (Crossref-verified). "Russo & Zou 2016" in the brief refers to the AISTATS version; the version read here is the 2019/2020 journal text.
- [NOTE-306](NOTE-306.md) (on [LIT-347](../literature.d/LIT-347.md)) says Russo & Zou bounded bias by I(Λ_W(S);W) "for finite hypothesis classes". That is Xu & Raginsky's restatement in their own notation. Russo & Zou's quantity is I(T;φ): the information the *selection index* carries about the vector of all candidate statistics (Prop. 1). This is the same quantity when φ_i is the empirical risk of hypothesis i and T indexes the output hypothesis. The finiteness is of the candidate set, {1,…,m}; m "can be exponential in the number of samples" (§II).
- The learning-theory application differs between versions. v1 has a short §2.7 "Empirical Risk Minimization": excess loss E[µ_T] − min_i µ_i ≤ σ√(2H(T)/n) for ERM over m classifiers. v3 replaces it with §V-F, Prop. 5: E[L(f̂) − L̂(f̂)] ≤ √(I(f̂(x);Y)/(2n)) ≤ √(d·log₊(ne/d)/(2n)) for VC dimension d, with training inputs held fixed and only the labels random. Prop. 3 (the general-µ lower bound), the FDR bound (Prop. 6), the strong-data-processing refinement (Prop. 4), the LARS simulation and the Markov-chain data splitting (§V-G) are not in v1's section list.
- Four slips in v3, none of which affects a stated result:
  - The proof of Prop. 1 (p. 12) sums over i = 1..n instead of 1..m.
  - The last display in the proof of Prop. 2(1) (p. 14) drops the factor c·σ ("E[Y_T] ≤ cσ√(2I(T;Y)) ≤ √(2I(T;φ))"). The proposition's statement is right.
  - The proof of Prop. 5 (p. 18) says a Bernoulli variable is sub-Gaussian with "parameter less than 1/4" and that "σ ≤ 1/2n". The values consistent with the final bound √(I/(2n)) are 1/2 and 1/(2√n).
  - Prop. 13's proof (p. 20) writes E|W| = √(2ω_{k+1}/(πn)) for ω_{k+1}√(2/(πn)).
  - In addition, log₊ is defined as max{1, log z} in Prop. 5 and as max{0, log x} in Prop. 6. App. C.C also refers to an undefined Z_T and a sum to n−1, left over from an earlier draft.
