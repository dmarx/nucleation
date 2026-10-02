---
status: Active
status_note: 'read in full 2026-10-02 ([NOTE-tmpt626p](../notes.d/NOTE-tmpt626p.md)); worth reading as the first published architecture of a mind-like process built from many quasi-independent "demons", each doing one narrow job, with no part holding the whole''s competence. That is the decomposition template that Minsky''s agents inherit. Cite it as an engineering proposal with a preliminary result reported only in discussion, not as a theory of mind. Its one remark on consciousness is McCarthy''s, in the discussion, and it is an aside.'
title: 'Pandemonium: A Paradigm for Learning'
version: 1
history:
- version: 1
  date: '2026-10-02'
  note: >-
    Read in full (a scan of the HMSO printing, Session 3 Paper 6 of
    Mechanisation of Thought Processes, Vol. I, pp. 511–531, hosted at
    gwern.net/doc/ai/nn/1959-selfridge.pdf; text extracted with PyMuPDF
    and checked against the page images where the OCR was garbled). It
    covers the session title page (p. 511), the biographical note (p. 512),
    the paper (pp. 513–526) and the recorded discussion with Selfridge's
    reply (pp. 527–531). HMSO is Crown copyright, which for a 1959
    publication expired in 2009. Not held in the Anthology of the SOTA: a
    grep of its literature.d for "Selfridge" and "Pandemonium" found
    nothing. `published:` is the year only (the volume carries no date
    beyond 1959; the symposium was 24–27 November 1958).
tags:
- cognition
- complex-systems
- representation-learning
- anthology-candidate
date: '2026-10-02'
published: '1959-01-01'
url: 'https://archive.org/details/mechanisationoft0001anon'
first_author: 'Selfridge'
keywords:
- 'pattern recognition'
- 'learning'
- 'parallel processing'
- 'demons'
- 'hill-climbing'
- 'feature weighting'
- 'subdemon selection'
- 'Morse code'
implementations: []
summary: >-
  Selfridge (1959), Mechanisation of Thought Processes Vol. I (HMSO),
  pp. 513–526 plus discussion to p. 531. Pattern recognition by a
  "pandemonium": data demons hold the input, computational subdemons
  compute features, each cognitive demon "shrieks" a weighted sum of them,
  and a decision demon picks the loudest. The system learns by
  hill-climbing on the weights and by "natural selection" on the subdemons,
  culling those of low worth and breeding new ones by mutation and by
  "conjugation" of pairs. It is applied to telling dots from dashes in
  hand-keyed Morse. In the discussion McCarthy proposes reading the demons'
  private computation as unconscious and their public shouting as
  conscious thought.
---
<!-- inactive-ok-file: LIT-tmpqepho — Deferred, no lawful full text; named as the decomposition side of the bridge, not leaned on -->

# LIT-tmpol46q: Pandemonium: A Paradigm for Learning

O. G. Selfridge (1959), "Pandemonium: A Paradigm for Learning", in
*Mechanisation of Thought Processes: Proceedings of a Symposium held at the
National Physical Laboratory on 24th, 25th, 26th and 27th November 1958*,
Vol. I, London: Her Majesty's Stationery Office, Session 3, Paper 6,
pp. 511–531. Reprinted in J. A. Anderson and E. Rosenfeld (eds.),
*Neurocomputing: Foundations of Research*, MIT Press, 1988, pp. 117–122
(DOI 10.7551/mitpress/4943.003.0011).

**On the citation.** The brief's details are right: the title, the
proceedings' title, the NPL symposium and HMSO. Two details need adding:

- **Pages.** Citations disagree: 511–526 (secondary listings found by
  search), 513–526 (the Crossref title of the 1988 reprint) and
  511–529 (ML Anthology). The scan settles it. P. 511 is the session title
  page and p. 512 the biographical note. The paper is pp. 513–526, and the
  discussion with Selfridge's reply is pp. 527–531. The whole item is
  pp. 511–531.
- **Date.** The symposium was November 1958. The volume is 1959, and the
  paper was written in July 1958 ("At the present (July)", p. 526). The
  Internet Archive also holds a copy dated 1961, which looks like a
  reprint; the volume read here is the one dated 1959.

## Key takeaways

- The **architecture** (pp. 514–516). An idealised pandemonium has one demon
  per pattern, each computing its similarity to the image, and a decision
  demon picking the largest. The amended pandemonium factors the
  computations the cognitive demons share into a "host of subdemons". That
  gives four levels: data demons, computational subdemons, cognitive demons
  and a decision demon.
- **Learning**. Three kinds of adaptive change:
  - feature weighting by hill-climbing (pp. 517–521);
  - subdemon selection (pp. 521–522): low-worth subdemons are eliminated,
    and new ones come from "mutated fission" or "conjugation" by one of the
    ten non-trivial binary functions of two subdemons;
  - control adaptation (p. 523): the controlling operations are themselves
    demons, some of which "will be in a position to change themselves".
- **Evolution and self-monitoring** (p. 523). "A natural selection on the
  processing demons", which could extend to a crowd of pandemoniums.
  Unsupervised operation scores itself by how unequivocally one cognitive
  demon "far outshines the rest".
- **Why parallel modules** (p. 513): parallel handling is often more
  natural, and "it is easier to modify an assembly of quasi-independent
  modules than a machine all of whose parts interact immediately and in a
  complex way".

## Standing in the record

Filed on 2026-10-02 for the bridge between Minsky's society of mind
([LIT-tmpqepho](LIT-tmpqepho.md)) and Schwitzgebel's conscious United States ([LIT-159](LIT-159.md), [NOTE-131](../notes.d/NOTE-131.md)).
It sits on the **decomposition side**, at its root. A competence the whole
has (recognising a pattern) is produced by demons none of which has it. The
anthropomorphism is declared to be vocabulary: "We are not going to
apologize for a frequent use of anthropomorphic or biamorphic terminology.
They seem to be useful words" (p. 513). The acknowledgements name M. Minsky
first (p. 526).

The paper's account of where agents come from is the one Minsky's
neurodevelopmental memo ([LIT-tmp4jv7c](LIT-tmp4jv7c.md)) relies on. In the memo new agents arise
"by splitting off from old ones, with only small changes"; here new
subdemons come by "mutated fission" of the survivors. Minsky also proposes
perceptron-like detectors "on tap, not on top", and Selfridge's cognitive
demons are weighted sums of feature outputs. The pairing is mine.

On [NOTE-131](../notes.d/NOTE-131.md)'s claims it is **neutral on C3, C4 and C5**. Its demons are
not minds, so it does not raise nesting. Its one bearing on consciousness
is McCarthy's remark in the discussion (p. 527): "what is going on within
the demons can be regarded as the unconscious part of thought, and what the
demons are publicly shouting for each other to hear, as the conscious part
of thought".
That is an aside, not an argument, and Selfridge does not take it up. It
puts consciousness in the *broadcast between parts*, not in any part. That
is the shape of the global-workspace or "fame" models that Schwitzgebel
(manuscript p. 29) calls subsystem-driven, in his reply to Chalmers's
relational-capacity objection. A whole whose shouting is its consciousness
is a whole whose experience arises from relations among parts. Read that
way it is evidence for the relational reading Chalmers's principle wants,
not against it. That reading is mine, and it is the remark's only purchase
on the seam.

The scale-free-architecture works filed alongside this one, Brooks's
layered behaviours and Levin's nested computational selves, continue this
line of decomposition without a central executive. The pandemonium still
has a decision demon on top. Whether those architectures give that piece
up is for their own readings to say.

**Boundary.** Its subject is a learning procedure for pattern recognition:
feature weights fitted by hill-climbing, and features evolved by mutation
and recombination. That is machine-learning content, and an anthology topic
could hold it. It is tagged `anthology-candidate` for that reason. It is
filed here under [ADR-013](../decisions.d/ADR-013.md) for nucleation's own question, what the demon
architecture contributes to the decomposition account of mind. If the
anthology takes it, the two entries should name each other.
