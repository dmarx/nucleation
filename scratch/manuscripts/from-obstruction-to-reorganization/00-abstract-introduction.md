<!-- scratch/manuscripts/from-obstruction-to-reorganization/00-abstract-introduction.md -->

# From Obstruction to Reorganization: Inquiry, Anchoring and the Governed Revision of a Research Record

*Working title. Alternatives: "Nucleating an Inquiry: A Longitudinal Case Study of Reflexive Research Infrastructure"; "luria: nucleating an argument, and revising what it is anchored in."*

## Abstract

An argument developed across many sessions with AI collaborators who keep no memory between them fails characteristically at identity, not structure. Concepts are redefined silently, objections return as though new, and the thesis moves with no turn arguing for the move. An earlier account, developed in the same project, proposed that a project memory supplies *anchors*: addressable, persistent structure on which later argument can grow, and against which a manuscript becomes a view rather than the argument's only copy. That account left an objection standing. The anchors are coded in a grammar of document types, fields, vocabularies and relations, and that grammar is fixed before the inquiry knows what it will need.

We take up the objection with an account of inquiry as specification. An inquiry poses a question in a language. It fixes an answer space, makes differences accessible through interventions and observations, judges candidate answers by criteria, and runs on bounded resources. It becomes reflexive when any of these becomes its object. On this account, a research record's grammar is part of the inquiry it records. Revising the grammar is the inquiry taking its own regime as its object. And a record that secures traceability for its claims must secure it for its grammar too, or drift recurs one level up. We show how Luria, a configurable system of typed, versioned and interlinked documents, realises each component of the inquiry and gives the reflexive step a governed place.

We then examine what happened when one inquiry took its grammar as its object. Between 25 September and 19 November 2026, the Nucleation record grew from 214 to 10,070 files. Its local schemes grew from five to twelve and its configured vocabularies from six to eighteen. We reconstruct eight interventions: vocabulary splits, added classification dimensions, scheme boundaries redrawn, an abstraction withdrawn, and lines of inquiry decomposed, together with decisions not to add structure. The new distinctions are in use. Fourteen of eighteen combinations of CASE kind and standing are populated. Among 766 claims, 39 are Proposed with a demonstrated warrant and 185 are Active with an interpretive one. Grammar change was coupled to ordinary work. In the record's first month, 94% of new vocabulary values were used in the unit of work that added them, and 91% of such units carried a decision record, against 16% of all pull requests.

A later mechanism, the postmortem, made review of the grammar's changes a record type of its own. In one cycle, a review found that the research-backlog scheme's stage field did not discriminate between entries, and the revision reduced the share of entries at its first stage from 96.4% to 69.2%.

The evidence supports the account's predictions about misfit, revision and traceable change. It cannot show that the revisions improved the inquiry, and it is bounded by the fact that the record's measures are counted in its own grammar. The process was directed by the owner and carried out by assistants. We identify the observable signatures that preceded each reorganisation, and propose evaluations of whether an assistant could detect them unprompted.

---

## 1. Introduction

### 1.1 The problem the first account posed

This record began, as a project, with a question: when an argument is developed across sessions with collaborators who keep no memory, what makes it settle into stable structure, and what can a project memory contribute (QUESTION-037)? The question came from experience. In the record's own exchanges with AI assistants, arguments did not fail for want of structure. Every session produced organised prose. They failed at identity (CLAIM-177). In one documented exchange, the manuscript drafted from an argument's matured state changed the thesis "with no turn arguing the move" and dropped 24 of the argument's items, none on request (CLAIM-324).

The answer proposed in the predecessor manuscript, "luria: nucleating an argument", was *anchoring*. As a crystal grows only on a nucleus that persists, an argument's later structure grows only on structures that persist. What makes a structure persist is not that it is stored but that it is addressable (CLAIM-182, CLAIM-185). A record that gives each claim, question, case and term a stable code, a status and typed relations supplies such anchors. A manuscript drafted against that record becomes a view over the argument, checkable against it, and no longer the argument's only copy (CLAIM-178).

### 1.2 The objection it left open

The predecessor's account came with an objection the record filed against itself (CLAIM-181). A record fixes the grammar in which an argument is expressed. Its closed vocabulary of document types, roles and relations formalises early. A move that fits no type or declared relation is therefore forced into the nearest one, or lost, until someone notices the misfit and amends the grammar. Anchoring buys continuity at the price of committing in advance to what can be anchored. If the inquiry outgrows that commitment, the record preserves the mistake as faithfully as everything else.

### 1.3 The move this paper makes

We answer the objection with the record's account of inquiry as specification (CLAIM-470). A question fixes which differences would count as an answer, and an inquiry can revise what an answer could be. Written as a tuple (TERM-095), an inquiry has a language, an answer space, interventions, observations, criteria and resources, and it is reflexive when any of these becomes its object. A record's grammar realises the language, and much of the answer space and criteria. Revising the grammar is therefore not maintenance done to the inquiry from outside. It is the inquiry's reflexive step (§2.7, T2). That turns the objection into two questions. Can a record make its grammar revisable without losing the continuity anchoring was for? And did one record actually do so?

The first question is answered by design. The traceability a record secures for its claims (CLAIM-189) must extend to its grammar: a grammar change must be announced, located and carried through the existing entries (§2.7, T3). The second is empirical, and most of this paper addresses it.

### 1.4 Research questions

- **RQ1.** What must a research record provide if arguments drift at identity, and if inquiry can revise its own regime? (§2)
- **RQ2.** How does Luria realise that account, and what does the account predict about a record's development? (§3)
- **RQ3.** How did one AI-assisted project actually reorganise its representation and governance when inquiry met the limits of its grammar? (§§5–7)
- **RQ4.** Which parts of that process could be delegated to assistants, and how could the delegation be tested? (§§8.7, 9)

### 1.5 Contributions

1. A statement of the record's account of inquiry: drift, anchoring and its costs, what a record of inquiry can secure, and inquiry as specification. It is gathered from its claims, with each claim's standing given (§2).
2. A mapping of Luria onto that account, component by component, and six predictions it makes about a record's own development (§3).
3. A longitudinal reconstruction of the Nucleation record's first eight weeks: growth, rates of grammar change, and the coupling of grammar change to decisions (§5).
4. A comparative analysis of eight interventions, including decisions not to add structure, each annotated with the component of the inquiry it revised (§6).
5. A worked account of the shift from recording grammar decisions to reviewing their consequences, through one complete review-and-revision cycle (§7).
6. The observable signatures that preceded each reorganisation, offered as a starting point for delegating diagnosis to assistants, with designs to test the delegation (§§8.7, 9).

### 1.6 The argument in brief

The record's grammar was not merely extended to hold more material. It was revised when its types, vocabularies and relations failed to keep apart, or hold together, what the inquiry needed. Each revision changed what the record could distinguish, which inferences it could express and contest, and how later work was organised. The revisions were made traceable: decision records kept their reasons, migrations kept entries' identities while reinterpreting them, and executable checks made them binding. Later, postmortems made their consequences evidence for further revision. In the terms of §2, the record's inquiry repeatedly took its own regime as its object, and progressively institutionalised doing so. The owner directed that process. Whether an assistant can take over the step of recognising when the regime is inadequate is the next question, and the record makes it a testable one.

### 1.7 Relation to the predecessor manuscript

This paper succeeds "luria: nucleating an argument" (proposed 11 October 2026), whose argument is held in the record's `nucleating-argument` line. Three things have changed since that proposal.

- **The line has grown and split.** On 7 November, ADR-082 divided it into `nucleating-argument` (drift, anchors and the costs of anchoring), `records-of-inquiry` (what a record of a developing argument keeps) and `record-as-apparatus` (the record's grammar as its own apparatus). This paper draws on all three. Its empirical part belongs mainly to the last.
- **Several results now qualify the first account.** Persistence is not productivity (CLAIM-595). The two justifications of the second-occurrence rule part when filing is dear (CLAIM-630). Conclusions, support graphs and sufficient states each fall short of what revision needs (CLAIM-293, CLAIM-294, CLAIM-299, CLAIM-300).
- **The objection has a history.** CLAIM-181 was filed on 11 October as a prediction. By 22 October CLAIM-419 recorded the record meeting it by amending its grammar, and by November it had a history of doing so, which this paper reports.

The predecessor's thesis survives. What changes is its scope: the anchors are themselves anchored in a grammar, and the grammar has to be anchored too.

### 1.8 Roadmap

Section 2 sets out the argument. Section 3 maps Luria onto it. Section 4 places the work in the literature, and Section 5 gives the method and the growth data. Section 6 presents the cases, and Section 7 the governance mechanisms. Section 8 discusses obstruction, capability, cost, risk and delegation, and returns to the argument. Sections 9 to 11 give evaluations, limitations and the conclusion.
