#!/usr/bin/python3
import sys
r = []
for line in open(sys.argv[1]):
	for rang in line.strip().split(","):
		ran = rang.split("-")
		[lo, hi] = [int(v) for v in ran]
		r.append((lo, hi))
r.sort(key=lambda v: v[0])
hp = 0
for lo, hi in r:
	if lo <= hp:
		print("   ooooo")
	print(f"{lo}-{hi}")
	hp = hi
