---
status: Read
paper: LIT-tmpyy78c
title: 'Identifying Quantum Structure in AI Language'
version: 1
history:
- version: 1
  date: '2026-09-27'
  note: >-
    Read in full (Full text of the published version of record (Entropy
    28(6), 622, CC BY 4.0), read from the PubMed Central / Europe PMC
    full-text XML (PMC13298953), because MDPI's site refused the PDF even
    with a browser-style User-Agent (HTTP 403). I read the abstract, §§1–5,
    Appendix A (the full ChatGPT CHSH conversation), Appendix B (both
    prompts), Appendix C (Gemini's full Winnie-the-Pooh story), and the
    author contributions, data availability, funding and reference list (101
    references). I read Table 4 for rows 1–79, rows 818–822 and the totals
    row. The published table itself omits rows 80–817. I did not see Figures
    1–2 as images, only their captions, because the XML has no rendered
    figures. I did not read the Supplementary Materials (a ChatGPT Pooh
    story and a Gemini H. G. Wells-style story, with their graphs). I did
    not read the arXiv versions (2511.21731 v1, 21 Nov 2025; v2, 1 Jun 2026)
    beyond the v1 abstract, and I read only the abstract of the published
    comment on v1 (Sienicki, arXiv 2601.06104).). The first NOTE on this
    paper, which was seeded from its abstract alone.
date: '2026-09-27'
summary: >-
  Two findings are reported. First, prompted as test subjects on Aerts &
  Sozzo's "The Animal Acts" concept-combination test, ChatGPT and Gemini
  give CHSH values above 2: 4 in a guided conversation, and 2.25 and 3.09
  (ChatGPT) and 2.12 and 4 (Gemini) over 81 prompted repetitions, against
  2.42 for the 81 humans in 2011. Second, the rank–frequency curve of one
  2,861-word Gemini story fits a Bose–Einstein form with energy
  E_i=(i−1)^0.8 far better than a Maxwell–Boltzmann form. The authors take
  these as showing that LLM "code is structurally quantum" (§5). The CHSH
  analysis never checks the strongly context-dependent marginals in its
  own tables. One reported expectation value disagrees with its table. The
  Bose–Einstein fit is numerically a Zipf–Mandelbrot law.
---

<!-- inactive-ok-file: LIT-tmpyy78c — Rejected: the paper this note reads, placed by this reading; the directive lapses when its status changes -->
# NOTE-tmpmpw3u: Identifying Quantum Structure in AI Language

## Contribution

The paper repeats two of the Brussels quantum-cognition group's human-subject analyses with LLMs as the subjects.

- **Bell test.** It runs the 2011 "The Animal Acts" Bell-type test (Aerts & Sozzo) on ChatGPT and Gemini and reports CHSH values above 2 (§2).
- **Word statistics.** It applies the group's "Bose–Einstein statistics of words" rank–frequency fit to a story Gemini wrote (§3).

Around these two small experiments it builds a larger argument: that meaning in human and LLM language is organised by "quantum-like" structure; that LLM intelligence lives in "vector-based semantic spaces" rather than in the neural network; that human and artificial cognition show "evolutionary convergence"; and that this matters for AI safety (§§3–5). §4 is a history of Einstein's light-quanta work, offered as a warrant for "Einsteinian unification" across domains.

## Key insight

The paper wants the reader to hold this picture: word combinations in any meaning-producing system are "entangled", and word counts in any coherent text "condense" like bosons. On this picture, both regularities are signatures of how meaning organises itself, whether the substrate is a brain or an LLM.

What the reading actually supports is narrower. The CHSH sums are computed from response tables whose single-concept marginals change drastically with context. That is exactly the situation in which a CHSH value above 2 is not evidence against a classical model ([LIT-264](../literature.d/LIT-264.md), [THEORY-013](../theory.d/THEORY-013.md)). The "Bose–Einstein" curve, with its fitted constants, reduces over most of its range to a Zipf–Mandelbrot power law, and the Maxwell–Boltzmann alternative is an exponential. The second test is therefore a test of Zipf-likeness, which is long known in human text and unsurprising in an LLM trained on it.

## Assumptions

- **Test design.** The CHSH test is run as a four-context design. Each "measurement" is a forced four-way choice of the best example of *The Animal Acts*, such as Horse/Bear × Growls/Whinnies, with outcomes ±1 assigned to the joint choice (§2). The single-concept measurements A, A′, B, B′ are defined, but no single-concept data are reported for the LLMs.
- **Pitowsky's reading of a violation.** A CHSH violation is taken to prove that no Kolmogorovian (single-sample-space) model generates the correlations (§1, §2, citing Pitowsky 1989/1994). The paper never states the condition this needs: each measurement's marginal distribution is the same in every context in which it appears (no-signalling, or consistent connectedness). The paper never checks that condition.
- **LLM "81 subjects".** The 81 LLM trials are 8 prompts, each asking for 10 "sessions" of the four tests, and 11 in the eighth, all within one response per prompt, with the instruction to disregard previous answers (Appendix B). They are not independent samples.
- **"Energy" of a word.** Energy is defined by the word's frequency rank: E_i = (i−1)^d, with ties among equal counts broken alphabetically (§3). The exponent d is chosen per text for best fit: d = 0.8 for the Gemini story, and d < 1 for short stories and d > 1 for novels "as a rule".
- **Fitting the two curves.** The BE form N(E_i) = 1/(A e^{E_i/B} − 1) and the MB form N(E_i) = 1/(C e^{E_i/D}) each have their two constants fixed by matching total word count N and "total energy" E = Σ N(E_i)E_i (Eqs. 3–6, 10).
- **Story prompting.** The story was produced "after explaining the nature of our research to the LLMs" (§1). §3 says it was written "without any input or constraints from our side".

## Key results

- **Human baseline (Table 1, from Aerts & Sozzo 2011).** E(A,B) = −0.7778, E(A′,B) = 0.6543, E(A,B′) = 0.3580, E(A′,B′) = 0.6296, so CHSH = 2.4197. The paper gives p = 0.0171 from "a single-sample t-test against the value 2" (§2). I recomputed the four expectation values from the table and they match.
- **Guided conversation (Appendix A).** Both LLMs give deterministic answers: Horse Whinnies, Horse Snorts, Tiger Growls, Cat Meows. That yields E(A,B) = −1, the other three = +1, so CHSH = 4, the algebraic maximum and above Cirel'son's bound 2√2. The paper does not remark that 4 exceeds the quantum bound. In this run the A′ answer is Tiger in context A′B and Cat in context A′B′, so each marginal is deterministic and different across contexts.
- **Prompted repetitions (Tables 2–3).** For ChatGPT, prompt 1 ("exploratory") gives CHSH = 2.25 and prompt 2 ("neutral") gives 3.09. For Gemini the paper reports only CHSH = 2.12 (prompt 1) and 4 (prompt 2), with no tables. The averages are 2.67 for ChatGPT and 3.06 for Gemini, called "consistent with" the human results (§2). The paper runs no significance test on any LLM value.
- **Internal inconsistency in Table 3.** The table's A′B row is Tiger Growls 0.778, Tiger Whinnies 0, Cat Growls 0, Cat Whinnies 0.222. That gives E(A′,B) = +1.000, but the text states 0.556. The CHSH of 3.09 uses 0.556; the table as printed gives 3.53. Either the table misplaces a cell (Cat Growls 0.222 would give 0.556) or the text is wrong. Which one is unverified.
- **Marginals depend on context (my recomputation from Tables 1–3; the paper does not report this).** Each line gives the probability of the +1 outcome in the two contexts where the concept appears:

  | Concept (+1 outcome) | Humans | ChatGPT, prompt 1 | ChatGPT, prompt 2 |
  |---|---|---|---|
  | A′ = Tiger (A′B vs A′B′) | 0.864 vs 0.234 | 0.617 vs 0.148 | 0.778 vs 0.037 |
  | B = Growls (AB vs A′B) | 0.308 vs 0.864 | 0.482 vs 1.000 | 0.543 vs 0.778 |
  | B′ = Snorts (AB′ vs A′B′) | 0.889 vs 0.247 | 0.951 vs 0.185 | 1.000 vs 0.037 |
- **Gemini story.** It has 822 distinct words ("energy levels") and N = 2861 words, with E = 145,694.86 at d = 0.8. The top counts are A 132, The 98, To 87, And 58. The BE predictions fit the data closely: A 185.36, The 103.39, Not (rank 79) 6.46 against the observed 7. MB predicts about 23 for the top word and about 10.8 at rank 79 (Table 4, Figs. 1–2). The paper reports no quantitative fit measure (R², χ², likelihood, KS); "almost complete fit" is judged from the plots.
- **The BE fit is a Zipf–Mandelbrot curve (my computation from Table 4).** The top two rows imply A ≈ 1.0054 and B ≈ 235.6, while the largest energy is E_822 ≈ 214.5. So E/B < 1 throughout, and N ≈ B/((i−1)^0.8 + 1.27): a Zipf–Mandelbrot law with exponent 0.8 and shift 1.27, bent only at the tail. This approximation is within about 1% of the BE column at ranks 3 and 8 and within 8% at rank 79. At rank 822 the BE form gives 0.67 against 1.09 for the pure power law, and the data give 1. The MB form, 1/(C e^{(i−1)^d/D}), is a stretched exponential in rank and cannot produce a heavy tail. The paper itself notes the kinship with Zipf's ranking scheme (§3) but claims BE "provides a superior and more fundamental fit". It makes no comparison against Zipf, Zipf–Mandelbrot or any other heavy-tailed form.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | ChatGPT and Gemini, used as subjects on the *Animal Acts* test, give CHSH > 2 (4; 2.25/3.09; 2.12/4) | moderate as a report of numbers; weak as data | Tables 2–3 and Appendix A–B, but no significance test, no model versions or sampling settings, Gemini tables omitted, and the Table 3 A′B row is inconsistent with the stated E(A′,B) |
| C2 | The CHSH violation shows a non-Kolmogorovian probability model underlies LLM concept combination | weak | Pitowsky's theorem is invoked, but the no-signalling / consistent-marginal premise it needs fails badly in Tables 1–3 (e.g. P(Snorts) 1.000 vs 0.037) and is never checked. [LIT-264](../literature.d/LIT-264.md) found the same design's human violation vanishes once this is accounted for |
| C3 | The LLM results are "consistent with" the human ones | weak | Averages across two different prompts (2.67, 3.06) compared by eye with 2.42; no test |
| C4 | Words in Gemini's story follow Bose–Einstein, not Maxwell–Boltzmann, statistics | moderate for "fits BE better than MB"; weak for anything more | Table 4 and Figs. 1–2 on one 2,861-word story, with d fitted and no goodness-of-fit statistic. The other two stories are asserted, in the Supplement (not read). The BE fit is numerically Zipf–Mandelbrot and MB is a straw exponential |
| C5 | The BE pattern arises from meaning rather than syntax or style | assertion | No manipulation separates meaning from syntax, and no shuffled, random-text or grammar-only control is used |
| C6 | d is "a structural parameter", "not a post hoc adjustment for curve-fitting" | assertion | Contradicted by the paper's own procedure: d = 0.8 "gave the best fit" (§3) and varies by text length |
| C7 | "We have demonstrated that this code is structurally quantum and not classical" (§5) | assertion | Does not follow from C1–C4 even if they held. The paper never examines model weights, activations or embeddings |
| C8 | LLM intelligence resides mainly in "vector-based semantic spaces" rather than the neural network; human and LLM cognition show evolutionary convergence; the framework bears on AI safety | assertion / informal argument | §3 discussion and §5. Analogies to Cambrian eye evolution, Word2Vec/GloVe/Transformer history, and Hinton and Tegmark quoted as authorities |
| C9 | Complex Hilbert spaces would "significantly increase" AI expressive power | assertion | §3, from an analogy with quantum interference; no experiment |
| C10 | Human p = 0.0171 for CHSH > 2 | weak | "single-sample t-test against the value 2" on a sum of four expectation values from different-subject contexts; how the test was set up is not given |

## Method

- **Bell test (§2, Appendices A–B).** There are three procedures. (a) A single guided chat walks the LLM through the four coincidence measurements one at a time. The authors reveal their own choices and the CHSH purpose only after the LLM's answers, then discuss entanglement, emotions and intelligence with it (Appendix A). (b) and (c) use one prompt per run, asking for 10 (or 11) independent-as-if "sessions" of the four tests, 8 runs per prompt, to reach 81 trials. Prompt 1 tells the model to "use all aspects of your cognition, including unconventional ones… be also exploratory". Prompt 2 omits that. Expectation values come from the relative frequencies of the four joint choices, and CHSH = E(A′,B′)+E(A′,B)+E(A,B′)−E(A,B).
- **Word statistics (§3).** Count word occurrences in the story (case-folded as far as Table 4 shows, e.g. "It's" and "You're" treated as words). Rank the words by count, breaking ties alphabetically, and set E_i = (i−1)^d. Fix (A,B) for BE and (C,D) for MB by matching N and E, choose d by fit, then compare the curves visually in linear and log–log plots.

## Concepts

- **Cogniton**: the group's "quantum" of language (introduced in Aerts & Beltran 2020); a word in a story is "a state of this cogniton".
- **Energy of a word**: E_i = (i−1)^d for the i-th most frequent word. §3 calls it a base unit, not a physical energy. "Radiated energy" at a level is N(E_i)·E_i.
- **d (energy-spacing exponent)**: read by analogy as the confining "semantic force". d = 1 is the harmonic oscillator, d = 2 the particle in a box, d = −2 the Coulomb case.
- **Semantic condensation**: the over-representation of frequent (mostly function) words at low ranks, read as analogous to Bose–Einstein condensation.
- **Entanglement (as used here)**: Schrödinger's sense that parts of a composite are not independent. Words "combined behave … differently from how they behave in isolation" (§2). Not tied to any test of no-signalling.
- **Einsteinian unification**: the paper's name for the method of seeking common structure across domains (§4).

## Connections

- **Contextuality-by-Default ([LIT-264](../literature.d/LIT-264.md), [THEORY-013](../theory.d/THEORY-013.md)).** This is the decisive connection. Dzhafarov, Zhang & Kujala (2015) re-analysed the human data for this very *Animal Acts* design (the Aerts–Gabora–Sozzo animal/sound choices, their §5). They found that the reported CHSH violation assumed consistent marginals and disappears once inconsistent connectedness is accounted for. The present paper reuses the design and the 2011 human data without citing that critique, and its LLM tables show even larger marginal shifts. In the guided-conversation run every variable is deterministic, and on my reading of the Contextuality-by-Default definition a system of deterministic variables always admits the trivial coupling, so it cannot be contextual. That reading is mine, not stated by [LIT-264](../literature.d/LIT-264.md). [THEORY-013](../theory.d/THEORY-013.md)'s promote_when already says "A CHSH-type violation computed without accounting for unequal marginals cannot settle it either way". This paper is such a violation, and it does not bear on [THEORY-013](../theory.d/THEORY-013.md) in either direction.
- **Sheaf-theoretic contextuality ([LIT-016](../literature.d/LIT-016.md), [THEORY-012](../theory.d/THEORY-012.md)).** The global-section characterisation in [LIT-016](../literature.d/LIT-016.md) / [THEORY-012](../theory.d/THEORY-012.md) is proved for no-signalling empirical models only. The paper's data sit outside that class, so Pitowsky / Fine-style "no joint distribution" conclusions do not apply as stated. The seeded [LIT-263](../literature.d/LIT-263.md) (Budroni et al. review) and [LIT-265](../literature.d/LIT-265.md) (contextual fraction) say the same from the physics side and are restricted to consistently connected models. The paper cites Pitowsky and Boole but none of this literature on signalling data. It does cite Bruza et al. 2023 on contextuality in cognition (ref. 37) without engaging its method.
- **Quantum and vector models of meaning ([LIT-262](../literature.d/LIT-262.md), [LIT-208](../literature.d/LIT-208.md)).** van Rijsbergen's geometric IR ([LIT-262](../literature.d/LIT-262.md)) and the distributional-semantics account of meaning ([LIT-208](../literature.d/LIT-208.md)) are the serious versions of the "meaning lives in vector spaces" theme of §3. The paper gestures at the same lineage (Harris, Firth, LSA, Word2Vec, GloVe) but adds no formal link between LLM embeddings and its Bell or BE results.
- **Classical accounts of power-law word statistics ([LIT-013](../literature.d/LIT-013.md)).** The Pitman–Yor process ([LIT-013](../literature.d/LIT-013.md)) is a classical generative model that produces power-law word frequencies. It illustrates what the paper does not test against: a heavy-tailed rank–frequency curve has classical explanations, which the paper acknowledges only as "stochastic processes with innovation [75]".
- **Anthology of the SOTA.** Nothing in ML practice bears on it; no ANTH- document is relevant.

## Bearing on the record

- **No THEORY is supported.** The paper is a further instance of the pattern [THEORY-013](../theory.d/THEORY-013.md) describes: a CHSH-type number reported as non-classicality in behavioural (here, LLM-behavioural) data without the marginal check. It is worth citing in [THEORY-013](../theory.d/THEORY-013.md)'s body as a 2026 example that the critique had not reached. It is not evidence for or against [THEORY-013](../theory.d/THEORY-013.md)'s claim.
- **No ML-practice content.** The only practice-shaped claim is that moving AI to complex vector spaces "could significantly increase their expressive power" (§3). It is an untested assertion and does not belong in the Anthology.
- **For filing.** File under `cognition` first. `contextuality` is justifiably appropriate because the Bell/CHSH analysis is a contextuality claim, and a browser of that topic should see this counter-example to careful practice. `linguistics` fits the word-statistics half. `quantum-foundations` is not proposed: the paper borrows formalism, and says nothing about physics foundations beyond the §4 history.

## Limitations

- **The no-signalling premise is never checked.** The CHSH analysis never states or tests it, although Tables 1–3 violate it heavily. So the step "violation ⇒ non-Kolmogorovian" (Pitowsky) is not licensed.
- **Guided CHSH = 4 exceeds the quantum bound.** It is presented as a violation "maximally" of CHSH, with no comment that it lies beyond the Cirel'son bound 2√2. Such values are therefore not "quantum" either. The group's own earlier chapter on violations "beyond Cirel'son's bound" (ref. 29) is cited but not used.
- **Weak statistical and reporting practice.** LLM trials are not independent (10 per generation). Model versions, dates and sampling parameters are missing from the body. Gemini tables are omitted, there are no LLM significance tests, and the Table 3 A′B row disagrees with its stated expectation value.
- **The word-statistics test is on one story, primed by the research topic.** The model had been told "the nature of our research" (§1), and the story is about words that "bunch up" like "tiny little pieces of light or very cold atoms" (Appendix C). "Words" is the 16th most frequent word (28 occurrences) and "Meaning" occurs 9 times. §3's statement that the story was written "without any input or constraints from our side" sits uneasily with §1.
- **No goodness-of-fit statistic, and d is fitted.** The paper then calls d not a curve-fitting adjustment. There are no controls: no shuffled, random-typing or non-meaningful text. Without them, "meaning, not syntax, produces BE" (C5) is untested. Zipf-like curves are known to arise in texts with no meaning.
- **The large claims do not follow.** §§3–5 (code "structurally quantum", evolutionary convergence, AI safety, cosmic cognition, interstellar-dust coherence) are argued by analogy and authority, not from the two experiments. Appendix A shows the authors steering ChatGPT towards agreement ("you possess human intelligence in the genuine sense of the word"), which is not a measurement procedure.

## Open questions

- **Does anything survive the marginal check?** Would a Contextuality-by-Default analysis (or any signalling-aware criterion) of the LLM *Animal Acts* data find contextuality once marginal shifts are accounted for? That analysis could be run directly on Tables 2–3 once the Table 3 inconsistency is resolved.
- **Does BE beat the standard heavy-tailed laws?** Does the BE form beat Zipf–Mandelbrot (same parameter count once d is counted) on held-out texts, by likelihood or an information criterion? And does it separate meaningful text from shuffled or random-typing text of the same length? Only such a comparison could make the Bose–Einstein reading more than a re-parameterisation.
- **Do the numbers replicate?** Do the reported values replicate across model versions, independent sessions and sampling temperatures, with those settings reported?

## Corrections to the seeded skim

- none (there was no seed or dossier for this work)
- Identification note for filing: the work has an arXiv preprint, 2511.21731 (v1 21 Nov 2025, v2 1 Jun 2026), which the task brief did not mention. The v1 abstract said the CHSH violation "indicates the presence of 'quantum entanglement' in the tested concepts". The published abstract says instead that it "indicates the presence of a 'non-classical probability model'". A published comment on v1 exists: Sienicki, arXiv 2601.06104, "a friendly technical check" that says the CHSH and Bose–Einstein interpretations "go beyond what the stated procedures can firmly support". Only its abstract was read.
- The published abstract names "ChatGPT (GPT-5.5 Thinking)" and "Gemini Advanced (Gemini 1.5 Pro)". The body names no model version, date, interface or sampling setting anywhere. The v1 abstract (Nov 2025) names only "ChatGPT and Gemini". Which model produced which result is unverified.
