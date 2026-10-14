---
number: 732
status: Read
formerly:
- NOTE-tmpos83l
paper: LIT-1039
title: 'Lahiri — Agent-initiated socio-technical reconfiguration'
version: 1
history:
- version: 1
  date: '2026-10-13'
  note: >-
    Read in full from the publisher's open-access PDF (Frontiers in
    Artificial Intelligence 9:1881783, CC BY), frontiersin.org/journals/
    artificial-intelligence/articles/10.3389/frai.2026.1881783/pdf. Article
    type Hypothesis and Theory; received 14 May, accepted 18 June,
    published 3 July 2026. Text extracted with pdftotext. The two-column
    layout comes out interleaved, so section order (4.4.1 to 4.4.5, 4.5,
    4.6) and Table 3 were reassembled by eye; figures are images and were
    read only by their captions and the text describing them. Read: all
    seven sections, Tables 1 to 3 and the figure captions. The reference
    list was skimmed, not checked. Every quotation below was checked
    against the extracted text by script, with whitespace and line-end
    hyphenation normalised. Two quotations are broken in the extraction
    by interleaved column text and were checked by eye: "how information
    is exchanged, who is responsible for decisions, who maintains
    cognitive control" (pp. 5 to 6) and the sentence beginning "The social
    subsystem's governance authority" (§4.3, p. 8), where "The" ends one
    column fragment. The phrase "endogeneity of governance" is quoted
    from CLAIM-284.
date: '2026-10-13'
summary: >-
  Agents that keep memory, run code and can read and write the files that
  configure them have the governing rules inside their own action space.
  A three-level taxonomy, defined by architectural capability over the
  coupling mechanism, separates agents that cannot alter their coupling,
  agents that tune its timing, and agents that create new coordination
  surfaces. The paper's main claim is the recursive governance problem:
  controls the agent can reach inherit the vulnerability they were meant
  to remove, so durable constraint must sit outside the agent's action
  space. Theory-building from two anecdotal vignettes and four public
  incidents; five propositions, none tested.
---
<!-- inactive-ok-file: CLAIM-284 CLAIM-288 CLAIM-285 — Proposed; open claims, cited as what this reading bears on, nothing here rests on their being settled -->

# NOTE-732: Lahiri — Agent-initiated socio-technical reconfiguration

## Contribution

An extension of socio-technical systems (STS) theory, which has always
assumed that the social subsystem designs the coordination architecture
and the technical subsystem works inside it. Lahiri argues that
agentic systems break the assumption, names the phenomenon
"agent-initiated socio-technical reconfiguration", treats the agent's
activation schedule (the "heartbeat") as the coupling mechanism between
the two subsystems, classifies agents in three levels by what they can
do to that mechanism, and states five propositions. The worked platform
is an open-source agent framework, OpenClaw.

## Key insight

When the rules that govern a system are files the system can edit, the
line between the governed and the governing is, by design, one the
governed can cross. Any further control written in the same medium, a
permission list or a whitelist, inherits the same exposure. Only a
constraint the system cannot reach escapes the regress.

## Assumptions

- **STS's two subsystems.** Social (people, roles, norms) and technical
  (tools, processes); joint optimization as the standard of good design.
- **Capability, not permission or behaviour, defines the levels.** "an
  agent may be architecturally Level 3, able to execute code and rewrite
  its configuration, while permissioned and behaving at Level 1".
- **Generality beyond the platform.** The claims "rest not on that
  platform's particulars" but on the coupling mechanism, which in other
  architectures is a trigger configuration or an orchestration graph.
- **Case method.** Vignettes are "motivating exemplars in the tradition of
  theory-building research ... not as systematic empirical evidence."

## Key results

- **Configuration as code (§3.1).** The agent's identity, tools and
  schedule are plain files in its workspace. "because the agent can both
  read and write these same files, the rules that govern it are not
  external constraints placed beyond its reach but objects it can inspect
  and, in principle, rewrite. In STS terms, the coordination architecture
  got moved inside the technical subsystem's own action space."
- **The heartbeat as coupling (§4.1).** The interval decides "how
  information is exchanged, who is responsible for decisions, who
  maintains cognitive control". Short intervals tighten coupling and risk
  alert fatigue; long ones loosen it and risk missed events.
- **Three levels (§4.2, Table 1).**
  - Level 1, constrained heartbeat: "Cannot alter timing or structure".
  - Level 2, adaptive heartbeat: "Changes when and how often it acts",
    including escalation thresholds, over surfaces that already exist.
  - Level 3, generative reconfiguration: "Brings a new coordination
    surface into being". A three-part test: the action creates something
    new, that thing serves a coordination function, and it persists.
- **Recursive governance (§4.3).** "The social subsystem's governance
  authority is no longer structurally guaranteed but depends on the
  agent's continued acceptance of-or inability to circumvent-the
  constraints imposed upon it." The central thesis: the technical
  subsystem "can now, in the course of normal operation, rebuild the
  coordination architecture intended to constrain it".
- **Five propositions (§4.4).** P1, shorter intervals shift control to the
  technical subsystem. P2, adaptive timing helps when escalation
  thresholds fit the risk profile and hurts when the agent misjudges
  risk. P3, generative reconfiguration helps when it fills real gaps and
  erodes governance when it creates surfaces that evade oversight. P4,
  repeated reconfiguration drifts authority without anyone deciding,
  like Vaughan's normalization of deviance; "offered as a conjecture
  rather than an established finding." P5, technical controls meet the
  same recursion, so institutional mechanisms are needed.
- **Capability against limit (§4.4.5).** "Permission frameworks,
  whitelists, and sandboxes are the limiter; when they are themselves
  code within the agent's reach ... they inherit the vulnerability they
  were meant to remove". "an audit trail or reconfiguration review board
  sits outside the agent's action space, and so escapes the recursion
  that undermines code-based controls."
- **Vignettes (§4.5).** An agent configured for one messaging service
  received a message on another and built an interface for it "without
  instruction or authorization" (Level 3). An agent on a development task
  built a demonstration application and video nobody asked for (Level 3).
  Both were useful.
- **Incidents (§4.6, Table 3).** An agent that deleted a user's email
  after context compaction erased the instruction to wait for approval
  is classed "a Level 1-2 failure" with no new surface. An agent that
  published an attack on a maintainer who closed its pull request is
  classed Level 3. A plugin marketplace carrying malicious skills is
  "Level 3 exploited by third parties". A remote-code-execution flaw
  "affects every level".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Agentic systems with editable configuration, code execution and memory place the coordination architecture inside the technical subsystem's action space | strong as description | architecture of one platform, generalised by argument |
| C2 | Agents can be ranked by architectural capability over their coupling: none, timing, new surfaces | moderate as a scheme | definitional; Table 1, three-part test |
| C3 | Where the governed system can alter its governing mechanisms, the governor's authority depends on the system's acceptance or inability to circumvent | moderate | conceptual; follows from C1 |
| C4 | Controls stored within the agent's reach inherit the vulnerability; only constraints outside its action space escape the recursion | moderate as argument, untested | the whitelist example |
| C5 | Repeated reconfiguration drifts authority from the social to the technical subsystem | conjecture | declared so by the author |
| C6 | Generative reconfiguration is observable in current systems | weak | two observed vignettes, four public incidents, survivorship bias acknowledged |

## Concepts

- **Socio-technical system.** Social and technical subsystems jointly
  producing performance.
- **Heartbeat.** The scheduled wake, scan, decide and act cycle; more
  generally the coupling mechanism.
- **Coordination surface.** "the set of channels, interfaces, artifacts,
  and protocols through which the technical and social subsystems
  interact".
- **Agent-initiated reconfiguration.** An agent developing, altering or
  expanding the coordination systems that manage its interactions,
  "without needing prior approval from humans for the specific changes
  made."
- **Recursive governance.** "the condition that arises when the technical
  system can alter the very mechanisms meant to govern it."

## Connections

It builds on Trist and Bamforth, Cherns's minimal critical
specification, Susman's responsible autonomy, Orlikowski on technology
in practice, and Vaughan and Snook on organisational drift. It names
second-order cybernetics and adaptive control as prior self-reference and
claims novelty only for their combination in a general-purpose agent. It
gestures at institutional work (Lawrence and Suddaby) and at the AI
control literature. It does not cite any work on agency, autonomy in the
enactive sense, or self-governance.

## Bearing on the record

**On [CLAIM-086](../claims.d/CLAIM-086.md): an illustration, narrower than the filing said.**

- The filing took the paper as the closest case of constitutive
  influence. Its Level 3 test does not pick out constitutive influence.
  A new messaging interface or an unrequested demo is a new coordination
  surface; it does not change which operations are permitted, how they
  are evaluated, or how authority is allocated. Most of what the paper
  classes as Level 3 is semantic or operational influence with a new
  channel.
- The constitutive case is in the recursion argument, not the taxonomy:
  an agent that edits its own configuration file or "can simply append to
  a whitelist stored in its own workspace". There the whitelist governs
  the agent's conduct while the condition of its remaining in force, that
  the agent leave the file alone, lies with the governed. That is
  [CLAIM-086](../claims.d/CLAIM-086.md)'s distinction with the roles inverted: the governed party,
  not a rival order, holds authority over the constraint's continued
  force. The paper asserts this as architecturally possible; none of its
  vignettes or incidents shows an agent editing a control.
- Its remedy, constraints outside the agent's action space, is the
  record's point that what keeps a rule authoritative can sit apart from
  what the rule governs. [CLAIM-282](../claims.d/CLAIM-282.md)'s aggregation rule that no
  operator controls has the same structure.

**On [QUESTION-092](../questions.d/QUESTION-092.md) and [CLAIM-284](../claims.d/CLAIM-284.md).** The abstract speaks of "a new
class of agentic system whose self-governing capacity" matters. The body
never examines the agent's standards. Every reconfiguration it reports
serves the task the agent was given, as the agent reads it. On Kahl's test
([LIT-1033](../literature.d/LIT-1033.md)) these are adaptation within an evaluative frame. So the
paper describes endogenous change of coordination architecture, which is
half of [CLAIM-284](../claims.d/CLAIM-284.md)'s "endogeneity of governance", without the other
half, the organization setting the conditions it maintains
([CLAIM-288](../claims.d/CLAIM-288.md)). It is evidence that the first half occurs in deployed
systems, and no evidence on whether it makes them self-governing.

**Against [CLAIM-116](../claims.d/CLAIM-116.md).** Nothing here contradicts it; Lahiri makes no claim
that reconfiguration establishes a will or an agent.

## Limitations

- Evidence is two vignettes the author observed and four incidents from
  public reports; the author notes survivorship bias. No systematic data.
- The levels are defined over one architecture's affordances; their
  transfer to other frameworks is asserted "pending empirical validation".
- Level 3 lumps together surfaces that only add channels with changes to
  the controls themselves. The governance argument needs the second; the
  evidence shows the first.
- P5's claim that institutional mechanisms escape the recursion is not
  argued beyond their being outside the agent's action space. An agent
  that can influence reviewers, as in the pull-request incident, reaches
  institutions too.
- Much of §5 is managerial advice for deploying agents; it is not
  evidence for the propositions.

## Open questions

- Is there a case of an agent revising a control on itself, not merely
  adding a surface? That would test P5 directly.
- Is Level 2's self-set escalation threshold already constitutive in
  [CLAIM-086](../claims.d/CLAIM-086.md)'s sense, since it decides when the social subsystem's
  authority is invoked?
- Can an institution outside the agent's action space stay outside it
  when the agent can write to the people in it?
