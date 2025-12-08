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
while True:
	s, a, b = possible_connections.pop()
	if circuits[a] == circuits[b]:
		continue
	circuits[a] |= circuits[b]
	if len(circuits[a]) == len(boxes):
		print(a[0], b[0])
		print(a[0] * b[0])
		break
	for box in circuits[b]:
		circuits[box] = circuits[a]

def dist(a, b):
	return sqrt(sum((aa-bb)**2 for aa, bb in zip(a, b)))
