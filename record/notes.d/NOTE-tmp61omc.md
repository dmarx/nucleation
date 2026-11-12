---
status: Read
paper: LIT-tmpeyhhi
title: 'Hasib et al. — Unifying AI-assisted scientific discovery around exploration, hypothesis generation, and testing'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 from
    https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13674306/fullTextXML.
    Read: the main text in full on 2026-11-12. The stage sub-sections and the
    tools and datasets sections were read in part. A delegated reader drafted
    the reading; quotations were rechecked by script against the downloaded
    copy, and any that did not match were kept as paraphrase without quotation
    marks.
date: '2026-11-12'
summary: >-
  The review introduces EXHYTE (Explore, Hypothesize, Test) as an empirical
  workflow abstraction for AI-assisted scientific discovery. It maps a
  corpus of 87 papers (2018 to July 2025) onto stages and substages: | Stage
  | Substages | |---|---| | Explore | E1 query structuring; E2 retrieval; E3
  knowledge assembly | | Hypothesize | H1 generation; H2 prioritization | |
  Test | T1 experimental design; T2 testing and refinement | Its main
  findings: - **Maturity.** Explore is most mature; Hypothesize is weak
  beyond generation. - **Bottleneck.** The bottleneck is Hypothesize → Test
  and the feedback that follows it. - **Human role.** Integration does not
  imply automation. Problem formulation, interpretation and revision still
  need humans. - **Evaluation.** Evaluation leans on proxies. -
  **Hypothesis-space narrowing.** Systems inherit the scope of their inputs
  and may narrow the hypothesis space. - **Trust.** Completing more stages
  does not make a system more trustworthy.
---

# NOTE-tmp61omc: Hasib et al. — Unifying AI-assisted scientific discovery around exploration, hypothesis generation, and testing

## Contribution

The contribution is a process-centric taxonomy and a gap analysis of LLM and agent systems for discovery, with an interactive website. The authors call it a "review framework and a design map", not a theory of scientific method.

## Key results

- **Abstract.** "The central bottleneck remains the transition from hypothesis or idea generation to executable experimental or computational testing, followed by feedback that can refine subsequent workflow steps."
- **Corpus.** "The final corpus comprises 87 papers". The literature runs to July 2025.
- **Stage-level maturity.** "Our synthesis finds that Explore is the most mature stage". Also: "The weakest link remains Hypothesize → Test".
- **Stage-level maturity.** Integrated systems still stop short because "evidence interpretation, hypothesis revision, and scientific value judgment still require human checkpoints."
- **Robustness.** "Left unexamined, such systems may appear productive while systematically contracting the space of hypotheses a researcher considers."
- **Robustness.** "a system that completes more workflow stages is not necessarily more trustworthy than one that completes fewer while keeping its reasoning legible and its hypothesis space open."
- **Outlook.** "T → H/E (feedback-to-revision) requires reliable interpretation of noisy empirical results".

## Assumptions

- EXHYTE is abstracted from the systems surveyed. It is not a full account of science.
- The corpus came from keyword search on arXiv, bioRxiv and Semantic Scholar, followed by manual filtering.
- The authors judge maturity qualitatively. No counts per stage were seen in the text read.

## Concepts

- EXHYTE, its stages and substages
- boundary conditions (human-supplied inputs)
- H→T transition and T→H/E feedback
- self-driving labs
- hypothesis-space narrowing
- traceability, legibility and auditability

## Bearing on the record

The LIT says the review finds that retrieval and idea generation have progressed faster than executable testing and evidence-driven revision. This is accurate. The bigger-picture abstract says nearly that: retrieval, knowledge organization and idea generation "are advancing rapidly, but comparatively few systems" convert hypotheses into executable tests and use the evidence. Three caveats:
1. The judgment is a qualitative synthesis over 87 papers, not a measured rate.
2. The corpus ends in July 2025.
3. The paper also stresses human checkpoints for revision and the narrowing of hypothesis space. Both bear on a record of inquiry.

**LIT-2306 (Gottweis, Co-Scientist).** Qualifies how it should be read. The review cites Co-Scientist (its ref. 53) and uses it as a case study of a wet-lab-integrated workflow. It also cites the Cell follow-up by Penadés et al. on the cf-PICI tail-hijacking mechanism (ref. 80). The review places Co-Scientist's strength in Explore and Hypothesize, with Test supported by human-run wet-lab validation. That gives a stage map for reading LIT-2306.

**LIT-2289 (Ghareeb, "A multi-agent system for automating scientific discovery").** The review cites Ghareeb et al., "Robin: A multi-agent system for automating scientific discovery" (arXiv 2505.13400, ref. 26). It describes Robin as a lab-in-the-loop with human-executed assays and an LLM judge ranking candidates. So LIT-2289 is the Robin paper, and the review supplies its stage placement.

**LIT-2297 (Jansen, "Generating Literature-Driven Scientific Theories at Scale").** The review does not cite this work. It cites a different Jansen paper, CodeScientist (arXiv 2503.22708, ref. 19). The LIT's claim that the review "bears on" LIT-2297 should be weakened to "covers the class of system": literature-driven generation sits in its H1-S3 category.

**Other bearing.**
- **QUESTION-tmp7a7l4.** "Feedback-to-revision" as the weakest link directly concerns whether a system improves its inquiry from evidence.
- **The record's use as a scaffold.** The review's demand for traceability, evidence linking and an open hypothesis space bears on the record's role as a legible scaffold for inquiry.

## Limitations

- This is a qualitative review, and its corpus is selected by keyword with manual filtering.
- The cutoff is July 2025, so newer systems appear only on the website.
- The maturity judgments are not quantified in the text read.
- The reader read the stage subsections only in part.
