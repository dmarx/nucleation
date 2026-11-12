---
status: Read
paper: LIT-2320
title: 'de Kleer — An assumption-based TMS'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 from
    https://www.dekleer.org/Publications/An%20Assumption-Based%20TMS.pdf.
    **Read** (main text §§1–4 and §7 read closely; §§5–6 skimmed). Read
    2026-11-12. A delegated reader drafted the reading; quotations were
    rechecked by script against the downloaded copy, and any that did not
    match were kept as paraphrase without quotation marks.
date: '2026-11-12'
summary: >-
  De Kleer proposes a truth maintenance system that, besides recording the
  problem solver's justifications as a conventional (Doyle-style) TMS does,
  labels every datum with the minimal sets of assumptions ("environments")
  under which it is derivable. Because contexts are explicit, the database
  need not be consistent: mutually contradictory assumptions can be explored
  at once, a contradiction just marks a set of assumptions as a "nogood",
  context switching is a subset test, and most backtracking and all
  retraction are avoided. The ATMS maintains four label properties
  (consistency, soundness, completeness, minimality) incrementally as
  justifications arrive.
---
<!-- inactive-ok-file: CASE-tmpvq90k CLAIM-tmp8qsef — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->
<!-- inactive-ok-file: CASE-194 LIT-2316 — Proposed, Unfetched; cited for what each holds, not as settled -->

# NOTE-tmp2l1rj: de Kleer — An assumption-based TMS

## Contribution

- A second kind of TMS: assumption-based rather than only justification-based; data are
  labelled with the contexts in which they hold instead of a single in/out status.
- A list of six limitations of conventional TMSs (single-state problem, overzealous
  contradiction avoidance, difficulty switching states, dominance of justifications,
  cumbersome machinery, unouting), each removed by the ATMS.
- The distinction between "the thing assumed" and "the decision to assume".
- Label semantics: a node holds in an environment iff that environment is a superset of
  some environment in its label.

## Key results

1. Abstract, p. 127: "it is possible to work effectively and efficiently with inconsistent
   information, context switching is free, and most backtracking (and all retraction) is
   avoided."
2. §1.1, p. 129: in a justification-based TMS each datum is in or out, so "the contexts
   under which a particular datum is believed are implicit." By contrast "in an ATMS each
   datum is labeled with the sets of assumptions (representing the contexts) under which it
   holds."
3. §1.1, p. 129: "There is no necessity that the overall database be consistent".
4. §1.2, p. 131: "Only assertions directly affected by the contradiction should be
   retracted. The fundamental difficulty is that it is costly to determine which data are
   affected." In an ATMS "one can tell directly whether an assertion is affected or not".
5. §1.2, p. 132: "A contradiction merely indicates that a specific set of assumptions is
   inconsistent, and that data depending on them are affected."
6. §1.3, pp. 132–133 (diagnosis): in LOCAL, "The assumptions are that individual components
   are functioning correctly. A contradiction implies that some assumption is violated";
   the program "requires that the assumptions of an inference be explicitly available and
   that multiple contradictory propagations be simultaneously present in the database." Its
   successor troubleshooter handling multiple faults is reference [11] (= LIT-2316).
7. §3.2, p. 138, the single-state problem: conventional TMSs allow one solution at a time,
   which makes comparing equally plausible solutions hard, yet "this is often exactly what
   one wants to do in problem solving—differential diagnosis to determine the best
   solution."
8. §3.2, p. 139: in a conventional TMS "there is no way to go back to a previous state"
   because "a TMS has no useful notion of global state."
9. §4.2, p. 142: "It is critical to distinguish the thing assumed from the decision to
   assume." Justifications are "propositional Horn clauses" (p. 143).
10. §4.3, p. 144: the ATMS guarantees each label is "consistent, sound, complete and
    minimal with respect to the justifications."
11. §4.9, p. 153, retraction: a retractable justification is "conjoined with an extra
    assumption which represents its defeasability. To retract the justification, the
    problem solver contradicts the conjoined assumption. This is the only reasonable way to
    retract a justification." Direct removal is possible but "directly removing a
    justifications is a bad idea" (sic).
12. §3 opening, p. 137: "The ATMS is not a panacea"; conventional TMSs are oriented to one
    solution, "The ATMS is oriented to finding all solutions".
13. §7, p. 161: the label properties hold only relative to the justifications so far:
    "With the addition of every justification, the set of contexts may change and nodes that
    were irrelevant become relevant and vice versa."

## Assumptions

- The problem solver supplies all inferences as justifications; the TMS records and
  propagates, it does not reason about domain content.
- Justifications are monotone propositional Horn clauses (no negated literals in the basic
  ATMS); nonmonotonicity is expressed through assumptions and nogoods.
- Support is all-or-nothing: an environment derives a node or it does not; there are no
  degrees of support.
- Efficiency depends on inconsistencies being "identifiable in small subsets of
  assumptions" (§4.8).

## Concepts

assumption vs assumed datum; justification (consequent, antecedents, informant);
environment; context; characterizing environment; label; nogood; label consistency,
soundness, completeness, minimality; dependency-directed backtracking; unouting;
single-state problem; node class; problem-solver–TMS interface protocol.

## Bearing on the record

The exchange cited it (per CLAIM-tmp8qsef, from A50 §7) as a truth maintenance system
that, unlike the record, "computes the new belief set". Accurate in kind: the ATMS
computes, for every datum, exactly the contexts in which it holds, from the justifications
alone. One refinement the record should carry: the ATMS does not "withdraw" beliefs in the
AGM sense either; it keeps all data and lets the problem solver choose the context, and it
treats retraction of a justification as something to avoid (result 11).

- **CLAIM-tmp8qsef** (Proposed, branch `claude/file-luria-experiment-design`): *qualifies*.
  It supports the contrast the claim draws (a TMS computes which data hold; the record only
  reports dependants). But it also shows where the impossibility half needs its scope stated:
  for edges read as Horn justifications (deductive, all-or-nothing), a rule reading only the
  justification graph and which assumptions are retired *does* compute correctly which
  conclusions still hold (results 2, 4, 10). CLAIM-293's counterexample works because the
  record's support edges carry evidence of unrecorded strength, not entailment. The claim's
  defeat clause already confines it to "CASE-089's worlds"; one may want the body to
  say that a graph whose edges are entailments is the case where a graph-only rule suffices,
  and that `rests_on` ("could not stand without") states a necessary premise, not a
  sufficient justification. Also relevant: de Kleer's "the only reasonable way to retract a
  justification" is to contradict an assumption, not delete it (result 11) — the same design
  as the record's "retire by status, never by deletion".
- **CLAIM-293** (Active): *supports by contrast*: the ATMS's correctness rests on edges being
  Horn implications; where they are, topology does fix revision. This is the boundary
  condition of CLAIM-293, not a counterexample to it.
- **QUESTION-tmps5iou** (Open, branch): *leaves open*. The paper concerns belief maintenance
  over a fixed vocabulary, not schema change; it names no governed change of the problem
  solver's categories. It is prior art for "truth maintenance", against which
  CLAIM-tmp8qsef says what the record does not do, as the question says.
- **CASE-tmpvq90k** (Proposed, branch; one symptom, several hidden causes) and **CASE-194**
  (Proposed): *bears*. Assumption-based diagnosis (components assumed working; a
  contradiction localizes the fault set; next measurement chosen to discriminate among
  unverified assumptions, result 6) and keeping rival solutions side by side for
  "differential diagnosis" (result 7) are the classical machinery for the diagnose-before-
  repair task those cases propose. Its multi-fault successor is LIT-2316 (Deferred).

## Limitations

OCR noise prevented checking formulas and the worked examples in §§2, 4.6 and 5. The two
companion papers ([7], [8]), where de Kleer compares the ATMS with other TMSs in detail and
gives the problem-solver protocol, were not read. No empirical evaluation is in this paper;
efficiency claims are argued, not measured.
