#!/usr/bin/python3
import sys

n = 0
v = 50
for line in open(sys.argv[1]):
	line = line.strip()
	dd = (-1 if line[0] == "L" else 1)
	vv = int(line[1:])
	n += vv // 100
	vv %= 100
	for i in range(vv):
		v = (v + dd) % 100
		if v == 0:
			n += 1

print(n)
