# LEAD-051 study directory

Reading of LIT-2462 (Peng et al. 2025, *Immunity*) for LEAD-051.

## How the paper was fetched (2026-11-22)

Prior stops (NOTE-1763, 2026-11-12): PMC reCAPTCHA, Europe PMC Cloudflare,
Europe PMC REST `fullTextXML` 500, publisher PDF 403.

Retried on 2026-11-22:
- Europe PMC REST `fullTextXML` for PMC12412910: still HTTP 500.
- NCBI PMC OA service (`oa.fcgi`): HTTP 404 (not in the OA subset).
- Publisher PDF (cell.com): refused by this session's permission classifier
  (Unauthorized Access) — not retried.
- **NCBI E-utilities `efetch` (db=pmc, id=12412910): HTTP 200**, full JATS
  XML of the NIH Public Access author manuscript (nihpa), 160 KB, with
  Introduction, Results, Discussion and STAR Methods. This is the
  repository's documented machine interface (ADR-101); it is the route read.

Downloaded XML and extracted text live only in the session scratchpad
(`lead-051/epmc/efetch.xml`, `lead-051/reading.txt`) and are **not** committed.

## Rerun

    curl -sS -o efetch.xml \
      "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=12412910&rettype=full&retmode=xml"
    python3 -I extract.py efetch.xml > reading.txt

`extract.py` parses the JATS XML into readable sections. No email is sent to
any service (ADR-008).
