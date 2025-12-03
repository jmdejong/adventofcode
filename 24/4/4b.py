#!/usr/bin/python3
import sys

lines = [line.strip() for line in sys.stdin if len(line.strip())]

count=0
for y, line in list(enumerate(lines))[1:-1]:
	for x, char in list(enumerate(line))[1:-1]:
		if char != "A":
			continue
		d1 = "".join(sorted([lines[y-1][x-1], lines[y+1][x+1]]))
		d2 = "".join(sorted([lines[y-1][x+1], lines[y+1][x-1]]))
		if d1 == "MS" and d2 == "MS":
			count += 1

print(count)
