---
status: Read
paper: LIT-tmpz3w7i
title: 'Donoghue, Schaworonkow & Voytek — Methodological considerations for neural oscillations'
version: 1
history:
- version: 1
  date: '2026-11-03'
  note: >-
    Read from the authors' PsyArXiv preprint (osf.io/hvd67, the download
    OpenAlex lists; PDF created 22 June 2021, 54 pp. with line numbers),
    text extracted with pypdf. I read the front matter, graphical
    abstract, abstract, introduction, Box 1, all seven sections with
    their recommendations and the captions of Figures 1–7, and the
    discussion. The reference list was checked only for the entries the
    PAC passage cites. Sections #4 and #6 were read more quickly than the
    rest. Pages are the preprint's. The published EJN text (55:
    3502–3527) was not compared. The waveform-shape result was reproduced
    in a short simulation (see Key results).
date: '2026-11-03'
summary: >-
  A methods review with simulations: seven ways field-potential analyses
  misread oscillations (absent oscillations, shifted peaks, aperiodic 1/f
  activity, bursts, non-sinusoidal shape, overlapping sources, low SNR),
  each with a recommendation. Non-sinusoidal waveforms produce
  significant phase-amplitude coupling with no interaction between
  rhythms, and aperiodic activity puts power in every band, so neither
  PAC nor band power is by itself evidence of coupled oscillations.
---
<!-- inactive-ok-file: THEORY-tmp6xjgq — Proposed; the reading of Jennings 2026 this bears on -->

# NOTE-tmpsrba2: Donoghue, Schaworonkow & Voytek — Methodological considerations for neural oscillations

## Contribution

It gathers, in one place and with simulations whose code is public
(github.com/voytekresearch/OscillationMethods), the ways in which
standard spectral methods applied to field potentials return numbers that
are easy to misread as oscillatory physiology. Its frame: "these are not
failures of the algorithms per se, which do, mathematically, exactly what
they should; the potential pitfalls lay in how we interpret their outputs"
(p. 6).

## Key insight

Most methods assume a sinusoidal, stationary, oscillation-present signal.
Neural field data are bursty, non-sinusoidal and sit on dynamic aperiodic
activity, so a measure can be numerically correct and still not mean what
it is read to mean. For coupling: "Numerically, these values are not
objectionable … However, there is possible fallacy in the interpretation,
if this relationship is taken to reflect significant coupling between
independent rhythms, when in fact no such interaction between multiple
rhythms need exist" (p. 25).

## Assumptions

- **Simulated data** made to match known properties of field recordings,
  with NeuroDSP (p. 7); "ground-truth properties of physiological data are
  not known" (p. 37), so the simulations show possibility, not prevalence.
- **Univariate focus** (power, phase); multivariate measures such as
  cross-frequency coupling are discussed as inheriting the problems
  (pp. 7, 38).

## Key results

The seven considerations (Box 1, p. 8):

1. **Oscillations may be absent** (pp. 9–12). Aperiodic 1/f^χ activity has
   power at all frequencies (χ typically 0–4), so "just because there is
   power in a frequency band does not imply that there is an oscillation"
   (p. 9); filtering aperiodic noise yields rhythmic-looking traces
   (Fig. 1C).
2. **Peak frequencies vary** (pp. 13–16): a canonical 8–12 Hz band
   misestimates an 8 Hz alpha (Fig. 2).
3. **Aperiodic activity is dynamic** (pp. 17–19): a change in the 1/f
   exponent produces correlated band-power changes across all bands
   (Fig. 3); the theta/beta ratio in ADHD "appears to be driven by
   aperiodic activity" (p. 18).
4. **Bursts** (pp. 21–23): averaging bursty trials creates "an illusion of
   sustained activity" (p. 21).
5. **Waveform shape** (pp. 24–27): narrowband filtering shifts the peaks
   and troughs of asymmetric waves (Fig. 5A); non-sinusoidal shape appears
   as harmonics (Fig. 5B–C), which can be read as separate coupled rhythms;
   and PAC measures "are greatly influenced by waveform shape", giving
   significant coupling from one non-sinusoidal 10 Hz rhythm (Fig. 5D–E).
   Diagnostic: "narrow ranges at exactly multiples of the base frequencies
   indicative of possible coupling caused by waveform shape" (p. 26).
6. **Overlapping sources** (pp. 28–31): volume conduction makes split peaks
   and spurious connectivity.
7. **SNR** (pp. 32–35): low power corrupts phase estimates and so PLVs and
   cross-frequency coupling (Fig. 7F; Aru et al. 2015).

**Reproduction of #5.** A 60 s, 10 Hz signal of sharp-peaked shape,
exp(3 cos φ), with white noise, gave a Tort modulation index between 8–12 Hz
phase and 25–60 Hz amplitude of 0.021, against 0.0001 for a pure cosine
with the same noise; with a 15–25 Hz amplitude band (one harmonic) and with
an 80–250 Hz band, both stayed at noise level (≤ 0.00006). So shape-induced
PAC is real and confined to bands spanning several harmonics. A strictly
periodic wave did not reproduce the 15–25 Hz case of Fig. 5D, which
presumably relies on the filter or on variability in the simulated rhythm
that the caption does not specify.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Band power does not imply an oscillation in that band | strong | the spectrum of aperiodic signals (Fig. 1); elementary |
| C2 | Changes in aperiodic activity can masquerade as changes in several oscillations | strong | simulation (Fig. 3); empirical cases cited (p. 18) |
| C3 | Non-sinusoidal waveforms produce significant PAC without interacting rhythms | strong | simulation (Fig. 5D–E); reproduced here for a multi-harmonic band |
| C4 | Coupling confined to exact harmonic multiples suggests shape; broad coupling suggests genuine nesting | moderate | heuristic, citing Cole et al. 2017, Vaz et al. 2017 (p. 26) |
| C5 | Low SNR biases PLV and coupling measures | strong | simulation (Fig. 7) |

## Concepts

- **Aperiodic activity** — the 1/f-like component of field data, with
  "different putative generators" from oscillations (p. 17).
- **Waveform shape** — rise/decay asymmetry, peak sharpness; measured
  cycle by cycle in the time domain (p. 25).
- **Phase-amplitude coupling** — treated as a measure of dependence that
  may or may not reflect "nested oscillations" (p. 25).

## Connections

- Kramer, Tort and Kopell 2008 (sharp edges and spurious coupling), Cole et
  al. 2017, Lozano-Soldevilla et al. 2016, Giehl et al. 2021 and Vaz et
  al. 2017 are the PAC-and-shape literature it rests on (p. 25).
- Voytek is senior author here and the source of the PAC method
  Szczepanski et al. used ([LIT-tmpkq6x5](../literature.d/LIT-tmpkq6x5.md), [NOTE-tmpryuio](NOTE-tmpryuio.md)).
- **"Park and colleagues (2017)", which A5 attributed to this line of
  caution, is not cited in this paper.** The only 2017 entries near the
  name are Cole et al. 2017 on Parkinson's beta, whose title contains
  "Parkinson's". It may be a garbled memory of that paper.

## Bearing on the record

- **Jennings 2026 ([LIT-tmpasemk](../literature.d/LIT-tmpasemk.md), [NOTE-tmpby7i2](NOTE-tmpby7i2.md)), on PAC.** Jennings reads PAC
  as "evidence that low frequency waves constrain high frequency waves, a
  form of power or control" (p. 28). This paper shows that a PAC measure
  can be significant with no second rhythm at all. A measured PAC therefore
  needs shape controls before it is evidence of one rhythm modulating
  another, let alone of a macro-level power ([THEORY-tmp6xjgq](../theory.d/THEORY-tmp6xjgq.md)).
- **On 1/f scaling.** Jennings offers the brain's self-organization "into
  scale-free patterns" as what "allows for the emergence of the subject"
  (pp. 27–29), noting in fn. 20 that such background activity was once
  treated as noise. Here 1/f activity is the aperiodic
  background, present in every recording, with putative generators in
  postsynaptic currents (p. 9; Gao et al. 2017). It is a physiological
  feature worth studying, but its presence is not by itself evidence of a
  higher-level constraint.
- **On Szczepanski et al. ([THEORY-tmp9pem2](../theory.d/THEORY-tmp9pem2.md)).** That study's 80–250 Hz
  coupling to a 2–5 Hz phase is broad and far from low harmonics, so by
  C4 it is not the typical shape artefact; but no shape control was run.
  A5's caution applies in principle and is not shown to defeat it.
- **The registration's summary held up**: "non-sinusoidal waveforms
  produce apparent coupling" is the paper's #5.
- **No instruction for machine-learning practice.**

## Limitations

- Simulations show what can go wrong, not how often it does in published
  findings; the paper does not re-analyse any empirical PAC result.
- Read from the preprint; the published version may differ.

## Open questions

- What fraction of reported attention-related PAC survives cycle-by-cycle
  shape controls and aperiodic correction?
