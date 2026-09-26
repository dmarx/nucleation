---
status: Deferred
status_note: seeded from the abstract and a skim on 2026-09-26; not read in full
title: 'Hilbert Spaces and the Riesz Representation Theorem'
version: 1
tags:
- mathematics
date: '2026-09-26'
published: '2021-08-01'
url: 'https://math.uchicago.edu/~may/REU2021/REUPapers/Adler.pdf'
first_author: 'Adler'
keywords:
- 'Hilbert spaces'
- 'Riesz representation theorem'
- 'orthonormal bases'
- 'duality'
- 'Radon–Nikodym theorem'
implementations: []
summary: >-
  Adler (2021), <https://math.uchicago.edu/~may/REU2021/REUPapers/Adler.pdf>. Every continuous linear functional on a Hilbert space is the inner product with a unique vector of equal norm, and the representer can be written explicitly as the sum of φ(e_k)e_k over any orthonormal basis, which in turn yields the Radon–Nikodym theorem.
---

# LIT-tmpsxt3s: Hilbert Spaces and the Riesz Representation Theorem

Ben Adler (2021), *University of Chicago Mathematics REU 2021 (student expository paper)* — <https://math.uchicago.edu/~may/REU2021/REUPapers/Adler.pdf>

## Key takeaways

- Every continuous linear functional on a Hilbert space is the inner product with a unique vector of equal norm, and the representer can be written explicitly as the sum of φ(e_k)e_k over any orthonormal basis, which in turn yields the Radon–Nikodym theorem.

*Seeded from the abstract and a skim, not a reading. What follows is what the work says about itself.*

An expository undergraduate paper that builds inner-product and Hilbert spaces from first principles and proves the Riesz representation theorem, which characterizes the continuous linear functionals on a Hilbert space through the inner product. It develops the metric tools needed (Cauchy–Schwarz, parallelogram law, projection onto closed convex sets, orthogonal complements), then gives a second, more constructive proof via orthonormal bases. It closes by deriving the Radon–Nikodym theorem, a measure-theoretic result, from the Riesz theorem.

## Standing in the record

Filed on 2026-09-26 at the owner's request, from a list they grouped under the heading *Riesz Representation Theorem*. `Deferred` because nobody has read it closely here yet, not on merit.

**Priority for a deeper reading: low — an expository proof of a standard theorem, already captured by this skim; useful only as a gentle on-ramp if the owner wants one.**

What a deeper reading should check:

- For the representation-learning readings, this is a from-scratch route to the one fact kernel methods need: if point evaluation f↦f(x) is continuous on a Hilbert space of functions, Riesz hands back a vector k_x with f(x)=⟨k_x,f⟩ — that vector is the reproducing kernel, and the RKHS is exactly this situation. The paper itself never mentions kernels; the bridge has to be made by the reader.
- Thm 4.9's basis expansion is the finite-rank intuition behind spectral approximation: expressing a functional (or a target function) through its coefficients on an orthonormal eigenbasis, and truncating.
- The Radon–Nikodym coda is the other live link: the densities it guarantees are what KL divergence and mutual information are defined through, i.e. the quantities an information-bottleneck objective optimises. Worth checking whether that proof (von Neumann's, via L²(μ+ν)) is presented cleanly enough to cite.
- It is student expository work: correct-looking and pedagogically clear, but not a source of new results; cite a textbook (Axler, Rudin) for any claim the anthology leans on.

Access when seeded: Fetched the 15-page PDF directly from math.uchicago.edu (HTTP 200) and extracted its text; read the abstract, contents, both statements and proofs of the theorem (Thm 3.5, Thm 4.9), the Radon–Nikodym coda and the acknowledgments/references. Author's full name "Ben Adler" is from the PDF title block; the paper is dated "August 2021" (no day; PDF CreationDate 2021-09-06), hence published YYYY-08-01. Mentor per acknowledgments: Jake Fiedler.
