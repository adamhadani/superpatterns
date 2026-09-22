# W38 — current results, 10 September 2026

The bounded follow-up is complete. [The diagnostic table](diagnostic-20260910.md)
replaces the previous unfilled canonical table. The underlying per-host data,
all overlap terms and four fixed-target checks are saved in
`out/review-20260910/summary.json` and the adjacent CSV files. The raw older
experiments remain in `out/`; their earlier interpretation is preserved in
`historical-results.md` and is superseded here.

## Main conclusion

At actual C=N/k²=1/4, the total canonical second-moment ratio is approximately
20.2,20.3,20.3 for k=6,8,10. Its off-diagonal part D, however, increases:

| k | sampled hosts | diagonal 1/μ_can | D | host-bootstrap 95% interval |
|---|---|---|---|---|
| 6 | 1000 | 19.22 | 0.98 | 0.89–1.08 |
| 8 | 400 | 16.52 | 3.79 | 3.53–4.07 |
| 10 | 64 | 13.40 | 6.94 | 6.25–7.71 |

Thus a flat total hides a decreasing diagonal and increasing off-diagonal
mass. Boundedness is unresolved. The largest off-diagonal term in each of
these runs is overlap k−2: 0.836,2.061,2.888, respectively. This gives a
concrete analytic target. The remaining mass is substantial; controlling
k−2 alone will not establish a full second-moment theorem.

The four fixed targets (identity, a seeded random target, a two-strip grid,
and repeated 21) have overlapping uncertainty intervals. At k=10 there are
only 4–7 containment hits per target. These data cannot establish pattern
uniformity or order the asymptotic difficulty of the families.

## What was checked

- Every k-subset and every ordered pair of canonical copies of the same
  pattern is counted within each host. All overlap bins are retained.
- Assertions check canonical existence iff ordinary containment, overlap
  k−1 vanishing, the diagonal identity and the full second-moment sum.
- A separately written Python checker matched all per-host counts and
  moments on 35 small hosts. It uses a direct empty-window test rather
  than the C prefix-sum implementation.
- Confidence intervals resample hosts jointly (2000 bootstrap replicates),
  preserving covariance between numerator and denominator. They are
  statistical intervals, not mathematical enclosures. Wilson intervals
  cover zero-hit fixed-target containment cases; sparse ratio intervals
  may be undefined.
- Requested coefficients 0.22,0.25,0.27,0.30,0.40 were rounded down to
  integer N. The table reports actual N/k², including merged grid points.

## Historical claims withdrawn

The plain-copy rate e^{Θ(k)} and proposed critical coefficient 1/2 remain
heuristic predictions, supported only at small k. The older canonical
runs do not prove O(1) or e^{o(k)} growth. The W12 upper first-moment bound
cannot prove growth above its numerical crossing approximately 0.1925.
The j=1 check formerly left blank actually reports k!p₁=1.3447±0.0521 at
k=8,N=320; it does not validate the claimed π/4 limiting approximation.
The inequality at overlap k−1 is an exact structural fact; zeros at
geometrically impossible overlaps j<max(0,2k−N) are also forced. Other
observed zeros must not be read as exact zeros.

## Next decision

Stop the parameter sweep. Derive the overlap-(k−2) canonical pair structure
and its joint-emptiness contribution, with small-host enumeration as a
check. Reopen asymptotic second-moment claims only after there is both a
first-moment lower bound and control beyond a single overlap regime. The
superposition proposition in `proof.md` is now normalized by intensity on
the unit square; a positive averaged success probability does not become
typical-target high probability at the same coefficient by that argument.
