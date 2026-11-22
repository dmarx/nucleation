# LEAD-138 progress

- Lead: LEAD-138, "Read the endosymbiosis primaries behind the integration question and its cases"
- Branch: claude/lead-138-endosymbiont-facts (from origin/staging)
- Task: read the endosymbiosis primaries the lead names (LIT-1557, 1563, 1565,
  1567, 1569, 1572, 1573, 1586, 1602, 1611, 1612, 1621, 2395, 2398) from lawful
  copies (Europe PMC REST full text, PMC, arXiv, bioRxiv, author copies); check
  each fact CASE-168, 171, 173, 174, 177 take from them; file readings per
  read-and-file steps 5-9; add a dated note on each case (held / did not hold /
  unverified) and on the lead. No status changes on held entries.
  (CASE-169, 170, 172, 175, 176 are not endosymbiont cases and take nothing
  from these works.)

## Done

## Next

- Search author, lab and institutional copies (web search).

## Choices

## Access log (2026-11-22)

- Europe PMC REST fullTextXML (ADR-101): HTTP 500 (not in the open-access
  subset) for PMC3325729, PMC3169327, PMC5027413, PMC39726, PMC5777040,
  PMC8879801, PMC2720180, PMC4547289, and the preprint records PPR30232
  (Husnik 2016 bioRxiv 042267) and PPR21684 (Campbell 2017 bioRxiv 199760).
  No PMCID for LIT-1563, 1567, 1569, 1621, 2395, 2398.
- NCBI E-utilities efetch db=pmc: "publisher ... does not allow downloading
  of the full text in XML form" (PMC39726, PMC3325729).
- pmc.ncbi.nlm.nih.gov/articles/PMC3325729/: reCAPTCHA challenge page. Stopped at PMC.
- biorxiv.org 042267.full.pdf: HTTP 429, Cloudflare error 1015. Stopped at bioRxiv.
- pnas.org/doi/pdf/10.1073/pnas.93.7.2873: Cloudflare "Just a moment". Stopped.
- cell.com/article/S0960982216302639/pdf: Cloudflare. Stopped.
- genome.cshlp.org/content/19/8/1450.full.pdf: "Access denied". Stopped.
- annualreviews.org/doi/pdf/10.1146/annurev-ento-121423-013425: Cloudflare. Stopped.
- repositorio.uchile.cl (LIT-1586 submitted version): "Verificando acceso" bot check. Stopped.
- ASEP (asep.lib.cas.cz) records for LIT-1567, 1569, 1572: metadata only, no file.
- Lund LUP record for LIT-1567: no file link found.
- SciSpace (LIT-1573): abstract only.

## Copies reached (2026-11-22, in scratchpad, not committed)

- LIT-1567 Karnkowska 2016: in-press article PDF on the University of Warsaw
  Faculty of Biology site (first author's institution):
  https://www.biol.uw.edu.pl/wp-content/uploads/sites/19/2020/10/A_Karnkowska_A_Eukaryote_without_a_Mitochondrial_Organelle_160516.pdf
- LIT-1586 Łukasik 2017/2018 PNAS: Symbiosis Evolution Group (Łukasik lab),
  Jagiellonian University, publications page:
  https://symbio.eko.uj.edu.pl/documents/25031683/26786549/2018_Lukasik_et_al_PNAS.pdf/6cddb8b9-6273-03e8-bab0-a957ec180c1d
- LIT-1602 Campbell 2017 Curr Biol: same lab page:
  https://symbio.eko.uj.edu.pl/documents/25031683/26786549/2017_Campbell_et_al_CurrBiol.pdf/1e83749e-750d-5fa5-6594-ec1a9b904fc2
- LIT-2395 Strand 2025/2026: NSF Public Access Repository,
  https://par.nsf.gov/servlets/purl/10652100 (publisher PDF, 2026 vol. 71:209-28)
- core.ac.uk download: Cloudflare. Stopped.

## Filing

- Choice: lead workers change no held status (run-lead step 6), so the read
  LITs stay Unfetched with a dated note; promotion to Active is the owner's.
- Choice: readings done by this worker directly, not by delegated readers
  (one worker, four short papers).
- Copies NOT reached, added 2026-11-22: mccutcheonlab.org (TLS: certificate
  name mismatch), web.biosci.utexas.edu/moran (TLS: incomplete chain),
  typeset.io PDF for LIT-1611 (refused by this session's permission
  system), core.ac.uk (Cloudflare).
- Done: LIT-1567 read: NOTE-tmpzlv8e, THEORY-tmpd9ysz, note on CASE-168, note on LIT-1567.
- Done: LIT-1586 (NOTE-tmp8zw3r, THEORY-tmp4pf2m), LIT-1602 (NOTE-tmpzfvzz,
  THEORY-tmpjqe6l), CASE-177 note, LIT-1586/1602 notes.
- Next: LIT-2395 (NOTE-tmpqvc1g, THEORY-tmp15tfp),
  CLAIM-661 note; notes on CASE-171/173/174 (unverified); LEAD-138 note; changelog.
