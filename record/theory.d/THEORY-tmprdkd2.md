---
# Don't copy this file by hand — run `luria new theory`, which assigns the
# code and fills in what a machine can compute.
#
# A theory is a claim about WHY something happens, or about what is true of
# these systems. State it as a finding, not as an instruction: "Batch
# normalization helps by smoothing the optimization landscape" rather than
# "Use batch normalization". If what you are about to write tells the reader
# what to do in machine learning, it is a practice, and it belongs in the
# Anthology of the SOTA (ANTH-ADR-031).

# Active | Proposed | Deferred | Superseded | Rejected, optionally " — note".
# What each one means here is in luria.yaml, and it is NOT what the same word
# means on a practice: this status says whether the record believes the
# ACCOUNT, and an explanation can be `Rejected` while the thing it explained
# goes on working exactly as well as it ever did.
status: 'Proposed'

# REQUIRED while the status is Proposed or Deferred; delete it when the
# explanation goes Active. What would settle it — a KIND of result, not a
# quantity of them (ANTH-ADR-014). An explanation that cannot say what would show
# it wrong is a story, and this field is where that shows up.
promote_when: 'A system whose relevant variables were not known beforehand, in two or more dimensions, where the coarse-graining that maximizes mutual information with the environment beyond a buffer is computed, iterated, and gives critical exponents that agree with an independent method (high-precision Monte Carlo, series or conformal bootstrap) within stated errors, while a coarse-graining fitted to the data distribution on the same samples does not. Or a proof, for a class of local Hamiltonians in two or more dimensions, that the maximizer yields an effective Hamiltonian whose couplings decay with distance. More rediscoveries of block spins or of other variables already known cannot settle it, because the account was shown on exactly those.'

# The claim. Repeat it as the body's `# THEORY-tmprdkd2:` heading; the lint checks
# that the two agree.
title: 'The block coarse-graining that maximizes mutual information with the system beyond a buffer picks out the renormalization-group-relevant variables in general, so those variables can be found from samples by information alone, without being known beforehand, as Koch-Janusz and Ringel propose'

version: 1

# One or more topics from luria.yaml, primary first — the same table the
# reading list uses. Take the topic of what the account is about.
tags:
- natural-sciences
- information-theory
- representation-learning

date: '2026-10-20'

# There is deliberately no `published:` line. It is DERIVED from the first
# entry in `source:` below, and writing it down is a lint violation, because
# the value has one home and this is not it.

# REQUIRED, and a LIST. The papers this account rests on, primary first. An
# explanation with no paper behind it is a hunch, and the lint will say so.
source:
- LIT-873

# What the index table shows. The title already carries the claim, so spend
# this on provenance and on the sharp edge: who said it, and what it does not
# say. Prose, so bare codes in it get linked by `luria link --fix`.
summary: >-
  Koch-Janusz and Ringel (2017), [LIT-873](../literature.d/LIT-873.md), propose that their mutual-information criterion finds a system's relevant degrees of freedom with no prior knowledge of them. What the record holds as shown, [THEORY-194](THEORY-194.md), is that it recovered variables renormalization already uses, on 2D models whose answer was known. This is the general thesis that result was offered for, filed under [ADR-047](../decisions.d/ADR-047.md) v4 when the narrowing dropped it.
extends:
- THEORY-194
answers:
- QUESTION-232
---


# THEORY-tmprdkd2: The block coarse-graining that maximizes mutual information with the system beyond a buffer picks out the renormalization-group-relevant variables in general, so those variables can be found from samples by information alone, without being known beforehand, as Koch-Janusz and Ringel propose

## Source

Koch-Janusz and Ringel (2017; Nature Physics 2018), [LIT-873](../literature.d/LIT-873.md), read in
[NOTE-674](../notes.d/NOTE-674.md). The abstract and closing discussion present the RSMI algorithm
as a way to find relevant degrees of freedom without prior knowledge of
them, and so as a route to renormalization in systems whose variables are
not known.

## What is asserted

That maximizing the mutual information between a block's coarse variable
and the environment beyond a buffer is a general criterion for the
renormalization-group-relevant variables, and not only one that agrees
with renormalization where its variables were already known. The authors
also contrast it with coarse-grainings fitted to reproduce the data
distribution, which on their noisy dimer data coupled to the noise.

## What the record holds toward it

[THEORY-194](THEORY-194.md), Active, is the measured part: on the 2D Ising and noisy 2D
dimer models the criterion recovered Kadanoff block spins and the dimers'
low-momentum electric fields, and iterated on Ising samples it located the
critical point to about 1% with ν ≈ 1.0 ± 0.15. Every case had a known
answer. The equivalence with a compact, short-ranged effective Hamiltonian
is proved only for 1D and quasi-1D chains. Whether the criterion finds the
variables where they are unknown is what [QUESTION-232](../questions.d/QUESTION-232.md) asks; this THEORY is
the proposed answer.

## What this does not say

- Not that distribution-fitting coarse-grainings always fail. One dataset
  shows they need not succeed.
- Not that the criterion is computable at scale; the published runs are
  small lattices.

## What would confirm or reject it

It is confirmed by the promote_when: a system with unknown relevant
variables where the iterated criterion gives critical exponents matching an
independent method, or a proof of short-ranged effective couplings in two
or more dimensions. It is in trouble if, on such a system, the
information-maximizing variables give a flow whose exponents disagree with
an independent determination, or an effective Hamiltonian that is not
short-ranged.
