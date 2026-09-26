---
number: 136
status: Read
formerly:
- NOTE-tmpixkib
paper: LIT-195
title: 'Safron et al. — World models and life–mind continuity'
version: 2
history:
- version: 2
  date: '2026-09-26'
  note: >-
    Read in full (The full published text: the open-access (CC BY) HTML
    version of record of the introductory editorial, Phil. Trans. R. Soc. A
    384(2320), 20240533. It was read from the Wayback capture that seeding
    saved to rawP3/p053w.html, copied to rawA/safron_wayback.html and
    extracted to rawA/safron.txt. The dossier dates the capture 2026-05-19;
    that date was not re-verified. The read covers the author block with
    CRediT roles, the abstract and keywords, §1, all 17 contribution
    summaries in §2(a)–(c) with the editors' commentary, §3, the back matter
    (data, AI-use declaration, contributions, conflict of interest, funding,
    acknowledgements) and all 57 references. Nothing was skipped. The HTML
    has no page numbers, so locations are sections. Fresh retrieval failed
    on 2026-09-26: royalsocietypublishing.org returned 403 to the DOI,
    article and PDF URLs, with both curl and browser user agents; PMC idconv
    says "Identifier not found in PMC"; Europe PMC returned 0 hits for the
    DOI and the title; Unpaywall lists only the publisher OA location and no
    repository copy; the author's page (adamsafron.com/world-models) links
    only to the publisher; and live Wayback requests were reset by the
    proxy.). Upgraded from `Skimmed` to `Read`: the claims table,
    assumptions and results are new, and the skim is corrected where the
    full text disagreed.
date: '2026-09-26'
summary: >-
  The editorial introduces a theme issue of 17 papers. It concludes that
  the issue "overall appears to converge" on one view: LLMs model the
  world in some senses but "probably" lack coherent causal world models,
  and are not likely paths to "artificial general superintelligence" (§1).
  It separates three senses of "world model": any information about the
  world a system cognizes over, which LLMs "clearly" have; representation
  of causal structure, "less certain"; and causal prediction "in the
  service of agentic functioning", where the divergence "may become even
  greater" (§3). It closes that world models are "context-dependent
  constructions shaped by embodiment, dynamics, goals and social
  learning".
---
<!-- inactive-ok-file: LIT-133 — Rejected on its 2026-09-26 close reading: cited as a related framing, not as a result -->
<!-- inactive-ok-file: NOTE-169 — Skimmed: another reading of a related work, cited for what its skim records; lapses when that paper is read in full -->
<!-- inactive-ok-file: NOTE-123 — Skimmed: another reading of a related work, cited for what its skim records; lapses when that paper is read in full -->
<!-- inactive-ok-file: LIT-131 — Deferred: a related work named by a 2026-09-26 close reading on the agency tag; lapses when the cited work is read -->
<!-- inactive-ok-file: LIT-135 — Deferred: a related work named by a 2026-09-26 close reading on the agency tag; lapses when the cited work is read -->

# NOTE-136: Safron et al. — World models and life–mind continuity

## Contribution

The editorial gathers the issue's 17 papers into one thesis. Present foundation models capture some of what "world model" can mean, but not the causal, agent-serving, embodied and value-laden world modelling that the editors take to characterise biological intelligence. It separates three senses of the term (§3). It also sets an agenda that ties world modelling to consciousness and to the definition of life, through "capacities for minimal agency that depend on—and also contribute to the learning of—predictive self-world modelling" (§1). It makes no argument or result of its own. The evidence sits in the contributions it summarises.

## Key insight

"Does an LLM have a world model?" has no single answer because "world model" names at least three things:
- information about the world that the system cognizes over;
- a representation of the world's causal structure;
- causal prediction used to control action toward goals.

On the editors' reading, LLMs clearly have the first, arguably have the second, and are furthest from biological systems on the third (§3). The editorial's recurring move is to tie the third sense to agency: agents learn better world models because they intervene (Yiu et al.; Amir et al.), and world models matter because they serve an agent's goals (Alicea et al.).

## Assumptions

(Premises and authorities, since this is an editorial.)

- **World models serve agency, and biological agents are the benchmark.** Life is framed as "value-driven, self-making agentic systems" (§1). Autopoiesis, holistic integration and active learning are treated as marks that current AI lacks (commentary on Rouleau & Levin, §2(c)(i); on Yiu et al., §2(b)(ii)).
- **LLMs model word transitions, not the processes words refer to** (§3). This is stated as a premise, not argued, and it drives the three-sense analysis.
- **Consciousness may be integrated world modelling.** The editors repeatedly cite Safron's own IWMT (refs 17, 18, 20, 47) as a possible functional account (§2(b)(viii) commentary; §2(c)(i) commentary). The first author's theory is thus part of the lens.
- **The summaries are interpretations.** The editors warn that their readings "should not be taken to be definitive statements and may diverge from the views of contributing authors" (§1).

## Key results

(What it argues and reports.)

- **The three senses of "world model"** (§3), each anchored to one citation:
  - information over which a system cognizes: LLMs "clearly reach this standard" (ref. 57, Gurnee & Tegmark);
  - representation of underlying causal structure: "less certain" (ref. 44, Pearl & Mackenzie);
  - capacities "to predict causal transitions in the service of agentic functioning": the divergence "may become even greater" (ref. 2, Ha & Schmidhuber).
- **Convergence verdict** (end of §1). The collection "overall appears to converge towards concluding" three things about LLMs. They "probably" model the world "without generating sufficiently coherent causal world models to attain human-like cognitive abilities". They lack "consciousness". And they are not "likely pathways to artificial general superintelligence".
- **World modelling and agency are "fundamentally entangled"** (commentary on Amir et al., §2(b)(iii)). World models help agents achieve goals, and agency supplies the context in which coherent models are learnt. The editors link this to the frame problem and to affordances.
- **Safety-relevant glosses:**
  - From Sacco et al.'s result that strictly autoregressive models cannot keep long-range order, the editors infer that recursively self-improving superintelligence "may not be one of the problems" posed by such systems (§2(b)(vii)).
  - From Battleday & Gershman, they infer "less reason to fear" autonomous AI science creating existential risk (§2(c)(iv)).
- **Pluralist close** (§3). "World models are not neutral abstractions but context-dependent constructions shaped by embodiment, dynamics, goals and social learning". The task is to "refine the questions" rather than answer them.
- **Reported contribution findings**, as the editors summarise them and not re-checked here:
  - Leivada et al.: ChatGPT-4o's leetspeak decoding "drops sharply" as substitutions increase, while humans stay near ceiling.
  - Tsividis et al.: EMPA matches human learning efficiency on a majority of games and beats deep-RL baselines "by orders of magnitude" in sample efficiency.
  - Zhu, Huang & Russell: transition and reward functions have lower circuit complexity than value functions.
  - Premakumar et al.: self-modelling auxiliary objectives reduce network complexity without hurting accuracy.
  - Collins et al.: an "AI Rogers paradox", in which adding a free AI social learner does not raise collective world understanding.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | "World model" has at least three senses: information cognized over; causal structure; causal prediction for agency. | informal argument (conceptual) | §3, each sense anchored to one citation (refs 57, 44, 2) |
| C2 | LLMs clearly meet the first sense, are uncertain on the second, and diverge most from biological systems on the third. | assertion | §3; relies on the premise that LLMs model word transitions only |
| C3 | The issue's contributions converge on LLMs "probably" lacking coherent causal world models, consciousness and a likely path to superintelligence. | editorial synthesis | end of §1; the editors themselves caveat the diversity of views and that their readings may diverge from the authors' |
| C4 | World modelling and agency are fundamentally entangled. | informal argument | commentary on Yiu et al., Amir et al. and Alicea et al., §2(b)(ii)–(iii), (vi) |
| C5 | Recursively self-improving superintelligence may not be among the problems posed by autoregressive systems. | weak: an editorial inference from one contribution | commentary on Sacco et al., §2(b)(vii) |
| C6 | Near-future AI gives "less reason to fear" existential risk from autonomous science. | weak: an editorial inference | commentary on Battleday & Gershman, §2(c)(iv) |
| C7 | Life might be defined by capacities for minimal agency that depend on, and contribute to, predictive self-world modelling. | posed as a question | §1 |
| C8 | Hofstadter's claim: passing a consistent-understanding Turing test suffices to attribute thinking, and conscious AI may come "perhaps even by 2033". | reported (Hofstadter's own view, quoted) | §1 epigraph and quotation; §2(a)(i) |

## Concepts

- **World model.** No single definition is adopted (abstract). The working gloss is to "usefully represent in compressed form" the world in which an agent acts and pursues goals (§1).
- **Suitcase word.** Minsky's term (ref. 22), used for the risk that "world model", like "consciousness", becomes semantically vacuous (§1).
- **Minimal agency.** Used in §1 for the agency that might define life. It is not defined.
- **Empowerment.** Mutual information between interventions and resulting states, as an intrinsic epistemic reward (from Yiu et al., §2(b)(ii)).
- **Telic state.** An equivalence class of experience distributions that are equally preferred under a goal (from Amir et al., §2(b)(iii)).
- **Cognitive glue.** A shared model that binds agents into a collective intelligence; for Lyons & Levin, the price system (§2(c)(ii)).
- **"Less is more" vs. "more is more".** Emergent intelligence as compact, generalisable abstraction, versus capability from scale. Taken from Krakauer, Krakauer & Mitchell and applied to OthelloGPT's "bag of heuristics" (§2(a)(ii)).

## Connections

The editorial is by the issue's 14 guest editors. Several have only a "conceptualization" CRediT role: Razi, Ha, Rish and Mitchell. The first author's integrated world modeling theory frames the discussion of consciousness. Its life–mind-continuity framing is shared with *What Lives?* ([LIT-211](../literature.d/LIT-211.md)). That note already records that Levin co-authored both, and the definitions of life there are agency-based. The appeal to autopoiesis as what AI lacks links to *Welfare Subjects and Autopoiesis* ([LIT-120](../literature.d/LIT-120.md)) and *Conscious artificial intelligence and biological naturalism* ([LIT-135](../literature.d/LIT-135.md)).

On whether LLMs understand, the three senses sit between *A Model of Understanding in Deep Learning Systems* ([LIT-131](../literature.d/LIT-131.md)) and *Talkative AI and the fiction of artificial minds* ([LIT-207](../literature.d/LIT-207.md)). [LIT-131](../literature.d/LIT-131.md) and its reading [NOTE-123](NOTE-123.md) cite this work for "the three-tier 'world model' criterion". That is a fair pointer, with the caveat above that the three senses are posed conditionally, not proposed as a criterion. The good-regulator contribution (Alicea et al.) is the cybernetic route to agency. It connects to *Towards a Generalized Theory of Observers* ([LIT-133](../literature.d/LIT-133.md)), whose minimal observer is a regulator loop without the good-regulator condition.

**Account of agency.** The editorial presupposes and does not argue an account. On that account:
- agency is goal-directed control guided by a predictive model of how actions change the world (§1: "Predictive models that reflect the ways the … structure of the world may be causally modified by actions allow agents to adaptively control their behaviour");
- it is intrinsically motivated, through curiosity and empowerment;
- it is value-driven and, in living systems, self-making;
- world modelling and agency constitute each other: agency shapes what is modelled and models serve agency.

This is closer to active-inference and enactivist views than to a thin cybernetic one. Its criterion for world modelling "in the service of agentic functioning" is where it locates the biggest gap between current AI and organisms.

**Agency tag: justified.** "agency" is one of the article's own keywords. The abstract names "robust agency" as a target. The editorial's main conceptual claim, that world modelling and agency are entangled, and its question about defining life by minimal agency are both about what it is to be an agent across organisms, collectives (price systems, human–AI populations) and machines. The tag order (cognition, consciousness, agency) is defensible. Agency could fairly be second.

## Bearing on the record

- **For ML practice: nothing directly.** The editorial carries no instruction a practitioner could act on. Some of the contributions it summarises may have ML-practice content, and the anthology would want those if a transfer were ever considered, not this editorial:
  - Zhu, Huang & Russell on the representation complexity of model-based vs. model-free RL;
  - Premakumar et al. on self-modelling as a regulariser;
  - Tsividis et al.'s EMPA sample-efficiency comparison;
  - Sacco et al.'s claim about autoregressive coherence limits.

  None of these is in the anthology's literature, checked by grep for Ha & Schmidhuber, Dreamer and Gurnee & Tegmark.
- **Record hygiene.** [LIT-131](../literature.d/LIT-131.md), [LIT-135](../literature.d/LIT-135.md), [LIT-211](../literature.d/LIT-211.md), [NOTE-123](NOTE-123.md) and [NOTE-169](NOTE-169.md) carry `inactive-ok-file` directives for [LIT-195](../literature.d/LIT-195.md) as Deferred. [NOTE-109](NOTE-109.md) also cites it in prose. Once it is Active, those directives lapse, as they say they will. The next `luria lint` should confirm.
- **Candidate follow-ups for nucleation**, if the record wants the claims and not the map: Hofstadter's "Is there an 'I' in AI"; Krakauer, Krakauer & Mitchell; Amir, Tiomkin & Langdon on telic states, which is agency-relevant; Rouleau & Levin.
- The record has no THEORY documents for it to support or contradict.

## Limitations

- It is an editorial. Every substantive claim is a gloss on a contribution, and the editors say their readings may diverge from the authors'.
- **The accepted-in-three-days review history (received 9 Jan, accepted 12 Jan 2026) is normal for an editorial,** and it means the synthesis was not independently refereed as an argument.
- **The strongest safety-relevant sentences are single-source inferences.** "Recursively self-improving superintelligences may not be one of the problems…" rests on one topology paper. Sacco et al. concern autoregressive coherence, and whether that bears on self-improvement is not argued.
- **The premise that LLMs model only word transitions is asserted,** while the first-sense citation (Gurnee & Tegmark) is evidence for internal world representations.
- **The convergence verdict weights the collection one way.** Hofstadter, the lead essay, argues nearly the opposite. The editors note the diversity of views but still report a convergence.

## Open questions

- Which experiment separates the second sense (causal structure) from the first (world information) in an LLM? The editorial leaves the second sense "less certain" and names no test.
- Can "minimal agency" be given a definition that makes the life-defining question in §1 answerable? The editorial poses it and does not define the term.
- Does Sacco et al.'s topological limit bear on agentic or tool-using LLM systems whose effective interaction graph is not one-dimensional? The editors' reassurance depends on the answer.

## Corrections to the seeded skim

- The dossier miscounts the contributions in §2. It lists three papers under (a), five topics under (b) and four items under (c). The editorial summarises 17 contributions: four in (a), eight in (b) and five in (c). The dossier omits:
  - Leivada, Marcus, Günther & Murphy, the "leetspeak" decoding experiment on ChatGPT-4o, in (a)(iv);
  - Tsividis et al., the EMPA theory-based RL agent, in (b)(i);
  - Amir, Tiomkin & Langdon, "telic states" and goals as preference relations over experience distributions, in (b)(iii);
  - Sacco, Sakthivadivel & Levin, topological constraints showing that autoregressive (effectively 1-D) models cannot keep long-range order, in (b)(vii);
  - Rouleau & Levin, on substrate-neutral restatements of theories of consciousness, in (c)(i).

  This matches the back matter: "One contribution of 18", meaning 17 papers plus the editorial.
- "Clearly meet only the first" overstates the text. On the second sense, causal structure, the editors say LLMs' capacities "become less certain". That leaves the second sense open, where the dossier's wording implies LLMs fail it. The editors also do not propose the three senses as a criterion of their own. They are three conditional readings ("If we think of…", "if our defining criteria require…", "Even more, if…"), each tied to a citation: Gurnee & Tegmark for the first, Pearl & Mackenzie for the second, Ha & Schmidhuber for the third.
- The dossier describes the editorial as neutral, which misses its verdicts. The editorial issues conclusions of its own that go beyond framing:
  - a convergence verdict against LLMs as paths to AGI (end of §1);
  - the inference that "recursively self-improving superintelligences may not be one of the problems that we have to face from such systems" (commentary on Sacco et al., §2(b)(vii));
  - the view that we "may have less reason to fear" near-future AI doing science autonomously in ways that create existential risk (commentary on Battleday & Gershman, §2(c)(iv)).
- "Krakauer et al." is Krakauer, Krakauer & Mitchell: David Krakauer, John Krakauer and Melanie Mitchell (§2(a)(ii)).
- The dossier's access note undersells the capture. It says the seeder read only "the subsection titles of §2 … and its opening Hofstadter summary". The saved capture contains every §2 summary and commentary in full.
