# Acoustic Measures of Voice Quality — A Living Reference

An open, versioned reference on the computation and clinical interpretation of
acoustic measures of voice quality, for speech-language pathologists and voice
scientists. Every reference value is reported with the pipeline that produced
it (software, version, settings, task, language) and a compatibility class.

Site: https://lucerojc.github.io/voice-measures

Text under CC BY 4.0, code under MIT. Built with [Quarto](https://quarto.org).

Competing interests: the author also develops
[PhonaLab](https://phonalab.com), a commercial voice-analysis application.
The reference is independent of it (see the Introduction).

## Repository layout

```
_quarto.yml              Project config: rendered chapters, sidebar, theme
index.qmd                Home page (release contents, roadmap, citation)
intro.qmd                Scope, reading paths, competing interests, licence
foundations-*.qmd        Part I chapters
cpps.qmd, avqi.qmd, ...  Measure chapters
_code/vmsynth.py         Plot style and signal helpers for the figures
_freeze/                 Cached results of executed code cells (commit it)
references.bib           Bibliography
CITATION.cff             Citation metadata (GitHub "cite" widget)
.zenodo.json             Zenodo deposition metadata
.github/workflows/       CI: render and publish to the gh-pages branch
```

Planned chapters exist as placeholder `.qmd` files. They are neither listed in
the sidebar nor rendered. To publish one, add it to **both**
`project.render` and `book.chapters` in `_quarto.yml`.

## Build locally

```bash
pip install -r requirements.txt
quarto preview          # live preview in the browser
quarto render           # full build into _book/
```

## Custom domain (when purchased)

1. At the registrar, point the domain to GitHub Pages. For an apex domain,
   add A records to 185.199.108.153, 185.199.109.153, 185.199.110.153 and
   185.199.111.153. For a `www` or other subdomain, add a CNAME record to
   `lucerojc.github.io`. Check GitHub's current Pages documentation for these
   addresses before entering them.
2. Add a file named `CNAME` at the repository root containing only the domain,
   and list it under `project.resources` in `_quarto.yml` so each publish
   copies it to `gh-pages`:
   ```yaml
   project:
     resources:
       - CNAME
   ```
3. In GitHub **Settings → Pages**, enter the custom domain and tick
   **Enforce HTTPS** once the certificate is issued.
4. Update the address in `_quarto.yml` (`site-url`), `CITATION.cff` (`url`),
   `index.qmd` and `intro.qmd` (citation examples).

GitHub redirects the old `lucerojc.github.io/voice-measures` links to the
custom domain.

## Release checklist (v0.1)

1. Custom domain live, and the address updated everywhere (above).
2. `CITATION.cff`: `version` and `date-released`.
3. Cut a GitHub release. Zenodo archives it and mints the DOI.
4. Add the DOI to `_quarto.yml` (`doi:`), `index.qmd` and `intro.qmd`.

## Adding Portuguese / Spanish later

English-first is intentional. When ready, use the `babelquarto` workflow
(https://docs.ropensci.org/babelquarto/).
