#!/usr/bin/python3
import sys
t = 0
for line in open(sys.argv[1]):
	for rang in line.strip().split(","):
		ran = rang.split("-")
		# print(
		[lo, hi] = [int(v) for v in ran]
		if len(ran[0]) != len(ran[1]):
			print(len(ran[0]), len(ran[1]))
			# print("jump")
			# print(lo, hi, hi - lo)
		t += hi - lo
print(t)
