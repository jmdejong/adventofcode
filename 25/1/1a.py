#!/usr/bin/python3
import sys

n = 0
v = 50
for line in open(sys.argv[1]):
	line = line.strip()
	v += int(line[1:]) * (-1 if line[0] == "L" else 1)
	v %= 100
	if v == 0:
		n += 1
print(n)
