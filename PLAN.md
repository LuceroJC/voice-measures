# Plan — *Acoustic Measures of Voice Quality*

The chapter plan for this reference, and the status of each chapter. Every
placeholder page in the repository links here for its intended scope.

Author: Jorge C. Lucero (University of Brasília). Text CC BY 4.0, code MIT.
Site: <https://voicemeasures.org>. Versioned DOIs on Zenodo; the concept DOI
`10.5281/zenodo.22739049` resolves to the latest release.

## Scope

Acoustic measures of voice quality: how each one is computed, what it
captures, what its reference values are, and which pipeline those values
belong to. Audience: speech-language pathologists and voice scientists.

Out of scope: general otolaryngology, surgical technique, imaging, perceptual
measures as instruments in their own right, and non-acoustic instrumentation.
Four scope decisions fix the edges:

- **DSI** is in Part IV, with its aerodynamic maximum-phonation-time term
  flagged as a scope exception in that chapter's Caveats.
- **Perceptual anchors (GRBAS, CAPE-V)** appear in Part I as reference
  entries, not as measures, because every composite in Part IV is fitted
  against them. The framing is "what the composites approximate".
- **EGG and aerodynamic measures** get one back-matter appendix covering only
  what informs acoustic interpretation.
- **Part V** ships as one landscape chapter plus two or three concrete example
  measures, not a survey.

Every chapter follows the same shape: Definition, Computation, Normative
values (with Pipeline and Class columns), Clinical interpretation, Caveats,
and Points of disagreement where sources conflict. Every factual claim traces
to a source in the companion source library before it reaches a chapter.

English first. Portuguese, and possibly Spanish, return through `babelquarto`
once the English edition is stable.

## Chapters

Published chapters are listed in `_quarto.yml` under both `project.render` and
`book.chapters`. A placeholder page exists in the repository for each planned
chapter but is neither listed nor rendered until it is written.

### Front matter

| File | Scope | Status |
|---|---|---|
| `index.qmd` | What this reference is, who it is for, current version and DOI, how to cite, how to contribute | Published |
| `intro.qmd` | How to use it: reading paths for the clinician, the researcher and the PhonaLab user; versioning and licensing | Published |

### Part I — Foundations

| File | Scope | Status |
|---|---|---|
| `foundations-signal.qmd` | Sampling, quantization, framing, windowing, spectra against cepstra, with computed figures | Published |
| `foundations-signal-typing.qmd` | Types 1 to 4. The gating chapter for every perturbation measure | Published |
| `foundations-pipeline.qmd` | Pipeline dependence and reference values: which pipeline elements change a value, the compatibility classes, and the rule of declaring absence instead of borrowing a cutoff | Published |
| `foundations-recording.qmd` | Recording protocol: microphone type and placement, mouth-to-microphone distance, signal-to-noise floor, room noise, sample rate, bit depth | Planned |
| `foundations-tasks.qmd` | Sustained vowel, connected speech, maximum phonation time, glissando. What each task supports and blocks | Planned |
| `foundations-f0-detection.qmd` | Pitch extraction methods and where each fails; what Praat and PhonaLab do | Planned |
| `foundations-perceptual-anchors.qmd` | GRBAS and CAPE-V as reference standards: rating protocols, rater reliability, and why a cutoff validated against one is not validated against the other | Next |

### Part II — Periodicity and stability

| File | Scope | Status |
|---|---|---|
| `jitter.qmd` | Local, absolute, RAP, PPQ5, DDP. Formulas, conventions across programs, sensitivity to signal typing | Published |
| `shimmer.qmd` | Local, local dB, APQ3, APQ5, APQ11, DDA | Published |
| `f0-measures.qmd` | Mean F0, F0 standard deviation and F0 range as clinical measures rather than as preprocessing. Sex and age norms, task effects | Next |
| `voice-breaks.qmd` | Number and degree of voice breaks, and how the definitions vary across programs | Planned |
| `perturbation-caveats.qmd` | Why Type 2 and above break every perturbation measure. Shared cautions, so each measure chapter stays focused | Planned |

### Part III — Noise and harmonic structure

| File | Scope | Status |
|---|---|---|
| `hnr.qmd` | Harmonics-to-noise ratio: time-domain, autocorrelation and cepstrum-based definitions | Published |
| `gne.qmd` | Glottal-to-noise excitation ratio, and its robustness to signal typing | Published |
| `cpps.qmd` | Cepstral peak prominence and its smoothed variant | Published |
| `nhr.qmd` | Noise-to-harmonic ratio, chiefly the MDVP variant. What it measures that HNR does not | Planned |
| `spectral-tilt.qmd` | Spectral slope, L1–L2, H1–H2, H1–A1, H1–A3. Breathy against pressed, and first-formant correction | Published in part: H1–H2 |

### Part IV — Composite indices

| File | Scope | Status |
|---|---|---|
| `avqi.qmd` | Acoustic Voice Quality Index, versions 02.06 and 03.01 | Published |
| `abi.qmd` | Acoustic Breathiness Index | Published |
| `dsi.qmd` | Dysphonia Severity Index. The aerodynamic term is flagged as a scope exception | Planned |
| `composite-caveats.qmd` | Cross-language validation, why thresholds drift, how the composites relate, and what external validation means | Planned |

### Part V — Model-derived measures

| File | Scope | Status |
|---|---|---|
| `ml-landscape.qmd` | Feature-based against end-to-end; training-data provenance; interpretability; validation standards. A framing chapter, not a survey | Planned |
| `ml-feature-based.qmd` | One representative example | Planned |
| `ml-end-to-end.qmd` | One representative example | Planned |

### Back matter

| File | Scope | Status |
|---|---|---|
| `release-notes.qmd` | Release notes and errata. Corrections are never made silently | Published |
| `appendix-adjunct-methods.qmd` | EGG and aerodynamic measures where they inform acoustic interpretation. A lookup, not a chapter | Planned |
| `appendix-reproducibility.qmd` | Script pointers, computation notes, known differences between programs per measure | Planned |
| `appendix-glossary.qmd` | Terms of art with brief definitions and cross-links | Planned |

## Build order

Two constraints set the order. Signal typing and pipeline dependence gate
every measure chapter, so they came first. After that, a chapter is written
when the sources behind it are in the library, not when its turn arrives in
the table of contents.

Released so far: v0.1.0 and v0.1.1 (front matter, the three Foundations
chapters, AVQI, ABI, CPPS), v0.2.0 (jitter, shimmer, HNR), v0.3.0 (GNE, plus
corrections to v0.2.0). See `release-notes.qmd`.

Remaining, in intended order:

1. The rest of Part I: perceptual anchors, then recording, tasks and F0
   detection.
2. The rest of Part II: F0 measures, voice breaks, perturbation caveats.
3. The rest of Part III: NHR, and spectral tilt beyond H1–H2.
4. The rest of Part IV: DSI and composite caveats.
5. Part V: the landscape chapter first, then the two examples.
6. Back matter.

A machine-readable measure registry runs alongside the chapters rather than
after them, emitting the normative tables and their JSON records from one
source so that a chapter and its machine record cannot disagree.

## What a chapter needs before it can be written

At least one source in the companion library, with a full citation record, for
every claim the chapter will make. A chapter is not started on the strength of
what its author remembers about the measure.
