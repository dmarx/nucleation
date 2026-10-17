---
status: Active
status_note: 'read in full 2026-10-17 (NOTE-tmpik4nc); worth reading as the short source of directed information, I(X^N→Y^N) = Σ I(X^n; Y_n | Y^{n−1}), and of the point that the usual definition of a memoryless channel silently forbids feedback because it confuses statistical with causal dependence. Read it knowing that "causal" here is a factorization condition on a system of sources and channels, not an interventional notion; that directed information conditions on the current input as well as the past, so it is not transfer entropy; and that the copy read is the author''s preprint, not the proceedings version. Filed as THEORY-tmppkvwa.'
title: 'Causality, Feedback and Directed Information'
version: 1
history:
- version: 1
  date: '2026-10-17'
  note: >-
    Filed at the owner's request as the information-theoretic counterpart
    of Granger causality and transfer entropy, which the record held no
    source for. Not held in the Anthology of the SOTA: a grep of its
    record/ (clone of 2026-10-12, d1573d2) for "Massey" and "directed
    information" found nothing. Read in full the same day (NOTE-tmpik4nc)
    from the preprint in the archive of Massey's own institute, ETH
    Zürich's Signal and Information Processing Laboratory
    (isiweb.ee.ethz.ch/papers/arch/mass-1990-1.pdf), a lawful author copy.
    The preprint says it is "to appear in Proc. 1990 Intl. Symp. on Info.
    Th. and its Applications, Waikiki, Hawaii, Nov. 27-30, 1990"; it
    carries no page numbers, and the proceedings version was not seen or
    compared. No DOI was found in Crossref. `published:` is the
    symposium's first day, the only full date the work carries.
tags:
- information-theory
- causality
date: '2026-10-17'
published: '1990-11-27'
url: 'https://isiweb.ee.ethz.ch/papers/arch/mass-1990-1.pdf'
first_author: 'Massey'
keywords:
- 'directed information'
- 'feedback'
- 'causality'
- 'discrete memoryless channel'
- 'channel capacity'
implementations: []
summary: >-
  Massey (1990), Proc. ISITA-90, Waikiki. The usual definition of a discrete memoryless channel, P(y^N|x^N) = Π P(y_n|x_n), holds only when the channel is used without feedback; the right definition is P(y_n|x^n y^{n−1}) = P(y_n|x_n). Defines directed information I(X^N→Y^N) = Σ_n I(X^n; Y_n | Y^{n−1}), after Marko (1973), and proves I(X^N→Y^N) ≤ I(X^N;Y^N) with equality without feedback, that it bounds what the output tells about the source in a causal system, and so that feedback does not increase DMC capacity. "Statistical dependence, unlike causality, has no inherent directivity."
---

# LIT-tmpcmyem: Causality, Feedback and Directed Information

James L. Massey (1990), "Causality, Feedback and Directed Information", *Proceedings of the 1990 International Symposium on Information Theory and its Applications (ISITA-90)*, Waikiki, Hawaii — <https://isiweb.ee.ethz.ch/papers/arch/mass-1990-1.pdf>

## Key takeaways

*From the reading, [NOTE-tmpik4nc](../notes.d/NOTE-tmpik4nc.md).*

- **The DMC without feedback (Eqs. 1–5).** A discrete channel is memoryless
  if P(y_n|x^n y^{n−1}) = P(y_n|x_n). It is used without feedback if
  P(x_n|x^{n−1} y^{n−1}) = P(x_n|x^{n−1}). Only both together give the
  textbook P(y^N|x^N) = Π P(y_n|x_n), which therefore excludes feedback.
- **Directed information (Eq. 7).** I(X^N→Y^N) = Σ_n I(X^n; Y_n | Y^{n−1}),
  a slight modification of Marko's 1973 definition. In general
  I(X^N→Y^N) ≠ I(Y^N→X^N).
- **Theorem 1.** I(X^N→Y^N) ≤ I(X^N;Y^N), with equality if the channel is
  used without feedback.
- **Theorem 3.** In a causal system, where a channel sees a source only
  through its own inputs and outputs (Eq. 8), I(U^K;Y^N) ≤ I(X^N→Y^N).
  With Theorem 2 this gives the capacity of a DMC unchanged by feedback.
- **The lesson.** "Probabilistic dependence is quite distinct from causal
  dependence." Mutual information is symmetric; directed information is
  not.

## Standing in the record

Filed on 2026-10-17 and read the same day. Filed as [THEORY-tmppkvwa](../theory.d/THEORY-tmppkvwa.md).
Directed information is the full-history, conditioned-on-the-present
relative of transfer entropy ([TERM-tmpj9z04](../terms.d/TERM-tmpj9z04.md)). By the chain rule it splits
into a sum of full-history transfer entropies and a sum of instantaneous
terms, which [NOTE-tmpik4nc](../notes.d/NOTE-tmpik4nc.md) checks; that decomposition is the record's,
not Massey's. `causality` is for its subject. Massey's "causal" is a
factorization condition, not intervention.
