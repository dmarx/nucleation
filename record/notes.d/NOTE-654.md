---
number: 654
status: Read
formerly:
- NOTE-tmp18bc8
paper: 'LIT-851'
title: 'Analysing Ambiguous Nouns and Verbs with Quantum Contextuality Tools'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the text layer of an author copy (33-page LaTeX PDF,
    created 18 March 2022, running head "Contextual and Direct Influences
    in Ambiguous Phrases"), which the reader of LIT-842 downloaded and
    gave as UCL Discovery eprint 10146180. Its provenance could not be
    confirmed here, because UCL Discovery answered with a Cloudflare
    challenge. Its title, authors, keywords and abstract match the KCI
    record of the DOI word for word. The journal's version of record (pp.
    391–420) was not reachable and was not compared. Read: abstract,
    §§1–5, Propositions 1–2, Lemma 1 and Corollary 1 with their proofs,
    the reference list and the dataset of Appendix A (Figs. 7–10, 90
    rows). Figures 4 and 6 are plots without a text layer and were not
    seen. Checked by hand: the worked example of §3 (Δ = 1; Δ* = 7/20 and
    3/20, summing to Δ/2). Recomputed by script from the appendix: the
    class means and standard errors of Fig. 5a, which match when the
    population standard deviation is used, and the standard deviations of
    Fig. 5b; the verb shares 2Δ_v/Δ by class; and a Welch t-test and a
    Mann–Whitney U on them, which the paper does not report. Cited works
    not read: Jones 2019 (Proposition 8.4, which the proof quotes),
    Kujala and Dzhafarov 2016, Pickering and Frisson 2001b.
date: '2026-10-09'
summary: >-
  Proves that in a binary cyclic system CbD's signalling quantity Δ is
  twice the sum of each content's minimal direct influence over Jones's
  canonical causal models, which is the total-variation distance between
  its marginals. In 90 rank-2 noun–verb systems from British corpora, Δ is
  about 1.35 for every ambiguity class, and homonymous verbs carry about
  70% of it against about 50% for polysemous verbs. That difference rests
  on 14 systems from six verbs and is marginal by a recomputed test (p ≈
  0.06 two-sided). No system is tested for contextuality.
---

<!-- inactive-ok-file: THEORY-013 — Proposed; cited for what this reading bears on, not as settled -->
<!-- inactive-ok-file: THEORY-168 — Proposed; cited for a consequence this reading illustrates -->
<!-- inactive-ok-file: THEORY-177 — Proposed; filed from this reading -->
<!-- inactive-ok-file: THEORY-174 — Proposed; cited for an open question this reading raises -->
<!-- inactive-ok-file: CLAIM-125 CLAIM-037 — Proposed; open, and cited as open: the claims this reading bears on -->

# NOTE-654: Analysing Ambiguous Nouns and Verbs with Quantum Contextuality Tools

## Contribution

[LIT-842](../literature.d/LIT-842.md) asked whether ambiguous phrases are contextual. It found corpus
data always signalling, and it secured no contextual case. This paper
turns to the signalling itself. It proves that CbD's measure of
signalling, Δ, is the least amount of direct causal influence of context
that any of Jones's canonical models of the data must contain. It then
measures Δ, and how it splits between verb and noun, across 90 rank-2
noun–verb systems. It reports that the split, not the total, tracks
whether a verb is homonymous or polysemous.

## Key insight

Signalling is not noise to be subtracted before the interesting question.
It is a measurable direct influence of context, and in a binary system it
has an exact causal reading. Δ counts how often, at minimum, a hidden
state that fixes all other influences would still have to give the word a
different interpretation in the two contexts. On that reading, "how much
does the partner word steer this word's interpretation" has a number, and
the number can be compared across kinds of word.

## Assumptions

- **Binary contents.** Each word is restricted to two interpretations,
  labelled ±1, though some have more (§4). Proposition 1 needs the
  binary case: for ±1 variables, |⟨R⟩ − ⟨R′⟩| = 2|P(R = +1) − P(R′ = +1)|.
- **Rank-2 cyclic systems.** Two contents (verb, noun) and two contexts
  (verb–object, subject–verb). Each content occurs in exactly two
  contexts. The same verb and the same noun are treated as the same
  content in both grammatical roles.
- **A context** is the phrase, its grammatical structure, and "any extra
  information available, such as the corpus" (§4).
- **Probabilities** are relative frequencies of interpretations that the
  authors assigned by hand to BNC and ukWaC occurrences. No annotation
  protocol or agreement is reported. Each combination had to occur at
  least once in both orders. Systems whose uncertainty on Δ was "bigger
  than the range of possible values" were dropped; how err(Δ) was
  computed is not stated.
- **Jones's canonical models.** Context C and a latent background Λ jointly
  determine each content F_q. Every system has such a model (Jones 2019,
  quoted).
- **Classification by psycholinguistic lists.** Verbs come from Pickering
  and Frisson (2001b) and Shutova (2010), nouns from Rayner and Duffy
  (1986) and Tanenhaus et al. (1979). Homonymous means "several
  meanings" and polysemous means "several senses", following those
  sources.

## Key results

- **Eq. 1.** Δ = Σ_i |⟨R_i^{j_i}⟩ − ⟨R_i^{j′_i}⟩|, and Δ = 0 iff the system
  is non-signalling.
- **Eq. 3.** The direct influence of switching context c to c′ on content
  q in a canonical model is Δ_{c,c′}(F_q) = P(Λ ∈ {λ : F_q(λ, c) ≠
  F_q(λ, c′)}).
- **Lemma 1** (via Dzhafarov and Kujala 2016, Theorem 3.3). Over couplings
  S, max P(S_q^c = S_q^{c′} = o) = min(P[R_q^c = o], P[R_q^{c′} = o]),
  and the maximum is attained.
- **Proposition 2** (quoted from Jones 2019, Proposition 8.4). Canonical
  models and couplings correspond, with Δ_{c,c′}(F_q) = P(S_q^c ≠
  S_q^{c′}). So the minimal direct influence is the minimal disagreement
  over couplings (Corollary 1).
- **Proposition 1.** For a binary cyclic system, Δ = 2 Σ_q Δ*(F_q), where
  Δ*(F_q) = 1 − Σ_{v∈{±1}} min(P[R_q^c = v], P[R_q^{c′} = v]) (Eq. 5). The
  proof is three lines given the above. Eq. 13 drops the absolute values
  that Eq. 12 carries. This is a slip, and the result is unaffected. In
  the worked example, Eq. 16 prints min(3/4, 3/4) where the data of Fig. 2
  give min(3/4, 3/5); the stated value 3/20 is correct.
- **Fig. 5a: Δ by class** (mean ± standard error). Meanings-verb with
  meanings-noun 1.24 ± 0.29 (n = 14); meanings-verb with senses-noun
  1.50 ± 0.43 (n = 4); senses-verb with meanings-noun 1.36 ± 0.15
  (n = 61); senses-verb with senses-noun 1.38 ± 0.36 (n = 11); overall
  1.35 ± 0.12 (n = 90). The class sizes are recounted here from the
  appendix; the paper does not print them. All the values reproduce from
  the appendix with the population standard deviation (ddof = 0).
- **Fig. 5b: standard deviation of Δ.** Meanings-verbs 1.04,
  senses-verbs 1.20, meanings-nouns 1.18, senses-nouns 1.11. All
  reproduce. The paper reads the larger values as more variable
  behaviour and cautions that the dataset is small. No test is given.
- **§4: verb share 2Δ_v/Δ**, over systems with Δ > 0. Meanings-verbs
  0.70 (n = 14, from cast 4, admit 3, file 3, saw 2, plug 1 and tap 1),
  senses-verbs 0.48 (n = 55). Nouns: meanings-nouns 0.53 (n = 57),
  senses-nouns 0.47 (n = 12), both about 50%. The paper says the
  meanings-verb share is "strictly higher … with more than 95%
  confidence", names no test, and shows 66% intervals in Fig. 6.
  Recomputed here: Welch t = 2.00, df ≈ 20, one-sided p ≈ 0.030,
  two-sided p ≈ 0.059; Mann–Whitney U = 511.5 of 770. Footnote 6 says
  setting the Δ = 0 systems to 50% changes nothing qualitative.
  Recomputed: 0.65 (n = 18) against 0.48 (n = 72).
- **Footnote 4.** A rank-2 model with Δ > 2 cannot be CbD-contextual. By
  the cyclic criterion of [LIT-777](../literature.d/LIT-777.md), s_odd ≤ 2 in rank 2 and contextuality
  needs s_odd > Δ, so Δ ≥ 2 already suffices. 34 of the 90 systems are
  ruled out on Δ alone.
- **§5.** It recalls [LIT-842](../literature.d/LIT-842.md)'s contextual systems, adopt/boxer (1/30) and
  throw/pitcher (7/30); the extraction garbles them. Their rows here are
  Δ = 1.87 and 0.87, matching [NOTE-645](NOTE-645.md)'s recomputation (56/30 and 13/15).
  "No contextual instances of rank-4 models have been found yet."

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | In a binary cyclic system, Δ is twice the summed minimal direct influences over canonical models | strong (proof), given Jones's Prop. 8.4 | Proposition 1, Lemma 1, Proposition 2 (quoted) |
| C2 | Mean Δ does not distinguish the four ambiguity classes | moderate | Fig. 5a; reproduced from Appendix A |
| C3 | Homonymous verbs carry a larger share of direct influence than polysemous verbs | weak | 14 against 55 systems, six homonymous verbs, unnamed test; p ≈ 0.06 two-sided on recomputation |
| C4 | The noun's share does not depend on homonymy or polysemy | weak | Fig. 6b; a null on 12 senses-noun systems |
| C5 | Verbs on average have a larger direct influence than nouns (§1, §4) | not supported | the appendix gives an overall verb share of 0.52 ± 0.04 |
| C6 | The verb result agrees with Pickering and Frisson's eye-tracking finding | informal argument | §4 discussion; no behavioural data here |
| C7 | Combinations with a polysemous verb or a homonymous noun vary more | weak | Fig. 5b standard deviations, untested |

## Concepts

- **content / context.** A content is the interpretation of a word. A
  context is a phrase with its grammatical structure and its corpus.
- **direct influence (Δ_{c,c′}(F_q))**: in a canonical model, the
  probability over the background that switching context changes the
  content's value. **Minimal direct influence (Δ\*)**: its least value
  over all canonical models compatible with the data.
- **degree of signalling (Δ)**: the summed absolute differences of a
  content's expectations across its contexts. The paper keeps the word
  "signalling" for what CbD calls inconsistent connectedness.
- **meanings / senses**: unrelated interpretations (homonymy, as in
  spring) versus related ones (polysemy, as in newspaper as object or as
  content). "Interpretation" covers both.
- **verb share**: 2Δ_v/Δ, the fraction of Δ due to the verb. By
  Proposition 1, verb and noun shares sum to 1.

## Connections

The framework is CbD ([LIT-777](../literature.d/LIT-777.md)) and the analysis of [LIT-264](../literature.d/LIT-264.md). Its systems
are modelled on question-order effects ([LIT-834](../literature.d/LIT-834.md)). The causal side is Jones
(2019), which builds on Cavalcanti (2018) and Pearl; neither is held here.
It continues [LIT-842](../literature.d/LIT-842.md). That paper used a few hand-chosen phrases to test
contextuality. This one uses 90 systems built systematically from
psycholinguistic word lists, and it measures signalling. The two share
adopt/boxer and throw/pitcher, and their numbers agree. [NOTE-645](NOTE-645.md)
summarises this paper from [LIT-842](../literature.d/LIT-842.md)'s side. This reading confirms its
figures, and adds that the 95% claim is one-sided at best and that the
overall verb-dominance claim does not survive the appendix. The
psycholinguistic findings it appeals to (Frazier and Rayner 1990,
Pickering and Frisson 2001b) are cited, not tested.

## Bearing on the record

- **It produces [THEORY-177](../theory.d/THEORY-177.md)**: in binary systems the CbD signalling
  measure is the minimal causal direct influence of context. The
  record's CbD readings ([LIT-777](../literature.d/LIT-777.md), [NOTE-600](NOTE-600.md)) hold the maximal coupling, so
  they hold the total-variation half. They do not hold its identification
  with direct influence in a causal model.
- **[CLAIM-125](../claims.d/CLAIM-125.md)** (transport between empirical models is open for
  signalling data). This paper does not address transport between
  scenarios, so it does not settle the claim's second part. It bears on it
  in two ways. It shows that natural-language meaning-selection data are
  heavily signalling: mean Δ is 1.35 out of a possible 4, and about half
  of these rank-2 systems are signalling enough (Δ ≥ 2) to be
  noncontextual automatically. So the signalling case is the typical
  case for language, not an edge case. It also gives a quantity a transport
  could be asked to carry or bound: per-content minimal direct influence,
  which is a total-variation distance with a causal reading. Whether
  simulations between scenarios can increase it is not asked.
- **[CLAIM-037](../claims.d/CLAIM-037.md)** (formal contextuality needs CbD when marginals shift).
  Consistent and reinforced: 69 of the 90 systems are signalling, and 18
  of the 21 with Δ = 0 have err(Δ) of 1 or more, so even those are not
  evidence of non-signalling.
- **[THEORY-013](../theory.d/THEORY-013.md).** No bearing on its verdict. No system is tested for
  contextuality, and the two contextual ones are [LIT-842](../literature.d/LIT-842.md)'s, already
  weighed in [NOTE-645](NOTE-645.md).
- **[THEORY-168](../theory.d/THEORY-168.md)** (CbD verdicts depend on representation). It is
  illustrated in passing. Restricting each word to two interpretations is
  a dichotomisation choice, and the paper says the ±1 labelling does not
  affect Δ or contextuality. Which two interpretations are kept is not
  discussed.
- No instruction for machine-learning practice; nothing for the
  anthology.

## Limitations

- **Small and degenerate counts.** Counts per system are not reported. 51
  of 90 systems have Δ exactly 0, 2 or 4, and 18 have err(Δ) = 1.41. Both
  patterns suggest one or a few occurrences per context. Eight of the 14
  homonymous-verb shares are exactly 0, 0.5 or 1.
- **Non-independent units.** Systems share verbs and nouns: six
  homonymous verbs supply the 14 systems behind the 70%. The test, if
  there is one, treats them as independent.
- **Unnamed test, one-sided at best.** "More than 95% confidence" holds
  one-sided under a Welch test on the appendix and fails two-sided.
  There is no correction for the several comparisons made (verbs, nouns,
  four classes, standard deviations).
- **Annotation.** The authors labelled the interpretations by hand, with
  no agreement measure. The corpora are British.
- **A context includes the corpus**, so pooling BNC and ukWaC occurrences
  is a modelling choice the paper does not examine.
- **Psycholinguistic interpretation** is by analogy. Δ is a corpus
  statistic, not a processing measure.
- **No contextuality results**, despite the title.
- **Version.** Read from an author copy whose provenance was not
  confirmed. The version of record was not compared.

## Open questions

- Whether the homonymous/polysemous verb difference survives with
  reported counts, a mixed model with verb and noun as random effects,
  and more homonymous verbs.
- Whether minimal direct influence, as a per-content total-variation
  distance, is monotone under the simulations of [THEORY-174](../theory.d/THEORY-174.md). If it were,
  that would be a first step on [CLAIM-125](../claims.d/CLAIM-125.md)'s signalling part.
- Whether a human-judgement version (proposed in §5) gives the same Δ
  levels as corpus frequencies.
- Whether Proposition 1 has a counterpart for non-binary contents, where
  Δ as defined is not available but Δ* (Eq. 5) is (footnote 3).
