---
status: Read
paper: LIT-2982
title: 'Takeuchi and Sano, read for KPZ exponents and Tracy-Widom fluctuations in a turbulent liquid-crystal front'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Read in full on 2026-11-22 by a delegated reader from the arXiv author
    source (arxiv.org/e-print/1001.5121v3, LaTeX, v3 of 14 June 2010,
    "note added"), checked against the arXiv PDF of v3 (4 pp.) for page
    numbers: abstract, all body text, the five figure captions, the note
    added in proof and the bibliography. Skipped: the figures themselves,
    read through captions and text, and the APS version, which was not
    sought. Every quotation below rechecked by the filer by script
    against the downloaded text. No email address sent.
date: '2026-11-22'
summary: >-
  An experiment on growing turbulent (DSM2) clusters in nematic
  electroconvection, repeated 563 times: the front roughens with the
  1+1-dimensional KPZ exponents, and its local-radius fluctuations follow
  the GUE Tracy-Widom distribution, with GOE and Gaussian ruled out by
  the parameter-free skewness and kurtosis, and Airy₂ correlations. The
  first quantitative test of the KPZ fluctuation predictions, in a field
  where "only two experiments among dozens directly found the KPZ
  exponents". The reading is THEORY-tmpmoyol.
---
<!-- inactive-ok-file: THEORY-tmpmoyol LIT-tmpoc5u6 — new or Deferred; this reading's account and the authors' directed-percolation letter -->
<!-- inactive-ok-file: CLAIM-841 CLAIM-803 THEORY-2148 TERM-139 ARG-tmp2xbl4 CLAIM-tmpvq33w — Proposed or new; the entries the reading bears on -->

# NOTE-tmpbmox1: Takeuchi and Sano, read for KPZ exponents and Tracy-Widom fluctuations in a turbulent liquid-crystal front

## Contribution

The first quantitative experimental test of KPZ predictions beyond the
exponents. The one earlier test, on paper combustion (Miettinen et al.
2005), reached "an apparent agreement" only after the authors "had to
shift and rescale" the distribution (p. 3). The paper is also among the
few experiments to find the KPZ exponents directly. The reading is
THEORY-tmpmoyol.

## Key results

Pages are the v3 PDF's.

1. **Experiments rarely find KPZ** (p. 1): "experimentally measured
   values of the exponents are widely diverse and mostly far from the KPZ
   values for both α and β [1]. To our knowledge, only two experiments
   among dozens directly found the KPZ exponents". In numerical models,
   by contrast, the class is "universal as widely confirmed".
2. **The system** (p. 2): a 12 µm homeotropic MBBA cell at 26 V, 250 Hz,
   "sufficiently larger than the DSM1-DSM2 threshold at 20.7 V"; a laser
   pulse nucleates a DSM2 cluster, which grows as a roughening circle;
   "We repeat it 563 times".
3. **Exponents** (p. 2): α = 0.50(5) at t = 28.4 s; W(t) and C_pl(t)^½
   grow as t^β with β = 0.336(11), "in remarkable agreement with the KPZ
   growth exponent" 1/3; a Family–Vicsek collapse with KPZ exponents. "We
   therefore safely conclude that the DSM2 interfacial growth belongs to
   the (1+1)-dimensional KPZ class", which "rules out the logarithmic
   temporal scaling claimed by Escudero for the droplet geometry".
4. **Parameters** (p. 3): λ = 35.40(23) µm/s from dR/dt against t^(−2/3);
   A only roughly, about 10 µm, by direct estimates.
5. **Distribution** (p. 3): skewness and kurtosis, "which do not depend
   on the parameter estimates", converge to those of the GUE TW
   distribution, "about 0.2241 for the skewness and 0.09345 for the
   kurtosis", and the data "clearly rules out the GOE TW and Gaussian
   distributions". Assuming GUE TW, A = 9.98(7) µm, consistent with the
   direct estimate. Histograms of the rescaled radius match GUE TW
   "without any fitting, apart from a slight horizontal translation",
   with finite-time corrections near t^(−1/3).
6. **Geometry picks the ensemble** (p. 3): GUE and GOE "for curved and
   flat interfaces, respectively"; the conclusion speaks of "the
   geometry-dependent universality" of the class (p. 4).
7. **Correlation** (p. 4): the two-point correlation agrees with the
   Airy₂ covariance, with a finite-time correction near t^(−1/3).
8. **Why this system** (p. 4): "The growth of DSM2 results from strictly
   local processes"; the stochasticity is intrinsic turbulence, not
   quenched disorder; and fast response allowed hundreds of runs.
   Reproducibility across voltages and resolutions is stated, not shown.
9. **Note added in proof** (p. 4): Sasamoto and Spohn's exact solution of
   the 1+1 KPZ equation "offers a clear theoretical ground of our
   experimental results".

## Assumptions

The DSM2 front is a 1+1-dimensional KPZ interface: local growth, white
noise, no quenched disorder, argued rather than derived. Prähofer and
Spohn's ansatz h ≃ v∞t + (A²λt/2)^(1/3)χ carries over from solvable models
to the class, and the asymptotic relations fixing λ and A hold for a
circular front. Times are short (to 28.4 s); higher cumulants are
"statistically more demanding and hence provide less conclusive
results".

## Concepts

KPZ class in 1+1 dimensions (α = ½, β = ⅓, z = 3/2); Family–Vicsek
scaling; Tracy-Widom GUE and GOE; Airy₂ process; DSM1 and DSM2
turbulence; quenched disorder; finite-time corrections.

## Bearing on the record

- **CLAIM-841** (KPZ row): **supports, with a qualification.** The front
  shows KPZ scaling in a state driven well above a threshold (item 2),
  reported robust across voltages, so nothing is tuned to a transition;
  the paper itself never speaks of criticality or tuning, and this
  reading is the record's. The qualification: untuned is not generic.
  The class needs locality and no quenched disorder (item 8), which most
  experiments lack (item 1). The claim's "generically" holds for theory
  and simulation, not for experiment (ARG-tmp2xbl4).
- **LEAD-209** (KPZ column): **supports and corrects.** Its cells
  "W ∝ L^α" and "3/2 in 1D" are what the paper measures. Its "nonzero
  skewness" is near the mark but misplaced: the skewness the paper
  measures (about 0.224) is of the height, the local radius, not of its
  increments. The paper supplies a sharper row: the parameter-free
  skewness and kurtosis, which tell GUE TW from GOE TW and Gaussian and
  so read the geometry.
- **QUESTION-508**: **a partial answer for one system, and a contrast.**
  The paper's three factors (local growth, intrinsic noise, no quenched
  disorder) say what this system has that others lack. The same system
  shows directed-percolation criticality at the DSM1–DSM2 threshold, a
  tuned absorbing-state transition ("spatiotemporal intermittency",
  p. 2, ref. [13]; LIT-tmpoc5u6, registered, unread, known here only by
  its title), and untuned KPZ growth above it.
- **CLAIM-803**: **parallel.** The paper goes "beyond the scaling laws"
  (p. 1): the class is identified by the whole fluctuation distribution
  and the correlation, and the distribution splits sub-classes (GUE,
  GOE) that share the exponents. No edge: the sub-classes are one
  universality class.
- **THEORY-2148**: **background.** The same GUE Tracy-Widom law Baik, Ben
  Arous and Péché find at a sample covariance's edge, here reached by a
  growing interface.
- **TERM-139**: background; the exact 1+1 exponents are cited to "the
  renormalization group approach" (p. 1).
- **CLAIM-tmpvq33w**: one of its cases is KPZ, whose untuned scaling this
  experiment shows in a laboratory.
- **No instruction for machine-learning practice.**

## Limitations

One system and one, curved, geometry; flat interfaces "in progress".
Short times with finite-time corrections; A is fixed by assuming GUE TW,
though skewness and kurtosis are free of it. Cumulants beyond the fourth
are not established. The three factors are argued, not tested.
