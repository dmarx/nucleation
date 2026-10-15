---
number: 341
status: Active
formerly:
- THEORY-tmpd0cwf
title: "Inferring not-P from failure to prove P is a deduction only under two separate conditions: Clark shows that when every branch of the search for a proof of P ends in failure, not-P is a theorem of the completed database, and a search that does not finish licenses nothing; Reiter's closed-world assumption, adding the negation of every ground atom the database does not entail, keeps a consistent Horn database consistent and can make a disjunctive one inconsistent"
version: 1
tags:
- logic
- databases
date: '2026-10-15'
source:
- LIT-1087
- LIT-1088
summary: >-
  Clark (1978), [LIT-1087](../literature.d/LIT-1087.md), read in [NOTE-894](../notes.d/NOTE-894.md), and Reiter (1978),
  [LIT-1088](../literature.d/LIT-1088.md), read in [NOTE-899](../notes.d/NOTE-899.md) from his 1977 workshop report. Clark
  proves negation as failure sound with respect to the completed database
  (the clauses read as if-and-only-if definitions, plus axioms that
  distinct names denote distinct things), given a finite failure tree for
  some selection rule; it is incomplete in general. Reiter defines the
  closed-world assumption by entailment, reduces closed-world query
  evaluation to open-world atomic queries when the assumption is
  consistent, and shows it consistent for Horn and definite databases but
  not for Pa ∨ Pb. Soundness here is relative to the completion, not to
  the world, and neither paper says anything about a search cut short by
  time.
supports:
- CLAIM-306
- CLAIM-tmpfpvgq
---
<!-- inactive-ok-file: THEORY-tmpg43pg — Proposed; a survey's report of unread work, cited as such -->

# THEORY-341: Inferring not-P from failure to prove P is a deduction only under two separate conditions: Clark shows that when every branch of the search for a proof of P ends in failure, not-P is a theorem of the completed database, and a search that does not finish licenses nothing; Reiter's closed-world assumption, adding the negation of every ground atom the database does not entail, keeps a consistent Horn database consistent and can make a disjunctive one inconsistent

## Source

Clark (1978), [LIT-1087](../literature.d/LIT-1087.md), "Negation as failure", read in full in
[NOTE-894](../notes.d/NOTE-894.md) from the author's posted scan. Reiter (1978), [LIT-1088](../literature.d/LIT-1088.md),
"On closed world data bases", read in full in [NOTE-899](../notes.d/NOTE-899.md) from UBC
Technical Report 77-16, the version presented at the 1977 Toulouse
workshop; the printed chapter was not seen.

## What was actually shown

**Clark: the rule and its soundness.** A ground negative literal ~P is
taken as a lemma when the evaluation of P fails on every path, "where the
proof that P is not provable is always the exhaustive but unsuccessful
search for a proof of P." Theorem 2: "If for some literal selection rule
every branch of the evaluation tree of a query ←Q terminates with
failure, then ~(∃x1,...,xk)Q where x1,...,xk are the free variables of
Q, is a theorem of the completed data base." The completed database is
each relation's clauses read as the if-half of a definition, the
only-if half added, plus an identity theory: distinct constants are
unequal, constructors are free. By König's lemma such a failure tree is
finite. A branch that does not terminate yields no conclusion, and a
different selection rule can turn an infinite branch into a finite
failure tree.

**Clark: where it stops.** The evaluator is incomplete: "In general, no."
Negation applies only to ground literals, one evaluation tree is grown,
and there is no case analysis, so a consequence of the completed
database can be out of reach. It is complete for allowed queries on
hierarchical (non-recursive) databases (Theorem 4), "unfortunately, a
very strong constraint." Clark identifies his assumption with Reiter's
closed world in one paragraph and makes no formal comparison.

**Reiter: the closed-world assumption.** For a function-free database DB,
EDB-bar is the set of ¬Pc for every ground atom Pc with DB ⊬ Pc, and an
answer under the assumption is one entailed by DB ∪ EDB-bar. The
convention "presumes total knowledge about the domain being
represented"; Reiter states this and does not prove any soundness
relative to the world. If DB ∪ EDB-bar is consistent, every closed-world
answer is definite (Theorem 3.1), and closed-world evaluation of any
existential query reduces to open-world evaluation of atomic queries
combined by union, intersection, difference and projection (Theorems
4.1–4.5), so EDB-bar is never listed. "Not every consistent data base
remains consistent under the CWA": DB = {Pa ∨ Pb} gives ¬Pa and ¬Pb
(Example 5.1). A consistent Horn database stays consistent (Theorem 5.1),
and every definite database is consistent under it (Corollary 5.4). The
workshop version omits all proofs, deferring them to a report not read.

**What could have come out otherwise.** Clark's construction could have
needed more than the completion and identity axioms to turn a failure
tree into a first-order proof; the lemma shows unification is emulated by
those axioms alone. Reiter's consistency result could have failed for
some Horn database; Theorem 5.1 says it does not (stated, proof not
seen).

## What this does not say

- **That failure to find shows absence in the world.** Clark's conclusion
  is a theorem of the completed database; it is true of the world only if
  the database's definitions are complete, which is Reiter's assumption,
  stated and not proved.
- **That the two conditions are one.** One is about the database (it says
  everything true of its relations); the other is about the search (it
  ran out of alternatives). Clark's rule requires the second outright, as
  a premise, not as an assumption.
- **That a time-bounded search is negation as failure.** Neither paper
  considers search time. Reiter's non-entailment is a fixed relation;
  Clark's rule needs every branch closed. A search stopped at a deadline
  has open branches and meets neither, and a rule that adds ¬Pc for an
  entailed but unfound Pc can make even a Horn database inconsistent
  ([NOTE-899](../notes.d/NOTE-899.md)).
- **That the closed-world assumption is always available.** A reasoner who
  knows an item is in one of several places holds a disjunction, Reiter's
  Example 5.1, where the assumption is inconsistent.
- **Anything probabilistic.** Both results are deductive.

## Connections

- [CLAIM-306](../claims.d/CLAIM-306.md) rests on exactly this pair of conditions. It now grounds
  [LIT-1087](../literature.d/LIT-1087.md) and [LIT-1088](../literature.d/LIT-1088.md) directly; this account is the read form of
  both and the stronger footing.
- [CASE-085](../cases.d/CASE-085.md)'s medic, who knew the drug was stocked, is Reiter's Example 5.1;
  [CASE-094](../cases.d/CASE-094.md)'s "may as well not be there" is a practical equivalence,
  not a closed-world inference.
- The search-time asymmetry the claim adds is [THEORY-358](THEORY-358.md)'s absent-trial
  result, not these papers'.
- [THEORY-tmpg43pg](THEORY-tmpg43pg.md) (Halevy's survey, reporting Abiteboul and Duschka 1998,
  unread): answering a query from stored partial views is co-NP-hard under
  the closed-world assumption even for conjunctive views, where it is often
  polynomial under the open-world one. The assumption that makes negation
  cheap in a complete database makes answering from incomplete stored
  answers harder. [CLAIM-tmpfpvgq](../claims.d/CLAIM-tmpfpvgq.md) uses this.
