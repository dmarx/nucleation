---
number: 72
status: Read
formerly:
- NOTE-tmprvi4j
paper: LIT-090
title: 'Hance et al., wavefunctions as knowledge and reality'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (full text of arXiv:2101.06436v4 (27 Apr 2022, "Matches
    published version"), 7 pp. I read §I–V (pp. 1–5), the acknowledgements
    and statements, references [1]–[42] (pp. 5–6), and Appendix A, "Issues
    with an Assumed Underlying State λ" (pp. 6–7). I extracted the text with
    PyMuPDF into raw4/2101.06436.txt. Figure 1, the overlap vs.
    disjoint-supports cartoon, came through as caption only. I did not
    compare the Springer version (DOI 10.1007/s40509-022-00271-3). Nothing
    was skipped.). Upgraded from `Skimmed` to `Read`: the claims table,
    assumptions and results are new, and the skim is corrected where the
    full text disagreed.
date: '2026-09-25'
summary: >-
  The paper argues, informally and without formal results, that
  Harrigan–Spekkens' ψ-ontic/ψ-epistemic are contradictories only by
  stipulation. On the informal senses, "represents reality" and
  "represents knowledge", a wavefunction can be both. It offers a weaker
  sufficient condition for "epistemic" (Eq. 6: for some ψ, A, S, the
  response function A(S|λ) is not equal to the Born probability p^ψ_A(S)
  throughout Λψ), which non-overlapping models can meet. It concludes that
  PBR "shows that wavefunctions cannot overlap on state space, but it says
  nothing about whether they are epistemic in the broader sense", so it
  "does not rule out all epistemic models" (§V).
---

# NOTE-072: Hance et al., wavefunctions as knowledge and reality

## Contribution

The paper makes a conceptual/terminological argument; it contains no theorem. It argues three things. (1) The informal notions "ontic" (pertaining to what exists) and "epistemic" (pertaining to knowledge) are not exclusive: thermodynamic entropy and proper mixtures are offered as terms that are both (§II). (2) Harrigan–Spekkens' formal definitions make ψ-ontic and ψ-epistemic contradictories by stipulation (§III). (3) Overlap is sufficient but not necessary for an epistemic reading, so the ψ-ontology theorems (PBR, Colbeck–Renner, Hardy, Patra et al., Ruebeck et al.) exclude overlap, not epistemic interpretations as such (§IV–V). Appendix A adds a list of doubts about the ontological-models framework itself.

## Key insight

"ψ-epistemic" in the no-go literature is a technical term: supports overlap. It is weaker than the informal thesis "ψ represents knowledge". A ψ-ontic model, one with no overlap, may still have ψ represent an observer's partial knowledge of a finer ontic state. So PBR-type results bound the *geometry* of µ_ψ, not the interpretation of ψ.

## Assumptions

The argument relies on:
- **Informal definitions (§II, p. 2).** A term is *ontic* when "taken to represent how the world is independently of our knowledge of it to some extent or other". It is *epistemic* when "taken to represent knowledge or information about the world to some extent or other". The two are explicitly non-exclusive, and both are matters of degree ("to some extent").
- **Ontological-models framework as restated (§III).** Response functions A(S|λ); distributions p(λ|ψ) normalised on the support Λψ; the Born rule p^ψ_A(S) = Σ_S |⟨s|ψ⟩|² = ∫ A(S|λ)p(λ|ψ)dλ (Eq. 1); eigenstate determinism for ψ's own projector on Λψ (Eq. 2). The framework's probabilities are nonnegative.
- **Overlap quantity (Eq. 4).** ∆ ≡ ∫_{Λψ} p(λ|ϕ)dλ ≤ |⟨ψ|ϕ⟩|². Here ∆ is a number, not PBR's region.
- **ψ-ontic defined as** disjoint supports: Λψ ∩ Λϕ = ∅ for ψ ≠ ϕ (Eq. 5). The paper's gloss of Harrigan–Spekkens' ψ-complete/ψ-supplemented taxonomy (p. 3) is garbled: it calls them "three subcategories of ψ-ontic model" and then describes two ψ-supplemented cases. I have not checked this against Harrigan–Spekkens, so it is unverified.

## Key results

There are no theorems. The load-bearing statements:
- **Eq. 6 (p. 4).** ∃{ψ, S, A}: ¬(A(S|λ) = p^ψ_A(S) ∀λ ∈ Λψ) ⟹ epistemic. Offered as a sufficient condition. Overlap implies it: on Λψ, A(ψ|λ) = 1 but p^ϕ_A(ψ) = |⟨ψ|ϕ⟩|² < 1. Non-overlapping models can satisfy it too.
- **§IV conclusion.** "There is nothing in Harrigan and Spekkens' formal definition for a model being ψ-ontic, nor a criterion we can build from their model, which is necessary or sufficient for a model to have wavefunctions representing reality" (p. 4).
- **§V conclusion.** PBR and the other no-go theorems "do not rule out all epistemic models". The formal terms "do not formalise these informal ideas", and people should not "conflate" the two (p. 5).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Informal "ontic" and "epistemic" are not mutually exclusive | informal argument | §II: entropy (Wallace, Ladyman et al.) and proper mixtures as examples |
| C2 | Harrigan–Spekkens define ψ-ontic/ψ-epistemic as contradictories without argument | informal argument | §III–IV; footnote 3 cites a referee and Bohr, Heisenberg, Friederich, Schrödinger for a history of "both" readings |
| C3 | Overlap is sufficient, not necessary, for an epistemic reading; Eq. 6 is a weaker sufficient condition | informal argument | §IV. Eq. 6 is proposed, not derived from the informal definition |
| C4 | Models can be ψ-ontic and epistemic at once (ψ-dependent models; Schlosshauer–Fine) | assertion (citation) | p. 4, [36]; no model given |
| C5 | PBR and related theorems rule out overlap only, not epistemic interpretations in the broad sense | moderate | Follows from C3 if C3 is granted, and is compatible with PBR's own text, which leaves the QBist option open (PBR p. 5) |
| C6 | Colbeck–Renner–Leegwater does not exclude Eq. 6 cases | assertion (citation) | Footnote 8, relying on Hermens [21] |
| C7 | Real-point ontic states "enforce locality of hidden variables, so violate Bell's theorem" | assertion | App. A; no argument; the framework does not require locality |
| C8 | Non-negative ontological models cannot evidently reproduce Elitzur–Vaidman or counterfactual communication | assertion | App. A. Contradicted for the bomb tester by [LIT-019](../literature.d/LIT-019.md)'s explicit model |
| C9 | Spekkens' measurement-disturbance account "sounds like superdeterminism-by-stealth" | assertion | App. A; no citation to the Spekkens text criticised |

## Concepts

- **Ontic / epistemic (informal, this paper).** See Assumptions. Both hold "to some extent", and they are not exclusive.
- **ψ-ontic / ψ-epistemic (Harrigan–Spekkens, as reported).** Disjoint supports vs. overlap for some pair (Eqs. 4–5).
- **Eq. 6 epistemic.** ψ does not fix every response function on its support. Equivalently, λ can predict some measurement better than ψ does.
- **ψ-dependent model.** A model whose response functions depend on ψ as well as λ (Schlosshauer–Fine [36]). Its individual overlap possibilities are "given by the relevant measurement probabilities, rather than being uniform" (p. 4).
- **"Mixed"/"Segregated".** Schlosshauer–Fine's alternative names for overlap / non-overlap, which the authors prefer (footnote 7).

## Connections

- **[LIT-062](../literature.d/LIT-062.md) (PBR; reads/c20.md).** The paper positions itself as a reinterpretation, not a refutation. It accepts PBR's result "given certain assumptions" and "even if those assumptions are valid" (§V, pp. 4–5). It never discusses preparation independence or any other PBR assumption. Its point is that PBR's conclusion is about overlap. That matches PBR's formal definition ("can justifiably be regarded as 'mere' information", PBR p. 2), and cuts against PBR's abstract, whose informal wording ("represents mere information") is broader than the theorem (c20 claim C6).

  The paper does not engage with the reason PBR gives for the overlap criterion, namely that without overlap ψ "can be inferred uniquely from the physical state" (PBR p. 2). Its answer to the parallel Hardy statement is the fingers-and-numbers analogy (p. 4).
- **[LIT-007](../literature.d/LIT-007.md) (Quasi-quantization; reads/14.md).** Not cited, though Spekkens 2005 and 2007 are ([39], [40]). The two papers diverge on a specific point. [LIT-007](../literature.d/LIT-007.md) is the source of the Harrigan–Spekkens distinction ("it was the work on epistricted theories that led to the articulation of the distinction", [LIT-007](../literature.d/LIT-007.md) §I.C), and its defence of the epistemic view is a defence of ψ-epistemicity in the overlap sense: nonorthogonal pure states "correspond to two probability distributions that overlap on one or more ontic states". This paper would count that as one sufficient route to an epistemic reading among others.

  Both papers leave room for the epistemic view after PBR, but by different routes. [LIT-007](../literature.d/LIT-007.md) drops the ontological-models framework's classical probability while keeping ψ epistemic. This paper keeps the framework and loosens the word "epistemic". Appendix A here also doubts the framework, on the ground that non-negative probabilities cannot reproduce interference effects. [LIT-007](../literature.d/LIT-007.md)/[LIT-019](../literature.d/LIT-019.md)'s programme is built on the opposite claim for the weakly nonclassical phenomena.
- **[LIT-019](../literature.d/LIT-019.md) (interference paper; reads/17.md).** Directly relevant to Appendix A, claim C8. [LIT-019](../literature.d/LIT-019.md) gives an explicit local, deterministic, non-negative, ψ-epistemic (overlap-sense) model that reproduces the Elitzur–Vaidman bomb tester and the Mach–Zehnder statistics. It also answers Hance & Hossenfelder's comment on its preprint ([92] there, reads/17.md). This paper, v4 dated April 2022, cites neither [LIT-019](../literature.d/LIT-019.md) (arXiv Nov 2021) nor that exchange. It cites Hance & Hossenfelder 2021 only for terminology ([15]).
- **[LIT-003](../literature.d/LIT-003.md) and [LIT-016](../literature.d/LIT-016.md).** No connection in the text. The paper does not discuss noncontextuality or sheaf-theoretic contextuality.
- **[LIT-054](../literature.d/LIT-054.md) (c16).** Not cited. c16's informal gloss of ψ-epistemic ("not real: only an artefact of restricted knowledge") is exactly the exclusive reading this paper argues against.
- **Cited literature.** The paper leans on Leifer's review [26] and Friederich [9] as the exclusive definitions it criticises, on Myrvold [28] as independent precedent (footnote 2), on Oldofredi–López [29] for further framework issues, and on Hermens [21, 22].

## Bearing on the record

- A caution for any THEORY or LIT summary in the cluster that paraphrases PBR as "the quantum state is not knowledge". The defensible paraphrase is "not ψ-epistemic in the Harrigan–Spekkens (overlap) sense, given preparation independence". This paper is a citable source for that distinction, alongside PBR's own p. 5.
- It should **not** be cited as evidence that ontological models cannot reproduce interference or bomb-testing (App. A). [LIT-019](../literature.d/LIT-019.md) shows otherwise for the fragment it models.
- Nothing here bears on ML practice. No ANTH- document is implicated.

## Limitations

- **No formal result.** Eq. 6 is a proposed sufficient condition with no derivation from the informal definition, and its content is predictive incompleteness of ψ (see corrections). Under it, Bohmian mechanics is "epistemic", in tension with §I.
- **"To some extent" makes the informal definitions graded and nearly unfalsifiable.** Almost any term in physics is both ontic and epistemic "to some extent". The paper does not say what would count against its thesis.
- **The Schlosshauer–Fine example** is asserted, not reproduced (C4).
- **Appendix A** makes strong claims against the framework without argument (C7, C9). One of them is contradicted by a paper in this record (C8).
- It does not engage PBR's assumptions, or the Spekkens-school response (reject the framework, keep ψ epistemic), which it could have used.

## Open questions

- A necessary-and-sufficient formal criterion for "ψ represents knowledge" within ontological models, or an argument that none exists. The paper says only that Harrigan–Spekkens' is not it.
- Whether Eq. 6 "epistemic" models of full quantum theory survive the Colbeck–Renner–Leegwater line. The paper relies on Hermens' critique [21] and does not settle it.
- Whether the Appendix A doubts survive [LIT-019](../literature.d/LIT-019.md)'s explicit non-negative model of the bomb tester, and which of the interference effects it lists (counterfactual communication, imaging) fall outside that model's fragment.

## Corrections to the seeded skim

- The dossier covers §I–V and **misses Appendix A (pp. 6–7)**, which carries the paper's most contestable claims:
  - (i) Associating a single point of a state space with "a real quantum state-of-the-world … enforces locality of hidden variables, so violates Bell's theorem". Bohmian mechanics is the exception the authors name.
  - (ii) Spekkens' account of measurement disturbance via the apparatus' initial state "sounds like superdeterminism-by-stealth".
  - (iii) Ontological models use nonnegative probabilities, whereas "negative probability interference" explains the Elitzur–Vaidman bomb detector and counterfactual communication/imaging. It is "unclear how the real non-negative probabilities of this real underlying state-of-the-world could replicate these effects – casting doubt on this framework".

  Claim (iii) is contradicted by [LIT-019](../literature.d/LIT-019.md), which gives an explicit nonnegative, local, ψ-epistemic model reproducing the Elitzur–Vaidman bomb tester (success probability ¼, reads/17.md). [LIT-019](../literature.d/LIT-019.md) also answers a Hance & Hossenfelder comment directly (its ref. [92], reads/17.md). Claim (i) is asserted without argument, and the ontological-models framework does not in general impose locality; PBR's own models are unrestricted in this respect (reads/c20.md).
- The dossier says "ψ-dependent models (Schlosshauer–Fine) are exhibited as both ontic and epistemic". **Nothing is exhibited.** The paper describes the idea: the response function depends on ψ, and the simplest case is p_ψ uniform on Λψ. It then asserts that "Schlosshauer and Fine give an ontic model which is also ψ-epistemic", citing [36] (p. 4). No model is written down or checked.
- The dossier's own open question, whether Eq. 6 "just relabels incompleteness … as 'epistemic'", can be answered from the text: essentially yes. Eq. 6 holds exactly when, for some measurement, the ontic state carries more predictive information than ψ, i.e. when ψ is not predictively complete. Footnote 8 concedes as much: it notes that the Colbeck–Renner–Leegwater theorem "claims to prohibit cases like this, where the quantum state does not provide a full description for the prediction of future measurement outcomes", and relies on Hermens [21] to dismiss it. By Eq. 6, any deterministic hidden-variable model of a state with non-trivial Born probabilities counts as "epistemic", **Bohmian mechanics included**. Yet §I (p. 1) lists Bohmian mechanics among interpretations that take the wavefunction "not to be epistemic in any way". This internal tension is my inference: the paper does not apply Eq. 6 to Bohm.
- The dossier says §IV rejects Hardy's "deduce ψ from λ" argument "via the fingers-and-numbers analogy". That is right, but it is the whole of the rejection. The analogy (p. 4; footnote 4, p. 2) is the only argument given that non-overlap does not make ψ "written into" reality.
