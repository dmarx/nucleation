---
status: Read
paper: 'LIT-tmpjjho1'
title: 'Stern, Pinson & Murugan — Distractor branches and folding islands in self-folding origami'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Read in full on 2026-11-05 from the arXiv v1 preprint,
    arXiv:1703.04161v1 (submitted 12 March 2017, 8 pp.), extracted by
    pdftotext both in layout mode and as running text, since the two-column
    layout breaks sentences across columns. The preprint is titled "The
    difficulty of folding self-folding origami"; the published version, in
    Physical Review X 7, 041070, is titled "The Complexity of Folding
    Self-Folding Origami". The published version was not read: journals.aps.org
    returned a Cloudflare challenge and was not retried, and a copy of it
    obtained by another route was set aside unused. Read: the abstract,
    Introduction, Results (4-vertex and chains of 4-vertices; branch
    selection through mechanical advantage; loops of vertices create glassy
    energy landscapes; large patterns; actuation of large loopy patterns;
    folding islands), Discussion and the captions of Figs. 1–5. The
    Supplementary Information it refers to (energy model, dot products,
    design comparison) is not in the arXiv PDF and was not read. The
    reference list was checked only for refs. [2] and [37]. Section names
    and quotes are the preprint's; the published text may differ.
date: '2026-11-05'
summary: >-
  From the arXiv v1 preprint. A generic 4-vertex has two branches meeting
  at the flat state; around a loop the fourth vertex is over-determined,
  so most branch assignments have energy of order κρ⁴ and the sheet's
  landscape is glassy, with distractor branches growing as 2^(α√A), α ≈
  2.25. Folding is zero-temperature descent, so randomly placed actuators
  usually misfold the sheet: 18 of 60 creases on one 4 × 4 pattern for a
  50% chance. Whether the union of the actuated creases' folding islands
  covers the sheet predicts success better than the number of actuators,
  and an added actuator with a small island can ruin a successful
  folding. The difficulty is at the flat state.
---
<!-- inactive-ok-file: THEORY-tmpq2qdv CLAIM-184 CLAIM-185 CLAIM-478 THEORY-521 LIT-tmpa3uim — Proposed, Unavailable or new; cited from the reading of Stern, Pinson & Murugan (2017) as open -->

# NOTE-tmp9dvve: Stern, Pinson & Murugan — Distractor branches and folding islands in self-folding origami

## Contribution

- A count, by simulation on random quadrilateral meshes, of the folding
  branches of a crease pattern designed with one folding motion: their
  number grows exponentially with the sheet's boundary length, and their
  attractor basins are small.
- An explanation: frustrated loops of bifurcated vertices make a glassy
  landscape, which designing the target branch does not remove.
- A heuristic for placing actuators, "folding islands", and a
  demonstration that adding an actuator can ruin folding that otherwise
  succeeds.

## Key insight

A single designed folding motion does not make a single folding motion
reachable. Each 4-vertex can leave the flat state along two branches; in a
chain the choices propagate without conflict, but around a loop the last
vertex is over-determined, so most combinations cost energy only at fourth
order. That makes an exponential number of dead ends near the flat state.
Folding seeded from the flat state at zero temperature cannot backtrack,
so where the sheet is pushed decides where it ends.

## Assumptions

- Idealized 4-vertices with rigid faces, constraint violations penalized
  by E = Σ T_a² (Eq. 1), faces bending to absorb them; the full energy
  model is in the SI, not read.
- Branch selection by a model landscape in which "the angular bisector of
  the two branches separates their attractor basins"; the authors say
  that real vertices' dividing lines may be skewed without changing the
  results qualitatively.
- Zero-temperature, noise-free descent: "folding is assumed to happen at
  ‘zero temperature’", so "the structure cannot backtrack out of a local
  minimum".
- Actuators apply fixed O(1) torques of the right sign at chosen creases:
  location is controlled, magnitude is not.
- Random quad meshes up to A = 36 (6 × 6), each folded with about 2000
  random torques; actuation statistics from one 4 × 4 pattern.

## Key results

- **Abstract.** "even crease patterns with only one designed folding
  motion inevitably contain an exponential number of ‘distractor’ folding
  branches accessible from a bifurcation at the flat state." The authors
  conclude that "our results point to fundamental limits on the
  programmability of energy landscapes in sheets."
- **Introduction.** The distractors "are dead-ends since they are of zero
  energy only to linear order." "The number of distractors grows
  exponentially with the boundary length of the sheet".
- **One vertex (4-vertex and chains).** "only 2 of the 3 vertex equations
  are independent when the vertex is laid out flat", so a generic 4-vertex
  has two branches meeting at the flat state; "one constraint is redundant
  at, but only at, the flat state."
- **Loops (glassy landscapes).** Closing a chain of three vertices with a
  fourth gives branches whose energies scale as κρ⁴: "the energy of these
  branches scale as κi ρ4 with κi 6= 0." (κ_i ≠ 0 in the extraction's
  rendering). "loops of vertices have a glassy folding energy landscape,
  much like a spin network with frustrated loops". Making the target the
  ground state by tuning in-plane angles "does not change the glassy
  attractor structure".
- **Large patterns.** N_branches ∼ 2^(α√A), α ≈ 2.25 (Eq. 2). "The largest
  attractor for the 4 × 4 mesh sampled is only ≈ 17%"; "Simulations of a
  6 × 6 lattice suggest that no mode has an attractor size exceeding
  0.2%."
- **Actuation.** On "a random pattern with a chosen branch", torques
  "always of the correct sign (Mountain or Valley) needed at that crease
  for the chosen branch.": "actuators are needed on 18 out of a total of
  60 creases to even have a 50% probability of folding the pattern."
  Fig. 5 caption: "at least 18 actuators (∼ 30% of creases) are needed to
  have a 50% chance of successful folding". And: "Requiring a large number
  of actuators or precise control of torque magnitudes defeats the purpose
  of designing a single degree of freedom mechanism".
- **Folding islands.** The folding island of a crease is "the largest
  subset of the pattern that will fold in the desired branch, if that
  subset is cut out and actuated at the chosen crease." "a set of 5
  actuators is 60× more likely to fold the pattern if it has U F I = 1
  rather than U F I < 1."; the union of folding islands, "and thus spatial
  placement of actuators is a much better predictor of folding success
  than just the number of actuators."
- **An added actuator.** "adding another actuator with a very small
  folding island as in Fig. 5h, can stop the previously successful
  folding!" "Such effects reduce the probability of success in Fig. 5g when
  U F I = 1 to be less than 1". Fig. 5 caption: successful actuation "can
  sometimes be ruined by actuating an additional crease (orange) with a
  small folding island." The authors' limit: "we are unable to formulate a
  strict necessary and sufficient condition for successful folding without
  full pattern information."
- **Discussion.** "carefully choosing the set of actuated creases can
  reduce their number dramatically". Scope: the "need for careful actuation
  mathematically applies only at the flat state", but because barriers
  grow more slowly for softer sheets, "careful actuation needs to be
  maintained until a larger folding angle for soft sheets."

## Concepts

- **Distractor branch**: a folding branch of zero energy to linear order
  at the flat state but nonzero at higher order; a high-energy minimum, a
  dead end.
- **Mechanical advantage rule**: a vertex relaxes into the branch whose
  fold-angle vector has the larger normalized dot product with the applied
  torques; with one crease actuated, the branch in which that crease folds
  more.
- **Folding island**: as quoted above, the largest sub-pattern that folds
  correctly when cut out and actuated at a given crease.
- **UFI**: the fraction of creases in the union of the actuated creases'
  folding islands.
- **Glassy landscape**: an exponential number of local minima arising from
  frustrated interactions between binary degrees of freedom (the vertices'
  branch choices).

## Connections

It draws the analogy to kinetic traps in self-assembly, Levinthal's
paradox in protein folding and NP-hard satisfiability (SAT), and sets
itself apart from Bern and Hayes's NP-hardness of flat-foldability, which
concerns finding a consistent mountain–valley assignment rather than
whether folding physics reaches one. It cites Silverberg et al. (2014),
LIT-tmpa3uim, as ref. [2], an application of self-folding, and Silverberg
et al. (2015), LIT-tmptep4g, as ref. [37], for the nonzero energy of an
over-determined vertex.

## Bearing on the record

- **The pasted synthesis on constraint architectures.** It cites this as
  S1. Its quoted sentences are A's paraphrase, not the paper's words, and
  each is right in substance.
  - "exponentially many competing folding branches near its unfolded
    configuration": right. The distractors are dead ends, not alternative
    folded shapes, which A does not say.
  - "In one simulated pattern with 60 creases, random actuator selection
    required approximately 18 actuators for a 50% success rate": right,
    with three qualifications. The caption says "at least 18". The
    actuators are fixed-torque, on randomly chosen creases, with signs
    already matched to the target. And it is one 4 × 4 pattern. A omits the
    paper's main point about that figure: count is a poor predictor and
    placement (UFI = 1) a much better one, five well-placed actuators
    succeeding 60 times as often.
  - "the authors also exhibit cases in which adding an actuator undermines
    an otherwise successful folding process": right (Fig. 5h). The paper
    explains it as competition between actuators, with misfolding just
    outside the small island, and presents it as something that "can
    sometimes" happen.
  - A's step to "greater intervention need not improve success
    monotonically" goes further than the paper shows. One added actuator
    ruins one success; with randomly placed actuators the paper's
    statistic is of success that needs more of them, 18 for an even
    chance.
  - A misses the scope: the difficulty "mathematically applies only at the
    flat state". A's "existence ≠ reliable emergence" is a fair gloss: the
    designed branch exists, can even be made the ground state, and is hard
    to reach.
- **TERM-060 (frustration of an organization's demands).** The term covers
  both structural frustration (no admissible transformation meets all the
  demands) and frustration by governance (one exists and is not
  selected); A glosses it as "structural frustration" only. Stern et al.'s
  failure mode, a feasible target that goes unreached because of where the
  system is pushed, sits nearer the governance and non-attainment side,
  which TERM-060's note of 2026-10-18 cautions against calling frustration
  ("Unmet is not obstructed"). Their own frustration is energetic, nonzero
  κρ⁴ branch energies, so it is a quantitative physical refinement of a
  combinatorial shape the record knows, not an instance of TERM-060. A's
  claim that the record's structural frustration is "an ordinal fact" is
  right and close to CLAIM-347's title, and A's contrast with mechanical
  frustration as stress or energy is the one TERM-060 already draws.
- **CLAIM-347 (jointly satisfiable demands form a downward-closed
  complex).** Qualifies. Every chain of 4-vertices has a zero-energy
  branch assignment and closing the loop removes it, so the minimal
  obstruction is a closed loop, here of four, the smallest loop in a
  quadrilateral mesh, as CLAIM-153 has a minimal model of three. But the
  designed branch is jointly realizable: frustration afflicts the
  distractors and makes the target hard to reach, not empty.
- **CLAIM-357 (structural infeasibility, realized violation and minimax
  suboptimality are separate).** Supports, by analogy: a feasible
  configuration (the designed branch) exists and goes unrealized under a
  given actuation. Misfolding is realized failure with no structural
  infeasibility.
- **CASE-119 (three demands, every pair satisfiable, the triple not).**
  Supports its use as the combinatorial twin of a frustrated vertex loop.
- **CLAIM-185 (nucleation threshold) and CLAIM-184 (anchors entrench).**
  Qualify. Folding islands are local seeds that fix a global outcome; the
  early branch choice locks in, there being no backtracking at zero
  temperature, and a badly placed seed locks in a distractor. A is right
  that this is "not automatically a nucleation site in the strict
  thermodynamic sense": no thermal barrier is crossed.
- **CLAIM-478 (scale separation makes constraints).** Weak. The paper notes
  that barriers between branches grow more slowly for softer sheets, so
  how far careful actuation must be kept up depends on stiffness; it does
  not frame this as an effective constraint.
- **QUESTION-281** (dynamical transitions, including nucleation across a
  finite barrier): related by name only, since the dynamics are
  zero-temperature descent. THEORY-1087 (frustration on a Kuramoto cycle)
  is a neighbouring case of loop frustration, different in mechanism.
  THEORY-272 and THEORY-521 are the record's nearest glassy-landscape
  entries, unrelated in content. CLAIM-480 is unrelated to these results.
- Filed: THEORY-tmpq2qdv. No instruction for machine-learning practice;
  nothing for the anthology.

## Limitations

- **The authors'.** No necessary and sufficient condition for success; the
  flat-state scope; folding islands only approximately deduced by the
  mountain–valley propagation rule, their exact shape depending on the
  in-plane angles.
- **Idealized.** Rigid-panel vertices and a model energy; the robustness
  checks the paper refers to are in the SI, not read.
- **One pattern** for the actuation statistics.
- **An analogy, not a reduction.** The link to SAT and protein folding is
  drawn by the authors without a hardness proof.
- **Noise-free.** Thermal or stochastic folding is not treated.
- **The preprint, not the published version.** The published text was not
  read and may differ in wording, figures and appendices.
