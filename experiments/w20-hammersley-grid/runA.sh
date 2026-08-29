for h in 8 16 32 64 128 256; do python3 bisect.py 2 $h; done
for h in 8 16 32 64; do python3 bisect.py 3 $h; done
for h in 8 16 32; do python3 bisect.py 4 $h; done
