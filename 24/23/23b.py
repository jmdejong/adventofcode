#!/usr/bin/python3
import sys
computers = {}
for line in open(sys.argv[1]):
	c1, c2 = [c.strip() for c in line.split("-")]
	computers.setdefault(c1, set()).add(c2)
	computers.setdefault(c2, set()).add(c1)


def all_connected(group, candidates):
	best = group
	while candidates:
		candidate = next(iter(candidates))
		candidates.remove(candidate)
		g = all_connected(group.union([candidate]), candidates.intersection(computers[candidate]))
		if len(g) > len(best):
			best = g
	return best

best = all_connected(frozenset(), set(computers.keys()))
print(",".join(sorted(best)))
