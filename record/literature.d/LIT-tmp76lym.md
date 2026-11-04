---
status: Active
status_note: >-
  read in full 2026-11-04 (NOTE-tmpke9h3) from the author's arXiv
  preprint, v2; worth reading as a clear map of what large-deviation
  theory proves about escape from a potential well and what it does not:
  Wentzell–Freidlin give the exponent (Arrhenius' law), even for
  non-gradient drift, while the Eyring–Kramers prefactor needed potential
  theory (Bovier, Eckhoff, Gayrard and Klein 2004) or the Witten Laplacian,
  degenerates at bifurcations, and can fail to converge for irreversible
  dynamics. Registered as the stand-in for Freidlin and Wentzell's book,
  LIT-tmp6rglf, whose exit-problem results it restates. A review: proofs
  are sketched, and most of it treats the gradient case.
title: "Kramers' law: Validity, derivations and generalisations"
version: 1
history:
- version: 1
  date: '2026-11-04'
  note: >-
    Registered and read on 2026-11-04 as a stand-in for Freidlin and
    Wentzell's Random Perturbations of Dynamical Systems (LIT-tmp6rglf),
    whose body could not be read, at the owner's request; that book is
    cited in the pasted bibliography on emergency readiness, written by
    another assistant (A) and pasted by the owner on 2026-11-04, which does
    not cite this survey. Citation checked against the arXiv record:
    Nils Berglund, arXiv:1106.5799 [math.PR], v1 of 28 June 2011
    (`published:`), v2 of 22 January 2013; journal reference Markov
    Processes and Related Fields 19 (2013) 459–490, from arXiv's
    journal_ref. No DOI was found and Crossref was not queried, so the
    journal pages are unverified. Not held before (no hit for 1106.5799 or
    the title). Copy: https://arxiv.org/pdf/1106.5799 (v2), 26 pages,
    extracted with pdftotext.
tags:
- mathematics
- probabilistic-modeling
- complex-systems
date: '2026-11-04'
published: '2011-06-28'
arxiv: '1106.5799'
first_author: 'Berglund'
keywords:
- "Arrhenius' law"
- "Kramers' law"
- 'metastability'
- 'large deviations'
- 'Wentzell-Freidlin theory'
- 'WKB theory'
- 'potential theory'
- 'capacity'
- 'Witten Laplacian'
- 'cycling'
implementations: []
summary: >-
  Berglund (2011; Markov Processes Relat. Fields 2013). A review of the
  routes to a rigorous Kramers' law, the mean transition time
  E τ ≃ C e^{[V(z*)−V(x*)]/ε} of an overdamped diffusion between potential
  minima. Large deviations (Wentzell–Freidlin) give the exponent through
  the action functional and quasi-potential, also for non-gradient drift,
  but "fails to control the prefactor"; explicit integrals settle one
  dimension, WKB gives formal results, potential theory and capacities gave
  the first full proof in 2004, and the Witten Laplacian the full
  expansion. The prefactor degenerates at non-quadratic saddles, and in
  the irreversible case Arrhenius' law holds while Kramers' fails
  (cycling).
---
<!-- inactive-ok-file: THEORY-tmp2rxfm — Proposed and new; the account filed from Berglund (2011), cited as open -->

# LIT-tmp76lym: Kramers' law: Validity, derivations and generalisations

Berglund, N. (2011). Kramers' law: Validity, derivations and generalisations. arXiv:1106.5799; *Markov Processes and Related Fields* 19 (2013): 459–490.

## Key takeaways

*From the reading, NOTE-tmpke9h3. Sections and equations are the preprint's.*

- **Wentzell–Freidlin, restated.** The rate function I(ϕ) = ½∫‖ϕ̇ − f(ϕ)‖² dt
  (eq. 2.3), the quasi-potential, which "measures the cost of reaching z in
  arbitrary time." (eq. 2.8), and the exit-time theorem
  lim 2ε log E τ = inf over ∂D of the quasi-potential (Theorem 2.2,
  credited to Wentzell and Freidlin 1969–70).
- **Exponent, not prefactor.** The large-deviation approach proves
  Arrhenius' law "for more general than gradient systems, but fails to
  control the prefactor." (§1).
- **Prefactor proved late.** The Eyring–Kramers formula had "a full proof
  of (1.9) having been obtained only in" 2004 (§1; Theorem 3.3).
- **Where it fails.** "Kramers’ law (1.9) cannot be true in the presence
  of" singular Hessians (§4.1); for irreversible dynamics the prefactor
  "need not even converge to a limiting value as ε → 0." (§4.3).

## Standing in the record

Registered as the stand-in for Freidlin and Wentzell's book, LIT-tmp6rglf,
of which only the front matter was read. It restates the book's exit
problem (Chapter 4): action functional, quasi-potential, exit time and
exit location; it points to, but does not state, the cycle hierarchy for
many attractors, and it does not touch the book's stationary-distribution,
averaging, Hamiltonian, graph or stabilization chapters. Its own subject,
the prefactor, is what the book leaves out by giving rough asymptotics
only. Bears on THEORY-1264 (it gives the exponent, so read that theory as
a statement about log-rates) and THEORY-1309. Filed from it:
THEORY-tmp2rxfm. No instruction for machine-learning practice; nothing for
the anthology.
