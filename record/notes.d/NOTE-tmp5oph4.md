---
status: Read
paper: LIT-tmpd7koy
title: 'Ott and Antonsen 2009, read for whether their reduced manifold attracts, and at what rate'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Read on 2026-11-22 for LEAD-094, as a supplement to Ott and Antonsen
    2008 (LIT-2248, NOTE-tmpd7trg), from the arXiv preprint
    (arxiv.org/pdf/0902.2773v2, 6 pp.), text extracted with pdftotext.
    Read in full, notes included. Pages are the preprint's. Every
    quotation below rechecked by script against the downloaded text. Read
    by the lead worker itself. No email address sent.
date: '2026-11-22'
summary: >-
  The sequel answers the 2008 paper's open question for the order
  parameter. For any phase velocity of the first-harmonic form, with a
  Lorentzian frequency spread Δ > 0 and analytic initial data, the
  frequency-weighted part of the distribution off the reduced manifold
  decays, so the order parameter obeys the reduced equation at long times:
  the manifold is inertial in a frequency-weighted metric, not for the
  distribution itself. The decay is phase mixing, bounded below by rate Δ;
  the proof uses no ratio of rates. For Δ = 0 there is long-time motion off
  the manifold. The reading is [THEORY-tmp0d58z](../theory.d/THEORY-tmp0d58z.md).
---
<!-- inactive-ok-file: THEORY-tmp0d58z CLAIM-tmpa694z CLAIM-tmpervl4 — Proposed or new; this reading and the verdict filed from it -->
<!-- inactive-ok-file: CLAIM-478 — Proposed; the claim the reading bears on -->

# NOTE-tmp5oph4: Ott and Antonsen 2009, read for whether their reduced manifold attracts, and at what rate

## Contribution

A proof that the 2008 reduced manifold attracts the order parameter's
dynamics whenever the oscillators' frequencies are spread, which makes the
reduction a method for all long-time macroscopic behaviour of the class,
not only for states prepared on the manifold. The reading is
[THEORY-tmp0d58z](../theory.d/THEORY-tmp0d58z.md).

## Key results

1. **The result** (abstract, p. 1): the evolution "is, in an appropriate
   physical sense, time-asymptotically attracted toward a reduced manifold
   of system states", and "attractors for the order parameter dynamics
   obtained by restriction to this reduced manifold are, in fact, the only
   such attractors of the full system."
2. **The condition** (p. 1): "the reduced manifold is globally attracting
   provided that the spread ∆ in the distribution of oscillator
   frequencies is nonzero." It resolves the earlier mixed findings: motion
   off the manifold was found for ∆ = 0, agreement for ∆ > 0.
3. **The class** (p. 2): "for all of the problems previously mentioned
   (Refs.[2] to [14]), vθ (θ, t) is expressible in the form" ω plus a
   first-harmonic term in θ with any time course H(t) (eq. 4): Kuramoto,
   a diurnal drive, delays, communities, bimodal g, chimeras, a
   footbridge. "Because the precise time dependence of H(t) will not
   matter in the derivation of our result, it suffices to consider H(t)
   as some general function of time".
4. **The distribution need not converge** (p. 3): with H = 0 the
   homogeneous solutions (eq. 11) keep their size, so "a simple counter
   examples shows that this cannot always be true"; but their
   frequency-weighted integrals decay, Iₙ = Aₙ e^{inθ − n∆t} for a
   Lorentzian (eq. 13).
5. **The mechanism and its rate** (pp. 4–5): integrating along
   characteristics, the decay exponent's last term exceeds (t − T)∆, so the
   off-manifold part of the order parameter goes to zero "if ∆ > 0". The
   bound is a rate of at least ∆; no other rate enters the condition.
   Note 19 compares the mechanism to the distribution function of
   "linear, Landau damped, waves in collisionless plasmas".
6. **Inertial in a metric** (p. 5): "our reduced manifold (Eq.(10)) is
   inertial with respect to the proper distance metric µ", a
   frequency-weighted L² distance chosen so that eq. 11's counterexample
   is avoided.
7. **Without spread** (note 16, p. 6): for ∆ = 0, Josephson-junction
   arrays can be chaotic while their reduced dynamics is two-dimensional,
   "Thus, there is long time dynamics not on the reduced manifold in this
   system if ∆ = 0."
8. **Beyond the Lorentzian** (p. 5): "we believe that this restriction
   does not greatly limit the usefulness of the resulting formulations for
   discovering typical system behavior", citing numerical agreement with a
   Gaussian g in their refs. 6 and 11.

## Assumptions

Infinite N; first-harmonic phase velocity (eq. 4); a Lorentzian g with
∆ > 0; initial data whose continuation is analytic in the lower half
ω-plane and decays there (an example on p. 5 shows the decay condition can
be met after a finite time when it fails initially).

## Concepts

Phase mixing: the frequency-weighted average of components that rotate at
different rates decays though each component keeps its size. An inertial
manifold relative to a chosen metric.

## Bearing on the record

- **[CLAIM-478](../claims.d/CLAIM-478.md), defeater (a).** This is what makes the 2008 reduction a
  serious candidate: the closed law is not only exact on M but reached from
  outside it, for every ∆ > 0, with no condition that the approach be
  faster than the dynamics on M. The approach rate is bounded below by ∆,
  and the rates on M are ∆ − K/2 below locking and of order K/2 − ∆ above
  it ([NOTE-tmpd7trg](NOTE-tmpd7trg.md), key result 4), so in the locked regime with K > 4∆
  the guaranteed approach is slower than the dynamics it constrains. The
  verdict is filed as alternatives, [CLAIM-tmpa694z](../claims.d/CLAIM-tmpa694z.md) and [CLAIM-tmpervl4](../claims.d/CLAIM-tmpervl4.md).
- **[QUESTION-391](../questions.d/QUESTION-391.md)** (bears on). An effective law ceasing to hold because
  suppressed degrees of freedom become important: here it fails as the
  frequency spread goes to zero, when phase mixing stops and motion off
  the manifold persists (key result 7).
- **[CLAIM-405](../claims.d/CLAIM-405.md)** (note only). Whether the population approaches a
  low-dimensional state depends on the metric: yes in the
  frequency-weighted metric µ, no for the distribution (key results 4,
  6). Fixing the metric fixes the verdict, as the claim says.

## Limitations

- The attraction is proved for the order parameter, not the
  distribution; the authors choose the metric to make the statement true.
- The rate bound is a lower bound; the paper gives no estimate of the
  actual approach rate, so it shows only that no rate separation is
  needed, not that none is present.
- Lorentzian g only; the extension to other g is the authors' belief
  backed by numerical comparisons in other papers.
