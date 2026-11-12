---
status: Read
paper: LIT-tmp1ur4j
title: 'Johnson and Hayes-Roth — Integrating Diverse Reasoning Methods in the BB1 Blackboard Control Architecture'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 from the copy named in the reading. **Read**,
    2026-11-12. This copy stands in for the unread original LIT-tmp4pa3f. A
    delegated reader drafted the reading; quotations were rechecked by script
    against the downloaded copy, and any that did not match were kept as
    paraphrase without quotation marks.
date: '2026-11-12'
summary: >-
  BB1 is a domain-independent blackboard architecture. Its knowledge sources
  (KSs) work on two blackboards: - **Domain KSs** solve the domain problem
  on the domain blackboard. - **Control KSs** build a dynamic control plan
  on the control blackboard. The plan is made of strategies, foci and
  heuristics. **The basic cycle** has three steps: 1.
---
<!-- inactive-ok-file: LIT-tmp4pa3f — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->

# NOTE-tmpgqis6: Johnson and Hayes-Roth — Integrating Diverse Reasoning Methods in the BB1 Blackboard Control Architecture

## Contribution

The paper extends BB1 with goal-directed control reasoning, and argues that a single explicit control plan on a blackboard can integrate several reasoning methods.

## Key results

- **§II.A:** "Domain KSs solve domain problems on the domain blackboard."
- **§II.A:** "If the KSAR changes the control blackboard, it may alter the criteria used to rate KSARs in the next step."
- **§IV, on integration (OCR "BBl"):** "BBl integrates diverse reasoning methods by permitting independent control knowledge sources to contribute decisions to an explicit, dynamic control plan on the control blackboard."
- **§IV:** "We have not yet implemented Satisfy-Priority-Focus."
- **§V:** Hearsay-II integrated similar reasoning methods, but "it engineered each method in a different domain-specific tailoring of its underlying architecture."

## Assumptions

- A single system with a single scheduler.
- Knowledge sources are triggered by events and preconditions.
- The control plan is a structure explicit enough for KSs to read and write.

## Concepts

- blackboard control architecture
- domain vs control blackboard
- knowledge source and KSAR
- agenda and scheduler
- strategy, focus and heuristic
- hierarchical planning, opportunistic focusing, goal-directed reasoning
- BB1, ACCORD, PROTEAN

## Bearing on the record

**What the paper shows.** It supports the claim that control of a blackboard system can live on a blackboard of its own: an explicit, revisable control plan.

**Where A's framing goes further than the paper.**
- A speaks of "shared structured hypotheses". BB1's agents are modules of one system, not separate holders of evidence.
- So the paper bears on the record's reflexive governance, where procedures sit in the same medium as content, rather than on the question's distributed-evidence comparison.

**Status for the question.** Leaves open.

**Restates:**
- the architecture of Hayes-Roth (1985), cited as [Hayes-Roth, 1985]: separate domain and control blackboards, with control KSs posting a dynamic control plan that rates actions;
- the integration of hierarchical planning with opportunistic focusing, which the paper attributes to earlier work including the 1985 paper.

**Does not restate:**
- the 1985 paper's eight behavioral goals for control;
- its comparison against other control approaches;
- its detailed examples, which were not seen.

## Limitations

- Short conference paper.
- Demonstrated on a single system (PROTEAN).
- One of the two goal-directed mechanisms is not implemented.
- The paper gives no costs; it refers them to Garvey et al. (1987).
- OCR quality is poor. Check quotes against the page image.
