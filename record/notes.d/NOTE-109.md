---
number: 109
status: Read
formerly:
- NOTE-tmp9afca
paper: LIT-211
title: 'Bender et al. — What Lives? (definitions of life)'
version: 2
history:
- version: 2
  date: '2026-09-26'
  note: >-
    Read in full (full text of arXiv:2505.15849 as served on 2026-09-26 (v2,
    revised 6 Aug 2025), 54 pp.: main text pp. 1–30 (§§1–5, §7; there is no
    §6), references pp. 31–33, and the in-PDF supplement pp. 34–54 (all 68
    definitions in Supp. Table 1, Supp. Tables 2–3, captions of Supp. Figs
    1–11; the figure images were not inspected). I also read the
    Supplemental Code repository (github.com/mrbende/what-lives, HEAD
    93c8e0c, 6 Jul 2026): the pairwise prompt, `what_lives.py`,
    `inference.py`, `stats_cross_cluster.py` and the saved correlation
    matrices and cluster statistics. I recomputed the clustering from the
    saved matrices. The four supplemental cluster-analysis markdown files
    (Supp. Files 1–4) were not read.). Upgraded from `Skimmed` to `Read`:
    the claims table, assumptions and results are new, and the skim is
    corrected where the full text disagreed.
date: '2026-09-26'
summary: >-
  Three LLMs (Claude 3.7 Sonnet, GPT-4o, Llama 3.3 70B), each run 3 times
  on both orderings of every pair, rated 68 hand-solicited definitions of
  life on a −1 to 1 "correlation" rubric. The averaged matrix, cut by
  complete-linkage clustering at an elbow, gives 8 clusters, 45/68 of them
  (66%) in "Cognitive Autonomy" (n=24) and "Dissipative Self-Organizing
  Systems" (n=21). The clusters are weak: the repo's own saved statistics
  give an overall silhouette of 0.079, and cross-model agreement is an
  unadjusted Rand index of 71–79% against a chance level of about 62–74%.
  The headline that life is "a continuous semantic landscape" is not
  tested against any alternative.
---

# NOTE-109: Bender et al. — What Lives? (definitions of life)

## Contribution

A dataset of 68 short definitions of life. They were solicited by email from researchers the authors hand-picked, and are printed in full with names (Supp. Table 1). The paper adds a manual thematic coding (Table 1, Fig. 2) and a pipeline for scoring and clustering short texts with LLM pairwise judgements. The dataset and the manual coding are what is new and durable. The computational "landscape" is one run of an untested pipeline with no human-rater validation and no null comparison.

## Key insight

With respondents chosen this way, definitions of life do not fall into a few crisp schools. The largest groups mix physics, information and agency vocabularies, and agency or goal-directedness now appears in about a quarter of expert definitions. That is a statement about expert discourse, which the paper sometimes rewrites as a statement about life: "reveals life as a continuous semantic landscape" (p. 27).

## Assumptions

- **LLM ratings as a similarity measure.** A number an LLM outputs when asked for a "correlation metric between -1.0 and 1.0" between two definitions is taken as a valid measure of conceptual similarity. It is not a Pearson correlation of anything. No human raters and no embedding baseline were used to check it (the embedding-based "bedrock" projections exist only in the repo).
- **Agreement as validity.** Agreement between three LLMs is treated as evidence that the structure is real (p. 24: "genuine features of the definitional landscape rather than analytical artifacts"). All three models read the same rubric, so shared priors and a shared prompt could explain the agreement equally well.
- **The sample.** 68 respondents, "hand-curated by the authors", "not ... a representative sample" (p. 28). 41 are affiliated in the US and 9 in the UK. Two are authors of the paper. Respondents could consult references and colleagues, saw some other definitions before proofing, and some responses were shortened by the editors (p. 10).
- **t-SNE axes.** The axes of a t-SNE map are interpretable coordinates. They are not: perplexity was 30, init random, seed 33 (`what_lives.py`, l. 861).

## Key results

- **Pairwise scoring (pp. 10–11).** Each unordered pair is scored 3 times per ordering at temperature 0.3 (`inference.py`, l. 58). The matrix is symmetrized as M′ = (M + Mᵀ)/2, giving 6 scores per model per pair. The three model matrices are averaged, so each cell is a mean of 18 LLM outputs.
- **Distributions (Supp. Table 2).**
  - Claude 3.7 Sonnet: mean 0.30, median 0.37.
  - Llama 3.3 70B: mean 0.17, median 0.20, SD 0.510.
  - GPT-4o: mean 0.20, median 0.32.
  - Averaged matrix: mean 0.22, median 0.32, range −0.84 to 0.82.
  - Skewness −0.76 to −0.97, i.e. biased toward similarity.
- **Inter-model matrix correlations (p. 18).**
  - Claude–Llama r = 0.7279, Claude–GPT r = 0.8103, Llama–GPT r = 0.7977.
  - Each model against the average: 0.90–0.94 (not independent, since each model is part of the average).
- **Clustering (pp. 11–12, 19).**
  - Distance d = √(2(1−r)), complete linkage.
  - k is the elbow of the merge heights. In code, the argmax of the second difference, clamped to 2–15.
  - Claude gives 7 clusters, Llama 11, GPT-4o 11, the average 8 (Supp. Table 3).
  - Average: intra-cluster r 0.509 ± 0.187, inter-cluster r 0.150 ± 0.390. The "contrast metric" 0.359 is intra minus inter; this holds for all four rows.
- **Robustness (p. 20).**
  - Pairwise "consistency" is 71.2–79.1%: an unadjusted Rand index, near its chance level (see corrections).
  - Overall "grouping stability" is 53.7%: the mean over definitions of the share of other definitions grouped the same way by all four partitions.
  - Most stable: Fields and Hoffman (100%). Least stable: Solms, Sloman, Davies, Froese, Wong (22–28%).
- **Clusters (Table 2, pp. 21–22; sizes pp. 23–26).**
  - Perceptual Categorization 2: Fields, Hoffman.
  - Self-Sustaining Dynamic Patterns 4.
  - Dynamic Relational Process 2.
  - Pragmatic Definitional Skepticism 4.
  - Cognitive Autonomy 24.
  - Dissipative Self-Organizing Systems 21.
  - Informational Self-Replication 3: Adamatzky, Adami, Pizzi.
  - Self-Replicating Thermodynamic Systems 8.
  - Consensus definitions and titles were written by Claude 3.7 Sonnet alone.
- **Manual coding (Table 1, Fig. 2, pp. 16–17).**
  - Themes: dynamics/self-organization 29%, thermodynamics 26% (18/68), information/pattern 25%. Autonomy/agency/goal-directedness covers 17/68 and cognition/intelligence 12/68.
  - Stances: 57% objective vs 43% observer-relative; 54% continuous vs binary; 88% "actionable".
- **t-SNE (pp. 22–24, 27).** Two post-hoc axes: observer-dependent ↔ objective, and process ↔ entity. The authors chose t-SNE over MDS, PCA and UMAP as "the best spatial projection" (p. 15), with no criterion stated.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Three LLMs' pairwise-similarity matrices over the 68 definitions correlate at r = 0.73–0.81. | moderate | Computed, p. 18. The repo's matrices give 0.77–0.85, so the numbers are not exactly reproducible. It shows the models agree, not that they are valid. |
| C2 | The averaged matrix partitions into 8 clusters, 45/68 of them in Cognitive Autonomy and Dissipative Self-Organizing Systems. | moderate as a description of this pipeline's output; weak as a claim about structure | Reproduced from the repo. Silhouette is 0.079 at k=8, and k=8 comes from a single elbow heuristic. |
| C3 | The clusters are "stable conceptual attractors that persist across different computational analyses" (p. 29). | weak | Per-model k is 7–11 (5 in the repo for Claude). The adjusted Rand index is 0.22–0.38. Grouping stability is 53.7%. |
| C4 | The definitions form "a continuous landscape" rather than discrete categories (abstract; p. 27). | weak | Not tested against any alternative. Graded ratings, averaged over 18 outputs and projected by t-SNE, will look continuous whatever the texts are. The low silhouette is consistent with this but is not a test of it. |
| C5 | Therefore "what is life?" should be treated as a multidimensional space, not a binary (abstract; p. 29). | assertion | This slides from the similarity of definitions to the nature of life. The only datum bearing on life itself is that 54% of respondents framed life as continuous (Fig. 2). |
| C6 | The t-SNE axes (observer-dependence; process vs entity) "emerge ... without explicit encoding" and recapitulate ancient philosophical tensions (p. 29). | assertion | Post-hoc reading of t-SNE axes. The repo prompt explicitly scores "Ontological claims" and "Epistemological approach", so the dimensions were at least partly encoded. |
| C7 | The 66% concentration "indicates emerging consensus" integrating physics, information and agency (pp. 27, 29). | weak | These are cluster memberships in a curated sample, not a density measured over any population. The authors disclaim representativeness on p. 28. |
| C8 | About a quarter of the definitions invoke autonomy, agency or goal-directedness. | moderate | Manual coding, Table 1: 17/68. There is a single unnamed coder, no reliability statistic, and categories may overlap. |
| C9 | Current LLMs "might occupy positions between 'Cognitive Autonomy' and 'Informational Self-Replication'" (p. 27). | assertion | No LLM or AI system was placed in the space. |

## Method

1. **Solicitation.** Researchers were emailed and asked for at most 3 sentences on "what is life?" (or an argument that it cannot be defined). 68 definitions were included.
2. **Manual coding.** The definitions were coded into 13 non-exclusive themes (Table 1) and three binary stances (Fig. 2).
3. **Pairwise scoring.** For each ordered pair, a system prompt holds the rubric and the two definitions, and the user turn asks "What is the correlation metric between -1.0 and 1.0 ... ONLY a single number!". This is run 3 times at temperature 0.3, averaged, and symmetrized. Models: `claude-3-7-sonnet-20250219`, `gpt-4o-2024-11-20`, and `us.meta.llama3-3-70b-instruct-v1:0` on Bedrock (`model_config.yml`). The three matrices are averaged element-wise.
4. **Clustering.** Distances d = √(2(1−r)); scipy complete linkage with `optimal_ordering=True`; k = the argmax of the second difference of merge heights, clamped to [2, 15]; `fcluster` with `maxclust`.
5. **Cluster analysis.**
   - Claude 3.7 Sonnet writes a thematic analysis of each cluster (the WHAT, HOW and WHY prompt, pp. 12–13).
   - It then writes a consensus definition. The prompt allows "Only majority-shared concepts (>50% frequency)", but whether the output complies is not checked.
   - Finally it writes a 2–4-word title.
6. **Projection.** t-SNE on the precomputed distance matrix. Contours are added for density. MDS, UMAP and ensemble projections appear in Supp. Fig. 11.

**Robustness checks, all of them.**
- Replicate averaging, within each model.
- Matrix correlation between models.
- Rand-type partition agreement between models.
- A per-definition grouping-stability score.

**Checks not done.**
- No silhouette or gap statistic is reported.
- No bootstrap over definitions.
- No null model, such as shuffled or synthetic definitions.
- No comparison with human similarity ratings or with a text-embedding baseline.
- No sensitivity analysis over prompt, linkage or k.

## Concepts

- **correlation (between definitions)**: an LLM-elicited rating on a verbal rubric running from −1 ("fundamentally opposing ... frameworks") to 1 ("aligned core frameworks and secondary elements"). It is not a statistical correlation.
- **contrast metric**: mean intra-cluster rating minus mean inter-cluster rating.
- **clustering consistency**: the fraction of definition pairs on which two partitions agree about together vs apart. This is the unadjusted Rand index.
- **grouping stability**: for each definition, the fraction of the others whose together-or-apart status is the same in all four partitions (the three models plus the average).
- **Cognitive Autonomy (cluster)**: Claude's label for the 24-member cluster. Its consensus definition: "a self-maintaining, goal-directed system that processes information ... an autonomous agent that actively opposes entropy ... a cognitive process that senses, interprets, and responds" (p. 21).
- **Its members** (repo): Ackley, Agüera y Arcas, Ball, Bongard, Calvo, Dodig-Crnkovic, Fontana, Froese, Gentili, Heylighen, Krakauer, Levin, Lyon, Miller, Noble, Reber, Rechavi, Shapiro, Solms, Soto, Stepney, Sultan, Vallverdú, Witkowski.

## Connections

The paper places itself among work on definitional pluralism and on life without a definition. It cites Machery 2012, Cleland & Chyba, Mariscal & Doolittle 2020, and Malaterre & Chartier 2021. Malaterre & Chartier is the closest methodological precedent (a data-driven "lifeness"), but it gets only a citation, with no comparison. None of those four works is held in this record; grep of literature.d found none.

- **[LIT-167](../literature.d/LIT-167.md) (Baedke, *The Organism*).** Baedke argues that self-maintenance or closure ("persister") criteria cannot single out organisms, because colonies and ecosystems meet them too. The Dissipative and Cognitive Autonomy consensus definitions are exactly persister criteria. So this dataset shows how common the criterion Baedke criticizes is. It does not answer his objection.
- **[LIT-168](../literature.d/LIT-168.md) (Wilson & Barker, *Biological Individuals*).** Their living-agent vs Darwinian-individual axis roughly lines up with the split in this paper: Cognitive Autonomy and Dissipative on one side, the two replication clusters on the other. The paper does not draw this connection.
- **[LIT-120](../literature.d/LIT-120.md) (Bruckner, *Welfare Subjects and Autopoiesis*; Deferred).** Bruckner's autopoiesis-sufficient criterion is close to the Heylighen, Soto and Lyon definitions in the Cognitive Autonomy cluster. The paper's suggestion to "guide ethical ... decisions" (p. 3) is the same link between life criteria and moral standing, but it goes undeveloped.
- **[LIT-195](../literature.d/LIT-195.md) (Safron et al., *World models ...*; Deferred).** It has Levin among its authors, and shares the life–mind-continuity framing of Levin's definition here and of the Dodig-Crnkovic, Lyon and Fontana definitions.

**Account of agency.** The paper holds none of its own. "Agency" appears as a theme label and as one of four integrating ingredients ("Agential properties (goal-directedness, adaptive behavior)", p. 27). The account of agency it presupposes is the respondents'. Examples:
- Ball: "the ability to manipulate themselves and their environment to achieve autonomously determined goals".
- Soto: "a goal-pursuing normative agent, capable of creating its own norms".
- Lyon: "actions aimed at realizing internally generated goals".
- Noble: "self-creating agency".
- Ellis: agency as flexible interaction that "enhances relative survival prospects of its progeny".

**Tag verdict.** The `agency` tag is justified. Someone browsing "what it is to be an agent ... in organisms, collectives or machines" would be right to expect this document. It is a census of how often experts make agency or goal-directedness constitutive of life (17/68, Table 1), and it prints those definitions verbatim. The justification should rest on Table 1 and the definitions, not on the LLM-named cluster. The cluster is an artifact of the pipeline, and it contains non-agential computational definitions: Ackley, Agüera y Arcas, Bongard, Stepney, Witkowski.

## Bearing on the record

- **Nucleation.** This is a primary-source collection for any THEORY or note on agency-based or life–mind-continuity definitions of life. The value is in Supp. Table 1 and Table 1, not in the clustering. It should not be cited as evidence that "life is continuous" or that there is an "emerging consensus" (C4, C5, C7).
- **[LIT-211](../literature.d/LIT-211.md).** The history note should be corrected to ground the agency tag in the manual 17/68 coding (see corrections).
- **ML practice.** Nothing for ML practice in the Anthology. The one ML-adjacent lesson is methodological and negative, and it is already standard in the LLM-as-judge literature: inter-model agreement is not validity, and a Rand index needs a chance correction. If the Anthology holds an LLM-as-judge practice, this is at most a cautionary example. It is not a source.

## Limitations

- **Sample.** Hand-picked, US-heavy, and including two of the authors. The authors concede it is not representative (p. 28).
- **Validity.** LLM ratings are never compared with human judgement. The prompt in the repo embeds anchor examples that fix some inter-framework similarities in advance.
- **Robustness.**
  - Only three models, one prompt and one linkage.
  - The robustness statistics are unadjusted, and one of the compared partitions is not independent of the others.
  - The per-model results in the repo differ from those in the paper.
- **Continuity.** "Continuity" is never set against a hypothesis that could fail. The discrete 8-cluster result and the "continuous landscape" are both asserted from the same weakly separated data (silhouette 0.079).
- **Interpretation.** The t-SNE axis readings are post hoc. The cluster names and consensus definitions are one model's (Claude's) output, unchecked against the >50%-frequency rule its prompt sets.
- **Manual coding.** A single coder, no reliability statistic. McShea is listed twice in the "Against strong definition" row.

## Open questions

- Do human expert raters reproduce the pairwise matrix? A rank correlation with a human-rated subsample would settle the validity question.
- Is the 8-cluster partition stable? Bootstrapping over definitions, or varying the prompt (printed vs repo rubric), would show it. So would comparing the result against a null of synthetic or shuffled definitions.
- Does the share of agency-based definitions (≈25%) hold in a sample not drawn from the authors' network, for instance a random draw of origin-of-life and astrobiology authors?

## Corrections to the seeded skim

- Table 1 (manual categorization) is on pp. 16–17, not pp. 30–31. pp. 30–33 are acknowledgements and references. The pairwise-correlation results are on p. 18, not pp. 17–19.
- The pairwise prompt printed in the paper (pp. 10–11) is a six-line rubric. The prompt file in the Supplemental Code (`prompts/definition_correlation.txt`) is much longer. It scores seven dimensions, adds calibration rules, and gives anchor benchmarks: "A purely thermodynamic vs purely informational definition ≈ 0.0 to 0.2", "A metabolism-first vs replication-first definition ≈ -0.4 to -0.6", "A definition based on reproduction vs one rejecting reproduction as necessary ≈ -0.7". Which version produced the published matrices is unverified. If it was the repo version, part of the geometry was set in advance by the authors' priors, not found by the models. At minimum, the printed prompt is abridged.
- The paper's "clustering consistency" of 71.2–79.1% (p. 20) is an unadjusted pairwise Rand index (`stats_cross_cluster.py`, lines 218–243). One of the four partitions compared is the multi-model average, which is built from the other three and so is not independent of them. Recomputed from the repo matrices, the chance Rand index for these partition sizes is 0.62–0.74, and the adjusted Rand index is 0.22–0.38. The paper's reading of this as "substantial agreement" overstates it.
- The saved `cluster_statistics.json` for the multi-model partition reports an overall silhouette of 0.079. Recomputed, the averaged matrix's silhouette is 0.22–0.23 at k=2–4 and 0.079 at the chosen k=8. The elbow (the maximum second difference of merge heights) chose a k at which the clusters barely separate. The paper does not report silhouette.
- The repo's per-model matrices do not reproduce the paper's per-model numbers. Inter-model r is 0.77 / 0.85 / 0.85 in the repo against 0.73 / 0.81 / 0.80 in the paper. The Claude elbow gives k=5 in the repo, not 7, and Llama's largest cluster is 18, not 32. The multi-model partition (8 clusters; 24, 21, 8, 4, 4, 3, 2, 2) does reproduce exactly.
- The skim's "two thirds ... in Cognitive Autonomy and Dissipative" is right: 45/68 = 66.2%. The LIT history's gloss, "so its subject is autonomy as a mark of life", is not. Cognitive Autonomy is 24/68 (35%). The Dissipative cluster (21) is thermodynamic and organizational, not agential. The cluster name was generated by Claude 3.7 Sonnet from a prompt demanding a "DISTINCTIVE" 2–4-word title (p. 14).
- Both author-supplied definitions (Agüera y Arcas, Levin) fall in the Cognitive Autonomy "primary attractor" (repo `cluster_statistics.json`). The paper says only that they received no extra weight (p. 10).
- agency tag: justified, but for a different reason than the LIT history gives. The grounds are the manual coding: "Autonomy/agency/goal-directedness" covers 17/68 definitions (Table 1, p. 16). There is also the paper's listing of "agential properties (goal-directedness, adaptive behavior)" among the four integrating themes (p. 27). The LLM-named cluster is weaker evidence: only 10 of those 17 fall in Cognitive Autonomy.
