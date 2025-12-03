#!/usr/bin/python3
import sys

initials = [int(line.strip()) for line in open(sys.argv[1])]

scores = {}
for num in initials:
	last = num % 10
	seq = tuple()
	known = set()
	for i in range(2000):
		num = (num ^ (num * 64)) % 16777216
		num = (num ^ (num // 32)) % 16777216
		num = (num ^ (num * 2048)) % 16777216
		seq = (num%10 - last, *seq)[:4]
		last = num%10
		if len(seq) == 4 and seq not in known:
			scores[seq] = last + scores.get(seq, 0)
			known.add(seq)

print(max(scores.items(), key=lambda item: item[1]))
