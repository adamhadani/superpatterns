#!/bin/bash
# structured patterns: run_struct.sh tag k samples ns W  -> patterns: id, dec, layered (21)^{k/2}, dechalf, tilted (if k is a square)
cd "$(dirname "$0")"
tag=$1; k=$2; S=$3; ns=$4; W=$5
ARGS=$(python3 -c "
from pats import *
k=$k; out=['id=%s'%s(ident(k)),'dec=%s'%s(dec(k))]
if k%2==0: out.append('lay=%s'%s(layered(k))); out.append('dechalf=%s'%s(dechalf(k)))
r=int(round(k**0.5))
if r*r==k: out.append('tilt=%s'%s(tilted(r)))
out.append('r0=%s'%s(randpats(k,1)[0][1]))
print(' '.join(out))")
W=$W exec python3 sweep.py $tag $k $S $ns $ARGS
