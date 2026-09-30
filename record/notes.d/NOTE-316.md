---
number: 316
status: Read
formerly:
- NOTE-tmpp9572
paper: LIT-368
title: 'A decision-making theory of visual detection'
version: 1
history:
- version: 1
  date: '2026-09-30'
  note: >-
    Read in full (Full text, Psychological Review 61(6):401–409, from the
    Internet Archive's open microfilm scan of the whole November 1954 issue
    (item sim_psychological-review_1954-11_61_6; not a lending item). All 9
    pages read: text, all 16 figures and captions, equations [1]–[3],
    conclusions (a)–(f), both references and footnote 1. The OCR text layer
    was read in full, and pp. 404–406 and 408 were rendered to images to
    check the equations, the figures and the one garbled significance
    statement. Nothing was skipped. Copyright: The Online Books Page's
    serial record for Psychological Review says the first copyright-renewed
    issue is January 1963 (v. 70 no. 1) and that it knows of no renewed
    contributions, so this 1954 issue is in the US public domain. The paper
    prints "Vol. 61, No. 6, 1954" but no month; `published:` uses 1 November
    1954 because the Internet Archive dates issue 6 to 1954-11. The paper
    was received 29 October 1953. No existing entry in the Anthology of the
    SOTA (grep of its literature.d for the DOI, "Tanner", "signal detection"
    and "receiver operating": no hits). A DTIC copy of the related 1955
    technical report "The evidence for a decision-making theory of visual
    detection" (AD0064143) was tried first, but DTIC returned a block page
    and then a maintenance page. That report is a different, longer work and
    was not read.). The first NOTE on this paper, which was seeded from its
    abstract alone.
date: '2026-09-30'
summary: >-
  Tanner and Swets model visual detection as testing a statistical
  hypothesis. The observer compares one sample of neural activity with a
  cutoff, and signal+noise and noise are Gaussian with equal variance,
  separated by d′ (the mean difference in noise-SD units, defined as the
  square root of Peterson and Birdsall's d). The cutoff moves along a
  curve of P_SN(A) against P_N(A) (the curve now called the ROC; for d′ =
  1 it passes through (.16, .50), (.50, .84) and (.84, .98)). The optimal
  operating point is where the slope equals β =
  [(1−P(SN))/P(SN)]·[(V_N·CA+K_N·A)/(V_SN·A+K_SN·CA)]. The 4AFC prediction
  is P(C)=∫F(x)³g(x)dx. With three paid observers, d′ estimated from
  yes-no data predicted 4AFC accuracy. The "false alarms are guesses"
  (high-threshold) hypothesis is rejected: false-alarm rate correlated
  with chance-corrected thresholds (ρ = .30, .71, .67; combined p ≪ .001),
  and all 12 fitted yes-no scatter lines miss the point (1, 1).
---

# NOTE-316: A decision-making theory of visual detection

## Contribution

The paper takes the engineering theory of signal detectability (Peterson and Birdsall's 1953 University of Michigan Electronic Defense Group report, its ref. 2) and makes it a theory of the human observer. It replaces the sensory threshold with a decision about a noisy continuous quantity. It introduces d′ as the observer's sensitivity, separate from the cutoff. It predicts that yes-no and forced-choice data must yield the same d′, and it shows three observers roughly meeting that prediction while their false-alarm rates moved with priors and cash payoffs. That movement is what the classical chance correction cannot accommodate.

## Key insight

A false alarm is not a guess made when "seeing" fails. It is the same decision rule, applied to noise, that produces hits on signal trials. Hits and false alarms therefore trade off along one curve fixed by d′. Where an observer sits on that curve (the criterion) is set by priors and payoffs, not by the sensory system. So "threshold" confounds two things, sensitivity and criterion, that the theory measures separately.

## Assumptions

- **Decision on one scalar.** For a signal at a known place and time, the observer uses only the neural activity for that location and time, reduced to a single measure x(M) (pp. 402–403).
- **Monotone transduction.** Neural activity is a monotonically increasing, not necessarily linear, function of light intensity (p. 402).
- **Gaussian, equal variance.** N and S+N are Gaussian with equal variance "for mathematical convenience". The authors say "Experimental results suggest that equal variance is not a true assumption, but that the deviations are not great enough to justify the inconvenience" (p. 403).
- **Fixed, stable cutoff.** A measure above the cutoff is "in the criterion" (a yes). Two justifications are given: such behaviour "is statistically optimum", and random instability of the cutoff is mathematically equivalent to extra variance (p. 403).
- **Signal known exactly.** The analysis corresponds to Peterson and Birdsall's "case of the signal known exactly" (p. 403). The variance of N depends on signal parameters because the observer knows a priori which signal it would be (p. 403).
- **Same d′ across tasks.** Yes-no and forced-choice decisions draw on the same display, so "the values of d′ for any given light intensity must be the same" (p. 405).

## Key results

- **The conventional account (p. 401).** Chance correction p = (p′ − c)/(1 − c) (eq. [1]; c is the curve's intercept at ΔI = 0) is valid only if a false alarm is a guess "independent of any sensory activity". That requires a mechanism that "becomes incapable of discriminating between quantities of neural activity when seeing does not occur".
- **d′ (p. 403).** d′ is "the difference between the means of N and S + N in terms of the standard deviation of N", and "the square root of Peterson and Birdsall's d". The paper does not define d.
- **The operating curve (Fig. 4, pp. 403–404).** For d′ = 1, with the cutoff at −∞, −1, 0, +1 and +∞ noise SDs: (P_N(A), P_SN(A)) = (1, 1), (.84, .98), (.5, .84), (.16, .5) and (0, 0). "The curve represents the best that can be done with the information available, and the mirror image is the curve of worst possible behaviors." Fig. 5 gives the family of such curves with d′ as the parameter; the curve labels are only partly legible in the scan, and the highest reads d′ = 4. For d′ > 4, "detection is very good" (p. 404).
- **Optimal criterion, eq. [2] (p. 404).** The maximum behaviour is the point on the curve where the slope is β = [(1 − P(SN))/P(SN)] · [(V_N·CA + K_N·A)/(V_SN·A + K_SN·CA)]. These are the prior of signal and the values and costs of correct rejection, false alarm, correct detection and miss. As P(SN) or V_SN·A rises, or K_N·A falls, β falls.
- **Guessing theory prediction (Fig. 6, p. 404).** Under the chance correction the operating curves would be straight lines to (1, 1). The chance correction would map them to horizontal lines.
- **Psychometric functions (Fig. 7, p. 405).** Under this theory, curves for different criteria differ by a horizontal shift, not a vertical one, so the chance correction cannot superimpose them.
- **Forced choice, eq. [3] (p. 405).** In m-interval forced choice, P(C) is the probability that the S+N sample exceeds the greatest of m − 1 noise samples. For m = 4, P(C) = ∫_{−∞}^{+∞} F(x)³ g(x) dx, where F is the noise CDF and g the S+N density (Fig. 8). The solution is credited to help from Peterson and Birdsall; it is "not contained in their study".
- **Experiment (pp. 405–406).** The target was a 30′ disc, 1/100 s, on a 10 ft-L background. Temporal 4AFC used five intensities with 100 test observations per point. Yes-no used the four highest intensities, reduced by a 0.1 filter. There were 4 practice sessions and 12 test sessions. In the test sessions P(SN) was .8 or .4, observers were told the values and costs, and they were paid in cash (up to $2 extra per session). Obtained P_N(A) varied "approximately" with the payoff information.
- **d′ agreement (pp. 406–408).** Yes-no scatter diagrams give d′ = .7 (Fig. 9) and 1.3 (Fig. 10), each from 560 observations. Log d′ against log ΔI (Figs. 11–13) puts yes-no and 4AFC estimates on roughly one line per observer, except for the top and bottom points. The top point is attributed to inadequate data; the low point "is unexplained". Figs. 14–16 predict 4AFC accuracy from yes-no d′.
- **Against the guessing theory (p. 408).** Rank-order correlations between P_N(A) and chance-corrected thresholds are .30, .71 and .67 (combined p ≪ .001). The guessing theory predicts independence. All 12 straight-line fits to the scatter diagrams cross P_SN(A) = 1 at P_N(A) between 0 and 1, in the order the theory predicts, rather than through (1, 1).
- **Phenomenal seeing (pp. 408–409).** In two further sessions with yes/no/doubtful responses, observers told to be sure of being correct still had P_N(A) that tracked P(SN). They reported their "yes" responses as "phenomenal" seeing. The authors read this as "phenomenal seeing develops through experience", with psychological "set" a function of β.
- **Conclusions (p. 409).** (a) The threshold concept "needs re-evaluation". (b) The hypothesis that false alarms are guesses is "rejected on the basis of statistical tests". (c) Change in neural activity is a power function of change in light intensity. (d) The detection model applies to vision. (e) The criterion of seeing has psychological as well as physiological determinants, and observers "tended to use optimum criteria". (f) The data support the forced-choice/yes-no link.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Yes-no detection is a statistical hypothesis test on one noisy measure, with a cutoff | modelling assumption | pp. 402–403 |
| C2 | For equal-variance Gaussians the achievable (P_N, P_SN) pairs form one curve per d′; worked values for d′ = 1 | derivation (Gaussian tails) | p. 404, Figs. 4–5 |
| C3 | The optimal cutoff is where the curve's slope equals β, set by prior and payoffs (eq. [2]) | stated, credited to Peterson and Birdsall's decision theory, not derived here | p. 404 |
| C4 | 4AFC accuracy is P(C)=∫F³g, a function of d′ alone | derivation | p. 405 |
| C5 | d′ from yes-no data predicts 4AFC accuracy (internal consistency) | experiment: 3 observers, visual inspection of fits, no fit statistic | pp. 406–408, Figs. 11–16 |
| C6 | False alarms are not guesses: they correlate with corrected thresholds, and the scatter lines miss (1, 1) | experiment plus significance test. The test statistic, n and combining method are not reported. The ρ = .30 is called "highly significant" without an n | p. 408 |
| C7 | Observers "tended to use optimum criteria" | assertion. No comparison of obtained with optimal β is reported | p. 409 |
| C8 | Neural activity is a power function of light intensity | inference from roughly linear log d′ vs log ΔI plots; slopes not reported | p. 409, Figs. 11–13 |
| C9 | Phenomenal seeing is learned and shifts with set | interview reports from two sessions | pp. 408–409 |

## Method

Theory followed by a psychophysical experiment. The model is equal-variance Gaussian signal detection with a fixed cutoff. Its predictions are derived for yes-no (operating curves) and 4AFC (order statistics). Priors and payoffs were manipulated across sessions to move observers' criteria. d′ was estimated from yes-no scatter diagrams (by eye against the theoretical curves) and from 4AFC percent correct (by inverting Fig. 8), and the two were compared.

## Concepts

- **d′.** Mean separation of S+N and N in noise-SD units, defined as √d of Peterson and Birdsall (p. 403). Its first appearance in psychology.
- **Criterion / cutoff.** The boundary above which a measure counts as "yes". Its placement sets P_N(A) and P_SN(A).
- **β.** The slope of the operating curve at the optimal point, equal to the prior-odds × payoff ratio of eq. [2] (the likelihood-ratio criterion).
- **Operating curve (later ROC).** P_SN(A) against P_N(A) as the cutoff varies (Figs. 4–5). The paper does not use the term "ROC".
- **Ideal behaviour.** "that which makes optimum use of the information available", as defined by Peterson and Birdsall (p. 403).
- **Guessing (high-threshold) hypothesis.** False alarms as sensory-independent guesses, which the chance correction presupposes (p. 401).
- **Yes-no vs forced choice.** Two tasks that share one d′ under the theory.

## Connections

- **Van Trees, Detection, Estimation, and Modulation Theory I ([LIT-351](../literature.d/LIT-351.md), Deferred).** This paper supplies the detection half of what map row 14 cites Van Trees for: the equal-variance Gaussian binary test, the cutoff in σ units, and error rates as Gaussian tails (P_N(A) = Q(k) for a cutoff k σ above the noise mean, matching the form P(flip) = Q(γ/σ)). It supplies none of the estimation half (Cramér–Rao, [LIT-349](../literature.d/LIT-349.md) and [LIT-311](../literature.d/LIT-311.md)). It states the model and the ROC but not the closed-form minimum-error rate.
- **Within this batch.** Peterson, Birdsall and Fox (1954), and the 1953 EDG Technical Report No. 13 cited here as ref. 2, are the source of the ideal-observer and likelihood-ratio mathematics this paper borrows. Neyman and Pearson (1933) is the likelihood-ratio lemma behind "statistically optimum" (p. 403). This paper does not cite it. Green and Swets (1966) is the book-length development. Stanislaw and Todorov (1999) gives the modern measures (d′ = Φ⁻¹(H) − Φ⁻¹(F), c, β) that this paper estimates graphically.
- **Ivy & Mroczko-Wąsowicz, "Framing Effects in Object Perception" ([LIT-099](../literature.d/LIT-099.md)).** That paper argues that learned "frames" change what perceivers individuate from identical input. Tanner and Swets's conclusion (e), that the criterion of seeing is learned and set-dependent, is the classical tool for asking whether such an effect is a change in sensitivity (d′) or in criterion. [LIT-099](../literature.d/LIT-099.md) does not use SDT. The link is thematic.
- **Barnett & Bossomaier, "Transfer Entropy as a Log-likelihood Ratio" ([LIT-048](../literature.d/LIT-048.md)).** It shares only the likelihood-ratio framing. There is no substantive link.
- **Anthology of the SOTA.** No entry covers signal detection theory, d′ or ROC analysis.

## Bearing on the record

- **SDT as a topic.** This is the founding citation for SDT in psychology. It is the first-hand source for: d′ (named and defined, p. 403); criterion versus sensitivity; the operating (ROC) curve for the observer; the prior-and-payoff optimal criterion β (eq. [2]); the yes-no/forced-choice equivalence; and the empirical rejection of the high-threshold "guessing" model. It is not the source for the likelihood-ratio decision rule or the ideal observer as mathematics. Those are Peterson and Birdsall's, and ultimately Neyman–Pearson's, and this paper credits them.
- **Map row 14.** It can be cited first-hand for the Gaussian equal-variance detection model and for detection error rates as Gaussian tails in noise-SD units (P_N(A) = Q(k), Fig. 4). It does not print P(error) = Q(d′/2) or the 2AFC formula Φ(d′/√2). Those follow in one line from its model, and Stanislaw and Todorov (1999) prints the second. It has nothing on the CRLB or on σ² = σ²_ε/B + σ²_q(b). As a replacement for Van Trees it covers only the detection half, and from psychophysics rather than engineering. For an engineering citation of the same model, Peterson, Birdsall and Fox is the better fit.
- **ML practice.** Nothing directly. ROC/AUC evaluation in ML descends from this line of work, but the paper says nothing about classifiers.
- **For filing.** `cognition` first (perception and decision). `probabilistic-modeling` (Gaussian hypothesis-testing model). `neuroscience` is justified by the neural-activity framing and the visual-pathway model (Fig. 2, p. 402), though no neural data are collected.

## Limitations

- The ideal-observer analysis is imported, not derived. Eq. [2] is stated without proof, and "d" is used without definition.
- The sample is small: three observers (with an inconsistent mention of four, p. 406), one target type, and four or five intensities.
- Equal variance is assumed while the authors say the data suggest it is false (p. 403). The later unequal-variance ROC literature (e.g. the zROC slope test Stanislaw and Todorov describe) grew from exactly this.
- d′ is estimated from the scatter diagrams by eye. No fitting procedure, standard errors or goodness-of-fit are reported for the internal-consistency test (C5).
- The significance claims (C6) give no n, test or combining method.
- "Observers tended to use optimum criteria" (C7) and the power-function conclusion (C8) go beyond anything tabulated.
- The phenomenal-seeing reinterpretation (pp. 408–409) rests on post-session interviews.

## Open questions

- How close were the obtained criteria to the β of eq. [2]? The paper gives the information needed to compute β but reports no comparison. The 1955 EDG report (DTIC AD0064143), which was unreachable here, may.
- Does the 4AFC agreement survive the unequal variance the authors suspect? This paper cannot tell.

## Corrections to the seeded skim

- none (there was no seed or dossier)
- The batch brief casts this as a candidate citation for map row 14's detection model. The paper supplies the equal-variance Gaussian model, d′ and the error rate at any cutoff (Fig. 4 tabulates P_N(A) = 1−Φ(k) at a cutoff k noise-SDs above the noise mean, which is exactly the tail form Q(γ/σ)). It does **not** state an error-probability formula such as P(error)=Q(d′/2). It gives no 2AFC formula (its only forced-choice case is m = 4). It has nothing on estimation, variance decomposition or the Cramér–Rao bound. It cannot stand in for Van Trees on the CRLB half of row 14.
- The paper counts its observers inconsistently. The Experimental Design section says "three Michigan sophomores" (p. 405), but Results speaks of d′s "for each of four signals for each of the four observers" (p. 406). Only three observers' data appear (Figs. 11–16).
