---
number: 8
status: Read
formerly:
- NOTE-tmp9ca8a
paper: LIT-013
title: 'Hierarchical Pitman-Yor topic models'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (full text of arXiv 1609.06783v1 (22 Sep 2016; header
    "Preprint for Int. J. Approximate Reasoning 78 (2016) 172–191, Submitted
    31 Jan 2016; Published 18 Jul 2016"), 41 pp. Read: §§1–6, Algorithms
    1–4, Tables 1–7, Figs. 1–4, Appendix A.1–A.5, and the reference list.
    Nothing was skipped. Eqs. 16, 53 and 82–84 were checked against the
    rendered page images. I did not read the published IJAR version, so
    whether it matches v1 word for word is unverified.). Upgraded from
    `Skimmed` to `Read`: the claims table, assumptions and results are new,
    and the skim is corrected where the full text disagreed.
date: '2026-09-25'
summary: >-
  The paper collapses every Pitman–Yor node to customer and table counts
  (Eq. 16, following Chen et al. 2011), which turns any HPYP topic model's
  posterior into a product of per-node factors, and it samples topics and
  counts jointly by decrement/propose/increment. The HPYP half of its
  Twitter-Network Topic Model uses this sampler; the network half is fit
  by a separate MH step. On one 240,517-tweet, 150-author corpus (T6) the
  TNTM reaches test perplexity 505.01 ± 7.8, against 664.25 ± 17.76 for a
  nonparametric ATM and 840.03 ± 15.7 for HDP-LDA, and network
  log-likelihood −500.63 against −557.86 for the random-function network
  model alone (Table 4). Removing the power-law discounts barely changes
  perplexity (508.64) but costs network likelihood (−560.28; Table 5).
---

# NOTE-008: Hierarchical Pitman-Yor topic models

## Contribution

The paper sets out, in one place and with a worked example, how to build and fit topic models whose probability vectors are all Pitman–Yor processes arranged in a DAG. Each PYP is integrated out and replaced by per-dish customer counts c_k and table counts t_k. That makes the joint posterior a product of per-node factors f(N) (Eq. 16) times a base-measure term (Eq. 19). Then one generic loop is used: decrement counts with a Bernoulli table indicator, block-sample the topic together with the count increments, increment. Models are thus assembled from reusable "blocks" (§3, §4, §6). This is an extension of Chen et al. (2011), not a new sampler; the base HPYP topic model is "a variant of those presented in Buntine and Mishra (2014)" (§3.1). What is new:
- the extension of the count posterior to a discrete base (the last factor in Eq. 19);
- a two-state table-removal indicator in place of Chen et al.'s restaurant indicator (§4.1);
- a multiple-parent extension, following Du et al. (2012a) (§5.3, A.1, A.3);
- the Twitter-Network Topic Model (TNTM), which extends the authors' 2013 NIPS-workshop paper (footnote 2).

## Key insight

Under the table-count representation, a PYP node's contribution to the collapsed posterior depends only on its own counts:

f(N) = (β|α)_T / (β)_C · Π_k S^{c_k}_{t_k,α} · (c_k choose t_k)^{−1}.

Adding one word changes each count by at most 1 (Table 2). Each step of the sampler is therefore a ratio of Pochhammer symbols, which reduces to x + T or x + yT (Eq. 25), times a cached Stirling-number ratio. The seating arrangement never has to be stored; it is resampled on removal through P(u = 1) = t_k/c_k (Eq. 21). That is why a deep, multi-parent PYP network costs no more to implement than LDA.

## Assumptions

- **Model class.** Every probability vector is a PYP (or GEM at a root) over a discrete space. Children use their parent as the base, or a fixed mixture of parents ρ_1P_1 + … + ρ_PP_P with ρ ~ Dirichlet(λ) (Eqs. 7, 74–75). Data are bags of tokens per document; hashtags share the word vocabulary (§5.2.1).
- **PYP parameters.** 0 ≤ α < 1 and β > −α (Eq. 1). The discounts α are **fixed**: they are not learned, "due to their coupling with the Stirling numbers cache" (§4.3). Concentrations β get a Gamma(τ0, τ1) hyperprior and are sampled with an auxiliary-variable scheme (Eqs. 26–29).
- **Root of the vocabulary side.** H_γ is discrete uniform over the vocabulary, chosen so unseen words get a small probability (§3.1).
- **Test-time estimation (§4.5.1).**
  - The trained counts are frozen.
  - Topics for the test documents' words are sampled sequentially from θ_dk φ_kw (Eq. 36).
  - The test document's table counts are set to half its customer counts rather than sampled.
  - New topics are disallowed.
  - The result is averaged over R runs (Eq. 37).
  The paper says "the estimated variables are unbiased" (§4.5.1). That is asserted without argument, and it is doubtful given the halved table counts.
- **Network model (§5.2.2).**
  - x_ij ~ Bernoulli(s(Q_ij)) for all ordered author pairs, including i = j (Eq. 59).
  - Q ~ GP with mean Sim(ν_i, ν_j) (cosine similarity).
  - The covariance is a squared-exponential in the *difference of similarities* plus a σ² nugget (Eq. 62).
  - The GP is over A² pair-values; with A = 150 authors that is 22,500. The paper states no scaling consideration, but it is consistent with filtering the corpus to 150 authors (§5.5).
- **Setting of the experiments.**
  - T6: tweets queried by six hashtags; authors outside the Kwak et al. (2010) follower graph are removed, as are authors with fewer than 50 tweets.
  - Words per tweet: 6.35. Hashtags per tweet: 1.34. Vocabulary: 5,343 (Table 3).
  - The goodness-of-fit and ablation results rest on this one corpus. Its hashtag density is an artefact of how it was queried (Table 3 caption).

## Key results

- **Modular posterior (Eq. 19; stated as a generalization of Chen et al. 2011, Theorem 1).** p(Z, T, C | W, Ξ) ∝ f(µ) f(ν) Π_d f(θ_d) Π_k f(φ_k) f(γ) Π_v (1/|V|)^{t^γ_v}. The proof is deferred to Chen et al.; the paper gives no derivation.
- **Posterior-mean reconstruction (Eq. 34).** E[N_k | …] = ((α_N T_N + β_N) E[P_k | …] + c_k^N − α_N t_k^N) / (β_N + C_N), applied recursively from the root. The multiple-parent form (Eqs. 76–78) replaces E[P_k] with Σ_i ρ̂_i E[P_ik], where ρ̂_i = (T^{N→P_i} + λ_i)/(T_N + Σλ).
- **Concentration sampling (Eqs. 27–29).** ω ~ Beta(C_N, β_N); ζ_i ~ Bernoulli(β/(β + iα)) for i = 0 … T_N − 1; then β ~ Gamma(τ0 + Σζ_i, τ1 − log(1 − ω)). I checked this against f(N): 1/(β)_C integrates to an auxiliary variable on 1 − ω ~ Beta(β, C), and each factor (β + iα) of (β|α)_T gives a Bernoulli split. It is correct. ζ_0 = 1 deterministically.
- **Goodness of fit (Table 4; T6; five runs; the ± quantity is not defined).**

  | model | test perplexity | network log-likelihood |
  |---|---|---|
  | HDP-LDA | 840.03 ± 15.7 | — |
  | nonparametric ATM | 664.25 ± 17.76 | — |
  | random-function network model | — | −557.86 ± 11.2 |
  | TNTM | **505.01 ± 7.8** | **−500.63 ± 13.6** |

- **Ablation (Table 5).**

  | variant | perplexity | network LL |
  |---|---|---|
  | no author | 669.12 ± 9.3 | — |
  | no hashtag | 1017.23 ± 27.5 | −522.83 ± 17.7 |
  | no µ1 | 607.70 ± 10.7 | −508.59 ± 9.8 |
  | no θ′–θ link | 551.78 ± 16.0 | −509.21 ± 18.7 |
  | no power-law | 508.64 ± 7.1 | −560.28 ± 30.7 |
  | full | 505.01 ± 7.8 | −500.63 ± 13.6 |

  - "No hashtag" perplexity is scored over a different token set: Eq. 68 normalizes by N_d + M_d, and the hashtags are gone.
  - "No µ1", "no θ′–θ" and "no power-law" have network LLs within about one reported ± of the full model. Only "no power-law" (and arguably "no hashtag") separate from it.
- **Clustering (Table 6; purity / NMI).**
  - TNTM (HPYP part only, K ≤ 20): Generic 0.66 / 0.43, Specific 0.68 / 0.31, Events 0.79 / 0.52.
  - Best pooling-LDA row per dataset, copied from Mehrotra et al. (2013), not rerun: hashtag pooling, 0.54 / 0.28, 0.68 / 0.23, 0.71 / 0.42 (author pooling ties on Generic purity at 0.54).
  - Ground truth is the query term; tweets matching several query terms are removed.
- **Topic labels (Table 7, §5.6.5).**
  - The top-3 hashtags per topic serve as labels.
  - The paper says "over 90 % of the hashtags are good candidates for the topic labels". No judges, protocol or sample size are given.
  - The six topics recover the six query hashtags, which the authors themselves call "to be expected".
- **Settings (§5.6.1).**
  - Word-side discounts: α = 0.7. Topic-side discounts are said to be "vary[ied]", and the values are never given.
  - β initialised at 0.5, with a Gamma(0.1, 0.1) hyperprior. λ, s, l, σ = 1; varying them over 0.01–10 made "no significant impact" (footnote 9, no data).
  - 2,000 iterations, with MH from iteration 1,000. Five repeats.
  - Not stated: the train/test split, and the fraction of each test document used for document completion.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The collapsed HPYP posterior factorizes into per-node count factors f(N), including under a discrete uniform base | strong (as a cited result) | Eq. 19, stated as a generalization of Chen et al. 2011 Thm 1; proof not given here |
| C2 | Removing one customer needs only the counts: the table is removed with probability t_k/c_k, so the seating arrangement need not be stored | moderate | Eq. 21 and §4.1; it follows Chen et al.; exchangeability argument not spelled out |
| C3 | The concentration-parameter auxiliary sampler (Eqs. 27–29) is exact given the counts | strong | Standard auxiliary construction (Teh 2006); I checked it against Eq. 16 |
| C4 | The framework lets new model variants be implemented "without significant reimplementation" and saves "significant time" | weak | Assertion (§3, §5.1, §6); no timings, lines of code, or list of the "number of other variants" said to have been built |
| C5 | The collapsed blocked sampler of Chen et al. "generally outperform[s]" variational methods and the Chinese restaurant franchise in time, space and some metrics | weak here | Cited to Buntine & Mishra (2014); no experiment in this paper |
| C6 | The TNTM fits tweet text much better than HDP-LDA and a nonparametric ATM | moderate | Table 4: one corpus, five runs, error bars undefined, split unstated; baseline implementation unstated |
| C7 | "Using more auxiliary information gives a better model fitting" (§5.6.2, §6) | weak as a general claim; moderate on T6 | Table 4/5 on one hashtag-queried corpus whose hashtag rate (1.34/tweet) is 5–13× that of the other three datasets |
| C8 | Jointly modelling text and network improves the network fit | moderate | Table 4, −500.63 ± 13.6 vs. −557.86 ± 11.2; not said whether this is held-out or training likelihood |
| C9 | Every TNTM component is important ("the result shows that each component … is important") | weak–moderate | Table 5: hashtags, authors, µ1 and θ′–θ clearly matter for perplexity; power-law is within error for perplexity; the network-LL gaps for µ1 and θ′–θ are within ~1 ±; no significance tests |
| C10 | Power-law discounts matter most for the network likelihood, "because the flexibility enables us to learn the author–topic distributions better", which "suggests that the authors … tend to focus on a specific topic" | weak | The number is in Table 5 (−560.28 ± 30.7, the largest ±); the mechanism and the inference about authors are interpretation, not tested |
| C11 | TNTM beats tweet-pooling LDA on purity and NMI on all three datasets except a purity tie on Specific | weak–moderate | Table 6; the baselines are transcribed from Mehrotra et al., not rerun under the same preprocessing; K capped at 20 for TNTM only as stated; single numbers, no variance |
| C12 | The proposed kernel "fits our purpose better and achieves significant improvement over the original kernel" of Lloyd et al. (2012) | weak | Assertion (§5.2.3); no kernel comparison is reported anywhere |
| C13 | Over 90% of top hashtags are good topic labels | weak | Assertion (§5.6.5); no evaluation protocol |
| C14 | The test-time θ estimates are unbiased | weak | Assertion (§4.5.1); the procedure fixes table counts at half the customer counts and freezes training counts |
| C15 | λ, s, l, σ have no significant effect over 0.01–10 | weak | Footnote 9; no data shown |
| C16 | "Our nonparametric model performs better than existing parametric models" (abstract) | weak | Both goodness-of-fit baselines (HDP-LDA, nonparametric ATM) are themselves nonparametric. The only parametric comparators are the pooled-LDA rows copied from another paper. The body does not show what the abstract says |

## Method

**Collapsed blocked Gibbs for an HPYP topic model (Algorithm 1, §4).**
1. **Initialize.** Assign random topics. Set customer counts from the assignments (Eq. 20) and table counts to about half the customer counts.
2. **Decrement (§4.1).** For each word w_dn:
   - Decrement c on the vocabulary side at φ_{z}.
   - Sample u ~ Bernoulli(t/c) (Eq. 21). If u = 1, decrement t there and c at the parent, and recurse to the root.
   - Do the same on the topic side, starting at θ_d.
   - Multiple parents (A.1, Algorithm 2): u ranges over {P_1, …, P_P, ∅}, with P(u = P_i) = t^{N→P_i}_k / c_k (Eq. 70).
3. **Block-sample (§4.2).** Enumerate every state (z, and each node's t and c either unchanged or +1). A parent's c increments only when a child's t increments; a new topic means t goes 0 → 1 at the root µ.
   - Score each state by the product of ratios f(N)/f(N^{−dn}) (Eqs. 23–25).
   - The Stirling ratios come from a cache.
   - Normalize and sample; the proposal is always accepted.
4. **Hyperparameters.** Sample each β_N (Eqs. 27–29). Repeat until converged or a fixed iteration count.
5. **Read-out.** Posterior means by recursion (Eq. 34). The extra "new topic" dimension is dropped or renormalized at µ (§4.4).

**TNTM (§5.2, A.4, Algorithm 4).**
- **Generative model.**
  - Topic side: µ0 ~ GEM; µ1 and ν_i ~ PYP(µ0); η_d ~ PYP(ν_{a_d}).
  - θ′_d ~ PYP(ρ′µ1 + (1 − ρ′)η_d) and θ_d ~ PYP(ρη_d + (1 − ρ)θ′_d), with ρ′, ρ ~ Beta.
  - Emission: hashtags from ψ′_{z′} and words from ψ_z, where ψ, ψ′ ~ PYP(γ) and γ ~ PYP(uniform).
  - Links: x_ij ~ Bernoulli(s(Q_ij)), with Q a GP over author pairs driven by the ν.
- **Inference.**
  - 1,000 sweeps of collapsed blocked Gibbs over words and hashtags.
  - Then alternate the MH step with Gibbs conditioned on µ0 and ν:
    - Propose µ0 ~ Dirichlet(β^{µ0}µ0) and ν_i ~ Dirichlet(β^{νi}ν_i).
    - Recompute the GP mean and covariance, and draw Q^new with an elliptical slice sampler.
    - Accept with the ratio in Eq. 82. That ratio uses p(Q | X, ν), multinomial factors f* in the table counts (Eqs. 83–84) and the Dirichlet proposal densities.
- **An unresolved question about the MH step.** The Q^new draw's own proposal density does not appear in the Hastings ratio. Whether this is a valid MH kernel for the joint posterior depends on details the paper does not state; unverified. The explicit-vector targets f* also drop the PYP prior of ν_i given µ0, which has no density on the simplex. That makes the MH target an approximation the paper does not discuss.

## Concepts

- **Restaurant / customer / table / dish.** A PYP node is a restaurant, and its data (or its children's tables) are its customers. Each table serves a dish (topic or word). A restaurant's tables are its parent's customers (§3.2, Fig. 2).
- **Customer count c^N_k, table count t^N_k.** The number of customers eating dish k at N, and the number of non-empty tables serving k. C_N and T_N are the totals. With several parents, t^{N→P}_k counts the tables sent to parent P (§5.3).
- **Table multiplicity representation.** Keep only (c, t) per dish, not the seating (Chen et al. 2011; Fig. 3).
- **Bernoulli table indicator u^N_k.** Here, whether removing a customer also removes its table. The paper notes explicitly that this differs from Chen et al.'s indicator, which picks the restaurant a customer contributes to (§4.1).
- **Modularised likelihood f(N).** A node's collapsed-posterior factor (Eq. 16), built from generalized Stirling numbers S^x_{y,α} and Pochhammer symbols (x)_T and (x|y)_T.
- **Topic side / vocabulary side.** The µ → ν → θ chain and the γ → φ chain of Fig. 1.
- **Document completion.** Estimate a test document's θ from some of its words and score the rest (Wallach et al. 2009b). The split fraction is not given here.
- **Compound Poisson–Dirichlet process / doubly hierarchical PYP.** A PYP with a mixture base (§2.2).

## Connections

- **Lineage.**
  - Pitman–Yor via Ishwaran & James (2001) and Pitman & Yor (1997), with Buntine & Hutter (2012) for the Stirling-number posterior.
  - HDP-LDA (Teh et al. 2006) and hierarchical Bayesian nonparametrics (Teh & Jordan 2010) supply the model class. The concentration sampler is from Teh (2006, the Kneser–Ney technical report).
  - The sampler is Chen, Du & Buntine (2011). The base HPYP topic model is from Buntine & Mishra (2014). Multiple-parent PYPs come from Du et al. (2012a, adaptive topic model).
  - The network half is Lloyd et al. (2012) random-function priors, with elliptical slice sampling from Murray et al. (2010).
  - The TNTM extends Lim, Chen & Buntine (2013, NIPS workshop).
  - Clustering baselines and three datasets are from Mehrotra et al. (2013), a paper that shares the author Buntine.
- **The nested HDP ([LIT-002](../literature.d/LIT-002.md); reading at reads/23).** Neither paper cites the other. This paper names the nCRP JACM paper (Blei et al. 2010) only for the restaurant metaphor. It groups SVI (Hoffman et al. 2013) and online HDP (Wang et al. 2011a) among the variational methods it says the Chen et al. sampler beats, citing Buntine & Mishra rather than showing it.
  - **Direction of generalization.** Both generalize HDP-LDA, in orthogonal directions. The nHDP puts DP topics in a tree with no discounts. This paper keeps a flat topic set, adds discounts (power law) and auxiliary-data nodes, and allows DAG-shaped (multiple-parent) node structure.
  - **Inference.** The choices are opposite: the nHDP uses truncated mean-field SVI with hard subtree pointers for millions of documents on one machine; this paper uses truncation-free collapsed MCMC over counts, demonstrated on at most ~360k tweets.
  - **Scale and evaluation.** Neither measures the other's regime. The nHDP never runs a PYP; this paper never reports wall-clock times, so its efficiency claim (C4, C5) cannot be set against the nHDP's ≈20 h per pass.
  - **Common flaw.** Both report held-out likelihood-type metrics against baselines with confounded capacity or implementation, and neither evaluates topic quality with humans.

## Bearing on the record

- This is the reading of [LIT-013](../literature.d/LIT-013.md). It supports moving [LIT-013](../literature.d/LIT-013.md) from `Deferred` to `Active` for the sampler exposition. The LIT's summary should drop "single" in "a single collapsed, blocked Gibbs sampler", and the TNTM results should be read as one-corpus evidence. [LIT-013](../literature.d/LIT-013.md)'s lineage could declare `extends:` Chen et al. (2011) and Lim et al. (2013), and `compared_against:` HDP-LDA, the nonparametric ATM, the random-function network model and Mehrotra et al.'s pooled LDA, if those works are ever filed. None of them is in the record now.
- No THEORY document in the nucleation record bears on it (checked by search).
- **ML practice.** Nothing that should become a practice. Three points of contact with the anthology:
  - (a) §5.6.4 is titled "Document Clustering and Topic Coherence" but reports no coherence measure. Topic quality rests on perplexity, clustering against query terms, and an unprotocolled "over 90%" label judgement. That is exactly the evaluation pattern [ANTH-SOTA-368](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/practices.d/SOTA-368.md) advises against: held-out likelihood is not interpretability. It is also why [ANTH-SOTA-371](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/practices.d/SOTA-371.md)'s PMI coherence exists. This paper is an example of the problem, not a source for either practice.
  - (b) Its own ablation undercuts the common folk-claim that PYP power-law discounts improve text fit: perplexity 508.64 ± 7.1 without them vs. 505.01 ± 7.8 with them (Table 5). It is one small data point, not a source for anything.
  - (c) Anyone implementing HPYP / Kneser–Ney-style hierarchical smoothing can use §§3–4 as a readable reference. Chen et al. (2011) and Buntine & Hutter (2012) are the primary sources.

## Limitations

- **One corpus for the headline results.** T6 was queried by six hashtags, so hashtags are dense (1.34 per tweet) and align with the evaluation's topics. It covers 150 authors, a number the network model's A² GP presumably forces (not stated). The claim that auxiliary information helps in general (C7) is not tested on any corpus without that alignment.
- **Evaluation gaps.**
  - The ± quantity is undefined. The train/test split and the document-completion fraction are not stated, and there are no significance tests.
  - Whether the network log-likelihood is held-out is not stated.
  - The clustering baselines are transcribed from another paper, not rerun.
  - There is no human or coherence evaluation of topics, despite the §5.6.4 title.
  - Runtime and memory are never measured, though efficiency is the paper's stated reason for the sampler.
- **Abstract overclaims.** It promises a win over "existing parametric models", but the goodness-of-fit baselines are nonparametric (C16).
- **Reproducibility.** The topic-side discount values are never given ("we vary"). The Stirling cache and table-count details are deferred to a thesis. No code location is given.
- **Inference approximations not analysed.**
  - Initial and test-time table counts are set to half the customer counts.
  - After iteration 1,000 the model mixes collapsed and uncollapsed nodes.
  - The MH acceptance ratio omits the Q proposal density and the PYP prior on ν (see Method).
  - There are no convergence diagnostics; "2,000 iterations for the models to converge" is asserted.
- **Typographical errors** in Eqs. 10 (text), 53 and 83, §5.6.1 and Algorithm 4 (see corrections). None changes a reported number.
- The authors state no limitations. §6.1 lists only extensions: other data, more metadata, retweet paths, combining topic models.

## Open questions

- Does the auxiliary-data gain survive on a corpus that was not queried by hashtags? The Generic/Specific/Events datasets have 0.10–0.25 hashtags per tweet. Rerunning Tables 4–5 there, with a stated split, would settle C7.
- Is the network-likelihood gain held-out? Link prediction on held-out author pairs would show whether the joint model generalizes or only fits.
- What is the actual cost of the table-count sampler against SVI/online HDP at matched perplexity, in time and memory? This is the paper's motivating claim (C4, C5), and it is not measured here.
- Does the proposed kernel beat Lloyd et al.'s original (C12)? A single ablation row would answer it.
- How much do the halved table counts at initialization and test time bias the perplexity estimate, compared with sampling the table counts?
- Is the power-law effect on the network likelihood robust? Its ± (30.7) is the largest in Table 5, and five runs is few.

## Corrections to the seeded skim

- **"Fit with a single collapsed, blocked Gibbs sampler" overstates it for the TNTM.** The sampler is collapsed and blocked only for the HPYP half. The full TNTM alternates that sampler with a Metropolis–Hastings step (Algorithm 3, §A.4). The MH step proposes µ0 and ν from Dirichlet(β·current) and draws Q with an elliptical slice sampler. From iteration 1,000 onward µ0 and ν are held as explicit probability vectors and no longer collapsed (§A.4, §A.5, Algorithm 4).
- **The dossier says to check "the table-count sampling details (§4, Appendix A) if implementing"; they are not in the paper.** The derivation of the modular likelihood is left to Chen et al. (2011, Theorem 1), and the Stirling-number cache to Lim (2016, PhD thesis) and Buntine & Hutter (2012) (§3.2, §4.2). Appendix A covers only the TNTM specifics: multiple-parent decrementing, multiple-parent posterior means, the MH step and hyperparameter sampling.
- **"Algorithm in §4.4" is misplaced.** Algorithm 1 (the collapsed Gibbs sampler) is on p. 15 at the end of §4.3. §4.4 is about reconstructing the probability vectors (Eqs. 30–34).
- **Clustering (Table 6) is not a like-for-like comparison, and the skim does not say so.** The six pooling-LDA rows are "obtained from Table 4 in Mehrotra et al. (2013)"; they were not rerun. The TNTM row uses "only the HPYP part" (those datasets have no network), with the number of topics capped at 20. The dossier's "tie on one dataset" is correct in a narrow sense: the tie is purity on the Specific dataset (0.68 vs. hashtag pooling 0.68). TNTM's NMI there is higher (0.31 vs. 0.23).
- **The dossier's ML link overstates the paper's power-law evidence.** The paper's own ablation shows that removing the power-law discounts changes perplexity from 505.01 ± 7.8 to 508.64 ± 7.1, within the error bars (Table 5). The effect appears only in network log-likelihood (−500.63 → −560.28).
- Minor: the dossier's `published: 2016-09-01` matches neither date the preprint gives. arXiv v1 is 22 Sep 2016 (the date [LIT-013](../literature.d/LIT-013.md) uses), and the preprint header gives journal publication as 18 Jul 2016.
- **Internal errors the dossier did not catch:**
  - §3.1 says ν "follows a PYP given ν, which acts as its base distribution". Eq. 10 has µ as the base.
  - Eq. 53 writes the base of θ_d as ρ^{θd} η_m + (1 − ρ^{θd}) θ′_d; it should be η_d. §5.6.1 likewise indexes η_m, θ′_m, θ_m and lists "ψ, φ′ and γ" for ψ, ψ′, γ.
  - Eq. 83, as printed, has exponent t_k^{µ1} + Σ_{i=1}^A ν_i, which puts a probability vector in an exponent. It presumably means Σ_i t_k^{νi}. Checked on the page image.
  - Algorithm 4 step 3(b) samples "z′_dn" for a hashtag; it should be z′_dm.
