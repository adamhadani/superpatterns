# W31 — certified typical-target lookahead bound

For a uniform target independent of a uniform host of length ceil(Ck²),
containment holds with probability 1−o(1) for every C>.4649.

- [proof.md](proof.md): rule, fresh-search reduction, padding, and the
  nonanticipating Bellman model.
- [certification.md](certification.md): directed MPFR verification of all
  512 supersolution inequalities, with exact margin ε=1/64.
- `mpfr_certificate.tsv`: exact dyadic candidates, upper recurrences,
  margins and ratios. `mpfr_certificate.txt`: successful run status.
- `dp.py`, `dp_cert.py` and their tables: historical numerical computations.
  The latter's rounding multiplier was not an interval proof. Its ε=.02
  table now supplies candidates checked independently for ε=1/64.
- `validate2d.py`, `freeshape_lb.py`, `results.md`, `log.md`: earlier simulations
  and chronology. The optimum near .4623 remains an extrapolation.

The theorem is asymptotic with large finite-k constants; it is neither
simultaneous universality nor a general impossibility bound for embedding
algorithms. Reproduce the certificate with the commands in certification.md.
