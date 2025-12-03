#!/usr/bin/python3
import sys
t = 0
for line in open(sys.argv[1]):
	for rang in line.strip().split(","):
		ran = rang.split("-")
		l = len(ran[0])
		if l%2 != 0:
			l += 1
		[lo, hi] = [int(v) for v in ran]
		print(ran)
		[hlo, hhi] = [int("0"+v[:(len(v)//2)]) for v in ran]
		# u = 10**l + 10**(l//2)
		print(rang, hlo, hhi)
		for i in range(hlo, hi + 1):
			v = int(str(i) + str(i))
			if v > hi:
				break
			if v >= lo:
				print(" ", v)
				t += v

print(t)
