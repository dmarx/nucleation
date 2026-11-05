---
status: Read
paper: 'LIT-tmpj5g19'
title: 'Akitaya et al. — Rigid foldability from flat is NP-hard'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Read on 2026-11-05 from the arXiv PDF
    (https://arxiv.org/pdf/1812.01160, v1), text extracted by pdftotext.
    Read in full: §1 (introduction and results), §2 (the mathematical and
    computational model), §3 (rigid origami basics: Theorem 6, Lemmas 7
    and 9, Corollaries 10 and 11, Definition 12 and Theorem 13) and the
    conclusion. Skimmed: the gadget constructions and the reduction proofs
    of Theorems 15 and 16. Registered as a stand-in for the unread
    belcastro and Hull (2002) and for the NP-hardness section of the unread
    chapter "Rigid Origami Theory" of Hull's Origametry, at the owner's
    request. Quotes below were checked against the extracted text, which
    loses the product symbol in Equations (5) and (6).
date: '2026-11-05'
summary: >-
  Proves rigid foldability from flat weakly NP-hard using all creases
  (from Partition) and strongly NP-hard with optional creases (from 1-in-3
  SAT). Takes belcastro and Hull's loop condition as the rigidity
  constraint, necessary and near flat sufficient. Flat-foldable degree-4
  vertices have two modes, linear in tan(ρ/2), meeting only at flat; a
  choice of mountain–valley assignment folds exactly when the fold-speed
  coefficients multiply to 1 around every face. The hardness is in
  choosing modes so that every face closes. Finite-precision degree-4
  flat-foldable versions are in NP; general membership is open.
---
<!-- inactive-ok-file: LIT-tmphy9wm LIT-tmpq0e56 THEORY-tmpj5wcc — Unavailable, Proposed or new; the works this stands in for, and the account filed from it -->

# NOTE-tmpd0dln: Akitaya et al. — Rigid foldability from flat is NP-hard

## Contribution

A single vertex's rigid foldability is easy to decide, but there was no
general result for crease patterns. The paper separates foldability using
every crease from foldability using some subset, and proves both hard:
the first weakly NP-hard, the second strongly. The hardness does not come
from self-intersection, which near flat cannot happen, but from the
combinatorics of choosing a folding mode at each vertex.

## Key insight

For a flat-foldable degree-4 mesh, a folding is fixed by a mode choice at
each vertex, and the choice is valid exactly when every face closes: the
product of fold-speed coefficients around it is 1. Each check is local and
exact, but choosing a consistent set of modes encodes Partition, or with
optional creases 1-in-3 SAT. Local closure conditions do not make the
global choice easy.

## Assumptions

- **Rigid panels and ideal hinges.** Folding a finite but small amount from
  flat, so the paper cannot meet itself.
- **Rational crease coordinates**; a finite-precision variant allows a
  tolerance ε on each face product (Definition 12).
- **Existence of a path only**, not its mechanics (§2).

## Key results

- **The loop condition** (§2, Equation 1): for any simple, closed,
  vertex-avoiding curve γ crossing creases c1 … cn in order,
  R_c1(ρ1)R_c2(ρ2)···R_cn(ρn) = I "for all such curves γ (see [5])", [5]
  being belcastro and Hull (2002). "A necessary (but not sufficient, since
  the paper may cross itself) condition for f to be a rigid origami folding
  is" this; near the flat state, "Under these conditions, which are the
  ones we will be using in this paper, Equation (1) will be a necessary and
  sufficient condition for rigid foldability."
- **The results** (§1): "deciding rigid foldability of a given crease
  pattern using all creases is weakly NP-hard by a reduction from
  Partition"; with optional "creases is strongly NP-hard by a reduction
  from 1-in-3 SAT" (Theorems 15 and 16).
- **Why** (§1): "the complexity comes from the combinatorial behavior of
  the different possible rigid folding configurations at each vertex", and
  "a mere intersection of such single vertex condition does not lead to
  useful condition of multi-vertex rigid-foldability". Also: "it is harder
  to fold from an unfolded sheet of paper than to unfold a folded state
  back to a plane".
- **Degree-4 modes** (§3, Theorem 6): two modes, linear in tan(ρ_i/2), and
  "the configuration space curves determined by Equation (2) share exactly
  one configuration point t = 0 (the flat state)".
- **Face closure** (Corollary 11, Closure Condition): "A MV assignment of
  flat-foldable quadrivalent mesh yields a rigid folding motion if and only
  if for each k-gonal face f surrounded by creases ci" the speed
  coefficients multiply to 1.
- **In NP for the degree-4 class** (Theorem 13): the finite-precision
  degree-4 flat-foldable problems are in NP, even with ε = 0.
- **Scope** (§2): whether a path exists, "not whether it is mechanically
  feasible to, say, program a rigid, self-folding material to do so".
- **Open** (conclusion): the lower bound is not shown tight, and "the rigid
  foldability problem belongs to Class ∃R".

## Concepts

- **Rigid foldability using all creases**: a continuous rigid motion from
  flat in which every crease's angle strictly increases or decreases.
- **With optional creases**: some nonempty subset of the creases is
  rigidly foldable using all of its creases.
- **Speed coefficient** (fold-angle multiplier): p(e_i, e_j) =
  tan(ρ_i/2)/tan(ρ_j/2) between adjacent creases at a vertex.
- **Mountain–valley assignment**: crease → {M, V, 0}, 0 marking an
  optional crease left unfolded.

## Connections

- **belcastro and Hull (2002)**, LIT-tmphy9wm, which it stands in for. It
  restates their loop condition, citing them, in its global form, and
  says when it is necessary (always), why it is not sufficient
  (self-intersection) and when it is (near flat). It does not restate
  their derivation, the "non-intuitive order" of the product that their
  abstract mentions, the affine bookkeeping of translations for loops
  around several vertices, or their discussion of sufficiency.
- **Hull's chapter "Rigid Origami Theory"**, LIT-tmpq0e56, which it stands
  in for in part. It is the result the chapter's first section "outlines a
  proof" of, deciding foldability from flat "using some subset of the
  creases" (strong NP-hardness with optional creases). It does not restate
  the chapter's germ theorem, its disconnected examples or its
  self-folding theory (for the last, see Hull and Tachi, LIT-tmp6aj47).
- **Neighbours.** Its Corollary 11 is the face-closure condition Hull and
  Tachi use; Foschi, Hull and Ku (LIT-tmpegvxm) state the single-vertex
  form of the loop condition; Berry et al. (LIT-tmp24k66) cite this paper
  for NP-hardness.

## Bearing on the record

- **The pasted synthesis.** A does not cite this paper. A cites belcastro
  and Hull's loop closure R1(θ1)…Rk(θk) = I, which this paper states in
  that form for any closed curve, and reads it as holonomy: a product of
  transports round a closed curve equal to the identity is the statement
  that the holonomy of that loop is trivial. That fits. The paper bears on
  A's "Feasible target ⇏ reachable target" with a third kind of obstacle
  beside A's geometric disconnection and control limitation: computational
  hardness of finding a consistent choice of modes even when one exists.
- **CLAIM-495 (O(d) holonomy; sections as the common fixed subspace), and
  A's distinction.** A says "the full origami closure condition is stronger
  than the partial fixed-subspace compatibility studied in CLAIM-495". As
  a comparison that is true: closure asks every loop's product to be I,
  which in the claim's terms makes Fix(H) the whole space for every loop,
  the "all" end of its range, and that implies full compatibility and not
  conversely. But it compares at different levels. In the claim the
  transports are given and the unknowns are sections; in origami the
  unknowns are the fold angles, that is the transports themselves, and
  closure constrains which transports are admissible. Closure is a
  requirement of flatness one level up, not a stronger form of the same
  compatibility. And it is not "the full" foldability condition either:
  loop closure is necessary, not sufficient, since the paper may cross
  itself; only near flat is it sufficient. Two further mismatches, the
  reader's inference from belcastro and Hull's title and this paper, not
  from their text: for loops round several vertices the transports are
  rigid motions with translations, not elements of O(3), and the claim is
  stated for O(d). What does fit the claim directly is its last clause:
  rotations about different crease axes, which do not commute, compose to
  I, so "non-commutativity is not holonomy" has a physical instance here.
  The partial-compatibility case the claim is filed for is not
  instantiated.
- **CLAIM-538 (cycle holonomy against summed tolerance).** Qualifies; the
  bearing is the reader's inference, and the paper mentions neither
  holonomy nor sheaves. In logarithms, Corollary 11 is an exact cycle
  condition, the log speed coefficients summing to 0 around each face
  (with sign bookkeeping): the claim's criterion with δ = 0, written
  multiplicatively, and Definition 12's tolerance ε is a multiplicative
  tolerance on the same cycle. In the claim the offsets are given and
  feasibility is a linear program in continuous x. Here the offsets come
  from a discrete choice of mode at each vertex, and deciding whether some
  choice closes every face is NP-hard. So exact cycle-local certificates
  do not make the global problem easy once the offsets are chosen
  discretely. The record does not say this; it is a candidate qualification
  of how far the claim's cycle certificate carries.
- **CLAIM-347 (the compatibility complex).** Qualifies. "a mere
  intersection of such single vertex condition does not lead to useful
  condition of multi-vertex rigid-foldability" is a local-to-global
  failure of the kind the complex encodes: each vertex's modes are
  feasible locally, and the set of jointly consistent assignments can be
  empty.
- **CLAIM-365 (a dual certificate of infeasibility).** Related, different.
  For a fixed assignment the face products are an exact check; across all
  assignments the problem is NP-hard, so no short certificate of
  infeasibility is to be expected unless NP = coNP (the reader's
  inference).
- **THEORY-171.** A cites it among the codes for its origami part, whose
  points include loop closure as holonomy, with the gloss "(local-to-global,
  gluing)". It is about causal contextuality:
  deterministic assignments causal in each context can fail to glue into
  one causal assignment. It contains no holonomy, and its gluing is of
  another kind; it is unrelated to loop closure.
- **THEORY-1082** (U(1) phases on a graph; a common solution iff every
  cycle's phase vanishes) is the nearest exact analogue of closure as
  trivial holonomy for d = 1, and supports the holonomy reading;
  **TERM-097** (coherence around cycles) fits: closure is coherence of
  transports around cycles. **QUESTION-319** asks whether nontrivial
  holonomy among an organization's parts is an error or a feature; in
  paper any nontrivial holonomy is forbidden, one pole of its
  alternative. These are loose fits, not dated notes.
- Filed: THEORY-tmpj5wcc. No instruction for machine-learning practice;
  nothing for the anthology.

## Limitations

- **Gadget proofs skimmed**, not checked line by line.
- **Not tight**: membership in NP is open in general; ∃R is the known
  upper class.
- **Mechanics ignored**: foldability is existence of a rigid path.
- **The journal version** (JoCG 2020) was not compared.
