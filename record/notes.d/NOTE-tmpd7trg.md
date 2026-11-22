---
status: Read
paper: LIT-2248
title: 'Ott and Antonsen 2008, read for an exact low-dimensional law without rate separation, as a candidate defeater of the rate-difference claim'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Read on 2026-11-22 for LEAD-094 from the arXiv preprint
    (arxiv.org/pdf/0806.0004v1, 16 pp.), text extracted with pdftotext.
    Read in full, notes included; Fig. 1 not viewed. Pages are the
    preprint's. Read with its sequel, Ott and Antonsen 2009 (LIT-tmpd7koy,
    NOTE-tmp5oph4), which answers its open question. Every quotation
    below rechecked by script against the downloaded text. Read by the
    lead worker itself, not a delegated reader. No email address sent.
date: '2026-11-22'
summary: >-
  For infinitely many globally coupled phase oscillators, distributions
  whose Fourier coefficients in phase are powers α(ω, t)ⁿ of one function
  form an invariant manifold M; for a Lorentzian (or any rational)
  frequency distribution the order parameter on M obeys a finite set of
  ordinary differential equations, exactly, while the distribution on M
  stays infinite-dimensional, with a continuous spectrum of neutral modes.
  Whether M attracts is left open (note 24). Read for the question whether
  this is the defeater (a) of CLAIM-478; the reading is THEORY-tmpmvcnr,
  and the verdict is filed as alternatives, CLAIM-tmpa694z and
  CLAIM-tmpervl4.
---
<!-- inactive-ok-file: THEORY-tmpmvcnr CLAIM-tmpa694z CLAIM-tmpervl4 CLAIM-tmpo6ehq ARG-tmp5xhiv — Proposed or new; this reading and the entries filed from it -->
<!-- inactive-ok-file: CLAIM-478 CLAIM-157 CLAIM-626 — Proposed; the entries the reading bears on -->

# NOTE-tmpd7trg: Ott and Antonsen 2008, read for an exact low-dimensional law without rate separation, as a candidate defeater of the rate-difference claim

## Contribution

An ansatz that turns the continuum Kuramoto problem, and several of its
extensions, into a finite set of ordinary differential equations for the
order parameter, exactly, on a restricted class of states. The reading is
THEORY-tmpmvcnr.

## Key results

1. **The claim** (abstract, p. 1): "in the infinite size limit, certain
   systems of globally coupled phase oscillators display low dimensional
   dynamics", with "an exact, closed form solution for the nonlinear time
   evolution of the Kuramoto problem with a Lorentzian oscillator frequency
   distribution function".
2. **Invariance, not attraction** (§II, p. 4): states satisfying the
   conditions "form a manifold M", and states in M evolve to states in M:
   "Thus M is ‘invariant’ under the dynamics." The order parameter's
   evolution "is exactly finite dimensional even though the manifold M and
   the dynamics of the distribution function f as it evolves in M are
   infinite dimensional."
3. **The ansatz** (§III, pp. 5–6): with f's Fourier coefficients
   fₙ = αⁿ, "we find the remarkable result that this special form of f
   represents a solution" of the continuity equation when α obeys
   ∂α/∂t + (K/2)(rα² − r*) + iωα = 0 (eq. 6). Motivation (p. 6–7): the
   incoherent and the partially locked stationary states both have this
   form, so the family "connect[s] these two states in a natural way".
4. **The Lorentzian case** (p. 8): closing the frequency integral on the
   pole of g gives dρ/dt + (1 − K/2)ρ + (K/2)ρ³ = 0 (eq. 10), solved in
   closed form (eq. 11); "Linearization of Eq. (10) yields an exponential
   damping rate of [1 − (K/2)] for perturbations" around ρ = 0 for K < 2,
   and (K/2) − 1 about the locked state above it.
5. **No microscopic relaxation** (p. 9): "linearization of Eqs. (6) and
   (7) about their equilibria yields a problem with a continuous spectrum
   of neutral modes [...]. Thus the microscopic dynamics in M of the
   distribution function is infinite dimensional, while the macroscopic
   dynamics of the order parameter is low dimensional."
6. **Extensions** (§IV, pp. 9–12): any rational g(ω) gives as many
   complex order parameters as g has poles in the lower half-plane
   ("the above considerations can be applied to any g(ω) that is a
   rational function of ω"); a periodic drive (eq. 14), whose equilibria,
   limit cycle and bifurcations match the full system's as computed in
   their ref. 10; communities of oscillators (eq. 15), one complex order
   parameter each, with chaos conjectured for two or three communities;
   uniform delay, which makes the reduced system a delay equation,
   "now infinite dimensional".
7. **Open: does M attract?** (note 24, p. 15): "we emphasize that M need
   not be attracting for the microscopic state", shown by a solution with
   r(t) = 0 for all t built from higher harmonics alone. And (§V, p. 13):
   "can any rigorous results be obtained relevant to whether our
   macroscopic order-parameter attractors obtained by considering f in the
   manifold M have general validity". The sequel (NOTE-tmp5oph4) answers
   this for the order parameter.

## Assumptions

- N → ∞; all-to-all coupling; a phase velocity carrying the first
  harmonic of the phase only (sin(θⱼ − θᵢ) and a sinusoidal drive). The
  paper does not say that a second harmonic would break the invariance;
  CLAIM-tmpo6ehq shows it does.
- α analytic in the lower half ω-plane and decaying there; |α| ≤ 1.
- Finite dimension needs a rational g(ω); a Gaussian g gives an
  infinite-dimensional reduced system. For the drive problem the authors
  report from their ref. 10 that Gaussian g gives the same attractors and
  bifurcations "(albeit at different parameter values)" (p. 5).

## Concepts

The order parameter r as an integral over the distribution; an invariant
manifold of distributions; the Poisson-kernel family (eq. 8); the residue
evaluation that makes the frequency integral finite-dimensional.

## Bearing on the record

- **CLAIM-478, defeater (a).** The reduction is exact and needs no small
  parameter: nothing on M relaxes onto anything (key result 5). What
  makes the order parameter's law closed is the invariance of a family of
  states under the first-harmonic form of the coupling, together with the
  analytic structure of g. Whether that meets (a) depends on whether an
  exact invariance counts as the persistence the defeater requires to be
  absent; the two readings are filed as alternatives, CLAIM-tmpa694z (not
  met; leaned to) and CLAIM-tmpervl4 (met within the class), with
  ARG-tmp5xhiv. Near the threshold the same equations illustrate the
  claim's second half: the collective mode's damping rate 1 − K/2 goes to
  zero at Kc = 2 (key result 4).
- **CLAIM-388** (corroborates). A nonlinear case of the same shape: under
  uniform all-to-all coupling, where no subset of oscillators is a weakly
  coupled block, a function of the whole state, the order parameter, is
  exactly closed on M.
- **QUESTION-218** (bears on). The closed variable is a function of the
  whole state, not a subset of members; in the community model (eq. 15)
  each community's order parameter closes at any inter-community coupling.
- **CLAIM-157** (note only). The community order parameters close
  whether or not the communities are weakly coupled blocks, a closure the
  block criterion does not register (as CLAIM-388 found for the linear
  case).
- **CLAIM-626** and **CLAIM-481** (note only). On M the coupling slows the
  collective mode as K → Kc; with the sequel's attraction rate of at least
  the frequency spread, the reduction sits on a separation that the
  instability makes, which is CLAIM-626's first case.
- **QUESTION-281** (bears on). The onset of partial locking at Kc is an
  instability amplifying small differences, here with an exact
  low-dimensional law; the driven problem adds the folds and limit cycle
  of eq. 14.
- **QUESTION-252** (bears on). On M the order parameter's law is closed
  and memoryless while the omitted variables are neither slaved nor
  decaying; off M the 2008 paper does not say.

## Limitations

- The result is for states on M only; the paper says itself that M need
  not attract the distribution (note 24). The sequel supplies attraction
  for the order parameter, not for the distribution.
- The class is narrow: infinite N, first-harmonic coupling, analytic
  initial data, rational g for finite dimension. The paper's evidence that
  the reduced attractors are the full system's is one numerical comparison
  (the driven problem, its ref. 10) and the Gaussian remark.
- The paper gives no account of why the ansatz works; the group-theoretic
  explanation (Watanabe and Strogatz, cited p. 12, and later work) is not
  in it.
