---
status: Skimmed
paper: 'LIT-tmp5bp7f'
title: "Hopkins — Parallel flexure design via Freedom and Constraint Topologies (master's thesis)"
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Read in part on 2026-11-05 from the DSpace@MIT ORIGINAL bitstream,
    182522845-MIT.pdf, a 75 MB scan with OCR,
    https://dspace.mit.edu/server/api/core/bitstreams/ff6562f6-68ef-4fbc-9e55-93ad38c7a061/content,
    extracted with pdftotext -layout; printed page numbers match the PDF's.
    Read: the abstract; ch. 1 (introduction); ch. 2 (constraint-based
    design); ch. 3 §§3.3–3.4 (twist–wrench reciprocity); ch. 5 (freedom
    and constraint space, including §5.2.1 on redundancy, §§5.2.4–5.2.5 and
    §5.3); ch. 9 (systems symmetry, including §§9.3–9.4); ch. 10 §10.1 (the
    six steps) and the Step 6 part of the STM-probe case study (§10.2.2);
    ch. 11 (conclusion); App. A. Skipped: ch. 4 (projective geometry), ch.
    6 (ruled surfaces), chs. 7–8 (the case-by-case derivation of the 26
    types, pp. 104–284), case studies §10.2.1 and §10.2.3, and Apps. B–N.
    Figures were not inspected; the OCR loses them. Skimmed, because the
    derivations that carry the enumeration were not read, though the
    argument chapters were.
date: '2026-11-05'
summary: >-
  The founding statement of FACT for parallel flexures. Motions are
  twists, constraints wrenches, and the freedom space is the null space of
  the constraint wrenches; each freedom space is linked one to one with a
  constraint space, and for ideal pure-force constraints the pairs fall
  into 26 types in six cases. A redundant constraint is one whose addition
  or removal leaves the freedom space unchanged while stiffness, load
  capacity and stability change, and the design procedure uses such
  constraints for stiffness and symmetry. Some motion sets cannot be had
  from constraints without unwanted extra freedoms. Elastomechanics,
  dynamics and actuation are out of scope.
---
<!-- inactive-ok-file: THEORY-tmpmbmox THEORY-144 NOTE-tmpnscd2 LIT-tmpf26t2 — Proposed, Skimmed, Unfetched or new; cited from the reading of Hopkins (2007) as open -->

# NOTE-tmpla9de: Hopkins — Parallel flexure design via Freedom and Constraint Topologies (master's thesis)

## Contribution

A design tool for flexure systems made of one rigid stage tied to ground
by slender flexures, each idealised as a constraint stiff along its axis
and infinitely compliant across it. It gives:

- a catalogue of freedom/constraint space pairs for ideal constraints: 26
  types, with Cases 1–6 holding 1, 3, 9, 9, 3 and 1;
- a kinematic definition of constraint redundancy, a count of it by the
  rank of the wrench matrix, and "sub-constraint spaces" that tell a
  designer which constraints are non-redundant;
- a symmetry between the Case N constraint spaces and the Case 6 − N
  freedom spaces;
- a six-step design procedure, illustrated by a ball joint, a five-axis
  STM probe and a rotary flexure.

## Key insight

Permitted motion and admissible constraint are two views of one object.
A twist is permitted when it does no work against every constraint
wrench, so the set of permitted motions and the set of lines along which a
constraint can be added without changing them fix each other: "This
principle that complementary spaces are uniquely linked with each other is
called the Principle of Complementary Topologies." (§5.3, p. 90). Drawing
both as geometric figures lets a designer read off the constraints from
the desired motions.

## Assumptions

- **One rigid stage, connected in parallel only.** Serial stacking is
  future work.
- **Small motions**, so twists are instantaneous (first order).
- **Ideal constraints**: a pure force along the flexure axis (pitch
  q = 0), infinitely stiff axially and infinitely compliant otherwise. The
  thesis notes that every real line has finite stiffness, so the freedom
  space keeps "only practical twist lines of greatest compliance"
  (p. 73).
- **Statics and kinematics only**: no elastomechanics, dynamics, buckling
  or actuation.

## Key results

- **The count (abstract, p. 3).** "twenty six unique matching pairs of
  freedom and constraint spaces were identified"; among the contributions,
  "it was proven that these spaces embody all possible solutions". Also
  §5.3, p. 91: "there are 26 freedom spaces each with a unique constraint
  space".
- **The count is for pure-force constraints (§9.4, pp. 298–299).** Once
  wrenches of any pitch are allowed (coils, torques), more types exist:
  "Case 3, therefore, has at least 11 types." The defence is that "those 26
  types shown in red in Table 9.2 are the only types with any useful spaces
  for designing flexure systems". Table 9.2 gives 1/3/10/?/10/3/1 types for
  any pitch against 1/1/3/9/9/3/1 for q = 0 (Cases 0–6); the 26 leave out
  Case 0.
- **Redundancy (§5.2.1, p. 75).** "A constraint is non-redundant if when it
  is added to or removed from a system, the kinematics or the freedom space
  of that system changes." And: "In practice, the flexure system's
  stiffness, load capacity, and stability change but the system's
  kinematics do not." The number of non-redundant constraints is the rank
  of the wrench matrix; no single member of a redundant set is "the"
  redundant one.
- **Redundancy as a design lever (abstract, p. 3).** A sub-process to "guide
  designers in the selection of redundant constraints that help satisfy
  stiffness and symmetry requirements without altering the mechanism's
  kinematics". Step 6, §10.1.6, p. 304: "By adding redundant constraints,
  the flexure system's kinematics will not change"; the payoffs named are
  thermal symmetry, tolerance of a failed constraint, and stiffness without
  thicker or shorter flexures. The STM probe adds four redundant
  constraints for thermal symmetry (§10.2.2, pp. 314–315).
- **Basis (§2.2, p. 35).** Blanding's rule, "Every freedom line intersects
  every constraint line.", which §3.3 shows is contained in the
  reciprocity condition and extended to screws.
- **A limit of the constraint-only route (§5.2.4, pp. 87–89).** "Instances
  exist in which some desired degrees of freedom may not be achieved
  without including other unwanted degrees of freedom." A disk of pure
  translations cannot be had alone: "the designer will have to make due
  with an extra, undesired, rotational degree of freedom".
- **Duality symmetry (§9.2, p. 294).** "Every Case N constraint space,
  therefore, looks geometrically identical to some Case 6-N freedom space".
- **Claimed novelty (§1.2.4, p. 31).** "Prior to FACT, no formal method
  existed that was capable of controlling useful system redundancy."
- **Scope (§11.3, pp. 328–329).** "The elasto-mechanics of systems has,
  however, not been addressed in this thesis." Actuation is future work:
  "Certain actuator locations and orientations are better than others for
  controlling these motions."

## Concepts

- **Freedom space**: the union of freedom sets, geometric figures of twist
  lines; "a visual representation of the complete kinematics" of the
  system (§5.1).
- **Constraint space**: "all the possible locations from which a designer
  could select a constraint without changing the freedom space of the
  system" (§5.2.2).
- **Redundant / non-redundant constraint**: by whether adding or removing
  it changes the freedom space.
- **Sub-constraint space**: the subset of a constraint space from which the
  non-redundant constraints are picked (ch. 8, §10.1.4).
- **Case N / type**: N is the number of non-redundant constraints; a type
  is a distinct geometric arrangement within a case.
- **Principle of Complementary Topologies**: the one-to-one link between a
  freedom space and its constraint space.

## Connections

It builds on Blanding's exact-constraint design and on screw theory
(twist–wrench reciprocity). Hopkins & Culpepper (2010), [LIT-tmpf26t2](../literature.d/LIT-tmpf26t2.md),
condenses it as the FACT "Principles" paper and stands unfetched; this
thesis restates what that paper is cited for in general (the reciprocity,
the definition of redundancy, the 26 types and the design steps), but not
that paper's own wording, any revision to the count or the procedure, or
its figures. The PhD thesis, [LIT-tmp9cusv](../literature.d/LIT-tmp9cusv.md) ([NOTE-tmpnscd2](NOTE-tmpnscd2.md)), extends it to
all wrench pitches (50 types), serial stacking and actuation.

## Bearing on the record

- **The pasted synthesis on constraint architectures.** A's quoted gloss,
  "constructs 26 matching pairs of freedom and constraint spaces and
  develops a systematic procedure", is A's paraphrase: those words are not
  in the thesis, whose abstract says "twenty six unique matching pairs".
  The substance is right, with one qualification A misses: **the 26
  matching pairs hold only for ideal pure-force constraints.** The thesis
  itself shows more types once general wrenches are allowed (§9.4), so its
  claim that "it was proven that these spaces embody all possible
  solutions" is restricted to that idealisation. A's "explicitly treats
  the use of redundant constraints to improve engineering performance
  without changing the intended kinematics" is also A's paraphrase, and
  right in substance (abstract, §5.2.1, §10.1.6, the STM case study).
  "Engineering performance" here means stiffness, symmetry and thermal
  stability, load capacity and tolerance of a failed constraint. The
  thesis does not treat the costs of redundancy, such as misfit stress or
  sensitivity to fabrication error.
- **Freedom, constraint and actuation.** **The thesis does not cover
  elastomechanics or actuation** (§11.3). Of A's three things it has only
  freedom and constraint; actuation enters with the PhD thesis.
- **Constraints making freedom possible.** A's framing that properly
  organized constraints make useful freedom possible, and [THEORY-1335](../theory.d/THEORY-1335.md)'s
  enabling constraints, are qualified here. In FACT a constraint only
  removes a freedom or leaves the freedom space unchanged; what it adds is
  stiffness and precision in the directions it removes, and redundant ones
  add robustness. **In FACT, new freedom comes from stacking bodies in
  series, not from adding constraints**; that is the PhD thesis's serial
  synthesis.
- **[CLAIM-345](../claims.d/CLAIM-345.md) (equal controllability rank does not fix the cost of
  control).** A proposes extending it to say that equal nominal freedom
  spaces do not entail equal control effort. This thesis supports that,
  weakly: redundant constraints change stiffness, load capacity and
  stability with the freedom space unchanged. It does not quantify effort.
- **[THEORY-144](../theory.d/THEORY-144.md) (redundant defences erode unobserved).** An analogue. A
  redundant constraint is, by FACT's definition, one whose removal leaves
  the kinematics unchanged, so its loss is invisible to kinematic
  observation and shows only in stiffness or stability. The thesis names
  tolerance of a failed constraint as a payoff (p. 304); it does not
  discuss erosion.
- **[CLAIM-347](../claims.d/CLAIM-347.md) (jointly satisfiable demands form a downward-closed
  complex).** Unrelated in substance. FACT's monotonicity, that a
  constraint removes a freedom or leaves the space unchanged, matches A's
  "If K'⊆K then Traj(K')⊆Traj(K)" in kinematic form, but says nothing of
  frustration among demands.
- Filed: [THEORY-tmpmbmox](../theory.d/THEORY-tmpmbmox.md). No instruction for machine-learning practice;
  nothing for the anthology.

## Limitations

- **The author's own (§11.3).** No elastomechanics, dynamics, buckling or
  actuation; parallel systems only; types for non-ideal wrenches left
  incomplete.
- **Completeness is model-relative.** It holds only under the
  ideal-constraint, small-motion model. The finiteness argument of §5.3 is
  offered as suggested by the six-constraint bound, and the enumeration is
  carried out case by case in chs. 7–8, which were not read.
- **A wording slip** in the proof of 6 − N = R (§5.2.5): "the number of
  columns that matrix has subtracted from that matrix's rank" where
  columns minus rank is meant.
- **A master's thesis**, not peer reviewed; the peer-reviewed statement,
  [LIT-tmpf26t2](../literature.d/LIT-tmpf26t2.md), was not reached.
