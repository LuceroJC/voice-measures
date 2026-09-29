# Acoustic Measures of Voice Quality — A Living Reference

An open, versioned reference on the computation and clinical interpretation of
acoustic measures of voice quality, for speech-language pathologists and voice
scientists. Every reference value is reported with the pipeline that produced
it (software, version, settings, task, language) and a compatibility class.

Site: https://voicemeasures.org

Text under CC BY 4.0, code under MIT. Built with [Quarto](https://quarto.org).

Competing interests: the author also develops
[PhonaLab](https://phonalab.com), a commercial voice-analysis application.
The reference is independent of it (see the Introduction).

## Repository layout

```
_quarto.yml Project config: rendered chapters, sidebar, theme
index.qmd Home page (release contents, roadmap, citation)
intro.qmd Scope, reading paths, competing interests, licence
foundations-*.qmd Part I chapters
cpps.qmd, avqi.qmd, ... Measure chapters
_code/vmsynth.py Plot style and signal helpers for the figures
_freeze/ Cached results of executed code cells (commit it)
analytics.html Analytics beacon injected into every page's <head>
references.bib Bibliography
CITATION.cff Citation metadata (GitHub "cite" widget)
.zenodo.json Zenodo deposition metadata
.github/workflows/ CI: render and publish to the gh-pages branch
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

## Custom domain setup

The site is served from `voicemeasures.org`, with DNS on Cloudflare. Kept here
for reference and for any future domain change.

**DNS records** (Cloudflare, DNS-only — proxy off — so GitHub Pages serves
HTTPS directly):

- `voicemeasures.org` CNAME → `lucerojc.github.io`
  (Cloudflare flattens the apex CNAME; on registrars that don't, use A
  records to GitHub Pages' four IPs — check GitHub's Pages docs for the
  current addresses.)
- `www.voicemeasures.org` CNAME → `lucerojc.github.io`

**Anti-spoofing DNS** (the domain sends no mail):

- `voicemeasures.org` MX → `0 .` (RFC 7505 null MX)
- `voicemeasures.org` TXT → `v=spf1 -all`
- `_dmarc.voicemeasures.org` TXT → `v=DMARC1; p=reject; adkim=s; aspf=s`
- `*._domainkey.voicemeasures.org` TXT → `v=DKIM1; p=`

**Repository and GitHub Pages:**

1. A file named `CNAME` at the repository root contains the domain, and it
   is listed under `project.resources` in `_quarto.yml` so each publish
   copies it to `gh-pages`:
```yaml
   project:
     resources:
       - CNAME
```
2. In GitHub **Settings → Pages**, the custom domain is set and
   **Enforce HTTPS** is ticked.
3. `_quarto.yml` (`site-url`), `CITATION.cff` (`url`), `index.qmd` and
   `intro.qmd` all carry the custom domain.

GitHub redirects the old `lucerojc.github.io/voice-measures` links to the
custom domain.

## Release checklist

For each release:

1. Working tree clean, with the release content pushed to `main` and CI
   green.
2. `CITATION.cff`: bump `version` and `date-released`.
3. Commit and push those.
4. Tag the release commit (`git tag -a vX.Y.Z -m "..."` then
   `git push origin vX.Y.Z`) and cut a **GitHub Release** from the tag.
   Zenodo archives the tarball and mints a new versioned DOI under the
   existing concept DOI.
5. Add the new versioned DOI to `CITATION.cff` (`identifiers:` block). The
   concept DOI in `_quarto.yml`, `index.qmd` and `intro.qmd` does not
   change — it always resolves to the latest release.
6. Update `CHANGELOG.md` (if kept) with the release notes and both DOIs.

v0.1.0 (2026-09-29): concept DOI
[10.5281/zenodo.22739049](https://doi.org/10.5281/zenodo.22739049),
version DOI [10.5281/zenodo.23045678](https://doi.org/10.5281/zenodo.23045678).

## Privacy


This site uses [Cloudflare Web Analytics](https://www.cloudflare.com/web-analytics/)
to count aggregate page views. It uses no cookies, sets no tracking
identifiers, and collects no personal data — no cookie banner is shown.


## Adding Portuguese / Spanish later

English-first is intentional. When ready, use the `babelquarto` workflow
(https://docs.ropensci.org/babelquarto/).