---
status: Read
paper: 'LIT-tmpko4oy'
title: 'Zeng et al. — HOT multi-network alignment'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Read in full from the arXiv preprint 2310.04470v2 (margin stamp 10 Feb
    2024), 15 pp., the AAAI paper (pp. 1–7, references to p. 10) with
    appendices A–E (pp. 11–15). Extracted with `pdftotext -layout`; the
    two-column layout interleaved, so I read it line by line and rendered
    p. 6 as an image to read Figures 2–5, whose values are given only as
    plots. Read: abstract, §§1–7, Algorithms 1–3, the proofs of
    Propositions 1–3 and Theorem 1 (Appendix B), Appendix C (Figs. 8–10,
    Tables 1–2), Appendix D (Tables 3–4, datasets), Appendix E, and all
    captions. Pages are the PDF's. The AAAI proceedings version was not
    read. Checks, numpy, my own script, K = 3 graphs of 4 nodes: (1) the
    tensor form of Proposition 1 equals the direct Gromov–Wasserstein term
    summed over pairs j < k, and is half the sum over all ordered pairs, so
    Definition 2's "1 ≤ j, k ≤ K" must be read as j < k; (2) the MFGW
    objective at a joint coupling equals the sum of the pairwise FGW
    objectives at its two-way marginals, the identity behind Theorem 1; (3)
    condition C2 in the proof of Proposition 3 fails: near a random
    feasible S′, u(S, S′) − f(S) reached −3 × 10⁻⁶, against the claim that
    it is never negative.
date: '2026-10-29'
summary: >-
  Aligns K networks at once by one multi-marginal coupling tensor. The
  networks are first co-clustered through a fused Gromov–Wasserstein
  barycenter, then each cluster's nodes are aligned by multi-marginal
  fused GW with a cost from anchor-based random-walk embeddings, solved by
  a KL proximal point method. The joint objective at any tensor is the sum
  of the pairwise objectives at its marginals, so it bounds the sum of
  pairwise optima from above. On three-network benchmarks whose true
  correspondences are consistent by construction, it beats pairwise and
  multi-network baselines in pairwise and high-order hits; no experiment
  isolates the joint coupling from the new cost and the clustering.
---
<!-- inactive-ok-file: QUESTION-tmp6byb6 THEORY-tmpy1s8c THEORY-tmpz6ryi — Open, Proposed or new; the entries this reading bears on, cited as open -->

# NOTE-tmpf8vbq: Zeng et al. — HOT multi-network alignment

## Contribution

HOT poses multi-network alignment as one multi-marginal optimal transport
problem. It uses the multi-marginal fused Gromov–Wasserstein (MFGW)
distance of Beier, Beinert and Steidl 2022, whose optimal coupling tensor
S(v₁, …, v_K) is the alignment (Definition 2, pp. 2–3). To make the O(n^K)
tensor tractable it first co-clusters the K networks around an FGW
barycenter (§3.2) and aligns nodes only within aligned clusters (§3.3),
giving a block-diagonal tensor. The cross-network cost comes from random
walk with restart (RWR) scores relative to anchor node sets, shared
landmarks that put all networks in one space (§3.1).

## Key insight

A joint coupling cannot hold an inconsistent set of pairwise alignments,
because its pairwise alignments are its marginals. The price is plain in
Theorem 1 (p. 5): the joint objective is never less than the sum of the
pairwise optima, and it equals that sum only if the pairwise optima can be
chosen as marginals of one tensor. The paper reads the inequality as
"the joint distance between multiple networks is likely to be
underestimated by the pairwise FGW distance" (p. 5).

## Assumptions

- **Anchors.** A set of anchor node sets L, each naming one node per
  network known to correspond (Problem 1, p. 2). They define the RWR
  landmarks and therefore the whole cross-network cost (eq. 3, p. 3).
  Experiments use 10% of the true node sets as anchors (p. 5).
- **Square loss, q = 2**, throughout (p. 2), which gives the tensor form of
  Proposition 1.
- **Hard cluster assignments.** Each node goes to the barycenter node with
  the largest coupling (Algorithm 1, step 11, p. 11). Nodes in different
  clusters can never be aligned at node level.
- **Uniform measures** on each cluster (p. 3); M = ⌈n/50⌉ clusters (p. 5).
- **Fixed hyperparameters** λ = 10⁻³, α = 0.5, β = 0.15 (p. 5).
- **Ground truth is a consistent set of K-tuples.** Hits are scored
  against node sets {xᵢ} (p. 5). The ER benchmark makes each network "a
  permutation of the base network with noise added by first inserting 10%
  edges and then removing 15% edges" (p. 15). How the three DBLP and ACM
  networks were derived is not described beyond sampling connected
  subgraphs (p. 15).

## Key results

- **Proposition 1 (p. 3; proof p. 11):** with q = 2, MFGW is
  min over S of ⟨(1 − α)C + αL(S), S⟩ with L built from one-way and two-way
  marginals of S. I checked it numerically. The sums must run over j < k:
  the coefficient (K − 1) and the proof use j < k, while Definition 2 and
  eq. (4) print 1 ≤ j, k ≤ K, which would double both terms.
- **Proposition 2 (p. 4):** space O(M n̄^K), time O(TKM(n̄² + K n̄^K)), with
  n̄ = n/M. Still exponential in K, as Appendix E says (p. 15).
- **Proposition 3 (p. 4; proof p. 12):** the proximal point sequence
  "converges to a stationary point of the MFGW problem". The abstract and
  §4 say "local optimum". The proof applies the successive upper-bound
  minimization theorem of Razaviyayn et al. and needs u(S, S′) ≥ f(S) (C2).
  It argues: "For C2, since KL(S∥S (t) ) ≥ 0 and the equation holds when S
  = S (t) , we have u(S, S ′ ) ≥ f (S)" (p. 12). That ignores that u
  replaces the quadratic term ⟨L(S), S⟩ by its linearization ⟨L(S′), S⟩;
  the difference is first order in S − S′ while the KL term is second
  order, so C2 fails near any non-stationary S′. My check found it
  negative. The proposition may still hold by another argument; this proof
  does not establish it. Fig. 6 shows the objective non-increasing on one
  run.
- **Theorem 1 (p. 5; proof p. 12):** Σ over j < k of FGW(G_j, G_k) ≤
  MFGW(G₁, …, G_K). The proof writes the MFGW objective at S as the sum of
  pairwise FGW objectives at the marginals P_{j,k}(S), each at least the
  pairwise optimum. I checked the identity numerically.
- **Effectiveness (§5.1, pp. 5–6; Figs. 2–3, 8–9).** Against 13 baselines
  (Table 3, p. 14), HOT is reported to beat "the best competitor by at least
  12.0% on plain networks in terms of high-order Hits@10" (p. 1). Read off
  the plots (approximately): on ER-500, pairwise Hits@K near 99% and
  high-order near 80%; on Douban-230, high-order Hits@50 near 90% and MRR
  near 57%. No numbers are tabulated for the main benchmarks, so these are
  readings, not values.
- **Pairwise baselines (p. 5)** are combined into a tensor by multiplying
  their three alignment matrices, S(x, y, z) = S₁₂(x, y)S₁₃(x, z)S₂₃(y, z).
- **Larger graphs (Tables 1–2, p. 14):** DBLP up to 6000 nodes, high-order
  Hits@10 between 54.0 and 72.2 (plain) and 85.0 and 91.6 (attributed),
  with no baseline, since all dense baselines run out of memory.
- **Scalability (§5.2, p. 6):** up to 360× faster and 1000× less memory than
  the non-hierarchical solution as K grows, and baselines out of memory at
  K ≥ 5.
- **Hyperparameters (§5.4, p. 7; Fig. 10, p. 13):** stable in β; worse as
  α → 1; more clusters cost a little accuracy and save much time.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | With square loss, MFGW has the tensor form of Proposition 1 (sums over j < k) | strong | proof p. 11; checked numerically |
| C2 | The MFGW objective at S equals the sum of pairwise FGW objectives at its marginals, so MFGW ≥ Σ pairwise FGW | strong | proof p. 12; checked numerically |
| C3 | The proximal point method converges to a stationary point | weak | the proof's step C2 is invalid as written (p. 12); one convergence plot (Fig. 6) |
| C4 | Hierarchical decomposition reduces space and time from O(n^K) to O(M n̄^K) | strong for the count; moderate for the effect | Proposition 2; Figs. 4–5 |
| C5 | HOT aligns three networks better than pairwise and multi-network baselines, in pairwise and high-order hits | moderate | Figs. 2–3, 8–9, ten splits each; plots only; on consistent ground truth |
| C6 | The gain comes from aligning jointly rather than in pairs | weak | asserted (p. 6); no ablation that holds the RWR cost and the clustering fixed |

## Method

1. RWR scores of every node relative to each anchor set, concatenated with
   attributes where present (eq. 3, p. 3).
2. FGW barycenter of the K networks by block coordinate descent (eqs.
   8–10, p. 4); each node is assigned to its argmax barycenter node, giving
   M aligned clusters.
3. Within each cluster, a cost tensor of summed squared embedding distances
   (eq. 4) and MFGW solved by a KL proximal point method: each step is an
   entropic multi-marginal OT problem solved by Sinkhorn scaling (eqs.
   11–13, p. 4).
4. The alignment tensor is the block-diagonal assembly of the cluster
   tensors (Algorithm 3, p. 11).

## Concepts

- **Multi-network alignment** — finding node correspondence across K ≥ 3
  networks, scored on whole K-tuples (p. 1).
- **High-order hit** — a test node whose entire true node set appears among
  the top-K candidate tuples: "Only if the whole corresponded node set {xi}
  appears in the top-K most similar node sets, it is regarded as a
  high-order hit" (p. 5). A pairwise hit needs only one partner.
- **MFGW** — fused GW with one coupling tensor across K measures, its
  Wasserstein term on a K-way cost and its GW term summed over pairs
  (Definition 2, pp. 2–3).
- **Position-aware cost** — distances between RWR profiles relative to
  shared anchors (§3.1).

## Connections

It builds on fused GW (Vayer et al. 2019, cited as Titouan et al.; LIT-tmpjs7kp),
GW averaging (Peyré, Cuturi and Solomon 2016; LIT-tmpprsxm), S-GWL (Xu, Luo
and Carin 2019) for the cluster-then-match strategy, and the proximal
point GW of Xu et al. 2019. The multi-marginal GW it adopts is Beier,
Beinert and Steidl 2022. AvAtar (LIT-tmpe5bbx, read in NOTE-tmp60yfn) is
from the same group and cites it. The record's network GW is LIT-tmpu05fk.

## Bearing on the record

- **CLAIM-tmpgwud2 and QUESTION-tmp6byb6: the exchange's description is
  right in kind, and the paper does not run the test A6 wanted.** A joint
  coupling does impose consistency by construction, but only in a precise
  sense: the pairwise alignments are marginals of one tensor, so they are
  jointly realizable. For deterministic couplings that implies composition
  (the 1→3 map is the 2→3 map after the 1→2 map); for soft couplings it
  does not, since a marginal-realizable triple of soft couplings need not
  compose. The gap between MFGW and the sum of pairwise optima (Theorem 1)
  is then a natural measure of how far the best pairwise alignments are
  from joint realizability, a holonomy-like quantity the paper names but
  never reports. The comparison "on held-out data" that A6 proposed is
  partly here: test sets are 90% of the node sets, held out from the
  anchors, and both pairwise and high-order hits are reported. But the
  ground truth is a consistent set of K-tuples, in ER by construction
  (p. 15), so global consistency cannot lose a true local distinction on
  these benchmarks. That is the same limit as LIT-tmpr8qf7's benchmark,
  where the truth was built flat (THEORY-tmpy1s8c). And HOT changes the
  cost (RWR embeddings) and the search space (clustering) at the same
  time, so its margin over pairwise methods does not isolate consistency.
  The question whether consistency is a useful regularizer or a loss of
  local distinctions stays open; what would settle it is in
  THEORY-tmpz6ryi's promote_when.
- **CASE-tmph0fxi:** its correspondence arm fits each edge independently
  so that composed and direct maps can disagree. HOT is the opposite design
  and a natural comparison arm: a joint fit makes path discrepancy zero for
  deterministic couplings by construction, so in that arm path agreement
  would carry no information at all. That is CLAIM-tmpgwud2's point in
  algorithmic form.
- **The pairwise baselines' combination rule** (product of three pairwise
  matrices, p. 5) scores a triple by its pairwise support and never tests
  composition. It is not the "independently fitted pairwise alignments"
  comparison the record wants.
- **No instruction for machine-learning practice.** The parameter settings
  are the paper's own.

## Limitations

- No ablation separates the joint coupling from the RWR cost and the
  clustering; C6 rests on assertion.
- Results are plots, without tables, for the main benchmarks; standard
  deviations are shaded in the plots.
- Ground truth is consistent by construction; no benchmark has
  non-transitive true correspondences.
- Errors in hard cluster assignment cannot be repaired at node level
  (Appendix C, p. 13).
- The convergence proof is flawed at C2 (above), and "local optimum"
  (abstract) overstates "stationary point" (Proposition 3).
- Table 4 (p. 14) gives ACM(A)-500 the same edge counts as ER, 1813, 2160
  and 1982, which looks like a copying error. Appendix D says code will be
  released "after the paper is published" (p. 15), while p. 5 gives a
  repository.
- Still exponential in K (Appendix E, p. 15); experiments mostly use K = 3.

## Open questions

- On networks whose true correspondences are not transitive, such as
  translations through intermediate languages or role mappings across
  reorganized units, does joint alignment lose accuracy on the pairs it
  forces into agreement?
- Does the gap MFGW − Σ pairwise FGW, computed on real data, predict where
  pairwise alignments compose badly?
- Does the method converge under a correct argument, for instance by
  bounding the linearization error with the KL term at large λ?
