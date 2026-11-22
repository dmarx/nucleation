---
status: Skimmed
paper: LIT-2238
title: 'Bumpus, Fairbanks, Karvonen, Leal and Simard — Towards a Unified Theory of Time-Varying Data'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Skimmed on 2026-11-22 for LEAD-023 from the arXiv copy (2402.00206v3,
    25 March 2025, 25 pages): the abstract, introduction and desiderata,
    the definitions of §2.1, Proposition 2.9, the statement of Theorem
    2.10 and the Discussion read; the proof of Theorem 2.10 and the
    temporal-graph and change-of-base sections (§2.4–2.6, §3) read for
    their headings only. Quotations checked by script.
date: '2026-11-22'
summary: >-
  Time-varying data as narratives: sheaves (persistent) or cosheaves
  (cumulative) on posets of time intervals, valued in any category with
  limits and colimits, so that a temporal graph, group or space is one
  definition with morphisms. The two views are related by an adjunction
  that can lose information; a sequence of snapshots does not determine a
  narrative without the spans relating successive times; and the link to
  the dynamics that generate the data is set as a desideratum, met only by
  sharing the interval sheaves of Schultz, Spivak and Vasilakopoulou.
---

# NOTE-tmpgeiy5: Bumpus, Fairbanks, Karvonen, Leal and Simard — Towards a Unified Theory of Time-Varying Data

## Contribution

A single categorical definition of temporal data, "narratives", built
from the lessons of temporal graph theory and stated as five desiderata
it meets.

## Key results (parts read)

1. **Narratives (abstract, Definition 2.8).** "categories of narratives.
   These are sheaves on posets of time intervals that encode snapshots of
   a temporal object along with the relationships between them." Persistent
   narratives are D-valued sheaves, cumulative ones D-valued cosheaves.
2. **Snapshots underdetermine (Proposition 2.9).** Objects on points and
   unit intervals with the spans between them determine a unique discrete
   narrative; "Conversely, a mere sequence of objects of D (i.e. a choice
   of one object for each interval of length zero) does not determine a
   unique discrete D-narrative."
3. **Adjunction (Theorem 2.10).** Functors K and P between persistent and
   cumulative narratives, with K ⊣ P; in general "there is the potential
   for a loss of information when one passes from one perspective (the
   persistent one, say) to another (the cumulative one) and back again."
4. **Data and dynamics (Introduction, D5).** "Since temporal data
   naturally arises from some underlying dynamical system, any theory of
   temporal data should be seamlessly interoperable with theories of
   dynamical systems." The paper meets this only by putting narratives
   and Schultz, Spivak and Vasilakopoulou's interval sheaves "on the same
   mathematical and linguistic footing" (Discussion).

## Assumptions

A time category of intervals with the Johnstone coverage (an interval is
covered by splitting it at a point); a value category with pullbacks (for
sheaves) or pushouts (for cosheaves), limits and colimits for the
adjunction.

## Concepts

Narrative, persistent and cumulative; time category; Johnstone coverage;
change of base; temporalization of a static property.

## Bearing on the record

- **[QUESTION-379](../questions.d/QUESTION-379.md).** It supplies a language for the question's "coherent
  family of local observations" over time, with the gluing built in, and
  a precise form of underdetermination: snapshots without the relations
  between times fix no temporal object. It does not ask when a narrative
  is the record of some realizable dynamics: that is its desideratum D5,
  left to future work, which is the question's step.
- **[LIT-2262](../literature.d/LIT-2262.md)** (Leal et al.) applies this framework; read in the same lead.

## Limitations

Skimmed. A foundations paper: definitions, an adjunction and examples, no
theorem about which narratives arise from dynamics. Examples mostly
temporal graphs.
