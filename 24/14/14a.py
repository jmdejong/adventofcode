#!/usr/bin/python3
import sys
import re
f = open(sys.argv[1])
[w, h] = [int(i) for i in f.readline().strip().split()]
quadrants = [0, 0, 0, 0]
for line in f:
	[px, py, vx, vy] = [int(i) for i in re.findall("[-0-9]+", line)]
	ex = (px + vx * 100) % w
	ey = (py + vy * 100) % h
	if ex == w // 2 or ey == h // 2:
		continue
	quadrants[(ex > w//2) + 2*(ey > h//2)] += 1

r = 1
for n in quadrants:
	r*=n
print(quadrants)
print(r)
