---
status: Active
status_note: >-
  read in full 2026-11-05 ([NOTE-tmp9dvve](../notes.d/NOTE-tmp9dvve.md)) from the arXiv v1 preprint,
  1703.04161v1, titled "The difficulty of folding self-folding origami";
  the published PRX version was not read. Worth reading as the case in
  which a target configuration exists and is designed to be the ground
  state, yet is hard to reach: a crease pattern with one designed folding
  motion still has exponentially many dead-end "distractor" branches at
  the flat state, from frustrated loops of two-branch vertices, so random
  actuation usually misfolds, and whether the actuated creases' "folding
  islands" cover the sheet predicts success better than how many creases
  are actuated. Its main limits: idealized rigid-panel vertices,
  zero-temperature descent, actuation statistics from one 4 × 4 pattern,
  an analogy to SAT and protein folding with no hardness proof, and a
  scope the authors limit to the flat state.
title: 'The Complexity of Folding Self-Folding Origami'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Registered and read on 2026-11-05 from the owner's pasted synthesis on
    FACT, rigidity, compliant mechanisms and origami (the pasted synthesis
    on constraint architectures, written by another assistant, A, in the
    same exchange as the emergency-readiness bibliography, pasted
    2026-11-04), which cites it as S1: Stern, Pinson & Murugan 2017, "The
    Complexity of Folding Self-Folding Origami", PRX 7, 041070,
    doi:10.1103/PhysRevX.7.041070. Citation checked against Crossref and
    the arXiv listing: Menachem Stern, Matthew B. Pinson and Arvind Murugan
    (University of Chicago), Physical Review X 7(4), 041070, journal
    article; Crossref gives online 22 December 2017.
    The only arXiv version, 1703.04161v1, was submitted on 12 March 2017
    under a different title, "The difficulty of folding self-folding
    origami"; `published:` is that date (ADR-002). A's attribution is
    right. Copy read: the arXiv v1 PDF (8 pp.), extracted by pdftotext.
    journals.aps.org returned a Cloudflare challenge and was not retried;
    a copy of the version of record obtained by another route was set
    aside unused, and nothing here rests on it. The published version was
    not read and may differ: its wording, figures and appendices are not
    reported here.
tags:
- natural-sciences
- complex-systems
- mathematics
date: '2026-11-05'
published: '2017-03-12'
arxiv: '1703.04161'
doi: '10.1103/PhysRevX.7.041070'
first_author: 'Stern'
keywords:
- 'self-folding origami'
- 'distractor branches'
- 'glassy energy landscape'
- 'frustrated loops'
- 'folding islands'
- 'actuation'
- 'mechanical advantage'
- 'satisfiability'
implementations: []
summary: >-
  Stern, Pinson & Murugan (2017), read from the arXiv v1 preprint. A
  generic 4-vertex has two folding branches meeting at the flat state.
  Around a loop of vertices three can choose freely and the fourth is
  over-determined, so most global branch choices have energy of order
  κρ⁴: a glassy landscape whose number of distractor branches grows as
  2^(α√A), exponentially in the sheet's boundary length, even when the
  designed branch is the ground state. Folding is zero-temperature descent
  from the flat state, so randomly placed actuators usually land in a
  distractor; on one 4 × 4 pattern 18 of 60 creases had to be actuated for
  a 50% chance. The union of the actuated creases' "folding islands"
  predicts success better than their number, and an extra actuator can
  ruin a successful folding.
---
<!-- inactive-ok-file: THEORY-tmpq2qdv — Proposed or new; cited from the reading of Stern, Pinson & Murugan (2017) as open -->

# LIT-tmpjjho1: The Complexity of Folding Self-Folding Origami

Stern, M., Pinson, M. B. & Murugan, A. (2017). The Complexity of Folding Self-Folding Origami. *Physical Review X* 7(4): 041070. doi:10.1103/PhysRevX.7.041070. Preprint: arXiv:1703.04161 ("The difficulty of folding self-folding origami").

## Key takeaways

*From the reading of the arXiv v1 preprint, [NOTE-tmp9dvve](../notes.d/NOTE-tmp9dvve.md). Quotes are the
preprint's, not the published text's.*

- **Distractors are inevitable.** "even crease patterns with only one
  designed folding motion inevitably contain an exponential number of
  ‘distractor’ folding branches accessible from a bifurcation at the flat
  state." (Abstract.)
- **Loops make the landscape glassy.** "loops of vertices have a glassy
  folding energy landscape, much like a spin network with frustrated
  loops"; designing the target branch "does not change the glassy attractor
  structure".
- **Count is a poor guide, placement a good one.** On one pattern
  "actuators are needed on 18 out of a total of 60 creases to even have a
  50% probability of folding the pattern."; "a set of 5 actuators is 60×
  more likely to fold the pattern if it has U F I = 1 rather than
  U F I < 1."
- **More can be worse.** "adding another actuator with a very small folding
  island as in Fig. 5h, can stop the previously successful folding!"
- **At the flat state.** The "need for careful actuation mathematically
  applies only at the flat state" (Discussion).

## Standing in the record

The pasted synthesis on constraint architectures cites it as S1, its first
priority: exponentially many competing branches near the unfolded state,
"folding islands", 18 actuators of 60 creases for a 50% success rate, an
added actuator that undermines successful folding, and links to glassy
landscapes and hard constraint satisfaction. All of that is in the
preprint. A leaves out three things. The 18 are randomly placed, with signs
already matched to the target, on one pattern. Placement predicts success
far better than count. And the difficulty is limited to the flat state.
The paper is the record's clearest physical case of A's "existence ≠
reliable emergence": the designed branch exists, and can be made the
ground state, yet is hard to reach. Its frustration is energetic, a
refinement of the loop shape behind [CLAIM-347](../claims.d/CLAIM-347.md) and [CASE-119](../cases.d/CASE-119.md) rather than an
instance of [TERM-060](../terms.d/TERM-060.md). Filed from it: [THEORY-tmpq2qdv](../theory.d/THEORY-tmpq2qdv.md).
