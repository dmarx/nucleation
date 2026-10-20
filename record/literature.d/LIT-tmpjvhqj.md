---
status: Active
status_note: 'read 2026-10-20 ([NOTE-tmpwosj3](../notes.d/NOTE-tmpwosj3.md)) in full, in the pre-publication version of 9 May 2025, the only version copyright.gov offers on that date; worth reading as the official US statement of where training touches copyright (collection, curation, training copies, and model weights only where they have memorized a work), as an application of the Warhol v. Goldsmith use-specific test of transformative purpose to generative training (a spectrum, from research and closed non-substitutive deployments to fine-tuning that reproduces a series''s characters), and for its new market-dilution theory of harm under the fourth factor. Read it knowing that it is an agency''s analysis, not a holding; that it predates the 2025 district-court rulings on training; that its account of the facts rests mostly on the parties'' own comments; that the dilution theory is offered as "uncharted territory" with no data; and that a final version was promised but had not appeared by 2026-10-20.'
title: 'Copyright and Artificial Intelligence, Part 3: Generative AI Training (Pre-Publication Version)'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Filed at the owner's request and read in full the same day. Source copy:
    the pre-publication version as published by the U.S. Copyright Office at
    copyright.gov/ai (the PDF named in `url:`, 113 PDF pp., report pp. ii–iii
    and 1–108 with 588 footnotes; the PDF metadata gives a creation date of 9
    May 2025). It is a work of the United States government, not subject to
    copyright in the US (17 U.S.C. § 105). Text extracted with pdftotext
    -layout. The version read is the pre-publication version released on 9
    May 2025. The Office's AI page, fetched 2026-10-20, still says only that a
    final version of Part 3 will be published in the future, with no
    substantive change expected in the analysis or conclusions, and links
    no final version, so none was read. The PDF's cover says the same, with
    "in the near future". The report has no appendices. Page
    references are the report's own page numbers (PDF page = report page +
    3). Crossref has no record for it (a bibliographic query returned only
    unrelated book chapters on AI and copyright); `published:` is the
    release date stated on the Office's page. Not held in the Anthology of
    the SOTA: a grep of its record/ (clone of 2026-10-20, commit d1573d2)
    for "copyright" and "fair use" found nothing. It is filed here because
    the anthology holds nothing on copyright, and for this record's own
    question: whether training is copying in Lessig's sense of the copy
    trigger (NOTE-tmptp3k0), and how the report treats transformative
    purpose and market harm under the Warhol v. Goldsmith standard. It is
    an anthology candidate all the same: the anthology's
    deployment-and-society topic could hold it, so it carries the
    `anthology-candidate` flag last (ADR-005).
tags:
- society-and-governance
- anthology-candidate
date: '2026-10-20'
published: '2025-05-09'
url: 'https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-3-Generative-AI-Training-Report-Pre-Publication-Version.pdf'
first_author: 'U.S. Copyright Office'
keywords:
- 'copyright'
- 'fair use'
- 'generative AI training'
- 'reproduction right'
- 'memorization'
- 'transformative use'
- 'market dilution'
- 'licensing'
- 'extended collective licensing'
implementations: []
summary: >-
  U.S. Copyright Office (2025), pre-publication version. Collecting, curating
  and training on copyrighted works implicate the reproduction right; model
  weights do so only where they have memorized substantially similar
  expression. Whether the copying is excused is a fair-use question, use by
  use. Training a foundation model will often be transformative, but less so
  the more its outputs serve the originals' purpose; the non-expressive and
  human-learning arguments are rejected; market dilution is cognizable harm.
  The Office recommends letting licensing markets develop, with extended
  collective licensing if they fail.
---
<!-- inactive-ok-file: CLAIM-002 — Proposed; open claims and accounts this reading bears on, cited as open, nothing here rests on their being settled -->

# LIT-tmpjvhqj: Copyright and Artificial Intelligence, Part 3: Generative AI Training (Pre-Publication Version)

U.S. Copyright Office (2025). *Copyright and Artificial Intelligence, Part 3:
Generative AI Training.* Pre-publication version, released 9 May 2025. A
Report of the Register of Copyrights. Washington, DC: U.S. Copyright Office.

## Key takeaways

*From the reading, [NOTE-tmpwosj3](../notes.d/NOTE-tmpwosj3.md).*

- **Training is copying, at the input.** Downloading, converting, filtering
  and compiling a dataset "clearly implicate" the reproduction right, and so
  does copying the dataset to storage for training (pp. 26–27). Whether the
  batch copies made during training are fixed is left to the facts, and the
  Office says it matters little: "Such temporary copying may, however, be of
  little significance given the other acts of reproduction in AI training."
  (p. 28 n. 160).
- **The weights are a copy only of what they can give back.** "Whether a
  model’s weights implicate the reproduction or derivative work rights turns
  on whether the model has retained or memorized substantial protectable
  expression from the work(s) at issue." (p. 30). The test is fixation plus
  recoverability with a machine, as for a JPEG (pp. 28–29).
- **Warhol makes the use the unit.** Each act (curation, pre-training,
  fine-tuning, RAG) is weighed separately but judged by its ultimate purpose
  (pp. 36–37, 45). Training a foundation model "will often be
  transformative" (p. 45). It is least so when a model is trained to emit
  work like what it was trained on, and "at best, modestly transformative"
  when its outputs share the originals' audience (p. 46).
- **Two arguments rejected.** Training is not non-expressive, because models
  learn selection and arrangement, "the essence of linguistic expression"
  (p. 47). It is not like human learning, because "Copyright law should not
  afford greater latitude for copying simply because it is done by a
  computer." (p. 48).
- **Market dilution.** Outputs that copy no particular work can still harm
  the market for works of the same kind, including by imitating a style:
  "If thousands of AI-generated romance novels are put on the market, fewer
  of the human-authored romance novels that the AI was trained on are
  likely to be sold." (p. 65). The Office calls this "uncharted territory".
- **Licensing, not legislation.** Voluntary licensing is growing. The Office
  recommends no government intervention for now, an antitrust clarification
  for collective licensing, and extended collective licensing where markets
  are shown to fail. It rejects an opt-out default (pp. 103–106).

## Standing in the record

Filed on 2026-10-20 at the owner's request, as the second work on copyright
after Lessig's *Remix* ([LIT-tmpreyek](LIT-tmpreyek.md)). It is read against Lessig's copy
trigger ([NOTE-tmptp3k0](../notes.d/NOTE-tmptp3k0.md)): the report confirms that training sets off the
trigger at every input step, and then puts the whole question into fair use,
as Lessig said the law does for every digital use. It applies the Supreme
Court's Warhol v. Goldsmith test, which is being filed in this record at the
same time. Its bearing on [CLAIM-002](../claims.d/CLAIM-002.md), [CLAIM-210](../claims.d/CLAIM-210.md) and the translation line is
set out in the reading. It is an anthology candidate (the anthology's
deployment-and-society topic could hold it) and is held here because the
anthology holds nothing on copyright.
