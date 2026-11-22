"""Classifier for LEAD-199: is a change to a CLAIM file a substantive revision?

Substantive (spec, LEAD-199): the commit changes title, role, warrant,
defeated_if, or the body outside sections headed "## Note of ...".
Not substantive: only history entries / dated notes / relation fields /
other frontmatter (version, summary, tags, line ...); and anything from the
CI repair bot or mechanical repair/regenerate/promote commits.

Normalisation before comparing (so mechanical rewrites do not count):
  - markdown links [X](target) -> X   (CI link repair)
  - codes mapped through an alias function (temp -> permanent code)
  - HTML comments dropped (inactive-ok lint suppressions)
  - the H1 line dropped (it repeats code and title)
  - whitespace collapsed (re-wrapping)
"""
import re
import yaml

BOT_AUTHORS = {"github-actions[bot]"}
MECH_MSG = re.compile(
    r"(docs: repair sources|docs: regenerate views|Promote staging|"
    r"concretiz|luria repair|link --fix|^Merge )", re.I)

LINK = re.compile(r"\[([^\]]*)\]\([^)]*\)")
COMMENT = re.compile(r"<!--.*?-->", re.S)
CODE = re.compile(r"\b([A-Z]+-(?:tmp[a-z0-9]+|[0-9]+))\b")
CITE_PAREN = re.compile(r"\(\s*(?:@CODE[\s,;]*(?:and\s*)?)+\)")
BACKFILL = ("role", "warrant")  # absent -> present is a schema backfill, not a revision


def split(text):
    """Return (frontmatter dict, body str)."""
    if text is None:
        return None, None
    if text.startswith("---"):
        parts = text.split("\n---", 2)
        if len(parts) >= 2:
            fm_txt = parts[0][3:]
            body = text[len(parts[0]) + 4:]
            try:
                fm = yaml.safe_load(fm_txt) or {}
            except Exception:
                fm = {}
            if not isinstance(fm, dict):
                fm = {}
            return fm, body
    return {}, text


def norm(s, alias=lambda c: c):
    if s is None:
        return ""
    s = str(s)
    s = COMMENT.sub(" ", s)
    s = LINK.sub(r"\1", s)
    # which code is cited is a relation, not the claim's text: mask codes, then
    # drop parentheses that held only citations, e.g. "(TERM-008)"
    s = CODE.sub("@CODE", s)
    s = CITE_PAREN.sub(" ", s)
    s = " ".join(s.split())
    return re.sub(r" ([.,;:)])", r"\1", s)


def sections(body, alias=lambda c: c):
    """List of (heading, normalised text) for '## ' sections; preamble keyed ''.
    The H1 line is dropped."""
    out, head, buf = [], "", []
    for line in body.splitlines():
        if line.startswith("# ") and not line.startswith("## "):
            continue
        if line.startswith("## "):
            out.append((head, norm("\n".join(buf), alias)))
            head, buf = norm(line[3:], alias), []
        else:
            buf.append(line)
    out.append((head, norm("\n".join(buf), alias)))
    return [(h, t) for h, t in out if h or t]


def is_dated(head):
    return head.startswith("Note of")


DEF_FIELDS = ("title", "role", "warrant", "defeated_if")


def classify(old, new, author="", message="", alias=lambda c: c):
    """Return dict: kind in {'created','deleted','mechanical','substantive',
    'nonsubstantive'}, plus flags: status_change, title_change,
    lenient (substantive even when whole new sections are ignored), fields."""
    r = {"kind": None, "status_change": False, "title_change": False,
         "lenient": False, "fields": []}
    if old is None:
        r["kind"] = "created"; return r
    if new is None:
        r["kind"] = "deleted"; return r
    fo, bo = split(old)
    fn, bn = split(new)
    r["status_change"] = str(fo.get("status")) != str(fn.get("status"))
    if author in BOT_AUTHORS or MECH_MSG.search(message or ""):
        r["kind"] = "mechanical"; return r
    changed = [f for f in DEF_FIELDS if norm(fo.get(f), alias) != norm(fn.get(f), alias)
               and not (f in BACKFILL and fo.get(f) in (None, ""))]
    r["title_change"] = "title" in changed
    so = [(h, t) for h, t in sections(bo, alias) if not is_dated(h)]
    sn = [(h, t) for h, t in sections(bn, alias) if not is_dated(h)]
    body_changed = so != sn
    if body_changed:
        changed.append("body")
    r["fields"] = changed
    r["kind"] = "substantive" if changed else "nonsubstantive"
    # lenient: ignore wholly added new sections; count a change only if an
    # existing section's text changed or a section was removed
    dn = {}
    for h, t in sn:
        dn.setdefault(h, []).append(t)
    sec_changed = False
    for h, t in so:
        if h not in dn or t not in dn[h]:
            sec_changed = True; break
    r["lenient"] = bool([f for f in changed if f != "body"]) or sec_changed
    return r


REL_FIELDS = ("rests_on", "grounds")


def edges(text):
    """Codes named in rests_on/grounds of a file's frontmatter (cheap parse)."""
    if not text or not text.startswith("---"):
        return set()
    end = text.find("\n---", 3)
    fm = text[3:end] if end > 0 else text[3:]
    out, cur = set(), None
    for line in fm.splitlines():
        m = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
        if m:
            cur = m.group(1) if m.group(1) in REL_FIELDS else None
            if cur and m.group(2).strip():
                out.update(CODE.findall(m.group(2)))
            continue
        if cur and re.match(r"^\s*-\s*", line):
            out.update(CODE.findall(line))
    return out
