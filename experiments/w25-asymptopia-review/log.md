# W25 log — Asymptopia review (2026-08-29)

## Steps
1. Read context: `memory/NOTES.md` (results ledger), `memory/SESSION-STATE.md`, W22 review (all of it),
   paper §"The lower bound", §"Random permutations", §"Towards Alon's conjecture", §"Open problems".
2. Located the book: the actual file name is `[Spencer] Asymptopia.pdf` (not the long Anna's-Archive name
   in the brief); 202 PDF pages, book page = PDF page − 18. Extracted with `pdftotext -layout` to the
   scratchpad and read the complete text (TOC pp. v–viii first, then Ch. 0–13, index).
3. Findings that shaped the review:
   - No LIS / Erdős–Szekeres / random-permutation chapter exists; no "Kinetic view"/"hypothetical reasoning"
     chapters (those are in other Spencer books). Items (2) and (5) of the brief are therefore near-empty.
   - The relevant content is Ch. 1/5/8 (Laplace method, `C(n,k)` regimes, Chernoff regimes), Ch. 7 and
     §12.2–12.4 (threshold heuristics, Poisson paradigm), §10.2 (certificate-style lower bounds).
4. The one quantitative lead: Theorem C's Poisson-type Chernoff for the slot count is in the wrong
   deviation regime (book p. 106/109). Derived Lemma B.1 (uniform Bernoulli domination via concavity of
   `s ↦ ln(1 + c(1 − x^s))`) and checked the setting against `experiments/w7-slots/proof.md` Steps 3–4
   (independent Bernoulli(`1 − x^{|A_ℓ|}`), `b−2` indicators, `Σ|A_ℓ| ≤ n−b−1`): hypotheses match.
5. Numerics (scipy via `uv run --with scipy --with numpy`, no scipy in system python):
   - `rate_bernoulli.py`: reproduced W7's `λ_C = 1.004829` (Poisson, fixed ε). Bernoulli with fixed ε gave
     `1.007756` but I then noticed the Bernoulli bad rate is not monotone in the width (tends to the Poisson
     value for wide windows), so the paper's "minimum at b = β" no longer holds: that number is NOT valid.
   - `rate_bernoulli2.py`: width-dependent ε(b) (flat bad exponent R, as W7's `rate2.py`), `c̄` recomputed as
     the minimum over widths. Poisson mode reproduces W7's `1.005007`; Bernoulli mode gives **`1.007338`**
     (`τ = 0.968, β̄ = 0.537, R = 0.0078`). Runtime ≈ 4 min each.
6. Wrote `review.md` (per-technique assessment with page references; ranked actions; dead ends).

## Caveats for the coordinator
- Lemma B.1 is my derivation, not the book's; verify it before using `1.0073` anywhere. The rest of the
  computation reuses W7's `R_good`/`s`-maximisation unchanged.
- `finite_check.py` (finite-k certificate for Theorem C) has not been rerun with the new bad term.
- Page numbers are book pages from the extracted text; equation numbers as printed.
- The book's Poisson-paradigm and clustering discussion is consistent with W22 and adds no new tool for the
  `k ln k`-per-pattern gap; I did not manufacture relevance where there is none.

## Files
- `review.md` — the review.
- `rate_bernoulli.py`, `rate_bernoulli.out` — fixed-ε comparison (Poisson reproduction; invalid Bernoulli value).
- `rate_bernoulli2.py`, `rate_bernoulli2.out` — width-dependent ε; the `1.007338` figure.
- Book text extraction: scratchpad only (not in repo).


## Review follow-up, 2026-09-10

Completed corrected C′ proof and outward Decimal certificate at coefficient 1.0073. See proof.md and cprime_certificate.json.
