#!/usr/bin/python3
import sys


ranges = []
for line in open(sys.argv[1]):
	for rang in line.strip().split(","):
		ran = rang.split("-")
		[lo, hi] = [int(v) for v in ran]
		ranges.append((lo, hi))
ranges.sort(key=lambda v: v[0])
# print(ranges)

top = ranges[-1][1]

# t = 0
invalids = set()
i = 1
while True:
	if int(str(i)*2) > top:
		break
	for repeats in range(2, 9999):
		v = int(str(i)*repeats)
		if v > top:
			break
		for lo, hi in ranges:
			if v >= lo and v <= hi:
				invalids.add(v)
				# t += v
				# print(v)
	i += 1

print(sum(invalids))
