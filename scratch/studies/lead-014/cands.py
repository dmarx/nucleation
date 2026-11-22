import re, glob, yaml, os, sys
root = sys.argv[1]; log = sys.argv[2]


def fm(p):
    t = open(p).read()
    if not t.startswith('---'):
        return {}
    try:
        return yaml.safe_load(t.split('---', 2)[1]) or {}
    except Exception:
        return {}


lits = {}
for p in glob.glob(root + '/record/literature.d/LIT-*.md'):
    d = fm(p)
    if d.get('arxiv'):
        lits[os.path.basename(p)[:-3]] = (d.get('arxiv'), d.get('title'))
commits = []; cur = None
for line in open(log):
    line = line.rstrip('\n')
    if line.startswith('@@'):
        h, dt, s = line[2:].split('|', 2); cur = [h, dt, s, []]; commits.append(cur)
    elif line and cur:
        st, path = line.split('\t', 1); cur[3].append((st, os.path.basename(path)[:-3]))
commits.reverse()
corr = re.compile(r'correct|missed|omit|left out|wrong|re-read|reread|backfill', re.I)
sweep = re.compile(r'directive|inactive-ok|status review|promot|concretiz|lint|sweep|repair|stale', re.I)
out = []
for p in glob.glob(root + '/record/notes.d/NOTE-*.md'):
    d = fm(p); lit = d.get('paper')
    if isinstance(lit, list):
        lit = lit[0] if lit else None
    if lit not in lits:
        continue
    names = {os.path.basename(p)[:-3]} | set(d.get('formerly') or [])
    created = None; later = []
    for h, dt, s, files in commits:
        if any(n in names for _, n in files):
            if created is None:
                created = (h, dt, s); continue
            if corr.search(s) and not sweep.search(s):
                later.append((h, dt, s[:90]))
    if created and later:
        out.append((created[1], os.path.basename(p)[:-3], lit, lits[lit][0], created[0], created[2][:80], later))
for o in sorted(out, reverse=True)[:40]:
    print(o[0], o[1], o[2], o[3], o[4], o[5])
    for l in o[6]:
        print('    ', l)
