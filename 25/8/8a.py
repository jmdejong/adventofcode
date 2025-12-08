#!/usr/bin/python3
import sys
from math import *
boxes = [tuple(int(n) for n in line.split(",")) for line in open(sys.argv[1])]
# print(boxes)
possible_connections = []
for i, box in enumerate(boxes[:-1]):
	# print(i, box)
	for j, other in enumerate(boxes[i+1:]):
		possible_connections.append((dist(box, other), box, other))
circuits = {box: {box} for box in boxes}
possible_connections.sort(reverse=True)
i=0
while i<int(sys.argv[2]):
	# print(set(frozenset(circuit) for circuit in circuits.values()))
	s, a, b = possible_connections.pop()
	# print(s, a, b, circuits[a] == circuits[b])
	i += 1
	if circuits[a] == circuits[b]:
		continue
	circuits[a] |= circuits[b]
	for box in circuits[b]:
		circuits[box] = circuits[a]

all_circuits = set(frozenset(circuit) for circuit in circuits.values())
# print(all_circuits)
lengths = [len(circuit) for circuit in all_circuits]
lengths.sort(reverse=True)
print(lengths)
print(lengths[0] * lengths[1] * lengths[2])

def dist(a, b):
	return sqrt(sum((aa-bb)**2 for aa, bb in zip(a, b)))
