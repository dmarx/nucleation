---
status: Read
paper: LIT-1590
title: 'Campbell et al. — Changes in endosymbiont complexity drive host-level compensatory adaptations in cicadas'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Read in full from the PubMed Central copy of the version of record
    (PMC6234865, CC BY 4.0), fetched on 2026-10-27 as full-text XML
    through the Europe PMC REST service and converted to text. Read: both
    abstracts, the introduction, the four results subsections, the three
    discussion subsections, Table 1 and its footnotes, the captions of
    Figures 1–4 and of Figures S1–S2 and Tables S1–S2, and all of
    Materials and Methods including the methodological caveats. The
    reference list was not read, except entries 19–22 and 30, to match
    them to the record's LITs. Figures were read from their captions
    and the text; the supplementary tables (sample details, accessions)
    were not opened, and the simulation code on GitHub was not run.
    Checks re-derived here: the Hodgkinia range 30,154 / 4,889 = 6.2
    ("up to 6-fold"); the Sulcia range 5,643 / 2,572 = 2.2 ("approximately
    2-fold"); the ratio of means for M. septendecim, 30,154 / 2,572 =
    11.7, against the reported 11.2:1; 0.8% of about 12,000 cells = 96,
    against the reported "∼80"; T. limbata lineage 5, 2.72 / 0.25 = 10.9
    ("over 10-fold").
date: '2026-10-27'
summary: >-
  In cicadas whose endosymbiont Hodgkinia has split into many lineages,
  each essential, the mother must put every lineage into every egg. A
  simulation shows that random transmission would need far more cells as
  lineages multiply and grow uneven. Counts in eggs of four species find
  Sulcia numbers roughly constant, and Hodgkinia numbers up to about six
  times higher in Magicicada septendecim than in a single-lineage
  species. Amplicon sequencing found every tracked Hodgkinia genotype in
  every egg sampled. The transmission route looks the same under the
  light microscope. Only M. septendecim differs significantly; the
  six-lineage species does not. So the compensation rests on one
  species. The authors call the raised titre a cost of fragmentation,
  and speculate that it could feed further splitting.
---
<!-- inactive-ok-file: THEORY-tmpjel7l — Proposed; filed from this reading -->
<!-- inactive-ok-file: QUESTION-277 CASE-177 CASE-173 THEORY-1049 THEORY-1051 LIT-1563 LIT-1586 LIT-1612 LIT-1602 — Open, Proposed or Unfetched; the question, cases, accounts and unread works this reading is set beside, nothing here rests on them -->

# NOTE-tmp6a57o: Campbell et al. — Changes in endosymbiont complexity drive host-level compensatory adaptations in cicadas

## Contribution

The authors had earlier found *Hodgkinia* splitting into lineages with
complementary gene sets (refs 19–22). They had also guessed that this
would make transmission to eggs risky. This paper tests the guess. It
measures how many symbiont cells reach each egg across cicadas with one,
six and "perhaps dozens" of *Hodgkinia* lineages. It asks whether every
egg gets every lineage, and whether the transmission route has changed.

## Key insight

A host whose essential symbiont has split into uneven parts faces a
sampling problem at each generation. The rarest essential lineage sets
the number of cells that must be sent. The answer found is not a new
sorting mechanism, but more of the same: the host sends more *Hodgkinia*
cells and not more *Sulcia*. The authors frame this as the host
compensating for changes in its symbiont, and as a cost the symbiont's
changes impose. They add a twist: a larger transmitted population means
weaker bottlenecks, which could make further splitting easier. In their
words, "the compensatory changes cicadas have evolved in response to
increasing Hodgkinia complexity might themselves make the problem of
splitting worse".

## Assumptions

- **The simulation (Fig. 1).** Cells are drawn at random, with
  replacement, from a mother's pool whose lineage proportions are taken
  from genome-assembly coverage. An egg is viable if it gets at least 1
  (or 50, or 100) cells of every lineage. For *Magicicada tredecim*, every
  finished genomic circle is treated as a separate cell lineage. The
  authors say this, and the 1-cell rule, make the result an upper bound.
- **Cell counts (Fig. 2).** *Sulcia* cells are counted in a box of about
  50 × 50 × 10 μm³ and scaled to the volume of the symbiont ball, taken as
  a sphere or spheroid. *Hodgkinia* is then estimated from the
  *Hodgkinia*:*Sulcia* ratio on one confocal slice. Cell shape may cause
  double counting, which the authors expect to affect all species alike.
  Egg age is uncontrolled; only eggs with an intact symbiont ball were
  counted.
- **Lineage presence (Fig. 3).** One marker gene stands for the
  lineages: rpoB in two *Tettigades* species, where every cellular lineage
  carries it; etfD in *M. septendecim*, where no gene is on every circle
  and two homologues were tracked. Abundances from amplicons (over 25 PCR
  cycles) are taken as less accurate than metagenomic ones.
- **Egg nests.** All eggs in a nest are assumed to come from one female.
  For *Magicicada*, nests in a series whose genotypes did not match were
  dropped.

## Key results

- **Simulation (Fig. 1).**
  - With lineage abundances from *M. tredecim*, the minimum number of
    cells that guarantees every egg all lineages grows "by more than
    2,000-fold" as lineages multiply and grow uneven.
  - For *T. chilensis* (6 lineages, 69-fold abundance range), 1 cell of
    each lineage needs over 500 cells per egg, 50 cells over 8,000, and
    100 cells over 15,000.
  - *M. tredecim* (30 putative lineages, 74-fold range) needs 4 to 5
    times as many as *T. chilensis*.
- **Counts in eggs (Fig. 2).** Five or six eggs per species.
  - *Sulcia*: 2,572 (*M. septendecim*) to 5,643 (*Diceroprocta
    semicincta*), about 2-fold. Only that pair differs significantly
    (P = 0.0005).
  - *Hodgkinia*: 4,889 (*T. ulnaria*, 1 lineage) to 30,154
    (*M. septendecim*), about 6-fold. *M. septendecim* is higher than
    every other species (P < 0.001). "The differences in other pairwise
    comparisons were not significant." So *T. chilensis*, with six
    lineages and about 12,000 cells, is not shown to differ from the
    single-lineage species.
  - *Hodgkinia*:*Sulcia* ratios: about 1:1 with one lineage, 2.4:1 with
    six, 11.2:1 in *M. septendecim*. Within a species, *Hodgkinia* exceeds
    *Sulcia* significantly in *T. chilensis* (P = 0.018) and
    *M. septendecim* (P < 0.0001).
  - Combining counts with the simulation: *T. chilensis* eggs should get
    50 to 100 cells of the rarest lineage, about 80 by coverage;
    *M. septendecim* fewer than 50.
- **Every egg, every lineage (Fig. 3).**
  - All *Tettigades* eggs carried all rpoB genotypes. All
    *M. septendecim* eggs carried both universally present etfD
    genotypes.
  - Lineage proportions differ between egg nests (*T. chilensis*: F₁₀,₆₈
    = 33.88; *T. limbata*: F₅,₃₇ = 30.16; both P < 0.001), and eggs of one
    nest cluster together. The rare lineage 5 of *T. limbata* ranged from
    0.25% to 2.72%.
  - Mothers "seem to avoid substantial genotype abundance shifts" when
    transmitting, "at least in the single generation we measured".
  - Amplicons found variation the metagenomes had missed: one-base
    variants in *T. chilensis*, and in *M. septendecim* many minor etfD
    genotypes, present in different combinations in each adult and nest.
- **The route (Fig. 4).** By light microscopy, transmission in
  *T. lacertosa* (3 lineages) and *M. septendecim* looks the same, and
  matches Buchner's early description. *Hodgkinia* leaves the syncytium
  in "large, nucleated subcellular compartments"; *Sulcia* leaves from
  peripheral bacteriocytes. Both cross the follicular cells and gather in
  an invagination of the oocyte, the "symbiont ball". In *Magicicada*,
  more cells migrate.
- **Comparison with other insects (Table 1).** Section-based estimates
  for symbiont balls of many hemipterans. *Buchnera* in eggs of three
  aphids, including *Acyrthosiphon pisum* at 1,872 ± 524, from earlier
  work. *T. lacertosa* 11,895–18,314 and *M. septendecim* 55,071–84,787
  (both symbionts together), from this study. The *M. septendecim*
  figure is 1.7 to 2.6 times the FISH-based total of Fig. 2 (about
  32,700), so the two methods disagree in absolute terms. That
  comparison is mine; the paper does not make it.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | As Hodgkinia lineages multiply and grow uneven, random transmission needs many more cells per egg to keep every lineage | moderate | simulation under stated assumptions; the 1-cell rule and one-circle-one-cell make the size an upper bound |
| C2 | Cicadas with more complex Hodgkinia transmit more Hodgkinia cells per egg, up to about 6-fold, but not more Sulcia | moderate for M. septendecim, weak as a trend | four species, five or six eggs each; only M. septendecim differs significantly; one species per complexity level, with no phylogenetic control |
| C3 | All eggs receive all Hodgkinia lineages | moderate | marker genotypes in all sampled eggs of three species; the authors say occasional loss of rare lineages could escape detection |
| C4 | The transmission mechanism is unchanged at the resolution of light microscopy | moderate | sections of two species, compared with Buchner's description |
| C5 | The raised titre is a host adaptation driven by Hodgkinia's splitting, and a cost of it | weak | inferred from C2 and Sulcia's stability; the reverse order (high titre first, enabling splitting) is argued unlikely, not excluded |
| C6 | Larger transmitted populations could weaken bottlenecks, reduce host control and feed further splitting | speculative | the authors' own word: "While speculative" |

## Concepts

- **Lineage splitting** or **fragmentation**: one ancestral *Hodgkinia*
  lineage becoming several, in separate cells, each with "a subset of the
  original gene set", all needed for the ancestral set of nutrients.
- **Complexity**: here, the number of *Hodgkinia* lineages and the
  unevenness of their abundances.
- **Symbiont ball**: the packet of *Sulcia* and *Hodgkinia* cells in an
  invagination at the base of the oocyte.
- **Titre**: the number of symbiont cells transmitted to each egg.
- **Three solutions** the authors name: the host sorts lineages actively
  (1); the host sends more cells (2); the host accepts some inviable eggs
  (3). They find evidence for 2, none for 3, and cannot test 1.
- **Surplus**: single-lineage cicadas already send "substantially more
  Hodgkinia cells than strictly necessary", which the authors think
  buffered the first splits.

## Connections

The splitting itself comes from the authors' earlier papers: *Tettigades*
(refs 19, 22: LIT-1563, LIT-1586) and *Magicicada* (refs 20, 21:
LIT-1612, LIT-1602), all filed and all Unfetched. Background stated here
from them: *Tettigades* has one to six lineages; the seven *Magicicada*
species have "possibly dozens"; splitting began within the last about 4
million years in *Tettigades* and over 5 to 20 million in *Magicicada*.
The authors place their result among other cases of host compensation:
nuclear genes tracking fast mitochondrial evolution in plants and
primates, horizontal transfer of bacterial genes to the host nucleus,
and trafficking systems between host and symbiont. They end on symbiont
replacement as another escape from a degrading symbiont. The claim that
small symbiont populations, kept small by bottlenecks, weaken selection
among symbionts is cited to refs 48–51 and is not tested here.

## Bearing on the record

- **CASE-177.** The case's last bullet and summary come from this
  paper's abstract. Corrections:
  - "Eggs still receive the full set, because hosts with more complex
    Hodgkinia transmit up to six times as many cells." The full set was
    tracked by one or two marker genes per species. The "because" is the
    authors' inference. The six-fold rise is one species,
    *M. septendecim*; the six-lineage *T. chilensis* did not differ
    significantly from single-lineage species.
  - "Lineages differing in abundance by over a hundredfold" is from the
    authors' earlier metagenomes (114-fold in rpoB), not measured here.
  - In *Magicicada*, genomic circles are not shown to be cell lineages.
    The simulation assumes they are, and the authors suspect that some
    circles share cells.
  - "The host's response raises reproductive cohesion (R)" overstates
    it. The host keeps co-transmission complete as the parts multiply.
    It maintains R; it does not raise it. And the authors suggest that
    the same response may lower host control (C) and raise selection
    among symbionts (S).
- **QUESTION-277.** Host compensation, the route the exchange named
  without a source, is here a change in one number, the titre, with the
  mechanism unchanged. It moves:
  - **R**: kept, not increased, by the host;
  - **D**: increased, since there are more essential parts;
  - **G**: distributed further among symbiont lineages (from earlier
    work);
  - **S** and **C**: possibly worsened, on the authors' speculation that
    larger populations mean weaker bottlenecks and "decrease the level of
    control that the host can exert". If so, compensation that saves R
    erodes S, and the dimensions trade off. The inference from the
    authors' speculation to the dimensions is mine.
- **THEORY-1049.** The authors write that "even the largest Hodgkinia
  genome no longer encodes the machinery to make its own membranes, the
  host must define Hodgkinia's envelope", and draw from it that the host
  could, in principle, sort lineages. That is the tipping-point argument
  turned toward control of transmission. Nothing here tests it.
- **THEORY-1051.** The model's one-symbiont collectives cannot hold a
  split symbiont. But this paper reports a related quantity: mothers pass
  their own lineage proportions to their eggs, so the composition of the
  symbiont community is inherited at the host level. The comparison is
  mine.
- **CASE-173.** Table 1 gives *Buchnera* counts in aphid eggs (886 to
  8,223 across three species, from earlier work), far fewer than in
  cicadas.
- Filed as THEORY-tmpjel7l. No instruction for machine-learning practice.

## Limitations

- **Four species for the comparison,** one per complexity level, five or
  six eggs each, with no phylogenetic correction. Two of the four, the
  single-lineage species, are tens of millions of years apart. The trend
  across complexity is one significant species.
- **Direction of causation is inferred.** The authors consider that a
  high titre came first and enabled splitting, and argue against it only
  because some cicadas keep an unsplit *Hodgkinia*.
- **Absolute counts are rough.** The authors say so (cell shape, egg
  age). Table 1's section-based estimate for *M. septendecim* is about
  twice the FISH estimate.
- **Lineage presence is shown by markers,** and the authors grant that
  rare lineages "are occasionally lost in certain eggs and that we lack
  the sensitivity to detect it".
- **Active sorting (solution 1) is untested.** The data cannot exclude
  it. Lineage-proportion variation tolerated across a population shows
  only that any sorting "is not highly accurate".
- **No data on adult symbiont numbers.** The authors' view that complex
  cicadas hold larger adult populations is "anecdotal".
- **Slips.** One sentence reports the *Hodgkinia* count "higher in
  M. tredecim than in any other species", where the species counted is
  *M. septendecim*. The methods print the same sequence for both etfD
  primers. The reported 11.2:1 ratio differs from the ratio of the
  reported means (11.7:1), perhaps a mean of per-egg ratios. "∼80" cells
  of the rarest *T. chilensis* lineage does not match 0.8% of about
  12,000 (96).

## Open questions

- Do hosts sort *Hodgkinia* lineages at all? Single-cell tracking of
  lineages through the ovariole would show it.
- Does the titre rise smoothly with the number of lineages, or only in
  *Magicicada*? More species, with phylogenetic control, would show it.
- Did a high titre precede splitting? Titres in cicadas just before and
  just after a split, in a clade with several independent splits such as
  *Tettigades*, would separate the two orders.
- Do complex cicadas hold more *Hodgkinia* as adults, and at what cost to
  *Sulcia* and to egg number?
- Is the positive feedback real: does a larger transmitted population
  raise *Hodgkinia* diversity within hosts, and the rate of further
  splitting?
