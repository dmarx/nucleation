---
number: 723
status: Read
formerly:
- NOTE-tmp0foxv
paper: LIT-1033
title: 'Kahl — How continuity distinguishes autonomy from agency in agentic AI'
version: 1
history:
- version: 1
  date: '2026-10-13'
  note: >-
    Read in full from the publisher's open-access PDF (Springer Nature,
    Discover Artificial Intelligence 6:1187, 29 pp., CC BY-NC-ND 4.0),
    link.springer.com/content/pdf/10.1007/s44163-026-01675-5.pdf. A
    Perspective article: received 10 February 2026, accepted 17 June 2026.
    Text extracted with pdftotext; the extraction is clean apart from
    zero-width characters in URLs and Table 1, whose columns come out of
    order and were reassembled by eye. Read: all nine sections, Table 1
    and the reference list. Nothing skipped. The "continuity-based
    account" the abstract draws on is not cited to any earlier work; the
    paper develops it "in compressed form" here. Every quotation below
    was checked against the extracted text by script, with whitespace and
    line-end hyphenation normalised. The one quotation from the record,
    QUESTION-092's "the scheduler's location beside the point", was
    checked against that entry.
date: '2026-10-13'
summary: >-
  Agency in the sense that bears on responsibility, authority and
  governance needs a persisting locus of evaluative authority under
  continuity pressure: when the inherited evaluative frame no longer
  settles what should count as success, the system itself settles a
  revised frame and carries it forward. Planning, tool use, memory,
  coordination and operational autonomy do not supply this. Tool-using
  agents, reinforcement learners, multi-agent workflows and institutional
  decision systems ordinarily fail it, because failure is corrected from
  outside. A conceptual necessary condition, applied to cases; not a
  sufficient theory and not measured.
---
<!-- inactive-ok-file: CLAIM-288 CLAIM-284 CLAIM-285 THEORY-071 — Proposed; open claims and readings, cited as what this reading bears on, nothing here rests on their being settled -->
<!-- inactive-ok-file: LIT-1031 — Unavailable; Benthall and Salge, named as the neighbouring legal argument, not leaned on -->

# NOTE-723: Kahl — How continuity distinguishes autonomy from agency in agentic AI

## Contribution

A diagnosis of "category inflation" in talk of agentic AI. Kahl separates
operational autonomy, which he accepts as engineering vocabulary, from
"attributive agency", agency for purposes of responsibility, authority
and governance. He gives a structural criterion for the second,
continuity pressure, positions it against five neighbouring accounts
(Floridi and Sanders, Dennett, Dung's dimensions, Bratman's planning,
Frankfurt's endorsement), applies it to four classes of system and two
borderline classes, and draws governance consequences: misattributed
agency displaces responsibility, worst where affected persons cannot
exit.

## Key insight

Optimising well is not the same as owning the standard one optimises
under. A system becomes a candidate for responsibility only when its
standard itself can break down and the system, not its operator, has to
settle what replaces it and live with the settlement. While failure is
met by retraining, rollback, prompt changes or replacement, the
evaluator is not at stake, and there is no agent there in this sense,
however capable the system.

## Assumptions

- **A distinct attributive sense of agency.** Thin operational
  agency-talk is left alone: "The present article accepts the usefulness
  of thin operational agency-talk in computer science and AI
  engineering. Its target is narrower: the migration from operational
  description to normative attribution in governance contexts."
- **Substrate neutrality.** "nothing in the account requires biology,
  consciousness, personhood, or human-like intelligence."
- **Functional, not metaphysical, continuity.** "The phrase 'continuing
  evaluative standpoint' is used functionally, not metaphysically. It
  does not require numerical identity, biological continuity,
  consciousness, or an enduring self."
- **Necessary only.** "It offers a necessary condition, not a sufficient
  theory of agency, and makes no claims about free will, consciousness,
  moral responsibility, or desert."
- **Diagnostic method.** "Its methodological posture is diagnostic rather
  than revisionary." No formal model, no data.

## Key results

- **Capability does not fix where evaluative authority sits (§2).** Table
  1 pairs each functional property of agentic AI with what it does not
  show: planning not authorship of evaluative standards, tool use not
  ownership of objectives, memory not continuity pressure, multi-agent
  coordination not unified evaluative authority, autonomous action not
  responsibility-bearing agency. "Multi-agent coordination may distribute
  execution, but distribution of execution is not the same as unity of
  authorship."
- **Neighbouring accounts presuppose the evaluator (§3).** Decision
  theory, planning and hierarchical endorsement "presuppose the existence
  of an agent whose attitudes are being organised". Dung's dimensions are
  in a different register: they say "what a system can do, whereas
  continuity pressure characterises what is at stake for the system in
  doing it." "Capability and continuity are independent properties, not
  endpoints on a single scale." Treating any of them as sufficient
  "reverses the order of explanation: it assumes what it ought to
  explain."
- **The criterion (§4).** "Continuity pressure is not persistence over
  time alone. It begins where an inherited evaluative frame no longer
  settles how future operation should proceed." The threshold "is
  therefore not revision as such, but revision whose consequences must
  be carried forward by a continuing evaluative standpoint." Authorship
  "marks the structural relation between frame-breakdown and attributable
  frame-settlement." Three exclusions: "Continuity pressure is absent
  where revision is externally imposed, where rollback avoids carrying
  forward the consequences of revision, or where the system merely
  selects among revision paths already ranked by a fixed higher-order
  criterion."
  - The doctor whose patient falls outside the protocol: "The issue is
    not correction within a rule, but whether the rule still governs the
    case."
  - Meta-learning, reward-model updating and constitutional constraints,
    if bounded by an antecedent rule, are "adaptation within an evaluative
    frame rather than authorship of that frame."
- **The test (§5).** Three questions: does future operation depend on
  preserving the same evaluative standpoint through revision; can failure
  threaten that standpoint rather than trigger correction; is the revised
  frame "settled under breakdown, rather than determined by an antecedent
  objective, reward structure, policy, or deployment constraint?"
  - Tool-using language-model agents fail by resetability: "The agent does
    not have to carry forward a revised standard as the basis for its
    future operation."
  - Reinforcement learners fail because revision stays bounded by "an
    antecedent admissibility structure". AlphaZero's novel strategy
    "emerged within an antecedent frame". Preference-trained assistants
    are the "most important contemporary stress test", and fail:
    "Internal representation of evaluative preference is not authorship
    of evaluation." Reward hacking is diagnosed and corrected from
    outside.
  - Multi-agent workflows: "unity of action is not unity of authorship."
    Disagreement among planner, critic and tester "is resolved within an
    orchestration regime".
  - Institutional systems (triage, the Dutch childcare benefits scandal,
    COMPAS, the Allegheny screening tool) exercise "authority without
    authorship".
  - Borderline: a self-modifying skill-library agent (Voyager) is closer,
    because history becomes operationally relevant, but still bounded by
    a meta-objective and resettable. A continually learning clinical
    system is closer still, because rollback is costly, but "inertia is
    not authorship."
- **The group-agency reply (§5.3).** Kahl grants that a workflow could be a
  List-and-Pettit group agent. What separates a court from an
  orchestration is that the court's standards for its own integration rule
  "are themselves contestable through institutional process", whereas a
  workflow's rule "is revisable only through external intervention".
  "The structural distinction is not whether the integration rule was
  originally 'designed', but whether revision of that rule under
  breakdown is internal or external to the candidate group agent."
- **The sceptic (§5).** The worry that no artefact can meet the criterion,
  since makers can always reset it, is met by saying the criterion is "a
  structural specification of what would need to change", "demanding by
  design, but not unfalsifiable."
- **Pseudo-agency (§6).** Distributed inputs plus concentrated
  institutional closure make an output decision-settling, and agency
  language "migrates upward to the system as a whole".
- **Governance (§§7–8).** Corrigibility, auditability, human authority over
  objectives and human accountability "presuppose that the system remains
  an object of governance rather than a bearer of evaluative authority."
  "In deployed governance contexts, operational autonomy without agency is
  often a condition of governability rather than a defect." Under
  non-exit, misattribution leaves "a gap in traceability between
  institutionally embedded evaluative standards and the actors
  responsible for specifying, relying on, and revising them."

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Operational capacities (planning, tool use, memory, coordination, autonomy) do not establish who authors the evaluative standards | moderate | conceptual; Table 1 |
| C2 | Attributive agency requires continuity pressure: settlement of a revised evaluative frame under breakdown, carried forward by the same standpoint | moderate as a proposal | definitional, motivated by the doctor case and the presupposition argument |
| C3 | Revision ranked by a fixed higher-order criterion, imposed from outside, or escaped by rollback is not authorship | moderate | follows from C2 |
| C4 | Representative current systems ordinarily fail the test | moderate for typical deployments | case analysis, not measurement |
| C5 | What separates a group agent from an orchestration is whether revision of its integration rule under breakdown is internal, not whether the rule was designed | moderate | the court contrasted with the workflow |
| C6 | Governance frameworks presuppose that deployed systems are not agents in this sense | moderate | NIST, ISO/IEC 42001, audit literature |
| C7 | Misattributed agency displaces responsibility, most under non-exit | moderate | mechanism argued from cases |

## Concepts

- **Operational autonomy.** Task execution with reduced need for
  prompting.
- **Attributive agency.** Agency for purposes of responsibility,
  authority and governance.
- **Evaluative frame.** The standards by which success, failure,
  relevance, risk or permissible action are assessed.
- **Continuity pressure.** The condition in which the inherited frame no
  longer settles future operation and a revision must be carried forward
  by a continuing standpoint.
- **Authorship.** The relation between frame breakdown and attributable
  frame settlement; not creation, intention or originality.
- **Closure.** The point at which an output is treated as
  decision-settling for institutional purposes.
- **Pseudo-agency.** Agency language attaching to a system because
  closure is organised around its output.

## Connections

It positions itself against Floridi and Sanders (2004) and Floridi's
agency without intelligence, Dennett's intentional stance, Dung (2025)
and van Lier's dimensional accounts, Butlin (2024) on reinforcement
learning and agency, Bratman's planning theory, Frankfurt's hierarchy,
List and Pettit's group agency, and the responsibility-gap literature
(Matthias; Santoni de Sio and Mecacci; Vallor and Vierkant). It cites no
enactive or autopoietic work, and none of Barandiaran, Di Paolo or
Moreno. Benthall and Salge ([LIT-1031](../literature.d/LIT-1031.md), not read) reach a neighbouring
legal conclusion from the enactive side.

## Bearing on the record

**On [QUESTION-092](../questions.d/QUESTION-092.md): Kahl's answer is that the location of control
matters, but not the location of the scheduler.**

- Allocation of execution among a system's own components is not what
  he counts. A multi-agent workflow allocates work internally, with
  "voting rules, ranking functions, confidence thresholds", and he says
  "These structures coordinate execution; they do not generate
  authorship of the governing frame." So internal authority allocation,
  as such, does not make the stronger difference.
- What does is whether the system revises its own integration rule and
  standards under breakdown. That is an internal/external distinction,
  and it does not reduce to behaviour: two workflows that behave alike
  differ if one's rule is revisable only by its developers. The
  question's summary expected Kahl to make "the scheduler's location
  beside the point". That was half right. The scheduler's location is
  beside the point; the location of revision under breakdown is the
  point.
- It rejects origin as the criterion: "not whether the integration rule
  was originally 'designed'". That bears on [CASE-081](../cases.d/CASE-081.md). On Kahl's view
  the second stage counts if, and only if, the system settles revised
  standards under breakdown. A system that keeps maintaining itself on
  the learned policy after the reward stops has not yet shown that; it
  "merely selects among revision paths already ranked by a fixed
  higher-order criterion", or does not revise at all.

**On [CLAIM-288](../claims.d/CLAIM-288.md): independent support, from a different notion of
agency.**

- Kahl argues from responsibility, not self-constitution, and never
  mentions enactivism. He reaches the same conclusion about systems whose
  objectives are fixed from outside: they "may optimise effectively while
  lacking authorship of those standards". Self-modification bounded by "an
  antecedent meta-objective" does not change that. [CLAIM-288](../claims.d/CLAIM-288.md)'s
  second answer, that the modeller's objectives are only initial
  conditions, is the case Kahl calls borderline, and his condition for
  crossing is stricter than the claim's: revision settled under
  breakdown, not ranked by any antecedent criterion.
- [CLAIM-285](../claims.d/CLAIM-285.md)'s endorsement scheme computes authority by an
  aggregation rule no operator controls. On Kahl's test, that is an
  orchestration regime, unless the population can revise the rule
  itself under breakdown.

**On [CLAIM-116](../claims.d/CLAIM-116.md).** Kahl's position is a version of it for evaluation:
adaptation, meta-learning and self-modification are regulation within a
frame, and do not establish an author of the frame.

**On [CLAIM-086](../claims.d/CLAIM-086.md).** Kahl's "authority without authorship" has the same shape:
an institutional system's output governs downstream action while the
authority of its standards lies elsewhere. Kahl does not frame it as a
claim about rules governing each other's scope, so this is resemblance,
not support.

**On [THEORY-071](../theory.d/THEORY-071.md).** Both deny that optimising an externally fixed
function makes an agent. They are not the same account. [THEORY-071](../theory.d/THEORY-071.md)'s
normativity is set by a self-maintaining organisation; Kahl's is
authority over evaluative frames, with no metabolic or organisational
grounding, and he expressly drops individuation by persistence ("not
numerical identity, personhood, or selfhood"). A bacterium is an agent on
[THEORY-071](../theory.d/THEORY-071.md) and plainly not on Kahl's attributive sense. Different
explananda, so no rivalry.

## Limitations

- Conceptual throughout. The cases are described at the level of typical
  deployments; nothing is measured.
- The phrase "settled under breakdown, rather than determined by an
  antecedent objective" carries the whole criterion, and it is not made precise.
  Every revision process has some prior structure; how much antecedent
  ranking is too much is not said. The paper concedes the threshold is
  approached "along a small number of overlapping dimensions" that are
  "illustrative rather than canonical".
- The sceptic's worry is answered by assertion that the criterion is
  falsifiable, without a case that would satisfy it.
- The governance sections assume the conclusion of §5 and add
  institutional mechanism; they are not further evidence for the
  criterion.
- Humans are said to remain "bearers of judgement through correction",
  but whether human standards are settled under breakdown rather than
  ranked by antecedent upbringing is not examined.

## Open questions

- What would a system look like that settles a revised frame under
  breakdown without an antecedent ranking of revisions? Kahl gives no
  positive case, artificial or biological.
- Is the court's internal contestability of its integration rule enough,
  or must the standards for that contest also be internal? The regress is
  not addressed.
- Does continuity pressure coincide with [CLAIM-025](../claims.d/CLAIM-025.md)'s capacity to
  transform the governing organization? It looks close, and a reading
  that set the two side by side could tell.
