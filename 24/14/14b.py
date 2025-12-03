#!/usr/bin/python3
import sys
import re
import time
from math import sqrt


def sqr(x):
    return x**2

def stddev(l):
    return sqrt(sum(map(sqr,l))/len(l)-sqr(sum(l)/len(l)))

f = open(sys.argv[1])
[w, h] = [int(i) for i in f.readline().strip().split()]
robots = []
for line in f:
	[px, py, vx, vy] = [int(i) for i in re.findall("[-0-9]+", line)]
	robots.append(((px, py), (vx, vy)))

def draw(grid):
	for y in range(h):
		for x in range(w):
			n = grid.get((x, y))
			sys.stdout.write("." if n == None else str(n))
		print("")
	print("")


for seconds in range(10000):
	nr = {}
	areas = {}
	for p, v in robots:
		ex = (p[0] + v[0] * seconds) % w
		ey = (p[1] + v[1] * seconds) % h
		e = (ex, ey)
		nr[e] = nr.setdefault(e, 0) + 1
		a = (ex // 10, ey // 10)
		areas[a] = areas.setdefault(a, 0) + 1
	d = stddev(list(areas.values()))
	if d > 8:
		print(seconds, d)
		draw(nr)


