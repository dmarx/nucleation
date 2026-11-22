# scratch/studies/unfetched-api-sweep/sweep.py
"""Sweep the record's Unfetched works through sanctioned machine routes.

Phase 1 (discover): OpenAlex, Unpaywall (email noreply@anthropic.com, ADR-008),
Europe PMC search, the NCBI ID converter. Phase 2 (probe): one GET per candidate
copy, no retries; a host that returns a challenge is not contacted again in the run.

Run: python3 -I sweep.py <unfetched.tsv> <out_dir>
"""
from __future__ import annotations

import csv
import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

UA = "nucleation-record-sweep/1.0 (research record; contact noreply@anthropic.com)"
EMAIL = "noreply@anthropic.com"  # ADR-008: never the owner's or anyone's address
CHALLENGE_MARKERS = (
    b"just a moment", b"cf-chl", b"challenge-platform", b"incapsula",
    b"_incapsula_resource", b"captcha", b"are you a robot", b"verify you are human",
    b"cf-browser-verification", b"enable javascript and cookies",
)
SKIP_HOSTS = ("doi.org", "dx.doi.org")  # resolvers, not copies


def classify(status: int | None, ctype: str, head: bytes) -> str:
    """Classify one probe from its status, content type and first bytes."""
    low = head[:65536].lower()
    if status is None:
        return "error"
    if status in (401, 403, 429, 503) or any(m in low for m in CHALLENGE_MARKERS):
        return "challenge" if status != 401 else "refused"
    if status == 404 or status == 410:
        return "not-found"
    if status >= 400:
        return "error"
    if head.startswith(b"%PDF") or "pdf" in ctype.lower():
        return "pdf"
    if "html" in ctype.lower():
        return "html"
    return "other"


def candidates(openalex: dict | None, unpaywall: dict | None) -> list[dict]:
    """Ordered, de-duplicated candidate copies from OpenAlex and Unpaywall records."""
    out: list[dict] = []
    seen: set[str] = set()

    def add(url: str | None, kind: str, version: str | None, src: str) -> None:
        if not url or url in seen:
            return
        host = urllib.parse.urlparse(url).netloc.lower()
        if any(host == h or host.endswith("." + h) for h in SKIP_HOSTS):
            return
        seen.add(url)
        out.append({"url": url, "kind": kind, "version": version or "", "via": src, "host": host})

    for loc in (unpaywall or {}).get("oa_locations") or []:
        add(loc.get("url_for_pdf"), loc.get("host_type") or "", loc.get("version"), "unpaywall")
    for loc in (openalex or {}).get("locations") or []:
        stype = ((loc.get("source") or {}).get("type")) or "unknown"
        add(loc.get("pdf_url"), stype, loc.get("version"), "openalex")
    for loc in (unpaywall or {}).get("oa_locations") or []:
        add(loc.get("url_for_landing_page"), loc.get("host_type") or "", loc.get("version"), "unpaywall")
    for loc in (openalex or {}).get("locations") or []:
        if (loc.get("source") or {}).get("type") != "journal":
            add(loc.get("landing_page_url"), ((loc.get("source") or {}).get("type")) or "unknown",
                loc.get("version"), "openalex")
    return out


def get(url: str, limit: int = 65536, timeout: int = 30) -> tuple[int | None, str, bytes, str]:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.headers.get("Content-Type", ""), r.read(limit), r.geturl()
    except urllib.error.HTTPError as e:
        try:
            body = e.read(limit)
        except Exception:
            body = b""
        return e.code, e.headers.get("Content-Type", "") if e.headers else "", body, url
    except Exception as e:  # network error, TLS, timeout
        return None, "", repr(e).encode()[:300], url


def get_json(url: str) -> dict | None:
    status, _, body, _ = get(url, limit=5_000_000)
    if status != 200:
        return None
    try:
        return json.loads(body)
    except ValueError:
        return None


def discover(doi: str) -> dict:
    q = urllib.parse.quote(doi, safe="/")
    oa = get_json(f"https://api.openalex.org/works/doi:{q}")
    time.sleep(0.2)
    up = get_json(f"https://api.unpaywall.org/v2/{q}?email={EMAIL}")
    time.sleep(0.2)
    ep = get_json("https://www.ebi.ac.uk/europepmc/webservices/rest/search?"
                  + urllib.parse.urlencode({"query": f'DOI:"{doi}"', "format": "json", "resultType": "lite"}))
    time.sleep(0.2)
    ic = get_json("https://pmc.ncbi.nlm.nih.gov/tools/idconv/api/v1/articles/?"
                  + urllib.parse.urlencode({"ids": doi, "format": "json", "tool": "nucleation-sweep"}))
    time.sleep(0.4)
    pmcid = ""
    for rec in (ic or {}).get("records") or []:
        pmcid = rec.get("pmcid") or pmcid
    ep_hits = ((ep or {}).get("resultList") or {}).get("result") or []
    ep_oa = [h for h in ep_hits if h.get("isOpenAccess") == "Y" or h.get("inEPMC") == "Y"]
    if not pmcid:
        for h in ep_hits:
            pmcid = h.get("pmcid") or pmcid
    return {
        "openalex_found": oa is not None,
        "oa_status": ((oa or {}).get("open_access") or {}).get("oa_status", ""),
        "unpaywall_found": up is not None,
        "pmcid": pmcid,
        "europepmc_oa": bool(ep_oa),
        "candidates": candidates(oa, up),
    }


def probe_all(cands: list[dict], challenged: set[str], max_per_work: int = 6) -> list[dict]:
    res = []
    for c in cands[:max_per_work]:
        if c["host"] in challenged:
            res.append({**c, "result": "skipped-host-challenged", "status": ""})
            continue
        status, ctype, head, final = get(c["url"])
        r = classify(status, ctype, head)
        if r == "challenge":
            challenged.add(c["host"])
        res.append({**c, "result": r, "status": status if status is not None else "", "final": final})
        time.sleep(0.5)
        if r == "pdf":
            break
    return res


def main(tsv: str, out_dir: str) -> None:
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    rows = list(csv.DictReader(open(tsv), delimiter="\t"))
    challenged: set[str] = set()
    results = []
    for i, row in enumerate(rows):
        rec = {"code": row["code"], "doi": row["doi"], "url": row["url"], "title": row["title"]}
        if row["doi"]:
            rec.update(discover(row["doi"]))
            if rec.get("pmcid"):
                rec["candidates"].insert(0, {
                    "url": f"https://www.ebi.ac.uk/europepmc/webservices/rest/{rec['pmcid']}/fullTextXML",
                    "kind": "repository", "version": "", "via": "europepmc-rest",
                    "host": "www.ebi.ac.uk"})
        else:
            rec.update({"candidates": [{"url": row["url"], "kind": "recorded", "version": "",
                                         "via": "record", "host": urllib.parse.urlparse(row["url"]).netloc}]})
        rec["probes"] = probe_all(rec["candidates"], challenged)
        results.append(rec)
        print(i, row["code"], [p["result"] for p in rec["probes"]], flush=True)
    (out / "results.json").write_text(json.dumps(results, indent=1))
    (out / "challenged_hosts.json").write_text(json.dumps(sorted(challenged), indent=1))


if __name__ == "__main__":
    main(*sys.argv[1:3])
