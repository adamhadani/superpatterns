for r in 2 4 8 16 32 64; do python3 bisect.py $r 1; python3 bisect.py $r 2; done
for r in 4 8 16 32; do python3 bisect.py $r 3; done
for r in 4 8 16 32; do python3 bisect.py $r 4; done
for r in 5 6 8; do python3 bisect.py $r 6; done
