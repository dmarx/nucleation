---
status: Skimmed
paper: LIT-tmpyap6v
title: 'Bender et al. — What Lives? (definitions of life)'
version: 1
date: '2026-09-26'
summary: >-
  When 68 expert definitions of life are scored pairwise by three LLMs and clustered, they form a continuous landscape with eight clusters, two thirds of them in overlapping "Cognitive Autonomy" and "Dissipative Self-Organizing Systems" clusters. The authors argue this makes "what is life?" a question about a multidimensional space rather than a binary demarcation.
---
<!-- inactive-ok-file: LIT-tmpvchky — Deferred: a seed from the same 2026-09-26 philosophy sweep, cross-referenced by the citing work's dossier; lapses when the cited work is read -->
<!-- inactive-ok-file: LIT-tmplgr0i — Deferred: a seed from the same 2026-09-26 philosophy sweep, cross-referenced by the citing work's dossier; lapses when the cited work is read -->
<!-- inactive-ok-file: LIT-tmp75cds — Deferred: a seed from the same 2026-09-26 philosophy sweep, cross-referenced by the citing work's dossier; lapses when the cited work is read -->

<!-- inactive-ok-file: LIT-tmpyap6v — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-26; the directive lapses when its status changes -->

# NOTE-tmp9afca: Bender et al. — What Lives? (definitions of life)

## Contribution

No definition of life commands universal agreement, and synthetic biology, AI and astrobiology make the question more pressing. The authors collected definitions of life from a curated set of cross-disciplinary experts and used large language models to score how similar each pair of definitions is. They then applied agglomerative clustering, LLM-driven analysis of the definitions within each cluster, and t-SNE projection. The result is a continuous landscape of themes, not a set of discrete camps. On that basis they recommend treating the definition of life as a set of perspectives within one conceptual space, and offer the method for other contested definitions.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §1 Introduction (p. 3): the paper positions itself between definitional pluralism and anti-binary or eliminativist views of life. The data are 68 expert answers to "what is life?". LLMs are used both to compute pairwise similarity and to write a consensus definition for each cluster.
- Table 1, manual coding (pp. 30–31): dynamics or self-organization is the most common theme (29%), thermodynamics and energetics 26% (18/68), information and pattern 25%. Respondents named in the table include Adami, Davies, Dussutour, Jablonka, Lane, Solms, Szathmáry, Watson and others.
- §4 Results, pairwise analysis (pp. 17–19): Claude 3.7 Sonnet, Llama 3.3 70B Instruct and GPT-4o each scored every pair on a −1 to 1 scale. Their matrices correlate at r = 0.73–0.81, and all three skew toward finding similarity. The paper uses the element-wise average.
- Table 2 (pp. 21–22): eight clusters with LLM-written consensus definitions: Perceptual Categorization, Self-Sustaining Dynamic Patterns, Dynamic Relational Process, Pragmatic Definitional Skepticism, Cognitive Autonomy (n = 24, the "primary attractor"), Dissipative Self-Organizing Systems, Informational Self-Replication, Self-Replicating Thermodynamic Systems.
- §7 Conclusion (p. 29): two emergent axes, observer-dependent vs objective and process-based vs entity-based, are said to "recapitulate ancient philosophical tensions". 66% of definitions fall in the overlapping Cognitive Autonomy and Dissipative clusters. The authors propose extending the method to cognition and memory.

## Open questions

- A data point for nucleation notes on life–mind continuity and on agency-based definitions of life. It is relevant alongside [LIT-tmplgr0i](../literature.d/LIT-tmplgr0i.md) (Baedke), [LIT-tmp75cds](../literature.d/LIT-tmp75cds.md) (autopoiesis) and [LIT-tmpvchky](../literature.d/LIT-tmpvchky.md) (Safron, Levin et al.).
- The method is the weak point to check. The "correlations" are LLM similarity judgments, not measurements. Model agreement shows the LLMs agree with each other, not that the clusters are real. The respondent pool was curated by the authors, many of them from Levin's network, so the "emerging consensus" on cognitive autonomy may reflect who was asked.
- Check whether the published version (if any) changed the analysis or the number of respondents from v1.
