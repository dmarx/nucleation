---
status: Read
paper: LIT-944
title: 'Kumar, Clune, Lehman and Stanley — The Fractured Entangled Representation Hypothesis'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv PDF (arxiv.org/pdf/2505.11581, v1 of
    2025-05-16, the only version, 43 pp.), text extracted with pdftotext:
    §§1–8 and Appendices A (NEAT, CPPNs, Picbreeder), B (layerization), C
    (SGD training), D (butterfly and apple), E (ReLU networks) and F
    (change of basis). The paper's evidence is images of neuron
    activations and weight sweeps, with no text layer, so what they show
    was read from captions and text. The released sweeps database was not
    examined.
date: '2026-10-14'
summary: >-
  For three images found by Picbreeder's human-guided evolution (skull,
  butterfly, apple), SGD in the same layerized architecture reproduces
  the image from random weights, but its neurons show no reuse of the
  symmetric parts, and sweeping its weights distorts the image where
  sweeping the evolved network's weights varies it meaningfully. This
  holds in a PCA basis, along random weight directions, and in ReLU
  networks. The evidence is qualitative and curated; the attribution to
  open-ended search is conjecture.
---
<!-- inactive-ok-file: THEORY-197 THEORY-206 THEORY-210 THEORY-112 THEORY-230 THEORY-117 THEORY-tmp37j6t — Proposed; the accounts this reading bears on, and the one filed from it -->

# NOTE-tmp8icvu: Kumar, Clune, Lehman and Stanley — The Fractured Entangled Representation Hypothesis

## Contribution

A position paper. It shows side by side, for the first time by its own
account, the internal representation of a network evolved in Picbreeder
and of a network of the same architecture trained by SGD to produce the
same image. It names what the SGD network does "fractured entangled
representation" (FER) and what the evolved network approaches "unified
factored representation" (UFR). It argues that FER may also be present
in large models and may harm generalisation, creativity and continual
learning.

## Key insight

The objective is satisfied by a whole set of networks, and the outputs
cannot tell them apart. Some reuse one computation for every instance of
a regularity and keep independent aspects in separate parts. Others build
the same output from many unrelated pieces. Which one training finds
depends on the path it takes: Picbreeder found symmetry before it found
the skull, and SGD went straight at the skull.

## Assumptions

- **The networks.** CPPNs map a pixel's (x, y, d, 1), with
  d = 1.4√(x² + y²), to (h, s, v). The image over the whole grid is the
  network's entire input–output function, so "same image" means "same
  function on the grid".
- **Layerization (App. B).** The evolved NEAT graph is rewritten as a
  dense MLP that computes exactly the same function. Skip connections
  become chains of identity neurons, and each neuron keeps its activation
  (identity, sin, cos, tanh, sigmoid, Gaussian).
- **The SGD comparison (App. C).** Same layerized architecture and
  activations, LeCun-normal initialisation, full batch of 256 × 256
  pixels, MSE, 100,000 iterations, learning rate 3 × 10⁻³ (3 × 10⁻⁴ for the
  apple). The optimiser is called SGD and not further specified.
- **SGD needs the layerized form.** On the raw NEAT architecture SGD fails
  for all three seeds shown (Fig. 12). So the comparison is in a space
  that contains the evolved solution but is much denser than the one it
  was found in.
- **"Conventional SGD"** means SGD on a fixed architecture with a single
  fixed objective. The authors say FER is likely under any
  single-objective optimiser, and need not occur under every use of SGD.

## Key results

- **Same output (Fig. 4, Fig. 13).** SGD reproduces the skull, butterfly
  and apple, called "effectively identical", with smooth loss curves.
- **Different internals (Fig. 5, Figs. 14–15, 18–19).**
  - The Picbreeder skull is y-symmetric from early layers. Its layerized
    form has only 24 novel feature maps, with distinct neurons for the
    outline, eyes, nose and mouth.
  - The SGD skull does not represent the two sides as symmetric until the
    output layer, across all 12 layers, and has many high-frequency maps.
  - The butterfly and apple show the same contrast. The evolved apple
    separates background, body and stem; the SGD apple mixes them.
- **Weight sweeps (Fig. 6, Fig. 16, Fig. 20).** Each weight is varied over
  [−1, 1].
  - In the Picbreeder skull, single weights open the mouth, wink an eye,
    or widen the eyes or the jaw, keeping a skull. One apple weight swings
    the stem.
  - In the SGD networks, sweeps give "meaningless distortions" that break
    the symmetry.
  - The shown sweeps were selected to present "both methods ... in their
    best light, while ... broadly representative". All sweeps are
    released.
- **Not a change of basis (App. F).**
  - In a PCA basis, the SGD skull looks "slightly" less fractured but
    nowhere near the evolved one (Fig. 24).
  - Sweeping a random column of a weight matrix along a random unit vector
    is equivalent to sweeping one weight after a random orthonormal change
    of basis. These sweeps still differ in kind between the two networks
    (Fig. 25).
- **ReLU networks (App. E).** Standard ReLU MLPs trained on the three images
  also show FER (Figs. 21–23).
- **Paths (Fig. 8, Fig. 17).** The skull's Picbreeder ancestors acquired
  left–right symmetry between iterations 20 and 36, and a face before a
  skull. SGD's intermediate images approach the skull directly, over
  10,000 iterations.
- **Behavioural hints in large models (§5.1).** Anecdotes:
  - GPT-3 counts nine office supplies correctly and the same numbers of
    birds as ten (3/3 trials each);
  - GPT-4o replaces numbers at given positions but not words (3/3);
  - GPT-4o's image model draws a man's hand with one extra thumb but not
    an ape's.
  It also cites reports of heuristic bags in OthelloGPT and in LLM
  arithmetic.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Networks of one architecture computing the same image can differ radically in internal organisation | moderate | three images, one SGD run each shown; qualitative neuron maps and sweeps |
| C2 | The difference is not a change of basis | moderate | PCA basis and random-direction sweeps, App. F |
| C3 | SGD on a single target produces FER | weak to moderate | three targets in one architecture family plus ReLU MLPs; no measure of FER |
| C4 | Open-ended search, through its order of discovery, produces UFR | weak | Picbreeder ancestries; Woolley & Stanley (2011) cited for objective-driven NEAT being bloated; untested here |
| C5 | Large models exhibit FER | weak | behavioural anecdotes and cited interpretability reports |
| C6 | FER harms generalisation, creativity and continual learning | weak | argument by analogy; the sweeps are the only evidence offered for creativity |

## Concepts

- **Fractured.** Information about one concept is split into disconnected
  pieces that are invoked separately in different contexts, so the
  pieces are redundant.
- **Entangled.** Behaviours that should be independent influence each
  other.
- **UFR.** One unbroken function for each capability (unified) and
  independent capabilities kept apart (factored), "a modular decomposition
  of the desired behavior". Offered as an ideal.
- **Representational optimism.** The implicit view that scaling data and
  compute makes internal representations good.
- **Imposter intelligence.** A system whose whole input–output behaviour
  is right while its internal representation is FER.

## Connections

The paper builds on Picbreeder (Secretan et al. 2008, 2011), CPPNs
(Stanley 2007), NEAT (Stanley and Miikkulainen 2002) and Huizinga, Stanley
and Clune (2018), which first showed meaningful weight sweeps in
Picbreeder CPPNs as evidence of canalisation and evolvability. Woolley and
Stanley (2011) found that NEAT driven to Picbreeder images as fixed
objectives gives bloated networks. On grokking it cites Nanda et al.
(2023), where generalisation includes a "cleanup" of memorising circuits.

## Bearing on the record

- **[QUESTION-060](../questions.d/QUESTION-060.md)** asks whether the learned variables are fixed by
  the objective or by what the architecture represents cheaply. Here both
  are held fixed: the same function on the grid, the same layerized
  architecture. The internal variables still differ radically. So neither
  fixes them, and the training path is a third determinant. [LIT-944](../literature.d/LIT-944.md)'s
  filing note said the paper shows "two training processes reaching
  one output with very different internal variables" and concludes "the
  objective does not fix the learned variables". That is accurate, with
  one precision: the evolved network was never trained on the image
  objective. Picbreeder users selected it with no target, and the image
  was then made the SGD target. So the comparison is between an
  objective-trained network and one that was not, not between two
  objectives.
- **[THEORY-197](../theory.d/THEORY-197.md)** holds that the objective, not the formal match,
  fixes what an RBM keeps. Kumar et al. add a case where the objective is
  satisfied exactly and still leaves the internal variables open, so
  [THEORY-197](../theory.d/THEORY-197.md)'s lesson reads "the objective constrains what is kept", not
  "the objective determines it".
- **[THEORY-206](../theory.d/THEORY-206.md)** concerns what an architecture can represent at what
  size. Here SGD failed in the sparse NEAT architecture that contains the
  UFR solution and succeeded only in a denser one. That is a case where
  the representable is not the reachable.
- **[THEORY-210](../theory.d/THEORY-210.md) and [THEORY-112](../theory.d/THEORY-112.md)** concern solutions that differ by
  a parameter symmetry. App. F argues the FER/UFR difference is not one:
  random-direction sweeps are basis-agnostic. The CPPN's mixed
  elementwise activations leave little continuous symmetry. So this is a
  difference between solutions not related by a symmetry, and the
  symmetry results do not cover it.
- **[THEORY-230](../theory.d/THEORY-230.md)** proves that two models with identical outputs can have
  different hidden geometries, through a GL(d) gauge. Kumar et al. give an
  empirical case beyond a gauge. The two together say that output
  identity fixes neither hidden geometry nor decomposition.
- **[THEORY-117](../theory.d/THEORY-117.md)** finds that compositional generalisation comes from
  diversity of combinations. The paper's §6.3 asks whether many skulls
  would unify the representation, the same question for a different
  target. It is not run.
- **Filed from this reading:** [THEORY-tmp37j6t](../theory.d/THEORY-tmp37j6t.md), the same-function,
  different-decomposition finding at the strength shown.
- The paper's suggestions to explore curricula, open-ended training, MoE,
  pruning and modified SGD are machine-learning practice and belong to the
  anthology.

## Limitations

- **No measure of FER or UFR.** The evidence is visual inspection of
  neuron maps and selected sweeps. The paper's one number, 24 novel maps
  in the layerized skull, is not given for the SGD skull.
- **Three images, curated.** The Picbreeder networks are celebrated finds
  of a large human search, chosen in part because their representations
  had already been shown to be good (Huizinga et al. 2018). Each is
  compared with an SGD network on one seed.
- **Unequal footing.** SGD could not train in the evolved architecture.
  The evolved network's weights were also selected for how they vary under
  mutation, which is what the sweeps test.
- **Scale.** The bridge from CPPNs to LLMs is analogy plus anecdote. The
  authors say "the simple demonstrations in this paper do not fully
  illuminate all these issues".
- **Cause.** That the order of discovery, rather than NEAT's growth or
  human selection, produces UFR is argued, not tested. The authors say the
  importance of NEAT "is not currently well understood".

## Open questions

- A quantitative measure of fracture and entanglement, compared across
  seeds, optimisers and architectures.
- The many-skulls experiment of §6.3: whether training on many related
  targets moves SGD from FER to UFR, gradually or abruptly.
- Whether SGD with an imposed curriculum (symmetry first) reaches UFR,
  which would separate the order of discovery from the search algorithm.
