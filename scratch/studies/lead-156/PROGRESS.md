# LEAD-156 progress

- Lead: LEAD-156, "Search for human studies that separate the germline route of intergenerational trauma from the uterine, parenting and cultural routes, and for studies of descendants' distress against group identification".
- Branch: `claude/lead-156-germline-route`, cut from `origin/staging`.
- Task: search Europe PMC (REST) and PMC (E-utilities), no email, for paternal-line, adoption, and IVF/donor designs that separate the germline route; retry the three registered works (Yehuda & Lehrner 2018, Yehuda 2016, Pembrey 2006) by lawful routes; read the closest studies; file NOTE + THEORY per work read; set out what each design separates and leaves confounded; file the verdict as Proposed CLAIMs (with alternatives); dated notes on the lead and its targets; curation entry; changelog fragment.

## Step 1: already held?

- CLAIM-644 (Proposed, 2026-11-11) already holds "no human study the record has read separates the germline route, and none of the designs now in use can", grounded on Horsthemke, Costa et al. and Youssef et al. It names in `defeated_if` the designs this lead searches for. No design search and no reading of the three registered works is on record, so the lead is not already done. New filings must refine CLAIM-644, not duplicate it.

## Done

- Searched Europe PMC REST (2026-11-23, no email): human sperm/germline + trauma; IVF/donor designs; Rice/Thapar assisted-conception design; Syrian refugees, Finnish evacuees, Yehuda paternal/maternal PTSD. None of the candidates is held in `record/literature.d`.
- Retried registered works (2026-11-23):
  - LIT-1715 (PMC6127768): Europe PMC fullTextXML HTTP 500; E-utilities efetch db=pmc returns front matter with "The publisher of this article does not allow downloading of the full text in XML form." Stopped. Stays Unfetched.
  - LIT-1692 (PMID 26410355) and LIT-1764 (PMID 16391557): Europe PMC lists no PMC copy. The publisher copies were refused on 2026-10-29 (Cloudflare; Nature sign-in); not retried (same host). Stay Unfetched.
- Fetched full text:
  - Rice et al. 2010, PMC2954294 (E-utilities; EPMC REST gave 500) — IVF design, prenatal stress.
  - Mulligan et al. 2025, PMC11868390 (E-utilities; EPMC REST gave 500) — Syrian refugees, germline exposure.
  - Zhou & Ryan 2023, PMC10454883 (EPMC REST) — scoping review of intergenerational epigenetic transmission in humans.
  - Tuulari et al. 2025, PMC12092256 (EPMC REST) — childhood maltreatment and sperm epigenetics.
- Not reached: Thapar & Rice 2021 (PMC7919395): EPMC 500; E-utilities says publisher disallows XML. Santavirta et al. 2018 (PMC5833542): EPMC 500.

- Read: Rice et al. 2010 (full), Lewis et al. 2011 (abstract, intro, methods, results), Mulligan et al. 2025 (full body), Tuulari et al. 2025 (full body), Zhou & Ryan 2023 (full). Rice & Thapar 2010 birth-weight paper (PMC2954294) fetched by mistake and read; not filed (neither quoted nor relied on).
- Identity-route search (Europe PMC): nothing meets QUESTION-297's identity test. Nearest: Kennedy et al. 2025 (PMC12781289), thoughts of historical loss against network talk of AI/AN identity; abstract read only; falls short (frequency of thoughts, not distress; family in the network). Not filed.
- Codes: Rice LIT-tmpr7q37 / NOTE-tmpso8z1 / THEORY-tmpo8don; Lewis LIT-tmpdsu42 / NOTE-tmp18gag / THEORY-tmp4fo7b; Mulligan LIT-tmpglael / NOTE-tmpxwx4b / THEORY-tmppcqht; Tuulari LIT-tmpuwnm5 / NOTE-tmpv0ug9 / THEORY-tmpseccf; Zhou & Ryan LIT-tmpdvx5j / NOTE-tmp05o0u / THEORY-tmplq0um.
- Claims: CLAIM-tmp3qsdg (design map, thesis, lean); CLAIM-tmpgv8bs (alternative: Mulligan as partial separation, counter); CLAIM-tmpv8nto (donor-gamete design puts marks with genes, demonstrated); ARG-tmpmenxz (Mulligan by abduction to CLAIM-tmpgv8bs).
- Written so far: five LITs, NOTE-tmpso8z1.

## Next

- Read the four texts; file LIT, NOTE, THEORY each.
- File the verdict claims; dated notes; curation; changelog.
- Second part of the lead (distress against group identification): search.
