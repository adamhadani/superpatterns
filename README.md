# Superpatterns: bounds, constructions and random universality

Research notes on permutations that contain every pattern of length $k$, by **Adam Ever-Hadani**.

A permutation is a *$k$-superpattern* if it contains all $k!$ patterns of length $k$; $\mathrm{sp}(k)$ is the least
length of one. Alon conjectured that a uniform random permutation of length $(1+\varepsilon)k^2/4$ is a
$k$-superpattern with high probability, for every fixed $\varepsilon > 0$. The best published bound is
$2000\,k^2\log\log k$ ([He–Kwan 2020](https://arxiv.org/abs/1911.12878)); a preprint of October 2026
([Chen–Wang, arXiv:2610.13530](https://arxiv.org/abs/2610.13530), not yet refereed) announces $32k^2$.

## Status (10 November 2026)

**Claim, with a complete written proof that has not yet been checked by a human specialist: Alon's conjecture is
false at the sharp constant $1/4$.** For small fixed $\varepsilon > 0$, a uniform random permutation of length
$(1+\varepsilon)k^2/4$ fails, with probability tending to 1, to contain the pattern $2\,1\,4\,3\cdots k\,(k-1)$.
The proof was produced with AI assistance on 10 November 2026 and reviewed only by AI reviewers; treat it as a
claim to be verified, not as an established result. What is and is not proved:

- **Proved.** Replacing a block $12$ by $21$ in any direct sum of patterns never increases the probability that a
  random permutation contains it. Consequently the pattern $2\,1\,4\,3\,\cdots$ is at least as hard as the identity:
  if $L_{21}(\sigma)$ is the largest $m$ with $\sigma \supseteq 21^{\oplus m}$, then $L_{21} \le_{st} \lfloor \mathrm{LIS}/2 \rfloor$
  and $c_{21} := \lim L_{21}(\sigma_n)/\sqrt n \le 1$.
- **Proved (W91, new on 10 November).** The gap is real and grows:
  $\mathbb{E}\,\mathrm{LIS}(\sigma_n) - 2\,\mathbb{E}L_{21}(\sigma_n) \ge c\,\sqrt n/\ln n$ for all large $n$. Hence the
  pattern $2\,1\,4\,3\cdots$ of length $k$ is, with high probability, *not* contained when
  $n \le (k^2/4)(1 + c'/\ln k)$, while the identity is contained just above $k^2/4$. So the identity is not the
  hardest pattern, and the $\varepsilon$ of the conjecture cannot be taken smaller than order $1/\ln k$. Also proved:
  one adjacent transposition at a typical position of the identity costs a positive constant in expected length.
  The proof is elementary (a planted copy of 3416725, the Mecke formula, first-moment bounds); its deterministic
  lemmas are brute-forced by two independently written programs and it has had one independent reading. It has
  not been refereed.
- **Proved (W91, part 2).** $c_{21} < 1$. The mean $\mathbb{E}L_{21}$ is superadditive, so it converges to
  $c_{21}\sqrt n$ at rate $O(\sqrt{\sqrt n \ln n})$ (the classical argument of Alexander for longest common
  subsequences: cut an optimal copy in two, plus Talagrand's inequality). A deficit of order $\sqrt n/\ln n$ is far
  larger than that error, so it is a deficit of the constant. Hence the statement in bold above, for every fixed
  $\varepsilon < c_{21}^{-2} - 1$. The proof gives no usable value for $1 - c_{21}$.
- **Numerical, not proved.** $\mathbb{E}\lfloor \mathrm{LIS}/2\rfloor - \mathbb{E}L_{21} = (0.00113 \pm 0.00002)\sqrt n$ for
  $n = 10^3,\dots,10^8$ (1.29 million paired samples, two independent programs), i.e. $c_{21} \approx 0.99887 < 1$.
  If so, a random permutation needs length about $1.0023\,k^2/4$ to contain $2\,1\,4\,3\,\cdots$, and Alon's
  conjecture fails for $\varepsilon < 0.0023$. Larger decreasing layers show larger gaps (about $1.4\%$ for layers of
  size 12).
- **For referees.** Start with the self-contained note
  [output/pdf/layered-refutation.pdf](output/pdf/layered-refutation.pdf) (16 pages: the full chain from the
  block-flip theorem to $c_{21} < 1$, with a record of what has been machine-checked).
- **Open.** (i) Independent verification of the two W91 proofs by a specialist. (ii) An effective bound: a
  deficit of order $\sqrt n$ with an explicit constant, reduced to one local estimate on the first steps of optimal
  copies ([W91 §7](experiments/w91-strict-deficit/proof.md)). (iii) The true threshold constant, and whether a
  random permutation of length $Ck^2$ is a $k$-superpattern for some absolute $C$ (published: $k^2\log\log k$;
  announced in the Chen–Wang preprint: $32k^2$, which is consistent with the claim above).

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
| $c_{21} < 1$ | A uniform permutation of length $(1+\varepsilon)k^2/4$ w.h.p. does not contain $2\,1\,4\,3\cdots$, for small fixed $\varepsilon$ (contradicts Alon's conjecture as stated) | Proof from the strict deficit and a rate-of-convergence lemma; two AI reviews; cutting inequality tested on 3,300 samples; **not checked by a human** | [W91, part 2](experiments/w91-strict-deficit/proof-c21.md) |
| Strict deficit | $\mathbb{E}\,\mathrm{LIS} - 2\,\mathbb{E}L_{21} \ge c\sqrt n/\ln n$; $2\,1\,4\,3\cdots$ not contained for $n \le (k^2/4)(1+c'/\ln k)$; one transposition costs a constant on average | Proof; gadget lemmas brute-forced (7,756 and 47,428 random plantings, two programs); independent reading; not refereed | [W91](experiments/w91-strict-deficit/) |

The block-flip inequality is, after reversing permutations, the size-2 transversal case of the skew shape
conjecture, proved by Jelínek (2008 thesis) and independently by
[Burstein–Pantone](https://arxiv.org/abs/1402.3842); see
[Jelínek–Karpilovskij](https://arxiv.org/abs/2002.12308), Theorem 2.5. No novelty is claimed for it. What appears to be new is its
asymptotic consequence for random permutations, its strict form (W91) and its bearing on Alon's conjecture; no
prior statement was found in the searches recorded in [memory/priority-check.md](memory/priority-check.md), and a
specialist has not yet been asked. Exact scopes, quantifiers and
withdrawn claims are in [memory/RESULTS.md](memory/RESULTS.md).

## Layout

- `experiments/wN-*/` — one folder per workstream: tools, raw outputs, `log.md` (chronology, dead ends), `proof.md`.
  Index: [experiments/README.md](experiments/README.md).
- `output/paper/` — the notes paper (Markdown → pandoc → xelatex): `superpatterns-notes.md`, and the standalone
  note `repeated-21-frontier.md`. Build with `make -C output/paper pdf`; `make -C output/paper check` must print `0`.
- `formal-verification/lean/` — Lean 4 / Mathlib: pattern containment, a verified superpattern checker with the
  $k = 7, 8$ certificates, the finite counting theorem A with its numeric certificate, finite moment inequalities,
  block splitting and Erdős–Szekeres, and (`BlockFlip.lean`) machine-checked small instances of the block-flip
  theorem: exact counts over $S_n$ for $n \le 9$ and the inequality for all $\alpha, \beta$ of size $\le 2$, $n \le 8$.
  The general block-flip theorem and everything probabilistic are not formalized; `BLOCKFLIP-PLAN.md` estimates
  what a formalization of the combinatorial core would take.
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
sh ../w91-strict-deficit/run_checks.sh          # gadget lemmas of the strict-deficit theorem (about 3 minutes)
cd ../../formal-verification/lean && lake exe cache get && lake build
```

## AI assistance disclosure

This research was developed by **Adam Ever-Hadani** with agentic AI tools (ChatGPT Codex, Claude Code, and a
multi-agent harness used in September 2026). The September multi-agent output is the part that was withdrawn; the
audit and the W90 results were produced with Claude Code and re-derived or recomputed as described in
`memory/SESSION-STATE.md`. The author takes responsibility for the mathematical claims.

## License

Code and Lean formalizations: MIT. Notes and papers: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
