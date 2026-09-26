---
number: 124
status: Read
formerly:
- NOTE-tmpfgy3y
paper: LIT-141
title: 'McKenzie — Emergence from physics to computer science'
version: 2
history:
- version: 2
  date: '2026-09-26'
  note: >-
    Read in full (full text of arXiv v4 (dated 2 July 2026), 187 pp. Body
    pp. 1–149 read in full: abstract, table of contents, §§1–24 including
    every case-study section (§§4–20), acknowledgements and all lettered
    footnotes a–y. References 1–474 (pp. 149–187) were checked for every
    citation used below, not read item by item. Several equations and
    figures are images and did not survive text extraction (e.g. the Ising
    Hamiltonian p. 29, Lorenz equations p. 42, Figs. 1–2, 4–8); their
    captions and surrounding text were read.). Upgraded from `Skimmed` to
    `Read`: the claims table, assumptions and results are new, and the skim
    is corrected where the full text disagreed.
date: '2026-09-26'
summary: >-
  Sole-authored survey by a condensed-matter physicist. It takes novelty
  (a property the parts lack) as the defining mark of emergence and sets
  it against twelve other characteristics in §2. The six "objective" ones
  are discontinuities, order, modification of parts, universality,
  diversity and mesoscale modularity. The six "subjective" ones are
  self-organisation, unpredictability, irreducibility,
  contextuality/downward causation, complexity and intra-stratum closure.
  Case studies from the Ising model to Schelling segregation and LLMs show
  that each can come apart from novelty: novelty without discontinuity
  (Kondo, Fermi liquids, spin ice), without unpredictability (BKT, spin
  ice), and with reduction (Butterfield). §22 sides with weak emergence
  and argues that strong-emergence claims from molecular structure are
  weak.
---
<!-- inactive-ok-file: LIT-110 — Deferred: a related work named by a 2026-09-26 close reading on the metaphysics tag; lapses when the cited work is read -->

# NOTE-124: McKenzie — Emergence from physics to computer science

## Contribution

A book-length (187 pp.) pedagogical survey, now in its fourth arXiv version. It gives a single working definition of emergence (novelty), a vocabulary of twelve further characteristics, and a systematic run of that vocabulary over about thirty case studies across physics, chemistry, biology, economics, sociology and computer science. What it adds is the case-by-case demonstration that the characteristics are logically independent of novelty and of each other. It also adds a physicist's defence of effective theories and toy models as the methods of emergence, and a sustained argument (§15) against using molecular structure as evidence for strong emergence.

## Key insight

Define emergence by novelty alone, then treat every other putative mark as a separate empirical question. Each can be present or absent in a given system: discontinuity, universality, unpredictability, irreducibility, mesoscale modularity. Condensed matter, "simple enough to be amenable to detailed and definitive analysis but complex enough to exhibit rich and diverse emergent phenomena" (idea 7, p. 6), is the place to find out which. The recurring constructive move is to find the emergent mesoscale at which new, weakly interacting entities (quasiparticles, domains, vortices, foldons, communities) appear.

## Assumptions

- **Definition**: a property of a many-part (or many-scale, or many-iteration) system is emergent iff "the individual parts of the system do not have this property" (§1.2 idea 1; §2.1). Alternative: a property absent when the parts' states are randomly assigned, i.e. absent at high temperature (p. 11).
- **Stratification**: "Reality is stratified. At each stratum (level) there is a distinct ontology … and epistemology" (idea 4). "Hierarchy" is avoided so that no level is privileged (§1.4).
- "Many" includes many iterations (dynamical systems, algorithms). For LLMs the "size of the system" is run time, dataset size or parameter count (p. 11–12).
- An equilibrium perspective is the author's default ("my implicit perspective if often that of thinking of a system in thermal equilibrium", p. 11).
- The objective/subjective split is explicitly fuzzy (p. 17).

## Key results

This is a survey, so the results are its argued conclusions and demonstrations:

- **Independence of characteristics from novelty** (§2 and case studies). Novelty without discontinuity: Kondo effect ("novelty does not necessarily imply discontinuity", p. 58), Fermi liquids, spin ices, quantum-statistics crossovers (p. 61). Discontinuity without novelty: the liquid–gas transition, adiabatically connected (p. 13). Novelty without unpredictability: BKT and the hexatic phase were predicted first ("unpredictability is not equivalent to novelty", p. 65), as were spin ice and quantum-statistics properties. Novelty with reduction: Butterfield's four rigorous cases (p. 20).
- **Ising model as emblem** (§4). Novelty via spontaneous symmetry breaking; Tc = 2.25J quoted for the square lattice (the exact value is 2/ln(1+√2) ≈ 2.269 J/k_B, so this is rounded); no symmetry breaking for finite N; mean-field fails for d = 1 and gives correct exponents only for d ≥ 4; frustrated hcp model with 32 ground states; ANNNI devil's staircase.
- **Unpredictability in practice**: most states of matter were found experimentally, not predicted. The exceptions (BEC, topological insulators, Anderson insulator, Haldane phase, hexatic) all started from effective Hamiltonians, "None started with a microscopic Hamiltonian for a material with a specific chemical composition" (p. 19). DFT-based superconducting Tc predictions typically differ from experiment "by the order of 50 percent" (p. 57).
- **Molecular structure is not strongly emergent** (§15). The BOA treats nuclei quantum-mechanically, so it does not violate the uncertainty principle (against Cartwright). Corrections are small, O((mₑ/M)^{1/2}). Non-BO calculations (Lang et al.) recover the triangular D₃⁺ structure. Electron–nuclear entanglement in benzene is very small. Decoherence matters only for degenerate structures such as ammonia (tunnel splitting 0.8 cm⁻¹ versus about 10⁻⁸ cm⁻¹ for PH₃).
- **Causal-emergence measures** (§14). The field has two frameworks: Hoel's effective information, which needs a coarse-graining fixed beforehand, and Rosas's PID, which gives a sufficient condition only. The section notes an "unrecognised similarity" with real-space mutual-information coarse-graining for phase transitions (Gokmen et al.).
- **LLMs** (§21.2): see corrections for the exact claims. The conclusion there is that emergent abilities satisfy novelty (against a random baseline) and diversity, while discontinuity is unresolved (no agreed metric or order parameter, finite-size issues).
- **Philosophy** (§22): most physicists hold weak emergence. Explanation is context-relative. What is "fundamental" is contested (Laughlin's exactness argument, Adlam). Quasiparticles are argued to be real (Falkenburg, Wallace, against Gelfert). Structuralism is "hard to justify".
- **Strategy** (§24): recommends a balanced funding portfolio, scepticism of brute-force "big science" (Human Brain Project, materials by design), and humility about controlling emergent properties.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Novelty is the defining characteristic of emergence | assertion | stipulated (§2.1); the author disclaims that it is better than alternatives |
| C2 | None of the twelve other characteristics is established as necessary or sufficient for novelty | moderate | counterexamples across case studies (Kondo, BKT, liquid–gas, Butterfield); no systematic logical analysis, which §24 leaves open |
| C3 | Reality is stratified, each stratum with its own ontology and epistemology | assertion | illustrated by Tables 1–3 and Figs. 2, 7; not argued against rivals |
| C4 | Identifying an emergent mesoscale with weakly interacting entities is the key insight in explaining emergence | informal argument | many examples (quasiparticles, domains, foldons, modules); a general existence question is posed as open (quasiparticle conjecture, p. 55) |
| C5 | Most new states of matter were not predicted; the successful predictions all started from effective Hamiltonians | moderate | historical enumeration (p. 19); not a systematic survey |
| C6 | Molecular structure gives no good evidence for strong emergence | informal argument | §15: BOA analysis, non-BO calculations (Lang et al.), entanglement estimates; responds to Primas, Cartwright, Hendry |
| C7 | Wei et al. made the LLM "phase transition" perspective "concrete and rigorous" | assertion | contradicted in the same section by the author's own report that agreed discontinuity metrics are lacking (Schaeffer et al.) and that true discontinuities need the thermodynamic limit |
| C8 | LLM emergent abilities show novelty relative to a random baseline | weak | reported from Wei et al.'s near-random-then-above-random curves; no independent analysis |
| C9 | Structuralism is an intellectual position that is hard to justify | informal argument | the Ising model's micro/meso/macro interplay (§§4, 22); structuralism is characterised through Cao's definition only |
| C10 | Brute-force big-science initiatives on emergent problems tend to disappoint | informal argument | anecdotes (GSK and the Human Genome Project, Human Brain Project, AlphaFold memorisation question); no systematic evidence |

## Concepts

- **Emergent property** — one the parts lack (novelty). The book extends "property" to state, phenomenon, process or entity (p. 12).
- **Stratum** — a level with its own ontology (entities, properties, interactions) and epistemology (theories, concepts, methods). It is well-defined when there is closure (p. 8).
- **Mesoscale / modularity** — an emergent intermediate scale at which new entities interact weakly (e.g. correlation length, coherence length, Kondo temperature, W/Z mass).
- **Effective theory vs toy model** — an effective theory is "an accurate representation of reality" at a scale. A toy model uses minimal degrees of freedom, interactions and parameters to show what is possible, and "should not be viewed as effective theories" for real materials (spin ice, p. 65).
- **Protectorate** (Laughlin) — universality hiding micro "ultimate causes".
- **Intra-stratum closure** — following Rosas et al.: informational and causal closure (shown equivalent) and computational closure (weaker, "strongly lumpable").
- **Objective vs subjective characteristics** — observable properties of the system (ontology) versus features of how the investigator thinks about it (epistemology). The split is explicitly fuzzy.
- **Top-down / bottom-up** — condensed-matter usage: top-down goes from long to short length scales. High-energy physics uses the opposite, so §11 renames them "low-energy" and "high-energy" approaches.

## Connections

The book is cited by Rizi ([LIT-150](../literature.d/LIT-150.md), x30), whose coarse-graining view it overlaps but does not share. McKenzie's mark is novelty relative to parts; Rizi's is predictive many-to-one maps. §14's causal-emergence review covers the Hoel effective-information and Rosas PID frameworks that the record holds through Varley & Hoel ([LIT-027](../literature.d/LIT-027.md)) and Mediano et al. ([LIT-025](../literature.d/LIT-025.md)). The book's §2.12 closure notions are from Rosas et al.'s 2024 "Software in the natural world", which is not held. The AdS/CFT discussion (§12) quotes Crowther that neither dual side should be called emergent. That is the position De Haro & Butterfield ([LIT-199](../literature.d/LIT-199.md)) develop and Le Bihan ([LIT-113](../literature.d/LIT-113.md)) discusses. The biology sections (§18) touch the extended-synthesis debate. Noble's "biological relativity" (no privileged causal level) and Ball's "causal spreading" are close to the organism-centred views of Baedke ([LIT-167](../literature.d/LIT-167.md), [LIT-110](../literature.d/LIT-110.md)), and to exactly the interlevel-causation question Hazelwood ([LIT-156](../literature.d/LIT-156.md)) presses. McKenzie reports Noble's upward and downward causation without engaging the exclusion or composition worry.

**Metaphysical thesis.** The book defends a stratified, pluralist ontology. Each stratum has "a distinct ontology (what is real)". Quasiparticles, and by parity share values, are real. No level is privileged or "more fundamental". This is combined with weak emergence (§22) and a rejection of strong emergence from chemistry (§15). It presupposes that novelty relative to parts is an objective feature of systems. These are theses about levels, reality and fundamentality, so the `metaphysics` tag is **justified**. The book states them from a physicist's side and explicitly defers "the philosophical questions" (§24 "Open questions").

## Bearing on the record

- No THEORY follows. The book is a hub citation for emergence examples and for the characteristics vocabulary.
- For ML practice: §21 is a secondary account of the emergent-abilities debate. It carries nothing the anthology does not hold first-hand in Wei et al. ([ANTH-LIT-470](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-470.md)) and Schaeffer et al. ([ANTH-LIT-471](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-471.md)). If the anthology ever cites McKenzie, cite the discontinuity paragraph (p. 138: no agreed metrics, order parameters or finite-size analysis), not the "concrete and rigorous" sentence (p. 135), and note the FLOPs mis-gloss. The pointers to Nam et al. (exactly solvable multitask sparse parity), Mehta & Schwab (RG and deep belief nets) and Bahri et al. are candidates for the anthology's reading list if not already held; they were not found by title in its literature directory.
- The §14 remark on the "unrecognised similarity" between causal-emergence measures and RSMI coarse-graining is a concrete, citable open connection.

## Limitations

- The definition is stipulated, and the logical relations among the thirteen characteristics are left open by the author (§24).
- Case studies are illustrative and selective, with no systematic coverage. Referencing is "selective, and is based on accessibility" (p. 5).
- Philosophical positions (Primas, Cartwright, Hendry, Ellis/Drossel, structuralism) are engaged through quotation and short replies. Structuralism in the humanities is characterised through a single definition (Cao).
- §21.2's headline claim about Wei et al. is unsupported by, and in tension with, the section's own analysis. There are also small factual slips (FLOPs gloss, 2023/2024 Nobel, section numbering, name and citation errors).
- The economics and sociology sections carry evaluative asides on political positions (Hayek, Marxism, structure versus agency) that are argued by analogy to physics, not by evidence from those fields.

## Open questions

- Are the characteristics logically related? Is any necessary or sufficient for novelty, or for another? The author poses this and gives counterexamples only.
- Does every system with physically reasonable interactions admit a weakly interacting quasiparticle description (the "quasiparticle conjecture", p. 55), and is there a general method to find the modules from the Hamiltonian?
- Can causal-emergence measures (Hoel, Rosas) be unified with RSMI-optimised coarse-graining, and made to work for systems whose symmetry breaking needs the thermodynamic limit?
- For LLMs: is there an order parameter and a finite-size scaling analysis under which a capability onset is a genuine transition rather than a metric artefact?

## Corrections to the seeded skim

- Authorship: sole author, Ross H. McKenzie (University of Queensland). There is no "et al.".
- Dossier: "§21 … recounting Wei et al.'s (2022) 'emergent abilities' as a phase-transition-like onset with scale". This understates §21.2 and does not say exactly what it claims. What McKenzie says about LLM emergent abilities (pp. 135–138):
  (i) The ChatGPT surprise made it seem "like the field underwent a 'phase transition.' That perspective turns out to be more than just a physics metaphor. It was made concrete and rigorous in a paper, 'Emergent Abilities of Large Language Models' … by Wei et al." (ref. 30 = [ANTH-LIT-470](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-470.md)). He quotes Wei's definitions ("An ability is emergent if it is not present in smaller models but is present in larger models"; few-shot ability "emergent when a model has random performance until a certain scale") and reproduces Wei's modular-arithmetic panel (onset near 10²² training FLOPs).
  (ii) He then quotes Schaeffer et al. (ref. 441 = [ANTH-LIT-471](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-471.md)) at length: apparent emergence is due to "the researcher's choice of metric", and "nonlinear or discontinuous metrics produce apparent emergent abilities". He notes their appeal to neural scaling laws (Hestness et al. 2017), and says the critique "did not quench interest", citing Berti et al.'s 2025 survey.
  (iii) He reports Krakauer, Krakauer & Mitchell's view that LLMs show "emergent capabilities" but not "emergent intelligence".
  (iv) He then runs his own checklist on LLMs. Scales: compute, parameters, data, and "more complicated" ones such as depth and training tasks. Novelty: abilities "not explicitly designed for", and near-random performance until a threshold. Diversity: "Wei et al. listed 137 emergent abilities in an Appendix!", a count unverified against Wei et al. here. Discontinuities: "Researchers are struggling to find agreed-upon metrics that show clear discontinuities. That was an essential point of Schaeffer et al." In condensed matter a new phase needs an identified broken symmetry and order parameter, and true discontinuities "only exist in the thermodynamic limit", with finite-size subtleties. Unpredictability: unsurprising given black-box models. Modularity: circuits and modules, and Mehta & Schwab's RG–deep-belief-net mapping. Toy models: Nam et al.'s multitask sparse-parity model and Bahri et al.
  So the analogy is **not unexamined** in McKenzie. He states the metric critique and the order-parameter and thermodynamic-limit objection himself. But he never retracts the opening claim that Wei et al. made the phase-transition view "concrete and rigorous", which his own discontinuity paragraph undercuts. The headline and the analysis disagree.
- Error in §21.2: the Wei figure's axis is glossed as "training FLOPs [Floating Point Operations Per second]" (p. 136). Wei et al.'s x-axis is total training compute, a count of floating-point operations, not a rate ([ANTH-LIT-470](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-470.md) records "scale is proxied by training FLOPs").
- Dossier: "§2 splits characteristics into 'objective' (discontinuities, order, universality, modularity…) and 'subjective' (self-organisation, unpredictability, irreducibility, complexity…)". This is incomplete. The objective six also include "modification of the parts" and "diversity with limitations". The subjective six also include "contextuality and downward causation" and "intra-stratum closure" (Rosas et al.'s informational, causal and computational closure). McKenzie himself says "twelve characteristics, besides novelty" in §2 (p. 12) but "thirteen different characteristics" in §22 (p. 142). The count is inconsistent within the paper.
- Dossier check: "whether the novelty criterion does real work". Partly answered by the text. Novelty does work as a sorting device: the case studies repeatedly exhibit novelty without discontinuity, without unpredictability, and with theory reduction (Butterfield, §2.9: "novelty is not sufficient for irreducibility"). McKenzie concedes he offers no argument that novelty is better than rival definitions ("I don't claim that defining emergence in terms of novelty is necessarily better", p. 12). He invokes Wittgensteinian family resemblance as an alternative framing, and supplies a second, non-mereological test (novel relative to a random configuration or high-temperature state, p. 11), which he uses for LLMs.
- Dossier on §22: "notes Laughlin's claim that some emergent properties are exact and hence more fundamental than micro-theories". Correct. The dossier misses what §22 concludes. McKenzie's "impression is that most physicists would subscribe to a view of 'weak' emergence", against Ellis and Drossel's strong-emergence reading of condensed matter. He argues structuralism is "an intellectual position that is hard to justify", because the Ising model shows no scale (macro, meso or micro) deserves "greater importance or reality". The dossier also misses §15, the book's most sustained philosophical argument: strong-emergence claims from molecular structure (Primas, Cartwright, Hendry) "are weak", because the Born–Oppenheimer approximation treats nuclei quantum-mechanically and full non-BO calculations (Lang et al., D₃⁺) recover structure.
- Section numbering slip: in the table of contents and the text, §21's subsections are numbered "19.1 Neural networks" and "19.2 Large Language Models".
- Factual slip: §24 says "The 2023 Nobel Prizes illustrate the dilemma of size" (Hopfield; Jumper and Hassabis). These were the 2024 prizes, as §17 and §21 themselves say.
- Minor citation and name slips: "Emily Adam" for Emily Adlam (§22, ref. 452); ref. 440, cited for Sompolinsky's 1989 review, carries the title of the 2024 ref. 439; "Degeut" for Deguet (§2).
- Missing link: this work is cited by Rizi ([LIT-150](../literature.d/LIT-150.md), ref. 133).
- metaphysics tag: justified. See Connections.
- primary topic: philosophy-of-science. The book's organising theses are about scientific explanation, method, theory reduction and scientific strategy: effective theories versus toy models, and "the perspective taken about emergence … matters for scientific strategy". Only §§1.4, 22 and parts of §15 argue ontology directly. `complex-systems`, the current lead, is the best alternative. `metaphysics` should stay as a tag.
