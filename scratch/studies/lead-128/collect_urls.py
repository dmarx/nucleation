#!/usr/bin/env python3
"""Collect OSF download URLs for the *_ED.csv files of project vnj8x.

Writes ed_urls.json into the download dir given as argv[1].
Run with: python3 -I collect_urls.py <download_dir>
No email or personal data sent (ADR-008).
"""
import json, urllib.request, time, ssl, sys, os

CA = "/root/.ccr/ca-bundle.crt"
FOLDER = ("https://api.osf.io/v2/nodes/vnj8x/files/osfstorage/"
          "640847d052d0610447d2319f/?page%5Bsize%5D=100")


def get(url, ctx):
    last = None
    for _ in range(8):
        try:
            with urllib.request.urlopen(url, timeout=60, context=ctx) as r:
                return json.load(r)
        except Exception as e:  # OSF API returns intermittent 500s
            last = e
            time.sleep(2)
    raise RuntimeError(f"fail {url}: {last}")


def main():
    out_dir = sys.argv[1]
    ctx = ssl.create_default_context(cafile=CA) if os.path.exists(CA) else None
    urls = {}
    url = FOLDER
    while url:
        d = get(url, ctx)
        for x in d["data"]:
            a = x["attributes"]
            if a["kind"] == "file":
                urls[a["name"]] = [x["links"]["download"], a["size"]]
        url = d["links"].get("next")
    eds = {k: v for k, v in urls.items() if k.endswith("_ED.csv")}
    json.dump(eds, open(os.path.join(out_dir, "ed_urls.json"), "w"))
    print("total files", len(urls), "ED files", len(eds),
          "total ED bytes", sum(v[1] for v in eds.values()))


if __name__ == "__main__":
    main()
