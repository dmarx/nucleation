---
number: 866
status: Read
formerly:
- NOTE-tmp689da
paper: LIT-1072
title: Hansson — Logic of Belief Revision (SEP, revision of 29 July 2026)
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full on 2026-10-15 from the Stanford Encyclopedia's own page, https://plato.stanford.edu/entries/logic-belief-revision/,
    which shows "First published Fri Apr 21, 2006; substantive revision Wed Jul
    29, 2026". The same revision is served as the Fall 2026 archive edition (plato.stanford.edu/archives/fall2026/entries/logic-belief-revision/).
    The HTML was saved (entry.html, 126,392 bytes) and its text extracted by a short
    script that strips tags and keeps the MathJax source of formulas (about 15,700
    words with navigation and bibliography). Read: the preamble, all ten sections
    and their subsections (1.1–10.2), the bibliography with its annotations, Other
    Internet Resources and Related Entries. The four diagrams in section 4 are images
    and were not viewed; the text describes each. Nothing else skipped. The works
    the entry reports on (AGM 1985, Hansson 1999, Darwiche and Pearl 1997, Doyle
    1979 and others) were not read, so what it says they show is its account of
    them. Every quotation below was checked against the extracted text by script,
    with whitespace normalised.
date: '2026-10-15'
summary: >-
  The entry separates two ways of representing what an agent believes: a logically
  closed belief set, and a belief base whose elements are the beliefs "held independently
  of any other belief", with everything else "merely derived". Two bases with the
  same closure can respond differently to the same input (its Abe and Bob example),
  so the closure is not a sufficient state for revision; belief-set models recover
  the difference only by attaching a different selection mechanism to the same set.
  Bases avoid the Recovery postulate, keep distinct inconsistent states apart, and
  permit operations (external revision, semi-revision by consolidation) that collapse
  on closed sets. The entry does not discuss keeping reasons, sources or justification
  records: its only mention of truth maintenance systems is historical, and a base
  records which beliefs are basic, not why they are held. Iterated revision is treated
  as an open area in which most proposals carry an ordering of worlds or an entrenchment
  relation as the state, not a base.
---
<!-- inactive-ok-file: CLAIM-295 — Proposed; open claims and accounts cited as open, nothing here rests on their being settled -->

# NOTE-866: Hansson — Logic of Belief Revision (SEP, revision of 29 July 2026)

## Contribution

A survey, not a research paper. It sets out the AGM model (contraction,
expansion, revision; partial meet and entrenchment-based contraction;
Grove's spheres), the debate over Recovery, belief bases and their
operations, non-prioritized change, other operations (update, replacement,
multiple, indeterministic, relevance-sensitive, resource-bounded,
strength-changing), iterated change, alternative accounts (learning theory,
dynamic doxastic logic, descriptor revision) and Bayesian change. Results
are stated, not proved; the author's own work (belief bases, descriptor
revision, hyperreal probability) is prominent.

## Key insight

A set of current conclusions, closed under consequence, does not fix how
those conclusions should change. Which of them are held in their own right,
and which only because others are, decides what survives a contraction and
what a revision yields. The entry's term for this is that two bases can be
"statically equivalent" and not "dynamically equivalent".

## Assumptions

- **Beliefs are sentences** of a classical truth-functional language with a
  Tarskian consequence operator Cn (inclusion, monotony, iteration),
  supraclassical. "Sentences do not capture all aspects of belief, but they
  are the best general-purpose representation that is presently
  available."
- **Belief sets are closed**, which is "clearly an unrealistic
  idealization, since it means that the agent is taken to be “logically
  omniscient”". Following Levi, a belief set is what one "is committed to
  believe".
- **Models are input-assimilating**: "No explicit representation of time is
  included. Instead, the characteristic mathematical constituent is a
  function that, to each pair of a belief set and an input, assigns a new
  belief set."
- **Full belief only** in sections 1–9: "In formal models of belief change,
  the belief set represents the set of full beliefs. Uncertain beliefs are
  not represented in these models."
- Belief bases are in general "not (except as a limiting case) closed under
  logical consequence", and the base results cited are for finite bases.

## Key results

### Belief sets vs belief bases (section 5)

- **What bases keep.** "In the approaches discussed above, all beliefs in
  the belief set are treated equally in the sense that they are all taken
  seriously as beliefs in their own right. However, due to its logical
  closure the belief set contains many elements that are not worth taking
  seriously." A base's "elements represent beliefs that are held
  independently of any other belief or set of beliefs. Those elements of
  the belief set that are not in the belief base are “merely derived”,
  i.e., they have no independent standing."
- **Derived beliefs fall with their support.** "The underlying intuition is
  that the merely derived beliefs are not worth retaining for their own
  sake. If one of them loses the support that it had in basic beliefs,
  then it will be automatically discarded."
- **Bases carry more than their closure.** "one and the same belief set can
  be represented by different belief bases. In this sense, belief bases
  have more expressive power than belief sets." {p, q} and {p, p ↔ q} "have
  the same logical closure. They are therefore statically equivalent, in
  the sense of representing the same beliefs. On the other hand, the
  following example shows that they are not dynamically equivalent in the
  sense of behaving in the same way under operations of change. They can
  be taken to represent different ways of holding the same beliefs."
  Abe holds p and q as basic, Bob p and p ↔ q. Both revise by ¬p:
  "Abe believes that q whereas Bob believes that ¬q."
- **How belief-set models answer this.** "(In belief set models, cases like
  these are taken care of by assuming that although Abe’s and Bob’s belief
  states are represented by the same belief set, this belief set is
  associated with different selection mechanisms in the two cases. Abe has
  a selection mechanism that gives priority to q over p ↔ q, whereas Bob’s
  selection mechanism has the opposite priorities.)" The difference can be
  carried by an ordering attached to the closed set instead of by a base.
- **Inconsistent states.** "There is only one inconsistent belief set
  (logically closed inconsistent set), namely the whole language. On the
  other hand there are, in any non-trivial logic, many different
  inconsistent belief bases. Therefore, belief bases make it possible to
  distinguish between different inconsistent belief states." So
  consolidation (A! = A ÷ ⊥) has no counterpart for sets: "Once an
  inconsistent belief set has been obtained, all distinctions have been
  lost, and consolidation cannot restore them." Likewise external revision,
  (A +′ p) ÷ ¬p, "does not exist for belief sets", and semi-revision as
  (A +′ p)! "cannot be used for belief sets".
- **Not foundationalism vs coherentism.** "In belief revision theory it has
  mostly been taken for granted that belief sets correspond to a
  coherentist epistemology, whereas belief bases represent foundationalism
  (Fuhrmann 1991, Nayak 1994b). However, the logical relationships among
  the elements of a logically closed set do not adequately represent
  epistemic coherence." Coherentists "hardly mean this to apply to merely
  derived beliefs". "Therefore, the distinction between operations on
  belief bases and operations on belief sets should not be equated with
  that between foundationalism and coherentism."
- **Base-generated contraction on sets** (5.5) is characterised: an
  operation on a consistent belief set is generated by partial meet
  contraction on some finite base for it iff it satisfies Closure, Success,
  Inclusion, Vacuity, Extensionality, Finitude, Symmetry and
  Conservativity. Recovery is not among them.

### Recovery and contraction (sections 2.1, 2.3, 5.2)

- Recovery: K ⊆ (K ÷ p) + p. "According to Recovery, so much is retained
  after p has been removed that everything will be recovered by
  reinclusion (through expansion) of p." It is part of the AGM
  representation theorem for partial meet contraction on belief sets.
- "Recovery is the most debated postulate of belief change." The
  counterexamples (Cleopatra's children; George the criminal, mass murderer
  and shoplifter) are cases where what is reinstated should not bring back
  what came with it. Core-retainment, which looks weaker, implies Recovery
  for belief sets. Severe withdrawal avoids Recovery but is Expulsive. "The
  construction of a plausible operation of contraction for belief sets
  that does not satisfy Recovery is still an open issue."
- "Recovery does not hold for partial meet contraction of belief bases."
  Levi's coin: base {p_1, …, p_n, c, h} with h implying c. Contracting by c
  removes h; reinserting c gives Cn({p_1, …, p_n, c}), "which does not
  contain h, as desired." On the set, Recovery forces h back.
- Partial meet contraction on bases is characterised (Hansson 1999) by
  Success, Inclusion, Relevance and Uniformity. "The Relevance postulate
  has much the same function as Recovery has for belief sets, namely to
  prevent unnecessary losses of beliefs." Kernel contraction (removing at
  least one element of every minimal p-implying subset) generalises it.
- Descriptor revision (9.3) also fails Recovery: "Notably, the recovery
  postulate that creates problems in the AGM framework does not hold in
  the descriptor revision framework."

### Iterated revision (section 8, with 7.8 and 10)

- "The preceding sections have only dealt with changes of one and the same
  belief set or belief base. This is clearly a severe limitation."
- One AGM selection function can serve all belief sets once the definition
  of partial meet contraction is adjusted for the empty remainder set; the
  result is global contraction and revision that "does not impose any new
  properties on contraction or revision" (Hansson 2012).
- "However, most of the discussion on iterated change has been based on
  the assumption that such additional properties are plausible and indeed
  desirable." The Darwiche–Pearl postulates DP1–DP4 express "that when we
  revise by a sentence p, then the ordering among p-worlds should be
  unchanged, and so should the ordering among ¬p-worlds." "A large number
  of proposals for such shifts have been put forward, but opinions differ
  widely on the adequacy of these proposals."
- Nayak (1994a) and Fermé and Rott (2004) take the belief state to be an
  entrenchment ordering: "from an entrenchment ordering ≤ and such a
  generalized input a new entrenchment ordering ≤′ is obtained that
  contains the information needed to construct the new belief set."
- 7.8: "An operation of change can raise or lower the position of a
  sentence in an entrenchment ordering without affecting the belief set
  (but affecting how the belief state responds to new inputs)."
- Bayesian (10.1): conditioning on s gives p′(¬s) = 0, "and consequently
  p′ cannot be revised by ¬s". Dyadic probability (10.2) can remove a full
  belief once, but "did not provide us with a new dyadic probability
  function to replace P. Therefore, iterated belief change with this method
  is not possible."
- The entry does not say whether bases handle iteration better. Section 8
  speaks of "any belief set (belief base)" alike and gives no base-specific
  iterated result.

### Justifications, reasons, truth maintenance

- The only mention of truth maintenance is historical (1.1): "The truth
  maintenance systems developed by Jon Doyle (1979) were important in this
  development", the development being models of database updating. Doyle
  1979 is in the bibliography, unannotated. Doyle 2013 is cited only among
  models for resource-bounded agents (7.7).
- The entry never discusses recording why a belief is held, its source,
  its derivation or defeated alternatives. The base-level notion is binary:
  a sentence is basic ("held independently") or derived. The "support that
  it had in basic beliefs" is logical implication from the base, computed,
  not stored.
- Sources appear only as inputs: merge "can represent a process of
  conflict resolution through selective combination of information from
  two agents or sources" (6.4). Time appears only in update (Katsuno and
  Mendelzon's time-indexed sentences, 7.1) and in Governatori and Rotolo's
  legal model (7.9).
- 7.7 ties bases to bounded resources: "The use of finite belief bases
  (section 5) can be seen as a way to avoid the operations on infinite
  belief sets that are standard in AGM."

### Small faults in the text

- 2.1 refers to "Section 6.5" for operations that fail Success; there is no
  6.5 (shielded contraction is 6.3).
- 5.1 says "models such as AGM that use belief sets as representations of
  belief sets", evidently meaning "of belief states".

## Bearing on the record

**The words the record attributes to the entry are not in it.** The LIT
entry [LIT-1072](../literature.d/LIT-1072.md) says A10 cited it for the distinction "between belief
states represented as closed sets" and "belief bases retaining additional
structure". Neither phrase occurs in the revision of 29 July 2026. They are
A10's paraphrase, and a fair one. The entry's own words are "statically
equivalent" versus "dynamically equivalent", and beliefs "held
independently" versus "merely derived". The LIT summary ("keep the beliefs
held in their own right apart from their consequences") matches the entry.

**On [QUESTION-105](../questions.d/QUESTION-105.md): the entry gives the logical starting point the
question expects, and narrows what that point is.**

- It confirms that current conclusions underdetermine revision and names
  three things the closed set loses: which beliefs are basic (Abe and Bob),
  the difference between inconsistent states (consolidation), and the
  ability to contract without Recovery bringing back what rode on the
  retracted belief (Levi's coin).
- It also shows the same revision behaviour can be kept without a base, by
  a selection mechanism or entrenchment ordering attached to the closed set
  (the Abe and Bob parenthetical; 2.2; 7.8; Nayak and Fermé–Rott in 8). So
  the logic offers at least two retained states of different form, a base
  and an ordering, for the same family of single revisions. Which is
  smaller, or which an optimum resembles, is not addressed. For iterated
  revision the literature it reports mostly keeps an ordering, and "opinions
  differ widely" on how the ordering should shift.
- A base is not provenance, dependencies or defeated alternatives in the
  question's sense. It marks sentences as basic and recomputes everything
  else. It does not store what supports what, where a basic belief came
  from, or what was given up. The question's candidate structures are
  nearer to Doyle's truth maintenance systems, which the entry names once,
  historically, and does not discuss.
- The entry treats only full belief (and, in 10, credences). Its own
  Bayesian section shows a probability function can lose the ability to
  revise (p′(¬s) = 0, the dyadic case), which is the probabilistic face of
  the same problem.

**On [CLAIM-294](../claims.d/CLAIM-294.md): the entry gives a qualitative analogue, not support for
the probabilistic construction.** Abe and Bob agree on every belief and
revise by ¬p to opposite conclusions about q. That is the same
non-implication in full-belief logic, in a survey that attributes it to
standard belief-base theory. It does not check or bear on [CASE-093](../cases.d/CASE-093.md)'s
arithmetic, which is about marginals and conditionals. The entry's
parenthetical, that a belief-set model handles the case by a different
selection mechanism on the same set, parallels the claim's own caveat: a
richer current state (there the joint, here the ordering) suffices.

**On [CLAIM-295](../claims.d/CLAIM-295.md): consistent with the first half, silent on the
second.**

- Read with the parenthetical and 5.5, base structure is information a
  suitably equipped current state can also carry. That fits the claim's
  view that a record of history adds nothing for decisions a sufficient
  state covers; the entry does not frame it so.
- Where bases do better than sets, it is by widening the family of
  operations that remain well defined (inconsistent states, external
  revision, semi-revision, contraction without Recovery). That is close to
  the claim's "wider family of decisions", but it is an argument for a
  base, not for a record of justifications.
- 7.7 and the remark in 9.3 that remainders and possible worlds are
  "logically infinite (if the language is so), and therefore cognitively
  inaccessible" bear on the computational value the claim names: a finite
  base or a choice over outcomes is what a bounded agent can operate on.
  The entry asserts this; it gives no measure.
- Nothing here addresses justification graphs, sources, audit or option
  value, and nothing weighs storage against benefit.
