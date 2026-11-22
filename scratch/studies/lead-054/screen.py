"""LEAD-054: write the screening table from hits.json and the decisions below.

Run:  python3 -I screen.py HITS_JSON > screening.tsv

Criteria, applied to title and abstract (2026-11-22):
  I1  flow (a flow scale, or the challenge/skill model) reported at the moment
      of a signal, i.e. by experience sampling during the activity, not by an
      end-of-day diary, a post-task questionnaire or a cross-sectional survey;
  I2  affect (happiness, valence, positive affect, mood, hedonic tone)
      reported at the same signal;
  I3  the study relates the two, or compares both across activities.
Q = meets all three; U = flow is sampled but the abstract names no affect
measure or no relation (not registered); X = excluded, with the reason.
"""
import json
import sys

Q, U = "Q", "U"
DECISIONS = {
    "10.31234/osf.io/wfa4h_v1": (Q, "ESM situational flow and happiness at work, 64 managers, 4383 reports"),
    "10.1080/02699931.2024.2367782": ("X", "flow conduciveness only in a recall study; the ESM study samples pleasantness, not flow"),
    "10.31234/osf.io/ew3tp": ("X", "ESM flow, no affect (distraction)"),
    "10.31234/osf.io/a7uqx": ("X", "earlier version of the same smartphone and flow preprint; no affect"),
    "10.1177/1757913917739041": (Q, "ESM, art-making with hedonic tone and flow state at the signal"),
    "10.3233/978-1-61499-121-2-177": ("X", "ESM form filled in after a VR session, not during it"),
    "10.1186/1472-6955-10-3": (U, "ESM flow situations at work; abstract names no affect measure"),
    "10.3233/978-1-61499-282-0-65": (U, "ESM flow events with heart rate; no affect relation in abstract"),
    "10.1037/0022-3514.95.3.679": ("X", "ESM activation and positive affect; flow not measured"),
    "10.1037/h0094578": (U, "ESM quality of experience by challenge/skill; affect not separated in abstract"),
    "10.1111/j.1467-6494.1996.tb00512.x": (Q, "ESM challenge/skill balance predicts momentary happiness, 208 adolescents"),
    "10.1002/smi.3424": ("X", "flow in the morning, vigour at end of day: affect not concurrent"),
    "10.1037/ocp0000369": ("X", "daily diary"),
    "10.1007/s11031-021-09894-2": ("X", "daily diary; no affect"),
    "10.1017/s0714980810000395": (U, "ESM flow in older adults; no affect in abstract"),
    "10.1111/jora.12522": (Q, "ESM, positive and negative affect related to optimal experience, 245 adolescents"),
    "10.1037/a0036519": (U, "ESM quality of experience in rehabilitation; affect not named"),
    "10.1007/s10964-006-9069-y": (U, "ESM optimal experience in learning; affect not named"),
    "10.1080/00223980.2012.656156": (Q, "ESM teachers, the work paradox: flow at work not felt as pleasant"),
    "10.1097/00005053-198709000-00006": (U, "ESM optimal experience by challenge/skill ratio; affect not named"),
    "10.1037//0022-3514.56.5.815": (Q, "ESM, flow (high challenge and skill) and quality of experience incl. affect, work vs leisure"),
    "10.1111/jopy.12938": ("X", "laboratory game, flow and affect rated after the task"),
    "10.1080/00223980.2022.2074347": ("X", "cross-sectional recall of flow"),
    "10.3389/fpsyg.2017.01121": ("X", "laboratory physiology; not ESM"),
    "10.3389/frobt.2024.1393795": ("X", "laboratory; not ESM"),
    "10.3389/fpsyg.2020.00300": ("X", "laboratory gambling; not ESM"),
    "10.3389/fpsyg.2019.02375": ("X", "pre/post session ratings; not ESM"),
    "10.1016/j.ijpsycho.2015.05.001": ("X", "laboratory game; post-task flow"),
    "10.1089/cyber.2010.0377": ("X", "laboratory physiology; not ESM"),
    "10.1007/s10964-010-9514-9": ("X", "self-efficacy; flow not analysed with affect in abstract"),
    "10.1177/00332941251415313": ("X", "systematic review of dispositional flow and well-being"),
    "10.1016/s2542-5196(21)00286-2": ("X", "commentary"),
    "10.5014/ajot.48.11.989": ("X", "commentary"),
    "10.3390/bs15060768": ("X", "intervention study; not ESM"),
    "10.20944/preprints202507.2670.v1": ("X", "protocol"),
    "2301.09402v1": ("X", "laboratory mixed-reality music; not ESM"),
    "1907.01934v2": ("X", "laboratory model of agency; not ESM"),
}
DEFAULT = ("X", "not about flow: ESM or EMA of other constructs ('flow of daily life' etc.)")

# Found by targeted Crossref title search or by the read papers' citations;
# not in the Europe PMC or arXiv result sets.
SUPPLEMENTARY = [
    ("10.1026/0932-4089.51.3.105", "Rheinberg, Manig, Kliegl, Engeser, Vollmeyer 2007", "Flow bei der Arbeit, doch Glück in der Freizeit", Q, "ESM, Flow Short Scale and happiness/satisfaction at each signal, 101 employees, 4603 reports; READ"),
    ("10.1007/s10902-014-9586-4", "Engeser, Baumann 2014/2016", "Fluctuation of Flow and Affect in Everyday Life", Q, "ESM, Flow Short Scale and PANAVA affect at each signal, 100 employees, 4504 reports; concurrent and lagged; READ"),
    ("10.1348/096317908x357903", "Fullagar, Kelloway 2009", "Flow at work: An experience sampling approach", Q, "ESM flow and mood among architecture students (as Engeser and Baumann report it)"),
    ("10.1026//0932-4089.45.4.176", "Schallberger, Pfister 2001", "Flow-Erleben in Arbeit und Freizeit", Q, "ESM, flow more frequent at work, happiness higher in leisure (as Rheinberg et al. 2007 report it)"),
    ("10.1007/s10902-008-9113-6", "Ceja, Navarro 2009", "Dynamics of Flow: A Nonlinear Perspective", U, "ESM flow at work; affect relation not checked"),
    ("10.1037/ocp0000039", "Rivkin, Diestel, Schmidt 2018", "Which daily experiences can foster well-being at work?", "X", "daily diary"),
]


def main(path):
    hits = json.load(open(path))
    print("decision\tid\tyear\tsource\ttitle\treason")
    tally = {}
    for r in hits:
        k = r.get("doi") or r.get("id")
        d, why = DECISIONS.get(k, DEFAULT)
        tally[d] = tally.get(d, 0) + 1
        print(f"{d}\t{k}\t{r.get('pubYear')}\t{r.get('source')}\t{r.get('title')}\t{why}")
    for k, who, title, d, why in SUPPLEMENTARY:
        tally["supp-" + d] = tally.get("supp-" + d, 0) + 1
        print(f"{d}\t{k}\t\tsupplementary\t{who}: {title}\t{why}")
    print("# tally\t" + "\t".join(f"{k}={v}" for k, v in sorted(tally.items())), file=sys.stderr)


if __name__ == "__main__":
    main(sys.argv[1])
