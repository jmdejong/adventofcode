#!/usr/bin/env python3
import sys

chs = [int(line) for line in sys.stdin]
f = 0
frs = []
for c in chs:
    f += c
    frs.append(f)
final = f

seen = {}
for f in frs:
    if f%final in seen:
        print(f, f % final, seen[f%final], f // final, seen[f%final]//final)
        #break
    else:
        seen[f%final] = f

print(f)
    
