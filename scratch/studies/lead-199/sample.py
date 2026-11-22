"""Draw a random sample of classified (non-mechanical, non-created) claim-file
changes for hand-checking; print a compact word diff of each."""
import json, os, random, subprocess, sys
D = os.path.dirname(os.path.abspath(__file__))
REPO = sys.argv[1]; N = int(sys.argv[2]); SEED = int(sys.argv[3])
R = json.load(open(f"{D}/revisions.json"))
P = json.load(open(f"{D}/population.json"))
KINDS = os.environ.get("KINDS", "substantive,nonsubstantive").split(",")
pool = [r for r in R if r["kind"] in KINDS]
random.seed(SEED)
for i, r in enumerate(random.sample(pool, N)):
    files = subprocess.run(["git", "-C", REPO, "show", "--format=", "--name-only", r["h"], "--", "record/claims.d/"],
                           capture_output=True, text=True).stdout.split()
    names = set([r["claim"]] + P[r["claim"]]["aliases"])
    path = next((f for f in files if os.path.basename(f)[:-3] in names), None)
    print(f"=== #{i} {r['h'][:9]} {r['claim']} kind={r['kind']} lenient={r['lenient']} fields={r['fields']} "
          f"status={r['status_change']} | {r['a']} | {r['s'][:80]} | files={len(files)}")
    if path is None:
        cand = [f for f in files]
        print("   paths:", cand[:5]); continue
    d = subprocess.run(["git", "-C", REPO, "show", "--format=", "--word-diff=plain", "-U0", r["h"], "--", path],
                       capture_output=True, text=True).stdout
    lines = [l for l in d.splitlines() if ("[-" in l or "{+" in l)]
    for l in lines[:8]:
        print("   ", l[:260])
    if len(lines) > 8:
        print("    ...", len(lines) - 8, "more changed lines")
