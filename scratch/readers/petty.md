# Reader notes: petty (Petty, van Steenkiste, Linzen 2024, arXiv 2409.04556)

## Copy located
- arXiv abs/HTML/PDF, v2 (25 Feb 2025), fetched 2026-11-19, HTTP 200, no check. Reading the PDF text.

## Read in full (pp. 1-12 body, App. A-C pp. 21-22; references skimmed)
- Two settings: competitive (Ntotal = 132B fixed, code 0-90%) and additive (Nlang = 132B fixed, code 0-50%, Ntotal up to 264B) plus language-only baselines of matched total size for each additive mixture.
- Order never varied: Fig. 1 caption "these sequences are shuffled during training, so models see code and language data at the same time."
- 374M decoder-only, t5x, 5 seeds per (mixture, setting). Text says 12-layer (s4.1) but App. A says nlayers = 24: internal inconsistency.
- Results: code helps COGS/COGS-vf (structural COGS-vf beta 0.147 comp / 0.165 add; language-only baseline beta -0.048), not via well-formedness; arithmetic up (inverted U in competitive, peak 40-50%); hurts Passivization, Common Morpheme, Fantasy Reasoning, General Knowledge; Implicatures additive beta +0.006 (not a harm).
- Permutation test: only variance (p=0.0002) and upper quartile (p~0.005) significant; mean diff p=0.1038, yet Discussion says aggregate improvement "at a statistically-significant level". Inconsistent.
- App. C.1: "code-pretraining does not help a model reach higher performance ... faster" -> directly relevant to the "cheaper later learning" lead.
- Doubt: arXiv listing abstract swaps the settings' definitions vs the PDF v2 abstract/body.

## Bearings searched
- Read CLAIM-756, QUESTION-039, TERM-131, THEORY-tmpk9cmk, THEORY-tmpd6l4a, THEORY-tmp0lbb1, LEAD-tmpjdtrl. Grep also surfaced THEORY-293/809 (fact capacity vs mixing ratio), THEORY-794 (combination diversity, vision), TERM-117, CLAIM-758.
- No LIT for 2409.04556 in the record yet; the only characterization is the caller's (accurate on proportion-not-order; settings correctly named).
- Main verdict for the lead: no order manipulation, no measure of later NL learning cost; it is a co-training mixture study. App. C.1 (fine-tuning speed unchanged by code) is the closest it comes to "cheaper later learning", and it is negative.
- Quotes rechecked by grep against the pdftotext file; all present.
