#!/usr/bin/python3
import sys

# sample out: 9021
EMPTY = "."
BOX = "O"
BOXLEFT = "["
BOXRIGHT = "]"
WALL = "#"
gridinp, _sep, movementsinp = open(sys.argv[1]).read().partition("\n\n")
robot = (0, 0)
grid = {}
w = 0
h = 0
for y, line in enumerate(gridinp.splitlines()):
	w = len(line) * 2
	h += 1
	for x_raw, char in enumerate(line):
		x = x_raw * 2
		if char == "@":
			robot = (x, y)
			grid[(x, y)] = EMPTY
			grid[(x+1, y)] = EMPTY
		elif char == ".":
			grid[(x, y)] = EMPTY
			grid[(x+1, y)] = EMPTY
		elif char == "O":
			grid[(x, y)] = BOXLEFT
			grid[(x+1, y)] = BOXRIGHT
		elif char == "#":
			grid[(x, y)] = WALL
			grid[(x+1, y)] = WALL

print(w, h)
		# grid[(x, y)] = val
# grid = {(x, y): char for y, line in enumerate(gridinp.splitlines()) for x, char in enumerate(line.strip())}
# movements = [c for c in movementsinp if c in "<>v^"]
directions = {">": (1, 0), "<": (-1, 0), "^": (0, -1), "v": (0, 1)}

def movebox(pos, d):
	x, y = pos
	nx = x + d[0]
	ny = y + d[1]
	newpos = (nx, ny)
	if d[1] == 0:
		if grid[newpos] == BOXLEFT or grid[newpos] == BOXRIGHT:
			movebox(newpos, d)
		if grid[newpos] == EMPTY:
			grid[newpos] = grid[pos]
			grid[pos] = EMPTY
	else:
		if grid[pos] == BOXRIGHT:
			return movebox((x-1, y), d)
		if grid[pos] != BOXLEFT:
			raise Exception("movepos on "+grid[pos])
		if grid[(nx-1, ny)] == BOXLEFT:
			movebox((nx-1, ny), d)
		if grid[newpos] == BOXLEFT:
			movebox(newpos, d)
		if grid[(nx+1, ny)] == BOXLEFT:
			movebox((nx+1, ny), d)
		if grid[newpos] == EMPTY and grid[nx+1, ny] == EMPTY:
			grid[newpos] = BOXLEFT
			grid[(nx+1, ny)] = BOXRIGHT
			grid[(x, y)] = EMPTY
			grid[(x+1,y)] = EMPTY


	# newpos = (pos[0] + d[0], pos[1] + d[1])
	# newposright = (pos[0] + d[0] + 1, pos[1] + d[1])
	# if grid[(nx-1, ny

def canmovebox(pos, d):
	x, y = pos
	dx, dy = d
	if dy == 0:
		return True
	if grid[pos] == BOXRIGHT:
		x -= 1
	ny = y+dy
	if grid[(x, ny)] == WALL or grid[(x+1, ny)] == WALL:
		return False
	if grid[(x, ny)] in (BOXLEFT, BOXRIGHT) and not canmovebox((x, ny), d):
		return False
	if grid[(x+1, ny)] == BOXLEFT and not canmovebox((x+1, ny), d):
		return False
	return True


def draw():
	for y in range(h):
		for x in range(w):
			pos = (x, y)
			if pos == robot:
				sys.stdout.write("@")
			else:
				sys.stdout.write(grid[pos])
		print("")

for c in movementsinp:
	# draw()
	print("")
	d = directions.get(c)
	if d == None:
		continue
	n = (robot[0] + d[0], robot[1] + d[1])
	if grid[n] in (BOXLEFT, BOXRIGHT):
		if canmovebox(n, d):
			movebox(n, d)
		# movebox(n, d)
	# if grid[n] == BOXRIGHT:
		# movebox((n[0]-1, n[1]), d)
		# print("movebox", n, d)
	if grid[n] == EMPTY:
		robot = n
	# draw()
	# input()
		# print("move", n, d)

draw()

print(sum(x+100*y for (x, y), tile in grid.items() if tile == BOXLEFT))
