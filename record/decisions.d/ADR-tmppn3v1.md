---
status: 'Proposed'
title: 'philosophy-of-technology joins the topics'
version: 1
tags:
- taxonomy
date: '2026-11-13'
summary: >-
  One topic word joins the closed vocabulary.
  `philosophy-of-technology` takes what technology is and what it does to
  those who live with it: the autonomy of technique, lock-in and practical
  compulsion, automation and deskilling, technical codes and the politics
  of artifacts, design that steers or captures its users, critical theory
  of technology and convivial tools. It enters because the filing of the
  exchange "Analyze technological civilization trap" (pull request #489)
  registered 27 works on these subjects under the nearest words, and the
  owner asked for the word. First applied beside the existing tags of 18
  held works whose subject it is; the 27 take it once both pull requests
  are merged. Rejected: the nearest words (`society-and-governance`,
  `social-science`, `ethics`), and a broader `science-and-technology-studies`.
  The wording is the assistant's (Claude, in this session); adopting it is
  the owner's call.
---
<!-- inactive-ok-file: ADR-097 — Proposed; the precedent this follows -->
<!-- inactive-ok-file: LIT-2225 LIT-1618 LIT-2373 — Unfetched; tagged by subject, unread -->
<!-- inactive-ok-file: LIT-753 LIT-197 LIT-1328 — Unavailable; tagged by subject, unread -->

# ADR-tmppn3v1: philosophy-of-technology joins the topics

## Context

The filing of the exchange "Analyze technological civilization trap"
(2026-11-13, https://chatgpt.com/share/6af6b47c-8b0c-83ea-ae04-3e3eb2649597;
pull request #489) registered 27 works A cited, unread and Deferred: Ellul,
Illich, Mumford, Marcuse, Postman, Winner, Feenberg, Hui, Han, Rosa,
Crawford, Zuboff and others. Most of them are about one subject: what
technology is, and what it does to the people who live with it. The
closed `topics` vocabulary has no word for that subject, so the filer
tagged the works with the nearest words, chiefly `society-and-governance`,
`social-science` and `ethics`, and reported the gap.

The vocabulary's alert says a work that wants a word the list lacks gets
it "with a label, a blurb and a decision", and CLAUDE.md that it is
"never replaced by the nearest wrong one". Each of the nearest words is
wrong in its own way:

- `society-and-governance` is law, politics, policy and institutions. It
  takes the regulation of a technology, not the claim that a technology
  reorganizes the life around it.
- `social-science` is empirical and theoretical work on people and
  societies. It takes a measured effect of a product, not Ellul's
  autonomy of technique or Feenberg's technical code.
- `ethics` is what is owed, permitted or good, and its blurb already
  takes the applied ethics of technology. It does not take the
  descriptive and critical question of what a technology does, which
  comes before any verdict on it.

The owner asked for the word ("add the phil tech topic"). ADR-062
records the owner's word that the vocabulary may be expanded where
merited, and ADR-097 is the latest decision of this form.

The record already held works of this kind without a word: Arthur on
increasing returns and the lock-in of technologies (LIT-1314, the
source of THEORY-863), Bainbridge's "Ironies of automation" (LIT-2225)
and the readings of it on AI and deskilling (LIT-2222, LIT-2224),
Susser, Roessler and Nissenbaum on technology and manipulation
(LIT-1002), and Doctorow on platform lock-in (LIT-731).

## Decision

Add one topic, **`philosophy-of-technology` (Philosophy of technology)**:
what technology is and what it does to those who live with it. It
covers:

- the autonomy of technique, technological determinism and its rivals,
  and the social shaping of technology;
- lock-in, path dependence of technologies and practical compulsion, where
  a technology becomes hard to decline for those who did not choose it;
- automation and what it leaves its operators: deskilling, the
  monitoring trap, skill decay under assistance;
- technical codes and the politics of artifacts: social choices and
  interests built into a design;
- design that steers, manipulates or captures its users;
- what a new technology is, as a kind (a cultural and social technology,
  agency without intelligence);
- critical theory of technology, conviviality and convivial tools.

It joins the `philosophy` group, beside `philosophy-of-science`. Its
boundary:

- The regulation and governance of a platform or technology stays with
  `society-and-governance`, a measured effect of one product with
  `social-science`, and a verdict on what is owed with `ethics`. A work
  takes this word as well when it argues about technology as such.
- How software is built, tested and changed is `software-engineering`.
- Instruction for machine-learning practice belongs to the anthology
  (ADR-048).

How it is applied:

- **Beside the existing tags** of 18 held works on the default branch
  whose subject it is. Primary topics are unchanged, and the word goes
  after the topics and before the `anthology-candidate` flag
  (ADR-005). Nothing is removed. Each work takes a version bump with a
  history note citing this decision.
  - Lock-in: LIT-1314 (Arthur, competing technologies and lock-in);
    LIT-731, LIT-033 and LIT-753 (Doctorow, platform decay sustained
    by lock-in and blocked interoperability).
  - Automation and deskilling: LIT-2225 (Bainbridge); LIT-2222 (Ahn,
    Bainbridge applied to AI in medical education); LIT-2224
    (Macnamara et al., skill decay under AI assistance).
  - Technology and autonomy, design that steers its users: LIT-1002
    (Susser, Roessler and Nissenbaum); LIT-1465 (Flayelle et al., design
    features that promote addictive use); LIT-2425 (Brown, recommender
    systems and authenticity); LIT-2373 (Dorsch et al., engagement
    algorithms and epistemic agency); LIT-197 (Sharman, AI and free
    will).
  - Technical codes: LIT-1297 (Perzanowski and Schultz, licences and DRM
    that remake ownership); LIT-1328 (Lan, verification interfaces that
    shift the cost of legibility onto users); LIT-1618 (Nissenbaum,
    barriers to accountability built into computerized systems).
  - What a technology is: LIT-848 (Farrell, Gopnik, Shalizi and Evans,
    large models as cultural and social technologies); LIT-896 and
    LIT-897 (Floridi, AI as agency without intelligence).
- **Not** to works whose subject is the governance or measurement of a
  platform rather than technology as such: the media and recommender
  works filed on 2026-11-11 and 12 (for example LIT-1331, LIT-2362,
  LIT-2361, LIT-1342, LIT-2386), algorithmic monoculture
  (LIT-1326), oversight of algorithmic nudging (LIT-179), and the
  safety-science works (LIT-743, LIT-2477). Nor to Pierson's increasing
  returns in politics (LIT-1372), technology adoption under trade
  protection (LIT-1489), cognitive offloading as a cognitive strategy
  (LIT-1059), or Jasanoff's "technologies of humility" (LIT-1594),
  where "technology" names habits of thought in governing science. Nor to
  the software-engineering works, which are about building software, not
  what it does to its users.
- **The 27 works of pull request #489** are not on the default branch.
  They take the word once both pull requests are merged, beside the tags
  they were filed with, and as primary where technology is the work's
  whole subject (Ellul, Winner, Feenberg, Illich's *Tools for
  Conviviality*). That re-tag is the decision's second application.
- **Readings** (THEORY) drawn from the tagged works keep their tags. A
  reading takes the word when it is next revised.

## Alternatives considered

- **The nearest words.** `society-and-governance` for Winner and
  `social-science` for Ellul are each defensible in a phrase and wrong as a
  statement of what the work is about, which is the case the vocabulary's
  rule forbids. They also scatter one inquiry across three words, so the
  topic page cannot show it.
- **A broader `science-and-technology-studies`.** It would take the
  sociology of science, which `philosophy-of-science` and `social-science`
  already hold, and it names a discipline rather than the question. The
  owner asked for the philosophy of technology.
- **Fold it into `ethics`.** Ethics' blurb already takes the applied
  ethics of technology. But Ellul, Mumford and Winner describe what
  technology does before anyone judges it, and a reader looking for that
  would not look under ethics.
- **Leave the vocabulary as it is.** The 27 works stay under words that do
  not describe them, and the record has no page for an inquiry it has
  begun to collect.

## Consequences

- `luria.yaml` gains the term, with its blurb, after
  `philosophy-of-science`, and the `philosophy` group lists it.
  docs/record.md and the topic pages are regenerated by CI, not edited.
- Future works on technology as such file here. The blurb says where its
  governance, its measured effects and its engineering go.
- Proposed until the owner adopts it, as with every topic decision so far.
