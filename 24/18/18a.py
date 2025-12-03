#!/usr/bin/python3
import sys
from collections import deque

WALL = "#"

f = open(sys.argv[1])
[size, num] = [int(n) for n in f.readline().strip().split()]
falling = []
for line in f:
	[x, y] = [int(n) for n in line.strip().split(",")]
	falling.append((x, y))
print(falling)
grid = {pos: WALL for pos in falling[:num]}
# print(len(grid.values()))
for y in range(size+1):
	print("".join("#" if grid.get((x, y)) == WALL else "." for x in range(size+1)))
visited = set()
fringe = deque([(0, (0,0))])
while len(fringe):
	# print(fringe)
	cost, pos = fringe.popleft()
	# print(cost, pos, fringe)
	if pos in visited:
		continue
	visited.add(pos)
	if pos == (size,size):
		print(cost)
		break
	x, y = pos
	for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
		nx = x + dx
		ny = y + dy
		n = (nx, ny)
		if nx < 0 or ny < 0 or nx > size or ny > size or grid.get(n) == WALL:
			continue
		fringe.append((cost+1, n))
else:
	print("no path")
# falling = [(int(x), int(y)) for line in f for x,
