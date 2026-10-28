---
number: 1064
status: Active
formerly:
- THEORY-tmpaw7dg
title: 'In counterexample-guided abstraction refinement, a spurious counterexample locates the distinction its abstraction lacked: walking it forward through the concrete system, the first abstract state where no concrete continuation exists merges the states the trace can reach with the states that have the transition onward, and splitting them removes the counterexample; for finite-state programs and ACTL* properties whose counterexamples are paths or loops, repeating check and split ends in a real counterexample or a proof'
version: 1
tags:
- logic
- mathematics
date: '2026-10-27'
source:
- LIT-1652
summary: >-
  Clarke, Grumberg, Jha, Lu and Veith (2000), [LIT-1652](../literature.d/LIT-1652.md), read in
  [NOTE-1231](../notes.d/NOTE-1231.md) from the authors' manuscript of the CAV paper. Active: the
  test for spuriousness (Lemma 1), the three-way cut at the failing state
  and the termination argument are given in full. The NP-hardness of the
  coarsest split is stated with its proof omitted, and the loop case rests
  on a theorem proved elsewhere. It does not say that the split found is
  the smallest, or how many rounds are needed.
---
# THEORY-1064: In counterexample-guided abstraction refinement, a spurious counterexample locates the distinction its abstraction lacked: walking it forward through the concrete system, the first abstract state where no concrete continuation exists merges the states the trace can reach with the states that have the transition onward, and splitting them removes the counterexample; for finite-state programs and ACTL* properties whose counterexamples are paths or loops, repeating check and split ends in a real counterexample or a proof

## Source

Clarke, Grumberg, Jha, Lu and Veith (2000), [LIT-1652](../literature.d/LIT-1652.md), §§2–4 (pp. 4–13 of
the authors' manuscript in CMU's repository); read in [NOTE-1231](../notes.d/NOTE-1231.md).

## What was actually shown

**The setting.** A finite-state program, an abstraction h: D → D̂ that
merges concrete states, and the existential abstraction M̂, which has an
abstract transition wherever some concrete transition joins the merged
classes (p. 5). If the property's atoms respect h, M̂ ⊨ φ implies M ⊨ φ
(Theorem 1, p. 5). The converse fails: merging can add behaviour, as when
green and yellow merged into "go" give a traffic light a self-loop no
concrete state has (Example 1, p. 6).

**The test, which could come out either way.** For an abstract path
⟨ŝ₁, …, ŝₙ⟩, put S₁ = h⁻¹(ŝ₁) ∩ I and Sᵢ = Img(Sᵢ₋₁, R) ∩ h⁻¹(ŝᵢ). The
counterexample is real iff every Sᵢ is non-empty (Lemma 1, p. 9). If it is
real it is reported and the procedure stops; if not, there is a first i
with Sᵢ₊₁ = ∅. Loops reduce to paths after at most min_j |h⁻¹(ŝⱼ)|
unwindings (Theorem 2, p. 10; proof in the technical report).

**Where the distinction is.** At that i, h⁻¹(ŝᵢ) splits into S_{i,0}, the
states reachable along the trace, S_{i,1}, the states with a transition into
h⁻¹(ŝᵢ₊₁), and the rest. S_{i,1} is non-empty, since the abstract
transition exists, and disjoint from S_{i,0}, since Sᵢ₊₁ = ∅. "Since S_{i,1}
is not empty, there is a spurious transition ŝᵢ → ŝᵢ₊₁. This causes the
spurious counterexample T̂ … we need a refined abstraction function which
separates the two sets S_{i,0} and S_{i,1}" (p. 11). Any refinement that
separates them removes the counterexample.

**Which split.** The refinement partitions the component classes of a
product-form abstraction; its size is the number of new classes. "(i) The
problem of finding the coarsest refinement is NP-hard; (ii) when
S_{i,x} = ∅, the problem can be solved in polynomial time" (Theorem 3,
p. 11; the proof of (i), by reduction from PARTITION INTO CLIQUES, is
omitted). The implementation folds the remainder into S_{i,1} and takes the
coarsest refinement against that, which is "not optimal, but it is a
correct refinement" (p. 12).

**Termination.** Each round splits a class of a finite domain, so the
abstraction cannot be refined forever: "The partitioning procedure is
guaranteed to terminate since each equivalence class must contain at least
one element. Thus, our method is complete" (p. 12). Theorem 4 (p. 13): the
algorithm finds an M̂ with M̂ ⊨ φ ⇔ M ⊨ φ.

## What this does not say

- **That the split is the smallest.** The method uses a non-optimal split,
  and the optimal one is NP-hard in general by a theorem whose proof is not
  in this text.
- **That the loop is short.** No bound on the number of rounds is given;
  the guarantee is only that the rounds are finite, and in the worst case
  the abstraction becomes the concrete model.
- **Anything for infinite-state systems** or for counterexamples that are
  neither paths nor loops. Extension to all of ACTL\* is claimed "in
  principle" (p. 2), not shown.
- **That the refinement touches one abstract state only.** §3 says "a single
  equivalence class", but the refinement acts on component relations, so
  every abstract state sharing a split component class is split too (a
  reading of pp. 11–12 that the paper does not discuss).
- **That the method finds what is wrong with the property.** The property
  is fixed; see [THEORY-1094](THEORY-1094.md).
