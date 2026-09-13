# Acoustic Measures of Voice Quality — A Living Reference

An open, versioned reference on the computation and clinical interpretation of
acoustic measures of voice quality. Methods companion to
[PhonaLab](https://phonalab.com).

Built with [Quarto](https://quarto.org). Text under CC BY 4.0, code under MIT.

## Repository layout

```
_quarto.yml              Project config (chapters, formats, theme)
index.qmd                Preface (what this is, how to cite, license)
intro.qmd                Scope and organization
foundations-signal.qmd   Part I stub — includes a runnable code cell
avqi.qmd                 Part IV stub — per-measure chapter template
references.bib           Bibliography
theme.scss               Custom styling
requirements.txt         Python deps for executable examples
.github/workflows/       CI: render + publish to GitHub Pages
CITATION.cff             Citation metadata (GitHub "cite" widget)
.zenodo.json             Zenodo deposition metadata
LICENSE-CODE / -TEXT     MIT (code) and CC BY 4.0 (prose)
```

## Build locally

Install Quarto (https://quarto.org/docs/get-started/) and the Python deps:

```bash
pip install -r requirements.txt
quarto preview          # live preview in the browser
quarto render           # full build into _book/
quarto render --to pdf  # build the PDF only
```

If `foundations-signal.qmd` renders with its figure, the executable pipeline
works.

## Fill in these placeholders before your first release

1. **Repo name / GitHub username** — this scaffold assumes
   `github.com/lucerojc/voice-measures`. Change `repo-url` in `_quarto.yml`,
   and the URLs in `CITATION.cff`, if different.
2. **ORCID** — uncomment and fill in `_quarto.yml` and `CITATION.cff`.
3. **CC BY 4.0 full text** — paste the legal code into `LICENSE-TEXT`
   (see the TODO in that file).
4. **DOI** — after the first Zenodo release, add it to `index.qmd` and
   uncomment `doi:` in `_quarto.yml`.

## One-time activation (do this on the empty scaffold, before writing content)

1. Create the GitHub repo and push this scaffold to the `main` branch.
2. Push once. The Action renders and creates a `gh-pages` branch.
3. In **Settings → Pages**, set the source to the `gh-pages` branch (root).
   Your site goes live at `https://<username>.github.io/<repo>/`.
4. Link the repo to **Zenodo** (https://zenodo.org, log in with GitHub, flip the
   toggle for this repo). From then on, every GitHub *release* is automatically
   archived and minted a DOI.
5. Cut a `v0.0.1` release to confirm the Zenodo hook fires end-to-end on the
   stub, then add the DOI to `index.qmd`.

Proving all five steps on the stub — before there is real content — means that
when you finish the AVQI chapter it publishes and archives with zero friction.

## Adding Portuguese / Spanish later

English-first is intentional; don't restructure now. When ready, use the
`babelquarto` workflow (https://docs.ropensci.org/babelquarto/). Nothing here
blocks it.
