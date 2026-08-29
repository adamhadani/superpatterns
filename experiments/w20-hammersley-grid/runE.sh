for r in 4 8 16 32 64; do python3 bisect.py $r 1 -iid; done
for r in 4 8 16 32 64; do python3 bisect.py $r 2 -iid; done
for r in 8 16 32; do python3 bisect.py $r 3 -iid; done
