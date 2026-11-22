"""Fetch the public series the LEAD-041 application uses into a directory
outside the repository. Never commit the downloads.

Sources, read 2026-11-22:
- Federal Reserve Board, H.15 Selected Interest Rates, the Data Download
  Program's preformatted package (series RIFSPFF_N.M, the monthly
  effective federal funds rate):
  https://www.federalreserve.gov/datadownload/Output.aspx?rel=H15&filetype=zip
- Federal Reserve Bank of Philadelphia, Real-Time Data Set for
  Macroeconomists: the civilian unemployment rate (rucQvMd.xlsx) and CPI
  (cpiQvMd.xlsx), quarterly vintages of monthly observations, linked from
  https://www.philadelphiafed.org/surveys-and-data/real-time-data-research/ruc
  and .../cpi

No key, registration or email address is sent to any of them.

Usage: python3 -I fetch.py <download-dir>
"""
import os
import subprocess
import sys

H15 = "https://www.federalreserve.gov/datadownload/Output.aspx?rel=H15&filetype=zip"
PHILLY = "https://www.philadelphiafed.org/-/media/FRBP/Assets/Surveys-And-Data/real-time-data/data-files/xlsx/"
FILES = {
    "rucQvMd.xlsx": PHILLY + "rucQvMd.xlsx?sc_lang=en&hash=A96BC0C2253B04EAEB8C4DC42D4F5CBA",
    "cpiQvMd.xlsx": PHILLY + "cpiQvMd.xlsx?sc_lang=en&hash=9659566E92130D1A394C7FEDB6EC4115",
}


def get(url, path):
    subprocess.run(["curl", "-sS", "-f", "-L", "-o", path, url], check=True)


def main(dl):
    os.makedirs(os.path.join(dl, "h15"), exist_ok=True)
    os.makedirs(os.path.join(dl, "philly"), exist_ok=True)
    z = os.path.join(dl, "h15.zip")
    if not os.path.exists(os.path.join(dl, "h15", "H15_data.xml")):
        get(H15, z)
        subprocess.run(["unzip", "-o", "-q", z, "-d", os.path.join(dl, "h15")], check=True)
    for name, url in FILES.items():
        p = os.path.join(dl, "philly", name)
        if not os.path.exists(p):
            get(url, p)


if __name__ == "__main__":
    main(sys.argv[1])
