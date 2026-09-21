# Quarto staging (updated 2026-09-21)

Files here are ready to drop into the `voice-measures` repo
(github.com/LuceroJC/voice-measures). This is Phase 1 of the book plan:
the front matter, the two Foundations chapters that gate every subsequent
measure entry, and a full-TOC `_quarto.yml` with placeholders for every
planned chapter so the sidebar shows the roadmap.

## What's here

### Ready chapters (full-length)

| File | Status | Action |
|---|---|---|
| `index.qmd` | new landing page | REPLACE existing scaffold if any |
| `intro.qmd` | full front matter | REPLACE scaffold stub |
| `foundations-signal.qmd` | Foundations — signal fundamentals | REPLACE scaffold stub |
| `foundations-signal-typing.qmd` | Foundations — gating chapter (Titze 1995 signal typing) | NEW |
| `cpps.qmd` | Part III | already staged 2026-09-20 |
| `avqi.qmd` | Part IV | already staged 2026-09-20 |
| `abi.qmd` | Part IV | already staged 2026-09-20 |
| `_quarto.yml` | full 5-part TOC | REPLACE |
| `references.bib` | 8 journal entries + 8 book entries (Baken, Kreiman, Kent-Read, Hirano, Rabiner, Ludlow-Kent-Gray, Titze × 2) | REPLACE |

### Placeholder chapters

Every chapter in the book plan has a placeholder .qmd file so the Quarto
sidebar shows the full roadmap. Each placeholder carries a callout stating
that the chapter is planned but not yet written, and links back to the
Introduction. The placeholders are:

- Part I: `foundations-recording.qmd`, `foundations-f0-detection.qmd`,
  `foundations-tasks.qmd`, `foundations-perceptual-anchors.qmd`
- Part II: `f0-measures.qmd`, `jitter.qmd`, `shimmer.qmd`,
  `voice-breaks.qmd`, `perturbation-caveats.qmd`
- Part III: `hnr.qmd`, `nhr.qmd`, `gne.qmd`, `spectral-tilt.qmd`
- Part IV: `dsi.qmd`, `composite-caveats.qmd`
- Part V: `ml-landscape.qmd`, `ml-feature-based.qmd`, `ml-end-to-end.qmd`
- Back matter: `appendix-adjunct-methods.qmd`,
  `appendix-reproducibility.qmd`, `appendix-glossary.qmd`

## To publish (in WSL)

```bash
cd ~/voice-measures
cp /mnt/c/Users/lucer/Dropbox/Voice/voice-analysis-kb/quarto-staging/*.qmd .
cp /mnt/c/Users/lucer/Dropbox/Voice/voice-analysis-kb/quarto-staging/_quarto.yml .
cp /mnt/c/Users/lucer/Dropbox/Voice/voice-analysis-kb/quarto-staging/references.bib .
quarto render        # optional local check
git add -A && git commit -m "Phase 1: intro + Foundations signal & signal-typing + full TOC skeleton" && git push
```

CI publishes to LuceroJC.github.io/voice-measures on push to main.

## Provenance

- Content is transposed from the KB wiki entries — the two Foundations
  chapters draw from `wiki/concepts/signal-fundamentals.md` and
  `wiki/concepts/signal-typing.md`, where every claim carries a citation
  slug into `raw/` with page anchors. The intro and index pages carry no
  factual claims that require slugs.
- New BibTeX entries were added for the five Tier 1 books ingested
  2026-09-21 (Baken-Orlikoff, Kreiman-Sidtis, Kent-Read, Hirano,
  Rabiner-Schafer), for Ludlow-Kent-Gray (ingested 2026-09-21), and for
  Titze 2000 *Principles of Voice Production* and the Titze 1995 NCVS
  workshop report.
- The `citation-slug` schema in the wiki entries maps to `@citekey`
  BibTeX citations in the Quarto chapters. The mapping for this batch:
  `baken-orlikoff-clinical-measurement` → `@baken2000clinical`,
  `kreiman-sidtis-foundations-voice-studies` → `@kreiman2011foundations`,
  `kent-read-acoustic-analysis-speech` → `@kent2002acoustic`,
  `hirano-clinical-examination-voice` → `@hirano1981clinical`,
  `rabiner-schafer-digital-speech-processing` → `@rabiner2011theory`,
  `ludlow-kent-gray-measuring-voice` → `@ludlow2018measuring`,
  `titze-principles-voice-production` → `@titze2000principles`,
  Titze 1995 workshop → `@titze1995workshop`.

## Open items

- Same open items as the 2026-09-20 staging carry over (AVQI coefficient
  discrepancy, ABI meta-analysis Table 1, ingest Maryn 2010 + Barsties
  2017 development papers).
- Rendering has not been re-verified against the repo `main` after this
  batch. Please run `quarto render` locally before pushing.
- Placeholder chapters render but the sidebar will show a lot of
  "placeholder" callouts until they are filled in over the coming
  phases. That is intentional — it shows readers the roadmap.
