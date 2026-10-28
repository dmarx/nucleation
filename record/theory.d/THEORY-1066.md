---
number: 1066
status: Active
formerly:
- THEORY-tmpc8ml4
title: 'In constructor theory, a set of attributes is an information variable when every permutation of it and its cloning are possible tasks, and distinguishability is defined afterwards, as the possibility of mapping a variable onto an information variable; so information is fixed by counterfactual properties of a substrate without presupposing distinguishability, and instantiating it is stated as an intrinsic property of the substrate in the sense of referring to no other specific substrate'
version: 1
tags:
- information-theory
- quantum-foundations
date: '2026-10-27'
source:
- LIT-1663
summary: >-
  Deutsch & Marletto (2015), [LIT-1663](../literature.d/LIT-1663.md), §§3–5, read in [NOTE-1219](../notes.d/NOTE-1219.md).
  Active as a fact about the construction: the definitions are given in
  that order, and the base they give the recursion of (1.1) is checkable on
  the page. It does not say that these notions are the intuitive ones, which
  the authors disclaim, nor that the principles built on them hold. Its
  "intrinsic" excludes reference to a specific other substrate, not to
  generic ones, which the cloning task and (5.1) both use.
---

# THEORY-1066: In constructor theory, a set of attributes is an information variable when every permutation of it and its cloning are possible tasks, and distinguishability is defined afterwards, as the possibility of mapping a variable onto an information variable; so information is fixed by counterfactual properties of a substrate without presupposing distinguishability, and instantiating it is stated as an intrinsic property of the substrate in the sense of referring to no other specific substrate

## Source

Deutsch & Marletto (2015), [LIT-1663](../literature.d/LIT-1663.md), §§1–5; read in [NOTE-1219](../notes.d/NOTE-1219.md)
from the published JATS XML (CC BY 4.0).

## What was actually shown

**The problem.** A non-perturbing measurement (1.1) takes a blank receiver
state *b* to *x* or *y* while leaving the message unchanged. But "this does
not, in fact, distinguish message *x* from message *y* unless the resulting
*receiver* states *x* and *y* are themselves distinguishable". Taken as a
definition, (1.1) is "*recursive*", and orthogonality would not do as its
base, because one would then have to say "*what it is* about orthogonal
states that would make them usable for communication" (§1).

**The order of the definitions.** A computation variable is a set *S* of at
least two attributes for which every permutation task
C_Π(S) = ⋃_{x∈S} {x → Π(x)} is possible with side-effects (§3). An
information variable is "a clonable computation variable", with cloning
R_S(x0) = ⋃_{x∈S} {(x, x0) → (x, x)} on **S**⊕**S** (4.1). Only then is *X*
distinguishable, when ⋃_{x∈X} {x → ψ_x} is possible with side-effects for
an information variable {ψ_x} (5.1). "That provides the base for the
recursive definition (1.1), because we have defined 'information variable'
above without reference to distinguishability, and only to the possibility
or impossibility of tasks (specifically, permutations and cloning)" (§5).

**Counterfactual and intrinsic.** "A substrate **S** *instantiates classical
information* if some information variable *S* of **S** is sharp, and if
giving it any of the other attributes in *S* was possible. Note that the
constructor-theoretic mode of explanation has allowed this to be expressed
as an exact, intrinsic property of the substrate" (§4). "Intrinsic" is
defined in §2: an attribute "that does not refer to any other specific
substrate".

The construction could have failed. Had information variable needed
distinguishability, the circle would have stayed. It does not, and that can
be checked on the page.

## What this does not say

- That the defined notions are the intuitive ones. "We think that these
  correspond reasonably closely to the intuitive concepts with those names,
  but our claims in no way depend on that being so" (§3).
- That information has its expected properties. "The most important
  properties of information do not follow from the definitions we have
  given" (§6). Those come from the conjectured principles III–IX, which are
  not established here.
- That an information medium is individuated with no reference to anything
  else. Cloning uses a second instance of the substrate, and (5.1) uses an
  information variable of some other medium. These are generic others, so
  the property is intrinsic only in the §2 sense. It is a modal property,
  not a relational constitution, and not a non-modal intrinsic nature.
- That possibility requires an actual constructor. "No perfect constructors
  exist in nature" (§2); a possible task is one the laws allow to be
  approximated without limit.
