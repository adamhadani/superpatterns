#!/bin/bash
# run_k.sh tag k samples ns W [npats]   -- identity + random patterns
cd "$(dirname "$0")"
tag=$1; k=$2; S=$3; ns=$4; W=$5; m=${6:-8}
ARGS=$(python3 -c "from pats import *; print('id=%s '%s(ident($k))+' '.join('%s=%s'%(n,s(p)) for n,p in randpats($k,$m)))")
W=$W exec python3 sweep.py $tag $k $S $ns $ARGS
