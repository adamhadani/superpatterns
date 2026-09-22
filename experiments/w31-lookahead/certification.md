# W31 directed supersolution certificate

10 September 2026. This replaces the rounding allowance in `dp_cert.py`.
For the fresh-window rule with exact margin ε=1/64 and h=512, the stored
potentials satisfy every supersolution inequality of proof.md, Lemma 3.2.
The last potential has V̄_512/512²≤0.46487433620981994<0.4649.
Together with the reduction and padding argument this proves typical-target
containment w.h.p. at every fixed coefficient C>0.4649. This is an asymptotic
statement with no useful explicit k₀; the collision bound has very large
constants for h=512. It is not a formal Lean proof or an optimality bound.

## Reproduction

From the repository root, with MPFR and GMP installed (the paths below are
Homebrew's Apple Silicon paths):

```sh
cc -O2 -std=c11 -ffp-contract=off -I/opt/homebrew/include experiments/w31-lookahead/certify_mpfr.c -L/opt/homebrew/lib -lmpfr -lgmp -lm -o /private/tmp/superpatterns-certify-mpfr
/private/tmp/superpatterns-certify-mpfr experiments/w31-lookahead/dp_cert_eps0.02.txt 512 > experiments/w31-lookahead/mpfr_certificate.tsv 2> experiments/w31-lookahead/mpfr_certificate.txt
```

The table named ε=0.02 supplies candidate numbers only: each parsed binary64
number is treated as an exact dyadic rational and printed in hexadecimal.
Every inequality is checked anew for ε=1/64. Exact complementary endpoints
ε and 1−ε justify reflecting A and B to halve the recurrence sum. No trust
is placed in the old quadrature or its claimed rounding margin.

## Enclosures

For A,B≥0 define φ(y)=A/y+B/(1−y) on the prescribed window, omitting zero
terms. Write a(s)=∫(s−φ(y))₊dy and w(s)=a′(s). The one-step expectation is
W(A,B)=∫₀∞exp(−a(s))ds. The sublevel interval is found from the quadratic
equation sy²−(s+A−B)y+A=0, then clipped to the window. Its integral is
evaluated by the analytic logarithm formula using interval endpoints.

Binary64 basic operations are widened outward by one adjacent representable
number. The program asserts binary radix, 53-bit precision and rounding to
nearest; compile without fast-math and with contraction disabled. MPFR at
128 bits computes transcendental endpoint bounds with directed rounding,
then converts them to binary64 in the same direction. Subtractive cancellation
is allowed to widen intervals; it is never compensated by assumed precision.

Near a double root, a naive interval discriminant was too wide. The final
checker evaluates its dyadic polynomial exactly at 256 MPFR bits. All nonzero
inputs s,A,B are asserted to lie in [1,2²⁴), so their common denominator
divides 2⁵². Their numerators have at most 76 bits; the sums and products in
(s+A−B)²−4sA fit comfortably within 256 bits. Square roots, root numerators,
and divisions are then rounded in both directions. This is an exactness
argument for the polynomial, not an assumption that high precision is enough.

Convexity of a gives the integration bounds. A midpoint tangent lies below
a, so its exponential integrates to an upper bound, using an upper bound
on the nonnegative tangent slope. A slightly enlarged symmetric interval
accounts for a rounded midpoint. The left rectangle gives another upper
bound; take the smaller. A chord joining upper endpoint enclosures lies
above a and gives a lower bound used only to choose refinement depth.
The tail at T is at most exp(−a(T))/w(T). Below an upper bound s₀ on min φ,
the integral is at most s₀. All sums and divisions are enclosed outward.
The tolerance controls runtime; acceptance depends on the final upper
recurrence lying below the exact candidate, never on the tolerance itself.

## Recorded checks

MPFR 4.2.2: all 512 recurrences passed, using 4,035,984 area evaluations.
The last upper recurrence is 121845.56860063219, below the candidate
121864.01799138699 by a certified margin exceeding 18.449.
Sanity checks include W(0,0)=1 and 3≤W_upper(1,0)<3.001. The unrestricted
value W₀(1,0)=3 is exact; the margin rule has a slightly larger value.
The earlier independent floating quadrature agrees at the scale expected
from its discretization, but is not used to validate any proof inequality.
