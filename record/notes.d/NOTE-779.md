---
number: 779
status: Read
formerly:
- NOTE-tmpda9q6
paper: LIT-921
title: 'Kanerva — Sparse Distributed Memory and Related Models'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the NASA NTRS PDF of RIACS TR 92.10 (April 1992,
    58 pages), text extracted with pdftotext from the report's OCR layer:
    every section (1–10), the derivations of §§3.5–3.7, the figure
    captions and the references. The figures themselves are drawings
    whose OCR is unusable; they were read from their captions and the
    text that describes them. The OCR garbles several equations (the
    optimal p, the capacity limit); they are given below as the
    surrounding text fixes them, and each was checked against the stated
    numbers (p = 0.000368 for M = 10⁶, T = 10⁴; τ ≈ 0.105 at φ = 0.999).
date: '2026-10-14'
summary: >-
  SDM is a two-layer memory: a fixed random address matrix selects a few
  of many hard locations near the cue, and an outer-product contents
  matrix stores the word there. Recall of uniform random data has
  signal pM against noise pM[1 + pT(1 + p²M)], best at p = (2MT)^−1/3, and
  capacity tends to 1/[Φ⁻¹(φ)]² of the hard locations, about 0.1 at
  fidelity 0.999. An ordinary RAM is the special case of radius zero.
---
<!-- inactive-ok-file: LIT-928 — Deferred, unread; Kanerva's book, named as where the critical distance is derived, not leaned on -->
<!-- inactive-ok-file: CLAIM-180 CLAIM-182 — Proposed; open, and cited as open: the theses of the nucleating-argument line are under test, not settled -->

# NOTE-779: Kanerva — Sparse Distributed Memory and Related Models

## Contribution

The report restates sparse distributed memory (SDM) in matrix form and
sets it within one framework with the ordinary random-access memory,
correlation-matrix memories, feed-forward networks, the cerebellar cortex,
Jaeckel's, Hassoun's and Prager and Fallside's variants, and the
cerebellar models of Marr and of Albus. Its own quantitative content is a
simple signal-to-noise analysis (after Jaeckel 1989a): bit fidelity, the
optimal probability of activation, and capacity as a fraction of the
number of hard locations. The rest is mapping between designs.

## Key insight

Address through a huge, sparse, random expansion. A long cue activates
the few hard locations within a radius of it, the word is added into all
of them, and retrieval sums whatever the cue's locations hold. Because
the activation sets of unrelated cues barely overlap, the sum is
dominated by the target, and capacity is set by how many hard locations
the memory has, not by the length of the words. Make the radius zero, the
locations complete and the counters one bit, and the same machine is an
ordinary RAM.

## Assumptions

- **Uniform random data.** Addresses and words have independent, equally
  likely bits, and hard addresses are a uniform random sample (§2.2). The
  capacity and optimal-p results hold only here; §8 says real data
  cluster and the uniform memory then wastes most locations.
- **Exact retrieval cues.** The fidelity and capacity analysis uses the
  storage address itself as the cue (§3.7). Noisy cues reduce signal,
  noise and their ratio, and that case "is not carried out here".
- **Independent Poisson overlaps.** The weights Lₜ = Yₜ·Y_T (overlap sizes)
  are treated as independent Poisson variables, so the result is
  "approximate" (§3.5).
- **Unsaturated counters.** C is the sum of the stored outer products only
  if counter capacity is never exceeded (§3.3).
- **Binary units**, ±1 in the matrix notation, Hamming distance or its
  equivalent inner-product threshold: h(Aₘ, x) ≤ H iff Aₘ·x ≥ N − 2H = D.

## Key results

- **Construction (§§2.2, 3.2).** M hard locations with fixed random
  addresses A (M × N); a cue x activates location m when d = Aₘ·x ≥ D,
  so y = y(Ax) has about pM ones. Storing w at x: C := C + y(Ax) ⊗ w,
  "the outer-product, or Hebbian, learning rule"; retrieving:
  z = z(Cᵀy(Ax)), thresholded at 0. Sample memory: N = U = 1,000,
  M = 10⁶, T = 10⁴, counters in −15…15, H = 447 (p = 0.000445; ideal
  0.000368).
- **RAM as a special case (§2.2).** With A containing all 2ᴺ addresses,
  H = 0 and one-bit counters, retrieval returns the word last written at
  x: "the sparse distributed memory is a generalization of the
  random-access memory".
- **Whole-set form (§3.3).** With Y = y(XAᵀ), C = YᵀW and recall
  Z = z(YYᵀW). If the rows of Y are orthogonal, YYᵀ ≈ pMI and recall is
  perfect; "the purpose of addressing through A is to produce (nearly)
  orthogonal activation vectors".
- **Relation to correlation-matrix memories (§3.4).** C is a matrix of
  unnormalised correlations between activation variables and word bits.
  Replacing the inputs X (Anderson, Kohonen) by the expanded Y "blown way
  up (from a thousand to a million)" makes capacity "independent of the
  input dimension N".
- **Signal, noise, fidelity (§§3.5–3.6).** For a bit stored as 1 and
  retrieved by its exact address, the sum Σ has mean μ = pM (all copies
  of the target) and variance σ² = pM[1 + pT(1 + p²M)]; the other
  (T − 1)p²M ≈ 2,000 contributions cancel on average. Bit fidelity
  φ = Φ(ρ), ρ = μ/σ. *Holds when:* uniform random data, exact cues,
  Poisson approximation.
- **Optimal activation (§3.6).** Maximising ρ² = pM/[1 + pT(1 + p²M)]
  gives p = (2MT)^−1/3. With approximate cues the best p is "somewhat
  larger … (typically, less than twice as large)"; with clustered data
  it is smaller.
- **Capacity (§3.7).** With τ = T_max/M at fidelity φ,
  [Φ⁻¹(φ)]² = 1 / [1/(pM) + τ(1 + p²M)], and as M → ∞ at the optimal p,
  τ → 1/[Φ⁻¹(φ)]². At φ = 0.999, τ ≈ 0.105 asymptotically and 0.096 for
  the million-location memory. Citing Keeler (1988), SDM and the binary
  Hopfield net with outer-product learning "have the same capacity per
  storage element"; the Hopfield net's 0.15N corresponds to φ = 0.995.
  The difference is that SDM's capacity grows with M while "the capacity
  of the Hopfield net is limited by the word size". With approximate cues
  and stricter output tolerance capacity "goes down" (Chou 1989). The
  practical guide is T at 1–5% of M.
- **As a neural network (§4).** A two-layer feed-forward net whose hidden
  layer (the hard locations) is far larger than its input, with A fixed
  and C trained; training is fast ("single-trial learning") but needs a
  suitable data representation.
- **Cerebellum (§5).** Mossy fibres as the address, granule cells as hard
  locations, parallel-fibre–Purkinje synapses as counters, climbing fibres
  as the word-in line; the cat's numbers (several million mossy fibres,
  billions of granule cells, about 10⁵ parallel fibres per Purkinje cell)
  are "reasonable". The text flags discrepancies: a granule cell has 3–5
  inputs, so activation is not by Hamming distance.
- **Variants (§6).** Jaeckel's selected-coordinate design (k = 10 address
  bits per location, p = 0.5ᵏ = 0.001) and hyperplane design (k = 3,
  p = (L/N)ᵏ) recover stored words better than the basic design by
  signal-to-noise ratio. For all designs the optimal p is near
  (2MT)^−1/3, because two cues' activation sets overlap by about p²M
  "unless x and x′ are very similar". Hassoun's p ≈ 0.5 design works
  poorly with outer-product learning but, with Ho–Kashyap recording,
  gives large basins and few false attractors.
- **Marr and Albus (§7).** Marr's codon cells and Albus' CMAC are both
  close to the hyperplane design; CMAC is shown to be a special case of
  it, trained by error correction.
- **What a memory does not do (§9).** It stores and recalls patterns with
  a reliability estimate, "But that is all; the memory assigns no meaning
  to the data beyond the reliability estimate." A name is "an ideal
  encoding, except that it is arbitrary"; the senses must produce
  encodings in which views of one object are close and other objects far.
- **Pattern computing (§10).** In symbolic computing the units are
  pointers, "names (very compact, 'ideal' encodings)"; in pattern
  computing the units "serve both as pointers and as data, and they need
  not be precise".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | SDM generalises the RAM: radius zero, complete addresses and one-bit counters give back an ordinary memory | strong | construction, §2.2 |
| C2 | For uniform random data and exact cues, bit fidelity is Φ(ρ) with ρ² = pM/[1 + pT(1 + p²M)], best at p = (2MT)^−1/3 | moderate | approximate derivation under a Poisson-independence assumption, §§3.5–3.6 |
| C3 | Capacity tends to 1/[Φ⁻¹(φ)]² of the hard locations, about 0.1 at φ = 0.999, independent of word length | moderate | limit of the same derivation, §3.7 |
| C4 | SDM and the Hopfield net have the same capacity per storage element | weak here | cited from Keeler (1988), not shown |
| C5 | The cerebellar cortex is organised like an SDM | weak | anatomical correspondence and counts, with discrepancies the text names, §5 |
| C6 | Sparse-address variants recover stored words better than the basic design | weak here | reported from Jaeckel (1989a, b), §6 |

## Method

- Address: d = Ax; activate y = 1[d ≥ D].
- Write: C := C + y ⊗ w (counters clipped at their range).
- Read: s = Cᵀy; z = sign(s).
- Iterate z as the next cue for autoassociative clean-up or for following
  a stored sequence (Figs. 2-1, 2-2).

## Concepts

- **Hard location.** One of M sampled addresses that has physical counters;
  all other addresses exist only as cues.
- **Probability of activation p.** The fraction of hard locations a cue
  activates; it sets the radius H.
- **Fidelity φ.** The probability that a stored bit is recalled correctly
  from its exact address.
- **Capacity τ.** T_max/M at a given φ, with exact cues.
- **Pattern computing.** Computing with long, imprecise vectors that are
  both pointer and datum, as against numbers (data) and symbols (names).

## Connections

The report puts SDM beside Anderson's and Kohonen's correlation-matrix
memories and beside Hopfield ([LIT-918](../literature.d/LIT-918.md)), whose net it compares only through
Keeler's capacity result and a citation; it gives no section to the
Hopfield model. It summarises Jaeckel, Hassoun, Prager and Fallside, Marr,
Albus, Keeler, Chou and the RIACS group's applications. The book
(Kanerva 1988, [LIT-928](../literature.d/LIT-928.md)) is cited for the full model. Bricken and Pehlevan
([LIT-269](../literature.d/LIT-269.md), read in [NOTE-242](NOTE-242.md)) cite this report as their ref. [15]; the anthology
holds it as [ANTH-LIT-669](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-669.md).

## Bearing on the record

- **[CLAIM-180](../claims.d/CLAIM-180.md) gains its missing half here.** The claim contrasts
  retrieval by content with retrieval by code, and Hopfield's model
  ([LIT-918](../literature.d/LIT-918.md)) has no addresses. This report has both ends in one machine: an
  SDM with radius zero and complete addresses is an ordinary RAM, which
  returns exactly what was written at an exact address and nothing for
  any other cue. Kanerva's own contrast (§§9–10) is the claim's: names are
  "ideal" encodings "except that [they are] arbitrary", while patterns are
  pointer and datum at once and need not be precise. The caution for the
  claim is the same passage: because a name is arbitrary, something else
  must map a cue to it. That is [QUESTION-038](../questions.d/QUESTION-038.md)'s point, and the report
  supports it.
- **The critical distance is not in this report.** [CLAIM-180](../claims.d/CLAIM-180.md) quotes the
  critical distance from [NOTE-242](NOTE-242.md). [NOTE-242](NOTE-242.md) records that Bricken and
  Pehlevan attribute the signal-to-noise optimum and the critical
  distance to this report. The signal-to-noise optimum is here
  (p = (2MT)^−1/3, §3.6). No critical-distance analysis is: the report
  shows iterated reads converging only in the examples of Figs. 2-1 and
  2-2. The critical distance belongs to the book ([LIT-928](../literature.d/LIT-928.md)).
- **[CLAIM-182](../claims.d/CLAIM-182.md)** (addressability makes an anchor) is consistent with the
  report but not argued by it; Kanerva treats exact addressing as the
  degenerate case, not as an advantage.
- **Filed from this reading:** [THEORY-261](../theory.d/THEORY-261.md), the signal-to-noise and
  capacity account under its stated conditions.
- **Anthology.** Held there as [ANTH-LIT-669](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-669.md) for its own question. The
  report carries no instruction for machine-learning practice.

## Limitations

- Every quantitative result assumes uniform random data and exact cues.
  The case that matters for associative recall, a noisy cue, is
  described qualitatively and deferred to Chou (1989).
- The derivation treats overlap sizes as independent Poisson variables;
  the author calls the result approximate and gives no error bound.
- The cerebellar correspondence is offered as "but an outline", with
  discrepancies at the level of cell morphology.
- Results attributed to Jaeckel, Hassoun, Keeler, Chou and others are
  reported, not reproduced.

## Open questions

- How capacity falls with cue noise, which the report leaves to Chou.
- Whether the optimum for clustered data can be had with uniform random
  hard addresses and an adapted activation rule (Kanerva 1991; Pohja and
  Kaski 1992), as §8 reports, and at what cost.
