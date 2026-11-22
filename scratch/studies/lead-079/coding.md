<!-- scratch/studies/lead-079/coding.md: the study materials of CASE-tmpzi1u3, copied from the delegated coder's working directory on 2026-11-22 -->
# LEAD-079 coding: "Rich Get Richer Power Laws" (ChatGPT, 2026-11-20 to 21)

Coded under codebook.md (written 2026-11-22T07:16Z, before coding). This file
was finished 2026-11-22T07:25Z (session clock). Coder: Claude Opus 5.5, a single
AI coder. Raw notes in reading order: notes_raw.md. Quotes are verbatim from
the visible turns (checked by grep against visible.txt).

Exchange: 27 owner turns (U1-U27; 17 are "continue"/"elaborate"), 43 assistant
turns, of which 16 are preamble stubs (<600 chars, not coded) and 27 are
substantive replies (~600k chars visible). Phases, fixed after reading:
- Exposition, U1-U17 / 17 replies (A1-A27): power laws, criticality, RG,
  information, nonequilibrium, Goldstone modes. Owner gives a topic, one
  hypothesis (U5) and then "continue".
- Argument, U18-U27 / 10 replies (A29-A43): the owner's own hypothesis built
  turn by turn (DNN representations as active matter; concentration of
  measure; entailment cones; singular learning theory; hyperribbons;
  small-eigenvalue subspaces).

## Coded failures

Item id, then each occurrence: turn | category | quote | earlier occurrence.

### Identity: ID-REDERIV (restated as though new, no back-reference)

| Item | Turn | Quote | Earlier |
|---|---|---|---|
| R0 (weak) | A8 | "That question is the motivation behind self-organized criticality" | A3 s3, A6 close |
| R1 | A10 | "This is what people mean when they say a power law has no characteristic scale" | A1 s7, A5 close, A8 s4 |
| R2 | A10 | "This process is called *coarse-graining*." | A6 s4 (same sentence) |
| R2 | A12 | coarse-grain / rescale / update rules explained from scratch (s1) | A6, A8, A10 |
| R3 | A10 | "This is called *universality*." | A3 s7, A6 s3 |
| R3 | A12 | s5 universality classes re-explained | A10 s5 |
| R4 | A10 | "This suggests an interesting reinterpretation" (tail as widening scaling regime) | A7 s1, s5 |
| R5 | A12 | "This classification is one of the central achievements of renormalization theory." (relevant/irrelevant) | A10 s5 |
| R6 | A12 | "that provides evidence for finite-size scaling" | A8 s6 |
| R6 | A17 | "Finite-size scaling: a concrete example" | A8 s6, A12 s8 |
| R7 | A12 | "Chaos concerns the predictability of individual trajectories." | A3 s6 "Statistical predictability and event-level predictability are different things." |
| R7 | A21 | "Knowing the law is different from knowing the future" | A3 s6, A12 s9 |
| R9 | A13 | "This leads to a compelling reinterpretation of everything we've discussed" | A10 s9, A12 opener |
| R10 | A15 | "A power-law memory kernel has emerged from a superposition of ordinary exponential processes." | A5 s4 (mixtures) |
| R10 | A23 | "If the unresolved dynamics have a broad hierarchy of relaxation times" | A5 s4, A15 s4 |
| R11 | A15 | "This resembles a more general idea in information theory and statistical learning" | A13 s4 (IB principle) |
| R11 | A17 | "The natural components of an effective theory may not be the visible pieces" | A13 s4, A15 s8 |
| R12 | A19 | "There's a philosophical implication here that I think is worth developing." | A12 s9, A13 s7, A17 opener |
| R13 | A23 | "the word *criticality* is often used too broadly" | A10 s6 |
| R13 | A24 | "need not be an equilibrium state or even a state tuned to an isolated critical point" | A10 s6, A23 s8 |
| R13 | A26 | "This is an important qualification to the idea that a power law implies criticality." | A10 s6, A23, A24 |
| R14 | A23 | "Here's one of the more surprising connections." (coarse-graining creates memory) | A17 s2 |
| R15 | A24 | "This is a crucial limitation of studying power laws only through histograms." | A1 s4/s7, A3 s5 |
| R16 | A26 | "In certain active systems, scaling is a property of the phase itself." | A12 s7 (BKT, critical phases) |
| R16 | A27 | "The exponent changes continuously with temperature throughout the low-temperature phase." | A12 s7 (same claim) |
| R17 | A24 | "The scale-free quantity is not necessarily a power-law-distributed event size." | A10 s2 |
| R17 | A27 | "the fundamental organizing object may be a scaling relation rather than a distribution of magnitudes" | A10 s2, A24 s3 |
| R18 (strong) | A30 | "I think this is a crucial correction to the model we've been developing." -- then re-derives Var(u.v)=1/D, distances ~ sqrt2, max cosine sqrt(2 log N / D) | A29 s5 "Effect A" (same three results) |
| R19 | A32 | "must be overcome by a coupling whose effective strength grows with dimension" | A30 s4 (kappa ~ D) |
| R20 | A39 | "And the latter cannot generally be inferred from the Fisher-information eigenvalues at one point." | A37 s2 "The geometry of the loss cannot be understood from its Hessian alone." |
| R21 | A41 | "This suggests a powerful correction to our hyperribbon account" | A19 s2 "A direction that looks irrelevant for one experiment may matter greatly for another." |
| R22 | A42 | "At the critical point, relaxation has changed from exponential to algebraic." | A39 s5 (t^-1/2) |
| R23 | A42 | "Z_n \asymp n^{-3/4}" at the threshold | A39 s3 (lambda = 3/4) |

33 occurrences, 23 items (27 in exposition, 6 in argument).

### Identity: other subtypes

| Code | Item | Turn | Quote | Note |
|---|---|---|---|---|
| ID-REDEF | X1 | A41 | "purely variance-based hyperribbon analysis could mislead us"; "We originally treated the hyperribbon hierarchy as a hierarchy of importance." | A19/A39: hyperribbon = Fisher-sensitivity widths of the model manifold, not a variance hierarchy |
| ID-CASE | C1 | A32 | "a small population of exceptional outcomes separated by a critical threshold" | owner's bulk-and-tail case; A7 s4: "there isn't usually a genuine gap between the bulk and the tail" |
| ID-DROP (dual ST-OBJ) | D1 | A30 | "A large \(m\) indicates global directional alignment" | A29 s3: "Alignment of embedding *positions* is different from alignment of particle *velocities*." Not carried or answered |
| ID-DROP | D1 | A32 | s7 mean-field O(D) "collective alignment" of positions | same |
| ID-THESIS (weak) | T1 | A6 | "This is the deepest connection" | each turn names a new "deepest" unifier, never set against the earlier one (A3 s6 first) |
| ID-THESIS (weak) | T1 | A8 | "I think this may be the most important implication of the whole discussion." | |
| ID-THESIS (weak) | T1 | A10 | "The deepest conceptual connection: scale invariance and emergence" | |
| ID-THESIS (weak) | T1 | A13 | "That may be the most general conceptual thread" | |
| ID-THESIS (weak) | T1 | A21 | "I think that's the central insight connecting the ideas we've explored." | |
| ID-THESIS (weak) | T1 | A24 | "The deepest insight is that statistical similarity and dynamical similarity aren't the same thing." | |

REDEF 1, CASE 1, DROP 2 occurrences (1 item), THESIS 6 occurrences (1 item,
weak). ID-HELD (record-relative) is reported separately, not coded blind.

### Structure

| Code | Item | Turn | Quote |
|---|---|---|---|
| ST-INF | S1 | A10 | "scale invariance offers a mathematical explanation for how complicated systems can have simple emergent laws" |
| ST-INF | S1 | A12 | "Large-scale reality is determined by the properties that remain important under repeated changes of scale." |
| ST-INF | S2 (weak) | A13 | "their relationship explains why the same mathematical tools can appear in physics, information theory, and machine learning" |
| ST-INF | S3 | A15 | "Criticality amplifies both information and uncertainty." (from a linear AR(1) toy) |
| ST-INF | S4 | A19 | "That offers an explanation for why useful scientific laws are possible at all." |
| ST-PREM | -- | -- | none coded |
| ST-OBJ | -- | -- | none coded on its own; D1 is dual |

5 occurrences, 4 items (all in exposition). 6 with D1's dual.

## Counts and rates (27 substantive replies; 27 owner turns)

| | Exposition (17 replies) | Argument (10 replies) | Total | per reply |
|---|---:|---:|---:|---:|
| ID-REDERIV | 27 | 6 | 33 | 1.22 |
| ID-REDEF | 0 | 1 | 1 | 0.04 |
| ID-CASE | 0 | 1 | 1 | 0.04 |
| ID-DROP | 0 | 2 | 2 | 0.07 |
| ID-THESIS (weak) | 6 | 0 | 6 | 0.22 |
| **Identity** | **33** | **10** | **43** | **1.59** |
| ST-INF | 5 | 0 | 5 | 0.19 |
| ST-PREM | 0 | 0 | 0 | 0 |
| ST-OBJ | 0 | 0 (1 dual) | 0 (1) | 0 (0.04) |
| **Structure** | **5** | **0 (1)** | **5 (6)** | **0.19** |

Per 100k characters of visible assistant text (~600k): identity ~7.2,
structure ~0.8.

Sensitivity:
- Drop the weak codes (R0, S2, all T1): identity 36, structure 4.
- Drop every exposition-phase re-derivation as tutorial restatement and all
  T1: identity 10, structure 5. Identity still the larger, and REDEF+REDERIV =
  7 over 27 replies (0.26 per reply), above the "rare" bar fixed in advance
  (< 1 per 5 replies).
- Argument phase only: identity 10, structure 0 (1 dual).

## Record-relative (ID-HELD), not blind

From the seven filing ledgers of this exchange already in share2/ (other
readers, 2026-11-21), counted by regex: of ~350 idea items, ~31 were marked
HELD and ~108 PARTLY. These are ideas the record holds and the exchange gives
as new. The assistant in this exchange had no access to the record (the will
exchange's assistant was shown it), so they are not failures of this exchange,
and they are not counted above. They show that the record's held content
comes back uncited, CLAIM-177's "readings come back as though new", seen from
the record's side.

## Not coded, noted

- Announced revisions are frequent and are not failures under C4: "I would
  sharpen the original claim this way" (A8), "I think the most important
  refinement is this" (A26), "I would now state the overarching idea
  somewhat differently from before" (A39), "I would now replace our earlier
  assumption" (A42). In the argument phase every change of the hypothesis is
  announced and given a reason.
- Many "X does not establish Y" disclaimers (as ADR-032 found for the will
  exchange); not defects.
- Citations were not checked. Several are to 2026 work that could not be
  verified here (e.g. arXiv 2606.28486; "Weilun Xu, revised November 3, 2026").
  A source-reliability defect is in neither scheme.
- Reasoning summaries were not coded.
