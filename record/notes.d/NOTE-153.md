---
number: 153
status: Read
formerly:
- NOTE-tmpog63l
paper: LIT-150
title: 'Rizi — What is emergence, after all?'
version: 2
history:
- version: 2
  date: '2026-09-26'
  note: >-
    Read in full (full text of arXiv v4 (9 Jan 2026; "compiled on January
    12, 2026"), 10 pp. in PNAS Nexus two-column layout — every section read
    (abstract; introduction; Levels of Description; Many-to-one Maps &
    Coarse-graining; Reductionism & "Theory of Everything"; A New Ontology;
    Effective Theories; Onset of Emergence, Symmetry Breaking & Criticality;
    Renormalization & Universality; Duality & Emergence; Emergence in
    Networks & Social Systems; Emergence of Herd Immunity; Weak vs. Strong
    Emergence; Conclusion and Discussion), captions of Figs. 1–3,
    acknowledgements, and refs. 1–168 checked for every citation used below.
    The published PNAS Nexus version was not compared against v4. Sections
    are unnumbered, so locations are headings and page numbers.). Upgraded
    from `Skimmed` to `Read`: the claims table, assumptions and results are
    new, and the skim is corrected where the full text disagreed.
date: '2026-09-26'
summary: >-
  A perspective, not an argument with results. Rizi proposes that
  emergence is present when a many-to-one coarse-graining F (Eq. 1, N′ <
  N) keeps the macro description predictive after most micro detail is
  discarded. He says the onset of emergence is located by order
  parameters, diverging susceptibility and correlation length, and RG
  fixed points, and that dualities show macro behaviour is not dictated by
  micro "stuff". Herd immunity on networks (percolation, the S–R interface
  density ρ_SR) is offered as a social case. The paper then asserts that
  science needs only weak emergence, and that invoking strong emergence
  "steps outside the scope of scientific method".
---

# NOTE-153: Rizi — What is emergence, after all?

## Contribution

A short perspective (PNAS Nexus) that collects, in one place, the physicist's operational toolkit for talking about emergence without mystique. The toolkit is a many-to-one coarse-graining map with predictive power retained, effective theories as self-contained descriptions at a scale, symmetry breaking and criticality as the testbed for locating onset, RG universality and dualities as grounds for macro autonomy, and weak emergence as the only notion science needs. It adds no new result. Its value is as a curated, heavily cited synthesis (168 references) and as an explicit statement of a position.

## Key insight

Emergence is a relation between descriptions at two scales. It holds when there is a many-to-one map from micro to macro under which the macro description stays predictive. The onset of such a map, in the cleanest cases, is exactly what phase-transition physics already measures: an order parameter turning on, a diverging susceptibility and correlation length, and data collapse. On this view, being surprised by emergence reflects where one stops asking questions, not a gap in physical law.

## Assumptions

- Physicalism: "If a property is observable (measurable), it is physical" (p. 7), and every genuine emergent feature has "an underlying mechanism, not beyond the standard physical interactions" (p. 8).
- Coarse-graining as a map F: (x₁…x_N) ↦ (X₁…X_{N′}) with N′ < N, possibly on a coarser time grid (Eq. 1). F "need not be simple, trivial, local, or unique" (p. 2). No distortion measure or predictive-information measure is fixed.
- Thermodynamic-limit reasoning: macro variables are sharp as N → ∞. For temperature, T = (1/3m)⟨v²⟩(1 ± 1/√N) with k_B = 1 (Eq. 2).
- Weak emergence is defined as explanatory autonomy plus in-principle, practically hard derivability (p. 7, citing Fodor, O'Connor and Bedau).
- For the social example, the contact structure is a static network with pre-outbreak immunisation. Fully mixed threshold π*_R = 1 − 1/R₀. The network case is taken from bond-percolation and message-passing results in the cited literature.

## Key results

There are no theorems or new results. The paper argues or reports the following.

- **Coarse-graining criterion** (p. 2): emergence is present when a many-to-one micro→macro map leaves the macro description predictive. The practical question is whether a finite macro parameter set reaches a given tolerance, and which F* minimises distortion.
- **Temperature as local, direct emergence** (pp. 2–3, citing Carroll & Parola 2024). It is local because it depends only on nearby particles. It is direct because F is a simple analytic function (mean kinetic energy), not "an algorithmically complex lookup". Its domain of applicability is set by the 1/√N fluctuation term (Eq. 2).
- **Onset diagnostics** (pp. 4–5): order parameter, diverging correlation length and relaxation time, finite-size scaling and data collapse, and critical exponents. Information-theoretic proxies are rising mutual information near criticality, transfer entropy and persistent mutual information. Criticality is "neither the only route to emergence nor trivial to establish empirically". "Critical-looking" statistics (power laws, avalanches) are "insufficient on their own".
- **Dualities** (p. 5): exact dictionaries between ontologically different theories (sine-Gordon/Thirring, AdS/CFT, particle–vortex) show that "large-scale behavior is not dictated by microscopic 'stuff'". Which language is useful depends on the question, "rather than on a uniquely privileged ontology".
- **Herd immunity as network emergence** (pp. 5–7). The fully mixed threshold is π*_R = 1 − 1/R₀ (measles R₀ ∼ 15). On real networks the remaining susceptible fraction satisfies π_S ≤ 1 − π_R, and the indirectly protected share is 1 − π_R − π_S. The S–R interface density ρ_SR is a proxy for containment. Targeting hubs raises collective immunity, while spatial structure can leave susceptible pockets.
- **Weak vs strong** (p. 7): science needs only weak emergence. Strong emergence "steps outside the scope of scientific method". Higher-level constraints ("downward or top-down causation") act "without violating the underlying laws".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Emergence can be formalised as a many-to-one coarse-graining that preserves predictive power | weak | definition stated (Eq. 1); no measure of "predictive" or of distortion given |
| C2 | Temperature is a local, direct emergent property, sharp only for large N | moderate | textbook statistical mechanics, Eq. 2; the local/direct classification is from Carroll & Parola |
| C3 | Order parameters, diverging susceptibility/correlation length and data collapse locate the onset of emergence | moderate | standard critical-phenomena results cited (Sethna, Kardar, Goldenfeld); the paper itself cautions this covers only one route to emergence |
| C4 | Dualities show macro behaviour is not fixed by micro ontology and ground autonomy "without extra causes" | weak | examples of dualities cited; the inference from duality to autonomy is asserted |
| C5 | LLMs "acquire new capabilities, such as multi-digit arithmetic or spatial reasoning, only after reaching a sufficient scale", a digital analogue of the thermodynamic limit | assertion | one sentence citing Krakauer, Krakauer & Mitchell 2025; the metric-artefact critique ([ANTH-LIT-471](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-471.md)) is not mentioned; no coarse-grained variable is named |
| C6 | Herd immunity is a paradigmatic, rigorously quantified case of emergence in social networks | moderate | summary of the author's co-authored percolation/message-passing papers (refs. 141, 144); not reproduced here |
| C7 | Invoking strong emergence for consciousness or society steps outside scientific method | assertion | no argument beyond the definition of strong emergence |
| C8 | Emergent phenomena possess causal power; science is compatible with pluralism about higher-level causal powers | assertion | stated (pp. 5, 8) with citations to Simpson & Horsley and Flack; not reconciled with "not a metaphysical extra cause" |

## Concepts

- **Emergence (operational)** — the existence of a many-to-one micro→macro map under which the macro theory remains predictive after most micro detail is discarded (p. 2).
- **Local / direct emergence** — following Carroll & Parola: "local" means the macro variable at a point depends only on nearby micro variables. "Direct" means the map is a simple analytic function rather than an algorithmically complex one.
- **Effective theory** — a "self-contained, predictive, and often universal" description at a scale, "not shortcuts" (p. 3). Mean-field theory is its zeroth order.
- **Weak emergence** — explanatory autonomy with in-principle but practically difficult derivability from the micro description (p. 7).
- **Strong emergence** — layers with their own fundamental rules, "possibly violating physical laws … or breaking causal closure or locality" (p. 7).
- **Explanatory vs ontological reduction** — reduction secures cross-scale consistency, while effective theories deliver explanation and control (p. 1). The distinction is announced in the introduction but developed only in passing.
- **ρ_SR** — density of susceptible–immune links. It is used as a structural measure of the "firefront" of indirect protection (p. 6).

## Connections

The paper sits squarely in the information-theoretic causal-emergence literature the record already holds. It cites Varley & Hoel ([LIT-027](../literature.d/LIT-027.md)) and the Rosas et al. PID framework that Mediano et al. review ([LIT-025](../literature.d/LIT-025.md)). Its duality section relies on De Haro & Butterfield ([LIT-199](../literature.d/LIT-199.md), cited as ref. 121) and on Castellani & De Haro. Its conclusion invokes De Haro 2019 on emergence in physics. For the mesoscale claim it cites McKenzie's survey ([LIT-141](../literature.d/LIT-141.md), read as x31), and the two share a physicist's stance, the Anderson/Laughlin–Pines lineage and the Ising exemplar. They differ in what they take emergence to be. McKenzie takes novelty relative to the parts; Rizi takes predictive coarse-graining. Where McKenzie spends several pages on LLM emergent abilities and reports the Schaeffer critique, Rizi gives one unhedged sentence. The editorial of Artime et al. ([LIT-021](../literature.d/LIT-021.md)) covers similar ground (origin of life to pandemics) and is not cited.

**Metaphysical thesis.** The paper defends non-reductive physicalism. All emergence is weak, meaning in-principle derivable. Yet higher-level patterns are "real" (Dennett's real patterns), and higher levels have causal powers exercised as constraint without extra causes. It presupposes that physical measurability exhausts what is real ("If a property is observable (measurable), it is physical"). These are claims about what exists and about causation across levels, so the `metaphysics` tag is **justified**. The paper does not argue them to a philosopher's standard. It asserts them against strong emergence and treats the causal-power question as settled by "constraint" talk.

## Bearing on the record

- No THEORY or practice follows from this reading. The work is a position statement, not evidence.
- For ML practice, nothing, except as a caution. The paper's only ML content is the unhedged LLM "digital analogue" sentence. It should not be cited in the anthology as support for emergent abilities being real, sharp, or thermodynamic-limit-like. The anthology's own records are Wei et al. ([ANTH-LIT-470](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-470.md)) and the metric critique by Schaeffer et al. ([ANTH-LIT-471](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-471.md)). The arithmetic example Rizi gives is one of the cases [ANTH-LIT-471](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-471.md) reanalyses.
- Useful in the record as the compact counterpart to McKenzie ([LIT-141](../literature.d/LIT-141.md)) and as a pointer into Carroll & Parola 2024 and Krakauer, Krakauer & Mitchell 2025, neither of which is held.

## Limitations

- F is never given a distortion measure or a predictive-information criterion, so "emergence is present when …" is not decidable from the paper's own definition.
- The weak/strong verdict is by stipulation about scientific method, not by argument. Philosophical strong-emergence positions are cited (Chalmers, Kim) but not engaged.
- The claims that higher levels have causal powers and that emergence is not an extra cause sit side by side without the exclusion problem being addressed. Hazelwood's composition-versus-causation point ([LIT-156](../literature.d/LIT-156.md)) is exactly the missing step.
- The LLM claim has no support within the paper and no link to its own diagnostics.
- The social example's rigour is borrowed from cited work.
- Minor technical and citation slips (m ≠ 0 "at" Tc; the Game of Life citation).

## Open questions

- Which distortion or predictive-information measure makes the coarse-graining criterion decidable, and does it agree with Hoel's effective information or Rosas's PID criteria on the paper's own examples?
- Do LLM capability onsets admit an order parameter and finite-size scaling in the paper's sense? That would be an actual test of the "digital analogue", and the metric-choice result ([ANTH-LIT-471](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-471.md)) suggests the answer turns on the observable chosen.
- How is "higher-level causal power" compatible with "no extra cause" under an interventionist account? Woodward's independent-fixability condition, as used by Hazelwood ([LIT-156](../literature.d/LIT-156.md)), would be the test.

## Corrections to the seeded skim

- Dossier and skim (NOTE-153): LLM capability onset is "offered as a digital analogue (Fig. 2)". Fig. 2 has nothing about LLMs. It shows temperature as coarse-graining, majority-vote block spins, liquid–gas/Ising universality, the order–disorder transition and RG flow. The LLM claim is one sentence in the running text of "A New Ontology" (p. 2).
- What the paper claims about LLM "emergent abilities", exactly: "Large language models (LLMs) display a digital analogue of this behavior: they acquire new capabilities, such as multi-digit arithmetic or spatial reasoning, only after reaching a sufficient scale (62)" (p. 2). "This behavior" is temperature and pressure becoming meaningful only in the thermodynamic limit. Ref. 62 is Krakauer, Krakauer & Mitchell 2025, "Large language models and emergence: a complex systems perspective" (arXiv:2506.11135). It is not Wei et al. ([ANTH-LIT-470](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-470.md)), which the paper never cites. Schaeffer et al. ([ANTH-LIT-471](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-471.md)) is not cited or mentioned either. The claim is stated flatly, without hedging, and is never returned to. It is also cited to a paper whose abstract says it "examine[s] claims that Large Language Models exhibit emergent capabilities" and asks whether LLMs have emergent intelligence, so the source is itself a critical treatment. Multi-digit arithmetic is the very case Schaeffer et al. reanalysed (2-shot 2-digit multiplication and 4-digit addition) as an artefact of the metric. The analogy is also a mismatch inside Rizi's own framework. Temperature is emergent because a many-to-one map with 1/√N fluctuations (Eq. 2) becomes sharp as N → ∞. The LLM claim names no coarse-grained variable, no map F and no order parameter, so none of the paper's diagnostics (order parameter, susceptibility, data collapse) is applied to it.
- Dossier: "Check whether 'information relevant for prediction and control' is given a formal measure". It is not. F is defined only as a lossy compression (Eq. 1). The "key practical question" is posed as finding F* that "minimizes the chosen distortion measure" at a "specified tolerance" (p. 2), but no measure is chosen. Effective information and partial information decomposition (Hoel et al. 2013; Rosas et al. 2020) are mentioned only as complementary "causal tests" (p. 4).
- Dossier's summary: "strong emergence would require new causal principles unsupported by evidence". The paper's wording is stronger and methodological rather than evidential. Invoking strong emergence for consciousness or social behaviour "amounts to introducing new causal principles not anchored in substrate dynamics, and thus steps outside the scope of scientific method" (p. 7). This is asserted, not argued.
- Missing from the dossier: the paper affirms "Emergent phenomena possess causal power" and that society and culture "act as real forces" (p. 5). It endorses "downward or top-down causation" as higher-level constraint "without violating the underlying laws" (p. 7), and "a form of pluralism that affirms the reality of higher-level causal powers" (p. 8, citing Simpson & Horsley). It never reconciles this with the claim that emergence is "not … a metaphysical extra cause" (p. 8). This tension is the paper's real metaphysical content.
- Minor technical slip: "At the critical point T = Tc … the actual state chooses a specific direction, resulting in m ≠ 0" (p. 4). For the continuous transition the paper describes, m = 0 at Tc and becomes non-zero only below it.
- Minor citation slip: gliders in Conway's Game of Life are cited to ref. 12, which is Barnett & Seth 2023 on dynamical independence.
- Minor: the herd-immunity section's rigour rests on the author's own co-authored papers (refs. 141, 143, 144), summarised rather than reproduced. The paper has no data (acknowledgements: "This work does not involve underlying data").
- Missing link: the paper cites McKenzie's survey (ref. 133 = [LIT-141](../literature.d/LIT-141.md)) for the claim that the mesoscale is "where compression, autonomy, and universality come together" (p. 5). It also cites De Haro & Butterfield's duality book (ref. 121 = [LIT-199](../literature.d/LIT-199.md)) and Varley & Hoel (ref. 53 = [LIT-027](../literature.d/LIT-027.md)).
- Missing topic: `epistemology` is justified. The Levels of Description section argues that what is called emergent "typically depends on … epistemology" (p. 2), and the paper's core distinction is explanatory versus ontological reduction.
- metaphysics tag: justified. See Bearing on the record.
- primary topic: philosophy-of-science. The paper's main job is conceptual clarification of a scientific term: what "emergence" should mean in physics, biology and social science, and what counts as scientific method. Its metaphysical theses (physicalism, higher-level causal powers) are asserted rather than argued. `metaphysics` should stay as a tag. `complex-systems`, the current lead, also fits well. It is a defensible alternative lead, but the paper is about the concept rather than about any complex system.
