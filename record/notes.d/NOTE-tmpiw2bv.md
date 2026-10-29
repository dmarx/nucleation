---
status: Read
paper: 'LIT-tmplfiq6'
title: 'Chalupka, Perona and Eberhardt — Multi-level cause-effect systems'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Read in full on 2026-10-29 from arXiv 1512.07942v1
    (https://arxiv.org/pdf/1512.07942v1, 13 pages: the 9-page paper and
    the supplementary material), text extracted with pdftotext. Read:
    the abstract, §§1–5, Algorithms 1 and 2, the captions of Figures
    1–5, the three supplementary sections (the proof of the sufficient
    causal description theorem, the details of Algorithm 1 and the proof
    of the fundamental causal coarsening theorem) and the references.
    The PMLR PDF (https://proceedings.mlr.press/v51/chalupka16.pdf, 9
    pages, no supplement) was checked for the passages quoted below;
    they match. Figures 3–5 were read from their captions and the text;
    no number was taken from a chart. Checked by a record script on
    2026-10-29: the minimality claim of Theorem 5 against a 2×3 example
    (it fails, below), and the step (2ii) of the coarsening proof by
    hand. The UAI 2015 paper whose cause-side proof part (1) borrows was
    not read; the overview is NOTE-tmpbrnim.
date: '2026-10-29'
summary: >-
  Defines the fundamental cause and effect of a confounded micro system
  as the partitions of causes by P(J | man(i)) and of effects by P(j |
  man(·)), learns both from experimental data, and proves they
  generically coarsen the observational partitions, so passive data plus
  one experiment per class find them. It assumes no distribution over
  interventions. Its claim that the effect partition is the minimal
  sufficient one fails for proportional, unequal columns.
---
<!-- inactive-ok-file: THEORY-787 — Proposed; the causal thesis this reading bears on, cited as open -->
<!-- inactive-ok-file: QUESTION-204 QUESTION-115 QUESTION-252 — Open; the questions this reading bears on, cited as open -->

# NOTE-tmpiw2bv: Chalupka, Perona and Eberhardt — Multi-level cause-effect systems

## Contribution

It extends causal feature learning from a cause of a given target
behaviour (UAI 2015) to the case where both the macro cause and the
macro effect are built from micro data. It defines the pair, gives an
algorithm that learns it from experiments, proves the coarsening theorem
for both sides, and defines coarser subsidiary cause–effect pairs, which
can compose into the fundamental one.

## Key insight

Cluster the rows and the columns of the interventional matrix P(j |
man(i)) at the same time. Rows that agree are one macro cause; columns
that agree are one macro effect. Structure in J that does not depend on
I, such as the distractor neurons' rhythm, is ignored because it does not
change any column's profile across manipulations, where simply
clustering J would split the true classes in half.

## Assumptions

- A causal ml-system: discrete I and J of possibly huge cardinality, a
  hidden confounder H, P(J, I) = Σ_H P(J | I, H)P(I | H)P(H), with
  independent noise on each side.
- A micro manipulation man(I = i) sets I without touching H or J:
  P(J | man(i)) = Σ_H P(J | i, H)P(H) (Def. 1).
- No distribution over interventions: "unless we assume a distribution
  P(man(I)) over the interventions, we cannot apply the notion of a
  sufficient statistic to manipulations in the I space. Following
  Pearl's approach, we refrain from specifying intervention
  distributions" (§2.2).
- For Algorithm 1, P(j | man(i)) smooth in i and j; for the theorem,
  Lebesgue measure on the free parameters.
- Micro variables "do not lump together atoms that belong to different
  'true fundamental partition' cells" (§5).

## Key results

- **Fundamental causal partition (Def. 2).** i₁ ~ i₂ iff P(j | man(i₁)) =
  P(j | man(i₂)) for all j; j₁ ~ j₂ iff P(j₁ | man(i)) = P(j₂ | man(i)) for
  all i. Their labels are the fundamental cause C and effect E (Def. 3);
  do(C = c) is man(i) for any i with C(i) = c (Def. 4).
- **Sufficient causal description (Theorems 5, 9, 12).** E is "the
  minimal sufficient statistic for P(J | man(i)) for any i" among
  partitions of J (Fisher factorization); C and E "losslessly recover
  P(j | man(i))", and any other partition "is either finer than C, E or
  does not define unambiguous manipulations". The authors add that E is
  minimal only among partitions; a histogram is a smaller sufficient
  statistic.
- **Fundamental causal coarsening (Theorems 7, 13).** Among generative
  distributions with given observational partitions of I and J, those
  whose causal partition of I, or of J, is not a coarsening of the
  observational one have measure zero. Part (1) is referred to the UAI
  2015 proof; part (2) writes P(j₁ | i) = P(j₂ | i) as Σ_h [α_{j₁,h,i} −
  α_{j₂,h,i}] β_{h,i} γ_h = 0, a polynomial in β = P(I | H) that is not
  identically zero, then integrates by Fubini.
- **Subsidiary variables (Def. 8, Alg. 2).** Strict coarsenings (C̄, Ē)
  with P(Ē | do(C = c)) constant over the C-cells inside each C̄-cell
  and distinct across C̄-cells. "v-bar" is not a cause of "pulse": an
  image with a v-bar and no h-bar gives P(pulse | man(i)) = 0, one with
  both gives 0.8, an ambiguous manipulation. Non-interacting subsidiary
  pairs factor the fundamental table (Def. 11); "in almost all the
  cases" there are none.
- **Simulation.** 10,000 images in four classes, 100 Izhikevich neurons,
  P(pulse | do(h-bar)) = P(30 Hz | do(v-bar)) = 0.8; Algorithm 1 recovers
  the four-by-four table, with clusters merged by a KL threshold, and
  "the best solution in practice is to cluster them by hand".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | (C, E) is the coarsest partition pair that losslessly recovers P(j \| man(i)) | moderate: right for C, wrong for E as stated | Theorem 12 proof; fails for proportional columns (below) |
| C2 | The causal partitions generically coarsen the observational ones on both sides | strong, as genericity | Theorem 13 with proof; slips in (2ii) do not break it |
| C3 | Algorithm 1 recovers the fundamental cause and effect | weak in general | one simulation built with that structure |
| C4 | Non-interacting subsidiary causes indicate independent mechanisms | weak | asserted |
| C5 | The interventional/observational distinction is "entirely lost" in Hoel et al. (2013) | weak | one sentence, no computation |
| C6 | Whether macro causes exist is an empirical question, since they "cannot be defined arbitrarily" | moderate | argument (§5) |

## Concepts

- **Fundamental cause and effect**: the class labels of the row and
  column partitions of P(j | man(i)).
- **Subsidiary cause–effect pair**: a coarsening of both that keeps
  manipulations unambiguous for the coarser effect.
- **Partition product**: the coarsest common refinement; composition of
  macro variables (Def. 10).

## Connections

It generalizes Chalupka, Perona and Eberhardt 2015 (UAI, not
registered). Its overview is LIT-tmpmefe6 (NOTE-tmpbrnim). Its cause
partition is the optimum of the causal information bottleneck
(LIT-1802, THEORY-1125). It credits computational mechanics (LIT-1126)
and Shalizi. Eberhardt and Lee (LIT-tmpr2bnp) recommend it against
Hoel's effective information (LIT-1038), which it dismisses in one
sentence. The effect-side coarsening it defines is the one Hoel's
coarse-grainings of a transition matrix also make.

## Bearing on the record

- **QUESTION-204, second half.** This is the paper that supplies the
  test the question names, for cause and effect together. It is
  independent of EI-type choices by design: the authors decline to put
  any distribution on interventions, and the partition is defined from
  point manipulations alone. THEORY-tmpyfcov, filed from this reading,
  shows that EI under one common full-support distribution ties the micro
  exactly at this partition (with effects grouped by normalized
  likelihood) and its refinements, whatever the distribution. On which
  coarse-grainings lose nothing, the causal criterion of THEORY-tmphfpe7's
  set-up and the interventionist test agree. Hoel's uniform-per-level EI
  does not: on Eberhardt and Lee's (13) and (14) it merges causes with
  different rows, and on their note 6 it keeps identical rows apart. The
  paper computes nothing on Hoel's systems; that comparison is the
  record's.
- **THEORY-787.** The verdict CFL gives on a transition matrix is a
  partition, not a level where causation is stronger: the micro
  description "contains no more causal information", but it loses none
  either. Where micro rows are exactly equal, as in Hoel's (11), CFL and
  EI pick the same macro; elsewhere CFL keeps the micro. So CFL can
  confirm that a macro is proportionate, never that it beats the micro.
  Hoel 2013's own examples (THEORY-222) were not recomputed.
- **QUESTION-115.** Its row and column clustering finds a cause and an
  effect with different partitions. On systems where EI's single
  partition and CFL's pair differ, which level each criterion picks can
  be read off at once (note 6).
- **QUESTION-252.** The sufficient-description theorem is a predictive
  sufficiency condition for a declared target under intervention, and
  the coarsening theorem relates it to observational sufficiency:
  generically the interventional condition holds wherever the
  observational one does, never the reverse under confounding.
  Subsidiary variables are coarser descriptions that keep sufficiency
  for a coarser declared target only.

## Limitations

- **The minimality claim is wrong as stated.** Definition 2 groups
  effects by equal columns. Two effect states with proportional, unequal
  columns, T(j₁ | i) = κ T(j₂ | i) for all i, can be merged with no loss:
  given the merged count, the split is binomial with a parameter that
  does not depend on i, so the merged partition is sufficient for the
  family {P(J | man(i))}. Example (record script): rows (0.2, 0.4, 0.4)
  and (0.1, 0.2, 0.7); merging the first two effects keeps I(X; Y)
  exactly (0.0667 bits under uniform w, 0.0238 under (0.9, 0.1)). The
  proof treats each p_j as a free parameter, not as a function of i,
  which is where it goes wrong. The overview's §3.3 normalizes
  likelihood vectors before merging, which is the right criterion, but
  for clusters only.
- **Proof slips in Theorem 13 (2ii).** "Set β_{h*,i} = 1 (and thus
  β_{h,i} = 0 for any h ≠ h*)" does not follow, since β_{h,i} = P(i | h)
  is normalized over i, not h; both can be set, so the argument
  survives. The conclusion then writes "≠" where "=" is meant.
- PMLR's metadata orders the authors Chalupka, Eberhardt, Perona; the
  PDFs give Chalupka, Perona, Eberhardt. The arXiv PDF prints "JMLR:
  W&CP volume 41"; the volume is PMLR 51.
- One simulation, built with the structure recovered; merge thresholds
  chosen by hand.
- Exact equality throughout: with estimated rows, the partition is a
  threshold choice.

## Open questions

- With the effect classes corrected to normalized columns, does the
  coarsening theorem's part (2) still hold as stated? Its constraint is
  written for equal columns.
- What happens "when this assumption is violated", that micro variables
  do not straddle true cells, is left open (§5).
