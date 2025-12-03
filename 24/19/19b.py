#!/usr/bin/python3
import sys
from functools import cache



f = open(sys.argv[1])
towels = tuple(f.readline().strip().split(", "))
assert f.readline().strip() == ""


@cache
def arrange(pattern):
	if pattern == "":
		return 1
	ways = 0
	for towel in towels:
		if pattern.startswith(towel):
			ways += arrange(pattern[len(towel):])
	return ways

total = 0
for line_raw in f:
	pattern = line_raw.strip()
	ways = arrange(pattern)
	print(ways)
	total += ways
print("+")
print(total)
