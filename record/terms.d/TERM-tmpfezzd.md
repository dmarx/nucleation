---
status: Active
title: 'closure, and which sense'
version: 2
history:
- version: 2
  date: '2026-10-21'
  note: >-
    Adopted by the owner at the second review of nucleation#305, 2026-10-21:
    status Proposed → Active. The definition is unchanged.
tags:
- complex-systems
- information-theory
- philosophy-of-biology
date: '2026-10-21'
line: formal-apparatus
summary: >-
  The record uses "closure" in at least eight senses and no entry says
  which is meant. This term lists them so that a claim using the word says
  which, as [TERM-045](TERM-045.md) does for "self". Sense 1, informational closure, is
  defined in full: I(X⃗_t; Z_{t+1} | Z⃗_t) = 0, which for a stationary
  discrete process is one condition with Barnett and Seth's dynamical
  independence and with causal closure ([THEORY-820](../theory.d/THEORY-820.md)), and is no mark of a
  system. Asked for at A11 of the exchange of 2026-10-20 ("That single
  disambiguation entry could save substantial rediscovery"), and at A12,
  A13 and A14, on the owner's U11 and U13. Adopted by the owner on
  2026-10-21. It adopts no definition the record does not already hold.
used_by:
- CLAIM-tmpshzxc
---
<!-- inactive-ok-file: CLAIM-119 CLAIM-172 CLAIM-341 CLAIM-347 — Proposed; named only for the homonym or the sense they use, nothing here rests on them -->
<!-- inactive-ok-file: THEORY-072 THEORY-071 — Proposed; the demarcation and agency readings that use organizational closure, cited as open -->

# TERM-tmpfezzd: closure, and which sense

## Definition

"Closure" in this record means one of the following, and a claim should say
which.

1. **Informational closure,** of a coarse-graining of a process.
   X is a stationary process with a discrete alphabet, X⃗_t its past up to
   t, and Z_t = g(X⃗_t) a coarse-graining, spatial if Z_t = f(X_t). Z is
   **informationally closed** when its own past carries everything the
   micro past carries about its future:

   Δ_X(Z) = I(X⃗_t; Z_{t+1} | Z⃗_t) = 0.

   This is transfer entropy from the micro past with Z's whole history and
   no environment ([TERM-057](TERM-057.md) with k and l unbounded). A12 wrote it as
   Δ_X(Z) = I(X_{≤t}; Z_{t+1} | Z_{≤t}) and Closed_X(Z) ⟺ Δ_X(Z) = 0. What
   the record holds of it ([THEORY-820](../theory.d/THEORY-820.md)):
   - *Every horizon reduces to one step,* so the definition is not
     relative to a horizon ([THEORY-820](../theory.d/THEORY-820.md) (a)).
   - *It is dynamical independence.* That is Barnett and Seth's condition
     ([LIT-979](../literature.d/LIT-979.md); [THEORY-733](../theory.d/THEORY-733.md) for the linear Gaussian form).
   - *It is causal closure,* Z's ε-machine coinciding with its υ-machine
     ([THEORY-820](../theory.d/THEORY-820.md) (c); [TERM-tmp23du2](TERM-tmp23du2.md)).
   - *It is not preserved by refinement, nor by coarsening* ([CLAIM-tmpshzxc](../claims.d/CLAIM-tmpshzxc.md)).

   It is used, with no TERM until now, in [THEORY-820](../theory.d/THEORY-820.md), [THEORY-822](../theory.d/THEORY-822.md),
   [THEORY-733](../theory.d/THEORY-733.md), [CLAIM-386](../claims.d/CLAIM-386.md), [CLAIM-388](../claims.d/CLAIM-388.md), [CLAIM-389](../claims.d/CLAIM-389.md), [CLAIM-394](../claims.d/CLAIM-394.md), [CLAIM-398](../claims.d/CLAIM-398.md),
   [CASE-120](../cases.d/CASE-120.md), [QUESTION-218](../questions.d/QUESTION-218.md), [QUESTION-221](../questions.d/QUESTION-221.md) and [QUESTION-222](../questions.d/QUESTION-222.md).
2. **Computational closure.** Z's causal states are a coarse-graining of
   X's. It follows from 1 for spatial maps only, and does not imply it
   ([THEORY-820](../theory.d/THEORY-820.md) (e) and its Counterexample 4).
3. **Strong lumpability.** Every state of a block sends equal probability
   into each block. It makes the label closed, and is equivalent to closure
   for a closed label that is Markov ([THEORY-822](../theory.d/THEORY-822.md)).
4. **Vanishing Mori–Zwanzig memory.** In a linear Gaussian VAR(1) it
   follows from 1 and does not imply it ([CLAIM-389](../claims.d/CLAIM-389.md), [CLAIM-397](../claims.d/CLAIM-397.md), [CLAIM-398](../claims.d/CLAIM-398.md)).
5. **Linear one-step closure defect.** QA − ÂQ of the Simon–Ando aggregate
   ([CLAIM-386](../claims.d/CLAIM-386.md)), a matrix, not a condition.
6. **Organizational closure of constraints** ([TERM-tmpnjo1t](TERM-tmpnjo1t.md); [THEORY-072](../theory.d/THEORY-072.md),
   [CLAIM-395](../claims.d/CLAIM-395.md)). A set of constraints each produced by and productive of
   another in the set. Mossio, Saborido and Moreno's 2009 closure, which a
   candle flame has ([LIT-570](../literature.d/LIT-570.md), inside [THEORY-072](../theory.d/THEORY-072.md)), is a weaker neighbour.
   [THEORY-071](../theory.d/THEORY-071.md)'s "autonomy" and "self" mean this sense, and [CLAIM-172](../claims.d/CLAIM-172.md)'s
   "operational closure" is the enactive form.
7. **Homonyms, not the argument's:** the closure of a belief set under
   consequence ([CLAIM-294](../claims.d/CLAIM-294.md)), Galois closures ([CLAIM-119](../claims.d/CLAIM-119.md)), a downward-closed
   complex ([CLAIM-347](../claims.d/CLAIM-347.md)), and an observer's feedback closure and semantic
   closure ([CLAIM-341](../claims.d/CLAIM-341.md)).

## What it is not

- **Not one property with several aspects.** 1 and 6 concern different
  objects: a variable's law, and a set of constraints. Noise has 1
  ([THEORY-820](../theory.d/THEORY-820.md): "An i.i.d. noise component is closed"); nothing shows a
  flame has 6 under the 2015 definitions. [QUESTION-093](../questions.d/QUESTION-093.md) asks which of them
  an agent needs.
- **Not a mark of a system,** in sense 1. Whether a closed variable is one
  system is [QUESTION-218](../questions.d/QUESTION-218.md)'s open half.
- **"Computational closure" is not computational tractability.** A11: "The
  similarity in names makes this an especially plausible source of future
  confusion."
- **"Causal closure" in sense 1 is closure in the Granger sense** unless X
  is fully observed ([THEORY-820](../theory.d/THEORY-820.md): "Not interventional causation unless X is
  fully observed").
- **Informational closure and "causal-state closure" are not two senses.**
  A11's and A14's tables listed them apart. [THEORY-820](../theory.d/THEORY-820.md) (a) and (c) prove
  they are one condition for stationary discrete processes.
- **Common refinement is a meet** in [THEORY-820](../theory.d/THEORY-820.md)'s convention. A13 writes
  the common refinement of A and B as A ∨ B. A claim using either symbol
  should say which order it means.
