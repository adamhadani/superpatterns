#!/usr/bin/env python3
"""Outward-rounded certificate for the corrected C-prime asymptotic bound.

Python standard library only. All proof inequalities use Decimal intervals.
Binary floats merely propose brackets, which are verified with intervals before
use. Decimal exp/ln are correctly rounded to nearest; one adjacent Decimal in
each direction encloses the exact value. See proof.md for the analytic tails,
monotonicity, and global strong-concavity bound (no sampled supremum).

Usage: python3 certify_cprime.py [--panels 8192] [--precision 50]
"""
import argparse
from decimal import Context, Decimal, ROUND_CEILING, ROUND_FLOOR
import json
import math


class Interval:
    precision = 50

    def __init__(self, lo, hi=None):
        self.lo = Decimal(lo)
        self.hi = Decimal(lo if hi is None else hi)
        assert self.lo <= self.hi

    @classmethod
    def cast(cls, x):
        return x if isinstance(x, cls) else cls(x)

    @classmethod
    def context(cls, rounding):
        return Context(prec=cls.precision, rounding=rounding)

    def __add__(self, other):
        b = self.cast(other)
        return Interval(self.context(ROUND_FLOOR).add(self.lo, b.lo),
                        self.context(ROUND_CEILING).add(self.hi, b.hi))

    __radd__ = __add__

    def __neg__(self):
        return Interval(self.hi.copy_negate(), self.lo.copy_negate())

    def __sub__(self, other):
        return self + -self.cast(other)

    def __rsub__(self, other):
        return self.cast(other) + -self

    def __mul__(self, other):
        b = self.cast(other)
        ends = [(a, c) for a in (self.lo, self.hi) for c in (b.lo, b.hi)]
        return Interval(min(self.context(ROUND_FLOOR).multiply(a, c) for a, c in ends),
                        max(self.context(ROUND_CEILING).multiply(a, c) for a, c in ends))

    __rmul__ = __mul__

    def __truediv__(self, other):
        b = self.cast(other)
        assert not b.lo <= 0 <= b.hi
        inv = Interval(self.context(ROUND_FLOOR).divide(Decimal(1), b.hi),
                       self.context(ROUND_CEILING).divide(Decimal(1), b.lo))
        return self * inv

    def __rtruediv__(self, other):
        return self.cast(other) / self

    def exp(self):
        ctx = Context(prec=self.precision)
        return Interval(ctx.next_minus(ctx.exp(self.lo)), ctx.next_plus(ctx.exp(self.hi)))

    def log(self):
        assert self.lo > 0
        ctx = Context(prec=self.precision)
        return Interval(ctx.next_minus(ctx.ln(self.lo)), ctx.next_plus(ctx.ln(self.hi)))

    def square_upper(self):
        ctx = self.context(ROUND_CEILING)
        a = max(self.lo.copy_abs(), self.hi.copy_abs())
        return Interval(0, ctx.multiply(a, a))

    def strings(self):
        return [str(self.lo), str(self.hi)]


I = Interval
LAM, TAU, BETA, RATE, CMIN = map(I, ["1.0073", "0.96813", "0.53692", "0.00783", "0.4805"])


def kl(u, p):
    return u * (u / p).log() + (1 - u) * ((1 - u) / (1 - p)).log()


def quantile(t):
    """Enclose u(t)>p(t) solving t D(u||p(t))=RATE."""
    tf = float(t.lo)
    pf = -math.expm1(-float(TAU.lo) / tf)
    lo, hi = pf, 1.0
    for _ in range(45):
        mid = (lo + hi) / 2
        value = tf * (mid * math.log(mid / pf)
                      + (1 - mid) * math.log((1 - mid) / (1 - pf)))
        if value < float(RATE.lo):
            lo = mid
        else:
            hi = mid
    p = 1 - (-TAU / t).exp()
    # Floats are suggestions only. Increase the bracket until both signs have
    # been proved for the entire interval t, including its endpoint roundoff.
    for extra in (1e-11, 1e-10, 1e-9, 1e-8):
        left, right = I(format(lo - extra, ".14f")), I(format(hi + extra, ".14f"))
        if left.lo <= p.hi or right.hi >= 1:
            continue
        if (t * kl(left, p) - RATE).hi < 0 < (t * kl(right, p) - RATE).lo:
            return Interval(left.lo, right.hi)
    raise ArithmeticError("Could not certify quantile bracket")


def certify(panels):
    theta = TAU * I(2).exp() / LAM
    p_beta = 1 - (-TAU / BETA).exp()
    # c(t)=t*u(t) increases; the finite-width proof also needs its large-width
    # mean bound at t=1 to exceed CMIN.
    assert (CMIN / BETA).lo > p_beta.hi
    assert (BETA * kl(CMIN / BETA, p_beta) - RATE).hi < 0
    assert (1 - (-3 * TAU / 4).exp() - CMIN).lo > 0
    assert (BETA * (-p_beta.log()) - RATE).lo > 0
    assert CMIN.lo > Decimal("0.125")

    def tail(t):
        v = theta * t
        return (1 + v) * (-v).exp()

    end = I(4)
    previous_t = BETA
    previous_tail = tail(previous_t)
    p_below = 1 - previous_tail
    previous_u = quantile(previous_t)
    integral = I(0)
    for j in range(1, panels + 1):
        t = BETA + (end - BETA) * j / panels
        next_tail = tail(t)
        next_u = quantile(t)
        mass = previous_tail - next_tail
        assert mass.lo >= 0
        # u(t) decreases, so exact Gamma(2) masses give Darboux bounds.
        integral += mass * Interval(next_u.lo, previous_u.hi)
        previous_t, previous_tail, previous_u = t, next_tail, next_u
    integral += Interval(0, previous_tail.hi)  # 0 <= u <= 1 on [4,infinity)

    # F''(s) <= -CMIN+1/8 for all real s. A tangent parabola bounds
    # the GLOBAL maximum, including the unbounded integration domain.
    s = I("0.1005")
    z = p_below + integral * s.exp()
    f = -CMIN * s * s / 2 + z.log() / 2
    derivative = -CMIN * s + integral * s.exp() / (2 * z)
    max_f_upper = f + derivative.square_upper() / (2 * (CMIN - I("0.125")))
    prefactor = TAU - 1 - TAU.log() + LAM.log()
    good = prefactor + max_f_upper
    bad = prefactor - RATE
    width_tail = prefactor - TAU / 4
    assert max(good.hi, bad.hi, width_tail.hi) < Decimal("-0.00001")
    return {
        "status": "PASS: all three rate upper bounds < -0.00001",
        "arithmetic": "outward Decimal intervals; correctly rounded exp/ln expanded by one neighbor",
        "precision": I.precision, "panels": panels,
        "lambda": str(LAM.lo), "tau": str(TAU.lo), "beta": str(BETA.lo),
        "R": str(RATE.lo), "c_lower": str(CMIN.lo),
        "theta": theta.strings(), "P_below": p_below.strings(),
        "integral": integral.strings(), "prefactor": prefactor.strings(),
        "good_rate_upper": str(good.hi), "bad_rate_upper": str(bad.hi),
        "width_tail_rate_upper": str(width_tail.hi),
        "scope": "asymptotic bound for all sufficiently large k; no explicit k0 or Lean certificate",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--panels", type=int, default=8192)
    parser.add_argument("--precision", type=int, default=50)
    args = parser.parse_args()
    if args.panels < 1 or args.precision < 30:
        parser.error("panels must be positive and precision at least 30")
    Interval.precision = args.precision
    print(json.dumps(certify(args.panels), indent=2))
