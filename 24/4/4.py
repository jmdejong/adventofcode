#!/usr/bin/python3
import sys
from itertools import *

inp = [line.strip() for line in sys.stdin if len(line.strip())]

# part 1

def flip(strings):
	return ["".join(column) for column in zip_longest(*strings, fillvalue=" ")]

def skew(strings):
	return [" "*i + string for i, string in enumerate(strings)]

transforms = [
	*inp,
	*flip(inp),
	*[s.strip() for s in flip(skew(inp))],
	*[s.strip() for s in flip(skew(reversed(inp)))],
]
transforms += ["".join(reversed(line)) for line in transforms]

print(sum(line.count("XMAS") for line in transforms))


# part 2

count=0
for y, line in list(enumerate(inp))[1:-1]:
	for x, char in list(enumerate(line))[1:-1]:
		if char != "A":
			continue
		d1 = "".join(sorted([inp[y-1][x-1], inp[y+1][x+1]]))
		d2 = "".join(sorted([inp[y-1][x+1], inp[y+1][x-1]]))
		if d1 == "MS" and d2 == "MS":
			count += 1

print(count)
