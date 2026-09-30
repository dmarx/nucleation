---
status: Read
paper: LIT-tmpcixzf
title: 'Calculation of signal detection theory measures'
version: 1
history:
- version: 1
  date: '2026-09-30'
  note: >-
    Read in full (Full text, 13 pp. (137–149), of the publisher's PDF on
    SpringerLink (link.springer.com/content/pdf/10.3758/BF03207704.pdf).
    OpenAlex and Semantic Scholar both mark this copy as bronze open access,
    so it is the publisher's own free copy, not a third-party upload. Read
    in full: overview, formulae (eqs. 1–15), methods of calculation, Tables
    1–6, the computational example, conclusion and reference list. The text
    layer was extracted with PyMuPDF, and pp. 142–143 were rendered to
    images to check the equations. Every number in Figure 1's worked
    example, and rows 2 and 5 of Table 6, were recomputed by hand and agree.
    This is the batch's first-choice tutorial. The Macquarie University
    repository record carries no file; the publisher copy is the legitimate
    open one. `published:` is the first day of the issue month Crossref
    gives (1999-03); the article prints only "1999, 31(1)". Manuscript
    received 15 August 1997, revision accepted 9 February 1998. No existing
    entry in the Anthology of the SOTA (grep of its literature.d for the
    DOI, "Stanislaw", "signal detection": no hits).). The first NOTE on this
    paper, which was seeded from its abstract alone.
date: '2026-09-30'
summary: >-
  A practical tutorial that gives closed-form SDT measures computed from
  the hit rate H and false-alarm rate F. They are d′ = Φ⁻¹(H) − Φ⁻¹(F); β
  = exp{[Φ⁻¹(F)² − Φ⁻¹(H)²]/2}; c = −[Φ⁻¹(H) + Φ⁻¹(F)]/2; the
  nonparametric A′ and Grier's B″ (single-formula versions, eqs. 3 and 9);
  A_z = Φ(intercept/√(1+slope²)) from the z-ROC, whose slope is
  σ_noise/σ_signal; and A_d′ = Φ(d′/√2), which equals 2AFC proportion
  correct under the d′ assumptions. It also gives one-line commands for
  seven software packages. Its worked rating example (50 signal and 25
  noise trials, noise SD larger than signal SD) shows d′ ranging from 0.84
  to 1.86 across criteria. The authors conclude that d′ should not be used
  without rating-task evidence of equal variance.
---

# NOTE-tmpfr7tp: Calculation of signal detection theory measures

## Contribution

The paper puts every standard SDT performance measure for yes/no, rating and forced-choice tasks into closed form as a function of the hit and false-alarm rates. It states the assumptions each measure needs, and shows how to compute each with general-purpose software (Tables 1–4). The declared motive is under-use: fewer than half of the studies to which SDT applies use it (Stanislaw & Todorov 1992, an abstract), because textbooks omit the computations (p. 137). It adds a double-regression (averaged OLS slopes) approximation for fitting z-ROCs without a dedicated program, and a worked example.

## Key insight

"The major contribution of SDT to psychology is the separation of response bias and sensitivity" (p. 139). Hit rate, false-alarm rate, H − F and proportion correct in yes/no tasks all confound the two (p. 139). Every measure in the paper is a way of pulling them apart, and each is valid only under stated assumptions about the decision variable. For d′ those are normality and equal variance, which "cannot actually be tested in yes/no tasks" (p. 140).

## Assumptions

- **Decision variable plus criterion.** Each trial yields a value of a decision variable. The subject says yes if it exceeds a criterion (p. 138). β instead assumes responses are based on a likelihood ratio (p. 140). c assumes they are based directly on the decision variable (p. 140).
- **The d′ assumptions.** Signal and noise distributions are (1) normal and (2) of equal SD. Under these, d′ is unaffected by response bias. If either fails, "d′ will vary with response bias" (p. 140). Equal SD "is particularly suspect" (p. 140, citing Swets 1986).
- **A_z.** Assumes normality but not equal SD (p. 141).
- **mAFC.** Proportion correct measures sensitivity free of bias only "if subjects do not favor any of the m alternatives a priori" (p. 141).

## Key results

With H the hit rate, F the false-alarm rate and Φ the standard normal CDF:

- **d′ (eq. 1):** d′ = Φ⁻¹(H) − Φ⁻¹(F). It is 0 at chance and +∞ for perfect performance, and can be negative through sampling error or response confusion (pp. 139–140).
- **A′ (eqs. 2–3):** A′ = .5 + sign(H − F)·[(H − F)² + |H − F|]/[4 max(H, F) − 4HF]. Earlier publications give only the H ≥ F branch (Grier 1971), and there is a typographical error in Cradit et al. 1994 (p. 142).
- **β (eqs. 4–6):** β is the ratio of the signal to the noise ordinate at the criterion: β = exp{[Φ⁻¹(F)² − Φ⁻¹(H)²]/2}, so ln β = [Φ⁻¹(F)² − Φ⁻¹(H)²]/2. β = 1 means no bias. β < 1 (ln β < 0) means a bias toward yes (p. 140).
- **c (eq. 7):** c = −[Φ⁻¹(H) + Φ⁻¹(F)]/2. It is the criterion's distance, in SD units, from the neutral point where the distributions cross (β = 1). Negative values mean a bias toward yes. Some authors omit the minus sign (p. 142). c is recommended over β because c "is unaffected by changes in d′, whereas β is not" (p. 140, citing Ingham 1970, Macmillan 1993, McNicol 1972).
- **B″ (eqs. 8–9):** B″ = sign(H − F)·[H(1 − H) − F(1 − F)]/[H(1 − H) + F(1 − F)]. It ranges from −1 to 1. Grier's original formula gives the wrong sign when H < F. Some authors (e.g. Macmillan & Creelman 1996) have confused Grier's B″ with Hodos's measure (p. 140).
- **A_z (eq. 10):** A_z = Φ[intercept/√(1 + slope²)] from the best-fitting line in z-space. The slope equals σ_noise/σ_signal, so testing slope = 1 (better, log slope = 0) tests equal variance (p. 143). A_z "(when it can be calculated) is the preferred measure of the ROC area and, thus, of sensitivity" (p. 141).
- **ROC area = 2AFC proportion correct.** The area under the ROC is "the proportion of times subjects would correctly identify the signal, if signal and noise stimuli were presented simultaneously" (p. 141, citing Green & Moses 1966 and Green & Swets 1966 pp. 45–49).
- **A_d′ (eq. 11):** A_d′ = Φ(d′/√2). If the d′ assumptions hold, it equals 2AFC proportion correct and the ROC area. Under normality, A_z from a rating task should equal 2AFC proportion correct, which equals A_d′ when variances are equal. "no such prediction can be made for A′" (p. 143).
- **Extreme rates (pp. 143–144).** A rate of 0 or 1 makes d′ infinite. Four remedies are reviewed: nonparametric measures; pooling subjects; the loglinear correction (add 0.5 to counts and 1 to trial totals, which "seems to work reasonably well", Hautus 1995); and replacing 0 by 0.5/n and 1 by (n − 0.5)/n. The last is biased (Miller 1996) and may be worse than loglinear, but is the most common, and the authors adopt it.
- **Fitting z-ROCs (pp. 146–147).** OLS on (z_F, z_H) is biased because both rates carry error. The authors recommend ROCFIT or RSCORE4, or else their double regression: Slope* = 0.5(Slope₁ + 1/Slope₂) (eq. 14) and Intercept* = z̄_H − Slope*·z̄_F (eq. 15).
- **Figure 1 example (pp. 138–140).** Noise N(0, 1), signal N(2, 1), criterion 0.5. This gives F = .3085, H = .9332, d′ = 2, β = .1295/.3521 = .37, ln β = −1.00, c = −0.50, A′ = .89, A_d′ = .92, B″ = −0.55. The quantities recomputed here (F, H, β, ln β, c, A_d′) agree.
- **Worked rating example (Tables 5–6, pp. 147–148).** Five criteria give d′ = 1.86, 1.56, 0.96, 0.84 and 1.70. ROCFIT gives slope 1.28, intercept 1.52 and A_z = .82. Double regression gives Slope₁ = 0.99, Slope₂ = 0.81, Slope* = 1.11, Intercept* = 1.44 and A_z = .83. OLS alone (slope ≈ 1) wrongly suggests equal variance even though r = .90 (p. 148). The conclusion: "researchers should not use d′ without first obtaining evidence (preferably from a rating task) that its underlying assumptions are valid" (p. 148). Those mainly interested in sensitivity "may wish to avoid yes/no tasks altogether" (p. 148).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | d′, β, ln β, c, A′, B″, A_z and A_d′ are given by eqs. 1–11 | standard derivations, stated with citations (Macmillan 1993; Snodgrass & Corwin 1988; Swets & Pickett 1982); not re-derived | pp. 142–143; Fig. 1 numbers check |
| C2 | Under normality and equal variance, d′ is independent of response bias; otherwise it varies with the criterion | stated; illustrated by the worked example | p. 140; Table 6 |
| C3 | ROC area equals 2AFC proportion correct, and A_d′ = Φ(d′/√2) estimates it under the d′ assumptions | cited (Green & Swets 1966 pp. 45–49; Macmillan 1993) | pp. 141, 143 |
| C4 | c is independent of d′ and β is not | cited | p. 140 |
| C5 | z-ROC slope = σ_noise/σ_signal, so rating tasks test equal variance | stated | p. 143 |
| C6 | OLS on z-scores gives biased z-ROC slopes; the averaged double regression is a reasonable fallback | argument plus one worked example (A_z .83 vs ROCFIT .82) | pp. 146–148 |
| C7 | The loglinear correction works "reasonably well"; the 0.5/n replacement is biased | cited (Hautus 1995; Miller 1996) | pp. 143–144 |
| C8 | Fewer than half of SDT-applicable studies use SDT | cited to the authors' own 1992 conference abstract | p. 137 |
| C9 | A_z is the preferred sensitivity measure | cited (Swets 1988a; Swets & Pickett 1982) | p. 141 |

## Method

Tutorial and review. Formulae are collected from the literature, rewritten in single-formula or numerically stable forms (eqs. 3, 5, 9), and illustrated with one analytic example (Fig. 1) and one hypothetical rating dataset (Tables 5–6). Software commands are listed for Excel, Mathematica, Minitab, Quattro Pro, SAS, SPSS and SYSTAT (Tables 1–4).

## Concepts

- **Hit rate H, false-alarm rate F.** Together they "fully describe performance on a yes/no task" (p. 138).
- **Sensitivity vs response bias.** The overlap of the signal and noise distributions vs the location of the criterion (p. 139).
- **d′.** The distance between the means in SD units (p. 139).
- **β.** The likelihood-ratio criterion: the ratio of the signal to the noise density at the criterion (p. 140).
- **c.** The criterion's distance from the neutral point (β = 1) in SD units (p. 140).
- **A′, B″.** "Nonparametric" sensitivity and bias indices, controversial (Macmillan & Creelman 1996).
- **ROC, z-ROC, A_z.** The hit rate against the false-alarm rate over all criteria, plotted in probability or z coordinates, and the area under it assuming normality (pp. 140–143).
- **mAFC.** One signal and m − 1 noise stimuli per trial, with no criterion. Chance is 1/m (p. 141).

## Connections

- **Van Trees, Detection, Estimation, and Modulation Theory I ([LIT-351](../literature.d/LIT-351.md), Deferred).** This paper can be cited for the equal-variance Gaussian detection model's error rates in closed form: F = 1 − Φ(criterion/σ) = Q(criterion/σ), and 2AFC error 1 − Φ(d′/√2) = Q(d′/√2). The yes/no minimum-error form Q(d′/2) is not printed. It follows from the paper's neutral point (β = 1 midway between the means, p. 140) with equal priors, but the paper never discusses priors or error minimisation. It has nothing on estimation bounds ([LIT-349](../literature.d/LIT-349.md), [LIT-311](../literature.d/LIT-311.md)).
- **Within this batch.** Tanner and Swets (1954) introduced d′, β-as-optimal-criterion and the yes-no/forced-choice equivalence that this paper turns into formulas. Green and Swets (1966) is the book this paper defers to, cited for the ROC-area = 2AFC result at pp. 45–49. Peterson, Birdsall and Fox (1954) and Neyman and Pearson (1933) are the likelihood-ratio source this paper does not cite. It motivates β by likelihood ratio without derivation.
- **Ivy & Mroczko-Wąsowicz, "Framing Effects in Object Perception" ([LIT-099](../literature.d/LIT-099.md)).** The swear-word threshold example (p. 139) is the textbook case of a supposed perceptual effect that SDT re-reads as possibly a criterion shift. It is the tool [LIT-099](../literature.d/LIT-099.md)'s claims about top-down frames would need in order to separate sensitivity from bias. The link is thematic.
- **Anthology of the SOTA.** No entry covers SDT measures or ROC analysis, although ROC/AUC is everyday ML evaluation practice.

## Bearing on the record

- **SDT as a topic.** This is the best compact, first-hand source in the batch for: the formula for d′; β as a likelihood ratio and its computation; c and why it is preferred; the ROC and z-ROC; A_z; the ROC area/2AFC identity; and the extreme-rate corrections. It is a tutorial. For the origin of the ideas, cite Tanner and Swets (1954) or Green and Swets (1966) as appropriate.
- **Map row 14.** It is a partial stand-in for Van Trees. It is citable for Gaussian detection error rates as Q-functions of criterion/σ and for Φ(d′/√2). It is not citable for Q(d′/2) as printed, or for the CRLB. A reader wanting "P(error) = Q(d′/2)" verbatim will still need an engineering text.
- **ML practice.** The paper is psychology-facing, but its content (ROC area as the probability of correctly ranking a signal–noise pair; the bias of OLS on z-ROCs; loglinear smoothing of 0/1 rates) is exactly what binary-classifier evaluation uses. If the anthology ever files an ROC/AUC practice, this is a reasonable secondary source; the anthology would name it in prose. Nothing here is specific to ML.
- **For filing.** `cognition` first (the tutorial is about human discrimination tasks). `probabilistic-modeling` for the Gaussian measurement model and ROC fitting.

## Limitations

- The paper derives nothing. Formulae are stated with citations, and correctness rests on the cited sources. (The worked numbers checked here are right.)
- There is no treatment of priors, payoffs, the optimal β, or minimum-error decision rules, although β is defined as a likelihood ratio.
- For mAFC with m > 2 it points to tables and algorithms rather than giving the d′ integral.
- There is no sampling theory for the measures (standard errors, confidence intervals) beyond citations (Miller 1996, Hautus 1995).
- Software specifics are 1999-dated. The FTP URLs for RSCORE4 and ROCFIT are almost certainly dead (not checked), and some package commands have changed.
- The motivating under-use statistic (C8) rests on the authors' own conference abstract.

## Open questions

- How good is the double-regression z-ROC fit relative to maximum-likelihood ROCFIT in general? The paper shows one example (.83 vs .82).
- Is c truly independent of d′ when variances are unequal? The claim (C4) is cited under equal variance only.

## Corrections to the seeded skim

- none (there was no seed or dossier)
- The batch brief lists "yes/no vs 2AFC" among the paper's contents. It covers yes/no, rating and general mAFC tasks. For mAFC it gives only proportion correct as the sensitivity measure. It gives no formula converting mAFC proportion correct to d′ for m > 2 and refers to published tables and algorithms instead (p. 144). The yes/no–2AFC link is made through A_d′ = Φ(d′/√2) (eq. 11), not through a 2AFC d′ formula.
- For map row 14: the paper does **not** print P(error) = Q(d′/2) or any minimum-error formula, and it has nothing on estimation or the Cramér–Rao bound. It does supply the ingredients: the neutral point where β = 1 lies midway between the means (Fig. 1: 1 SD above the noise mean when d′ = 2, p. 140), and the Gaussian tail areas at any criterion.
- Eq. 4 (p. 142), the ratio-of-ordinates form of β, prints its normal-density normaliser as "√2p". This is evidently √(2π); the normalisers cancel, and eq. 5 is the form the authors recommend.
