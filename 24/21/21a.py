#!/usr/bin/python3
import sys

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

	def key(self, pos):
		return self.keys.get(pos)

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

	def press_keys(self, keys):
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

def complexity(path):
	l = float("inf")
	for path2 in robopad.press_keys(path):
		for path3 in robopad.press_keys(path2):
			# print(path3)
			if len(path3) < l:
				l = len(path3)
	return l

def best(paths):
	l3 = float("inf")
	b = None
	for path in paths:
		for path2 in robopad.press_keys(path):
			for path3 in robopad.press_keys(path2):
				# print(path3)
				if len(path3) < l3:
					l3 = len(path3)
					b = path
	return (b, l3)


codes = [line.strip() for line in open(sys.argv[1])]
assert len(codes) == 5
for code in codes:
	assert len(code) == 4
	assert code[3] == "A"
total = 0
for code in codes:
	path, l = best(doorpad.press_keys(code))
	total += l * int(code[:-1])
print(total)




