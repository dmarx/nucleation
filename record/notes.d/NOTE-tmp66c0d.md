---
status: Read
paper: LIT-tmpuxnf3
title: 'Jaradeh et al. — Open Research Knowledge Graph: Next Generation Infrastructure for Semantic Scholarly Knowledge'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 from https://arxiv.org/pdf/1901.10816. **Read** in
    full, from the authors' arXiv manuscript (v3, headed "in Review for
    KCap'19"). The ACM published version is Unfetched (Cloudflare challenge);
    differences between the two are not known. A delegated reader drafted the
    reading; quotations were rechecked by script against the downloaded copy,
    and any that did not match were kept as paraphrase without quotation
    marks.
date: '2026-11-12'
summary: >-
  ORKG proposes to represent scholarly *knowledge* — research contributions,
  not bibliographic metadata — as a graph. A ResearchContribution relates a
  ResearchProblem to a ResearchMethod and at least one ResearchResult,
  described with unconstrained, user-chosen properties; statements are
  triples whose edge instances can be identified and annotated (for
  provenance). Features: State-of-the-Art comparison tables across
  contributions (similar predicates found by FastText embeddings),
  contribution similarity by TF-IDF, and NER/entity linking toward automated
  extraction.
---
<!-- inactive-ok-file: CLAIM-tmpyp3u3 TERM-tmp8deza — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->

# NOTE-tmp66c0d: Jaradeh et al. — Open Research Knowledge Graph: Next Generation Infrastructure for Semantic Scholarly Knowledge

## Contribution

An infrastructure design and alpha implementation for crowdsourced plus automated acquisition of structured descriptions of research contributions, with comparison across papers as the main service.

## Key results

- §4.1: "Currently, we do not further constrain the description of these resources." Users pick any vocabulary for problems, methods and results.
- §4.1 architecture: "Versioning and provenance handles tracking changes to stored data." — yet §6 lists "User authentication and versioning to track the evolution of curated scholarly knowledge are additional important features on the ORKG development roadmap." (The architecture names a layer whose function is still roadmap.)
- §6: "we opted for a simplistic model with lower barriers for content creation."
- §6: representing "as well as knowledge evolution is another open issue".
- §6: future: "we plan to integrate a discussion feature that will enable debating existing scholarly knowledge".
- §5.1: 12 participants; "While the cohort of participants was too small for statistically significant conclusions"; §6: "we suggest that authors are willing to provide structured descriptions of the key contribution".

## Assumptions

Published contributions are the unit; knowledge is captured after (or as) it is published, by authors and curators; a light schema with free properties will scale better than a rich model; comparison across papers is the main payoff.

## Concepts

Semantic scholarly knowledge; ResearchContribution (problem, method, result); statement-level provenance on edges; State-of-the-Art comparison; contribution similarity; crowdsourced and automated acquisition; curation roles (author, researcher, reviewer, curator).

## Bearing on the record

A (A20 §1) cites ORKG for structured representations of research contributions compared across publications, distinguishing a record of an evolving inquiry from a representation of published contributions. **Accurate.** The reading supports A's distinction directly: ORKG's unit is a published contribution, its schema is deliberately unconstrained, and versioning, evolution and debate are, in this paper, future work.

- **QUESTION-tmps5iou**. **Supports the distinction A draws; leaves the question open.** ORKG (2019) couples none of rationale, migration or executable checks to schema change; its schema is almost absent by design ("we do not further constrain"). It is evidence that the scholarly-knowledge-graph line, as of this paper, chose low-barrier unconstrained description over governed schema, which is the opposite trade from luria's. It does not show later ORKG versions lack governance (templates and versioning came later; not read).
- **CLAIM-tmpyp3u3 / TERM-tmp8deza** (shared epistemic state; who contributed what): ORKG's per-statement provenance annotations are a precedent for contributor attribution in a shared graph. Mention only.

## Limitations

The arXiv v3 is a review manuscript; the ACM version may differ. Evaluation is a 12-person qualitative session; scalability on synthetic data.
