---
number: 645
status: Read
formerly:
- NOTE-tmpj1l5b
paper: 'LIT-842'
title: 'On the Quantum-like Contextuality of Ambiguous Phrases'
version: 2
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the arXiv PDF (2107.14589v1, 6 pages, text layer
    extracted): abstract, §§1–9, every table and the reference list. The
    ACL Anthology PDF (2021.semspace-1.5) was compared with it by the
    vocabulary of the two text extracts and the figures of §8; they
    differ only in the Anthology's header. The possibilistic analysis of §5.2 (global
    assignments of the tap/box model) was redone by hand; the CbD
    quantities of §8.1 were recomputed from Fig. 12 (Δ = 56/30 and 13/15,
    excesses 4/30 and 28/30 over Δ, in the ratio 1 : 7 of the reported
    1/30 and 7/30); the row sums of Figs. 9–12 were checked. The linear
    program of §8 and the bootstrap of §8.1 were not rerun. Also read in
    full, for comparison, the journal follow-up (Journal of Cognitive
    Science 22(3):391–420, author copy from UCL Discovery, 33 pages):
    §§1–5, Proposition 1 with its proof, and the dataset of Appendix A.
    Cited works not read: Kujala and Dzhafarov 2016, Dzhafarov, Kujala
    and Cervantes 2020, Jones 2019, Wang's 2020 MRes thesis.
- version: 2
  date: '2026-10-09'
  note: >-
    Corrected the account of the journal follow-up, at the owner's
    request, after its own reading (NOTE-654, LIT-851). The verb-share
    difference was given here as "significant at 95%". The paper names no
    test; recomputed from its appendix, a Welch t-test gives t = 2.00, df
    ≈ 20, p ≈ 0.03 one-sided and ≈ 0.06 two-sided, on 14 homonymous-verb
    systems from six verbs against 55. Over all 69 signalling systems the
    verb share is 0.52 ± 0.04, so verbs do not carry more of Δ in general.
date: '2026-10-09'
summary: >-
  Models meaning selection in two-word ambiguous phrases as a Bell-type
  measurement scenario. Hand-set supports give one possibilistically
  contextual (Hardy-type) model; every corpus-estimated model is
  signalling, so only Contextuality-by-Default applies, under which two
  noun–verb pairs read in both grammatical orders are contextual (1/30
  and 7/30). The paper's own bootstrap leaves both plausibly
  noncontextual (probabilities above .56 and .08), on very small counts.
---

<!-- inactive-ok-file: THEORY-013 — Proposed; cited for what this reading bears on, not as settled -->
<!-- inactive-ok-file: CLAIM-009 CLAIM-037 CLAIM-038 CLAIM-044 — Proposed; open, and cited as open: the claims this reading bears on -->

# NOTE-645: On the Quantum-like Contextuality of Ambiguous Phrases

## Contribution

Before this paper the quantum-cognition literature had tested concept
combinations ("apple chip", Bruza et al.) for contextuality, and
Dzhafarov and colleagues had found none of them contextual once
signalling was accounted for ([LIT-264](../literature.d/LIT-264.md)). This paper puts two-word
ambiguous phrases of English into the sheaf-theoretic and
Contextuality-by-Default frameworks, with meanings estimated from corpus
frequencies. It shows that a non-signalling, possibilistically
contextual language model can be written down. It shows that corpus
estimates are signalling in every case examined. And it reports the
first CbD-contextual systems from language data, which its own bootstrap
does not secure.

## Key insight

Treat each ambiguous word as a measurement and its selected meaning as
the outcome; a phrase is a joint measurement. Then "context changes
meaning" splits into two different things. The marginal for a word can
shift between phrases (signalling, a direct influence of the partner
word), or the joint selections can fail to come from any one global
assignment beyond what those shifts allow (contextuality). Language data
show plenty of the first. The second needs CbD to be asked at all.

## Assumptions

- **Two meanings per word**, or three in the press/box model, chosen by
  the authors; other senses and metaphorical readings are ignored (§4
  footnote 2, §9).
- **Supports by judgement.** The possibilistic models of §5 encode which
  readings the authors judge possible; they are not observed.
- **Probabilities by hand annotation of corpus hits.** In §6 each
  occurrence of a phrase in the BNC or ukWaC is assigned a reading by the
  authors. No annotator agreement is reported.
- **A context is a word pair plus its grammatical relation.** In §5.4
  the verb–object and subject–verb readings of one noun–verb pair are
  two contexts sharing both contents, so the same word counts as the same
  measurement in both orders.
- **Binary outcomes** for the CbD cyclic criterion; the three-outcome
  model is handled by dichotomization.

## Key results

- **§5.1 {coach, boxer} × {lap, file}** is possibilistically signalling:
  coach = bus is possible with lap and not with file. The sheaf criterion
  cannot be applied.
- **§5.2 {tap, box} × {pitcher, cabinet}** is possibilistically
  non-signalling and contextual. The constraints force tap = box =
  pitcher and cabinet the other value, so there are exactly two global
  assignments, and the locally possible (tap = touch, pitcher = baseball
  player) extends to neither. The paper's phrasing, that "tap ↦ touch"
  cannot be extended, is loose: tap = touch extends; the pair does not.
  This is Hardy-type (possibilistic) contextuality, not strong.
- **§5.3 {press, box} × {can, leaves}** is possibilistically
  non-signalling and noncontextual; §5.4's two noun–verb pairs are
  possibilistically signalling.
- **§6 corpus versions.** All are probabilistically signalling, e.g.
  P(box = put in boxes) is 2/3 in "box leaves" and 7/74 in "box can"
  (Eq. 1). The tap/box model's corpus support also differs from §5.2's.
- **§8 CbD.** press/box is noncontextual by a feasible linear program
  (105 constraints on 2¹⁶ events; the extraction prints "216"); coach/
  boxer and tap/box are noncontextual by the Kujala–Dzhafarov cyclic
  inequality.
- **§8.1 noun–verb pairs.** adopt/boxer and throw/pitcher are
  CbD-contextual, with measures 1/30 and 7/30. Recomputed here from
  Fig. 12: for adopt/boxer the two contexts' correlations are −1 and +1,
  so s_odd = 2, against Δ = 56/30; for throw/pitcher s_odd = 1.8 against
  Δ = 13/15. The excesses, 4/30 and 28/30, stand in the paper's 1 : 7
  ratio; its measure is a quarter of the excess.
- **§8.1 reliability.** Parametric bootstrap: the probability of a
  noncontextual system given these estimates is "larger than .56" for
  adopt/boxer and "larger than .08" for throw/pitcher.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | A two-word ambiguous-phrase scenario can be possibilistically non-signalling and contextual | strong, for the hand-set supports | §5.2, checked here |
| C2 | Corpus-estimated meaning-selection models are signalling | moderate | every model examined (§§6–7), a handful of phrases |
| C3 | Signalling models of ambiguous phrases can be CbD-contextual | weak | §8.1: two systems on small counts, both plausibly noncontextual by the paper's own bootstrap |
| C4 | There is no reason for language to satisfy non-signalling | informal argument | §7, the coach/lap example |
| C5 | Contextuality frameworks let the effect of context on interpretation be studied formally | programme statement | §9 |

## Concepts

- **measurement / outcome**: an ambiguous word / the meaning selected
  for it in a phrase.
- **measurement context**: the words of a phrase together with their
  grammatical relation (subject–verb, verb–object, adjective–noun).
- **possibilistically contextual (logical contextuality)**: some locally
  possible joint outcome belongs to no consistent global assignment
  (after Abramsky and Hardy).
- **signalling**: a word's meaning distribution differs between the
  contexts it occurs in; in CbD terms, inconsistent connectedness.
- **CbD-contextual**: no coupling of all contexts makes each word's
  copies agree with the maximal probability their marginals allow.

## Connections

The scenario and the possibilistic criterion are Abramsky and
Brandenburger's ([LIT-016](../literature.d/LIT-016.md)), with bundle diagrams from Abramsky et al.
([LIT-278](../literature.d/LIT-278.md)). The probabilistic criterion is Contextuality-by-Default
([LIT-777](../literature.d/LIT-777.md)) through the cyclic-system results of Kujala and Dzhafarov
(2016) and the measures of Dzhafarov, Kujala and Cervantes (2020),
neither held. The rank-2 noun–verb design is modelled on question-order
effects (Wang and Busemeyer, [LIT-834](../literature.d/LIT-834.md)), which CbD had already found
noncontextual ([LIT-264](../literature.d/LIT-264.md)). The paper does not cite Abramsky and
Sadrzadeh's Semantic Unification ([LIT-841](../literature.d/LIT-841.md)); the journal follow-up names
it only as a future direction. The two works share an author and a
framework, not a construction: [LIT-841](../literature.d/LIT-841.md) glues discourse sections, this
paper tests distributions over word meanings.

The journal follow-up (Wang et al., Journal of Cognitive Science 2021,
read in full) changes the question. Across 90 rank-2 noun–verb systems
it measures direct influence, Δ, which by its Proposition 1 is twice the
sum over contents of Jones's minimal direct influences. Verbs with
several meanings carry about 70% of Δ (0.70, on 14 systems from six
verbs), verbs with several senses about 50% (0.48, on 55), and nouns
about 50% either way. The paper calls the difference significant with
"more than 95% confidence" but names no test; recomputed, it holds only
one-sided (Welch p ≈ 0.03; two-sided ≈ 0.06), and over all 69 signalling
systems the verb share is 0.52 ± 0.04 ([NOTE-654](NOTE-654.md)). It
notes that Δ > 2 rules out contextuality in rank-2 systems, and it
reports no new contextual system. Its conclusion prints the earlier
measures garbled in extraction; they are the 1/30 and 7/30 here.

## Bearing on the record

- **[THEORY-013](../theory.d/THEORY-013.md)** (behavioural, social and word-meaning data published as
  contextual show none once signalling is separated). This paper is the
  first claim of CbD contextuality in language data. It does not meet
  [THEORY-013](../theory.d/THEORY-013.md)'s `promote_when` the other way: its own bootstrap gives
  noncontextuality a probability above .56 and .08. The record should
  not cite it as a robust counterexample. The candidate that might be is
  the 2025 BERT study by Lo, Sadrzadeh and Mansfield (not held), whose
  distributions come from a language model, not from people or corpora.
- **[CLAIM-044](../claims.d/CLAIM-044.md)** (ambiguity admits several global assignments,
  contextuality none). Here ambiguity is the outcome set and is never by
  itself contextual: press/box has several readings and global
  assignments for all of them. But the one contextual model, tap/box,
  is possibilistically contextual and still has two global assignments.
  What fails is that one locally possible reading extends to none. So
  "a contextual one admits none" holds only for strong contextuality.
  Possibilistic and probabilistic contextuality are compatible with
  global assignments existing.
- **[CLAIM-037](../claims.d/CLAIM-037.md)** (formal contextuality needs Contextuality-by-Default when
  marginals shift). Supported directly: every corpus model was
  signalling, and the sheaf criterion could not be applied to any.
- **[CLAIM-038](../claims.d/CLAIM-038.md)** (a communicative object is a compatible family over a
  cover). The data here are not compatible families: meaning marginals
  disagree on overlaps. Applied to language, the claim's premise of
  compatibility needs either CbD or a signalling-corrected sheaf
  treatment, as in Lo et al.'s later work.
- **[CLAIM-009](../claims.d/CLAIM-009.md)** (pragmatic judgements may be formally contextual). The
  paper tests lexical meaning selection, not pragmatic judgement. Its
  contextual systems are not secured. It shows the test can be run on
  language data; it is not evidence that the supposition holds.
- **[CLAIM-041](../claims.d/CLAIM-041.md)** (context sensitivity does not by itself establish
  contextuality). Consistent: the bulk of what the data show is
  signalling.
- No instruction for machine-learning practice; nothing for the
  anthology.

## Limitations

- A handful of phrases, chosen by hand, with two meanings each.
- Supports in §5 are the authors' judgements, and the corpus readings
  are their annotations, with no agreement measure.
- Small counts throughout: the contextual systems rest on fractions with
  denominators of 3 to 30, and the bootstrap leaves both plausibly
  noncontextual.
- British corpora: the bus sense of coach was nearly absent (§9).
- Possibilistic contextuality appears only in a model whose supports are
  stipulated; once estimated from the corpus it is signalling.
- One printed error: in Fig. 10a the tap/pitcher row reads 17/22 and
  15/22, which sum to 32/22; one entry is wrong, probably 7/22.

## Open questions

- Whether CbD contextuality in ambiguous phrases survives with human
  plausibility judgements and adequate sample sizes. The authors
  propose this (§9). Wang and Sadrzadeh's 2023 human-judgement data, and
  Lo et al.'s crowdsourced Winograd schemas, would answer it in part.
- Whether treating "adopt" in "adopt boxer" and "boxer adopts" as one
  content is right. If the grammatical role changes what is measured,
  the rank-2 systems are not about one property in two contexts.
- Whether any non-signalling language system exists outside stipulated
  supports.
