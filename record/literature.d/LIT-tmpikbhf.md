---
status: Deferred
status_note: >-
  filed 2026-10-27, not read. Registered from U15–U23 of the owner's exchange of 2026-10-27, "Field Existence Question". No NOTE is filed.
title: 'Counterexample-Guided Abstraction Refinement'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed, not read. Citation checked against Crossref on 2026-10-27:
    Edmund Clarke, Orna Grumberg, Somesh Jha, Yuan Lu and Helmut Veith,
    Computer Aided Verification (CAV 2000), Lecture Notes in Computer
    Science 1855, pp. 154–169, Springer, 2000, with the year only, so
    `published:` carries a placeholder, 1 January 2000. The journal
    version is J. ACM 50(5), 2003.
tags:
- logic
- mathematics
date: '2026-10-27'
published: '2000-01-01'
doi: '10.1007/10722167_15'
first_author: 'Clarke'
keywords:
- 'model checking'
- 'abstraction refinement'
- 'spurious counterexample'
- 'verification'
implementations: []
summary: >-
  Clarke et al. (2000). Model checking runs on an abstraction that
  merges concrete states; when it yields a counterexample, the
  counterexample is checked against the concrete system, and if it is
  spurious the abstraction is refined to separate the states whose
  merging produced it, and checking runs again.
---

# LIT-tmpikbhf: Counterexample-Guided Abstraction Refinement

Clarke, E., Grumberg, O., Jha, S., Lu, Y., & Veith, H. (2000). Counterexample-guided abstraction refinement. In *Computer Aided Verification* (LNCS 1855, pp. 154–169). Springer. doi:10.1007/10722167_15.

Not read. The summary is drawn from what the work is standardly cited
for and from the exchange's description of it. A reading should check it
first.

## Why this is here

A16 §6 called it "the strongest formal connection" for inquiry as
specification, and read luria's DP-016 (an awkward relation discloses a
missing distinction; [CLAIM-419](../claims.d/CLAIM-419.md) in this record) as "the same epistemic
pattern": failure under a specification, diagnosis of the missing
distinction, refinement. A16 added the limit that CEGAR refines an
abstraction for a fixed property and cannot find the property misguided.
It bears on [CLAIM-tmpalzo4](../claims.d/CLAIM-tmpalzo4.md) and [CLAIM-tmpl228b](../claims.d/CLAIM-tmpl228b.md).
