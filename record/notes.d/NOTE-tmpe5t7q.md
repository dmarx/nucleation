---
status: Read
paper: LIT-1561
title: 'Bernabeu, Manzano-Morales, Marcet-Houben & Gabaldón — Gene ancestries reveal diverse microbial associations during eukaryogenesis'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Read in full from the PubMed Central copy of the version of record
    (PMC13468126, open access), fetched on 2026-10-27 as full-text XML
    through the Europe PMC REST service and converted to text. Read: both
    abstracts, the introduction, "Reconstruction of the proteome",
    "Determining the ancestries of LECA", "Donor relative timing and
    metabolism", "Viruses as mediators of gene acquisition", the
    Discussion, all of Methods, the captions of Figures 1–4 and of
    Extended Data Figures 1–5. Figures were read from their captions and
    the text only; no figure image was seen. The Supplementary
    Information (Methods, Discussion, Figures 1–15, Tables 1–8), which
    holds several of the controls the main text relies on, was not read.
    Nor were the Zenodo data or the GitHub code. The reference list was
    not read, except to identify ten works the text cites (refs 4, 5, 6,
    21, 28, 29, 31, 38, 39 and 50). Checks made here: 4.5% × 74% = 3.33%,
    matching the stated 3.32% of the proteome from giant-virus sisters;
    the four donor shares sum to 13.43% of the proteome; innovations,
    acquisitions and unknowns (33%, about 53%, about 13%) sum to about
    99%, which places the viral 4.5% inside the acquisitions.
date: '2026-10-27'
summary: >-
  A fresh reconstruction of the last eukaryotic common ancestor's proteome
  from three 100-genome eukaryotic datasets, with each family's origin
  read from its sister group in a maximum-likelihood tree. Under
  thresholds tuned to maximize assignments to Alphaproteobacteria and
  Asgard archaea, two further bacterial donors pass in every dataset,
  Myxococcota (3.92% of the proteome) and Planctomycetota (2.24%),
  comparable to Alphaproteobacteria (3.99%) and Asgard (3.28%). A control
  that removes Alphaproteobacteria from the database does not reproduce
  their pattern. About 4.5% of families have a viral sister, mostly giant
  viruses. Stem-length distributions place Asgard earliest and
  Planctomycetota before the mitochondrion and Myxococcota. The authors
  read this as waves of transfer from several partners and challenge
  two-partner models. They concede their data say nothing about whether
  any donor was a symbiont.
---
<!-- inactive-ok-file: THEORY-tmphywi5 — Proposed; filed from this reading -->
<!-- inactive-ok-file: NOTE-tmppkn6v NOTE-tmphab0m THEORY-tmpfoo2c THEORY-tmpbinho THEORY-tmpyr6q4 — filed in the same batch of readings and not yet merged; the companion readings this one is set beside -->
<!-- inactive-ok-file: QUESTION-277 LIT-1566 LIT-1595 LIT-1591 LIT-1597 — Open, Deferred or Unavailable; the question and works this reading is set beside, nothing here rests on them -->

# NOTE-tmpe5t7q: Bernabeu, Manzano-Morales, Marcet-Houben & Gabaldón — Gene ancestries reveal diverse microbial associations during eukaryogenesis

## Contribution

It asks whether any donor other than the two accepted partners,
Alphaproteobacteria and Asgard archaea, can be traced in the LECA proteome
"with a level of support similar to those traced to these broadly accepted
partners". It answers yes for two bacterial phyla, Myxococcota and
Planctomycetota. It adds viruses as a route: giant viruses
(Nucleocytoviricota) as carriers of some prokaryotic genes into the
eukaryotic lineage. It then orders the donors in time with stem lengths
and infers each donor's likely metabolism from its living relatives. It is
the current statement of the Gabaldón group's "premitochondrial symbioses"
hypothesis, continuing Pittis and Gabaldón 2016 (LIT-1595).

## Key insight

Calibrate on the partners everyone accepts, then see who else survives.
The authors search over support thresholds for the setting that maximizes
the share of trees assigned to Alphaproteobacteria and Asgard, on the
assumption that those signals are real and the rest is mostly noise. At
that setting two more bacterial phyla still hold a share as large as the
accepted partners'. A negative control asks whether they could be
misplaced alphaproteobacterial genes, and the answer is no. If their genes
also cluster in time, each looks like a "transfer wave" from one donor in
one period. That is what a sustained association would leave. The authors
stop short of calling it symbiosis: "our data do not provide information
on potential types of interaction (endosymbiotic, ectosymbiotic,
parasitic, and so on)".

## Assumptions

- **LECA families by spread.** An orthologous group is ancestral if it has at
  least five species, both main eukaryotic stems, and three (relaxed) or five
  (strict) of nine supergroups; the donor analysis uses seven. Recent
  in-paralogues are collapsed to one representative, and contaminants removed
  by identity and taxonomy rules.
- **Order-level prokaryotic pangenomes.** One genome per GTDB genus; genes
  kept if present in 15% or more of genus representatives in an order, "the
  cutoff for the 'cloud' component of the pangenome". Viral proteins from 1.3
  million clusters are added.
- **The first sister is the donor.** Trees are rooted at the non-eukaryotic
  node farthest from the LECA clade. The donor is the most abundant taxon in
  the first non-eukaryotic sister, or, for viral sisters, in the first
  non-viral sister further back. A sister with over 25% eukaryotic sequences
  is not assigned.
- **The accepted partners calibrate the thresholds.** Thresholds (ultrafast
  bootstrap > 75%, "taxonomic bootstrap" > 95%, seven supergroups, donor
  certainty > 95%) are those that maximize the share of trees assigned to
  Alphaproteobacteria and Asgard, "assuming that the selected thresholds
  properly removed noise and kept only the reliable signals".
- **Stem length is relative time.** Normalized stem length, as in Pittis and
  Gabaldón, with "longer normalized lengths ... interpreted as indicating
  more ancient relatedness". The mode of each donor's distribution is
  estimated as a gamma mode by MCMC (Bernabeu, Armero & Gabaldón).
  Families with stems past the first minimum after the peak are dropped as
  later transfers, "heterotachy or ghost lineages".
- **Living relatives stand for the donor.** Donor metabolism is the
  prevalence of pathways in extant genomes of the donor clade that share
  more than half of the KOs it gave to LECA. "Note that this reconstruction
  was different from standard ancestral state reconstruction."

## Key results

- **The LECA proteome.** 12,907 (relaxed) or 7,751 (strict) monophyletic
  families on average; a consensus of 5,317 KEGG orthologs. 96% consistency
  of LECA groups across datasets, 79% after the monophyly refinement. LECA
  looks complex, heterotrophic and aerobic. It lacks pyruvate:ferredoxin
  oxidoreductase, [FeFe] hydrogenase and rhodoquinone synthesis, and its
  cell cycle "seemed to be incipient". Only 3% of families might come from
  transfer between eukaryotic supergroups.
- **Origins (Fig. 2a).** About 33% innovations (no non-eukaryotic homologue),
  about 53% acquisitions, about 13% unknown. 918 KOs are proposed as a
  revised set of eukaryotic signature proteins.
- **Donors (Fig. 2b), as shares of the LECA proteome at the calibrated
  thresholds:**

  | donor | share |
  |---|---|
  | Alphaproteobacteria | 3.99% |
  | Myxococcota | 3.92% |
  | Asgard archaea | 3.28% |
  | Planctomycetota | 2.24% |

  Chloroflexota and Gammaproteobacteria appear but fail in some datasets
  and are dropped. The four shares sum to 13.43% of the proteome, about a
  quarter of the acquisitions. The rest of the acquisitions are not
  assigned to a major donor at these thresholds.
- **Controls.**
  - Trees pointing to the new donors were not harder to resolve than
    alphaproteobacterial ones (Supplementary Fig. 6).
  - The "verticality test": rerunning the pipeline on alphaproteobacterial
    genomes with Alphaproteobacteria removed from the database assigns
    most trees to Gammaproteobacteria, with lower shares for more distant
    groups. Myxococcota and Planctomycetota do not follow that pattern
    (Supplementary Fig. 4).
  - Reanalysis of one earlier study's trees with this pipeline suggests that
    "Database completeness rather than methodological choices" drives
    differences between studies (Supplementary Fig. 7).

  All three are in the unread Supplementary Information; the main text
  reports their outcome.
- **Function (Fig. 2d,e).** Donor contributions are "broad and patchy";
  most modules mix origins, "a high degree of chimerism". Known trends
  return: archaeal information processing, alphaproteobacterial energy
  production.
- **Viruses.** About 4.5% of trees have a viral first sister, 74% of them
  giant viruses (3.32% of the proteome). Behind the virus, the first
  prokaryotic sister includes all the major donors, Asgard most often (about
  10%). Viral-route genes are enriched for signal transduction (kinases),
  chromatin and post-translational modification.
- **Timing (Fig. 3, Extended Data Figs 2–3).** Asgard is "the most ancestral
  signal". Among bacteria Planctomycetota has the longest stems, "followed by
  later contributions from the mitochondrial ancestor and Myxococcota, with
  largely overlapping transfer waves". The order matches the depth of these
  taxa in one studied microbial mat (Gutiérrez-Preciado et al. 2018).
  Supplementary Fig. 13 is cited for functional classes giving "overlapping
  distributions with similar modes", the authors' answer to the worry that
  function, not time, sets stem length. It was not read here.
- **Donor metabolism (Fig. 4, Extended Data Figs 4–5), as prevalence in
  donor-like genomes:**
  - Asgard ancestor: no complete methyl-coenzyme M reductase, so "may not
    have a methanogenic nature"; fermentation (ethanol 0.63, butyrate 0.67).
  - Mitochondrial ancestor: aerobic respiration strongly supported;
    photosynthesis 0.34–0.51 ("moderately supports"); no hydrogenases, "as
    implied by the hydrogen hypothesis and reverse-flow models".
  - Sulfate reduction in Myxococcota (0.44) and Planctomycetota (0.5);
    anammox in Planctomycetota weak (0.23).
- **Interpretation.** The data "challenge models depicting eukaryogenesis as a
  one-off event resulting from a binary symbiotic interaction and support a
  paradigm shift towards more gradual scenarios". Planctomycetota, with its
  cellular complexity and engulfment in one genus, "may lend some support"
  as an alternative bacterial host. The authors add at once that "our data
  do not provide information on the host or endosymbiotic nature of any
  partner".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The LECA proteome contains families traceable to Myxococcota and Planctomycetota with a share comparable to those traced to Alphaproteobacteria and Asgard | moderate | consistent across three datasets and both LECA criteria; verticality control; difficulty control; controls in the unread supplement |
| C2 | These signals are not misplaced alphaproteobacterial genes | moderate | the verticality test, which addresses vertical misplacement only, not transfer into the alphaproteobacterial or Asgard lineages before they reached eukaryotes |
| C3 | Genes from each donor were acquired in waves at distinct relative times: Asgard first, then Planctomycetota, then the mitochondrial ancestor and Myxococcota | weak–moderate | posterior modes of stem-length distributions; rests on stem length as a clock, which Tobiasson et al. dispute on their own data |
| C4 | Some bacterial transfers preceded mitochondrial endosymbiosis | weak–moderate | follows from C3 for Planctomycetota |
| C5 | Giant viruses mediated some gene transfers into the eukaryotic lineage, including of prokaryotic genes | moderate | tree topology with a viral first sister and prokaryotic sisters behind; strict filtering for direction |
| C6 | Eukaryogenesis involved serial interactions with several bacterial partners, not a single binary symbiosis | weak | an interpretation of C1–C4; the authors concede the data cannot tell symbiosis from other interactions |
| C7 | LECA was an aerobic heterotroph, and its Asgard ancestor was not a methanogen | weak–moderate | absence of anaerobic markers in the reconstruction; prevalence in donor-like genomes, which the authors call "incomplete and indirect" |

## Concepts

- **mLECA-OG**: a monophyletic LECA orthologous group, after splitting
  groups whose eukaryotic sequences are not monophyletic in the tree.
- **Innovation / acquisition / unknown**: no non-eukaryotic homologue; LECA
  nested among non-eukaryotic sequences; direction unclear.
- **Taxonomic bootstrap**: the share of bootstrap trees that assign the same
  taxon to the LECA clade's sister, regardless of which sequences form it.
- **Transfer wave**: "a set of genes potentially acquired from the same donor
  during the same period of time", seen as a peak in a donor's stem-length
  distribution.
- **Premitochondrial symbioses hypothesis**: Gabaldón's 2018 proposal that the
  host had symbiotic partners before the mitochondrion.
- **Donor-like genomes**: extant genomes of a donor clade sharing at least 50%
  of the KOs that donor gave to LECA.

## Connections

- **Pittis and Gabaldón 2016** (LIT-1595, unread here). Its stem-length
  method is reused here, now in a Bayesian frame, with a study of taxon sampling
  (Bernabeu, Manzano-Morales & Gabaldón 2024) cited in its support. Tobiasson et
  al. (LIT-1558, read in NOTE-tmppkn6v) test the same method and find that
  stem length behaves mainly like something other than time.
- **Tobiasson et al.** The two papers thank each other's authors. Tobiasson
  et al. cite this work's first preprint and attribute its "far greater
  bacterial contribution" to "more liberal criteria for core pangenome
  construction" letting in late transfer. This paper's pangenome cutoff is
  15% of genera in an order, against their 50% of species in a class. This
  paper does not answer that critique in the main text.
- **Syntrophy models.** It names the hydrogen–sulfur ("HS") syntrophy
  hypothesis (López-García & Moreira) as supported in its sulfate
  reduction, but with Planctomycetota as an earlier contributor than the
  Myxococcota host that model proposes. It finds no hydrogenases in the
  mitochondrial ancestor's relatives, against the hydrogen hypothesis
  (Martin & Müller, LIT-1597, unavailable here) and the reverse-flow model.
  It notes that both cultured Asgard archaea grow in syntrophy with
  sulfate-reducing partners. That is the subject of LIT-1591 (Imachi et al.),
  unread here and not cited by number in the passage.

## Bearing on the record

- **QUESTION-277 and the "live disagreement".** This is the record's
  "distributed" side, and the reading supports that placement with three
  qualifications.
  - **The distribution is of gene donors, not of partners in a collective.**
    The authors grant that "different forms of interactions beyond symbiosis
    could explain this genetic exchange". A2's caution, kept on LIT-1561,
    is the authors' own.
  - **It is mitochondrion-late, like Tobiasson et al.** Both papers have
    bacterial genes arriving before the mitochondrion. They differ on how
    the non-alphaproteobacterial genes are grouped (a few major donors in
    waves, here; diffuse transfer, there), on whether stem lengths can be
    read as times, and on how large the Asgard share is.
  - **The Asgard share is the starkest difference, but the two numbers are
    not the same quantity.** Here Asgard is 3.28% of the reconstructed
    proteome under calibrated thresholds. In Tobiasson et al. it is half of
    likelihood weight among the best-resolved families with prokaryotic
    homologues. The inference is mine: neither paper's figure can be
    converted into the other's, and the record should not set them against
    each other as rival percentages.
- **For the dimensions.** Like Tobiasson et al., this bears on G (whose genes
  carry which functions) and not on D, R, C or S. If any of the extra donors
  was a partner, the question's routes would apply to a partnership the
  record has no case for. The paper does not supply one.
- **Gene transfer by viruses** is a route to a chimeric genome that involves
  no partnership at all. It sits outside QUESTION-277's five routes, which
  are routes to dependence between partners.
- Filed as THEORY-tmphywi5. No instruction for machine-learning practice.

## Limitations

- **The calibration is partly circular.** Thresholds are chosen to maximize
  the accepted partners' share, assuming those signals are the true ones.
  Any donor that survives is real only relative to that assumption. The
  authors state the assumption.
- **The controls are in the supplement**, which was not read here:
  verticality, tree difficulty, reanalysis of an earlier study, functional
  classes in the stem-length analysis, and the effect of OrthoFinder
  splitting.
- **A liberal pangenome filter.** At 15% of genera per order, more
  lineage-specific genes enter the database than under Tobiasson et al.'s
  filter. Whether that admits late transfer into eukaryotes is the other
  group's objection and is not tested here.
- **Stem length as time** is assumed, defended by citation, and contested by
  Tobiasson et al.'s data. If it fails, the order of waves fails with it,
  and with it the claim that some transfers preceded the mitochondrion.
- **The donor metabolisms are indirect.** They are prevalences in living
  relatives, not ancestral reconstructions. No statistical test was used for
  functional enrichment, "as the sample sizes were non-homogeneous".
- **The mat comparison is an analogy** with one mat (Fig. 3b).
- **A slip.** The viral share is given as "approximately 4.5% of the
  mLECA-OG phylogenies" in the results and as "at least 4.5% of all
  acquisitions" in the virus section. If acquisitions are about 53% of
  families, those cannot both hold. The first is the better supported, by
  the arithmetic in the history above.

## Open questions

- Does the Myxococcota and Planctomycetota signal survive Tobiasson et al.'s
  stricter pangenome filter, or do theirs fail under this paper's thresholds?
  Running each pipeline on the other's database would settle which filter
  drives the difference.
- What would distinguish a symbiotic donor from a source of transferred
  genes in phylogenomic data? The paper does not say; nor does Tobiasson et
  al.'s.
- Is stem length a clock? The answer decides the ordering of waves and the
  premitochondrial claim.
- Were the viral-route genes picked up from extinct eukaryote-like lineages,
  as the authors suggest? That would make some "acquisitions" transfers
  between stem eukaryotes.
