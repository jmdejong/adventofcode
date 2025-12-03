#!/usr/bin/python3
import sys

keys = []
locks = []
for kl in open(sys.argv[1]).read().split("\n\n"):
	# print(kl)
	h = [line.count("#")-1 for line in zip(*kl.splitlines())]
	if kl[0] == "#":
		keys.append(h)
	else:
		locks.append(h)
print(keys)
print(locks)

matches = 0
for key in keys:
	for lock in locks:
		for l in zip(key, lock):
			if sum(l) > 5:
				break
		else:
			matches += 1
print(matches)
