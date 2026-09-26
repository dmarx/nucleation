---
number: 52
status: Read
formerly:
- NOTE-tmpevggu
paper: LIT-056
title: 'Consciousness in AI: indicator properties'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (I read the full text of arXiv:2308.08708v3 (22 Aug 2023;
    v1 17 Aug and v2 21 Aug, all three listed at 1,543 KB), 88 PDF pp. That
    covers the title page and the p. 1 footnote, the author list and
    authorship, funding and conflicts page, the Executive Summary with Table
    1, §1 (terminology; the three methodological assumptions; Boxes 1–2), §2
    (RPT, GWT, higher-order theories/PRM/HOSS, AST, PP, midbrain, UAL,
    agency and embodiment, time and recurrence; Box 3 on attention; Table 2
    of entailments), §3 (implementations; case studies of Transformer LLMs,
    Perceiver/Perceiver IO, PaLM-E, the virtual rodent and AdA), §4 (under-
    and over-attribution; capabilities; recommendations; Box 4) and the
    Glossary (pp. 71–74). The bibliography (pp. 75–88) I scanned rather than
    read entry by entry. Extraction was with PyMuPDF. I checked Crossref for
    the later journal version: "Identifying indicators of consciousness in
    AI systems", Trends in Cognitive Sciences 30(6), 488–501 (issue June
    2026; DOI 10.1016/j.tics.2025.10.011), 20 authors. I could not read it:
    the Cell page returned 403. I did not compare v1 or v2 against v3 beyond
    the footnote that documents the change.). Upgraded from `Skimmed` to
    `Read`: the claims table, assumptions and results are new, and the skim
    is corrected where the full text disagreed.
date: '2026-09-25'
summary: >-
  The report assumes computational functionalism and takes a
  "theory-heavy" approach. From it the authors derive 14 indicator
  properties: RPT-1–2, GWT-1–4, HOT-1–4, AST-1, PP-1 and AE-1–2. The claim
  for them is only that more of them raises the probability of
  consciousness. They assess a handful of systems against subsets of the
  list and conclude that no current system "appears to be a strong
  candidate". Transformer LLMs have "only a relatively weak case" for any
  GWT indicator, because a single forward pass has no recurrence or global
  broadcast. Perceiver arguably has GWT-1, GWT-2 and half of GWT-4 but
  lacks broadcast. Among the embodied agents, AdA is the likeliest to meet
  AE-2. Most indicators could be built with standard ML techniques. The
  abstract's "no current AI systems are conscious" is stronger than
  anything the body shows.
---

<!-- inactive-ok-file: LIT-066 — Deferred; named in Connections, not yet read closely -->
<!-- inactive-ok-file: LIT-080 — Deferred; named in Connections, not yet read closely -->

# NOTE-052: Consciousness in AI: indicator properties

## Contribution

The report turns "could this AI system be conscious?" from an intuition or behavioural-test question into an architectural audit. It rests on three things:
- **An explicit conditional premise:** computational functionalism, adopted "as a working hypothesis … for pragmatic reasons" (§1.2.1).
- **A survey of the scientific theories** compatible with that premise.
- **A list of 14 computationally stated indicator properties**, each drawn from a theory that holds it to be necessary, or jointly sufficient with others. The report adds Table 2, which records the entailments between indicators (e.g. GWT-3/4 ⇒ RPT-1; PP-1 ⇒ RPT-1 and HOT-1).

It then shows, section by section, how each indicator could be built with existing ML, and applies part of the rubric to five named system families.

## Key insight

Behaviour cannot settle AI consciousness, because systems can be trained to mimic human reports while working differently ("gaming"; §1.2.3). If computational functionalism is granted, the question becomes whether the system implements the algorithms that the best-supported theories tie to consciousness. The answer is graded by three things (§1.2.3):
- (a) how similar the implementation is;
- (b) credence in the theory;
- (c) credence in functionalism.

On that reading, the obstacle to building candidate systems is combining known components, not inventing new ones. Whether a trained network has an indicator can depend on what it learned rather than on its architecture, which makes interpretability part of the method (§3, lesson 2).

## Assumptions

- **Computational functionalism.** "Implementing computations of a certain kind is necessary and sufficient for consciousness" (§1.2, assumption 1). It operates at Marr's algorithmic and representational level, not the input–output or implementation level (§1.2.1). Theories that deny it are set aside: IIT, biological interpretations of RPT, and nanoscale-metabolism or material-composition views (§2.1.3, §2.4, §2.4.5(c)).
- **Validity of the theories.** Neuroscientific theories built from contrastive analysis in healthy adult humans (report, no-report and metacognitive paradigms) identify functions that transfer to AI (§1.2.2).
- **Theory-heavy over theory-light.** The report accepts Birch's objection that human evidence does not say how far conditions can be relaxed. It argues that this does not stop more-similar systems from being better candidates (§1.2.3).
- **Narrow formulation.** Indicators involving the environment (agency, embodiment, self-maintenance) are restated "narrowly", as internal models and learning dispositions, so that they are functionalism-compatible (§2.4.5(c)). As a result, a system controlling a virtual avatar can count as embodied.
- **Simplifications flagged by the authors.** Consciousness is treated as all-or-nothing for convenience (Box 1). Valence, and the kinds of experience a system would have, are set aside (§4.1.1, Box 4).

## Key results

- **Indicators (Table 1; §2.5):**

  | theory | indicators |
  |---|---|
  | Recurrent processing theory | RPT-1 algorithmic recurrence in input modules; RPT-2 organised, integrated perceptual representations |
  | Global workspace theory | GWT-1 parallel specialised modules; GWT-2 limited-capacity workspace with bottleneck and selective attention; GWT-3 global broadcast to all modules; GWT-4 state-dependent attention usable to query modules in succession |
  | Computational higher-order theories | HOT-1 generative, top-down or noisy perception; HOT-2 metacognitive monitoring separating reliable percepts from noise; HOT-3 agency guided by a general belief-formation and action-selection system, strongly disposed to update on monitoring outputs; HOT-4 sparse and smooth coding giving a "quality space" |
  | Attention schema theory | AST-1 predictive model of, and control over, attention |
  | Predictive processing | PP-1 predictive coding in input modules |
  | Agency and embodiment | AE-1 learning from feedback to pursue goals, especially with flexible responsiveness to competing goals; AE-2 an output–input (forward) model used in perception or control |

- **Algorithmic versus implementational recurrence (§2.1.3).** An unrolled RNN with shared weights is algorithmically, not implementationally, recurrent. The report adopts only the algorithmic reading, citing Lamme's personal communication that RPT admits it.
- **Implementation feasibility (§3.1).**
  - RPT-1: RNNs, LSTMs and GRUs.
  - PP-1: PredNet and related predictive-coding networks.
  - RPT-2: partially, via PredNet's Kanizsa-contour sensitivity (which Lamme says is "inference", not organisation), MONet and OSRT.
  - HOT-4: DNN representation spaces are smooth, and sparsity can be added by regularisation.
  - HOT-1/2: first-order networks plus scalar second-order "realness" networks, e.g. GAN discriminators or GFlowNet world models.
  - HOT-3: sketched as a Transformer whose query–key scores are multiplied by "real" tags.
  - AST-1: Liu et al. 2023.
  - AE-1: RL is argued to be sufficient.
  - AE-2: rare in current systems. One example is Friedrich et al. 2021 (Kalman-filter forward model in control).
- **Case studies (§3.2):**
  - **Transformer LLMs.** The residual-stream reading might give GWT-1–3, but the dimensionality is not a bottleneck (it equals the input's). "More fundamentally … Transformers are not recurrent": no module both writes to and reads from the stream. Verdict: "only a relatively weak case" for any GWT indicator.
  - **Perceiver / Perceiver IO.** Arguably GWT-1, GWT-2 and the first half of GWT-4, but the number of sequential inputs is bounded by the cross-attention layers. There is no global broadcast: one output module per query, and input modules receive nothing back.
  - **PaLM-E.** Its components are trained by imitation (next-token prediction; a behavioural-cloning policy) and not end-to-end on the effects of its own outputs, so agency and embodiment are doubtful. The best case is the policy unit.
  - **Virtual rodent** (38-DoF body, LSTM actor–critic trained end-to-end by RL). It has agency. Embodiment is possible, but the tasks may be solved by stereotyped movements in a static environment.
  - **AdA** (Transformer over hundreds of past timesteps into an LSTM predicting actions, values and rewards; meta-RL). The "most likely of the three" to be embodied by the report's standard.
- **Implications (§4).**
  - Under-attribution risks moral harm, while over-attribution misallocates resources, undermines better-evidenced claims, may conflict with beneficial training, and exposes users to manipulation.
  - Consciousness does not imply human-like motives or emotions.
  - Existential-risk arguments do not assume consciousness.
  - The recommendations are research funding, prospective and retrospective theory-heavy assessment with interpretability, and theory-informed policy.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Assessment of AI consciousness is "scientifically tractable" | informal argument | §1.2 (conditional on computational functionalism and on the surveyed theories; both are stated as uncertain) |
| C2 | Behavioural tests are unreliable for AI because systems can be trained to mimic human behaviour | informal argument | §1.2.3; LLMs cited as an existence case; no empirical test |
| C3 | Systems with more indicator properties are more likely to be conscious | informal argument | Stated as the report's operative claim (§2 intro, §2.5); no weighting or aggregation rule; indicators are not independent (Table 2) |
| C4 | No current AI system is a strong candidate for consciousness | weak | Case studies cover five system families on subsets of indicators (GWT for LLMs and Perceiver; AE for three agents); no system scored on all 14 |
| C5 | "No current AI systems are conscious" (abstract) | assertion | Stronger than C4; not what the method can deliver, since it yields credences, not verdicts |
| C6 | Most indicators can be implemented with existing ML techniques | moderate | §3.1 walks through each indicator with cited systems or sketches; HOT-3 and GWT-4 training regimes are acknowledged open |
| C7 | Transformer LLMs have only a weak case for GWT indicators because a Transformer is not recurrent and has no distinct workspace with broadcast | moderate | Architectural argument (§3.2.1) about a single forward pass. Autoregressive feedback of generated tokens, which applies the same weights repeatedly, is not discussed as possible algorithmic recurrence (RPT-1 by the report's own glossary definition) or as broadcast |
| C8 | Reinforcement learning suffices for agency in the AE-1 sense | informal argument | §2.4.5(a), §3.1.5, building on Dretske and Butlin 2022/2023; bandits noted as a possible exception |
| C9 | Among PaLM-E, the virtual rodent and AdA, AdA is likeliest to meet AE-2 | weak | Reasoning from training objective and environment; no interpretability evidence that any learned a forward model used in perception or control |
| C10 | If computational functionalism is true, conscious AI could realistically be built in the near term | informal argument | Executive Summary; §3 "lesson 3"; conditional on functionalism and on theories the authors decline to rank |
| C11 | Consciousness does not entail human-like motives or emotions, and x-risk arguments do not presuppose consciousness | informal argument | §4.2; conceptual |

## Method

The procedure has four steps.
1. **Fix the premises:** computational functionalism, and the evidential standing of scientific theories.
2. **Extract indicators from each theory.** For each theory the report extracts computationally stated conditions. Readings that conflict with functionalism are set aside: biological RPT, IIT and material-composition views. Readings that are too liberal (Russell–Norvig agency) or duplicate other indicators (intentional agency, which is already in HOT-3) are rejected, with reasons given in each subsection.
3. **Record dependencies:** the entailments and independences between indicators (Table 2).
4. **Assess candidate systems.** For each indicator the report describes how an ML system could possess it (§3.1). For each chosen system it argues from architecture and training objective whether it plausibly does (§3.2). Credence is to be combined informally from similarity × theory credence × functionalism credence (§1.2.3). No formal scoring procedure is given, and the authors say one "is questionable … at present" (Box 4).

## Concepts

- **Phenomenal consciousness**: "something it is like" to be the system. The report's sole target, distinguished from access consciousness (availability for report, reasoning and action).
- **Computational functionalism**: the right computations, at the algorithmic and representational level, are necessary and sufficient. The substrate matters only through which algorithms it can implement.
- **Theory-heavy approach**: assessing systems by whether they implement theory-specified processes, rather than by theory-neutral behavioural signatures (after Birch 2022b, who argues for "theory-light" in animals).
- **Indicator property**: a property that credible theories hold to be necessary or jointly sufficient. The report claims only that its presence raises the probability of consciousness.
- **Algorithmic versus implementational recurrence**: repeated application of the same operation (e.g. weight-shared layers, unrolled RNNs), as against physical feedback loops through the same units.
- **Global workspace / global broadcast / ignition**: a limited-capacity shared representation, selected into by competition and made available to all modules. Ignition is its non-linear, step-like onset in the neural version.
- **Perceptual reality monitoring (PRM)**: consciousness as a higher-order tag marking first-order perceptual activity as reliable ("real") rather than noise or imagination, feeding a belief and action system with "assertoric force".
- **Quality space**: the similarity/discriminability space of phenomenal qualities, hypothesised to depend on sparse, smooth coding.
- **Narrow formulation**: stating agency and embodiment indicators as internal models and learning dispositions rather than as actual environmental relations, so that they are consistent with functionalism.
- **Embodiment (AE-2)**: having and using a model of output→input contingencies, including systematic effects, for perception (self versus exogenous change) or motor control. Planning use alone does not count.

## Connections

The report builds on Birch's theory-light/theory-heavy distinction and on Chalmers (2023) "Could a large language model be conscious?". It builds on the theories themselves:
- Lamme (RPT);
- Baars, and Dehaene, Changeux and Mashour (GWT);
- Lau, Michel and Fleming (PRM/HOSS);
- Graziano (AST);
- Seth, Hohwy and Clark (PP);
- Merker (midbrain);
- Ginsburg & Jablonka (UAL).

Several of its GWT implementation sketches come from its own authors, Bengio's group and VanRullen–Kanai.

Relations to nucleation:
- **[LIT-025](../literature.d/LIT-025.md)** (ΦID review, Mediano et al.). The report sets IIT aside but mentions "weak IIT" (Mediano et al. 2022), on which integration and differentiation measures correlate with global states (wake, sleep, coma). It says this "does not (yet) tell us which measures to rely on" for AI. [LIT-025](../literature.d/LIT-025.md)'s synergy and causal-emergence measures are candidates for exactly that gap. The report does not engage them.
- **[LIT-080](../literature.d/LIT-080.md)** (Vohryzek et al., whole-brain models of brain states) concerns global states of consciousness (metastability, psychedelics), the dimension the report explicitly does not address; its question is which states are conscious, not level or state. The two are complementary, not in tension.
- **[LIT-066](../literature.d/LIT-066.md)** (Lindahl et al., meditation-related experiences) is phenomenological, on human experience reports. It illustrates the report-based evidence base the report relies on and criticises (§1.2.2).

The network readings named in the brief ([LIT-020](../literature.d/LIT-020.md), [LIT-004](../literature.d/LIT-004.md), [LIT-028](../literature.d/LIT-028.md)) have no substantive connection to this work.

## Bearing on the record

**Does it belong in the Anthology of the SOTA rather than here? Yes, as a LIT note there. Flagging, not moving.**
- Its subject is properties of AI systems, its method is an evaluation rubric, and it assesses named ML architectures:
  - Transformer residual streams;
  - Perceiver cross-attention bottlenecks;
  - RL agents' forward models;
  - GAN discriminators as metacognitive monitors.
- It argues a measurement-validity point: behavioural tests are gameable by imitation training, so architecture and interpretability evidence is required. That is what the anthology's `analysis-and-evaluation` topic covers: "what to measure, what a measurement cannot tell you … theory, interpretability". Its §4 over-attribution and policy material fits `deployment-and-society`.
- Under [ANTH-ADR-059](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/decisions.d/ADR-059.md) the topics are an axis, not a scope, so "consciousness is not an ML topic" is not a reason to decline it there.
- Suggested anthology tags: `analysis-and-evaluation` first, `deployment-and-society` second, `model-architecture` arguably third, given how much of §3.2 is architectural analysis.

It would source a note, not a practice:
- The nearest instruction-shaped claim is "assess consciousness-relevant properties by architecture and interpretability, not behaviour" (C2). It is argued, not tested, so it could not by itself carry an ANTH-SOTA.
- It carries no ANTH-THEORY about why an ML technique works.

Nucleation should keep, or cross-reference, it for its consciousness-science content: the §2 survey is one of the clearer compact statements of RPT, GWT, PRM, AST and PP and their evidence.

Two aging notes for whoever files it in the anthology:
1. §3.2.1's verdict is about a single forward pass of the 2021 residual-stream picture (Elhage et al.). The anthology's own notes record residual-stream designs that have since changed shape: [ANTH-LIT-141](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-141.md) (Hyper-Connections), [ANTH-LIT-140](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-140.md) (mHC) and [ANTH-LIT-134](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-134.md) (Attention Residuals, learned attention over earlier layers). The report does not address, and I do not claim, whether those change the GWT analysis.
2. The report never considers autoregressive token feedback as algorithmic recurrence.

The TiCS 2026 version should be checked as the anthology's citable source.

For nucleation THEORY documents: none exist to support or contradict.

## Limitations

- **Everything is conditional on computational functionalism**, which the authors call "disputed". Credences in it vary across the authors, and no aggregate is given (§1.2.1).
- **No aggregation rule.** The indicators are unweighted and interdependent (Table 2). Some are described as "plausibly necessary conditions that do not make consciousness significantly more likely in isolation" (RPT-1, GWT-1, HOT-1; p. 45). The rubric therefore cannot produce the verdict the abstract states (C5).
- **Partial case studies.** Only GWT is applied to LLMs and Perceiver, and only AE to the three agents. HOT, AST, PP and RPT-2 are not assessed for any named current system. The analysis of LLMs is of the forward pass. Autoregressive generation, tool use and agent scaffolds are not considered, although they bear directly on RPT-1, GWT-3 and GWT-4.
- **Indicator status depends on what was learned.** Whether a system has an indicator can depend on learned internals (lesson 2, §3), yet no interpretability evidence is brought for any system.
- **Theory selection.** IIT, and any theory that ties consciousness to biology, is excluded by the functionalist premise, not by evidence. The relaxation problem (how far human-derived conditions can be loosened) is acknowledged and not solved (§1.2.3).
- **Scope exclusions by design:** valence and moral status (the practically decisive question) are set aside (§4.1.1, Box 4).
- **The architecture verdicts age quickly.** The report dates from 2023 (GPT-4, PaLM-E, AdA era).

## Open questions

- Does autoregressive generation, or an agentic loop, give LLM-based systems algorithmic recurrence and a broadcast-like workspace in the report's own sense? What would an interpretability test for GWT-3 or GWT-4 in such a system look like?
- Can the indicators be weighted and aggregated into credences defensibly? Box 4 doubts it is justified now. A calibration against animal cases (theory-light evidence) would be the obvious test.
- Which measures from "weak IIT" or information decomposition, if any, carry over to artificial systems as indicators ([LIT-025](../literature.d/LIT-025.md)'s territory)?
- A computational theory of valence: what would make an AI system capable of experiences that feel good or bad (Box 4)?
- Does the 2026 TiCS version change the indicator list or the case-study verdicts?

## Corrections to the seeded skim

- **The footnote change is larger than the dossier records.** The dossier says "shows" became "suggests". The p. 1 footnote gives the earlier sentence as "…but also shows that there are no obvious barriers to building conscious AI systems". v3 reads "…suggests that there are no obvious technical barriers to building AI systems which satisfy these indicators". The object changed from "conscious AI systems" to "systems which satisfy these indicators", with an explicit note that "satisfying the indicators would not mean that such an AI system would definitely be conscious". The body keeps the stronger conditional: the Executive Summary says "if computational functionalism is true, conscious AI systems could realistically be built in the near term", and p. 47 says "If it is possible at all to build conscious AI systems without radically new hardware, it may well be possible now".
- **The abstract claims more than the body shows.** Abstract: "Our analysis suggests that no current AI systems are conscious". Executive Summary: "no current system appears to be a strong candidate". §3.2: "This work does not suggest that any existing AI system is a strong candidate". The body never assesses any system against all 14 indicators and assigns no credences. The dossier's summary uses the body's weaker form, which is correct, but does not flag the gap.
- **"Prior systems have been built to implement GWT and AST" (dossier) needs qualifying.**
  - VanRullen & Kanai (2021) is "a 'roadmap' to a possible implementation, rather than a working system" (p. 50).
  - Goyal et al.'s (2022) "modules" were token or patch processors, so "it is questionable whether they were specialised subsystems".
  - Of the AST systems, Wilterson & Graziano's had a non-predictive schema over an input "spotlight". Liu et al.'s had a learnt predictive model, but only in simple 2D multi-agent RL.
  - The report's own summary is that neither GWT study "produced a working system that clearly satisfies all four GWT indicators".
- **The journal version is now verified in metadata.** The dossier's "reportedly in Trends in Cognitive Sciences, 2025; unverified" becomes: TiCS 30(6):488–501, print issue June 2026, DOI 10.1016/j.tics.2025.10.011, 20 authors (Butlin, Long, Bayne, Bengio, Birch, Chalmers, … VanRullen). Bayne and Chalmers are added; Frith is not listed. Its content was not read.
- The rest of the dossier's skim matches the text:
  - the 14-indicator table;
  - IIT excluded as incompatible with computational functionalism (weak IIT noted but set aside);
  - RPT-1 already met by existing systems;
  - AE-1's first part "arguably" met by RL;
  - the case-study list.
