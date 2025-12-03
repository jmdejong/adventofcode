#!/usr/bin/python3
import sys
EMPTY = "."
BOX = "O"
WALL = "#"
gridinp, _sep, movementsinp = open(sys.argv[1]).read().partition("\n\n")
robot = (0, 0)
grid = {}
for y, line in enumerate(gridinp.splitlines()):

	for x, char in enumerate(line):
		val = char
		if char == "@":
			robot = (x, y)
			val = EMPTY
		grid[(x, y)] = val
# grid = {(x, y): char for y, line in enumerate(gridinp.splitlines()) for x, char in enumerate(line.strip())}
# movements = [c for c in movementsinp if c in "<>v^"]
directions = {">": (1, 0), "<": (-1, 0), "^": (0, -1), "v": (0, 1)}
for c in movementsinp:
	d = directions.get(c)
	if d == None:
		continue
	n = (robot[0] + d[0], robot[1] + d[1])
	if grid[n] == EMPTY:
		robot = n
	elif grid[n] == WALL:
		pass
	elif grid[n] == BOX:
		f = n
		while grid[f] == BOX:
			f = (f[0] + d[0], f[1] + d[1])
		if grid[f] == EMPTY:
			grid[f] = BOX
			grid[n] = EMPTY
			robot = n

print(sum(x+100*y for (x, y), tile in grid.items() if tile == BOX))
