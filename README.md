# Superpatterns: bounds, constructions and random universality

Research notes on permutations that contain every pattern of length $k$, by **Adam Ever-Hadani**.

A permutation is a *$k$-superpattern* if it contains all $k!$ patterns of length $k$; $\mathrm{sp}(k)$ is the least
length of one. Alon conjectured that a uniform random permutation of length $(1+\varepsilon)k^2/4$ is a
$k$-superpattern with high probability, for every fixed $\varepsilon > 0$. The best published bound is
$2000\,k^2\log\log k$ ([He–Kwan 2020](https://arxiv.org/abs/1911.12878)).

## Status (10 November 2026)

**Alon's conjecture is neither proved nor disproved here.** The current evidence is that it is *false at the sharp
constant* $1/4$:

- **Proved.** Replacing a block $12$ by $21$ in any direct sum of patterns never increases the probability that a
  random permutation contains it. Consequently the pattern $2\,1\,4\,3\,\cdots$ is at least as hard as the identity:
  if $L_{21}(\sigma)$ is the largest $m$ with $\sigma \supseteq 21^{\oplus m}$, then $L_{21} \le_{st} \lfloor \mathrm{LIS}/2 \rfloor$
  and $c_{21} := \lim L_{21}(\sigma_n)/\sqrt n \le 1$.
- **Numerical, not proved.** $\mathbb{E}\lfloor \mathrm{LIS}/2\rfloor - \mathbb{E}L_{21} = (0.00113 \pm 0.00002)\sqrt n$ for
  $n = 10^3,\dots,10^8$ (1.29 million paired samples, two independent programs), i.e. $c_{21} \approx 0.99887 < 1$.
  If so, a random permutation needs length about $1.0023\,k^2/4$ to contain $2\,1\,4\,3\,\cdots$, and Alon's
  conjecture fails for $\varepsilon < 0.0023$. Larger decreasing layers show larger gaps (about $1.4\%$ for layers of
  size 12).
- **Open.** A proof that the gap is of order $\sqrt n$. The gap is an explicit sum of non-negative local terms, and
  the problem is reduced to one lemma; see [W90](experiments/w90-layered-deficit/).

An earlier version of this README (September 2026) announced proofs of universality at $Ck^2$, of the sharp
threshold for bounded-LDS classes and of $c_{21} = 1$. Those claims were withdrawn after a line-by-line audit
([memory/AUDIT-2026-11-10.md](memory/AUDIT-2026-11-10.md)); the corresponding workstreams are archived in
[experiments/archive-2026-09-unverified/](experiments/archive-2026-09-unverified/).

## Results

| Result | Statement and scope | Verification | Workstream |
|---|---|---|---|
| Deterministic lower bound | $\mathrm{sp}(k) > 1.0073\,k^2/e^2$ for all large $k$ (previous: $1.000076$) | Analytic proof; outward interval certificate | [W25](experiments/w25-asymptopia-review/) |
| Short superpatterns | $\mathrm{sp}(7) \le 23$, $\mathrm{sp}(8) \le 30$ | Exhaustive check; Lean `native_decide` | [witnesses](experiments/witnesses/) |
| Typical target | An independent uniform pattern is contained w.h.p. at $Ck^2$ for every $C > 0.4649$ | Directed MPFR certificate (512 inequalities) | [W31](experiments/w31-lookahead/) |
| Tilted grids | Contained at $(1/4+\varepsilon)k^2$ under a revisit-separation hypothesis | Proof; exact mean $\gamma_\infty = 1$ of the strip functional | [W34](experiments/w34-grid-lookahead/), [W36](experiments/w36-gamma-limit/) |
| Monotone inflations | All inflations with monotone blocks of length $\ge K\sqrt{\log k}$, simultaneously, at $(1/4+\varepsilon)k^2$ | Shared squares + Deuschel–Zeitouni lower tail | [W39](experiments/w39-shared-squares/) |
| Larger quasirandom class | All but $k!\,e^{-\Theta(k/\ln k)}$ patterns at $72k^2$ (He–Kwan's method, re-tuned; $\log\log k$ not removed) | Proof | [W9](experiments/w9-alon-threads/) |
| Repeated $21$, algorithm | Exact $O(n\log n)$ computation of $L_{21}$ | 372,249 prefix checks | [W40](experiments/w40-c21-frontier/) |
| Repeated $21$, bounds | $0.7866 \le c_{21} \le 1$ | Renewal rules (lower); block-flip theorem (upper) | [W17](experiments/w17-hammersley/), [W90](experiments/w90-layered-deficit/) |
| Block flip | $\#\{\sigma \supseteq \alpha\oplus 21\oplus\beta\} \le \#\{\sigma \supseteq \alpha\oplus 12\oplus\beta\}$ for all $\alpha, \beta, n$, with an exact formula for the difference | Proof; brute force for all $\sigma \in S_n$, $n \le 8$ | [W90](experiments/w90-layered-deficit/) |

The block-flip inequality is the size-2 transversal case of a theorem of
[Jelínek and Karpilovskij](https://arxiv.org/abs/2002.12308) (see also
[Burstein–Pantone](https://arxiv.org/abs/1402.3842)); no novelty is claimed for it. What appears to be new is its
asymptotic consequence for random permutations and its bearing on Alon's conjecture. Exact scopes, quantifiers and
withdrawn claims are in [memory/RESULTS.md](memory/RESULTS.md).

## Layout

- `experiments/wN-*/` — one folder per workstream: tools, raw outputs, `log.md` (chronology, dead ends), `proof.md`.
  Index: [experiments/README.md](experiments/README.md).
- `output/paper/` — the notes paper (Markdown → pandoc → xelatex): `superpatterns-notes.md`, and the standalone
  note `repeated-21-frontier.md`. Build with `make -C output/paper pdf`; `make -C output/paper check` must print `0`.
- `formal-verification/lean/` — Lean 4 / Mathlib: pattern containment, a verified superpattern checker with the
  $k = 7, 8$ certificates, the finite counting theorem A with its numeric certificate, finite moment inequalities,
  block splitting and Erdős–Szekeres. Nothing about random permutations containing all patterns is formalized.
- `memory/` — `SESSION-STATE.md` (current state), `RESULTS.md` (ledger), `AUDIT-2026-11-10.md`,
  `ALON-STRATEGY.md` (research plan).

## Reproduction

```sh
python3 experiments/witnesses/check_witness.py --all
python3 experiments/w25-asymptopia-review/certify_cprime.py
cd experiments/w90-layered-deficit
python3 verify_fibers.py 8                      # block-flip theorem and fibre identity, all of S_n, n <= 8
cc -O2 -o /tmp/exact_dist exact_dist.c && /tmp/exact_dist 9     # first discrepancy: one permutation at n = 9
sh run_paired.sh && python3 aggregate.py        # paired L21 / LIS batches (long)
cd ../../formal-verification/lean && lake exe cache get && lake build
```

## AI assistance disclosure

This research was developed by **Adam Ever-Hadani** with agentic AI tools (ChatGPT Codex, Claude Code, and a
multi-agent harness used in September 2026). The September multi-agent output is the part that was withdrawn; the
audit and the W90 results were produced with Claude Code and re-derived or recomputed as described in
`memory/SESSION-STATE.md`. The author takes responsibility for the mathematical claims.

## License

Code and Lean formalizations: MIT. Notes and papers: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
