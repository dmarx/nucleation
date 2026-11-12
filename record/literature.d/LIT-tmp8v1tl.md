---
status: Active
status_note: >-
  Read on 2026-11-12 (NOTE-tmpnyqd9) from the authors' manuscript on the University of Wollongong's Research Online repository, hosted on Figshare (https://ro.uow.edu.au/articles/journal_contribution/Metamorphic_Testing_A_Review_of_Challenges_and_Opportunities/27764520, file https://ndownloader.figshare.com/files/50531136), a copy lawful under ADR-074. The University of Nottingham's accepted manuscript returned a Cloudflare challenge and UOW's older URL an AWS WAF challenge on 2026-11-12; neither was retried.
title: 'Metamorphic Testing: A Review of Challenges and Opportunities'
version: 2
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Filed, not read. Identifier checked on 2026-11-12 with Crossref, and confirmed not held by DOI, exact title and first author in record/literature.d. `published:`: Crossref's online date; the print issue is dated 2019-01-31. No email address was sent to any service. First application of ADR-tmppzz2h.
- version: 2
  date: '2026-11-12'
  note: >-
    Read (NOTE-tmpnyqd9), and Active: it supplies the vocabulary and the limits for scoring a change by relations rather than by one expected output. Metadata corrected from the manuscript: all seven authors (Tsong Yueh Chen, Fei-Ching Kuo, Huai Liu, Pak-Lok Poon, Dave Towey, T. H. Tse and Zhi Quan Zhou); venue ACM Computing Surveys 51(1), article 4, pp. 4:1–4:27; a review article, which the authors call "different from traditional surveys". `published:` unchanged. The summary is rewritten from the reading. THEORY-tmpw3g5u states its account.
tags:
- software-engineering
date: '2026-11-12'
published: '2018-01-04'
doi: '10.1145/3143561'
first_author: 'Chen'
keywords:
- metamorphic testing
- oracle problem
- metamorphic relation
implementations: []
summary: >-
  Tsong Yueh Chen, Fei-Ching Kuo, Huai Liu, Pak-Lok Poon, Dave Towey, T. H. Tse and Zhi Quan Zhou (2018), ACM Computing Surveys 51(1), article 4, DOI 10.1145/3143561. A review by the originators of metamorphic testing: where no practical oracle checks one output, a program is checked against metamorphic relations, necessary properties of the target algorithm across two or more related inputs and their outputs. It formalizes the relations, corrects four common misreadings, and is explicit that the method alleviates the oracle problem and "can never completely solve it", since the relations are necessary, not sufficient. Read for the exchange "luria experiment design", where A proposed such relations as the hidden scorer of a change to a record's schema; the reading supports that use with three limits (NOTE-tmpnyqd9).
---
<!-- inactive-ok-file: ADR-tmppzz2h — Proposed; the decision this entry first applies -->
<!-- inactive-ok-file: THEORY-tmpw3g5u — Proposed; the account this reading files -->

# LIT-tmp8v1tl: Metamorphic Testing: A Review of Challenges and Opportunities

Tsong Yueh Chen, Fei-Ching Kuo, Huai Liu, Pak-Lok Poon, Dave Towey, T. H. Tse and Zhi Quan Zhou (2018). ACM Computing Surveys 51(1), article 4, 4:1–4:27. DOI 10.1145/3143561.

## Key takeaways

- A metamorphic relation is a necessary property over two or more inputs and their outputs; a violation shows a fault, satisfaction does not show correctness (§2.2, §4.1).
- The relations need not be equalities, and are tested, not proven (Concept 3, §5.1).
- Where the relations come from decides what passing them shows: from a specification for verification, from users' expectations for validation (§5.2).
- Relations mined from the program's own runs "may be erroneous if the implementation is faulty" (Challenge 2).

## Standing in the record

Registered on 2026-11-12 from the exchange "luria experiment design" (https://chatgpt.com/share/6af35bfc-35f8-83e9-a63d-d594703eabda), at A50 (§11), once ADR-tmppzz2h added `software-engineering`, and read the same day. A cited it as the oracle for scoring a change to a record's schema without one canonical patch. The reading bears on the proposed schema-change study of that exchange and on CLAIM-266, as NOTE-tmpnyqd9 sets out.
