---
status: Read
paper: LIT-tmp0o6ud
title: 'Blei, Ng & Jordan — Latent Dirichlet allocation'
version: 1
history:
- version: 1
  date: '2026-11-03'
  note: >-
    Read in full from the JMLR PDF (jmlr.org/papers/volume3/blei03a/
    blei03a.pdf), JMLR 3: 993–1022, "Submitted 2/02; Published 1/03",
    30 pp.: the abstract, §§1–8, the acknowledgements, the references and
    Appendix A (A.1–A.4). Text was extracted with pypdf; Figures 4 and 8
    came through as glyph debris, so what is said of them is the caption's.
    Equations were reconstructed from the extraction and checked against
    the update equations they must agree with. Pages are the journal's.
date: '2026-11-03'
summary: >-
  LDA draws one topic mixture θ_d ~ Dir(α) per document and a topic for
  every word from it, a three-level model (corpus α, β; document θ_d;
  word z, w), justified by de Finetti's theorem for exchangeable words.
  The paper sets it against the mixture of unigrams, which gives each
  document exactly one topic, and pLSI, which has a mixture per training
  document but no model for it. Inference is variational (eqs. 6–7); on
  two corpora LDA has the lowest held-out perplexity of the four models.
---
<!-- inactive-ok-file: NOTE-tmpagiju — Proposed, Open, Deferred, Unfetched, Unavailable or new; cited as open -->
<!-- inactive-ok-file: CLAIM-tmpwh2jo CASE-165 THEORY-614 LIT-677 — Proposed or Open; the entries the reading bears on, cited as open -->

# NOTE-tmplt5sh: Blei, Ng & Jordan — Latent Dirichlet allocation

## Contribution

A generative probabilistic model at the level of documents, which pLSI
lacked. pLSI gives each training document a mixture p(z | d) but "no
generative probabilistic model for these numbers" (p. 994), so its
parameters grow with the corpus and it cannot score a new document. LDA
makes the mixture a k-dimensional random variable with a Dirichlet prior,
so the model has k + kV parameters whatever the corpus size (p. 1001) and
assigns probability to unseen documents (eq. 3).

## Key insight

Treat the words of a document as exchangeable and take de Finetti
seriously: an exchangeable sequence is a mixture of i.i.d. sequences, so a
document is a draw of a latent parameter θ followed by i.i.d. topic and word
draws given θ (§3.1, p. 998). Putting a Dirichlet on θ gives LDA. The
intra-document structure lives in the mixing distribution, not in the
conditional factors, which "is simple and factored" (p. 995).

## Assumptions

- **Generative process (p. 996).** For each document: N ~ Poisson(ξ);
  θ ~ Dir(α); for each of the N words, zₙ ~ Multinomial(θ) and
  wₙ ~ p(wₙ | zₙ, β). The dimension k is known and fixed; β is a k × V
  matrix with βᵢⱼ = p(wʲ = 1 | zⁱ = 1), treated as fixed; N is ancillary.
- **Exchangeability** of words within a document and of documents within a
  corpus (the bag-of-words assumption, pp. 994–995). The paper is explicit
  that exchangeability is "conditionally independent and identically
  distributed", not i.i.d. (p. 995).
- **Smoothed LDA (§5.4, p. 1006).** Each row βᵢ of β is drawn independently
  from one *exchangeable* Dirichlet with a single scalar parameter η
  (footnote 2): every topic gets the same prior Dir(η, …, η).
- Footnote 1 (p. 996): "we make no epistemological claims regarding these
  latent variables beyond their utility in representing probability
  distributions on sets of words."

## Key results

- **Three levels (p. 997, Figure 1).** "α and β are corpus-level
  parameters … θ_d are document-level variables, sampled once per document
  … z_dn and w_dn are word-level variables and are sampled once for each
  word in each document." The abstract: "a three-level hierarchical
  Bayesian model". It is drawn in plate notation (Figure 1).
- **The contrast the authors draw themselves (p. 997).** "It is important to
  distinguish LDA from a simple Dirichlet-multinomial clustering model. A
  classical clustering model would involve a two-level model in which a
  Dirichlet is sampled once for a corpus, a multinomial clustering variable
  is selected once for each document … such a model restricts a document to
  being associated with a single topic. LDA, on the other hand, involves
  three levels, and notably the topic node is sampled *repeatedly* within the
  document." Such structures are "conditionally independent hierarchical
  models" (Kass and Steffey).
- **Mixture of unigrams (§4.2, p. 1000).** p(w) = Σ_z p(z) Πₙ p(wₙ | z):
  "each document exhibits exactly one topic". LDA costs "just one
  additional parameter": k − 1 for p(z) against k for p(θ | α).
- **Unigram model (§4.1, p. 999).** Every word of every document from one
  multinomial, p(w) = Πₙ p(wₙ).
- **A continuous mixture of unigrams (§3.2, p. 998).** Marginalizing z,
  p(w | θ, β) = Σ_z p(w | z, β) p(z | θ), and LDA is a two-level continuous
  mixture with k + kV parameters.
- **Geometry (§4.4, Figure 4, pp. 1001–1002).** Mixture of unigrams puts each
  document at a corner of the topic simplex; pLSI an empirical distribution
  on it; LDA a smooth distribution on it.
- **Variational inference (eqs. 4–8, pp. 1004–1005).**
  q(θ, z | γ, φ) = q(θ | γ) Πₙ q(zₙ | φₙ); φₙᵢ ∝ β_{i,wₙ} exp{Ψ(γᵢ) −
  Ψ(Σⱼγⱼ)}, γᵢ = αᵢ + Σₙ φₙᵢ. Derived in A.3 from the lower bound (12)–(15);
  the two updates (16), (17) agree with (6), (7). M-step βᵢⱼ ∝ Σ_d Σₙ φ*_dni
  wʲ_dn (eq. 9); α by a linear-time Newton–Raphson (A.2, A.4.2).
- **Example (§6).** 100-topic LDA on 16,000 TREC AP documents; for one
  held-out article four topics have γᵢ − αᵢ ≥ 1 (p. 1007).
- **Document modeling (§7.1, Figure 9, Table 1).** C. elegans abstracts
  (5,225 documents, 28,414 terms) and TREC AP (16,333 articles, 23,075
  terms), 90/10 split. LDA has the lowest held-out perplexity at every k.
  Uncorrected, the mixture of unigrams overfits explosively (AP perplexity
  2.20 × 10⁸ at k = 5, 2.39 × 10¹⁵⁰ at k = 100) and so does pLSI (17,588 at
  k = 5, 1.72 × 10⁷ at k = 100); the figure's curves use corrected versions.
- **Classification (§7.2).** On Reuters-21578 (8,000 documents, 15,818 words),
  an SVM on 50-topic LDA features (a 99.6% reduction) does about as well as
  on all word features, "in almost all cases" better (Figure 10).
- **Collaborative filtering (§7.3).** EachMovie, 3,300 training and 390 test
  users: LDA has the lowest predictive perplexity (Figure 11).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | LDA is a well-defined generative model of documents with k + kV parameters, independent of corpus size | strong | construction, §§3, 4.3 |
| C2 | The mixture of unigrams restricts a document to one topic; LDA lets topics be resampled within a document | strong | definitions, pp. 997, 1000 |
| C3 | Exchangeable words and topics within a document must have the LDA-type integral form, by de Finetti | strong | §3.1; the Dirichlet itself is a choice of convenience (p. 996), not forced |
| C4 | The variational updates (6)–(7) maximize the bound (15) coordinatewise | strong | Appendix A.3, rederivable |
| C5 | LDA generalizes better than unigram, mixture of unigrams and pLSI | moderate | two corpora, perplexity only, one stopping rule (§7.1) |
| C6 | LDA features lose little discriminative information | weak | two binary tasks; "these results need further substantiation" (p. 1013) |

## Concepts

- **Topic** — a latent multinomial variable z, "so as to exploit
  text-oriented intuitions" (footnote 1); each topic i is characterized by a
  distribution over words, the row βᵢ.
- **Topic mixture θ** — a point on the (k − 1)-simplex, drawn once per
  document from Dir(α). The Dirichlet is the distribution over mixtures; the
  topics are the categories a mixture weights.
- **Exchangeable Dirichlet** — a Dirichlet with all components equal to one
  scalar (footnote 2).
- **Word simplex / topic simplex** — the (V − 1)-simplex of word
  distributions and the sub-simplex spanned by the k topics (§4.4).

## Connections

- **pLSI** (Hofmann 1999), the immediate predecessor, criticized for having
  no document-level model (pp. 994, 1000–1001).
- **de Finetti, Aldous, Diaconis** for exchangeability (pp. 994–998).
- **Kass and Steffey; Gelman et al.; Morris**: hierarchical and parametric
  empirical Bayes models (p. 997).
- In the record: hLDA ([LIT-1542](../literature.d/LIT-1542.md)) and the nested HDP ([LIT-002](../literature.d/LIT-002.md)) build on it;
  [LIT-677](../literature.d/LIT-677.md) is an ELBO paper about it.

## Bearing on the record

- **[CLAIM-tmphbnqm](../claims.d/CLAIM-tmphbnqm.md): its account of LDA matches the paper, with one
  over-statement and one gloss to add.**
  - *Matches.* "Each episode draws its own mixture θ_d ~ Dir(α), then
    z_{d,n} ~ Cat(θ_d)" is the generative process (p. 996). "The Dirichlet
    is a distribution over mixtures … the perspectives are the categories
    each mixture weights" is the paper's usage: topics are the z's and the
    βᵢ's, θ is the mixture (pp. 996–997). The a → 0 limit, one topic per
    document, is the paper's mixture of unigrams (§4.2), and the paper itself
    names the one-topic-per-document comparison, "a simple
    Dirichlet-multinomial clustering model" (p. 997). The agreement formula
    (a + 1)/(Ka + 1) follows from E[θ_k²] for a symmetric Dirichlet and was
    re-simulated for this reading (200,000 episodes each: K = 3, a = 1:
    0.4987 against 0.5; K = 5, a = 0.2: 0.5985 against 0.6; K = 4, a = 10:
    0.2667 against 0.2683; across-episode 0.332, 0.202, 0.249 against 1/K).
  - *Gloss.* The a → 0 limit of a *symmetric* Dir(a) gives a mixture of
    unigrams with uniform p(z). The paper's mixture of unigrams has a free
    p(z), k − 1 parameters (p. 1000); it is the limit of Dir(sπ) as s → 0
    with π fixed. The other limit, a → ∞, is the paper's *unigram model*
    (§4.1) once z is marginalized: every word from the single distribution
    Σ_k π_k β_k. So with latent perspectives, "independent draws per act"
    cannot be told from one fixed output distribution; only a fit with
    many episodes can.
  - *Over-statement.* "In smoothed LDA each topic's distribution over outputs
    has its own Dirichlet prior". Each row of β is drawn independently, but
    from one exchangeable Dirichlet with a single shared scalar η (§5.4,
    footnote 2). "Its own draw from a shared prior" is what the paper says.
  - *On "the topics … are the dirichlet".* The abstract's second sentence
    reads "Each topic is, in turn, modeled as an infinite mixture over an
    underlying set of topic probabilities", which is garbled in the same
    direction as the owner's phrase. The body is unambiguous (pp. 996–998).
- **[CLAIM-tmpwh2jo](../claims.d/CLAIM-tmpwh2jo.md).** Its quotation is exact: "a three-level hierarchical
  Bayesian model" (abstract), drawn in plates (Figure 1). Its point that the
  topic assignments are "conditionally independent given a document's
  proportions" is the paper's own description, "conditionally independent
  hierarchical models" (p. 997), and the paper adds that the components are
  exchangeable by assumption (§3.1). The paper also names the extensions
  that would break exchangeability among topics, a time series of topics,
  conditioning on exogenous variables, mixtures of Dirichlets (p. 1015). None
  of them is a dependency in which one topic conditions which others are
  available, so none would be organization in [CLAIM-tmpwh2jo](../claims.d/CLAIM-tmpwh2jo.md)'s sense; the
  correlated and Pachinko models it names are later.
- **[QUESTION-tmpildq9](../questions.d/QUESTION-tmpildq9.md).** The test it proposes, within- against
  between-episode co-occurrence, is exactly what separates LDA from the
  paper's two-level clustering model. The paper's own discussion (p. 1015)
  says that in LDA "the 'emission' probability p(wₙ | zₙ) contributes only a
  likelihood value", which is the additive-mixture structure the question
  contrasts with the J-space's product of experts.
- **No instruction for machine-learning practice.**

## Limitations

- Bag-of-words: the paper's own example splits "William Randolph Hearst
  Foundation" across topics (p. 1008).
- The empirical comparisons are perplexity on two corpora, two binary
  classification tasks and one recommendation set, with no error bars.
- The Dirichlet is chosen for conjugacy and convenience (p. 996); nothing in
  the paper argues it is the right prior on mixtures.
- k is fixed and known; selecting it is not treated.

## Open questions

- The paper's suggested relaxations to partial exchangeability (time series
  of topics, conditioning on paragraph or sentence) are where a
  sequence-aware analogue for an Assistant episode would start; the
  Assistant Axis reading ([NOTE-tmpagiju](NOTE-tmpagiju.md)) finds within-episode drift driven by
  the latest message, which no exchangeable model represents.
