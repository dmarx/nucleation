---
status: Read
paper: LIT-tmpynu35
title: 'Attention Approximates Sparse Distributed Memory'
version: 1
history:
- version: 1
  date: '2026-09-27'
  note: >-
    Read in full (Full text of arXiv:2111.05498v2 (17 Jan 2022; NeurIPS 2021
    camera-ready), 57 pp., via PyMuPDF text extraction. I read the abstract,
    Introduction, §1–§8, the acknowledgements, the reference list and
    Appendices A.1–A.4 and B.1–B.7 (including B.7.1 Random Patterns and
    B.7.2 Learnt Projections). Figures 1–31 are plots or diagrams. I read
    their captions and the prose around them, not the images, so any value
    that appears only in a figure is unverified. That includes the βCD and
    βSNR marks in Fig. 4 and the Fig. 3 insets. No skim dossier existed for
    this work. I started from the Anthology's entry ANTH-LIT-641 and its
    theory ANTH-THEORY-097, and I checked both against the text. I
    recomputed the paper's exact circle-intersection formula (Eq. 2) and its
    β regression (Eq. 10) myself for n = 64 and n = 1000. Where those
    numbers are mine, the note says so.). The first NOTE on this paper,
    which was seeded from its abstract alone.
date: '2026-09-27'
summary: >-
  Kanerva's SDM read weights each stored pointer by the number of neurons
  in the intersection of two Hamming balls of radius d. The paper shows
  that this weight is roughly log-linear in Hamming distance for close
  patterns. As a result, with L²-normalised vectors and a
  regression-fitted β, softmax attention reproduces SDM's retrieval
  behaviour on random and learnt-projection data (App. B.7). Two things
  are weaker than they look. The analytic derivation (App. B.2, Eqs.
  16–21) gets the exponent wrong: by my recomputation its β is ≈2–2.5× too
  small. The biological case is Kanerva's 1988 cerebellar mapping,
  restated rather than re-argued. It also needs r = 2⁶⁴ ≈ 1.8×10¹⁹ neurons
  in the Attention setting, which the paper itself calls "biologically
  implausible" (App. B.5).
---

<!-- inactive-ok-file: THEORY-004 — Proposed: cited as the record's current account or reading, for comparison; the directive lapses when its status changes -->
<!-- inactive-ok-file: THEORY-008 — Proposed: cited as the record's current account or reading, for comparison; the directive lapses when its status changes -->
<!-- inactive-ok-file: THEORY-001 — Proposed: cited as the record's current account or reading, for comparison; the directive lapses when its status changes -->
<!-- inactive-ok-file: THEORY-007 — Proposed: cited as the record's current account or reading, for comparison; the directive lapses when its status changes -->
# NOTE-tmpk6gen: Attention Approximates Sparse Distributed Memory

## Contribution

The paper makes a known qualitative observation precise for the first time: Kanerva's SDM read operation (1988) and Transformer attention are the same normalised, similarity-weighted average of stored pointers, once the weighting is right. It contributes four things:
- an exact, more interpretable closed form for the Hamming-ball intersection (Eq. 2 / Eq. 12, after Jaeckel);
- a reason why that intersection is approximately exponential in distance (App. B.2);
- a continuous (hypersphere-cap) version of SDM (App. B.3, using the cap-intersection formulas of Lee & Kim);
- simulations in which eight SDM and fitted-softmax variants retrieve almost identically (App. B.7).

It also identifies Query-Key Normalisation as the Transformer variant that satisfies SDM's two requirements. Finally, it reuses the cerebellar mapping of SDM to propose a biological implementation of attention (§5).

## Key insight

In SDM a pattern's weight in the read-out is the number of neurons that both stored that pattern and were read by the query, which is the size of the intersection of two radius-d balls. That count falls roughly geometrically as the query moves away from the pattern. A geometric fall-off in Hamming distance is an exponential in cosine similarity, and a normalised exponential of cosine similarity is softmax attention with unit-norm vectors. So attention's softmax can be read as a population count over threshold neurons, and β is the read/write radius in disguise. A larger β means a smaller d, so fewer neurons and fewer patterns are consulted.

## Assumptions

- **Random patterns and random, uniformly distributed neuron addresses** in {0,1}ⁿ (§1). All optimal-d* values (Table 1) and all SNR and capacity results (App. B.4–B.5) depend on this. The authors call it "a strong assumption that deviates from … the learned representations used by Transformer Attention" (App. B.5).
- **Same radius d for read and write** (Eq. 1, Eq. 2).
- **A map h from binary to L²-normalised vectors with d(a, b) = ⌊n/2 (1 − âᵀb̂)⌋** (Eq. 5), "assume[d] … exists, at least approximately". For binary vectors this map exists exactly, as the bipolar rescaling x ↦ (2x − 1)/√n. The paper uses the bipolar identity d = (n − xᵀy)/2 in App. B.6 but does not point this out in §2. The substantive assumption runs the other way: that continuous queries and keys can be treated as images of binary vectors. In App. B.7 the authors binarise by sign and report that pairwise distances stay "approximately equal". No error is quantified.
- **Attention setting:** n = 64 (head dimension), m ≤ 1024 (GPT-2 context), and r = 2ⁿ. Floating-point weights are read as "every address holds a neuron" (App. B.5).
- **L²-normalised queries and keys, and a β fitted to the circle intersection** (§2, conditions (i)–(ii)). Softmax's standard β = 1/√n is not the fitted value.
- **SNR derivation (App. B.4):** bipolar pattern entries; intersection counts Iµ that are Poisson and i.i.d.; all non-target patterns exactly at the orthogonal distance n/2. The authors say this underestimates the variance, so the SNR is an upper bound.
- **Critical-distance and SNR/memory optima:** a noise-free query for SNR and memory, and a noisy query for critical distance (App. B.5).

## Key results

- **Exact circle intersection (Eq. 2/12, App. B.1).** I(dv, d, n) = Σ_{a=n−d−⌊dv/2⌋}^{n−dv} Σ_{c=max(0,n−d−a)}^{dv−(n−d−a)} C(n−dv, a)·C(dv, c). It is zero for dv > 2d. The paper checked it against Kanerva's own exact lune formula and against simulation (Fig. 11; n = 100, r = 10⁴, d = 35). It also reports that the book's tabulated intersection values lie between the exact equation and its continuous approximation (Fig. 10), and puts this down to rounding.
- **Exponential approximation, informal (Eq. 3).** I ≈ c₁ exp(−c₂ d(pa, ξ)) "for the closest, most important patterns where d(pa, ξ) ≤ 2d" (§1.1). App. B.2 is narrower: the log-linear fit holds "until around dv = 20" for the d = 15 example, and beyond that point the curve is super-exponential (Fig. 12).
- **Exponential approximation, analytic (App. B.2, Eqs. 16–21).** The derivation keeps only the largest summand, a = n−d−⌊dv/2⌋ and c = ⌊dv/2⌋, which gives a lower bound. It replaces each binomial coefficient by a Gaussian, sets ⌊dv/2⌋ ≈ dv/2, Taylor-expands 1/(1−dv/n) to first order (valid for dv/n ≪ 1, and the analysis is restricted to dv < 0.1n), and lower-bounds the non-exponential prefactor 2ⁿ⁺¹/(π√(dv(n−dv))) by its value at dv = n/2. The result is I ≳ (2ⁿ⁺²/πn) exp(−(n−2d)²/2n) · exp(−(n−2d)²/(2n²) · dv). In cosine form (Eq. 21) the implied β is (n−2d)²/(4n). The authors call this derivation of "moderate success".
- **Attention ≈ SDM (Eqs. 6–9).** With h, ξ̃ⁿᵉʷ = P̂p softmax(β P̂aᵀ ξ̂) ≈ Σ I(⌊n/2(1 − p̂aᵀξ̂)⌋, d, n) p̂p / Σ I(·). The same holds with the continuous cap intersection Ic in place of I (Eq. 9). β is fitted by the univariate log-linear regression of Eq. 10 on distances d(pa, ξ) < d, then extrapolated.
- **Continuous SDM (App. B.3, Eq. 22).** On the unit sphere, the neurons read are the intersection of two hyperspherical caps. The paper computes its area with the regularised incomplete Beta function (Lee & Kim). Unlike the binary case it stays nonzero beyond dv = 2d. The paper derives no analytic exponential approximation for it ("We do not attempt…").
- **SNR and capacity (App. B.4, Eqs. 25–27).** SNR ≈ E[I*] / √(E[I*] + (m−1)(E[Iµ] + E[Iµ]²)). Simulations (Fig. 16) show it is tighter than the book's variance formula. Capacity at z-score z is m = (E[I*]²/z² − E[I*]) / (E[Iµ] + E[Iµ]²) + 1.
- **Optimal radii (App. B.5, Table 1).** The SNR optimum is p* = (2mr)^(−1/3). I checked both values: the canonical setting (n = 1000, r = 10⁶, m = 10⁴) gives p* = 3.7×10⁻⁴ and d* = 447, and the Attention setting (n = 64, r = 2⁶⁴, m = 1024) gives p* = 2.98×10⁻⁸ and d* = 11. The memory-capacity optima are d* = 444 (canonical) and 5 (Attention). The critical-distance optima are d* = 448 and 15. For m ≤ 512, d*CD ranges from 16 to 22 (Fig. 17c).
- **Trained β (§3, Fig. 4).** QK-norm heads on the five low-resource translation tasks of Henry et al. learn β ∈ [10, 25]. The values came by private correspondence. GPT-2 small and large give an effective β (the maximum observed softmax input) in [3, 71], almost all in [3, 12] (App. A.2, Fig. 5). Across layers it follows a high–dip–spike–fall pattern, which the paper compares with Ramsauer et al.'s BERT analysis (Fig. 7).
- **Hopfield as a special case (App. B.6).** Set d_write = 0 and neurons = patterns, remove the read threshold, and use the raw bipolar dot product instead of Hamming distance. SDM then becomes the Hopfield update ξⁿᵉʷ = g(PaPaᵀξ). This follows Keeler 1988.
- **Value-norm observation (App. A.3, Fig. 8).** In GPT-2, some low-attention tokens have value vectors with large L² norms, so attention weights alone misstate what each token contributes. A GPT-2 trained with L²-normalised values reached "virtually identical" training performance. The paper names no dataset or numbers beyond "an autoregressive word corpus benchmark".
- **Convergence experiments (App. B.7).** The paper compares eight algorithms on random patterns (n = 64 and 1000, m = 1024; 15,360 convergences per perturbation level) and on MNIST and CIFAR-10, both raw and through a learnt n = 64 projection. It reports "close agreement between all of the algorithms", with named exceptions:
  - d = 5 at large perturbation (binary circle intersection vanishes);
  - d = 19 at perturbation 12 for Binary-SDM-Binary-Fit-Attention ("unclear");
  - canonical d = 447 at large perturbation, where the true circle intersection beats every fitted-softmax variant ("We cannot explain this difference currently").

  The learnt projections do not generalise to test data (Figs. 30–31).

### What my recomputation of the approximation shows

I evaluated Eq. 2 exactly and fitted Eq. 10 as the paper describes. This is my calculation, not the paper's.
- **The intersection is a staircase.** I(2k−1) = I(2k) exactly at every radius I checked (n = 64: d = 5, 11, 15; n = 1000: d = 447, 451), so the exponential fits an envelope. Over d(pa, ξ) < d the log-linear fit has R² = 0.89 (d = 5), 0.97 (d = 11) and 0.98 (d = 15) at n = 64, and 0.99 at n = 1000. Fitted to even distances only, R² rises to ≥ 0.998 at n = 64.
- **The fit window moves β.** At n = 64, d = 11: β = 14.4 fitted on dv < d, but 19.3 on dv ≤ 2d. At n = 1000 the curve is not exponential over dv ≤ 2d at all (R² ≈ 0.68). The "≤ 2d" range quoted in §1.1 and the Fig. 3 caption overstates where the approximation holds. B.2's "until around dv = 20" (for d = 15) is the accurate statement.
- **The analytic β of Eq. 21 is off by a factor of about 2–2.5.** β_analytic = (n−2d)²/(4n) gives 11.4, 6.9 and 4.5 for n = 64 at d = 5, 11, 15. The regression gives 28.4, 14.4 and 9.4. The single largest summand alone reproduces the regression slope (e.g. 14.8 vs 14.6 for d = 11, even distances), so the error is not in keeping the largest term. It comes from replacing a far-tail binomial coefficient by a Gaussian. At n = 64, d = 11 the lower summation limit sits about 5 standard deviations from the mean, where the Gaussian badly underestimates the decay rate. By hand: C(64,11)/(2·C(62,10)) ≈ 3.46 per two Hamming steps, which is β ≈ 20 at dv = 0, against 6.9 from Eq. 21. B.2 therefore explains why the intersection is exponential-like. It does not supply the constant the approximation uses, which comes from the regression.
- **Normalised-weight discrepancy.** Place one pattern at every distance 0…64 and compare the normalised SDM and fitted-softmax weights. Their total-variation distance is 0.16 (d = 5), 0.12 (d = 11) and 0.09 (d = 15).
- **Weight on far patterns.** The paper's argument that far patterns do not matter (Fig. 3, App. B.2: normalised weights "≈ 0") looks at one pattern per distance. With m = 1024 random patterns at about the orthogonal distance n/2 and the query equal to its target, softmax gives the non-targets a total weight of about m·e^(−β)/(1 + m·e^(−β)). That is ≈ 0.07 at βCD ≈ 9.4 and ≈ 6×10⁻⁴ at βSNR ≈ 14.4, where SDM gives them exactly 0 (dv > 2d). Wide-radius instances therefore disagree more than Fig. 3 suggests. App. B.7's convergence plots show that this disagreement does not change retrieval outcomes on random patterns.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Eq. 2 is the exact Hamming-ball intersection size | proof + check | App. B.1 derivation; agreement with Kanerva's lune formula and simulation (Fig. 11) |
| C2 | The circle intersection is approximately exponential in distance for close patterns | experiment (numerical) + informal argument | Figs. 2, 3, 12–14. The staircase structure goes unmentioned; see my recomputation above |
| C3 | The circle intersection is approximately exponential "where d(pa, ξ) ≤ 2d" | weak (contradicted in part by the paper's own App. B.2) | §1.1 and Fig. 3 caption vs App. B.2 ("until around dv = 20" for d = 15) |
| C4 | An analytic exponential bound follows from the Gaussian approximation (Eq. 20/21) | informal derivation, "moderate success" | App. B.2. By my recomputation its β is ≈ 2–2.5× too small in the Attention setting |
| C5 | Attention with L²-normed vectors and fitted β closely approximates SDM | experiment | App. B.7, Figs. 18–31. Qualitative plot agreement with three named, partly unexplained exceptions; no quantitative error metric |
| C6 | SDM "predicted" Query-Key Norm | retrodiction (assertion of priority reversed) | QK-norm (2020) predates the paper; App. A.1 concedes "this idea … was already tested" |
| C7 | Trained QK-norm heads learn β ∈ [10, 25], interpolating between the CD- and SNR-optimal βs | measurement (third-party, private correspondence) + weak reference | Fig. 4. The optima assume random patterns, which the authors call "only a weak reference". βMem = 35.5 lies outside the band (Fig. 7 caption) |
| C8 | Pre-trained GPT-2 satisfies the conditions / uses SDM-like β | weak | App. A.2. The effective β is a maximum-observed-input heuristic, mostly in [3, 12]; GPT-2 does not L²-normalise; the abstract says "confirm" |
| C9 | Hopfield networks are a special case of SDM | informal argument | App. B.6, after Keeler. It needs the threshold replaced by a raw dot product, which is a change of rule rather than a parameter setting, so "generalization" is loose |
| C10 | Feed-forward layers can be "directly interpreted as SDM" | argument by citation | §4, from Sukhbaatar et al. and Geva et al.; no new evidence |
| C11 | LayerNorm plays the role of L² normalisation | informal argument | §4; the authors themselves note that LayerNorm does not bound dot products to [−1, 1] |
| C12 | Attention weights are misleading without value-norm normalisation | experiment (descriptive) | App. A.3, Fig. 8 (500,000 sampled tokens per model) |
| C13 | L²-normalising value vectors leaves GPT-2 performance unchanged | experiment, unreported detail | App. A.3; no dataset, metric or numbers given |
| C14 | Multi-head attention lets SDM model probabilistic outputs | informal argument | §4, an A→B / A→Z example |
| C15 | The cerebellar cortex can implement SDM's three connectivity requirements, hence attention | assertion via prior literature | §5, restating Kanerva 1988/1993. Undercut for attention specifically by App. B.5 (r = 2⁶⁴ is "biologically implausible") and by the finite-neuron results (B.7) |
| C16 | The softmax "emerges with no additional computational cost" from binary threshold neurons | informal argument | §6. True of the weights in expectation with exhaustive neurons; with biologically sized r the weights are coarse integers, and convergence degrades (App. B.5, B.7, Figs. 19, 22, 28–29) |

## Method

SDM (the pattern view, Eq. 1) is written as a normalised weighted sum of pattern pointers. The weights are the ball-intersection counts, followed by an element-wise majority threshold g. Attention (Eq. 4) is rewritten in SDM notation: keys are pattern addresses, values are pointers, the query is the read address. The two are identified through the binary-to-sphere map (Eq. 5), the exponential approximation (Eqs. 3, 6), and a β fitted by log-linear regression (Eq. 10). Optimal radii come from an SNR model (App. B.4) optimised three ways (App. B.5). The comparison with trained models reads β from QK-norm checkpoints and infers an "effective β" for GPT-2 as the largest softmax input over eight long prompts. The experiments run eight SDM and softmax variants on autoassociative recovery from perturbed queries, iterating up to 100 times for random patterns and up to 10 at test time for the learnt projections.

## Concepts

- **Pattern address / pointer**: the key under which a memory is stored, and the content returned. Autoassociative if the pointer is the address, heteroassociative otherwise.
- **Neuron (hard location)**: a fixed random address xτ with a storage vector that superposes the pointers of all patterns within d of it.
- **Circle intersection I(dv, d, n)**: the number of the 2ⁿ addresses within d of both query and pattern. Multiplied by r/2ⁿ, it is the expected number of neurons.
- **p**: the fraction of the space inside a radius-d ball. It is independent of n, which makes it the paper's preferred parameter.
- **d*SNR / d*Mem / d*CD**: the radius maximising, respectively, a noise-free query's retrieval probability, the number of storable patterns at 99% whole-pattern retrieval, and the tolerable query noise.
- **Critical distance**: the largest query–target distance from which iterated reads still converge to the target.
- **Effective β**: for unnormalised attention, the maximum softmax input observed per head, used as a stand-in for a learned temperature.
- **Continuous SDM**: SDM on the unit sphere, where neurons are read if they lie within cosine 1 − 2d/n and weights are cap-intersection areas.

## Connections

**What the approximation is, stated as a kernel statement (my formulation; the paper never uses the word "kernel").**
- **The ball intersection is a positive-definite kernel.** With r = 2ⁿ, I(dv, d, n) = Σₓ 1[d(x, ξ) ≤ d]·1[d(x, p) ≤ d] is the autocorrelation of the ball indicator on the group ℤ₂ⁿ. It is therefore a positive-definite kernel that depends only on Hamming distance, because its Fourier transform is the squared transform of the ball indicator. With r finite random neurons it is, up to the factor r/2ⁿ, the expectation of the inner product φ(ξ)ᵀφ(p) of binary random features φτ(x) = 1[d(x, xτ) ≤ d].
- **The continuous version is the same construction on the sphere.** The cap intersection Ic is the autocorrelation of a cap indicator on S^(n−1), so it is a zonal positive-definite kernel.
- **The exponential side is also positive definite.** exp(β x̂ᵀŷ) is positive definite on the sphere (its power series has nonnegative coefficients) and is the unnormalised von Mises–Fisher density with concentration β. Softmax(β P̂aᵀξ̂) is therefore exactly the posterior responsibility of an equal-weight vMF mixture centred at the stored addresses.
- **What the paper's approximation amounts to.** It is a statement about two zonal positive-definite kernels, both used as Nadaraya–Watson (normalised kernel-smoother) weights. It says that the compactly supported ball-autocorrelation kernel is approximately log-linear in the inner product over a local window, roughly d(pa, ξ) < d at n = 64. The conditions are: the Attention parameters or large n; a regression-fitted β, not the analytic one; and exhaustive neurons (r = 2ⁿ) or r large enough that integer counts do not quantise the weights. It cannot hold globally, because the binary kernel vanishes beyond 2d and the exponential never does.

**Neuron-view SDM is linear attention with a fixed binary feature map (my observation).** The storage is xᵥ = Σµ φ(pµ) pₚ^µᵀ, and the read is φ(ξ)ᵀxᵥ / φ(ξ)ᵀΣµ φ(pµ). This is exactly Katharopoulos et al.'s linear attention ([ANTH-LIT-428](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-428.md)) with feature map φ = thresholded random projections. The paper cites that work (its [49]) only for the claim that removing softmax hurts performance. It describes Performer (its [42]) as using "a reduced set of latent keys and values". Performer's own mechanism is positive random features approximating the softmax kernel, which is the closer analogue of SDM's random neurons. Neither record holds Performer, so that description is from general knowledge and unverified here.

**Van Rijsbergen's retrieval geometry ([LIT-262](../literature.d/LIT-262.md), [NOTE-239](NOTE-239.md)).**
- **The shared form is a kernel over a stored set.** GIR scores a document y against a query or cluster ρ = Σ aᵢ|xᵢ⟩⟨xᵢ| by tr(ρ|y⟩⟨y|) = Σ aᵢ cos²(xᵢ, y). SDM/attention computes Σ w(cos(pµ, ξ)) pₚ^µ with w = I or exp(β·).
- **The kernels differ.** GIR's is cos², the Hilbert–Schmidt inner product of the rank-one projectors |x⟩⟨x| and |y⟩⟨y|, i.e. a degree-2 polynomial kernel on unit vectors (the Born rule). SDM/attention's is a sharp, local kernel (ball autocorrelation, or exp(β cos)). Its sharpness, set by d or β, is the design parameter, and GIR has no analogue for it.
- **The outputs differ.** GIR returns a score or probability per document: ranking, with the query fixed. SDM/attention returns a new vector, a weighted mixture of pointers, and may iterate. That is retrieval as reconstruction (the Best Match Problem of Minsky & Papert), not as ranking.
- **The normalisations differ.** GIR normalises the query-side mixture (tr ρ = 1). SDM normalises over the stored memories (the denominator of Eq. 1, softmax's partition function).
- **The operators correspond, as my inference.** GIR's cluster-representative-as-mixed-state corresponds to SDM's neuron storage vector, a superposition of the pointers written to it. The heteroassociative storage Σµ φ(pµ) pₚ^µᵀ is a cross-moment operator in feature space where GIR's ρ is a second-moment operator. Neither work draws this comparison.
- **What is invariant.** Both are invariant under a joint orthogonal change of basis in the continuous setting, as is everything that depends only on inner products. Binary SDM is invariant only under the hypercube's symmetries.

**Kernel THEORY documents.**
- **[THEORY-004](../theory.d/THEORY-004.md):** attention and continuous-SDM weights depend on the query and keys only through their cosines, so any two realisations with the same Gram matrix read out identically. This is consistent with [THEORY-004](../theory.d/THEORY-004.md) and neither supports nor tests it.
- **[THEORY-008](../theory.d/THEORY-008.md):** SDM/attention's readout is not the regularised linear readout of [THEORY-008](../theory.d/THEORY-008.md). It is a nonlinear normalised kernel smoother, which is outside [THEORY-008](../theory.d/THEORY-008.md)'s stated scope ("anything about nonlinear readouts" is excluded).
- **[THEORY-001](../theory.d/THEORY-001.md) / [THEORY-007](../theory.d/THEORY-007.md):** softmax over exp(β cos) with L²-normalised features is the same functional form as the InfoNCE critic with temperature τ = 1/β. [THEORY-001](../theory.d/THEORY-001.md)'s population optimum makes that critic proportional to the positive-pair density ratio. So a learned QK-norm β plays the role of a learned contrastive temperature, and in that reading attention weights are a posterior over which stored key is the "positive". This is my inference; the paper does not make it. Nothing here bears on [THEORY-007](../theory.d/THEORY-007.md)'s eigenfunction result.
- **Mean embeddings ([LIT-260](../literature.d/LIT-260.md)):** SDM's normalised read is a ratio of two feature-space sums, the empirical embeddings of the pointer-weighted and unweighted address distributions, evaluated at φ(ξ). This is my inference. I have not checked whether [LIT-260](../literature.d/LIT-260.md) covers conditional or cross-covariance embeddings (unverified).

**Neuroscience holdings.**
- [LIT-153](../literature.d/LIT-153.md) (Angius et al.) sorts explanations of transformer success into functional analysis, mechanism sketches and brain-score co-simulation. Bricken & Pehlevan is a fourth kind: a formal correspondence between a trained operation and a biologically motivated algorithm. They offer it as "a novel mechanistic perspective". On Angius et al.'s terms it would count as a mechanism sketch at best, because the cerebellar mechanism is posited, not observed in the model. This placement is my reading.
- [LIT-148](../literature.d/LIT-148.md) (computational functionalism for deep networks) is the philosophical frame in which "attention is implementable by cerebellar circuitry" would matter.
- [LIT-250](../literature.d/LIT-250.md) and [LIT-257](../literature.d/LIT-257.md), both neuroscience-tagged, concern kernel-level comparison of representations, the invariants the Connections above rely on.
- The record holds no Marr–Albus–Ito cerebellar work, no Kanerva, and no Hopfield-network or Ramsauer et al. paper. The Anthology holds Kanerva's book and review ([ANTH-LIT-666](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-666.md), [ANTH-LIT-669](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-669.md)), QK-norm ([ANTH-LIT-640](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-640.md)), Geva et al. ([ANTH-LIT-575](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-575.md)), Layer Normalization ([ANTH-LIT-005](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-005.md)) and Attention Is All You Need ([ANTH-LIT-008](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-008.md)).

## Bearing on the record

**For this record,** the paper belongs to the associative-memory and retrieval thread: a content-addressable read written as a kernel-weighted average. It sharpens [LIT-262](../literature.d/LIT-262.md)'s retrieval geometry by showing a different, local and tunable kernel at work in a memory rather than a ranking system. It should not source a THEORY on the biology.

**The cerebellar case, section by section:**
- **Introduction.** It rests on citation ("maps strikingly well onto the cerebellum [13, 16]") and on SDM respecting Dale's law. No evidence is offered in this paper.
- **§5.** Three connectivity requirements are mapped as follows:
  - address decoding → granule cells sharing mossy-fibre input;
  - distributed storage → parallel-fibre–Purkinje synapses under climbing-fibre LTP/LTD;
  - summation and threshold → Purkinje cells.

  The mushroom-body relabelling (Kenyon cells, dopaminergic neurons, output neurons) is cited to Modi et al. This is Kanerva's mapping, restated. The authors list open problems themselves: sparse granule dendrites, inhibitory interneurons, mossy/climbing-fibre timing for STDP, and Purkinje interval timing.
- **App. B.5.** It shows the Attention instance needs r = 2⁶⁴ ≈ 1.8×10¹⁹ neurons, "many orders of magnitude greater than the number of granule cells". With a biological r in n = 64, only d = 19 keeps a nonzero critical distance (App. B.7.1). Weights are then coarse integer counts, and convergence degrades as r falls (Figs. 19, 22, 28–29).
- **Not addressed.** Attention's keys and values are ephemeral: every token is written and read within one forward pass. A cerebellar implementation would therefore need one-shot synaptic writes at token rate, which the paper does not discuss. §4 instead assigns persistent memory to the feed-forward block.

In sum, the biological case for SDM is Kanerva's and is plausible at the level of connectivity. The biological case for attention in particular is weak, and partly undercut by the paper's own appendix.

**For ML practice** the paper carries two things, both already held in the Anthology. One is the QK-norm reading ([ANTH-LIT-641](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-641.md), [ANTH-THEORY-097](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-097.md), and the practice [ANTH-SOTA-192](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/practices.d/SOTA-192.md) that the theory explains). The other is the value-norm caution for interpreting attention weights (App. A.3). The corrections above go to the Anthology's owner.

## Limitations

- The random-pattern assumption underlies every d* and β reference. The authors call the resulting βs "only a weak reference" (§3).
- The analytic exponential (App. B.2) is qualitative. It lower-bounds with a single summand, uses a Gaussian where the binomial tail is far from Gaussian, drops a dv-dependent prefactor, and holds only for dv < 0.1n. The β actually used comes from a regression whose value depends on the fit window.
- The staircase structure of I (equal values at distances 2k−1 and 2k) is not mentioned. It limits how exponential the binary kernel can be.
- The validation experiments report agreement by eye from plots. No error metric is given, and two discrepancies are left unexplained.
- The GPT-2 "effective β" depends on the prompts (eight texts, one of only 195 tokens) and is a maximum, not a fit. The abstract's "confirm" outruns App. A.2.
- The QK-norm β band is third-party data from private correspondence, and I could not check it. The head dimension of those models, which the reference βs assume is 64, is not stated (unverified).
- The value-norm training experiment reports no dataset or numbers.
- The Hopfield "special case" needs a change of weighting rule, not a parameter choice.
- The biological implementation of attention needs a neuron count the paper itself calls implausible, and it does not address fast, per-token writing.

## Open questions

- Is there a correct analytic β(n, d)? A large-deviation (entropy) treatment of the tail binomial in place of the Gaussian should give the slope. By hand it gives ≈ 20 at dv = 0 for n = 64, d = 11, against a regression value of 14.4. Worked out, it would replace Eq. 21.
- [ANTH-THEORY-097](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-097.md)'s promotion test would settle whether the correspondence predicts anything. Does retrieval accuracy in a trained QK-norm model degrade with context length m along the shape the SDM capacity formula (Eq. 26) gives?
- How does a biologically sized r (≤ 10¹¹, or fewer per microzone) trade off against n, so that a cerebellar SDM approximates a softmax to a stated tolerance? And is any cerebellar or mushroom-body circuit known to write at the rate attention requires?
- Does the vMF/InfoNCE reading, with β as an inverse temperature and attention as a posterior over keys, predict the learned β band better than SDM's random-pattern optima do?

## Corrections to the seeded skim

- [ANTH-LIT-641](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-641.md) says the learned QK-norm range β ∈ [10, 25] "interpolates between" SDM's three optimality criteria (critical distance, SNR, memory capacity), and [ANTH-THEORY-097](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-097.md) says the same ("interpolates between SDM's critical-distance, signal-to-noise and memory-capacity optima"). The paper does not say this, and its own numbers contradict it. The Fig. 7 caption gives the memory-optimal β = 35.5, "much larger than the largest learned βs in Query-Key Norm". The main text claims interpolation only "in particular with the critical distance optimal … and the SNR optimal" (§3, p. 7). My own regression by the paper's stated method (Eq. 10, fit over d(pa, ξ) < d, n = 64) gives βCD ≈ 9.4 (d = 15), βSNR ≈ 14.4 (d = 11) and βMem ≈ 28–33 (d = 5, depending on the fit window). The learned band runs from about βCD to below βMem. I could not reproduce the paper's 35.5 exactly (unverified).
- [ANTH-LIT-641](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-641.md) says §4 "interprets LayerNorm, the feed-forward block and the residual stream through the SDM frame". The paper never mentions the residual stream (the word does not occur in the text). §4 interprets the feed-forward layer, LayerNorm (with its value-vector-norm corollary, App. A.3), multi-head attention, and hierarchical stacking, which it calls an unreconciled difference.
- [ANTH-THEORY-097](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-097.md) says the critical-distance optimum "is derived in Kanerva's book ([ANTH-LIT-666](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-666.md)), the other two in his 1992 review ([ANTH-LIT-669](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-669.md))". The paper attributes SNR and critical distance to [15] (Kanerva, "Sparse distributed memory and related models", which the paper dates 1993). Its Fig. 17(a) reproduces the book's Fig. 7.3 convergence plot. The memory-capacity optimum is derived in the paper itself (App. B.4 Eq. 26, App. B.5). The three optima as reported for the Attention parameters (Table 1) are the paper's own computations. This is reported, not fixed. The anthology may hold a date for LIT-669 that differs from the paper's reference list.
- [ANTH-LIT-641](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-641.md) reports the GPT-2 check with the authors' gloss, "largely in agreement". The numbers are these: effective β in [3, 71], "almost all" in [3, 12] (App. A.2, Fig. 5). That is mostly below the QK-norm band. The authors reconcile the two by arguing that the inferred values are lower bounds. The abstract's "We confirm that these conditions are satisfied in pre-trained GPT2" claims more than App. A.2 shows. GPT-2 does not L²-normalise its queries and keys, and its "effective β" is the maximum observed softmax input, not a fitted temperature.
- [ANTH-LIT-641](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-641.md)'s other statements are accurate: the correspondence, its two conditions, the QK-norm retrodiction (which App. A.1 itself concedes: "It turns out this idea … was already tested"), the private-correspondence source of the [10, 25] figure, and the authors' "weak reference" caveat, quoted correctly from §3.
