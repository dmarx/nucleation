---
status: Read
paper: LIT-tmp4mxqc
title: 'Simon — ill structured problems'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Read in full from a scan of the published article (Artificial
    Intelligence 4, 181–201), the open copy Unpaywall lists (gold,
    publishedVersion) at ojs.unbc.ca, fetched 2026-10-27, 21 pp. The text
    was extracted with `pdftotext -layout` and read whole: the abstract,
    §§1–5, the footnotes (the acknowledgement, footnote 1 on p. 185,
    footnote 2 on p. 195), Fig. 1 and its caption (p. 192), the two long
    quotations (Reitman, pp. 189–190; Murray, pp. 193–194), the fifteen
    references and the received dates (p. 201). Pages are the journal's.
    The OCR is imperfect ("~roblems", "WPSs", "Ding an ~'ich"). The
    quotations below were checked against page images rendered with
    `pdftoppm` where the OCR was doubtful: the "no WSPs, only ISPs"
    sentence (p. 186; the OCR's full stop after "WSPs" is a comma), "well
    structured in the small, but ill structured in the large" (p. 190),
    the heating-system figures (p. 190), the footnote marker on p. 185
    (the OCR's "?" is the superscript 1) and "Ding an sich" (p. 199). The
    rest is quoted from the extraction with its obvious character errors
    corrected. Fig. 1, which the extraction only partly recovers, was
    read from the page image (p. 192).
date: '2026-10-27'
summary: >-
  Simon argues that there is no real boundary between well and ill
  structured problems. Well-structuredness is judged by six conditions
  read as practicable, not in-principle, computability, so it is a
  relation between a problem and a bounded solver. On that reading even
  theorem proving and chess fail some conditions, chess is "well
  structured in the small" and ill structured "in the large", and "there
  are no WSPs, only ISPs that have been formalized for problem solvers"
  (p. 186). House design, a battleship's design by an organization and a
  robot in a real environment are handled by alternating a solver working
  on a locally well structured problem with a recognition and retrieval
  system that keeps modifying the problem space. Simon's conclusion is
  deflationary: ill structured problems may differ from well structured
  ones only in the size of the knowledge base, and need no qualitatively
  new mechanisms.
---
<!-- inactive-ok-file: CLAIM-tmpi1bjh CLAIM-tmpalzo4 CLAIM-184 CLAIM-tmpmx2ql CLAIM-419 THEORY-tmpq9x5h LIT-tmpikbhf LIT-tmpekh9l — Proposed, Deferred or Unavailable; the entries the reading bears on, cited as open -->

# NOTE-tmpy78q5: Simon — ill structured problems

## Contribution

A positive characterization of "ill structured problem" (ISP), which Simon
calls "a residual concept", defined by what it is not (§1, p. 181), and an
argument about artificial intelligence. Its aim is not to narrow the class
of ISPs: "I shall argue that many kinds of problems often treated as well
structured are better regarded as ill structured. Instead, I will try to
show that there is no real boundary between WSPs and ISPs, and no reason to
think that new and hitherto unknown types of problem solving processes are
needed to enable artificial intelligence systems to solve problems that are
ill structured" (p. 182). It continues Reitman's "ill defined problems" and
Newell's characterization of the ISP domain as the one where only weak
methods are available (p. 182).

## Key insight

The criteria for a well structured problem (WSP) "generally express a
relation between characteristics of a problem domain, on the one hand, and
the characteristics and power of an implicit or explicit problem solving
mechanism, on the other" (p. 182). Once "notions of computability in
principle be replaced by notions of practicable computability in the
definition of WSP" (p. 197), a problem with a large base of potentially
relevant knowledge will appear ill structured to a serial solver, because
only a small part of that knowledge can bear on its processing in any
short interval. The solver copes by working on a well structured problem at
each moment while a recognition system changes which problem that is.

## Assumptions

- **The solver is serial.** Its processes take "a few arguments as inputs
  and [produce] a small number of symbol structures as outputs. There is no
  way in which a large amount of information can be brought to bear upon
  these processes locally" (p. 192). Everything in §3.6 rests on this.
- **Practicable, not in-principle, computability** is the standard
  throughout. Footnote 1 (p. 185): "Notice that we are not appealing here to
  formal undecidability or incompleteness. Our concern throughout is with
  effective or practicable solvability using reasonable amounts of
  computation."
- **Long-term memory is large and its format is the designer's.** Retrieval
  from it "should not create particular difficulties of assimilation" (p.
  198), an assumption Simon flags: "This does not mean that we have had
  much actual experience in constructing and using such semantic
  information stores. Perhaps, when we come to have such experience,
  difficulties will emerge that cannot now be anticipated" (p. 198).
- **The design examples are described, not run.** The architect's process
  is a "general scheme" we "can imagine" (p. 189); the chess program of §3.5
  is "(over-simplified)" and hypothetical, with the convergence of its
  dynamic evaluation assumed "without specifying exact mechanisms" (p. 196).

## Key results

### The six conditions for a WSP (§2, p. 183)

A problem "may be regarded as well structured to the extent that it has
some or all of" these: (1) a definite criterion for testing a proposed
solution and a mechanizable process for applying it; (2) at least one
problem space representing the initial state, the goal state and all states
reachable or considered; (3) attainable state changes (legal moves)
representable as transitions, and also "considerable moves, whether legal or
not"; (4) "Any knowledge that the problem solver can acquire about the
problem can be represented in one or more problem spaces"; (5) where the
problem acts on the world, state changes "reflect with complete accuracy …
the laws (laws of nature) that govern the external world"; (6) all of these
hold "in the strong sense that the basic processes postulated require only
practicable amounts of computation". Simon calls them "not entirely
definite", and the vagueness reflects "the continuum of degrees of
definiteness between the well structured and ill structured ends of the
problem spectrum" (p. 183). It is "impossible to construct a formal
definition" (p. 182). The GPS input requirements (five items, pp. 183–184)
correspond to conditions 1–4.

### Theorem proving fails condition 4 for some solvers (§2.2, pp. 184–185)

Restricting the space to wffs excludes considering non-wffs; considerable
moves (working backwards from unproved wffs) are not fixed by legal ones;
and nothing excludes "metalinguistic knowledge, knowledge expressed in a
model space, or even analogical or metaphorical knowledge" (p. 184). If the
solver may not introduce "new resources that "occur" to him in the course
of his solution efforts", then "a problem that admits restructuring through
the introduction of such new resources would be an ill structured problem"
(p. 185). So "under a literal interpretation of Condition 4, problems of
discovering proofs in formal logic are not, for all problem solvers, well
structured" (p. 185). Ingenuity "generally requires violating Condition 4"
(p. 185).

### Chess: well structured in the small, ill structured in the large (§2.3, pp. 185–186)

"Best move" is well defined in principle but in practice is replaced by
maximizing an approximate evaluation function (p. 186). The real move
differs from moves in analysis "by its irrevocability", and "Playing a game
of chess—viewing this activity as solving a single problem—involves
continually redefining what the problem is. Even if we regard chess playing
as a WSP in the small (i.e., during the course of considering a single
move), by most criteria it must be regarded as an ISP in the large" (p. 186).

### The elusiveness of structure (§2.4, pp. 186–187)

"Definiteness of problem structure is largely an illusion that arises when
we systematically confound the idealized problem that is presented to an
idealized (and unlimitedly powerful) problem solver with the actual problem
that is to be attacked by a problem solver with limited (even if large)
computational capacities." Then: "In general, the problems presented to
problem solvers by the world are best regarded as ISPs. They become WSPs only
in the process of being prepared for the problem solvers. It is not
exaggerating much to say that there are no WSPs, only ISPs that have been
formalized for problem solvers" (p. 186; checked against the page image).

AI's "standard posture" has been to consider only idealized problems, "and
to leave the quality of the approximation, and the processes for
formulating that approximation to informal discussion outside the scopes
both of the theory and of the problem solving programs" (p. 186). That
"encourages allegations that the "real" problem solving activity occurs
while providing a problem with structure" (p. 187). Simon rejects the
strong form, quoting Newell and Simon (*Human Problem Solving*, p. 850, fn.
20): if it were correct, "and tasks from the same environment were presented
sequentially to a subject, only the first of them would present him with a
problem, since he would not need to determine a new problem space and
program for the subsequent tasks". He grants the weak form: "Nevertheless,
there is merit to the claim that much problem solving effort is directed at
structuring problems, and only a fraction of it at solving problems once
they are structured" (p. 187).

### House design and the architect's processes (§§3.1–3.2, pp. 187–191)

- The architect's task is ill structured only "if the architect is trying to
  be "creative"—if he does not begin the task by taking off his shelf one of
  a set of standard house designs" (p. 187). It lacks conditions 1–5: no
  initial criterion, and no problem space that could not "find its
  boundaries breached by the intrusion of new alternatives" (p. 188).
  Models and renderings stand in for condition 5 and still fail it (Wright's
  leaking roofs, the Seagram Building's change of colour; p. 188).
- Even if the space is in principle what memory and the library hold, some
  of it "only shows up in late stages … and some of it shows up … almost
  accidentally. Hence, the problem is even less well defined when considered
  from the standpoint of what is actually known at any point in time than
  when considered from the standpoint of what is knowable, eventually and in
  principle" (p. 188).
- Following Reitman's fugue protocol: few constraints are given; "the main
  initial constraint, and it is an open constraint at that …, is that the
  end product be a fugue. All other constraints are in a sense
  supplementary, generated from one transformation of the problem to the
  next" (Reitman, quoted p. 189). The task evokes attributes to specify, an
  executive program, requirements (the heating system's 70° and −5°,
  p. 190) and generators of alternatives, component by component. "During
  any given short period of time, the architect will find himself working on
  a problem which, perhaps beginning in an ill structured state, soon
  converts itself through evocation from memory into a well structured
  problem … the problem is well structured in the small, but ill structured
  in the large" (p. 190; checked against the page image).
- **Coordination** (§3.2.2, p. 191): the final product "may violate some of
  the requirements that were imposed (and temporarily satisfied) at an
  earlier stage", and some criteria "simply remain dormant, never having been
  evoked". Skill lies partly in dividing the task into components "as nearly
  "self-contained" as possible" (citing Alexander), and in early global
  parameters that "become constraints operating on each of the components".
  "The final product may be very much influenced by the order in which the
  design steps are taken up", so style can come "as readily from the
  organization of the design process as from explicit decisions" (p. 191).

### The architecture: a GPS plus a noticing and evoking mechanism (§3.2.3, pp. 191–193)

A GPS "which at any given moment finds itself working on some well
structured subproblem, with a retrieval system, which continually modifies
the problem space by evoking from long-term memory, new constraints, new
subgoals, and new generators for design alternatives" (pp. 191–192); the
retrieval system can interrupt the solver. Fig. 1's caption: "It shows the
alternation between a problem solver working on a well structured problem,
and a recognition system continually modifying the problem space" (p. 192). In the drawing (read
from the page image) the problem solver and a "noticing & evoking
mechanism" sit on either side of one block divided by a dashed line into
the external environment above and long-term memory below, with the
"immediate problem space (goals; constraints; specifications; & alternative
generators)" beneath it; both the solver and the mechanism have arrows into
the immediate problem space, so the external world and memory enter it by
the same route.
Why not assemble all relevant information "once and for all at the outset"?
"One must ask "bringing it together where?"" Retrieval would still be
needed, and to an observer the shifting attention "would still look like a
series of transformations of the problem space" (pp. 192–193). So "there is
no need for this initial definition of the problem space and task
structure" (p. 193).

### Battleship design by an organization (§3.3, pp. 193–194)

Sir Oswyn Murray's 1923 account (quoted at length) of designing a
battleship: general requirements from the Sea Lords, provisional schemes,
departments called in in turn, and a final stage where "requirements
overlap, and that the best possible cannot be achieved in regard to numbers
of points", settled by round-table compromise (pp. 193–194). Simon reads the
evoking as organizational and long-term memory as "literally a distributed
memory, divided among the various groups of experts" (p. 194). "Each small
phase of the activity appears to be quite well structured, but the overall
process meets none of the criteria we set down for WSPs" (p. 194).

### A robot in a real environment (§3.4, p. 195)

Its internal representation must abstract and cannot predict effects
exactly, so new information keeps arriving. "The problem representation can
be revised continually … so that the problem solver is faced at each moment
with a well structured problem, but one that changes from moment to moment"
(p. 195). Short-term reversible revision is "adaptation" or "feedback";
"more or less permanent (e.g., revising the "laws of nature")" revision is
"learning" (p. 195). Footnote 2: Winograd's system is not a robot in this
sense, since PLANNER is given "a complete and accurate characterization of
the toy world of blocks" (p. 195).

### Chess as an ISP (§3.5, p. 196)

A program of productions (a discrimination net that evokes moves), an
evaluator and an updater. Taking the subspace of features actually evoked as
"the effective problem space", it changes through the game, "moving from one
subspace to another of the large space defined by the entire contents of
long-term memory". "The problem faced by the chess program will appear just
as ill structured as the architect's problem or the robot's problem—and for
exactly the same reasons" (p. 196).

### The thesis (§3.6, p. 197)

"Any problem solving process will appear ill structured if the problem
solver is a machine that has access to a very large long-term memory (an
effectively infinite memory) of potentially relevant information, and/or
access to a very large external memory that provides information about the
actual real-world consequences of problem-solving actions." "Large" is
"relative to the amount of information that can direct or affect the
behavior of the processor over any short period of time". It "suggests that
there may be nothing other than the size of the knowledge base to
distinguish ISPs from WSPs", and that mechanisms that handle large,
apparently well structured domains "should be extendable to ill structured
domains without any need for introducing qualitatively new components"
(p. 197).

### Assimilating new information (§4, pp. 197–199)

Three sources: long-term memory (easiest, since its format is designed:
"Interfacing with an environment whose design is under our control (memory
search) is always several orders of magnitude easier than interfacing with
a given external environment (perception)", p. 198); instructions (Hayes and
Simon's program "carries out the major steps in translating relatively
simple ISPs into WSPs", p. 198); and the external world. Of the last two:
the interaction with stored programs and data "is both a vital aid to, and a
limitation upon, the understanding process … it tends to mold all new
information to the paradigms that are already available. The problem solver
never perceives the Ding an sich … Hence the acquisition process exercises a
strong influence in the direction of conserving existing problem
formulations. The world as perceived is better structured than the raw world
outside" (p. 199).

### Implications for AI (§5, pp. 199–200)

Existing programs have handled ill structured aspects "unknowingly", like
Molière's hero: the NSS chess program's feature-triggered move generators,
and GPS planning in an abstracted space whose plan is then tested in the
original space (pp. 199–200). What is missing is "a very large long-term
memory of potentially evocable information that can be used to bring about
repeated modifications in the problem space" (p. 200). Close: "The boundary
between well structured and ill structured problem solving is indeed a vague
and fluid boundary. There appears to be no reason to suppose that concepts
as yet uninvented and unknown stand between us and the fuller exploration of
those problem domains that are most obviously and visibly ill structured"
(p. 200).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | No formal definition of WSP is possible; the criteria are relative to the solver's power | strong, as conceptual analysis | follows from reading condition 6 as practicable computation (pp. 182–183, 197); a definitional argument, not a result |
| C2 | Theorem proving and chess, the standard WSPs, fail some conditions | strong | §§2.2–2.3 work through conditions 1–6 for each (pp. 184–186) |
| C3 | Problems from the world become WSPs only by being prepared for the solver; "there are no WSPs, only ISPs that have been formalized" | moderate | an argued generalization from two examples, hedged ("not exaggerating much", p. 186) |
| C4 | Much problem solving effort goes to structuring problems, but the "real" problem solving is not only in structuring | moderate | the second half by the Newell–Simon sequential-tasks argument (p. 187); the first half granted without evidence |
| C5 | Ill structured design is handled by alternating a locally well structured solver with a recognition system that modifies the problem space | moderate | described for the architect, matched to Murray's account of ship design and to the NSS chess program (pp. 189–196, 199); not implemented or tested here |
| C6 | The alternation is forced by seriality: assembling everything at the outset gains nothing | moderate | an argument from a serial processor (pp. 192–193); its force depends on that assumption |
| C7 | Nothing but knowledge-base size may separate ISPs from WSPs; no qualitatively new mechanisms are needed | weak | stated as what the analysis "suggests" (p. 197) and as "reason to be optimistic" (p. 200); no test |
| C8 | Assimilation conserves existing problem formulations; "the world as perceived is better structured than the raw world" | moderate | argued from fitting new data to existing formats (p. 199); no evidence offered |

## Concepts

- **ISP / WSP** — the paper's abbreviations. WSP: a problem having "some or
  all" of the six conditions, "to the extent" it has them (p. 183), so a
  matter of degree. ISP: initially a residual, "a problem whose structure
  lacks definition in some respect" (p. 181).
- **Problem space** — where initial, goal and intermediate states are
  represented (condition 2). The **effective problem space** is the part
  actually evoked over a short period (p. 196).
- **Considerable moves** — transitions the solver may consider, legal or not;
  distinct from legal moves (p. 183).
- **Open constraint** — Reitman's term, a constraint "incompletely
  specified", like "that the end product be a fugue" (p. 189).
- **Evoking / noticing and evoking mechanism** — recognition of a feature of
  the current problem space or external memory that retrieves information
  and adds it to (or substitutes it in) the space (pp. 192–193, Fig. 1).
- **Well structured in the small, ill structured in the large** — the
  paper's recurrent formula for chess and design (pp. 186, 190).
- **Adaptation vs. learning** — reversible against more or less permanent
  revision of the problem representation (p. 195).

## Connections

- **Reitman** (refs. [10, 11]): ill defined problems, open constraints, the
  fugue protocol (Cognition and Thought, ch. 8), which Simon follows "quite
  closely" (p. 189).
- **Newell** (ref. [6]): ISPs as the domain of weak methods (p. 182).
- **Newell and Simon, *Human Problem Solving*** (ref. [7]): the
  sequential-tasks argument (p. 187).
- **Alexander, *Notes on the Synthesis of Form*** (ref. [1]): decomposing a
  design into nearly self-contained components (p. 191). The near-decomposability
  theme is the one the record holds as Simon–Ando (LIT-1241).
- **Simon, "Style in design"** (ref. [13]): order of design steps and style
  (p. 191).
- **Murray 1923** (ref. [5]): the battleship account (pp. 193–194).
- **Hayes and Simon** (ref. [2]): a program translating problem instructions
  into GPS input (p. 198).
- **Winograd** (ref. [15]): the contrast case of a given, complete world
  model (fn. 2, p. 195).
- The record holds none of these as LITs except the Simon–Ando entry.

## Bearing on the record

- **CLAIM-tmpi1bjh: support, with two qualifications.** The registration and
  A17 §3 cite the paper for "The representation of the problem is itself part
  of the work, rather than something handed to the reasoner for free." The
  paper supports that in its own terms: problems "become WSPs only in the
  process of being prepared for the problem solvers" (p. 186), and AI's
  standard posture leaves "the processes for formulating that approximation"
  outside "the scopes both of the theory and of the problem solving programs"
  (p. 186), which is A17's complaint against making the most important
  operation free, made in 1973 of AI. Two of the claim's consequences have
  textual support. Amortization: the Newell–Simon footnote's point is that
  once a problem space is determined for a task environment, later tasks
  from it need no new one (p. 187), and the architect's shelf of standard
  designs removes the ill-structuredness (p. 187). Entrenchment: the
  acquisition process "exercises a strong influence in the direction of
  conserving existing problem formulations" (p. 199), and early global
  parameters and the order of design steps shape the final product (p. 191).
  The qualifications: (1) Simon rejects the strong form, that the "real"
  problem solving is the structuring (p. 187), granting only that "much"
  effort goes to it; (2) he does not treat formulation as a stage that comes
  before solving. In his model the problem space is never fixed at the outset
  and is modified throughout by the same retrieval machinery (pp. 191–193),
  and he argues that defining it at the outset would gain nothing for a
  serial solver (pp. 192–193). His bound is on how much of what is known can
  bear on processing at once (p. 197), not on time to formulate as such. The
  paper speaks of problems and problem spaces, not of questions or inquiry;
  carrying it to askable questions is the record's step.
- **CLAIM-tmpalzo4: a partial case of the last clause, and a pull towards
  defeater (a).** The paper has a process that changes what counts as a
  considered alternative and as a test while solving: in chess "continually
  redefining what the problem is" (p. 186); in design, requirements evoked
  late, earlier ones violated, and some never evoked (pp. 190–191); in the
  robot, revising its "laws of nature" as "learning" (p. 195). That bears on
  the reflexive operation the claim takes from A16 ("Evaluate or revise ℛ"):
  the solution criterion, condition 1, is itself built up during the process.
  But most of Simon's revision is selection: what enters the problem space
  is "generated from, or dredged from, his resources of memory or his
  reference library" (p. 188), and the effective space moves "from one
  subspace to another of the large space defined by the entire contents of
  long-term memory" (p. 196). That is close to the claim's defeater (a),
  reformulation as a choice among distinctions already admitted, with the
  admitting done by memory rather than by the current specification. It is
  refinement within a framework (the CEGAR-like case, LIT-tmpikbhf), except
  for the robot's "learning" and the possibility, which Simon raises and does
  not develop, of new resources that "occur" to the solver (p. 185). Simon
  does not treat inquiry, and Dewey (LIT-tmpekh9l) is not cited.
- **TERM-065: the query family and the tolerance arrive during solving.** In
  Simon's design process the tests a solution must meet are evoked as the
  design proceeds and "need not be specified in advance" (p. 190), and the
  final product may fail tests imposed earlier (p. 191). That is a case of
  the regime's 𝒬 and ε being outputs of the process, as CLAIM-tmpi1bjh says;
  it does not touch TERM-065's reason for fixing the regime during a
  comparison.
- **CLAIM-184 (anchors entrench):** a design case. Early global parameters
  "become constraints operating on each of the components", and the order of
  steps can fix the style of the result (p. 191). Consistent with the claim;
  described, not measured.
- **CLAIM-tmpmx2ql (scale separation makes constraints):** the adaptation
  and learning distinction (p. 195) separates fast reversible revision of a
  representation from slow permanent revision, and the standard design on
  the shelf is a slow product used as fixed by a fast process (p. 187).
  Consistent; no more.
- **CLAIM-419 (the record's grammar, fixed but amendable):** Simon's
  alternation is a model for a record that works on a fixed schema in the
  small and amends it in the large; his §4 point that new information is
  fitted to existing formats (p. 199) is the hazard the claim's last clause
  ("whether every such move is caught is not shown") leaves open.
- **LIT-1071 (resource-rational analysis):** Simon's bound is seriality and
  practicable computation, not an optimality criterion; the paper does not
  price structuring against solving.
- **No instruction for machine-learning practice.** The paper's conclusions
  are about AI architecture in 1973 and are not ML practice in the
  anthology's sense.

## Limitations

- **A position paper.** Nothing is implemented or measured. The architect's
  process is imagined, the chess program hypothetical, and the battleship
  account a 1923 administrator's description (pp. 189, 193, 196).
- **The deflationary conclusion is a suggestion.** "May be nothing other
  than the size of the knowledge base" (p. 197) and "reason to be
  optimistic" (p. 200) are hedged by Simon himself, and §4 sets aside both
  natural-language understanding and perception, the two sources of
  information he calls hard (pp. 198–199).
- **The seriality premise carries the architecture.** The argument against
  assembling the problem space at the outset (pp. 192–193) is for a serial
  processor; the paper does not consider a parallel one.
- **"Ill structured" slides between a property of the problem and how it
  "will appear"** to a solver (p. 197). Simon embraces the relativity, but
  it leaves open whether anything is ill structured for every solver; the
  hedged "there are no WSPs" (p. 186) answers it only for problems "presented
  … by the world".
- **Scan quality.** The text is OCR of a scan; quotations were corrected
  from the page images where doubtful (see history).

## Open questions

- Is there a class of problems that stays ill structured for a solver with
  unbounded parallel access to its memory, so that something other than
  knowledge-base size separates ISPs from WSPs (p. 197)?
- Where does a new resource that "occurs" to a solver (p. 185) come from, if
  every evoked element is dredged from memory (p. 188)? The paper does not
  reconcile the two.
- How much problem solving effort goes to structuring, measured? Simon grants
  "much" (p. 187) without a figure.
