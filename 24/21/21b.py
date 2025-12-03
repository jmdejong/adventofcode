#!/usr/bin/python3
import sys
from functools import cache

DIRECTIONS = {
	"<": (-1,0),
	"v": (0,1),
	">": (1,0),
	"^": (0,-1)
}

class Keypad:

	def __init__(self, rows):
		self.rows = rows
		self.keys = {(x, y): key for y, row in enumerate(rows) for x, key in enumerate(row) if key.strip() != ""}
		self.positions = {key: pos for pos, key in self.keys.items()}

	def position(self, key):
		return self.positions.get(key)

	def is_valid_path(self, pos, steps):
		x, y = pos
		for step in steps:
			dx, dy = DIRECTIONS[step]
			x += dx
			y += dy
			if (x, y) not in self.keys:
				return False
		return True

	def paths_between(self, start, end):
		sx, sy = start
		ex, ey = end
		dx = ex - sx
		dy = ey - sy
		px = ">" * dx + "<" * -dx
		py = "v" * dy + "^" * -dy
		paths = [px + py, py + px]
		return set(path for path in paths if self.is_valid_path(start, path))

	def press_single(self, start, key):
		return [path + "A" for path in self.paths_between(start, self.position(key))]

	@cache
	def press_keys(self, start, path, depth):
		if depth == 0 or len(path) == 0:
			return len(path)
		key = path[0]
		keypos = self.position(key)
		apos = self.position("A")
		return min(self.press_keys(apos, p, depth-1) + self.press_keys(keypos, path[1:], depth) for p in self.press_single(start, key))


	def paths(self, keys):
		start = self.position("A")
		paths = [""]
		for key in keys:
			pos = self.position(key)
			step_paths = self.paths_between(start, pos)
			paths = set(path + step_path + "A" for path in paths for step_path in step_paths)
			start = pos
		return paths


doorpad = Keypad(["789", "456", "123", " 0A"])
robopad = Keypad([" ^A", "<v>"])



codes = [line.strip() for line in open(sys.argv[1])]
for code in codes:
	assert code[-1] == "A"
total = 0
btotal = 0
for code in codes:
	h = int(code[:-1])
	paths = doorpad.paths(code)
	r = min(robopad.press_keys(robopad.position("A"), p, 2) for p in paths)
	total += r * h
	rb = min(robopad.press_keys(robopad.position("A"), p, 25) for p in paths)
	btotal += rb * h
	print(code, r, rb)
print("")
print(total)
print(btotal)


