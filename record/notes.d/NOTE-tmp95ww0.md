---
status: Read
paper: LIT-2312
title: 'Kephart and Chess — The vision of autonomic computing'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 from https://jmvidal.cse.sc.edu/lib/kephart03a.html.
    **Read**, in full, 2026-11-12. A delegated reader drafted the reading;
    quotations were rechecked by script against the downloaded copy, and any
    that did not match were kept as paraphrase without quotation marks.
date: '2026-11-12'
summary: >-
  A programmatic statement of IBM's autonomic-computing agenda: computing
  systems that manage themselves "given high-level objectives from
  administrators". It sets out four aspects of self-management
  (configuration, optimization, healing, protection), proposes that
  autonomic systems be collections of autonomic elements each consisting of
  managed elements and an autonomic manager, and lists engineering and
  scientific challenges: element life cycles, service relationships
  negotiated between elements, security and trust, the specification of
  goals by humans, emergent behaviour, robustness, multi-agent learning,
  negotiation theory and statistical modelling. The architectural picture
  later called MAPE-K, and an agenda.
---
<!-- inactive-ok-file: CASE-tmpvq90k — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->
<!-- inactive-ok-file: CASE-194 — Proposed; cited for what each holds, not as settled -->

# NOTE-tmp95ww0: Kephart and Chess — The vision of autonomic computing

## Contribution

The architectural picture later called MAPE-K, and an agenda. The paper's Figure 2 labels the autonomic manager's parts Monitor, Analyze, Plan, Execute and Knowledge; the text describes the manager as monitoring the managed element and its environment and constructing and executing plans from an analysis of that information. **The paper does not use the acronym "MAPE-K"**; the text does not describe a knowledge component of the manager (it mentions knowledge only as, e.g., a problem-diagnosis component using "knowledge about the system configuration").

## Key results

- The goal (Autonomic option): “computing systems that can manage themselves given high-level objectives from administrators”.
- The manager (Architectural considerations): “By monitoring the managed element and its external environment, and constructing and executing plans based on an analysis of this information, the autonomic manager will relieve humans of the responsibility of directly managing the managed element.” (The sentence crosses the page break onto p. 44, so extracted text interrupts it.)
- Upgrade, regression test and revert (Self-management; Figure 1): the system will install upgrades, “run a regression test to make sure all is well”, and on errors “revert to the older version while its automatic problem-determination algorithms try to isolate the source of the error”.
- Authority over an element (Architectural considerations): behaviour is “driven by goals that its designer has embedded in it, by other elements that have authority over it, or by subcontracts to peer elements with its tacit or explicit consent.”
- Goal specification stays with humans (Goal specification): “it will still be up to humans to provide those systems with policies—the goals and constraints that govern their actions”; leverage “will also greatly magnify the consequences of any error humans do make in specifying goals”, and “tracing and correcting policy errors will be very difficult.”
- Policy as an attack surface (Systemwide issues): “By altering or otherwise manipulating high-level policies, an attacker could gain much greater leverage than is possible in nonautonomic systems.”
- Multi-agent learning (Scientific challenges): “There are no guarantees of convergence.”

## Assumptions

Self-management can be built from locally managed elements whose interactions produce system-level behaviour; humans set policy and the system realizes it; biological and economic self-governance are sources of design.

## Concepts

Autonomic computing; self-configuration, self-optimization, self-healing, self-protection; autonomic element; managed element; autonomic manager; policy (goals and constraints as rules or utility functions); service agreements and negotiation; sentinel elements; goal specification.

## Bearing on the record

The exchange (A50 §2, decoded lines 7086–7090): Kephart and Chess "describes self-managing computing systems organized around monitor, analyze, plan, and execute operations, supported by shared knowledge", and "This is the well-known **MAPE-K loop**." Substantially accurate: the figure shows exactly that structure. Two refinements: the knowledge is the autonomic manager's (one per element in Figure 2), not described as shared across elements; and the paper does not itself name the loop MAPE-K. A50's "strongest architectural predecessor" for luria is A's judgement. Note that the paper leaves the revision of *policy*, the analogue of schema and governance change, to humans and names policy error and policy tampering as hard problems; it proposes no mechanism for governing policy change.

- **[QUESTION-tmps5iou](../questions.d/QUESTION-tmps5iou.md)** (lists it as self-adaptive prior art): **bears on part 1, against a MAPE-K reading of luria's novelty and also against MAPE-K covering it**. The paper couples change to regression tests and reversion (executable checks) and gives elements authority relations, but its object of self-management is configuration, parameters and components under fixed human policy; the revision of the goals and constraints themselves is left to humans with no recorded decision or migration. A50's remark that luria is at most a "governed knowledge substrate" for such a loop fits the paper.
- **[QUESTION-388](../questions.d/QUESTION-388.md)** (programmable system vs one that governs its own reconfiguration): **bears directly, as a foil**. Autonomic systems reconfigure themselves under policies they do not revise; the paper's own division of labour (humans specify goals) places it on the "programmable" side of [QUESTION-388](../questions.d/QUESTION-388.md)'s distinction.
- **[CLAIM-086](../claims.d/CLAIM-086.md)** (a constraint may govern conduct without governing the conditions under which it remains authoritative): **supports, as an instance**. Policies govern element behaviour; what keeps a policy authoritative, and how a wrong one is traced and corrected, is named as an open problem.
- **[CASE-tmpvq90k](../cases.d/CASE-tmpvq90k.md) / [CASE-194](../cases.d/CASE-194.md)** (diagnosis of one symptom with several causes): Figure 1's problem determiner, which uses inter-element dependencies to pick the culprit among three suspect modules, is a model-based diagnosis step inside the loop. Illustration only.

## Limitations

A 2003 vision paper: no implementation, no evaluation, much of it forecast; IBM authorship with a product agenda.
