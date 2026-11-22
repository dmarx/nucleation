---
status: Read
paper: LIT-3007
title: 'Reed and Hughes, From gene families and genera to incomes and internet file sizes, read for power laws from exponential growth killed at a random time'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Read on 2026-11-22 by a delegated reader from the published version
    (Phys. Rev. E 66, 067103, a Brief Report, 4 pages) on W. J. Reed's
    faculty page at the University of Victoria
    (https://web.uvic.ca/~math-statistics/emeritus/wjreed/PREpowerlaws.pdf),
    a lawful copy under ADR-074: all four pages, equations 1–11, figure
    captions and references; the figures seen only through their captions.
    Nothing skipped. The derivations for the birth-and-death, total-progeny
    and branching cases are deferred to other papers (refs. 10, 13, 19),
    not read. Every quotation below rechecked by the filer by script against
    the extracted text; the double Pareto (zero drift) and the pure-birth
    tail checked by simulation by the reader, and the quadratic's roots by
    the filer, with python3 -I.
date: '2026-11-22'
summary: >-
  Exponential growth killed or observed at a time with constant hazard
  gives power-law tails: a pure Pareto for deterministic growth, a double
  Pareto with exponents from a quadratic for geometric Brownian motion,
  and analogues for multiplicative, birth-and-death and branching
  processes. Support for the applications is visual.
---
<!-- inactive-ok-file: CLAIM-795 CLAIM-803 CLAIM-815 CASE-303 QUESTION-505 SYNTHESIS-119 THEORY-tmphwf0q ARG-tmpadlas NOTE-tmpa7yd2 THEORY-2150 CLAIM-824 CLAIM-830 CLAIM-817 CLAIM-806 — Proposed or new; the entries this reading bears on, its own reading and argument -->

# NOTE-tmpbic9d: Reed and Hughes, From gene families and genera to incomes and internet file sizes, read for power laws from exponential growth killed at a random time

## Contribution

One mechanism, random killing or observation of a process with
"exponential growth in expectation", gives power-law behaviour "in one or
both tails" (abstract). It unifies earlier models (Reed on incomes and
cities, Huberman and Adamic on web sites, Mitzenmacher on file sizes, Yule
on genera) and predicts a lower-tail power law where the process can
decrease, "facts previously unrecognized" for incomes and settlement
sizes.

## Key results

1. **Deterministic case** (p. 1): "Consider the simple case of
   deterministic exponential growth X(t) = e^(μt) killed at a random time
   T which is exponentially distributed with parameter ν." The killed
   state has density (ν/μ)x^(−ν/μ−1) for x > 1, "giving power-law behavior
   over its full range"; survival x^(−ν/μ).
2. **Killed geometric Brownian motion** (p. 2, eqs. 8–9): log X̄ is
   asymmetric Laplace, and "the distribution of X̄ is a two-sided Pareto or
   double Pareto distribution", density ∝ x^(β−1) below X₀ and x^(−α−1)
   above, where α and −β "are the roots of the quadratic equation"
   ½σ²s² + (μ − ½σ²)s − ν = 0. The filer checked: at μ = ½, σ = 1, ν = 1
   (zero log drift) the roots are ±√2, where the deterministic ν/μ would
   be 2; at σ = 0.01, μ = 1, ν = 0.5 the upper root is 0.500012, near
   ν/μ = 0.5. The reader's four-million-draw simulation at the zero-drift
   point matched P(X̄ > 5) and P(X̄ > 20) to three figures.
3. **Why ages are exponential** (p. 2): "the time that an individual has
   been earning and the time a settlement has been in existence can
   reasonably be modeled as having exponential distributions, based on the
   assumption that the workforce and the population of settlements are
   growing at a fixed rate."
4. **Killed multiplicative process** (p. 2): with geometric killing, an
   upper tail if every factor exceeds 1, a lower one if every factor is
   below 1, and "power-law behavior in both tails" if it can go either way.
5. **Killed birth-and-death** (p. 3, eq. 10): P(X̄ = n) ∼ k₁n^(−[1+ν/(λ−δ)])
   for λ > δ; a "stretched exponential" at λ = δ; a geometric factor times
   a power for λ < δ. The reader's pure-birth check (λ = 1, δ = 0, ν = ½)
   held n^(ν/λ)·P(X̄ ≥ n) near 0.89 from n = 10 to 1,000.
6. **Yule** (p. 3): Yule "developed the eponymous Yule distribution to fit
   such data, using essentially the above model with δ = 0. He assumed
   that the size of a genus was that of a killed pure birth (or Yule)
   process."
7. **Total progeny** (p. 3, eq. 11): the number ever alive has the same
   upper exponent, for λ > δ + ν.
8. **Killed Galton–Watson** (pp. 3–4): P(X̄ = m) ∼ R(m)m^(−1−κ),
   κ = ln[(1 − p)^(−1)]/ln μ, with "log-periodic oscillations" in R(m),
   proved for geometric offspring and "of very small amplitude"; argued
   elsewhere (ref. 19).

## Assumptions

- A constant killing hazard (exponential or geometric observation time),
  independent of the state.
- Growth exponential in expectation.
- For the applications, a population whose units enter at a fixed
  exponential rate, so that ages are exponential.
- Empirical support is visual linearity of log-log rank-size and
  survival plots, binned where needed ("unbinned income data are not
  available"); no fit, no test, no alternative.

## Concepts

Killed (or once-observed) process; constant hazard; double Pareto; the
asymmetric Laplace law of the logarithm; poles of the generating function
setting the tail exponents; stretched exponential at the balanced
birth-death point; log-periodic oscillation; Yule process; rank-size plot.

## Bearing on the record

- **CLAIM-795, item 6: grounds it, and qualifies its framing.** Result 1
  is item 6 exactly, with ν = λ and μ = g. It is the paper's opening
  illustration, not its result: with noise the upper exponent is the
  positive root of the quadratic, not ν/μ (the limit σ → 0), and a lower
  power tail appears. "Even identical growth rates can coexist with highly
  unequal sizes" is A's gloss, true of the deterministic case and not said
  by the paper. ARG-tmpadlas argues the support.
- **CLAIM-795, item 1, CLAIM-815, CASE-303: a contrast.** The killed
  supercritical Galton–Watson process is a second branching route, with
  exponent 1 + κ, unrelated to the critical s^(−3/2).
- **QUESTION-505: qualifies the partial pattern.** Only the deterministic
  case is a bare ratio of rates. With noise α solves a quadratic in μ, σ²
  and ν; at zero log drift α = √(2ν)/σ, a ratio under a square root. The
  birth-death ν/(λ − δ) and the branching ln[1/(1 − p)]/ln μ fit the
  pattern.
- **SYNTHESIS-119: supports** its link that an exponentially distributed
  observation time turns Gibrat's lognormal into a power law (eq. 9).
- **CLAIM-803: background, illustrating it**: one mechanism offered for
  six domains, on log-log plots alone.
- **THEORY-2150, NOTE-tmpa7yd2: consistent.** Mitzenmacher's zero-drift
  double Pareto is eq. 9 at μ = ½σ²; Newman's α = 1 − a/b is result 1's
  density exponent. Newman's reading covers the deterministic case only.
- **Filer A's and C's files** (reported, not noted): CLAIM-824 (Gibrat
  plus a random observation time is that claim's bullet; supports),
  CLAIM-830 (result 3 and Yule's entry of genera support the age half and
  the role of entry, not the identification with attachment), CLAIM-817
  (parallel: entry in a non-network setting), CLAIM-806 (contrast: balance
  at λ = δ kills the power law here).

## Limitations

- A four-page Brief Report: the birth-death, total-progeny and branching
  results are stated, with proofs elsewhere.
- The empirical figures are visual. No fitted exponents, no test against
  the lognormal, no independent estimate of ν or μ: the tie between
  mechanism and data is plausibility.
- Exponential observation times are justified only by fixed-rate
  population growth.
