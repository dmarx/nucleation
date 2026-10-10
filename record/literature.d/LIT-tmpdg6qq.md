---
status: Active
status_note: 'read in full 2026-10-10 ([NOTE-tmpr4vy8](../notes.d/NOTE-tmpr4vy8.md)); worth reading as the founding statement of Floridi''s line on artificial agency: agenthood as interactivity, autonomy and adaptability at a stated level of abstraction, and moral agency as the capacity to cause moral good or evil, with accountability split from responsibility. Read §2.5, §2.6.2 (MENACE) and §3.2 for the position. It argues by cases and by rebutting four objections; nothing in it is derived, the permissiveness of its criteria is answered by assertion (p. 26), and the distributed morality it says the approach is for is promised, not worked out.'
title: 'On the Morality of Artificial Agents'
version: 2
history:
- version: 2
  date: '2026-10-10'
  note: >-
    Read in full from the authors' preprint in the University of
    Hertfordshire repository (uhra.herts.ac.uk/id/eprint/2235, file
    901820.pdf, 29 pp., self-numbered 1–29, digitally signed by Floridi
    2004-01-30; its acknowledgements thank the Minds and Machines referees,
    so it is the post-review text). The PDF's fonts are Type 3 with no text
    layer, so the text was read from rendered page images, all 29 pages:
    abstract, §§1–5, acknowledgements, footnotes 1–7, Figures 1–3 and the
    37 references. The preprint does not show the published pagination
    (Minds and Machines 14(3):349–379, 31 pp.), and the published text was
    not seen beyond the Springer landing page, whose abstract matches the
    preprint's. Page numbers in the NOTE are the preprint's. Crossref gives
    volume, issue, pages and an August 2004 issue date with no day, so
    `published:` is 2004-08-01 (month precision). Earlier appearances
    exist but carry no citable date: the paper was presented at CEPE 2001
    (Lancaster) and at Bari (acknowledgements), and the preprint was signed
    on 2004-01-30, a signing date rather than a posting date. The paper
    has no keyword list; the keywords below are its own terms. Status set
    from the reading: Active.
tags:
- agency
- ethics
- social-ontology
date: '2026-10-10'
published: '2004-08-01'
doi: '10.1023/B:MIND.0000035461.63578.9d'
first_author: 'Floridi'
keywords:
- 'artificial agents'
- 'moral agent'
- 'Method of Abstraction'
- 'level of abstraction'
- 'mind-less morality'
- 'accountability'
- 'Computer Ethics'
implementations: []
summary: >-
  Floridi & Sanders (2004), DOI-10.1023/B:MIND.0000035461.63578.9d. Whether
  something is an agent is fixed only relative to a level of abstraction
  (LoA), a chosen set of observables. At a suitable LoA a system is an agent
  if it is interactive, autonomous (changes state without stimulus) and
  adaptable (its interactions change its transition rules); humans,
  learning software and organisations all qualify. An agent is a moral
  agent if it can cause moral good or evil. Such an agent is accountable
  for what it causes, but responsibility (praise and blame) needs
  intentional states as well, so artificial agents can be moral agents
  that are accountable and not responsible, and are censured by
  modification, disconnection or deletion. The argument is by cases and
  by rebutting four objections. The paper's own MENACE example shows
  agenthood appearing and vanishing as the LoA changes.
extended_by:
- LIT-tmpqbvu8
- LIT-tmpqgb1s
---
<!-- inactive-ok-file: LIT-tmpqgb1s — Floridi 2013, distributed morality, filed unread in the same contribution; named as the paper that takes up what this one promises -->
<!-- inactive-ok-file: LIT-tmp6juhh — Floridi 2025, filed unread in the same contribution; named as the paper this line leads to -->
<!-- inactive-ok-file: QUESTION-009 — Deferred; the open question this paper offers an answer to -->
<!-- inactive-ok-file: CLAIM-010 — Rejected; the permissiveness objection, cited as the objection this paper's criteria meet -->

# LIT-tmpdg6qq: On the Morality of Artificial Agents

Luciano Floridi & J. W. Sanders (2004), *Minds and Machines 14(3), 349–379 (August 2004 issue)* — DOI-10.1023/B:MIND.0000035461.63578.9d

## Key takeaways

- Agenthood is relative to a level of abstraction. At the LoA the paper proposes, an agent is a system that is interactive, autonomous and adaptable. At a video-camera LoA a rock is none of the three, a thermostat is only interactive, and a human is all three (Figure 2). Learning software, webbots and organisations are agents at a suitable LoA (§2.6).
- The same system can be an agent at one LoA and not at a lower one. MENACE, Michie's matchbox noughts-and-crosses learner, is adaptable when only its games are observed. When its matchboxes are observed, the "learning" shows up as a deterministic update of state, and adaptability fails (pp. 11–13). Whether closed-source software is an agent therefore depends on whether its code can be seen.
- A moral agent is any agent capable of an action that "can cause moral good or evil" (criterion O, p. 15). This criterion is neither consequentialist nor intentionalist.
- Accountability and responsibility come apart. An agent is accountable for what it is the source of. To be responsible as well, it needs "the right intentional states" (p. 21). Search-and-rescue dogs and Oedipus are the paper's moral agents without responsibility. An artificial agent can be "accountable — though not responsible" (p. 26).
- Moral goodness at an LoA is a threshold function on the observables that stays within a tolerance. Human ethical judgement sets the tolerance, so the formalism supplies none of the normative content.
- For Computer Ethics, the paper argues that most of the ACM Code applies to artificial agents. Censure of an immoral artificial agent is maintenance, disconnection or deletion (§4).

## Standing in the record

Filed on 2026-10-10 at the owner's request, as part of the line of work that Floridi's "AI as Agency without Intelligence" (2025, [LIT-tmp6juhh](LIT-tmp6juhh.md)) builds on. The anthology holds none of the works in this line. This is the earliest paper in the line: it is where Floridi first separates moral agency from intelligence and mental states ("AAs, though not intelligent and fully responsible, can be fully accountable sources of moral action", p. 3), and the 2023 and 2025 papers carry it into their title, "agency without intelligence" ([LIT-tmp0pyws](LIT-tmp0pyws.md)). Its levels-of-abstraction method is the one used in Floridi's informational structural realism ([LIT-152](LIT-152.md), [NOTE-099](../notes.d/NOTE-099.md)) and his account of personal identity ([LIT-136](LIT-136.md)). Here the method is only outlined, and its definition is deferred to a 2003 Floridi & Sanders chapter, "The Method of Abstraction", which the record does not hold. The paper promises that its LoA will make "distributed morality" intelligible (pp. 3, 16), and takes this no further than naming it in the conclusion. Floridi 2013 ([LIT-tmpqgb1s](LIT-tmpqgb1s.md)) is the paper that takes it up.

For the record's agency line, the paper gives an answer to [QUESTION-009](../questions.d/QUESTION-009.md): a pattern is an agent when, at some LoA, it is interactive, autonomous and adaptable. That answer is as permissive as the objection the line already carries ([CLAIM-010](../claims.d/CLAIM-010.md)), and [NOTE-tmpr4vy8](../notes.d/NOTE-tmpr4vy8.md) sets out why.

[NOTE-tmpr4vy8](../notes.d/NOTE-tmpr4vy8.md) is the close reading of 2026-10-10, and it placed the work: **Active** — worth reading as the founding statement of the line. It argues by cases and by rebutting objections, and its criteria are LoA-relative in a way the paper embraces and does not limit.
