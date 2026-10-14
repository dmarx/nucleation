---
number: 727
status: Read
formerly:
- NOTE-tmp88qyc
paper: 'LIT-1027'
title: 'Rubin, Roli, Stano & Damiano — Genealogies of organizational closure'
version: 1
history:
- version: 1
  date: '2026-10-13'
  note: >-
    Read in full from the publisher's typeset PDF (Frontiers, open access
    under CC BY, 20 pp.), fetched from
    frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2026.1806435/pdf.
    Text extracted with pdftotext; the two-column layout comes out
    interleaved in places, and Tables 2 and 3 come out scrambled, so
    they were read from the column fragments and are paraphrased, not
    quoted. Read: the whole text, all 35 footnotes, the three tables and
    the two figure captions. The reference list was consulted for
    attributions only. None of the primary works the paper reconstructs
    (Rosen, Maturana and Varela, Varela 1979) was read, so what it says
    they claim is its account of them. Every quotation below was checked
    against the extracted text by script, with whitespace and line-end
    hyphenation normalised.
date: '2026-10-13'
summary: >-
  A conceptual genealogy of the notions of closure (closure to information,
  cyclic, operational, semantic, catalytic, metabolic, closure to efficient
  causation, closure of constraints) from mathematical logic, cybernetics,
  systems theory, thermodynamics, relational biology and the biology of
  cognition. Its thesis is that closure is best read as a circular
  organization of efficient causes by which a living system produces the
  conditions of its own existence. That is not feedback, self-organization
  or a catalytic cycle, and it cannot be exhaustively characterized as a
  state-determined syntactic procedure. Current AI, agentic LLM systems
  included, is said to approximate closure without instantiating it. The
  genealogy is historical; the non-computability and AI verdicts are
  asserted or argued from Rosen, not demonstrated.
---
<!-- inactive-ok-file: CLAIM-284 CLAIM-288 CLAIM-194 THEORY-072 THEORY-071 — Proposed; open claims and accounts this reading bears on, nothing here rests on their being settled -->
<!-- inactive-ok-file: LIT-536 — Unavailable; Biological Autonomy, named as the source of the closure-of-constraints account, not leaned on -->

# NOTE-727: Rubin, Roli, Stano & Damiano — Genealogies of organizational closure

## Contribution

A map of where the many notions of "closure" in theories of autonomy came
from, and a classification of them (Table 3) by what is closed, what kind
of circularity, what causal regime, whether it is material, whether it is
computable, where semantics sits, and what it explains. On that map the
authors rest an interpretive thesis: closure, properly so called, is a
circular organization of efficient causes, and it is not captured by any
state-determined syntactic description. They apply the thesis to current
AI and conclude that its loops are "engineered approximations of closure
rather than instances of organizational closure itself".

## Key insight

The same word names different things that close. Ashby closed information,
Maturana and Varela operations, Rosen efficient causes, Montévil and Mossio
constraints, Kauffman catalysts. In the authors' words, "each explicative
account apparently identifies a different “thing” that closes upon itself",
while "every closure theory attempts to solve the same problem: How can a
living system become the cause of the conditions required for its own
persistence?" A loop that only feeds a signal back, or a pattern that
persists only while a gradient is maintained from outside, answers a
different question.

## Assumptions

- **Genealogy as conceptual analysis.** Not "merely as a historical
  reconstruction of facts", but a mapping of origins to show how research
  programmes "progressively converged". The transition from logic to
  biology "is not deductive"; logic supplies precursors, not a theory.
- **A stipulated sense of "non-computable".** It "does not refer simply to
  practical computational limitations, computational complexity, or the
  impossibility of simulation". It means that closure "cannot be
  exhaustively characterized as a state-determined syntactic procedure in
  the sense inherited from the Church–Turing thesis".
- **A reading of the Church–Turing thesis.** "Within the interpretation
  adopted here", effective procedures "characterize physical phenomena
  insofar as they are non-self-referential and formally specifiable". The
  thesis is thereby read as a claim about natural systems, which is not
  the usual reading.
- **Rosen's relational biology taken as the strongest causal account.**
  The paper says it "does not seek to adjudicate these controversies or to
  provide a definitive assessment of Rosen’s formal claims", but its
  conclusions lean on them.

## Key results

- **Closure is not feedback (§3).** First-order cybernetics recast
  circular causality as a feedback mechanism taken from the governor:
  "Circular causality was thus equated with feedback loops". The BCL turn
  was to read circular causality as self-reference instead. Von Foerster
  called first-order cybernetics "rather unfascinating".
- **Order is not organization (§4).** Reaction–diffusion, Turing patterns
  and dissipative structures produce physical order. Organization is "the
  relations between components which define a system as a unity"
  (Maturana). Open systems are "necessary but insufficient" for Maturana
  and Piaget; Piaget's "cyclic closure" is the complement.
- **Regulation belongs to the observer, for Maturana and Varela (note
  17).** "for Maturana and Varela, regulation (and self-regulation in
  particular—a central piece of cybernetic terminology at the time)
  depends entirely on the observer and does not belong to the intrinsic
  organization of the living."
- **Self-reproducing automata are heteronomous (note 4).** "Their
  efficient causal structures execute preprogramed instructions and thus
  remain heteronomous". Rosen (1959) argued the von Neumann automaton is
  an inconsistent model of life, conflating efficient with material
  causes. Varela's 1974 autopoiesis model also had catalysts supplied from
  outside.
- **Rosen's (M, R)-systems (§6).** Metabolism M, repair R, and a
  replication map produced inside the system close the regress of
  catalysts. Rosen's theorem: "a material system is an organism if, and
  only if, it is closed to efficient causation". The authors add that the
  four Aristotelian causes are interchangeable within the structure.
  Protein folding is offered as a paradigm and as "essentially
  non-syntactic (non-algorithmic)"; AlphaFold's results are called
  statistical approximations.
- **A halting-problem argument (§6).** Mossio, Longo & Stewart (2009, not
  held; cited in the paper as "Mossio et al. (2009)", which is not
  [LIT-570](../literature.d/LIT-570.md)) gave a computable expression of closure to efficient
  causation. The authors reply that "if we enforce the requirement that
  every computation must terminate in a finite number of steps, the
  Mossio et al. (2009) model of closure-to-efficient causation collapses
  into uncomputability". Their own conclusion is conditional: "Rosen’s
  claim that (M, R)-systems are non-computable holds true if and only if
  computability is defined by halting algorithms", and "these conclusions
  remain provisional".
- **Three senses of non-computability (Table 1).** Not Turing-computable;
  not formally axiomatizable; not adequately modelled by classical
  computational cognitive science. Rosen's claims are said to concern the
  first two, enactivism mainly the third.
- **Convergence and its limits (§7).** Catalytic closure is "not the
  organizational closure found in autopoietic or (M, R)-systems", because
  catalysts are not produced by a closed network of efficient causes.
  Viability theory, with its kernel, "complements rather than replaces
  autopoiesis, closure-to-efficient causation, or closure of constraints":
  it asks under what conditions the system can continue, not how its
  causes are produced.
- **The AI verdict (§7).** In-context learning, agentic loops, persistent
  memory and RLHF "introduce forms of operational circularity and adaptive
  regulation". "Their feedback loops do not regenerate the constraints
  that make those loops possible, nor do they fabricate the conditions of
  their own continued existence. What recurs are information flows,
  policy updates, and state transitions, not the mutual production of the
  efficient causes that constitute the system as an autonomous unity."
  LLMs remain "computationally mediated heteronomy".
- **Detection (§7 and note 35).** "A robust understanding of closure—and
  the methods used to model it—must ultimately rely on the ability to
  detect when closure occurs" (after Chemero and Turvey). Note 35: "a
  degree of heteronomy is typically embedded within the design process
  itself", and "questions whether true organizational closure has been
  achieved frequently re-emerge when the analysis is shifted to
  descriptive levels other than those initially specified by the model."
- **Conclusion (§7 a–d).** Closure is "the circular entailment of
  efficient causes that fabricate and regenerate one another while
  maintaining their own boundary conditions". Such systems "actively
  conserve and re-establish the constraints that make their own
  continuation possible". "It provides a proposed necessary and sufficient
  criterion for distinguishing living from non-living systems."

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The notions of closure derive from distinct research programmes and differ in what they take to be closed | moderate | historical reconstruction from published sources and recollections; Table 3 |
| C2 | Closure is not feedback, self-organization, physical order or a catalytic cycle | moderate | conceptual distinctions drawn from the sources (Maturana, Rosen, Chemero and Turvey) |
| C3 | Closure is best read as a circular organization of efficient causes that produces the conditions of the system's own existence | weak to moderate | stated as an "interpretative thesis", supported by the convergence C1 traces |
| C4 | Closure cannot be exhaustively characterized as a state-determined syntactic procedure | weak | Rosen's arguments, reported and not assessed; a halting-problem argument the authors call provisional |
| C5 | Current AI, agentic LLM systems included, approximates closure without instantiating it | weak | asserted from C3: loops not regenerating their constraints; two neurolinguistic citations on grounding |
| C6 | Closure is a necessary and sufficient criterion of life | weak | stated in the conclusion, called "proposed" |

## Concepts

- **Organizational closure.** As the paper concludes, the circular
  entailment of efficient causes that produce and regenerate one another
  while maintaining their own boundary conditions; open to matter and
  energy, with the causal roles needed for persistence produced inside.
- **Closure to information** (Ashby). Systems "open to energy but closed
  to information and control"; a formalism over Shannon information, with
  no causal thesis.
- **Operational closure** (Maturana and Varela). A closed domain of
  relations of material production; the authors note the 1973 book does
  not use the word "closure".
- **Closure to efficient causation** (Rosen). Every efficient cause in the
  system is produced inside it; here the replication map.
- **Closure of constraints** (Montévil and Mossio). Mutual dependence among
  constraints, each produced by and productive of another.
- **Catalytic closure** (Kauffman). Every molecule is food or is made by
  reactions the set catalyses; not closure of efficient causes.
- **Heteronomy.** Organization specified from outside: by design,
  objectives, training or supplied catalysts.

## Connections

The paper reconstructs Ashby, von Foerster, Piaget, Maturana and Varela,
Rosen, Pattee, Kauffman, Letelier and Montévil and Mossio. In the record,
Montévil & Mossio (2015) is [LIT-582](../literature.d/LIT-582.md) and the organizational account of
function is [LIT-570](../literature.d/LIT-570.md); Moreno & Mossio's book is [LIT-536](../literature.d/LIT-536.md), unavailable.
Weber & Varela (2002, [LIT-1018](../literature.d/LIT-1018.md)) appears in note 29 as Varela's move to
"immanent teleology", lacking "a complete formalization of its
organizational basis". It cites Di Paolo et al. (2022) on structural
coupling and treats the free energy principle as a formalism for the
relational domain of autopoiesis, not for its constitution. Aubin's
viability theory, which the record holds through [THEORY-134](../theory.d/THEORY-134.md), is named
as a complement to closure accounts.

## Bearing on the record

**On [CLAIM-284](../claims.d/CLAIM-284.md) and [CLAIM-288](../claims.d/CLAIM-288.md).** The paper gives the thesis an
adversary sharper than the counter the record filed. [CLAIM-288](../claims.d/CLAIM-288.md) says a
simulation whose operators maximize objectives the modeller fixed has
borrowed its norms. The paper says the same of AI architectures, which
"remain fundamentally dependent on externally specified objectives,
training procedures, evaluation criteria, computational infrastructures,
and energy flows". It then goes further. Even a system that revises its
own policy is, on this account, not closed, because what recurs is
"information flows, policy updates, and state transitions, not the mutual
production of the efficient causes". So the route [CLAIM-288](../claims.d/CLAIM-288.md) leaves open,
operators whose objectives the organization produces and revises, would
not satisfy these authors either, unless the organization also produced
the substrate those processes run on. That is support for the counter and
a reason to think it cannot be answered inside a simulation. Whether
[CLAIM-284](../claims.d/CLAIM-284.md) needs closure in this material sense is the record's question,
not the paper's. Its "self" is organizational, and it does not say that
the processes must produce their own efficient causes.

**On [CLAIM-116](../claims.d/CLAIM-116.md).** The paper's distinction between feedback and closure, and
note 17's report that for Maturana and Varela regulation "depends entirely
on the observer", agree with the disclaimer that regulation does not make
an agent. But the paper goes the other way at the top. It follows
Maturana in equating life with mind and calls closure the basis of "the
continuity between life, mind, and organized agency". [CLAIM-116](../claims.d/CLAIM-116.md) lists
organizationally closed systems among those that regulate without
warranting a will. The two are not in contradiction, since mind and
cognition in Maturana's sense are not a will, but they are not saying the
same thing.

**On [QUESTION-086](../questions.d/QUESTION-086.md) and [CASE-076](../cases.d/CASE-076.md).** The paper offers no
intervention that tells a closed system from a matched heteronomous one.
It says detection is the condition of a robust understanding and leaves it
there. Note 35 is the case's complication stated by these authors: whether
closure has been achieved changes "when the analysis is shifted to
descriptive levels other than those initially specified by the model".

**On [THEORY-072](../theory.d/THEORY-072.md).** That account, following [LIT-570](../literature.d/LIT-570.md), grants a candle
flame closure and draws the line at differentiation. This paper's
efficient-cause closure would deny the flame closure in the first place:
"Unlike transient self-organizing processes that persist only while
external gradients are maintained, organizationally closed systems
actively conserve and re-establish the constraints". It does not discuss
differentiation or analyse a flame. The two place the same line by
different criteria, and neither has applied its criterion to both sides.

**On [THEORY-071](../theory.d/THEORY-071.md) and [CLAIM-194](../claims.d/CLAIM-194.md).** Consistent with both: closure is a
matter of production, not of coupling. It adds nothing that tells a
produced boundary from an imposed one by observation.

**Not ML practice.** The AI section is a verdict about what current
systems are, not an instruction for building them.

## Limitations

- The non-computability thesis rests on Rosen, whose arguments the paper
  reports and does not assess. The halting-problem argument is weak as
  given. That a non-terminating process has no halting output is a
  consequence of the definition chosen, and the undecidability of halting
  for arbitrary programs does not show that a particular model's closure
  cannot be computed. The authors make the conclusion conditional on the
  definition and call it provisional.
- The reading of the Church–Turing thesis as a thesis about natural
  systems is adopted, not argued.
- The protein-folding claim, that a folded shape "cannot be deduced or
  predicted" from sequence or landscape, is asserted. The paper's own
  evidence is that predictors rely on crystallographic data.
- The AI verdict is drawn from the definition, not from an analysis of
  any system. No architecture is examined against the criteria of Table 3.
- The "necessary and sufficient criterion" of life is stated in the
  conclusion without argument beyond the genealogy.
- Much of the history rests on participants' recollections.

## Open questions

- Can closure of efficient causes be detected in a system whose substrate
  is supplied, as every computational system's is? The paper's criterion
  seems to say no by definition. A criterion that admits degrees of
  closure relative to a level would make it an empirical question.
- Does the computational-heteronomy verdict survive a system whose
  objectives, evaluation criteria and constraints are all produced by its
  own processes, with only energy and hardware supplied? Organisms also
  have their energy supplied.
- Which notion of closure does the record need for [CLAIM-284](../claims.d/CLAIM-284.md): efficient
  causes, constraints, or operations? Table 3's criteria are a way to
  state the choice.
