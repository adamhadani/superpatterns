# W32 — information outside the current gap (2026-08-29)

Question: can a sequential embedding rule for a uniformly random π ∈ S_k get below the in-gap cap ≈ 0.4623·k²
(W31 Thm 4.1) by using information outside the current gap — the other gaps' half-strips, neighbouring strips,
other processing orders, the whole of π?  Answer (proof.md): no.

* proof.md — Theorem 2.1 (PROVED): every rule that places one position at a time inside the gap of its value,
  choosing from a region where the process is conditionally Poisson (the fresh-search lemma's hypothesis), has
  E[consumption] ≥ V_k/(Ck) whatever it looks at, whatever partition it uses, however far it looks ahead;
  hence no threshold below inf_n V_n/n² ≈ 0.4623.  Theorem 2.2: knowing π in advance changes the cap by
  4·10^{−5} (random binary search tree recursion).  Obs. 3.1 + numerics: two-sided scans and lanes give no gain.
  §4: staleness — out-of-gap information needs lookahead Θ(k).
* results.md — all numbers; log.md — chronology and dead ends.
* Code (python, venv ../w12-c21/.venv; potentials from ../w31-lookahead/dp_V.txt):
  - single_strip.py k m C runs seed — one-sided in-gap rule on m strips (m = 1: single strip), true clock, records
    the staleness statistics (stale_k*_m*_C*.txt).  Outputs: runs_m1.out, runs_m.out.
  - diag.py — revisit-advance distribution by time (k = 1024).
  - twosided.py k m C runs seed [eps] [one] — two-sided scan (or one-sided with "one").  two_c.out, two_k1024.out, one_k1024.out.
  - lanes.py k m r C runs seed — r two-sided lanes.  lanes_a.out, lanes_b.out, lanes_k1024_r4.out.
  - zdiag.py — score-change statistics of the two candidates (two-sided, k = 512).
  - bst.py nexact nquant K — anticipating Bellman value E V(T) over random BSTs.  bst.out.
  Reproduce e.g.: `../w12-c21/.venv/bin/python single_strip.py 2000 1 0.6 10 7`.
