# scratch/readers/sweep-pages.md

Which of the sweep's 17 landing pages hold a lawful copy (ADR-108 running notes).

Checked 2026-11-22. Outcomes: (a) full text reached, (b) metadata only or
restricted, (c) obstacle.

## LIT-1409 (Schulz-Hardt et al. 2006, hidden profiles)

- (c) http://mediatum.ub.tum.de/node?id=1156056 redirects to https and
  returns an Anubis "Making sure you're not a bot!" proof-of-work page
  (HTTP 200, /.within.website/). Stopped; not retried. 2026-11-22.

## LIT-1481 (Tilly 1985, War Making and State Making)

- (c) http://deepblue.lib.umich.edu/bitstream/2027.42/51028/1/256.pdf now
  serves the DSpace 7 Angular shell (HTML, not the PDF). Its documented
  REST API (https://deepblue.lib.umich.edu/server/api/pid/find?id=hdl:2027.42/51028)
  returned a Cloudflare "Just a moment..." challenge. Stopped. 2026-11-22.

## LIT-1567 (Karnkowska et al. 2016, Current Biology)

- (b) https://lup.lub.lu.se/search/publication/cfb80059-c720-48dd-9030-f0f47b3ba35b
  is a metadata record (authors Karnkowska ... Hampl, DOI matches); its
  only links are the Research Portal page, the DOI and Google Scholar. No
  file.

## LIT-1586 (Łukasik et al. 2018, PNAS)

- (b) https://ruj.uj.edu.pl/handle/item/54669: DSpace REST API
  (server/api/pid/find?id=item/54669, item ff8fb082-...) gives title,
  authors and DOI matching, dc.rights "Dodaję tylko opis bibliograficzny"
  (bibliographic description only), share type "otwarte czasopismo" (open
  journal, open 6 months after publication). The item has no bundles or
  bitstreams. Metadata only.

## LIT-1639 (Cervera, van der Schaft, Baños 2007, Automatica)

- (c), copy located: the RUG Pure record lists
  https://research.rug.nl/files/2818803/2007AutomaticaCervera.pdf,
  labelled "Final publisher's version, 366 KB" (title and authors on the
  record match the LIT). The file request returned HTTP 403 with a
  Cloudflare "Just a moment..." challenge. Stopped. 2026-11-22. Pure's web
  service needs an API key, so no documented open route was tried.

## LIT-1764 (Pembrey et al. 2006, EJHG)

- (b) Bristol Pure record: metadata only; "Access to Document" gives the
  DOI and a nature.com abstract link. No file.

## LIT-1862 (Contrast effects in stereotype formation, JESP 2002)

- (b) VU Pure record: metadata only; "Access to Document" gives the DOI
  and an old ScienceDirect link. No file.
