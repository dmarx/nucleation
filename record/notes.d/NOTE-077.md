---
number: 77
status: Read
formerly:
- NOTE-tmptrfhe
paper: LIT-037
title: 'Cuffaro & Hartmann, The Open Systems View'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (full text of arXiv:2112.11095v2 (stamped 2 Jun 2023; the
    PDF is dated 2023-06-05), 60 pp. I read §1–6 (pp. 1–46), the
    acknowledgements (p. 47), the reference list (pp. 48–60) and all 88
    footnotes. I extracted the text with PyMuPDF into raw4/2112.11095.txt;
    pdftotext is not on this host. Figure 1 (p. 21) is an interpretation
    genealogy reproduced from Janas, Cuffaro & Janssen 2022, and only its
    caption came through. I did not compare this version with the Philosophy
    of Physics version (DOI 10.31389/pop.90) or with the OUP chapter.
    Nothing was skipped.). Upgraded from `Skimmed` to `Read`: the claims
    table, assumptions and results are new, and the skim is corrected where
    the full text disagreed.
date: '2026-09-25'
summary: >-
  The paper argues philosophically, not formally, that the quantum theory
  of open systems "GT" is more fundamental than standard closed-system
  quantum theory "ST". GT treats states as density operators that evolve,
  in general, non-unitarily, and it admits not-completely-positive maps.
  The ontic and epistemic cases each win only on a second, interpretation-
  or practice-laden criterion: OntFund-2 and EpFund-2. On the first,
  formal criteria (OntFund-1, EpFund-1) the two frameworks tie, and the
  authors say so because Stinespring dilation and dropping the Lindblad
  terms translate in both directions (§4.1, §4.2.1). Explanatory
  fundamentality is granted only deflationarily (ExFund-1), and the
  authors recommend dropping the notion (§4.2.2). The step from there to
  "the open systems view is fundamental tout court" (§4.3) rests on the
  special sciences and on "there are no other options".
---

# NOTE-077: Cuffaro & Hartmann, The Open Systems View

## Contribution

The paper names and separates two "views" in the sense of §2: (i) methodological presuppositions for characterising a domain's objects, (ii) motivated by a metaphysical position about those objects. The closed systems view says open systems are modelled by coupling them to a further system so that the whole is isolated. The open systems view writes the environment's influence into the system's own dynamical law. The paper instantiates the two views as two quantum frameworks: ST, with state vectors, Hamiltonians and unitary evolution, and GT, with density operators under general linear maps (Sudarshan–Mathews–Rau 1961; Jordan–Sudarshan 1961). It argues that GT is more fundamental. It also offers explications of relative fundamentality *between frameworks* (as opposed to between models inside one theory): OntFund-O/1/2, EpFund-1/2 with EpistemicOrder, and ExFund-1/2/3. The new material is the conceptual apparatus and the argument. There are no new physical results.

## Key insight

A framework's formalism can be motivated by one metaphysics while its objects, on any interpretation that takes it as complete, represent something else. Here ST is built on the closed systems view, yet on orthodox readings a state vector encodes an open system's possible manifestations in interaction with some further system. On Everettian readings, reduced density operators are as real as the universal state (§3). Once formal intertranslatability (Stinespring one way, dropping Lindblad terms the other) is granted to settle nothing, the fundamentality question is decided by what the objects actually represent (OntFund-2). By the practice of assignment, density operators always come first: a pure state is an idealisation of ρ = (1−ε)|ψ⟩⟨ψ| + εσ, Eq. 4.2, and a global state is only reachable through subsystems (EpFund-2).

## Assumptions

- **Scope of "candidate fundamental" ST.** Only interpretations that take ST to be complete count: Everettian and orthodox, the latter covering neo-Bohrian, neo-Copenhagen, QBist, pragmatist and relational readings. Hidden-variable and dynamical-collapse views are treated as different frameworks or theories and are set aside (fn 41, p. 32). The ontic verdict holds only relative to this partition, which "there are no other options" (p. 26) asserts rather than argues.
- **Physical closure is rare.** The premise that the cosmos is the only genuinely closed system rests on unshieldable gravity (the Borel/Zeh Sirius example, fn 2), distance-independent entanglement and vacuum fluctuations (§1). It is asserted with citations, not derived.
- **The overlap restriction.** The ontic argument (up to OntFund-2) and EpFund-1 are run only on "dynamical descriptions that can be made sense of in both frameworks" (pp. 29, 35). The greater expressiveness of GT (non-CP maps) is not used as a premise because doing so would be circular.
- **Complete positivity is not mandatory in GT.** Following Shaji & Sudarshan 2005, the witness argument for CP binds only if S is entangled with the witness W_n. A not-CP map evolves every state in its compatibility domain validly (Jordan–Shaji–Sudarshan 2004). A non-CP map arises as a contraction only from an indefinite-metric, pseudo-unitary S+E, which is "unphysical" (fn 36, p. 16).
- **Lindblad derivation conditions (§2.2.1).** These are: a Markov/semigroup property Λ_{t+s} = Λ_t Λ_s (Eq. 2.13), complete positivity, and continuity in t, for a separable Hilbert space and a bounded generator. The paper credits the general form to Lindblad 1976, and to GKS 1976 for the finite-dimensional case. It notes that the result fails for unbounded generators (fn 30).
- **Epistemic order.** EpFund-2 assumes that frameworks share at least one object, here the density operator (p. 38). It also assumes that "perfect global measurements are not actually possible" (citing Vaidman 2003, p. 37).
- **Global argument.** The claim that the open view already prevails in the special sciences (biology, much of economics, psychology; fn 4–5) is taken as given and motivates the whole argument (p. 38, §4.3).

## Key results

- **The ST open-systems recipe (§2.1.2).** Take a two-level atom with H = H_S + H_E + H_SE, under the Born approximation (weak coupling, initially uncorrelated) and the Markov approximation, and trace out E. This gives ρ̇ = −i[H_S, ρ] + A([σ₋ρ, σ₊] + [σ₋, ρσ₊]) (Eq. 2.10). In general ρ̇ = (L_u + L_{n−u})ρ with L_{n−u}ρ = ½ Σ_i ([L_iρ, L_i†] + [L_i, ρL_i†]) (Eqs. 2.11–2.12). Trace, and hence probability, is conserved because the right-hand side is a sum of commutators (proof, fn 23).
- **OntFund-1 is a stalemate (p. 29).** ST dynamics re-describe losslessly in GT via ρ = |ψ⟩⟨ψ|, and GT's CP dynamics derive from ST via Stinespring. "neither dependence nor determination can help."
- **The ontic verdict via OntFund-2 (pp. 30–33).** Orthodox readings are already committed to open systems as "the stuff of the world" (p. 24), and GT "strips away the 'ultimate observer'" (p. 30). For Everettians, a non-unitarily evolving universal density operator is consistent with Everett (Wallace 2012 §10.5; Carroll 2022). Only GT permits it fundamentally. A decoherent mixture p|ψ₁⟩⟨ψ₁| + (1−p)|ψ₂⟩⟨ψ₂| (Eq. 4.1) gives strictly, not just FAPP, independent worlds.
- **The empirical success of ST supports GT equally (p. 34).** ST's successes are all on subsystems, whose effective dynamics are non-unitary. The authors credit the argument to Myrvold (fn 76).
- **EpFund-1 is a tie and EpFund-2 favours GT (pp. 35–38).** Under GNS reduction with non-redundancy and immanence, each framework justifies the other. Under EpistemicOrder, the density operator precedes the state vector in both routes to assigning a state vector: an idealised preparation (Eq. 4.2) and an S+E dilation.
- **Explanatory fundamentality (pp. 39–41).** ExFund-1 is deflationary. ExFund-2 is rejected as formal. ExFund-3 is refuted by the GR/Newton reductio. So "explanatory goodness does not entail explanatory fundamentality, at least not in science." GT is explanatorily more fundamental only under ExFund-1.
- **Wider claims (§5).** The arrow-of-time and information-loss puzzles become conceptually unproblematic under GT, because non-unitary evolution is allowed (§5.1). A "view", unlike van Fraassen's "stance", can be rationally argued for (§5.2). For the cosmos, the open/closed distinction breaks down (§5.3).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Lindblad-form dynamics conserve probability without an underlying unitary dynamics | strong | proof, fn 23 (trace of commutators) |
| C2 | Under OntFund-1 and EpFund-1, ST and GT tie, because each translates into the other on their common domain | moderate | informal argument, pp. 29, 35–36, via Stinespring and dropping the L_i terms |
| C3 | The witness argument for complete positivity binds only if S is entangled with the witness; otherwise not-CP maps evolve compatible states validly | moderate | cited results (Shaji & Sudarshan 2005; Jordan, Shaji & Sudarshan 2004); not re-proved |
| C4 | On orthodox and on Everettian interpretations, ST's subject matter includes open systems (exclusively for orthodox readings) | moderate | informal interpretive argument, §3 |
| C5 | GT is ontologically more fundamental than ST (OntFund-2) | weak | informal argument conditional on C4 and on only Everettian and orthodox readings counting as "candidate fundamental" |
| C6 | GT is epistemically more fundamental (EpFund-2): density operators precede state vectors in epistemic order | moderate | informal argument from preparation imperfection (Eq. 4.2) and inaccessibility of global measurements |
| C7 | Explanatory goodness is not a reliable guide to explanatory fundamentality | weak | a single reductio (Newton vs GR, p. 40) |
| C8 | GT is explanatorily more fundamental than ST | weak | holds only under the deflationary ExFund-1, which the authors themselves suggest discarding |
| C9 | The open systems view is fundamental "tout court", across science | weak | assertion: special-sciences premise plus "no other options" (§4.3, §6); the abstract states it more strongly than §4 shows |
| C10 | Under GT, the information-loss and arrow-of-time problems lose their basic conceptual difficulty | weak | assertion; details explicitly left to others (§5.1, fn 86) |
| C11 | For the cosmos, the ontological open/closed distinction breaks down in GT | weak | informal argument, §5.3 |

## Method

This is conceptual analysis. The authors distinguish model, theory, framework and view (§2), and they explicate relative fundamentality between frameworks in three families: ontic (Object, OntFund-O, OntFund-1, OntFund-2), epistemic (EpFund-1 with Generalized Nagel–Schaffner reduction plus non-redundancy and immanence; EpistemicOrder and EpFund-2, after Carnap's *Aufbau*) and explanatory (ExFund-1/2/3). Each explication is tested on the ST/GT case. When one yields a tie it is diagnosed as "too abstract", and a representation- or practice-sensitive successor replaces it.

## Concepts

- **View**: a pair of (i) methodological presuppositions for characterising a domain's objects and (ii) a motivating metaphysical position about those objects (§2, §5.2). Unlike a van Fraassen stance, a view can be argued for rationally.
- **Closed systems view**: isolated systems are a priori the subject matter. An open S is modelled by coupling it to E so that S+E is isolated.
- **Open systems view**: systems are a priori in general open. The environment's influence is represented in S's own dynamical equations. The view does not deny that closed systems exist, only that one must exist (p. 18).
- **ST**: standard quantum theory, with normalised state vectors, Hermitian Hamiltonians and unitary evolution. Open-system dynamics come from partial traces of S+E.
- **GT**: the general quantum theory of open systems. States are density operators evolving under general linear maps, in general non-unitary, with CP not required (§2.2.2).
- **Object (capital O)**: whatever represents (little-o, pre-theoretic) objects in every model of every theory of a framework, e.g. "the state vector" and "the density operator" in general (p. 28).
- **OntFund-2**: F_F is ontologically more fundamental than F_P iff the way F_P's objects actually represent their targets matches F_F's motivating metaphysics rather than F_P's own (p. 33).
- **Epistemic order / EpFund-2**: C1 precedes C2 iff every instance of C2 is constructed from an instance of C1 in empirical investigation, never the reverse. F_F is epistemically more fundamental iff at least one of its objects always precedes a corresponding object of F_P, and none follows (pp. 36, 38).
- **Compatibility domain**: the set of states of S on which a not-CP map yields valid states of S+W_n (fn 34).
- **Big and small measurement problems**: the terms follow Pitowsky, Bub and Janas–Cuffaro–Janssen. The big problem is why one definite outcome occurs. The small problem is that there is no global prior distribution over all observables; Everettians know it as the preferred-basis problem (§3).

## Connections

§3 places the ontological-models framework (Harrigan & Spekkens 2010) and PBR, [LIT-062](../literature.d/LIT-062.md), inside a wider map of interpretations. It follows Ben-Menahem 2017 in holding that orthodox interpretations are neither ψ-ontic nor ψ-epistemic. On that view they fall outside PBR's scope, so "the ontological models framework turns out to be of rather limited use" (p. 20). This makes the same terminological point as [LIT-090](../literature.d/LIT-090.md) from a different side: [LIT-090](../literature.d/LIT-090.md) argues that Harrigan–Spekkens "ψ-epistemic" is narrower than "epistemic", and Cuffaro & Hartmann say orthodox "epistemic" readings are "a very different sense of that word" (p. 22). The paper names Spekkens' 2007 toy theory as a modern successor to Einstein's ψ-epistemic view (p. 20). That programme is read closely in [LIT-007](../literature.d/LIT-007.md), [LIT-019](../literature.d/LIT-019.md), [LIT-054](../literature.d/LIT-054.md) and [LIT-003](../literature.d/LIT-003.md). The paper engages none of their results; it treats the whole class as hidden-variable programmes that are "not really relevant" to the ST/GT comparison (p. 32).

The complete-positivity discussion cites Schmid, Reid & Spekkens 2019 (fn 31). That paper gives a causal-model analysis of initial system–environment correlations and is not filed here. The purification remark (p. 25) and fn 61 invoke D'Ariano–Chiribella–Perinotti's purification principle as distinguishing quantum from other theories in the GPT sense; [LIT-073](../literature.d/LIT-073.md) gives that framework. The §6 item on ontic structural realism (Ladyman & Ross 2007) connects directly to [LIT-045](../literature.d/LIT-045.md), the SEP entry whose §4 surveys OSR. Ladyman is also in the authors' research group (acknowledgements), and fn 69 aligns the Object/object distinction with Ladyman & Ross's formal/material modes. The §6 causality item (interventionism assumes the closed view) is a pointer only, with no argument. Whether it bears on the record's causal-modelling papers is unverified.

## Bearing on the record

Nothing here is an instruction for ML practice. The one ML-adjacent item is fn 5's passing citation of "the construal of agents as open systems in artificial intelligence" (Russell & Norvig; Briegel), and §6.6 on agency. It is a pointer only, with no argument. Within this record, the paper supplies the vocabulary of "view vs framework vs theory vs model" and a worked case that intertranslatable frameworks can differ in fundamentality only through interpretation. That case is worth citing in any THEORY document about theoretical equivalence. No record document is known to cite it for more than it says. [LIT-045](../literature.d/LIT-045.md)'s OSR discussion should note that the paper's §6.4 challenge (on the open view the extrinsic/intrinsic distinction breaks down) is a conjecture: the authors "speculate" that OSR is consistent with the open view.

## Limitations

- The fundamentality verdicts are only as strong as the interpretive partition in §3. A reader who counts Bohmian or collapse theories as candidate-fundamental ST, or who reads orthodox state vectors differently, loses the OntFund-2 argument. The paper does not defend excluding them beyond classifying them as separate theories or frameworks.
- The Everettian step shows only that non-unitary universal dynamics are *consistent* with Everett. The authors concede that nothing makes that description "any more likely to be true" (p. 32). So the ontic verdict for Everettians amounts to "GT allows a live option ST forbids". This is close to the expressiveness argument the authors earlier called circular.
- EpFund-2 relies on imperfect preparation. That is an epistemic fact about us, and it grounds an ordering over frameworks. The authors disclaim foundationalism (p. 38), but they do not show why epistemic order should confer fundamentality at all.
- Explanatory fundamentality is effectively abandoned (p. 41), so the abstract's "three alternative notions" reduce to two with independent content.
- There are no formal results. The physical exposition is standard and cited: Lindblad, GKS, Stinespring, Jordan–Shaji–Sudarshan.
- There is a slip on p. 39: "one also has to conclude that ST is explanatorily more fundamental than ST" (GT is meant). It is harmless, but it sits at the crux of the ExFund-1 discussion.

## Open questions

The paper lists seven (§6): (1) laws of nature, with GT reformulations of QFT, perhaps from Schwinger–Keldysh; (2) theoretical equivalence between theories inside ST vs GT; (3) levels of description (List 2019); (4) whether OSR needs the extrinsic/intrinsic distinction that the open view dissolves; (5) interventionist causality at cosmic scale once the universe can be open; (6) agency and free will (Briegel & Müller 2015) in GT; (7) persistence of objects construed as open systems. Beyond these, what would settle the ontic claim is a physical case that forces a not-CP or non-Markovian fundamental dynamics. The authors concede that "no phenomena are known that would absolutely force us to consider one of these dynamical possibilities" (fn 83).

## Corrections to the seeded skim

- The dossier asks whether Stinespring dilation "undercuts" the ontic argument. The paper concedes the point itself. OntFund-1, its first explication, gives a stalemate precisely because "Stinespring's theorem … shows us how to derive the non-unitary evolution of a given density operator, ρS, from the fundamental unitary evolution of a state vector |Ψ⟩S+E" (p. 29). The authors add that "neither dependence nor determination can help". The ontic verdict comes only from OntFund-2 (p. 33). That criterion asks whether a framework's objects actually represent their targets in the way its motivating metaphysics says. It is settled by the §3 reading of orthodox and Everettian interpretations, not by expressiveness. The expressiveness argument (not-completely-positive maps) is set aside as circular (pp. 29, 33, 35).
- The dossier says the open view "wins on each" of the three senses. It does not win on explanatory fundamentality in any independent sense. ExFund-2 is dismissed, and ExFund-3 on its face favours ST, since ST's explanations are "simpler, more tractable, and easier to understand", p. 40. The authors reject ExFund-3 by a reductio (Newtonian mechanics vs GR on Halley's comet). They then adopt the deflationary ExFund-1, under which explanatory fundamentality is inherited from the ontic and epistemic verdicts. Finally they suggest the notion "is probably best discarded altogether" (p. 41). On epistemic fundamentality, EpFund-1 (justification, with GNS reduction) is a tie (p. 36). Only EpFund-2 (epistemic order) favours GT.
- On non-Markovian dynamics, the dossier says the Lindblad derivation "sets aside" the question. The paper addresses it. Fn 25 says the Lindblad form is not the most general GT dynamics ("Most completely positive trace-preserving maps … will, in fact, not be of this form", citing Wolf & Cirac 2008). Fn 38 says fundamental non-Markovian dynamics are "not conceptually problematic on the open systems view". It also notes Bassi–Dürr–Hinrichs 2013: complete positivity need not be separately assumed if the dynamics are Markovian.
- §6 lists seven open questions, not six. The dossier omits "Persistence" (item 7, p. 47).
- On §5.3, the dossier says the paper "raises the question" of whether the universe is open or closed. It goes further: it concludes that "the ontological distinction between open and closed systems (at least when it pertains to the cosmos) breaks down in GT" (p. 45). It proposes treating the form of cosmic dynamics as a brute fact, like the principle of inertia, and it rejects a Newtonian external intervener.
- The skim describes GT as the framework in which the environment "enters through their own (generally non-unitary, Lindblad-type) dynamics". Lindblad-type is one important special case (quantum dynamical semigroups), not GT's defining form. GT is characterised by density operators under linear maps, in general non-unitary and not necessarily completely positive (§2.2.2).
