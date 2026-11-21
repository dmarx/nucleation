# Reader notes: semicontraction-jafarpour (LIT-tmpavt0i)

## Step 1: copy located (2026-11-21)

- https://arxiv.org/pdf/2005.09774 : arXiv, author preprint, HTTP 200,
  application/pdf, 19 pages; header reads arXiv:2005.09774v8 [eess.SY]
  4 Oct 2020, "Submitted to IEEE TAC, May 18, 2020". Lawful (arXiv).
- Codes read first: CLAIM-tmpdx6l8, TERM-tmp7i7ed, ARG-tmp5ahr5, CLAIM-635,
  THEORY-960, THEORY-2044, LEAD-tmpywiwn, LIT-tmpavt0i.

## Step 2: sections read (2026-11-21)

Read in full: abstract, I (intro), II (notation), III (Defs 1, 2, 4, 12;
Thms 5, 6 statements, 7, 11, 13 with proof; Lemma 9; Remarks 14, 15;
Ex. 16), IV (Def 17, Lemma 18, Thms 19, 21, Ex. 23), V (Thm 24 with proof,
Rmk 25), VI (Thms 26, 27, 28, 30 with proofs; Rmks 29, 31, 32), VII,
App. A. Skimmed/skipped: App. B-F (tensor-norm lemmas, proofs of Thms 5-6,
Thm 30 extension, Lotka-Volterra).

Findings so far:
- Semicontraction = mu_seminorm(Df) <= -c (Def 12). Convergence to
  x* + Ker (Thm 13(ii)) needs shifted invariance; the theorem does NOT say
  where in the kernel the trajectory ends, and Ex. 16 has a trajectory
  that converges to the kernel and runs off to infinity along it.
- Weak contraction = mu(Df) <= 0 w.r.t. a norm (Def 17): distances
  non-increasing. Doubly contracting (Thm 24): a limit point exists in S,
  still not identified by the seminorm.
- The limit is identified only in the examples, and by a separate
  conservation law: Thm 26 limit L^+ b + (v^T x0) 1_n, from v^T L = 0,
  v the dominant LEFT eigenvector. This is an oblique projection along
  Img(L), not the orthogonal projection onto Ker (unless v = 1/n).
- No Markov chains, no discrete time ("extensions to discrete-time" is
  future work, VII), nothing on approximate conservation.

## Step 3: recheck and draft (2026-11-21)

Recheck searches (seminorm, semicontract, weak contraction/non-expansive,
matrix measure, Laplacian, left eigenvector, Coppel, horizontal/Finsler,
QUAD/diffusive coupling, primal-dual, Bullo/Jafarpour, invariant subspace,
consensus). Held and relevant, missed by the brief: CLAIM-481 (Laplacian
flow: kernel is exact compatibility, nonzero spectrum the rates);
THEORY-321 (Golub-Jackson, influence = left eigenvector); THEORY-1161
(Friedkin-Johnsen "anchoring on initial positions", a rival sense of
anchoring); LIT-2837 is the paper's ref [52] (Wang-Slotine); LIT-tmpru0xs
is the sibling seminorm paper. Not held: Pham-Slotine 2007 [40], Slotine
2003 [47], Forni-Sepulchre horizontal contraction [21], Cisneros-Velarde
et al. primal-dual arXiv 2003.12665 [10], Di Bernardo et al. [17].

Draft verdict: characterization CORRECTED. Semicontraction is contraction
transverse to the seminorm's kernel; it does not by itself keep anything
(Ex. 16 diverges along the kernel). Keeping needs weak contraction too
(Thm 24) and, to say what is kept, an exact conserved functional (v^T x
in Thm 26), an oblique not orthogonal projection.
