---
number: 315
status: Skimmed
formerly:
- NOTE-tmpiyyzi
paper: LIT-364
title: 'The Theory of Signal Detectability. Part I: The General Theory; Part II: Applications with Gaussian Noise'
version: 1
history:
- version: 1
  date: '2026-09-30'
  note: >-
    Read in part (The 1953 technical report, not the 1954 journal paper. The
    work is registered as the report: University of Michigan Engineering
    Research Institute, Electronic Defense Group, Technical Report No. 13,
    in two separately issued parts. Part I, "The General Theory", is dated
    June 1953 (DTIC AD0016786, 60 PDF pp.). Part II, "Applications with
    Gaussian Noise", is dated July 1953 (DTIC AD0016787, 99 PDF pp.). Both
    are Signal Corps contract DA-36-039 sc-15358 reports approved for
    release. I read them as the DTIC scans mirrored on the Internet
    Archive's US-government-documents collection (identifiers
    DTIC_AD0016786, DTIC_AD0016787). DTIC's own server and UMich Deep Blue
    (hdl 2027.42/7068) both refused this session. DTIC stamps the scans
    "best quality available … a significant number of pages which do not
    reproduce legibly". The text layer is poor OCR, so I read it alongside
    page images of every page carrying a theorem statement, key equation,
    figure or conclusion. **Part I: all of it**, printed pp. 1–50 plus the
    errata sheet and the symbol list: §1 (pp. 1–11), §2 Theorems 1–8 with
    proofs (pp. 12–30), Appendix A (pp. 31–32), Appendix B Lemmas 1–4 (pp.
    33–41), Appendix C Theorems C1–C4 (pp. 42–47) and the bibliography.
    **Part II, read closely:** §3 (pp. 1–8), §4.1–4.2 (signal known exactly,
    pp. 9–13, including Fig. 4.1), §4.3 (pp. 17–21), §5 in full (pp. 55–71:
    5.1.1–5.1.6, 5.2 receiver design, and the conclusions). **Part II,
    skimmed** from the OCR plus figures: §4.4–4.9 (noise-like signal,
    broad-band video receiver, radar pulse train, approximate evaluation, M
    orthogonal signals), Appendices D (sampling theorem), E and F (RC-filter
    approximation), and the bibliography. The Part II derivations in
    §4.4–4.9 are partly illegible in this scan. Printed page numbers are
    cited; in Part I, printed page = PDF page − 8. `published:` is
    1953-06-01, the first day of Part I's issue month; the day is not
    printed. There is no anthology entry for this work (grep of
    /home/user/anthology-of-the-sota/record/literature.d for "detectab" and
    "Birdsall" found nothing), and no nucleation entry.). The first NOTE on
    this paper, which was seeded from its abstract alone.
date: '2026-09-30'
summary: >-
  Peterson and Birdsall show that the criterion approach (maximise P_SN(A)
  − β·P_N(A), or maximise detection at fixed false-alarm k) and the
  Woodward–Davies a-posteriori approach are all solved by one receiver
  that computes the likelihood ratio ℓ(x) = f_SN(x)/f_N(x) and thresholds
  it (Part I, Theorems 1–7). They introduce the receiver operating
  characteristic, whose slope at each point is the threshold β (Theorem 8,
  Eq. 2.51). For a signal known exactly in white Gaussian noise, ln ℓ is
  normal with equal variance 2E/N₀ under both hypotheses and means 2E/N₀
  apart, so the ROC is a one-parameter family indexed by the "detection
  index" d = (M_SN − M_N)²/σ² = 2E/N₀ (Part II, Eqs. 4.1–4.8, Fig. 4.1).
  The receiver is a correlator or matched filter (Eq. 5.3, 4.10).
---

# NOTE-315: The Theory of Signal Detectability. Part I: The General Theory; Part II: Applications with Gaussian Noise

## Contribution

Before this report, radar-detection work used two statistical framings. One was the "criterion" approach, which asks yes or no and trades false alarms against misses (Lawson and Uhlenbeck, North, Middleton, and others). The other was Woodward and Davies' a-posteriori-probability approach. The report proves that one receiver, one that outputs the likelihood ratio, is optimal for all of them (Part I §2.6: "In this theory likelihood ratio plays the central role"). It gives existence and uniqueness proofs under general hypotheses, including analytic noise densities and Lebesgue-measure versions. It introduces the **receiver operating characteristic** (P_SN(A) against P_N(A)) as the complete summary of a receiver, and proves that the optimal ROC's slope is the operating likelihood-ratio level. Part II then computes likelihood-ratio distributions, and hence ROCs, for Gaussian-noise cases from the signal known exactly to signals with unknown phase, time or frequency, and it quantifies how signal uncertainty costs energy.

## Key insight

Everything the receiver needs is the scalar ℓ(x) = f_SN(x)/f_N(x). Every optimality criterion, and the posterior probability P_x(SN) = P(SN)ℓ(x)/[P(SN)ℓ(x) + 1 − P(SN)] (Eq. 1.2/2.10), is a monotone function of ℓ, so the criteria differ only in where they set the threshold β. Receiver performance is then the pair of complementary distribution functions (F_N(β), F_SN(β)) of ℓ, and dF_SN = β dF_N ties them together. When ln ℓ is normal with equal variances, one number d fixes the whole ROC.

## Assumptions

- **Finite-dimensional input.** Inputs are band-limited to W and observed over [0, T]. By the sampling theorem each input is a point in a 2WT-dimensional space R (Part I §2.2, p. 12; Part II App. D).
- **Densities exist.** f_N and f_SN exist, with signal and noise independent and f_SN(x) = ∫ f_N(x − s) dP_S(s) (Eqs. 2.1–2.2). Appendix A sketches the measure-theoretic extension.
- **Uniqueness (Theorems 3–4)** needs f_N analytic, plus Lemma 3 or 3′ (bounded signal energy suffices; Gaussian noise satisfies it).
- **Deterministic operator.** The operator always gives the same response to the same input (Part I p. 3 fn.). Appendix A shows that randomised responses p(x) add nothing.
- **Part II noise** is white Gaussian, band-limited to W, with noise power N and N₀ = N/W per unit bandwidth: f_N(x) = (2πN)^(−n/2) exp[−Σx_i²/2N] (Eq. 3.2a). Non-white band-limited noise is to be pre-whitened (p. 4 fn.).
- **Signal known exactly** (§4.2): s(t) is completely specified.

## Key results

**Part I (general theory).**
- **Eq. 1.4–1.6 (p. 6–7).** With values and costs on the four outcomes, maximising expected value is equivalent to maximising P_SN(A) − β·P_N(A), where β = [1 − P(SN)](V_N·CA + K_N·A) / [P(SN)(V_SN·A + K_SN·CA)].
- **Theorem 1 (p. 16).** The set A = {x : ℓ(x) ≥ β} is an optimum criterion A₁(β), maximising P_SN(A) − β·P_N(A). The proof compares A with any B over A−B and B−A.
- **Theorem 2 (p. 18).** Any A₁(β) contains, up to probability zero, all points with ℓ > β and none with ℓ < β.
- **Theorems 3–4 (p. 20).** If f_N is analytic, {ℓ = β} has probability zero, so A₁(β) is unique up to null sets. The proof is in Appendix B.
- **Theorem 5 (p. 20–22).** A likelihood-ratio set with P_N(A) = k is an optimum criterion A₂(k): it maximises P_SN subject to P_N ≤ k. This is the Neyman–Pearson form.
- **Theorems 6–7 (pp. 22–24).** For every k in (0, 1) there is an A₁ with P_N = k (using Lemma 4 to split atoms), and every A₂(k) is an A₁(β_k). The two optimum types coincide.
- **Theorem 8 (p. 24–26).** On intervals where ℓ has no gaps, β_k is single-valued and continuous and dP_SN(A₁(β_k))/dk = β_k. The ROC's slope is the threshold (Eq. 2.51: dF_SN(β)/dF_N(β) = β; Eq. 2.52: F_SN(β) = −∫_β^∞ y dF_N(y)).
- **Corollary (Eq. 2.53, p. 28).** The n-th moment of ℓ under noise alone equals the (n−1)-th moment under signal plus noise. Hence E_N[ℓ] = 1, E_SN[ℓ] = 1 + σ_N², and the difference of means equals σ_N². Detection "corresponding roughly to Fig. 2.1" needs σ_N² ≈ σ_N, i.e. σ_N² of order unity (Eq. 2.54).
- **§1.6 and Figs. 1.2–1.3 (pp. 8–10).** The ROC is introduced. No receiver lies above the optimal curve (1); the reflected curve (3) is a floor; the diagonal is guessing. A non-optimum receiver can be given "a db rating" against the optimum.
- **Appendix C (pp. 42–47).** "k-equivalence" characterises uniformly best tests (Theorems C1–C2). Signal ensembles differing only in energy are k-equivalent for the signal known exactly, known except for phase, and noise-like cases, so for these the optimal receiver needs no knowledge of the energy (Theorems C3–C4).

**Part II (Gaussian noise).**
- **Eq. 3.7–3.9 (pp. 6–7).** ℓ(x) = ∫ exp(−E(s)/N₀) exp[(2/N₀)∫x(t)s(t)dt] dP_S(s): the likelihood ratio for an ensemble is the average of the known-signal ratios.
- **§4.2, signal known exactly (pp. 9–11).** ℓ(x) = exp(−E/N₀) exp[(2/N₀)∫₀ᵀ x(t)s(t)dt] (4.1b). The statistic (1/N)Σx_i s_i is normal, with variance 2E/N₀ (Eq. 4.2: "2 × Signal Energy / Noise Power Per Unit Bandwidth"), mean 0 under noise alone and mean 2E/N₀ under signal plus noise. With β = exp(−E/N₀ + α):
  - F_N(β) = √(N₀/4πE) ∫_α^∞ exp[−½(N₀/2E)y²] dy (4.4);
  - F_SN(β) = √(N₀/4πE) ∫_α^∞ exp[−(N₀/4E)(y − 2E/N₀)²] dy (4.8).
  - "α, and therefore ln β, has a normal distribution with signal plus noise as well as with noise alone; the variance of both distributions is 2E/N₀, and the difference of the means is 2E/N₀" (p. 11). Fig. 4.1 plots the ROC family for d = ¼, ½, 1, 2, 4, 8, 16, with d = 2E/N₀.
- **§5.1.1 worked numbers (p. 55).** With E = 2N₀ (d = 4), a receiver can reach false-alarm 0.25 with detection 0.90. At false-alarm ≤ 0.10, detection is ≤ 0.76. False-alarm ≤ 0.023 with detection ≥ 0.98 requires E ≥ 8N₀. (Checked here: with d′ = √d these are Φ(2 − 0.674) = 0.907, Φ(2 − 1.282) = 0.764 and, at d = 16, Φ(4 − 2.0) = 0.977. So the report's curves are the equal-variance normal ROC with separation √d.)
- **§4.3 and Fig. 5.2.** For a signal known except for carrier phase, the ROC lies below the known-signal curve for the same 2E/N₀. The distributions involve the Bessel function I₀ (noise alone gives a Rayleigh-type envelope, Eq. 4.22; signal plus noise a Rice-type, Eq. 4.26).
- **§4.4, noise-like signal (p. 26).** For small S/N and many samples, the equal-variance approximation holds with d = (2n − 1)(1 − √(N/(N+S)))² ≈ (n/2)(S/N)² (Eq. 4.37). For the broad-band receiver and the incoherent pulse train, d ≈ (1/4M)(2E/N₀)² (Eq. 4.71).
- **§5.1.3 (p. 59).** As a general approximation, fit any ROC by the Fig. 5.1 family with d = ln(1 + σ_N²) (Eq. 4.94), which is exact when ln ℓ is normal. σ_N² "seems to characterize signal detectability better than any other single number".
- **§5.1.4–5.1.6 (pp. 60–62).** For a signal that is one of M orthogonal equal-energy signals, σ_N² = (1/M)[exp(2E/N₀) − 1] (4.102) and d = ln[1 − 1/M + (1/M)exp(2E/N₀)] (4.103). With unknown phase, exp is replaced by I₀ (4.117–4.118). Solving gives 2E/N₀ ≈ ln M + ln(e^d − 1) for large 2E/N₀ (Eq. 5.2; error under 10% if 2E/N₀ > 3). At fixed detectability, the energy needed grows linearly in ln M. A footnote generalises this to unequal priors as −ln Σp_i² (not entropy) (p. 62 fn. 2).
- **§5.2 (p. 64).** For the signal known exactly, the optimal receiver computes the cross-correlation ∫₀ᵀ s(t)x(t)dt (Eq. 5.3), equivalently a filter with impulse response h(t) = s(T − t) (Eq. 4.10) read at time T. This "is the same filter specified by Middleton, Van Vleck, Wiener, North, and [others] … which maximizes signal-to-noise ratio" (p. 65, OCR-degraded). The ratio of the correlation to N₀ is half of ln ℓ.

## Claims

Restricted to the parts read closely: all of Part I, and Part II §§3, 4.1–4.3 and 5.

| id | claim | strength | support |
|---|---|---|---|
| C1 | The likelihood-ratio threshold set maximises P_SN − β·P_N (expected-value optimum) | proof | Part I Theorem 1, pp. 16–18 |
| C2 | A likelihood-ratio set with false-alarm k maximises detection among criteria with false-alarm ≤ k | proof | Theorem 5, pp. 20–22 |
| C3 | The two optimum types coincide: every A₂(k) is an A₁(β_k), and every k in (0, 1) is attained | proof | Theorems 6–7 and Lemma 4 |
| C4 | Optimum criteria are unique up to probability zero when f_N is analytic | proof, with an added hypothesis (Lemma 3 or 3′) | Theorems 3–4, App. B; Lemma 3′'s proof is "omitted" (p. 39) |
| C5 | The posterior P_x(SN) is a monotone function of ℓ, so the likelihood-ratio receiver also serves the Woodward–Davies approach | derivation | Eqs. 2.3–2.10 |
| C6 | The optimal ROC's slope equals the threshold β, and F_SN is determined by F_N | proof | Theorem 8, Eqs. 2.51–2.52 |
| C7 | E_N[ℓ] = 1, and the difference of the means of ℓ equals its variance under noise | proof (corollary) | Eq. 2.53, p. 28 |
| C8 | For a signal known exactly in white Gaussian noise, ln ℓ is normal with equal variances 2E/N₀ and means 2E/N₀ apart, so d = 2E/N₀ | derivation | Part II Eqs. 4.1–4.8, pp. 9–11 |
| C9 | The optimal receiver for a known signal is a correlator or matched filter h(t) = s(T − t) | derivation | Eqs. 4.1b, 4.10, 5.3 |
| C10 | Not knowing carrier phase lowers the ROC at fixed 2E/N₀ | computation and figures | §4.3, Figs. 4.5 and 5.2 |
| C11 | Any ROC is well approximated by the equal-variance normal family with d = ln(1 + σ_N²) | heuristic ("It seemed reasonable"), exact only in the log-normal case | §5.1.3, p. 59 |
| C12 | For one-of-M orthogonal signals, the energy needed at fixed d grows as ln M | approximate derivation (large 2E/N₀) plus the C11 heuristic | Eq. 5.2, p. 62 |
| C13 | Optimum performance bounds what any receiver can do | informal argument | p. 71 |

## Method

The method is measure-theoretic and Neyman–Pearson in style. Part I compares a candidate criterion with any rival over their set differences (Theorems 1 and 5) and uses a sup/inf argument over nested level sets for attainability (Theorem 6, with Lemma 4 splitting an atom of the ℓ-distribution). The analyticity lemmas use Lindelöf covering and the implicit-function theorem (Lemma 2), and differentiation under the integral (Lemmas 3 and 3′). Part II writes each signal ensemble's likelihood ratio as the P_S-average of the known-signal ratio (Eq. 3.9). It finds its distribution under noise directly and gets the signal-plus-noise distribution from Theorem 8 (dF_SN = β dF_N) rather than computing it separately.

## Concepts

- **Criterion A.** The set of receiver inputs for which the operator says "signal present" (Part I §1.2).
- **Optimum criterion of the first type, A₁(β).** Maximises P_SN(A) − β·P_N(A). This is the value-weighted (Bayes) optimum.
- **Optimum criterion of the second type, A₂(k).** Maximises P_SN(A) subject to P_N(A) ≤ k. This is the Neyman–Pearson optimum.
- **Likelihood ratio ℓ(x) = f_SN(x)/f_N(x).** "a measure of how likely that receiver input is to occur when there is signal plus noise as compared with when there is noise alone" (p. 5).
- **Receiver operating characteristic.** P_SN(A) plotted against P_N(A). "The reliability of any receiver in any given situation can be summarized in one graph" (p. 8).
- **Operating level β.** The likelihood-ratio threshold, equal to the ROC slope.
- **Detection index d.** The squared difference of the means of ln ℓ divided by its variance, when ln ℓ is normal with equal variances (Part II p. 11, p. 59). It equals 2E/N₀ for the signal known exactly, and is the square of the later d′.
- **k-equivalence.** Two signal-plus-noise distributions (with the same noise) whose likelihood ratios order inputs identically up to a null set. They share every optimum criterion, which gives uniformly best tests (App. C).
- **Ideal receiver.** One that computes ℓ, or a monotone function of it. The report does not use the phrase "ideal observer".

## Connections

- **Neyman and Pearson (1933), in this batch.** Cited as ref. 13 and in Appendix C for "uniformly best tests". Theorem 5 is the Neyman–Pearson lemma restated for receivers, and Theorems 6–7 add the Bayes-form equivalence. As far as the degraded scan shows, Theorems 1 and 5 carry no in-text attribution to Neyman–Pearson. Cramér's *Mathematical Methods of Statistics* ([LIT-311](../literature.d/LIT-311.md), Deferred, unreachable) is cited throughout as ref. 14 for measure theory (Part I pp. 14, 19, 36) and for independence, sums of normals and the chi-square distribution (Part II e.g. pp. 5, 10, 23). It is a background reference, not a source of the Cramér–Rao bound, which the report never uses.
- **Tanner and Swets (1954), in this batch.** This report is the engineering theory that the psychophysical "decision-making theory of visual detection" transfers to human observers. Whether Tanner and Swets use d′ = √(2E/N₀), i.e. √d in this report's notation, is for that reading to confirm.
- **Green and Swets (1966) and a modern SDT tutorial, in this batch.** These are the later consolidations. This report already has the likelihood-ratio rule, the bias/criterion as the threshold β (and its expression through priors and payoffs, Eq. 1.6), the ROC and its slope property, and the equal-variance Gaussian index. It has no yes/no vs. 2AFC comparison and no human observer.
- **Van Trees 1968 ([LIT-351](../literature.d/LIT-351.md), Deferred).** Van Trees's Part I is the textbook consolidation of exactly this material (likelihood-ratio tests, ROC, d, the Gaussian known-signal case) together with estimation theory and the Cramér–Rao bound, which this report lacks.
- **Rao 1945 ([LIT-349](../literature.d/LIT-349.md)) and Cramér 1946 ([LIT-311](../literature.d/LIT-311.md)), both Deferred.** No overlap: the report does no estimation.
- **[LIT-044](../literature.d/LIT-044.md) (Stigler, Active).** Background on the Neyman–Fisher line of likelihood-based inference. It has no direct link to this report.

## Bearing on the record

- **(a) SDT as a topic.** The report can be cited first-hand for:
  - the likelihood-ratio decision rule and its optimality under both the Bayes/payoff and Neyman–Pearson criteria (Part I Theorems 1–7);
  - the criterion/bias as a threshold on ℓ set by priors and payoffs (Eq. 1.6);
  - the ROC as the complete description of a detector, and the slope-equals-β property (§1.6, Theorem 8);
  - the equal-variance Gaussian model, with index d = 2E/N₀ = (ΔM)²/σ² (Part II §4.2, Fig. 4.1);
  - the matched-filter/correlator ideal receiver (§5.2).
  It **cannot** be cited for: the term or symbol d′ (it has d = d′²); "ideal observer"; the criterion measures c or β as behavioural statistics; the yes/no vs. 2AFC relation; or any human-observer claim. Those belong to Tanner and Swets, Green and Swets, and the tutorial.
- **(b) Map row 14.** It can stand in for Van Trees for the *detection half*, the Gaussian equal-variance detection model, provided the Q-function form is attributed as a derivation from the report and not as a quotation. From Eqs. 4.3–4.4 and 4.8: with threshold ln β = ln ℓ₀, false alarm = Q((E/N₀ + ln β)/√(2E/N₀)) and miss = Q((E/N₀ − ln β)/√(2E/N₀)). At the equal-prior, equal-cost threshold β = 1, both equal Q(√(E/2N₀)) = Q(√d/2) = Q(d′/2). This is the row's `P(flip) = Q(γ/σ)` shape, with γ the half-separation E/N₀ of the log-likelihood means and σ = √(2E/N₀) their common standard deviation. This derivation is mine; the report states only the normal integrals and the ROC curves. It **cannot** stand in for the Cramér–Rao half of row 14 ([LIT-349](../literature.d/LIT-349.md), [LIT-311](../literature.d/LIT-311.md)), since it has no estimation theory. Van Trees remains the single source that holds both; this report plus a CRLB source splits the row. Recommendation: cite this report for the detection model and ROC, and keep Rao/Cramér (still Deferred) for the bound.
- **No THEORY in the record bears on this.** It carries no instruction for ML practice. The one ML-adjacent thread is that ROC analysis and threshold choice by payoff (Eq. 1.6) are the origin of ROC/AUC evaluation. The anthology has no LIT for this work, and the report is a historical source rather than a practice source, so no dual holding is proposed.
- **For filing.** `information-theory` first: Trans. IRE PGIT, radar and communication detection, and the Woodward–Davies information framing. `probabilistic-modeling` covers likelihood-ratio tests and Gaussian noise models. `mathematics` covers the measure-theoretic proofs in Part I and App. B–C. `cognition` is justified only as SDT's topic home, since browsers of signal detection theory would expect its founding source; the report itself has no human observer, so drop `cognition` if the record reads tags strictly as the document's own subject.

## Limitations

- **Scan quality.** Several Part II pages, and the Part I errata sheet, are partly illegible. Part II §4.4–4.9 and Appendices D–F were skimmed, not verified equation by equation. Hence `note_status: Skimmed`.
- **Scope.** The report covers only detection of presence or absence (Part II p. 70: "the problem of obtaining information from signals or about signals, except as to whether or not they are present, is not discussed"). Gaussian noise is assumed throughout Part II.
- **Heuristics.** The ROC-fitting rule d = ln(1 + σ_N²) (§5.1.3) and the ln M energy law (Eq. 5.2) are heuristic outside the log-normal case. The report says so ("It seemed reasonable").
- **Uniqueness.** Uniqueness needs analytic f_N plus Lemma 3 or 3′. The proof of Lemma 3′ is omitted, so Theorem 3 is fully proved only under the bounded-energy condition (Lemma 3).
- **Priority.** The report credits Neyman–Pearson only in the bibliography and in App. C (as far as the scan shows). Its bibliography notes that Lawson–Uhlenbeck's minimum-error criterion is "a special case of an optimum criterion of the first type", and that Middleton's 1953 treatment covers both optimum types "not in their full generality".
- **Version.** The 1954 journal version (with Fox) was not read. Any changes between the report and the paper are unverified.

## Open questions

- Does the 1954 IRE version change the notation (d vs. d′), the theorem numbering, or the attribution to Neyman–Pearson? Reading the journal version would settle this.
- Is the planned "introduction to the theory of signal detectability using as little mathematics as possible", with sequential analysis (announced on the errata sheet, report number illegible), the source that Tanner and Swets actually used?
- For map row 14: is the row's σ² = σ²_ε/B + σ²_q(b) a noise variance on the same decision statistic, so that Q(γ/σ) maps onto this report's Q(√d/2) with γ = half the mean separation? This depends on the owner's §5 model, not on the report.

## Corrections to the seeded skim

- none (there was no seed or dossier)
- **Authors.** The batch brief gives "Peterson, Birdsall & Fox 1954". The 1953 report is by W. W. Peterson and T. G. Birdsall only. W. C. Fox appears in Part I's acknowledgements, for the proofs of Lemmas 1 and 2 in Appendix B (with a "Mr. Paul Both" or "Roth"; the scan is unclear), for the proof of Lemma 4, and for "careful reading of the text". Crossref lists Fox as third author of the 1954 journal version (DOI 10.1109/TIT.1954.1057460, Trans. IRE PGIT 4(4):171–212, September 1954).
- **Structure.** "Technical Report No. 13, 1953" is two documents, Part I (June 1953) and Part II (July 1953), "issued separately", with two DTIC accession numbers. Part I carries an errata sheet. The errata sheet announces a planned non-mathematical introduction covering sequential analysis as a further EDG technical report (its number is illegible in the scan).
- **Terminology.** The report's index is **d**, not d′, defined as "the square of the difference of the means, divided by the variance" of ln ℓ (Part II p. 11; Fig. 4.1 caption "(M_SN − M_N)² = d σ_N²"). For the signal known exactly, d = 2E/N₀. The later psychophysical d′ is the square root of this quantity. The report never writes d′. It speaks of the "operator" and the "ideal receiver", never of an "ideal observer" (no occurrence of "observer" in either part's text).
- **Scope for map row 14.** The report contains no estimation theory and no Cramér–Rao bound. It never writes a Q-function or an explicit P(error) formula; error probabilities appear as normal-integral distribution functions (Eqs. 4.4, 4.8) and as ROC curves. So `P(error) = Q(√d/2)` is a one-line consequence of its Eqs. 4.3–4.8, but it is not stated in the report (see Bearing on the record).
