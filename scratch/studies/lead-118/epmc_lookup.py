"""LEAD-118: look up the record's Unfetched works in Europe PMC by its REST API.

For each LIT code given (default: the 48 that LEAD-118 lists), read the LIT's
`doi:` (else its title), search Europe PMC
(rest/search?query=DOI:"..."&format=json&resultType=core), and, where the hit
carries a PMCID, ask rest/<PMCID>/fullTextXML whether the open full text is
served. No email address is sent anywhere (ADR-008); requests carry a generic
User-Agent and no contact fields.

Usage (from the repository root):
    python3 -I scratch/studies/lead-118/epmc_lookup.py \
        --out scratch/studies/lead-118/results.tsv [--save-dir DIR] [CODES...]

`--save-dir` keeps the fetched XML (never commit it). Output: a TSV with one
row per LIT and a summary of counts on stdout.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

BASE = "https://www.ebi.ac.uk/europepmc/webservices/rest"
UA = "nucleation-record-lookup/1.0 (no contact)"
LEAD = Path("record/leads.d/LEAD-118.md")
LITDIR = Path("record/literature.d")


def lead_codes(lead_text: str) -> list[str]:
    """The LIT codes listed as members (`- [LIT-n](...)`) in the lead."""
    return re.findall(r"^- \[(LIT-\d+)\]", lead_text, flags=re.M)


def frontmatter_field(text: str, key: str) -> str | None:
    m = re.search(rf"^{key}:\s*(.+)$", text, flags=re.M)
    if not m:
        return None
    return m.group(1).strip().strip("'\"").replace("''", "'")


def classify(hit: dict | None, fulltext_status: int | None, obstacle: str | None) -> str:
    """One of: open-full-text, abstract-only, not-found, obstacle."""
    if obstacle:
        return "obstacle"
    if hit is None:
        return "not-found"
    if hit.get("pmcid") and fulltext_status == 200:
        return "open-full-text"
    return "abstract-only"


def get(url: str) -> tuple[int, bytes]:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        return e.code, b""


def search(query: str) -> tuple[int, list[dict]]:
    url = f"{BASE}/search?" + urllib.parse.urlencode(
        {"query": query, "format": "json", "resultType": "core", "pageSize": 5})
    status, body = get(url)
    if status != 200:
        return status, []
    return status, json.loads(body).get("resultList", {}).get("result", [])


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def pick(results: list[dict], doi: str | None, title: str | None) -> dict | None:
    for r in results:
        if doi and (r.get("doi") or "").lower() == doi.lower():
            return r
    if title:
        t = norm(title)
        for r in results:
            if norm(r.get("title") or "").startswith(t[:60]):
                return r
    return None


def lookup(code: str, save_dir: Path | None) -> dict:
    text = (LITDIR / f"{code}.md").read_text()
    doi = frontmatter_field(text, "doi")
    title = frontmatter_field(text, "title")
    row = {"code": code, "identifier": f"doi:{doi}" if doi else
           f"url:{frontmatter_field(text, 'url')}", "pmid": "", "pmcid": "",
           "isOpenAccess": "", "fulltext_http": "", "result": "", "obstacle": "",
           "other_versions": ""}
    obstacle = None
    hit = None
    if doi:
        st, res = search(f'DOI:"{doi}"')
        if st != 200:
            obstacle = f"search HTTP {st}"
        hit = pick(res, doi, None)
    if hit is None and obstacle is None and title:
        st, res = search(f'TITLE:"{title}"')
        if st != 200:
            obstacle = f"title search HTTP {st}"
        hit = pick(res, None, title)
    ft_status = None
    if hit:
        row["pmid"] = hit.get("pmid", "") or ""
        row["pmcid"] = hit.get("pmcid", "") or ""
        row["isOpenAccess"] = hit.get("isOpenAccess", "") or ""
        if row["pmcid"]:
            ft_status, body = get(f"{BASE}/{row['pmcid']}/fullTextXML")
            row["fulltext_http"] = str(ft_status)
            if ft_status not in (200, 404):
                obstacle = f"fullTextXML HTTP {ft_status}"
            if ft_status == 200 and save_dir:
                save_dir.mkdir(parents=True, exist_ok=True)
                (save_dir / f"{code}_{row['pmcid']}.xml").write_bytes(body)
    # Other versions Europe PMC indexes under the same title (e.g. a preprint,
    # source PPR), and whether the REST full-text route serves them.
    if title and ft_status != 200:
        st, res = search(f'TITLE:"{title}"')
        vers = []
        for r in res:
            if r.get("id") == (hit or {}).get("id") or not \
                    norm(r.get("title") or "").startswith(norm(title)[:50]):
                continue
            vid = r.get("pmcid") or (r.get("id") if r.get("source") == "PPR" else "")
            vst = get(f"{BASE}/{vid}/fullTextXML")[0] if vid else ""
            vers.append(f"{r.get('source')}:{r.get('id')}:doi={r.get('doi','')}"
                        f":fullTextXML={vst}")
        row["other_versions"] = "; ".join(vers)
    row["result"] = classify(hit, ft_status, obstacle)
    row["obstacle"] = obstacle or ""
    return row


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("codes", nargs="*")
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--save-dir", type=Path)
    a = ap.parse_args(argv)
    codes = a.codes or lead_codes(LEAD.read_text())
    cols = ["code", "identifier", "pmid", "pmcid", "isOpenAccess",
            "fulltext_http", "result", "obstacle", "other_versions"]
    rows = []
    for c in codes:
        rows.append(lookup(c, a.save_dir))
        print("\t".join(rows[-1][k] for k in cols), file=sys.stderr)
        time.sleep(0.5)
    with a.out.open("w") as f:
        f.write("\t".join(cols) + "\n")
        for r in rows:
            f.write("\t".join(r[k] for k in cols) + "\n")
    counts: dict[str, int] = {}
    for r in rows:
        counts[r["result"]] = counts.get(r["result"], 0) + 1
    print(json.dumps(counts, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
