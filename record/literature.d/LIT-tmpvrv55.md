---
status: Proposed
status_note: 'read in full 2026-10-02 ([NOTE-tmpmbgch](../notes.d/NOTE-tmpmbgch.md)); worth reading for the Morality-as-Cooperation Dictionary and for what it shows about the sixty-society result, not as a replication of it. The dictionary counts words and, by the authors'' own statement, "cannot be used to estimate the moral valence of cooperation", so it does not test the 961-of-962 finding at all. Its agreement with the earlier hand codes is slight to fair (κ .08–.25), and it inflates fairness from 15% to 58% of societies. It detects significant, though small, regional differences, against the earlier claim of equal frequency. A spot-check of its paragraphs found admired theft in four more societies. It would be settled by valence-aware coding validated against blind hand codes, run with dictionaries for non-cooperative domains on the same corpus.'
title: 'Moral universals: A machine-reading analysis of 256 societies'
version: 1
history:
- version: 1
  date: '2026-10-02'
  note: >-
    Read in full (the version of record, Heliyon 10(6):e25940, open access
    under CC BY-NC-ND 4.0, full-text XML of PMC10945118 from Europe PMC; the
    PMC page itself returned a bot challenge). I read the abstract, §§1–5,
    Tables 1–6, the figure captions, the significance statement, the
    footnotes and the reference list. The figures were not seen, and the
    supplementary file (the dictionary) was not opened. The Research Square
    preprint (rs-1841350 v1, 2022-07-18) was not compared. Not held in the
    Anthology of the SOTA: a grep of its literature.d for the DOI, the
    title, "Alfano", "LIWC" and "morality" found nothing. `published:` is
    the preprint date; the article was received 2023-03-17 and appears in
    the 30 March 2024 issue.
tags:
- moral-psychology
- social-science
date: '2026-10-02'
published: '2022-07-18'
doi: '10.1016/j.heliyon.2024.e25940'
first_author: 'Alfano'
keywords:
- 'morality'
- 'cooperation'
- 'ethnography'
- 'universals'
- 'natural language processing'
- 'LIWC'
implementations: []
summary: >-
  Alfano, Cheong & Curry (2024), DOI-10.1016/j.heliyon.2024.e25940. A
  word-count dictionary for the seven morality-as-cooperation domains
  (MAC-D, built by expert brainstorming and WordNet expansion) is run over
  9,653 eHRAF Ethics paragraphs from 256 societies. Most morals are detected
  in most societies, with small but significant differences by region and
  subsistence. Against the earlier hand codes the dictionary agrees only
  slightly to fairly (κ .08–.25) and overstates prevalence. It cannot tell
  praise from condemnation, so it says nothing about valence.
---

<!-- inactive-ok-file: LIT-047 — Proposed: the sixty-society test this paper extends, whose verdict this reading bears on -->

# LIT-tmpvrv55: Moral universals: A machine-reading analysis of 256 societies

Mark Alfano, Marc Cheong, Oliver Scott Curry (2024), *Heliyon* 10(6):e25940 —
DOI-10.1016/j.heliyon.2024.e25940

## Key takeaways

- A dictionary for the seven morality-as-cooperation domains, run over the
  whole eHRAF Ethics corpus, detects most of the seven in most of 256
  societies.
- The tool is valence-blind, and agrees poorly with the hand codes it was
  validated against, so it extends the presence result of the sixty-society
  study and leaves its valence result untouched.

## Standing in the record

Filed on 2026-10-02 at the owner's request, with the rest of the
morality-as-cooperation programme ([ADR-018](../decisions.d/ADR-018.md)). It is the programme's attempt to
go beyond the sixty-society hand coding ([LIT-047](LIT-047.md)).

[NOTE-tmpmbgch](../notes.d/NOTE-tmpmbgch.md) is the close reading of 2026-10-02, and it placed the work
**Proposed**. It bears on [NOTE-034](../notes.d/NOTE-034.md)'s verdict in three ways, and none of them
moves [LIT-047](LIT-047.md) toward Active.

- **Valence.** The 99.9% positive-valence finding is the result [NOTE-034](../notes.d/NOTE-034.md)
  judged weakly diagnostic, and this paper cannot test it. The authors say
  the limitation is "probably not a major problem, given that cooperation
  had a positive moral valence in 99.9% cases". That leans on the finding
  in question.
- **Counterexamples.** The paper's own spot-check found admired theft among
  Bedouin, Greek, Pashtun and Wogeo groups. It also found !Kung San who
  "attach no value to fighting" and a Navajo ethnography reporting no
  obligation to reciprocate. [LIT-047](LIT-047.md) counted one negative in 962
  observations. The authors frame the new cases as "competition between the
  morals", which is footnote 3's move again. These were found by reading
  for them, and they bear out [NOTE-034](../notes.d/NOTE-034.md)'s point that the original design
  could hardly register a negative.
- **Regions.** All seven domains differ significantly by region
  (Kruskal–Wallis, p < .001), with small effects (ε² ≤ .055). [NOTE-034](../notes.d/NOTE-034.md)
  judged [LIT-047](LIT-047.md)'s "equal frequency across all regions" (its C4) to be
  absence of evidence; this paper finds a difference.

The comparison [NOTE-034](../notes.d/NOTE-034.md) asked for, non-cooperative content coded the same
way, is again not run. The authors say it cannot be, because there is "no
ground truth coding of Moral Foundations in HRAF". There is no ML practice
in it. It is a word-count method from before large language models, so it
is not an anthology candidate.
