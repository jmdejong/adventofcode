#!/usr/bin/python3
import sys#!/usr/bin/python3
import sys
beams = {}
for line in open(sys.argv[1]):
	for i, c in enumerate(line):
		if c == "S":
			beams[i] = 1
		if c == "^" and i in beams:
			beams[i+1] = beams.get(i+1, 0) + beams[i]
			beams[i-1] = beams.get(i-1, 0) + beams[i]
			beams[i] = 0
print(sum(beams.values()))

