#!/usr/bin/env python3
"""Host bootstrap preserves numerator/denominator and overlap covariance."""
from pathlib import Path
import csv
import json
import math
import numpy as np

HERE = Path(__file__).resolve().parent
OUT = HERE / "out" / "review-20260910"


def interval(values):
    finite = np.asarray(values)[np.isfinite(values)]
    if len(finite) < len(values) * .99:
        return None
    return [float(x) for x in np.quantile(finite, [.025, .975])]


def wilson(hits, n):
    z = 1.959963984540054
    p = hits / n
    center = (p + z*z/(2*n)) / (1+z*z/n)
    half = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n)) / (1+z*z/n)
    return [max(0, center-half), min(1, center+half)]


def analyze(raw, meta):
    data = np.genfromtxt(raw, delimiter=",", names=True)
    k, hosts = meta["k"], meta["hosts"]
    assert data.shape == (hosts,)
    assert np.all(sum(data[f"overlap_{j}"] for j in range(k+1)) == data["sum_y2"])
    assert np.all(data[f"overlap_{k}"] == data["sum_y"])
    assert np.all(data[f"overlap_{k-1}"] == 0)
    factorial = math.factorial(k)
    a, b = data["sum_y"].mean(), data["sum_y2"].mean()
    ratio, off = factorial*b/a**2, factorial*(b-a)/a**2
    influence = factorial/a**2*((data["sum_y2"]-b) - 2*b/a*(data["sum_y"]-a))
    delta_se = float(influence.std(ddof=1)/math.sqrt(hosts))
    rng = np.random.default_rng(meta["seed"]+1)
    indices = rng.integers(0, hosts, (2000, hosts))
    aa = data["sum_y"][indices].mean(axis=1)
    bb = data["sum_y2"][indices].mean(axis=1)
    with np.errstate(divide="ignore", invalid="ignore"):
        boot_r = factorial*bb/aa**2
        boot_d = factorial*(bb-aa)/aa**2
    result = dict(meta, EY=float(a/factorial), R=float(ratio), diagonal=float(factorial/a),
                  D=float(off), delta_se=delta_se, R_ci=interval(boot_r), D_ci=interval(boot_d),
                  containment=float(data["distinct"].mean()/factorial),
                  bootstrap_hosts=2000, overlap=[], targets=[])
    for j in range(k+1):
        series = data[f"overlap_{j}"]
        boot = factorial*series[indices].mean(axis=1)/aa**2
        result["overlap"].append(dict(j=j, term=float(factorial*series.mean()/a**2), ci=interval(boot)))
    for q, name in enumerate(("identity", "random", "two_strip_grid", "repeated_21")):
        y, yy = data[f"target{q}_y"], data[f"target{q}_y2"]
        ey, ey2 = y.mean(), yy.mean()
        by, by2 = y[indices].mean(axis=1), yy[indices].mean(axis=1)
        with np.errstate(divide="ignore", invalid="ignore"):
            br = by2/by**2
        hits = int(data[f"target{q}_hit"].sum())
        result["targets"].append(dict(name=name, EY=float(ey), hits=hits,
                                     containment=hits/hosts, containment_ci=wilson(hits,hosts),
                                     R=float(ey2/ey**2) if ey else None,
                                     R_ci=interval(br)))
    return result


def main():
    results = []
    for meta_file in sorted(OUT.glob("k*_n*.json"), key=lambda p: (json.loads(p.read_text())["k"],json.loads(p.read_text())["n"])):
        meta = json.loads(meta_file.read_text())
        results.append(analyze(meta_file.with_suffix(".csv"), meta))
    (OUT / "summary.json").write_text(json.dumps(results, indent=2, allow_nan=False)+"\n")
    lines = ["# W38 bounded diagnostic — 10 September 2026", "",
             "Every subset and canonical overlap is enumerated within each sampled host. "
             "Uncertainty is over hosts: paired 2000-resample bootstrap intervals preserve covariance. "
             "These are numerical confidence intervals, not rigorous probability bounds. "
             "The C column is the actual integer-host N/k²; rounding can merge requested grid points.", "",
             "| k | N | C | hosts | EY | R (95% interval) | diagonal | D (95% interval) | containment |",
             "|---|---|---|---|---|---|---|---|---|"]
    for r in results:
        def ci(value):
            return "undefined" if value is None else f"{value[0]:.2f}–{value[1]:.2f}"
        lines.append(f"| {r['k']} | {r['n']} | {r['actual_C']:.4f} | {r['hosts']} | {r['EY']:.5f} | "
                     f"{r['R']:.2f} ({ci(r['R_ci'])}) | {r['diagonal']:.2f} | {r['D']:.2f} ({ci(r['D_ci'])}) | {r['containment']:.4f} |")
    lines += ["", "Full overlap terms (including observed zeros) and the four fixed-target diagnostics "
              "are in `out/review-20260910/summary.json`. An observed zero is not an asymptotic zero; "
              "Overlap k−1 and geometrically impossible bins are exact zeros; other zero observations need uncertainty bounds. Fixed-target ratios with "
              "insufficient hits are reported without a bootstrap interval. Containment intervals "
              "use the Wilson formula, including zero-hit cases.", "",
              "Reproduce: `python3 run_diagnostic.py`, then run `analyze_diagnostic.py` with NumPy. "
              "The runner preserves existing host files. `verify_diagnostic.py` checks the enumeration "
              "against an independently written Python implementation on small hosts."]
    (HERE / "diagnostic-20260910.md").write_text("\n".join(lines)+"\n")
    print("\n".join(lines[:len(results)+6]))


if __name__ == "__main__":
    main()
