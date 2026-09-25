---
number: 23
status: Read
formerly:
- NOTE-tmpt8n2t
paper: LIT-002
title: 'Nested Hierarchical Dirichlet Processes'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (full text of arXiv 1210.6738v4 (2 May 2014), 15 pp. —
    §§1–6, Algorithms 1–2, Tables 1–2, Figs. 1–14 (Figs. 2–4, 7–9 and 12–14
    rendered and read off), references and author bios; nothing skipped. For
    the Wikipedia-count question I also pulled v1 (25 Oct 2012, a 26-pp.
    double-spaced "DRAFT") and v3 (9 Oct 2013) and searched them for the
    corpus description, setup and update equations. I read only those parts
    of v1 and v3, not the whole. I did not read the published TPAMI version
    (vol. 37, pp. 256–270), so whether it matches v4 word for word is
    unverified.). Upgraded from `Skimmed` to `Read`: the claims table,
    assumptions and results are new, and the skim is corrected where the
    full text disagreed.
date: '2026-09-25'
summary: >-
  The nHDP gives each document its own DP over the children of every node
  of a shared global nCRP tree (G_i^(d) ~ DP(βG_i)), plus a per-node
  stop/continue switch U_{d,i} ~ Beta(γ1, γ2). Each word then takes its
  own path, and β → 0 recovers the single-path nCRP. The paper fits this
  with SVI plus a greedy per-document subtree selection. On small corpora
  the variational nHDP beats variational nCRP on all three datasets and
  Gibbs nCRP on two of three (PNAS −6.304 vs −6.496/−6.574 held-out
  log-likelihood). On 1.8M NYT and 2.7M Wikipedia documents it tops
  stochastic HDP and LDA-50/150/250 by roughly 0.08 and 0.11 nats (read
  off Figs. 2, 7), using ≈12 and ≈8 topics per document.
---


# NOTE-023: Nested Hierarchical Dirichlet Processes

## Contribution

The paper defines the nested hierarchical Dirichlet process. A global nCRP tree T (a stick-breaking DP G_i at every node) serves as the base measure for per-document trees T_d. Each document draws G_i^(d) ~ DP(βG_i) independently at every node, so all documents share one set of nodes and topics but each has its own transition probabilities (§3.1, Eq. 8). A per-document, per-node beta switch decides where a word stops (§3.2, Eq. 10). Before this, the nCRP restricted every document to a single root-to-leaf path. The paper derives a stochastic variational inference algorithm for the model and uses it to fit three-level trees to about 2 million documents on one desktop machine, one pass taking ≈20 hours (§5.3.2).

## Key insight

The nCRP clusters *documents* into paths. Letting each *word* take its own path under a single corpus-wide nCRP would give every document the same path distribution. The HDP solves exactly this problem one level down: a global DP supplies the atoms and per-group DPs reweight them. Applying the HDP node by node to the tree's DPs gives each document a distribution over the whole tree that is concentrated on a subtree when β is small, not confined to a single path. The single path returns in the limit β → 0 (§2.2.3, §3.1).

## Assumptions

- **Data model:** bag-of-words documents. Topics are θ_i ~ Dirichlet(λ0·1_V), and words are drawn i.i.d. given their topic (§2.2.2).
- **Prior structure:** the global tree uses G_i = Σ_j V_{i,j} Π_{m<j}(1 − V_{i,m}) δ_{θ(i,j)}, with V_{i,j} ~ Beta(1, α) and θ ~ G0 (Eq. 4). Each document draws G_i^(d) ~ DP(βG_i) at every node, represented as G_i^(d) = Σ_j V^(d)_{i,j} Π_{m<j}(1 − V^(d)_{i,m}) δ_{φ^(d)_{i,j}}, with V^(d) ~ Beta(1, β) and φ^(d) ~ G_i i.i.d. (Eq. 9). The switches are U_{d,i} ~ Beta(γ1, γ2) (Eq. 10).
- **Variational family (Table 1):** mean-field.
  - Global: q(θ_i) = Dirichlet(λ_i) and q(V_{i,j}) = Beta(τ^(1), τ^(2)).
  - Local: q(V^(d)_{i,j}) = Beta(u, v), q(U_{d,i}) = Beta(a, b) and q(c_{d,n}) = Discrete(ν_{d,n}).
  - The pointer z^(d)_{i,j} (which global atom the jth local break points to) gets a **delta** q, a hard assignment.
  - Every DP is truncated. Large-scale runs use (20, 10, 5) children per level, 1,220 nodes. Batch runs use (10, 7, 5) plus a shared root.
- **Greedy subtree restriction:** each document may place words only in a subtree chosen greedily (§4.2.1). ν_{d,n}(i) is fixed at 0 outside it, and no global atom is duplicated within a document's DP. This restricts the variational family; it is not the model's own structure.
- **Depth in practice:** the model is described as nonparametric in depth, but every experiment truncates at three levels (§5, "we are more interested in the nonparametric aspect of the Dirichlet process here"). The motivation in §1 and §2.2.3 about deep nCRP trees having "too many nodes to infer" is never tested at greater depth.
- **SVI convergence:** the step size must satisfy Σρ_s = ∞ and Σρ_s² < ∞ (§4.1.2, citing Sato [20]). The v4 experiments instead use an adaptive step size [29], and the paper does not say whether that schedule meets the condition.

## Key results

- **Recovery of the nCRP (§3.1, informal argument):** as β → 0, each G_i^(d) becomes a point mass on one φ ~ G_i, every word in a document follows the same path, "thus recovering the nCRP".
- **Word-topic prior (Eq. 11):** Pr(φ_{d,n} = θ_{i_l} | T_d, U_d) = [Π_{m=0}^{l−1} G^(d)_{i_m}({θ_{i_{m+1}}})] · [U_{d,i_l} Π_{m=1}^{l−1}(1 − U_{d,i_m})]. The first bracket is the probability of the path; the second is the probability of stopping at level l. The switches U are per *node* and shared by every path through that node ("overlapping" stick-breaking).
- **Unbiased stochastic objective (§4.1.2, short proof in text):** L_s = (D/|C_s|) Σ_{d∈C_s} E_Q[ln P(W_d, φ_d | Φ_W)] + E_Q[ln P(Φ_W) − ln Q] (Eq. 14). With C_s uniform over subsets of size |C_s|, each d lies in (D−1 choose |C_s|−1) of the (D choose |C_s|) subsets, so E_{p(C_s)}[L_s] = L.
- **Natural-gradient step (Eqs. 13, 15):** in a conjugate-exponential model, ∇_ψ L = −[∂² ln f / ∂ψ∂ψᵀ] · [χ + Σ_d t(W_d) − χ′ ; ν + D − ν′] (Eq. 13). Preconditioning with B = (−∂² ln q(η|ψ)/∂ψ∂ψᵀ)^{−1}, the inverse Fisher information of q (Eq. 15), cancels the matrix. The update ψ_s = ψ_{s−1} + ρ_s B ∇_ψ L_s then reduces to a convex combination of old and new sufficient statistics. The algebra checks, taking ψ as q's natural parameter so that ln q is linear in ψ and its Hessian equals that of ln f.
- **Printed global updates are inconsistent with this derivation.** Carried through, §4.1.2 gives λ^{s+1} = (1 − ρ_s)λ^s + ρ_s(λ0 + λ′). Eq. 23 prints λ^{s+1} = λ0 + (1 − ρ_s)λ^s + ρ_s λ′, which adds the full prior λ0 at *every* step. Its fixed point is λ′ + λ0/ρ_s, which diverges as ρ_s → 0. Eqs. 26–27 have the same form, with 1 and α outside the combination. The same equation appears in v1 (Eq. 23 there). The text of §4.2.3 ("a blending of the old statistics with the new") describes the correct form, so this is most likely typographical. Whether the code did it correctly is unverified.
- **Batch comparison (Table 2; five-fold CV; the ± quantity and the per-word normalization are not stated):**

  | method | JACM (536 docs, V=1,539, 45 w/doc) | Psych. Review (1,272, 1,971, 108) | PNAS (5,000, 7,762, 179) |
  |---|---|---|---|
  | variational nHDP | −5.405 ± 0.012 | **−5.674 ± 0.019** | **−6.304 ± 0.003** |
  | variational nCRP [2] | −5.433 ± 0.010 | −5.843 ± 0.015 | −6.574 ± 0.005 |
  | Gibbs nCRP [2] | **−5.392 ± 0.005** | −5.783 ± 0.015 | −6.496 ± 0.007 |

- **Large scale (Figs. 2, 7; values read off the plots):**
  - NYT, final values: nHDP ≈ −7.245, HDP ≈ −7.32, LDA-250 ≈ −7.355, LDA-150 ≈ −7.42, LDA-50 ≈ −7.57.
  - Wikipedia: nHDP ≈ −6.51, HDP ≈ −6.62, LDA-250 ≈ −6.65, LDA-150 ≈ −6.695, LDA-50 ≈ −6.855.
  - The nHDP leads from the first evaluation onward.
  - The metric is the average predictive log-likelihood of the held-out 10% of each test document, after fitting local parameters on the other 90% (14,268 NYT and 8,704 Wikipedia test documents).
- **Tree use (Figs. 3, 4, 8, 9, read off):**
  - Of 1,220 initial nodes, ≈255 / 415 / 565 hold 95 / 99 / 99.9% of the posterior mass on NYT, and ≈205 / 318 / 425 on Wikipedia.
  - Topics per document with more than one expected word, by level: NYT ≈ 3.8 / 5.5 / 2.8 (≈12, as the text says); Wikipedia ≈ 2.8 / 3.4 / 1.8 (≈8; the text gives no number for Wikipedia).
- **Sensitivity (Fig. 14, Wikipedia only):** the predictive log-likelihood moves by ≈0.013 over γ1 ∈ [0.1, 0.5] (with γ2 = 1 − γ1) and by ≈0.003 over β ∈ [0.25, 1]. That is an order of magnitude below the nHDP–HDP gap. The best values in the sweep (γ1 = 0.5, β = 0.75) are not the defaults used (1/3, 1).
- **Cost:** ≈20 hours for one pass through NYT on a single desktop, "sufficient for the model to converge"; Wikipedia "comparable" (§5.3.2). No runtimes are given for the baselines.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The nHDP lets each word follow its own path through a shared tree with document-specific path probabilities | strong | Construction, Eqs. 8–11 (a definition) |
| C2 | The nCRP is the β → 0 limit of the nHDP | moderate | Informal limiting argument, §3.1; no formal statement |
| C3 | The subsampled objective is unbiased: E[L_s] = L | strong | Counting argument, §4.1.2 |
| C4 | For conjugate-exponential q, preconditioning by the inverse Fisher information turns the stochastic gradient step into a convex blend of sufficient statistics | strong | Derivation, Eqs. 13–15; standard (Hoffman et al. [8], Sato [20]) |
| C5 | The global updates are λ^{s+1} = λ0 + (1−ρ)λ^s + ρλ′, and likewise for τ | weak | Eqs. 23, 26–27 as printed contradict the derivation in C4; almost certainly a typographical error |
| C6 | Greedy subtree selection is a valid part of variational inference, since it maximizes a fixed objective | moderate | Informal argument, §4.2 (a restricted q still gives a lower bound). There is no guarantee the greedy subtree is optimal, and the effect of the restriction on the bound is not measured |
| C7 | Variational nHDP beats variational nCRP on JACM, Psych. Review and PNAS, and beats Gibbs nCRP on the latter two | moderate | Table 2, five-fold CV, one run per fold; the error-bar definition is not stated |
| C8 | "The benefit … appears to increase as the corpus size and document size increase", which "strongly hints" at an advantage in the Big Data regime | weak | Three corpora differing in size, document length, vocabulary and field at once. The nCRP is never run at large scale |
| C9 | Stochastic nHDP achieves higher held-out predictive log-likelihood than stochastic HDP and LDA (50/150/250) on NYT (1.8M) and Wikipedia (2.7M) | moderate | Figs. 2, 7; one run each, no error bars; baseline truncation and initialization not stated |
| C10 | Documents use ≈12 topics (NYT) against the 3 an nCRP path would allow, a "clear advantage" of access to the whole tree | weak as evidence of advantage; moderate as a statistic | Fig. 4 measures use of the tree, not quality; there is no nCRP comparison at this scale |
| C11 | The model learns "meaningful" hierarchies (sports → sport → team; foreign affairs → region → issue) | weak | Hand-picked qualitative trees (Figs. 6, 11); no human or quantitative evaluation of the hierarchy |
| C12 | Results are insensitive to λ0 and α, and fairly robust to β and (γ1, γ2) | weak (λ0, α); moderate (β, γ) | λ0 and α are assertion only; β and γ rest on Figs. 12–14, Wikipedia only |
| C13 | The algorithm scales to millions of documents: ≈20 h per pass on one desktop | moderate | Reported runtime (§5.3.2); single machine, no comparison of wall-clock time against the baselines |

## Method

**Generative model (Algorithm 1):** (1) Draw the global tree T by nCRP stick-breaking (Eq. 4). (2) For each document d, draw G_i^(d) ~ DP(βG_i) at every node (Eq. 8) and U_{d,i} ~ Beta(γ1, γ2) at every node (Eq. 10). (3) For each word: start at the root. At node i, stop with probability U_{d,i}; otherwise move to a child drawn from G_i^(d). Emit the word from the topic where it stops (Eq. 11). Because the atoms φ^(d) of Eq. 9 are drawn from the discrete G_i, they can repeat. The mass on a global node is G_i^(d)({θ(i,j)}) = Σ_m G_i^(d)({φ^(d)_{i,m}}) · I(φ^(d)_{i,m} = θ(i,j)).

**SVI (Algorithm 2), per mini-batch C_s:**

1. **Greedy subtree (§4.2.1, Eq. 16).**
   - Start from an empty subtree; every child of the root is a candidate. The candidates S_{d,t} are the nodes not yet in the subtree whose parents are in it.
   - Add i* = argmax_{i′∈S_{d,t}} Σ_n max_{ν_{d,n}} (E_q[ln p(W_{d,n} | c, θ)] + E_q[ln p(c_{d,n}, z^(d) | V, V_d, U)] − E_q[ln q(c_{d,n})]).
   - While scoring, the local beta q's are fixed at their priors and ν is zero outside I_{d,t} ∪ {i′}. This makes each score closed-form.
   - Stop when the marginal gain falls below 10^−3 (§5.3.1).
   - Selecting a node sets the hard pointer z^(d)_{i,j}: the next local break at the parent points to that global atom. The subtree is therefore a truncated, reordered, duplicate-free stick-breaking representation of each G_i^(d).
   - A candidate's prior changes with its position: it depends on whether it would fill break j or j′ at its parent, so adding a sibling changes the prior on the remaining candidates.
2. **Local coordinate ascent on the subtree (§4.2.2).** Iterate until the fractional change in the L1 distance of the empirical word distribution falls below 10^−2.
   - **Eq. 17:** ν_{d,n}(i) ∝ exp(E_q[ln θ_{i,W_{d,n}}] + E_q[ln π_{d,i}]). Here π_{d,i} (Eq. 18) is the product of the local stick weights along the path, selected by z, times U_{d,i} Π_{i′⊂i}(1 − U_{d,i′}). E[ln θ_{i,w}] = ψ(λ_{i,w}) − ψ(Σ_w λ_{i,w}), and E[ln Y] = ψ(a) − ψ(a+b) and E[ln(1−Y)] = ψ(b) − ψ(a+b) for Y ~ Beta(a, b).
   - **Eq. 19:** u^(d)_{i,j} = 1 + (expected words passing through or stopping at the node that break (i,j) points to). v^(d)_{i,j} = β + (expected words through parent i that go on to nodes pointed to by breaks m > j).
   - **Eqs. 20–21:** a_{d,i} = γ1 + Σ_n ν_{d,n}(i), the words that stop at i. b_{d,i} = γ2 + Σ_{i′: i⊂i′} Σ_n ν_{d,n}(i′), the words that pass through i without stopping.
3. **Global natural-gradient step (§4.2.3).**
   - **Topics.** Eq. 22 forms λ′_{i,w} = (D/|C_s|) Σ_{d∈C_s} Σ_n ν_{d,n}(i) I{W_{d,n} = w}. Eq. 23 blends it into λ_i (see Key results for the printed-form error).
   - **Global sticks.** Eq. 24 counts documents whose subtree contains the node: τ′ = (D/|C_s|) Σ_d I{node ∈ I_d}. Eq. 25 counts documents that use a sibling of higher index. Eqs. 26–27 give the updates, with prior 1 on τ^(1) and α on τ^(2).
   - These are *document counts from hard subtree membership*, the analogue of the HDP's table counts with exactly one "table" per used atom per document.
   - The notation in Eqs. 24–25 is loose: the left side is indexed by (i_l, j), the right side by i_l, and the sum in Eq. 25 is written "Σ_{j>i_l}".
4. **Step size and initialization.** Step size: Ranganath et al.'s adaptive ρ_s (Figs. 5, 10). Initialization (§5.1):
   - Run hierarchical k-means (L1 distance) on the empirical word distributions of about 10,000 documents. At each level, subtract the cluster mean, clip at zero, renormalize and recurse.
   - Set λ_i = N(κλ̂_i + (1 − κ)(1/V + v_i)), with v_i ~ Dirichlet(100·1_V/V), κ = 0.5 and N = the number of documents.

**Large-scale hyperparameters (§5.3.1):** α = 5, β = 1, γ1 = 1/3, γ2 = 2/3, λ0 = 0.1. Stop words and rare words are removed, and no root topic is used. Vocabularies: NYT 8,000, averaging 254 words per document; Wikipedia 7,702, averaging 164 words per document.

## Concepts

- **Global tree T** — the nCRP in stick-breaking form: an infinite collection of DPs G_i, one per node, whose atoms are that node's children's topics.
- **Document tree T_d** — the same nodes as T, with transition DPs G_i^(d) ~ DP(βG_i). The nodes are shared; the path probabilities are the document's own.
- **Stochastic switch U_{d,i}** — the per-document, per-node probability that a word reaching node i stops there.
- **Activated node** — a node not in the document's current subtree whose parent is in it; the candidate set S_{d,t} for the greedy step.
- **z^(d)_{i,j}** — the pointer from the jth break of the document DP at node i to an atom of the global G_i, given a delta q. The set of pointers defines the document's subtree.
- **Word-specific vs. document-specific path clustering** — the paper's framing of what separates the nHDP from the nCRP (§1).
- **Predictive log-likelihood (as used here)** — hold the global parameters fixed, fit the local q on 90% of a test document's words, and score the other 10% under the means of the q distributions [28][2].

## Connections

- **Built on:** the nCRP (Blei, Griffiths & Jordan [1][4]) and its variational treatment (Wang & Blei [2]), which supply the stick-breaking tree and the batch baselines. The HDP (Teh et al. [5]) supplies the global-to-local mechanism. SVI (Hoffman et al. [8]) and its online predecessors for LDA [9] and the HDP [10] supply the inference template, which this paper extends from a flat HDP to a tree. The tree-structured stick-breaking of Adams, Ghahramani & Jordan [19] is named as the closest prior in form. There, all groups share one tree distribution and whole objects cluster at a node.
- **Lim, Buntine, Chen & Du, the hierarchical Pitman–Yor topic model ([LIT-013](../literature.d/LIT-013.md)).** What the two texts support is limited:
  - Neither paper cites the other. Lim et al. (arXiv 1609.06783v1) cites the nCRP JACM paper only for the Chinese-restaurant metaphor. It cites SVI (Hoffman et al. 2013) and online HDP (Wang, Paisley & Blei 2011) among variational HDP methods, which it says the collapsed blocked Gibbs sampler of Chen et al. (2011) "has been shown to generally outperform".
  - Both generalize HDP-LDA, in different directions. The nHDP arranges DP-distributed topics in a tree and keeps α, β as DP concentrations with no discount. Lim et al. keep a flat topic layer, replace DPs with Pitman–Yor processes (discounts for power-law behaviour) and attach auxiliary data.
  - They make opposite inference choices: truncated mean-field SVI with hard subtree pointers here, collapsed blocked Gibbs with table counts there. The contrast is real, but neither paper tests the other's choice. No comparison between the two exists in either text.
- The only anthology document the search turned up that touches natural gradients ([ANTH-LIT-476](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-476.md), on basin volume) is unrelated. The anthology holds no LIT for SVI or the HDP.

## Bearing on the record

- This is the reading of [LIT-002](../literature.d/LIT-002.md). It supports promoting [LIT-002](../literature.d/LIT-002.md) from `Deferred` to `Active` on merit, with the Eq. 23/26–27 caveat recorded on the LIT. [LIT-002](../literature.d/LIT-002.md)'s lineage could declare `extends:` the nCRP and HDP papers and `compared_against:` variational/Gibbs nCRP and stochastic LDA/HDP, if those works are ever filed. None of them is in the record now.
- No THEORY document in the nucleation record bears on it, as checked by search; it neither supports nor contradicts any.
- **ML practice:** nothing current. The transferable content is the SVI template: split local from global, optimize local parameters per mini-batch, then take a natural-gradient step that reduces to a ρ-weighted blend of sufficient statistics. That template belongs to Hoffman et al. (2013), which the anthology does not hold, and this paper is not its best source. If the anthology ever files SVI, this paper is at most a secondary worked example. It should not be cited for the update equations as printed.

## Limitations

- **No large-scale nCRP baseline.** Every large-scale comparison is against *flat* models (LDA, HDP). The central claim that multiple paths beat a single path rests at scale on topics-per-document counts (C10) and qualitative trees (C11). Head-to-head evidence covers only three corpora of at most 5,000 abstracts, and on the smallest one Gibbs nCRP wins (Table 2).
- **Confounded comparisons.** The nHDP has up to 1,220 topics, while LDA has at most 250 and the HDP's truncation is not stated. Only the nHDP gets a hierarchical k-means initialization, and the paper itself says initialization "can benefit greatly" (§5.1). Each curve is one run, with no error bars.
- **Evaluation.** The measure is held-out likelihood under q means, not a bound or an estimate of the true marginal. Hierarchy quality gets no human evaluation and no quantitative evaluation.
- **Printed update equations are wrong as stated** (Eqs. 23, 26–27). There are also smaller slips: "Table 2" for Table 1, 420 for 430 nodes, and the Fig. 14 caption.
- **Heuristic parts of the inference.** The greedy subtree scores candidates with the local betas held at their priors. The hard pointers z make the global-stick statistics document counts. With a subtree chosen this way, the stochastic step is not the exact natural gradient of the collapsed-over-local bound, since local parameters are only approximately optimized. The paper does not measure how much bound this gives up.
- **Depth untested.** Every experiment uses three levels, the same depth the paper criticizes the nCRP for being limited to.
- **Reproducibility gaps in v4.** The mini-batch size is not stated, and neither is the adaptive-step configuration. v1 gave |C_s| = 5000 and ρ_s = (1+s)^−0.75, but those settings belong to the superseded experiments.
- The authors state no limitations of their own. The conclusion only restates the contributions.

## Open questions

- Does the multi-path advantage survive a large-scale comparison with a stochastic-variational nCRP, with matched truncation and initialization? Such a comparison would settle C8 and C10.
- How much of the gain over the HDP comes from the tree prior, and how much from greater capacity and the k-means initialization? An HDP with 1,220-atom truncation and the same initialization would answer this.
- What does the greedy subtree restriction cost in bound, measured against a soft or exhaustive local optimization on small corpora?
- Does the model use depth when it is allowed more than three levels? The paper claims the nHDP is nonparametric in depth but never exercises it.
- Was Eq. 23 implemented as printed or as derived? The released code, if any, would show. Its location is not given in the paper.

## Corrections to the seeded skim

- **3.3M vs 2.7M Wikipedia documents, resolved.** v1 (Oct 2012) says 3.3 million in every place: the abstract, §1, §5 and §5.C ("Wikipedia roughly 3.3 million web pages"). v3 (Oct 2013) and v4 (May 2014) say 2.7 million in every place: the abstract, §1, §5 and §5.3. The arXiv listing abstract is v1's abstract, never updated. It still says 3.3 million, and it still has the v1-only sentence about "a greedy subtree selection method", which the v3/v4 abstract dropped (the method itself stays, in §4.2.1). So the dossier's choice of 2.7M is right, and 2.7M is the paper's own figure. The x-axis of Fig. 7 ends at ≈2.7 × 10^6 documents seen, which agrees. The text never explains the change. Every other corpus figure is identical across versions: 164 words per document, vocabulary 7,702, 8,704 test documents. The experiments did change between v1 and v4 (next bullet), so the 3.3M figure belongs to a superseded draft and should not be cited.
- **The dossier treats the experiments as fixed; they changed between versions.** v1 used γ1 = 2/3, γ2 = 4/3, a 75/25 test split, mini-batch |C_s| = 5000, step size ρ_s = (1+s)^−0.75, stopping thresholds of 10^−2 and 10^−1, and LDA-50/100/150 baselines on Wikipedia. It reported "roughly eight topics" per NYT document. v4 uses γ1 = 1/3, γ2 = 2/3, a 90/10 split, the adaptive step size of Ranganath et al. [29], thresholds of 10^−3 and 10^−2, and LDA-50/150/250. It reports "roughly 12". **v4 never states its mini-batch size.** The batch comparison (Table 2) is numerically identical in v1 and v4.
- The dossier asks "how much of the large-scale gain is due to the model versus the inference method". The text settles half of this. At large scale nHDP, HDP and LDA all run SVI with the same adaptive step size and the same evaluation (§5.3.1), so the inference method is held roughly fixed. The comparisons still differ in truncation/capacity (nHDP starts from 1,220 topics; the HDP truncation is not stated) and in initialization: hierarchical k-means for the nHDP (§5.1), unstated for the baselines. The other half: **the nCRP is not run at large scale at all.** The "advantage over nCRP" there is argued from about 12 topics used per document against the 3 the nCRP would allow (§5.3.2, Fig. 4). It is not measured.
- The dossier cites Figs. 12–14 as "sensitivity to hyperparameters". They cover only β and (γ1, γ2), and only on Wikipedia. The insensitivity to λ0 and α is asserted in the text with no figure (§5.3.4).
- Internal errors the dossier did not catch:
  - §4.2 twice points to "Table 2" for the list of variables and q distributions. That list is Table 1; Table 2 is the batch results.
  - §5.2 says a (10, 7, 5) tree has "a total of 420 nodes". 10 + 70 + 350 = 430 (431 with the shared root). The (20, 10, 5) count of 1,220 in §5.3.1 is correct.
  - The Fig. 14 caption reads "(γ1, γ2 = 1 − γ2)"; it should be 1 − γ1.
  - The most consequential: Eqs. 23, 26 and 27 (see Key results and Method).
