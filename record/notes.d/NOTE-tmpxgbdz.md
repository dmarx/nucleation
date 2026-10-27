---
status: Read
paper: LIT-tmpikbhf
title: 'Clarke, Grumberg, Jha, Lu & Veith — Counterexample-guided abstraction refinement'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Read in full from the copy in Carnegie Mellon University's repository
    (KiltHub, doi:10.1184/r1/6604547, "In Copyright", listed by Unpaywall
    as green), downloaded 2026-10-27, 16 pp. It is the authors' manuscript
    of the CAV 2000 paper, not the technical report and not the J. ACM
    version: it carries no LNCS running heads or page numbers and is set
    on letter paper, its 16 pages match the published pp. 154–169, and it
    cites the technical report CMU-CS-00-103 as a separate document ([7],
    "our technical report") for the proof of Theorem 2 and the
    implementation details. Whether its wording is identical to the
    Springer text was not checked. The mathematics is set in Type 3 fonts
    that `pdftotext -layout` turns to noise, so p. 2 was read from the
    extraction and pp. 1 and 3–16 from page images rendered at 110 dpi.
    I read the abstract, §§1–7, Theorems 1–4, Lemmas 1–2, Examples 1–4,
    Figures 1–8, the table of §6, the funding footnote and the 23
    references. Pages below are the PDF's, counted from 1.
date: '2026-10-27'
summary: >-
  A model checker runs on an existential abstraction that merges concrete
  states, so a property true of the abstraction is true of the program
  (Theorem 1). An abstract counterexample is checked against the concrete
  system by image computation; if it has no concrete counterpart, the
  first abstract state where it breaks is split to separate the concrete
  states reachable along it from those with the transition onward, and
  checking runs again. The coarsest such split is stated to be NP-hard
  (proof omitted), so a polynomial, non-optimal split is used. For
  finite-state programs and ACTL* properties whose counterexamples are
  paths or loops, the loop ends in a real counterexample or a proof. The
  property is fixed throughout.
---
<!-- inactive-ok-file: CLAIM-tmpalzo4 CLAIM-tmpl228b CLAIM-419 CLAIM-181 — Proposed; the claims the reading bears on, cited as open -->

# NOTE-tmpxgbdz: Clarke, Grumberg, Jha, Lu & Veith — Counterexample-guided abstraction refinement

## Contribution

An automatic loop for model checking with abstraction: build an abstraction
from the program's own conditions, check the property on it, and when the
check fails, test whether the counterexample is real; if it is not, split
the abstract state where it breaks and check again (§3, p. 7). Abstraction
had been "typically a manual process, often requiring considerable
creativity" (p. 1). What is new against Kurshan's localization reduction,
which also refines from counterexamples, is the grain of the refinement:
abstraction functions over clusters of related variables, which "distinguish
many degrees of abstraction for each program variable" (abstract, p. 1),
where localization "either leaves a variable unchanged or replaces it by a
nondeterministic assignment" (p. 3). It adds symbolic (BDD) tests for
spurious path and loop counterexamples, a complexity result for the optimal
split, and an implementation in NuSMV that found an unreported bug in a
Fujitsu design that two other checkers could not handle (pp. 4, 15).

## Key insight

An abstraction that merges states can only add behaviour, so it can prove a
universal property but may refute it falsely. A false refutation is not
noise: it shows exactly where the merge went wrong. Walking the abstract
counterexample forward through the concrete system, the set of concrete
states that can follow it becomes empty at some first step. At the state
before that step, the merged class holds concrete states that the trace can
reach and concrete states that have the transition onward, and no concrete
state that is both. The abstraction asserted a path by joining the two; the
refinement is to stop joining them (§4.3, p. 11). The counterexample names
the distinction the abstraction lacked, and the concrete system certifies
that it was lacking.

## Assumptions

- **Finite state.** A program has variables v₁, …, vₙ, each with a finite
  domain D_{vᵢ}; the state space is D = D_{v₁} × ⋯ × D_{vₙ} (§2, p. 4).
  Each variable's next value is fixed by a transition block, an SMV-style
  case statement whose conditions C_i^j are predicates (Fig. 1, pp. 4–5).
- **ACTL\* specifications.** Properties are in ACTL\*, the fragment of CTL\*
  "which only allows universal quantification over paths" (p. 1).
- **Existential abstraction.** An abstraction is a surjection h: D → D̂,
  equivalently an equivalence relation, d ≡ e iff h(d) = h(e) (p. 5). The
  abstract structure M̂ has an initial abstract state where some concrete
  state mapping to it is initial, and a transition R̂(d̂₁, d̂₂) iff
  ∃d₁∃d₂(h(d₁) = d̂₁ ∧ h(d₂) = d̂₂ ∧ R(d₁, d₂)) (p. 5, items 1–4).
- **The abstraction respects the property's atoms.** An atomic formula f
  respects h if d ≡ d′ implies (d ⊨ f ⇔ d′ ⊨ f) (p. 5). Theorem 1 needs it,
  and §4.2 assumes it: "assume that φ respects h" (p. 8).
- **Product-form abstractions over variable clusters.** h = (h₁, …, h_m),
  one surjection per variable cluster, with ≡ the product of the components
  ≡ᵢ (pp. 6–7). Refinement keeps this form (p. 11).
- **Counterexamples that are paths or loops.** The procedure and its
  completeness are stated for these only (pp. 2, 8, 13). Extension to the
  "trace"-like counterexamples of a larger fragment of ACTL\* is future work
  (§7, p. 15).
- **The concrete transition relation can be imaged.** Spuriousness is
  decided by forward images under the concrete R, computed with OBDDs
  (p. 9). Where the full concrete relation is too large, §5 uses
  partitioned relations and approximations (pp. 13–14).

## Key results

### Soundness of the abstraction (§2, p. 5)

- **Theorem 1.** If the atomic subformulas of an ACTL\* specification φ
  respect h, then (i) every abstract label L̂(d̂) is consistent (all
  concrete states in h⁻¹(d̂) satisfy it) and (ii) M̂ ⊨ φ ⇒ M ⊨ φ. "On the
  other hand, if the abstract model invalidates an ACTL\* specification,
  i.e., M̂ ⊭ φ, the actual model may still satisfy the specification"
  (p. 5). No proof is given in this text.
- **Example 1** (p. 6, Fig. 2). A traffic light red → green → yellow → red
  and ψ = AG AF(state = red). With h(green) = h(yellow) = go, M ⊨ ψ but
  M̂ ⊭ ψ: the abstract trace ⟨red, go, go, …⟩ is "a spurious
  counterexample". Merging green and yellow created a self-loop on go that
  no concrete state has.
- **Why clusters.** With D = {0,1,2} × {0,1,2} and D̂ = {0,1} × {0,1} there
  are 4⁹ = 262144 functions h: D → D̂, but only 64 of the per-variable form
  (h₁, h₂) used in the earlier framework [10] (p. 6). The paper's
  abstractions are surjections on cluster domains D_{VCᵢ} = ∏_{v ∈ VCᵢ} D_v,
  "more general than the one used in [10]" (p. 6).

### The loop (§3, p. 7)

1. "Generate the initial abstraction" from the conditions of the transition
   blocks.
2. "Model-check the abstract structure." If M̂ ⊨ φ, conclude M ⊨ φ. If not,
   take the counterexample T̂ and ascertain whether it is "an actual
   counterexample … If T̂ turns out to be an actual counterexample, we
   report it to the user, otherwise T̂ is a spurious counterexample, and we
   proceed to step 3."
3. "Refine the abstraction: We refine the abstraction function h by
   partitioning a *single equivalence class* of ≡ so that after the
   refinement the abstract structure M̂ corresponding to the refined
   abstraction function does not admit the spurious counterexample T̂ …
   After refining the abstraction function, we return to step 2."

### The initial abstraction (§4.1, pp. 7–8)

- Atoms(P) is "the set of atomic formulas that appear in the specification
  or in the conditions of the transition blocks" (p. 5). Two atomic formulas
  interfere if they share a variable; the reflexive, transitive closure
  gives formula clusters FCᵢ and, from them, variable clusters VCᵢ (p. 7).
- hᵢ(d₁, …, d_k) = hᵢ(e₁, …, e_k) iff for all f ∈ FCᵢ, (d₁, …, d_k) ⊨ f ⇔
  (e₁, …, e_k) ⊨ f: "two values are in the same equivalence class if they
  cannot be "distinguished" by atomic formulas appearing in the formula
  cluster" (p. 8). So the first abstraction draws exactly the distinctions
  the program's conditions and the specification's atoms draw, and no
  others.
- **Example 2** (p. 8): x, y ∈ {0,1,2} and reset, with atoms reset = TRUE,
  x = y, x < y, y = 2. The cluster {x, y} gets five classes,
  0 = {(0,0),(1,1)}, 1 = {(0,1)}, 2 = {(0,2),(1,2)}, 3 = {(1,0),(2,0),(2,1)},
  4 = {(2,2)}; h₂ is the identity on reset.

### Is a counterexample spurious? (§4.2, pp. 8–11)

- **Paths.** For T̂ = ⟨ŝ₁, …, ŝₙ⟩, h⁻¹(T̂) is the set of concrete paths
  {⟨s₁, …, sₙ⟩ | ⋀ᵢ h(sᵢ) = ŝᵢ ∧ I(s₁) ∧ ⋀ᵢ R(sᵢ, sᵢ₊₁)} (p. 9). Set
  S₁ = h⁻¹(ŝ₁) ∩ I and Sᵢ := Img(Sᵢ₋₁, R) ∩ h⁻¹(ŝᵢ).
- **Lemma 1** (p. 9). Equivalent: (i) T̂ corresponds to a concrete
  counterexample; (ii) h⁻¹(T̂) is non-empty; (iii) Sᵢ ≠ ∅ for all
  1 ≤ i ≤ n. So a spurious path has a minimal i (2 ≤ i ≤ n) with Sᵢ = ∅,
  and **SplitPATH** (Fig. 4) returns it with S_prev = Sᵢ₋₁ (pp. 9–10).
- **Example 3** (p. 9, Fig. 3). D = {1, …, 12}, h(x) = ⌊(x − 1)/3⌋ + 1, so
  four abstract states {1,2,3}, {4,5,6}, {7,8,9}, {10,11,12}. For
  T̂ = ⟨1̂, 2̂, 3̂, 4̂⟩: S₁ = {1,2,3}, S₂ = {4,5,6}, S₃ = {9}, S₄ = ∅.
- **Loops** (p. 10, Fig. 5). For T̂ = ⟨ŝ₁, …, ŝᵢ⟩⟨ŝᵢ₊₁, …, ŝₙ⟩^ω, one
  abstract loop may match concrete loops of different sizes starting at
  different stages, and the unwinding becomes periodic only with period the
  least common multiple of their sizes, "in general *exponential*". The
  "surprising result": the number of unwindings needed is at most
  min = min_{i+1≤j≤n} |h⁻¹(ŝⱼ)|. **Theorem 2**: T̂ corresponds to a
  concrete counterexample iff h⁻¹_path(T̂_unwind) is non-empty, where
  T̂_unwind = ⟨ŝ₁, …, ŝᵢ⟩⟨ŝᵢ₊₁, …, ŝₙ⟩^min. The proof "is not immediate;
  for details, we refer to [7]" (p. 10). So the loop case reduces to the
  path case (**SplitLOOP**, p. 11).

### What refinement is (§4.3, pp. 11–12)

- At the failure index i, with Sᵢ ⊆ h⁻¹(ŝᵢ) reachable and
  Img(Sᵢ, R) ∩ h⁻¹(ŝᵢ₊₁) = ∅, h⁻¹(ŝᵢ) is cut into three (p. 11, Fig. 6):
  - S_{i,0} = Sᵢ, the states reachable along the trace;
  - S_{i,1} = {s ∈ h⁻¹(ŝᵢ) | ∃s′ ∈ h⁻¹(ŝᵢ₊₁). R(s, s′)}, states not
    reachable along it that have a transition into the next abstract state;
    it "cannot be empty" because the abstract transition exists;
  - S_{i,x} = h⁻¹(ŝᵢ) \ (S_{i,0} ∪ S_{i,1}), the rest.
  "Since S_{i,1} is not empty, there is a spurious transition ŝᵢ → ŝᵢ₊₁.
  This causes the spurious counterexample T̂. Hence in order to refine the
  abstraction h so that the new model does not allow T̂, we need a refined
  abstraction function which separates the two sets S_{i,0} and S_{i,1}"
  (p. 11). In Example 3, S_{3,0} = {9}, S_{3,1} = {7}, S_{3,x} = {8}.
- Formally, h⁻¹(ŝ) is a product E₁ × ⋯ × E_m of component classes, and a
  refinement ≡′ of ≡ is obtained by partitioning the Eⱼ, i.e. refining the
  component relations ≡ⱼ. "The *size of the refinement* is the number of
  new equivalence classes. Ideally, we would like to find the coarsest
  refinement that separates the two sets, i.e., the refinement with the
  smallest size" (p. 11).
- **Theorem 3** (p. 11). "(i) The problem of finding the coarsest
  refinement is NP-hard; (ii) when S_{i,x} = ∅, the problem can be solved in
  polynomial time." The hardness is by reduction from PARTITION INTO
  CLIQUES; "The proof is omitted due to space restrictions" (p. 11).
- **PolyRefine** (Fig. 7, p. 12). For each component j, start from ≡′ⱼ := ≡ⱼ
  and remove (a, b) whenever proj(S_{i,0}, j, a) ≠ proj(S_{i,0}, j, b),
  where proj(S_{i,0}, j, a) is the set of the other components of states in
  S_{i,0} whose jth component is a. Two values are split exactly when some
  state of S_{i,0} with one value becomes a state outside S_{i,0} with the
  other. **Lemma 2** (p. 12): when S_{i,x} = ∅, the result refines ≡ⱼ,
  separates S_{i,0} from S_{i,1}, and is "the coarsest refinement of ≡ⱼ".
  Symbolically the projection is a generalized cofactor (p. 12).
- **The heuristic used** (p. 12): merge S_{i,x} into S_{i,1} and run
  PolyRefine on S_{i,0} against S_{i,1} ∪ S_{i,x}. "The equivalence relation
  computed by PolyRefine in this manner is not optimal, but it is a correct
  refinement which separates S_{i,0} and S_{i,1}, and eliminates the
  spurious counterexample."

### Termination and completeness (pp. 2, 12–13)

- "Our refinement procedure continues to refine the abstraction function by
  partitioning equivalence classes until a real counterexample is found, or
  the ACTL\* property is verified. The partitioning procedure is guaranteed
  to terminate since each equivalence class must contain at least one
  element. Thus, our method is complete" (p. 12). Each refinement strictly
  splits a class of a finite domain, so the abstraction can be refined only
  finitely often; at worst it reaches the concrete model, where no
  counterexample is spurious. (The bound to the concrete model is my
  gloss of the one-sentence argument; the paper gives no bound on the
  number of iterations.)
- **Theorem 4** (p. 13). "Given a model M and an ACTL\* specification φ
  whose counterexample is either path or loop, our algorithm will find a
  model M̂ such that M̂ ⊨ φ ⇔ M ⊨ φ."
- In the introduction: "we are guaranteed to either find a valid
  counterexample or prove that the system satisfies the desired property.
  In principle, our methodology can be extended to all of ACTL\*" (p. 2).

### Engineering (§5, pp. 13–14)

- **Two-phase refinement.** Before splitting a spurious loop, check the
  property on the concrete states of the counterexample alone, S_local; in
  Fig. 8 a spurious ⟨1̂, 2̂⟩^ω covers a real path ⟨1, 1, …⟩. Slower when no
  real counterexample is found, often faster when one is (p. 13).
- **Approximation.** Early approximation (abstracting each transition block
  before conjoining) over-approximates M̂; a per-cluster heuristic chooses
  between it and exact abstraction, and "the overall method … remains
  complete with this approximation" (p. 14).
- **Distant variables** in the variable dependency graph are abstracted
  completely; unlike localization, refinement can then pass through
  "intermediate abstraction functions" (p. 14).

### Experiments (§6, pp. 14–15)

- NuSMV with CUDD, on a 200 MHz PentiumPro with 1 GB RAM. Five public
  benchmarks against NuSMV with cone-of-influence reduction (table, p. 14):

  | design | #Var | #Prop | COI time | COI \|TR\| | COI \|MC\| | ABS time | ABS \|TR\| | ABS \|MC\| |
  |---|---|---|---|---|---|---|---|---|
  | gigamax | 10(16) | 1 | 0.3 | 8346 | 1822 | 0.2 | 13151 | 816 |
  | guidance | 40(55) | 8 | 35 | 140409 | 30467 | 30 | 147823 | 10670 |
  | p-queue | 12(37) | 1 | 0.5 | 51651 | 1155 | 0.4 | 52472 | 1114 |
  | waterpress | 6(21) | 4 | 273 | 34838 | 129595 | 170 | 38715 | 3335 |
  | PCI bus | 50(89) | 10 | 2343 | 121803 | 926443 | 546 | 160129 | 350226 |

  The authors: one case uses "50% more memory" to build the transition
  relation (gigamax, 13151 against 8346), but model checking "requires one
  magnitude less memory" (pp. 14–15). By the table that holds for
  waterpress (3335 against 129595); for guidance and PCI bus the ratio is
  about 2.9 and 2.6, and for p-queue about 1.
- **Fujitsu MMA-ASIC** (p. 15): about 10,600 lines of Verilog after manual
  abstraction, about 500 registers, 9,500 lines of SMV. NuSMV with cone of
  influence and Yang's SMV "failed to verify the design". The method
  "abstracted 144 symbolic variables and with three refinement steps,
  successfully verified the design, and found a bug which has not been
  discovered before."

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | If an ACTL\* property's atoms respect h, the abstraction satisfying it implies the program does | strong | Theorem 1, p. 5; the standard existential-abstraction result of [8, 10], no proof here |
| C2 | A path counterexample is real iff the forward image sequence Sᵢ stays non-empty | strong | Lemma 1, p. 9; immediate from the definitions |
| C3 | A loop counterexample needs at most min_j \|h⁻¹(ŝⱼ)\| unwindings to decide | moderate | Theorem 2, p. 10; proof deferred to the technical report [7], not read |
| C4 | A spurious counterexample is removed by separating, at its first failing abstract state, the states reachable along it from those with the transition onward | strong | §4.3, p. 11, argued in full; PolyRefine and Lemma 2, p. 12 |
| C5 | Finding the coarsest such separation is NP-hard, and polynomial when S_{i,x} = ∅ | moderate | Theorem 3, p. 11: (i) proof omitted, the reduction only named; (ii) via Lemma 2, whose proof is also not given |
| C6 | The loop terminates with a real counterexample or a proof, for path or loop counterexamples | strong | finiteness argument, p. 12; Theorem 4, p. 13 |
| C7 | The method stays complete with early approximation and with the two-phase heuristic | weak | asserted, pp. 13–14; details in [7] |
| C8 | The method uses less memory in model checking than cone-of-influence reduction, by about an order of magnitude | weak | five benchmarks, p. 14; the order of magnitude holds for one of five |
| C9 | It found an unknown bug in an industrial design two other checkers could not handle | moderate | one case, p. 15; the bug is not described |

## Concepts

- **Abstraction** — a surjection h: D → D̂ from concrete to abstract states,
  or the equivalence relation it induces (p. 5).
- **Existential abstraction** — an abstract transition exists if some
  concrete transition between the merged classes exists (p. 5), so the
  abstraction has every concrete behaviour and possibly more.
- **Respects** — an atomic formula respects h if no class contains states
  that disagree on it (p. 5).
- **Spurious counterexample** — an abstract counterexample with no concrete
  counterpart (p. 6). Such techniques "are also known as false negative
  techniques" (p. 2).
- **Formula cluster, variable cluster** — classes of atomic formulas linked
  by shared variables, and the variables they use (p. 7).
- **Refinement** — a finer equivalence relation ≡′ ⊆ ≡, obtained by
  partitioning component classes; its **size** is the number of new classes,
  and the **coarsest** is the one of least size that separates S_{i,0}
  from S_{i,1} (p. 11). The paper writes "separation problem" for it in §7
  (p. 15).
- **Complete** — here: the procedure ends with a real counterexample or a
  proof that the property holds (p. 2). Not completeness of a logic.

## Connections

- **Clarke, Grumberg and Long** [10], *Model checking and abstraction*
  (TOPLAS 1994): the framework and the existential abstraction it extends
  from per-variable to per-cluster functions (pp. 2, 6).
- **Kurshan's localization reduction** [14] and **Balarin** [2, 15]: earlier
  counterexample-driven refinement that adds whole variables (p. 3).
- **Lind-Nielsen and Andersen** [17]: refinement with upper and lower
  approximations for all of CTL (p. 3). Lee, Pardo, Hachtel and Somenzi [16,
  18, 19]: CTL abstraction refinement not driven by counterexamples.
- **Govindaraju and Dill** [12]: also seeks the first spurious state, but
  extends by random choice and treats only safety and paths (p. 3).
- **Graf and Saidi** [13] and successors [11, 20]: predicate abstraction;
  here the atoms build an explicit abstraction function rather than an
  abstract transition system (p. 2).
- **The technical report** CMU-CS-00-103 [7], "Counterexample-guided
  abstraction refinement", holds Theorem 2's proof and the implementation
  details (pp. 10, 13). The J. ACM version (2003), named in the
  registration, is not cited here and was not read.

## Bearing on the record

- **CLAIM-tmpalzo4: the exchange's description holds, and its limit is
  exact; CEGAR is a worked case of refinement within a fixed answer space,
  not of revising it.** A16 §6's four steps are the paper's §3 (p. 7):
  merged states, a counterexample, a check against the concrete system,
  a split, and again. Three things the reading adds. (1) The property does
  more than wait to be checked. Its atoms are in Atoms(P), from which the
  first abstraction is built (pp. 5, 7–8), and every abstraction must
  respect them (Theorem 1, p. 5; "assume that φ respects h", p. 8). So the
  question fixes which differences may never be merged, which is the
  claim's first part made formal for this case. (2) The limit A16 gave is
  stronger than "does not automatically recognize". The procedure has no
  operation on φ or on M at all. A real counterexample ends it: "we report
  it to the user and stop" (p. 2). (3) Every refinement is a split toward
  the concrete model, and termination rests on that: the finer
  abstractions all lie between the first one and the concrete state space
  (p. 12). Each refinement is "a choice among distinctions its earlier
  specification already admitted", which is the shape of the claim's
  defeater (a). CEGAR therefore supports the claim's first two parts by
  analogy and bounds its last clause. Revising what an answer could be is
  exactly what it does not do (THEORY-tmpz87qo).
- **CLAIM-419 (luria's DP-016 in this record): the pattern matches, and two
  disanalogies are worth keeping.** The match: a failure under a fixed
  specification is read as the abstraction's fault, located, and answered
  by a split that removes it (pp. 7, 11). A spurious counterexample is the
  abstraction asserting a behaviour the system lacks, as in CASE-131 the
  grammar "asserted an inference nobody made". First disanalogy: in CEGAR
  the misfit is certified. Lemma 1 decides spuriousness against the
  concrete system, and §4.3 computes the distinction that was missing
  (S_{i,0} against S_{i,1}). The record has no concrete model to image
  against, and CLAIM-419's own limit, that a move silently forced into a
  wrong shape leaves no trace, has no counterpart in CEGAR: there, every
  wrong merge that matters to φ eventually shows up as a spurious
  counterexample. Second disanalogy: CEGAR only splits. Luria's
  amendments include adding relations (ADR-044's `corroborates`) and
  fields (ADR-043's `warrant`), which are not splits of a class. Of
  CLAIM-419's five, only a split of a conflated relation fits the
  algorithm. The anti-ad-hoc constraint that CLAIM-419 takes from A18 has a
  formal neighbour here: the paper wants the coarsest split that removes
  the counterexample, and finds that it is NP-hard in general (Theorem 3,
  p. 11). The least amendment that answers a misfit can be hard to find
  even when the misfit is certified.
- **CLAIM-tmpl228b.** A7's formalization, Obj(A_t, D_t) ≠ Obj(A_{t+1}, D_t),
  has its exact counterpart here: the same concrete M under a refined h
  yields a different abstract structure M̂ and different abstract states
  (p. 5). But the concrete states are individuated before any abstraction
  and independently of it (§2, p. 4). In CEGAR the apparatus constitutes
  only the abstract objects. That is the part of CLAIM-tmpl228b that A7
  called demonstrable, and the paper offers no support beyond it.
- **CLAIM-181.** CEGAR's grammar (the abstraction) is fixed at each step and
  amended on misfit, and the misfit that drives it is always detected,
  since the check is exhaustive and finite. It is a case where a move the
  grammar cannot hold is never lost. That depends on a concrete model and a
  decidable check, which an argument record does not have.
- **No instruction for machine-learning practice.** The paper is formal
  verification of hardware designs.

## Limitations

- **Proofs not in this text.** Theorem 1 has no proof here, Theorem 2's proof
  is in [7], and Theorem 3's is "omitted due to space restrictions"
  (p. 11). The introduction says "We prove, however, that finding the
  coarsest refinement is NP-hard" (p. 2). Lemma 2 is stated without proof.
- **Hardness wording.** Theorem 3 says NP-hard; §7 calls it "the
  NP-complete separation problem" (p. 15). The decision version is not
  stated.
- **"A single equivalence class".** §3 says refinement partitions "a single
  equivalence class of ≡" (p. 7). But §4.3 refines the component relations
  ≡ⱼ, and since ≡ is their product, splitting a component class splits
  every abstract state that shares it, not only h⁻¹(ŝᵢ). This is my reading
  of pp. 11–12; the paper does not address it.
- **Loops are sketched.** The refinement for spurious loops "works
  analogously … Details are omitted due to space restrictions" (p. 12).
- **No iteration bound.** Termination is by finiteness; the paper gives no
  bound on the number of refinements or on the size of the final
  abstraction, and the PolyRefine heuristic is "not optimal" (p. 12).
- **Experimental claims are thin.** Five benchmarks and one industrial case.
  "One magnitude less memory" holds for one benchmark of five (table,
  p. 14). The Fujitsu design is said both to have been "successfully
  verified" and to have "a bug which has not been discovered before"
  (p. 15). Presumably some properties held and one failed; the bug is not
  described.
- **Small errors in the manuscript.** "previously known poblem" (p. 11);
  "Lind-Nielson" in the text against "Lind-Nielsen" in ref. 17 (p. 3,
  p. 16); a missing full stop after "full version" (p. 3).
- **The repository's metadata is wrong in two places.** KiltHub's "Publisher
  Statement" points to doi:10.1007/978-3-642-25510-6_27, which Crossref
  gives as Othman and Sandholm, "Liquidity-Sensitive Automated Market
  Makers via Homogeneous Risk Measures" (2011), not this paper. Its "Date"
  is 2011-11-01. Its "References" field has the right DOI,
  10.1007/10722167_15.
- **Not compared** with the Springer text, the technical report, or the J.
  ACM 2003 version.

## Open questions

- What is the complexity of the coarsest separation with S_{i,x} ≠ ∅ for a
  fixed number of components, and how far is PolyRefine's heuristic from
  optimal in practice? The paper asks for "efficient approximation
  algorithms" for it (p. 15).
- Does the method extend to all of ACTL\*, as the introduction says it can
  "in principle" (p. 2), and to the "trace"-like counterexamples of [4]
  (p. 15)?
- Is there a counterpart that revises the property rather than the
  abstraction, with a check as decisive as Lemma 1? Nothing in the paper
  bears on it. It is the question CLAIM-tmpalzo4's last clause raises.
