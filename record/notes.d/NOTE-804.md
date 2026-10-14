---
number: 804
status: Read
formerly:
- NOTE-tmpr0hmw
paper: LIT-941
title: 'Goldwasser et al. — A Theory of Unsupervised Translation Motivated by Animal Communication'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from arXiv:2211.11081v2 (3 November 2023, the NeurIPS 2023
    version), text extracted with pdftotext: §§1–4 with every theorem
    statement, and appendices A (the MLE theorem and its proof), B (the
    tree model, Theorem B.1 and Lemma B.2), E (experiments), F–J (related
    work, future work, priors from prompts, lossy translation, infinite
    families, Occam bounds). Of the long proofs in B.2, C (upper and lower
    bounds for the common-nonsense model) and D (knowledge graphs), the
    overviews, lemma statements and the opening of each proof were read;
    the combinatorial and concentration steps were not checked line by
    line. Figures were read from captions and the table in Figure 4.
date: '2026-10-14'
summary: >-
  With a plausibility prior over the target language and no parallel data,
  maximum likelihood learns a translator whose error is bounded like a
  supervised Occam bound divided by the common ground. In the
  common-nonsense model err = O(log|Θ| / (α·min(m,|T|))), tight up to a
  constant; in the knowledge-graph model more knowledge per node needs less
  agreement. Information-theoretic only, lossless, uniform languages.
---
<!-- inactive-ok-file: CLAIM-199 CLAIM-054 THEORY-170 THEORY-270 — Proposed; the claims and theories this reading bears on or files, open -->
<!-- inactive-ok-file: LIT-767 — Unavailable; Wyner–Ziv, named by QUESTION-020, not leaned on -->

# NOTE-804: Goldwasser et al. — A Theory of Unsupervised Translation Motivated by Animal Communication

## Contribution

The paper gives what it calls the first theoretical treatment of
unsupervised machine translation (UMT). It drops the usual assumption that
the target language's distribution resembles the translations, and replaces
it with a prior ρ over target texts that scores how plausible a translation
is. It then proves sample-complexity bounds for maximum likelihood against
that prior in two stylised random models of language, with a matching
lower bound in one. After it, there is a formal sense in which a receiver's
background knowledge can stand in for parallel data.

## Key insight

A wrong translator gives itself away by producing, somewhere among many
translations, text the prior finds impossible. Translation is learnable
when the ground truth survives the prior and every badly wrong translator
does not. That gets easier with more shared knowledge, with a richer source
language that offers more chances to be caught, and with a simpler
translator family that has fewer ways to be wrong.

## Assumptions

- **Lossless translators.** Each f_θ : X ↪ Y is one-to-one. A lossy
  extension is sketched in Appendix I.1 and not analysed.
- **Realisability.** The ground truth ⋆ ∈ Θ, and the prior never rules it
  out: Pr_{x∼µ}[ρ(f_⋆(x)) = 0] = 0 (Definition 2.1). In the knowledge-graph
  model the prior is smoothed to full support instead.
- **Finite sets.** X, Y and Θ are finite; log|Θ| is the description length.
  Infinite families are handled by a trick in Appendix I.2, left informal.
- **Uniform languages.** In every model, source and prior are uniform over
  sets; Zipfian distributions are named as future work.
- **The target subsumes the source.** Everything sayable in the source is
  sayable in the target (Appendix G, item 1).
- **Information-theoretic.** MLE is analysed as an estimator; no efficient
  algorithm is given.

## Key results

- **MLE** (Definition 1.1): θ̂ = argmin_θ Σ_i log 1/ρ(f_θ(x_i)), which
  approximately minimises D(θ) = KL(f_θ ∘ µ ‖ ρ).
- **Theorem A.2 (the general bound).** Call θ a γ-plausible ambiguity if
  at most a γ fraction of its translations are impossible under ρ, and let
  ε_γ be the largest loss of any such θ. If γ ≥ (1/m) ln(|Θ|/δ), then with
  probability > 1 − δ, L(θ̂) ≤ ε_γ. *Holds:* realisable prior; any µ, ρ.
  The proof is the realisable Occam argument with "impossible under ρ" in
  place of "disagrees with the label".
- **Theorem 3.2 (knowledge graphs).** Source and target are correlated
  Erdős–Rényi digraphs on r ≤ n nodes, edge probability p, agreement α
  (each source edge copies the target with probability α, else is
  redrawn). Translators map nodes to nodes, |Θ| = n!/(n−r)!. With
  probability ≥ 1 − δ,
  err(θ̂) ≤ max( (64/(α²pq²r²)) ln(6nr/δ), (2/(αq))·√((2/m) ln(6nr/δ)) ),
  q = 1 − p; for p < 0.99, with probability ≥ 0.99,
  err = O( log n/(α²pr) + (1/α)√(r log n / m) ).
  The first term does not shrink with data: residual ambiguities like
  matching triangles. It is small when the per-node knowledge pr ≫ 1/α².
- **Theorem 3.4 (common nonsense).** Prior and translations are uniform over
  T ⊆ P ⊆ Y after removing a random α-fraction S of Y from both, α ≤ 1/2.
  For any finite Θ, with probability ≥ 1 − δ,
  err(θ̂) ≤ (6/α)·max(1/m, 16/|T|)·ln(6|Θ|/δ); more simply, with
  probability ≥ 0.99, err = O( log|Θ| / (α·min(m, |T|)) ).
- **Theorem 3.5 (lower bound).** For c₁ ≤ log|Θ| ≤ α·min(m, |T|) there is
  a family of no greater size on which every algorithm has error
  ≥ log|Θ| / (c₂·α·min(m, |T|)) with probability ≥ 0.99. So Theorem 3.4 is
  tight up to a constant.
- **Theorem B.1 (random trees).** Texts are root-to-leaf paths of depth n
  in a random b-ary tree; the source uses a random a-ary subtree. Then
  err(θ̂) ≤ 16·max(1/m, 4/aⁿ)·ln(6|Θ|/δ). For word-for-word translators,
  |Θ| = |W|!, so m = O(|W| log|W|) and a text length logarithmic in the
  vocabulary suffices. For the family of all translators the bound is
  vacuous: "no free lunch."
- **Theorem J.1 (supervised comparison).** Realisable supervised
  translation has the Occam bound (1/m) ln(|Θ|/δ). The unsupervised bounds
  match it in m, at the cost of a factor 1/α and of the source size |T|.
- **Experiments (App. E).** Knowledge graphs with n = 10, p = 0.5, brute
  force over injective maps: error falls with m and with α; with α = 0.5
  and all edges, accuracy is 0.10 ± 0.05 for r = 4, 0.74 ± 0.08 for r = 7,
  1.00 for r = 10 (Fig. 4). Common nonsense with |T| = 10⁵, |P| = 10⁶ and
  10⁵ random translators: error falls with m and with α (Fig. 5).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | MLE against a plausibility prior learns a translator with an Occam-type guarantee, without parallel data | strong | Theorem A.2, proved |
| C2 | In the common-nonsense model, error scales as log|Θ| / (α·min(m,|T|)), and no algorithm does better than a constant factor | strong | Theorems 3.4 and 3.5, proved |
| C3 | More complex source languages need less common ground | strong in the models; weak beyond them | Theorems 3.2 and 3.4; the stylised models are "not intended to accurately capture natural language" |
| C4 | Unsupervised translation needs about as much data as supervised | moderate | the matching m-dependence; information-theoretic only |
| C5 | Prompting a language model can supply the prior | weak | Appendix H, two toy probabilities from GPT-3 |

## Method

Maximum likelihood over a finite translator family, scored by the prior,
analysed through "revisions" π_θ = f_θ ∘ f_⋆⁻¹ and plausible ambiguities.
Each random model is used to bound ε_γ; Theorem A.2 then gives the error.
The common-nonsense upper bound avoids dependence among the indicators by
partitioning the mistranslated set into three parts on which f_θ and f_⋆
have disjoint images (C.1.1).

## Concepts

- **Prior ρ.** A distribution over target texts measuring how plausible a
  translation is, not the distribution of target-language text. It can be
  focused on the source domain, e.g. by a prompt ("A sperm whale said:").
- **Common ground α.** In knowledge graphs, the probability that a source
  edge agrees with the target graph. In the common-nonsense model, the
  fraction of texts that are implausible to both, "the laws of nature"
  modelled as random.
- **Plausible ambiguity.** A translator that the prior rarely rules out;
  only supervision can resolve one.
- **Ground-truth translator.** What a hypothetical bilingual "mermaid"
  would output; error is measured against it.

## Connections

It contrasts with the alignment view of UMT, where the target distribution
is close to a simple transform of the source, and with Juba and Sudan's
goal-oriented communication, where a participant can verify success. Its
knowledge-graph model is a correlated-graph matching problem. Its prior is
a receiver's background knowledge, so it sits beside the record's
side-information question ([QUESTION-020](../questions.d/QUESTION-020.md)) and A86's Wyner–Ziv reading
([LIT-767](../literature.d/LIT-767.md)), though it never mentions rate–distortion.

## Bearing on the record

- **[QUESTION-020](../questions.d/QUESTION-020.md).** The LIT registered this paper with: "its error
  bounds for translation without parallel data depend on the translator's
  prior. That is a formal case of the interpreter substituting for
  transmitted information." The first half is right; the bounds depend on
  the common ground α between prior and translations. The second half is
  stronger than the paper. What the receiver's knowledge substitutes for
  here is *parallel data* (labels) in *learning* the decoder, not bits in
  an utterance. The number of source texts m is not a rate: each text is
  fixed, and nothing in the model shortens a message because the receiver
  knows more. The closest the paper comes to the question is in the
  common-nonsense bound, where α and min(m, |T|) enter as a product, so at
  fixed error halving the common ground needs twice the source data, tight
  up to a constant. That is an exchange rate between receiver knowledge and
  observed data for learning, which is a different trade-off from A86's
  R_K(D). Appendix H's "background prompts", explaining once what would
  otherwise be repeated in every translation, is the nearest thing to the
  question's "explicit explanatory material", and it is an unanalysed
  suggestion.
- **"Judging success" (§4).** If the KL between translations and prior is
  near zero, translations are predictive "regardless of whether the
  translations are correct": two parties can find a wrong translator
  natural. That bears on [CLAIM-054](../claims.d/CLAIM-054.md)'s separation of kinds of fidelity:
  plausibility to the receiver and correctness against the source come
  apart, and only an outside ground truth can tell them.
- **[THEORY-170](../theory.d/THEORY-170.md)** says translation must add and drop information because
  grammars oblige different things. This paper assumes the opposite case,
  lossless translation into a target that can say everything the source
  says, and names the partly overlapping case as open. The two do not
  conflict; they mark where this theory stops.
- **[CLAIM-199](../claims.d/CLAIM-199.md)** bounds what any receiver can do with a garbling. Here
  the receiver's prior does not add information about a given message; it
  narrows which decoders are consistent. The two are about different
  things, a single message against a learned code.
- Files [THEORY-270](../theory.d/THEORY-270.md).
- The paper ends with advice on what data to collect for whale
  communication. That is not ML practice in the anthology's sense, and the
  LIT's `anthology-candidate` flag, for its learning-theory content, is a
  separate matter left as filed.

## Limitations

- **Information-theoretic only.** MLE over all of Θ may be intractable.
- **Stylised random models.** The authors say they "are not intended to
  accurately capture natural language".
- **Lossless, uniform, target subsumes source.** Each is named in the
  future-work list.
- **The prior is assumed realisable.** A prior that rules out a true
  translation even rarely breaks Theorem 3.4's assumptions; only the
  knowledge-graph model smooths it.
- **Experiments are tiny** (ten nodes, brute force) and confirm only the
  direction of each dependence.

## Open questions

- Does the α·m exchange survive non-uniform, Zipfian languages?
- Is there an efficient algorithm for either model, perhaps from correlated
  graph matching?
- What does the lossy objective of Appendix I.1 trade, and how should its λ
  be set? That trade-off, between plausibility under the prior and
  information kept about the source, is the nearest the framework comes to
  a rate–distortion question.
