---
number: 206
status: Skimmed
formerly:
- NOTE-tmpaqx17
paper: LIT-243
title: 'Adler — Hilbert spaces and the Riesz representation theorem'
version: 1
date: '2026-09-26'
summary: >-
  Every continuous linear functional on a Hilbert space is the inner product with a unique vector of equal norm, and the representer can be written explicitly as the sum of φ(e_k)e_k over any orthonormal basis, which in turn yields the Radon–Nikodym theorem.
---
<!-- inactive-ok-file: LIT-243 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-26; the directive lapses when its status changes -->

# NOTE-206: Adler — Hilbert spaces and the Riesz representation theorem

## Contribution

An expository undergraduate paper that builds inner-product and Hilbert spaces from first principles and proves the Riesz representation theorem, which characterizes the continuous linear functionals on a Hilbert space through the inner product. It develops the metric tools needed (Cauchy–Schwarz, parallelogram law, projection onto closed convex sets, orthogonal complements), then gives a second, more constructive proof via orthonormal bases. It closes by deriving the Radon–Nikodym theorem, a measure-theoretic result, from the Riesz theorem.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §1–2 (pp. 1–6): inner product presented as a similarity measure; norm, Cauchy–Schwarz, parallelogram equality; Hilbert projection theorem (Thm 2.2) and orthogonal complements are the machinery the first proof rests on.
- §3, Thm 3.5 (p. 7): existence and uniqueness of u with φ(v)=⟨u,v⟩ and ‖u‖=‖φ‖, proved by picking a unit vector orthogonal to ker φ; footnote 9 notes general Banach spaces are not isometric to their duals, so completeness plus an inner product is what makes this work.
- p. 8: the author flags that this proof "falls from the sky" — it does not say how to find the representer — which motivates §4.
- §4, Thm 4.9 (p. 12): constructive form, u = Σ_k φ(e_k) e_k for any orthonormal basis, with ‖φ‖² = Σ|φ(e_k)|²; footnote 11 notes Gram–Schmidt makes this concrete in the separable case.
- §5, Thm 5.1 (pp. 12–15): Radon–Nikodym (existence of a density dν/dμ for absolutely continuous σ-finite measures) proved from the Riesz theorem, following Axler / Stein–Shakarchi.

## Open questions

- For the representation-learning readings, this is a from-scratch route to the one fact kernel methods need: if point evaluation f↦f(x) is continuous on a Hilbert space of functions, Riesz hands back a vector k_x with f(x)=⟨k_x,f⟩ — that vector is the reproducing kernel, and the RKHS is exactly this situation. The paper itself never mentions kernels; the bridge has to be made by the reader.
- Thm 4.9's basis expansion is the finite-rank intuition behind spectral approximation: expressing a functional (or a target function) through its coefficients on an orthonormal eigenbasis, and truncating.
- The Radon–Nikodym coda is the other live link: the densities it guarantees are what KL divergence and mutual information are defined through, i.e. the quantities an information-bottleneck objective optimises. Worth checking whether that proof (von Neumann's, via L²(μ+ν)) is presented cleanly enough to cite.
- It is student expository work: correct-looking and pedagogically clear, but not a source of new results; cite a textbook (Axler, Rudin) for any claim the anthology leans on.
