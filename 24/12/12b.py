#!/usr/bin/python3
import sys

grid = {(x, y): char for y, line in enumerate(open(sys.argv[1])) for x, char in enumerate(line.strip())}
visited = {}
cost = 0
for pos in grid:
	if pos in visited:
		continue
	fringe = [pos]
	visited[pos] = True
	edges = set()
	surface = 0
	while len(fringe):
		p = fringe.pop()
		v = grid[p]
		surface += 1
		for d in [(0,-1), (1,0), (0,1), (-1,0)]:
			n = tuple(pp+dd for pp, dd in zip(p,d))
			if grid.get(n) != v:
				edges.add((p,d))
				continue
			if n in visited:
				continue
			visited[n] = True
			fringe.append(n)
	sides = [((x, y), (dx, dy)) for (x, y), (dx, dy) in edges if ((x + dy, y - dx), (dx, dy)) not in edges]
	cost += surface * len(sides)
	print(grid[pos], surface, len(sides), surface * len(sides))

print(cost)
