<!-- scratch/atlas/atlas-v0.3.md -->

# The hyperarticle atlas, v0.3 (verbatim)

ChatGPT's A65 in the exchange "Hyper article interpretation" (share 6b0679de, the branch continued to U29, 2026-11-25 04:26 UTC), answering the owner's U29: "update the atlas to adda sketched outline to each microabstract. be sure to list relevant Nucleation record items (i.e. we are mapping the core fibers of the atlas)". Kept verbatim as the map the owner chose on 2026-11-25 ("A59 is probably the better decomposition. use the last message … as your map"); the lines for its fifteen scopes are ADR-tmpd3ckn. Its codes are as at main 23b9dff; its words are ChatGPT's.

---

# Nucleation Hyperarticle Atlas — v0.3
<text color="secondary" size="sm">Second draft revised with section outlines and source fibers · November 24, 2026</text>

This version retains the **15 primary hyperarticle scopes from v0.2**, but adds two things to each: a proposed narrative outline and a *core fiber* identifying the Nucleation records from which the article would be constructed.

I'm using *fiber* informally for now: the collection of source objects supporting a view at a particular region of the atlas. These are **candidate source spines, not exhaustive dependency closures**. In particular, the outlines may propose transitions that no existing ARG or CLAIM establishes.

The distinction between a proposed exposition and a claim held by Nucleation remains important. Most SYNTHESIS records are still Proposed, and a proposed experimental CASE is not evidence that its predicted result occurred.

<box border radius="lg" padding={3} gap={2}>
  **Atlas structure**

  <grid columns={3} gap={2}>
    <grid-item>
      <title size="2xl" tabularNums>15</title>
      <caption>Primary article scopes</caption>
    </grid-item>
    <grid-item>
      <title size="2xl" tabularNums>4</title>
      <caption>Thematic regions</caption>
    </grid-item>
    <grid-item>
      <title size="2xl" tabularNums>60</title>
      <caption>Proposed section beats</caption>
    </grid-item>
  </grid>
  <caption>Source references below use the repository snapshot at commit 23b9dff. Existing draft boundaries are retained unless explicitly identified as proposed editorial changes.</caption>
</box>

## I. Inquiry and its records

<box gap={4}>
  <box gap={2}>
    <row align="center" justify="between">
      <title size="lg">01. Inquiry Can Change the Question</title>
      <text color="secondary" size="xs">Source-rich</text>
    </row>
    **Microabstract.** Inquiry is not merely a process of selecting answers from a fixed space of possibilities. It can revise the language, observations, distinctions, and criteria by which answers become recognizable. This article develops inquiry as resource-bounded, revisable specification and examines how maintained conceptual capacities change the questions an investigator can practically pursue.

    **Sketched outline**

    1. **A question already contains a specification.** Define inquiry in terms of language, answer space, interventions, observations, criteria, and resources (TERM-095, CLAIM-470).
    2. **The inquiry frontier.** Show why formulating a question has a cost and how preserved abstractions alter which questions are affordable (TERM-092, CLAIM-475).
    3. **Refinement is not revision.** Distinguish improving answers under an existing specification from changing what would count as an answer (SYNTHESIS-114).
    4. **Inquiry into inquiry.** Consider collective question formation and the remaining problem of what makes revision self-governed (ARG-221, QUESTION-388).

    **Core fiber**

    <text color="secondary" size="sm">TERM</text> [TERM-095](https://github.com/dmarx/nucleation/blob/main/record/terms.d/TERM-095.md) · [TERM-092](https://github.com/dmarx/nucleation/blob/main/record/terms.d/TERM-092.md)

    <text color="secondary" size="sm">CLAIM / ARG</text> [CLAIM-470](https://github.com/dmarx/nucleation/blob/main/record/claims.d/CLAIM-470.md) · [CLAIM-475](https://github.com/dmarx/nucleation/blob/main/record/claims.d/CLAIM-475.md) · ARG-221 (Proposed)

    <text color="secondary" size="sm">SYNTHESIS / CASE / QUESTION</text> [SYNTHESIS-114](https://github.com/dmarx/nucleation/blob/main/record/syntheses.d/SYNTHESIS-114.md) · SYNTHESIS-118 · CASE-395 (proposed comparative study) · QUESTION-388

    **Open seam:** What independently observable result would show that a change in representational specification improved inquiry, rather than merely changed its categories?
  </box>
  <divider/>
  <box gap={2}>
    <row align="center" justify="between">
      <title size="lg">02. What Does a Research Record Keep?</title>
      <text color="secondary" size="xs">Source-rich</text>
    </row>
    **Microabstract.** Preserving the history of an inquiry can make its commitments, revisions, and dependencies inspectable, but history alone guarantees neither correctness nor sufficient information for future decisions. Using formal counterexamples and documented argumentative drift, this article identifies what a persistent record can secure, what it cannot, and when its maintenance costs are justified.

    **Sketched outline**

    1. **A transcript without an enduring argument.** Introduce documented drift, missed commitments, and the distinction between storing and addressing an intellectual object (CLAIM-177, CLAIM-182).
    2. **Traceability is not correctness.** Examine the perfectly accountable false theory and the sufficient posterior without its history (CASE-084, CASE-082).
    3. **When histories matter.** Compare identical support graphs with different evidential strengths, and identical current beliefs requiring different updates (CASE-089, CASE-093).
    4. **How much history is worth keeping?** Develop task-relative accountability and identify what an empirical memory-ablation study would actually measure (CLAIM-299, CASE-091).

    **Core fiber**

    <text color="secondary" size="sm">CLAIM</text> [CLAIM-177](https://github.com/dmarx/nucleation/blob/main/record/claims.d/CLAIM-177.md) · CLAIM-250 · [CLAIM-299](https://github.com/dmarx/nucleation/blob/main/record/claims.d/CLAIM-299.md) · CLAIM-293 · CLAIM-294

    <text color="secondary" size="sm">CASE</text> [CASE-082](https://github.com/dmarx/nucleation/blob/main/record/cases.d/CASE-082.md) · [CASE-084](https://github.com/dmarx/nucleation/blob/main/record/cases.d/CASE-084.md) · CASE-089 · CASE-093 · CASE-091

    <text color="secondary" size="sm">SYNTHESIS</text> [SYNTHESIS-017](https://github.com/dmarx/nucleation/blob/main/record/syntheses.d/SYNTHESIS-017.md) · SYNTHESIS-115

    **Open seam:** The value of keeping history needs to be evaluated relative to specified future tasks; no single amount of historical detail is optimal for every inquiry.
  </box>
  <divider/>
  <box gap={2}>
    <row align="center" justify="between">
      <title size="lg">03. From Obstruction to Reorganization</title>
      <badge>Working draft</badge>
    </row>
    **Microabstract.** An inquiry may expose failures in the representations used to maintain it and revise those representations in response. This case study examines Nucleation's development using Luria, including argumentative identity, schema changes, governance decisions, and the proposed feedback between the inquiry and the machinery used to maintain it.

    **Sketched outline**

    1. **The continuity problem.** Explain Luria's software-development origins and its transfer to a philosophical inquiry (ADR-032, ADR-043).
    2. **The record as apparatus.** Describe how typed objects, relations, and validators make distinctions operationally available (TERM-089, CLAIM-469).
    3. **When the schema misrepresents the inquiry.** Walk through the false dependency incident, its correction, and the broader history of grammar revisions (CASE-131, ARG-096, CASE-300).
    4. **What the demonstration establishes.** Compare recorded improvements and failures, governance roles, maintenance costs, and proposed controlled evaluations (CLAIM-419, ADR-127, CASE-252, CASE-253).

    **Core fiber**

    <text color="secondary" size="sm">TERM / CLAIM</text> [TERM-089](https://github.com/dmarx/nucleation/blob/main/record/terms.d/TERM-089.md) · CLAIM-181 · [CLAIM-419](https://github.com/dmarx/nucleation/blob/main/record/claims.d/CLAIM-419.md) · CLAIM-469

    <text color="secondary" size="sm">ARG / CASE</text> ARG-096 (Proposed) · [CASE-131](https://github.com/dmarx/nucleation/blob/main/record/cases.d/CASE-131.md) · CASE-178 · [CASE-300](https://github.com/dmarx/nucleation/blob/main/record/cases.d/CASE-300.md) · CASE-252 (proposed study) · CASE-253 (proposed study)

    <text color="secondary" size="sm">SYNTHESIS / ADR</text> SYNTHESIS-012 · ADR-032 · ADR-043 · ADR-127 · ADR-143

    **Open seam:** The observed development is not a controlled demonstration that Luria improves inquiry over alternatives. The manuscript's existing independent review and census should remain part of the evidence, including their identified limitations.

    <text size="sm">Existing manuscript: <Link url="https://github.com/dmarx/nucleation/tree/main/scratch/manuscripts/from-obstruction-to-reorganization" title="From Obstruction to Reorganization"/></text>
  </box>
</box>

## II. Structure, individuation, and learning

<box gap={4}>
  <box gap={2}>
    <title size="lg">04. What Makes an Organized Whole?</title>
    **Microabstract.** An organized individual need not be identified by immutable components or a structure preserved under every transformation. This article examines individuation, persistence, and maintained capacities, separating structural similarity from continuity of a particular organization.

    **Sketched outline**

    1. **Recognizing a whole.** Begin with systems such as a reef or dancing couple, where the boundary and relevant organization depend on the question (CASE-024, CASE-046, TERM-088).
    2. **What persists through replacement?** Examine causal transmission of organization rather than mere component identity or resemblance (CLAIM-329).
    3. **Persistence under constraints.** Relate individuation to realizability, observation, and action budgets (SYNTHESIS-040, SYNTHESIS-048).
    4. **Contested succession.** Ask how organizational continuity should be judged when maintainers, participants, or social recognition diverge (CLAIM-328, CASE-223, CASE-411).

    **Core fiber**

    <text color="secondary" size="sm">TERM</text> [TERM-088](https://github.com/dmarx/nucleation/blob/main/record/terms.d/TERM-088.md) · TERM-071 · TERM-074

    <text color="secondary" size="sm">CLAIM / ARG</text> [CLAIM-329](https://github.com/dmarx/nucleation/blob/main/record/claims.d/CLAIM-329.md) · CLAIM-328 · CLAIM-418 · ARG-216 (Proposed)

    <text color="secondary" size="sm">CASE / SYNTHESIS</text> CASE-024 · CASE-076 · [CASE-411](https://github.com/dmarx/nucleation/blob/main/record/cases.d/CASE-411.md) (Proposed coding study) · [SYNTHESIS-048](https://github.com/dmarx/nucleation/blob/main/record/syntheses.d/SYNTHESIS-048.md) · SYNTHESIS-040

    **Open seam:** Different persistence criteria may legitimately yield different answers. The article should not assume a unique, context-independent identity criterion.
  </box>
  <divider/>
  <box gap={2}>
    <title size="lg">05. The Cost Structure of Possibility</title>
    **Microabstract.** Earlier work can persist as constraints that change what later activity costs. This article studies how stabilized organization makes new capabilities feasible, why attainable configurations differ from reachable ones, and how the same accumulated structure can create both opportunity and lock-in.

    **Sketched outline**

    1. **Capability depends on cost.** Introduce stored work as a constraint that replaces expensive future operations with cheaper ones (CLAIM-761).
    2. **Holding is not reaching.** Use barrier constructions to distinguish the resources needed to maintain a configuration from those needed to attain it (CASE-233, ARG-077).
    3. **Paths matter.** Show why identical feasible endpoints can differ in cumulative cost or reliable attainment (ARG-078, SYNTHESIS-042).
    4. **When investment becomes productive.** Examine the target- and comparator-relative meaning of a productive nucleus and the risks of path dependence (TERM-117, SYNTHESIS-106).

    **Core fiber**

    <text color="secondary" size="sm">TERM / CLAIM</text> [TERM-117](https://github.com/dmarx/nucleation/blob/main/record/terms.d/TERM-117.md) · [CLAIM-761](https://github.com/dmarx/nucleation/blob/main/record/claims.d/CLAIM-761.md) · CLAIM-571

    <text color="secondary" size="sm">ARG / CASE</text> [ARG-077](https://github.com/dmarx/nucleation/blob/main/record/arguments.d/ARG-077.md) · ARG-078 (Proposed) · [CASE-233](https://github.com/dmarx/nucleation/blob/main/record/cases.d/CASE-233.md) · CASE-295 (Proposed)

    <text color="secondary" size="sm">SYNTHESIS</text> [SYNTHESIS-106](https://github.com/dmarx/nucleation/blob/main/record/syntheses.d/SYNTHESIS-106.md) · SYNTHESIS-042

    **Open seam:** A structure's persistence, usefulness, and productivity must remain distinct; the same constraint can be enabling under one target and obstructive under another.
  </box>
  <divider/>
  <box gap={2}>
    <title size="lg">06. How Training Finds Structure</title>
    **Microabstract.** Learned representations develop features, symmetries, and internal organizations through particular training dynamics. This article examines mechanisms of structural acquisition and distinguishes features that can be decoded from distinctions that become reusable and consequential for a learned system.

    **Sketched outline**

    1. **What is being acquired?** Distinguish superposed features, decodable information, and operational concepts (CASE-197, TERM-098).
    2. **The geometry of learning.** Examine high-dimensional separation, spectra, and parameter-coupled learning dynamics (SYNTHESIS-120, ARG-126).
    3. **Category changes under different budgets.** Use the nonnested optimal-partition result to challenge a simple refinement model of learning (CLAIM-387).
    4. **When structure becomes a capacity.** Survey the proposed checkpoint and intervention studies that would distinguish persistent, usable representations from incidental structure (CASE-272, CASE-274, SYNTHESIS-034).

    **Core fiber**

    <text color="secondary" size="sm">TERM / CLAIM</text> [TERM-098](https://github.com/dmarx/nucleation/blob/main/record/terms.d/TERM-098.md) (Proposed) · [CLAIM-387](https://github.com/dmarx/nucleation/blob/main/record/claims.d/CLAIM-387.md)

    <text color="secondary" size="sm">ARG / CASE</text> ARG-126 (Proposed) · ARG-137 (Proposed) · CASE-197 · CASE-272 (proposed study) · CASE-274 (proposed study) · CASE-301 (Proposed)

    <text color="secondary" size="sm">SYNTHESIS</text> [SYNTHESIS-025](https://github.com/dmarx/nucleation/blob/main/record/syntheses.d/SYNTHESIS-025.md) · [SYNTHESIS-120](https://github.com/dmarx/nucleation/blob/main/record/syntheses.d/SYNTHESIS-120.md) · SYNTHESIS-034

    **Open seam:** The conditions under which a learned distinction counts as a concept remain unresolved. The article should distinguish established results for particular models from general hypotheses about learning.
  </box>
  <divider/>
  <box gap={2}>
    <title size="lg">07. What Survives Translation?</title>
    **Microabstract.** A rendering can preserve propositional content while changing the communicative act. This article develops a task- and receiver-relative account of pragmatic fidelity, asking which communicative distinctions survive transformation between languages, contexts, and media.

    **Sketched outline**

    1. **The proposition is not the act.** Begin with utterances whose words or truth-conditional content remain similar while their pragmatic force changes (CLAIM-061, CASE-018).
    2. **Communicative identity.** Define communicative kinds as relational organizations of events, roles, norms, and anticipated uptake (TERM-040, SYNTHESIS-068).
    3. **Fidelity for which receiver?** Use comparison of experiments to distinguish information preserved by a rendering from distinctions available to a bounded receiver (CLAIM-050, ARG-019).
    4. **Contextuality and limits.** Separate ordinary context dependence from formal contextuality, locate the proposal against prior art, and specify what would count as a novel prediction (CLAIM-041, SYNTHESIS-070).

    **Core fiber**

    <text color="secondary" size="sm">TERM / CLAIM</text> [TERM-040](https://github.com/dmarx/nucleation/blob/main/record/terms.d/TERM-040.md) · [CLAIM-061](https://github.com/dmarx/nucleation/blob/main/record/claims.d/CLAIM-061.md) · CLAIM-038 · CLAIM-050 · CLAIM-023

    <text color="secondary" size="sm">ARG / CASE</text> ARG-019 (Proposed) · CASE-018 · CASE-005

    <text color="secondary" size="sm">SYNTHESIS</text> [SYNTHESIS-058](https://github.com/dmarx/nucleation/blob/main/record/syntheses.d/SYNTHESIS-058.md) · [SYNTHESIS-064](https://github.com/dmarx/nucleation/blob/main/record/syntheses.d/SYNTHESIS-064.md) · SYNTHESIS-068 · SYNTHESIS-070

    **Open seam:** A proposed measure of pragmatic fidelity requires declared receivers, tasks, and procedures. Similarity in a few examples does not establish procedure-level fidelity.
  </box>
</box>

## III. Agency, norms, and governance

<box gap={4}>
  <box gap={2}>
    <title size="lg">08. The Organization of Will</title>
    **Microabstract.** Practical agency need not depend on a sovereign executive faculty. This article examines how maintained relations among available regimes make some commitments effective rather than others, and why the capacity to govern those relations is distinct from simply possessing the commitments.

    **Sketched outline**

    1. **Having a regime is not enacting it.** Distinguish available action-generating capacities from those that become practically effective (TERM-023, CLAIM-047).
    2. **Who decides what counts?** Use Northstar's incident classifications to show how jurisdiction, precedence, and escalation authority affect action (CASE-002, CASE-003, ARG-001).
    3. **Governing the governor.** Examine the separation between rules governing ordinary conduct and authority over whether those rules apply (CLAIM-057, ARG-003).
    4. **Effectiveness is not authenticity.** Explain why an account of effective will doesn't establish whose will it is or whether its organization is normatively justified (CLAIM-022, SYNTHESIS-035).

    **Core fiber**

    <text color="secondary" size="sm">TERM / CLAIM</text> [TERM-023](https://github.com/dmarx/nucleation/blob/main/record/terms.d/TERM-023.md) · [CLAIM-027](https://github.com/dmarx/nucleation/blob/main/record/claims.d/CLAIM-027.md) · CLAIM-047 · CLAIM-057 · CLAIM-022

    <text color="secondary" size="sm">ARG / CASE</text> [ARG-001](https://github.com/dmarx/nucleation/blob/main/record/arguments.d/ARG-001.md) · ARG-003 · ARG-005 (Proposed) · CASE-003 · CASE-013

    <text color="secondary" size="sm">SYNTHESIS</text> [SYNTHESIS-035](https://github.com/dmarx/nucleation/blob/main/record/syntheses.d/SYNTHESIS-035.md) · SYNTHESIS-036 · SYNTHESIS-041

    **Open seam:** Effective coordination is not by itself evidence of ownership, authenticity, autonomy, or moral legitimacy.
  </box>
  <divider/>
  <box gap={2}>
    <title size="lg">09. The Organization of Perspective</title>
    **Microabstract.** A perspective is a historically maintained organization through which information becomes salient, interpretable, evaluable, and consequential. This article distinguishes a perspective from the people carrying it, the agents acting through it, and the institutions that make it effective.

    **Sketched outline**

    1. **A perspective is not its carrier.** Distinguish organization, agent, perspective, and institution (CLAIM-418).
    2. **Perspective and action.** Examine cases where matching ordinary behavior conceals different responses to interventions (ARG-025).
    3. **History without a permanent subject.** Use memory and political continuity cases to ask how perspectives persist despite changes to their carriers (CASE-137, CASE-133, CLAIM-329).
    4. **Reflexivity across a population.** Investigate how shared interpretive structures can be reproduced or collectively contested without assuming one sovereign agent controls them (CLAIM-424, TERM-121).

    **Core fiber**

    <text color="secondary" size="sm">TERM / CLAIM</text> TERM-071 · [TERM-121](https://github.com/dmarx/nucleation/blob/main/record/terms.d/TERM-121.md) (Proposed) · [CLAIM-418](https://github.com/dmarx/nucleation/blob/main/record/claims.d/CLAIM-418.md) · CLAIM-329 · CLAIM-424

    <text color="secondary" size="sm">ARG / CASE</text> [ARG-025](https://github.com/dmarx/nucleation/blob/main/record/arguments.d/ARG-025.md) (Proposed) · CASE-137 · CASE-133 · CASE-138

    <text color="secondary" size="sm">SYNTHESIS</text> [SYNTHESIS-122](https://github.com/dmarx/nucleation/blob/main/record/syntheses.d/SYNTHESIS-122.md) (broad, Proposed)

    **Open seam:** A perspective may persist without an independently individuated agent. The article must resist treating continuity of interpretation as proof of continuity of agency.
  </box>
  <divider/>
  <box gap={2}>
    <title size="lg">10. How an Organization Can Know and Fail to Correct</title>
    **Microabstract.** An organization can possess accurate information about a problem without giving that information influence over decisions. This article separates admission, recognition, credibility, uptake, authority, and practical correctability, showing how failures at different stages require different interventions.

    **Sketched outline**

    1. **Two true classifications, different consequences.** Begin with the complaint routed through different taxonomies (CASE-132, TERM-064).
    2. **The stages of correction.** Distinguish recognizing a problem, making it consequential for decisions, and carrying out a suitable response (CLAIM-523).
    3. **Why organizations reproduce their errors.** Examine the Challenger–Columbia record and the consequences of interpretive capture or repeated filtering of objections (CASE-138, SYNTHESIS-111).
    4. **Correcting the correction process.** Ask how an organization can change the standards and authority relationships that determine which objections count (CLAIM-424, SYNTHESIS-121).

    **Core fiber**

    <text color="secondary" size="sm">TERM / CLAIM</text> [TERM-064](https://github.com/dmarx/nucleation/blob/main/record/terms.d/TERM-064.md) · [CLAIM-523](https://github.com/dmarx/nucleation/blob/main/record/claims.d/CLAIM-523.md) · CLAIM-535 · CLAIM-403 · CLAIM-466

    <text color="secondary" size="sm">ARG / CASE</text> ARG-062 (Proposed) · [CASE-132](https://github.com/dmarx/nucleation/blob/main/record/cases.d/CASE-132.md) · CASE-138

    <text color="secondary" size="sm">SYNTHESIS</text> [SYNTHESIS-111](https://github.com/dmarx/nucleation/blob/main/record/syntheses.d/SYNTHESIS-111.md) · SYNTHESIS-121

    **Open seam:** An organization can acquire new channels of correction without developing justified standards for using them. Institutional responsiveness and epistemic correctness remain separate.
  </box>
  <divider/>
  <box gap={2}>
    <title size="lg">11. Can an Organization's Viability Ground a Norm?</title>
    **Microabstract.** A self-maintaining organization can continue functioning while doing harm or preserving an unjust arrangement. This article distinguishes functional success from moral justification and asks what must be specified before an organization's behavior can be judged good, defective, or wrongful.

    **Sketched outline**

    1. **Viability isn't justification.** Introduce the failure of the inference from persistence or self-maintenance to what ought to persist (CLAIM-075).
    2. **Fix the relata.** Explain why a normative judgment must identify the object, standards, circumstances, and relevant comparators (CLAIM-363, TERM-074).
    3. **The wrong beyond the outcome.** Contrast equal harms arising under different institutional arrangements of review and correction (CASE-229, ARG-055).
    4. **Second-order answerability.** Examine the proposed duty to maintain means of recognizing and correcting violations when independently justified standards and feasible alternatives are present (CLAIM-624, SYNTHESIS-094).

    **Core fiber**

    <text color="secondary" size="sm">TERM / CLAIM</text> [TERM-074](https://github.com/dmarx/nucleation/blob/main/record/terms.d/TERM-074.md) · [CLAIM-075](https://github.com/dmarx/nucleation/blob/main/record/claims.d/CLAIM-075.md) · CLAIM-363 · CLAIM-624 (Proposed)

    <text color="secondary" size="sm">ARG / CASE</text> ARG-043 (Proposed) · ARG-055 (Proposed) · CASE-229 (Proposed) · CASE-241 (Proposed)

    <text color="secondary" size="sm">SYNTHESIS</text> [SYNTHESIS-091](https://github.com/dmarx/nucleation/blob/main/record/syntheses.d/SYNTHESIS-091.md) · SYNTHESIS-094

    **Open seam:** No fact about an organization's effective operation alone establishes its moral worth or the legitimacy of preserving its existing structure.
  </box>
  <divider/>
  <box gap={2}>
    <title size="lg">12. Dependence, Domination, and the Terms of Participation</title>
    **Microabstract.** Dependence alone does not establish domination or exploitation. This article investigates how the control of terms, alternatives, access, and contestability affects the relationship between organized wholes and their participants, with judgments indexed to explicit normative standards.

    **Sketched outline**

    1. **Who depends on whom?** Separate the magnitude of dependence from who exercises control over its terms (CLAIM-690).
    2. **Same dependence, different authority.** Use matched workshop arrangements to show how control over conditions changes the character of the relation (CASE-264, ARG-110).
    3. **Exploitation through access.** Examine arrangements that create or intensify dependence while appearing to provide valuable opportunities (CLAIM-669, CLAIM-670).
    4. **Answerability and alternatives.** Investigate what obligations arise where one party controls indispensable conditions of participation (TERM-123, SYNTHESIS-103).

    **Core fiber**

    <text color="secondary" size="sm">TERM / CLAIM</text> [TERM-123](https://github.com/dmarx/nucleation/blob/main/record/terms.d/TERM-123.md) (Proposed) · CLAIM-669 · CLAIM-670 · CLAIM-690

    <text color="secondary" size="sm">ARG / CASE</text> [ARG-110](https://github.com/dmarx/nucleation/blob/main/record/arguments.d/ARG-110.md) (Proposed) · [CASE-264](https://github.com/dmarx/nucleation/blob/main/record/cases.d/CASE-264.md) (Proposed) · CASE-261 (Proposed)

    <text color="secondary" size="sm">SYNTHESIS</text> [SYNTHESIS-092](https://github.com/dmarx/nucleation/blob/main/record/syntheses.d/SYNTHESIS-092.md) · SYNTHESIS-103

    **Open seam:** Distinctions among dependence, domination, and exploitation require more than measuring the amount of dependence. Normative verdicts need independently stated standards.
  </box>
  <divider/>
  <box gap={2}>
    <title size="lg">13. Capability, Restraint, and Relational Freedom</title>
    **Microabstract.** Whether a capability should be restricted is distinct from who may legitimately restrict it. This article considers the authority to constrain action among interdependent agents, including proportionality, answerability, available remedies, and restrictions that undermine a party's future ability to contest them.

    **Sketched outline**

    1. **A capability and the authority to restrict it.** Establish why judging an intervention necessary does not establish that a particular actor may impose it (SYNTHESIS-100).
    2. **Power over the conditions of challenge.** Examine control over forums, timing, costs, and access to remedies (CLAIM-727).
    3. **Responsibility without simple blame assignment.** Use institutional investigation and accountability examples to distinguish tracing causes from assigning fault (CASE-292, ARG-118).
    4. **Testing reasonable restrictions.** Compare arrangements that hold outcomes similar while varying rights of contestation or control over review (CASE-336, ARG-203).

    **Core fiber**

    <text color="secondary" size="sm">TERM / CLAIM</text> [TERM-126](https://github.com/dmarx/nucleation/blob/main/record/terms.d/TERM-126.md) (Proposed) · [CLAIM-727](https://github.com/dmarx/nucleation/blob/main/record/claims.d/CLAIM-727.md) · CLAIM-703 · CLAIM-723 (Proposed)

    <text color="secondary" size="sm">ARG / CASE</text> ARG-118 (Proposed) · ARG-203 (Proposed) · CASE-286 (Proposed) · [CASE-292](https://github.com/dmarx/nucleation/blob/main/record/cases.d/CASE-292.md) (Proposed) · CASE-336 (Proposed)

    <text color="secondary" size="sm">SYNTHESIS</text> [SYNTHESIS-100](https://github.com/dmarx/nucleation/blob/main/record/syntheses.d/SYNTHESIS-100.md) · SYNTHESIS-103

    **Open seam:** The argument must keep the justification of a restriction separate from the legitimacy of its enforcer, including who may revise that restriction and under what procedures.
  </box>
  <divider/>
  <box gap={2}>
    <row align="center" justify="between">
      <title size="lg">14. Regulation as the Governance of Possibility</title>
      <badge>Working draft</badge>
    </row>
    **Microabstract.** Regulation shapes not only present conduct but the future configurations an ecosystem can attain, sustain, and revise. This article develops identity stabilization, temporal filtering, and adaptive readiness, using matched-performance constructions to expose differences between current output and the capacity to reorganize.

    **Sketched outline**

    1. **Present performance isn't the whole target.** Distinguish operating successfully in an existing regime from retaining the capacity to change that regime (CLAIM-099).
    2. **Temporal organization.** Explore the different costs of forming, maintaining, and reaching configurations, including transition barriers (SYNTHESIS-112, CASE-233).
    3. **Readiness under different budget regimes.** Present the executed matched-performance model without treating stipulated outcomes as independent discoveries (CASE-412).
    4. **Lock-in and corrective governance.** Examine disuse, resource withdrawal, and mechanisms for keeping reorganization possible (CASE-315, SYNTHESIS-124).

    **Core fiber**

    <text color="secondary" size="sm">TERM / CLAIM</text> [TERM-115](https://github.com/dmarx/nucleation/blob/main/record/terms.d/TERM-115.md) · CLAIM-099 · CLAIM-577 · CLAIM-582

    <text color="secondary" size="sm">ARG / CASE</text> ARG-077 · [CASE-233](https://github.com/dmarx/nucleation/blob/main/record/cases.d/CASE-233.md) · CASE-315 (Proposed) · [CASE-412](https://github.com/dmarx/nucleation/blob/main/record/cases.d/CASE-412.md) (Proposed executed model)

    <text color="secondary" size="sm">SYNTHESIS</text> [SYNTHESIS-112](https://github.com/dmarx/nucleation/blob/main/record/syntheses.d/SYNTHESIS-112.md) · SYNTHESIS-124

    **Open seam:** The manuscript still needs an industrial case tied to its substantive setting. The model illustrates stipulated mechanisms; it does not establish empirical effectiveness in industrial ecosystems.

    <text size="sm">Existing manuscript: <Link url="https://github.com/dmarx/nucleation/tree/main/scratch/manuscripts/governance-of-possibility" title="Regulation as the Governance of Possibility"/></text>
  </box>
</box>

## IV. Publishing the atlas

<box gap={2}>
  <title size="lg">15. Just Show Your Work: Publishing Research as a Governed Atlas</title>
  <text color="secondary" size="xs">New proposal · Most important record gap</text>

  **Microabstract.** Scholarly publishing treats a manuscript as the unit of communication, attribution, preservation, editorial assessment, and evaluation. This article proposes separating these functions: research would persist as governed, addressable objects; hyperarticles would provide audience-relative views; editors would contribute independent assessments; and journals would organize those assessments into feeds. Nucleation supplies a reference implementation of the governed research substrate, not yet of the complete publishing network.

  **Sketched outline**

  1. **The paper is a presentation, not the inquiry.** Develop the distinction between an evolving body of research and the narratives selected to communicate it (CLAIM-178, CLAIM-324).
  2. **A research record with addressable commitments.** Explain which identities, relationships, and standings can be maintained and where record governance stops short of deciding epistemic correctness (CLAIM-299, CLAIM-469, CASE-084).
  3. **Hyperarticles as views.** Propose a versioned publication object declaring its source dependencies, audience, scope, and maintenance obligations. Identify the additional scholarly identifier and preservation requirements not yet implemented (ADR-143 as procedural precedent).
  4. **Editorial feeds and institutional judgment.** Propose independently attributable assessments and journals as views over editors; apply the distinctions between legibility, authority, and correction to editorial governance (CLAIM-523, TERM-064).

  **Core fiber already present in Nucleation**

  <text color="secondary" size="sm">TERM / CLAIM</text> [TERM-064](https://github.com/dmarx/nucleation/blob/main/record/terms.d/TERM-064.md) · [CLAIM-178](https://github.com/dmarx/nucleation/blob/main/record/claims.d/CLAIM-178.md) (Proposed) · CLAIM-324 · CLAIM-299 · CLAIM-469 · CLAIM-523

  <text color="secondary" size="sm">CASE / SYNTHESIS</text> CASE-084 · CASE-131 · [SYNTHESIS-017](https://github.com/dmarx/nucleation/blob/main/record/syntheses.d/SYNTHESIS-017.md) (Proposed) · SYNTHESIS-012 (Proposed)

  <text color="secondary" size="sm">ADR</text> [ADR-143](https://github.com/dmarx/nucleation/blob/main/record/decisions.d/ADR-143.md) (Proposed manuscript protocol) · ADR-104 (work membership)

  **Missing from the fiber:** An explicit publication-specific TERM for *hyperarticle*, a CLAIM defining the source/view contract, ARGs supporting the editorial separation, and CASEs or studies testing whether the proposed architecture improves scholarly communication. The journal-as-feed and feed-with-memory ideas remain proposals developed in this conversation rather than established Nucleation arguments.

  **Open seam:** The reference implementation of a governed research record does not establish the advantages of a distributed publishing network. That transition needs its own warrants and defeaters.
</box>

---

## V. The connective tissue: shared fibers

These shared source objects are especially interesting because they connect articles without requiring the articles to make identical claims.

| Shared record or distinction | Articles | Function of the overlap |
|---|---|---|
| [CLAIM-470](https://github.com/dmarx/nucleation/blob/main/record/claims.d/CLAIM-470.md): inquiry as specification | 01, 03 | Theory to operational case |
| [CLAIM-475](https://github.com/dmarx/nucleation/blob/main/record/claims.d/CLAIM-475.md): resource-bounded specification | 01, 05 | Inquiry to stored work |
| [CASE-084](https://github.com/dmarx/nucleation/blob/main/record/cases.d/CASE-084.md): accountable false theory | 02, 15 | Limit on provenance-based publishing claims |
| [TERM-088](https://github.com/dmarx/nucleation/blob/main/record/terms.d/TERM-088.md): individuation | 04, 09 | Identity across transformations |
| [CLAIM-329](https://github.com/dmarx/nucleation/blob/main/record/claims.d/CLAIM-329.md): historical organizational persistence | 04, 09 | Continuity of organization versus carriers |
| [CLAIM-387](https://github.com/dmarx/nucleation/blob/main/record/claims.d/CLAIM-387.md): nonnested optimal partitions | 01, 06 | Refinement versus reorganization of distinctions |
| [CLAIM-523](https://github.com/dmarx/nucleation/blob/main/record/claims.d/CLAIM-523.md): legibility, efficacy, correctability | 10, 13, 15 | Institutional action, legitimacy, and editorial governance |
| [CLAIM-178](https://github.com/dmarx/nucleation/blob/main/record/claims.d/CLAIM-178.md): manuscript as view | 02, 03, 15 | Maintained research to publication architecture |

A future atlas implementation could distinguish the nature of each of these connections: shared source object, formal dependency, interpretive application, proposed analogy, or contested transition.

For now, the table records where such relationships need to be examined, not a proof that all the corresponding charts are compatible.

## VI. What still needs coverage in this version

I wouldn't yet promote the outlines into 15 governed manuscript works. Three kinds of work remain.

**1. Source closure.** Each core fiber is a verified starting set. The next audit should traverse the record's declared relations to find missing premises, relevant objections, superseded dependencies, and literature that the short outline currently omits.

**2. Narrative joins.** Some outlines introduce transitions that may be useful for exposition but are not yet claimed by Nucleation. Those should be checked against existing SYNTHESIS accounts, then filed appropriately where they add a genuinely new argument.

**3. View evaluation.** Good source coverage doesn't automatically produce a good article. Each view needs a defined audience, an account of what it excludes, and independent review of the finished narrative against the record.

The most important outcome of v0.3 is that we can now ask two different questions of every candidate:

*Does Nucleation contain the intellectual objects needed to make this argument?*

And:

*Can those objects be assembled into a coherent view without silently changing their standing or introducing unsupported inferences?*

That gives us a concrete way to assess atlas coverage and decide which hyperarticles are ready for composition, which need better curation, and which require further research.

<caption>Source basis: [Nucleation commit 23b9dff](https://github.com/dmarx/nucleation/tree/23b9dff3637330df0488ecb6fc32e479ec13e32b). This is an editorial proposal; no Nucleation records were changed.</caption>

---

If you want, I can:

- Add source-backed outlines for remaining articles
- Propose new argumentative joins for open seams
- Draft accountability annotations per section
