---
number: 172
status: Open
formerly:
- QUESTION-tmpq0kil
title: "Does a transient change to one regulator, released with the environment held fixed, leave a bacterium's other genes in a changed expression state for many generations once slow return is excluded?"
version: 1
tags:
- complex-systems
- network-science
- natural-sciences
date: '2026-10-19'
line: nucleating-argument
summary: >-
  The promotion condition formerly on [THEORY-178](../theory.d/THEORY-178.md), moved here when [THEORY-178](../theory.d/THEORY-178.md)
  was narrowed to the Boolean model ensemble it was shown in and promoted on
  2026-10-19 ([ADR-047](../decisions.d/ADR-047.md) v3). [LIT-854](../literature.d/LIT-854.md) predicts lasting expression changes after
  a transient single-gene perturbation of E. coli's regulatory core, but no
  such perturbation has been done in cells. Filed under the
  nucleating-argument line because [CLAIM-184](../claims.d/CLAIM-184.md), the claim that grounds on
  [THEORY-178](../theory.d/THEORY-178.md), reads it as evidence about what a lasting state needs.
answered_by:
- THEORY-tmp0drff
---

# QUESTION-172: Does a transient change to one regulator, released with the environment held fixed, leave a bacterium's other genes in a changed expression state for many generations once slow return is excluded?

## Why it is a question

Zhao, Wytock, Reynolds and Motter ([LIT-854](../literature.d/LIT-854.md), read in full in [NOTE-655](../notes.d/NOTE-655.md)) show
that in an ensemble of sign-consistent Boolean rules on the 87-gene core of
the E. coli regulatory network, clamping one gene and releasing it often
leaves the network in a different attractor ([THEORY-178](../theory.d/THEORY-178.md)). In the model the
new state is permanent by construction. In cells, noise and division may
make it only long-lived, as the authors expect. The one comparison with
data is evolution under a permanent crp knockout, which is not a temporary
disturbance. [NOTE-655](../notes.d/NOTE-655.md) lists the cell experiment as its first open question.
Until 2026-10-19 it was [THEORY-178](../theory.d/THEORY-178.md)'s promote_when. [THEORY-178](../theory.d/THEORY-178.md)'s body
disclaimed it, so the clause moved here when the title was narrowed to the
model.

## What would answer it

An experiment in bacteria, read first-hand, in which a gene is perturbed
transiently (for example by inducible CRISPR interference, then released)
with the growth environment held fixed, and other genes stay in their
changed expression state for many generations after the perturbation is
gone. Slow return must be excluded ([THEORY-136](../theory.d/THEORY-136.md)'s standard): either by
following the culture until the state has outlasted any plausible
relaxation time, or by showing that unperturbed cells started from the
other state hold it under the same conditions. The paper's candidates are
crp as the perturbed gene, with zraR, melR or rhaRS as responders. It would
answer no for this network if well-powered transient perturbations of
those genes are always followed by a return to the starting state.

What would not answer it: further simulations or rule ensembles; agreement
with strains evolved under a permanent knockout; and environmentally
induced bistable switches such as the lac operon, which were known before
and are not perturbations of regulation alone.
