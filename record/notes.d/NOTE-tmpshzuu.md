---
status: Read
paper: LIT-tmpsd4w3
title: 'Notes on Landauer''s principle, reversible computation, and Maxwell''s Demon'
version: 1
history:
- version: 1
  date: '2026-09-29'
  note: >-
    Read in full (I read the full text of arXiv physics/0210005 v2 (9 Jan
    2003; "revised and enlarged from v1"), 7 pp., from the arXiv PDF. The
    text was extracted with PyMuPDF, and p. 3 was rendered to read Fig. 1. I
    read all of it: the abstract, "Landauer's Principle" (p. 1), "Objections
    to Landauer's Principle" (pp. 1–5), "Landauer's principle in the context
    of other ideas in 19'th and 20'th century physics" (pp. 5–6), the
    Szilard footnote (p. 5), the acknowledgements and all 19 references.
    Nothing was skipped. I did not read v1 (1 Oct 2002) or the version of
    record in *Stud. Hist. Phil. Mod. Phys.* 34 (2003) 501–510, so page
    numbers are those of the arXiv PDF. The PDF's printed date line,
    "(November 26, 2024)", is an artefact of arXiv regenerating the file,
    not a date of writing. `published:` is the arXiv v1 date. No anthology
    entry exists for this paper (I grepped the arXiv id and the title in
    record/literature.d).). The first NOTE on this paper, which was seeded
    from its abstract alone.
date: '2026-09-29'
summary: >-
  Bennett states Landauer's principle as a consequence of the Second Law.
  A logically irreversible step, meaning erasure or a *merge of control
  flow*, must export at least the lost entropy (k ln 2 per bit) to
  non-information-bearing degrees of freedom. That export need not take
  the form of heat (p. 1). Logically reversible operations, including
  copying onto a blank register and measurement, have no minimum cost. He
  calls "an intrinsic cost of order kT for every elementary act of
  information processing" a 20th-century "misconception" (pp. 5–6).
  Erasing random data can itself be thermodynamically reversible; the
  waste comes from applying a many-to-one operation to *known* data (pp.
  1, 4).
---

# NOTE-tmpshzuu: Notes on Landauer's principle, reversible computation, and Maxwell's Demon

## Contribution

This is a short defence of Landauer's principle against three kinds of objection:

1. that it compares incommensurables (heat and logic);
2. that its converse fails because every operation costs at least kT ln 2;
3. that even irreversible operations can be done without an entropy cost.

Bennett also takes up Earman and Norton's charge that the principle is either unnecessary or insufficient as an exorcism of Maxwell's demon. The paper adds two things to the stock statement of the principle. It identifies **merging of control flow** as a logically irreversible step, which answers Earman and Norton's demon program (p. 3). It gives a mechanical account, via Fig. 1, of *where* the entropy is produced when a constrained coordinate is released (p. 4). It also sorts reversible computers into three kinds (ballistic, externally clocked Brownian, fully Brownian) and says how the principle applies to each (pp. 4–5).

## Key insight

The cost attaches to **many-to-one mappings of the logical state**, not to information. Because Hamiltonian or unitary dynamics conserves fine-grained entropy, a loss of distinguishable logical states must be matched by entropy gained elsewhere (p. 1). Anything that can be written as a bijection has no floor. That includes copying onto a blank register, erasing one of two copies known to be equal, and measurement into a standard-state memory. Such operations can be run arbitrarily close to reversibly.

Whether a many-to-one step is *thermodynamically* irreversible depends on what is known about its input. Applied to random data it is a reversible transfer of entropy, like isothermal compression. Applied to known data it is waste, like free expansion followed by compression (pp. 1, 4).

## Assumptions

- **Physicalism about the demon.** Intelligence is replaced by "an automatically functioning mechanism", and "the entire universe, including the Demon, should obey Hamiltonian or unitary dynamics" (p. 2).
- **The IBDF/NIBDF split.** Some degrees of freedom are information-bearing and robust, so the logical state evolves deterministically "regardless of small fluctuations" (p. 1).
- **The Second Law, via conservation of fine-grained entropy.** The principle is presented as "a straightforward consequence or restatement of the Second Law" (abstract), not an independent postulate.
- **Idealised thought-experiment conventions.** These include slow (quasistatic) driving, nonzero but arbitrary backlash (p. 3), and infinite barriers ruling out hardware errors (p. 5; flagged as an idealisation).

## Key results

What the paper argues, in its order:

- **Statement of the principle (p. 1).** During a logically irreversible operation "the entropy decrease of the IBDF … must be compensated by an equal or greater entropy increase in the NIBDF and environment". Typically this takes the form of heat, "but it need not".
- **Random versus known data (pp. 1, 4).** A logically irreversible operation on random data "may be thermodynamically reversible". On known data it is thermodynamically irreversible. Any deterministic computation that saves a copy of its input can be reprogrammed as logically reversible steps "which need not use much more time or memory" and can then in principle be run reversibly (p. 1; the time/space trade-offs are referenced in [13]).
- **Objection 2 answered (p. 2).** Explicit models of zero-cost ballistic computation (Fredkin–Toffoli) and of Brownian computation with per-step cost tending to zero exist. Real hardware dissipates "far in excess" of the bound. DNA→RNA transcription is offered as a reversible-in-practice case.
- **Logically reversible primitives (p. 2).** `y := y + x` copies x onto a blank y, and `y := y − x` erases y when y = x is known. Each undoes the other. Reversible measurement (S → L or R) is one such primitive, with explicit mechanisms cited ([5] Fig. 12, [7]).
- **Earman–Norton's demon program (p. 3).** Subroutines L and R are each reversible, but instruction M1 has two predecessors (L4 and R5). That "merging in the flow of control" is a 2:1 map of the logical state, and there "the work extracted by the demon must be paid back". So no cost need be sought in the measurement step M2.
- **Shenker's pinion (pp. 3–4, Fig. 1).** When the barrier between two about-to-merge paths disappears (stage 2), the information-bearing coordinate "suddenly gains access to twice as large a range". That is an irreversible entropy increase of k ln 2, like free expansion. The resetting rotation is therefore not thermodynamically reversible for any nonzero backlash.
- **Shenker's 1:1 argument (p. 4).** A deterministic computation visits an unbranched chain of states, so Shenker concludes it is not bound by the principle. Bennett replies that performing a 1:1 map "by a manipulation that could have performed a 2:1 mapping is thermodynamically irreversible". What the observation really shows is that reversible reprogramming is always possible.
- **Schneider's two-step biological account (p. 4).** Bennett says it is "not inconsistent" with the principle, and that transcription is better seen as reversible copying driven by pyrophosphate removal.
- **Three machine classes (pp. 4–5).** *Ballistic* machines cannot merge trajectories and dissipate nothing, but must be isolated from baths. For *externally clocked Brownian* machines (most Szilard engines, most proposed quantum computers) the cost is the integrated work of the external agency: merges on nonrandom data are costly, and otherwise dissipation per step is proportional to the driving force and tends to zero. For *fully Brownian* machines the cost is "the weakest spring sufficient to achieve a net positive drift velocity", and a little merging costs less than in the clocked case.
- **Error correction (p. 5).** The thermodynamics of fault-tolerant computation "appears to be in its infancy". Bennett's 1979 proofreading model [18] and Schulman–Vazirani's algorithmic cooling [19] are the only cited cases.
- **The Earman–Norton dilemma conceded (p. 5).** If the demon already obeys the Second Law, nothing more is needed; if it does not, nothing about information can save the Law. Bennett grants this "with some justice". He defends the principle as pedagogy, against the "informal belief that there is an intrinsic cost of order kT for every elementary act of information processing" that he attributes to von Neumann, Gabor, Brillouin and "perhaps" Szilard (pp. 5–6).
- **Szilard footnote (p. 5).** Szilard 1929 is "tantalizingly ambiguous". Most of it attributes the cost to acquisition, but its final analysis places the entropy increase at the resetting step.
- **Gabor's engine and Feynman's ratchet (p. 6).** A trap dissipating E runs backward with probability exp(−E/k_BT). If E > k_BT ln X the engine runs forward but loses energy; if E < k_BT ln X it runs backward. Either way it does not violate the Second Law.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Logically irreversible operations (erasure, path merging) must be accompanied by an equal or greater entropy increase in the NIBDF or environment, not necessarily as heat | informal argument from conservation of fine-grained entropy | p. 1; presented as a restatement of the Second Law, not derived formally |
| C2 | Logically reversible operations, including copying onto a blank register and measurement, can in principle be done with arbitrarily small dissipation | argument by cited explicit models | p. 2; Fredkin–Toffoli [4], Brownian computers [5], clockwork measurement [7]; the models are not reproduced here |
| C3 | A merge in the flow of control is a logical irreversibility on a par with erasure, and it is where the Earman–Norton demon pays | informal argument | p. 3 (the M1 two-predecessor step) |
| C4 | The release of a constrained information-bearing coordinate (Fig. 1, stage 2) is an irreversible k ln 2 entropy increase, for any nonzero backlash | informal argument with a schematic figure | pp. 3–4 |
| C5 | Erasure of random data is thermodynamically reversible; erasure or merging applied to known data is not | informal argument by thermodynamic analogy | pp. 1, 4 (isothermal compression vs free expansion) |
| C6 | Any deterministic computation that saves its input can be reprogrammed as logically reversible steps without much more time or memory | assertion here (a known result, cited) | p. 1; [12], [13] |
| C7 | There is no intrinsic kT-order cost per elementary act of information processing; the belief that there is, is a misconception | argued position | pp. 5–6; rests on C2 |
| C8 | Landauer's principle is dispensable for saving the Second Law but has "considerable pedagogic and explanatory power" | concession plus assertion | abstract, p. 5 |

## Concepts

- **IBDF / NIBDF.** Information-bearing and non-information-bearing degrees of freedom (p. 1).
- **Logical irreversibility.** A logical state with two or more distinct predecessors. The paper's examples are erasure, and merging of computation paths or control flow (pp. 1, 3).
- **Thermodynamic irreversibility.** Entropy production not compensated elsewhere. Logical irreversibility entails it only when the input is not random (p. 4).
- **Reversible measurement.** A logically reversible S → L/R transition of a memory initially in a standard state (p. 2).
- **Ballistic / externally clocked Brownian / fully Brownian machines.** The three classes of p. 4, each with its own cost accounting.

## Connections

- **Landauer 1961 ([LIT-328](../literature.d/LIT-328.md), Deferred, unreachable).** This is the principle as Bennett restates it. It is not Landauer's text, so it cannot be quoted as Landauer. The title in Bennett's reference [2] is wrong (see corrections).
- **Still et al., "Thermodynamics of Prediction" ([LIT-327](../literature.d/LIT-327.md); [NOTE-295](NOTE-295.md)).** Their only per-bit heat bound is the Landauer term I_e, the conditional entropy removed. That is Bennett's erasure cost, and Bennett's account explains why [NOTE-295](NOTE-295.md) found no bound on acquiring or keeping predictive information. The nostalgia term is a separate, dissipative cost of memory that fails to predict, which Bennett does not discuss.
- **Goldt & Seifert, "Stochastic Thermodynamics of Learning" ([LIT-308](../literature.d/LIT-308.md); [NOTE-296](NOTE-296.md)).** [NOTE-296](NOTE-296.md) found that information learnt can be paid for almost entirely by growth of weight entropy, with vanishing heat under slow driving, and that the heat falls due when the weights are reset. That is Bennett's picture exactly. Acquisition is reversible in principle (C2, C7), and the cost comes due at erasure (C1, C5).
- **SEP, "Philosophy of statistical mechanics" ([LIT-114](../literature.d/LIT-114.md); [NOTE-103](NOTE-103.md)).** Its §7.2 reports the Earman–Norton dilemma and Norton's verdict that the Landauer literature is "too fragile", and names Bennett among the replies. This paper is that reply, and on the dilemma itself it concedes.
- **Bub 2002** (arXiv quant-ph/0203017) is named in the abstract as giving "similar arguments". It is not in either record.
- **Anthology of the SOTA.** No entry. It carries nothing for ML practice.

## Bearing on the record

**Map row 13. What it supplies, and what it repairs.** The row cites Landauer 1961 ([LIT-328](../literature.d/LIT-328.md)), which is unreachable, as the owner of the physics behind "`0/1` predicate → `k_B T ln 2` floor; per-step heat `Q ≥ k_B T ln2 · C_step`". Bennett is a legitimate, reachable, first-hand statement of what that physics requires, and it supplies what the map needs. But it supplies it *against* the row's formulation:

1. **The floor is on logical irreversibility, not on judgment.** A 0/1 predicate that is *evaluated*, with its result written to a blank register, is a copy and has no floor (C2, C7). A floor applies only if the evaluation overwrites a previous value or merges paths. The map's "per-judgment floor" is the "kT for every elementary act of information processing" belief that Bennett calls a misconception (pp. 5–6).
2. **The floor is not heat.** It is entropy exported to non-information-bearing degrees of freedom (p. 1). "Q ≥" is the typical case, not the principle.
3. **Random versus known data matters.** For a trained model's deterministic forward pass, the inputs to any overwrite are not random given the state. Bennett's accounting then makes the overwrite *thermodynamically irreversible*, with the k ln 2 wasted (pp. 1, 4). The same accounting also says the waste is avoidable by reversible reprogramming. So the "floor" is neither forced for the computation nor a floor on the information content.

This converges with [NOTE-295](NOTE-295.md) and [NOTE-296](NOTE-296.md). Three reachable sources now say the same thing: acquisition, copying and evaluation have no minimum cost, and erasure costs at least k ln 2 of entropy per bit of lost distinguishability. The map's `KNOWN (physics) / SYNTHESIS (bridge) / NOVEL-NARROW` verdict for row 13 should be restated. The defensible bridge is **k_BT ln 2 per predicate bit *erased or overwritten***, attributed to Landauer *as stated by Bennett 2003*, and not per judgment. "Per step, Q ≥ k_BT ln 2 · C_step" is not supported unless every step irreversibly overwrites C_step bits of known state. Even then the principle requires only entropy export, and reversible reprogramming could avoid most of it.

**Citation hygiene.** Cite Bennett for the scope of the principle, and do not quote him as Landauer. His title for Landauer's paper is wrong. Use [LIT-328](../literature.d/LIT-328.md)'s bibliographic data for Landauer.

**ML practice.** None. Bennett notes that real hardware dissipates "far in excess" of the bound (p. 2).

## Limitations

- **Position paper, no formal derivations.** Every claim is argued informally or by reference to Bennett's earlier models. The central principle is asserted as a consequence of entropy conservation, not derived for any stated dynamics.
- **The Earman–Norton dilemma is conceded, not answered** (p. 5). The paper's defence of the principle's *explanatory* value is an assertion about pedagogy.
- **Hardware errors and fault tolerance are set aside** as a subject "in its infancy" (p. 5). So the thermodynamics of noisy computation, which is where real per-step costs arise, is not addressed.
- **Quantum and single-shot versions are not treated.** Everything is ensemble-level, classical thought-experiment reasoning.
- **An editing slip in the arXiv text.** "it increases decreases the entropy of the data" (p. 4) is an unfinished edit; the sense is "decreases".

## Open questions

- What is the minimal entropy cost of *fault-tolerant* computation at a fixed error rate? Bennett names this as open (p. 5). It is the question a realistic per-step floor for learning hardware would have to answer.
- Does a per-bit accounting survive for operations whose inputs are partly random, such as stochastic rounding or dropout masks? Bennett's random-versus-known distinction suggests their erasures are partly reversible, but he gives no quantitative interpolation.

## Corrections to the seeded skim

- none (there was no seed or dossier)
- The batch brief's title ("Notes on Landauer's principle, reversible computation, and Maxwell's demon") and year are confirmed. Crossref confirms the version of record as *Studies in History and Philosophy of Modern Physics* 34(3):501–510 (September 2003), DOI 10.1016/S1355-2198(03)00039-X. The PDF title capitalises "Reversible Computation" and "Maxwell's Demon".
- Map row 13 cites the physics as "`0/1` predicate → `k_B T ln 2` floor; per-step heat `Q ≥ k_B T ln2 · C_step`" and lists Landauer 1961 as its owner. This text says the opposite for any operation that is not a many-to-one mapping. "Information processing and acquisition have no intrinsic, irreducible thermodynamic cost, whereas the seemingly humble act of information destruction does have a cost" (p. 6). Charging kT "for every elementary act of information processing … regardless of the act's logical reversibility or irreversibility" is the misconception the principle exists to correct (pp. 5–6). A per-judgment or per-step floor therefore holds only for judgments that overwrite or merge.
- The cost is an entropy increase in the non-information-bearing degrees of freedom and the environment. It "need not" be heat, since "entropy can be exported in other ways, for example by randomizing configurational degrees of freedom" (p. 1). So even for erasure, "heat Q ≥ k_BT ln 2" is the typical realisation, not the principle itself. This matches [NOTE-296](NOTE-296.md)'s finding for [LIT-308](../literature.d/LIT-308.md), where learning's cost is total entropy production and not heat.
- Bennett's reference [2] gives Landauer 1961 the title "Dissipation and Heat Generation in the Computing Process" (p. 6). The paper's actual title, recorded on [LIT-328](../literature.d/LIT-328.md) and verified via Crossref there, is "Irreversibility and Heat Generation in the Computing Process". The volume and pages (IBM J. Res. Develop. 5, 183–191) match.
- The arXiv listing's abstract says the principle is "a trivial and obvious restatement of the Second Law". The v2 PDF's abstract says "a straightforward consequence or restatement". The listing appears to carry older wording. Cite the PDF.
