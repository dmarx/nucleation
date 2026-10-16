---
status: Active
title: "In the donation game, where a cooperator pays c for another to get b, defectors win in a well-mixed population, and each of five mechanisms makes cooperators evolutionarily stable above a benefit-to-cost threshold: kin selection r > c/b, direct reciprocity w > c/b, indirect reciprocity q > c/b, network reciprocity b/c > k and group selection b/c > 1 + n/m; the rules cover altruism only, not mutualism, coordination or conflict"
version: 1
tags:
- natural-sciences
- game-theory
date: '2026-10-16'
source:
- LIT-501
extends:
- THEORY-tmp15rjw
- THEORY-tmpxorvn
summary: >-
  Nowak (2006), [LIT-501](../literature.d/LIT-501.md), read in [NOTE-409](../notes.d/NOTE-409.md), main text only. A four-page review
  that casts each known mechanism as a 2×2 game so that one set of criteria
  applies to all. The five ESS conditions are confirmed by the main text; the
  derivations are in the supporting material, which was not read, and in
  cited papers. Several rules hold only under weak selection, regular graphs
  or rare group splitting. Every mechanism is modelled with the donation
  game, so mutualism, coordination and conflict are outside it.
---

<!-- inactive-ok-file: LIT-503 — Proposed: Curry 2016, the statement of morality-as-cooperation; cited for listing this review as incomplete -->
<!-- inactive-ok-file: LIT-495 — Unavailable: Alexander 1987, The Biology of Moral Systems; cited as the source of the review's one sentence on morality -->

# THEORY-tmpkifk7: In the donation game, where a cooperator pays c for another to get b, defectors win in a well-mixed population, and each of five mechanisms makes cooperators evolutionarily stable above a benefit-to-cost threshold: kin selection r > c/b, direct reciprocity w > c/b, indirect reciprocity q > c/b, network reciprocity b/c > k and group selection b/c > 1 + n/m; the rules cover altruism only, not mutualism, coordination or conflict

## Source

Nowak (2006), "Five Rules for the Evolution of Cooperation", [LIT-501](../literature.d/LIT-501.md)
(*Science* 314: 1560–1563), read in [NOTE-409](../notes.d/NOTE-409.md). The main text, figure
captions, Table 1 and references were read. Table 1's matrices and its
risk-dominance and advantageousness columns did not survive extraction. The
supporting material with the derivations was not read.

## What was actually shown

**The baseline (Fig. 1).** In a well-mixed population of N with i
cooperators, f_C = b(i − 1)/(N − 1) − c and f_D = bi/(N − 1). Defectors
always do better, and selection lowers mean fitness.

**The five rules (eqs. 1–5).** Kin selection, r > c/b, by the inclusive-
fitness method. Direct reciprocity, w > c/b, with TIT FOR TAT against
always-defect over an expected 1/(1 − w) rounds. Indirect reciprocity,
q > c/b, where q is the probability of knowing a recipient's reputation.
Network reciprocity, b/c > k, on a regular graph with k neighbours under
weak selection. Group selection, b/c > 1 + n/m, with m groups of maximum
size n, under weak selection and rare splitting.

**Three criteria.** With a 2×2 matrix (a, b; g, d), cooperators are an ESS
if a > g, risk-dominant if a + b > g + d, and advantageous if
a + 2b > g + 2d. For kin selection, network reciprocity and group selection
the rule makes cooperators dominate, so it gives all three. For the two
reciprocities it gives the ESS condition, and the other two criteria need
"slightly more stringent conditions".

**The common thread.** Every mechanism makes cooperators meet cooperators
more often than chance would, and its rule says how much more is needed per
unit of b/c ([NOTE-409](../notes.d/NOTE-409.md)'s reading).

**What could have come out otherwise.** A mechanism could have resisted
reduction to a single threshold. None of the five does.

## What this does not say

- **Anything about mutualism, coordination, contests, division or
  possession.** The donation game has none. Morality-as-cooperation ([LIT-503](../literature.d/LIT-503.md),
  Table 3) lists this review as incomplete for that reason.
- **That the rules hold outside their models.** Several need weak selection,
  regular graphs or rare splitting.
- **That punishment is ruled out.** The claim that punishment "is not a
  mechanism for the evolution of cooperation" is a survey claim: every model
  of it so far rests on one of the five.
- **That indirect reciprocity produced morality.** One sentence says it
  "leads to the evolution of morality and social norms", citing Alexander
  ([LIT-495](../literature.d/LIT-495.md)). That is an assertion, and nothing in the review tests it.
- **That the five are distinct.** The closing paragraph allows that all may
  be expressible as kin selection in a broad, Price-equation sense. The
  review does not settle it, and Nowak's later work is among the
  criticisms of that Price-equation view which Luque answers ([LIT-205](../literature.d/LIT-205.md)).

## Connections

- It extends Hamilton's threshold ([THEORY-tmp15rjw](THEORY-tmp15rjw.md)), restated as r > c/b,
  and Axelrod & Hamilton's stability condition ([THEORY-tmpxorvn](THEORY-tmpxorvn.md)),
  specialized to the donation game as w > c/b.
- Network reciprocity and group selection are routes to altruism. They do
  not map onto morality-as-cooperation's group domain, which is mutualism
  and coordination ([NOTE-409](../notes.d/NOTE-409.md)).
- Luque's analysis of the Price equation ([LIT-205](../literature.d/LIT-205.md), [NOTE-101](../notes.d/NOTE-101.md)) defends the
  equation against critics who later include Nowak & Highfield (2011). The
  tension is between Nowak's later work and this paper.
- Lloyd's entry ([LIT-160](../literature.d/LIT-160.md)) treats the multilevel-selection debate that the
  fifth rule enters.
