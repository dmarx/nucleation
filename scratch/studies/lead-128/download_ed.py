#!/usr/bin/env python3
"""Download the *_ED.csv files listed in ed_urls.json into <dir>/osf_raw.

Run: python3 -I download_ed.py <download_dir>
Downloads go to the session scratchpad only; never committed (ADR per brief).
"""
import json, urllib.request, time, ssl, sys, os

CA = "/root/.ccr/ca-bundle.crt"


def main():
    out_dir = sys.argv[1]
    raw = os.path.join(out_dir, "osf_raw")
    os.makedirs(raw, exist_ok=True)
    ctx = ssl.create_default_context(cafile=CA) if os.path.exists(CA) else None
    eds = json.load(open(os.path.join(out_dir, "ed_urls.json")))
    done = 0
    for name, (url, size) in sorted(eds.items()):
        dest = os.path.join(raw, name)
        if os.path.exists(dest) and os.path.getsize(dest) > 0:
            done += 1
            continue
        for attempt in range(6):
            try:
                with urllib.request.urlopen(url, timeout=60, context=ctx) as r:
                    data = r.read()
                open(dest, "wb").write(data)
                done += 1
                break
            except Exception as e:
                if attempt == 5:
                    print("FAILED", name, e)
                time.sleep(2)
    print("downloaded/present", done, "of", len(eds))


if __name__ == "__main__":
    main()
