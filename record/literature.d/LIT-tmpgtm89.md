---
status: Deferred
status_note: >-
  filed 2026-10-18, not read. Registered from the exchange of 2026-10-17, "Synthesis opportunities analysis" (workbench entries of 2026-10-18). No NOTE is filed.
title: 'Practical Byzantine Fault Tolerance'
version: 1
history:
- version: 1
  date: '2026-10-18'
  note: >-
    Filed, not read. Citation checked on 2026-10-18 against the USENIX page (which gives February 1999) and the paper's own header ("February 22-25, 1999, New Orleans"); `published:` is the symposium's opening day. The OSDI paper has no DOI, so the source is the URL. The journal version is a different, longer paper, "Practical byzantine fault tolerance and proactive recovery", *ACM TOCS* 20(4), 2002, doi:10.1145/571637.571640 (Crossref checked). Not held in the Anthology of the SOTA: a grep of its record/ (clone of 2026-10-18, commit d1573d2) for the authors and the title found nothing.
tags:
- network-science
- operations-research
date: '2026-10-18'
published: '1999-02-22'
url: 'https://www.usenix.org/conference/osdi-99/practical-byzantine-fault-tolerance'
first_author: 'Castro'
keywords:
- 'Byzantine fault tolerance'
- 'state machine replication'
- 'asynchronous systems'
- 'NFS'
implementations: []
summary: >-
  Castro & Liskov (1999). A replication algorithm that tolerates Byzantine faults in asynchronous networks such as the Internet and is fast enough to use: a Byzantine-fault-tolerant NFS built on it was only 3% slower than unreplicated NFS.
---

# LIT-tmpgtm89: Practical Byzantine Fault Tolerance

Castro, M. & Liskov, B. (1999). Practical Byzantine Fault Tolerance. In *Proceedings of the Third Symposium on Operating Systems Design and Implementation (OSDI '99)*, New Orleans. USENIX Association. Journal version: Castro & Liskov (2002), *ACM Transactions on Computer Systems* 20(4): 398–461, doi:10.1145/571637.571640.

Not read. The summary is drawn from the abstract or from what the work is
standardly cited for. A reading should check it first.

## Why this is here

A41 of the exchange called it "a central reference" for the owner's U41 question of governance under compromised constituents, and noted its limit: "A Byzantine protocol generally takes the specification of correct behavior as given." Bears on [CLAIM-tmpp9ox0](../claims.d/CLAIM-tmpp9ox0.md) and [CASE-tmp4nzjz](../cases.d/CASE-tmp4nzjz.md). The anthology holds Byzantine-robust learning ([ANTH-LIT-257](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-257.md), [ANTH-LIT-344](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-344.md)), not this distributed-systems paper.
