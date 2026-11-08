# scratch/formal/synthesis_fixture.py: fire the SYNTHESIS scheme's rules and view on a throwaway record (ADR-tmp72iro; DP-4)
# run: python3 scratch/formal/synthesis_fixture.py   (needs luria and jinja2; uses the repo's luria.yaml, writes only to a temp dir)
"""A fixture record, built from this repository's luria.yaml in a temporary
directory, holding a few components and eight accounts (ADR-tmp72iro: a
SYNTHESIS is an account, and whatever adds to its components is a CLAIM):

  S1  Current, integrating an Active and a Proposed claim and a term  -> clean
  S2  Proposed, integrating S1                                          -> clean
  S3  Current, integrating a Superseded claim                           -> current_account_on_superseded_claim
  S4  Superseded by S1                                                  -> clean, hidden from the view
  S5  Current, integrating the Superseded S4                            -> current_account_on_superseded_account
  S6  Proposed, integrating a Superseded claim                          -> clean: only an account in force must follow
  S7  keeping a removed claim field (route)                             -> accepted: luria does not refuse an
                                                                           undeclared field, so a moved entry drops them by hand
  S8  Superseded by the claim its content returned to                   -> clean
  CLAIM-004 resting on S1                                               -> refused: a claim's premises are claims

It runs `luria lint` on the fixture and checks each rule fires where it should
and nowhere else, then renders the current-account view, checks what it shows,
changes a component's status, and checks the change appears on the next render.
"""
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]

def entry(code, fm, body=""):
    lines = ["---"] + fm + ["---", "", f"# {code}: {dict(l.split(': ', 1) for l in fm if ': ' in l)['title'].strip(chr(39))}", "", body or "Fixture entry."]
    return "\n".join(lines) + "\n"

def claim(code, status, title):
    return entry(code, [f"status: {status}", f"title: '{title}'", "version: 1", "role: thesis",
                        "warrant: interpretive", "defeated_if: >-\n  a fixture case", "tags:\n- individuation",
                        "date: '2026-11-07'", "line:\n- distributed-agency", "summary: >-\n  Fixture claim."])

def term(code, title):
    return entry(code, ["status: Active", f"title: '{title}'", "version: 1", "tags:\n- individuation",
                        "date: '2026-11-07'", "line: distributed-agency", "summary: >-\n  Fixture term."])

def synthesis(code, title, status, integrates, extra=()):
    fm = [f"status: {status}", f"title: '{title}'", "version: 1",
          "defeated_if: >-\n  a component misstated", "tags:\n- individuation",
          "date: '2026-11-08'", "line:\n- distributed-agency",
          "integrates:\n" + "".join(f"- {c}\n" for c in integrates).rstrip("\n"), *extra,
          "summary: >-\n  Fixture account."]
    return entry(code, fm)

def build(root: Path):
    shutil.copy(REPO / "luria.yaml", root / "luria.yaml")
    (root / "record" / "views.d").mkdir(parents=True)
    shutil.copy(REPO / "record/views.d/current-account.md.j2", root / "record/views.d/")
    for d in ("claims.d", "terms.d", "syntheses.d"):
        (root / "record" / d).mkdir(parents=True, exist_ok=True)
    w = lambda rel, text: (root / rel).write_text(text)
    w("record/claims.d/CLAIM-001.md", claim("CLAIM-001", "Active", "An active fixture claim"))
    w("record/claims.d/CLAIM-002.md", claim("CLAIM-002", "Proposed", "A proposed fixture claim"))
    w("record/claims.d/CLAIM-003.md", claim("CLAIM-003", "Superseded", "A replaced fixture claim").replace(
        "role: thesis", "superseded_by:\n- CLAIM-001\nrole: thesis", 1))
    w("record/claims.d/CLAIM-004.md", claim("CLAIM-004", "Proposed", "A claim resting on an account").replace(
        "role: thesis", "rests_on:\n- SYNTHESIS-001\nrole: thesis", 1))
    w("record/terms.d/TERM-001.md", term("TERM-001", "a fixture term"))
    S = [
        ("SYNTHESIS-001", "S1 clean", "Current", ["CLAIM-001", "CLAIM-002", "TERM-001"]),
        ("SYNTHESIS-002", "S2 over S1", "Proposed", ["SYNTHESIS-001", "CLAIM-001"]),
        ("SYNTHESIS-003", "S3 current on a superseded claim", "Current", ["CLAIM-003"]),
        ("SYNTHESIS-004", "S4 superseded", "Superseded", ["CLAIM-001"], ["superseded_by:\n- SYNTHESIS-001"]),
        ("SYNTHESIS-005", "S5 current on a superseded account", "Current", ["SYNTHESIS-004"]),
        ("SYNTHESIS-006", "S6 proposed on a superseded claim", "Proposed", ["CLAIM-003"]),
        ("SYNTHESIS-007", "S7 keeping a route", "Proposed", ["CLAIM-001"], ["route: derived"]),
        ("SYNTHESIS-008", "S8 returned to a claim", "Superseded", ["CLAIM-001"], ["superseded_by:\n- CLAIM-002"]),
    ]
    for code, *rest in S:
        w(f"record/syntheses.d/{code}.md", synthesis(code, *rest))

def lint(root: Path) -> str:
    r = subprocess.run(["luria", "lint"], cwd=root, capture_output=True, text=True)
    return r.stdout + r.stderr

def render(root: Path) -> str:
    code = ("import os,sys; os.chdir(sys.argv[1]); from luria.config import current; from luria import views;"
            "print(views.render(current().views['current-account']))")
    r = subprocess.run([sys.executable, "-c", code, str(root)], capture_output=True, text=True)
    if r.returncode:
        raise SystemExit("render failed:\n" + r.stderr[-2000:])
    return r.stdout

def main():
    failures = []
    def check(ok, what):
        print(("ok   " if ok else "FAIL ") + what)
        if not ok:
            failures.append(what)
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        build(root)
        out = lint(root)
        lines = out.splitlines()
        expect = {"current_account_on_superseded_claim": "SYNTHESIS-003",
                  "current_account_on_superseded_account": "SYNTHESIS-005"}
        def matches(rule):
            # the documents listed under "N match(es) of the pattern `rule`"
            found, on = [], False
            for l in lines:
                if f"of the pattern `{rule}`" in l:
                    on = True
                    continue
                if on and l.strip().startswith("record/"):
                    found.append(l.split(":")[0].rsplit("/", 1)[-1].removesuffix(".md"))
                    continue
                on = False
            return found
        for rule, code in expect.items():
            got = matches(rule)
            check(got == [code], f"{rule} fires on {code} and nothing else (got {got})")
        rest_lines = [l for l in lines if "CLAIM-004" in l and "SYNTHESIS-001" in l]
        check(bool(rest_lines), "a claim resting on an account is refused" + (f" ({rest_lines[0].strip()[:90]})" if rest_lines else ""))
        page = render(root)
        check("SYNTHESIS-001" in page and "SYNTHESIS-002" in page, "the view shows the accounts in force and offered")
        check("### SYNTHESIS-004" not in page, "the view leaves out a superseded account")
        check("### SYNTHESIS-008" not in page, "the view leaves out an account that returned to a claim")
        check("| TERM |" in page and "| CLAIM |" in page and "| SYNTHESIS |" in page, "the view shows each component's kind")
        check("## Lines with no account yet" in page, "the view lists the lines with no account")
        claim_file = root / "record/claims.d/CLAIM-001.md"
        claim_file.write_text(claim_file.read_text().replace("status: Active", "status: Superseded", 1))
        page2 = render(root)
        row = [l for l in page2.splitlines() if l.startswith("| [CLAIM-001]") or l.startswith("| CLAIM-001")]
        check(bool(row) and "Superseded" in row[0], "a component's status change shows on the next render")
        if failures:
            print("\n--- lint output (tail) ---\n" + "\n".join(lines[-40:]))
    print(f"\n{len(failures)} failure(s)")
    sys.exit(1 if failures else 0)

if __name__ == "__main__":
    main()
