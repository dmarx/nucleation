---
status: Read
paper: LIT-tmpc7kaa
title: 'Larremore and others 2014 — Efficiently inferring community structure in bipartite networks'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    URL read: https://arxiv.org/pdf/1403.2933 (HTTP 200, 4.1 MB PDF, v2 of
    10 Jul 2014, 12 pages), fetched 2026-11-19. Kind of copy (step 5): arXiv
    preprint, the authors' own upload. No obstacle (pdftotext reported a
    reconstructed xref table; the text extracted in full). Text extracted
    with pdftotext (reading order) to dl/text.txt and with -layout to
    dl/text_layout.txt. Read: the whole paper — abstract, §I-V, Appendices
    A-B, figure captions; references glanced. Skipped: nothing of substance;
    figures read from captions, not inspected as images.
date: '2026-11-19'
---
<!-- inactive-ok-file: CASE-tmpsjjgx CLAIM-tmpj540o — Proposed; cited in this filing of 2026-11-19 -->

# NOTE-tmp823hg: Larremore and others 2014 — Efficiently inferring community structure in bipartite networks

## Contribution

Larremore, Clauset and Jacobs (arXiv 1403.2933, v2 2014) formulate a bipartite stochastic block model (biSBM), with and without degree correction, in which vertex types are given and every group is of one type. A community is "a group of vertices with similar connectivity patterns to other groups", not a densely connected cluster. They give maximum-likelihood objectives (Eqs. 9 and 16) and a Kernighan–Lin-style search that moves vertices only within their type. They show that the biSBM is the SBM with two constraints applied, but finds better partitions faster. On synthetic networks it recovers planted structure that one-mode projections hide. They apply it to the Southern Women data, a malaria var-gene network and an IMDb actor–movie network.

## Key results

- **Community as connectivity pattern** (§I, p. 1): the biSBM "defines a community as a group of vertices with similar connectivity patterns to other groups". In bipartite data "assortativity-based definitions of communities are ill-suited".
- **Degree-corrected objective** (§II.B, Eq. 16, p. 3): L(G | g) = Σ mrs ln(mrs/κr κs) over pairs of groups of different types. Without degree correction "the uncorrected biSBM finds edge bundles between communities with Poisson degree distributions, which in practice tends to sort vertices by degree" (p. 3).
- **Same ensemble, different inference** (§III.A, p. 4): the biSBM and constrained SBM are numerically equivalent, "However, these equations, while numerically equivalent, are not identical due to their meanings and behaviors." The SBM "often overfits bipartite data by mixing vertices of different types within communities" (p. 4). It found pure-type partitions in only "eight of 2000 replicates" on the malaria data, and the biSBM converged "3.25 times faster" (p. 6).
- **Projections hide structure** (§IV.A, p. 7 and Fig. 3B): in the difficult case, "When using either weighted or unweighted projections, the SBM (with or without degree correction) is unable to find any community structure." The degree-corrected biSBM shows a detectability transition "with a critical point at λ ≈ 0.33".
- **IMDb actor–movie network** (§IV.B.3, p. 9–10, Fig. 8): 53,158 actors and 39,768 movies (1995–2000). With Ka = Kb = 6, "Groups 5 and 6 are predominantly English movies, while groups 1, 2, and 3 are foreign films, separated by language. Group 4 on the other hand, is defined not by language, but by genre, consisting of Adult films across many languages." Groups 5 and 6 "showed similar language and genre profiles, but their separation suggests the existence of an additional variable governing the probability of edge existence" (Fig. 8 caption).
- **Generative interpretation** (§IV.B.3, p. 10): "this correspondence between genre, language, and inferred blocks provides insight into the multiple mechanisms responsible for the existence of edges."
- **Model selection is open** (§V, p. 11): the choice of Ka and Kb "can be framed as a question of model selection", and the likelihood's "ruggedness makes the standard limiting assumptions inapplicable".

## Assumptions

- Vertex types are known. Edges join only different types, and edge counts are Poisson with mean θiθjωgigj (degree-corrected).
- Each vertex belongs to exactly one group (no mixed membership: "Mixed-membership stochastic block models ... have not yet been formulated for bipartite networks", p. 11).
- Ka and Kb are given, not inferred.

## Concepts

- **Stochastic block model**: groups defined by stochastic equivalence, that is, by the same expected connection rates to every group, not by internal density.
- **Degree correction**: per-vertex propensities θ, so that groups are not just degree classes.
- **One-mode projection**: linking two same-type vertices that share a neighbour. It discards information and creates overlapping cliques.
- **Pure-type and mixed-type partitions; detectability limit; normalized mutual information.**

## Bearing on the record

- **CASE-tmpsjjgx** — supports the case's method and qualifies its example. The joint identification the case describes is what the biSBM does: groups of films and groups of people, each defined by their connection pattern to the other side's groups. But the paper's own film data is actor–film co-appearance, not ratings or engagement. There, the inferred film blocks were mostly language groups, and only one block (Adult) was defined by genre. So in the one film example the paper gives, the blocks that emerge are mostly not genres, and the authors read them as traces of "multiple mechanisms responsible for the existence of edges". This is direct support for the case's confounds section: blocks track whatever generates edges (language, market, casting), which need not be the category a person would name. The paper does not study recommendation or feedback, so the case's laboratory arms are untouched. Its warnings that projections hide structure and that uncorrected models sort by degree bear on the case's popularity control: degree correction is the in-model way to keep popularity from defining classes.
- **QUESTION-tmpex36a, THEORY-1065** — an observation, not the paper's. An SBM block is a stochastic analogue of a balanced partition: vertices in a group have the same expected number of edges to each group. This is THEORY-1065's condition, the same number of inputs from each class, holding in expectation. Neither the paper nor the record states this link. If it were made, the genres case and the fibration hunch would share one formal object.
- **TERM-062, QUESTION-tmpcb0bf, CLAIM-tmpj540o, THEORY-1059** — no direct bearing.

## Limitations

- Single membership and fixed numbers of groups. Model selection is left open.
- Edge presence only (unweighted, Poisson multi-edges). Ratings or graded engagement would need a weighted extension, which the paper names as future work.
- The IMDb interpretation is descriptive: language and genre labels were compared with the blocks by inspection ("over 90% of movies in the indicated language are in that group", Fig. 8). No quantitative test is given.
- Synthetic tests use planted biSBM structure, so they show recovery under the model, not that real communities have this form.
