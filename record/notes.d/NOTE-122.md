---
number: 122
status: Read
formerly:
- NOTE-tmpeucsy
paper: LIT-185
title: 'Barrett et al. — IIT: good, bad and misunderstood'
version: 2
history:
- version: 2
  date: '2026-09-26'
  note: >-
    Read in full (full text of arXiv:2604.11482v1 [q-bio.NC], 13 Apr 2026,
    19 pp., fetched 2026-09-26 from arxiv.org/pdf/2604.11482. Read every page:
    abstract, §1 Introduction, §2 with Box 1 (the six axioms with
    clarifications), §3.1–3.2, §4.1–4.2, §5.1.1–5.1.2, §5.2, §5.3, §6
    Discussion with Box 2 (recommendations), acknowledgements, data
    statement and the full reference list. The captions of Figs 1–3 were
    read; the figures themselves are schematics with no data.). Upgraded
    from `Skimmed` to `Read`: the claims table, assumptions and results are
    new, and the skim is corrected where the full text disagreed.
date: '2026-09-26'
summary: >-
  A position paper with no new formal result. It argues four things. IIT's
  algorithm is undefined whenever any spatial, temporal or state graining
  of a system is non-Markovian (Barrett & Mediano 2019), and so gives no
  output for brains; it cannot handle unbounded continuous state
  variables; and it has never been computed on any real system. PCI and
  other "approximations" of Φ are proxies, capturing at most two of the
  six axioms. The theory would need recasting in continuous fields (the EM
  field) to fit the standard model. Against critics, the authors hold that
  IIT can be read with a multi-dimensional measure of global state (mean
  Φ, variance of cause-effect-structure quantities, structural
  complexity), on which Aaronson's inactive expander grid is only
  minimally conscious, and that IIT's implied "tiling" panpsychism is no
  worse than any rival metaphysics.
---
<!-- inactive-ok-file: LIT-191 — Deferred: a related work named by a 2026-09-26 close reading on the metaphysics tag; lapses when the cited work is read -->
<!-- inactive-ok-file: LIT-143 — Deferred: a related work named by a 2026-09-26 close reading on the metaphysics tag; lapses when the cited work is read -->
<!-- inactive-ok-file: LIT-135 — Deferred: a related work named by a 2026-09-26 close reading on the metaphysics tag; lapses when the cited work is read -->

# NOTE-122: Barrett et al. — IIT: good, bad and misunderstood

## Contribution

The paper consolidates, for a general audience, the known formal problems of IIT 4.0 (non-Markovian grainings, continuous states, the unexplored maximisation over grainings, discrete units vs continuous fields). It adds a crisp proxy/approximation distinction that reclassifies all empirical "Φ" work, PCI included, as proxy work. It proposes revisions: a multi-dimensional global-state suite, an algorithm defined on the current state only, and a field formulation. Its new conceptual item is an explicit description of IIT's panpsychism as a time-varying, gapless tiling of space by non-overlapping substrates, derived from the exclusion axiom.

## Key insight

Strong IIT's Φ is not a quantity anyone has measured, approximated or can even define for a brain. Its formula needs the next-state distribution given the present state alone, under every candidate graining, and brains are non-Markovian under the grainings anyone uses. So everything empirical that has been said "for IIT" is evidence for weak IIT's intuitions (integration and differentiation), equally compatible with rival theories. The theory's real current achievements are qualitative structure-to-phenomenology links (grid → spatial extension, directed chain → temporal flow) on toy systems, where Φ need not be computed at all.

## Assumptions

- **IIT 4.0 as specified by Albantakis et al. 2023**: six axioms (Box 1: existence, intrinsicality, information, integration, exclusion, composition). They are "not contested" here (§6). The authors add clarifications from the IIT wiki and note that exclusion alone "is not obvious from introspection" but is "a reasonable assumption".
- **The algorithm's outputs**: system integrated information φs (where consciousness is: a patch is a substrate iff φs(P) exceeds that of every overlapping patch), cause-effect structure C (contents), and structure integrated information Φ (quantity). All derive from past and future state probabilities given current states of parts, under a uniform ("maximum entropy") prior, with grainings chosen to maximise φs and Φ (§2). C is "distinct from physical causal structure".
- **IIT is "canonically non-computational"**: the algorithm is a researcher's tool, and consciousness is not claimed to be algorithmic (§2).
- **Brain dynamics are non-Markovian under typical grainings** (§5.1.1). The only citation is Fuliński et al. 1998, on ionic current fluctuations in membrane channels.
- **Approximation** is defined as: A approximates B only if both are well defined and a bound on |A − B| can be determined (§5.2).
- **Fundamental physics is field-theoretic at all observable scales** (§5.3), with possible Planck-scale discreteness set aside.
- **Weak vs strong IIT** (Mediano et al. 2022): strong IIT identifies experience with IIT's quantities universally; weak IIT seeks explanatory correlates in specific settings.

## Key results

There are no theorems. The arguments, by section:

- **§3.1 Empirical evidence.** TMS-EEG studies (Massimini et al.; Casali et al. 2013) show local, stereotyped responses under anaesthesia, sleep and disorders of consciousness, and diverse, spreading responses in conscious states. PCI is clinically useful. These results "give validation to the information and integration axioms" but are "equally compatible with alternative weaker versions of IIT, as well as, arguably, with other theories" such as global neuronal workspace (Farisco & Changeux 2023).
- **§3.2 Structure to qualia.** A non-directed 2-D grid entails an experience of space (Haun & Tononi 2019); a directed chain entails temporal flow (Comolatti et al. 2024). For these synchronous, discrete toy systems, C is fixed by which component sets cannot be bipartitioned without cutting connections: contiguous sets contribute, non-contiguous sets do not (Fig. 2). This "does not require the ability to measure Φ". "None of the other major theories" have comparable accounts.
- **§4.1 Φ and quantity.** They propose a multi-dimensional global-state characterisation: (i) mean Φ over time as "intensity"; (ii) variances over time of C quantities (how much contents change); (iii) mean geometric and topological complexity of C. On this, the inactive expander grid (Aaronson 2014) has large mean Φ, zero variance and minimal complexity, so "minimal consciousness". Complex phenomenology requires many components to be *dynamically* active; one static high-Φ state is not enough, a point "not much discussed in the IIT literature". But IIT is unlikely to capture metacognition, sense of self or capacity for suffering, which "challenges the notion of IIT being a fully comprehensive theory".
- **§4.2 Panpsychism.** IIT "does not assume panpsychism" but implies it. By exclusion, substrates of distinct experiences never overlap, so space and time are tiled "with no gaps". All matter is conscious "in the sense that it contributes to precisely one substrate" at a time. Boundaries shift as matter moves. Most substrates are "ontological dust" (Tononi et al. 2022) (Fig. 3).
- **§5.1.1 Ill-definedness.** The formulae need P(future | present) for each graining, which is not uniquely specified when a graining is non-Markovian. So "the IIT algorithm is therefore not well-defined whenever there is at least one non-Markovian graining", and "does not produce an output for brains". Fixes fail. A uniform prior over the whole past does not converge for non-ergodic dynamics such as a random walk (Barrett & Mediano 2019). Kleiner & Tull's (2021) future trajectories still leave unspecified the evolution of one part given no knowledge of another part's present state. The possible cure is to reformulate on the instantaneous state's geometry and topology alone, which would de-emphasise causal mechanisms.
- **§5.1.2 Never computed on a real system.** Applications are all to finite binary Markovian units assumed indivisible. The maximisation over all grainings has never been studied. The maximum-entropy prior is undefined for continuous variables without hard bounds.
- **§5.2 Proxies are not approximations.** Examples: GDP is a proxy for living standard; Newton approximates GR with a bound on deviation; Granger causality approximates transfer entropy, which itself is only a proxy for inter-regional information transfer from EEG. Since Φ is undefined for a brain, it cannot be approximated. Existing measures are "operational proxies for at most two of the total set of six" axioms. PCI links to an earlier Φ only in logic-gate proof-of-principle work (Sevenius Nilsen et al. 2019). Candidate empirical Φ measures disagree, "often moving in different directions under the same change of parameters" (Mediano et al. 2019).
- **§5.3 Fields.** IIT's discrete units in discrete time conflict with continuous field theories (GR, Maxwell, the standard model). They propose recasting IIT on field configurations, especially the electromagnetic field (Barrett 2014), with neurons as "scaffolding" for a complex EM field.
- **§6 and Box 2.** Recommendations: a multi-dimensional measure suite; clear communication of the panpsychism; reformulation on the current state only; the word "proxy" for empirical measures; a field reformulation. Even a well-defined revision would face the challenge of proving it "the only such algorithm consistent with its axioms". The authors are "agnostic" on whether this is possible. They propose weak IIT as a route to testing IIT's intuitions without strong IIT's identity claim.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | IIT 4.0's algorithm is undefined whenever any graining of a system is non-Markovian | informal argument (mathematical, not a new proof) | §5.1.1; the formal case is Barrett & Mediano 2019 |
| C2 | Brain dynamics are non-Markovian under typical grainings, so IIT gives no output for brains | assertion with one citation | §5.1.1: Fuliński et al. 1998 (ion-channel currents) |
| C3 | Proposed fixes (a uniform prior over the past; future trajectories) do not resolve C1 | informal argument | §5.1.1: non-convergence under non-ergodic dynamics; Kleiner & Tull 2021 |
| C4 | IIT cannot handle unbounded continuous state variables, and boundedness under refined graining is unknown | informal argument | §5.1.2 |
| C5 | Φ has never been computed on a realistic model of any real physical system | assertion (survey-level) | §5.1.2 |
| C6 | Empirical IIT measures, PCI included, are proxies, not approximations, capturing at most two of six axioms | argument from definition | §5.2, with the definition of approximation |
| C7 | Evidence from PCI supports weak and strong IIT equally and possibly rival theories | informal argument, cited | §3.1, §6 |
| C8 | IIT gives principled structure-to-phenomenology accounts of spatial and temporal experience that no rival theory offers | informal argument, cited | §3.2: Haun & Tononi 2019; Comolatti et al. 2024 (toy systems) |
| C9 | On a multi-dimensional global-state characterisation, an inactive expander grid has only minimal consciousness | informal argument, conditional on the authors' proposal | §4.1. High Φ at assembly is conceded |
| C10 | IIT implies a gapless, shifting tiling of space-time by non-overlapping substrates of (proto-)consciousness | informal derivation from the exclusion axiom | §4.2, Fig. 3 |
| C11 | This panpsychism is "not a problematic metaphysical position" and is "perfectly compatible with empirical science" | assertion, supported by tu quoque | §4.2 (all metaphysics of consciousness look implausible; materialism's explanatory gap), §6 |
| C12 | IIT must be reformulated in continuous fields to fit fundamental physics | informal argument | §5.3; Barrett 2014 |
| C13 | Exclusion and intrinsicality are consistent if intrinsicality means observer-independence | assertion, parenthetical | §6, against Mørch 2019 |
| C14 | IIT is unlikely to capture metacognition, sense of self or capacity for suffering | assertion | §4.1, §6 |

## Concepts

- **patch**: an arbitrary region of physical matter to which the IIT algorithm is applied; a **system** when it is a specific object of study (§2).
- **graining**: one of three discretisation choices, spatial components, time step, and state definition, all chosen to maximise φs and Φ (§2, citing Marshall et al. 2024).
- **φs (system integrated information)**: information the whole patch's current state holds about its past and future states that cannot be attributed to parts under any partition. It determines *where* consciousness is.
- **cause-effect structure C**: informational relations between past, present and future states of all pairs of parts. It determines contents and is distinct from physical causal structure.
- **Φ (structure integrated information)**: the sum of integrated information over sets of parts in C; the quantity of consciousness in IIT 4.0.
- **global state of consciousness**: the overall (un)conscious condition of a system, e.g. NREM sleep or anaesthesia (Bayne et al. 2016).
- **ontological dust**: micro-substrates with minimal phenomenal content (Tononi et al. 2022).
- **proto-consciousness**: the proposed relabelling of ontological dust (§4.2).
- **proxy vs approximation**: an approximation has a well-defined target and a determinable error bound; a proxy is a practically informative stand-in with no precise link (§5.2).
- **weak vs strong IIT**: explanatory correlates in specific settings vs a universal identity of experience with IIT's quantities (§3.1, §6).

## Connections

**Metaphysical thesis defended or presupposed.** The paper defends one metaphysical thesis and presupposes another. It defends the claim that IIT's implied ontology, a gapless tiling of space-time by non-overlapping substrates of (proto-)consciousness with shifting boundaries, is a coherent and non-problematic panpsychism, no worse off than materialism given the explanatory gap. It presupposes that the correct physical ontology is field-theoretic, which is its reason to rebuild IIT on the EM field. It keeps strong IIT's identity thesis (experience *is* a cause-effect structure) at arm's length and recommends weak IIT for empirical work. So the `metaphysics` tag is justified; `consciousness` is the right primary topic, and `information-theory` fits the technical core (§§5.1–5.2).

**Links in this record.**
- [LIT-159](../literature.d/LIT-159.md) (Schwitzgebel, the US is probably conscious): its §2 argues that IIT's exclusion postulate is unmotivated and yields absurdities (voters losing consciousness at a one-ballot threshold). Barrett et al. do not engage it. Their tiling picture, in which each piece of matter belongs to exactly one maximal-φs substrate, makes the reductio sharper, and their one exclusion argument addresses only Mørch's intrinsicality objection.
- [LIT-135](../literature.d/LIT-135.md) (Seth, biological naturalism): Seth is a co-author. The dossier asked whether the paper's charity toward IIT's panpsychism is consistent with Seth's biological naturalism. The text gives no direct answer: it never discusses AI, life or biological naturalism. Two points reduce the apparent tension. The paper defends the panpsychism only as "not problematic" relative to rival metaphysics, not as true. And it recommends *weak* IIT for empirical work, which carries no universal identity claim and so no commitment about non-living substrates. Both IIT (§2, "non-computational") and Seth reject computational functionalism, so they agree on that much.
- [LIT-056](../literature.d/LIT-056.md) (Butlin et al.): sets IIT aside because IIT denies computational functionalism. This paper's statement that IIT is "canonically non-computational" (§2) is the reason, and its §5 explains why IIT could not have been used as an indicator source anyway: Φ is not computable for real systems.
- [LIT-143](../literature.d/LIT-143.md) (Kleiner et al., mathematical structure of experience): relevant to C8. Whether the grid-to-space and chain-to-time mappings are structures *of* experience, rather than descriptions, is exactly the test that paper proposes.
- [LIT-025](../literature.d/LIT-025.md) (Mediano et al., causal emergence review) and [LIT-027](../literature.d/LIT-027.md) (Varley et al.): the same group's information-decomposition programme, from which the weak-IIT and ΦID measures come.
- [LIT-096](../literature.d/LIT-096.md) (Nagel): the "something it is like" notion behind the existence and intrinsicality axioms, though Nagel is not cited.
- [LIT-191](../literature.d/LIT-191.md) (Schwitzgebel, AI and Consciousness): mainstream theories disagreeing about AI systems. This paper's §5 implies IIT cannot presently return a verdict on any real system, silicon included.

## Bearing on the record

It carries nothing for ML practice as an instruction, and nothing belongs in the Anthology. Its §5.2 proxy-versus-approximation distinction (a quantity approximates another only with a well-defined target and an error bound) is a general methodological point that would transfer to evaluation practice, but the paper does not make that transfer and it is not an ML claim. For nucleation it is the reference for "Φ is undefined for brains and has never been computed on a real system". Any note that cites IIT on AI consciousness should cite this paper for the fact that IIT currently delivers no verdict on real hardware, only verdicts on toy systems. The record should *not* cite it for "IIT does not say high Φ means more consciousness"; the paper concedes IIT 4.0 says exactly that and proposes changing it.

## Limitations

- It is a position paper with no new formal results. The load-bearing technical claim (C1) is restated from Barrett & Mediano 2019 rather than proved here.
- C2 (brains are non-Markovian under typical grainings) rests on a single 1998 citation about ion-channel current fluctuations. It is plausible, but the grainings at which IIT would be applied are not examined.
- The defences in §4 are revisions, not readings. The multi-dimensional suite (C9) and the proto-consciousness relabelling are proposals, yet the Discussion states their conclusion as a fact about IIT ("IIT does not attribute substantial consciousness to an inactive grid").
- The panpsychism defence (C11) is comparative (tu quoque) and terminological. It shows the view is no worse than materialism on the hard problem, not that the tiling ontology is unproblematic. The combination problem and anti-nesting objections ([LIT-159](../literature.d/LIT-159.md)) are not addressed.
- The field reformulation (§5.3) is a direction, not a construction. It inherits the same uniqueness challenge the authors raise (§6).
- Axioms are explicitly uncontested, so the paper cannot adjudicate whether IIT's starting point is sound (Bayne 2018 is deferred to).
- Several authors are proponents of weak IIT and of rival measures (ΦID, PCI analyses), which is relevant context for the proxy critique; the paper does not flag it as a conflict.

## Open questions

- Can the algorithm be reformulated on the instantaneous state alone (Box 2), and would the result still be IIT? The authors call this "a major change".
- Is there a unique algorithm consistent with the axioms once it is well defined (§6)? A uniqueness proof would settle strong IIT's credentials. The authors are agnostic that one exists.
- Does IIT's exclusion-driven tiling survive Schwitzgebel's anti-nesting reductio ([LIT-159](../literature.d/LIT-159.md))? A formal Φ comparison between a polity-scale system and its members, which neither paper attempts, would bear on it.
- Will INTREPID's inactivated-vs-inactive neuron test (Olcese et al. 2024) confirm the one core IIT claim testable without well-defined Φ?

## Corrections to the seeded skim

- The LIT summary says the authors hold that "'high Φ = more consciousness' is a misreading". The paper concedes the opposite about the theory as stated: "IIT does state that Φ corresponds to the quantity of consciousness (Albantakis et al., 2023)" (§4.1, p. 8). The claimed misunderstanding is narrower: that "subscribing to IIT *necessarily* implies" a one-dimensional level of consciousness. Their multi-dimensional suite is a *proposal* (Box 2, "Φ might be replaced with a suite of quantities"), a revision of IIT, not a clarification of it.
- Likewise, the dossier and the paper's Discussion ("contrary to much commentary, IIT does not attribute substantial consciousness to an inactive grid", p. 14) overstate what §4.1 shows. §4.1 says "IIT would posit that the grid has a conscious experience with a high Φ when it is first assembled", with a phenomenology of an empty spatial field without even time (citing Haun & Tononi 2019). The grid comes out "minimal" only on the authors' proposed multi-dimensional characterisation; unboundedly high Φ is conceded, and they say the result "may still be considered a problem" of "a lesser order" (p. 9).
- The dossier's §4.2 bullet attributes "perfectly compatible with empirical science" to §4.2. That phrase is in §6 (p. 14). §4.2 argues only that panpsychism is "not a problematic metaphysical position", and its support is comparative: materialism also has an explanatory gap (Levine 1983; Chalmers 1995), and "most, if not all" metaphysical positions look implausible (Kuhn 2024). It adds a terminological workaround: call the micro-level "proto-consciousness" and reserve "consciousness" for complex cause-effect structures, which "could have ethical implications" by allaying over-attribution of moral patienthood (p. 11).
- The dossier omits two §5.1.2 problems that are independent of non-Markovianity. (1) The maximum-entropy prior over states is undefined for continuous state variables (membrane potential, LFP) without hard bounds, and it is "uncertain" whether quantities stay bounded as state graining is refined. (2) Maximising φs and Φ over all grainings of space, time and state, down to particles, "has never been" investigated.
- The dossier says §6 offers "a reconciliation of exclusion with intrinsicality … against Mørch". That is a parenthetical remark (pp. 14–15): intrinsicality means independence from any external observer's frame of reference, not immunity to external matter. The paper does not engage Schwitzgebel's anti-nesting critique of exclusion ([LIT-159](../literature.d/LIT-159.md)), which its tiling picture (every piece of matter belongs to exactly one substrate) if anything sharpens.
- Minor: the dossier omits the Discussion's remarks on the COGITATE adversarial test (it tested IIT's intuitions about location and connectivity, not integrated-information measures) and on INTREPID (inactivated vs merely inactive neurons would test a core IIT claim without strong IIT's measures being well defined). Affiliations: five authors are at Sussex, Mediano at Imperial and Bor at Queen Mary, so "Sussex-centred" is right.
- metaphysics tag: justified — §4.2 states and defends an ontology (a gapless, shifting tiling of space-time by non-overlapping substrates of (proto-)consciousness, with "ontological dust"), and §5.3 is about which physical entities are fundamental (fields vs units). The strong-IIT identity claim is a metaphysical thesis the paper keeps separate from weak IIT.
