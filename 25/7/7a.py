#!/usr/bin/python3
import sys
beams = set()
splits = 0
for line in open(sys.argv[1]):
	for i, c in enumerate(line):
		if c == "S":
			beams.add(i)
		if c == "^" and i in beams:
			beams.remove(i)
			beams.add(i+1)
			beams.add(i-1)
			splits += 1
print(splits)
