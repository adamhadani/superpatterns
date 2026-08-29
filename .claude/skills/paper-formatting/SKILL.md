---
name: paper-formatting
description: Use when writing or editing a math/CS paper as Markdown that is built to PDF with pandoc + xelatex (or when the PDF has overlapping text, overfull lines, unreadable tables, or literal [@citations]). Covers the build setup (defaults.yaml, references.bib, Makefile with an overfull-box check), how to write tables/equations/long strings so they never overflow, and how to verify the PDF visually.
---

# Paper formatting (Markdown → pandoc → xelatex)

## Build setup (do this once per paper directory)

1. `references.bib` — every citation as a BibTeX entry. In the Markdown cite with `[@Key]`, `[@Key, Thm 1]`, `@Key`.
   **Never hand-type a reference list**; end the document with
   ```
   # References

   ::: {#refs}
   :::
   ```
2. `defaults.yaml` (pandoc defaults file) — pins engine, citeproc, bib, geometry, fonts, header packages.
   Template (copy from `output/paper/defaults.yaml`):
   ```yaml
   from: markdown+tex_math_dollars+pipe_tables+raw_tex
   pdf-engine: xelatex
   citeproc: true
   bibliography: references.bib
   csl: springer-basic-brackets.csl   # numeric [n] citations
   number-sections: true
   variables:
     fontsize: 11pt
     geometry: margin=1in
     colorlinks: true
     link-citations: true
     header-includes:
       - \usepackage{microtype}
       - \usepackage{amsthm}
       - \setlength{\emergencystretch}{3em}
       - \usepackage[htt]{hyphenat}
       - \allowdisplaybreaks
   ```
   Do **not** add `breakurl` (pdflatex-only) or redefine `\texttt` with `seqsplit` under xelatex — both broke the build.
3. `Makefile` with two targets: `pdf` (`pandoc -d defaults.yaml paper.md -o paper.pdf`) and `check`, which runs
   `pandoc -s -d defaults.yaml paper.md -o build.tex` (**`-s` is required** — without it the .tex is a fragment and the log is garbage), compiles with `xelatex -interaction=nonstopmode` twice, and greps `Overfull \hbox` from `build.log`.
   **Goal: `make check` prints 0.** Run it after every edit; each overfull line names the paragraph's source lines in `build.tex`.

## Citations and cross-references

- **Numeric citations** (`[3]` in text, numbered bibliography): set `csl: springer-basic-brackets.csl` in `defaults.yaml` (file from https://raw.githubusercontent.com/citation-style-language/styles/master/springer-basic-brackets.csl; `ieee.csl` also works). The default (no csl) is Chicago author–year, which gives an unnumbered list that is hard to match against in-text mentions.
- **Section cross-references that are hyperlinks**: give headings explicit ids — `# The lower bound {#sec:lower}` — and refer with raw LaTeX `\S\ref{sec:lower}` (requires `raw_tex` in `from:`; pandoc emits `\label{sec:lower}` and hyperref makes it clickable). Plain `§2` is dead text and goes stale when sections move. Inside a citation locator keep the literal form: `[@EV21, §6]` means section 6 *of that paper*.
- When bulk-editing `§N` with a script, exclude the `[@Key, §N]` locators (a regex that rewrites every `§` will silently destroy them — it happened).

## Writing rules that prevent overflow

- **Tables**: pipe tables only. Put the widths in the separator row — the dash counts set relative column widths (`|:----|:--------------------|:----|`) and, if any source line is wider than 72 chars, cells wrap. Keep cells short prose or short math; put big formulas in the text and reference the section from the table ("Thm A, §2"). Add a caption with a `Table: …` line before the table. Never use grid tables for math-heavy content.
- **Display equations**: anything longer than ~70% of the line goes in `$$\begin{aligned} … \\ … \end{aligned}$$` (or `gathered`), broken at `=`/`\le`. Put `\tag{n}` outside the environment. Lists of numeric values: `gathered`, two per line.
- **Long inline math** (`$a=..., b=..., c=...$`): split into separate `$…$` pieces with words between so the line can break.
- **Digit strings / permutations / words**: write them as plain text (`7 20 13 10 …`), not `$7\,20\,13$` — math with `\,` cannot break and runs off the page. Use `$\sigma_7 =$ 7 20 13 …`.
- **Inline code**: keep `code` spans short (< 30 chars). Long expressions → math or prose. The `hyphenat[htt]` package lets `\texttt` hyphenate but not break arbitrary identifiers.
- **Proof end markers**: `$\blacksquare$` at the end of the last text line, or on its own line after a display — never appended inside a long display.
- **Section titles**: avoid math that is wide; `$k^2/2$` is fine, multi-term formulas are not.
- Escape sequences in Python edit scripts: write `\\;` / `\\,` in normal strings or use raw strings — a `\;` in a non-raw string silently doesn't match.

## Verify visually before declaring done

```
pdftoppm -r 60 -png paper.pdf pg   # then Read pg-01.png, pg-02.png, … (check title page, every table, every long equation, references)
```
Look for: literal `[@Key]` (citeproc not running), text past the right margin, tall narrow table columns, an orphan page holding one reference line. Delete `pg-*.png` afterwards.

## Reference implementation

`output/paper/` in this repo: `superpatterns-notes.md`, `defaults.yaml`, `references.bib`, `Makefile`. Build: `make pdf`; lint: `make check`.
