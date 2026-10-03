---
status: Deferred
status_note: 'registered 2026-10-03 from metadata and from what the papers that cite it say, not read. Project Euclid hosts the Annals of Mathematical Statistics free to read, and OpenAlex marks this article diamond open access, but every request for the article page (by DOI, by the euclid.aoms handle and by the full-text URL) returned an Incapsula bot challenge, which I did not try to get past. OpenAlex lists no repository copy. A human reader with a browser can open the publisher''s free copy, and a reading from it would move this to Active.'
title: 'The Weighted Likelihood Ratio, Linear Hypotheses on Normal Location Parameters'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Registered unread. Crossref confirms the title, the single author
    (James M. Dickey), The Annals of Mathematical Statistics 42(1):204–223,
    February 1971, and the DOI; `published:` is the first of February
    1971 because Crossref gives only the month. Not held in the Anthology
    of the SOTA: a grep of its record for "Dickey", "Savage" and the DOI
    found nothing.
tags:
- model-comparison
- probabilistic-modeling
date: '2026-10-03'
published: '1971-02-01'
doi: '10.1214/aoms/1177693507'
first_author: 'Dickey'
keywords:
- 'weighted likelihood ratio'
- 'Bayes factor'
- 'linear hypotheses'
- 'normal location parameters'
- 'Savage–Dickey density ratio'
implementations: []
summary: >-
  Dickey (1971), Annals of Mathematical Statistics 42(1):204–223. Unread.
  The paper the Savage–Dickey density ratio is named after: per the papers
  in the record that cite it, it treats the Bayes factor (the "weighted
  likelihood ratio") for linear hypotheses on normal location parameters,
  and states the result that the Bayes factor for a nested point
  hypothesis is the posterior-to-prior density ratio at the hypothesised
  value. The record reads that result through Wagenmakers et al.
  ([LIT-tmp2suxj](LIT-tmp2suxj.md)).
extended_by:
- LIT-tmp2suxj
- LIT-tmpuhjzx
---

# LIT-tmp6vz5e: The Weighted Likelihood Ratio, Linear Hypotheses on Normal Location Parameters

James M. Dickey (1971), *The Annals of Mathematical Statistics* 42(1):204–223 — DOI-10.1214/aoms/1177693507

## Key takeaways

*Registered from metadata and from what citing papers in the record say,
not a reading.*

- **What the record's readings say it is.** Wagenmakers et al.
  ([LIT-tmp2suxj](LIT-tmp2suxj.md)) say the density-ratio result was first published by Dickey
  and Lientz (1970), who attributed it to Savage, and cite this paper as one
  of the sources under which it "is now generally known as the
  Savage–Dickey density ratio". Friston & Penny ([LIT-tmpuhjzx](LIT-tmpuhjzx.md)) cite it,
  together with Verdinelli & Wasserman (1995), as the source of the ratio
  that their reduced-evidence identity recovers when the reduced prior is a
  point mass (their Eq. 6).
- **What the title says.** The "weighted likelihood ratio" is the ratio of
  likelihoods each averaged over its prior, that is, a Bayes factor, here
  for linear hypotheses about the means of normal distributions.

## Standing in the record

Filed on 2026-10-03 at the owner's request, in the model-comparison batch.
No anthology topic holds it, and it carries no instruction for
machine-learning practice.

`Deferred` because it was not read, not on merit. A lawful free copy
exists at the publisher, behind a bot challenge. The record does not lose
the result while this stays unread: Wagenmakers et al. ([LIT-tmp2suxj](LIT-tmp2suxj.md)) derive
the ratio and its continuity condition in full (their Appendix A), and the
record reads it there. What only this paper can settle is the original
setting and conditions: whether Dickey states the result for general
nested models or only for normal linear hypotheses, and how he states the
prior condition that Wagenmakers et al. write as continuity of the
nuisance prior. That matters for the claim in Friston & Penny and in
Bayesian model reduction ([LIT-tmpbgf7s](LIT-tmpbgf7s.md)) that they generalise "the
Savage–Dickey ratio".

**Priority for a reading: medium.** The result is held; the original
statement is not.

Access when registered:

- Crossref record (title, author, volume, issue, pages, February 1971).
- OpenAlex: `is_oa` true, `oa_status` diamond, `any_repository_has_fulltext`
  false; locations only the DOI and the Project Euclid handle.
- Unpaywall: open access, publisher host, no PDF URL.
- Project Euclid: the article page and the canonical handle
  (projecteuclid.org/euclid.aoms/1177693507) both returned an Incapsula
  "Request unsuccessful" challenge page.
