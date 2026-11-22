"""Fetch the public series the LEAD-041 application uses, into a directory
outside the repository, and write a small monthly CSV beside them.

Sources (US federal statistics, public domain):
- Federal Reserve Board, H.15 Selected Interest Rates, the Data Download
  Program's preformatted package (rel=H15&filetype=zip), series
  RIFSPFF_N.M, the monthly effective federal funds rate.
- Bureau of Labor Statistics public API v1 (no key, no registration, no
  email): LNS14000000, the civilian unemployment rate (SA), and
  CUSR0000SA0, CPI-U all items (SA).

Usage:
    python3 -I fetch.py <download-dir>

Writes <download-dir>/monthly.csv with columns month,ffr,unrate,cpi.
H.15 must already be unzipped at <download-dir>/h15/H15_data.xml (the
script downloads it if absent). Never commit the downloads.
"""
import csv
import json
import os
import subprocess
import sys
import xml.etree.ElementTree as ET

H15_URL = "https://www.federalreserve.gov/datadownload/Output.aspx?rel=H15&filetype=zip"
BLS_URL = "https://api.bls.gov/publicAPI/v1/timeseries/data/"
SERIES = {"LNS14000000": "unrate", "CUSR0000SA0": "cpi"}


def curl(args):
    subprocess.run(["curl", "-sS", "-f"] + args, check=True)


def h15_monthly_ffr(path):
    out = {}
    in_series = False
    for event, el in ET.iterparse(path, events=("start", "end")):
        tag = el.tag.rsplit("}", 1)[-1]
        if event == "start" and tag == "Series":
            in_series = el.get("SERIES_NAME") == "RIFSPFF_N.M"
        elif event == "end" and tag == "Obs" and in_series:
            v = el.get("OBS_VALUE")
            t = el.get("TIME_PERIOD")
            if v not in (None, "", "NA", "ND"):
                try:
                    out[t[:7]] = float(v)
                except ValueError:
                    pass
        elif event == "end" and tag == "Series":
            in_series = False
            el.clear()
    return out


def bls(dl, start, end):
    fn = os.path.join(dl, f"bls_{start}_{end}.json")
    if not os.path.exists(fn):
        body = json.dumps({"seriesid": list(SERIES), "startyear": str(start),
                           "endyear": str(end)})
        curl(["-X", "POST", "-H", "Content-Type: application/json",
              "--data", body, "-o", fn, BLS_URL])
    with open(fn) as f:
        d = json.load(f)
    if d.get("status") != "REQUEST_SUCCEEDED":
        raise RuntimeError(f"BLS refused {start}-{end}: {d.get('message')}")
    rows = {}
    for s in d["Results"]["series"]:
        name = SERIES[s["seriesID"]]
        for o in s["data"]:
            if o["period"].startswith("M") and o["period"] != "M13":
                m = f"{o['year']}-{o['period'][1:]}"
                rows.setdefault(m, {})[name] = float(o["value"])
    return rows


def main(dl):
    os.makedirs(dl, exist_ok=True)
    xml = os.path.join(dl, "h15", "H15_data.xml")
    if not os.path.exists(xml):
        z = os.path.join(dl, "h15.zip")
        curl(["-L", "-o", z, H15_URL])
        os.makedirs(os.path.join(dl, "h15"), exist_ok=True)
        subprocess.run(["unzip", "-o", "-q", z, "-d", os.path.join(dl, "h15")], check=True)
    ffr = h15_monthly_ffr(xml)
    macro = {}
    for start in range(1955, 2027, 10):
        for m, v in bls(dl, start, min(start + 9, 2026)).items():
            macro.setdefault(m, {}).update(v)
    with open(os.path.join(dl, "monthly.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["month", "ffr", "unrate", "cpi"])
        for m in sorted(set(ffr) & set(macro)):
            r = macro[m]
            if "unrate" in r and "cpi" in r:
                w.writerow([m, ffr[m], r["unrate"], r["cpi"]])


if __name__ == "__main__":
    main(sys.argv[1])
