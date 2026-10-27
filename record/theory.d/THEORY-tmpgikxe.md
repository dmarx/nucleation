---
status: Active
title: 'The inputs causal scrubbing samples for a treeified hypothesis are the unique maximum-entropy distribution, on finite inputs, among those that give the inputs of every interpretation node the joint distribution they have on the data, so whatever the hypothesis does not claim is resampled as independently as the claims allow'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed Active from NOTE-tmpymmuh. It is the appendix post's Lemma 1 and
    Theorem 2. The record re-derived the proof's steps and checked the
    theorem numerically: in five random cases of a two-leaf hypothesis on
    six inputs, iterative proportional fitting to the constraints from the
    uniform distribution converged to the algorithm's distribution (largest
    difference below 1e-15, equal entropies). Lemma 1's statement is
    corrected from "product" to "joint" distribution, as its proof shows.
tags:
- causality
- information-theory
date: '2026-10-27'
source:
- LIT-tmpt2u54
summary: >-
  Chan, Garriga-Alonso, Goldowsky-Dill, Greenblatt et al. (2022),
  [LIT-tmpt2u54](../literature.d/LIT-tmpt2u54.md), read in [NOTE-tmpymmuh](../notes.d/NOTE-tmpymmuh.md), §5. Every node's datum is
  distributed as D, so each node's scrubbed inputs are jointly as on the
  data, and among all distributions with that property the algorithm's
  has the greatest entropy. It characterizes the sampling, not the score:
  it does not say that a hypothesis whose score matches the model is
  true, and the same appendix's §7 builds one that is false.
---
<!-- inactive-ok-file: CLAIM-454 — Proposed; the claim this bears on, cited as open -->

# THEORY-tmpgikxe: The inputs causal scrubbing samples for a treeified hypothesis are the unique maximum-entropy distribution, on finite inputs, among those that give the inputs of every interpretation node the joint distribution they have on the data, so whatever the hypothesis does not claim is resampled as independently as the claims allow

## Source

Chan, Garriga-Alonso, Goldowsky-Dill, Greenblatt, Nitishinskaya,
Radhakrishnan, Shlegeris and Thomas (2022), *Causal scrubbing: Appendix*,
[LIT-tmpt2u54](../literature.d/LIT-tmpt2u54.md), §5 ("An alternative formalism: constructing a distribution
on treeified inputs"), read in full in [NOTE-tmpymmuh](../notes.d/NOTE-tmpymmuh.md).

## What was actually shown

**The setting.** An isomorphic treeified hypothesis h = (G_T, I_T, c_T)
for f, with the input repeated n times, D a distribution on X, and D̃
the distribution on Xⁿ that the algorithm produces. On a consistent input
(x, …, x) with x ∼ D, each node u of I_T has "f-consistent" inputs. On
the algorithm's sample it has "scrubbed" inputs.

**Lemma 1.** The datum assigned to every node is distributed as D. The
root's is D by construction. A child's is drawn from D conditioned on
agreeing with its parent's datum on the child's value, and a draw from D
restricted to the equivalence class of a D-distributed point is again D.
So the scrubbed inputs to u are jointly distributed as its f-consistent
inputs. The post's statement says "product distribution"; its proof
shows the joint, and Theorem 2 needs the joint.

**Theorem 2.** D̃ is the maximum-entropy distribution on Xⁿ subject to
Lemma 1's constraints, and for finite X it is unique (strictly concave
entropy, linear constraints). The proof moves a minimal cut up through
I_T one node at a time. With x a node's inputs, y = u(x) its output and z
the rest of the cut, H(x, z) = H(y, z) − I(x; z | y) + H(x) − H(y). The
constraints fix H(x) − H(y). The inductive hypothesis maximizes H(y, z).
The algorithm makes x and z independent given y, so I(x; z | y) = 0 and
H(x, z) is maximal.

**The record's check.** Take X of six points with a random D, a root that
reads h₁(x₁) ∈ {0, 1} and h₂(x₂) ∈ {0, 1, 2}, and random h₁, h₂. The
constraints are: x₁ ∼ D, x₂ ∼ D, and (h₁(x₁), h₂(x₂)) distributed as
(h₁(x), h₂(x)) for x ∼ D. Iterative proportional fitting from the
uniform distribution converges to the maximum-entropy distribution under
these linear constraints. In five random cases it agreed with the
algorithm's distribution to within 1e-15, with equal entropies (record
simulation, 2026-10-27).

## What this does not say

- **Nothing about the score.** The theorem characterizes the sampled
  inputs. It does not say that matching the model's loss makes a
  hypothesis true. §7 of the same post gives a false hypothesis that
  scores 2.625 against the model's 0.25.
- **Not that maximum entropy is the right null.** Independence of
  everything unclaimed is the authors' choice (§4.1). It is what lets
  omitted correlations raise a score (§6.1, [THEORY-tmpnu6ih](THEORY-tmpnu6ih.md)).
- **Not for non-isomorphic hypotheses** as written. §4.2 shows how to
  make a hypothesis isomorphic, and the grouping chosen changes D̃.
- **Not for infinite input spaces** as to uniqueness.

## Connections

- **[THEORY-978](THEORY-978.md).** The constraints depend on each node only through the
  equivalence classes it induces on X. Two hypotheses that induce the
  same classes therefore define the same D̃ and the same score. The tie
  that account derives from the pseudocode follows from this theorem.
- **[THEORY-tmpnu6ih](THEORY-tmpnu6ih.md).** The paren post's 3c and 3d are this independence
  at work: more terms resampled separately, more entropy, a signal
  washed out, a higher score.
- **[CLAIM-454](../claims.d/CLAIM-454.md).** What the scrub preserves is each node's partition of the
  data and nothing more, by theorem.
