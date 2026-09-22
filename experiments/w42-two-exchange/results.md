# W42 results: removing two-point exchanges has a target-dependent cost

**Exact outcome:** selection preserves containment and removes overlaps
k−1 and k−2, but its first moment is not pattern-independent. The smallest
census cell studied, k=3,n=6, already gives totals 594–598 over 720 hosts,
against the common ordinary-canonical total 672. All six targets have the
same containment count 588, so the difference is introduced by selection.
See [proof and exact formulas](proof.md).

[The census](exact-census.json) enumerates every host at seven (k,n) cells,
through n=8. It stores, separately for every target, containment counts,
first and second moments of both selectors, and maximum retained count.
[The generated summary](summary.md) gives pattern-averaged moments and
R_d=E[(Yπ^(d))²]/(E Yπ^(d))², averaging jointly over host and target.
R_2 is smaller than R_1 in all seven tested cells; this is finite evidence
for reducing clustering, not a theorem that the ratio improves generally.
The cells do not test the k→∞ quadratic regime of Alon's conjecture.

Independent replacement-neighbourhood enumeration agrees on 93,416 local
decisions across 2,684 host/target-length cases: every host of lengths 3–6
with 2≤k≤min(4,n), and 80 seeded larger cases. A separate
aggregate recount reproduces the six-target counterexample and its second
moments exactly. See [verification.txt](verification.txt) and
[census-verification.txt](census-verification.txt).

Reproduce from the repository root:

```sh
python3 experiments/w42-two-exchange/selection.py
python3 experiments/w42-two-exchange/analyze.py
python3 experiments/w42-two-exchange/verify.py
python3 experiments/w42-two-exchange/verify_census.py
```

The exact first moment now has a forbidden-pair kernel representation
(Proposition 2). The useful next step is to bound that cost for adversarial
targets at n=Ck², starting with repeated small patterns and the identity as
a control. Further small-host enumeration alone will not resolve the new
dependence. No random containment bound is claimed from these computations.
