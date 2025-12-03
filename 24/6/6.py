#!/usr/bin/python3
import sys

OBSTACLE = "#"
EMPTY = 0

EXIT = "EXIT"
LOOP = "LOOP"

field = {}
w = -1
h = -1
start = None


for y, line_raw in enumerate(open("input.in")):
	line = line_raw.strip()
	if line == "":
		break
	h += 1
	w = len(line)
	for x, char in enumerate(line):
		pos = (x, y)
		if char == "#":
			field[pos] = OBSTACLE
		elif char == ".":
			field[pos] = EMPTY
		elif char == "^":
			field[pos] = EMPTY
			start = pos

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def is_visited(tile):
	return isinstance(tile, int) and tile > 0

def draw(field):
	for y in range(h):
		for x in range(w):
			v = field[(x, y)]
			if v == OBSTACLE:
				sys.stdout.write("#")
			elif v == EMPTY:
				sys.stdout.write(".")
			elif is_visited:
				sys.stdout.write(hex(v)[-1])
			else:
				sys.stdout.write("?")
		sys.stdout.write("\n")
	sys.stdout.flush()

def walk(field, guard, direction):
	while True:
		d = directions[direction]
		dk = 1 << direction
		if field[guard] & dk:
			return LOOP
		field[guard] |= dk
		nex = (guard[0] + d[0], guard[1] + d[1])
		if nex not in field:
			return EXIT
		elif field[nex] == OBSTACLE:
			direction = (direction + 1) % 4
		else:
			guard = nex
first = field.copy()
print(walk(first, start, 0))
draw(first)
visited = [pos for pos, v in first.items() if is_visited(v)]
print(visited)
print(len(visited))


looping = 0
for tile in visited:
	if tile == start:
		continue
	attempt = field.copy()
	attempt[tile] = OBSTACLE
	result = walk(attempt, start, 0)
	# draw(attempt)
	# print(result)
	if result == LOOP:
		looping += 1
print("looping", looping)
