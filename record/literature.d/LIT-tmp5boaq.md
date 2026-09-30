---
status: Active
status_note: 'read in part 2026-09-30 ([NOTE-tmpiyyzi](../notes.d/NOTE-tmpiyyzi.md)); worth reading as the founding engineering statement of signal detection theory: the likelihood-ratio receiver, the ROC and its slope property, and the equal-variance Gaussian case with an explicit d = 2E/N₀. Read the 1953 report knowing that the scan is poor and that the 1954 IRE paper (with W. C. Fox) is the citable journal form, which was not read here.'
title: 'The Theory of Signal Detectability. Part I: The General Theory; Part II: Applications with Gaussian Noise'
version: 2
history:
- version: 2
  date: '2026-09-30'
  note: >-
    Read in part (The 1953 technical report, not the 1954 journal paper. The
    work is registered as the report: University of Michigan Engineering
    Research Institute, Electronic Defense Group, Technical Report No. 13,
    in two separately issued parts. Part I, "The General Theory", is dated
    June 1953 (DTIC AD0016786, 60 PDF pp.). Part II, "Applications with
    Gaussian Noise", is dated July 1953 (DTIC AD0016787, 99 PDF pp.). Both
    are Signal Corps contract DA-36-039 sc-15358 reports approved for
    release. I read them as the DTIC scans mirrored on the Internet
    Archive's US-government-documents collection (identifiers
    DTIC_AD0016786, DTIC_AD0016787). DTIC's own server and UMich Deep Blue
    (hdl 2027.42/7068) both refused this session. DTIC stamps the scans
    "best quality available … a significant number of pages which do not
    reproduce legibly". The text layer is poor OCR, so I read it alongside
    page images of every page carrying a theorem statement, key equation,
    figure or conclusion. **Part I: all of it**, printed pp. 1–50 plus the
    errata sheet and the symbol list: §1 (pp. 1–11), §2 Theorems 1–8 with
    proofs (pp. 12–30), Appendix A (pp. 31–32), Appendix B Lemmas 1–4 (pp.
    33–41), Appendix C Theorems C1–C4 (pp. 42–47) and the bibliography.
    **Part II, read closely:** §3 (pp. 1–8), §4.1–4.2 (signal known exactly,
    pp. 9–13, including Fig. 4.1), §4.3 (pp. 17–21), §5 in full (pp. 55–71:
    5.1.1–5.1.6, 5.2 receiver design, and the conclusions). **Part II,
    skimmed** from the OCR plus figures: §4.4–4.9 (noise-like signal,
    broad-band video receiver, radar pulse train, approximate evaluation, M
    orthogonal signals), Appendices D (sampling theorem), E and F (RC-filter
    approximation), and the bibliography. The Part II derivations in
    §4.4–4.9 are partly illegible in this scan. Printed page numbers are
    cited; in Part I, printed page = PDF page − 8. `published:` is
    1953-06-01, the first day of Part I's issue month; the day is not
    printed. There is no anthology entry for this work (grep of
    /home/user/anthology-of-the-sota/record/literature.d for "detectab" and
    "Birdsall" found nothing), and no nucleation entry.); the first NOTE on
    it, since it was seeded from the abstract alone. Status set from the
    reading: Active.
tags:
- information-theory
- probabilistic-modeling
- mathematics
date: '2026-09-30'
published: '1953-06-01'
url: 'https://deepblue.lib.umich.edu/handle/2027.42/7068'
first_author: 'Peterson'
keywords:
- 'signal detection theory'
implementations: []
summary: >-
  Peterson & Birdsall (1953),
  <https://deepblue.lib.umich.edu/handle/2027.42/7068>. Peterson and
  Birdsall show that the criterion approach (maximise P_SN(A) − β·P_N(A),
  or maximise detection at fixed false-alarm k) and the Woodward–Davies
  a-posteriori approach are all solved by one receiver that computes the
  likelihood ratio ℓ(x) = f_SN(x)/f_N(x) and thresholds it (Part I,
  Theorems 1–7). They introduce the receiver operating characteristic,
  whose slope at each point is the threshold β (Theorem 8, Eq. 2.51). For
  a signal known exactly in white Gaussian noise, ln ℓ is normal with
  equal variance 2E/N₀ under both hypotheses and means 2E/N₀ apart, so the
  ROC is a one-parameter family indexed by the "detection index" d = (M_SN
  − M_N)²/σ² = 2E/N₀ (Part II, Eqs. 4.1–4.8, Fig. 4.1). The receiver is a
  correlator or matched filter (Eq. 5.3, 4.10).
---

# LIT-tmp5boaq: The Theory of Signal Detectability. Part I: The General Theory; Part II: Applications with Gaussian Noise

Peterson & Birdsall (1953), *University of Michigan Engineering Research Institute, Electronic Defense Group, Technical Report No. 13 (Project M970; Signal Corps contract DA-36-039 sc-15358), Part I June 1953 (DTIC AD0016786), Part II July 1953 (DTIC AD0016787); read from the DTIC scans mirrored at archive.org/details/DTIC_AD0016786 and archive.org/details/DTIC_AD0016787. Journal version, with W. C. Fox as third author and not read here: "The theory of signal detectability", Transactions of the IRE Professional Group on Information Theory 4(4):171–212, September 1954, doi:10.1109/TIT.1954.1057460* — <https://deepblue.lib.umich.edu/handle/2027.42/7068>

## Standing in the record

Filed on 2026-09-30 at the owner's request, as one of the sources registered to cover signal detection theory,
which the record lacked; its only detection-theory entry, Van Trees 1968 ([LIT-351](LIT-351.md)), is unreachable.
`published:` is the first appearance ([ADR-002](../decisions.d/ADR-002.md)).

It was filed `Deferred`, unread. [NOTE-tmpiyyzi](../notes.d/NOTE-tmpiyyzi.md) is the close reading of 2026-09-30, and it placed the work: **Active** — worth reading as the founding engineering statement of signal detection theory: the likelihood-ratio receiver, the ROC and its slope property, and the equal-variance Gaussian case with an explicit d = 2E/N₀. Read the 1953 report knowing that the scan is poor and that the 1954 IRE paper (with W. C. Fox) is the citable journal form, which was not read here.
