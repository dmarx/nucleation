# scratch/readers/lit-tmpa7f10.md

Running notes (ADR-108). Reader: sweep batch E, 2026-11-22.

## Step 1: copy located and fetched (2026-11-22)

- **Fetched once**: https://osf.io/29jeb/download, 2026-11-22 ~11:34 UTC, one
  GET with curl (generic user agent, no email or other identifier sent).
  Redirect chain: osf.io/29jeb/download -> 301 osf.io/download/29jeb -> 308
  .../29jeb/ -> 302 files.osf.io/v1/resources/29jeb_v1/providers/osfstorage/64f8b4716c0f5a31cad05897
  -> 302 to OSF's object storage (signed URL) -> 200. **No bot check, no
  challenge.** Saved at scratchpad/downloads/sweep-e/LIT-tmpa7f10/law2023-preprint.docx
  (123 KB, Word 2007+). Text extracted with python3 -I (zipfile + XML).
- **File name served**: "CFC, FSC & RFG Manuscript 5-21-24 - Preprint.docx".
  So the file now behind the DOI is a manuscript dated **21 May 2024**, not
  necessarily the text first posted on 6 September 2023 (`published:`).
  The filer should record that the version read is the 2024-05-21 file.
- **Kind (step 5)**: the authors' own preprint on PsyArXiv/OSF (CC BY per the
  LIT's status note). Lawful.
- **Identity check: matches, with an author-order correction.** Title "A
  Future Beyond Ourselves: Can Self-Oriented Prospection Motivate
  Intergenerational Beneficence?" Authors on the file: "*Stylianos
  Syropoulos, *Kyle F. Law, Matthew Coleman, & Liane Young", "* Denotes joint
  first-authorship" (Boston College; University at Albany; Northeastern).
  The LIT (from Europe PMC) lists Law first; this version lists Syropoulos
  first, as joint first author. Abstract matches the LIT's quotation (ten
  studies, N = 11,261 US participants). No page numbers in the docx; sections
  are cited below by heading and study.
