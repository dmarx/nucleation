---
number: 916
status: Proposed
formerly:
- THEORY-tmphmdtd
promote_when: >-
  A checked re-derivation, recorded here and gone through by a second
  checker (ADR-065 §5), of Lemmas 3.1 and 3.2, Theorem 4.1, Proposition
  4.2 and the Section 5 result, since this reading skimmed the proofs; or
  a published independent proof or extension that restates Theorem 4.1
  and Proposition 4.2. The theorems are refuted only by an error in the
  proofs. Simulations of the model cannot settle it.
title: "In the DeGroot–Friedkin model, where a group reaches DeGroot consensus on each issue and each member's self-weight on the next issue equals their control over the last, with fixed relative interpersonal weights that form a strongly connected network, self-weights converge from every non-autocratic start to one equilibrium ordered by the eigenvector centralities of those weights: power accumulates above a centrality threshold, is autocratic exactly when the network is a star and democratic exactly when it is doubly stochastic; and in the networks that are not strongly connected that the authors treat, members to whom some other member does not listen, even indirectly, end with none"
version: 2
history:
- version: 2
  date: '2026-10-30'
  note: >-
    The twenty-third status review, at the status review's ruling (the
    owner delegated these rulings; ADR-065, ADR-058). The title is
    narrowed to the paper's scope (NOTE-1135): Theorem 4.1 assumes a
    strongly connected network, and Section 5's zero-power result is for
    the reducible case the authors treat, where every member who is not
    globally reachable ends with none, not only members no path reaches
    (ADR-047 kind 3). The old title: "In the DeGroot–Friedkin model, where
    a group reaches DeGroot consensus on each issue and each member's
    self-weight on the next issue equals their control over the last,
    with fixed relative interpersonal weights, self-weights converge from
    every non-autocratic start to one equilibrium ordered by the
    eigenvector centralities of those weights: power accumulates above a
    centrality threshold, is autocratic exactly when the network is a
    star and democratic exactly when it is doubly stochastic, and members
    whom no path of influence reaches end with none". The promote_when now
    asks only for what the title asserts, the proofs (ADR-065 §1). Its
    second part, a test in groups, asks whether real groups behave as the
    model does, which the authors do not assert ("an assessment of the
    validity of the model has just begun", p. 386), so it moves to
    QUESTION-348 (ADR-047 kind 4). The old promote_when: "Two things.
    First, the proofs checked by a reader of this record (or a published
    independent proof or extension that restates Theorem 4.1 and
    Proposition 4.2), since this reading skimmed them. Second, because the
    record would lean on the model as a description of groups, a test in
    groups with a stable network of relative influence, measured
    independently of the members' self-weights, showing that their
    influence over outcomes across a sequence of issues orders as the
    network's eigenvector centralities and concentrates above them. It is
    refuted as a description if power in such groups orders otherwise, and
    the theorems are refuted only by an error in the proofs. Simulations
    of the model cannot settle the second part." CLAIM-448 moves from
    supports to corroborates (ADR-058): the claim cites the model as its
    baseline, a proved special case, and does not rest on it.
tags:
- network-science
- social-science
- mathematics
date: '2026-10-24'
source:
- LIT-1146
summary: >-
  Jia, MirTabatabaei, Friedkin & Bullo (2015), [LIT-1146](../literature.d/LIT-1146.md), read in
  [NOTE-1135](../notes.d/NOTE-1135.md) from the version of record posted on the author's site;
  proofs skimmed. Theorems about a model, not findings about groups. The
  empirical companion, [LIT-1482](../literature.d/LIT-1482.md) ([THEORY-902](THEORY-902.md)), uses anchored
  dynamics and a changing network, whose attractor is autocracy rather
  than this interior equilibrium.
corroborates:
- CLAIM-448
bears_on:
- QUESTION-348
---
<!-- inactive-ok-file: THEORY-321 LIT-1482 — Proposed or Deferred; the accounts and companion work this bears on, named, nothing here rests on them -->
<!-- inactive-ok-file: QUESTION-348 — Open; the question the condition's test in groups moved to -->
<!-- inactive-ok-file: THEORY-1161 — Proposed; the Friedkin–Johnsen comparison, cited in the note of 2026-10-29 as open -->

# THEORY-916: In the DeGroot–Friedkin model, where a group reaches DeGroot consensus on each issue and each member's self-weight on the next issue equals their control over the last, with fixed relative interpersonal weights that form a strongly connected network, self-weights converge from every non-autocratic start to one equilibrium ordered by the eigenvector centralities of those weights: power accumulates above a centrality threshold, is autocratic exactly when the network is a star and democratic exactly when it is doubly stochastic; and in the networks that are not strongly connected that the authors treat, members to whom some other member does not listen, even indirectly, end with none

## Source

Jia, MirTabatabaei, Friedkin & Bullo, [LIT-1146](../literature.d/LIT-1146.md), read in [NOTE-1135](../notes.d/NOTE-1135.md):
Lemmas 2.2–3.2, Theorem 4.1, Proposition 4.2 and Section 5 (pp. 376–385),
with proofs in Appendices B–G, skimmed.

## What was actually shown

A proof, not an experiment. The model: on each issue, opinions follow
DeGroot averaging with W(x) = diag(x) + (I − diag(x))C and reach
consensus; then x(s+1) = w(x(s)), the dominant left eigenvector of W.

- **The only parameter is c,** the eigenvector centrality of C (Lemma 2.2).
- **Interior equilibrium.** Unless C is a star, every non-autocratic start
  converges to one x*, ordered as c (Theorem 4.1).
- **Accumulation.** Above a threshold power exceeds centrality; below it,
  falls short (Proposition 4.2). "social power tends to accumulate at the
  top of the hierarchy" (p. 367).
- **The extremes.** A star converges to autocracy; a doubly stochastic C to
  equal power, and only then (Lemmas 3.1, 3.2).
- **The unreached.** With a reducible C, members not globally reachable
  end with zero power (Section 5); in Krackhardt's advice network, the four
  managers nobody consults.

## What this does not say

- **That groups behave this way.** The authors: "an assessment of the
  validity of the model has just begun" (p. 386).
- **That it is robust.** Anchored dynamics differ, and "At the present
  time, we cannot assert robustness" (p. 386).
- **That authority is chosen or maintained.** C is fixed and exogenous;
  nobody decides who is heard.
- **That the equilibrium is autocratic in general.** Only for a star.
  Short of that, the most central member gains disproportionately but does
  not take everything.

## Connections

- **[CLAIM-448](../claims.d/CLAIM-448.md).** The baseline it names, now in exact form. Every
  issue ends in consensus, so the record is always coherent; its content
  is weighted toward the central, and the unreached contribute nothing.
  That is a proved instance of coherence without integration, produced by
  uptake rather than by a regime of admission.
- **[THEORY-902](THEORY-902.md).** The experiment on the same mechanism under anchored
  dynamics.
- **[THEORY-321](THEORY-321.md).** Golub & Jackson's DeGroot result: a consensus is right
  in large societies only if no member's influence weight stays large.
  Under reflected appraisal the most central member's weight grows, which
  is the condition [THEORY-321](THEORY-321.md) says defeats the wisdom of crowds. That
  combination is the record's, not the paper's.

## Note of 2026-10-29: the same rule under the Friedkin–Johnsen step

Friedkin's reflected-appraisal theory, [LIT-1404](../literature.d/LIT-1404.md), read in [NOTE-1374](../notes.d/NOTE-1374.md),
uses the same appraisal rule with a different single-issue step:
Friedkin–Johnsen anchoring on initial positions instead of DeGroot
consensus. Its model differs, so it is not a counter-example to this
account. But the same rule gives autocracy under that step. Re-run as
printed on 300 random complete networks each of sizes 5, 10 and 20, every
one ended with one self-weight above 0.99; the DeGroot–Friedkin update on
100 random complete networks of sizes 5 and 10 gave a median largest
self-weight of 0.29 and 0.13, never above 0.40. The comparison is
[THEORY-1161](THEORY-1161.md), Proposed. This account is unchanged and stays Proposed.

## Note of 2026-10-30: what holds it back

The proofs of Lemmas 3.1–3.2, Theorem 4.1, Proposition 4.2 and Section 5
were skimmed, not checked step by step ([NOTE-1135](../notes.d/NOTE-1135.md)), and the record holds
no published independent proof. The title asserts the theorems, so it
waits on that check ([ADR-065](../decisions.d/ADR-065.md) §5). Whether groups behave as the model does
is [QUESTION-348](../questions.d/QUESTION-348.md).
